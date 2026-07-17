# coding=utf-8
"""LatheToolModel -- composes core tool-table columns with tool_lathe
extras and user-defined custom-field columns into one flat, editable table
(plan §6 Phase 3).

Core columns are the same letter-keyed data (T P X Z D I J Q R ...) served by
``qtpyvcp.plugins.db_tool_table.DBToolTable``; extras are ``tool_lathe``
attribute names; custom fields are keyed ``custom:<name>``. All three groups
are staged in one in-memory dict per tool and committed together by
:meth:`saveToolTable` -- one widget, one Save action, per the plan's single-
store rule. Every column (core, extras, custom) locks while a program is
running -- not just the ones LinuxCNC itself reads live: a custom/extras
value could still be referenced by a subroutine or some other mid-program
logic, so editing any of it while the machine is running is unsafe practice
regardless of whether LinuxCNC's own interpreter happens to consume that
particular column.
"""

from PySide6.QtCore import Qt, QModelIndex, Signal
from PySide6.QtGui import QStandardItemModel, QColor, QBrush

from qtpyvcp.utilities.logger import getLogger
from qtpyvcp.plugins import getPlugin
from qtpyvcp.actions import IN_DESIGNER
from qtpyvcp.actions.machine_actions import issue_mdi

LOG = getLogger(__name__)

CUSTOM_PREFIX = 'custom:'

# tool_lathe columns, in display order (plan §4 DDL) -- labels for the header
# and the column-visibility menu.
EXTRAS_LABELS = {
    'type': 'Type',
    'insert_shape': 'Insert Shape',
    'insert_size_mode': 'Size Mode',
    'insert_size': 'Insert Size',
    'insert_thickness': 'Insert Thk',
    'holder_style': 'Holder',
    'holder_hand': 'Hand',
    'holder_shank_width': 'Shank W',
    'holder_cut_width': 'Cut W',
    'holder_oal': 'Holder OAL',
    'groove_width': 'Groove W',
    'max_depth_of_cut': 'Max DOC',
    'drill_point_angle': 'Point Angle',
    'flute_length': 'Flute Len',
    'overall_length': 'Overall Len',
    'shaft_diameter': 'Shaft Dia',
    'chamfer_threads': 'Chamfer Thds',
    'thread_pitch_max': 'Max Pitch',
    'thread_angle': 'Thread Angle',
    'thread_tip_type': 'Tip Type',
    'surface_speed': 'Surface Speed',
    'feed_per_rev': 'Feed/Rev',
    'depth_of_cut': 'DOC',
    'notes': 'Notes',
}
EXTRAS_ORDER = list(EXTRAS_LABELS)  # dict preserves insertion order (py3.7+)

TEXT_EXTRAS = {'type', 'insert_shape', 'insert_size_mode', 'holder_style',
              'holder_hand', 'thread_tip_type', 'notes'}

# Extras columns that feed real machine-facing behavior somewhere -- the
# VTK insert display and/or the lathe conversational operations (core
# columns cover LinuxCNC itself and are always default-visible) -- are all
# shown by default, per Chris (2026-07-05): a user setting up a tool should
# see every parameter something actually consumes without having to know
# to unhide it first. Consumer mapping verified against the actual reads
# in pb_lathe_conv (lathe_insert_geometry/lathe_conv/dexel_simulation/
# tool_library/operations), not just docs/schema_v1/schema_v1_audit.md
# §1-2 -- the audit listed holder_hand as consumed, but in code the hand
# that geometry actually uses is the trailing letter of the holder_style
# ISO code (SCLCR vs SCLCL); the standalone column is written once at
# tool creation and never read back. The others excluded here are
# reference-only (nothing in LinuxCNC, VTK, or the ops layer reads them
# -- the same-named values in conversational dialogs are per-operation
# user inputs, not tool-table reads). thread_tip_type is likewise stored-
# but-never-read: build_thread_shape() accepts it but only echoes it into
# its dims metadata (which nothing reads back) -- the actual thread tip
# geometry is filleted from the tip *radius* (core D), not the type.
# chamfer_threads IS read, but only to draw a tap's lead-in taper in the
# VTK rendering (sane 2.5-thread default; no op math or g-code touches
# it) -- deliberately opted out per Chris: most tap makers don't even
# publish the value, so a default column would just invite guessing.
REFERENCE_ONLY_EXTRAS = ('holder_hand', 'thread_tip_type', 'chamfer_threads',
                         'surface_speed', 'feed_per_rev', 'depth_of_cut',
                         'notes')
DEFAULT_VISIBLE_EXTRAS = [c for c in EXTRAS_ORDER
                          if c not in REFERENCE_ONLY_EXTRAS]

# Custom-column display, by the field's own value_type (plan §5.7) -- text
# reads like the other text-ish columns (left), float/int/bool read like
# data rather than prose (right for float since that's the numeric-column
# convention everywhere else in this table; centered for int/bool since
# they're short, discrete values rather than magnitudes to compare).
CUSTOM_FIELD_ALIGNMENT = {
    'text': Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft,
    'float': Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight,
    'int': Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter,
    'bool': Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter,
}
# Single source of truth for float display precision, table-wide (core
# columns, extras, and custom float fields alike) -- named and centralized
# rather than a bare "4" repeated wherever a float gets formatted, so
# every float column stays uniform on purpose, not by coincidence.
FLOAT_DECIMALS = 4

# Strict, DB-enforced enums (CHECK constraints in migrations/001_initial.sql)
# -- these become non-editable combo pick-lists; the user literally cannot
# enter a value the database would reject.
TYPE_OPTIONS = ['turning', 'boring', 'grooving', 'parting', 'threading',
               'drill', 'tap', 'custom']
INSERT_SIZE_MODE_OPTIONS = ['IC', 'edge_length']
HOLDER_HAND_OPTIONS = ['R', 'L']
# Not DB-enforced, but a documented closed convention (schema_v1_audit.md §4:
# "D=0 remains for thread_tip_type='point' inserts and is valid data").
THREAD_TIP_TYPE_OPTIONS = ['point', 'flat', 'radius']

STRICT_ENUM_OPTIONS = {
    'type': TYPE_OPTIONS,
    'insert_size_mode': INSERT_SIZE_MODE_OPTIONS,
    'holder_hand': HOLDER_HAND_OPTIONS,
    'thread_tip_type': THREAD_TIP_TYPE_OPTIONS,
}

# insert_shape and holder_style are open vocabularies in practice -- real
# data mixes plain ISO letters (turning: C/D/V/W) with descriptive codes for
# other tool families (grooving: "GROOVE SQUARE"; threading: "THREAD ISO
# TRIPLE"; holder_style: "GROOVE EXTERNAL", full ISO holder codes like
# "SCLCR", ...). These get an *editable* combo -- not a strict pick-list --
# but which choices are actually offered is discriminated by the row's own
# `type` (and, for holder_style, by the row's already-chosen `insert_shape`)
# rather than dumping every value ever used for any tool into one list.
# Ported from pb_lathe_conv's Fusion-era tool library
# (lathe_conversational/tool_library_table.py:
# _tool_library_combo_options_for_column), which encoded the same
# discrimination for its own (differently-shaped) schema -- see
# LatheToolModel.insertShapeOptionsForType/holderStyleOptionsForRow.
OPEN_VOCAB_SEED_OPTIONS = {'insert_shape', 'holder_style'}

NO_INSERT_TYPES = {'drill', 'tap'}
GROOVING_TYPES = {'grooving', 'parting'}
THREADING_TYPES = {'threading'}

# turning/boring/custom insert shapes share one ISO-letter vocabulary.
GENERAL_INSERT_SHAPES = ['C', 'D', 'V', 'W', 'T', 'S', 'R']
GROOVING_INSERT_SHAPES = ['GROOVE SQUARE', 'GROOVE ROUND']
THREADING_INSERT_SHAPES = ['THREAD ISO TRIPLE', 'THREAD ISO DOUBLE']

GROOVING_HOLDER_STYLES = ['GROOVE EXTERNAL', 'GROOVE INTERNAL', 'GROOVE FACE']
THREADING_HOLDER_STYLES = ['THREAD STRAIGHT', 'THREAD FACE',
                           'THREAD INTERNAL', 'THREAD OFFSET']


MAX_COLUMNS = 200  # generous fixed capacity; mirrors the row model's
                   # existing fixed setRowCount(1000)/max-1000-tools limit


class LatheToolModel(QStandardItemModel):

    # Machine-flavor configuration, hoisted to class attributes so a
    # machine variant is a subclass overriding data, not a fork of the
    # logic (see widgets.mill_tool_table.MillToolModel). The module-level
    # constants above stay as the lathe values; these class attributes are
    # what the model methods (and LatheItemDelegate, via self._model)
    # actually consult.
    EXTRAS_LABELS = EXTRAS_LABELS            # column key -> header label, in display order
    TEXT_EXTRAS = TEXT_EXTRAS                # extras rendered/edited as free text
    BOOL_EXTRAS = frozenset()                # extras rendered/edited as True/False
    EXTRAS_DEFAULTS = {}                     # value shown when a tool has no extras row
    DEFAULT_VISIBLE_EXTRAS = DEFAULT_VISIBLE_EXTRAS
    STRICT_ENUM_OPTIONS = STRICT_ENUM_OPTIONS
    OPEN_VOCAB_SEED_OPTIONS = OPEN_VOCAB_SEED_OPTIONS
    EXTRAS_GROUP_LABEL = 'Lathe Extras'      # header-menu section title
    # Core columns forced to render AFTER extras/custom instead of in their
    # normal core position -- for the wide free-text Remark, so machine
    # extras sit between the numeric offsets and it. Empty by default (the
    # lathe keeps Remark in its ratified core position); the mill sets
    # ('R',) so ATC lands just before Remark. Membership only -- these stay
    # 'core' for grouping; only their column position moves.
    TRAILING_CORE_COLUMNS = ()

    dirtyChanged = Signal(bool)

    def __init__(self, parent=None):
        super(LatheToolModel, self).__init__(parent)
        self._dirty = False

        if IN_DESIGNER:
            self._initEmptyStub()
            return

        try:
            self.status = getPlugin('status')
            self.stat = self.status.stat
            self.tt = getPlugin('tooltable')

            required = ('columns', 'COLUMN_LABELS', 'getToolTable',
                       'saveToolTable', 'newTool', 'tool_table_changed')
            missing = [attr for attr in required if not hasattr(self.tt, attr)]
            if missing:
                # Something fundamentally incompatible -- not even the base
                # (mill-and-lathe-shared) tool-table interface every
                # 'tooltable' plugin is expected to implement. A plugin
                # merely lacking the *lathe-specific* DB extras (see
                # _db_backed below) is not this case -- that's a normal,
                # supported backend, not an error.
                raise TypeError(
                    "'tooltable' plugin (%s) doesn't implement the base "
                    "tool-table interface -- missing: %s"
                    % (type(self.tt).__name__, ', '.join(missing)))

            # True for qtpyvcp.plugins.db_tool_table:DBToolTable (this
            # project's schema v1 backend); False for the classic file-based
            # qtpyvcp.plugins.tool_table:ToolTable. Both are first-class,
            # supported backends for this one widget -- it adapts at runtime
            # to whichever 'tooltable' plugin the .ini/yaml config actually
            # wires up, rather than requiring a second copy of the .ui with
            # a different widget class promoted. (That was tried; Designer
            # bakes the promoted class into the .ui statically, so two
            # backends meant two .ui files that inevitably drift out of
            # sync on any unrelated edit -- a real, since-reverted mistake,
            # not a hypothetical one.)
            self._db_backed = hasattr(self.tt, 'getCustomFieldDefs')

            self.current_tool_color = QColor(Qt.darkGreen)
            self.current_tool_bg = None

            self._core_columns = list(self.tt.columns)
            self._core_labels = dict(self.tt.COLUMN_LABELS)
            if self._db_backed and self._pluginServesOurExtras():
                self._extras_columns = list(self.EXTRAS_LABELS)
                self._extras_labels = dict(self.EXTRAS_LABELS)
            else:
                self._extras_columns = []
                self._extras_labels = {}
            self._custom_columns = []
            self._custom_labels = {}
            self._custom_value_types = {}

            self.row_offset = 1
            self._interp_idle = True
            self._tool_table = {}

            if self._db_backed:
                self._refresh_custom_columns()

            # Restore whatever the user last had checked visible (schema
            # v2) -- core, extras, and custom columns alike -- so a widget
            # restart shows the same columns instead of always reverting
            # to the hardcoded default. No persisted preference yet (fresh
            # DB, or classic file-based backend, which has nowhere to
            # persist this at all) falls back to the default set.
            persisted = self.tt.getVisibleColumns() if self._db_backed else None
            self._visible_columns = (self._filterToKnownColumns(persisted) if persisted
                                     else self._default_visible_columns())
            # Fixed capacity, set once, before any view/proxy is attached --
            # never touched again (see MAX_COLUMNS and setVisibleColumns below
            # for why: calling setColumnCount() again later, after a proxy is
            # watching, raced its own columnsInserted signal against our
            # columnCount() override still reporting the pre-growth count).
            self.setColumnCount(MAX_COLUMNS)
            self.setRowCount(1000)

            self._load_full_table()

            self.status.tool_in_spindle.notify(self.refreshModel)
            self.status.interp_state.notify(self._onInterpStateChanged)
            self._reload_signals_suppressed = False
            self.tt.tool_table_changed.connect(lambda *_: self._load_full_table())
            if self._db_backed:
                self.tt.extras_changed.connect(self._onExtrasChanged)
                self.tt.fields_changed.connect(self._onFieldsChanged)
        except Exception:
            # A Python exception escaping this constructor would propagate
            # up through QUiLoader's C++ widget-tree building (this widget
            # gets built via .ui customwidget promotion) -- PySide6 segfaults
            # instead of raising cleanly there, rather than just failing this
            # one widget. Fail soft into an empty, read-only stub instead;
            # see LatheToolTable.__init__ for the matching self.tt is-None
            # guard.
            LOG.exception(
                "LatheToolModel: failed to initialize against the "
                "'tooltable' plugin -- falling back to an empty table "
                "instead of crashing. This means the plugin is missing even "
                "the base tool-table interface (columns/getToolTable/"
                "saveToolTable/...) -- a lathe-only DB backend is not "
                "required (both qtpyvcp.plugins.tool_table:ToolTable and "
                "qtpyvcp.plugins.db_tool_table:DBToolTable work), so check "
                "'tooltable' is wired to one of those two, not something "
                "else entirely.")
            self._initEmptyStub()

    def _initEmptyStub(self):
        self.status = None
        self.stat = None
        self.tt = None
        self._db_backed = False
        self._reload_signals_suppressed = False
        # Real-path defaults for LatheToolTable's currentToolColor/
        # currentToolBackground @Property getters, which read these
        # unconditionally. Missing here meant Qt Designer's startup widget-
        # database scan (grabs every registered custom widget's default
        # property values, on a freshly-constructed instance -- independent
        # of which .ui is even open) hit an AttributeError from inside a
        # C++-invoked property getter and segfaulted instead of raising.
        self.current_tool_color = QColor(Qt.darkGreen)
        self.current_tool_bg = None
        self._core_columns = ['T', 'P', 'X', 'Z', 'D', 'I', 'J', 'Q', 'R']
        self._extras_columns = []
        self._custom_columns = []
        self._visible_columns = list(self._core_columns)
        self._core_labels = {c: c for c in self._core_columns}
        self._extras_labels = {}
        self._custom_labels = {}
        self._custom_value_types = {}
        # _tool_table must exist before setColumnCount/setRowCount below --
        # both synchronously invoke our overridden rowCount(), which reads it.
        self._tool_table = {}
        self.setColumnCount(len(self._visible_columns))
        self.setRowCount(10)
        self.row_offset = 1
        self._interp_idle = True

    # ------------------------------------------------------------ columns

    def _pluginServesOurExtras(self):
        """True when the DB plugin's configured extras table carries every
        column this model wants to show. A mismatch (e.g. this .ui promotes
        the mill widget but the config's yaml left the plugin on
        `extras: lathe`) would otherwise stage edits into attributes the
        plugin never persists -- silently. Hide the extras columns and say
        so instead; core and custom columns keep working either way."""
        plugin_extras = getattr(self.tt, '_EXTRAS_COLUMNS', [])
        missing = [c for c in self.EXTRAS_LABELS if c not in plugin_extras]
        if missing:
            LOG.error(
                "The 'tooltable' plugin serves extras columns %s, but this "
                "widget (%s) renders %s -- missing %s. Check the config "
                "yaml's data_plugins.tooltable.kwargs.extras matches the "
                "promoted tool table widget. Hiding the extras columns.",
                plugin_extras, type(self).__name__,
                list(self.EXTRAS_LABELS), missing)
            return False
        return True

    def _refresh_custom_columns(self):
        defs = self.tt.getCustomFieldDefs()
        self._custom_columns = [CUSTOM_PREFIX + d['name'] for d in defs]
        self._custom_labels = {CUSTOM_PREFIX + d['name']: d['label'] for d in defs}
        self._custom_value_types = {CUSTOM_PREFIX + d['name']: d['value_type'] for d in defs}

    def _order_columns(self, cols):
        """Move any TRAILING_CORE_COLUMNS to the end (after extras/custom),
        preserving their relative order -- everything else keeps its order.
        No-op when TRAILING_CORE_COLUMNS is empty (the lathe)."""
        if not self.TRAILING_CORE_COLUMNS:
            return list(cols)
        trailing = [c for c in cols if c in self.TRAILING_CORE_COLUMNS]
        head = [c for c in cols if c not in self.TRAILING_CORE_COLUMNS]
        return head + trailing

    def _default_visible_columns(self):
        extras = [c for c in self.DEFAULT_VISIBLE_EXTRAS if c in self._extras_columns]
        return self._order_columns(list(self._core_columns) + extras)

    def allColumns(self):
        """Every known column key, in display order: core, then extras, then
        custom -- with any TRAILING_CORE_COLUMNS (e.g. Remark on the mill)
        moved to the very end so "Show All Columns" and the default order
        agree.

        Capped at MAX_COLUMNS -- the model's real (fixed) column count; see
        setVisibleColumns. An overflow here would mean ~150+ custom fields
        defined, at which point the newest ones are silently unavailable
        rather than crashing; raising MAX_COLUMNS is the fix if that's ever
        a real shop's use case.
        """
        cols = self._order_columns(
            list(self._core_columns) + list(self._extras_columns)
            + list(self._custom_columns))
        return cols[:MAX_COLUMNS]

    def visibleColumns(self):
        return list(self._visible_columns)

    def _filterToKnownColumns(self, columns):
        """columns, minus any key that no longer exists (a removed custom
        column, or one from a differently-configured core set) -- falls
        back to just the core columns if that leaves nothing at all."""
        all_cols = self.allColumns()
        return [c for c in columns if c in all_cols] or list(self._core_columns)

    def setVisibleColumns(self, columns):
        # Toggling column *visibility* only ever changes _visible_columns
        # (what columnCount() reports) -- it never touches the model's real
        # (fixed, MAX_COLUMNS) column count. An earlier version grew the
        # real count here via setColumnCount() as new custom fields showed
        # up; calling that *after* a proxy/view was already attached raced
        # its columnsInserted signal against our columnCount() override
        # still reporting the pre-growth total ("QSortFilterProxyModel:
        # invalid inserted rows reported by source model"). Fixed capacity
        # sidesteps this the same way the row model already does.
        visible = self._filterToKnownColumns(columns)
        self.beginResetModel()
        self._visible_columns = visible
        self.endResetModel()
        if self._db_backed:
            # Persist every change, not just user-initiated ones (e.g. a
            # custom column disappearing out from under an existing
            # selection): the persisted set should always mirror what's
            # actually currently shown, with no special-casing over who
            # triggered the change.
            self.tt.setVisibleColumns(visible)

    def columnLabel(self, key):
        if key in self._core_labels:
            return self._core_labels[key]
        if key in self._extras_labels:
            return self._extras_labels[key]
        return self._custom_labels.get(key, key)

    def columnGroup(self, key):
        if key in self._core_columns:
            return 'core'
        if key in self._extras_columns:
            return 'extras'
        return 'custom'

    # ------------------------------------------------------------ loading

    def _load_full_table(self):
        core = self.tt.getToolTable()  # {0: NO_TOOL, tnum: {letter: value}}
        table = {}
        for tnum, core_row in core.items():
            row = dict(core_row)
            if tnum != 0 and self._db_backed:
                extras = self.tt.getToolExtras(tnum) or {}
                for key in self._extras_columns:
                    value = extras.get(key)
                    if value is None:
                        # no extras row yet (or an unset cell): show the
                        # machine flavor's default (e.g. mill atc = True)
                        # instead of a blank that reads as "no value".
                        value = self.EXTRAS_DEFAULTS.get(key)
                    row[key] = value
                values = self.tt.getCustomFieldValues(tnum)
                for key in self._custom_columns:
                    row[key] = values.get(key[len(CUSTOM_PREFIX):])
            table[tnum] = row

        self.beginResetModel()
        self._tool_table = table
        self.endResetModel()
        self._set_dirty(False)
        LOG.debug("LatheToolModel reload: tools=%s", len(table) - 1)

    def _onExtrasChanged(self, tool_no):
        # saveAllToolExtras() emits this once per tool in the batch (a
        # correct, real per-tool signal -- kept that way in case anything
        # ever wants that granularity). But saveToolTable() below already
        # does its own single authoritative _load_full_table() right after
        # the whole batch commits, so reacting here too, once per tool,
        # would turn one Save into N redundant full reloads -- suppressed
        # for the duration of that batch call.
        if not self._reload_signals_suppressed:
            self._load_full_table()

    def _onFieldsChanged(self):
        self._refresh_custom_columns()
        # keep whatever core/extras columns were visible; drop any custom
        # column that no longer exists, but don't force newly-added ones
        # into view (the user picks those from the header menu).
        # setVisibleColumns() grows column capacity itself, atomically, if
        # a new custom field means there's more room needed.
        kept = [c for c in self._visible_columns
                if not c.startswith(CUSTOM_PREFIX) or c in self._custom_columns]
        self.setVisibleColumns(kept)
        self._load_full_table()

    def refreshModel(self):
        self.beginResetModel()
        self.endResetModel()

    def _onInterpStateChanged(self, interp_state):
        import linuxcnc
        was_idle = self._interp_idle
        self._interp_idle = (interp_state == linuxcnc.INTERP_IDLE)
        if was_idle != self._interp_idle:
            self.beginResetModel()
            self.endResetModel()

    # ------------------------------------------------------------ Qt model

    def columnCount(self, parent=None):
        return len(self._visible_columns)

    def rowCount(self, parent=None):
        return max(0, len(self._tool_table) - 1)

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self.columnLabel(self._visible_columns[section])
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Vertical:
            # Row header shows the tool number instead of a plain row
            # index -- it's Qt's own always-visible-through-horizontal-
            # scroll widget, so this is what keeps T in view without
            # needing a frozen/pinned column (see ToolNumberHeaderView).
            return self.toolDataFromRow(section)['T']
        return QStandardItemModel.headerData(self, section, orientation, role)

    def _tool_no_for_row(self, row):
        return sorted(self._tool_table)[row + self.row_offset]

    def flags(self, index):
        col_key = self._visible_columns[index.column()]

        if col_key == 'T':
            return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable

        if not self._interp_idle:
            # Every column locks while a program runs, not just core --
            # a custom/extras value could still be referenced by a
            # subroutine or other mid-program logic, so editing any of it
            # during machine operation is unsafe practice regardless of
            # whether LinuxCNC's own interpreter reads that column live.
            return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable

        return (Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable |
                Qt.ItemFlag.ItemIsEditable)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        row, col = index.row(), index.column()
        key = self._visible_columns[col]
        tnum = self._tool_no_for_row(row)

        if role in (Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole):
            return self._tool_table[tnum].get(key)

        elif role == Qt.ItemDataRole.TextAlignmentRole:
            if self.columnGroup(key) == 'custom':
                value_type = self._custom_value_types.get(key)
                return CUSTOM_FIELD_ALIGNMENT.get(
                    value_type, Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
            if key in ('R',) or key in self.TEXT_EXTRAS:
                return Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
            elif key in ('T', 'P', 'Q') or key in self.BOOL_EXTRAS:
                return Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter
            else:
                return Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight

        elif role == Qt.ItemDataRole.ForegroundRole:
            if self.stat.tool_in_spindle == tnum:
                return QBrush(self.current_tool_color)
            return QStandardItemModel.data(self, index, role)

        elif role == Qt.ItemDataRole.BackgroundRole and self.current_tool_bg is not None:
            if self.stat.tool_in_spindle == tnum:
                return QBrush(self.current_tool_bg)
            return QStandardItemModel.data(self, index, role)

        return QStandardItemModel.data(self, index, role)

    def setData(self, index, value, role):
        key = self._visible_columns[index.column()]
        tnum = self._tool_no_for_row(index.row())
        self._tool_table[tnum][key] = value
        self._set_dirty(True)
        return True

    def _set_dirty(self, dirty):
        """Track unsaved edits staged in memory since the last save/reload;
        emits only on an actual state change so listeners (the Save button's
        color indicator) aren't hit on every single keystroke."""
        dirty = bool(dirty)
        if dirty == self._dirty:
            return
        self._dirty = dirty
        self.dirtyChanged.emit(self._dirty)

    # ------------------------------------------------------------ actions

    def toolDataFromRow(self, row):
        tnum = self._tool_no_for_row(row)
        return self._tool_table[tnum]

    def distinctColumnValues(self, key):
        """Distinct non-empty values currently loaded for `key`, sorted --
        used to seed open-vocabulary combo editors (insert_shape,
        holder_style) with whatever this shop's own data already uses,
        alongside a fixed seed list."""
        values = set()
        for tnum, row in self._tool_table.items():
            if tnum == 0:
                continue
            value = row.get(key)
            if value:
                values.add(value)
        return sorted(values)

    def distinctColumnValuesForType(self, key, tool_type):
        """Like distinctColumnValues, but scoped to rows whose `type`
        matches `tool_type` -- e.g. only holder_style values this shop has
        actually used on grooving tools, not every holder_style value ever
        used on any tool."""
        t = (tool_type or '').strip().lower()
        values = set()
        for tnum, row in self._tool_table.items():
            if tnum == 0:
                continue
            if (row.get('type') or '').strip().lower() != t:
                continue
            value = row.get(key)
            if value:
                values.add(value)
        return sorted(values)

    def insertShapeOptionsForType(self, tool_type):
        """insert_shape choices valid for a given tool `type` -- the same
        discrimination pb_lathe_conv's Fusion-era tool library made (see
        OPEN_VOCAB_SEED_OPTIONS docstring above)."""
        t = (tool_type or '').strip().lower()
        if t in NO_INSERT_TYPES:
            return []  # no insert-shape concept for drills/taps

        if t in GROOVING_TYPES:
            seed = list(GROOVING_INSERT_SHAPES)
        elif t in THREADING_TYPES:
            seed = list(THREADING_INSERT_SHAPES)
        else:
            return list(GENERAL_INSERT_SHAPES)  # turning/boring/custom

        for value in self.distinctColumnValuesForType('insert_shape', t):
            if value not in seed:
                seed.append(value)
        return seed

    def holderStyleOptionsForRow(self, tool_type, insert_shape):
        """holder_style choices valid for a given tool `type`, further
        narrowed by the row's already-chosen `insert_shape` for turning/
        boring/custom tools. Full ISO holder codes (e.g. "SCLCR") encode
        their compatible insert shape as the 2nd character of the code
        (verified against every turning/boring row in the shipped seed
        data: insert_shape 'C' pairs only with holder codes like SCLCR/
        SCLCL/SCMCN, never SDJCR) -- so an insert shape discriminates which
        holder codes make physical sense, the same way pb_lathe_conv's
        Fusion-era tool library discriminated its own (single-letter THSC)
        holder field from insert shape."""
        t = (tool_type or '').strip().lower()
        if t in NO_INSERT_TYPES:
            return []  # no holder concept for drills/taps

        if t in GROOVING_TYPES:
            seed = list(GROOVING_HOLDER_STYLES)
            for value in self.distinctColumnValuesForType('holder_style', t):
                if value not in seed:
                    seed.append(value)
            return seed

        if t in THREADING_TYPES:
            seed = list(THREADING_HOLDER_STYLES)
            for value in self.distinctColumnValuesForType('holder_style', t):
                if value not in seed:
                    seed.append(value)
            return seed

        # turning / boring / custom -- one shared pool of full ISO holder
        # codes; narrow to ones compatible with the chosen insert shape.
        shape = (insert_shape or '').strip().upper()
        all_values = self.distinctColumnValues('holder_style')
        if len(shape) == 1:
            matching = [v for v in all_values if len(v) >= 2 and v[1].upper() == shape]
            if matching:
                return matching
        return all_values

    def addTool(self):
        try:
            tnum = max(k for k in self._tool_table if k != 0) + 1
        except ValueError:
            tnum = 1

        row = len(self._tool_table) - 1
        if row == 1000:
            return False  # max 1000 tools, matches the core widget's limit

        self.beginInsertRows(QModelIndex(), row, row)
        new_row = self.tt.newTool(tnum=tnum)
        for key in self._extras_columns:
            new_row.setdefault(key, self.EXTRAS_DEFAULTS.get(key))
        for key in self._custom_columns:
            new_row.setdefault(key, None)
        self._tool_table[tnum] = new_row
        self.endInsertRows()
        return True

    def removeTool(self, row):
        tnum = self._tool_no_for_row(row)
        self.beginRemoveRows(QModelIndex(), row, row)
        del self._tool_table[tnum]
        self.endRemoveRows()
        return True

    def renumberTool(self, row, new_tool_no):
        """Commits immediately (unlike core-column edits, which stage in
        memory until Save) -- schema v1 makes this a single UPDATE that
        can't lose extras/custom data, so there's no reason to defer it.

        The classic file-based ToolTable plugin has no equivalent atomic
        op -- but also no extras/custom data that a delete+recreate could
        lose, so that's exactly what it falls back to here.
        """
        tnum = self._tool_no_for_row(row)
        new_tool_no = int(new_tool_no)
        if hasattr(self.tt, 'renumberTool'):
            self.tt.renumberTool(tnum, new_tool_no)
        else:
            table = self.tt.getToolTable()
            if new_tool_no != 0 and new_tool_no in table:
                raise ValueError('tool %s already exists' % new_tool_no)
            core = dict(table[tnum])
            core['T'] = new_tool_no
            del table[tnum]
            table[new_tool_no] = core
            self.tt.saveToolTable(table)
        self._load_full_table()
        return True

    def saveToolTable(self):
        # Snapshot before the core save: self.tt.saveToolTable() below emits
        # tool_table_changed synchronously, which our own _load_full_table
        # slot (connected in __init__) reacts to immediately -- that would
        # overwrite self._tool_table with freshly-reloaded (pre-extras-save)
        # data before the extras/custom loop below ever runs, silently
        # discarding those in-memory edits.
        snapshot = {tnum: dict(row) for tnum, row in self._tool_table.items()}

        if self._db_backed:
            # `row` here is core+extras+custom all flattened into one dict
            # (see _load_full_table) -- filter down to just the core subset
            # before handing it to the core-only saveToolTable() call.
            core_table = {tnum: {k: v for k, v in row.items() if k in self._core_columns}
                          for tnum, row in snapshot.items()}
        else:
            # Nothing to filter out here: with no extras/custom columns in
            # this mode, `row` already *is* the classic plugin's own tool
            # dict, untouched -- which includes keys beyond
            # self._core_columns that the *configured display columns*
            # don't cover but the plugin's own saveToolTable() still
            # unconditionally requires (e.g. 'P', inserted into its column
            # list internally regardless of what's configured, for the
            # .tbl file format). Filtering to self._core_columns here
            # stripped 'P' right back out and crashed with KeyError('P').
            core_table = snapshot
        self.tt.saveToolTable(core_table)

        if not self._db_backed:
            # The classic plugin's saveToolTable() only writes the .tbl
            # file and tells the LinuxCNC *task* to reload it
            # (CMD.load_tool_table(), an NML command) -- it does not
            # refresh its own Python-side self.TOOL_TABLE cache (what
            # getToolTable() below actually returns). That only happens
            # asynchronously, ~50ms later, via a QFileSystemWatcher
            # noticing the file changed -- relying on that alone races
            # _load_full_table() below, which could read stale (pre-save)
            # data if it runs first. Force the refresh synchronously
            # instead, the same way the DB-backed plugin's own
            # saveToolTable() already does internally (it calls its own
            # loadToolTable() as part of the same method).
            self.tt.loadToolTable()

        # One batched transaction each for extras/custom values, not one
        # commit per tool (or per tool per custom column) -- see
        # saveAllToolExtras/setCustomFieldValues docstrings: the per-tool
        # loop this replaced made a single-cell edit take ~1.6s against the
        # real 23-tool fixture (47 individual disk-sync'd commits). N/A at
        # all for the classic file-based backend -- no extras/custom
        # concept there, core_table above is the whole save.
        if self._db_backed:
            extras_by_tool = {}
            custom_by_tool = {}
            for tnum, row in snapshot.items():
                if tnum == 0:
                    continue
                extras_by_tool[tnum] = {k: row.get(k) for k in self._extras_columns}
                if self._custom_columns:
                    custom_by_tool[tnum] = {key[len(CUSTOM_PREFIX):]: row.get(key)
                                            for key in self._custom_columns}

            self._reload_signals_suppressed = True
            try:
                if extras_by_tool:
                    self.tt.saveAllToolExtras(extras_by_tool)
                if custom_by_tool:
                    self.tt.setCustomFieldValues(custom_by_tool)
            finally:
                self._reload_signals_suppressed = False

        self._load_full_table()  # authoritative final state after everything committed

        # Writing the table and telling LinuxCNC to re-read it (self.tt.
        # saveToolTable() above) does NOT, on its own, re-apply the
        # *currently active* tool's offset -- LinuxCNC only recomputes that
        # on a tool change or an explicit G43, not just because the
        # underlying table file/row changed. If the tool actually in the
        # spindle is what got edited, the DRO keeps showing its old offset
        # until G43 is reissued. Same recipe qtpyvcp's own classic
        # ToolTable plugin already uses after homing (reload_tool():
        # "M61 Q<n> G43") -- just not currently wired to fire after a
        # table save the way it is after homing.
        if self._interp_idle:
            tnum = self.stat.tool_in_spindle
            if tnum:
                issue_mdi("M61 Q%s G43" % tnum)

        return True

    def clearToolTable(self):
        self.beginRemoveRows(QModelIndex(), 0, 100)
        self._tool_table = {0: self._tool_table[0]}
        self.endRemoveRows()
        return True

    def loadToolTable(self):
        self._load_full_table()
        return True

# coding=utf-8
"""LatheToolModel -- composes core tool-table columns with tool_lathe
extras and user-defined custom-field columns into one flat, editable table
(plan §6 Phase 3).

Core columns are the same letter-keyed data (T P X Z D I J Q R ...) served by
``qtpyvcp.plugins.db_tool_table.DBToolTable``; extras are ``tool_lathe``
attribute names; custom fields are keyed ``custom:<name>``. All three groups
are staged in one in-memory dict per tool and committed together by
:meth:`saveToolTable` -- one widget, one Save action, per the plan's single-
store rule. Core columns lock while a program is running (LinuxCNC owns
them via the tooldb protocol meanwhile); extras and custom columns stay
editable throughout, since LinuxCNC never sees them.
"""

from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtGui import QStandardItemModel, QColor, QBrush

from qtpyvcp.utilities.logger import getLogger
from qtpyvcp.plugins import getPlugin
from qtpyvcp.actions import IN_DESIGNER

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

DEFAULT_VISIBLE_EXTRAS = ['type', 'insert_shape', 'holder_style']

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
# "SCLCR", ...). These get an *editable* combo seeded with common values
# plus whatever this shop's own data already uses (see
# LatheToolModel.distinctColumnValues), not a strict pick-list.
OPEN_VOCAB_SEED_OPTIONS = {
    'insert_shape': ['C', 'D', 'V', 'W', 'T', 'R', 'S'],
    'holder_style': [],
}


MAX_COLUMNS = 200  # generous fixed capacity; mirrors the row model's
                   # existing fixed setRowCount(1000)/max-1000-tools limit


class LatheToolModel(QStandardItemModel):

    def __init__(self, parent=None):
        super(LatheToolModel, self).__init__(parent)

        if IN_DESIGNER:
            self._core_columns = ['T', 'P', 'X', 'Z', 'D', 'I', 'J', 'Q', 'R']
            self._extras_columns = []
            self._custom_columns = []
            self._visible_columns = list(self._core_columns)
            self._core_labels = {c: c for c in self._core_columns}
            self._extras_labels = {}
            self._custom_labels = {}
            self.setColumnCount(len(self._visible_columns))
            self.setRowCount(10)
            self._tool_table = {}
            self.row_offset = 1
            self._interp_idle = True
            return

        self.status = getPlugin('status')
        self.stat = self.status.stat
        self.tt = getPlugin('tooltable')

        self.current_tool_color = QColor(Qt.darkGreen)
        self.current_tool_bg = None

        self._core_columns = list(self.tt.columns)
        self._core_labels = dict(self.tt.COLUMN_LABELS)
        self._extras_columns = list(EXTRAS_ORDER)
        self._extras_labels = dict(EXTRAS_LABELS)
        self._custom_columns = []
        self._custom_labels = {}

        self.row_offset = 1
        self._interp_idle = True
        self._tool_table = {}

        self._refresh_custom_columns()
        self._visible_columns = self._default_visible_columns()
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
        self.tt.tool_table_changed.connect(lambda *_: self._load_full_table())
        self.tt.extras_changed.connect(lambda *_: self._load_full_table())
        self.tt.fields_changed.connect(self._onFieldsChanged)

    # ------------------------------------------------------------ columns

    def _refresh_custom_columns(self):
        defs = self.tt.getCustomFieldDefs()
        self._custom_columns = [CUSTOM_PREFIX + d['name'] for d in defs]
        self._custom_labels = {CUSTOM_PREFIX + d['name']: d['label'] for d in defs}

    def _default_visible_columns(self):
        extras = [c for c in DEFAULT_VISIBLE_EXTRAS if c in self._extras_columns]
        return list(self._core_columns) + extras

    def allColumns(self):
        """Every known column key, grouped: core, then extras, then custom.

        Capped at MAX_COLUMNS -- the model's real (fixed) column count; see
        setVisibleColumns. An overflow here would mean ~150+ custom fields
        defined, at which point the newest ones are silently unavailable
        rather than crashing; raising MAX_COLUMNS is the fix if that's ever
        a real shop's use case.
        """
        cols = list(self._core_columns) + list(self._extras_columns) + list(self._custom_columns)
        return cols[:MAX_COLUMNS]

    def visibleColumns(self):
        return list(self._visible_columns)

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
        all_cols = self.allColumns()
        visible = [c for c in columns if c in all_cols] or list(self._core_columns)
        self.beginResetModel()
        self._visible_columns = visible
        self.endResetModel()

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
            if tnum != 0:
                extras = self.tt.getToolExtras(tnum) or {}
                for key in self._extras_columns:
                    row[key] = extras.get(key)
                values = self.tt.getCustomFieldValues(tnum)
                for key in self._custom_columns:
                    row[key] = values.get(key[len(CUSTOM_PREFIX):])
            table[tnum] = row

        self.beginResetModel()
        self._tool_table = table
        self.endResetModel()
        LOG.debug("LatheToolModel reload: tools=%s", len(table) - 1)

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
        return QStandardItemModel.headerData(self, section, orientation, role)

    def _tool_no_for_row(self, row):
        return sorted(self._tool_table)[row + self.row_offset]

    def flags(self, index):
        col_key = self._visible_columns[index.column()]

        if col_key == 'T':
            return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable

        if self.columnGroup(col_key) == 'core' and not self._interp_idle:
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
            if key in ('R',) or key in TEXT_EXTRAS or self.columnGroup(key) == 'custom':
                return Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
            elif key in ('T', 'P', 'Q'):
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
        return True

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
            new_row.setdefault(key, None)
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
        can't lose extras/custom data, so there's no reason to defer it."""
        tnum = self._tool_no_for_row(row)
        self.tt.renumberTool(tnum, new_tool_no)
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

        core_table = {tnum: {k: v for k, v in row.items() if k in self._core_columns}
                      for tnum, row in snapshot.items()}
        self.tt.saveToolTable(core_table)

        for tnum, row in snapshot.items():
            if tnum == 0:
                continue
            extras = {k: row.get(k) for k in self._extras_columns}
            self.tt.saveToolExtras(tnum, extras)
            for key in self._custom_columns:
                self.tt.setCustomFieldValue(tnum, key[len(CUSTOM_PREFIX):], row.get(key))

        self._load_full_table()  # authoritative final state after everything committed
        return True

    def clearToolTable(self):
        self.beginRemoveRows(QModelIndex(), 0, 100)
        self._tool_table = {0: self._tool_table[0]}
        self.endRemoveRows()
        return True

    def loadToolTable(self):
        self._load_full_table()
        return True

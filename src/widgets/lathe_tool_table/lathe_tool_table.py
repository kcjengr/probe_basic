# coding=utf-8
"""LatheToolTable -- unified tool table widget (plan §6 Phase 3).

One editing surface for core tool-table columns, tool_lathe extras, and
user-defined custom columns. Keeps the same public slot surface as
qtpyvcp's stock ``qtpyvcp.widgets.input_widgets.tool_table.ToolTable``
(saveToolTable/loadToolTable/addTool/deleteSelectedTool/... ) so it can
promote the existing ``tooltable`` object in probe_basic_lathe.ui without
changing any `.ui` signal/slot wiring -- only the promoted class changes.
"""

from PySide6.QtCore import (Qt, Slot, Signal, Property, QModelIndex, QTimer,
                            QSortFilterProxyModel)
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QTableView, QHeaderView, QAbstractItemView,
                               QStyledItemDelegate, QDoubleSpinBox, QSpinBox,
                               QLineEdit, QComboBox, QMessageBox, QMenu,
                               QInputDialog)

from qtpyvcp.actions.machine_actions import issue_mdi
from qtpyvcp.utilities.logger import getLogger
from qtpyvcp.actions import IN_DESIGNER

from .lathe_tool_model import (LatheToolModel, TEXT_EXTRAS, CUSTOM_PREFIX,
                               STRICT_ENUM_OPTIONS, OPEN_VOCAB_SEED_OPTIONS,
                               FLOAT_DECIMALS)
from .add_column_dialog import AddColumnDialog

LOG = getLogger(__name__)

GROUP_LABELS = {'core': 'Core', 'extras': 'Lathe Extras', 'custom': 'Custom'}

# Qt's QComboBox default (10) puts a scrollbar inside the popup well before
# any of this table's real option lists are long enough to need one (e.g.
# holder_style already has 14+ distinct real values) -- a scrollable list
# popped out of a table cell is one nested-scroll-region too many. Generous
# enough that realistic option counts just show in full instead.
COMBO_MAX_VISIBLE_ITEMS = 25

# Dynamic property tagging the bool-custom-column combo editor, so
# setEditorData/setModelData can special-case it without relying on Qt's
# built-in QVariant(bool)->QString marshaling (confirmed live: it lowercases
# to "true"/"false", not "True"/"False" -- matching combo item text against
# that silently mismatches and leaves the wrong item pre-selected) -- easier
# to just own the round-trip as a real Python bool throughout.
BOOL_EDITOR_PROP = '_lathe_bool_editor'

class LatheItemDelegate(QStyledItemDelegate):

    def __init__(self, model, table=None):
        super(LatheItemDelegate, self).__init__()
        self._model = model
        self._table = table
        self._padding = ' ' * 2

    def _sourceRowForIndex(self, index):
        """Map a (possibly proxy) row index back to the model's own row
        numbering. Needed now that some editors' choices depend on the
        row's *data* (type/insert_shape), not just the column: index.row()
        is the view's visual (post-sort) row, which only matches the
        model's internal row order when the table isn't currently sorted
        by some other column."""
        proxy = getattr(self._table, 'proxy_model', None)
        if proxy is not None and index.model() is proxy:
            index = proxy.mapToSource(index)
        return index.row()

    def displayText(self, value, locale):
        if isinstance(value, float):
            # Explicit, named setting (not a bare magic number) so every
            # float column -- core, extras, or a custom float field --
            # displays at the same precision on purpose, not by accident.
            return f"{value:.{FLOAT_DECIMALS}f}"
        if value is None:
            return ''
        return f"{self._padding}{value}"

    def sizeHint(self, option, index):
        # ResizeToContents sizes columns off this; the base implementation
        # has no margin, so content butts right up against the divider.
        size = super(LatheItemDelegate, self).sizeHint(option, index)
        size.setWidth(size.width() + 10)  # 5px each side
        return size

    def createEditor(self, parent, option, index):
        key = self._model._visible_columns[index.column()]
        group = self._model.columnGroup(key)

        if key in STRICT_ENUM_OPTIONS:
            # DB CHECK-constrained: a strict pick-list, not editable free
            # text -- the user cannot enter a value the database would
            # reject on save.
            editor = QComboBox(parent)
            editor.setFrame(False)
            editor.setMaxVisibleItems(COMBO_MAX_VISIBLE_ITEMS)
            editor.addItems(STRICT_ENUM_OPTIONS[key])
            self._popOpenOnceShown(editor)
            return editor

        if key in OPEN_VOCAB_SEED_OPTIONS:
            # Open vocabulary in practice (mixes ISO letters with descriptive
            # codes depending on tool type) -- editable combo, but *which*
            # choices are offered is discriminated by this row's own `type`
            # (and, for holder_style, its already-chosen `insert_shape`)
            # rather than dumping every value ever used for any tool into
            # one list -- see LatheToolModel.insertShapeOptionsForType /
            # holderStyleOptionsForRow.
            row_data = self._model.toolDataFromRow(self._sourceRowForIndex(index))
            tool_type = row_data.get('type')
            if key == 'insert_shape':
                options = self._model.insertShapeOptionsForType(tool_type)
            else:  # 'holder_style'
                options = self._model.holderStyleOptionsForRow(tool_type, row_data.get('insert_shape'))
            current_value = row_data.get(key)

            if not options:
                # e.g. drill/tap rows have no insert-shape/holder concept at
                # all -- a combo with nothing valid to offer is worse than
                # plain free text.
                editor = QLineEdit(parent)
                editor.setFrame(False)
                return editor

            editor = QComboBox(parent)
            editor.setFrame(False)
            editor.setEditable(True)
            # Qt auto-attaches a QCompleter to every editable combobox, which
            # pops its own inline autocomplete list -- a second popup
            # mechanism fighting our explicit showPopup() below for focus
            # (the seeded item list below is already the intended picker;
            # there's no free-text-filter feature here to complete against).
            editor.setCompleter(None)
            editor.setMaxVisibleItems(COMBO_MAX_VISIBLE_ITEMS)
            seen = set()
            for value in options + ([current_value] if current_value else []):
                if value and value not in seen:
                    seen.add(value)
                    editor.addItem(value)
            # 200ms, not 0: opening the popup this way (rather than Qt's own
            # native double-click handling, which non-editable combos like
            # TYPE get for free) races the initiating double-click's own
            # trailing mouse-release event still draining through the queue
            # if fired too soon -- confirmed live (60ms wasn't enough, 200ms
            # is stable).
            self._popOpenOnceShown(editor, delay_ms=200)
            return editor

        if group == 'custom':
            # Chris: typing "3.5" into an int-typed custom column used to be
            # accepted at the cell (plain QLineEdit for every custom column
            # regardless of its declared value_type), only to blow up later
            # -- qtpyvcp's _cast_custom_value() does int(raw) on the next
            # load, which raises ValueError on a non-integer string instead
            # of truncating. Guard at entry instead: pick the editor widget
            # from the field's own value_type so an invalid entry can't be
            # typed in the first place.
            value_type = self._model._custom_value_types.get(key)
            if value_type == 'int':
                editor = QSpinBox(parent)
                editor.setFrame(False)
                editor.setAlignment(Qt.AlignmentFlag.AlignCenter)
                editor.setRange(-999999, 999999)
                return editor
            if value_type == 'float':
                editor = QDoubleSpinBox(parent)
                editor.setFrame(False)
                editor.setAlignment(Qt.AlignmentFlag.AlignCenter)
                editor.setDecimals(FLOAT_DECIMALS)
                editor.setRange(-100000, 100000)
                return editor
            if value_type == 'bool':
                editor = QComboBox(parent)
                editor.setFrame(False)
                editor.addItems(['True', 'False'])
                editor.setProperty(BOOL_EDITOR_PROP, True)
                self._popOpenOnceShown(editor)
                return editor
            # text (or an unrecognized/future value_type): free text, same
            # as always.
            editor = QLineEdit(parent)
            editor.setFrame(False)
            return editor

        if key == 'R' or key in TEXT_EXTRAS:
            editor = QLineEdit(parent)
            editor.setFrame(False)
            return editor

        if key in ('T', 'P', 'Q'):
            editor = QSpinBox(parent)
            editor.setFrame(False)
            editor.setAlignment(Qt.AlignmentFlag.AlignCenter)
            editor.setMaximum(9 if key == 'Q' else 99999)
            return editor

        # everything else (X/Z/D/I/J offsets, numeric extras) is a float
        editor = QDoubleSpinBox(parent)
        editor.setFrame(False)
        editor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        editor.setDecimals(4)
        editor.setRange(-100000, 100000)
        return editor

    def setEditorData(self, editor, index):
        if isinstance(editor, QComboBox) and editor.property(BOOL_EDITOR_PROP):
            value = bool(index.data(Qt.ItemDataRole.EditRole))
            editor.setCurrentIndex(editor.findText('True' if value else 'False'))
            return
        super(LatheItemDelegate, self).setEditorData(editor, index)

    def setModelData(self, editor, model, index):
        if isinstance(editor, QComboBox) and editor.property(BOOL_EDITOR_PROP):
            model.setData(index, editor.currentText() == 'True',
                          Qt.ItemDataRole.EditRole)
            return
        super(LatheItemDelegate, self).setModelData(editor, model, index)

    @staticmethod
    def _popOpenOnceShown(combo, delay_ms=0):
        """Open the dropdown the instant the editor appears, instead of
        requiring a second tap on the (tiny, easy-to-miss on a touchscreen)
        arrow button after the first double-click/tap creates it.

        delay_ms matters for editable combos specifically: non-editable
        ones (e.g. TYPE) open fine at 0ms because Qt's own native
        mouseDoubleClickEvent handling opens those synchronously as part of
        the same double-click, which correctly accounts for the initiating
        click's mouse button still being logically "down". Editable combos
        never auto-open natively, so *our* showPopup() call is the only
        thing opening them -- firing it before that button-down state has
        fully drained through the event queue raced Qt's popup grab into
        treating the eventual release as "dismiss", closing it almost
        immediately (confirmed live; see callers for the delay each editor
        type actually needs).
        """
        def _fire():
            # The popup defaults to the combo's own width (i.e. the cell/
            # column's width), which the item padding above then eats into --
            # long entries (e.g. "THREADING", "GROOVE EXTERNAL") were getting
            # elided even though the column itself is wide enough to show
            # them as plain (non-editing) cell text. Widen the popup to
            # actually fit its widest item instead of inheriting the cell's
            # (possibly narrower) width.
            view = combo.view()
            if view is not None:
                hint = view.sizeHintForColumn(0)
                if hint > 0:
                    view.setMinimumWidth(hint + 24)
            combo.showPopup()
        QTimer.singleShot(delay_ms, _fire)


class LatheToolTable(QTableView):
    toolSelected = Signal(int)

    def __init__(self, parent=None):
        super(LatheToolTable, self).__init__(parent)

        self.clicked.connect(self.onClick)
        self.doubleClicked.connect(self.onDoubleClick)

        self.tool_model = LatheToolModel(self)

        if not IN_DESIGNER and self.tool_model.tt is not None:
            self.tool_model.tt.tool_table_changed.connect(self._onToolTableChanged)

        self.item_delegate = LatheItemDelegate(self.tool_model, self)
        self.setItemDelegate(self.item_delegate)

        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setFilterKeyColumn(0)
        self.proxy_model.setSourceModel(self.tool_model)
        self.setModel(self.proxy_model)

        self._confirm_actions = False
        self._current_tool_color = QColor('sage')
        self._current_tool_bg = None

        self.setSortingEnabled(True)
        self.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)
        # Center the tool numbers (the styled default is left/vcenter) and
        # give them 3px of breathing room on the right -- ResizeToContents
        # sizes the header to the text alone, which left the numbers
        # touching the right border edge. Padding-only stylesheet, scoped
        # to this header instance: the theme's global QHeaderView rule
        # (background/color/font) still cascades in for everything not set
        # here, so this can't repeat the earlier solid-black regression
        # (that came from overriding background-color itself).
        self.verticalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalHeader().setStyleSheet(
            'QHeaderView::section { padding-right: 3px; }')
        # Double-clicking a cell in the (permanently non-editable) T column
        # already opens the renumber dialog (see onDoubleClick) -- now that
        # the row header is *also* effectively a pinned tool-number label
        # (it stays put through horizontal scrolling, unlike the real T
        # column), give it the same affordance.
        self.verticalHeader().sectionDoubleClicked.connect(
            self._onRowHeaderDoubleClicked)
        self.setAlternatingRowColors(True)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.setSelectionMode(QTableView.SingleSelection)
        self.setWordWrap(False)
        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)
        # NOT unconditionally setStretchLastSection(True): it forces the
        # last visible column to exactly fill whatever space remains after
        # the others take their content-sized width -- shrinking it *below*
        # its own content's needed width if the rest already fill the
        # viewport (e.g. a "Holder" column showing "GROOVE EXTERNAL" got
        # clipped this way). But leaving it permanently off left a bare gap
        # after the last column for the classic (core-columns-only, fewer/
        # narrower columns) backend, which rarely fills the viewport at
        # all. _updateLastColumnStretch() below toggles it dynamically:
        # stretch only when there's genuinely leftover width to fill.
        self.horizontalHeader().setSortIndicator(0, Qt.AscendingOrder)

        # Per-item vertical scrolling (Qt's default) stops short of the
        # last row whenever the viewport height isn't an exact multiple of
        # row height -- the remaining sliver isn't enough to trigger one
        # more scroll step, so the last row sits half (or fully) clipped at
        # the bottom. Per-pixel scrolling has no such quantization.
        self.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)

        # per-column visibility menu (UX carried from tool_library_table.py)
        header = self.horizontalHeader()
        header.setContextMenuPolicy(Qt.CustomContextMenu)
        header.customContextMenuRequested.connect(self._onHeaderContextMenu)

        self._updateLastColumnStretch()

    def resizeEvent(self, event):
        super(LatheToolTable, self).resizeEvent(event)
        self._updateLastColumnStretch()

    def _updateLastColumnStretch(self):
        """Stretch the last visible column to fill any leftover viewport
        width -- but only when there actually is leftover width. Whether
        that's true depends on the current viewport size *and* how many/
        how wide the visible columns are (e.g. the classic core-columns-
        only backend rarely fills the viewport at all; the full DB-backed
        table with several extras/custom columns visible often already
        exceeds it) -- not fixed, so this recomputes on every resize
        rather than being decided once from the backend alone."""
        header = self.horizontalHeader()
        count = header.count()
        if count == 0:
            return

        if header.stretchLastSection():
            # Un-stretch first to measure the last column's own actual
            # content-based width -- while stretching is on, sectionSize()
            # for it reports the stretched size, not its natural one.
            header.setStretchLastSection(False)
            self.resizeColumnToContents(count - 1)

        total_width = sum(header.sectionSize(i) for i in range(count))
        header.setStretchLastSection(total_width < self.viewport().width())

    def _refreshDelegate(self):
        """Shared tail for anything that changes the visible/available
        column set (Add/Remove Column, visibility toggles): the delegate
        caches column info that needs rebuilding, and whether the last
        column should stretch can change along with the column set."""
        self.item_delegate = LatheItemDelegate(self.tool_model, self)
        self.setItemDelegate(self.item_delegate)
        self._updateLastColumnStretch()

    # ------------------------------------------------------------ sync

    @Slot(dict)
    def _onToolTableChanged(self, table):
        if not table or len(table) <= 1:
            return
        self.proxy_model.invalidate()
        self.sortByColumn(0, Qt.AscendingOrder)

    # ------------------------------------------------------- column menu

    def _onHeaderContextMenu(self, position):
        header = self.horizontalHeader()
        menu = QMenu(self)

        clicked_idx = header.logicalIndexAt(position)
        visible_cols = self.tool_model.visibleColumns()
        clicked_key = (visible_cols[clicked_idx]
                       if 0 <= clicked_idx < len(visible_cols) else None)

        # Custom columns are a DB-backed-only concept (qtpyvcp.plugins.
        # tool_table:ToolTable, the classic file-based backend, has no
        # custom-field storage) -- offering "Add Column..." against that
        # backend would just crash in AddColumnDialog. remove_column never
        # needs the same guard: _custom_columns is always empty without a
        # DB backend, so there's never a custom column to right-click.
        add_column = None
        if self.tool_model._db_backed:
            add_column = menu.addAction('Add Column...')
        remove_column = None
        if clicked_key and self.tool_model.columnGroup(clicked_key) == 'custom':
            remove_column = menu.addAction(
                'Remove Column "%s"...' % self.tool_model.columnLabel(clicked_key))
        menu.addSeparator()
        show_all = menu.addAction('Show All Columns')
        reset_default = menu.addAction('Reset Default Columns')
        menu.addSeparator()

        visible = set(self.tool_model.visibleColumns())
        sections = {'core': [], 'extras': [], 'custom': []}
        for key in self.tool_model.allColumns():
            sections[self.tool_model.columnGroup(key)].append(key)

        toggles = {}
        for group in ('core', 'extras', 'custom'):
            keys = sections[group]
            if not keys:
                continue
            section_menu = menu.addMenu(GROUP_LABELS[group])
            for key in keys:
                action = section_menu.addAction(self.tool_model.columnLabel(key))
                action.setCheckable(True)
                action.setChecked(key in visible)
                toggles[action] = key

        selected = menu.exec(header.mapToGlobal(position))
        if selected is None:
            return

        if selected == add_column:
            self.showAddColumnDialog()
        elif remove_column is not None and selected == remove_column:
            self._removeCustomColumn(clicked_key)
            return  # column set already refreshed via fields_changed
        elif selected == show_all:
            self.tool_model.setVisibleColumns(self.tool_model.allColumns())
        elif selected == reset_default:
            self.tool_model.setVisibleColumns(self.tool_model._default_visible_columns())
        elif selected in toggles:
            key = toggles[selected]
            cols = self.tool_model.visibleColumns()
            if selected.isChecked():
                if key not in cols:
                    cols.append(key)
            else:
                cols = [c for c in cols if c != key]
                if not cols:
                    QMessageBox.warning(self, 'Tool Table',
                                        'At least one column must remain visible.')
                    return
            self.tool_model.setVisibleColumns(cols)
        else:
            return

        self._refreshDelegate()

    @Slot()
    def showAddColumnDialog(self):
        """Define a new custom column (plan §5.7) -- grows the table
        immediately; no schema migration, no restart."""
        dialog = AddColumnDialog(self.tool_model.tt, self)
        before_all = set(self.tool_model.allColumns())
        if dialog.exec() == AddColumnDialog.DialogCode.Accepted:
            # fields_changed (emitted by addCustomField) already refreshed
            # tool_model's column bookkeeping; make the newly-defined column
            # visible too, so the user sees it land without a second trip
            # to this menu.
            new_keys = set(self.tool_model.allColumns()) - before_all
            if new_keys:
                self.tool_model.setVisibleColumns(
                    self.tool_model.visibleColumns() + list(new_keys))
            self._refreshDelegate()

    def _removeCustomColumn(self, key):
        """Delete a custom column definition -- and every tool's value in
        it -- permanently (cascades via the DB's FK, plan §5.7)."""
        name = key[len(CUSTOM_PREFIX):]
        label = self.tool_model.columnLabel(key)
        if not self.confirmAction(
                'Delete custom column "%s"?\n'
                'This removes it, and every tool\'s value in it, '
                'permanently.' % label):
            return
        self.tool_model.tt.removeCustomField(name)
        self._refreshDelegate()

    # ------------------------------------------------------------ slots

    @Slot()
    def saveToolTable(self):
        if not self.confirmAction("Do you want to save changes and\n"
                                  "load tool table into LinuxCNC?"):
            return
        self.tool_model.saveToolTable()

    @Slot()
    def loadToolTable(self):
        if not self.confirmAction("Do you want to re-load the tool table?\n"
                                  "All unsaved changes will be lost."):
            return
        self.tool_model.loadToolTable()

    @Slot()
    def deleteSelectedTool(self):
        current_row = self.selectedRow()
        if current_row == -1:
            return

        tdata = self.tool_model.toolDataFromRow(current_row)
        tnum = tdata['T']

        if tnum == self.tool_model.stat.tool_in_spindle:
            box = QMessageBox(QMessageBox.Warning,
                              "Can't delete current tool!",
                              "Tool #{} is currently loaded in the spindle.\n"
                              "Please remove tool from spindle and try again.".format(tnum),
                              QMessageBox.StandardButton.Ok,
                              parent=self)
            box.show()
            return False

        if not self.confirmAction('Are you sure you want to delete T{tdata[T]}?\n'
                                  '"{tdata[R]}"'.format(tdata=tdata)):
            return

        self.tool_model.removeTool(current_row)

    @Slot()
    def renumberSelectedTool(self):
        """Renumber the selected tool in place (extras/custom data follow --
        this is not a delete+recreate; see LatheToolModel/renumberTool)."""
        current_row = self.selectedRow()
        if current_row == -1:
            return
        tdata = self.tool_model.toolDataFromRow(current_row)
        old_tnum = tdata['T']

        new_tnum, ok = QInputDialog.getInt(
            self, 'Renumber Tool', 'New tool number for T%s:' % old_tnum,
            value=old_tnum, minValue=1, maxValue=99999)
        if not ok or new_tnum == old_tnum:
            return

        try:
            self.tool_model.renumberTool(current_row, new_tnum)
        except (LookupError, ValueError) as exc:
            QMessageBox.warning(self, 'Renumber Tool', str(exc))

    @Slot()
    def selectPrevious(self):
        self.selectRow(self.selectedRow() - 1)
        return True

    @Slot()
    def selectNext(self):
        self.selectRow(self.selectedRow() + 1)
        return True

    @Slot()
    def clearToolTable(self, confirm=True):
        if confirm:
            if not self.confirmAction("Do you want to delete the whole tool table?"):
                return
        self.tool_model.clearToolTable()

    @Slot()
    def addTool(self):
        self.tool_model.addTool()
        self.selectRow(self.tool_model.rowCount() - 1)

    @Slot()
    def loadSelectedTool(self):
        current_row = self.selectedRow()
        if current_row == -1:
            return
        tnum = self.tool_model.toolDataFromRow(current_row)['T']
        issue_mdi("T%s M6" % tnum)

    def selectedRow(self):
        return self.selectionModel().currentIndex().row()

    def onClick(self, index):
        row = index.row()
        tnum = self.tool_model.toolDataFromRow(row)['T']
        self.toolSelected.emit(tnum)

    def onDoubleClick(self, index):
        """The T column is never directly editable (see LatheToolModel.flags:
        a raw cell edit can't re-key the outer table dict), so double-
        clicking it doesn't open the normal in-place editor. Route it to
        renumberSelectedTool() instead -- same dialog the (also existing,
        but otherwise unreachable in the UI) Renumber action opens."""
        source_index = self.proxy_model.mapToSource(index)
        col_key = self.tool_model.visibleColumns()[source_index.column()]
        if col_key == 'T':
            self.renumberSelectedTool()

    def _onRowHeaderDoubleClicked(self, logical_row):
        """logical_row is already in view (proxy/sorted) row space -- same
        numbering QHeaderView uses for any row header, since rows (unlike
        columns) can't be drag-reordered independently of sort order."""
        self.selectRow(logical_row)
        self.renumberSelectedTool()

    def confirmAction(self, message):
        if not self._confirm_actions:
            return True
        box = QMessageBox.question(self, 'Confirm Action', message,
                                   QMessageBox.StandardButton.Yes,
                                   QMessageBox.StandardButton.No)
        return box == QMessageBox.StandardButton.Yes

    # Explicit setFoo()/foo() pairs alongside each @Property below: uic-
    # generated setupUi() code calls the conventional Qt Designer accessor
    # names directly (e.g. self.tooltable.setConfirmActions(True)), not the
    # Python property descriptor -- confirmed by compiling a scratch .ui
    # with these properties set and finding AttributeError without these.
    # (The stock qtpyvcp ToolTable widget has the same @Property-only gap;
    # it's just never been exercised because no .ui sets those properties
    # on it today.)

    @Property(bool)
    def confirmActions(self):
        return self._confirm_actions

    @confirmActions.setter
    def confirmActions(self, confirm):
        self._confirm_actions = confirm

    def setConfirmActions(self, confirm):
        self._confirm_actions = confirm

    @Property(QColor)
    def currentToolColor(self):
        return self.tool_model.current_tool_color

    @currentToolColor.setter
    def currentToolColor(self, color):
        self.tool_model.current_tool_color = color

    def setCurrentToolColor(self, color):
        self.tool_model.current_tool_color = color

    @Property(QColor)
    def currentToolBackground(self):
        return self.tool_model.current_tool_bg or QColor()

    @currentToolBackground.setter
    def currentToolBackground(self, color):
        self.tool_model.current_tool_bg = color

    def setCurrentToolBackground(self, color):
        self.tool_model.current_tool_bg = color

    @Property(int)
    def currentRow(self):
        return self.selectedRow()

    @currentRow.setter
    def currentRow(self, row):
        self.selectRow(row)

    def setCurrentRow(self, row):
        self.selectRow(row)

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
                               STRICT_ENUM_OPTIONS, OPEN_VOCAB_SEED_OPTIONS)
from .add_column_dialog import AddColumnDialog

LOG = getLogger(__name__)

GROUP_LABELS = {'core': 'Core', 'extras': 'Lathe Extras', 'custom': 'Custom'}


class LatheItemDelegate(QStyledItemDelegate):

    def __init__(self, model):
        super(LatheItemDelegate, self).__init__()
        self._model = model
        self._padding = ' ' * 2

    def displayText(self, value, locale):
        if isinstance(value, float):
            return f"{value:.4f}"
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
            editor.addItems(STRICT_ENUM_OPTIONS[key])
            self._popOpenOnceShown(editor)
            return editor

        if key in OPEN_VOCAB_SEED_OPTIONS:
            # Open vocabulary in practice (mixes ISO letters with descriptive
            # codes depending on tool type) -- editable combo seeded with a
            # baseline list plus whatever this shop's own data already uses,
            # so picking a value already in use is one click, not retyping.
            editor = QComboBox(parent)
            editor.setFrame(False)
            editor.setEditable(True)
            seen = set()
            for value in OPEN_VOCAB_SEED_OPTIONS[key] + self._model.distinctColumnValues(key):
                if value and value not in seen:
                    seen.add(value)
                    editor.addItem(value)
            self._popOpenOnceShown(editor)
            return editor

        if key == 'R' or key in TEXT_EXTRAS or group == 'custom':
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

    @staticmethod
    def _popOpenOnceShown(combo):
        """Open the dropdown the instant the editor appears, instead of
        requiring a second tap on the (tiny, easy-to-miss on a touchscreen)
        arrow button after the first double-click/tap creates it."""
        QTimer.singleShot(0, combo.showPopup)


class LatheToolTable(QTableView):
    toolSelected = Signal(int)

    def __init__(self, parent=None):
        super(LatheToolTable, self).__init__(parent)

        self.clicked.connect(self.onClick)

        self.tool_model = LatheToolModel(self)

        if not IN_DESIGNER:
            self.tool_model.tt.tool_table_changed.connect(self._onToolTableChanged)

        self.item_delegate = LatheItemDelegate(self.tool_model)
        self.setItemDelegate(self.item_delegate)

        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setFilterKeyColumn(0)
        self.proxy_model.setSourceModel(self.tool_model)
        self.setModel(self.proxy_model)

        self._confirm_actions = False
        self._current_tool_color = QColor('sage')
        self._current_tool_bg = None

        self.setSortingEnabled(True)
        self.verticalHeader().hide()
        self.setAlternatingRowColors(True)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.setSelectionMode(QTableView.SingleSelection)
        self.setWordWrap(False)
        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)
        # Deliberately NOT setStretchLastSection(True): it forces the last
        # visible column to exactly fill whatever space remains after the
        # others take their content-sized width -- shrinking it *below*
        # its own content's needed width if the rest already fill the
        # viewport (e.g. a "Holder" column showing "GROOVE EXTERNAL" got
        # clipped this way). That directly fights ResizeToContents, so any
        # column can end up last as visibility toggles; none should be
        # arbitrarily squeezed. A wider table just gets a horizontal
        # scrollbar instead, which is what "size by content" implies.
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

        self.item_delegate = LatheItemDelegate(self.tool_model)
        self.setItemDelegate(self.item_delegate)

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
            self.item_delegate = LatheItemDelegate(self.tool_model)
            self.setItemDelegate(self.item_delegate)

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
        self.item_delegate = LatheItemDelegate(self.tool_model)
        self.setItemDelegate(self.item_delegate)

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

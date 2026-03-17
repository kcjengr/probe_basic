from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtGui import QStandardItemModel
from PySide6.QtWidgets import QTableView, QStyledItemDelegate

from qtpyvcp.utilities import logger

from qtpyvcp.ops.drill_ops import DrillOps
from .drill_widget import DrillWidgetBase
from .float_line_edit import FloatLineEdit
from .base_widget import _is_qt_valid


LOG = logger.getLogger(__name__)


class XYCoordItemDelegate(QStyledItemDelegate):
    def __init__(self):
        super(XYCoordItemDelegate, self).__init__()

    def displayText(self, value, locale):
        try:
            return "{0:.3f}".format(float(value))
        except ValueError:
            return "0.000"

    def createEditor(self, parent, option, index):
        editor = FloatLineEdit(parent)
        editor.setFrame(False)
        editor.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        return editor


class XYCoordModel(QStandardItemModel):
    def __init__(self, holes):
        super(XYCoordModel, self).__init__()
        self._holes = holes
        self._column_names = ['X', 'Y']
        self.setRowCount(100)
        self.setColumnCount(2)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._column_names[section]

        return QStandardItemModel.headerData(self, section, orientation, role)

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def data(self, index, role=Qt.DisplayRole):
        if (role == Qt.DisplayRole or role == Qt.EditRole) and index.row() < len(self._holes):
            return self._holes[index.row()][index.column()]
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignVCenter | Qt.AlignRight

        return QStandardItemModel.data(self, index, role)

    def setData(self, index, value, role):
        if index.row() == len(self._holes):
            self._holes.append([0, 0])
            if index.row() == self.rowCount() - 1:
                self.insertRow(len(self._holes))
        if index.row() < len(self._holes):
            self._holes[index.row()][index.column()] = float(value)

        return True

    def deleteRow(self, position):
        if position < len(self._holes):
            self.beginRemoveRows(QModelIndex(), position, position)
            del self._holes[position]
            self.endRemoveRows()
            self.insertRows(len(self._holes), 1, QModelIndex())
            return True
        else:
            return False

    def deleteAll(self):
        remove_count = len(self._holes)
        if remove_count > 0:
            self.beginRemoveRows(QModelIndex(), 0, remove_count - 1)
            del self._holes[:]
            self.endRemoveRows()
            self.insertRows(0, remove_count, QModelIndex())
            return True
        else:
            return False


class XYCoordWidget(DrillWidgetBase):
    def __init__(self, parent=None):
        super(XYCoordWidget, self).__init__(parent, 'xy_coord.ui')

        self.drill_op = DrillOps()
        self.xy_coord_input.setModel(XYCoordModel(self.drill_op.holes))
        self.xy_coord_input.setItemDelegate(XYCoordItemDelegate())
        self.xy_coord_input.setAlternatingRowColors(True)
        self.xy_coord_input.setSelectionBehavior(QTableView.SelectRows)
        self.xy_coord_input.setSelectionMode(QTableView.SingleSelection)

        self.delete_all_input.clicked.connect(self.deleteAll)
        self.delete_selected_input.clicked.connect(self.deleteSelected)

    def _resolve_xy_coord_table(self):
        table = getattr(self, 'xy_coord_input', None)
        if not _is_qt_valid(table) and hasattr(self, 'findChild'):
            table = self.findChild(QTableView, 'xy_coord_input')

        if _is_qt_valid(table):
            self.xy_coord_input = table
            return table

        return None

    def create_op(self):
        d = self.drill_op
        self._set_common_fields(d)
        d.retract_mode = self.retract_mode()

        if self.drill_type() == 'PECK':
            op = d.peck(self.drill_peck_depth())
        elif self.drill_type() == 'DWELL':
            op = d.dwell(self.drill_dwell_time())
        elif self.drill_type() == 'BREAK':
            op = d.chip_break(self.drill_break_depth())
        elif self.drill_type() == 'TAP':
            op = d.tap(self.tap_pitch())
        elif self.drill_type() == 'RIGID TAP':
            op = d.rigid_tap(self.tap_pitch())
        elif self.drill_type() == 'MANUAL':
            op = d.manual()
        else:
            op = d.drill()

        return op

    def deleteSelected(self):
        table = self._resolve_xy_coord_table()
        if table is None:
            LOG.debug("deleteSelected skipped: xy_coord_input not available")
            return

        try:
            selection_model = table.selectionModel()
            model = table.model()
            if not _is_qt_valid(selection_model) or not _is_qt_valid(model):
                return

            selected_indexes = selection_model.selectedIndexes()
            if selected_indexes:
                for i in selected_indexes:
                    if i.column() == 1:
                        model.deleteRow(i.row())
            else:
                current = table.currentIndex()
                if current.isValid():
                    model.deleteRow(current.row())

            table.setFocus()
        except RuntimeError:
            return

    def deleteAll(self):
        table = self._resolve_xy_coord_table()
        if table is None:
            LOG.debug("deleteAll skipped: xy_coord_input not available")
            return

        if len(self.drill_op.holes) > 0:
            if self._confirm_action('Delete All', 'Are you sure you want to delete all coordinates?'):
                try:
                    model = table.model()
                    if not _is_qt_valid(model):
                        return
                    model.deleteAll()
                    table.selectRow(0)
                    table.setFocus()
                except RuntimeError:
                    return

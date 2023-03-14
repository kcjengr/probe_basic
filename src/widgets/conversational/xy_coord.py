from qtpy.QtCore import Qt, QModelIndex
from qtpy.QtGui import QStandardItemModel
from qtpy.QtWidgets import QTableView, QStyledItemDelegate

from qtpyvcp.ops.drill_ops import DrillOps
from .drill_widget import DrillWidgetBase
from .float_line_edit import FloatLineEdit


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
        for i in self.xy_coord_input.selectionModel().selectedIndexes():
            if i.column() == 1:
                self.xy_coord_input.model().deleteRow(i.row())
        self.xy_coord_input.setFocus()

    def deleteAll(self):
        if len(self.drill_op.holes) > 0:
            if self._confirm_action('Delete All', 'Are you sure you want to delete all coordinates?'):
                self.xy_coord_input.model().deleteAll()
                self.xy_coord_input.selectRow(0)
                self.xy_coord_input.setFocus()

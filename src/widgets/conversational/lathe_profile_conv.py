import os
import json

from qtpy.QtCore import Qt, QModelIndex, QUrl, Signal, Slot, QObject, QItemSelectionModel
from qtpy.QtGui import QStandardItemModel
from qtpy.QtWidgets import QWidget, QTableView, QStyledItemDelegate, QDoubleSpinBox
from qtpy.QtQuickWidgets import QQuickWidget


WIDGET_PATH = os.path.dirname(os.path.abspath(__file__))

class LatheProfileConvItemDelegate(QStyledItemDelegate):

    def __init__(self):
        super(LatheProfileConvItemDelegate, self).__init__()

    def displayText(self, value, locale):
        try:
            return "{0:.3f}".format(float(value))
        except ValueError:
            return "0.000"

    def createEditor(self, parent, option, index):
        editor = QDoubleSpinBox(parent)
        
        editor.setMinimum(-9999)
        editor.setMaximum(9999)
        
        editor.setFrame(False)
        editor.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        return editor
    

class LatheProfileConvModel(QStandardItemModel):
    
    editCompleted = Signal(dict)
    
    def __init__(self,):
        super(LatheProfileConvModel, self).__init__()
        
        self._data  = {}
        self._segments = [[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        
        self._column_names = ['X', 'Z', 'R']
        
        self.setRowCount(6)
        self.setColumnCount(3)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._column_names[section]

        return QStandardItemModel.headerData(self, section, orientation, role)

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def data(self, index, role=Qt.DisplayRole):
        if (role == Qt.DisplayRole or role == Qt.EditRole) and index.row() < len(self._segments):
            return self._segments[index.row()][index.column()]
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignVCenter | Qt.AlignRight

        return QStandardItemModel.data(self, index, role)

    def setData(self, index, value, role):
        
        if index.row() == len(self._segments):
            self._segments.append([0, 0])
            if index.row() == self.rowCount() - 1:
                self.insertRow(len(self._segments))
        if index.row() < len(self._segments):
            self._segments[index.row()][index.column()] = float(value)
        

        for data_column, data_row in enumerate(self._segments):
            self._data[data_column] =  data_row
                    
        self.editCompleted.emit(self._data )
        
        return True

    def deleteRow(self, position):
        if position < len(self._segments):
            self.beginRemoveRows(QModelIndex(), position, position)
            del self._segments[position]
            self.endRemoveRows()
            self.insertRows(len(self._segments), 1, QModelIndex())
            return True
        else:
            return False
        

    

    def deleteAll(self):
        remove_count = len(self._segments)
        if remove_count > 0:
            self.beginRemoveRows(QModelIndex(), 0, remove_count - 1)
            del self._segments[:]
            self.endRemoveRows()
            self.insertRows(0, remove_count, QModelIndex())
            return True
        else:
            return False


class LatheProfileConvWidget(QTableView):
    dataChangedSignal = Signal(dict)
    
    
    
    def __init__(self, parent=None):
        super(LatheProfileConvWidget, self).__init__(parent)


        self._lathe_profile_conv_item_delegate = LatheProfileConvItemDelegate()
        self._lathe_profile_conv_model = LatheProfileConvModel()
        
        self.setModel(self._lathe_profile_conv_model)
        self.setItemDelegate(self._lathe_profile_conv_item_delegate)
        self.setAlternatingRowColors(True)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.setSelectionMode(QTableView.SingleSelection)
        
        self._lathe_profile_conv_model.editCompleted.connect(self.onDataChanged)

        #  self._lathe_profile_conv_table.show()
        # self.delete_all_input.clicked.connect(self.deleteAll)
        # self.delete_selected_input.clicked.connect(self.deleteSelected)
        
        
    @Slot(dict)
    def onDataChanged(self, data):
        # print("Table data changed:", data)
        self.dataChangedSignal.emit(data)
    
    @Slot()
    def deleteSelected(self):
        for i in self.selectionModel().selectedIndexes():
            if i.column() == 1:
                self.model().deleteRow(i.row())
                
        self.setFocus()

    @Slot()
    def deleteAll(self):
        if len(self.drill_op.holes) > 0:
            if self._confirm_action('Delete All', 'Are you sure you want to delete all coordinates?'):
                self.model().deleteAll()
                self.selectRow(0)
                self.setFocus()

    
    @Slot()
    def addRow(self):
        """Insert a new empty row next to the selected row or at the end of the model."""
        indexes = self.selectionModel().selectedIndexes()
    
        # If no rows are selected, insert the new row at the bottom
        if not indexes:
            current_row_count = self.model().rowCount()
            self.model().insertRows(current_row_count, 1)
            new_index = self.model().index(current_row_count, 0)  # Get the index of the newly added row
        else:
            # Get the first selected index (assuming only one for simplicity)
            selected_index = indexes[0]
            
            # Insert a new row next to the selected row
            row = selected_index.row() + 1  # Get the row just after the current selection
            self.model().insertRows(row, 1)
            new_index = self.model().index(row, 0)  # Get the index of the newly added row
        
        self.setCurrentIndex(new_index)
        
    
class LatheProfileConvQML(QQuickWidget):

    segmentsSig = Signal(str, arguments=['data'])

    def __init__(self, parent=None):
        super(LatheProfileConvQML, self).__init__(parent) 
        
        self.engine().rootContext().setContextProperty("handler", self)
        url = QUrl.fromLocalFile(os.path.join(WIDGET_PATH, "lathe_profile_conv.qml"))
        self.setSource(url)

    @Slot(dict)
    def update(self, values):
        json_data = json.dumps(values)
        self.segmentsSig.emit(json_data)



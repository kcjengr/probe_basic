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
        
        editor.setMinimum(-9999.0)
        editor.setMaximum(9999.0)
        
        editor.setFrame(False)
        editor.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        return editor
    

class LatheProfileConvModel(QStandardItemModel):
    
    editCompleted = Signal(dict)
    
    def __init__(self, parent=None):
        super(LatheProfileConvModel, self).__init__(parent)
        
        self._data  = {}
        self._empty_row = [0.0] * 3
        self._column_names = ['X', 'Z', 'R']
        
#        self.setRowCount(1)
        self.setColumnCount(3)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._column_names[section]

        return QStandardItemModel.headerData(self, section, orientation, role)

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def data(self, index, role=Qt.DisplayRole):
        if (role == Qt.DisplayRole or role == Qt.EditRole) and index.row() < len(self._data):
            return self._data[index.row()][index.column()]
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignVCenter | Qt.AlignRight

        return QStandardItemModel.data(self, index, role)

    def setData(self, index, value, role):
        
        self._data[index.row()][index.column()] = float(value)
        self.editCompleted.emit(self._data)
        
        return True


    def addRow(self, indexes):
    
        current_row_count = self.rowCount()
        
        # If no rows are selected, insert the new row at the bottom
        if not indexes:
            #current_row_count = self.rowCount()
            
            self.beginInsertRows(QModelIndex(), current_row_count, 0)
            
            self._data[current_row_count] = self._empty_row.copy()
            self.setRowCount(current_row_count+1)
            self.endInsertRows()
            
            new_index = self.index(current_row_count, 0)  # Get the index of the newly added row
        else:
            # Get the first selected index (assuming only one for simplicity)
            selected_index = indexes[0].row()
            
            self.beginInsertRows(indexes[0], selected_index, selected_index)

            self._data[selected_index+1] =  self._empty_row.copy()
            self.setRowCount(current_row_count+1)
            self.endInsertRows()
            
            new_index =  self.index(selected_index+1, 0)
            
        return new_index


    def deleteRow(self, position):
        if position < len(self._data):
            self.beginRemoveRows(QModelIndex(), position, position)
            del self._data[position]
            self.endRemoveRows()
            # self.insertRows(len(self._data), 1, QModelIndex())
            return True
        else:
            return False
        

    

    def deleteAll(self):
        remove_count = len(self._data)
        if remove_count > 0:
            self.beginRemoveRows(QModelIndex(), 0, remove_count - 1)
            del self._data[:]
            self.endRemoveRows()
            # self.insertRows(0, remove_count, QModelIndex())
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
        print("Table data changed:", data)
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
        indexes = self.selectionModel().selectedIndexes()
        new_index = self._lathe_profile_conv_model.addRow(indexes)
        
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
        print(values)
        json_data = json.dumps(values)
        self.segmentsSig.emit(json_data)

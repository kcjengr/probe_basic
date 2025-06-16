import os
import json
import csv
import tempfile
import time

from io import StringIO

from qtpy.QtCore import Qt, QModelIndex, QUrl, Signal, Slot, QObject, QItemSelectionModel, QTimer, QEvent
from qtpy.QtGui import QStandardItemModel, QKeyEvent, QColor, QMouseEvent
from qtpy.QtWidgets import QWidget, QTableView, QStyledItemDelegate, QLineEdit
from qtpy.QtQuickWidgets import QQuickWidget


WIDGET_PATH = os.path.dirname(os.path.abspath(__file__))

class LatheProfileConvItemDelegate(QStyledItemDelegate):

    def __init__(self):
        super(LatheProfileConvItemDelegate, self).__init__()

    def displayText(self, value, locale):
        # Keep empty cells as empty, don't convert to "0.0000"
        if value == '' or value is None:
            return ''
        try:
            return "{0:.4f}".format(float(value))
        except (ValueError, TypeError):
            return ''

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setFrame(False)
        editor.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        return editor

    def setEditorData(self, editor, index):
        """Set data and prevent auto-selection"""
        value = index.model().data(index, Qt.EditRole)
        text = str(value) if value is not None else ''
        editor.setText(text)
        # Position cursor at end instead of selecting all
        editor.setCursorPosition(len(text))

    def setModelData(self, editor, model, index):
        """Handle empty text properly"""
        text = editor.text().strip()
        model.setData(index, text, Qt.EditRole)

class LatheProfileConvModel(QStandardItemModel):
    
    editCompleted = Signal(dict)
    
    def __init__(self, parent=None):
        super(LatheProfileConvModel, self).__init__(parent)
        
        self._data  = {}
        self._empty_row = [''] * 3
        self._column_names = ['X', 'Z', 'R']
        self._max_display_rows = 50
        self._active_rows = set()  # Track which rows have been used
        self._active_rows.add(0)  # Always show first row number
        
        self.setColumnCount(3)
        self.setRowCount(self._max_display_rows)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._column_names[section]
            elif orientation == Qt.Vertical:
                # Always show first row, then only active rows
                if section == 0 or section in self._active_rows:
                    return str(section + 1)
                else:
                    return ""
        elif role == Qt.BackgroundRole and orientation == Qt.Vertical:
            # Different background for active vs inactive row headers
            if section == 0 or section in self._active_rows:
                return QColor(114, 121, 242)  # for active rows
            else:
                return QColor(240, 240, 240)  # Light gray for inactive rows

        return QStandardItemModel.headerData(self, section, orientation, role)

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            if index.row() in self._data:
                return self._data[index.row()][index.column()]
            else:
                return ''
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignVCenter | Qt.AlignRight
        # Remove custom background role to let stylesheet handle alternating colors

        return QStandardItemModel.data(self, index, role)

    def setData(self, index, value, role):
        # Ensure the row exists in our data structure
        if index.row() not in self._data:
            self._data[index.row()] = self._empty_row.copy()
        
        self._data[index.row()][index.column()] = value
        
        # Mark this row as active if it has any content
        if value and str(value).strip():
            self._active_rows.add(index.row())
        else:
            # Check if row still has content in other columns
            row_has_content = False
            for col in range(3):
                if (index.row() in self._data and 
                    self._data[index.row()][col] and 
                    str(self._data[index.row()][col]).strip()):
                    row_has_content = True
                    break
            
            # Don't remove row 0 from active rows (always keep it visible)
            if not row_has_content and index.row() != 0:
                self._active_rows.discard(index.row())
        
        # Update header display
        self.headerDataChanged.emit(Qt.Vertical, index.row(), index.row())
        
        self.editCompleted.emit(self._data)
        
        return True

    def addRow(self, indexes):
        """Add a new row by finding the next available row"""
        try:
            # Find the next available row
            next_row = 0
            while next_row < self._max_display_rows and next_row in self._active_rows:
                next_row += 1
            
            if next_row >= self._max_display_rows:
                # Find the highest active row and use the next one
                if self._active_rows:
                    next_row = max(self._active_rows) + 1
                else:
                    next_row = 0
                    
                if next_row >= self._max_display_rows:
                    print(f"Maximum of {self._max_display_rows} rows reached")
                    return QModelIndex()
            
            # Initialize the row data
            if next_row not in self._data:
                self._data[next_row] = self._empty_row.copy()
            
            # Mark as active and update header
            self._active_rows.add(next_row)
            self.headerDataChanged.emit(Qt.Vertical, next_row, next_row)
            
            self.editCompleted.emit(self._data)
            
            return self.index(next_row, 0)
                
        except Exception as e:
            print(f"Error in addRow: {e}")
            return QModelIndex()

    def deleteRow(self, position):
        if position < self._max_display_rows and position in self._data:
            # Clear the row data
            self._data[position] = self._empty_row.copy()
            # Remove from active rows (but keep row 0 always active)
            if position != 0:
                self._active_rows.discard(position)
            # Update header
            self.headerDataChanged.emit(Qt.Vertical, position, position)
            self.editCompleted.emit(self._data)
            return True
        else:
            return False

    def deleteAll(self):
        # Clear all data
        self._data.clear()
        self._active_rows.clear()
        self._active_rows.add(0)  # Keep first row always visible
        # Update all headers
        self.headerDataChanged.emit(Qt.Vertical, 0, self._max_display_rows - 1)
        self.editCompleted.emit(self._data)
        return True

class LatheProfileConvWidget(QTableView):
    dataChangedSignal = Signal(dict)
    selectedRowSignal = Signal(int)
    
    exportCSVSignal = Signal(str, arguments=['csv_file'])
    
    def __init__(self, parent=None):
        super(LatheProfileConvWidget, self).__init__(parent)

        self._lathe_profile_conv_item_delegate = LatheProfileConvItemDelegate()
        self._lathe_profile_conv_model = LatheProfileConvModel()
        
        self.setModel(self._lathe_profile_conv_model)
        self.setItemDelegate(self._lathe_profile_conv_item_delegate)
        
        # Keep existing stylesheet styling - restore alternating colors
        self.setAlternatingRowColors(True)  # Let stylesheet handle alternating colors
        self.setGridStyle(Qt.SolidLine)
        self.setShowGrid(True)
        self.setSelectionBehavior(QTableView.SelectRows);
        # self.setSelectionBehavior(QTableView.SelectItems)
        # self.setSelectionMode(QTableView.SingleSelection) 
        
        # Style the headers
        self.verticalHeader().setDefaultSectionSize(25)
        self.verticalHeader().setMinimumSectionSize(25)
        self.horizontalHeader().setStretchLastSection(True)
        
        # Control edit triggers
        self.setEditTriggers(QTableView.DoubleClicked | QTableView.EditKeyPressed | QTableView.AnyKeyPressed)
        
        self._lathe_profile_conv_model.editCompleted.connect(self.onDataChanged)
        self._last_data_length = 0
        
        
        self.selectionModel().selectionChanged.connect(self.onSelectionChanged)
        
    
    @Slot(result=str)
    def exportToCSV(self):
        """Export table data to CSV file in /tmp and return file path"""
        try:
            # Generate timestamped filename
            # timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"lathe_profile_save.csv"
            filepath = os.path.join(tempfile.gettempdir(), filename)
            
            with open(filepath, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                
                # Write headers
                writer.writerow(['Row', 'X', 'Z', 'R'])
                
                # Write data rows
                for row in sorted(self._lathe_profile_conv_model._data.keys()):
                    row_data = self._lathe_profile_conv_model._data[row]
                    if any(cell != '' and cell is not None for cell in row_data):
                        writer.writerow([row + 1] + row_data)  # +1 to match displayed row numbers
            
            print(f"CSV saved to: {filepath}")
            return filepath
            
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return ""
        
    @Slot(result=bool)
    def loadFromCSV(self):
        """Load table data from CSV file in /tmp"""
        try:
            self._lathe_profile_conv_model.deleteAll()  # Clear existing data
            
            filename = "lathe_profile_save.csv"
            filepath = os.path.join(tempfile.gettempdir(), filename)
            
            if not os.path.exists(filepath):
                print(f"CSV file not found: {filepath}")
                return False
                
            with open(filepath, 'r') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip header row
                
                for row_idx, row in enumerate(reader):
                    if len(row) >= 4:  # Row, X, Z, R columns
                        try:
                            # Convert displayed row number (1-based) to model index (0-based)
                            model_row = int(row[0]) - 1
                            x_val = row[1].strip()
                            z_val = row[2].strip()
                            r_val = row[3].strip()
                            
                            # Set data in model
                            if model_row >= 0 and model_row < self._lathe_profile_conv_model._max_display_rows:
                                index_x = self._lathe_profile_conv_model.index(model_row, 0)
                                index_z = self._lathe_profile_conv_model.index(model_row, 1)
                                index_r = self._lathe_profile_conv_model.index(model_row, 2)
                                
                                self._lathe_profile_conv_model.setData(index_x, x_val, Qt.EditRole)
                                self._lathe_profile_conv_model.setData(index_z, z_val, Qt.EditRole)
                                self._lathe_profile_conv_model.setData(index_r, r_val, Qt.EditRole)
                                
                        except (ValueError, IndexError) as e:
                            print(f"Skipping malformed row {row_idx}: {e}")
                            
            print("CSV data loaded successfully")
            return True
            
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return False

    def onSelectionChanged(self, selected, deselected):
        """Handle selection changes and emit the current row"""
        current_index = self.currentIndex()
        if current_index.isValid():
            self.selectedRowSignal.emit(current_index.row())
    
    def mousePressEvent(self, e: QMouseEvent) -> None:
        """Handle mouse clicks and ensure selection is emitted"""
        current_index = self.currentIndex()
        if current_index.isValid():
            self.selectedRowSignal.emit(current_index.row())

        super().mousePressEvent(e)
        
    def moveCursor(self, cursorAction, modifiers):
        """Override to handle tab navigation and new row creation"""
        current_index = self.currentIndex()
        
        self.selectedRowSignal.emit(current_index.row())
        
        # Handle Tab key (MoveNext) behavior
        if cursorAction == QTableView.MoveNext:
            print(f"Tab navigation from row={current_index.row()}, col={current_index.column()}")
            
            
            # If we're in the last column (R column, index 2)
            if current_index.isValid() and current_index.column() == 2:
                print("In last column - creating new row...")
                # Add new row and move to first column of new row
                new_index = self._lathe_profile_conv_model.addRow([])
                if new_index.isValid():
                    print(f"New row created at row={new_index.row()}")
                    return new_index
                else:
                    print("Failed to create new row")
                    return current_index
        
        # Use default behavior for all other cursor movements
        return super(LatheProfileConvWidget, self).moveCursor(cursorAction, modifiers)

    def keyPressEvent(self, event):
        try:
            # Clear current cell with Delete key
            if event.key() == Qt.Key_Delete:
                current_index = self.currentIndex()
                if current_index.isValid():
                    self._lathe_profile_conv_model.setData(current_index, '', Qt.EditRole)
                    print(f"Cleared cell at row={current_index.row()}, col={current_index.column()}")
                return
                
            # Insert new row with Insert key
            elif event.key() == Qt.Key_Insert:
                self.addRow()
                print("Insert key - added new row")
                return
            
            # Let parent handle all other keys (including Tab, Return, etc.)
            super(LatheProfileConvWidget, self).keyPressEvent(event)
            
        except Exception as e:
            print(f"Error in keyPressEvent: {e}")
            import traceback
            traceback.print_exc()
        super(LatheProfileConvWidget, self).keyPressEvent(event)
    
    @Slot(dict)
    def onDataChanged(self, data):
        # Only emit data for rows that have content
        filtered_data = {}
        for row_index, row_data in data.items():
            if any(cell != '' and cell is not None for cell in row_data):
                filtered_data[row_index] = row_data
        
        if len(filtered_data) != self._last_data_length:
            print(f"Active rows changed: {len(filtered_data)} rows with data")
            self._last_data_length = len(filtered_data)
        
        print(f"Data changed: {filtered_data}")
        self.dataChangedSignal.emit(filtered_data)
    
    @Slot()
    def addRow(self):
        new_index = self._lathe_profile_conv_model.addRow([])
        if new_index.isValid():
            self.setCurrentIndex(new_index)

    @Slot()
    def deleteRow(self):
        current_index = self.currentIndex()
        if current_index.isValid():
            self._lathe_profile_conv_model.deleteRow(current_index.row())
    
    @Slot()
    def deleteAll(self):
        self._lathe_profile_conv_model.deleteAll()
        self.dataChangedSignal.emit({})

class LatheProfileConvQML(QQuickWidget):

    segmentsSig = Signal(str, arguments=['data'])
    selectedSig = Signal(int, arguments=['index'])
    clickedSig = Signal(int, arguments=['index'])

    def __init__(self, parent=None):
        super(LatheProfileConvQML, self).__init__(parent) 
        
        self.engine().rootContext().setContextProperty("handler", self)
        url = QUrl.fromLocalFile(os.path.join(WIDGET_PATH, "lathe_profile_conv.qml"))
        self.setSource(url)


    @Slot(int)
    def selected(self, value):
        print(f"Emitting Table Event INT: {value}")
        self.selectedSig.emit(value)

    @Slot(int)
    def clicked(self, value):
        print(f"Emitting Plot Event INT: {value}")
        self.clickedSig.emit(value)
        
    @Slot(dict)
    def update(self, values):
        try:
            print("VALUES received in QML handler:")
            print(values)
            
            # Process inheritance in a single pass
            processed_values = self.processInheritance(values)
            
            print("Processed values for plotting:")
            print(processed_values)
            
            json_data = json.dumps(processed_values)
            print(f"Emitting JSON: {json_data}")
            self.segmentsSig.emit(json_data)
            
        except Exception as e:
            print(f"Error in update method: {e}")
            import traceback
            traceback.print_exc()

    def processInheritance(self, values):
        """Process inheritance logic for empty cells"""
        processed = {}
        
        for row_index in sorted(values.keys()):
            row_data = values[row_index]
            processed[row_index] = row_data.copy() if row_data else ['', '', '']
            
            if row_data:
                for col_index, cell_value in enumerate(row_data):
                    if cell_value == '' or cell_value is None:
                        print(f"Found empty cell at row {row_index}, col {col_index}")
                        
                        # Special handling for R column (index 2)
                        if col_index == 2:  # R column
                            print(f"R column empty at row {row_index} - setting to 0")
                            processed[row_index][col_index] = '0'
                        else:
                            # X and Z columns inherit from previous rows
                            inherited_value = self.findInheritedValue(processed, row_index, col_index)
                            if inherited_value:
                                print(f"Inheriting value for row {row_index}, col {col_index}: {inherited_value}")
                                processed[row_index][col_index] = inherited_value
        
        return processed

    def findInheritedValue(self, processed_data, current_row, column):
        """Find the nearest non-empty value in the same column from previous rows"""
        for prev_row in range(current_row - 1, -1, -1):
            if prev_row in processed_data:
                prev_row_data = processed_data[prev_row]
                if (prev_row_data and column < len(prev_row_data) and 
                    prev_row_data[column] != '' and prev_row_data[column] is not None):
                    return prev_row_data[column]
        return None

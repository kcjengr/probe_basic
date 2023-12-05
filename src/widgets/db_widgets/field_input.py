"""
Tool DB Field Widget
---------
"""

from qtpy.QtCore import Slot, Property
from qtpy.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QPushButton, QFileDialog, QDialog, QLabel


from db_tool.base import Session, Base, engine
from db_tool.tool_table import ProbeParams, Tool, ToolTable

from qtpyvcp.utilities.logger import getLogger
from qtpyvcp.widgets.base_widgets.base_widget import VCPWidget

LOG = getLogger(__name__)


class DBInputWidget(QWidget):
    """Tool DB Field Widget"""

    def __init__(self, parent=None):
        super(DBInputWidget, self).__init__(parent)
        
        self.session = Session()
        
        self._name = ""
        self._type = ""
        self._text = ""
        self._desc = ""
        self._db_path = ""
        
        self.tool_selected = None
        
        self.layout = QHBoxLayout(self)
        self.value = 0.0
        
        self.label = QLabel()
        self.value_input = QLineEdit()
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.value_input)
    
    ##############################################
    # PROPERTIES
    ##############################################
    
    @Property(str)
    def field_name(self):
        return self._name

    @field_name.setter
    def field_name(self, value):
        self._name = value     
    
    ##############################################
      
    @Property(str)
    def field_type(self):
        return self._type

    @field_type.setter
    def field_type(self, value):
        self._type = value
    
    ##############################################
        
    @Property(str)
    def field_label_text(self):
        return self._text

    @field_label_text.setter
    def field_label_text(self, value):
        self._text = value
        self.label.setText(self._text)
    
    ##############################################
    
    @Property(str)
    def field_description(self):
        return self._desc

    @field_description.setter
    def field_description(self, value):
        self._desc = value
    
    ##############################################
    
    @Property(str)
    def field_db_path(self):
        return self._db_path

    @field_db_path.setter
    def field_db_path(self, value):
        self._db_path = value
    
    ##############################################
    # SLOTS
    ##############################################

    @Slot(int)
    def toolSelected(self, tool_no):
        self.tool_selected = tool_no
        
        tool_tables = self.session.query(ToolTable).all()
        
        for tool_table in tool_tables:
            for tool in tool_table.tools:
                if tool.tool_no == tool_no:
                    
                    print(tool)
                    
                    if (len(tool.probe_params) > 0) and (self._db_path != ""):
                        self.setValue(str(getattr(tool.probe_params[0], self._db_path)))
                    else:
                        print("NANAI")
                        self.clearValue()
    
    @Slot()
    def saveField(self):
        if self.tool_selected is not None:
            
            tool_tables = self.session.query(ToolTable).all()
            
            for tool_table in tool_tables:
                for tool in tool_table.tools:
                    if tool.tool_no == self.tool_selected:
                        
                        if (len(tool.probe_params) > 0) and (self._db_path != ""):
                            setattr(tool.probe_params[0], self._db_path, self.value_input.text())
                            self.session.commit()
                        else:
                            print("tool has no params yet")
        
    
    ##############################################
    # OTHER
    ##############################################
    
    def setValue(self, value):
        self.value = value
        self.value_input.setText(self.value)

    def clearValue(self):
        self.value = ""
        self.value_input.setText("")



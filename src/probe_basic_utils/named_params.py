from ruamel.yaml import YAML

from qtpy.QtCore import QObject
from qtpy.QtWidgets import QLineEdit, QPushButton, QCheckBox, QWidget

from qtpyvcp import hal as qhal
from pprint import pprint
from pyqtgraph.parametertree.parameterTypes import str


class NamedParams(QObject):
    
    def __init__(self, config, parent):
        super(NamedParams, self).__init__()
        
        
        self.config_file = config
        self.parent = parent
        self.widget_obj = dict()
        self.widget_param = dict()
        
        yaml=YAML(typ='safe')
        
        with open(self.config_file, "r") as cfg:
            self.named_params = yaml.load(cfg)
            
        self.comp = qhal.getComponent("probe_basic")
        
        for widget_name, widget in self.named_params.get("widget_named_params").items():
            if widget.get("enabled"):
                hal_name = widget.get("name")
                hal_type = widget.get("type")
                hal_access = widget.get("access")
                
                print(f"WIDGET Name : {hal_name}")
                print(f"\tType : {hal_type}")
                print(f"\taccess  : {hal_access}")
                
                self.widget_param[hal_name] = self.comp.addParam(hal_name, hal_type, hal_access)
                self.widget_obj[hal_name] = self.parent.findChildren(QWidget, widget_name)[0]
                
                if isinstance(self.widget_obj[hal_name], QPushButton):
                    self.widget_obj[hal_name].toggled.connect(self.onWidgetButtonToggled)
                    self.comp.addParamsListener(hal_name, self.onParamsButtonChanged)
                elif isinstance(self.widget_obj[hal_name], QLineEdit):
                    self.widget_obj[hal_name].textEdited.connect(self.onWidgetTextChanged)
                    self.comp.addParamsListener(hal_name, self.onParamsTextChanged)
                    
        pprint(self.widget_obj)
        pprint(self.widget_param)
        
    def onParamsButtonChanged(self, value):
        param = self.sender()
        self.widget_obj[param.name].setChecked(value)
        
    def onParamsTextChanged(self, text):
        param = self.sender()
        self.widget_obj[param.name].setText(f"{text}")
        
    def onWidgetButtonToggled(self, value):
        widget = self.sender()
        param_name = self.named_params.get("widget_named_params")[f"{widget.objectName()}"]["name"]
        self.widget_param[param_name].value = value
        
    def onWidgetTextChanged(self, value):
        widget = self.sender()
        param_name = self.named_params.get("widget_named_params")[f"{widget.objectName()}"]["name"]
        self.widget_param[param_name].value = value


        
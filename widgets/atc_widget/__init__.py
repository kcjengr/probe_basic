from qtpyvcp.widgets.qtdesigner import _DesignerPlugin

from atc import DynATC
class DynATC_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return DynATC
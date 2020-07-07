from qtpyvcp.widgets.qtdesigner import _DesignerPlugin

from linear_atc import LinearATC
class LinearATC_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return LinearATC
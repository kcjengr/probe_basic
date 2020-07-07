from qtpyvcp.widgets.qtdesigner import _DesignerPlugin

from linear_atc_widget.linear_atc import LinearATC
from atc_widget.atc import DynATC


class LinearATC_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return LinearATC


class DynATC_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return DynATC

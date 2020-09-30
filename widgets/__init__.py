from qtpyvcp.widgets.qtdesigner import _DesignerPlugin

from widgets.lathe_tool_touch_off.lathe_tool_touch_off import LatheToolTouchOff
from widgets.atc_widget.atc import DynATC


class LatheToolTouchOff_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return LatheToolTouchOff


class DynATC_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return DynATC

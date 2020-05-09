from qtpyvcp.widgets.qtdesigner import _DesignerPlugin

from lathe_tool_touch_off.lathe_tool_touch_off import LatheToolTouchOff
class LatheToolTouchOff_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return LatheToolTouchOff

from atc_widget.atc import DynATC
class DynATC_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return DynATC

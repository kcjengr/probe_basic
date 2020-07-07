from qtpyvcp.widgets.qtdesigner import _DesignerPlugin

from lathe_tool_touch_off import LatheToolTouchOff
class LatheToolTouchOff_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return LatheToolTouchOff
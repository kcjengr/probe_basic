from qtpyvcp.widgets.qtdesigner import _DesignerPlugin

from widgets.lathe_tool_touch_off.lathe_tool_touch_off import LatheToolTouchOff
from widgets.atc_widget.atc import DynATC
from widgets.rack_atc_widget.rack_atc import RackATC

from widgets.conversational.facing import FacingWidget
from widgets.conversational.xy_coord import XYCoordWidget
from widgets.conversational.hole_circle import HoleCircleWidget
from widgets.conversational.int_line_edit import IntLineEdit
from widgets.conversational.float_line_edit import FloatLineEdit

from widgets.conversational.lathe_profile_conv import LatheProfileConvWidget
from widgets.conversational.lathe_profile_conv import LatheProfileConvQML



class LatheToolTouchOff_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return LatheToolTouchOff


class DynATC_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return DynATC
    
class RackATC_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return RackATC


class FloatLineEditPlugin(_DesignerPlugin):
    def pluginClass(self):
        return FloatLineEdit


class IntLineEditPlugin(_DesignerPlugin):
    def pluginClass(self):
        return IntLineEdit


class HoleCircleWidgetPlugin(_DesignerPlugin):
    def pluginClass(self):
        return HoleCircleWidget


class XYCoordWidgetPlugin(_DesignerPlugin):
    def pluginClass(self):
        return XYCoordWidget


class FacingWidgetPlugin(_DesignerPlugin):
    def pluginClass(self):
        return FacingWidget

class LatheProfileConvWidgetPlugin(_DesignerPlugin):
    def pluginClass(self):
        return LatheProfileConvWidget
    
    
class LatheProfileConvQMLPlugin(_DesignerPlugin):
    def pluginClass(self):
        return LatheProfileConvQML
from qtpyvcp.widgets.qtdesigner import _DesignerPlugin

from widgets.db_widgets.field_input import DBInputWidget

from widgets.lathe_tool_touch_off.lathe_tool_touch_off import LatheToolTouchOff
from widgets.atc_widget.atc import DynATC

from widgets.conversational.facing import FacingWidget
from widgets.conversational.xy_coord import XYCoordWidget
from widgets.conversational.hole_circle import HoleCircleWidget
from widgets.conversational.int_line_edit import IntLineEdit
from widgets.conversational.float_line_edit import FloatLineEdit

class DBInputWidget_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return DBInputWidget

class LatheToolTouchOff_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return LatheToolTouchOff


class DynATC_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return DynATC


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

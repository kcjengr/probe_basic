import os as _os
from qtpyvcp.widgets.qtdesigner import _DesignerPlugin
from PySide6.QtWidgets import QWidget

# In Designer mode, ALWAYS use placeholder widgets.
# The real widgets (atc.py, rack_atc.py) load libGL via ctypes at module import
# time with RTLD_GLOBAL which corrupts Qt's own OpenGL loader → SIGSEGV.
_IN_DESIGNER = bool(_os.getenv('DESIGNER'))

if _IN_DESIGNER:
    # Designer mode: safe QWidget placeholders only — no GL, no linuxcnc
    from widgets.conversational.designer_plugins import (
        FacingWidget, XYCoordWidget, HoleCircleWidget
    )

    class LatheToolTouchOff(QWidget):
        def __init__(self, parent=None):
            super().__init__(parent)

    class DynATC(QWidget):
        def __init__(self, parent=None):
            super().__init__(parent)

    class RackATC(QWidget):
        def __init__(self, parent=None):
            super().__init__(parent)

    class IntLineEdit(QWidget):
        def __init__(self, parent=None):
            super().__init__(parent)

    class FloatLineEdit(QWidget):
        def __init__(self, parent=None):
            super().__init__(parent)

else:
    # Runtime: import the real widgets
    try:
        from widgets.lathe_tool_touch_off.lathe_tool_touch_off import LatheToolTouchOff
        from widgets.atc_widget.atc import DynATC
        from widgets.rack_atc_widget.rack_atc import RackATC
        from widgets.conversational.facing import FacingWidget
        from widgets.conversational.xy_coord import XYCoordWidget
        from widgets.conversational.hole_circle import HoleCircleWidget
        from widgets.conversational.int_line_edit import IntLineEdit
        from widgets.conversational.float_line_edit import FloatLineEdit
    except (ImportError, AttributeError) as e:
        print(f"Warning: could not import probe_basic widgets: {e}")



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

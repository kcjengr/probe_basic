"""Designer plugins for conversational widgets.

Tries to load real conversational widgets; falls back to lightweight placeholders
for Designer or when dependencies are missing.
"""

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from qtpyvcp.widgets.qtdesigner import _DesignerPlugin


def _placeholder(label_text: str):
    class _P(QWidget):
        def __init__(self, parent=None):
            super().__init__(parent)
            layout = QVBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)
            label = QLabel(label_text)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label)
            self.setLayout(layout)
            self.setMinimumSize(200, 150)
            self.setStyleSheet("background-color: #3a3a3a; color: #cccccc;")
    return _P


try:
    from .facing import FacingWidget  # type: ignore
except Exception:
    FacingWidget = _placeholder("Facing Widget\n(Conversational)")

try:
    from .hole_circle import HoleCircleWidget  # type: ignore
except Exception:
    HoleCircleWidget = _placeholder("Hole Circle Widget\n(Conversational)")

try:
    from .xy_coord import XYCoordWidget  # type: ignore
except Exception:
    XYCoordWidget = _placeholder("XY Coord Widget\n(Conversational)")


class FacingWidgetPlugin(_DesignerPlugin):
    def pluginClass(self):
        return FacingWidget
    
    def toolTip(self):
        return "Facing conversational widget"
    
    def isContainer(self):
        return False


class HoleCircleWidgetPlugin(_DesignerPlugin):
    def pluginClass(self):
        return HoleCircleWidget
    
    def toolTip(self):
        return "Hole circle conversational widget"
    
    def isContainer(self):
        return False


class XYCoordWidgetPlugin(_DesignerPlugin):
    def pluginClass(self):
        return XYCoordWidget
    
    def toolTip(self):
        return "XY coordinate conversational widget"
    
    def isContainer(self):
        return False

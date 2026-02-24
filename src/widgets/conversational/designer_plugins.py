"""Designer plugins for conversational widgets.

These provide simplified placeholder versions that don't require LinuxCNC to be running.
"""

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from qtpyvcp.widgets.qtdesigner import _DesignerPlugin


class FacingWidget(QWidget):
    """Placeholder for FacingWidget in Designer mode."""
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        label = QLabel("Facing Widget\n(Conversational)")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        self.setLayout(layout)
        self.setMinimumSize(200, 150)
        self.setStyleSheet("background-color: #3a3a3a; color: #cccccc;")

    def setFilePath(self, path):
        """Dummy method for UI connections."""
        pass


class HoleCircleWidget(QWidget):
    """Placeholder for HoleCircleWidget in Designer mode."""
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        label = QLabel("Hole Circle Widget\n(Conversational)")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        self.setLayout(layout)
        self.setMinimumSize(200, 150)
        self.setStyleSheet("background-color: #3a3a3a; color: #cccccc;")


class XYCoordWidget(QWidget):
    """Placeholder for XYCoordWidget in Designer mode."""
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        label = QLabel("XY Coord Widget\n(Conversational)")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        self.setLayout(layout)
        self.setMinimumSize(200, 150)
        self.setStyleSheet("background-color: #3a3a3a; color: #cccccc;")


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

import os
import linuxcnc

from PySide6.QtCore import Qt, QObject
from PySide6.QtWidgets import QWidget

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger
from qtpyvcp.utilities.runtime_ui_loader import load_ui as load_runtime_ui

LOG = logger.getLogger(__name__)

STATUS = getPlugin('status')
TOOL_TABLE = getPlugin('tooltable')

INI_FILE = linuxcnc.ini(os.getenv('INI_FILE_NAME'))

# Pre-import RackATC so PySide6's QUiLoader can find it as a custom widget.
from widgets.rack_atc_widget.rack_atc import RackATC  # noqa: F401


def _load_ui(ui_path, parent):
    return load_runtime_ui(ui_path, parent)


class RackAtc(QWidget):
    def __init__(self, parent=None):
        super(RackAtc, self).__init__(parent)
        ui_file = os.path.splitext(os.path.basename(__file__))[0] + ".ui"
        ui_path = os.path.join(os.path.dirname(__file__), ui_file)
        self.ui = _load_ui(ui_path, self)

        for child in self.ui.findChildren(QObject):
            name = child.objectName()
            if name and not hasattr(self, name):
                setattr(self, name, child)

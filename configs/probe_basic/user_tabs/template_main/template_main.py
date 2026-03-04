import os
import linuxcnc

from PySide6.QtCore import Qt, QFile
from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)

STATUS = getPlugin('status')
TOOL_TABLE = getPlugin('tooltable')

INI_FILE = linuxcnc.ini(os.getenv('INI_FILE_NAME'))


def _load_ui(ui_path, parent):
    ui_file = QFile(ui_path)
    if not ui_file.open(QFile.ReadOnly):
        raise RuntimeError(f"Unable to open UI file: {ui_path}")
    try:
        loader = QUiLoader()
        loaded = loader.load(ui_file, parent)
    finally:
        ui_file.close()
    if loaded is None:
        raise RuntimeError(f"Unable to load UI file: {ui_path}")
    return loaded


class UserTab(QWidget):
    def __init__(self, parent=None):
        super(UserTab, self).__init__(parent)
        ui_file = os.path.splitext(os.path.basename(__file__))[0] + ".ui"
        ui_path = os.path.join(os.path.dirname(__file__), ui_file)
        self.ui = _load_ui(ui_path, self)
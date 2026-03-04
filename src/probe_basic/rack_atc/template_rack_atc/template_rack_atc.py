import os
import linuxcnc

from PySide6.QtCore import Qt, QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)

STATUS = getPlugin('status')
TOOL_TABLE = getPlugin('tooltable')

INI_FILE = linuxcnc.ini(os.getenv('INI_FILE_NAME'))


class RackAtc(QWidget):
    def __init__(self, parent=None):
        super(RackAtc, self).__init__(parent)
        ui_file = os.path.splitext(os.path.basename(__file__))[0] + ".ui"
        ui_path = os.path.join(os.path.dirname(__file__), ui_file)
        ui_file_handle = QFile(ui_path)
        if not ui_file_handle.open(QFile.ReadOnly):
            raise RuntimeError(f"Unable to open UI file: {ui_path}")
        try:
            loader = QUiLoader()
            self.ui = loader.load(ui_file_handle, self)
        finally:
            ui_file_handle.close()
        if self.ui is None:
            raise RuntimeError(f"Unable to load UI file: {ui_path}")

import os
import sys
sys.path.insert(0, "/usr/lib/python3/dist-packages/probe_basic")
from probe_basic_rc import *
import linuxcnc

from PySide6.QtCore import Qt, QFile
from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)

# Detect if we're running in Qt Designer
IN_DESIGNER = os.getenv('DESIGNER', False)

# Defer plugin imports to avoid issues in designer
STATUS = None
TOOL_TABLE = None

def _get_status():
    global STATUS
    if STATUS is None:
        STATUS = getPlugin('status')
    return STATUS

def _get_tool_table():
    global TOOL_TABLE
    if TOOL_TABLE is None:
        TOOL_TABLE = getPlugin('tooltable')
    return TOOL_TABLE

INI_FILE = linuxcnc.ini(os.getenv('INI_FILE_NAME')) if not IN_DESIGNER else None


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


class UserDRO(QWidget):
    def __init__(self, parent=None):
        super(UserDRO, self).__init__(parent)
        ui_file = os.path.splitext(os.path.basename(__file__))[0] + ".ui"
        ui_path = os.path.join(os.path.dirname(__file__), ui_file)
        self.ui = _load_ui(ui_path, self)
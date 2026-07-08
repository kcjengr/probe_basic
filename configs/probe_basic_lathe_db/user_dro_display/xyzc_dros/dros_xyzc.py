import os
import sys
import probe_basic_lathe as _pb_lathe_pkg
sys.path.insert(0, os.path.dirname(os.path.abspath(_pb_lathe_pkg.__file__)))
from probe_basic_lathe_rc import *
import linuxcnc

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger
from qtpyvcp.utilities.runtime_ui_loader import load_ui as load_runtime_ui

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
    return load_runtime_ui(ui_path, parent)


class UserDRO(QWidget):
    def __init__(self, parent=None):
        super(UserDRO, self).__init__(parent)
        ui_file = os.path.splitext(os.path.basename(__file__))[0] + ".ui"
        ui_path = os.path.join(os.path.dirname(__file__), ui_file)
        self.ui = _load_ui(ui_path, self)
import os
import linuxcnc

from qtpy import uic
from qtpy.QtWidgets import QWidget

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)

STATUS = getPlugin('status')
TOOL_TABLE = getPlugin('tooltable')

INI_FILE = linuxcnc.ini(os.getenv('INI_FILE_NAME'))

# Pre-import DynATC so PySide6's QUiLoader can find it as a custom widget.
from widgets.atc_widget.atc import DynATC  # noqa: F401


class Atc(QWidget):
    def __init__(self, parent=None):
        super(Atc, self).__init__(parent)
        ui_file = os.path.splitext(os.path.basename(__file__))[0] + ".ui"
        uic.loadUi(os.path.join(os.path.dirname(__file__), ui_file), self)

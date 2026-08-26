import os
import linuxcnc

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger
from qtpyvcp.utilities.runtime_ui_loader import load_ui as load_runtime_ui

LOG = logger.getLogger(__name__)

STATUS = getPlugin('status')
TOOL_TABLE = getPlugin('tooltable')

INI_FILE = linuxcnc.ini(os.getenv('INI_FILE_NAME'))


def _load_ui(ui_path, parent):
    return load_runtime_ui(ui_path, parent)


def _adopt_ui_identity(widget, loaded_ui):
    """Copy the .ui root widget's name and dynamic properties onto widget.

    PySide6's QUiLoader nests a separate widget inside the parent it is given,
    unlike PyQt's uic.loadUi(path, baseinstance), which made baseinstance the
    root widget. probe_basic reads this tab's objectName (used as the tab
    label, underscores shown as spaces) and its "sidebar" property off the
    UserTab instance, so put them back where it looks for them.
    """
    widget.setObjectName(loaded_ui.objectName())
    for prop_name in loaded_ui.dynamicPropertyNames():
        key = bytes(prop_name).decode()
        if key.startswith("_"):
            continue  # PySide6 bookkeeping, e.g. _PySideInvalidatePtr
        try:
            widget.setProperty(key, loaded_ui.property(key))
        except RuntimeError as exc:
            LOG.warning(f"Could not copy user tab property '{key}': {exc}")


class UserTab(QWidget):
    def __init__(self, parent=None):
        super(UserTab, self).__init__(parent)
        ui_file = os.path.splitext(os.path.basename(__file__))[0] + ".ui"
        ui_path = os.path.join(os.path.dirname(__file__), ui_file)
        self.ui = _load_ui(ui_path, self)
        _adopt_ui_identity(self, self.ui)

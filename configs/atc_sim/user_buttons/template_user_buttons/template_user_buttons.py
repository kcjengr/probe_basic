import os
import linuxcnc

from PySide6.QtWidgets import QWidget

from qtpyvcp.widgets.button_widgets.action_button import ActionButton

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger
from qtpyvcp.actions import bindWidget, InvalidAction
from qtpyvcp.utilities.runtime_ui_loader import load_ui as load_runtime_ui

LOG = logger.getLogger(__name__)

STATUS = getPlugin('status')
TOOL_TABLE = getPlugin('tooltable')

INI_FILE = linuxcnc.ini(os.getenv('INI_FILE_NAME'))


def _load_ui(ui_path, parent):
    return load_runtime_ui(ui_path, parent)


class UserButton(QWidget):
    def __init__(self, parent=None):
        super(UserButton, self).__init__(parent)
        # The .ui is named after this file, so a copied folder just works.
        ui_file = os.path.splitext(os.path.basename(__file__))[0] + ".ui"
        ui_path = os.path.join(os.path.dirname(__file__), ui_file)
        self.ui = _load_ui(ui_path, self)
        self._bind_action_buttons()

    def _bind_action_buttons(self):
        # Explicitly bind dynamic buttons in case property-based binding was skipped.
        for button in self.findChildren(ActionButton):
            action_name = button.property("actionName")
            if not action_name:
                continue
            try:
                bindWidget(button, str(action_name))
            except InvalidAction:
                LOG.warning("Invalid action for user button %s: %s", button.objectName(), action_name)

import os
import linuxcnc

from PySide6.QtWidgets import QWidget

from qtpyvcp.widgets.button_widgets.action_button import ActionButton
from qtpyvcp.utilities.runtime_ui_loader import load_ui

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger
from qtpyvcp.actions import bindWidget, InvalidAction

LOG = logger.getLogger(__name__)

STATUS = getPlugin('status')
TOOL_TABLE = getPlugin('tooltable')

INI_FILE = linuxcnc.ini(os.getenv('INI_FILE_NAME'))


class UserButton(QWidget):
    def __init__(self, parent=None):
        super(UserButton, self).__init__(parent)
        ui_path = os.path.join(os.path.dirname(__file__), "template_user_buttons.ui")
        load_ui(ui_path, self)
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
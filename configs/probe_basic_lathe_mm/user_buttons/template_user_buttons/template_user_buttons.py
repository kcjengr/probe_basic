import os
import linuxcnc

from PySide6.QtWidgets import QWidget

import template_user_buttons_ui
from qtpyvcp.widgets.button_widgets.action_button import ActionButton

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
        self.ui = template_user_buttons_ui.Ui_USER_BUTTONS()
        self.ui.setupUi(self)
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
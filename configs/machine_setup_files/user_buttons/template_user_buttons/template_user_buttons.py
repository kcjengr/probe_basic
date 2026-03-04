import os
import linuxcnc

from PySide6.QtWidgets import QWidget

import template_user_buttons_ui

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)

STATUS = getPlugin('status')
TOOL_TABLE = getPlugin('tooltable')

INI_FILE = linuxcnc.ini(os.getenv('INI_FILE_NAME'))


class UserButton(QWidget):
    def __init__(self, parent=None):
        super(UserButton, self).__init__(parent)
        self.ui = template_user_buttons_ui.Ui_USER_BUTTONS()
        self.ui.setupUi(self)
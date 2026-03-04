import os
import linuxcnc

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger
import template_user_atc_buttons_ui

LOG = logger.getLogger(__name__)

STATUS = getPlugin('status')
TOOL_TABLE = getPlugin('tooltable')

INI_FILE = linuxcnc.ini(os.getenv('INI_FILE_NAME'))


class UserAtcButton(QWidget):
    def __init__(self, parent=None):
        super(UserAtcButton, self).__init__(parent)
        self.ui = template_user_atc_buttons_ui.Ui_USER_ATC_BUTTONS()
        self.ui.setupUi(self)
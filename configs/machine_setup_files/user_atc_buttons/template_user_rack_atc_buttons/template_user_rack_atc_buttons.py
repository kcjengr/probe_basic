import os
import linuxcnc

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger
import template_user_rack_atc_buttons_ui

LOG = logger.getLogger(__name__)

STATUS = getPlugin('status')
TOOL_TABLE = getPlugin('tooltable')

INI_FILE = linuxcnc.ini(os.getenv('INI_FILE_NAME'))


class UserRackAtcButton(QWidget):
    def __init__(self, parent=None):
        super(UserRackAtcButton, self).__init__(parent)
        ui_cls = getattr(template_user_rack_atc_buttons_ui, "Ui_USER_RACK_ATC_BUTTONS", None)
        if ui_cls is None:
            ui_cls = template_user_rack_atc_buttons_ui.Ui_USER_ATC_BUTTONS
        self.ui = ui_cls()
        self.ui.setupUi(self)
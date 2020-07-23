# required packages
# sudo apt-get install python-pyqt5.qtquick qml-module-qtquick-controls

import os

# Workarround for nvidia propietary drivers

import ctypes
import ctypes.util

import linuxcnc
from qtpyvcp.actions.machine_actions import issue_mdi

ctypes.CDLL(ctypes.util.find_library("GL"), mode=ctypes.RTLD_GLOBAL)

# end of Workarround

from qtpy import uic
from qtpy.QtWidgets import QFrame
from qtpy.QtWidgets import QFrame
from qtpyvcp.widgets.base_widgets import VCPWidget

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)
STATUS = getPlugin('status')
WIDGET_PATH = os.path.dirname(os.path.abspath(__file__))


class BasicToolInfo(QFrame, VCPWidget):

    def __init__(self, parent=None):
        super(BasicToolInfo, self).__init__(parent)

        if parent is None:
            return
        uic.loadUi(os.path.join(WIDGET_PATH, "BasicToolInfo.ui"), self)
        self.show()

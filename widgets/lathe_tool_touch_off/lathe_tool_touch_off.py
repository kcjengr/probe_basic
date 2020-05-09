# required packages
# sudo apt-get install python-pyqt5.qtquick qml-module-qtquick-controls

import os

# Workarround for nvidia propietary drivers

import ctypes
import ctypes.util

ctypes.CDLL(ctypes.util.find_library("GL"), mode=ctypes.RTLD_GLOBAL)

# end of Workarround

from qtpy.QtCore import Signal, Slot, QUrl, QObject
from qtpy.QtQuickWidgets import QQuickWidget

WIDGET_PATH = os.path.dirname(os.path.abspath(__file__))


class LatheToolTouchOff(QQuickWidget):

    def __init__(self, parent=None):
        super(LatheToolTouchOff, self).__init__(parent)

        if parent is None:
            return

        self.engine().rootContext().setContextProperty("handler", self)
        url = QUrl.fromLocalFile(os.path.join(WIDGET_PATH, "lathe_tool_touch_off.qml"))
        self.setSource(url)

        self.selected_tool = None

    pocketSig = Signal(int, arguments=['pocket_number'])

    @Slot(int)
    def pocket(self, pocket_num):
        self.pocketSig.emit(pocket_num)

    @Slot(str, int)
    def selected_tool(self, parent, tool_index):

        tool = 0

        if parent == "upper":
            tool = tool_index
        elif parent == "lower":
            tool = tool_index + 5
        elif tool == "right":
            tool = tool_index + 10

        return tool

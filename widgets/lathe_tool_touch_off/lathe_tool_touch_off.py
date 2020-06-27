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

from qtpy.QtCore import Signal, Slot, QUrl, QObject
from qtpy.QtQuickWidgets import QQuickWidget

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)
STATUS = getPlugin('status')
WIDGET_PATH = os.path.dirname(os.path.abspath(__file__))


class LatheToolTouchOff(QQuickWidget):

    toolActiveImageSig = Signal(str, int, arguments=['group', 'index'])
    toolResetSig = Signal()

    def __init__(self, parent=None):
        super(LatheToolTouchOff, self).__init__(parent)

        if parent is None:
            return

        self.dm = getPlugin('persistent_data_manager')

        self.stat = STATUS
        self.engine().rootContext().setContextProperty("handler", self)
        url = QUrl.fromLocalFile(os.path.join(WIDGET_PATH, "lathe_tool_touch_off.qml"))
        self.setSource(url)

        self.tool_image = self.dm.getData('tool-touch-off.tool-image-table') or dict()

        self.current_group = ""
        self.current_index = 0

        self.stat.tool_in_spindle.onValueChanged(self.set_active_tool)
        # self.stat.tool_table.onValueChanged(self.update_tools)

        issue_mdi.bindOk(widget=self)

    def update_tools(self, args):

        for key, value in self.tool_image.items():
            group, index = value

            self.tool_image[int(key)] = [group, index]

        self.dm.setData('tool-touch-off.tool-image-table', self.tool_image)

    def set_active_tool(self):
        tool_num = self.stat.tool_in_spindle.getValue()

        if self.tool_image is None:
            self.toolResetSig.emit()
        elif tool_num not in self.tool_image.keys():
            self.toolResetSig.emit()
        else:
            group, index = self.tool_image[tool_num]
            if (group == self.current_group) & (index == self.current_index):
                return

            self.toolActiveImageSig.emit(group, index)

            self.current_group = group
            self.current_index = index

    @Slot()
    def reset_tools(self):
        tool_num = self.stat.tool_in_spindle.getValue()
        self.tool_image.pop(tool_num, None)
        self.toolResetSig.emit()

    @Slot(str, int, int)
    def tool_select(self, group, index, orientation):

        tool_num = self.stat.tool_in_spindle.getValue()
        issue_mdi("G10 L1 P{} Q{}".format(tool_num, orientation))

        self.tool_image[tool_num] = [group, index]
        self.dm.setData('tool-touch-off.tool-image-table', self.tool_image)

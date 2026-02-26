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

from qtpy.QtCore import Signal, Slot, QUrl, QObject, QTimer
from qtpy.QtWidgets import QMessageBox, QWidget, QVBoxLayout, QApplication
from PySide6.QtQuick import QQuickView

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)
STATUS = getPlugin('status')
WIDGET_PATH = os.path.dirname(os.path.abspath(__file__))
ORIENTATION_ACK_DELAY_MS = 600
ORIENTATION_ACK_POS_X = 550
ORIENTATION_ACK_POS_Y = 250


class LatheToolTouchOff(QWidget):

    toolActiveImageSig = Signal(str, int, arguments=['group', 'index'])
    toolResetSig = Signal()

    def __init__(self, parent=None):
        super(LatheToolTouchOff, self).__init__(parent)

        self._view = None
        self._container = None
        self._cleanup_done = False

        if parent is None:
            return

        self.dm = getPlugin('persistent_data_manager')
        self.tooltable = getPlugin('tooltable')

        self.stat = STATUS
        qml_path = os.path.join(WIDGET_PATH, "lathe_tool_touch_off.qml")
        self._view = QQuickView()
        self._view.engine().rootContext().setContextProperty("handler", self)
        self._view.setResizeMode(QQuickView.SizeRootObjectToView)
        self._view.setSource(QUrl.fromLocalFile(qml_path))

        self._container = QWidget.createWindowContainer(self._view, self)
        self._container.setFocusPolicy(self.focusPolicy())

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self._container)

        self.tool_image = self.dm.getData('tool-touch-off.tool-image-table') or dict()

        self.current_group = ""
        self.current_index = 0

        self.stat.tool_in_spindle.onValueChanged(self.set_active_tool)
        # self.stat.tool_table.onValueChanged(self.update_tools)

        # Command issuance does not require bindOk on this container widget.
        app = QApplication.instance()
        if app is not None:
            try:
                app.aboutToQuit.connect(self._cleanup_qml)
            except Exception:
                pass

    def _cleanup_qml(self):
        if self._cleanup_done:
            return
        self._cleanup_done = True

        try:
            if hasattr(self, "stat") and self.stat is not None:
                self.stat.tool_in_spindle.onValueChanged.disconnect(self.set_active_tool)
        except Exception:
            pass

        try:
            if self._view is not None:
                self._view.engine().rootContext().setContextProperty("handler", None)
                self._view.setSource(QUrl())
        except Exception:
            pass

        try:
            if self._container is not None:
                self._container.setParent(None)
                self._container.deleteLater()
                self._container = None
        except Exception:
            pass

        try:
            if self._view is not None:
                self._view.deleteLater()
                self._view = None
        except Exception:
            pass

    def closeEvent(self, event):
        self._cleanup_qml()
        super(LatheToolTouchOff, self).closeEvent(event)

    def deleteLater(self):
        self._cleanup_qml()
        super(LatheToolTouchOff, self).deleteLater()

    def _show_orientation_ack_dialog(self, tool_num, from_q, to_q):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Tool Orientation Updated")
        msg.setText(
            f"Tool {tool_num} orientation changed from Q{from_q} to Q{to_q}.\n\n"
            "This updates the tool table."
        )
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        self._position_ack_dialog(msg)
        msg.exec_()

    def _position_ack_dialog(self, msg_box):
        msg_box.adjustSize()
        msg_box.move(int(ORIENTATION_ACK_POS_X), int(ORIENTATION_ACK_POS_Y))

    def _show_ack_then_reset(self, tool_num, from_q, to_q):
        self._show_orientation_ack_dialog(tool_num, from_q, to_q)
        self.reset_tools()

    def update_tools(self, args):

        for key, value in list(self.tool_image.items()):
            group, index = value

            self.tool_image[int(key)] = [group, index]

        self.dm.setData('tool-touch-off.tool-image-table', self.tool_image)

    def set_active_tool(self):
        tool_num = self.stat.tool_in_spindle.getValue()

        if self.tool_image is None:
            self.toolResetSig.emit()
        elif tool_num not in list(self.tool_image.keys()):
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
        self.current_group = ""
        self.current_index = 0
        self.toolResetSig.emit()

    @Slot(str, int, int)
    def tool_select(self, group, index, orientation):

        tool_num = self.stat.tool_in_spindle.getValue()
        previous_orientation = None

        try:
            if self.tooltable is not None:
                table = self.tooltable.getToolTable() or {}
                tool_data = table.get(tool_num, {})
                previous_orientation = int(tool_data.get('Q', 0))
        except Exception:
            LOG.debug("Failed reading previous orientation for tool %s", tool_num, exc_info=True)

        issue_mdi("G10 L1 P{} Q{}".format(tool_num, orientation))

        if previous_orientation is None:
            previous_orientation = 0

        self.tool_image[tool_num] = [group, index]
        self.dm.setData('tool-touch-off.tool-image-table', self.tool_image)

        QTimer.singleShot(
            ORIENTATION_ACK_DELAY_MS,
            lambda tn=tool_num, fq=previous_orientation, tq=orientation: self._show_ack_then_reset(tn, fq, tq)
        )

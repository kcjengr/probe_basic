import os

import linuxcnc

# Workaround for nvidia proprietary drivers
import ctypes
import ctypes.util
ctypes.CDLL(ctypes.util.find_library("GL"), mode=ctypes.RTLD_GLOBAL)
# end of workaround

from PySide6.QtCore import Property, Signal, Slot, QUrl, QTimer
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtQuick import QQuickView

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)
STATUS = getPlugin('status')
TOOLTABLE = getPlugin('tooltable')
GCODE_PROPERTIES = getPlugin('gcode_properties')
IN_DESIGNER = os.getenv('DESIGNER', False)
WIDGET_PATH = os.path.dirname(os.path.abspath(__file__))
INIFILE = linuxcnc.ini(os.getenv("INI_FILE_NAME"))


class DynATC(QWidget):
    """ATC carousel widget.

    Uses QQuickView + createWindowContainer (the Qt6-recommended approach
    for mixing QML and regular widgets) instead of QQuickWidget, which has
    known compositing issues under Qt6 on X11.
    """

    atcInitSig  = Signal(int, int,   arguments=['pockets', 'step_duration'])
    resizeSig   = Signal(int, int,   arguments=['width', 'height'])
    rotateSig   = Signal(int, int,   arguments=['steps', 'direction'])
    showToolSig = Signal(float, float, arguments=['pocket', 'tool_num'])
    hideToolSig = Signal(float,      arguments=['pocket'])
    highlightPocketSig = Signal(float, bool, arguments=['pocket', 'highlight'])
    bgColorSig  = Signal(QColor,     arguments=['color'])
    homeMsgSig  = Signal(str,        arguments=['message'])

    def __init__(self, parent=None):
        super(DynATC, self).__init__(parent)

        self._background_color = QColor(0, 0, 0)
        self.atc_position = 0
        self.pocket = 1
        self.home = 0
        self.homing = 0
        self.pocket_slots = int(INIFILE.find("ATC", "POCKETS") or 12)
        self.rotaion_duration = int(INIFILE.find("ATC", "STEP_TIME") or 1000)

        self.tool_table = None
        self.status_tool_table = None
        self.pockets = dict()
        self.tools = None
        self.required_tools = set()

        self._view = None
        self._container = None

        if not IN_DESIGNER:
            self._setup_view()
            self._connect_required_tool_signals()

    def _setup_view(self):
        qml_path = os.path.join(WIDGET_PATH, "atc.qml")
        LOG.info("[DynATC] loading QML via QQuickView: %s", qml_path)

        self._view = QQuickView()
        self._view.engine().rootContext().setContextProperty("atc_spiner", self)
        self._view.setResizeMode(QQuickView.SizeRootObjectToView)
        self._view.setSource(QUrl.fromLocalFile(qml_path))

        LOG.info("[DynATC] QQuickView status=%s  pockets=%s  step_time=%s",
                 self._view.status(), self.pocket_slots, self.rotaion_duration)

        # createWindowContainer wraps the QWindow in a QWidget so it sits
        # cleanly inside the widget hierarchy without GL-compositing the
        # entire parent window.
        self._container = QWidget.createWindowContainer(self._view, self)
        self._container.setFocusPolicy(self.focusPolicy())

        self.setFixedSize(500, 500)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self._container)

        # Defer signal emissions by one event-loop tick so the QML Connections
        # objects are fully active before we send initialisation signals.
        QTimer.singleShot(0, self._init_qml_state)

    def _init_qml_state(self):
        """Send initialisation signals to QML after the event loop has ticked."""
        self.atcInitSig.emit(self.pocket_slots, self.rotaion_duration)
        for pocket in range(1, self.pocket_slots + 1):
            self.hideToolSig.emit(pocket)
            self.highlightPocketSig.emit(pocket, False)

    def _connect_required_tool_signals(self):
        """Wire program tool updates to pocket highlight updates."""
        try:
            if GCODE_PROPERTIES is not None and hasattr(GCODE_PROPERTIES, 'tools'):
                GCODE_PROPERTIES.tools.signal.connect(self._on_required_tools_changed)
        except Exception:
            LOG.exception("Failed to connect gcode_properties.tools signal")

        try:
            if STATUS is not None and hasattr(STATUS, 'tool_table'):
                STATUS.tool_table.signal.connect(self._on_required_tools_changed)
        except Exception:
            LOG.exception("Failed to connect status.tool_table signal")

        self._update_required_pocket_highlights()

    def _resolve_required_tool_numbers(self):
        required_tools = set()

        if GCODE_PROPERTIES is None or not hasattr(GCODE_PROPERTIES, 'tools'):
            return required_tools

        try:
            required_indices = GCODE_PROPERTIES.tools.getValue() or []
        except Exception:
            return required_tools

        try:
            tool_table = STATUS.tool_table.getValue() if STATUS is not None else []
        except Exception:
            tool_table = []

        for idx in required_indices:
            try:
                tool_num = int(tool_table[int(idx)][0])
            except Exception:
                continue

            if tool_num > 0:
                required_tools.add(tool_num)

        return required_tools

    @Slot(object)
    def _on_required_tools_changed(self, *_):
        self._update_required_pocket_highlights()

    def _update_required_pocket_highlights(self):
        self.required_tools = self._resolve_required_tool_numbers()

        for pocket in range(1, self.pocket_slots + 1):
            tool_num = int(self.pockets.get(pocket, 0) or 0)
            highlight = tool_num > 0 and tool_num in self.required_tools
            self.highlightPocketSig.emit(pocket, highlight)

    def resizeEvent(self, event):
        size = event.size()
        self.resizeSig.emit(size.width(), size.height())
        super().resizeEvent(event)

    @Property(QColor)
    def backgroundColor(self):
        return self._background_color

    @backgroundColor.setter
    def backgroundColor(self, color):
        self.bgColorSig.emit(color)
        self._background_color = color

    def load_tools(self):
        for i in range(1, self.pocket_slots + 1):
            self.hideToolSig.emit(i)
        for pocket, tool in list(self.pockets.items()):
            if tool != 0:
                self.showToolSig.emit(pocket, tool)
            else:
                self.hideToolSig.emit(pocket)
        self._update_required_pocket_highlights()

    def store_tool(self, pocket, tool_num):
        self.pockets[pocket] = tool_num
        if tool_num != 0:
            self.showToolSig.emit(pocket, tool_num)
        else:
            self.hideToolSig.emit(pocket)
        self._update_required_pocket_highlights()

    def atc_message(self, msg=""):
        self.homeMsgSig.emit(msg)

    def rotate(self, steps, direction):
        if direction == "cw":
            self.rotateSig.emit(int(steps), 1)
        elif direction == "ccw":
            self.rotateSig.emit(int(steps), -1)

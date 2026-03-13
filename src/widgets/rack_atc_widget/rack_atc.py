import os

import linuxcnc

# Workarround for nvidia propietary drivers

import ctypes
import ctypes.util

ctypes.CDLL(ctypes.util.find_library("GL"), mode=ctypes.RTLD_GLOBAL)

# end of Workarround

from PySide6.QtGui import QColor

from PySide6.QtCore import Property, Signal, Slot, QUrl, QTimer
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

class RackATC(QWidget):
    atcInitSig = Signal(int, arguments=['pockets'])
    
    resizeSig = Signal(int, int, arguments=["width", "height"])
    
    showToolSig = Signal(float, float, arguments=['pocket', 'tool_num'])
    hideToolSig = Signal(float, arguments=['pocket'])
    highlightPocketSig = Signal(float, bool, arguments=['pocket', 'highlight'])

    bgColorSig = Signal(QColor, arguments=["color"])

    homeMsgSig = Signal(str, arguments=["message"])

    def __init__(self, parent=None):
        super(RackATC, self).__init__(parent)

        # properties
        self._background_color = QColor(0, 0, 0)
        
        self.atc_position = 0
        self.pocket = 1
        self.home = 0
        self.homing = 0
        self.pocket_slots = int(INIFILE.find("ATC", "POCKETS") or 12)
        self.rotaion_duration = int(INIFILE.find("ATC", "STEP_TIME") or 1000)

        self._view = None
        self._container = None

        self.tool_table = None
        self.status_tool_table = None
        self.pockets = dict()
        self.tools = None
        self.required_tools = set()

        if not IN_DESIGNER:
            self._setup_view()
            self._connect_required_tool_signals()

    def _setup_view(self):
        qml_path = os.path.join(WIDGET_PATH, "rack_atc.qml")
        LOG.info("[RackATC] loading QML via QQuickView: %s", qml_path)

        self._view = QQuickView()
        self._view.engine().rootContext().setContextProperty("rack_atc", self)
        self._view.setResizeMode(QQuickView.SizeRootObjectToView)
        self._view.setSource(QUrl.fromLocalFile(qml_path))

        self._container = QWidget.createWindowContainer(self._view, self)
        self._container.setFocusPolicy(self.focusPolicy())

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self._container)

        QTimer.singleShot(0, self._init_qml_state)

    def _init_qml_state(self):
        self.atcInitSig.emit(self.pocket_slots)
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
        # print("load_tools")
        for i in range(1, self.pocket_slots+1):
            self.hideToolSig.emit(i)

        for pocket, tool in list(self.pockets.items()):
            if tool != 0:
                self.showToolSig.emit(pocket, tool)
            else:
                self.hideToolSig.emit(pocket)
        self._update_required_pocket_highlights()

    def store_tool(self, pocket, tool_num):
        self.pockets[pocket] = tool_num
        #
        # print(type(pocket), pocket)
        # print(type(tool_num), tool_num)
        if tool_num != 0:
            # print("show tool {} at pocket {}".format(tool_num, pocket))
            self.showToolSig.emit(pocket, tool_num)
        else:
            # print("Hide tool at pocket {}".format(pocket))
            self.hideToolSig.emit(pocket)
        self._update_required_pocket_highlights()


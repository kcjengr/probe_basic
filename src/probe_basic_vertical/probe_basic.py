#!/usr/bin/env python

import os

from qtpy.QtCore import QTimer
from qtpy.QtGui import QPalette
from qtpy.QtWidgets import QApplication

from qtpyvcp.utilities import logger
from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

from . import probe_basic_rc

LOG = logger.getLogger('QtPyVCP.' + __name__)

VCP_DIR = os.path.abspath(os.path.dirname(__file__))
LIGHT_STYLESHEET_FILE = "probe_basic_light.qss"
DARK_STYLESHEET_FILE = "probe_basic_dark.qss"


class ProbeBasic(VCPMainWindow):
    """Main window class for the ProbeBasic VCP."""
    def __init__(self, *args, **kwargs):
        super(ProbeBasic, self).__init__(*args, **kwargs)
        self._connect_theme_tracking()
        self._apply_theme_stylesheet()

    def _is_dark_theme(self):
        app = QApplication.instance()
        if app is None:
            return False
        palette = app.palette()
        window_lightness = palette.color(QPalette.Window).lightness()
        base_lightness = palette.color(QPalette.Base).lightness()
        return ((window_lightness + base_lightness) / 2) < 128

    def _connect_theme_tracking(self):
        app = QApplication.instance()
        if app is None:
            return
        palette_changed = getattr(app, 'paletteChanged', None)
        if palette_changed is not None:
            try:
                palette_changed.connect(self._on_palette_changed)
            except Exception:
                LOG.exception("Failed to connect paletteChanged signal")

    def _on_palette_changed(self, *_args):
        QTimer.singleShot(0, self._apply_theme_stylesheet)

    def _apply_theme_stylesheet(self):
        dark_theme = self._is_dark_theme()
        stylesheet_file = DARK_STYLESHEET_FILE if dark_theme else LIGHT_STYLESHEET_FILE
        stylesheet_path = os.path.join(VCP_DIR, stylesheet_file)
        app = QApplication.instance()
        if app is None:
            return
        try:
            with open(stylesheet_path, 'r', encoding='utf-8') as style_file:
                app.setStyleSheet(style_file.read())
        except Exception:
            LOG.exception("Failed to load theme stylesheet: %s", stylesheet_path)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets

try:
    from ._version import get_versions
    __version__ = get_versions()['version']
except Exception:
    __version__ = "Unknown"

from . import about_ui


class AboutDialog(QtWidgets.QDialog):
    """Custom About dialog with version information."""
    
    def __init__(self, parent=None, ui_file=None, **kwargs):
        super(AboutDialog, self).__init__(parent)
        self.ui = about_ui.Ui_Dialog()
        self.ui.setupUi(self)
        
        # Update label with version information
        version_text = (
            f"<html><head/><body><p align=\"center\">"
            f"<span style=\" font-weight:600;\">ProbeBasic</span><br/>"
            f"Version: {__version__}<br/>"
            f"https://kcjengr.github.io/probe_basic/"
            f"</p></body></html>"
        )
        self.ui.label.setText(version_text)

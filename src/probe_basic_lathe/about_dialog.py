#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets

try:
    # Try to get version from package metadata (for installed packages)
    from importlib.metadata import version, PackageNotFoundError
    try:
        __version__ = version("probe-basic")
    except PackageNotFoundError:
        # Fall back to versioneer for development installations
        from probe_basic._version import get_versions
        __version__ = get_versions()['version']
except ImportError:
    # Python < 3.8 fallback
    try:
        from probe_basic._version import get_versions
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
            f"<span style=\" font-weight:600;\">ProbeBasic Lathe</span><br/>"
            f"Version: {__version__}<br/>"
            f"https://kcjengr.github.io/probe_basic/"
            f"</p></body></html>"
        )
        self.ui.label.setText(version_text)

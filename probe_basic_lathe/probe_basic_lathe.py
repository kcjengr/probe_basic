#!/usr/bin/env python

import os

from qtpy.QtCore import Slot, QRegExp
from qtpy.QtGui import QFontDatabase, QRegExpValidator
from qtpyvcp.actions.machine_actions import issue_mdi

from qtpyvcp import actions
from qtpyvcp.utilities import logger
from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

import probe_basic_lathe_rc

LOG = logger.getLogger('QtPyVCP.' + __name__)

VCP_DIR = os.path.abspath(os.path.dirname(__file__))

# Add custom fonts
QFontDatabase.addApplicationFont(os.path.join(VCP_DIR, 'fonts/BebasKai.ttf'))

class ProbeBasicLathe(VCPMainWindow):
    """Main window class for the ProbeBasic VCP."""
    def __init__(self, *args, **kwargs):
        super(ProbeBasicLathe, self).__init__(*args, **kwargs)
        self.run_from_line_Num.setValidator(QRegExpValidator(QRegExp("[0-9]*")))
        self.feed_unit_per_minute = 0.0
        self.feed_per_rev = 0.0
        self.css_sword = 0.0
        self.rpm_mode = 0.0

    def on_feed_unit_per_minute_entry_textChanged(self, value):
        if value:
            self.feed_unit_per_minute = float(value)
        else:
            self.feed_unit_per_minute = 0.0

    def on_feed_unit_per_minute_entry_returnPressed(self):
        cmd = "G94 F{}".format(self.feed_unit_per_minute)
        issue_mdi(cmd)

    def on_feed_per_rev_entry_textChanged(self, value):
        if value:
            self.feed_per_rev = float(value)
        else:
            self.feed_per_rev = 0.0000

    def on_feed_per_rev_entry_returnPressed(self):
        cmd = "G95 F{}".format(self.feed_per_rev)
        issue_mdi(cmd)

    def on_css_sword_entry_textChanged(self, value):
        if value:
            self.css_sword = float(value)
        else:
            self.css_sword = 0.0

    def on_css_sword_entry_returnPressed(self):
        cmd = "G96 S{}".format(self.css_sword)
        issue_mdi(cmd)

    def on_rpm_mode_entry_textChanged(self, value):
        if value:
            self.rpm_mode = float(value)
        else:
            self.rpm_mode = 0

    def on_rpm_mode_entry_returnPressed(self):
        cmd = "G97 S{}".format(self.rpm_mode)
        issue_mdi(cmd)

    def on_use_tcp_clicked(self):
        if self.use_tcp.isChecked():
            self.use_tcp_mode.setText('1')
        else:
            self.use_tcp_mode.setText('0')

    def on_run_from_line_Btn_clicked(self):
        try:
            lineNum = int(self.run_from_line_Num.text())
        except:
            return False

        actions.program_actions.run(lineNum)


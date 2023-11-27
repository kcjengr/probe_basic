#!/usr/bin/env python

import os

from qtpy.QtCore import Slot, QRegExp
from qtpy.QtGui import QFontDatabase, QRegExpValidator
from qtpyvcp.actions.machine_actions import issue_mdi
from qtpy.QtWidgets import QAbstractButton

from qtpyvcp import actions
from qtpyvcp.utilities import logger
from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from qtpyvcp.utilities.settings import getSetting, setSetting


from . import probe_basic_lathe_rc

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
        self.btnMdiBksp.clicked.connect(self.mdiBackSpace_clicked)
        self.btnMdiSpace.clicked.connect(self.mdiSpace_clicked)
        self.conv_g94_g95.setText(str(getSetting("conversational.g94-g95-status").getValue()))
        self.conv_g96_g97.setText(str(getSetting("conversational.g96-g97-status").getValue()))
        self.conv_m3_m4.setText(str(getSetting("conversational.m3-m4-status").getValue()))
        self.conv_m7_m8_m9.setText(str(getSetting("conversational.m7-m8-m9-status").getValue()))


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

    @Slot(QAbstractButton)
    def on_sidebartabGroup_buttonClicked(self, button):
        self.sidebar_widget.setCurrentIndex(button.property('page'))

    # MDI Panel
    @Slot(QAbstractButton)
    def on_gcodemdibtnGroup_buttonClicked(self, button):
        self.gcode_mdi.setCurrentIndex(button.property('page'))

    @Slot(QAbstractButton)
    def on_btngrpMdi_buttonClicked(self, button):
        char = str(button.text())
        text = self.mdiEntry.text() or 'null'
        if text != 'null':
            text += char
        else:
            text = char
        self.mdiEntry.setText(text)

    def mdiBackSpace_clicked(parent):
        if len(parent.mdiEntry.text()) > 0:
            text = parent.mdiEntry.text()[:-1]
            parent.mdiEntry.setText(text)

    def mdiSpace_clicked(parent):
        text = parent.mdiEntry.text() or 'null'
        # if no text then do not add a space
        if text != 'null':
            text += ' '
            parent.mdiEntry.setText(text)

    @Slot(QAbstractButton)
    def on_spindlerpmsourcebtnGroup_buttonClicked(self, button):
        self.spindle_rpm_source_widget.setCurrentIndex(button.property('page'))

    @Slot(QAbstractButton)
    def on_convg20g21btngrp_buttonClicked(self, button):
        if button.isChecked():
            self.conv_g20_g21.setText(button.property('checkedAction'))

    @Slot(QAbstractButton)
    def on_convg94g95btngrp_buttonClicked(self, button):
        setSetting("conversational.g94-g95-status", button.property('checkedAction'))
        self.conv_g94_g95.setText(str(getSetting("conversational.g94-g95-status").getValue()))
        print(getSetting("conversational.g94-g95-status").getValue())

    @Slot(QAbstractButton)
    def on_convg96g97btngrp_buttonClicked(self, button):
        setSetting("conversational.g96-g97-status", button.property('checkedAction'))
        self.conv_g96_g97.setText(str(getSetting("conversational.g96-g97-status").getValue()))
        self.conversational_stacked_widget.setCurrentIndex(button.property('page'))
        print(getSetting("conversational.g96-g97-status").getValue())

    @Slot(QAbstractButton)
    def on_convm3m4btngrp_buttonClicked(self, button):
        setSetting("conversational.m3-m4-status", button.property('checkedAction'))
        self.conv_m3_m4.setText(str(getSetting("conversational.m3-m4-status").getValue()))
        print(getSetting("conversational.m3-m4-status").getValue())

    @Slot(QAbstractButton)
    def on_convm7m8m9btngrp_buttonClicked(self, button):
        setSetting("conversational.m7-m8-m9-status", button.property('checkedAction'))
        self.conv_g94_g95.setText(str(getSetting("conversational.m7-m8-m9-status").getValue()))
        print(getSetting("conversational.m7-m8-m9-status").getValue())

#!/usr/bin/env python

import os
import sys
import importlib.util

import linuxcnc

from qtpy.QtCore import Slot, QRegExp
from qtpy.QtGui import QFontDatabase, QRegExpValidator
from qtpyvcp.actions.machine_actions import issue_mdi
from qtpy.QtWidgets import QAbstractButton
from qtpy.QtWidgets import QWidget
from qtpy import uic

from qtpyvcp import actions
from qtpyvcp.utilities import logger
from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

sys.path.insert(0,'/usr/lib/python3/dist-packages/probe_basic_lathe')
from . import probe_basic_lathe_rc

LOG = logger.getLogger('QtPyVCP.' + __name__)
VCP_DIR = os.path.abspath(os.path.dirname(__file__))
INIFILE = linuxcnc.ini(os.getenv("INI_FILE_NAME"))

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
        
        self.load_user_tabs()
        
        self.load_user_buttons()

        self.load_user_dros()

        self.load_offset_dro()

        # Set jog_button_stacked_widget index based on DRO_DISPLAY and LATHE/BACK_TOOL_LATHE presence
        dro_display = (INIFILE.find("DISPLAY", "DRO_DISPLAY") or "").strip().lower()

        # Normalize DRO_DISPLAY value to lowercase so user can enter XZ, xz, etc.
        dro_display = dro_display.lower()

        lathe_mode = INIFILE.find("DISPLAY", "LATHE") or False
        lathe_back_mode = INIFILE.find("DISPLAY", "BACK_TOOL_LATHE") or False
        
        lathe_type = "LATHE"
        
        if lathe_mode:
            lathe_type = "LATHE"
            self.vtkbackplot.setViewXZ2()
            
        if lathe_back_mode:
            lathe_type = "BACK_TOOL_LATHE"
            self.vtkbackplot.setViewXZ()


        index_map = {
            ("xz", "LATHE"): 0,
            ("xz", "BACK_TOOL_LATHE"): 1,
            ("xzc", "LATHE"): 2,
            ("xzc", "BACK_TOOL_LATHE"): 3,
            ("xyzc", "LATHE"): 4,
            ("xyzc", "BACK_TOOL_LATHE"): 5,
        }
        idx = index_map.get((dro_display, lathe_type), 0)
        self.jog_button_stacked_widget.setCurrentIndex(idx)

    def load_user_buttons(self):
        self.user_button_modules = {}
        self.user_buttons = {}
        
        user_buttons_paths = INIFILE.findall("DISPLAY", "USER_BUTTONS_PATH")

        for user_buttons_path in user_buttons_paths:
            user_button_path = os.path.expanduser(user_buttons_path)
            user_button_folders = os.listdir(user_buttons_path)
            for user_button in user_button_folders:
                if not os.path.isdir(os.path.join(user_buttons_path, user_button)):
                    continue
                module_name = "user_buttons." + os.path.basename(user_buttons_path) + "." + user_buttons_path
                spec = importlib.util.spec_from_file_location(module_name, os.path.join(os.path.dirname(user_buttons_path), user_button, user_button + ".py"))
                self.user_button_modules[module_name] = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = self.user_button_modules[module_name]
                spec.loader.exec_module(self.user_button_modules[module_name])
                
                self.user_buttons[module_name] = self.user_button_modules[module_name].UserButton()
                
                self.user_buttons_layout.addWidget( self.user_buttons[module_name])

    def load_user_dros(self):
        self.user_dros_modules = {}
        self.user_dros = {}

        dro_type = INIFILE.find("DISPLAY", "DRO_DISPLAY")
        if not dro_type:
            LOG.warning("No DRO_DISPLAY specified in INI.")
            return
        dro_type = dro_type.strip().lower()  # Normalize to lowercase

        user_dros_paths = INIFILE.findall("DISPLAY", "USER_DROS_PATH")

        for user_dros_path in user_dros_paths:
            user_dros_path = os.path.expanduser(user_dros_path)
            dro_folder = f"{dro_type}_dros"
            dro_py_file = f"dros_{dro_type}.py"
            dro_folder_path = os.path.join(user_dros_path, dro_folder)
            dro_py_path = os.path.join(dro_folder_path, dro_py_file)
            if os.path.isfile(dro_py_path):
                module_name = f"user_dros.{dro_folder}.{dro_py_file[:-3]}"
                spec = importlib.util.spec_from_file_location(module_name, dro_py_path)
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)
                if hasattr(module, "UserDRO"):
                    self.user_dros[module_name] = module.UserDRO()
                    self.dro_display_layout.addWidget(self.user_dros[module_name])
                return  # Only load one DRO, then exit

    def load_offset_dro(self):
        # Clear any existing widgets from the layout
        while self.offset_dro_layout.count():
            child = self.offset_dro_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        dro_type = INIFILE.find("DISPLAY", "DRO_DISPLAY")
        if not dro_type:
            LOG.warning("No DRO_DISPLAY specified in INI.")
            return
        dro_type = dro_type.strip().lower()  # Normalize to lowercase

        user_dros_paths = INIFILE.findall("DISPLAY", "USER_DROS_PATH")

        for user_dros_path in user_dros_paths:
            user_dros_path = os.path.expanduser(user_dros_path)
            dro_folder = f"{dro_type}_dros"
            offset_ui_file = f"offset_dros_{dro_type}.ui"
            offset_ui_path = os.path.join(user_dros_path, dro_folder, offset_ui_file)
            if os.path.isfile(offset_ui_path):
                offset_widget = QWidget()
                uic.loadUi(offset_ui_path, offset_widget)
                self.offset_dro_layout.addWidget(offset_widget)
                return  # Only load one offset DRO, then exit

    def load_user_tabs(self):
        self.user_tab_modules = {}
        self.user_tabs = {}
        sidebar_loaded = False;
        user_tabs_paths = INIFILE.findall("DISPLAY", "USER_TABS_PATH")

        for user_tabs_path in user_tabs_paths:
            user_tabs_path = os.path.expanduser(user_tabs_path)
            user_tab_folders = os.listdir(user_tabs_path)
            for user_tab in user_tab_folders:
                if not os.path.isdir(os.path.join(user_tabs_path, user_tab)):
                    continue

                module_name = "user_tab." + os.path.basename(user_tabs_path) + "." + user_tabs_path
                spec = importlib.util.spec_from_file_location(module_name, os.path.join(os.path.dirname(user_tabs_path), user_tab, user_tab + ".py"))
                self.user_tab_modules[module_name] = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = self.user_tab_modules[module_name]
                spec.loader.exec_module(self.user_tab_modules[module_name])
                self.user_tabs[module_name] = self.user_tab_modules[module_name].UserTab()
                if self.user_tabs[module_name].property("sidebar"):
                    if sidebar_loaded == False:
                        sidebar_loaded = True
                        self.user_tabs[module_name].setParent(self.sb_page_4)
                        self.user_sb_tab.setText(self.user_tabs[module_name].objectName().replace("_", " "))
                    else:
                        # can not load more than one sidebar widget
                        pass
                else:
                    self.tabWidget.addTab(self.user_tabs[module_name], self.user_tabs[module_name].objectName().replace("_", " "))

        if sidebar_loaded == False:
            self.user_sb_tab.hide()
            self.dro_tab.setStyleSheet(self.user_sb_tab.styleSheet())

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

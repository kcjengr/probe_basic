#!/usr/bin/env python


import os
import sys
import importlib.util

import linuxcnc

from qtpy.QtCore import Slot, QRegExp, Qt
from qtpy.QtGui import QFontDatabase, QRegExpValidator
from qtpy.QtWidgets import QAbstractButton
from qtpy.QtWidgets import QAction, QWidget

from qtpyvcp import actions
from qtpyvcp.utilities import logger
from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from qtpyvcp.utilities.settings import getSetting, setSetting


sys.path.insert(0,'/usr/lib/python3/dist-packages/probe_basic')
import probe_basic_rc

LOG = logger.getLogger('QtPyVCP.' + __name__)
VCP_DIR = os.path.abspath(os.path.dirname(__file__))
INIFILE = linuxcnc.ini(os.getenv("INI_FILE_NAME"))

# Add custom fonts
QFontDatabase.addApplicationFont(os.path.join(VCP_DIR, 'fonts/BebasKai.ttf'))

class ProbeBasic(VCPMainWindow):
    """Main window class for the ProbeBasic VCP."""
    def __init__(self, *args, **kwargs):
        super(ProbeBasic, self).__init__(*args, **kwargs)
        self.filesystemtable.sortByColumn(3, Qt.DescendingOrder)
        self.filesystemtable_2.sortByColumn(3, Qt.DescendingOrder)
        self.run_from_line_Num.setValidator(QRegExpValidator(QRegExp("[0-9]*")))
        self.btnMdiBksp.clicked.connect(self.mdiBackSpace_clicked)
        self.btnMdiSpace.clicked.connect(self.mdiSpace_clicked)

        if (0 == int(INIFILE.find("DISPLAY", "ATC_TAB_DISPLAY") or 0)):
            atc_tab_index = self.tabWidget.indexOf(self.atc_tab)
            self.tabWidget.setTabVisible(atc_tab_index, False)
            self.tabWidget.removeTab(atc_tab_index)

        elif (1 == int(INIFILE.find("DISPLAY", "ATC_TAB_DISPLAY") or 1)):
            self.load_atc()

        else:
            self.load_rack_atc()
            
        self.vtk.setViewMachine()

        if (getSetting("spindle-rpm-display.calculated-rpm").getValue()):
            self.spindle_rpm_source_widget.setCurrentIndex(self.spindle_calculated_rpm_button.property('page'))
        
        else:
            self.spindle_rpm_source_widget.setCurrentIndex(self.spindle_encoder_rpm_button.property('page'))
    
        self.load_user_tabs()

        self.load_user_buttons()

        self.help_menu = self.menuBar().addMenu("Help")
        self.interactive_help_action = QAction("Interactive Help", self, checkable=True)
        self.interactive_help_action.setChecked(False)
        self.interactive_help_action.toggled.connect(self.toggle_tooltips)
        self.help_menu.addAction(self.interactive_help_action)  # Moved to HELP menu
        self.store_original_tooltips()
        self.toggle_tooltips(False)

    def store_original_tooltips(self):
        """Store the original tooltips for all widgets to restore later."""
        for widget in self.findChildren(QWidget):
            if widget.toolTip():  # Only store if a tooltip exists
                widget.setProperty("original_tooltip", widget.toolTip())

    def toggle_tooltips(self, enabled):
        """Enable or disable tooltips across all widgets."""
        for widget in self.findChildren(QWidget):
            original_tooltip = widget.property("original_tooltip")
            if enabled and original_tooltip:
                widget.setToolTip(original_tooltip)  # Restore tooltip
            else:
                widget.setToolTip("")  # Disable tooltip

    def load_atc(self):
        self.atc_modules = {}
        self.atc = {}
        
        atc_paths = [os.path.join(VCP_DIR, "atc")]

        for atc_path in atc_paths:
            atc_path = os.path.expanduser(atc_path)
            if not os.path.exists(atc_path):
                LOG.warning(f"ATC path does not exist: {atc_path}")
                continue
                
            atc_folders = os.listdir(atc_path)
            for atc in atc_folders:
                atc_dir = os.path.join(atc_path, atc)
                if not os.path.isdir(atc_dir):
                    continue
                    
                module_name = f"atc.{atc}"
                module_file = os.path.join(atc_dir, f"{atc}.py")
                spec = importlib.util.spec_from_file_location(module_name, module_file)
                self.atc_modules[module_name] = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = self.atc_modules[module_name]
                spec.loader.exec_module(self.atc_modules[module_name])
                
                self.atc[module_name] = self.atc_modules[module_name].Atc()
                
                self.atc_layout.addWidget( self.atc[module_name])

    def load_rack_atc(self):
        self.rack_atc_modules = {}
        self.rack_atc = {}

        rack_atc_paths = [os.path.join(VCP_DIR, "rack_atc")]

        for rack_atc_path in rack_atc_paths:
            rack_atc_path = os.path.expanduser(rack_atc_path)
            if not os.path.exists(rack_atc_path):
                LOG.warning(f"Rack ATC path does not exist: {rack_atc_path}")
                continue
                
            rack_atc_folders = os.listdir(rack_atc_path)
            for rack_atc in rack_atc_folders:
                rack_atc_dir = os.path.join(rack_atc_path, rack_atc)
                if not os.path.isdir(rack_atc_dir):
                    continue
                    
                module_name = f"rack_atc.{rack_atc}"
                module_file = os.path.join(rack_atc_dir, f"{rack_atc}.py")
                spec = importlib.util.spec_from_file_location(module_name, module_file)
                self.rack_atc_modules[module_name] = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = self.rack_atc_modules[module_name]
                spec.loader.exec_module(self.rack_atc_modules[module_name])
                
                self.rack_atc[module_name] = self.rack_atc_modules[module_name].RackAtc()
                
                self.atc_layout.addWidget( self.rack_atc[module_name])
    
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
               
    def load_user_tabs(self):
        self.user_tab_modules = {}
        self.user_tabs = {}
        sidebar_loaded = False
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
            self.plot_tab.setStyleSheet(self.user_sb_tab.styleSheet())

    @Slot(QAbstractButton)
    def on_probetabGroup_buttonClicked(self, button):
        self.probe_tab_widget.setCurrentIndex(button.property('page'))

    @Slot(QAbstractButton)
    def on_settertabGroup_buttonClicked(self, button):
        self.setter_tab_widget.setCurrentIndex(button.property('page'))

    @Slot(QAbstractButton)
    def on_sidebartabGroup_buttonClicked(self, button):
        self.sidebar_widget.setCurrentIndex(button.property('page'))

    @Slot(QAbstractButton)
    def on_spindlerpmsourcebtnGroup_buttonClicked(self, button):
        self.spindle_rpm_source_widget.setCurrentIndex(button.property('page'))

    @Slot(QAbstractButton)
    def on_gcodemdibtnGroup_buttonClicked(self, button):
        self.gcode_mdi.setCurrentIndex(button.property('page'))

    # Fwd/Back buttons off the stacked widget
    def on_probe_help_next_released(self):
        lastPage = 6
        currentIndex = self.probe_help_widget.currentIndex()
        if currentIndex == lastPage:
            self.probe_help_widget.setCurrentIndex(0)
        else:
            self.probe_help_widget.setCurrentIndex(currentIndex + 1)

    def on_probe_help_prev_released(self):
        lastPage = 6
        currentIndex = self.probe_help_widget.currentIndex()
        if currentIndex == 0:
            self.probe_help_widget.setCurrentIndex(lastPage)
        else:
            self.probe_help_widget.setCurrentIndex(currentIndex - 1)


    @Slot(QAbstractButton)
    def on_fileviewerbtnGroup_buttonClicked(self, button):
        self.file_viewer_widget.setCurrentIndex(button.property('page'))

    def on_run_from_line_Btn_clicked(self):
        try:
            lineNum = int(self.run_from_line_Num.text())
        except:
            return False

        actions.program_actions.run(lineNum)

    # MDI Panel
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
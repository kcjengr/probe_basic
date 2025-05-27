#!/usr/bin/env python

import os
import sys
import importlib.util

import linuxcnc

from qtpy.QtCore import Slot, QRegExp, Qt
from qtpy.QtGui import QFontDatabase, QRegExpValidator
from qtpy.QtWidgets import QAbstractButton
from qtpy.QtWidgets import QAction, QWidget
from qtpy import uic

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

        if (0 == int(INIFILE.find("ATC", "POCKETS") or 0)):
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
	
        self.load_user_dros()

        self.load_offset_dro()

        # Set jog_button_stacked_widget index based on DRO_DISPLAY and LATHE/BACK_TOOL_LATHE presence
        dro_display = (INIFILE.find("DISPLAY", "DRO_DISPLAY") or "").strip().lower()

        # Normalize DRO_DISPLAY value to lowercase so user can enter XZ, xz, etc.
        dro_display = dro_display.lower()
        
        self.help_menu = self.menuBar().addMenu("Help")
        
        self.interactive_help_action = QAction("Interactive Help", self, checkable=True)
        self.interactive_help_action.setChecked(False)
        self.interactive_help_action.toggled.connect(self.toggle_tooltips)
        self.help_menu.addAction(self.interactive_help_action)  # Moved to HELP menu
        self.store_original_tooltips()
        self.toggle_tooltips(False)

        self.filesystemtable.gcodeFileSelected['bool'].connect(lambda x: self.main_load_gcode_button.setEnabled(True))

        self.filesystemtable_2.rootChanged.connect(lambda: self.device_folder_up_button.setEnabled(False) 
           if self.filesystemtable_2.model.rootPath().lower() == '/home'
           else self.device_folder_up_button.setEnabled(True))

        self.filesystemtable.rootChanged.connect(lambda: self.main_folder_up_button.setEnabled(False) 
           if self.filesystemtable.model.rootPath().lower() == '/home'
           else self.main_folder_up_button.setEnabled(True))
        self.filesystemtable.gcodeFileSelected['bool'].connect(lambda x: (
           self.main_load_gcode_button.setText("SELECT FOLDER") if not x else None,
           self.main_load_gcode_button.setText("LOAD G-CODE") if x else None
        ))

        self.main_load_gcode_button.clicked.connect(lambda: ( 
            self.main_load_gcode_button.setText("LOAD G-CODE") if self.main_load_gcode_button.text() == 'SELECT FOLDER' else None
        ))

        self.filesystemtable.model.rootPathChanged.connect(lambda: (
            self.filesystemtable.clearSelection(),
            self.main_load_gcode_button.setEnabled(False)
        ))

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
                
                self.atc_layout.addWidget(self.atc[module_name])

                # Load user ATC buttons after loading the ATC
                if hasattr(self.atc[module_name], 'user_atc_buttons_layout'):
                    self.load_user_atc_buttons(self.atc[module_name].user_atc_buttons_layout)
                else:
                    LOG.warning(f"user_atc_buttons_layout not found in {module_name}. Unable to add ATC buttons.")

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
                
                self.atc_layout.addWidget(self.rack_atc[module_name])
                
                # Load user ATC buttons after loading the rack ATC
                if hasattr(self.rack_atc[module_name], 'user_atc_buttons_layout'):
                    self.load_user_atc_buttons(self.rack_atc[module_name].user_atc_buttons_layout)
                else:
                    LOG.warning(f"user_atc_buttons_layout not found in {module_name}. Unable to add ATC buttons.")

    def load_user_atc_buttons(self, layout):
        self.user_atc_button_modules = {}
        self.user_atc_buttons = {}
        
        user_atc_buttons_paths = INIFILE.findall("DISPLAY", "USER_ATC_BUTTONS_PATH")

        for user_atc_buttons_path in user_atc_buttons_paths:
            user_atc_button_path = os.path.expanduser(user_atc_buttons_path)
            if not os.path.exists(user_atc_button_path):
                LOG.warning(f"User ATC buttons path does not exist: {user_atc_button_path}")
                continue
            
            user_atc_button_folders = os.listdir(user_atc_button_path)
            for user_atc_button in user_atc_button_folders:
                button_dir = os.path.join(user_atc_button_path, user_atc_button)
                if not os.path.isdir(button_dir):
                    continue
                
                module_name = f"user_atc_buttons.{os.path.basename(user_atc_button_path)}.{user_atc_button}"
                module_file = os.path.join(button_dir, f"{user_atc_button}.py")
                spec = importlib.util.spec_from_file_location(module_name, module_file)
                self.user_atc_button_modules[module_name] = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = self.user_atc_button_modules[module_name]
                spec.loader.exec_module(self.user_atc_button_modules[module_name])
                
                self.user_atc_buttons[module_name] = self.user_atc_button_modules[module_name].UserAtcButton()
                
                layout.addWidget(self.user_atc_buttons[module_name])

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

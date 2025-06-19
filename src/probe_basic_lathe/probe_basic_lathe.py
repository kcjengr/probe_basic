#!/usr/bin/env python

import os
import sys
import importlib.util
import csv

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
from qtpyvcp.utilities.settings import getSetting, setSetting  # <-- ADD THIS LINE

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
        self.btnMdiBksp.clicked.connect(self.mdiBackSpace_clicked)
        self.btnMdiSpace.clicked.connect(self.mdiSpace_clicked)
        
        self.load_user_tabs()
        
        self.load_user_buttons()

        self.load_user_dros()

        self.load_offset_dro()

        # --- Synchronize conversational_tab_widget and conversational_stackedwidget ---
        if hasattr(self, "conversational_tab_widget") and hasattr(self, "conversational_stackedwidget"):
            self.conversational_tab_widget.currentChanged.connect(self.sync_conversational_stack)

        # --- Startup Tab Selection Logic (using tab text property) ---
        startup_tab_text = getSetting("startup-settings.user-startup-tab").getValue()
        if hasattr(self, "tabWidget") and hasattr(self, "startup_tab_combobox"):
            # Populate ComboBox with current tab texts if not already set
            self.startup_tab_combobox.clear()
            for i in range(self.tabWidget.count()):
                self.startup_tab_combobox.addItem(self.tabWidget.tabText(i))
            # Set ComboBox to saved tab text, or default to first tab
            idx = self.startup_tab_combobox.findText(startup_tab_text)
            if idx != -1:
                self.startup_tab_combobox.setCurrentIndex(idx)
            else:
                self.startup_tab_combobox.setCurrentIndex(0)
            # Connect to save selection and switch tab on change
            self.startup_tab_combobox.currentTextChanged.connect(self.on_startup_tab_combobox_changed)
            # Set the main tab widget to the correct tab at startup
            self.set_startup_tab_by_text(self.startup_tab_combobox.currentText())
        # --- End Startup Tab Selection Logic ---

        # Set jog_button_stacked_widget index based on DRO_DISPLAY and LATHE/BACK_TOOL_LATHE presence
        dro_display = (INIFILE.find("DISPLAY", "DRO_DISPLAY") or "").strip().lower()

        # Normalize DRO_DISPLAY value to lowercase so user can enter XZ, xz, etc.
        dro_display = dro_display.lower()

        lathe_mode = INIFILE.find("DISPLAY", "LATHE") or False
        lathe_back_mode = INIFILE.find("DISPLAY", "BACK_TOOL_LATHE") or False

        if lathe_mode:
            lathe_type = "LATHE"
            self.vtkbackplot.setViewXZ2()
        elif lathe_back_mode:
            lathe_type = "BACK_TOOL_LATHE"
            self.vtkbackplot.setViewXZ()
        else:
            lathe_type = "LATHE"

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

        # Load thread data
        self.load_thread_data()
        
        # Connect your existing combo boxes
        self.sae_threads_combobox.currentTextChanged.connect(self.on_sae_thread_changed)
        self.metric_threads_combobox.currentTextChanged.connect(self.on_metric_thread_changed)
        
        # Populate the combo boxes
        self.populate_thread_combos()

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
            self.dro_tab.setStyleSheet(self.user_sb_tab.styleSheet())

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

    def set_startup_tab_by_text(self, tab_text):
        """Set the main tab widget to the tab matching tab_text."""
        if hasattr(self, "tabWidget"):
            for i in range(self.tabWidget.count()):
                if self.tabWidget.tabText(i).strip() == tab_text.strip():
                    self.tabWidget.setCurrentIndex(i)
                    break

    def on_startup_tab_combobox_changed(self, value):
        """Save ComboBox selection for startup, but do not change the current tab."""
        setSetting("startup-settings.user-startup-tab", value)
        # Do not call self.set_startup_tab_by_text(value)

    def sync_conversational_stack(self, index):
        """Synchronize stacked widget with tab widget selection."""
        if hasattr(self, "conversational_stackedwidget"):
            self.conversational_stackedwidget.setCurrentIndex(index)

    def load_thread_data(self):
        """Load thread data from CSV files"""
        import csv
        import os
        from collections import OrderedDict
        
        self.metric_threads = OrderedDict()
        self.sae_threads = OrderedDict()

        # Load metric threads
        metric_file = os.path.join(VCP_DIR, '../widgets/conversational/threads_metric.csv')
        if os.path.exists(metric_file):
            with open(metric_file, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row and not row[0].startswith('#') and len(row) >= 7:
                        desc, pitch, e_maj, e_min, i_maj, i_min, l_len = row[:7]
                        self.metric_threads[desc.strip()] = {
                            'description': desc.strip(),
                            'pitch': float(pitch),
                            'e_maj': float(e_maj),
                            'e_min': float(e_min),
                            'i_maj': float(i_maj),
                            'i_min': float(i_min),
                            'l_len': float(l_len)
                        }

        # Load SAE threads  
        sae_file = os.path.join(VCP_DIR, '../widgets/conversational/threads_sae.csv')
        if os.path.exists(sae_file):
            with open(sae_file, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row and not row[0].startswith('#') and len(row) >= 7:
                        desc, tpi, e_maj, e_min, i_maj, i_min, l_len = row[:7]
                        # Convert TPI to pitch (inches per thread)
                        pitch = 1.0 / float(tpi) if float(tpi) > 0 else 0
                        self.sae_threads[desc.strip()] = {
                            'description': desc.strip(),
                            'pitch': pitch,
                            'e_maj': float(e_maj),
                            'e_min': float(e_min),
                            'i_maj': float(i_maj),
                            'i_min': float(i_min),
                            'l_len': float(l_len)
                        }

    def populate_thread_combos(self):
        """Populate both thread combo boxes"""
        
        # Populate SAE threads combo (preserve file order)
        self.sae_threads_combobox.clear()
        sae_items = list(self.sae_threads.keys())
        self.sae_threads_combobox.addItems(sae_items)
        
        # Populate Metric threads combo (preserve file order)
        self.metric_threads_combobox.clear()
        metric_items = list(self.metric_threads.keys())
        self.metric_threads_combobox.addItems(metric_items)

    def on_sae_thread_changed(self, thread_size):
        """Handle SAE thread selection"""
        if not thread_size or thread_size not in self.sae_threads:
            return
            
        thread_data = self.sae_threads[thread_size]
        self.populate_thread_fields(thread_data)

    def on_metric_thread_changed(self, thread_size):
        """Handle Metric thread selection"""
        if not thread_size or thread_size not in self.metric_threads:
            return
            
        thread_data = self.metric_threads[thread_size]
        self.populate_thread_fields(thread_data)

    def calculate_npt_taper_change(self, z_start, z_end, lead_length, is_external=True):
        """Calculate X radius change for NPT taper"""
        import math
        
        # Total Z distance: difference between start and end + lead length
        z_distance = abs(z_end - z_start) + lead_length
        
        # NPT taper: 1.7899 degrees from centerline
        taper_angle_rad = math.radians(1.7899)
        
        # X radius change (short leg of right triangle)
        x_radius_change = z_distance * math.tan(taper_angle_rad)
        
        # Apply sign based on thread type:
        # External NPT: positive taper (pipe gets smaller toward end)
        # Internal NPT: negative taper (hole gets larger toward end)
        if is_external:
            return x_radius_change  # Positive for external
        else:
            return -x_radius_change  # Negative for internal

    def calculate_and_set_npt_taper(self, is_external=True):
        """Calculate NPT taper X change and update the taper widget"""
        try:
            # Get current Z positions and lead length using .text() method
            z_start = float(self.z_start_thread_rh_ext.text()) if self.z_start_thread_rh_ext.text() else 0.0
            z_end = float(self.z_end_thread_rh_ext.text()) if self.z_end_thread_rh_ext.text() else 0.0
            lead_length = float(self.lead_length_thread_rh_ext.text()) if self.lead_length_thread_rh_ext.text() else 0.0
            
            # Calculate X radius change with proper sign
            x_change = self.calculate_npt_taper_change(z_start, z_end, lead_length, is_external)
            
            # Set the calculated value in the taper widget
            self.taper_thread_ext.setValue(x_change)
            
        except Exception as e:
            # If we can't get the values or calculation fails, set to 0
            self.taper_thread_ext.setValue(0.0)

    def populate_thread_fields(self, thread_data):
        """Populate VCPSettingsLineEdit widgets with thread data"""
        
        # Calculate depth of cut (half the difference between major and minor)
        depth = (thread_data['e_maj'] - thread_data['e_min']) / 2
        
        # Populate shared widgets (no LH/RH variants)
        self.pitch_thread_ext.setValue(thread_data['pitch'])
        self.x_start_diam_thread_ext.setValue(thread_data['e_maj'])
        self.x_end_diam_thread_ext.setValue(thread_data['e_min'])
        self.depth_of_cut_thread_ext.setValue(depth)
        
        # Populate BOTH LH and RH lead length widgets with the CSV data
        self.lead_length_thread_lh_ext.setValue(thread_data['l_len'])
        self.lead_length_thread_rh_ext.setValue(thread_data['l_len'])
        
        # Handle NPT taper calculation
        thread_desc = thread_data.get('description', '')
        if 'NPT' in thread_desc.upper():
            # External threads always get positive taper
            self.calculate_and_set_npt_taper(is_external=True)
        else:
            # Clear taper for non-NPT threads (straight threads)
            self.taper_thread_ext.setValue(0.0)

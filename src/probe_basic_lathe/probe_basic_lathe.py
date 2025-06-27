#!/usr/bin/env python

import os
import sys
import importlib.util
import json

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
        
        # Initialize thread data containers
        self.sae_threads = {}
        self.metric_threads = {}
        self.custom_threads = {}
        
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
        
        # Populate combo boxes with loaded thread data
        self.populate_thread_combos()
        
        # Connect thread combo boxes (matching the working version's approach)
        if hasattr(self, 'sae_ext_threads_combobox'):
            self.sae_ext_threads_combobox.currentTextChanged.connect(self.on_sae_thread_changed)
        if hasattr(self, 'metric_ext_threads_combobox'):
            self.metric_ext_threads_combobox.currentTextChanged.connect(self.on_metric_thread_changed)
        if hasattr(self, 'custom_ext_threads_combobox'):
            self.custom_ext_threads_combobox.currentTextChanged.connect(self.on_custom_thread_changed)
        
        # Also connect internal combo boxes to the same handlers (since they use the same thread data)
        if hasattr(self, 'sae_threads_int_combobox'):
            self.sae_threads_int_combobox.currentTextChanged.connect(self.on_sae_thread_changed)
        if hasattr(self, 'metric_threads_int_combobox'):
            self.metric_threads_int_combobox.currentTextChanged.connect(self.on_metric_thread_changed)
        if hasattr(self, 'custom_threads_int_combobox'):
            self.custom_threads_int_combobox.currentTextChanged.connect(self.on_custom_thread_changed)

        # Connect tap combo boxes to the same handlers (since they use the same thread data)
        if hasattr(self, 'sae_tap_combobox'):
            self.sae_tap_combobox.currentTextChanged.connect(self.on_sae_thread_changed)
        if hasattr(self, 'metric_tap_combobox'):
            self.metric_tap_combobox.currentTextChanged.connect(self.on_metric_thread_changed)
        
        # Connect thread store buttons
        self.connect_thread_store_buttons()

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

    def resolve_config_path(self, path):
        """Resolve a path from INI file relative to the config directory"""
        import os
        
        # Expand user home directory if present
        expanded_path = os.path.expanduser(path)
        
        # If it's already an absolute path, return as-is
        if os.path.isabs(expanded_path):
            return expanded_path
        
        # For relative paths, resolve relative to the INI file directory
        ini_file_path = os.getenv("INI_FILE_NAME")
        if ini_file_path:
            config_dir = os.path.dirname(os.path.abspath(ini_file_path))
            resolved_path = os.path.join(config_dir, expanded_path)
            return resolved_path
        else:
            # Fallback: resolve relative to current directory
            return os.path.abspath(expanded_path)

    def get_machine_units(self):
        """Get machine units from INI file"""
        try:
            linear_units = INIFILE.find("TRAJ", "LINEAR_UNITS")
            if linear_units:
                linear_units = linear_units.strip().lower()
                if linear_units in ['mm', 'millimeter', 'metric']:
                    return 'mm'
                elif linear_units in ['inch', 'in', 'imperial']:
                    return 'inch'
            LOG.warning(f"Unknown or missing LINEAR_UNITS: {linear_units}, defaulting to inch")
            return 'inch'
        except Exception as e:
            LOG.error(f"Error reading LINEAR_UNITS from INI: {e}")
            return 'inch'

    def load_thread_data(self):
        """Load thread data from JSON files"""
        try:
            import json
            import os
            
            # Initialize containers
            self.sae_threads = {}
            self.metric_threads = {}
            self.custom_threads = {}
            
            # Get machine units
            self.machine_units = self.get_machine_units()
            LOG.info(f"Machine units from INI: {self.machine_units}")
            
            LOG.info("Starting thread data loading...")
            
            # Determine file suffixes based on machine units
            if self.machine_units == 'mm':
                sae_suffix = '_mm'
                metric_suffix = '_mm'
            else:  # inch
                sae_suffix = '_inch'
                metric_suffix = '_inch'
            
            # Load SAE threads (from installation directory)
            sae_file = os.path.join(VCP_DIR, f'../widgets/conversational/threads_sae{sae_suffix}.json')
            LOG.info(f"Loading SAE threads from: {sae_file}")
            
            if os.path.exists(sae_file):
                try:
                    with open(sae_file, 'r') as f:
                        data = json.load(f)
                        self.sae_threads = data.get('sae_threads', {})
                        LOG.info(f"Loaded {len(self.sae_threads)} SAE threads ({self.machine_units} units)")
                except Exception as e:
                    LOG.error(f"Error loading SAE threads: {e}")
                    self.sae_threads = {}
            else:
                LOG.warning(f"SAE threads file not found: {sae_file}")
            
            # Load Metric threads (from installation directory)
            metric_file = os.path.join(VCP_DIR, f'../widgets/conversational/threads_metric{metric_suffix}.json')
            LOG.info(f"Loading Metric threads from: {metric_file}")
            
            if os.path.exists(metric_file):
                try:
                    with open(metric_file, 'r') as f:
                        data = json.load(f)
                        self.metric_threads = data.get('metric_threads', {})
                        LOG.info(f"Loaded {len(self.metric_threads)} metric threads ({self.machine_units} units)")
                except Exception as e:
                    LOG.error(f"Error loading metric threads: {e}")
                    self.metric_threads = {}
            else:
                LOG.warning(f"Metric threads file not found: {metric_file}")
            
            # Load Custom threads
            custom_threads_file = INIFILE.find("DISPLAY", "USER_CUSTOM_THREADS_FILE")
            LOG.info(f"Custom threads file setting from INI: '{custom_threads_file}'")
            
            if custom_threads_file:
                # Get the config directory (where the INI file is located)
                ini_file_path = os.getenv("INI_FILE_NAME")
                LOG.info(f"INI_FILE_NAME environment variable: '{ini_file_path}'")
                
                if ini_file_path:
                    config_dir = os.path.dirname(os.path.abspath(ini_file_path))
                    LOG.info(f"Config directory resolved to: '{config_dir}'")
                    
                    custom_file_path = os.path.join(config_dir, custom_threads_file)
                    LOG.info(f"Full custom threads path: '{custom_file_path}'")
                    LOG.info(f"Custom threads file exists: {os.path.exists(custom_file_path)}")
                    
                    if os.path.exists(custom_file_path):
                        try:
                            LOG.info(f"Attempting to read custom threads file...")
                            with open(custom_file_path, 'r') as f:
                                file_content = f.read()
                                LOG.info(f"File content length: {len(file_content)} characters")
                                
                                # Parse JSON
                                data = json.loads(file_content)
                                LOG.info(f"JSON parsed successfully. Keys: {list(data.keys())}")
                                
                                self.custom_threads = data.get('custom_threads', {})
                                LOG.info(f"Custom threads extracted: {list(self.custom_threads.keys())}")
                                LOG.info(f"Loaded {len(self.custom_threads)} custom threads")
                        except json.JSONDecodeError as e:
                            LOG.error(f"JSON decode error in custom threads file: {e}")
                        except Exception as e:
                            LOG.error(f"Error loading custom threads: {e}")
                    else:
                        LOG.warning(f"Custom threads file not found at: {custom_file_path}")
                        # Let's also check what files ARE in that directory
                        try:
                            config_files = os.listdir(config_dir)
                            LOG.info(f"Files in config directory: {config_files}")
                        except Exception as e:
                            LOG.error(f"Error listing config directory: {e}")
                else:
                    LOG.warning("Could not determine config directory (INI_FILE_NAME not set)")
            else:
                LOG.warning("No USER_CUSTOM_THREADS_FILE setting found in INI file")
                # Let's also show what settings ARE available
                try:
                    display_section = {}
                    for option in INIFILE.options("DISPLAY"):
                        display_section[option] = INIFILE.find("DISPLAY", option)
                    LOG.info(f"Available DISPLAY section settings: {display_section}")
                except Exception as e:
                    LOG.error(f"Error reading DISPLAY section: {e}")
                
            LOG.info(f"Thread loading complete. SAE: {len(self.sae_threads)}, Metric: {len(self.metric_threads)}, Custom: {len(self.custom_threads)}")
                
        except Exception as e:
            LOG.error(f"Error in load_thread_data: {e}")
            # Ensure we have empty containers even if loading fails
            self.sae_threads = {}
            self.metric_threads = {}
            self.custom_threads = {}

    def load_custom_threads(self):
        """Load custom thread data (universal file with unit metadata)"""
        try:
            import json
            
            custom_file_path = self.get_custom_threads_file_path()
            
            if custom_file_path and os.path.exists(custom_file_path):
                try:
                    LOG.info(f"Loading custom threads from: {custom_file_path}")
                    with open(custom_file_path, 'r') as f:
                        data = json.load(f)
                        all_custom_threads = data.get('custom_threads', {})
                        
                        # Load all custom threads but log unit information
                        self.custom_threads = {}
                        for thread_name, thread_data in all_custom_threads.items():
                            thread_units = thread_data.get('units', 'unknown')
                            if thread_units != self.machine_units and thread_units != 'unknown':
                                LOG.info(f"Custom thread '{thread_name}' is in {thread_units} units (machine: {self.machine_units})")
                            self.custom_threads[thread_name] = thread_data
                        
                        LOG.info(f"Loaded {len(self.custom_threads)} custom threads")
                except Exception as e:
                    LOG.error(f"Error loading custom threads: {e}")
            else:
                if custom_file_path:
                    LOG.info(f"Custom threads file not found, creating: {custom_file_path}")
                    self.create_default_custom_threads_file(custom_file_path)
                else:
                    LOG.warning("Could not determine custom threads file path")
                    
        except Exception as e:
            LOG.error(f"Error in load_custom_threads: {e}")

    def get_custom_threads_file_path(self):
        """Get the path to the custom threads file (universal)"""
        try:
            custom_threads_file = INIFILE.find("DISPLAY", "USER_CUSTOM_THREADS_FILE") or "threads_custom.json"
            
            # Get the config directory (where the INI file is located)
            ini_file_path = os.getenv("INI_FILE_NAME")
            if ini_file_path:
                config_dir = os.path.dirname(os.path.abspath(ini_file_path))
                return os.path.join(config_dir, custom_threads_file)
            return None
        except Exception as e:
            LOG.error(f"Error determining custom threads file path: {e}")
            return None

    def create_default_custom_threads_file(self, file_path):
        """Create a default custom threads file if it doesn't exist"""
        try:
            import json
            
            # Create universal template (starts empty except for template)
            template = {
                "custom_threads": {
                    "BLANK-TEMPLATE": {
                        "pitch": 0.0000 if self.machine_units == 'inch' else 0.000,
                        "external": {
                            "major_diameter": 0.0000 if self.machine_units == 'inch' else 0.000,
                            "minor_diameter": 0.0000 if self.machine_units == 'inch' else 0.000,
                            "pitch_diameter": 0.0000 if self.machine_units == 'inch' else 0.000
                        },
                        "internal": {
                            "major_diameter": 0.0000 if self.machine_units == 'inch' else 0.000,
                            "minor_diameter": 0.0000 if self.machine_units == 'inch' else 0.000,
                            "pitch_diameter": 0.0000 if self.machine_units == 'inch' else 0.000
                        },
                        "lead_length": 0.0000 if self.machine_units == 'inch' else 0.000,
                        "description": "NONE",
                        "thread_type": "CUSTOM",
                        "npt_taper": False,
                        "units": self.machine_units,
                        "drill_sizes": {
                            "tap_drill": "NONE",
                            "clearance_close": "NONE",
                            "clearance_free": "NONE"
                        }
                    }
                }
            }
            
            with open(file_path, 'w') as f:
                json.dump(template, f, indent=2)
            
            LOG.info(f"Created default custom threads file: {file_path}")
            self.custom_threads = template.get('custom_threads', {})
            
        except Exception as e:
            LOG.error(f"Error creating default custom threads file: {e}")

    def save_custom_thread(self, thread_name, thread_data):
        """Save a custom thread to the universal JSON file"""
        try:
            import json
            
            # Get the custom threads file path
            custom_file_path = self.get_custom_threads_file_path()
            
            if not custom_file_path:
                LOG.error("Could not determine custom threads file path")
                return False
            
            # Load existing custom threads or create new structure
            if os.path.exists(custom_file_path):
                try:
                    with open(custom_file_path, 'r') as f:
                        data = json.load(f)
                except Exception as e:
                    LOG.error(f"Error reading existing custom threads file: {e}")
                    data = {"custom_threads": {}}
            else:
                data = {"custom_threads": {}}
            
            # Add or update the thread
            data["custom_threads"][thread_name] = thread_data
            
            # Save back to file
            with open(custom_file_path, 'w') as f:
                json.dump(data, f, indent=2)
            
            # Update our in-memory copy
            self.custom_threads[thread_name] = thread_data
            
            # Refresh the combo boxes
            self.populate_thread_combos()
            
            LOG.info(f"Saved custom thread '{thread_name}' to {custom_file_path} ({thread_data.get('units', 'unknown')} units)")
            return True
            
        except Exception as e:
            LOG.error(f"Error saving custom thread: {e}")
            return False

    def load_thread_data(self):
        """Load thread data from JSON files"""
        try:
            import json
            import os
            
            # Initialize containers
            self.sae_threads = {}
            self.metric_threads = {}
            self.custom_threads = {}
            
            # Get machine units
            self.machine_units = self.get_machine_units()
            LOG.info(f"Machine units from INI: {self.machine_units}")
            
            LOG.info("Starting thread data loading...")
            
            # Determine file suffixes based on machine units
            if self.machine_units == 'mm':
                sae_suffix = '_mm'
                metric_suffix = '_mm'
            else:  # inch
                sae_suffix = '_inch'
                metric_suffix = '_inch'
            
            # Load SAE threads (from installation directory)
            sae_file = os.path.join(VCP_DIR, f'../widgets/conversational/threads_sae{sae_suffix}.json')
            LOG.info(f"Loading SAE threads from: {sae_file}")
            
            if os.path.exists(sae_file):
                try:
                    with open(sae_file, 'r') as f:
                        data = json.load(f)
                        self.sae_threads = data.get('sae_threads', {})
                        LOG.info(f"Loaded {len(self.sae_threads)} SAE threads ({self.machine_units} units)")
                except Exception as e:
                    LOG.error(f"Error loading SAE threads: {e}")
                    self.sae_threads = {}
            else:
                LOG.warning(f"SAE threads file not found: {sae_file}")
            
            # Load Metric threads (from installation directory)
            metric_file = os.path.join(VCP_DIR, f'../widgets/conversational/threads_metric{metric_suffix}.json')
            LOG.info(f"Loading Metric threads from: {metric_file}")
            
            if os.path.exists(metric_file):
                try:
                    with open(metric_file, 'r') as f:
                        data = json.load(f)
                        self.metric_threads = data.get('metric_threads', {})
                        LOG.info(f"Loaded {len(self.metric_threads)} metric threads ({self.machine_units} units)")
                except Exception as e:
                    LOG.error(f"Error loading metric threads: {e}")
                    self.metric_threads = {}
            else:
                LOG.warning(f"Metric threads file not found: {metric_file}")
            
            # Load Custom threads
            custom_threads_file = INIFILE.find("DISPLAY", "USER_CUSTOM_THREADS_FILE")
            LOG.info(f"Custom threads file setting from INI: '{custom_threads_file}'")
            
            if custom_threads_file:
                # Get the config directory (where the INI file is located)
                ini_file_path = os.getenv("INI_FILE_NAME")
                LOG.info(f"INI_FILE_NAME environment variable: '{ini_file_path}'")
                
                if ini_file_path:
                    config_dir = os.path.dirname(os.path.abspath(ini_file_path))
                    LOG.info(f"Config directory resolved to: '{config_dir}'")
                    
                    custom_file_path = os.path.join(config_dir, custom_threads_file)
                    LOG.info(f"Full custom threads path: '{custom_file_path}'")
                    LOG.info(f"Custom threads file exists: {os.path.exists(custom_file_path)}")
                    
                    if os.path.exists(custom_file_path):
                        try:
                            LOG.info(f"Attempting to read custom threads file...")
                            with open(custom_file_path, 'r') as f:
                                file_content = f.read()
                                LOG.info(f"File content length: {len(file_content)} characters")
                                
                                # Parse JSON
                                data = json.loads(file_content)
                                LOG.info(f"JSON parsed successfully. Keys: {list(data.keys())}")
                                
                                self.custom_threads = data.get('custom_threads', {})
                                LOG.info(f"Custom threads extracted: {list(self.custom_threads.keys())}")
                                LOG.info(f"Loaded {len(self.custom_threads)} custom threads")
                        except json.JSONDecodeError as e:
                            LOG.error(f"JSON decode error in custom threads file: {e}")
                        except Exception as e:
                            LOG.error(f"Error loading custom threads: {e}")
                    else:
                        LOG.warning(f"Custom threads file not found at: {custom_file_path}")
                        # Let's also check what files ARE in that directory
                        try:
                            config_files = os.listdir(config_dir)
                            LOG.info(f"Files in config directory: {config_files}")
                        except Exception as e:
                            LOG.error(f"Error listing config directory: {e}")
                else:
                    LOG.warning("Could not determine config directory (INI_FILE_NAME not set)")
            else:
                LOG.warning("No USER_CUSTOM_THREADS_FILE setting found in INI file")
                # Let's also show what settings ARE available
                try:
                    display_section = {}
                    for option in INIFILE.options("DISPLAY"):
                        display_section[option] = INIFILE.find("DISPLAY", option)
                    LOG.info(f"Available DISPLAY section settings: {display_section}")
                except Exception as e:
                    LOG.error(f"Error reading DISPLAY section: {e}")
                
            LOG.info(f"Thread loading complete. SAE: {len(self.sae_threads)}, Metric: {len(self.metric_threads)}, Custom: {len(self.custom_threads)}")
                
        except Exception as e:
            LOG.error(f"Error in load_thread_data: {e}")
            # Ensure we have empty containers even if loading fails
            if not hasattr(self, 'sae_threads'):
                self.sae_threads = {}
            if not hasattr(self, 'metric_threads'):
                self.metric_threads = {}
            if not hasattr(self, 'custom_threads'):
                self.custom_threads = {}

    def connect_thread_store_buttons(self):
        """Connect the custom thread store buttons"""
        try:
            if hasattr(self, 'store_custom_ext_thread'):
                self.store_custom_ext_thread.clicked.connect(self.store_external_thread)
                LOG.info("Connected external thread store button")
            
            if hasattr(self, 'store_custom_int_thread'):
                self.store_custom_int_thread.clicked.connect(self.store_internal_thread)
                LOG.info("Connected internal thread store button")
        except Exception as e:
            LOG.error(f"Error connecting thread store buttons: {e}")

    def get_current_external_thread_values(self):
        """Collect current external thread values from UI"""
        values = {}
        
        try:
            # Basic thread parameters - use .text() for line edits, .value() for spinboxes/DROs
            if hasattr(self, 'pitch_thread_ext'):
                try:
                    # Try .value() first (for DROs/spinboxes), then .text() (for line edits)
                    if hasattr(self.pitch_thread_ext, 'value'):
                        values['pitch'] = float(self.pitch_thread_ext.value() or 0)
                    else:
                        values['pitch'] = float(self.pitch_thread_ext.text() or 0)
                except (ValueError, AttributeError):
                    values['pitch'] = 0.0
            
            # External thread diameters - these come from the conversational fields
            if hasattr(self, 'x_start_diam_thread_ext'):
                try:
                    if hasattr(self.x_start_diam_thread_ext, 'value'):
                        major_diam = float(self.x_start_diam_thread_ext.value() or 0)
                    else:
                        major_diam = float(self.x_start_diam_thread_ext.text() or 0)
                    
                    minor_diam = 0
                    if hasattr(self, 'x_end_diam_thread_ext'):
                        if hasattr(self.x_end_diam_thread_ext, 'value'):
                            minor_diam = float(self.x_end_diam_thread_ext.value() or 0)
                        else:
                            minor_diam = float(self.x_end_diam_thread_ext.text() or 0)
                    
                    values['external'] = {
                        'major_diameter': major_diam,
                        'minor_diameter': minor_diam,
                        'pitch_diameter': (major_diam + minor_diam) / 2 if minor_diam else major_diam
                    }
                except (ValueError, AttributeError):
                    values['external'] = {'major_diameter': 0, 'minor_diameter': 0, 'pitch_diameter': 0}
            
            # Internal thread diameters - estimated from external for dialog pre-fill
            if 'external' in values:
                major = values['external']['major_diameter']
                minor = values['external']['minor_diameter']
                pitch = values.get('pitch', 0)
                values['internal'] = {
                    'major_diameter': major + (pitch * 0.25),  # Rough estimate
                    'minor_diameter': minor,
                    'pitch_diameter': (major + minor) / 2
                }
            
            # Lead length calculation
            if hasattr(self, 'z_start_thread_rh_ext') and hasattr(self, 'z_end_thread_rh_ext'):
                try:
                    if hasattr(self.z_start_thread_rh_ext, 'value'):
                        z_start = float(self.z_start_thread_rh_ext.value() or 0)
                        z_end = float(self.z_end_thread_rh_ext.value() or 0)
                    else:
                        z_start = float(self.z_start_thread_rh_ext.text() or 0)
                        z_end = float(self.z_end_thread_rh_ext.text() or 0)
                    values['lead_length'] = abs(z_end - z_start)
                except (ValueError, AttributeError):
                    values['lead_length'] = 0.0
            
            # Default values
            values['thread_type'] = 'Custom'
            values['npt_taper'] = False
            values['drill_sizes'] = {
                'tap_drill': '',
                'clearance_close': '',
                'clearance_free': ''
            }
            
        except Exception as e:
            LOG.error(f"Error getting external thread values: {e}")
            
        return values

    def get_current_internal_thread_values(self):
        """Collect current internal thread values from UI"""
        values = {}
        
        try:
            # Basic thread parameters
            if hasattr(self, 'pitch_thread_int'):
                try:
                    if hasattr(self.pitch_thread_int, 'value'):
                        values['pitch'] = float(self.pitch_thread_int.value() or 0)
                    else:
                        values['pitch'] = float(self.pitch_thread_int.text() or 0)
                except (ValueError, AttributeError):
                    values['pitch'] = 0.0
            
            # Internal thread diameters
            if hasattr(self, 'x_start_diam_thread_int') and hasattr(self, 'x_end_diam_thread_int'):
                try:
                    if hasattr(self.x_start_diam_thread_int, 'value'):
                        start_diam = float(self.x_start_diam_thread_int.value() or 0)
                        end_diam = float(self.x_end_diam_thread_int.value() or 0)
                    else:
                        start_diam = float(self.x_start_diam_thread_int.text() or 0)
                        end_diam = float(self.x_end_diam_thread_int.text() or 0)
                    
                    values['internal'] = {
                        'major_diameter': max(start_diam, end_diam),  # Larger diameter is major for internal
                        'minor_diameter': min(start_diam, end_diam),  # Smaller diameter is minor for internal
                        'pitch_diameter': (start_diam + end_diam) / 2
                    }
                    
                    # External thread diameters - estimated for dialog pre-fill
                    pitch = values.get('pitch', 0)
                    values['external'] = {
                        'major_diameter': values['internal']['minor_diameter'],  # External minor ≈ internal major
                        'minor_diameter': values['internal']['minor_diameter'] - (pitch * 0.75),  # Rough estimate
                        'pitch_diameter': values['internal']['pitch_diameter']
                    }
                except (ValueError, AttributeError):
                    values['internal'] = {'major_diameter': 0, 'minor_diameter': 0, 'pitch_diameter': 0}
                    values['external'] = {'major_diameter': 0, 'minor_diameter': 0, 'pitch_diameter': 0}
            
            # Lead length calculation
            if hasattr(self, 'z_start_thread_rh_int') and hasattr(self, 'z_end_thread_rh_int'):
                try:
                    if hasattr(self.z_start_thread_rh_int, 'value'):
                        z_start = float(self.z_start_thread_rh_int.value() or 0)
                        z_end = float(self.z_end_thread_rh_int.value() or 0)
                    else:
                        z_start = float(self.z_start_thread_rh_int.text() or 0)
                        z_end = float(self.z_end_thread_rh_int.text() or 0)
                    values['lead_length'] = abs(z_end - z_start)
                except (ValueError, AttributeError):
                    values['lead_length'] = 0.0
            
            # Default values
            values['thread_type'] = 'Custom'
            values['npt_taper'] = False
            values['drill_sizes'] = {
                'tap_drill': '',
                'clearance_close': '',
                'clearance_free': ''
            }
            
        except Exception as e:
            LOG.error(f"Error getting internal thread values: {e}")
            
        return values

    def store_external_thread(self):
        """Open dialog to store current external thread as custom thread"""
        try:
            from .custom_thread_dialog import CustomThreadDialog
            
            # Get current values from UI
            current_values = self.get_current_external_thread_values()
            
            # Try to get the currently selected thread data to pre-populate more fields
            selected_thread_data = self.get_currently_selected_thread_data()
            
            # Get thread source type for informational display
            thread_source_type = None
            if selected_thread_data:
                thread_source_type = selected_thread_data.get('thread_type')
                # Merge selected thread data with current UI values
                current_values = self.merge_thread_data(selected_thread_data, current_values)
            
            # Open dialog - data is always in machine units
            dialog = CustomThreadDialog(self, current_values, thread_source_type)
            if dialog.exec_() == dialog.Accepted:
                # Get the stored thread name and data from dialog attributes
                thread_name = dialog.thread_name
                thread_data = dialog.thread_data
                if thread_name and thread_data:
                    self.save_custom_thread(thread_name, thread_data)
                    
        except Exception as e:
            LOG.error(f"Error storing external thread: {e}")
            from qtpy.QtWidgets import QMessageBox
            QMessageBox.critical(self, "Error", f"Failed to store custom thread: {str(e)}")

    def store_internal_thread(self):
        """Open dialog to store current internal thread as custom thread"""
        try:
            from .custom_thread_dialog import CustomThreadDialog
            
            # Get current values from UI
            current_values = self.get_current_internal_thread_values()
            
            # Try to get the currently selected thread data for context
            selected_thread_data = self.get_currently_selected_thread_data()
            
            # Get thread source type for informational display (not for unit determination)
            thread_source_type = None
            if selected_thread_data:
                thread_source_type = selected_thread_data.get('thread_type')
                # Merge selected thread data with current UI values for internal
                current_values = self.merge_thread_data(selected_thread_data, current_values)
            
            # Open dialog - data is always in machine units, source type is just informational
            dialog = CustomThreadDialog(self, current_values, thread_source_type)
            if dialog.exec_() == dialog.Accepted:
                # Get the stored thread name and data from dialog attributes
                thread_name = dialog.thread_name
                thread_data = dialog.thread_data
                if thread_name and thread_data:
                    self.save_custom_thread(thread_name, thread_data)
                    
        except Exception as e:
            LOG.error(f"Error storing internal thread: {e}")
            from qtpy.QtWidgets import QMessageBox
            QMessageBox.critical(self, "Error", f"Failed to store custom thread: {str(e)}")

    def save_custom_thread(self, thread_name, thread_data):
        """Save a custom thread to the JSON file"""
        try:
            # Get the custom threads file path
            custom_threads_file = self.get_custom_threads_file_path()
            
            # Load existing custom threads
            custom_threads = {}
            if os.path.exists(custom_threads_file):
                try:
                    with open(custom_threads_file, 'r') as f:
                        data = json.load(f)
                        custom_threads = data.get('custom_threads', {})
                except Exception as e:
                    LOG.error(f"Error loading existing custom threads: {e}")
            
            # Add new thread
            custom_threads[thread_name] = thread_data
            
            # Save back to file
            thread_file_data = {
                "custom_threads": custom_threads
            }
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(custom_threads_file), exist_ok=True)
            
            with open(custom_threads_file, 'w') as f:
                json.dump(thread_file_data, f, indent=2)
            
            LOG.info(f"Saved custom thread '{thread_name}' to {custom_threads_file}")
            
            # Reload thread data and refresh combo boxes
            self.load_thread_data()
            self.populate_thread_combos()
            
            # Show success message
            from qtpy.QtWidgets import QMessageBox
            QMessageBox.information(self, "Success", 
                                  f"Custom thread '{thread_name}' has been saved successfully!")
            
        except Exception as e:
            LOG.error(f"Error saving custom thread: {e}")
            from qtpy.QtWidgets import QMessageBox
            QMessageBox.critical(self, "Error", f"Failed to save custom thread: {str(e)}")

    def get_custom_threads_file_path(self):
        """Get the path to the custom threads JSON file"""
        try:
            # Get from INI file
            config_dir = os.path.dirname(os.environ.get('INI_FILE_NAME', ''))
            custom_threads_filename = INIFILE.find('PROBE_BASIC_LATHE', 'USER_CUSTOM_THREADS_FILE') or 'threads_custom.json'
            return os.path.join(config_dir, custom_threads_filename)
        except:
            # Fallback
            return os.path.join(os.path.expanduser('~'), '.config', 'probe_basic_lathe', 'threads_custom.json')

    def on_sae_thread_changed(self, thread_name):
        """Handle SAE thread selection"""
        if not thread_name or thread_name.startswith("---"):
            return
        
        if thread_name in self.sae_threads:
            thread_data = self.sae_threads[thread_name]
            
            # Determine which operation this is for based on the sender
            sender = self.sender()
            operation = "all"  # default fallback
            
            if sender == getattr(self, 'sae_ext_threads_combobox', None):
                operation = "external"
            elif sender == getattr(self, 'sae_threads_int_combobox', None):
                operation = "internal"
            elif sender == getattr(self, 'sae_tap_combobox', None):
                operation = "tap"
            
            self.populate_thread_fields(thread_data, operation)

    def on_metric_thread_changed(self, thread_name):
        """Handle metric thread selection"""
        if not thread_name or thread_name.startswith("---"):
            return
            
        if thread_name in self.metric_threads:
            thread_data = self.metric_threads[thread_name]
            
            # Determine which operation this is for based on the sender
            sender = self.sender()
            operation = "all"  # default fallback
            
            if sender == getattr(self, 'metric_ext_threads_combobox', None):
                operation = "external"
            elif sender == getattr(self, 'metric_threads_int_combobox', None):
                operation = "internal"
            elif sender == getattr(self, 'metric_tap_combobox', None):
                operation = "tap"
            
            self.populate_thread_fields(thread_data, operation)

    def on_custom_thread_changed(self, thread_name):
        """Handle custom thread selection"""
        if not thread_name or thread_name.startswith("---"):
            return
            
        if thread_name in self.custom_threads:
            thread_data = self.custom_threads[thread_name]
            
            # Determine which operation this is for based on the sender
            sender = self.sender()
            operation = "all"  # default fallback
            
            if sender == getattr(self, 'custom_ext_threads_combobox', None):
                operation = "external"
            elif sender == getattr(self, 'custom_threads_int_combobox', None):
                operation = "internal"
            # Note: No custom tap combo box in current implementation
            
            self.populate_thread_fields(thread_data, operation)

    def populate_thread_fields(self, thread_data, operation="all"):
        """Populate thread parameter fields with selected thread data for specific operation"""
        try:
            from qtpyvcp.utilities.settings import setSetting
            
            # Get basic parameters
            pitch = thread_data.get('pitch', 0)
            lead_length = thread_data.get('lead_length', 0)
            external_data = thread_data.get('external', {})
            internal_data = thread_data.get('internal', {})
            thread_name = thread_data.get('description', 'Unknown thread')
            
            LOG.info(f"Populating thread fields for {operation}: {thread_name}")
            
            # Populate external thread fields only if operation is 'external' or 'all'
            if operation in ['external', 'all']:
                # Set external thread size (both setting and widget)
                try:
                    setSetting("thread-ext.size", thread_name)
                    LOG.info(f"Set external thread size setting to: {thread_name}")
                except Exception as e:
                    LOG.error(f"Error setting external thread size: {e}")
                
                # Also update the thread_ext_size widget directly if it exists
                if hasattr(self, 'thread_ext_size'):
                    try:
                        if hasattr(self.thread_ext_size, 'setText'):
                            self.thread_ext_size.setText(thread_name)
                        elif hasattr(self.thread_ext_size, 'setValue'):
                            self.thread_ext_size.setValue(thread_name)
                        LOG.info(f"Set external thread size widget to: {thread_name}")
                    except Exception as e:
                        LOG.error(f"Error setting external thread size widget: {e}")
                
                if hasattr(self, 'pitch_thread_ext'):
                    try:
                        if hasattr(self.pitch_thread_ext, 'setValue'):
                            self.pitch_thread_ext.setValue(pitch)
                        elif hasattr(self.pitch_thread_ext, 'setText'):
                            self.pitch_thread_ext.setText(str(pitch))
                        LOG.info(f"Set external pitch to: {pitch}")
                    except Exception as e:
                        LOG.error(f"Error setting external pitch: {e}")
                
                # Set TPI for external threads
                if hasattr(self, 'tpi_thread_ext'):
                    try:
                        # Calculate TPI from pitch (TPI = 1/pitch for inch threads)
                        if pitch > 0:
                            tpi = 1.0 / pitch
                        else:
                            tpi = 0
                        
                        LOG.info(f"Calculated TPI: {tpi} from pitch: {pitch}")
                        
                        if hasattr(self.tpi_thread_ext, 'setValue'):
                            self.tpi_thread_ext.setValue(tpi)
                            LOG.info(f"Set external TPI widget (setValue) to: {tpi}")
                        elif hasattr(self.tpi_thread_ext, 'setText'):
                            self.tpi_thread_ext.setText(str(round(tpi, 1)))
                            LOG.info(f"Set external TPI widget (setText) to: {round(tpi, 1)}")
                        else:
                            LOG.warning(f"tpi_thread_ext widget has no setValue or setText method")
                            
                    except Exception as e:
                        LOG.error(f"Error setting external TPI: {e}")
                else:
                    LOG.warning("tpi_thread_ext widget not found")
                
                # External diameter fields
                if hasattr(self, 'x_start_diam_thread_ext'):
                    try:
                        major_diam = external_data.get('major_diameter', 0)
                        if hasattr(self.x_start_diam_thread_ext, 'setValue'):
                            self.x_start_diam_thread_ext.setValue(major_diam)
                        elif hasattr(self.x_start_diam_thread_ext, 'setText'):
                            self.x_start_diam_thread_ext.setText(str(major_diam))
                        LOG.info(f"Set external start diameter to: {major_diam}")
                    except Exception as e:
                        LOG.error(f"Error setting external start diameter: {e}")
                
                if hasattr(self, 'x_end_diam_thread_ext'):
                    try:
                        minor_diam = external_data.get('minor_diameter', 0)
                        if hasattr(self.x_end_diam_thread_ext, 'setValue'):
                            self.x_end_diam_thread_ext.setValue(minor_diam)
                        elif hasattr(self.x_end_diam_thread_ext, 'setText'):
                            self.x_end_diam_thread_ext.setText(str(minor_diam))
                        LOG.info(f"Set external end diameter to: {minor_diam}")
                    except Exception as e:
                        LOG.error(f"Error setting external end diameter: {e}")
                
                # Populate lead length for external threads (both left and right hand)
                for widget_name in ['lead_length_thread_lh_ext', 'lead_length_thread_rh_ext']:
                    if hasattr(self, widget_name):
                        try:
                            widget = getattr(self, widget_name)
                            if hasattr(widget, 'setValue'):
                                widget.setValue(lead_length)
                            elif hasattr(widget, 'setText'):
                                widget.setText(str(lead_length))
                            LOG.info(f"Set {widget_name} to: {lead_length}")
                        except Exception as e:
                            LOG.error(f"Error setting {widget_name}: {e}")
                
                # Handle NPT taper for external if applicable
                if thread_data.get('npt_taper', False):
                    LOG.info("Thread has NPT taper - setting npt-taper flag")
                    try:
                        setSetting("thread-ext.npt-taper", True)
                        LOG.info("Set thread-ext.npt-taper to True")
                    except Exception as e:
                        LOG.error(f"Error setting thread-ext.npt-taper: {e}")
                else:
                    try:
                        setSetting("thread-ext.npt-taper", False)
                    except Exception as e:
                        LOG.error(f"Error setting thread-ext.npt-taper to False: {e}")
            
            # Populate internal thread fields only if operation is 'internal' or 'all'
            if operation in ['internal', 'all']:
                # Set internal thread size (just like other field settings)
                try:
                    setSetting("thread-int.size", thread_name)
                    LOG.info(f"Set internal thread size to: {thread_name}")
                except Exception as e:
                    LOG.error(f"Error setting internal thread size: {e}")
                
                if hasattr(self, 'pitch_thread_int'):
                    try:
                        if hasattr(self.pitch_thread_int, 'setValue'):
                            self.pitch_thread_int.setValue(pitch)
                        elif hasattr(self.pitch_thread_int, 'setText'):
                            self.pitch_thread_int.setText(str(pitch))
                        LOG.info(f"Set internal pitch to: {pitch}")
                    except Exception as e:
                        LOG.error(f"Error setting internal pitch: {e}")
                
                # Set TPI for internal threads
                if hasattr(self, 'tpi_thread_int'):
                    try:
                        # Calculate TPI from pitch (TPI = 1/pitch for inch threads)
                        if pitch > 0:
                            tpi = 1.0 / pitch
                        else:
                            tpi = 0
                        
                        LOG.info(f"Calculated TPI: {tpi} from pitch: {pitch}")
                        
                        if hasattr(self.tpi_thread_int, 'setValue'):
                            self.tpi_thread_int.setValue(tpi)
                            LOG.info(f"Set internal TPI widget (setValue) to: {tpi}")
                        elif hasattr(self.tpi_thread_int, 'setText'):
                            self.tpi_thread_int.setText(str(round(tpi, 1)))
                            LOG.info(f"Set internal TPI widget (setText) to: {round(tpi, 1)}")
                        else:
                            LOG.warning(f"tpi_thread_int widget has no setValue or setText method")
                            
                    except Exception as e:
                        LOG.error(f"Error setting internal TPI: {e}")
                else:
                    LOG.warning("tpi_thread_int widget not found")
                
                # Internal diameter fields
                if hasattr(self, 'x_start_diam_thread_int'):
                    try:
                        major_diam = internal_data.get('major_diameter', 0)
                        if hasattr(self.x_start_diam_thread_int, 'setValue'):
                            self.x_start_diam_thread_int.setValue(major_diam)
                        elif hasattr(self.x_start_diam_thread_int, 'setText'):
                            self.x_start_diam_thread_int.setText(str(major_diam))
                        LOG.info(f"Set internal start diameter to: {major_diam}")
                    except Exception as e:
                        LOG.error(f"Error setting internal start diameter: {e}")
                
                if hasattr(self, 'x_end_diam_thread_int'):
                    try:
                        minor_diam = internal_data.get('minor_diameter', 0)
                        if hasattr(self.x_end_diam_thread_int, 'setValue'):
                            self.x_end_diam_thread_int.setValue(minor_diam)
                        elif hasattr(self.x_end_diam_thread_int, 'setText'):
                            self.x_end_diam_thread_int.setText(str(minor_diam))
                        LOG.info(f"Set internal end diameter to: {minor_diam}")
                    except Exception as e:
                        LOG.error(f"Error setting internal end diameter: {e}")
                
                # Populate lead length for internal threads (both left and right hand)
                for widget_name in ['lead_length_thread_lh_int', 'lead_length_thread_rh_int']:
                    if hasattr(self, widget_name):
                        try:
                            widget = getattr(self, widget_name)
                            if hasattr(widget, 'setValue'):
                                widget.setValue(lead_length)
                            elif hasattr(widget, 'setText'):
                                widget.setText(str(lead_length))
                            LOG.info(f"Set {widget_name} to: {lead_length}")
                        except Exception as e:
                            LOG.error(f"Error setting {widget_name}: {e}")
                
                # Handle NPT taper for internal if applicable
                if thread_data.get('npt_taper', False):
                    LOG.info("Thread has NPT taper - setting internal npt-taper flag")
                    try:
                        setSetting("thread-int.npt-taper", True)
                        LOG.info("Set thread-int.npt-taper to True")
                    except Exception as e:
                        LOG.error(f"Error setting thread-int.npt-taper: {e}")
                else:
                    try:
                        setSetting("thread-int.npt-taper", False)
                    except Exception as e:
                        LOG.error(f"Error setting thread-int.npt-taper to False: {e}")
            
            # Populate tap fields only if operation is 'tap' or 'all'
            if operation in ['tap', 'all']:
                # Set tap size (just like other field settings)
                try:
                    setSetting("tap.size", thread_name)
                    LOG.info(f"Set tap size to: {thread_name}")
                except Exception as e:
                    LOG.error(f"Error setting tap size: {e}")
                
                # Also update the tap_size_tap widget directly if it exists
                if hasattr(self, 'tap_size_tap'):
                    try:
                        if hasattr(self.tap_size_tap, 'setText'):
                            self.tap_size_tap.setText(thread_name)
                        elif hasattr(self.tap_size_tap, 'setValue'):
                            self.tap_size_tap.setValue(thread_name)
                        LOG.info(f"Set tap size widget to: {thread_name}")
                    except Exception as e:
                        LOG.error(f"Error setting tap size widget: {e}")
                
                # Set pitch for tap
                if hasattr(self, 'pitch_thread_tap'):
                    try:
                        if hasattr(self.pitch_thread_tap, 'setValue'):
                            self.pitch_thread_tap.setValue(pitch)
                        elif hasattr(self.pitch_thread_tap, 'setText'):
                            self.pitch_thread_tap.setText(str(pitch))
                        LOG.info(f"Set tap pitch to: {pitch}")
                    except Exception as e:
                        LOG.error(f"Error setting tap pitch: {e}")
                
                # Set TPI for tap
                if hasattr(self, 'tpi_thread_tap'):
                    try:
                        # Calculate TPI from pitch (TPI = 1/pitch for inch threads)
                        if pitch > 0:
                            tpi = 1.0 / pitch
                        else:
                            tpi = 0
                        
                        LOG.info(f"Calculated TPI: {tpi} from pitch: {pitch}")
                        
                        if hasattr(self.tpi_thread_tap, 'setValue'):
                            self.tpi_thread_tap.setValue(tpi)
                            LOG.info(f"Set tap TPI widget (setValue) to: {tpi}")
                        elif hasattr(self.tpi_thread_tap, 'setText'):
                            self.tpi_thread_tap.setText(str(round(tpi, 1)))
                            LOG.info(f"Set tap TPI widget (setText) to: {round(tpi, 1)}")
                        else:
                            LOG.warning(f"tpi_thread_tap widget has no setValue or setText method")
                            
                    except Exception as e:
                        LOG.error(f"Error setting tap TPI: {e}")
                else:
                    LOG.warning("tpi_thread_tap widget not found")
                
                # Set hole diameter for tap (using drill_diam from drill_sizes if available)
                if hasattr(self, 'hole_diam_tap'):
                    drill_diam = None
                    drill_sizes = thread_data.get('drill_sizes', {})
                    # Try to get drill_diam as float, fallback to 0 if not found or not convertible
                    try:
                        drill_diam = float(drill_sizes.get('drill_diam', 0))
                    except Exception:
                        drill_diam = 0
                    self.hole_diam_tap.setValue(drill_diam)
                
                # Set drill size for tap
                if hasattr(self, 'drill_tap'):
                    try:
                        drill_sizes = thread_data.get('drill_sizes', {})
                        tap_drill = drill_sizes.get('tap_drill', 'NONE')
                        
                        # Format the decimal value to 4 decimal places if it contains parentheses
                        if '(' in tap_drill and ')' in tap_drill:
                            # Extract the parts: "#7 (0.201000000)" -> "#7" and "0.201000000"
                            parts = tap_drill.split('(')
                            if len(parts) == 2:
                                drill_name = parts[0].strip()
                                decimal_part = parts[1].replace(')', '').strip()
                                try:
                                    # Convert to float and format to 4 decimal places
                                    decimal_value = float(decimal_part)
                                    formatted_drill = f"{drill_name} ({decimal_value:.4f})"
                                    tap_drill = formatted_drill
                                except ValueError:
                                    # If conversion fails, use original value
                                    pass
                        
                        if hasattr(self.drill_tap, 'setText'):
                            self.drill_tap.setText(tap_drill)
                        elif hasattr(self.drill_tap, 'setValue'):
                            self.drill_tap.setValue(tap_drill)
                        LOG.info(f"Set tap drill size to: {tap_drill}")
                    except Exception as e:
                        LOG.error(f"Error setting tap drill size: {e}")
                
                LOG.info(f"Populated all tap fields for: {thread_name}")
            
        except Exception as e:
            LOG.error(f"Error populating thread fields: {e}")

    def populate_thread_combos(self):
        """Populate all thread combo boxes with data from JSON files"""
        try:
            # Get sorted thread lists
            sae_sorted = self.sort_threads_by_type_and_size(self.sae_threads)
            metric_sorted = self.sort_threads_by_type_and_size(self.metric_threads)
            custom_sorted = self.sort_threads_by_type_and_size(self.custom_threads)
            
            # Populate SAE external threads
            if hasattr(self, 'sae_ext_threads_combobox'):
                self.sae_ext_threads_combobox.clear()
                self.sae_ext_threads_combobox.addItem("")  # Empty default option
                for thread_name, thread_data in sae_sorted:
                    if thread_data is None:  # Category separator
                        self.sae_ext_threads_combobox.addItem(thread_name)
                        # Disable the separator item
                        model = self.sae_ext_threads_combobox.model()
                        item = model.item(self.sae_ext_threads_combobox.count() - 1)
                        if item:
                            item.setEnabled(False)
                    else:
                        self.sae_ext_threads_combobox.addItem(thread_name)
                LOG.info(f"Populated SAE external combo with {len(sae_sorted)} threads")
        
            # Populate Metric external threads
            if hasattr(self, 'metric_ext_threads_combobox'):
                self.metric_ext_threads_combobox.clear()
                self.metric_ext_threads_combobox.addItem("")  # Empty default option
                for thread_name, thread_data in metric_sorted:
                    if thread_data is None:  # Category separator
                        self.metric_ext_threads_combobox.addItem(thread_name)
                        # Disable the separator item
                        model = self.metric_ext_threads_combobox.model()
                        item = model.item(self.metric_ext_threads_combobox.count() - 1)
                        if item:
                            item.setEnabled(False)
                    else:
                        self.metric_ext_threads_combobox.addItem(thread_name)
                LOG.info(f"Populated Metric external combo with {len(metric_sorted)} threads")
                        
            # Populate Custom external threads
            if hasattr(self, 'custom_ext_threads_combobox'):
                self.custom_ext_threads_combobox.clear()
                self.custom_ext_threads_combobox.addItem("")  # Empty default option
                for thread_name, thread_data in custom_sorted:
                    if thread_data is None:  # Category separator
                        self.custom_ext_threads_combobox.addItem(thread_name)
                        # Disable the separator item
                        model = self.custom_ext_threads_combobox.model()
                        item = model.item(self.custom_ext_threads_combobox.count() - 1)
                        if item:
                            item.setEnabled(False)
                    else:
                        self.custom_ext_threads_combobox.addItem(thread_name)
                LOG.info(f"Populated Custom external combo with {len(custom_sorted)} threads")
            
            # Populate internal thread combos (same data, different widgets)
            if hasattr(self, 'sae_threads_int_combobox'):
                self.sae_threads_int_combobox.clear()
                self.sae_threads_int_combobox.addItem("")  # Empty default option
                for thread_name, thread_data in sae_sorted:
                    if thread_data is None:  # Category separator
                        self.sae_threads_int_combobox.addItem(thread_name)
                        # Disable the separator item
                        model = self.sae_threads_int_combobox.model()
                        item = model.item(self.sae_threads_int_combobox.count() - 1)
                        if item:
                            item.setEnabled(False)
                    else:
                        self.sae_threads_int_combobox.addItem(thread_name)
                LOG.info(f"Populated SAE internal combo with {len(sae_sorted)} threads")
                        
            if hasattr(self, 'metric_threads_int_combobox'):
                self.metric_threads_int_combobox.clear()
                self.metric_threads_int_combobox.addItem("")  # Empty default option
                for thread_name, thread_data in metric_sorted:
                    if thread_data is None:  # Category separator
                        self.metric_threads_int_combobox.addItem(thread_name)
                        # Disable the separator item
                        model = self.metric_threads_int_combobox.model()
                        item = model.item(self.metric_threads_int_combobox.count() - 1)
                        if item:
                            item.setEnabled(False)
                    else:
                        self.metric_threads_int_combobox.addItem(thread_name)
                LOG.info(f"Populated Metric internal combo with {len(metric_sorted)} threads")
                        
            if hasattr(self, 'custom_threads_int_combobox'):
                self.custom_threads_int_combobox.clear()
                self.custom_threads_int_combobox.addItem("")  # Empty default option
                for thread_name, thread_data in custom_sorted:
                    if thread_data is None:  # Category separator
                        self.custom_threads_int_combobox.addItem(thread_name)
                        # Disable the separator item
                        model = self.custom_threads_int_combobox.model()
                        item = model.item(self.custom_threads_int_combobox.count() - 1)
                        if item:
                            item.setEnabled(False)
                    else:
                        self.custom_threads_int_combobox.addItem(thread_name)
                LOG.info(f"Populated Custom internal combo with {len(custom_sorted)} threads")
            
            # Populate tap combo boxes (same data, different widgets)
            if hasattr(self, 'sae_tap_combobox'):
                self.sae_tap_combobox.clear()
                self.sae_tap_combobox.addItem("")  # Empty default option
                for thread_name, thread_data in sae_sorted:
                    if thread_data is None:  # Category separator
                        self.sae_tap_combobox.addItem(thread_name)
                        # Disable the separator item
                        model = self.sae_tap_combobox.model()
                        item = model.item(self.sae_tap_combobox.count() - 1)
                        if item:
                            item.setEnabled(False)
                    else:
                        self.sae_tap_combobox.addItem(thread_name)
                LOG.info(f"Populated SAE tap combo with {len(sae_sorted)} threads")
                        
            if hasattr(self, 'metric_tap_combobox'):
                self.metric_tap_combobox.clear()
                self.metric_tap_combobox.addItem("")  # Empty default option
                for thread_name, thread_data in metric_sorted:
                    if thread_data is None:  # Category separator
                        self.metric_tap_combobox.addItem(thread_name)
                        # Disable the separator item
                        model = self.metric_tap_combobox.model()
                        item = model.item(self.metric_tap_combobox.count() - 1)
                        if item:
                            item.setEnabled(False)
                    else:
                        self.metric_tap_combobox.addItem(thread_name)
                LOG.info(f"Populated Metric tap combo with {len(metric_sorted)} threads")
                        
        except Exception as e:
            LOG.error(f"Error populating thread combos: {e}")
    
    def sort_threads_by_type_and_size(self, threads_dict):
        """Sort threads by type and size for better organization"""
        
        def get_major_diameter(thread_data):
            """Extract major diameter for sorting"""
            try:
                # Use external major diameter as the sorting key
                return float(thread_data.get('external', {}).get('major_diameter', 0))
            except:
                return 0
        
        def get_thread_category(thread_name, thread_data):
            """Categorize thread by type"""
            thread_type = thread_data.get('thread_type', '').upper()
            description = thread_data.get('description', '').upper()
            
            # NPT/Tapered threads
            if (thread_data.get('npt_taper', False) or 
                'NPT' in thread_type or 'NPT' in description or 'NPT' in thread_name.upper()):
                return 1, "NPT/Tapered"
            
            # ACME threads
            if ('ACME' in thread_type or 'ACME' in description or 'ACME' in thread_name.upper()):
                return 2, "ACME" 
            
            # Custom threads (not UNC, UNF, or standard metric)
            if (thread_type == 'CUSTOM' or 
                ('UNC' not in thread_type and 'UNF' not in thread_type and 
                 'COARSE' not in thread_type and 'FINE' not in thread_type and
                 not thread_name.startswith('M') and 'Custom' in description)):
                return 3, "Custom"
            
            # Standard threads (UNC, UNF, Metric)
            return 0, "Standard"
        
        # Group threads by category
        categorized = {}
        for thread_name, thread_data in threads_dict.items():
            category_order, category_name = get_thread_category(thread_name, thread_data)
            if category_name not in categorized:
                categorized[category_name] = []
            categorized[category_name].append((thread_name, thread_data))
        
        # Sort each category by major diameter
        sorted_threads = []
        category_order = ["Standard", "NPT/Tapered", "ACME", "Custom"]
        
        for category in category_order:
            if category in categorized:
                # Sort threads in this category by major diameter
                category_threads = sorted(categorized[category], 
                                        key=lambda x: get_major_diameter(x[1]))
                
                # Add category separator (if not first category and has threads)
                if sorted_threads and category_threads:
                    sorted_threads.append(("--- " + category + " Threads ---", None))
                elif category_threads:  # First category, just add threads
                    pass
                
                # Add the sorted threads from this category
                sorted_threads.extend(category_threads)
        
        return sorted_threads

    def get_currently_selected_thread_data(self):
        """Get the currently selected thread data from combo boxes"""
        try:
            # Check SAE external combo
            if hasattr(self, 'sae_ext_threads_combobox'):
                current_text = self.sae_ext_threads_combobox.currentText()
                if current_text and current_text in self.sae_threads and not current_text.startswith("---"):
                    return {
                        'thread_name': current_text,
                        'thread_data': self.sae_threads[current_text],
                        'thread_type': 'SAE'
                    }
            
            # Check metric external combo
            if hasattr(self, 'metric_ext_threads_combobox'):
                current_text = self.metric_ext_threads_combobox.currentText()
                if current_text and current_text in self.metric_threads and not current_text.startswith("---"):
                    return {
                        'thread_name': current_text,
                        'thread_data': self.metric_threads[current_text],
                        'thread_type': 'Metric'
                    }
            
            # Check custom external combo
            if hasattr(self, 'custom_ext_threads_combobox'):
                current_text = self.custom_ext_threads_combobox.currentText()
                if current_text and current_text in self.custom_threads and not current_text.startswith("---"):
                    return {
                        'thread_name': current_text,
                        'thread_data': self.custom_threads[current_text],  # Fixed: was currentText
                        'thread_type': 'Custom'
                    }
            
            # Check internal combos as well
            if hasattr(self, 'sae_threads_int_combobox'):
                current_text = self.sae_threads_int_combobox.currentText()
                if current_text and current_text in self.sae_threads and not current_text.startswith("---"):
                    return {
                        'thread_name': current_text,
                        'thread_data': self.sae_threads[current_text],
                        'thread_type': 'SAE'
                    }
            
            if hasattr(self, 'metric_threads_int_combobox'):
                current_text = self.metric_threads_int_combobox.currentText()
                if current_text and current_text in self.metric_threads and not current_text.startswith("---"):
                    return {
                        'thread_name': current_text,
                        'thread_data': self.metric_threads[current_text],
                        'thread_type': 'Metric'
                    }
            
            if hasattr(self, 'custom_threads_int_combobox'):
                current_text = self.custom_threads_int_combobox.currentText()
                if current_text and current_text in self.custom_threads and not current_text.startswith("---"):
                    return {
                        'thread_name': current_text,
                        'thread_data': self.custom_threads[current_text],
                        'thread_type': 'Custom'
                    }
            
        except Exception as e:
            LOG.error(f"Error getting selected thread data: {e}")
        
        return None

    def merge_thread_data(self, selected_thread_data, current_values):
        """Merge selected thread data with current UI values - UI data takes priority except for specific thread parameters"""
        try:
            thread_name = selected_thread_data['thread_name']
            thread_data = selected_thread_data['thread_data']
            
            # Create the custom name with modifier
            custom_name = f"{thread_name} CUSTOM"
            
            # Start with current UI values as the base
            merged_values = current_values.copy()
            
            # Override UI lead_length with thread database lead_length (thread-specific parameter)
            if 'lead_length' in thread_data:
                merged_values['lead_length'] = thread_data['lead_length']
        
            # Only add data from JSON that's NOT available from UI
            # Add suggested name
            merged_values['suggested_name'] = custom_name
            merged_values['original_name'] = thread_name
            
            # Add description if not already set
            if 'description' not in merged_values or not merged_values.get('description'):
                merged_values['description'] = thread_data.get('description', '')
            
            # Add thread type from the JSON (override the default 'Custom')
            merged_values['thread_type'] = thread_data.get('thread_type', 'Custom')
            
            # Add drill sizes (these usually aren't in the UI)
            if 'drill_sizes' not in merged_values or not merged_values['drill_sizes'].get('tap_drill'):
                merged_values['drill_sizes'] = thread_data.get('drill_sizes', {
                    'tap_drill': '',
                    'clearance_close': '',
                    'clearance_free': ''
                })
            
            return merged_values
            
        except Exception as e:
            LOG.error(f"Error merging thread data: {e}")
            return current_values

    def on_thread_selection_changed(self):
        """Handle thread selection change"""
        try:
            # Get the currently selected thread data
            selected_thread_data = self.get_currently_selected_thread_data()
            
            if selected_thread_data:
                # Populate UI fields
                self.populate_thread_fields(selected_thread_data)
    
        except Exception as e:
            LOG.error(f"Error handling thread selection change: {e}")
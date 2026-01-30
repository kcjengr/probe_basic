#!/usr/bin/env python

import os
import sys
import importlib.util

import linuxcnc

from qtpy.QtCore import Slot, QRegExp
from qtpy.QtGui import QFontDatabase, QRegExpValidator, QTextCursor
from qtpyvcp.actions.machine_actions import issue_mdi
from qtpy.QtWidgets import QAbstractButton
from qtpy.QtWidgets import QAction, QWidget
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
        
        # M6 finder initialization
        self.m6_lines = []
        self.current_m6_index = 0
        self.find_m6_button.clicked.connect(self.on_find_m6_clicked)
        
        # Cycle start button interception for run from line functionality
        self.cycle_start_button.clicked.connect(self.on_cycle_start_clicked)
        
        self.load_user_tabs()
        
        self.load_user_buttons()

        self.load_user_dros()

        self.load_offset_dro()

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

        self.help_menu = self.menuBar().addMenu("Help")
        self.interactive_help_action = QAction("Interactive Help", self, checkable=True)
        self.interactive_help_action.setChecked(False)
        self.interactive_help_action.toggled.connect(self.toggle_tooltips)
        self.help_menu.addAction(self.interactive_help_action)
        self.store_original_tooltips()
        self.toggle_tooltips(False)  # Hide tooltips by default

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

    def store_original_tooltips(self):
        """Store the original tooltips for all widgets to restore later."""
        self._stored_tooltips = {}
        for widget in self.findChildren(QWidget):
            tooltip = widget.toolTip()
            if tooltip:  # Only store if a tooltip exists
                self._stored_tooltips[widget] = tooltip
                LOG.debug(f"Stored tooltip for {widget.objectName()}: {tooltip[:50]}...")

    def toggle_tooltips(self, enabled):
        """Show tooltips when Interactive Help is enabled, hide them otherwise."""
        LOG.info(f"Toggle tooltips: enabled={enabled}")
        count = 0
        for widget, original_tooltip in self._stored_tooltips.items():
            if enabled:
                # Interactive Help ON: Show tooltip with extended duration
                widget.setToolTip(original_tooltip)
                widget.setToolTipDuration(-1)  # Tooltip stays until mouse moves away
                count += 1
            else:
                # Interactive Help OFF: Clear tooltip to avoid distractions
                widget.setToolTip("")
        LOG.info(f"Toggled {count} tooltips")

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

    def extract_m6_line_numbers(self):
        """Extract line numbers containing M6 commands from the loaded G-code file."""
        m6_lines = []
        if not hasattr(self, 'gcodetextedit_2'):
            LOG.warning("gcodetextedit_2 not found")
            return m6_lines
        
        try:
            text = self.gcodetextedit_2.toPlainText()
            if not text:
                LOG.warning("No G-code loaded in gcodetextedit_2")
                return m6_lines
            
            for line_num, line in enumerate(text.split('\n'), start=1):
                # Search for M6 (tool change command) - case insensitive
                if 'M6' in line.upper():
                    m6_lines.append(line_num)
            
            LOG.info(f"Found {len(m6_lines)} M6 commands in G-code")
        except Exception as e:
            LOG.error(f"Error extracting M6 line numbers: {e}")
        
        return m6_lines

    @Slot()
    def on_find_m6_clicked(self):
        """Find next M6 command in the loaded G-code file and display line number."""
        # Re-extract M6 lines (in case file was reloaded)
        self.m6_lines = self.extract_m6_line_numbers()
        
        if not self.m6_lines:
            LOG.warning("No M6 commands found in G-code file")
            self.run_from_line_Num.setText("")
            return
        
        # Display the current M6 line number
        line_num = self.m6_lines[self.current_m6_index]
        self.run_from_line_Num.setText(str(line_num))
        LOG.info(f"M6 found at line {line_num}")
        
        # Scroll and highlight the M6 line in gcodetextedit_2
        self.scroll_to_line_in_gcode(line_num)
        
        # Advance to next M6 for next button click (wrap around at end)
        self.current_m6_index = (self.current_m6_index + 1) % len(self.m6_lines)

    def scroll_to_line_in_gcode(self, line_num):
        """Scroll and highlight a specific line in the G-code text editor."""
        if not hasattr(self, 'gcodetextedit_2'):
            return
        
        try:
            # Get the text cursor
            cursor = self.gcodetextedit_2.textCursor()
            
            # Move cursor to the beginning of the desired line
            # line_num is 1-based, so we need line_num - 1 blocks
            cursor.movePosition(QTextCursor.Start)
            for _ in range(line_num - 1):
                cursor.movePosition(QTextCursor.Down)
            
            # Select the entire line
            cursor.movePosition(QTextCursor.StartOfLine)
            cursor.movePosition(QTextCursor.EndOfLine, QTextCursor.KeepAnchor)
            
            # Set the cursor (this will scroll the view to show the line)
            self.gcodetextedit_2.setTextCursor(cursor)
            
            # Ensure the line is visible in the center of the view
            self.gcodetextedit_2.ensureCursorVisible()
            
            LOG.info(f"Scrolled to M6 line {line_num}")
        except Exception as e:
            LOG.error(f"Error scrolling to line {line_num}: {e}")

    @Slot()
    def on_cycle_start_clicked(self):
        """Intercept cycle start to check if running from M6 line is enabled."""
        if self.run_from_line_Btn.isChecked():
            # Run from the queued M6 line
            try:
                lineNum = int(self.run_from_line_Num.text())
                actions.program_actions.run(lineNum)
                LOG.info(f"Cycle started from M6 line {lineNum}")
            except ValueError:
                LOG.warning("No valid line number queued for run from line")
            finally:
                # Auto-uncheck the button after running
                self.run_from_line_Btn.setChecked(False)
        else:
            # Normal cycle start - just run the program normally
            actions.program_actions.run()
            LOG.info("Normal cycle start")

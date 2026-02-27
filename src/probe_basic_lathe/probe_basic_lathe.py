#!/usr/bin/env python

import os
import sys
import importlib.util

import linuxcnc

from qtpy.QtCore import Slot, QRegularExpression, QTimer
from qtpy.QtGui import QFontDatabase, QRegularExpressionValidator, QTextCursor, QPalette
from qtpyvcp.actions.machine_actions import issue_mdi
from qtpy.QtWidgets import QApplication, QAbstractButton, QMessageBox
from qtpy.QtWidgets import QAction, QWidget
from qtpy import uic

from qtpyvcp import actions
from qtpyvcp.utilities import logger
from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from qtpyvcp.utilities.settings import getSetting, setSetting

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from . import probe_basic_lathe_rc  # noqa: F401 - registers Qt resources

LOG = logger.getLogger('QtPyVCP.' + __name__)
VCP_DIR = os.path.abspath(os.path.dirname(__file__))
INIFILE = linuxcnc.ini(os.getenv("INI_FILE_NAME"))
MASTER_TOOL_DIALOG_POS_X = 400
MASTER_TOOL_DIALOG_POS_Y = 215
LIGHT_STYLESHEET_FILE = "probe_basic_lathe_light.qss"
DARK_STYLESHEET_FILE = "probe_basic_lathe_dark.qss"

# Add custom fonts
QFontDatabase.addApplicationFont(os.path.join(VCP_DIR, 'fonts/BebasKai.ttf'))


def _resolve_config_path(path_str: str):
    if not path_str:
        return None
    expanded = os.path.expanduser(path_str)
    if os.path.isabs(expanded):
        return expanded
    ini_file = os.getenv("INI_FILE_NAME")
    base_dir = os.path.dirname(ini_file) if ini_file else os.getcwd()
    return os.path.abspath(os.path.join(base_dir, expanded))

class ProbeBasicLathe(VCPMainWindow):
    """Main window class for the ProbeBasic VCP."""
    def __init__(self, *args, **kwargs):
        super(ProbeBasicLathe, self).__init__(*args, **kwargs)
        self.run_from_line_Num.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]*")))
        self.btnMdiBksp.clicked.connect(self.mdiBackSpace_clicked)
        self.btnMdiSpace.clicked.connect(self.mdiSpace_clicked)
        self.btnMdiLeft_arrow.clicked.connect(self.mdiLeftArrow_clicked)
        self.btnMdiRight_arrow.clicked.connect(self.mdiRightArrow_clicked)
        
        # M6 finder initialization
        self.m6_lines = []
        self.current_m6_index = 0
        self.find_m6_button.clicked.connect(self._find_m6_clicked)
        
        # Cycle start button interception for run from line functionality
        self.cycle_start_button.clicked.connect(self._cycle_start_clicked)
        
        self.load_user_tabs()
        
        self.load_user_buttons()

        self._connect_theme_tracking()
        self._apply_theme_stylesheet()

        from PySide6.QtCore import QTimer
        QTimer.singleShot(100, self._load_dros_after_ui)

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

        self._lathe_type = lathe_type
        if hasattr(self, "tabWidget") and hasattr(self, "main_tab"):
            self.tabWidget.currentChanged.connect(self._on_tab_changed_refresh_views)
        QTimer.singleShot(0, self._refresh_vtk_view)

        # Set tool offset mode (absolute or master_tool) from INI file
        master_tool_mode = INIFILE.find("DISPLAY", "MASTER_TOOL_OFFSET_MODE")
        if master_tool_mode:
            # Handle boolean-like values: true/True/1/yes = master mode, anything else = absolute
            is_master_mode = str(master_tool_mode).strip().lower() in ('true', '1', 'yes')
            mode_index = 1 if is_master_mode else 0
            if hasattr(self, "tool_offset_stacked_widget"):
                self.tool_offset_stacked_widget.setCurrentIndex(mode_index)
                LOG.info(f"Tool offset mode set to: {'MASTER_TOOL' if is_master_mode else 'ABSOLUTE'}")
        else:
            # Default to absolute mode (index 0) if not specified
            if hasattr(self, "tool_offset_stacked_widget"):
                self.tool_offset_stacked_widget.setCurrentIndex(0)
                LOG.info("MASTER_TOOL_OFFSET_MODE not found in INI, defaulting to ABSOLUTE mode")

        # Master tool promotion handling
        if hasattr(self, "master_tool_number"):
            # Load saved master tool number from settings
            saved_value = getSetting("touch-parameters.master-tool-number").getValue()
            if saved_value:
                self.master_tool_number.setText(str(int(saved_value)))
            # Connect to both signals - flag prevents double-execution
            self._master_tool_processing = False  # Flag to prevent double-execution
            self.master_tool_number.returnPressed.connect(self.on_master_tool_editing_finished)
            self.master_tool_number.editingFinished.connect(self.on_master_tool_editing_finished)

    def _is_dark_theme(self):
        app = QApplication.instance()
        if app is None:
            return False
        palette = app.palette()
        window_lightness = palette.color(QPalette.Window).lightness()
        base_lightness = palette.color(QPalette.Base).lightness()
        return ((window_lightness + base_lightness) / 2) < 128

    def _connect_theme_tracking(self):
        app = QApplication.instance()
        if app is None:
            return
        palette_changed = getattr(app, 'paletteChanged', None)
        if palette_changed is not None:
            try:
                palette_changed.connect(self._on_palette_changed)
            except Exception:
                LOG.exception("Failed to connect paletteChanged signal")

    def _on_palette_changed(self, *_args):
        QTimer.singleShot(0, self._apply_theme_stylesheet)

    def _apply_theme_stylesheet(self):
        dark_theme = self._is_dark_theme()
        stylesheet_file = DARK_STYLESHEET_FILE if dark_theme else LIGHT_STYLESHEET_FILE
        stylesheet_path = os.path.join(VCP_DIR, stylesheet_file)
        app = QApplication.instance()
        if app is None:
            return
        try:
            with open(stylesheet_path, 'r', encoding='utf-8') as style_file:
                app.setStyleSheet(style_file.read())
        except Exception:
            LOG.exception("Failed to load theme stylesheet: %s", stylesheet_path)

    def _position_master_dialog(self, msg_box):
        msg_box.adjustSize()
        msg_box.move(int(MASTER_TOOL_DIALOG_POS_X), int(MASTER_TOOL_DIALOG_POS_Y))

    def _on_tab_changed_refresh_views(self, index):
        if hasattr(self, "tabWidget") and self.tabWidget.widget(index) is getattr(self, "main_tab", None):
            QTimer.singleShot(0, self._refresh_vtk_view)

    def _refresh_vtk_view(self):
        if not hasattr(self, "vtkbackplot"):
            return
        try:
            if getattr(self, "_lathe_type", "LATHE") == "BACK_TOOL_LATHE":
                self.vtkbackplot.setViewXZ()
            else:
                self.vtkbackplot.setViewXZ2()
            self.vtkbackplot.update()
        except Exception:
            LOG.exception("Failed to refresh VTK backplot view")

    def _load_dros_after_ui(self):
        self.load_user_dros()
        self.load_offset_dro()
        for _timer_label in ("timerhours", "timerminutes", "timerseconds"):
            lbl = getattr(self, _timer_label, None)
            if lbl is not None:
                lbl.textFormat = "02.0f"

    def store_original_tooltips(self):
        """Store the original tooltips for all widgets to restore later."""
        self._stored_tooltips = {}
        for widget in self.findChildren(QWidget):
            tooltip = widget.toolTip()
            if tooltip:  # Only store if a tooltip exists
                self._stored_tooltips[widget] = tooltip
        LOG.debug("Stored %d widget tooltips", len(self._stored_tooltips))

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
        if not user_buttons_paths:
            return

        # user_buttons_layout is a QVBoxLayout; with QUiLoader fallback it may not
        # be set as an attribute, so fall back to findChild.
        from qtpy.QtWidgets import QVBoxLayout
        layout = getattr(self, "user_buttons_layout", None)
        if layout is None:
            layout = self.findChild(QVBoxLayout, "user_buttons_layout")
        if layout is None:
            LOG.error("user_buttons_layout not found on main window; skipping user buttons load")
            return

        for user_buttons_path in user_buttons_paths:
            user_buttons_path = _resolve_config_path(user_buttons_path)
            if not user_buttons_path or not os.path.isdir(user_buttons_path):
                continue
            user_button_folders = os.listdir(user_buttons_path)
            for user_button in user_button_folders:
                if not os.path.isdir(os.path.join(user_buttons_path, user_button)):
                    continue
                module_name = "user_buttons." + os.path.basename(user_buttons_path) + "." + user_button
                spec = importlib.util.spec_from_file_location(
                    module_name,
                    os.path.join(user_buttons_path, user_button, user_button + ".py")
                )
                self.user_button_modules[module_name] = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = self.user_button_modules[module_name]
                spec.loader.exec_module(self.user_button_modules[module_name])

                self.user_buttons[module_name] = self.user_button_modules[module_name].UserButton()
                layout.addWidget(self.user_buttons[module_name])

    def load_user_dros(self):
        self.user_dros_modules = {}
        self.user_dros = {}

        layout = getattr(self, "dro_display_layout", None)
        if layout is None:
            from qtpy.QtWidgets import QHBoxLayout
            layout = self.findChild(QHBoxLayout, "dro_display_layout")
        if layout is None:
            LOG.error("dro_display_layout not found on main window; skipping user DRO load")
            return

        dro_type = INIFILE.find("DISPLAY", "DRO_DISPLAY")
        if not dro_type:
            LOG.warning("No DRO_DISPLAY specified in INI.")
            return
        dro_type = dro_type.strip().lower()  # Normalize to lowercase

        user_dros_paths = INIFILE.findall("DISPLAY", "USER_DROS_PATH")

        for user_dros_path in user_dros_paths:
            user_dros_path = _resolve_config_path(user_dros_path)
            if not user_dros_path or not os.path.isdir(user_dros_path):
                continue
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
                    layout.addWidget(self.user_dros[module_name])
                return  # Only load one DRO, then exit

    def load_offset_dro(self):
        layout = getattr(self, "offset_dro_layout", None)
        if layout is None:
            from qtpy.QtWidgets import QVBoxLayout
            layout = self.findChild(QVBoxLayout, "offset_dro_layout")
        if layout is None:
            LOG.error("offset_dro_layout not found on main window; skipping offset DRO load")
            return
        # Clear any existing widgets from the layout
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        dro_type = INIFILE.find("DISPLAY", "DRO_DISPLAY")
        if not dro_type:
            LOG.warning("No DRO_DISPLAY specified in INI.")
            return
        dro_type = dro_type.strip().lower()  # Normalize to lowercase

        user_dros_paths = INIFILE.findall("DISPLAY", "USER_DROS_PATH")

        for user_dros_path in user_dros_paths:
            user_dros_path = _resolve_config_path(user_dros_path)
            if not user_dros_path or not os.path.isdir(user_dros_path):
                continue
            dro_folder = f"{dro_type}_dros"
            offset_ui_file = f"offset_dros_{dro_type}.ui"
            offset_ui_path = os.path.join(user_dros_path, dro_folder, offset_ui_file)
            if os.path.isfile(offset_ui_path):
                offset_widget = QWidget()
                uic.loadUi(offset_ui_path, offset_widget)
                layout.addWidget(offset_widget)
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

    @Slot()
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
        
        # Skip special buttons that have their own handlers
        if not char or len(char) > 1:
            return
            
        text = self.mdiEntry.text() or 'null'
        cursor_pos = self.mdiEntry.cursorPosition()
        
        if text != 'null':
            new_text = text[:cursor_pos] + char + text[cursor_pos:]
        else:
            new_text = char
            
        self.mdiEntry.setText(new_text)
        self.mdiEntry.setFocus()
        self.mdiEntry.setCursorPosition(cursor_pos + 1)
        self.mdiEntry.deselect()

    def mdiBackSpace_clicked(parent):
        if len(parent.mdiEntry.text()) > 0:
            cursor_pos = parent.mdiEntry.cursorPosition()
            if cursor_pos > 0:
                text = parent.mdiEntry.text()
                new_text = text[:cursor_pos-1] + text[cursor_pos:]
                parent.mdiEntry.setText(new_text)
                parent.mdiEntry.setFocus()
                parent.mdiEntry.setCursorPosition(cursor_pos - 1)
                parent.mdiEntry.deselect()

    def mdiSpace_clicked(parent):
        text = parent.mdiEntry.text() or 'null'
        cursor_pos = parent.mdiEntry.cursorPosition()
        # if no text then do not add a space
        if text != 'null':
            new_text = text[:cursor_pos] + ' ' + text[cursor_pos:]
            parent.mdiEntry.setText(new_text)
            parent.mdiEntry.setFocus()
            parent.mdiEntry.setCursorPosition(cursor_pos + 1)
            parent.mdiEntry.deselect()

    def mdiLeftArrow_clicked(parent):
        cursor_pos = parent.mdiEntry.cursorPosition()
        if cursor_pos > 0:
            parent.mdiEntry.setFocus()
            parent.mdiEntry.setCursorPosition(cursor_pos - 1)
            parent.mdiEntry.deselect()

    def mdiRightArrow_clicked(parent):
        cursor_pos = parent.mdiEntry.cursorPosition()
        if cursor_pos < len(parent.mdiEntry.text()):
            parent.mdiEntry.setFocus()
            parent.mdiEntry.setCursorPosition(cursor_pos + 1)
            parent.mdiEntry.deselect()

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
    def _find_m6_clicked(self):
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
    def _cycle_start_clicked(self):
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
        # Normal cycle start is handled by the button's bound actionName (program.run).

    # Master Tool Promotion Methods
    def on_master_tool_editing_finished(self):
        """Handle master tool number change with confirmation dialog."""
        from qtpyvcp.plugins import getPlugin
        
        # Prevent double-execution from multiple signals
        if self._master_tool_processing:
            return
        self._master_tool_processing = True
        
        try:
            # Get new value from widget
            try:
                new_master = int(self.master_tool_number.text()) if self.master_tool_number.text() else None
            except ValueError:
                LOG.warning("Invalid master tool number entered")
                return
            
            # Get current saved value
            saved_value = getSetting("touch-parameters.master-tool-number").getValue()
            current_master = int(saved_value) if saved_value else None
            
            # If no change, do nothing
            if new_master == current_master:
                return
            
            # If invalid, revert
            if new_master is None:
                if current_master is not None:
                    self.master_tool_number.setText(str(current_master))
                else:
                    self.master_tool_number.setText("")
                return
            
            # Show confirmation dialog
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Question)
            msg.setWindowTitle("Promote Tool to Master")
            msg.setText(f"Promoting Tool {new_master} to Master Tool!")
            msg.setInformativeText(
                "This action will Recalculate all stored tool offsets relative to the new master tool."
                )
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            yes_btn = msg.button(QMessageBox.Yes)
            yes_btn.setText("Yes, Promote New Tool")
            cancel_btn = msg.button(QMessageBox.Cancel)
            cancel_btn.setText("Cancel")
            msg.setDefaultButton(QMessageBox.Cancel)
            self._position_master_dialog(msg)
            
            result = msg.exec_()
            
            if result == QMessageBox.Yes:
                # User confirmed - promote the tool
                success = self.promote_tool_to_master(new_master, current_master)
                
                if success:
                    # Save the new master tool number to settings
                    setSetting("touch-parameters.master-tool-number", new_master)
                    LOG.info(f"Saved master tool number: {new_master}")
                    
                    # Show confirmation
                    confirm_msg = QMessageBox(self)
                    confirm_msg.setIcon(QMessageBox.Information)
                    confirm_msg.setWindowTitle("Master Tool Promoted")
                    confirm_msg.setText(f"Tool {new_master} is now the Master Tool")
                    confirm_msg.setInformativeText(
                        "All tool offsets have been recalculated.\n"
                        f"Tool {new_master} offset is now (X0, Z0)."
                    )
                    confirm_msg.setStandardButtons(QMessageBox.Ok)
                    self._position_master_dialog(confirm_msg)
                    
                    confirm_msg.exec_()
                else:
                    # Promotion failed - revert to original
                    if current_master is not None:
                        self.master_tool_number.setText(str(current_master))
                    else:
                        self.master_tool_number.setText("")
                    LOG.warning("Tool promotion failed, reverted to original value")
            else:
                # User cancelled - revert to original master tool number
                if current_master is not None:
                    self.master_tool_number.setText(str(current_master))
                else:
                    self.master_tool_number.setText("")
                LOG.info(f"Tool promotion cancelled, reverted to: {current_master}")
        
        finally:
            # Reset flag after processing
            self._master_tool_processing = False

    def promote_tool_to_master(self, new_master_tool, old_master_tool):
        """
        Promote a secondary tool to become the new master tool.
        Recalculates all tool offsets to maintain spatial relationships.
        
        Args:
            new_master_tool (int): Tool number to promote to master
            old_master_tool (int): Current master tool number (can be None)
        
        Returns:
            bool: True if successful, False otherwise
        """
        from qtpyvcp.plugins import getPlugin
        
        LOG.info(f"Promoting tool {new_master_tool} to master (was tool {old_master_tool})")
        
        try:
            # Get tool table plugin
            tooltable = getPlugin('tooltable')
            if not tooltable:
                LOG.error("Tool table plugin not found")
                return False
            
            # Get current tool table
            tool_table = tooltable.getToolTable()
            if not tool_table:
                LOG.error("Could not read tool table")
                return False
            
            # Check if new master tool exists
            if new_master_tool not in tool_table:
                LOG.error(f"Tool {new_master_tool} not found in tool table")
                return False
            
            # Get the offset of the tool being promoted
            promoted_tool_data = tool_table[new_master_tool]
            promoted_x_offset = promoted_tool_data.get('X', 0.0)
            promoted_z_offset = promoted_tool_data.get('Z', 0.0)
            
            LOG.info(f"Promoted tool current offsets - X: {promoted_x_offset}, Z: {promoted_z_offset}")
            
            # Recalculate all tool offsets
            for tool_num in tool_table.keys():
                if tool_num == 0:  # Skip the "No Tool" entry
                    continue
                
                tool_data = tool_table[tool_num]
                old_x = tool_data.get('X', 0.0)
                old_z = tool_data.get('Z', 0.0)
                
                # New offset = old offset - promoted tool offset
                new_x = old_x - promoted_x_offset
                new_z = old_z - promoted_z_offset
                
                # Update the tool data
                tool_data['X'] = new_x
                tool_data['Z'] = new_z
                
                LOG.info(f"Tool {tool_num}: X {old_x:.6f} -> {new_x:.6f}, Z {old_z:.6f} -> {new_z:.6f}")
            
            # Save the updated tool table with explicit zeros to prevent omission
            self.save_tool_table_with_zeros(tooltable, tool_table)
            
            # Reload tool table in LinuxCNC
            CMD = linuxcnc.command()
            CMD.load_tool_table()
            
            # Reload in UI
            tooltable.loadToolTable()
            
            LOG.info(f"Successfully promoted tool {new_master_tool} to master")
            return True
            
        except Exception as e:
            LOG.error(f"Error promoting tool to master: {e}", exc_info=True)
            return False

    def save_tool_table_with_zeros(self, tooltable, tool_table):
        """
        Save tool table ensuring zero values are explicitly written.
        This prevents LinuxCNC from omitting columns with zero values.
        """
        import os
        from qtpyvcp.utilities.info import Info
        
        INFO = Info()
        tool_file = INFO.getToolTableFile()
        
        if not tool_file:
            LOG.error("Could not determine tool table file path")
            return
        
        # Get columns to write (typically XZDR for lathe)
        columns = list(tooltable.columns) if hasattr(tooltable, 'columns') else ['T', 'P', 'X', 'Z', 'D', 'R']
        
        # Ensure P is in columns
        if 'P' not in columns:
            columns.insert(1, 'P')
        
        LOG.info(f"Saving tool table to: {tool_file}")
        LOG.info(f"Columns: {columns}")
        
        try:
            lines = []
            
            # Preserve header if it exists
            if hasattr(tooltable, 'orig_header_lines') and tooltable.orig_header_lines:
                lines.extend(tooltable.orig_header_lines)
            
            # Create table header
            header_items = []
            for col in columns:
                if col == 'R':
                    continue
                if col in 'TPQ':
                    w = 6 - (1 if col == columns[0] else 0)
                else:
                    w = 12 - (1 if col == columns[0] else 0)
                col_label = tooltable.COLUMN_LABELS.get(col, col) if hasattr(tooltable, 'COLUMN_LABELS') else col
                header_items.append('{:<{w}}'.format(col_label, w=w))
            header_items.append('Remark')
            lines.append(';' + ' '.join(header_items))
            
            # Write each tool with explicit zeros
            for tool_num in sorted(tool_table.keys())[1:]:  # Skip tool 0
                tool_data = tool_table[tool_num]
                items = []
                
                for col in columns:
                    if col == 'R':
                        continue
                    
                    val = tool_data.get(col, 0.0 if col not in 'TPQ' else 0)
                    
                    if col in 'TPQ':
                        # Integer columns
                        items.append('{col}{val:<{w}}'.format(col=col, val=int(val), w=6))
                    else:
                        # Float columns - explicitly format zeros
                        items.append('{col}{val:<+{w}.6f}'.format(col=col, val=val, w=12))
                
                # Add remark
                comment = tool_data.get('R', '')
                if comment:
                    items.append('; ' + comment)
                
                lines.append(''.join(items))
            
            # Write to file
            with open(tool_file, 'w') as f:
                f.write('\n'.join(lines))
                f.write('\n')  # Ensure final newline
            
            LOG.info(f"Tool table saved successfully with {len(tool_table)-1} tools")
            
        except Exception as e:
            LOG.error(f"Error saving tool table: {e}", exc_info=True)
            raise

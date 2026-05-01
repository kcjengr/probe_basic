#!/usr/bin/env python

import os
import sys
import re
import importlib.util

import linuxcnc

from PySide6.QtCore import Slot, QRegularExpression, QTimer, Qt
from PySide6.QtGui import QFontDatabase, QRegularExpressionValidator, QTextCursor, QPalette, QAction
from qtpyvcp.actions.machine_actions import issue_mdi
from PySide6.QtWidgets import QAbstractButton, QMessageBox, QApplication
from PySide6.QtWidgets import QWidget

from qtpyvcp import actions
from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger
from qtpyvcp.utilities.runtime_ui_loader import load_ui as load_runtime_ui
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


def _load_ui(ui_path, parent):
    return load_runtime_ui(ui_path, parent)


# Add custom fonts
QFontDatabase.addApplicationFont(os.path.join(VCP_DIR, 'fonts/ProbeBasicBebasMono.ttf'))


def _resolve_config_path(path_str: str):
    if not path_str:
        return None
    expanded = os.path.expanduser(path_str)
    if os.path.isabs(expanded):
        return expanded
    ini_file = os.getenv("INI_FILE_NAME")
    base_dir = os.path.dirname(ini_file) if ini_file else os.getcwd()
    return os.path.abspath(os.path.join(base_dir, expanded))


def _ini_bool(value, default=False):
    if value is None:
        return default

    normalized = str(value).strip().lower()
    if normalized in ("1", "true", "yes", "on", "y"):
        return True
    if normalized in ("0", "false", "no", "off", "n", ""):
        return False
    return default


def _import_module_from_path(module_name: str, module_path: str):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to create module spec for {module_name} from {module_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module

    module_dir = os.path.dirname(os.path.abspath(module_path))
    added_to_path = False
    if module_dir and module_dir not in sys.path:
        sys.path.insert(0, module_dir)
        added_to_path = True

    spec.loader.exec_module(module)

    # Cleanup the temporary import path only after a successful import.
    if added_to_path and module_dir in sys.path:
        sys.path.remove(module_dir)

    return module


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
        self._applying_external_program_selection = False
        self._install_gcode_run_from_line_context_menu()
        self._install_gcode_selected_line_sync()
        
        self.load_user_tabs()
        
        self.load_user_buttons()
        self._theme_preference_mode = self._theme_preference()
        self._connect_theme_tracking()
        self._apply_system_theme_stylesheet()

        from PySide6.QtCore import QTimer
        QTimer.singleShot(100, self._load_dros_after_ui)

        # --- Startup Tab Selection Logic (using tab text property) ---
        startup_tab_value = getSetting("startup-settings.user-startup-tab").getValue()
        if hasattr(self, "tabWidget") and hasattr(self, "startup_tab_combobox"):
            # Populate ComboBox with current tab texts if not already set
            self.startup_tab_combobox.clear()
            for i in range(self.tabWidget.count()):
                self.startup_tab_combobox.addItem(self.tabWidget.tabText(i))
            # Set ComboBox to saved tab index/text, or default to first tab
            idx = self._resolve_startup_tab_index(startup_tab_value)
            self.startup_tab_combobox.setCurrentIndex(idx if idx != -1 else 0)
            # Connect to save selection and switch tab on change
            self.startup_tab_combobox.currentIndexChanged.connect(self.on_startup_tab_combobox_changed)
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

        lathe_mode = _ini_bool(INIFILE.find("DISPLAY", "LATHE"), default=False)
        lathe_back_mode = _ini_bool(INIFILE.find("DISPLAY", "BACK_TOOL_LATHE"), default=False)

        if lathe_back_mode:
            lathe_type = "BACK_TOOL_LATHE"
            self.vtkbackplot.setViewXZ()
        elif lathe_mode:
            lathe_type = "LATHE"
            self.vtkbackplot.setViewXZ2()
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

        self._initialize_master_tool_controls()

    # Master Tool Promotion Methods
    def _initialize_master_tool_controls(self):
        """Initialize strict master-tool widget behavior and signal wiring."""
        master_tool_widget = self._master_tool_widget()

        # Keep manual control so confirmation occurs before committing.
        master_tool_widget.autoWriteEnabled = False

        self._last_master_tool_value = self._read_master_tool_var_value()
        if self._last_master_tool_value is not None:
            self._set_master_tool_widget_value(self._last_master_tool_value)

        # Connect to both signals; guard flag prevents double execution.
        self._master_tool_processing = False
        master_tool_widget.returnPressed.connect(self.on_master_tool_editing_finished)
        master_tool_widget.editingFinished.connect(self.on_master_tool_editing_finished)

    def _master_tool_widget(self):
        widget = getattr(self, "master_tool_number_3100", None)
        if widget is None:
            raise AttributeError(
                "Required widget 'master_tool_number_3100' not found in ProbeBasicLathe UI"
            )
        return widget

    def _read_master_tool_var_value(self):
        value = self._master_tool_widget().readParameterFromVarFile()

        if value in (None, ""):
            return None

        parsed = self._parse_master_tool_number(value)
        if parsed is None:
            LOG.warning("Master tool var value is not integer-compatible: %s", value)
        return parsed

    def _parse_master_tool_number(self, raw_value):
        """Parse widget/var input into a non-negative integer master tool number.

        Accepts integer-like text such as "5" or "5.0000" and rejects fractional values.
        """
        if raw_value is None:
            return None

        if isinstance(raw_value, (int, float)):
            numeric_value = float(raw_value)
        elif isinstance(raw_value, str):
            raw_text = raw_value.strip()
            if raw_text == "":
                return None

            if not re.fullmatch(r"[+-]?\d+(\.\d+)?", raw_text):
                return None

            numeric_value = float(raw_text)
        else:
            return None

        if numeric_value < 0:
            return None

        rounded_value = int(round(numeric_value))
        if abs(numeric_value - rounded_value) > 1e-6:
            return None

        return rounded_value

    def _set_master_tool_widget_value(self, tool_number, persist=False):
        master_tool_widget = self._master_tool_widget()

        if tool_number is None:
            master_tool_widget.setText("")
        else:
            master_tool_widget.setValue(float(tool_number))

        if persist:
            master_tool_widget.writeToLinuxCNC(force=True)

    def on_master_tool_editing_finished(self):
        """Handle master tool number change with confirmation dialog."""

        # Prevent double-execution from multiple signals
        if self._master_tool_processing:
            return
        self._master_tool_processing = True

        master_tool_widget = self._master_tool_widget()
        new_text = master_tool_widget.text()
        new_master = self._parse_master_tool_number(new_text)

        # Get current saved value from LinuxCNC var storage
        current_master = self._read_master_tool_var_value()
        if current_master is None:
            current_master = getattr(self, "_last_master_tool_value", None)

        # If no change, do nothing
        if new_master == current_master:
            self._master_tool_processing = False
            return

        if new_master is None:
            if new_text.strip() != "":
                LOG.warning("Invalid master tool number entered: %s", new_text)
            self._set_master_tool_widget_value(current_master)
            self._master_tool_processing = False
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

        result = msg.exec()

        if result == QMessageBox.Yes:
            # User confirmed - promote the tool
            success = self.promote_tool_to_master(new_master, current_master)

            if success:
                # Save the new master tool number to LinuxCNC var storage
                self._set_master_tool_widget_value(new_master, persist=True)
                self._last_master_tool_value = new_master
                LOG.info(f"Saved master tool number to var storage: {new_master}")

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

                confirm_msg.exec()
            else:
                # Promotion failed - revert to original
                self._set_master_tool_widget_value(current_master)
                LOG.warning("Tool promotion failed, reverted to original value")
        else:
            # User cancelled - revert to original master tool number
            self._set_master_tool_widget_value(current_master)
            LOG.info(f"Tool promotion cancelled, reverted to: {current_master}")

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
            raise RuntimeError("Could not determine tool table file path")

        # Get columns to write (typically XZDR for lathe)
        columns = list(tooltable.columns)

        # Ensure P is in columns
        if 'P' not in columns:
            columns.insert(1, 'P')

        LOG.info(f"Saving tool table to: {tool_file}")
        LOG.info(f"Columns: {columns}")

        lines = []

        # Preserve header if it exists
        if tooltable.orig_header_lines:
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
            col_label = tooltable.COLUMN_LABELS.get(col, col)
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

    def _position_master_dialog(self, msg_box):
        msg_box.adjustSize()
        msg_box.move(int(MASTER_TOOL_DIALOG_POS_X), int(MASTER_TOOL_DIALOG_POS_Y))

    def _theme_preference(self):
        theme_color = (INIFILE.find("DISPLAY", "THEME_COLOR") or "light").strip().lower()
        if theme_color in ("light", "dark", "system"):
            return theme_color
        return "light"

    def _is_dark_theme(self):
        app = QApplication.instance()
        if app is None:
            return False
        palette = app.palette()
        window_lightness = palette.color(QPalette.Window).lightness()
        base_lightness = palette.color(QPalette.Base).lightness()
        return ((window_lightness + base_lightness) / 2) < 128

    def _connect_theme_tracking(self):
        if self._theme_preference_mode != 'system':
            return
        app = QApplication.instance()
        if app is None:
            raise RuntimeError("QApplication instance is required for system theme tracking")

        app.paletteChanged.connect(self._on_palette_changed)

    def _on_palette_changed(self, *_args):
        if self._theme_preference_mode != 'system':
            return
        QTimer.singleShot(0, self._apply_system_theme_stylesheet)

    def _apply_system_theme_stylesheet(self):
        if self._theme_preference_mode != 'system':
            return
        dark_theme = self._is_dark_theme()
        stylesheet_file = DARK_STYLESHEET_FILE if dark_theme else LIGHT_STYLESHEET_FILE
        stylesheet_path = os.path.join(VCP_DIR, stylesheet_file)
        app = QApplication.instance()
        if app is None:
            raise RuntimeError("QApplication instance is required for stylesheet application")

        with open(stylesheet_path, 'r', encoding='utf-8') as style_file:
            app.setStyleSheet(style_file.read())

    def _on_tab_changed_refresh_views(self, index):
        if hasattr(self, "tabWidget") and self.tabWidget.widget(index) is getattr(self, "main_tab", None):
            QTimer.singleShot(0, self._refresh_vtk_view)

    def _refresh_vtk_view(self):
        if getattr(self, "_lathe_type", "LATHE") == "BACK_TOOL_LATHE":
            self.vtkbackplot.setViewXZ()
        else:
            self.vtkbackplot.setViewXZ2()
        self.vtkbackplot.update()

    def _load_dros_after_ui(self):
        self.load_user_dros()
        self.load_offset_dro()
        for _timer_label in ("timerhours", "timerminutes", "timerseconds"):
            lbl = getattr(self, _timer_label, None)
            if lbl is not None:
                if hasattr(lbl, 'valueFormat'):
                    lbl.valueFormat = "02.0f"

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
        from PySide6.QtWidgets import QVBoxLayout
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
                module_file = os.path.join(user_buttons_path, user_button, user_button + ".py")
                self.user_button_modules[module_name] = _import_module_from_path(module_name, module_file)

                self.user_buttons[module_name] = self.user_button_modules[module_name].UserButton()
                layout.addWidget(self.user_buttons[module_name])

    def load_user_dros(self):
        self.user_dros_modules = {}
        self.user_dros = {}

        layout = getattr(self, "dro_display_layout", None)
        if layout is None:
            from PySide6.QtWidgets import QHBoxLayout
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
                module = _import_module_from_path(module_name, dro_py_path)
                if hasattr(module, "UserDRO"):
                    self.user_dros[module_name] = module.UserDRO()
                    layout.addWidget(self.user_dros[module_name])
                return  # Only load one DRO, then exit

    def load_offset_dro(self):
        layout = getattr(self, "offset_dro_layout", None)
        if layout is None:
            from PySide6.QtWidgets import QVBoxLayout
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
                offset_widget = _load_ui(offset_ui_path, self)
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
                module_file = os.path.join(os.path.dirname(user_tabs_path), user_tab, user_tab + ".py")
                self.user_tab_modules[module_name] = _import_module_from_path(module_name, module_file)
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
    @Slot(object)
    def on_spindlerpmsourcebtnGroup_buttonClicked(self, button):
        if button is None or not hasattr(button, 'property'):
            return
        page = button.property('page')
        if page is None:
            return
        self.spindle_rpm_source_widget.setCurrentIndex(int(page))

    def set_startup_tab_by_text(self, tab_text):
        """Set the main tab widget to the tab matching tab_text."""
        if hasattr(self, "tabWidget"):
            for i in range(self.tabWidget.count()):
                if self.tabWidget.tabText(i).strip() == tab_text.strip():
                    self.tabWidget.setCurrentIndex(i)
                    break

    def _resolve_startup_tab_index(self, saved_value):
        """Resolve saved startup-tab setting to a valid combobox index."""
        if not hasattr(self, "startup_tab_combobox"):
            return -1

        item_count = self.startup_tab_combobox.count()
        if item_count == 0:
            return -1

        value_text = "" if saved_value is None else str(saved_value).strip()
        if not value_text:
            return -1

        if value_text.isdigit():
            value_index = int(value_text)
            if 0 <= value_index < item_count:
                return value_index

        for idx in range(item_count):
            if self.startup_tab_combobox.itemText(idx).strip() == value_text:
                return idx

        return -1

    def on_startup_tab_combobox_changed(self, value):
        """Save ComboBox selection for startup, but do not change the current tab."""
        setSetting("startup-settings.user-startup-tab", self.startup_tab_combobox.currentIndex())
        # Do not call self.set_startup_tab_by_text(value)

    def extract_m6_line_numbers(self):
        """Extract line numbers containing M6 commands from the loaded G-code file."""
        m6_lines = []
        editor = self._resolve_m6_editor()
        text = editor.toPlainText()
        if not text:
            LOG.warning("No G-code loaded in editor")
            return m6_lines

        for line_num, line in enumerate(text.split('\n'), start=1):
            # Search for M6 (tool change command) - case insensitive
            if 'M6' in line.upper():
                m6_lines.append(line_num)

        LOG.info(f"Found {len(m6_lines)} M6 commands in G-code")
        
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
        
        # Scroll and highlight the M6 line in the active G-code editor.
        self.scroll_to_line_in_gcode(line_num)
        
        # Advance to next M6 for next button click (wrap around at end)
        self.current_m6_index = (self.current_m6_index + 1) % len(self.m6_lines)

    def scroll_to_line_in_gcode(self, line_num):
        """Scroll and highlight a specific line in the G-code text editor."""
        editor = self._resolve_m6_editor()

        # Get the text cursor
        cursor = editor.textCursor()

        # Move cursor to the beginning of the desired line
        # line_num is 1-based, so we need line_num - 1 blocks
        cursor.movePosition(QTextCursor.Start)
        for _ in range(line_num - 1):
            cursor.movePosition(QTextCursor.Down)

        # Select the entire line
        cursor.movePosition(QTextCursor.StartOfLine)
        cursor.movePosition(QTextCursor.EndOfLine, QTextCursor.KeepAnchor)

        # Set the cursor (this will scroll the view to show the line)
        editor.setTextCursor(cursor)

        # Ensure the line is visible in the center of the view
        editor.ensureCursorVisible()

        LOG.info(f"Scrolled to M6 line {line_num}")

    def _resolve_m6_editor(self):
        """Return the primary editor used by the FIND M6 workflow."""
        for name in ('gcodeEditor', 'gcodeEditor_2'):
            editor = getattr(self, name, None)
            if editor is not None:
                return editor
        raise AttributeError("Required G-code editor widget not found (expected gcodeEditor or gcodeEditor_2)")

    def _install_gcode_run_from_line_context_menu(self):
        for name in ('gcodeEditor', 'gcodeEditor_2'):
            editor = getattr(self, name, None)
            if editor is None:
                continue
            editor.setContextMenuPolicy(Qt.CustomContextMenu)
            editor.customContextMenuRequested.connect(lambda pos, ed=editor: self._show_gcode_context_menu(ed, pos))

    def _iter_gcode_editors_for_line_sync(self):
        for name in ('gcodeEditor', 'gcodeEditor_2'):
            editor = getattr(self, name, None)
            if editor is not None:
                yield editor

    def _install_gcode_selected_line_sync(self):
        self._status_plugin = getPlugin('status')
        if self._status_plugin is None:
            LOG.warning("Status plugin unavailable; cannot sync selected G-code line")
            return

        for editor in self._iter_gcode_editors_for_line_sync():
            cursor_signal = getattr(editor, 'cursorPositionChanged', None)
            if cursor_signal is None:
                continue
            cursor_signal.connect(lambda *args, ed=editor: self._publish_selected_program_line_from_editor(ed))
            selection_signal = getattr(editor, 'selectionChanged', None)
            if selection_signal is not None:
                selection_signal.connect(lambda *args, ed=editor: self._publish_selected_program_line_from_editor(ed))

        file_channel = getattr(self._status_plugin, 'file', None)
        file_notify = getattr(file_channel, 'notify', None)
        if callable(file_notify):
            file_notify(lambda *_args: QTimer.singleShot(0, self._publish_selected_program_line_from_any_editor))

        selected_line_channel = getattr(self._status_plugin, 'selected_program_line', None)
        selected_line_notify = getattr(selected_line_channel, 'notify', None)
        if callable(selected_line_notify):
            selected_line_notify(lambda *_args: QTimer.singleShot(0, self._apply_selected_program_line_to_any_editor))

        selected_lines_channel = getattr(self._status_plugin, 'selected_program_lines', None)
        selected_lines_notify = getattr(selected_lines_channel, 'notify', None)
        if callable(selected_lines_notify):
            selected_lines_notify(lambda *_args: QTimer.singleShot(0, self._apply_selected_program_line_to_any_editor))

        QTimer.singleShot(0, self._publish_selected_program_line_from_any_editor)

    def _publish_selected_program_line_from_editor(self, editor):
        if self._applying_external_program_selection:
            return
        if not self._selected_line_sync_allowed():
            return

        line_numbers = self._selected_line_numbers_from_editor(editor)
        if not line_numbers:
            return

        self._set_selected_program_line_channels(line_numbers)

    @staticmethod
    def _normalize_selected_lines(line_numbers):
        normalized = []
        seen = set()
        for raw in line_numbers:
            try:
                line_no = int(raw)
            except Exception:
                continue
            if line_no <= 0 or line_no in seen:
                continue
            seen.add(line_no)
            normalized.append(line_no)
        normalized.sort()
        return normalized

    def _selected_line_numbers_from_editor(self, editor):
        try:
            cursor = editor.textCursor()
        except Exception:
            return []

        try:
            if not cursor.hasSelection():
                return [int(cursor.blockNumber()) + 1]

            start_pos = int(cursor.selectionStart())
            end_pos = int(cursor.selectionEnd())
            if end_pos < start_pos:
                start_pos, end_pos = end_pos, start_pos

            if end_pos > start_pos:
                end_pos -= 1

            document = editor.document()
            start_line = int(document.findBlock(start_pos).blockNumber()) + 1
            end_line = int(document.findBlock(end_pos).blockNumber()) + 1
            if end_line < start_line:
                start_line, end_line = end_line, start_line
            return list(range(start_line, end_line + 1))
        except Exception:
            return [int(cursor.blockNumber()) + 1]

    def _set_selected_program_line_channels(self, line_numbers):
        status_plugin = getattr(self, '_status_plugin', None) or getPlugin('status')
        normalized_lines = self._normalize_selected_lines(line_numbers)
        if not normalized_lines:
            return

        selected_lines_channel = getattr(status_plugin, 'selected_program_lines', None)
        set_lines = getattr(selected_lines_channel, 'setValue', None)
        if callable(set_lines):
            set_lines(normalized_lines)

        selected_line_channel = getattr(status_plugin, 'selected_program_line', None)
        set_value = getattr(selected_line_channel, 'setValue', None)
        if callable(set_value):
            set_value(normalized_lines[0])

    def _selected_line_sync_allowed(self):
        status_plugin = getattr(self, '_status_plugin', None) or getPlugin('status')
        stat_obj = getattr(status_plugin, 'stat', None)
        if stat_obj is None:
            return True

        interp_state = getattr(stat_obj, 'interp_state', None)
        return interp_state in (linuxcnc.INTERP_IDLE, linuxcnc.INTERP_PAUSED)

    def _publish_selected_program_line_from_any_editor(self):
        editors = list(self._iter_gcode_editors_for_line_sync())
        if not editors:
            return

        focus_widget = QApplication.focusWidget()
        focused_editor = next((ed for ed in editors if ed is focus_widget), None)
        target_editor = focused_editor or editors[0]
        self._publish_selected_program_line_from_editor(target_editor)

    def _selected_program_line_values_from_status(self):
        status_plugin = getattr(self, '_status_plugin', None) or getPlugin('status')
        selected_lines_channel = getattr(status_plugin, 'selected_program_lines', None)
        selected_lines_raw = getattr(selected_lines_channel, 'value', None)
        if isinstance(selected_lines_raw, (list, tuple, set)):
            selected_lines = self._normalize_selected_lines(selected_lines_raw)
            if selected_lines:
                return selected_lines

        selected_line_channel = getattr(status_plugin, 'selected_program_line', None)
        selected_line_raw = getattr(selected_line_channel, 'value', None)
        return self._normalize_selected_lines([selected_line_raw])

    def _apply_selected_program_line_to_any_editor(self):
        if self._applying_external_program_selection:
            return
        if not self._selected_line_sync_allowed():
            return

        selected_lines = self._selected_program_line_values_from_status()
        if not selected_lines:
            return

        editors = list(self._iter_gcode_editors_for_line_sync())
        if not editors:
            return

        focus_widget = QApplication.focusWidget()
        focused_editor = next((ed for ed in editors if ed is focus_widget), None)
        target_editor = focused_editor or editors[0]
        self._apply_selected_program_lines_to_editor(target_editor, selected_lines)

    def _apply_selected_program_lines_to_editor(self, editor, line_numbers):
        normalized_lines = self._normalize_selected_lines(line_numbers)
        if not normalized_lines:
            return

        start_line = normalized_lines[0]
        end_line = normalized_lines[-1]
        if start_line <= 0 or end_line < start_line:
            return

        self._applying_external_program_selection = True
        try:
            if self._apply_selected_program_lines_to_qsci_editor(editor, start_line, end_line):
                return
            self._apply_selected_program_lines_to_qtext_editor(editor, start_line, end_line)
        finally:
            self._applying_external_program_selection = False

    @staticmethod
    def _apply_selected_program_lines_to_qsci_editor(editor, start_line, end_line):
        set_selection = getattr(editor, 'setSelection', None)
        set_cursor_position = getattr(editor, 'setCursorPosition', None)
        if not callable(set_selection) or not callable(set_cursor_position):
            return False

        start_zero = int(start_line) - 1
        end_zero = int(end_line) - 1

        end_col = 0
        text_method = getattr(editor, 'text', None)
        if callable(text_method):
            try:
                end_text = text_method(end_zero)
                end_col = len(end_text) if isinstance(end_text, str) else 0
            except Exception:
                end_col = 0

        try:
            set_selection(start_zero, 0, end_zero, end_col)
            set_cursor_position(start_zero, 0)
            ensure_line_visible = getattr(editor, 'ensureLineVisible', None)
            if callable(ensure_line_visible):
                ensure_line_visible(start_zero)
            ensure_cursor_visible = getattr(editor, 'ensureCursorVisible', None)
            if callable(ensure_cursor_visible):
                ensure_cursor_visible()
            send_scintilla = getattr(editor, 'SendScintilla', None)
            sci_vertical_center = getattr(type(editor), 'SCI_VERTICALCENTRECARET', None)
            if callable(send_scintilla) and sci_vertical_center is not None:
                send_scintilla(sci_vertical_center)
            return True
        except Exception:
            return False

    @staticmethod
    def _apply_selected_program_lines_to_qtext_editor(editor, start_line, end_line):
        get_cursor = getattr(editor, 'textCursor', None)
        set_cursor = getattr(editor, 'setTextCursor', None)
        get_document = getattr(editor, 'document', None)
        if not callable(get_cursor) or not callable(set_cursor) or not callable(get_document):
            return False

        try:
            document = get_document()
            start_block = document.findBlockByNumber(int(start_line) - 1)
            end_block = document.findBlockByNumber(int(end_line) - 1)
            if not start_block.isValid() or not end_block.isValid():
                return False

            cursor = get_cursor()
            cursor.setPosition(int(start_block.position()))
            end_pos = int(end_block.position()) + max(0, int(end_block.length()) - 1)
            cursor.setPosition(end_pos, QTextCursor.KeepAnchor)
            set_cursor(cursor)

            ensure_cursor_visible = getattr(editor, 'ensureCursorVisible', None)
            if callable(ensure_cursor_visible):
                ensure_cursor_visible()
            center_cursor = getattr(editor, 'centerCursor', None)
            if callable(center_cursor):
                center_cursor()
            return True
        except Exception:
            return False

    def _show_gcode_context_menu(self, editor, pos):
        cursor = editor.cursorForPosition(pos)
        if cursor is not None:
            editor.setTextCursor(cursor)

        line_num = editor.textCursor().blockNumber() + 1
        menu = editor.createStandardContextMenu()
        run_action = menu.addAction(f"Run from line {line_num}")
        run_action.setEnabled(actions.program_actions.run_from_line.ok())
        run_action.triggered.connect(lambda checked=False, ln=line_num: actions.program_actions.run(ln))

        first_action = menu.actions()[0] if menu.actions() else None
        if first_action is not None:
            menu.insertAction(first_action, run_action)
            menu.insertSeparator(first_action)

        menu.exec(editor.mapToGlobal(pos))

    @Slot()
    def _cycle_start_clicked(self):
        """Intercept cycle start to check if running from M6 line is enabled."""
        if self.run_from_line_Btn.isChecked():
            line_text = self.run_from_line_Num.text().strip()
            # Auto-uncheck after this intercepted run attempt.
            self.run_from_line_Btn.setChecked(False)

            if not line_text.isdigit():
                raise ValueError("No valid line number queued for run from line")

            lineNum = int(line_text)
            actions.program_actions.run(lineNum)
            LOG.info(f"Cycle started from M6 line {lineNum}")
        # Normal cycle start is handled by the button's bound actionName (program.run).


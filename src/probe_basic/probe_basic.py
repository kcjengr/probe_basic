#!/usr/bin/env python

import os
import sys
import importlib.util

import linuxcnc

from qtpyvcp.widgets.display_widgets.vtk_backplot.vtk_backplot import VTKBackPlot
from qtpy.QtCore import Slot, QRegularExpression, Qt, QObject, QTimer
from qtpy.QtGui import QFontDatabase, QRegularExpressionValidator, QTextCursor, QPalette
from qtpy.QtWidgets import QAbstractButton, QApplication
from qtpy.QtWidgets import QAction, QWidget
from qtpy import uic

from qtpyvcp import actions
from qtpyvcp.utilities import logger
from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from qtpyvcp.utilities.settings import getSetting, setSetting

sys.path.insert(0,'/usr/lib/python3/dist-packages/probe_basic')
from . import probe_basic_rc  # noqa: F401 - registers Qt resources

LOG = logger.getLogger('QtPyVCP.' + __name__)
VCP_DIR = os.path.abspath(os.path.dirname(__file__))
INIFILE = linuxcnc.ini(os.getenv("INI_FILE_NAME"))
LIGHT_STYLESHEET_FILE = "probe_basic_light.qss"
DARK_STYLESHEET_FILE = "probe_basic_dark.qss"

QFontDatabase.addApplicationFont(os.path.join(VCP_DIR, 'fonts/BebasKai.ttf'))

def _resolve_config_path(path_str: str):
    """Resolve a config path relative to the INI directory if not absolute."""
    if not path_str:
        return None
    expanded = os.path.expanduser(path_str)
    if os.path.isabs(expanded):
        return expanded
    ini_file = os.getenv("INI_FILE_NAME")
    base_dir = os.path.dirname(ini_file) if ini_file else os.getcwd()
    return os.path.abspath(os.path.join(base_dir, expanded))

class ProbeBasic(VCPMainWindow):
    """Main window class for the ProbeBasic VCP."""
    def __init__(self, *args, **kwargs):
        super(ProbeBasic, self).__init__(*args, **kwargs)
        self.filesystemtable.sortByColumn(3, Qt.DescendingOrder)
        self.filesystemtable_2.sortByColumn(3, Qt.DescendingOrder)
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

        if (0 == int(INIFILE.find("DISPLAY", "ATC_TAB_DISPLAY") or 0)):
            atc_tab_index = self.tabWidget.indexOf(self.atc_tab)
            self.tabWidget.setTabVisible(atc_tab_index, False)
            self.tabWidget.removeTab(atc_tab_index)

        elif (1 == int(INIFILE.find("DISPLAY", "ATC_TAB_DISPLAY") or 1)):
            LOG.info("[ATC] Loading carousel ATC")
            self.load_atc()

        else:
            LOG.info("[ATC] Loading rack ATC")
            self.load_rack_atc()

        # Ensure the VTK backplot widget is present before using it
        vtk_candidates = [obj for obj in self.findChildren(QObject) if "vtk" in (obj.objectName() or "").lower()]
        LOG.debug("VTK candidates by name: %s", [obj.objectName() for obj in vtk_candidates])

        # Prefer an existing VTKBackPlot; fall back to any widget named "vtk".
        self.vtk = (
            getattr(self, "vtk", None)
            or self.findChild(VTKBackPlot)
            or self.findChild(QWidget, "vtk")
        )

        if self.vtk is not None:
            try:
                self.vtk.setViewMachine()
            except Exception:
                LOG.exception("VTK widget 'vtk' found but failed to initialize")
        else:
            LOG.critical("VTK widget 'vtk' not found in UI; backplot disabled")

        if (getSetting("spindle-rpm-display.calculated-rpm").getValue()):
            self.spindle_rpm_source_widget.setCurrentIndex(self.spindle_calculated_rpm_button.property('page'))
        
        else:
            self.spindle_rpm_source_widget.setCurrentIndex(self.spindle_encoder_rpm_button.property('page'))
    
        self.load_user_tabs()

        self.load_user_buttons()
        self._theme_preference_mode = self._theme_preference()
        self._connect_theme_tracking()
        self._apply_system_theme_stylesheet()
        
        # Defer loading DROs until UI is fully loaded
        QTimer.singleShot(100, self._load_dros_after_ui)

        # Set jog_button_stacked_widget index based on DRO_DISPLAY and LATHE/BACK_TOOL_LATHE presence
        dro_display = (INIFILE.find("DISPLAY", "DRO_DISPLAY") or "").strip().lower()

        dro_display = dro_display.lower()
        
        self.help_menu = self.menuBar().addMenu("Help")
        self.interactive_help_action = QAction("Interactive Help", self, checkable=True)
        self.interactive_help_action.setChecked(False)
        self.interactive_help_action.toggled.connect(self.toggle_tooltips)
        self.help_menu.addAction(self.interactive_help_action)  # Moved to HELP menu
        self.store_original_tooltips()
        self.toggle_tooltips(False)  # Hide tooltips by default

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

        # Ensure timer labels render as zero-padded integers (no decimals)
        for _timer_label in ("timerhours", "timerminutes", "timerseconds"):
            lbl = getattr(self, _timer_label, None)
            if lbl is not None:
                lbl.textFormat = "02.0f"

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
            return
        palette_changed = getattr(app, 'paletteChanged', None)
        if palette_changed is not None:
            try:
                palette_changed.connect(self._on_palette_changed)
            except Exception:
                LOG.exception("Failed to connect paletteChanged signal")

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
            return
        try:
            with open(stylesheet_path, 'r', encoding='utf-8') as style_file:
                app.setStyleSheet(style_file.read())
        except Exception:
            LOG.exception("Failed to load theme stylesheet: %s", stylesheet_path)

    def _load_dros_after_ui(self):
        """Load DROs after UI is fully initialized."""
        self.load_user_dros()
        self.load_offset_dro()

        self.main_load_gcode_button.clicked.connect(lambda: ( 
            self.main_load_gcode_button.setText("LOAD G-CODE") if self.main_load_gcode_button.text() == 'SELECT FOLDER' else None
        ))

        self.filesystemtable.model.rootPathChanged.connect(lambda: (
            self.filesystemtable.clearSelection(),
            self.main_load_gcode_button.setEnabled(False)
        ))

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
                LOG.info("[ATC] loading module %s from %s", module_name, module_file)
                spec = importlib.util.spec_from_file_location(module_name, module_file)
                self.atc_modules[module_name] = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = self.atc_modules[module_name]
                try:
                    spec.loader.exec_module(self.atc_modules[module_name])
                except Exception as exc:
                    LOG.exception("[ATC] failed to import %s: %s", module_name, exc)
                    continue
                try:
                    self.atc[module_name] = self.atc_modules[module_name].Atc(parent=self)
                    LOG.info("[ATC] instantiated %s", module_name)
                except Exception as exc:
                    LOG.exception("[ATC] failed to instantiate %s: %s", module_name, exc)
                    continue

                if getattr(self, "atc_layout", None) is None:
                    LOG.error("[ATC] atc_layout not found on main window")
                else:
                    self.atc_layout.addWidget(self.atc[module_name])
                    # QQuickWidget doesn't fully init its GL context in a hidden
                    # tab. Force update every time the ATC tab is shown.
                    atc_widget = self.atc[module_name]
                    def _on_tab_changed(idx, _widget=atc_widget):
                        from PySide6.QtCore import QTimer
                        tab = getattr(self, 'atc_tab', None)
                        if tab is not None and self.tabWidget.widget(idx) is tab:
                            dynatc = getattr(_widget, 'dynatc', None)
                            if dynatc is not None:
                                QTimer.singleShot(0, dynatc.update)
                    try:
                        self.tabWidget.currentChanged.connect(_on_tab_changed)
                        LOG.info("[ATC] connected tab change handler for QQuickWidget repaint")
                    except Exception as exc:
                        LOG.warning("[ATC] could not connect tab change handler: %s", exc)

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
                
                rack_buttons_layout = getattr(self.rack_atc[module_name], 'user_rack_atc_buttons_layout', None)
                if rack_buttons_layout is not None:
                    self.load_user_atc_buttons(rack_buttons_layout)
                else:
                    LOG.warning(
                        "user_rack_atc_buttons_layout not found in %s. Unable to add rack ATC buttons.",
                        module_name,
                    )

    def load_user_atc_buttons(self, layout):
        self.user_atc_button_modules = {}
        self.user_atc_buttons = {}

        atc_tab_display = int(INIFILE.find("DISPLAY", "ATC_TAB_DISPLAY") or 0)
        if atc_tab_display == 0:
            return  # Do not load any user ATC buttons

        if atc_tab_display == 1:
            folder_name = "template_user_atc_buttons"
            file_name = "template_user_atc_buttons.py"
            class_name = "UserAtcButton"
        elif atc_tab_display == 2:
            folder_name = "template_user_rack_atc_buttons"
            file_name = "template_user_rack_atc_buttons.py"
            class_name = "UserRackAtcButton"
        else:
            return

        user_atc_buttons_path = INIFILE.find("DISPLAY", "USER_ATC_BUTTONS_PATH")
        if not user_atc_buttons_path:
            LOG.warning("USER_ATC_BUTTONS_PATH not set in INI.")
            return

        user_atc_buttons_path = os.path.expanduser(user_atc_buttons_path)
        full_folder = os.path.join(user_atc_buttons_path, folder_name)
        target_path = os.path.join(full_folder, file_name)
        if not os.path.isdir(full_folder):
            LOG.warning(f"User ATC buttons folder does not exist: {full_folder}")
            return
        if not os.path.isfile(target_path):
            LOG.warning(f"User ATC button file does not exist: {target_path}")
            return

        module_name = f"user_atc_buttons.{folder_name}.{folder_name}"
        spec = importlib.util.spec_from_file_location(module_name, target_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)

        if hasattr(module, class_name):
            self.user_atc_buttons[module_name] = getattr(module, class_name)()
            layout.addWidget(self.user_atc_buttons[module_name])
        else:
            LOG.warning(f"{class_name} not found in {target_path}")

    def load_user_buttons(self):
        self.user_button_modules = {}
        self.user_buttons = {}
        layout = getattr(self, "user_buttons_layout", None)
        if layout is None:
            try:
                from PySide6.QtWidgets import QVBoxLayout
                layout = self.findChild(QVBoxLayout, "user_buttons_layout")
            except Exception:
                layout = None
        if layout is None:
            LOG.error("user_buttons_layout not found on main window; skipping user buttons load")
            return

        user_buttons_paths = INIFILE.findall("DISPLAY", "USER_BUTTONS_PATH")

        for user_buttons_path in user_buttons_paths:
            resolved_base = _resolve_config_path(user_buttons_path)
            LOG.info(f"[user_buttons] base path from INI: {user_buttons_path} -> {resolved_base}")
            if not resolved_base or not os.path.isdir(resolved_base):
                LOG.warning(f"[user_buttons] path invalid or missing: {user_buttons_path}")
                continue

            for user_button in os.listdir(resolved_base):
                folder_path = os.path.join(resolved_base, user_button)
                if not os.path.isdir(folder_path):
                    continue
                target_py = os.path.join(folder_path, f"{user_button}.py")
                LOG.info(f"[user_buttons] candidate: {target_py}")
                if not os.path.isfile(target_py):
                    LOG.warning(f"[user_buttons] User button file not found: {target_py}")
                    continue

                module_name = f"user_buttons.{os.path.basename(resolved_base)}.{user_button}"
                spec = importlib.util.spec_from_file_location(module_name, target_py)
                self.user_button_modules[module_name] = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = self.user_button_modules[module_name]
                spec.loader.exec_module(self.user_button_modules[module_name])
                if hasattr(self.user_button_modules[module_name], "UserButton"):
                    self.user_buttons[module_name] = self.user_button_modules[module_name].UserButton()
                    layout.addWidget(self.user_buttons[module_name])
                    LOG.info(f"[user_buttons] added {module_name}")
                else:
                    LOG.warning(f"[user_buttons] UserButton class not found in {target_py}")

    def load_user_dros(self):
        self.user_dros_modules = {}
        self.user_dros = {}

        layout = getattr(self, "dro_display_layout", None)
        if layout is None:
            try:
                from PySide6.QtWidgets import QHBoxLayout
                layout = self.findChild(QHBoxLayout, "dro_display_layout")
            except Exception:
                layout = None
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
            LOG.info(f"[user_dros] base path from INI: {user_dros_path}")
            if not user_dros_path or not os.path.isdir(user_dros_path):
                LOG.warning(f"[user_dros] path invalid or missing: {user_dros_path}")
                continue
            dro_folder = f"{dro_type}_dros"
            dro_py_file = f"dros_{dro_type}.py"
            dro_folder_path = os.path.join(user_dros_path, dro_folder)
            dro_py_path = os.path.join(dro_folder_path, dro_py_file)
            LOG.info(f"[user_dros] looking for {dro_py_path}")
            if os.path.isfile(dro_py_path):
                module_name = f"user_dros.{dro_folder}.{dro_py_file[:-3]}"
                spec = importlib.util.spec_from_file_location(module_name, dro_py_path)
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)
                if hasattr(module, "UserDRO"):
                    self.user_dros[module_name] = module.UserDRO()
                    layout.addWidget(self.user_dros[module_name])
                    LOG.info(f"[user_dros] added {module_name}")
                else:
                    LOG.warning(f"[user_dros] UserDRO class not found in {dro_py_path}")
                return  # Only load one DRO, then exit

    def load_offset_dro(self):
        # Clear any existing widgets from the layout
        layout = getattr(self, "offset_dro_layout", None)
        if layout is None:
            try:
                from PySide6.QtWidgets import QVBoxLayout
                layout = self.findChild(QVBoxLayout, "offset_dro_layout")
            except Exception:
                layout = None
        if layout is None:
            LOG.error("offset_dro_layout not found on main window; skipping offset DRO load")
            return

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
            LOG.info(f"[offset_dro] base path from INI: {user_dros_path}")
            if not user_dros_path or not os.path.isdir(user_dros_path):
                LOG.warning(f"[offset_dro] path invalid or missing: {user_dros_path}")
                continue
            dro_folder = f"{dro_type}_dros"
            offset_ui_file = f"offset_dros_{dro_type}.ui"
            offset_ui_path = os.path.join(user_dros_path, dro_folder, offset_ui_file)
            LOG.info(f"[offset_dro] looking for {offset_ui_path}")
            if os.path.isfile(offset_ui_path):
                offset_widget = QWidget()
                uic.loadUi(offset_ui_path, offset_widget)
                layout.addWidget(offset_widget)
                LOG.info(f"[offset_dro] added {offset_ui_path}")
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
                    if not sidebar_loaded:
                        sidebar_loaded = True
                        self.user_tabs[module_name].setParent(self.sb_page_4)
                        self.user_sb_tab.setText(self.user_tabs[module_name].objectName().replace("_", " "))
                    else:
                        # can not load more than one sidebar widget
                        pass
                else:
                    self.tabWidget.addTab(self.user_tabs[module_name], self.user_tabs[module_name].objectName().replace("_", " "))

        if not sidebar_loaded:
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
    @Slot()
    def on_probe_help_next_released(self):
        lastPage = 6
        currentIndex = self.probe_help_widget.currentIndex()
        if currentIndex == lastPage:
            self.probe_help_widget.setCurrentIndex(0)
        else:
            self.probe_help_widget.setCurrentIndex(currentIndex + 1)

    @Slot()
    def on_probe_help_prev_released(self):
        lastPage = 6
        currentIndex = self.probe_help_widget.currentIndex()
        if currentIndex == 0:
            self.probe_help_widget.setCurrentIndex(lastPage)
        else:
            self.probe_help_widget.setCurrentIndex(currentIndex - 1)


    @Slot(QAbstractButton)
    def _fileviewerbtnGroup_buttonClicked(self, button):
        self.file_viewer_widget.setCurrentIndex(button.property('page'))

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

    # MDI Panel
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

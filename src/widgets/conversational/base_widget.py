import os
import linuxcnc

from PySide6.QtCore import Qt, Slot, QFile, QObject
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget, QMessageBox, QLabel, QLineEdit

from qtpyvcp.utilities import logger
from qtpyvcp.utilities.qt_safety import safe_qt_callback

from qtpyvcp.ops.gcode_file import GCodeFile

from . import conversational_rc

try:
    from shiboken6 import isValid as _is_qt_valid
except ImportError:
    def _is_qt_valid(obj):
        return obj is not None

LOG = logger.getLogger(__name__)

# Detect if we're running in Qt Designer
IN_DESIGNER = os.getenv('DESIGNER', False)

# Defer plugin imports to avoid issues in designer
STATUS = None
TOOL_TABLE = None


class _UiLoader(QUiLoader):
    def __init__(self, base_instance, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_instance = base_instance

    def _bind_widget_attr(self, name, widget):
        if self.base_instance is None or not name:
            return

        setattr(self.base_instance, name, widget)

        # Clear stale python references when Qt deletes/rebuilds widgets.
        try:
            widget.destroyed.connect(
                lambda *_, n=name, base=self.base_instance: setattr(base, n, None)
            )
        except Exception:
            pass

    def createWidget(self, class_name, parent=None, name=''):
        if parent is None and self.base_instance is not None:
            self.base_instance.setObjectName(name)
            return self.base_instance

        widget = super().createWidget(class_name, parent, name)
        self._bind_widget_attr(name, widget)
        return widget


def _load_ui(ui_path, parent):
    def _bind_widget_attr(base_instance, name, widget):
        if base_instance is None or not name:
            return

        setattr(base_instance, name, widget)

        try:
            widget.destroyed.connect(
                lambda *_, n=name, base=base_instance: setattr(base, n, None)
            )
        except Exception:
            pass

    import importlib
    import xml.etree.ElementTree as ET

    def _register_ui_custom_widgets(loader, path):
        try:
            tree = ET.parse(path)
            root = tree.getroot()
        except Exception:
            LOG.exception("Unable to parse UI for custom widget registration: %s", path)
            return

        customwidgets = root.find('customwidgets')
        if customwidgets is None:
            return

        for customwidget in customwidgets.findall('customwidget'):
            class_name = customwidget.findtext('class')
            header = customwidget.findtext('header')
            if not class_name or not header:
                continue

            module_path = header.strip()
            if module_path.endswith('.h'):
                continue

            candidate_modules = [module_path]

            for candidate in candidate_modules:
                try:
                    module = importlib.import_module(candidate)
                    widget_class = getattr(module, class_name, None)
                    if widget_class is not None:
                        loader.registerCustomWidget(widget_class)
                        break
                except Exception:
                    continue

    ui_file = QFile(ui_path)
    if not ui_file.open(QFile.ReadOnly):
        raise RuntimeError(f"Unable to open UI file: {ui_path}")
    try:
        loader = _UiLoader(parent)
        _register_ui_custom_widgets(loader, ui_path)
        loaded = loader.load(ui_file)
    finally:
        ui_file.close()
    if loaded is None:
        raise RuntimeError(f"Unable to load UI file: {ui_path}")

    for child in loaded.findChildren(QObject):
        name = child.objectName()
        if name:
            _bind_widget_attr(parent, name, child)

    return loaded

def _get_status():
    global STATUS
    if STATUS is None:
        from qtpyvcp.plugins import getPlugin
        STATUS = getPlugin('status')
    return STATUS

def _get_tool_table():
    global TOOL_TABLE
    if TOOL_TABLE is None:
        from qtpyvcp.plugins import getPlugin
        TOOL_TABLE = getPlugin('tooltable')
    return TOOL_TABLE

def _get_load_program():
    from qtpyvcp.actions.program_actions import load as loadProgram
    return loadProgram

# Initialize INI-dependent constants conditionally
if IN_DESIGNER:
    # Default values for designer mode
    PROGRAM_PREFIX = '/tmp'
    DEFAULT_SPINDLE_SPEED = 300.0
    DEFAULT_LINEAR_VELOCITY = 10.0
else:
    INI_FILE = linuxcnc.ini(os.getenv('INI_FILE_NAME'))
    PROGRAM_PREFIX = os.path.expandvars(os.path.expanduser(INI_FILE.find('DISPLAY', 'PROGRAM_PREFIX') or '/tmp'))
    DEFAULT_SPINDLE_SPEED = float(INI_FILE.find('DISPLAY', 'DEFAULT_SPINDLE_SPEED') or 0.000)
    DEFAULT_LINEAR_VELOCITY = float(INI_FILE.find('DISPLAY', 'DEFAULT_LINEAR_VELOCITY') or 0.000)

class ConversationalBaseWidget(QWidget):
    def __init__(self, parent=None, ui_file=''):
        super(ConversationalBaseWidget, self).__init__(parent)
        self.ui = _load_ui(os.path.join(os.path.dirname(__file__), ui_file), self)

        self._tool_is_valid = False
        self._tool_table = _get_tool_table() if not IN_DESIGNER else None

        self._validators = [self._validate_z_heights,
                            self._validate_spindle_rpm,
                            self._validate_xy_feed_rate,
                            self._validate_z_feed_rate,
                            self._validate_tool_number,
                            self._validate_retract_height]

        self.save_file_path = None

        if self.wcs_input.count() == 0:
            self.wcs_input.addItem('G54')
            self.wcs_input.addItem('G55')
            self.wcs_input.addItem('G56')
            self.wcs_input.addItem('G57')
            self.wcs_input.addItem('G58')
            self.wcs_input.addItem('G59')
            self.wcs_input.addItem('G59.1')
            self.wcs_input.addItem('G59.2')
            self.wcs_input.addItem('G59.3')

        if self.unit_input.count() == 0:
            self.unit_input.addItem('IN')
            self.unit_input.addItem('MM')
        self.update_selected_unit()

        if self.coolant_input.count() == 0:
            self.coolant_input.addItem('OFF')
            self.coolant_input.addItem('MIST')
            self.coolant_input.addItem('FLOOD')

        if self.spindle_direction_input.count() == 0:
            self.spindle_direction_input.addItem('CW')
            self.spindle_direction_input.addItem('CCW')

        self.xy_feed_rate_input.setText('{0:.3f}'.format(DEFAULT_LINEAR_VELOCITY))
        self.spindle_rpm_input.setText('{0:.3f}'.format(DEFAULT_SPINDLE_SPEED))

        self.post_to_file.clicked.connect(self.on_post_to_file)

        self.tool_number_input.editingFinished.connect(self.set_tool_description_from_tool_num)
        self.tool_number_input.editingFinished.connect(self._validate_tool_number)
        self.tool_number_input.textChanged.connect(self.set_tool_description_from_tool_num)
        self.tool_number_input.textChanged.connect(self._validate_tool_number)
        self.z_start_input.editingFinished.connect(self._validate_z_heights)
        self.z_end_input.editingFinished.connect(self._validate_z_heights)
        self.spindle_rpm_input.editingFinished.connect(self._validate_spindle_rpm)
        self.xy_feed_rate_input.editingFinished.connect(self._validate_xy_feed_rate)
        self.z_feed_rate_input.editingFinished.connect(self._validate_z_feed_rate)
        self.retract_height_input.editingFinished.connect(self._validate_retract_height)

        # Initialize description immediately to avoid deferred callbacks racing page teardown.
        self.set_tool_description_from_tool_num()

        # Only connect to plugins if not in designer mode
        if not IN_DESIGNER:
            if self._tool_table is not None:
                self._tool_table.tool_table_changed.connect(safe_qt_callback(self, self._update_fields))

            status = _get_status()
            if status is not None:
                status.g5x_index.onValueChanged(safe_qt_callback(self, self.update_wcs))
                status.program_units.onValueChanged(safe_qt_callback(self, self.update_selected_unit))
                status.tool_in_spindle.onValueChanged(safe_qt_callback(self, self.update_tool_number))

    def _resolve_widget(self, name, widget_type=None):
        widget = getattr(self, name, None)
        if _is_qt_valid(widget):
            return widget

        if not _is_qt_valid(self):
            return None

        try:
            widget = self.findChild(widget_type or QObject, name)
        except RuntimeError:
            return None

        if _is_qt_valid(widget):
            setattr(self, name, widget)
            return widget

        return None

    def update_wcs(self):
        if not IN_DESIGNER:
            status = _get_status()
            if status is not None:
                wcs_input = self._resolve_widget('wcs_input')
                if _is_qt_valid(wcs_input):
                    wcs_input.setCurrentIndex(status.g5x_index() - 1)

    def update_selected_unit(self):
        if not IN_DESIGNER:
            status = _get_status()
            if status is not None:
                unit_input = self._resolve_widget('unit_input')
                if _is_qt_valid(unit_input):
                    unit_input.setCurrentIndex(status.program_units() - 1)

    def update_tool_number(self):
        if not IN_DESIGNER:
            status = _get_status()
            if status is not None:
                try:
                    tool_in_spindle = status.tool_in_spindle()
                except TypeError:
                    tool_in_spindle = status.tool_in_spindle
                tool_input = self._resolve_widget('tool_number_input')
                if not _is_qt_valid(tool_input):
                    return
                tool_input.setText('{}'.format(tool_in_spindle))
                self.set_tool_description_from_tool_num()

    def set_tool_description_from_tool_num(self):
        if not _is_qt_valid(self):
            return

        tool_label = self._resolve_widget('tool_description', QLabel)
        tool_input = self._resolve_widget('tool_number_input')

        if not _is_qt_valid(tool_input):
            self._tool_is_valid = False
            return

        if IN_DESIGNER:
            self._tool_is_valid = True
            if _is_qt_valid(tool_label):
                # In designer mode, just set a placeholder
                tool_label.setText('TOOL DESCRIPTION')
                tool_label.setToolTip('TOOL DESCRIPTION')
            return

        tool_number = self.tool_number()
        tool = self._get_tool_from_table(tool_number) if self._tool_table is not None else None
        self._tool_is_valid = (tool is not None and tool_number > 0)

        if not _is_qt_valid(tool_label):
            return
        
        if tool_number <= 0:
            tool_label.setText('NO TOOL SELECTED')
            tool_label.setToolTip('NO TOOL SELECTED')
            return

        if tool is not None:
            desc = tool.get('R') or ''
            if not desc:
                desc = 'TOOL {}'.format(tool_number)
            tool_label.setText((desc[:30] + '...') if len(desc) > 30 else desc)
            tool_label.setToolTip(desc)
        else:
            tool_label.setText('TOOL NOT IN TOOL TABLE')
            tool_label.setToolTip('TOOL NOT IN TOOL TABLE')

    def name(self):
        name_input = self._get_name_input_widget()
        if not _is_qt_valid(name_input):
            return ''
        return name_input.text()

    def _get_name_input_widget(self):
        return self._resolve_widget('name_input', QLineEdit)

    def wcs(self):
        return self.wcs_input.currentText()

    def unit(self):
        return self.unit_input.currentText()

    def tool_number(self):
        try:
            return int(self.tool_number_input.value())
        except (TypeError, ValueError):
            try:
                return int(float(self.tool_number_input.text()))
            except (TypeError, ValueError):
                return 0

    def _get_tool_from_table(self, tool_number):
        if self._tool_table is None:
            return None

        tool_table = self._tool_table.getToolTable()
        candidates = [tool_number]

        try:
            normalized = int(tool_number)
            candidates.extend([normalized, str(normalized)])
        except (TypeError, ValueError):
            pass

        for key in candidates:
            tool = tool_table.get(key)
            if tool is not None:
                return tool

        # Final fallback for mixed key types (e.g. numeric-like non-str/non-int keys)
        try:
            normalized = int(tool_number)
        except (TypeError, ValueError):
            return None

        for key, tool in tool_table.items():
            try:
                if int(key) == normalized:
                    return tool
            except (TypeError, ValueError):
                continue
        return None

    def tool_diameter(self):
        if self._tool_is_valid:
            tool = self._get_tool_from_table(self.tool_number())
            if tool is None:
                return 0.0
            dia = tool.get('D')
            return float(dia) if dia is not None else 0.0
        else:
            return 0.0

    def spindle_rpm(self):
        return self.spindle_rpm_input.value()

    def spindle_direction(self):
        return self.spindle_direction_input.currentText()

    def coolant(self):
        return self.coolant_input.currentText()

    def xy_feed_rate(self):
        return self.xy_feed_rate_input.value()

    def z_feed_rate(self):
        return self.z_feed_rate_input.value()

    def clearance_height(self):
        return self.clearance_height_input.value()

    def retract_height(self):
        return self.retract_height_input.value()

    def z_start(self):
        return self.z_start_input.value()

    def z_end(self):
        return self.z_end_input.value()

    def on_post_to_file(self):
        ok, errors = self.is_valid()
        if ok:
            f = GCodeFile()
            f.ops.append(self.create_op())

            program_path = self._get_next_available_file_name()

            f.write_to_file(program_path)
            if self._confirm_action('Load GCode', 'Would you like to open the file in the viewer?'):
                _get_load_program()(program_path)
        else:
            self._show_error_msg('GCode Error', '\n'.join(errors))

    def is_valid(self):
        errors = []
        for f in self._validators:
            ok, error = f()
            if not ok:
                errors.append(error)

        return len(errors) == 0, errors

    def _set_common_fields(self, op):
        op.wcs = self.wcs()
        op.coolant = self.coolant()
        op.units = self.unit()
        op.tool_number = self.tool_number()
        op.spindle_rpm = self.spindle_rpm()
        op.spindle_dir = self.spindle_direction()
        op.z_clear = self.clearance_height()
        op.xy_feed = self.xy_feed_rate()
        op.z_start = self.z_start()
        op.z_end = self.z_end()
        op.retract = self.retract_height()
        op.z_feed = self.z_feed_rate()

    def _get_next_available_file_name(self):
        name_input = self._get_name_input_widget()
        if self.name() == '':
            if _is_qt_valid(name_input):
                name_input.setText('Untitled')
            program_name = 'Untitled'
        else:
            program_name = self.name()

        if self.save_file_path is not None:
            path = self.save_file_path
        else:
            path = PROGRAM_PREFIX

        program_base = os.path.join(path, program_name)
        program_path = program_base + '.ngc'

        i = 1
        while os.path.exists(program_path):
            program_path = '{}_{:d}.ngc'.format(program_base, i)
            i += 1

        return program_path

    def _validate_z_heights(self):
        if not self.z_start() > self.z_end():
            self.z_start_input.setStyleSheet("background-color: rgb(205, 141, 123)")
            self.z_end_input.setStyleSheet("background-color: rgb(205, 141, 123)")
            error = 'Z start position must be greater than end position.'
            self.z_end_input.setToolTip(error)
            return False, error
        else:
            self.z_start_input.setStyleSheet('')
            self.z_end_input.setStyleSheet('')
            return True, None

    def _validate_spindle_rpm(self):
        if self.spindle_rpm() > 0:
            self.spindle_rpm_input.setStyleSheet('')
            return True, None
        else:
            self.spindle_rpm_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            error = 'Spindle RPM must be greater than 0.'
            self.spindle_rpm_input.setToolTip(error)
            return False, error

    def _validate_xy_feed_rate(self):
        if self.xy_feed_rate() > 0:
            self.xy_feed_rate_input.setStyleSheet('')
            return True, None
        else:
            self.xy_feed_rate_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            error = 'XY feed rate must be greater than 0.'
            self.xy_feed_rate_input.setToolTip(error)
            return False, error

    def _validate_z_feed_rate(self):
        if self.z_feed_rate() > 0:
            self.z_feed_rate_input.setStyleSheet('')
            return True, None
        else:
            self.z_feed_rate_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            error = 'Z feed rate must be greater than 0.'
            self.z_feed_rate_input.setToolTip(error)
            return False, error

    def _validate_tool_number(self):
        # Recompute validity from current input value to avoid stale cached state.
        self.set_tool_description_from_tool_num()

        if self._tool_is_valid:
            self.tool_number_input.setStyleSheet('')
            return True, None
        else:
            self.tool_number_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            error = 'Tool is not valid.'
            self.tool_number_input.setToolTip(error)
            return False, error

    def _validate_retract_height(self):
        if self.retract_height() >= 0:
            self.retract_height_input.setStyleSheet('')
            return True, None
        else:
            self.retract_height_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            error = 'Retract height must be 0 or greater.'
            self.retract_height_input.setToolTip(error)
            return False, error

    def _confirm_action(self, title, message):
        msg = QMessageBox(QMessageBox.Question, title, message, QMessageBox.Yes | QMessageBox.No, self,
                          Qt.FramelessWindowHint)

        return msg.exec() == QMessageBox.Yes

    def _show_error_msg(self, title, message):
        msg = QMessageBox(QMessageBox.Critical, title, message, QMessageBox.Ok, self,
                          Qt.FramelessWindowHint)

        msg.exec()

    def _update_fields(self, tool_table):
        self.update_tool_number()
        self.set_tool_description_from_tool_num()

    @Slot(str)
    def setFilePath(self, path):
        self.save_file_path = path
        
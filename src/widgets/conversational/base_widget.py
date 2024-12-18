import os
import linuxcnc
from pyqtgraph import Qt

from qtpy import uic
from qtpy.QtCore import Qt, Slot
from qtpy.QtWidgets import QWidget, QMessageBox

from qtpyvcp.actions.program_actions import load as loadProgram
from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger

from qtpyvcp.ops.gcode_file import GCodeFile

LOG = logger.getLogger(__name__)

STATUS = getPlugin('status')
TOOL_TABLE = getPlugin('tooltable')

INI_FILE = linuxcnc.ini(os.getenv('INI_FILE_NAME'))
PROGRAM_PREFIX = os.path.expandvars(os.path.expanduser(INI_FILE.find('DISPLAY', 'PROGRAM_PREFIX') or '/tmp'))
DEFAULT_SPINDLE_SPEED = float(INI_FILE.find('DISPLAY', 'DEFAULT_SPINDLE_SPEED') or 0.000)
DEFAULT_LINEAR_VELOCITY = float(INI_FILE.find('DISPLAY', 'DEFAULT_LINEAR_VELOCITY') or 0.000)

class ConversationalBaseWidget(QWidget):
    def __init__(self, parent=None, ui_file=''):
        super(ConversationalBaseWidget, self).__init__(parent)
        uic.loadUi(os.path.join(os.path.dirname(__file__), ui_file), self)

        self._tool_is_valid = False
        self._tool_table = TOOL_TABLE

        self._validators = [self._validate_z_heights,
                            self._validate_spindle_rpm,
                            self._validate_xy_feed_rate,
                            self._validate_z_feed_rate,
                            self._validate_tool_number,
                            self._validate_retract_height]

        self.save_file_path = None

        self.wcs_input.addItem('G54')
        self.wcs_input.addItem('G55')
        self.wcs_input.addItem('G56')
        self.wcs_input.addItem('G57')
        self.wcs_input.addItem('G58')
        self.wcs_input.addItem('G59')
        self.wcs_input.addItem('G59.1')
        self.wcs_input.addItem('G59.2')
        self.wcs_input.addItem('G59.3')

        self.unit_input.addItem('IN')
        self.unit_input.addItem('MM')
        self.update_selected_unit()

        self.coolant_input.addItem('OFF')
        self.coolant_input.addItem('MIST')
        self.coolant_input.addItem('FLOOD')

        self.spindle_direction_input.addItem('CW')
        self.spindle_direction_input.addItem('CCW')

        self.xy_feed_rate_input.setText('{0:.3f}'.format(DEFAULT_LINEAR_VELOCITY))
        self.spindle_rpm_input.setText('{0:.3f}'.format(DEFAULT_SPINDLE_SPEED))

        self.post_to_file.clicked.connect(self.on_post_to_file)

        self.tool_number_input.editingFinished.connect(self.set_tool_description_from_tool_num)
        self.tool_number_input.editingFinished.connect(self._validate_tool_number)
        self.z_start_input.editingFinished.connect(self._validate_z_heights)
        self.z_end_input.editingFinished.connect(self._validate_z_heights)
        self.spindle_rpm_input.editingFinished.connect(self._validate_spindle_rpm)
        self.xy_feed_rate_input.editingFinished.connect(self._validate_xy_feed_rate)
        self.z_feed_rate_input.editingFinished.connect(self._validate_z_feed_rate)
        self.retract_height_input.editingFinished.connect(self._validate_retract_height)

        self._tool_table.tool_table_changed.connect(self._update_fields)

        STATUS.g5x_index.onValueChanged(self.update_wcs)
        STATUS.program_units.onValueChanged(self.update_selected_unit)
        STATUS.tool_in_spindle.onValueChanged(self.update_tool_number)

    def update_wcs(self):
        self.wcs_input.setCurrentIndex(STATUS.g5x_index() - 1)

    def update_selected_unit(self):
        self.unit_input.setCurrentIndex(STATUS.program_units() - 1)

    def update_tool_number(self):
        self.tool_number_input.setText('{}'.format(STATUS.tool_in_spindle))
        self.set_tool_description_from_tool_num()

    def set_tool_description_from_tool_num(self):
        tool_table = self._tool_table.getToolTable()
        tool_number = self.tool_number()

        tool = tool_table.get(tool_number)
        
        if tool is not None:
            desc = tool.get('R')
            self.tool_description.setText((desc[:30] + '...') if len(desc) > 30 else desc)
            self.tool_description.setToolTip(desc)
            self._tool_is_valid = (tool_number > 0)
        else:
            self._tool_is_valid = False
            self.tool_description.setText('TOOL NOT IN TOOL TABLE')
            self.tool_description.setToolTip('TOOL NOT IN TOOL TABLE')

    def name(self):
        return self.name_input.text()

    def wcs(self):
        return self.wcs_input.currentText()

    def unit(self):
        return self.unit_input.currentText()

    def tool_number(self):
        return self.tool_number_input.value()

    def tool_diameter(self):
        if self._tool_is_valid:
            
            tool_table = self._tool_table.getToolTable()
            tool = tool_table.get(self.tool_number())
            dia = tool.get('D')
            
            return dia
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
                loadProgram(program_path)
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
        if self.name() == '':
            self.name_input.setText('Untitled')

        if self.save_file_path is not None:
            path = self.save_file_path
        else:
            path = PROGRAM_PREFIX

        program_base = os.path.join(path, self.name())
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

        return msg.exec_() == QMessageBox.Yes

    def _show_error_msg(self, title, message):
        msg = QMessageBox(QMessageBox.Critical, title, message, QMessageBox.Ok, self,
                          Qt.FramelessWindowHint)

        msg.exec_()

    def _update_fields(self, tool_table):
        self.update_tool_number()
        self.set_tool_description_from_tool_num()

    @Slot(str)
    def setFilePath(self, path):
        self.save_file_path = path
        
from qtpyvcp.ops.face_ops import FaceOps

from .base_widget import ConversationalBaseWidget

class FacingVerticalWidget(ConversationalBaseWidget):
    def __init__(self, parent=None):
        super(FacingVerticalWidget, self).__init__(parent, 'facing_vertical.ui')

        self.step_down_input.editingFinished.connect(self._validate_step_down)
        self.step_over_input.editingFinished.connect(self._validate_step_over)
        self.x_start_input.editingFinished.connect(self._validate_x_positions)
        self.x_end_input.editingFinished.connect(self._validate_x_positions)
        self.y_start_input.editingFinished.connect(self._validate_y_positions)
        self.y_end_input.editingFinished.connect(self._validate_y_positions)

        self._validators.extend([self._validate_step_down,
                                 self._validate_step_over,
                                 self._validate_x_positions,
                                 self._validate_y_positions])

    def step_over(self):
        return self.step_over_input.value()

    def step_down(self):
        return self.step_down_input.value()

    def x_start(self):
        return self.x_start_input.value()

    def x_end(self):
        return self.x_end_input.value()

    def y_start(self):
        return self.y_start_input.value()

    def y_end(self):
        return self.y_end_input.value()

    def create_op(self):
        f = FaceOps()
        self._set_common_fields(f)

        f.tool_diameter = self.tool_diameter()
        f.x_start = self.x_start()
        f.x_end = self.x_end()
        f.y_start = self.y_start()
        f.y_end = self.y_end()

        if self.step_down() == 0:
            f.step_down = abs(self.z_end() - self.z_start())
            self.step_down_input.setText('{0:.3f}'.format(f.step_down))
        else:
            f.step_down = self.step_down()

        if self.step_over() == 0:
            f.step_over = self.tool_diameter() * 0.9
            self.step_over_input.setText('{0:.3f}'.format(f.step_over))
        else:
            f.step_over = self.step_over()

        return f.face()

    def _validate_step_over(self):
        if self.step_over() < 0:
            self.step_over_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            error = 'Step over cannot be negative.'
            self.step_over_input.setToolTip(error)
            return False, error
        else:
            self.step_over_input.setStyleSheet('')
            return True, None

    def _validate_step_down(self):
        if self.step_down() < 0:
            self.step_down_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            error = 'Step down cannot be negative.'
            self.step_down_input.setToolTip(error)
            return False, error
        else:
            self.step_down_input.setStyleSheet('')
            return True, None

    def _validate_x_positions(self):
        if self.x_start() < self.x_end():
            self.x_start_input.setStyleSheet('')
            self.x_end_input.setStyleSheet('')
            return True, None
        else:
            self.x_start_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            self.x_end_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            error = 'X start position must be less than end position.'
            self.x_start_input.setToolTip(error)
            self.x_end_input.setToolTip(error)
            return False, error

    def _validate_y_positions(self):
        if self.y_start() > self.y_end():
            self.y_start_input.setStyleSheet('')
            self.y_end_input.setStyleSheet('')
            return True, None
        else:
            self.y_start_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            self.y_end_input.setStyleSheet('background-color: rgb(205, 141, 123)')
            error = 'Y start position must be greater than end position.'
            self.y_start_input.setToolTip(error)
            self.y_end_input.setToolTip(error)
            return False, error

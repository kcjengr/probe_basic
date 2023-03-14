from qtpyvcp.ops.drill_ops import DrillOps
from .drill_widget import DrillWidgetBase


class HoleCircleWidget(DrillWidgetBase):
    def __init__(self, parent=None):
        super(HoleCircleWidget, self).__init__(parent, 'hole_circle.ui')

        self.diameter_input.editingFinished.connect(self._validate_diameter)
        self.num_holes_input.editingFinished.connect(self._validate_num_holes)

        self._validators.extend([self._validate_num_holes, self._validate_diameter])

    def circle_diameter(self):
        return self.diameter_input.value()

    def num_holes(self):
        return self.num_holes_input.value()

    def start_angle(self):
        return self.start_angle_input.value()

    def circle_center(self):
        return [self.center_x_input.value(), self.center_y_input.value()]

    def create_op(self):
        d = DrillOps()
        self._set_common_fields(d)
        d.retract_mode = self.retract_mode()

        d.add_hole_circle(num_holes=self.num_holes(),
                          circle_diam=self.circle_diameter(),
                          circle_center=self.circle_center(),
                          start_angle=self.start_angle())

        if self.drill_type() == 'PECK':
            op = d.peck(self.drill_peck_depth())
        elif self.drill_type() == 'DWELL':
            op = d.dwell(self.drill_dwell_time())
        elif self.drill_type() == 'BREAK':
            op = d.chip_break(self.drill_break_depth())
        elif self.drill_type() == 'TAP':
            op = d.tap(self.tap_pitch())
        elif self.drill_type() == 'RIGID TAP':
            op = d.rigid_tap(self.tap_pitch())
        elif self.drill_type() == 'MANUAL':
            op = d.manual()
        else:
            op = d.drill()

        return op

    def _validate_diameter(self):
        if self.circle_diameter() > 0:
            self.diameter_input.setStyleSheet('')
            return True, None
        else:
            self.diameter_input.setStyleSheet("background-color: rgb(205, 141, 123)")
            error = 'Diameter must be greater than 0.'
            self.diameter_input.setToolTip(error)
            return False, error

    def _validate_num_holes(self):
        if self.num_holes() > 0:
            self.num_holes_input.setStyleSheet('')
            return True, None
        else:
            self.num_holes_input.setStyleSheet("background-color: rgb(205, 141, 123)")
            error = 'Num holes must be greater than 0.'
            self.num_holes_input.setToolTip(error)
            return False, error

from .base_widget import ConversationalBaseWidget


class DrillWidgetBase(ConversationalBaseWidget):
    def __init__(self, ui, parent=None):
        super(DrillWidgetBase, self).__init__(ui, parent)

        self.drill_retract_mode_input.addItem('G98')
        self.drill_retract_mode_input.addItem('G99')

        self.drill_type_input.addItem('DRILL')
        self.drill_type_input.addItem('PECK')
        self.drill_type_input.addItem('BREAK')
        self.drill_type_input.addItem('DWELL')
        self.drill_type_input.addItem('TAP')
        self.drill_type_input.addItem('RIGID TAP')
        self.drill_type_input.addItem('MANUAL')
        self.drill_type_param_value.setVisible(False)
        self.drill_type_param_label.setVisible(False)
        self.drill_type_input.currentIndexChanged.connect(self.set_drill_type_params)

        self.z_feed_rate_input.setEnabled(True)

    def drill_type(self):
        return self.drill_type_input.currentText()

    def drill_peck_depth(self):
        return self.drill_type_param_value.value()

    def drill_break_depth(self):
        return self.drill_type_param_value.value()

    def drill_dwell_time(self):
        return self.drill_type_param_value.value()

    def tap_pitch(self):
        return self.drill_type_param_value.value()

    def retract_mode(self):
        return self.drill_retract_mode_input.currentText()

    def set_drill_type_params(self, _):
        self.z_feed_rate_input.setEnabled(True)
        if self.drill_type() == 'DWELL':
            self.drill_type_param_label.setText('DWELL TIME (SEC.)')
            self.drill_type_param_value.setText('0.00')
            self.drill_type_param_value.setVisible(True)
            self.drill_type_param_label.setVisible(True)
        elif self.drill_type() == 'PECK':
            self.drill_type_param_label.setText('PECK DEPTH')
            self.drill_type_param_value.setText('0.0000')
            self.drill_type_param_value.setVisible(True)
            self.drill_type_param_label.setVisible(True)
        elif self.drill_type() == 'BREAK':
            self.drill_type_param_label.setText('BREAK DEPTH')
            self.drill_type_param_value.setText('0.0000')
            self.drill_type_param_value.setVisible(True)
            self.drill_type_param_label.setVisible(True)
        elif self.drill_type() in ['TAP', 'RIGID TAP']:
            self.z_feed_rate_input.setEnabled(False)
            self.drill_type_param_label.setText('PITCH')
            self.drill_type_param_value.setText('0.00')
            self.drill_type_param_value.setVisible(True)
            self.drill_type_param_label.setVisible(True)
        else:
            self.drill_type_param_value.setVisible(False)
            self.drill_type_param_label.setVisible(False)

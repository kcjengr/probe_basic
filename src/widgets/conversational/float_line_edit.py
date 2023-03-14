from qtpy.QtCore import Property
from qtpy.QtGui import QDoubleValidator
from qtpy.QtWidgets import QLineEdit

from qtpyvcp.widgets.input_widgets.line_edit import VCPLineEdit


class FloatLineEdit(VCPLineEdit):
    def __init__(self, parent=None):
        super(FloatLineEdit, self).__init__(parent)
        self._default_value = 0.
        self._format_string = "{0:.3f}"
        self.setValidator(QDoubleValidator())
        self.validator().setNotation(QDoubleValidator.StandardNotation)

    @Property(float)
    def default_value(self):
        return self._default_value

    @default_value.setter
    def default_value(self, value):
        self._default_value = value

    @Property(str)
    def format_string(self):
        return self._format_string

    @format_string.setter
    def format_string(self, value):
        self._format_string = value

    @Property(str)
    def inputType(self):
        return 'number:float'

    def value(self):
        return float(self.text())

    def focusOutEvent(self, evt):
        try:
            float(self.text())
        except ValueError:
            self.setText(self._format_string.format(self._default_value))

        super(FloatLineEdit, self).focusOutEvent(evt)

from qtpy.QtGui import QIntValidator
from qtpy.QtCore import Property
from qtpy.QtWidgets import QLineEdit

from qtpyvcp.widgets.input_widgets.line_edit import VCPLineEdit


class IntLineEdit(VCPLineEdit):
    def __init__(self, parent=None):
        super(IntLineEdit, self).__init__(parent)
        self._default_value = 0
        self.setValidator(QIntValidator())

    @Property(int)
    def default_value(self):
        return self._default_value

    @default_value.setter
    def default_value(self, value):
        self._default_value = value

    @Property(str)
    def inputType(self):
        return 'number:int'

    def value(self):
        return int(self.text())

    def focusOutEvent(self, evt):
        self.setText('{:d}'.format(self.value() if self.text() else self._default_value))
        super(IntLineEdit, self).focusOutEvent(evt)

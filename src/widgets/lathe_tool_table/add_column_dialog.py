# coding=utf-8
"""AddColumnDialog -- define a new custom tool-table column (plan §5.7).

Grows the table immediately on accept: no schema migration, no restart, no
Python required. Calls straight through to
``DBToolTable.addCustomField()``, which does the actual validation
(duplicate name, invalid value_type) -- this dialog only checks that a name
was given and looks like a machine-readable key before attempting it.
"""

from PySide6.QtWidgets import (QDialog, QFormLayout, QVBoxLayout, QLineEdit,
                               QComboBox, QDialogButtonBox, QMessageBox)

VALUE_TYPES = ['text', 'float', 'int', 'bool']


class AddColumnDialog(QDialog):

    def __init__(self, tooltable_plugin, parent=None):
        super(AddColumnDialog, self).__init__(parent)
        self.tt = tooltable_plugin
        self.setWindowTitle('Add Column')

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText('e.g. vendor_part_no')
        self.label_edit = QLineEdit()
        self.label_edit.setPlaceholderText('e.g. Vendor Part No.')
        self.type_combo = QComboBox()
        self.type_combo.addItems(VALUE_TYPES)
        self.unit_edit = QLineEdit()
        self.unit_edit.setPlaceholderText('optional, e.g. in / mm / deg')
        self.default_edit = QLineEdit()
        self.default_edit.setPlaceholderText('optional')

        form = QFormLayout()
        form.addRow('Name (machine key):', self.name_edit)
        form.addRow('Label (column header):', self.label_edit)
        form.addRow('Type:', self.type_combo)
        form.addRow('Unit:', self.unit_edit)
        form.addRow('Default value:', self.default_edit)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok |
                                   QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self._onAccept)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(buttons)
        self.setLayout(layout)

    def _onAccept(self):
        name = self.name_edit.text().strip()
        if not name:
            QMessageBox.warning(self, 'Add Column', 'Name is required.')
            return
        if not all(c.isalnum() or c == '_' for c in name) or name[0].isdigit():
            QMessageBox.warning(
                self, 'Add Column',
                'Name must be a machine-readable key: letters, digits, and '
                'underscore only, not starting with a digit.')
            return

        label = self.label_edit.text().strip() or name
        value_type = self.type_combo.currentText()
        unit = self.unit_edit.text().strip() or None
        default_value = self.default_edit.text().strip() or None

        try:
            self.tt.addCustomField(name, label, value_type, unit=unit,
                                   default_value=default_value)
        except ValueError as exc:
            QMessageBox.warning(self, 'Add Column', str(exc))
            return

        self.accept()

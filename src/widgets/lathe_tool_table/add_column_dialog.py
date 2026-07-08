# coding=utf-8
"""AddColumnDialog -- define a new custom tool-table column (plan §5.7).

Grows the table immediately on accept: no schema migration, no restart, no
Python required. Calls straight through to
``DBToolTable.addCustomField()``, which does the actual validation
(duplicate name, reserved parameter name, invalid value_type) -- this
dialog only checks that a name was given and looks like a machine-readable
key before attempting it.

The machine key doubles as the column's access name everywhere (the
generated tool_data.ngc G-code parameters and the current_tool Rules
channel), so the dialog previews those names live as the key is typed --
the user sees exactly what they'll paste into a subroutine before the
column even exists.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QDialog, QFormLayout, QVBoxLayout, QLineEdit,
                               QComboBox, QDialogButtonBox, QMessageBox,
                               QLabel)

VALUE_TYPES = ['text', 'float', 'int', 'bool']


def _is_valid_key(name):
    return bool(name) and not name[0].isdigit() and all(
        c.isalnum() or c == '_' for c in name)


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
        # Same button-padding/row-spacing treatment as
        # ParameterNamesDialog: the theme's dense defaults cramped button
        # text and packed form rows together.
        self.setStyleSheet('QPushButton { padding: 3px; }')
        form.setVerticalSpacing(10)
        self.form = form
        form.addRow('Name (machine key):', self.name_edit)
        form.addRow('Label (column header):', self.label_edit)
        form.addRow('Type:', self.type_combo)
        form.addRow('Unit:', self.unit_edit)
        form.addRow('Default value:', self.default_edit)

        self.preview = QLabel()
        self.preview.setWordWrap(True)
        self.preview.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse)
        self.name_edit.textChanged.connect(self._updatePreview)
        self.type_combo.currentTextChanged.connect(self._updatePreview)
        self._updatePreview()

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok |
                                   QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self._onAccept)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(self.preview)
        layout.addWidget(buttons)
        self.setLayout(layout)

        # Placeholder text (e.g. "e.g. vendor_part_no") was getting clipped
        # at the dialog's natural width -- double it for breathing room.
        self.resize(self.sizeHint().width() * 2, self.sizeHint().height())

    def _updatePreview(self, *_args):
        """Live preview of the access names this column will provide,
        keyed off whatever is currently typed -- kept in lockstep with
        probe_basic's M6 remap epilog (configs/probe_basic_lathe/python/
        stdglue.py: refresh_current_tool_params), which is what actually
        writes the G-code parameter."""
        name = self.name_edit.text().strip()
        if not _is_valid_key(name):
            self.preview.setText(
                'Access preview: enter a machine key above to see the '
                'parameter names this column will provide to subroutines '
                'and widget rules.')
            return
        if self.type_combo.currentText() == 'text':
            self.preview.setText(
                'Access preview -- text columns have no G-code form (RS274 '
                'has no string type); widgets/Rules only:\n'
                '    tooltable:current_tool?custom:%s' % name)
            return
        self.preview.setText(
            'Access preview (in G-code, always live, no call needed):\n'
            '    #<_current_tool_%(key)s>    (the tool in the spindle)\n'
            'Widget rules:\n'
            '    tooltable:current_tool?custom:%(key)s' % {'key': name})

    def _onAccept(self):
        name = self.name_edit.text().strip()
        if not name:
            QMessageBox.warning(self, 'Add Column', 'Name is required.')
            return
        if not _is_valid_key(name):
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

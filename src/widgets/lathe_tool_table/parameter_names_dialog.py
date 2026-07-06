# coding=utf-8
"""Copyable access names for one tool-table cell (plan §6 Phase 3
follow-up, Chris 2026-07-06).

Right-clicking a cell offers "Parameter Names" -- a dialog listing every
way that cell's data can be reached from G-code/subroutines (the
generated ``tool_data.ngc`` parameters) and from other widgets (the
``tooltable:current_tool`` Rules channel), each in a read-only line edit
with a Copy button, ready to paste into a subroutine.

``parameter_entries()`` is a pure function (no Qt) so the content -- the
part that must stay in lockstep with qtpyvcp's tool_data_sub generator
naming scheme -- is testable without exec'ing a modal dialog.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QDialog, QGridLayout, QVBoxLayout, QLabel,
                               QLineEdit, QPushButton, QApplication)

from .lathe_tool_model import CUSTOM_PREFIX

# Loaded-tool numbered parameters LinuxCNC itself maintains for the core
# columns. Core is deliberately NOT mirrored into tool_data.ngc (a copy
# could go stale after a mid-run G10/touch-off), so for core cells the
# right answer is LinuxCNC's own live parameter.
CORE_LCNC_PARAMS = {
    'T': '#5400', 'X': '#5401', 'Y': '#5402', 'Z': '#5403', 'A': '#5404',
    'B': '#5405', 'C': '#5406', 'U': '#5407', 'V': '#5408', 'W': '#5409',
    'D': '#5410', 'I': '#5411', 'J': '#5412', 'Q': '#5413',
}

TEXT_NOTE = ('Text column: no G-code representation (RS274 has no string '
             'type). Available to widgets through the Rules channel.')


def parameter_entries(col_key, group, is_text, tool_no):
    """Build the (caption, snippet) rows for one cell.

    Args:
        col_key: model column key ('D', 'groove_width', 'custom:weight').
        group: 'core' | 'extras' | 'custom' (LatheToolModel.columnGroup).
        is_text: True when the column's values are text (no G-code form).
        tool_no: the clicked row's tool number.

    Returns:
        (entries, note): list of (caption, snippet) plus a footnote string
        or None.
    """
    if group == 'custom':
        key = col_key[len(CUSTOM_PREFIX):]
        rules = 'tooltable:current_tool?custom:' + key
    else:
        key = col_key
        rules = 'tooltable:current_tool?' + col_key
    rules_row = ('Rules channel (widgets)', rules)

    if group == 'core':
        lcnc_param = CORE_LCNC_PARAMS.get(col_key)
        if lcnc_param is None:  # P (pocket) and R (remark)
            return [rules_row], (
                TEXT_NOTE if col_key == 'R' else
                'The pocket number has no numbered G-code parameter; '
                'widgets can read it through the Rules channel.')
        return [
            ('Tool in spindle (LinuxCNC built-in)', lcnc_param),
            rules_row,
        ], ('Core column: LinuxCNC exposes this live for the loaded tool. '
            'It is deliberately not duplicated in tool_data.ngc, where a '
            'copy could go stale after a G10/touch-off.')

    if is_text:
        return [rules_row], TEXT_NOTE

    return [
        ('This tool (T%s)' % tool_no, '#<_tool_%s_%s>' % (tool_no, key)),
        ('Tool in spindle', '#<_current_tool_%s>' % key),
        ('Selected tool (from the call argument)', '#<_tool_%s>' % key),
        ('Run first, to load the values', 'o<tool_data> call [#5400]'),
        rules_row,
    ], ('G-code parameters hold values as of the last o<tool_data> call '
        '(pass a tool number, e.g. [7], to select a different tool into '
        '#<_tool_%s>).' % key)


class ParameterNamesDialog(QDialog):

    def __init__(self, title, entries, note=None, parent=None):
        super(ParameterNamesDialog, self).__init__(parent)
        self.setWindowTitle(title)

        layout = QVBoxLayout(self)
        # Padding-only button rule (theme's dense default cramped the
        # Copy/Close text against the button edges) plus roomier rows --
        # padding-only is safe against the app QSS cascade, unlike
        # overriding colors (see the row-header lesson in
        # lathe_tool_table.py).
        self.setStyleSheet('QPushButton { padding: 3px; }')
        grid = QGridLayout()
        grid.setVerticalSpacing(10)
        self.grid = grid
        self.snippet_edits = []
        self.copy_buttons = []
        for row, (caption, snippet) in enumerate(entries):
            grid.addWidget(QLabel(caption + ':'), row, 0)
            edit = QLineEdit(snippet)
            edit.setReadOnly(True)
            edit.setMinimumWidth(300)
            grid.addWidget(edit, row, 1)
            button = QPushButton('Copy')
            button.clicked.connect(
                lambda _checked=False, s=snippet:
                    QApplication.clipboard().setText(s))
            grid.addWidget(button, row, 2)
            self.snippet_edits.append(edit)
            self.copy_buttons.append(button)
        layout.addLayout(grid)

        if note:
            note_label = QLabel(note)
            note_label.setWordWrap(True)
            layout.addWidget(note_label)

        close = QPushButton('Close')
        close.clicked.connect(self.accept)
        layout.addWidget(close, alignment=Qt.AlignmentFlag.AlignRight)

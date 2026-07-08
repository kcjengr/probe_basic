# coding=utf-8
"""Copyable access names for one tool-table cell (plan §6 Phase 3/6
follow-up, Chris 2026-07-06/08).

Right-clicking a cell offers "Parameter Names" -- a dialog listing every
way that cell's data can be reached from G-code/subroutines and from
other widgets (the ``tooltable:current_tool`` Rules channel), each in a
read-only line edit with a Copy button, ready to paste into a
subroutine.

The G-code parameter (``#<_current_tool_<key>>``) is written directly by
probe_basic's M6 remap epilog (configs/probe_basic_lathe/python/
stdglue.py: refresh_current_tool_params(), called from change_epilog
right after the tool-change commit) -- not by a generated subroutine
that needs calling. It runs inside the interpreter process itself, so
the parameter is correct from the instant a tool change commits,
unconditionally; there is no manual call, and no gap, not even for a
program that changes tools mid-run and reads the value later in that
same run.

``parameter_entries()`` is a pure function (no Qt) so the content is
testable without exec'ing a modal dialog.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QDialog, QGridLayout, QVBoxLayout, QLabel,
                               QLineEdit, QPushButton, QApplication)

from .lathe_tool_model import CUSTOM_PREFIX

# Loaded-tool numbered parameters LinuxCNC itself maintains for the core
# columns. Core is deliberately NOT mirrored into #<_current_tool_*> (a
# copy could go stale after a mid-run G10/touch-off), so for core cells
# the right answer is LinuxCNC's own live parameter.
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
            'It is deliberately not duplicated in #<_current_tool_*>, '
            'where a copy could go stale after a G10/touch-off.')

    if is_text:
        return [rules_row], TEXT_NOTE

    return [
        ('Tool in spindle', '#<_current_tool_%s>' % key),
        rules_row,
    ], ('#<_current_tool_%s> always describes the currently LOADED tool, '
        'not necessarily T%s -- there is no by-tool-number lookup (only '
        'the loaded tool\'s data is published to G-code). Written '
        'directly by the M6 remap the instant a tool change commits, so '
        'it is always correct -- no call needed anywhere, ever, '
        'including mid-program tool changes.' % (key, tool_no))


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

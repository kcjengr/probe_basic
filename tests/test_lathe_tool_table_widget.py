#!/usr/bin/env python3
"""Headless verification for the Phase 3 LatheToolTable widget/model.

Drives the actual LatheToolModel (not a mock of it) against a scratch copy
of the real seeded probe_basic tool database, using an offscreen QApplication
and a minimal fake `status` plugin (duck-typed: only the attributes the
model actually reads/calls). Run directly:

    QT_QPA_PLATFORM=offscreen python3 tests/test_lathe_tool_table_widget.py
"""

import os
import shutil
import sys

os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')
os.environ.setdefault('DB_DEBUG', '')

HERE = os.path.dirname(os.path.abspath(__file__))
QTPYVCP_SRC = os.path.expanduser('~/dev/qtpyvcp/src')
LCNC_PY = os.path.expanduser('~/dev/linuxcnc/lib/python')
sys.path.insert(0, QTPYVCP_SRC)
sys.path.insert(0, LCNC_PY)
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', 'src')))

import linuxcnc
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

from qtpyvcp.plugins import registerPlugin
from qtpyvcp.plugins.db_tool_table import DBToolTable

failures = []


def expect(desc, cond):
    print(('PASS  ' if cond else 'FAIL  ') + desc)
    if not cond:
        failures.append(desc)


class FakeChannel:
    """Duck-typed stand-in for a qtpyvcp DataChannel: only `.notify()` (to
    register a callback) and `.fire()` (test-only, to invoke it) are used."""

    def __init__(self, value=None):
        self.value = value
        self._callbacks = []

    def notify(self, slot, *a, **kw):
        self._callbacks.append(slot)

    # qtpyvcp.actions.machine_actions wires onValueChanged(...) at import
    # time (module-level); alias it to the same store-a-callback behavior.
    onValueChanged = notify

    def fire(self, value):
        self.value = value
        for cb in list(self._callbacks):
            cb(value)


class FakeStat:
    tool_in_spindle = 0


class FakeStatus:
    def __init__(self):
        self.stat = FakeStat()
        self.tool_in_spindle = FakeChannel(0)
        self.interp_state = FakeChannel(linuxcnc.INTERP_IDLE)


def main():
    app = QApplication.instance() or QApplication([])

    real_db = os.path.expanduser(
        '~/dev/probe_basic/configs/probe_basic_lathe/tool_table.db')
    scratch_db = os.path.join(HERE, 'widget_test_scratch.db')
    for suffix in ('', '-wal', '-shm'):
        p = scratch_db + suffix
        if os.path.exists(p):
            os.remove(p)
    shutil.copy2(real_db, scratch_db)

    fake_status = FakeStatus()
    registerPlugin('status', fake_status)

    # db_file passed explicitly -- initialise() otherwise recomputes its own
    # default path from INFO.CONFIG_DIR and would ignore configure_database().
    plugin = DBToolTable(db_file=scratch_db)
    plugin.initialise()
    registerPlugin('tooltable', plugin)

    from widgets.lathe_tool_table.lathe_tool_model import LatheToolModel
    model = LatheToolModel()

    # >= not ==: the real fixture is also the live sim config, so it
    # legitimately accumulates extra tools (e.g. "New Tool" placeholders)
    # from manual GUI testing between runs -- the 23 shipped tools (T1-T23)
    # should always still be present, but the total isn't pinned to exactly
    # that.
    expect('model loaded at least the 23 real tools', model.rowCount() >= 23)
    expect('default visible columns are core + a few extras',
           set(model.visibleColumns()) >= set(model._core_columns) and
           len(model.visibleColumns()) > len(model._core_columns))

    # -------------------------------------------------- composed column data
    t23_row = None
    for row in range(model.rowCount()):
        if model.toolDataFromRow(row)['T'] == 23:
            t23_row = row
            break
    expect('found T23 (the tap) by row scan', t23_row is not None)

    model.setVisibleColumns(model.allColumns())  # show extras/custom too
    t23 = model.toolDataFromRow(t23_row)
    expect('T23 core data present', t23['D'] == 0.5)
    expect('T23 extras data present (composed from tool_lathe)',
           t23.get('type') == 'tap')

    # ---------------------------------------------------- core-column lock
    EDITABLE = Qt.ItemFlag.ItemIsEditable

    idx = model.index(t23_row, model.visibleColumns().index('D'))
    editable_when_idle = bool(model.flags(idx) & EDITABLE)
    fake_status.interp_state.fire(linuxcnc.INTERP_READING)
    editable_when_running = bool(model.flags(idx) & EDITABLE)
    fake_status.interp_state.fire(linuxcnc.INTERP_IDLE)
    editable_when_idle_again = bool(model.flags(idx) & EDITABLE)

    expect('core column (D) editable while interp idle', editable_when_idle)
    expect('core column (D) LOCKED while a program runs', not editable_when_running)
    expect('core column (D) editable again once idle', editable_when_idle_again)

    extras_idx = model.index(t23_row, model.visibleColumns().index('type'))
    fake_status.interp_state.fire(linuxcnc.INTERP_READING)
    extras_editable_while_running = bool(model.flags(extras_idx) & EDITABLE)
    fake_status.interp_state.fire(linuxcnc.INTERP_IDLE)
    expect('extras column stays editable even while a program runs',
           extras_editable_while_running)

    # -------------------------------------------------------- add/save/reload
    model.addTool()
    new_row = model.rowCount() - 1
    new_tnum = model.toolDataFromRow(new_row)['T']
    d_idx = model.index(new_row, model.visibleColumns().index('D'))
    model.setData(d_idx, 0.75, None)
    type_idx = model.index(new_row, model.visibleColumns().index('type'))
    model.setData(type_idx, 'turning', None)
    model.saveToolTable()

    model2 = LatheToolModel()  # fresh instance -- second "process" read-back
    model2.setVisibleColumns(model2.allColumns())
    reloaded = model2._tool_table.get(new_tnum)
    expect('addTool()+saveToolTable() persisted core + extras together',
           reloaded is not None and reloaded['D'] == 0.75 and
           reloaded.get('type') == 'turning')

    # ------------------------------------------------------------- renumber
    new_row2 = None
    for row in range(model2.rowCount()):
        if model2.toolDataFromRow(row)['T'] == new_tnum:
            new_row2 = row
            break
    model2.renumberTool(new_row2, 900)
    still_there = model2._tool_table.get(900)
    expect('renumberTool() through the widget model preserves extras',
           still_there is not None and still_there.get('type') == 'turning')

    # -------------------------------------------------------- add column dialog
    from PySide6.QtWidgets import QMessageBox
    from widgets.lathe_tool_table.add_column_dialog import AddColumnDialog

    warnings = []
    QMessageBox.warning = staticmethod(
        lambda *a, **kw: warnings.append(a) or QMessageBox.StandardButton.Ok)

    before_cols = set(model2.allColumns())
    dlg = AddColumnDialog(model2.tt, None)
    dlg.name_edit.setText('coating')
    dlg.label_edit.setText('Coating')
    dlg.type_combo.setCurrentText('text')
    dlg._onAccept()
    expect('AddColumnDialog accepts a valid new field',
           dlg.result() == AddColumnDialog.DialogCode.Accepted)
    expect('new custom field defined shows up in getCustomFieldDefs()',
           any(d['name'] == 'coating' for d in model2.tt.getCustomFieldDefs()))
    expect('model column set grew by exactly the new field',
           set(model2.allColumns()) - before_cols == {'custom:coating'})

    dlg2 = AddColumnDialog(model2.tt, None)
    dlg2.name_edit.setText('coating')  # duplicate
    dlg2.type_combo.setCurrentText('float')
    dlg2._onAccept()
    expect('duplicate field name rejected (warning shown, dialog not accepted)',
           dlg2.result() != AddColumnDialog.DialogCode.Accepted and len(warnings) >= 1)

    dlg3 = AddColumnDialog(model2.tt, None)
    dlg3.name_edit.setText('9bad name')  # invalid key
    dlg3._onAccept()
    expect('invalid field name rejected before touching the DB',
           dlg3.result() != AddColumnDialog.DialogCode.Accepted and len(warnings) >= 2)

    # ------------------------------------------------- column visibility + removal
    # Regression coverage for a real crash: toggling a custom column's
    # visibility off (shrinking _visible_columns) while a QSortFilterProxyModel
    # is attached used to raise IndexError inside flags() -- and, separately,
    # calling setColumnCount() again later (to make room for a new custom
    # field) after the proxy was already attached corrupted it with
    # "invalid inserted rows reported by source model". Both require an
    # actual LatheToolTable (the model alone never attaches a proxy).
    from widgets.lathe_tool_table import LatheToolTable
    from PySide6.QtCore import qInstallMessageHandler

    qt_warnings = []
    qInstallMessageHandler(lambda mode, ctx, msg: qt_warnings.append(msg))

    table = LatheToolTable()
    model2.tt.addCustomField('vendor', 'Vendor', 'text')  # after the widget/proxy exist
    table.tool_model.setVisibleColumns(table.tool_model.allColumns())
    expect('new custom field visible through a live widget+proxy',
           'custom:vendor' in table.tool_model.visibleColumns())

    shrunk = [c for c in table.tool_model.visibleColumns() if c != 'custom:vendor']
    try:
        table.tool_model.setVisibleColumns(shrunk)
        shrink_ok = True
    except Exception:
        shrink_ok = False
    expect('hiding a column (shrinking visible columns) does not crash', shrink_ok)
    expect('no Qt-level warnings from the shrink or the earlier growth',
           not any('invalid inserted rows' in w for w in qt_warnings))

    table.tool_model.setVisibleColumns(table.tool_model.allColumns())
    table._removeCustomColumn('custom:vendor')
    expect('Remove Column actually deletes the custom field from the DB',
           not any(d['name'] == 'vendor' for d in table.tool_model.tt.getCustomFieldDefs()))
    expect('removed column disappears from the model', 'custom:vendor' not in table.tool_model.allColumns())

    qInstallMessageHandler(None)

    # --------------------------------------------------------- combo editors
    from PySide6.QtWidgets import QComboBox, QStyleOptionViewItem

    table.tool_model.setVisibleColumns(table.tool_model.allColumns())
    type_col = table.tool_model.visibleColumns().index('type')
    idx = table.proxy_model.mapFromSource(table.tool_model.index(0, type_col))
    opt = QStyleOptionViewItem()
    type_editor = table.item_delegate.createEditor(table, opt, idx)
    expect('type column gets a strict (non-editable) combo box',
           isinstance(type_editor, QComboBox) and not type_editor.isEditable())
    table.item_delegate.setEditorData(type_editor, idx)
    expect('strict combo pre-selects the current DB value',
           type_editor.currentText() == table.tool_model.data(
               table.tool_model.index(0, type_col)))

    holder_col = table.tool_model.visibleColumns().index('holder_style')
    idx2 = table.proxy_model.mapFromSource(table.tool_model.index(0, holder_col))
    holder_editor = table.item_delegate.createEditor(table, opt, idx2)
    expect('holder_style column gets an editable combo (open vocabulary)',
           isinstance(holder_editor, QComboBox) and holder_editor.isEditable())

    # ---------------------------------------------------------------- cleanup
    for suffix in ('', '-wal', '-shm'):
        p = scratch_db + suffix
        if os.path.exists(p):
            os.remove(p)

    print()
    print('ALL CHECKS PASSED' if not failures else 'FAILURES: %s' % failures)
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())

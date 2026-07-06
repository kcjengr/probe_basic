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

    # Same "real fixture accumulates real state" caveat as above, now for
    # visible columns: schema v2 persistence (ui_visible_column) means the
    # scratch copy of the real DB may already carry whatever Chris last had
    # checked/unchecked from manual GUI testing (e.g. unchecking 'P', adding
    # the 4 test:* custom columns) -- not necessarily _default_visible_
    # columns()'s pristine core-plus-a-few-extras set. Only assert the
    # pristine-default shape when nothing was actually persisted yet.
    persisted_from_real_db = plugin.getVisibleColumns()
    if persisted_from_real_db:
        expect("visible columns match whatever was persisted from real "
               "manual testing (not necessarily the pristine defaults)",
               set(model.visibleColumns()) == set(persisted_from_real_db))
    else:
        expect('default visible columns are core + a few extras',
               set(model.visibleColumns()) >= set(model._core_columns) and
               len(model.visibleColumns()) > len(model._core_columns))

    # Chris (2026-07-05): every column consumed by a real machine-facing
    # consumer -- LinuxCNC (core), the VTK insert display, or a lathe
    # conversational operation -- must be default-visible. This list was
    # verified against the actual reads in pb_lathe_conv code, not just
    # docs/schema_v1/schema_v1_audit.md §1-2: the audit listed holder_hand
    # as consumed, but nothing reads the standalone column (geometry takes
    # the hand from the holder_style ISO code's trailing letter), so it
    # stays out. Asserted against the default *function* (what a pristine
    # install and Reset Default Columns give), independent of whatever
    # this fixture DB has persisted.
    CODE_CONSUMED_EXTRAS = {
        'type', 'insert_shape', 'insert_size_mode', 'insert_size',
        'insert_thickness', 'holder_style',
        'holder_shank_width', 'holder_cut_width', 'holder_oal',
        'groove_width', 'max_depth_of_cut', 'drill_point_angle',
        'flute_length', 'overall_length', 'shaft_diameter',
        'thread_pitch_max', 'thread_angle',
    }
    defaults = set(model._default_visible_columns())
    expect('default columns include all of core (LinuxCNC) plus every '
           'extras column the VTK display or a conversational op consumes',
           defaults >= set(model._core_columns) | CODE_CONSUMED_EXTRAS)
    expect('opted-out extras stay out of the defaults (holder_hand and '
           'thread_tip_type are stored-but-never-read; chamfer_threads is '
           'tap-drawing-only with a sane built-in default and a value most '
           'tap makers do not even publish)',
           not defaults & {'holder_hand', 'thread_tip_type',
                           'chamfer_threads', 'surface_speed',
                           'feed_per_rev', 'depth_of_cut', 'notes'})

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

    # -------------------------------------------------- all-columns lock
    # Every column (core, extras, custom) locks while a program runs, not
    # just core -- a custom/extras value could still be referenced by a
    # subroutine or other mid-program logic, so editing any of it during
    # machine operation is unsafe practice regardless of whether
    # LinuxCNC's own interpreter reads that particular column live.
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
    extras_editable_when_idle = bool(model.flags(extras_idx) & EDITABLE)
    fake_status.interp_state.fire(linuxcnc.INTERP_READING)
    extras_editable_while_running = bool(model.flags(extras_idx) & EDITABLE)
    fake_status.interp_state.fire(linuxcnc.INTERP_IDLE)
    extras_editable_when_idle_again = bool(model.flags(extras_idx) & EDITABLE)

    expect('extras column editable while interp idle', extras_editable_when_idle)
    expect('extras column LOCKED while a program runs (safety practice, not '
           'just what LinuxCNC itself reads live)',
           not extras_editable_while_running)
    expect('extras column editable again once idle', extras_editable_when_idle_again)

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

    # ------------------------------------- save doesn't reload once per tool
    # Regression coverage for a real perf bug: extras_changed used to fire
    # once per tool in the table (each triggering a full _load_full_table()
    # reload -- core+extras+custom for every tool), so saving got slower the
    # more tools/custom columns existed, on top of the separate one-commit-
    # per-tool DB bug fixed alongside this (see qtpyvcp's
    # test_batch_extras_and_custom_values_use_one_commit_each). A save still
    # triggers a small *fixed* number of reloads today (one via the core
    # save's tool_table_changed, one via the custom-field batch's
    # fields_changed, one explicit final reload) -- none of which scale with
    # how many tools are in the table. The bug this guards against is that
    # count growing with tool count again, not the exact fixed number.
    # Patched on the *instance*, not the class: model2 (above) is a second
    # LatheToolModel sharing the same plugin singleton, also connected to
    # its signals -- a class-level patch would count its reloads too.
    reload_count = [0]
    orig_reload = model._load_full_table

    def counting_reload():
        reload_count[0] += 1
        return orig_reload()

    model._load_full_table = counting_reload
    try:
        model.setData(d_idx, 0.8, None)
        model.saveToolTable()
    finally:
        del model._load_full_table
    expect('saveToolTable() reload count stays small and fixed, not one per tool (23+)',
           reload_count[0] <= 3)

    # ---------------------------------------------- visible columns persist
    # Regression coverage for a real bug Chris hit live: added custom
    # columns, saved, reloaded, restarted the app -- the columns were still
    # defined (data intact, still in the header menu) but no longer shown,
    # since column *visibility* was only ever tracked in the widget's own
    # memory. Schema v2 (ui_visible_column) persists it instead.
    model.tt.addCustomField('sessioncol', 'Session Col', 'text')
    model.setVisibleColumns(model.visibleColumns() + ['custom:sessioncol'])

    model3 = LatheToolModel()  # fresh instance -- simulates an app restart
    expect("a newly-added custom column's visibility survives a restart "
           "(not just its data)",
           'custom:sessioncol' in model3.visibleColumns())

    hidden = [c for c in model3.visibleColumns() if c != 'custom:sessioncol']
    model3.setVisibleColumns(hidden)
    model4 = LatheToolModel()  # restart again
    expect('explicitly hiding a column also persists across a restart',
           'custom:sessioncol' not in model4.visibleColumns())
    expect("hiding one column doesn't disturb the rest of the visible set",
           set(model4.visibleColumns()) >= {'type', 'insert_shape', 'holder_style'})

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

    # -------------------------------------------- double-click T renumbers
    # Chris: "does double clicking the tool number cell activate whatever
    # editing trigger is required?" -- T is intentionally never made
    # ItemIsEditable (see LatheToolModel.flags: a raw cell edit can't re-key
    # the outer table dict, which is keyed by the OLD tool number), so the
    # normal double-click-to-edit trigger silently does nothing there. There
    # was also no button/menu anywhere wired to the existing (working)
    # renumberSelectedTool() action, so it was unreachable in the UI at all.
    # onDoubleClick() special-cases the T column to open that same dialog.
    renumber_calls = []
    table.renumberSelectedTool = lambda: renumber_calls.append(True)

    t_col = table.tool_model.visibleColumns().index('T')
    d_col2 = table.tool_model.visibleColumns().index('D')
    t_idx = table.proxy_model.mapFromSource(table.tool_model.index(0, t_col))
    d_idx2 = table.proxy_model.mapFromSource(table.tool_model.index(0, d_col2))

    table.onDoubleClick(t_idx)
    expect('double-clicking the T cell routes to renumberSelectedTool()',
           renumber_calls == [True])

    table.onDoubleClick(d_idx2)
    expect('double-clicking a non-T cell does not trigger renumber',
           renumber_calls == [True])

    # ---------------------------------------- row header shows tool number
    # Chris: horizontal scrolling could carry the T column out of sight,
    # disorienting once you lose which row you're editing. Considered a
    # true Excel-style "freeze column" (a second overlaid QTableView
    # showing only T), then a custom-painted row header matching the row's
    # own alternating/current-tool colors -- both tried live and rejected
    # (the freeze-column overlay was reverted unbuilt in favor of the row
    # header idea Chris suggested instead; the custom-painted version hit
    # a real live bug -- reading the header's own QSS-assigned palette
    # instead of the table's -- and even once fixed, Chris still preferred
    # something simpler). Landed on the plainest option: a completely
    # stock, unhidden `QHeaderView` -- same global `QHeaderView { ... }`
    # QSS rule already styling the horizontal (column) header styles this
    # one identically, no custom subclass or painting at all -- labeled
    # with the tool number via `LatheToolModel.headerData()`'s new
    # `Qt.Orientation.Vertical` branch.
    expect('vertical header is visible (no longer hidden)',
           not table.verticalHeader().isHidden())
    expect('row header numbers are centered, with right padding so they '
           "don't touch the border edge",
           table.verticalHeader().defaultAlignment() ==
           Qt.AlignmentFlag.AlignCenter and
           'padding-right' in table.verticalHeader().styleSheet())

    row0_tnum = table.tool_model.toolDataFromRow(0)['T']
    expect('row header shows the tool number for row 0',
           table.tool_model.headerData(0, Qt.Orientation.Vertical,
                                       Qt.ItemDataRole.DisplayRole) == row0_tnum)

    # Sort descending by X and confirm the row header follows the *visual*
    # (post-sort/proxy) row, not the model's original row order -- queried
    # through the proxy, the same path Qt itself uses for header data.
    table.sortByColumn(table.tool_model.visibleColumns().index('X'),
                       Qt.SortOrder.DescendingOrder)
    proxy_row0_source_row = table.proxy_model.mapToSource(
        table.proxy_model.index(0, 0)).row()
    proxy_row0_tnum = table.tool_model.toolDataFromRow(proxy_row0_source_row)['T']
    expect('row header follows sorted (proxy) row order, not model row order',
           table.proxy_model.headerData(0, Qt.Orientation.Vertical,
                                        Qt.ItemDataRole.DisplayRole) == proxy_row0_tnum)
    table.sortByColumn(0, Qt.SortOrder.AscendingOrder)  # restore T-ascending

    renumber_calls2 = []
    table.renumberSelectedTool = lambda: renumber_calls2.append(True)
    table._onRowHeaderDoubleClicked(0)
    expect('double-clicking the row header also routes to renumberSelectedTool()',
           renumber_calls2 == [True])

    # ------------------------------------- custom-column type-based format
    # Chris: custom columns should format/align by their own value_type --
    # text left, float right, int/bool centered -- plus float should
    # display at the same fixed precision every other float column in this
    # table already uses, not whatever Python's default str() would give.
    ALIGN_LEFT = Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
    ALIGN_RIGHT = Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight
    ALIGN_CENTER = Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignCenter

    table.tool_model.tt.addCustomField('coating2', 'Coating2', 'text')
    table.tool_model.tt.addCustomField('weight', 'Weight', 'float')
    table.tool_model.tt.addCustomField('cycles', 'Cycles', 'int')
    table.tool_model.tt.addCustomField('active', 'Active', 'bool')
    table.tool_model.tt.setCustomFieldValue(1, 'coating2', 'TiAlN')
    table.tool_model.tt.setCustomFieldValue(1, 'weight', 3.14159265)
    table.tool_model.tt.setCustomFieldValue(1, 'cycles', 42)
    table.tool_model.tt.setCustomFieldValue(1, 'active', True)
    table.tool_model.loadToolTable()
    table.tool_model.setVisibleColumns(table.tool_model.allColumns())

    t1_row = None
    for row in range(table.tool_model.rowCount()):
        if table.tool_model.toolDataFromRow(row)['T'] == 1:
            t1_row = row
            break

    def _alignment_for(key):
        col = table.tool_model.visibleColumns().index(key)
        idx = table.tool_model.index(t1_row, col)
        return table.tool_model.data(idx, Qt.ItemDataRole.TextAlignmentRole)

    expect('custom text column aligns left', _alignment_for('custom:coating2') == ALIGN_LEFT)
    expect('custom float column aligns right', _alignment_for('custom:weight') == ALIGN_RIGHT)
    expect('custom int column aligns center', _alignment_for('custom:cycles') == ALIGN_CENTER)
    expect('custom bool column aligns center', _alignment_for('custom:active') == ALIGN_CENTER)

    weight_col = table.tool_model.visibleColumns().index('custom:weight')
    weight_idx = table.tool_model.index(t1_row, weight_col)
    weight_value = table.tool_model.data(weight_idx, Qt.ItemDataRole.DisplayRole)
    expect('custom float value is cast to a real float (for both alignment '
           'and decimal formatting to apply)', isinstance(weight_value, float))
    expect('custom float column displays at the table-wide fixed precision '
           '(FLOAT_DECIMALS), not raw str()',
           table.item_delegate.displayText(weight_value, None) == '3.1416')

    # --------------------------------- custom-column type-safe editors
    # Chris: entering "3.5" into an int-typed custom column used to be
    # accepted at the cell -- every custom column got a plain QLineEdit
    # regardless of its declared value_type -- only to blow up later, since
    # qtpyvcp's _cast_custom_value() does int(raw) on the next load/save,
    # which raises ValueError on a non-integer string rather than
    # truncating it. The editor widget itself should now make an
    # out-of-type entry impossible instead of catching it after the fact.
    from PySide6.QtWidgets import (QSpinBox, QDoubleSpinBox, QStyleOptionViewItem,
                                   QLineEdit, QComboBox)
    from widgets.lathe_tool_table.lathe_tool_model import FLOAT_DECIMALS as _FLOAT_DECIMALS

    opt2 = QStyleOptionViewItem()
    cycles_col = table.tool_model.visibleColumns().index('custom:cycles')
    cycles_idx = table.proxy_model.mapFromSource(table.tool_model.index(t1_row, cycles_col))
    cycles_editor = table.item_delegate.createEditor(table, opt2, cycles_idx)
    expect('custom int column gets a QSpinBox editor (cannot type a decimal point)',
           isinstance(cycles_editor, QSpinBox))

    weight_idx_proxy = table.proxy_model.mapFromSource(table.tool_model.index(t1_row, weight_col))
    weight_editor = table.item_delegate.createEditor(table, opt2, weight_idx_proxy)
    expect('custom float column gets a QDoubleSpinBox editor',
           isinstance(weight_editor, QDoubleSpinBox))
    expect('custom float editor uses the same table-wide FLOAT_DECIMALS precision',
           weight_editor.decimals() == _FLOAT_DECIMALS)

    coating2_col = table.tool_model.visibleColumns().index('custom:coating2')
    coating2_idx = table.proxy_model.mapFromSource(table.tool_model.index(t1_row, coating2_col))
    coating2_editor = table.item_delegate.createEditor(table, opt2, coating2_idx)
    expect('custom text column still gets a plain QLineEdit',
           isinstance(coating2_editor, QLineEdit))

    active_col = table.tool_model.visibleColumns().index('custom:active')
    active_idx_src = table.tool_model.index(t1_row, active_col)
    active_idx = table.proxy_model.mapFromSource(active_idx_src)
    active_editor = table.item_delegate.createEditor(table, opt2, active_idx)
    expect('custom bool column gets a strict True/False combo box, not free text',
           isinstance(active_editor, QComboBox) and not active_editor.isEditable())

    table.item_delegate.setEditorData(active_editor, active_idx)
    expect('bool combo editor pre-selects True for a tool whose stored value is True',
           active_editor.currentText() == 'True')

    active_editor.setCurrentIndex(active_editor.findText('False'))
    table.item_delegate.setModelData(active_editor, table.proxy_model, active_idx)
    expect('picking False in the bool combo writes back a real Python bool, '
           'not the string "False"',
           table.tool_model.toolDataFromRow(t1_row).get('custom:active') is False)

    # --------------------------------------------------------- combo editors
    from PySide6.QtWidgets import QComboBox, QStyleOptionViewItem, QLineEdit

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

    # -------------------------------- dependent (type-discriminated) combos
    # Regression coverage for "selection set discrimination based on
    # previous selection" ported from pb_lathe_conv's Fusion-era tool
    # library (tool_library_table.py): insert_shape/holder_style choices
    # must narrow by the row's own type (and, for holder_style, by the
    # row's already-chosen insert_shape) instead of listing every value
    # ever used by any tool regardless of fit.
    def _row_for_tool(tnum):
        for row in range(table.tool_model.rowCount()):
            if table.tool_model.toolDataFromRow(row)['T'] == tnum:
                return row
        return None

    insert_col = table.tool_model.visibleColumns().index('insert_shape')

    t2_row = _row_for_tool(2)  # turning, insert_shape='C', holder_style='SCLCR'
    idx_t2_holder = table.proxy_model.mapFromSource(table.tool_model.index(t2_row, holder_col))
    holder_editor_t2 = table.item_delegate.createEditor(table, opt, idx_t2_holder)
    t2_holder_options = [holder_editor_t2.itemText(i) for i in range(holder_editor_t2.count())]
    expect("holder_style options for a 'C' insert include its own real holder code",
           'SCLCR' in t2_holder_options)
    expect("holder_style options for a 'C' insert exclude a 'D'-only holder code",
           'SDJCR' not in t2_holder_options)

    t10_row = _row_for_tool(10)  # grooving
    idx_t10_shape = table.proxy_model.mapFromSource(table.tool_model.index(t10_row, insert_col))
    shape_editor_t10 = table.item_delegate.createEditor(table, opt, idx_t10_shape)
    t10_shape_options = [shape_editor_t10.itemText(i) for i in range(shape_editor_t10.count())]
    expect('insert_shape options for a grooving tool are grooving-specific, not ISO letters',
           'GROOVE SQUARE' in t10_shape_options and 'C' not in t10_shape_options)

    t20_row = _row_for_tool(20)  # drill -- no insert/holder concept at all
    idx_t20_shape = table.proxy_model.mapFromSource(table.tool_model.index(t20_row, insert_col))
    drill_shape_editor = table.item_delegate.createEditor(table, opt, idx_t20_shape)
    expect('insert_shape falls back to plain text for a drill (no valid options)',
           isinstance(drill_shape_editor, QLineEdit))

    # ----------------------------------------- classic (non-DB) backend
    # LatheToolTable is meant to be a genuine drop-in replacement for the
    # classic file-based qtpyvcp.plugins.tool_table:ToolTable, not just the
    # new DB-backed one -- one .ui, one widget class, adapting at runtime to
    # whichever 'tooltable' plugin the config actually wires up (a real
    # earlier attempt at two separate .ui files -- one per backend --
    # turned out to be unsustainable: Designer bakes the promoted widget
    # class into the .ui statically, so any edit made against one .ui
    # silently never appeared in the other).
    class _NoOpSignal:
        """Only .connect() is exercised for tool_table_changed in this
        test -- no need to actually fire it anywhere."""
        def connect(self, *a, **kw):
            pass

    class ClassicToolTablePlugin:
        """Duck-typed stand-in for the real qtpyvcp.plugins.tool_table:
        ToolTable interface -- core-only, no extras/custom-field concept,
        no renumberTool (LatheToolModel falls back to delete+recreate for
        that -- there's no extras/custom data such a plugin could lose).

        `columns` deliberately excludes 'P', matching this shop's real
        TOOL_TABLE_COLUMNS = TXZIJDQR ini setting -- and saveToolTable()
        below reproduces the real plugin's quirk of unconditionally
        requiring 'P' anyway (the .tbl file format needs a pocket number
        for every tool regardless of configured *display* columns), which
        is exactly what caught a real KeyError('P') here: LatheToolModel's
        save path used to filter each row down to self._core_columns
        (correctly, for the DB-backed core+extras+custom split) even for
        this backend, stripping 'P' back out before it ever reached here.
        """
        columns = ['T', 'X', 'Z', 'D', 'I', 'J', 'Q', 'R']
        COLUMN_LABELS = {c: c for c in columns}

        def __init__(self):
            self._table = {0: {c: 0 for c in self.columns}}
            self.tool_table_changed = _NoOpSignal()

        def getToolTable(self):
            return dict(self._table)

        def loadToolTable(self, tool_file=None):
            # Real plugin re-reads the .tbl file here; this duck-type's
            # saveToolTable() below already updates self._table
            # synchronously (no real file/async watcher gap to simulate),
            # so this just needs to exist and return the current state.
            return dict(self._table)

        def saveToolTable(self, tool_table, columns=None):
            cols = list(self.columns)
            if 'P' not in cols:
                cols.insert(1, 'P')
            for tnum in sorted(tool_table)[1:]:  # [1:]: real plugin skips T0 too
                row = tool_table[tnum]
                for col in cols:
                    if col == 'R':
                        continue
                    row[col]  # KeyError here if missing -- the real bug
            self._table = dict(tool_table)

        def newTool(self, tnum=None):
            if tnum is None:
                tnum = len(self._table)
            # DEFAULT_TOOL always has every key (incl. 'P'), regardless of
            # configured display columns -- same reasoning as saveToolTable.
            row = {c: 0 for c in self.columns}
            row.setdefault('P', 0)
            row.update({'T': tnum, 'R': 'New Tool'})
            return row

    classic_plugin = ClassicToolTablePlugin()
    registerPlugin('tooltable', classic_plugin)
    classic_model = LatheToolModel()
    classic_table = LatheToolTable()
    expect('classic (non-DB) plugin does not crash model/widget construction',
           classic_model.tt is classic_plugin)
    expect('classic plugin is recognized as not DB-backed',
           classic_model._db_backed is False)
    expect('only core columns visible against a classic plugin (no Type/Insert '
           'Shape/Holder)', classic_model.visibleColumns() == classic_model._core_columns)

    classic_model.addTool()
    new_row = classic_model.rowCount() - 1
    new_tnum = classic_model.toolDataFromRow(new_row)['T']
    d_idx = classic_model.index(new_row, classic_model.visibleColumns().index('D'))
    classic_model.setData(d_idx, 0.6, None)
    classic_model.saveToolTable()  # must not touch saveAllToolExtras/setCustomFieldValues
    expect("addTool()+saveToolTable() round-trips through the classic plugin's "
           "saveToolTable() alone",
           classic_plugin._table.get(new_tnum, {}).get('D') == 0.6)

    new_row2 = None
    for row in range(classic_model.rowCount()):
        if classic_model.toolDataFromRow(row)['T'] == new_tnum:
            new_row2 = row
            break
    classic_model.renumberTool(new_row2, 77)
    expect('renumberTool() falls back to delete+recreate for a plugin with no '
           'renumberTool() of its own',
           77 in classic_plugin._table and new_tnum not in classic_plugin._table
           and classic_plugin._table[77]['D'] == 0.6)

    # ---------------------------------------- wrong-plugin-type crash guard
    # Regression coverage for a real crash found via a core dump: launching
    # against a 'tooltable' plugin missing even the *base* tool-table
    # interface (not just the DB-only extras -- see the classic-backend
    # block above for that, now a fully supported case) segfaulted the
    # whole app -- the AttributeError raised inside LatheToolModel.__init__
    # escaped up through QUiLoader's C++ widget-tree construction (this
    # widget is built via .ui customwidget promotion) instead of
    # propagating as a normal Python exception.
    class WrongTypeToolTablePlugin:
        """Missing saveToolTable/newTool/tool_table_changed -- not even the
        base interface every 'tooltable' plugin (DB-backed or classic) is
        expected to implement, unlike ClassicToolTablePlugin above."""
        columns = ['T', 'P', 'X', 'Z', 'D', 'I', 'J', 'Q', 'R']
        COLUMN_LABELS = {c: c for c in columns}

        def getToolTable(self):
            return {0: {c: 0 for c in self.columns}}

    registerPlugin('tooltable', WrongTypeToolTablePlugin())
    try:
        bad_model = LatheToolModel()
        bad_table = LatheToolTable()
        wrong_plugin_ok = True
    except Exception:
        wrong_plugin_ok = False
    expect('wrong-type tooltable plugin does not crash model/widget construction',
           wrong_plugin_ok)
    if wrong_plugin_ok:
        expect('falls back to an empty stub table instead', bad_model.rowCount() == 0)
        expect('stub leaves tt as None (no calls made against the wrong plugin)',
               bad_model.tt is None and bad_table.tool_model.tt is None)

        # Regression coverage for a second real crash found via a core dump:
        # Qt Designer's startup widget-database scan reads every *declared
        # Qt property* on a freshly-constructed instance of every registered
        # custom widget (independent of which .ui is even open) --
        # currentToolColor/currentToolBackground read
        # self.tool_model.current_tool_color/current_tool_bg unconditionally,
        # which the stub path above never set, so Designer's C++-invoked
        # property read hit an AttributeError and segfaulted instead of
        # raising. Exercise exactly what Designer does: read every property
        # via the meta-object system, not just construct the widget.
        mo = bad_table.metaObject()
        property_read_ok = True
        for i in range(mo.propertyCount()):
            try:
                mo.property(i).read(bad_table)
            except Exception:
                property_read_ok = False
        expect('every Qt property reads cleanly on the stub-backed widget '
               '(what Designer\'s startup widget-database scan does)',
               property_read_ok)

    registerPlugin('tooltable', plugin)  # restore the real plugin

    # -------------------------------------------------- last-column stretch
    # Regression coverage: the last column should fill leftover viewport
    # width when there's genuinely spare room (classic backend, few narrow
    # core columns -- Chris found a bare gap after the last column here)
    # but must NOT stretch below its own content width when the columns
    # already need more room than available (DB backend with many columns
    # visible in a narrow window -- the original reason stretch was off at
    # all). See LatheToolTable._updateLastColumnStretch.
    classic_table.resize(1200, 300)
    classic_table.show()
    app.processEvents()
    header = classic_table.horizontalHeader()
    expect('classic (narrow-columns) table stretches the last column to '
           'fill the container',
           header.stretchLastSection() and
           sum(header.sectionSize(i) for i in range(header.count()))
           == classic_table.viewport().width())

    table.tool_model.setVisibleColumns(table.tool_model.allColumns())
    table.resize(500, 300)
    table.show()
    app.processEvents()
    header2 = table.horizontalHeader()
    total2 = sum(header2.sectionSize(i) for i in range(header2.count()))
    expect('DB-backed table with many columns in a narrow window does not '
           'stretch (would squeeze the last column below its content width)',
           not header2.stretchLastSection() and total2 > table.viewport().width())

    # ------------------------------------------ G43 reissue for active tool
    # Regression coverage for a real bug Chris hit live: editing a cell for
    # the tool currently in the spindle, saving, and seeing the DRO still
    # show the *old* offset. Writing the table and telling LinuxCNC to
    # reload it (self.tt.saveToolTable()) does not, on its own, re-apply
    # the active tool's offset -- that needs an explicit G43 (or a tool
    # change), the same recipe qtpyvcp's own classic ToolTable plugin
    # already uses after homing (reload_tool(): "M61 Q<n> G43") -- just not
    # wired to fire after a table save. Never exercised by any check above:
    # tool_in_spindle stayed 0 (no tool loaded) throughout every one of
    # them, so this path was never actually called until now.
    import widgets.lathe_tool_table.lathe_tool_model as ltm_module
    orig_issue_mdi = ltm_module.issue_mdi

    mdi_calls = []
    ltm_module.issue_mdi = lambda cmd, *a, **kw: mdi_calls.append(cmd)
    try:
        fake_status.stat.tool_in_spindle = 2
        model.saveToolTable()
    finally:
        ltm_module.issue_mdi = orig_issue_mdi
        fake_status.stat.tool_in_spindle = 0
    expect('saveToolTable() reissues G43 for whatever tool is currently in '
           'the spindle', mdi_calls == ['M61 Q2 G43'])

    mdi_calls2 = []
    ltm_module.issue_mdi = lambda cmd, *a, **kw: mdi_calls2.append(cmd)
    try:
        model.saveToolTable()  # tool_in_spindle back to 0 (no tool loaded)
    finally:
        ltm_module.issue_mdi = orig_issue_mdi
    expect('saveToolTable() does not reissue G43 when no tool is loaded',
           mdi_calls2 == [])

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

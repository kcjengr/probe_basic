========================
Running Notes Workflow
========================

Purpose
-------

This page is a working log for active development and bug-fix sessions.
Keep entries short and release-note ready so they can be copied into formal
release notes with minimal editing.

Rules
-----

- Add an entry for every meaningful fix or feature touching Probe Basic or QtPyVCP.
- Write what changed, why it changed, and how it was validated.
- Include impacted files for quick traceability.
- Keep temporary diagnostics out of the final summary unless they remain in code.
- Keep newest entries at the top.

Entry Template
--------------

Date
   YYYY-MM-DD

Area
   Subsystem or feature name.

Summary
   One short paragraph describing the user-visible outcome.

Changes
   - concise implementation change
   - concise implementation change

Validation
   - explicit behavior that was verified

Files
   - relative/path/to/file.py


2026-03-13
----------

Area
   ATC QML pocket highlighting for required program tools

Summary
   Added dynamic pocket label background highlighting in carousel and rack ATC
   QML views to indicate pockets holding tools required by the loaded program.

Changes
   - Added `highlightPocketSig(pocket, highlight)` from both ATC bridge widgets
     (`DynATC` and `RackATC`) into QML.
   - Connected runtime updates to `gcode_properties.tools` and
     `status.tool_table` so required-tool mapping refreshes when file/tool data
     changes.
   - Implemented required tool-number resolution from program tool indexes and
     emitted per-pocket highlight state based on current pocket contents.
   - Updated `atc.qml` and `rack_atc.qml` to color pocket label backgrounds via
     the new highlight signal.

Validation
   - Verified no syntax/analysis errors across updated Python and QML files.
   - Confirmed highlight signal handlers and delegate aliases exist in both QML
     files.

Files
   - src/widgets/atc_widget/atc.py
   - src/widgets/atc_widget/atc.qml
   - src/widgets/rack_atc_widget/rack_atc.py
   - src/widgets/rack_atc_widget/rack_atc.qml
   - audit_reports/running_notes.rst


2026-03-13
----------

Area
   Runtime rules evaluation with ATC `.var` parameters

Summary
   Fixed runtime rule expressions using `param()` to reflect live `.var`
   parameter updates instead of using only startup-time values.

Changes
   - Updated `VCPBaseWidget.registerRules()` so `param(number, default)` reads
     current values from the parameter file on each evaluation.
   - Kept `params` snapshot behavior unchanged for compatibility with existing
     expressions.

Validation
   - Verified runtime rule eval context still exposes `ch`, `widget`, `params`,
     and `param` with no syntax/analysis errors in modified file.

Files
   - qtpyvcp/src/qtpyvcp/widgets/base_widgets/base_widget.py
   - audit_reports/running_notes.rst


2026-03-13
----------

Area
   Qt Designer rules editor persistence (`tools_check_list`)

Summary
   Fixed rules save path to target the edited widget explicitly in Designer,
   resolving save failures where `rules` updates were rejected or not persisted
   for `tools_check_list`.

Changes
   - Replaced cursor-position-dependent `setProperty("rules", ...)` flow with
     `cursor.setWidgetProperty(self.widget, "rules", data)`.
   - Added compatibility fallback to cursor `setProperty` for bindings without
     matching `setWidgetProperty` signature.
   - Marked form dirty after successful save to ensure Designer persists changes.

Validation
   - Verified updated save path uses widget-targeted property update and dirty
     form marking in `rules_editor.saveChanges()`.

Files
   - qtpyvcp/src/qtpyvcp/widgets/qtdesigner/rules_editor.py
   - audit_reports/running_notes.rst


2026-03-13
----------

Area
   Qt Designer rules editor save behavior

Summary
   Fixed a silent-failure path in Rules Editor save handling so failed writes
   no longer close the dialog without feedback.

Changes
   - Added explicit error handling when no Designer form window is found during
     save.
   - Added explicit error handling when `setProperty("rules", ...)` is
     rejected by Designer.
   - Preserved existing validation behavior and only changed failure reporting.

Validation
   - Verified updated save path now returns early on failure and shows a
     critical message box rather than silently accepting.

Files
   - qtpyvcp/src/qtpyvcp/widgets/qtdesigner/rules_editor.py
   - audit_reports/running_notes.rst


2026-03-13
----------

Area
   Widget rules expression context (`.var` machine parameters)

Summary
   Added LinuxCNC `.var` parameter access to widget rule expressions so rules
   can use real machine parameter values instead of hardcoded constants.

Changes
   - Added `machine_parameters` utility to resolve the active `RS274NGC`
     parameter file and parse parameter/value pairs from the `.var` file.
   - Extended runtime rule evaluation context to include:
     `params` (dict of parameter number to value) and `param(number, default)`.
   - Extended Rules Editor validation context with the same `params` and
     `param()` helpers so expressions validate consistently in Designer.

Validation
   - Verified modified rule-evaluation and validation modules have no syntax/
     analysis errors.
   - Confirmed expression eval environments now include both channel values and
     parsed `.var` parameter values.

Files
   - qtpyvcp/src/qtpyvcp/utilities/machine_parameters.py
   - qtpyvcp/src/qtpyvcp/widgets/base_widgets/base_widget.py
   - qtpyvcp/src/qtpyvcp/widgets/qtdesigner/rules_editor.py
   - audit_reports/running_notes.rst


2026-03-13
----------

Area
   QtPyVCP Designer channel autocomplete (`gcode_properties`)

Summary
   Restored Rules Editor channel autocomplete for `gcode_properties:*` in Qt
   Designer by ensuring the plugin is auto-loaded in Designer mode and does not
   fail when `INI_FILE_NAME` is unavailable.

Changes
   - Added `gcode_properties` to the Designer auto-load plugin set.
   - Made `gcode_properties` import/constructor initialization resilient when
     running in Designer mode by avoiding hard dependence on `INI_FILE_NAME`.
   - Added a clean runtime guard/log when `INI_FILE_NAME` is missing.

Validation
   - Confirmed Rules Editor completer source (`iterPlugins()` over `DataPlugin`
     channels) now has a path to include `gcode_properties` in Designer mode.
   - Verified no syntax/analysis errors in modified plugin files.

Files
   - qtpyvcp/src/qtpyvcp/plugins/__init__.py
   - qtpyvcp/src/qtpyvcp/plugins/gcode_properties.py
   - audit_reports/running_notes.rst


2026-03-13
----------

Area
   QtPyVCP Designer rules editor channel lookup

Summary
   Fixed a Designer-time plugin fallback contract mismatch that caused rule
   selection in the Rules Editor to crash with `TypeError: cannot unpack
   non-iterable bool object`.

Changes
   - Added an explicit `NullPlugin.getChannel()` implementation that returns
     `(None, None)` to match the `DataPlugin.getChannel()` tuple contract.
   - Kept general fallback behavior unchanged for other `NullPlugin` methods.

Validation
   - Verified the failing call site expects tuple unpacking in
     `rules_editor.get_channel_data()` and now receives a tuple-compatible
     return from the Designer fallback plugin path.

Files
   - qtpyvcp/src/qtpyvcp/plugins/__init__.py
   - audit_reports/running_notes.rst


2026-02-20
----------

Area
   MDI queue + feedhold/cycle-start recovery

Summary
   Resolved MDI queue and feedhold recovery behavior so paused queued MDI commands
   can resume reliably from cycle start without requiring abort/restart workarounds.

Changes
   - Hardened MDI history queue selection/state handling for null and invalid index paths.
   - Updated MDI dispatch flow to avoid forced mode switching when already in MDI.
   - Adjusted run-action eligibility to allow valid MDI resume paths while no file is loaded.
   - Removed duplicate normal cycle-start invocation in both mill and lathe handlers.

Validation
   - Pause/resume queue flow works as expected.
   - Feedhold during a running queued MDI line resumes correctly from cycle start.

Files
   - qtpyvcp/src/qtpyvcp/widgets/input_widgets/mdihistory_widget.py
   - qtpyvcp/src/qtpyvcp/actions/program_actions.py
   - qtpyvcp/src/qtpyvcp/actions/machine_actions.py
   - probe_basic/src/probe_basic/probe_basic.py
   - probe_basic/src/probe_basic_lathe/probe_basic_lathe.py

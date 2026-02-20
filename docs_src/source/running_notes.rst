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

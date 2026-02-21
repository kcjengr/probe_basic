Purpose
-------
This file gives concise, actionable guidance for AI coding agents working in the Probe Basic repository.

Running notes rule
------------------
- Keep running notes current for every meaningful Probe Basic or QtPyVCP change.
- Update `audit_reports/running_notes.rst` with release-note-ready entries.
- Each entry should include: date, area, summary, changes, validation, and touched files.
- Keep newest entries at the top.

Docs and packaging hygiene
-------------------------
- Do not add standalone `.rst` files under `docs_src/source/` unless they are included in a toctree (for example via `docs_src/source/index.rst`).
- Keep doc markup warning-free for Sphinx builds used by docs/deb packaging.

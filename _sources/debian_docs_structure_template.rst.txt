:orphan:

==========================================
Template: Debian Docs Split File Structure
==========================================

Purpose
-------

This template defines a clean and maintainable docs structure that separates
Debian 12 Bookworm and Debian 13 Trixie into dedicated sections.

Design Goals
------------

- Keep navigation OS-first: Debian 12 and Debian 13 at top level.
- Keep all editable content inside the OS directory it belongs to.
- Keep one canonical source file per topic (no duplicated editable content).
- Allow Bookworm and Trixie to evolve independently for install, release notes, and parameters.

Proposed Target Structure
-------------------------

.. code-block:: text

   docs_src/source/
   |- index.rst
   |
   |- debian_12_bookworm/
   |  |- index.rst
   |  |- installation/
   |  |  |- index.rst
   |  |  |- probe_basic_apt_stable_install.rst
   |  |  |- probe_basic_apt_develop_install.rst
   |  |  |- probe_basic_stable_develop_change.rst
   |  |  |- probe_basic_deb_install.rst
   |  |  |- probe_basic_dev_install.rst
   |  |- release_notes/
   |  |  |- index.rst
   |  |  |- update_notes_stable.rst
   |  |  |- update_notes_develop.rst
   |  |- configuration/
   |  |  |- index.rst
   |  |  |- probe_basic_parameters.rst
   |  |  |- machine_config.rst
   |  |  |- atc_setup.rst
   |  |- interface/
   |  |  |- index.rst
   |  |  |- mill_interface.rst
   |  |  |- lathe_interface.rst
   |  |  |- tool_offsets_lathe.rst
   |  |  |- probing.rst
   |  |  |- tool_length_setter.rst
   |  |- extending/
   |  |  |- index.rst
   |  |  |- user_tabs.rst
   |  |  |- custom_ux_hacking.rst
   |
   |- debian_13_trixie/
   |  |- index.rst
   |  |- installation/
   |  |  |- index.rst
   |  |  |- probe_basic_trixie_apt_develop_install.rst
   |  |  |- probe_basic_trixie_dev_install.rst
   |  |- release_notes/
   |  |  |- index.rst
   |  |  |- update_notes_stable.rst
   |  |  |- update_notes_develop.rst
   |  |- configuration/
   |  |  |- index.rst
   |  |  |- probe_basic_parameters_trixie.rst
   |  |  |- pb_var_parameter_trixie.csv
   |  |  |- machine_config.rst
   |  |  |- atc_setup.rst
   |  |- interface/
   |  |  |- index.rst
   |  |  |- mill_interface.rst
   |  |  |- lathe_interface.rst
   |  |  |- tool_offsets_lathe.rst
   |  |  |- probing.rst
   |  |  |- tool_length_setter.rst
   |  |- extending/
   |  |  |- index.rst
   |  |  |- user_tabs.rst
   |  |  |- custom_ux_hacking.rst

Canonical Content Rules
-----------------------

- Canonical content lives inside ``debian_12_bookworm/`` or ``debian_13_trixie/``.
- Root-level docs contain only the main docs hub (``index.rst``) and planning/template docs.
- If two OS pages are identical, use a shared include source to avoid copy/paste drift.

Template Navigation Model
-------------------------

Root index (``index.rst``):

- Debian 12 Bookworm -> ``debian_12_bookworm/index``
- Debian 13 Trixie -> ``debian_13_trixie/index``

Debian 12 index:

- Installation -> ``debian_12_bookworm/installation/index``
- Update Release Notes -> ``debian_12_bookworm/release_notes/index``
- Configuration -> ``debian_12_bookworm/configuration/index``
- Interface -> ``debian_12_bookworm/interface/index``
- Extending -> ``debian_12_bookworm/extending/index``

Debian 13 index:

- Installation -> ``debian_13_trixie/installation/index``
- Update Release Notes -> ``debian_13_trixie/release_notes/index``
- Configuration -> ``debian_13_trixie/configuration/index``
- Interface -> ``debian_13_trixie/interface/index``
- Extending -> ``debian_13_trixie/extending/index``

Implementation Checklist
------------------------

1. Create full section trees under ``debian_12_bookworm/`` and ``debian_13_trixie/``.
2. Move canonical pages into their OS directories.
3. Wire root ``index.rst`` to OS hub pages only.
4. Run ``make clean && make html`` and verify zero new warnings.

Decision Notes
--------------

This model intentionally keeps all real content under OS directories.
No compatibility wrapper layer is used in this clean update model.

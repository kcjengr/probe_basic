=============================
Trixie Develop Release Notes
=============================

This section tracks Debian 13 Trixie develop release updates for Probe Basic and related packages.

July 17, 2026 - Develop Update Release Notes
--------------------------------------------

**Database Tool Table for Mill Configurations**

Mill configurations can now store tool data in a SQLite database instead of the classic ``.tbl`` file, using LinuxCNC's native tool database interface. LinuxCNC and the Probe Basic tool table editor read and write the same database file, so the GUI and the machine can never disagree about tool data.

- Unified tool table editor on the tool page: core offset columns plus mill extras stored per tool, including a new **ATC column** marking whether each tool is storable in the ATC carousel.
- Enabled per config with ``[EMCIO] DB_PROGRAM = ./tool_db.sh`` and ``TOOL_DB_FILE``, plus ``CONFIG_FILE = custom_config.yml`` (wired for the DB tool table plugin) in ``[DISPLAY]``. The classic ``.tbl`` workflow remains available for a hand-built machine config that wants it.
- New import tools in the **Tools** menu seed a database from existing tool data: legacy ``.tbl`` files, Fusion 360 tool library exports (``.tools``/``.json``), or both merged by tool number. Importers write to a standalone file (never the live database) and offer to point the INI at the result, with an automatic INI backup.
- New reference sim config: ``configs/atc_sim/vmc_index_inch.ini``.
- New documentation page: :doc:`/debian_13_trixie/configuration/db_tool_table`.

**Database Tool Table Is Now the Standard for All Sim Configs**

Every sim config that ships a ``.desktop`` launcher (``atc_sim`` - all four inch/metric/index/graycode variants, ``rack_atc_sim``, ``probe_basic``, and ``probe_basic_lathe``) now runs the database tool table by default. The ``_db``-suffixed filenames used while this was an opt-in variant (``vmc_index_inch_db.ini``, ``custom_config_db.yml``) are gone - there is no longer a non-database sibling to distinguish them from, so the plain names (``custom_config.yml``, etc.) are the database-backed configs.

- ``probe_basic_lathe_db`` (the separate database-backed lathe folder) has been folded into ``probe_basic_lathe`` - it is no longer a separate directory. The classic ``.tbl``-based lathe config it replaces has been removed.
- ``rack_atc_sim`` and ``probe_basic`` (the base mill, no ATC) gained the database tool table for the first time as part of this change.
- The legacy ``.tbl`` files backing these sim configs were deleted; the database files they seeded remain in each config folder.
- ``probe_basic_asm`` and ``probe_basic_robot`` are unaffected - neither ships a launcher today.

**Manual Tool Change Fallback for Carousel ATC Machines**

The carousel M6 remap no longer aborts when a change cannot be completed automatically - it parks the carousel, shows the manual tool change dialog, and waits for the operator to swap the tool by hand. This covers tools not stored in the carousel, a full carousel, and tools flagged manual only.

- Unchecking a tool's ATC column in the database tool table makes it **manual only**: it is never stored into or fetched from the carousel - for oversize tools that do not fit between carousel pockets.
- The dialog now words the prompt for what the operator actually has to do. Manual removals show a bright red warning naming the cause (tool flagged non storable, or carousel full) instead of a routine-looking "insert tool" prompt, since confirming a removal without actually removing the tool could crash an oversize tool into the carousel on a later store attempt. An optional warning icon on the dialog is supported via the ``toolchange_dialog_pb.ui`` file, and terminal recovery commands for ending a manual change are documented in the Carousel ATC Setup page.
- Optional drawbar interlock: set ``[ATC] DRAWBAR_MONITOR_PIN`` to a HAL pin or signal reflecting drawbar actuation and the dialog resume button stays disabled during a manual removal until the drawbar has been pressed and released - physical evidence the tool came out. Fails open (button enables, error logged) if the pin cannot be read, so a misconfiguration can never strand the operator mid-change.
- Optional ``[ATC] MANUAL_CHANGE_X`` / ``MANUAL_CHANGE_Y`` move the head to a convenient position for hand swaps.
- Documented in :doc:`/debian_13_trixie/configuration/atc_setup`.

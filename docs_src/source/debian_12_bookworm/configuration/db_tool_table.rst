===================
Database Tool Table
===================

Overview
--------

Probe Basic mill configurations can now store tool data in a SQLite database
file (``.db``) instead of the classic LinuxCNC tool table file (``.tbl``).
This uses LinuxCNC's native tool database interface: LinuxCNC itself reads and
writes tools through a small backend program, and Probe Basic's tool table
editor opens the very same database file, so the GUI and the machine can never
disagree about tool data - one file is the single source of truth.

What the database version adds over the ``.tbl`` file:

- A unified tool table editor on the tool page with the core offset columns
  plus mill extras stored per tool.
- An **ATC column** (checkbox) marking whether each tool is storable in the
  ATC carousel. Unchecking it makes a tool "manual only" - the carousel M6
  remap will never try to store or fetch it, and instead walks the operator
  through a hand swap with the manual tool change dialog. This is meant for
  oversize tools that physically do not fit between carousel pockets. See
  :doc:`atc_setup` for how manual-only tools behave during tool changes.
- Import tools in the **Tools** menu to seed a database from your existing
  ``.tbl`` file and/or a Fusion 360 tool library export.
- Keep as many named ``.db`` files as you like in the config folder (backups,
  per-job tool sets); which one is live is a single INI line.

The classic ``.tbl`` workflow remains fully supported - the database version
is opt-in per machine configuration.

How it works
------------

Two halves, both pointed at the same file:

- **LinuxCNC side:** ``[EMCIO] DB_PROGRAM = ./tool_db.sh`` tells LinuxCNC to
  start the bundled wrapper script, which runs qtpyvcp's tool database
  backend (``qtpyvcp.tools.tool_db_backend``). LinuxCNC talks to it over the
  standard tooldb protocol for every tool lookup, offset update, and tool
  change. When ``DB_PROGRAM`` is set, the ``TOOL_TABLE`` entry is not used.
- **Probe Basic side:** ``[DISPLAY] CONFIG_FILE = custom_config_db.yml``
  loads the database tool table plugin (with the mill extras table) instead
  of the file-based one, which drives the unified editor on the tool page.

Both halves resolve the database file the same way: ``[EMCIO] TOOL_DB_FILE``
if set, otherwise ``tool_table.db`` in the config folder.

Enabling it in a machine config
-------------------------------

The atc_sim configuration ships a complete working reference:
``configs/atc_sim/vmc_index_inch_db.ini``.

1. Copy ``tool_db.sh`` and ``custom_config_db.yml`` from the atc_sim config
   folder into your machine config folder. Make sure the script stays
   executable (``chmod +x tool_db.sh``).

2. Edit your machine INI:

   .. code-block:: bash

      [DISPLAY]
      CONFIG_FILE = custom_config_db.yml
      #  loads the database tool table plugin in Probe Basic
      #  (replaces the custom_config.yml line)

      [EMCIO]
      #TOOL_TABLE = tool.tbl
      #  comment out: TOOL_TABLE is not used when DB_PROGRAM is set

      DB_PROGRAM = ./tool_db.sh
      #  LinuxCNC starts this backend and reads/writes all tool data
      #  through it (LinuxCNC tool database interface)

      TOOL_DB_FILE = my_machine_tools.db
      #  which database file in this config folder is live; omit to
      #  default to tool_table.db. Switching tool sets is this one
      #  line plus a restart.

3. Seed the database from your existing tool data (pick one):

   - **Tools menu importers** (recommended): with Probe Basic running, use
     the entries in the **Tools** menu:

     - *Import Legacy Tool Table [.tbl]* - your classic ``.tbl`` file, core
       columns only.
     - *Import Fusion 360 Tool Library [.tools/.json]* - tool numbers,
       cutting diameters and descriptions from a Fusion library export.
     - *Import + Merge .tbl and Fusion Library* - machine data (offsets,
       pocket) from the ``.tbl``, tool identity (diameter, description) from
       Fusion, merged by tool number.

     The importers write to a standalone destination file (never the live
     database), so they are safe to run at any time. After a successful
     import the dialog offers to point ``TOOL_DB_FILE`` at the new file for
     you - the INI is backed up first, and the change takes effect on the
     next restart.

   - **Command line:** ``tbl2db my_old_table.tbl my_machine_tools.db``

   - **Start empty:** skip seeding entirely; the database file is created
     on first launch and tools can be added in the editor.

4. Restart LinuxCNC / Probe Basic and verify the tool page shows your tools.
   Every imported tool starts with the ATC column checked (storable); uncheck
   it for oversize tools that must never enter the carousel.

Switching back to the ``.tbl`` file
-----------------------------------

Reverting is the mirror of step 2: uncomment ``TOOL_TABLE``, comment out
``DB_PROGRAM`` and ``TOOL_DB_FILE``, and point ``CONFIG_FILE`` back at
``custom_config.yml``. The ``.db`` file stays in the folder untouched, so you
can switch back and forth while trying it out. Note that offset changes made
in one mode do not flow into the other - the ``.tbl`` and ``.db`` files are
independent once created.

Notes
-----

- ``tool_db.sh`` finds a Python interpreter with qtpyvcp installed by
  walking ``PATH`` itself, so the same config folder works unchanged on a
  machine with an apt install or a development install - nothing
  machine-specific is hardcoded in the config.
- The database is plain SQLite: back it up by copying the ``.db`` file while
  the machine is shut down.

#!/bin/bash
# LinuxCNC tool database program wrapper (tooldb interface).
# Referenced by probe_basic_lathe_db.ini: [EMCIO] DB_PROGRAM = ./tool_db.sh
#
# Runs the qtpyvcp tool_db_backend against tool_table.db in this config dir —
# the same file the DBToolTable GUI plugin opens (single source of truth).
# Seed the database first:  python3 ~/dev/scratch/qtpyvcp/tests/seed_db_from_tbl.py
#
# Uses whatever "python3" is already on PATH -- qtpyvcp must already be
# importable from it (system dist-packages on an installed/apt machine, or
# an activated dev venv here) -- no machine-specific paths hardcoded, so
# this config folder stays copyable to any machine as-is.

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

exec python3 -m qtpyvcp.tools.tool_db_backend "$DIR/tool_table.db" debug

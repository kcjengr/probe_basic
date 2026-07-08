#!/bin/bash
# LinuxCNC tool database program wrapper (tooldb interface, Phase 1 gate demo).
# Referenced by probe_basic_lathe_db.ini: [EMCIO] DB_PROGRAM = ./tool_db.sh
#
# Runs the qtpyvcp tool_db_backend against tool_table.db in this config dir —
# the same file the DBToolTable GUI plugin opens (single source of truth).
# Seed the database first:  python3 ~/dev/scratch/qtpyvcp/tests/seed_db_from_tbl.py

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export PYTHONPATH="$HOME/dev/qtpyvcp/src:$HOME/dev/linuxcnc/lib/python:$PYTHONPATH"

exec "$HOME/dev/venv/bin/python" \
    "$HOME/dev/qtpyvcp/src/qtpyvcp/tools/tool_db_backend.py" \
    "$DIR/tool_table.db" debug

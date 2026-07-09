#!/bin/bash
# LinuxCNC tool database program wrapper (tooldb interface).
# Referenced by probe_basic_lathe_db.ini: [EMCIO] DB_PROGRAM = ./tool_db.sh
#
# Runs the qtpyvcp tool_db_backend against tool_table.db in this config dir —
# the same file the DBToolTable GUI plugin opens (single source of truth).
# Seed the database first:  python3 ~/dev/scratch/qtpyvcp/tests/seed_db_from_tbl.py
#
# Deliberately does NOT just exec a bare "python3": LinuxCNC's own launcher
# puts /usr/bin ahead of an active dev venv in PATH for the processes it
# spawns (this runs as [EMCIO] DB_PROGRAM, a child of `io`), so a bare
# `python3` can silently resolve to a system interpreter with no qtpyvcp
# installed, even on a machine where a working venv is also on PATH --
# confirmed via io's own /proc/<pid>/environ showing /usr/bin before the
# venv. Walk PATH ourselves and use the first python3 that can actually
# import qtpyvcp -- correct whether qtpyvcp lives in a dev venv or the
# system dist-packages (a real apt install), no machine-specific path
# hardcoded, so this config folder stays copyable to any machine as-is.

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python3_bin=""
IFS=':' read -ra path_dirs <<< "$PATH"
for path_dir in "${path_dirs[@]}"; do
    candidate="$path_dir/python3"
    if [ -x "$candidate" ] && "$candidate" -c "import qtpyvcp.tools.tool_db_backend" >/dev/null 2>&1; then
        python3_bin="$candidate"
        break
    fi
done

if [ -z "$python3_bin" ]; then
    echo "tool_db.sh: no python3 on PATH has qtpyvcp installed" >&2
    exit 1
fi

exec "$python3_bin" -m qtpyvcp.tools.tool_db_backend "$DIR/tool_table.db" debug

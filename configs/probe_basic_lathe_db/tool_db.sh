#!/bin/bash
# LinuxCNC tool database program wrapper (tooldb interface).
# Referenced by probe_basic_lathe_db.ini: [EMCIO] DB_PROGRAM = ./tool_db.sh
#
# Runs the qtpyvcp tool_db_backend against a tool database file in this
# config dir -- the same file the DBToolTable GUI plugin opens (single
# source of truth, see db_tool_table.py's _default_db_path -- kept in sync
# with the INI lookup here on purpose, or the GUI and this backend could
# silently disagree about which file is "live").
#
# WHICH FILE: [EMCIO] TOOL_DB_FILE in the ini if set, else "tool_table.db"
# in this same folder. This is deliberately a SEPARATE ini line from
# DB_PROGRAM, not an argument tacked onto it -- keep as many named .db
# files as you want in this folder (backups, per-job tool sets, etc.);
# switching which one loads is one line + a restart, and nothing is ever
# "the" database except by that one explicit reference, so nothing here
# can silently clobber another file.
#
# Seed a new database from a legacy .tbl file with: tbl2db old.tbl NAME.db
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

# First value for KEY within [SECTION] of an ini file, LinuxCNC ini
# conventions (# starts a comment, values may carry a trailing comment).
ini_get() {
    awk -F= -v section="[$1]" -v key="$2" '
        $0 == section { in_section=1; next }
        /^\[/ { in_section=0 }
        in_section && $1 ~ "^[ \t]*" key "[ \t]*$" {
            sub(/^[^=]*=[ \t]*/, "")
            sub(/[ \t]*#.*$/, "")
            sub(/[ \t]*$/, "")
            print
            exit
        }
    ' "$3"
}

DB_FILE="tool_table.db"
if [ -n "$INI_FILE_NAME" ] && [ -f "$INI_FILE_NAME" ]; then
    configured="$(ini_get EMCIO TOOL_DB_FILE "$INI_FILE_NAME")"
    if [ -n "$configured" ]; then
        DB_FILE="$configured"
    fi
fi

case "$DB_FILE" in
    /*) DB_PATH="$DB_FILE" ;;
    *)  DB_PATH="$DIR/$DB_FILE" ;;
esac

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

exec "$python3_bin" -m qtpyvcp.tools.tool_db_backend "$DB_PATH" debug

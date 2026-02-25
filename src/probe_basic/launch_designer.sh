#!/bin/bash
#
# Launch Qt Designer with Probe Basic stylesheet loaded for live preview
#
# This script sets the QSS_STYLESHEET environment variable so that Qt Designer
# can load and display the probe_basic.qss stylesheet in real-time.
#
# SINGLE SOURCE OF TRUTH WORKFLOW:
# 1. Edit probe_basic.qss for all styling changes
# 2. Use this script to open probe_basic.ui in Designer with styling preview
# 3. The .ui file has NO embedded stylesheet - only .qss file exists
# 4. Both Designer and runtime load from the same .qss file
#

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
QSS_FILE="$SCRIPT_DIR/probe_basic.qss"
UI_FILE="$SCRIPT_DIR/probe_basic.ui"

# Activate virtual environment if it exists
if [ -f "/home/g0704/Dev/venv/bin/activate" ]; then
    source /home/g0704/Dev/venv/bin/activate
fi

echo "=================================================="
echo "  Probe Basic Qt Designer Launcher"
echo "=================================================="
echo "Stylesheet: $QSS_FILE"
echo "UI File:    $UI_FILE"
echo ""
echo "✅ Single Source of Truth: probe_basic.qss"
echo "=================================================="
echo ""

# Launch editvcp (the proper tool for editing QtPyVCP UIs)
# Using --qss-file ensures Designer shows styling without embedding it in the .ui file
if command -v editvcp &> /dev/null; then
    editvcp --ui-file="$UI_FILE" --qss-file="$QSS_FILE"
else
    echo "ERROR: editvcp not found!"
    echo "Please ensure QtPyVCP is installed:"
    echo "  pip install -e /path/to/qtpyvcp"
    exit 1
fi

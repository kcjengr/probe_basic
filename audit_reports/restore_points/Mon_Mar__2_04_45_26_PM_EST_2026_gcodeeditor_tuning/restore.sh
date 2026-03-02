#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="/home/g0704/Dev"

cp -f "$SCRIPT_DIR/editor_widget/gcodeeditor.h" "$ROOT_DIR/editor_widget/gcodeeditor.h"
cp -f "$SCRIPT_DIR/editor_widget/gcodeeditor.cpp" "$ROOT_DIR/editor_widget/gcodeeditor.cpp"
cp -f "$SCRIPT_DIR/editor_widget/gcodehighlighter.h" "$ROOT_DIR/editor_widget/gcodehighlighter.h"
cp -f "$SCRIPT_DIR/editor_widget/gcodehighlighter.cpp" "$ROOT_DIR/editor_widget/gcodehighlighter.cpp"
cp -f "$SCRIPT_DIR/probe_basic/src/probe_basic_lathe/probe_basic_lathe_dark.qss" "$ROOT_DIR/probe_basic/src/probe_basic_lathe/probe_basic_lathe_dark.qss"

echo "Restored files from: $SCRIPT_DIR"

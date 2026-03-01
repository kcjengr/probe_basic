#!/bin/bash

source ~/Dev/venv/bin/activate
cd ~/Dev/

VCP_DIR="$HOME/Dev/probe_basic/src/probe_basic"
LIGHT_QSS="$VCP_DIR/probe_basic_light.qss"
DARK_QSS="$VCP_DIR/probe_basic_dark.qss"

THEME="light"
if command -v python >/dev/null 2>&1; then
	THEME="$(python - <<'PY'
import sys
try:
	from PySide6.QtWidgets import QApplication
	from PySide6.QtGui import QPalette
except Exception:
	print("light")
	sys.exit(0)

app = QApplication.instance() or QApplication([])
palette = app.palette()
window_lightness = palette.color(QPalette.Window).lightness()
base_lightness = palette.color(QPalette.Base).lightness()
print("dark" if ((window_lightness + base_lightness) / 2) < 128 else "light")
PY
)"
fi

if [[ "$THEME" == "dark" ]]; then
	QSS_FILE="$DARK_QSS"
else
	QSS_FILE="$LIGHT_QSS"
fi

editvcp probe_basic --qss-file="$QSS_FILE"

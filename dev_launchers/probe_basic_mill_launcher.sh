#!/bin/bash

source ~/dev/venv/bin/activate

# $1 is an ini path relative to configs/, e.g. probe_basic/probe_basic.ini
INI="${1:-probe_basic/probe_basic.ini}"
cd ~/dev/probe_basic/configs/"$(dirname "$INI")"
linuxcnc "$(basename "$INI")"
#!/bin/bash

source ~/dev/venv/bin/activate

# $1 is an ini path relative to configs/, e.g. rack_atc_sim/vmc_index_inch.ini
INI="${1:-rack_atc_sim/vmc_index_inch.ini}"
cd ~/dev/probe_basic/configs/"$(dirname "$INI")"
linuxcnc "$(basename "$INI")"
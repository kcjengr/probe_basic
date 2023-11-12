#!/bin/bash

source ~/dev/venv/bin/activate
cd ~/dev/probe_basic/linuxcnc/configs/probe_basic
linuxcnc probe_basic.ini

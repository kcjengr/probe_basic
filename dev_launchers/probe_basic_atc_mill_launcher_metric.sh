#!/bin/bash

source ~/dev/venv/bin/activate
cd ~/dev/probe_basic/configs/atc_sim
linuxcnc vmc_index_metric.ini

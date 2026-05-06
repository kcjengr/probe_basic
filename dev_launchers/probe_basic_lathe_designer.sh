#!/bin/bash

source ~/dev/venv/bin/activate
cd ~/dev/

# Include primary lathe_conv config so settings appear in Designer tools
export VCP_CONFIG_FILES="${VCP_CONFIG_FILES:+${VCP_CONFIG_FILES}:}${HOME}/dev/pb_lathe_conv/src/lathe_conversational/lathe_conv.yml"

editvcp probe_basic_lathe

#!/usr/bin/env bash

# install python deps
pip install docopt qtpy pyudev psutil HiYaPyCo

libpath="/usr/lib/x86_64-linux-gnu/qt5/plugins/designer"
oldlib=$libpath/"libpyqt5.so"
if [ -f "$oldlib" ]
then
    echo "renaming existing libpyqt5.so to libpyqt5.so.old"
    mv "$oldlib" "$oldlib.old"
fi

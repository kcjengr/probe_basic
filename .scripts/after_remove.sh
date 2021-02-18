#!/usr/bin/env bash

# unrename the old libpyqt5.so file
libpath="/usr/lib/x86_64-linux-gnu/qt5/plugins/designer"
oldlib="${libpath}/libpyqt5.so.old"
if [ -f "$oldlib" ]
then
    echo "renaming libpyqt5.so.old to libpyqt5.so"
    mv "$oldlib" "${libpath}/libpyqt5.so"
fi

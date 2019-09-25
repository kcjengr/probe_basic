#!/usr/bin/env bash

echo 'Installing fpm gem...'
gem install fpm

echo 'Creating debs dir'
mkdir debs

export DEB_BUILD=true

echo 'Building debian package in debs/...'
fpm -t deb \
    -p debs/ \
    -s python \
    -f \
    --license "GPLv2" \
    --vendor "Lcvette" \
    --maintainer "'Lcvette'" \
    --url "https://github.com/kcjengr/probe_basic" \
    --description "ProbeBasic - QtPyVCP interface for LinuxCNC." \
    -d python-pip \
    -d python-pyqt5 \
    -d python-dbus.mainloop.pyqt5 \
    -d python-pyqt5.qtopengl \
    -d python-pyqt5.qsci \
    -d python-pyqt5.qtmultimedia \
    -d python-pyqt5.qtquick \
    -d gstreamer1.0-plugins-bad \
    -d libqt5multimedia5-plugins \
    -d pyqt5-dev-tools \
    -d qttools5-dev-tools \
    --after-install .travis/after_install.sh \
    --after-remove .travis/after_remove.sh \
    --no-auto-depends \
    --verbose \
    setup.py

unset DEB_BUILD
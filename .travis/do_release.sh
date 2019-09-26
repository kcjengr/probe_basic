#!/usr/bin/env bash

echo '------------- Building Python Package -------------'
python setup.py sdist

echo '------------- Building Debian Package -------------'
./.travis/build_deb.sh

echo '------------ Publishing GitHub Release ------------'
./.travis/publish_github_release.sh

echo '------------- Publishing PyPi Release -------------'
./.travis/publish_pypi_release.sh
#!/usr/bin/env bash

echo 'Installing twine... '
pip install twine

echo -n 'Using setuptools version: '
python -c "import setuptools; print setuptools.__version__"

echo 'Uploading files to PyPi...'
twine upload \
    --username kcjengr \
    --password $PYPI_PASS \
    'dist/qtpyvcp*.tar.gz'

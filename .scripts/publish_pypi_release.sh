#!/usr/bin/env bash

PYPI_AUTH=$1

echo 'Installing twine... '
pip install twine

echo -n 'Using setuptools version: '
python -c "import setuptools; print(setuptools.__version__)"

echo 'Uploading files to PyPi...'
twine upload \
    --username __token__ \
    --password $PYPI_AUTH \
    'dist/*'

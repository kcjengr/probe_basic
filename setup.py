#!/usr/bin/env python3
import sys
import os

# Add src to path so we can import versioneer
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import versioneer
from setuptools import setup

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)

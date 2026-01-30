#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import setuptools
import versioneer

if __name__ == "__main__":
    setuptools.setup(
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
    )

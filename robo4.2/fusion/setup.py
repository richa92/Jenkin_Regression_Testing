#!/usr/bin/env python
"""
FusionLibrary setup file.  Please do not run directly (python setup.py).
Instead, run install.bat or install.sh.
"""

import sys
from setuptools import setup, find_packages

DESCRIPTION = """
FusionLibrary is built as an external python test library for Fusion/OneView automation.
It's a library for Fusion product specific API, CLI and UI interfaces.
"""[1:-1]

setup(name='FusionLibrary',
      version=5.00,
      description='Fusion Web, API and CLI testing library for Robot Framework',
      long_description=DESCRIPTION,
      author='EM DVT , AM DVT, Cosmos, FVT CRM',
      author_email='<emgmtdvt@hp.com> ,  <amdvt@hp.com> ,  <cosmos_automation@hp.com>',
      url='',
      keywords='fusion FusionLibrary robotframework robogalaxy robogalaxylibrary',
      platforms='any',
      classifiers=[
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Topic :: Software Development :: Testing"
      ],
      install_requires=[
          'datadiff == 2.0.0',
          'GitPython == 2.1.11',
          'RoboGalaxyLibrary == 3.0'
      ] + (['pyautoit == 0.4'] if "win" in sys.platform else []),
      packages=find_packages()
      )

#!/usr/bin/env python
""" Package setup file """
from setuptools import setup, find_packages


DESCRIPTION = """
i3SLibrary is the automation framework for the HP i3S Product.
This library is dependent on the RoboGalaxyLibrary and FusionLibrary.
"""[1:-1]

setup(name='i3SLibrary',
      version='1.0',
      description='Web, API and CLI testing library for Robot Framework',
      long_description=DESCRIPTION,
      author='i3S Automation Team',
      author_email='PDL-TBird-i3S-QA <pdl-tbird-i3s-qa@hp.com',
      url='https://cgit-pro.houston.hpecorp.net/gerrit/i3s',
      keywords='i3S i3SLibrary',
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
          'RoboGalaxyLibrary==3.0',
          'FusionLibrary==5.0',
          'urllib3'],
      packages=find_packages())

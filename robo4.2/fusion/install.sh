#!/bin/bash
# This script will install using pip from your local folder.
# Note that it will download dependencies from the RoboGalaxyLibrary binary repository
# and will install in "development" mode.


ver=$(python --version 2>&1 | sed 's/.* \([0-9]\).\([0-9]\).*/\1\2/')
if [ "$ver" -ne "27" ]; then
  echo "Python version is $ver.  This version is not supported by RoboGalaxy"
  exit 1
fi

export PIP_CONFIG_FILE=pip.ini
python -m pip install -U pip
python -m pip uninstall -y FusionLibrary RoboGalaxyLibrary
python -m pip install -U -e .

#!/bin/sh

PROXY=web-proxy.houston.hpecorp.net:8080

export http_proxy=http://$PROXY
export https_proxy=https://$PROXY

HOST=robogalaxy.us.rdlabs.hpecorp.net
REPO=RoboGalaxyLibrary-300-cp27-linux_x86_64
REPO_URL=https://$HOST/repo/$REPO

PYVER=$(python -c "import sys; print(sys.version)")
COMMIT=$(git rev-parse HEAD)
python -m pip install --upgrade pip
python -m pip install pep8 pylint virtualenv

virtualenv py27
source py27/bin/activate
pip wheel --trusted-host $HOST -f $REPO_URL -w dist .

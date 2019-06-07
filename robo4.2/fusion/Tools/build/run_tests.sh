#!/bin/bash

export PATH=/usr/local/bin:$PATH
VENV=pyenv
GIT_COMMIT=$(git rev-list --max-count=1 HEAD)

if [ ! -d $VENV ]; then
    virtualenv $VENV
fi

source $VENV/bin/activate
source ./install.sh

echo Files in this commit:
printf "\t%s\n" $(git diff-tree --no-commit-id --name-only --diff-filter=ACM -r $GIT_COMMIT)

# pep8
echo Running pep8
git diff-tree --no-commit-id --name-only --diff-filter=ACM -r $GIT_COMMIT | grep '\.py$' | awk '{print "\x22" $0 "\x22"}' | xargs -r pep8 --ignore=E501 $files
if [ $? != 0 ]; then
    exit $?
fi

# pylint
echo Running pylint
git diff-tree --no-commit-id --name-only --diff-filter=ACM -r $GIT_COMMIT | grep '\.py$' | awk '{print "\x22" $0 "\x22"}' | xargs -r pylint --rcfile=./Tools/lint/pylint.gate.rc '--msg-template={path}:{line}: [{msg_id}({symbol}), {obj}] {msg}'
if [ $? != 0 ]; then
    exit $?
fi

# rflint
echo Running rflint
git diff-tree --no-commit-id --name-only --diff-filter=ACM -r $GIT_COMMIT | grep '\.txt$\|\.robot$' | awk '{print "\x22" $0 "\x22"}' | xargs -r rflint --argumentfile=.rflintrc --format "RFLINT: {severity}: {linenumber}, {char}: {message} ({rulename})"
if [ $? != 0 ]; then
    exit $?
fi

# import test
which python
python -c "import FusionLibrary"
if [ $? != 0 ]; then
  exit $?
fi

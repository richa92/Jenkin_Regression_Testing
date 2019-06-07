#!/bin/sh

pip install pylint
COMMIT=$(git rev-parse HEAD)
git diff-tree --no-commit-id --name-only --diff-filter=ACM -r $COMMIT | grep "\\.py" | awk '{print "\\x22" $0 "\\x22"}' | xargs -r pylint --rcfile=.pylintrc

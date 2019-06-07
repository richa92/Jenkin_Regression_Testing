#!/bin/sh

pip install pep8
COMMIT=$(git rev-parse HEAD)
git diff-tree --no-commit-id --name-only --diff-filter=ACM -r $COMMIT | grep "\\.py" | awk '{print "\\x22" $0 "\\x22"}' | xargs -r pep8 --config=.pep8

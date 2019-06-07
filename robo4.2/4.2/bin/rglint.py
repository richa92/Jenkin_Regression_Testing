#!/robo4.2/4.2/bin/python
"""rglint.py is a convenient pylint wrapper that specifies the rg pylint rules,
and acts as a document of the agreed upon RoboGalaxy rules.
Usage: rglint.py <module|file>"""

import sys
from pkg_resources import resource_filename
from subprocess import call

if len(sys.argv) > 1:
    rglintrc = resource_filename(__name__, '../data/rglint.rc')
    call('pylint --rcfile=' + rglintrc + ' ' + " ".join(sys.argv[1:]), shell=True)
else:
    print "Usage: rglint.py <module|file>"

#!/robo4.2/4.2/bin/python
"""rgpep8.py is a convenient pep8 wrapper that specifies the rg pep8 rules,
and acts as a document of the agreed upon RoboGalaxy rules.
Usage: rgpep8.py <file|path>"""

import sys
from subprocess import call
if len(sys.argv) > 1:
    call('pep8 --ignore=E501 ' + " ".join(sys.argv[1:]), shell=True)
else:
    print "Usage: rgpep8.py <file|path>"

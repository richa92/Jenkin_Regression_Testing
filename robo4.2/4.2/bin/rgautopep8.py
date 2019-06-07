#!/robo4.2/4.2/bin/python
"""rgautopep8.py is a convenient autopep8 wrapper that specifies the
rg pep8 rules, and makes it easier to use autopep8.
Usage: rgautopep8.py <file|path>"""

import sys
from subprocess import call
if len(sys.argv) > 1:
    call('autopep8 -j 0 --ignore E501 -a -a -a -a -a -a -a -i -r ' + " ".join(sys.argv[1:]), shell=True)
else:
    print "Usage: rgautopep8.py <file|path>"

#!/robo4.2/4.2/bin/python
# EASY-INSTALL-ENTRY-SCRIPT: 'jsonpath-rw','console_scripts','jsonpath.py'
__requires__ = 'jsonpath-rw'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('jsonpath-rw', 'console_scripts', 'jsonpath.py')()
    )

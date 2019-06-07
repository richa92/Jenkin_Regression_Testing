"""
Version file to initialize interpreter for OvsLibrary.
"""

import sys

VERSION = '5.00'
RELEASE = 'beta'


def get_version(sep=' '):
    """
    To check the final version of the appliance
    :param sep:
    :return:
    """
    if RELEASE == 'beta':
        return VERSION
    return VERSION + sep + RELEASE


def get_full_version(who=''):
    """
    To get the version of Python and interpreter used
    :param who:
    :return:
    """
    sys_version = sys.version.split()[0]
    version = '%s %s (%s %s on %s)' \
        % (who, get_version(), _get_interpreter(), sys_version, sys.platform)
    return version.strip()


def _get_interpreter():
    """
    To check the interpreter
    :return:
    """
    if sys.platform.startswith('java'):
        return 'Jython'
    if sys.platform == 'cli':
        return 'IronPython'
    if 'PyPy' in sys.version:
        return 'PyPy'
    return 'Python'

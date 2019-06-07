"""
OvsLibrary OneView Supportibility Keywords.

"""

import os
from robot import version as robot_version
from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib
from version import get_version
from FusionLibrary.keywords.fusion_api import FusionAPIKeywords
from ovs_api import OvsIndexResourceKeywords
from ovs_api import OvsTaskKeywords
from ovs_api import OvsEventKeywords
from ovs_ui import OVSUIKeywords
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
execfile(os.path.join(THIS_DIR, 'version.py'))
__version__ = get_version()


class OvsLibrary(
        FusionAPIKeywords,
        FusionAPIKeywords.LoginSessionKeywords,
        OvsIndexResourceKeywords,
        OvsTaskKeywords,
        OvsEventKeywords,
        OVSUIKeywords):
    """
    This class is used for OVS related keywords
    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self):
        logger._log_to_console_and_log_file(
            "Fusion library version %s" % __version__)
        for base in OvsLibrary.__bases__:
            base.__init__(self)

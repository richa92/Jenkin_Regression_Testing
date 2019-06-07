# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Activity Page
"""


from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.general.activity_elements import FusionActivityPage
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco
from robot.libraries.BuiltIn import BuiltIn


class CommonOperationActivity(object):

    @classmethod
    def get_latest_activity(cls, wait_timeout=5, fail_if_false=True):
        logger.debug("GETTING THE LATEST MSG IN ACTIVITY PAGE")
        ui_lib.is_visible(FusionActivityPage.ID_LATEST_ACTIVITY_LABEL, wait_timeout, fail_if_false)
        return ui_lib.get_text(FusionActivityPage.ID_LATEST_ACTIVITY_LABEL, wait_timeout, fail_if_false)

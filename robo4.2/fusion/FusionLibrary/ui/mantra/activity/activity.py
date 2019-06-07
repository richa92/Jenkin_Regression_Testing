# (C) Copyright 2014 Hewlett-Packard Development Company, L.P.

"""
    Activity Page
"""

from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.mantra.activity.activity_elements import activityPage


def checkAddBladeTasks():
    # Checking Add task
    failure = False
    if ((ui_lib.wait_for_element_visible(activityPage.ID_ADD_NAME, timeout=60) and ui_lib.wait_for_element_visible(activityPage.ID_ADD_STATUS, timeout=60)) or (ui_lib.wait_for_element_visible(activityPage.ID_ADD_NAME2, timeout=60) and ui_lib.wait_for_element_visible(activityPage.ID_ADD_STATUS2, timeout=60))):
        logger._log_to_console_and_log_file(" Add task was correctly completed")
    else:
        logger._log_to_console_and_log_file(" Add task was completed with Errors")
        failure = True

    # Checking the Health task
    if (ui_lib.wait_for_element_visible(activityPage.ID_HEALTH_MESSAGE, timeout=60) and ui_lib.wait_for_element_visible(activityPage.ID_HEALTH_STATUS, timeout=600)):
        logger._log_to_console_and_log_file("- Health status is OK")
    else:
        logger._log_to_console_and_log_file("- Health status is NOT OK")
        failure = True

    # Checking test result
    if failure:
        ui_lib.fail_test("- At least one task was not completed. Please check the 'Health' or the 'Add' task status")

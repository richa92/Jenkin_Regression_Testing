# (C) Copyright 2014 Hewlett-Packard Development Company, L.P.

"""
    Enclosures Page
"""

from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.mantra.enclosures.enclosures_elements import enclosuresPage


def wait_for_blade_to_be_added(encSettings):
    logger._log_to_console_and_log_file(" Waiting for the blade be added...")
    if ui_lib.wait_for_element_visible(enclosuresPage.ID_BLADE % str(encSettings.expansionBayNumber), timeout=300):
        # Waiting for the blade be added...
        if ui_lib.wait_for_element_visible(enclosuresPage.ID_BLADE_OK % str(encSettings.expansionBayNumber), timeout=300):
            logger._log_to_console_and_log_file("- Blade was successfully added")
        else:
            ui_lib.fail_test("- After 5 minutes, the blade status is NOT OK")
    else:
        ui_lib.fail_test("- Bay is empty")

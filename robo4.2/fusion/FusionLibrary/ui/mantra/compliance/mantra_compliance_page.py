# (C) Copyright 2014 Hewlett-Packard Development Company, L.P.

"""
    Mantra UI investigation using Compliance feature as example.
    Objectives: Understand and implement a UI test in RoboGalaxy framework structure
"""

from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.mantra.compliance.mantra_elements_compliance import MantraCompliancePage
from FusionLibrary.ui.general import base_page

# Navigate to compliance page


def navigate():
    base_page.navigate_base(MantraCompliancePage.ID_PAGE_LABEL, MantraCompliancePage.ID_MENU_LINK_COMPLIANCE, "css=span.hp-page-item-count")


def set_ok_filter():
    ui_lib.wait_for_element_and_click(MantraCompliancePage.ID_ALL_STATUSES_FILTER)
    BuiltIn().sleep(3)
    ui_lib.wait_for_element_and_click(MantraCompliancePage.ID_ALL_STATUSES_FILTER_SETED_OK)
    logger._log_to_console_and_log_file("")
    logger._log_to_console_and_log_file("OK option was checked")

# Check the enclosure status


def check_ok():
    # While we have enclosure in the list, check the status
    enc_number = 1
    while enc_number:
        # Setting the enclosure number
        enclosure_xpath = "xpath=//html/body/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div[2]/table/tbody/tr[" + str(enc_number) + "]/td[2]"
        # Check if the enclosure is present
        if ui_lib.wait_for_element_and_click(enclosure_xpath):
            BuiltIn().sleep(1)
            # Checking if the status is OK
            if ui_lib.wait_for_element_text(MantraCompliancePage.ID_EXPECTED_VALUE, "= 1"):
                logger._log_to_console_and_log_file("Enclosure " + str(enc_number) + " is OK")
            else:
                logger._log_to_console_and_log_file("Enclosure " + str(enc_number) + " is NOT OK")
                ui_lib.fail_test("Test FAILED")
            enc_number += 1
        else:
            logger._log_to_console_and_log_file("No more enclosures")
            break

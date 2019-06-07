# (C) Copyright 2013-2015 Hewlett-Packard Development Company, L.P.
"""
    Login Appliance for NEC Page
"""

from FusionLibrary.ui.general.rebranding_elements import RebrandLoginPage,\
    CertificateTypes, ProductName
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants

import Selenium2Library

selenium2lib = Selenium2Library.Selenium2Library()


def navigate():
    # Navigate to page
    base_page.navigate_base(RebrandLoginPage.ID_PAGE_SETTINGS,
                            FusionUIBaseElements.ID_MENU_LINK_SETTINGS,
                            "css=span.hp-page-item-count")
    # Verify
    if not ui_lib.wait_for_element_visible(RebrandLoginPage.ID_LINK_SETTINGS, PerfConstants.FUSION_PAGE_SYNC):
        logger._warn("Unable to open the settings page")
        return False
    return True


def product_name():

    testResult = True
    logger._log_to_console_and_log_file("########### Start to appliance NEC ###########")
    """ Login Page """
    testResult &= correctly_executed(ui_lib.wait_for_element_visible, RebrandLoginPage.ID_PRODUCT_NAME % ProductName.ONEVIEW_FOR_NEC,
                                     " --> Product Name in title: '%s' " % ProductName.ONEVIEW_FOR_NEC)


def rebrand_help():

    testResult = True
    logger._log_to_console_and_log_file("\n########### Accessing the Help icon on page ###########")
    testResult &= correctly_executed(ui_lib.wait_for_element_and_click, RebrandLoginPage.ID_ICON_HELP, " --> Clicking on Help icon ")
    testResult &= correctly_executed(ui_lib.wait_for_element_visible, RebrandLoginPage.ID_REST_REFERENCE, " --> Clicking REST API reference on this page ")
    testResult &= correctly_executed(ui_lib.wait_for_element_visible, RebrandLoginPage.ID_REST_HELP, " --> Clicking REST API help on this page ")
    testResult &= correctly_executed(ui_lib.wait_for_element_visible, RebrandLoginPage.ID_BROWSE_HELP, " --> Clicking Help on this page ")


def rebrand_certificates():

    testResult = True
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(RebrandLoginPage.ID_PAGE_SETTINGS):
        navigate()

    logger._log_to_console_and_log_file("\n########### Accessing the Settings page ###########")
    testResult &= correctly_executed(ui_lib.wait_for_element_and_click, RebrandLoginPage.ID_SETTINGS_SECURITY, " --> Clicking Security on this settings")
    testResult &= correctly_executed(ui_lib.wait_for_element_visible, RebrandLoginPage.LIST_REQUIRED_INFORMATION % CertificateTypes.NEC_CORPORATION,
                                     " --> Certificate in the organization name: '%s'" % CertificateTypes.NEC_CORPORATION)


def correctly_executed(function, parameters, message):
    """ Executes a generic function with parameters and prints a message based on its result """
    if function(parameters):
        logger._log_to_console_and_log_file(message + " was correctly displayed")
        return True
    else:
        logger._log_to_console_and_log_file(message + " was NOT correctly displayed. Failed to access: " + str(parameters))
        selenium2lib = ui_lib.get_s2l()
        selenium2lib.capture_page_screenshot()
        return False

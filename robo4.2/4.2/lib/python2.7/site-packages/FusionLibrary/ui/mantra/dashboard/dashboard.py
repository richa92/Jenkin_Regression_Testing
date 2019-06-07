# (C) Copyright 2014 Hewlett-Packard Development Company, L.P.

"""
    Dashboard page
"""

from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.mantra.dashboard.dashboard_elements import DashboardPage
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.general import base_page


def navigate():
    base_page.navigate_base(DashboardPage.ID_PAGE_LABEL, FusionUIBaseElements.ID_MENU_LINK_DASHBOARD, "css=span.hp-count")


def checkDashboardPage():

    if not ui_lib.wait_for_element_visible(DashboardPage.ID_PAGE_LABEL):
        navigate()

    FAILURE = False

    # Checking "Dashboard" page label
    logger._log_to_console_and_log_file("")
    if ui_lib.wait_for_element_visible(DashboardPage.ID_PAGE_LABEL):
        logger._log_to_console_and_log_file("- Dashboard page: OK ")
    else:
        logger._log_to_console_and_log_file("- Unable to access 'Dashboard' page")
        FAILURE = True

    # Check test result
    if FAILURE:
        ui_lib.fail_test("At least one page element was not found.")


def checkSystemProfilesDashboardStatus(expected_status):
    """ This method compares the UI status of the 'System Profiles' component with the input argument
        # Check the status inside the circle and the counters
        # Available inputs are:
            #  OK
            #  Warning
            #  Critical
            #  Other
    """

    if not ui_lib.wait_for_element_visible(DashboardPage.ID_PAGE_LABEL):
        navigate()

    logger._log_to_console_and_log_file("\nVerifying system profile donut status...")
    if (expected_status.lower() == 'critical'):
        status = DashboardPage.Status.CRITICAL
    elif (expected_status.lower() == 'warning'):
        status = DashboardPage.Status.WARNING
    elif (expected_status.lower() == 'ok'):
        status = DashboardPage.Status.OK
    elif (expected_status.lower() == 'other'):
        status = DashboardPage.Status.OTHER
    else:
        ui_lib.fail_test("\t- Status not recognized: " + expected_status + ", please use a valid dashboard status.")

    if __checkSystemProfilesDonutStatus(status):
        logger._log_to_console_and_log_file("\t- SystemProfiles donut is at status " + status)
    else:
        ui_lib.fail_test("\t- System Profiles donut at wrong status! Expected " + status)

    if __checkSystemProfilesSummaryStatus(status):
        logger._log_to_console_and_log_file("\t- SystemProfiles donut summary is at status " + status)
    else:
        ui_lib.fail_test("\t- System Profiles donut summary at wrong status! Expected " + status)


def __checkSystemProfilesDonutStatus(status):
    if ui_lib.wait_for_element_visible(DashboardPage.SYSTEM_PROFILES_DONUT_STATUS_LABEL % status):
        return True
    else:
        return False


def __checkSystemProfilesSummaryStatus(expectedStatus):
    # read counters from the UI
    try:
        ui_lib.wait_for_element_visible(DashboardPage.SYSTEM_PROFILES_CONTAINER_PATH)
        CriticalCounter = int(ui_lib.get_text(DashboardPage.SYSTEM_PROFILES_CRITICAL_COUNTER, timeout=2))
        WarningCounter = int(ui_lib.get_text(DashboardPage.SYSTEM_PROFILES_WARNING_COUNTER, timeout=2))
        OKCounter = int(ui_lib.get_text(DashboardPage.SYSTEM_PROFILES_OK_COUNTER, timeout=2))
        logger._log_to_console_and_log_file("\t- Counters found: Critical = %i | Warning = %i | OK = %i" % (CriticalCounter, WarningCounter, OKCounter))
    except Exception, e:
        logger._log_to_console_and_log_file(e)
        logger._log_to_console_and_log_file("\tWarning! At least one of the summary counters is not available")
        return False

    # define UI status based on the counters
    if (CriticalCounter + WarningCounter + OKCounter == 0):
        logger._warn("\tUnexpected behavior! We found all the counters and they're all empty!")
    if (CriticalCounter + WarningCounter == 0):
        currStatus = DashboardPage.Status.OK
    elif (CriticalCounter == 0):
        currStatus = DashboardPage.Status.WARNING
    else:
        currStatus = DashboardPage.Status.CRITICAL

    # final assertion
    if (currStatus == expectedStatus):
        return True
    else:
        logger._warn("\tChecking summary for System Profiles got %s summary and expected %s" % (currStatus, expectedStatus))
        return False

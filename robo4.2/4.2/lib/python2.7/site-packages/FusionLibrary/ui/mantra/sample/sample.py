# (C) Copyright 2014 Hewlett-Packard Development Company, L.P.

"""
    Mantra SAMPLE investigation using Server Profiles and Add Users pages as an example.
    Objectives: Understand the RoboGalaxy framework structure, create the Mantra structure and
    investigate what fusion/robo functions can be reused on Mantra scripts (e.g. navigate, load data file, etc...)
"""

from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.mantra.sample.sample_elements import SampleElements

# Navigate to server profiles page


def navigateServerProfiles():
    base_page.navigate_base(SampleElements.ID_PAGE_LABEL_SERVERS, SampleElements.ID_MENU_LINK_SERVER_PROFILE, "css=span.hp-page-item-count")

# Verify if the label "No server profiles" are being displayed


def VerStrLabel():
    if ui_lib.wait_for_element_visible(SampleElements.ID_STRING_TEST, PerfConstants.DEFAULT_SYNC_TIME):
        logger._log_to_console_and_log_file("Label found")
    else:
        logger._log_to_console_and_log_file("Label NOT found")
        ui_lib.fail_test("Test FAILED")

# Navigate to Users and Groups page


def navigateUsersAndGroups():
    base_page.navigate_base(SampleElements.ID_PAGE_LABEL_USERS, SampleElements.ID_LINK_ADD_USER, "css=span.hp-page-item-count")

# Wait until the "Add User" button be displayed and click


def adduser():
    ui_lib.wait_for_element_and_click(SampleElements.ID_ADD_USER_BUTTON)

    # If "Add User" form don't be displayed, click on button again
    if ui_lib.wait_for_element_visible(SampleElements.ID_LOGIN_NAME, PerfConstants.DEFAULT_SYNC_TIME):
        logger._log_to_console_and_log_file("Add User form was correctly displayed")
    else:
        ui_lib.wait_for_element_and_click(SampleElements.ID_ADD_USER_BUTTON)
        logger._log_to_console_and_log_file("A second click was necessary")

# Fill the user fields with valid data (from a data file)


def fillinfo(*user_obj):
    selenium2lib = ui_lib.get_s2l()
    ui_lib.wait_for_element(SampleElements.ID_LOGIN_NAME)

    # Copying the users to a list
    user_list = []
    for user in user_obj:
        user_list.append(user)

    # Filling the fields with the users from user_list
    for user in user_list:
        selenium2lib.input_text(SampleElements.ID_LOGIN_NAME, user.name)
        selenium2lib.input_text(SampleElements.ID_FULL_NAME, user.fullname)
        selenium2lib.input_text(SampleElements.ID_INITIAL_PASSWORD, user.password)
        selenium2lib.input_text(SampleElements.ID_CONFIRM_PASSWORD, user.password)
        ui_lib.wait_for_element_and_click(SampleElements.ID_FULL_RADIO)
        ui_lib.wait_for_element_and_click(SampleElements.ID_ADD_BUTTON)
        # Checking the task results
        BuiltIn().sleep(1)
        if ui_lib.wait_for_element(SampleElements.ID_GREEN_LIGHT):
            logger._log_to_console_and_log_file("User '" + user.name + "' was correctly added")
        else:
            logger._log_to_console_and_log_file("User '" + user.name + "' was NOT added")

# Fill the user fields with invalid data


def fillinfo_negative():
    selenium2lib = ui_lib.get_s2l()

    ui_lib.wait_for_element(SampleElements.ID_LOGIN_NAME)
    selenium2lib.input_text(SampleElements.ID_LOGIN_NAME, "111")
    selenium2lib.input_text(SampleElements.ID_INITIAL_PASSWORD, "123")

    # Checking the warning messages
    if ui_lib.wait_for_element_visible(SampleElements.ID_INVALID_LOGIN_NAME, PerfConstants.DEFAULT_SYNC_TIME):
        logger._log_to_console_and_log_file("Invalid Login Name message correctly was displayed")
    else:
        logger._log_to_console_and_log_file("Warning message was not displayed")
        ui_lib.fail_test("Test FAILED")

    if ui_lib.wait_for_element_visible(SampleElements.ID_INVALID_PASSWORD, PerfConstants.DEFAULT_SYNC_TIME):
        logger._log_to_console_and_log_file("Invalid Password message correctly was displayed")
    else:
        logger._log_to_console_and_log_file("Warning message was not displayed")
        ui_lib.fail_test("Test FAILED")

    BuiltIn().sleep(1)

# (C) Copyright 2013-2015 Hewlett-Packard Development Company, L.P.
"""
    Base Page
"""


from i3SLibrary.ui.general.base_elements import i3SBasePage
from i3SLibrary.ui.general.login_elements import i3SLoginPage
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from i3SLibrary.ui.ui_constants import UiConstants
from RoboGalaxyLibrary.utilitylib import logging as logger
from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib

class MyNonFatalError(RuntimeError):
    ROBOT_EXIT_ON_FAILURE = False


def logout():
    # get a reference to the selenium lib
    # s2l = ui_lib.get_s2l()

    # check the existing login status
    if logged_in():
        logger._log_to_console_and_log_file("Logging out of i3S..")
        ui_lib.wait_for_element(i3SBasePage.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_visible(i3SBasePage.ID_SESSION_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_and_click(i3SBasePage.ID_SESSION_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_visible(i3SBasePage.ID_SESSION_LOGOUT)
        ui_lib.wait_for_element_and_click(i3SBasePage.ID_SESSION_LOGOUT, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_visible(i3SLoginPage.ID_INPUT_LOGIN_USER, UiConstants.i3S_LOGOUT_TIME)
        set_logged_user(None)
        return True
    return False


def navigate_base(currentpage, menulink, itemcount):
    s2l = ui_lib.get_s2l()
    logger._log_to_console_and_log_file('Navigating to "{0}"'.format(currentpage))
    if not s2l._is_element_present(currentpage):
        ui_lib.wait_for_element(i3SBasePage.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_and_click(i3SBasePage.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element(i3SBasePage.ID_MENU_LINK_DASHBOARD, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_and_click(menulink, PerfConstants.DEFAULT_SYNC_TIME)
        s2l.wait_until_page_contains_element(currentpage, PerfConstants.DEFAULT_SYNC_TIME)
    # wait for the page to get loaded
    s2l.wait_until_page_contains_element(itemcount, PerfConstants.DEFAULT_SYNC_TIME)
    # added wait to remove int Base 10 conversion error while running with Selenium speed 0.0
    BuiltIn().sleep(1)
    for x in range(1, 5):
        try:
            el = int(s2l.get_text(itemcount))
        except ValueError:
            BuiltIn().sleep(1)
            pass
    while el >= 0:
        BuiltIn().sleep(0.1)
        tmp_el = int(s2l.get_text(itemcount))
        if el == tmp_el:
            break
    # wait for page controls to complete expanding
    # ui_lib.wait_for_element_expand(i3SBasePage.ID_MASTER_PANE)


def get_page_name():
    # get a reference to the selenium lib
    s2l = ui_lib.get_s2l()

    # get the current page
    s2l.wait_until_page_contains_element(i3SBasePage.ID_PAGE_LABEL)
    page_name = s2l.get_text(i3SBasePage.ID_PAGE_LABEL)
    return page_name

def set_logged_user(user):
    """ set_logged_user
        Description : Function used for setting the logged user, set user name once you are logged in to the applicance
    """
    test_data.set_variable(test_data.GlobalProperty.UiLoggedIn, user)


def get_logged_user():
    """ get_logged_user
        Description : Function used for retrieving the logged in user. If no user is logged in, it will return None.
    """
    return test_data.get_variable(test_data.GlobalProperty.UiLoggedIn)


def logged_in():
    """ logged_in
        Description : Function used for retrieving the login status (True of False). Returns true if test_data.GlobalProperty.UiLoggedIn is not None
    """
    return get_logged_user() is not None

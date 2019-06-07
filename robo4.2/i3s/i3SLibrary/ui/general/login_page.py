# (C) Copyright 2013-2015 Hewlett-Packard Development Company, L.P.
"""
    Login Page

"""


from i3SLibrary.ui.general.dashboard_elements import i3SDashboardPage
from i3SLibrary.ui.general.login_elements import i3SLoginPage
from i3SLibrary.ui.general import base_page
from i3SLibrary.ui.ui_constants import UiConstants
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from robot.libraries.BuiltIn import BuiltIn


def login(user_name):
    s2l = ui_lib.get_s2l()
    logger._log_to_console('Login status = {0}'.format(str(base_page.logged_in())))

    if base_page.logged_in():
        base_page.logout()

    user = test_data.get_user_by_name(user_name)

    # check the existing login status
    logger._log_to_console_and_log_file("Logging into i3S as {0}/{1}".format(user.name, user.password))
    if s2l._is_element_present(i3SLoginPage.ID_BTN_EULA_AGREE):
        s2l.click_button(i3SLoginPage.ID_BTN_EULA_AGREE)

    s2l.wait_until_page_contains_element(i3SLoginPage.ID_BTN_LOGIN_BUTTON)
    s2l.input_text(i3SLoginPage.ID_INPUT_LOGIN_USER, user.name)
    s2l.input_text(i3SLoginPage.ID_INPUT_LOGIN_PASSWORD, user.password)

    # code to login as  active directory user
    if(user.has_property("domainName")):
        s2l.click_element(i3SLoginPage.ID_ELEMENT_AUTHN_PROVIDER)
        dirListObj = i3SLoginPage.ID_ELEMENT_DIR % user.domainName.strip()

        s2l.click_element(dirListObj)
        activedir = s2l.get_text(i3SLoginPage.ID_COMBO_AUTHN_PROVIDER)
        if not activedir == user.domainName.strip():
            logger._warn("Not able to login to the appliance with active directory users ..")
            ui_lib.fail_test("not able to login as active directory users... verify AD users and groups is added to the appliance")

    s2l.click_button(i3SLoginPage.ID_BTN_LOGIN_BUTTON)
    # These elements may not exist if the login page is transitioning to the dashboard
    # page.  In order to avoid failing conditions, we will catch any exceptions
    try:
        s2l.element_should_not_be_visible(i3SLoginPage.ID_ALL_ERROR_FIELDS)
        s2l.element_text_should_be(i3SLoginPage.ID_LABEL_LOGIN_STATUS, "")
    except:
        pass

    s2l.wait_until_page_contains_element(i3SDashboardPage.ID_PAGE_LABEL,
                                         UiConstants.i3S_LOGIN_TIME,
                                         "Failed to load the Login Page")
    base_page.set_logged_user(user_name)
    logger._log_to_console_and_log_file("Logged into i3S as {0}".format(base_page.get_logged_user()))
    return True

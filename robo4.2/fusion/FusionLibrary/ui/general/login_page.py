# (C) Copyright 2013-2015 Hewlett-Packard Development Company, L.P.
"""
    Login Page

"""


from FusionLibrary.ui.business_logic.general.dashboard_elements import FusionDashboardPage
from FusionLibrary.ui.general.login_elements import FusionLoginPage
from FusionLibrary.ui.general import base_page
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.base import FusionUIBase


def login(user_name):
    s2l = ui_lib.get_s2l()
    logger._log_to_console('Login status = {0}'.format(str(FusionUIBase.logged_in())))

    if FusionUIBase.logged_in():
        base_page.logout()

    user = test_data.get_user_by_name(user_name)

    # check the existing login status
    logger._log_to_console_and_log_file("Logging into Fusion as {0}/{1}".format(user.name, user.password))
    if s2l._is_element_present(FusionLoginPage.ID_BTN_EULA_AGREE):
        s2l.click_button(FusionLoginPage.ID_BTN_EULA_AGREE)

    s2l.wait_until_page_contains_element(FusionLoginPage.ID_BTN_LOGIN_BUTTON)
    s2l.input_text(FusionLoginPage.ID_INPUT_LOGIN_USER, user.name)
    s2l.input_text(FusionLoginPage.ID_INPUT_LOGIN_PASSWORD, user.password)

    # code to login as  active directory user
    if(user.has_property("domainName")):
        s2l.click_element(FusionLoginPage.ID_ELEMENT_AUTHN_PROVIDER)
        dirListObj = FusionLoginPage.ID_ELEMENT_DIR % user.domainName.strip()

        s2l.click_element(dirListObj)
        activedir = s2l.get_text(FusionLoginPage.ID_COMBO_AUTHN_PROVIDER)
        if not activedir == user.domainName.strip():
            logger._warn("Not able to login to the appliance with active directory users ..")
            ui_lib.fail_test("not able to login as active directory users... verify AD users and groups is added to the appliance")

    s2l.click_button(FusionLoginPage.ID_BTN_LOGIN_BUTTON)

    # Close Oneview Tutorial Dialog Box if Exits
    if ui_lib.wait_for_element_visible(FusionLoginPage.ID_ONEVIEW_TUTORIAL_DIALOG, 15):
        s2l.click_element(FusionLoginPage.ID_ONEVIEW_TUTORIAL_CLOSE)
        logger.info("OneView Tutorial Dialog existed and is now closed")

    # These elements may not exist if the login page is transitioning to the dashboard
    # page.  In order to avoid failing conditions, we will catch any exceptions
    try:
        s2l.element_should_not_be_visible(FusionLoginPage.ID_ALL_ERROR_FIELDS)
        s2l.element_text_should_be(FusionLoginPage.ID_LABEL_LOGIN_STATUS, "")
    except:
        pass

    if s2l._is_element_present(FusionLoginPage.ID_BTN_EULA_AGREE):
        s2l.click_button(FusionLoginPage.ID_BTN_EULA_AGREE)
    if s2l._is_element_present(FusionLoginPage.ID_BTN_EULA_OK):
        s2l.click_button(FusionLoginPage.ID_BTN_EULA_OK)

    if s2l._is_element_present(FusionLoginPage.ID_INPUT_APPLIANCE_HOSTNAME):
        s2l.click_element(FusionLoginPage.ID_RADIO_IPV4_DHCP)
        s2l.click_button(FusionLoginPage.ID_APPLIANCE_OK)
        # wait up to 2 mins for applying settings screen to disappear
        ui_lib.wait_for_element_notvisible(FusionLoginPage.ID_APPLIANCE_APPLYING_SETTINGS,
                                           150, "Applying Setting screen did not disappear")

    s2l.wait_until_page_contains_element(FusionDashboardPage.ID_PAGE_LABEL,
                                         PerfConstants.FUSION_LOGIN_TIME,
                                         "Failed to load the Login Page")
    FusionUIBase.set_login_status(True)

    # hide the guided setup panel
    base_page.close_guided_setup_panel()
    return True

# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    First Time Wizard page
"""


from FusionLibrary.ui.business_logic.general.dashboard_elements import FusionDashboardPage
from FusionLibrary.ui.general.login_elements import FusionLoginPage
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.business_logic.base import FusionUIBase


def fusion_configure_first_time_wizard():
    """ fusion_configure_first_time_wizard    """
    logger._log_to_console_and_log_file("Configuring fusion first time wizard..")
    env_data = test_data.get().envconfigs
    env_data = env_data[0]
    ftw_data = test_data.get().ftwizard
    ftw_data = ftw_data[0]
    ftw_data_ipv4 = ftw_data.ipv4[0]
    ftw_data_ipv6 = ftw_data.ipv6[0]

    selenium2lib = ui_lib.get_s2l()
    default_wait = PerfConstants.DEFAULT_SYNC_TIME

    """  Accepting EULA page  """
    if ui_lib.wait_for_element_visible(FusionLoginPage.ID_BTN_EULA_AGREE, default_wait):
        selenium2lib.click_button(FusionLoginPage.ID_BTN_EULA_AGREE)
    if ui_lib.wait_for_element_visible(FusionLoginPage.ID_BTN_OK_CONVERGED_INFRA_SUPPORT, default_wait):
        if ftw_data.hp_support_access.upper() == "DISABLE":
            selenium2lib.click_element(FusionLoginPage.ID_TOGGLE_HP_SUPPORT_ACCESS_ENABLE)
        selenium2lib.click_button(FusionLoginPage.ID_BTN_OK_CONVERGED_INFRA_SUPPORT)

    """    Login into appliance with default IP address and default credentials    """
    selenium2lib.wait_until_page_contains_element(FusionLoginPage.ID_INPUT_LOGIN_USER, default_wait, "Failed to load the Login Page")
    ui_lib._set_browser_status(True)
    _first_time_login(env_data.appliance_default_password)

    """    Changing appliance default password    """
    if (env_data.appliance_password is not None) or (len(env_data.appliance_password) >= 8) or (env_data.appliance_password == env_data.confirm_password):
        if ui_lib.wait_for_element_visible(FusionLoginPage.ID_INPUT_NEW_PASSWORD, default_wait):
            selenium2lib.input_text(FusionLoginPage.ID_INPUT_NEW_PASSWORD, env_data.appliance_password)
            selenium2lib.input_text(FusionLoginPage.ID_INPUT_CONFIRM_PASSWORD, env_data.appliance_password)
            selenium2lib.click_button(FusionLoginPage.ID_BTN_OK_PASSWORD_SCREEN)
    else:
        logger._warn("Mandatory fields for changing default password can't be empty and should be at least 8 characters")

    """    Updating Network parameters    """
    if ui_lib.wait_for_element_visible(FusionLoginPage.ID_INPUT_APPLIANCE_HOSTNAME, default_wait):
        logger._log_to_console_and_log_file("Configuring Appliance Networking")
        if ftw_data_ipv4.assignments.upper() == "DHCP":
            selenium2lib.click_element(FusionLoginPage.ID_RADIO_IPV4_DHCP)
        elif (ftw_data_ipv4.ipaddress is not None) and (ftw_data_ipv4.subnetmask is not None):
            selenium2lib.click_element(FusionLoginPage.ID_RADIO_IPV4_MANUAL)
            selenium2lib.input_text(FusionLoginPage.ID_INPUT_IPV4_IPADDRESS, ftw_data_ipv4.ipaddress)
            selenium2lib.input_text(FusionLoginPage.ID_INPUT_IPV4_MASK, ftw_data_ipv4.subnetmask)
            ui_lib.input_text_if_property_exist(FusionLoginPage.ID_INPUT_IPV4_GATEWAY, "gateway", ftw_data_ipv4)
        else:
            logger._warn("Mandatory fields for configuring appliance can't be empty")

        ui_lib.input_text_if_property_exist(FusionLoginPage.ID_INPUT_PREFFERED_DNS, "preferred_dns", ftw_data)
        ui_lib.input_text_if_property_exist(FusionLoginPage.ID_INPUT_ALTERNATE_DNS, "alternate_dns", ftw_data)
        selenium2lib.input_text(FusionLoginPage.ID_INPUT_APPLIANCE_HOSTNAME, ftw_data.appliance_hostname)

        """    IPv6    """
        selenium2lib.click_element(FusionLoginPage.ID_COMBO_MENU_VIEW)
        selenium2lib.click_element(FusionLoginPage.ID_LINK_DNS)
        ui_lib.wait_for_element_visible(FusionLoginPage.ID_RADIO_IPV6_MANUAL, 5)
        if ftw_data_ipv6.assignments.upper() == "MANUAL":
            selenium2lib.click_element(FusionLoginPage.ID_RADIO_IPV6_MANUAL)
            selenium2lib.input_text(FusionLoginPage.ID_INPUT_IPV6_IPADDRESS, ftw_data_ipv6.ipaddress)
            selenium2lib.input_text(FusionLoginPage.ID_INPUT_IPV6_MASK, ftw_data_ipv6.subnetmask)
            ui_lib.input_text_if_property_exist(FusionLoginPage.ID_INPUT_IPV6_GATEWAY, "gateway", ftw_data_ipv6)
        elif ftw_data_ipv6.assignments.upper() == "DHCP":
            selenium2lib.click_element(FusionLoginPage.ID_RADIO_IPV6_DHCP)
        else:
            selenium2lib.click_element(FusionLoginPage.ID_RADIO_IPV6_UNASSIGN)
        selenium2lib.click_button(FusionLoginPage.ID_BTN_OK_NETWORK_ASSIGNMENT)

        """    Verifying the configured appliance IP address"""
        apply_network_settings = PerfConstants.CONFIGURE_NETWORK_SETTINGS_FTW
        if ui_lib.wait_for_element_visible(FusionLoginPage.ID_ELEMENT_ERROR_MESSAGE, default_wait):
            ui_lib.fail_test("Error message displayed while configuring the network")
        else:
            if ui_lib.wait_for_element_visible(FusionLoginPage.ID_INPUT_LOGIN_USER, apply_network_settings):
                selenium2lib.input_text(FusionLoginPage.ID_INPUT_LOGIN_USER, env_data.appliance_username)
                selenium2lib.input_text(FusionLoginPage.ID_INPUT_LOGIN_PASSWORD, env_data.appliance_password)
                selenium2lib.click_element(FusionLoginPage.ID_BTN_LOGIN_BUTTON)
                if ui_lib.wait_for_element_visible(FusionDashboardPage.ID_ELEMENT_ENCLOSURE, default_wait):
                    ui_lib.fail_test("Failed to configure the appliance")
                else:
                    logger._log_to_console_and_log_file("Appliance Network Configuration is done successfully")


def _first_time_login(password):
    logger._log_to_console_and_log_file("Login to Fusion..")
    env_data = test_data.get().envconfigs
    env_data = env_data[0]
    selenium2lib = ui_lib.get_s2l()
    if not ui_lib._get_browser_status():
        ui_lib.open_browser()

    if selenium2lib._is_element_present(FusionLoginPage.ID_BTN_EULA_AGREE):
        selenium2lib.click_button(FusionLoginPage.ID_BTN_EULA_AGREE)

    selenium2lib.wait_until_page_contains_element(FusionLoginPage.ID_BTN_LOGIN_BUTTON)
    selenium2lib.input_text(FusionLoginPage.ID_INPUT_LOGIN_USER, env_data.appliance_username)
    selenium2lib.input_text(FusionLoginPage.ID_INPUT_LOGIN_PASSWORD, password)
    selenium2lib.click_button(FusionLoginPage.ID_BTN_LOGIN_BUTTON)
    if not ui_lib.wait_for_element_visible(FusionLoginPage.ID_INPUT_NEW_PASSWORD, 4):
        selenium2lib.wait_until_page_contains("Dashboard", 10, "Failed to load the Login Page")
    FusionUIBase.set_login_status(True)

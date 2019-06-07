# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
#    Fusion SAN Managers UI page. """
#    added HP switch 5900 info """


from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.sanmanager.sanmanagers_elements import FusionSANManagersPage
from FusionLibrary.ui.san.san_elements import FusionSANPage
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from FusionLibrary.keywords import fusion_ui
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.storage.sanmanagers import CommonOperationSANMangers
from FusionLibrary.ui.business_logic.storage.sanmanagers import AddSANMangers, EditSANMangers, RemoveSANMangers, RefreshSANMangers
from FusionLibrary.ui.business_logic.base import FusionUIBase
from FusionLibrary.ui.business_logic.base import SectionType
import time

# from datetime import datetime

ROBOT_LIBRARY_VERSION = '0.0'
CONF_DICT = {
    'browser_type': None,
    'remote_run': False,
    'timeout': 5,
    'speed': 0.01
}


def navigate():
    base_page.navigate_base(FusionSANManagersPage.ID_PAGE_LABEL,
                            FusionUIBaseElements.ID_MENU_LINK_SAN_MANAGERS,
                            "css=span.hp-page-item-count")
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionSANManagersPage.ID_PAGE_LABEL):
        logger._warn("Failed to navigate to san managers page")
        return False
    else:
        return True


def navigate_to_san_managers_page_negative(renavigate=False):
    if not renavigate and ui_lib.wait_for_element_visible(FusionSANManagersPage.ID_PAGE_LABEL):
        logger._info('Label [SAN Managers] is shown')
        return True

    def page_navigated(self):
        xpath_main_menu = FusionUIBaseElements.ID_MAIN_MENU_CONTROL
        xpath_page_label = FusionSANManagersPage.ID_PAGE_LINK
#       xpath_details_title = FusionSANManagersPage.DETAILS_TITLE
        try:
            style = ui_lib.get_webelement_attribute(locator=xpath_main_menu, attribute='style')
            if 'width' not in style:
                logger._info('Clicking Main Menu [%s]' % xpath_main_menu)
                ui_lib.wait_for_element_and_click(xpath_main_menu)

            logger._info('Waiting for link [SAN Managers] shown')
            ui_lib.wait_for_element_visible(xpath_page_label, 5)
            logger._info('Clicking [SAN Managers] [%s]' % xpath_page_label)
            ui_lib.wait_for_element_and_click(xpath_page_label)
            logger._info('Waiting for page label [SAN Managers] shown')

        except:
            return False

        return True
    selenium2lib = ui_lib.get_s2l()
    timeout = CONF_DICT['timeout'] or 10
    wait = WebDriverWait(selenium2lib._current_browser(),
                         timeout,
                         CONF_DICT['speed'],
                         StaleElementReferenceException)
    logger._info('Waiting for navigation')
    return wait.until(page_navigated)


def sanmgr_change_tab(tab_name):
    xpath_tab = FusionSANManagersPage.ID_SAN_MANAGER_TABS

    if (tab_name == "General"):
        xpath_tab_name = FusionSANManagersPage.ID_VIEW_GENERAL
    elif (tab_name == "Activity"):
        xpath_tab_name = FusionSANManagersPage.ID_VIEW_ACTIVITY
    elif (tab_name == "Map"):
        xpath_tab_name = FusionSANManagersPage.ID_VIEW_MAP

    try:
        ui_lib.wait_for_element_visible(xpath_tab, 10)

    except:
        pass

    ui_lib.wait_for_element_and_click(xpath_tab)
    ui_lib.wait_for_element_and_click(xpath_tab_name)


def open_add_san_manager_dialog_page():
    xpath_dialog_title = FusionSANManagersPage.ID_ADD_SAN_MANAGER_TITLE
    xpath_add_san_manager_link = FusionSANManagersPage.ID_ADD_SAN_MANAGER

    def is_dialog_open(self):
        if ui_lib.wait_for_element_visible(xpath_dialog_title):
            return True
        try:
            logger._info('Clicking %s' % xpath_add_san_manager_link)
            ui_lib.wait_for_element_and_click(xpath_add_san_manager_link, 5)
            logger._info('Waiting for [Add San Manager] dialog open')
#           ui_lib.wait_for_element_visible(xpath_dialog_title, 10)
#            if not ui_lib.wait_for_element_visible(xpath_dialog_title):
#                return False
        except:
            return False
        return True
    selenium2lib = ui_lib.get_s2l()
    timeout = CONF_DICT['timeout'] or 10
    wait = WebDriverWait(selenium2lib._current_browser(),
                         timeout,
                         CONF_DICT['speed'],
                         StaleElementReferenceException)
    return wait.until(is_dialog_open)


def close_add_san_manager_dialog():
    xpath_dialog_title = FusionSANManagersPage.ID_ADD_SAN_MANAGER_TITLE3
    xpath_cancel = FusionSANManagersPage.ID_BTN_SAN_MANAGER_CANCEL

    def is_dialog_open(self):
        if not ui_lib.wait_for_element_visible(xpath_dialog_title):
            return True
        try:
            logger._info('Clicking %s' % xpath_cancel)
            ui_lib.wait_for_element_and_click(xpath_cancel, 5)
            logger._info('Waiting for [Add SAN Manager] dialog close')
#            ui_base.wait_elt_disappear(xpath_dialog_title, 10)
#            if ui_lib.wait_for_element_visible(xpath_dialog_title):
#                return False
        except:
            return False
        return True
    selenium2lib = ui_lib.get_s2l()
    timeout = CONF_DICT['timeout'] or 10
    wait = WebDriverWait(selenium2lib._current_browser(),
                         timeout,
                         CONF_DICT['speed'],
                         StaleElementReferenceException)
    return wait.until(is_dialog_open)


def add_user_input_host_name(host):
    xpath_host = FusionSANManagersPage.ID_SAN_BNA_HOST
    try:
        ui_lib.wait_for_element_visible(xpath_host, 10)
    except:
        pass

    ui_lib.wait_for_element_and_input_text(xpath_host, host)


def add_user_input_username(username):
    xpath_username = FusionSANManagersPage.ID_SAN_BNA_USER
    try:
        ui_lib.wait_for_element_visible(xpath_username, 10)
    except:
        pass

    ui_lib.wait_for_element_and_input_text(xpath_username, username)


def add_user_input_pswd(password):
    xpath_password = FusionSANManagersPage.ID_SAN_BNA_PSWD
    try:
        ui_lib.wait_for_element_visible(xpath_password, 10)
    except:
        pass

    ui_lib.wait_for_element_and_input_text(xpath_password, password)


def add_san_manager_click_add():
    xpath_add = FusionSANManagersPage.ID_BTN_SAN_MANAGER_ADD
    try:
        ui_lib.wait_for_element_visible(xpath_add, 10)
    except:
        pass

    ui_lib.wait_for_element_and_click(xpath_add)


def add_san_manager_click_cancel():
    xpath_cancel = FusionSANManagersPage.ID_BTN_SAN_MANAGER_CANCEL
    try:
        ui_lib.wait_for_element_visible(xpath_cancel, 15)
    except:
        pass

    ui_lib.wait_for_element_and_click(xpath_cancel)


def add_san_manager_click_add_plus():
    xpath_add_plus = FusionSANManagersPage.ID_BTN_SAN_MANAGER_ADD_PLUS
    try:
        ui_lib.wait_for_element_visible(xpath_add_plus, 10)
    except:
        pass

    ui_lib.wait_for_element_and_click(xpath_add_plus)


def add_san_manager_click_type(stype):
    xpath_type = FusionSANManagersPage.ID_SELECT_BOX_LABEL + stype
    try:
        ui_lib.wait_for_element_visible(xpath_type, 10)
    except:
        pass

    ui_lib.wait_for_element_and_input_text(xpath_type, stype)


def validate_hostname_should_contain_character_only():
    xpath_input_error = FusionSANManagersPage.ADD_SAN_ERR_LINE_DETAILS
    try:
        ui_lib.wait_for_element_visible(xpath_input_error, 10)
    except:
        pass
    msg = "Enter valid hostname or IP address."
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_input_error), msg)


def validate_unable_add_san_manager(err_type):
    xpath_unable_to_add_error = FusionSANManagersPage.ADD_SAN_ERR_MSG
    logger._log_to_console_and_log_file("Validate %s error" % err_type)
    msg1 = "Unable to add SAN manager."
    msg3 = "Resolution: "

    if (err_type == 'credentials'):
        xpath_error_details = FusionSANManagersPage.ADD_SAN_ERR_CREDENTIALS
        xpath_error_resolution = (FusionSANManagersPage.ADD_SAN_ERR_CREDENTIALS +
                                  FusionSANManagersPage.ADD_SAN_ERR_RESOLUTION)
        msg = "The specified user name and/or password is not valid for the SAN manager."
    elif (err_type == 'fielderr'):
        xpath_error_details = FusionSANManagersPage.ADD_SAN_ERR_HOST_REQUIRED
        xpath_error_resolution = (FusionSANManagersPage.ADD_SAN_ERR_HOST_REQUIRED + FusionSANManagersPage.ADD_SAN_ERR_RESOLUTION)
        msg = "One or more fields have an invalid value."
    else:
        logger._log_to_console_and_log_file("Validate field invalid error")

    try:
        ui_lib.wait_for_element_visible(xpath_unable_to_add_error, 10, fail_if_false=True)
        ui_lib.wait_for_element_visible(xpath_error_details, 10, fail_if_false=True)
        ui_lib.wait_for_element_visible(xpath_error_resolution, 10, fail_if_false=True)
    except:
        pass

    logger._log_to_console_and_log_file("Validate '%s' message" % msg)
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_unable_to_add_error), msg1)
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_error_details), msg)
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_error_resolution), msg3)


def add_user_input_port(port):
    xpath_port = FusionSANManagersPage.ID_SAN_MANAGER_BNA_PORT
    try:
        ui_lib.wait_for_element_visible(xpath_port, 10)
    except:
        pass

    ui_lib.wait_for_element_and_input_text(xpath_port, port)


def validate_port_should_contain_numeric_only():
    xpath_input_error = FusionSANManagersPage.ADD_SAN_ERR_PORT_DETAILS
    try:
        ui_lib.wait_for_element_visible(xpath_input_error, 10)
    except:
        pass
    msg = "Enter a valid port number (1 - 65535)"
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_input_error), msg)


def validate_field_required():
    xpath_input_error = FusionSANManagersPage.ADD_SAN_REQUIRED_ERR_MSG
    try:
        ui_lib.wait_for_element_visible(xpath_input_error, 5)
    except:
        pass
    msg = "This field is required."
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_input_error), msg)


def validate_tab_required():
    logger._log_to_console_and_log_file("Function call to validate tabs on SAN managers")
    s2l = ui_lib.get_s2l()

    """ Navigate to SAN Manager Page """
    if not s2l._is_element_present(FusionSANManagersPage.ID_PAGE_LABEL):
        if not navigate():
            return False

    san_mangr_list = [ui_lib.get_webelement_attribute("text", el) for el in s2l._element_find(FusionSANManagersPage.ID_SAN_MANAGER_LIST_NAMES, False, False)]
    for san_mangr in san_mangr_list:
        logger._log_to_console_and_log_file("validating san manager %s" % san_mangr)
        ui_lib.wait_for_element_and_click(FusionSANManagersPage.ID_ELEMENT_SAN_MANAGER % san_mangr)

        if ((san_mangr.__contains__("OneView") or san_mangr.__contains__("Direct")) is False):
            '''validate_general_section_titles()'''
            logger._log_to_console_and_log_file("san manager= %s" % san_mangr)
            validate_general_section_titles()
            sanmanager_actions_validate()

        else:
            logger._log_to_console_and_log_file("Flat san found as san manager")
            sanmanager_actions_flatsan_validate()

    return True


def sanmanager_action_menu_set(action_option):
    xpath_action = FusionSANManagersPage.ID_MENU_ACTION_MAIN_BTN

    try:
        ui_lib.wait_for_element_visible(xpath_action, 5)
    except:
        pass

    ui_lib.wait_for_element_and_click(xpath_action)
    logger._log_to_console_and_log_file("Action= %s passed" % action_option)
    if (action_option == "Add"):
        ui_lib.wait_for_element_and_click(FusionSANManagersPage.ID_ACTIONS_ADD_SAN_MANAGER)
    elif (action_option == "Refresh"):
        ui_lib.wait_for_element_and_click(FusionSANManagersPage.ID_ACTIONS_REFRESH_SAN_MANAGER)
    elif (action_option == "Edit"):
        ui_lib.wait_for_element_and_click(FusionSANManagersPage.ID_ACTIONS_EDIT_SAN_MANAGER)
    else:
        logger._log_to_console_and_log_file("Invalid action= %s passed for flatsan" % action_option)
        ui_lib.fail_test("unable to find the" + action_option + "action")

    return True


def sanmanager_actions_validate():
    xpath_tab = FusionSANManagersPage.ID_MENU_ACTION_MAIN_BTN
    xpath_tab_option1 = FusionSANManagersPage.ID_ACTIONS_ADD_SAN_MANAGER
    xpath_tab_option2 = FusionSANManagersPage.ID_ACTIONS_EDIT_SAN_MANAGER
    xpath_tab_option3 = FusionSANManagersPage.ID_ACTIONS_REFRESH_SAN_MANAGER
    xpath_tab_option4 = FusionSANManagersPage.ID_ACTIONS_REMOVE_SAN_MANAGER

    try:
        ui_lib.wait_for_element_visible(xpath_tab, 10)
    except:
        pass

    ui_lib.wait_for_element_and_click(xpath_tab)
    tab_name = "Add"
    if ((ui_lib.get_text(xpath_tab_option1, 1)) == tab_name):
        logger._log_to_console_and_log_file(tab_name + "Tab found")
    else:
        ui_lib.fail_test("unable to find the" + tab_name + "tab")

    tab_name = "Refresh"
    if ((ui_lib.get_text(xpath_tab_option3, 1)) == tab_name):
        logger._log_to_console_and_log_file(tab_name + "Tab found")
    else:
        ui_lib.fail_test("unable to find the" + tab_name + "tab")

    tab_name = "Edit"
    if ((ui_lib.get_text(xpath_tab_option2, 1)) == tab_name):
        logger._log_to_console_and_log_file(tab_name + "Tab found")
    else:
        ui_lib.fail_test("unable to find the" + tab_name + "tab")

    tab_name = "Remove"
    if ((ui_lib.get_text(xpath_tab_option4, 1)) == tab_name):
        logger._log_to_console_and_log_file(tab_name + "Tab found")
    else:
        ui_lib.fail_test("unable to find the" + tab_name + "tab")
    return True


def sanmanager_actions_flatsan_validate():
    xpath_tab = FusionSANManagersPage.ID_MENU_ACTION_MAIN_BTN
    xpath_tab_option1 = FusionSANManagersPage.ID_ACTIONS_ADD_SAN_MANAGER
    xpath_tab_option2 = FusionSANManagersPage.ID_ACTIONS_EDIT_SAN_MANAGER
    xpath_tab_option3 = FusionSANManagersPage.ID_ACTIONS_REFRESH_SAN_MANAGER
    xpath_tab_option4 = FusionSANManagersPage.ID_ACTIONS_REMOVE_SAN_MANAGER

    try:
        ui_lib.wait_for_element_visible(xpath_tab, 10)
    except:
        pass

    ui_lib.wait_for_element_and_click(xpath_tab)
    tab_name = "Add"
    if ((ui_lib.get_text(xpath_tab_option1, 1)) == tab_name):
        logger._log_to_console_and_log_file(tab_name + "Tab found")
    else:
        ui_lib.fail_test("unable to find the" + tab_name + "tab")

    tab_name = "Refresh"
    if ((ui_lib.get_text(xpath_tab_option3, 1)) == tab_name):
        logger._log_to_console_and_log_file(tab_name + "Tab found")
    else:
        ui_lib.fail_test("unable to find the" + tab_name + "tab")

    tab_name = "Edit"
    if ((ui_lib.get_text(xpath_tab_option2, 1)) == tab_name):
        ui_lib.fail_test("Error- " + tab_name + "tab was found in action menu for flatsan")
        logger._log_to_console_and_log_file(tab_name + "Tab found- error")
    else:
        logger._log_to_console_and_log_file(tab_name + "Tab not found - pass")

    tab_name = "Remove"
    if ((ui_lib.get_text(xpath_tab_option4, 1)) == tab_name):
        ui_lib.fail_test("Error- " + tab_name + "tab was found in action menu for flatsan")
        logger._log_to_console_and_log_file(tab_name + "Tab found- error")
    else:
        logger._log_to_console_and_log_file(tab_name + "Tab not found - pass")
    return True


def validate_general_section_titles():
    xpath_section = FusionSANManagersPage.ID_MENU_VIEW_MAIN_BTN
    xpath_title1 = FusionSANManagersPage.ID_VIEW_GENERAL_SAN_MANAGER
    xpath_title3 = FusionSANManagersPage.ID_VIEW_ACTIVITY_SAN_MANAGER
    xpath_title4 = FusionSANManagersPage.ID_VIEW_MAP_SAN_MANAGER

    try:
        ui_lib.wait_for_element_visible(xpath_section, 5)
    except:
        pass
    ui_lib.wait_for_element_and_click(xpath_section)

    title = "General"
    if ((ui_lib.get_text(xpath_title1, 1)) == title):
        logger._log_to_console_and_log_file(title + "Section found")
    else:
        ui_lib.fail_test("unable to find the" + title + "section")

    title = "Activity"
    if ((ui_lib.get_text(xpath_title3, 1)) == title):
        logger._log_to_console_and_log_file(title + "Section found")
    else:
        ui_lib.fail_test("unable to find the" + title + "section")

    title = "Map"
    if ((ui_lib.get_text(xpath_title4, 1)) == title):
        logger._log_to_console_and_log_file(title + "Section found")
    else:
        ui_lib.fail_test("unable to find the" + title + "section")
    return True


def verify_sanmanager_managedsans_count_link():
    logger._log_to_console_and_log_file("Function call to validate managedsanscount link from Sanmanager")
    s2l = ui_lib.get_s2l()

    """ Navigate to SAN Manager Page """
    if not s2l._is_element_present(FusionSANManagersPage.ID_PAGE_LABEL):
        if not navigate():
            return False

    san_mangr_list = [ui_lib.get_webelement_attribute("text", el) for el in s2l._element_find(FusionSANManagersPage.ID_SAN_MANAGER_LIST_NAMES, False, False)]
    for san_mangr in san_mangr_list:
        """ skip hp direct attach san manager - can not be deleted """
        if ((san_mangr.__contains__("OneView") or san_mangr.__contains__("Direct")) is False):
            logger._log_to_console_and_log_file("validating san manager %s" % san_mangr)
            ui_lib.wait_for_element_and_click(FusionSANManagersPage.ID_ELEMENT_SAN_MANAGER % san_mangr)
            xpath_section = FusionSANManagersPage.ID_LINK_SANSCOUNT
            try:
                ui_lib.wait_for_element_visible(xpath_section, 5)
            except:
                pass
            ui_lib.wait_for_element_and_click(xpath_section)
            san_page_title = FusionSANPage.ID_SAN_HEADING_TOP
            try:
                ui_lib.wait_for_element_visible(san_page_title, 5)
            except:
                pass
            title = "SANs"
            if ((ui_lib.get_text(san_page_title, 1)) == title):
                logger._log_to_console_and_log_file("Navigated to" + title + "Page")
            else:
                ui_lib.fail_test("unable to navigate to" + title + "page")
            if not s2l._is_element_present(FusionSANManagersPage.ID_PAGE_LABEL):
                if not navigate():
                    return False

        else:
            """ add to count so that len of list and count are equal """
            logger._log_to_console_and_log_file("Flat san could not be validated")

    return True


def verify_sanmanager_managedsan_link():
    logger._log_to_console_and_log_file("Function call to validate managedsan link from Sanmanager")
    s2l = ui_lib.get_s2l()

    """ Navigate to SAN Manager Page """
    if not s2l._is_element_present(FusionSANManagersPage.ID_PAGE_LABEL):
        if not navigate():
            return False

    san_mangr_list = [ui_lib.get_webelement_attribute("text", el) for el in s2l._element_find(FusionSANManagersPage.ID_SAN_MANAGER_LIST_NAMES, False, False)]
    for san_mangr in san_mangr_list:
        """ skip hp direct attach san manager - can not be processed """
        if ((san_mangr.__contains__("OneView") or san_mangr.__contains__("Direct")) is False):
            logger._log_to_console_and_log_file("validating san manager %s" % san_mangr)
            ui_lib.wait_for_element_and_click(FusionSANManagersPage.ID_ELEMENT_SAN_MANAGER % san_mangr)
            xpath_section = FusionSANManagersPage.ID_MANAGEDSAN_LIST
            sans_number = ui_lib.get_text(FusionSANManagersPage.ID_LINK_SANSCOUNT, 1)
            sans_count = sans_number.replace("SANs", "")
            sans_count = int(sans_count)
            try:
                ui_lib.wait_for_element_visible(xpath_section, 5)
            except:
                pass
            for san in range(sans_count):
                xpath_san = build_xpath_managed_sans_table(str(san + 1))
                try:
                    ui_lib.wait_for_element_visible(xpath_san, 5)
                except:
                    pass
                san_value_sanmanagerpage = ui_lib.get_text(xpath_san, 1)
                ui_lib.wait_for_element_and_click(xpath_san)
                xpath_sanvalue_sanpage = FusionSANPage.ID_SAN_DETAILS_TITLE
                try:
                    ui_lib.wait_for_element_visible(xpath_sanvalue_sanpage, 5)
                except:
                    pass
                san_value_sanspage = ui_lib.get_text(xpath_sanvalue_sanpage, 1)
                if(san_value_sanmanagerpage == san_value_sanspage):
                    logger._log_to_console_and_log_file(san_value_sanmanagerpage + " link and value verified ")
                else:
                    ui_lib.fail_test("unable to navigate to" + san_value_sanspage + "page and verify")

                if not s2l._is_element_present(FusionSANManagersPage.ID_PAGE_LABEL):
                    if not navigate():
                        return False

        else:
            """ add to count so that len of list and count are equal """
            logger._log_to_console_and_log_file("Flat san could not be validated")

    return True


def build_xpath_managed_sans_table(x):
    xpath_input = "xpath=//*[@id='cic-sanmanagers-managed-sans-table']/tbody/tr[" + x + "]/td[2]/a"
    return xpath_input


def verify_sanmanagers_count_dashboard(*sanmanager_obj):
    logger._log_to_console_and_log_file("Function call to Add dashboard panel and validate sanmanagers count from Dashboard")
    s2l = ui_lib.get_s2l()

    """ Navigate to SAN Manager Page """
    if not s2l._is_element_present(FusionSANManagersPage.ID_PAGE_LABEL):
        if not navigate():
            return False

    san_managers_count = ui_lib.get_text(FusionSANManagersPage.ID_SAN_MANAGERS_COUNT, 2)

    """ Retrieve data from datasheet """
    if isinstance(sanmanager_obj, test_data.DataObj):
        sanmanager_obj = [sanmanager_obj]
    elif isinstance(sanmanager_obj, tuple):
        sanmanager_obj = list(sanmanager_obj)

    """ Navigate to Dashboard Page  *sanmanager_obj """
    fusion_ui.dashboard.navigate()
    fusion_ui.dashboard.create_dashboard(sanmanager_obj)
#    fusion_ui.dashboard.verify_dashboard_exist(sanmanager_obj)
    fusion_ui.dashboard.navigate()
    san_managers_count_dashboard = ui_lib.get_text(FusionSANManagersPage.ID_DASHBOARD_SAN_MANAGERS_COUNT, 1)
    if(san_managers_count == san_managers_count_dashboard):
        logger._log_to_console_and_log_file("successfully verified dashboard san managers count")
        return True
    else:
        message = "Dashboard san managers count failed to match with actual sanmanagers count"
        raise AssertionError(message)


def highlight_san_manager(sanmgr_value):
    xpath_input = (FusionSANManagersPage.ID_SAN_MANAGER_LIST + "[text()='%s']" % sanmgr_value)
    try:
        ui_lib.wait_for_element_visible(xpath_input, 5)
    except:
        pass
    logger._info("Highlighting san manager=%s" % sanmgr_value)
    ui_lib.wait_for_element_and_click(xpath_input)


def edit_user_input_pswd(password):
    xpath_password = FusionSANManagersPage.ID_SAN_EDIT_BNA_PSWD
    try:
        ui_lib.wait_for_element_visible(xpath_password, 10)
    except:
        pass

    ui_lib.wait_for_element_and_input_text(xpath_password, password)


def edit_user_input_username(username):
    selenium2lib = ui_lib.get_s2l()
    selenium2lib.reload_page()
    xpath_username = FusionSANManagersPage.ID_SAN_EDIT_BNA_USERNAME
    try:
        ui_lib.wait_for_element_visible(xpath_username, 10)
    except:
        pass

    ui_lib.wait_for_element_and_input_text(xpath_username, username)


def edit_user_input_hostname(hostname):
    selenium2lib = ui_lib.get_s2l()
    selenium2lib.reload_page()
    xpath_hostname = FusionSANManagersPage.ID_SAN_EDIT_BNA_HOSTNAME
    try:
        ui_lib.wait_for_element_visible(xpath_hostname, 10)
    except:
        pass

    ui_lib.wait_for_element_and_input_text(xpath_hostname, hostname)


def edit_san_manager_click_ok():
    xpath_ok = FusionSANManagersPage.ID_BTN_EDIT_SAN_MANAGER_OK
    try:
        ui_lib.wait_for_element_visible(xpath_ok, 10)
    except:
        pass

    ui_lib.wait_for_element_and_click(xpath_ok)


def edit_san_manager_click_cancel():
    xpath_cancel = FusionSANManagersPage.ID_BTN_EDIT_SAN_MANAGER_CANCEL
    try:
        ui_lib.wait_for_element_visible(xpath_cancel, 10)
    except:
        pass

    ui_lib.wait_for_element_and_click(xpath_cancel)


def validate_unable_to_edit_san_manager(err_type):
    xpath_unable_to_add_error = FusionSANManagersPage.EDIT_SAN_MANAGER_ERR_MSG
    logger._log_to_console_and_log_file("Validate %s error" % err_type)
    xpath_required = FusionSANManagersPage.EDIT_SAN_MANAGER_REQUIRED_ERR_MSG
    msg1 = "Unable to edit SAN manager."
    msg2 = "This field is required."
    msg3 = "Resolution: "
    field_req = False

    if (err_type == 'credentials'):
        xpath_error_details = FusionSANManagersPage.EDIT_SAN_MANAGER_ERR_CREDENTIALS
        xpath_error_resolution = (FusionSANManagersPage.EDIT_SAN_MANAGER_ERR_CREDENTIALS +
                                  FusionSANManagersPage.EDIT_SAN_MANAGER_ERR_RESOLUTION)
        msg = "The specified user name and/or password is not valid for the SAN manager."
    elif (err_type == 'fielderr'):
        xpath_error_details = FusionSANManagersPage.ADD_SAN_ERR_HOST_REQUIRED
        xpath_error_resolution = (FusionSANManagersPage.ADD_SAN_ERR_HOST_REQUIRED + FusionSANManagersPage.ADD_SAN_ERR_RESOLUTION)
        msg = "One or more fields have an invalid value."
        field_req = True

    else:
        logger._log_to_console_and_log_file("Validate field invalid error")

    try:
        ui_lib.wait_for_element_visible(xpath_unable_to_add_error, 10)
        ui_lib.wait_for_element_visible(xpath_error_details, 10)
        ui_lib.wait_for_element_visible(xpath_error_resolution, 10)
    except:
        pass

    logger._log_to_console_and_log_file("Validate '%s' message" % msg)
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_unable_to_add_error), msg1)
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_error_details), msg)
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_error_resolution), msg3)
    if (field_req is True):
        BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_required), msg2)


def create_oneview_users(*sanmanager_obj):
    logger._log_to_console_and_log_file("Function call to Create all users and verify auth levels")
    """ Create all the users   *sanmanager_obj """
    fusion_ui.usersandgroups.create_user(*sanmanager_obj)


def verify_san_manager_actions_unauthorized_users(user):
    xpath_tab = FusionSANManagersPage.ID_MENU_ACTION_MAIN_BTN
    xpath_tab_option1 = FusionSANManagersPage.ID_NO_AUTH
    try:
        ui_lib.wait_for_element_visible(xpath_tab, 10)
    except:
        pass

    ui_lib.wait_for_element_and_click(xpath_tab)
    msg_name = "No authorization"
    if ((ui_lib.get_text(xpath_tab_option1, 1)) == msg_name):
        logger._log_to_console_and_log_file(msg_name + " msg found")
    else:
        ui_lib.fail_test("unable to find the" + msg_name + " msg")


def click_map_level(maplevel):

    if (maplevel == 'Level1'):
        xpath_level = FusionSANManagersPage.ID_MAP_TOP_LEVEL
    else:
        xpath_level = FusionSANManagersPage.ID_MAP_SECOND_LEVEL

    try:
        ui_lib.wait_for_element_visible(xpath_level, 5)
    except:
        pass
    logger._info("Click on Map page level=%s" % maplevel)
    ui_lib.wait_for_element_and_click(xpath_level)


def validate_page_title(pagetitle):
    if (pagetitle == 'SAN Managers'):
        xpath_title = FusionSANManagersPage.ID_PAGE_LABEL
    else:
        xpath_title = FusionSANPage.ID_PAGE_LABEL

    try:
        ui_lib.wait_for_element_visible(xpath_title, 10)
    except:
        pass

    if ((ui_lib.get_text(xpath_title, 1)) == pagetitle):
        logger._log_to_console_and_log_file(pagetitle + " page found")
    else:
        ui_lib.fail_test("unable to find the" + pagetitle + " page")


def click_san_manager_edit_help():

    xpath_help = FusionSANManagersPage.ID_EDIT_HELP_LINK

    try:
        ui_lib.wait_for_element_visible(xpath_help, 5)
    except:
        pass

    logger._info("Click on SAN manager edit help icon")
    ui_lib.wait_for_element_and_click(xpath_help)


def add_san_managers(version, *sanmanager_obj):
    """
        add_san_manager function to add san manager to the appliance

        Example:
        | Add San Managers      | @{sanmanager_obj}    |
    """
    FusionUIBase.navigate_to_section(SectionType.SAN_MANAGERS)
    if isinstance(sanmanager_obj, test_data.DataObj):
        sanmanager_obj = [sanmanager_obj]
    elif isinstance(sanmanager_obj, tuple):
        sanmanager_obj = list(sanmanager_obj)
    count = 0
    new_sanmanager_obj = []
    logger.info("{0} PREPARATION  {0}".format('-' * 17))
    for n, sanmanager in enumerate(sanmanager_obj):
        name = sanmanager.sanip
        if getattr(sanmanager, 'remove_if_exists', 'true').lower() == 'true':
            remove_if_exists = True
        else:
            remove_if_exists = False

        if not CommonOperationSANMangers.verify_san_manager_not_exist(name, fail_if_false=False):
            logger.warn("SAN manager '{0}' already exists".format(name))
            if remove_if_exists is True:
                logger.info("Removing the SAN manager since 'remove_if_exists' is set to 'True'")
                if not remove_san_manager(name, fail_if_false=False):
                    count += 1
                else:
                    new_sanmanager_obj.append(sanmanager)
            else:
                logger.warn("Error: Would not be able to create the existing san manager '%s'." % name)
                count += 1
        else:
            new_sanmanager_obj.append(sanmanager)

    for n, sanmanager in enumerate(new_sanmanager_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(sanmanager_obj), '-' * 14))
        name = sanmanager.sanip
        logger.info("Adding a san manager with name '{0}'".format(name))
        if n == 0:
            FusionUIBase.show_activity_sidebar()
            AddSANMangers.click_add_san_manager_button()
        AddSANMangers.wait_add_san_manager_dialog_shown()
        AddSANMangers.select_san_manager_type(sanmanager.type)
        if sanmanager.type.lower().replace(' ', '') == "Brocade Network Advisor".lower().replace(' ', ''):
            AddSANMangers.input_ip_address_or_host_name(name, appversion=version)
            if getattr(sanmanager, 'port', '') != '':
                AddSANMangers.input_port(sanmanager.port)
            if sanmanager.sanmanagerssl.lower() == 'true':
                AddSANMangers.tick_use_ssl(appversion=version)
            else:
                AddSANMangers.untick_use_ssl(appversion=version)
            if getattr(sanmanager, 'username', '') != '':
                AddSANMangers.input_user_name(sanmanager.username, appversion=version)
            AddSANMangers.input_password(sanmanager.password, appversion=version)
        elif sanmanager.type.lower() == "cisco":
            AddSANMangers.input_ip_address_or_host_name_cisco(name)
            if getattr(sanmanager, 'snmpport', '') != '':
                AddSANMangers.input_snmp_port(sanmanager.snmpport)
            AddSANMangers.input_snmp_user_name(sanmanager.username)
            if getattr(sanmanager, 'securitylevel', '') != '':
                AddSANMangers.choose_security_level(sanmanager.securitylevel, sanmanager.type)
            if getattr(sanmanager, 'authprotocol', '') != '':
                AddSANMangers.select_authentication_protocol(sanmanager.authprotocol)
            AddSANMangers.input_authentication_password(sanmanager.authpassword)
        elif sanmanager.type.lower() == "hpe":
            AddSANMangers.input_ip_address_or_host_name_hpe(name)
            if getattr(sanmanager, 'snmpport', '') != '':
                AddSANMangers.input_snmp_port(sanmanager.snmpport)
            AddSANMangers.input_snmp_user_name(sanmanager.username)
            if getattr(sanmanager, 'securitylevel', '') != '':
                AddSANMangers.choose_security_level(sanmanager.securitylevel, sanmanager.type)
            if getattr(sanmanager, 'authenticationprotocol', '') != '':
                AddSANMangers.select_authentication_protocol(sanmanager.authenticationprotocol)
            if getattr(sanmanager, 'authenticationpassword', '') != '':
                AddSANMangers.input_authentication_password(sanmanager.authenticationpassword)
            if getattr(sanmanager, 'privacypassword', '') != '':
                AddSANMangers.input_privacy_password(sanmanager.privacypassword)
        else:
            ui_lib.fail_test("unsupported san_manager type '%s', please specify 'Brocade Network Advisor', 'Cisco' or 'HPE'" % sanmanager.type)

        if n == (len(new_sanmanager_obj) - 1):
            AddSANMangers.click_add_button()
        else:
            AddSANMangers.click_add_plus_button()
        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
        if status is True:
            ui_lib.fail_test(msg)
        FusionUIBase.wait_activity_action_ok(name, message="Add SAN manager", timeout=30)
    AddSANMangers.wait_add_san_manager_dialog_disappear(timeout=5)
    FusionUIBase.show_activity_sidebar()
    logger.info("{0} VERIFICATION {0}".format('-' * 17))
    for n, sanmanager in enumerate(new_sanmanager_obj):
        name = sanmanager.sanip
        CommonOperationSANMangers.wait_san_manager_status_ok(name)
        logger.info("Add san manager {0} successfully".format(name))

    if count > 0:
        logger.warn("Failure: Not able to add some of san managers, please check all warning messages")
        return False

    return True


def edit_san_managers(*sanmanager_obj):
    """ Edit san managers    """
    FusionUIBase.navigate_to_section(SectionType.SAN_MANAGERS)
    if isinstance(sanmanager_obj, test_data.DataObj):
        sanmanager_obj = [sanmanager_obj]
    elif isinstance(sanmanager_obj, tuple):
        sanmanager_obj = list(sanmanager_obj)
    count = 0
    for n, sanmanager in enumerate(sanmanager_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(sanmanager_obj), '-' * 14))
        logger.info("Editing a san manager with name '{0}'".format(sanmanager.sanip))
        if not select_san_manager(sanmanager.sanip):
            count += 1
            continue

        EditSANMangers.select_action_edit()
        EditSANMangers.wait_edit_san_manager_dialog_shown()
        if getattr(sanmanager, 'newsanip', '') != '':
            name = sanmanager.newsanip
            EditSANMangers.input_ip_address_or_host_name(sanmanager.newsanip)
        else:
            name = sanmanager.sanip
        if getattr(sanmanager, 'port', '') != '':
            EditSANMangers.input_port(sanmanager.port)
        if getattr(sanmanager, 'sanmanagerssl', '') != '':
            if sanmanager.sanmanagerssl.lower() == 'true':
                EditSANMangers.tick_use_ssl()
            else:
                EditSANMangers.untick_use_ssl()
        if getattr(sanmanager, 'username', '') != '':
            EditSANMangers.input_user_name(sanmanager.username)
        if getattr(sanmanager, 'password', '') != '':
            EditSANMangers.input_password(sanmanager.password)

        EditSANMangers.click_ok_button()
        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
        if status is True:
            ui_lib.fail_test(msg)
        EditSANMangers.wait_edit_san_manager_dialog_disappear(timeout=10)
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(sanmanager.sanip, "Update SAN manager", timeout=30)
        FusionUIBase.show_activity_sidebar()
        CommonOperationSANMangers.wait_san_manager_status_ok(name)
        logger.info("Edit san manager {0} successfully".format(sanmanager.sanip))
    if count > 0:
        logger.warn("Not able to edit some of SAN managers, please check warning messages!")
        return False
    return True


def remove_san_manager(name, fail_if_false=True):
    select_san_manager(name)
    RemoveSANMangers.select_action_remove()
    RemoveSANMangers.wait_remove_san_manager_dialog_shown()
    RemoveSANMangers.click_yes_remove()
    RemoveSANMangers.wait_remove_san_manager_dialog_disappear()
    FusionUIBase.show_activity_sidebar()
    FusionUIBase.wait_activity_action_ok(name, "Remove SAN manager", timeout=50)
    FusionUIBase.show_activity_sidebar()
    if CommonOperationSANMangers.wait_san_manager_show_not_found(name, timeout=15, fail_if_false=False):
        logger.info("SAN manager status appear as 'not found', remove san manager {0} successfully.".format(name))
        return True
    elif CommonOperationSANMangers.verify_san_manager_not_exist(name, timeout=5, fail_if_false=False):
        logger.info("Remove SAN manager {0} successfully".format(name))
        return True
    else:
        if fail_if_false is True:
            ui_lib.fail_test("The SAN manager does not disappear in 20s!")
        else:
            logger.warn("The SAN manager does not disappear in 20s!")


def remove_san_managers(*sanmanager_obj):
    logger.info("Function call to remove san manager")
    FusionUIBase.navigate_to_section(SectionType.SAN_MANAGERS)
    if isinstance(sanmanager_obj, test_data.DataObj):
        sanmanager_obj = [sanmanager_obj]
    elif isinstance(sanmanager_obj, tuple):
        sanmanager_obj = list(sanmanager_obj)

    count = 0
    for n, sanmanager in enumerate(sanmanager_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(sanmanager_obj), '-' * 14))
        logger.info("Removing a SAN manager with name %s" % sanmanager.sanip)
        if not select_san_manager(sanmanager.sanip):
            count += 1
            continue
        remove_san_manager(sanmanager.sanip)
    if count > 0:
        logger.warn("Not able to remove some of SAN managers, please check warning messages!")
        return False
    return True


def remove_all_san_managers():
    logger.info("Function call to remove SAN managers")
    FusionUIBase.navigate_to_section(SectionType.SAN_MANAGERS)
    san_list = CommonOperationSANMangers.get_san_manager_list()
    san_obj_list = []
    for san_name in san_list:
        logger.info("Deleting SAN manager %s" % san_name)
        san_obj = test_data.DataObj()
        san_obj.add_property('name', san_name)
        san_obj_list.append(san_obj)
    return remove_san_managers(*san_obj_list)


def edit_san_manager(*sanmanager_obj):
    """ Edit san managers    """
    FusionUIBase.navigate_to_section(SectionType.SAN_MANAGERS)
    if isinstance(sanmanager_obj, test_data.DataObj):
        sanmanager_obj = [sanmanager_obj]
    elif isinstance(sanmanager_obj, tuple):
        sanmanager_obj = list(sanmanager_obj)
    count = 0
    for n, sanmanager in enumerate(sanmanager_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(sanmanager_obj), '-' * 14))
        logger.info("Editing a san manager with name '{0}'".format(sanmanager.sanip))
        if not select_san_manager(sanmanager.sanip):
            count += 1
            continue

        EditSANMangers.select_action_edit()
        EditSANMangers.wait_edit_san_manager_dialog_shown()
        if getattr(sanmanager, 'newsanip', '') != '':
            name = sanmanager.newsanip
            EditSANMangers.input_ip_address_or_host_name(sanmanager.newsanip)
        else:
            name = sanmanager.sanip
        if getattr(sanmanager, 'port', '') != '':
            EditSANMangers.input_port(sanmanager.port)
        if getattr(sanmanager, 'sanmanagerssl', '') != '':
            if sanmanager.sanmanagerssl.lower() == 'true':
                EditSANMangers.tick_use_ssl()
            else:
                EditSANMangers.untick_use_ssl()
        if getattr(sanmanager, 'username', '') != '':
            EditSANMangers.input_user_name(sanmanager.username)
        if getattr(sanmanager, 'password', '') != '':
            EditSANMangers.input_password(sanmanager.password)

        EditSANMangers.click_ok_button()
        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
        if status is True:
            ui_lib.fail_test(msg)
        EditSANMangers.wait_edit_san_manager_dialog_disappear(timeout=10)
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(sanmanager.sanip, "Update SAN manager", timeout=30)
        FusionUIBase.show_activity_sidebar()
        CommonOperationSANMangers.wait_san_manager_status_ok(name)
        logger.info("Edit san manager {0} successfully".format(sanmanager.sanip))
    if count > 0:
        logger.warn("Not able to edit some of SAN managers, please check warning messages!")
        return False
    return True


def select_san_manager(name):
    """ Select san manager  """
    logger.info("Selecting a SAN manager with name {0}".format(name))
    if CommonOperationSANMangers.verify_san_manager_exist(name, fail_if_false=False):
        CommonOperationSANMangers.click_san_manager(name)
        CommonOperationSANMangers.wait_san_manager_selected(name)
        return True
    else:
        logger.warn("SAN manager '{0}' does not exist".format(name))
        return False


def refresh_san_managers(*sanmanager_obj):
    FusionUIBase.navigate_to_section(SectionType.SAN_MANAGERS)
    if isinstance(sanmanager_obj, test_data.DataObj):
        sanmanager_obj = [sanmanager_obj]
    elif isinstance(sanmanager_obj, tuple):
        sanmanager_obj = list(sanmanager_obj)
    count = 0

    for n, sanmanager in enumerate(sanmanager_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(sanmanager_obj), '-' * 14))
        name = sanmanager.sanip
        logger.info("Refreshing a san manager with name '{0}'".format(name))
        if not select_san_manager(name):
            count += 1
            continue
        RefreshSANMangers.select_action_refresh()
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(name, "Refresh SAN manager", timeout=30)
        FusionUIBase.show_activity_sidebar()
        CommonOperationSANMangers.wait_san_manager_status_ok(name)
        logger.info("Refresh san manager {0} successfully".format(name))
    if count > 0:
        logger.warn("Failure: Not able to refresh some of san managers, please check warning messages.")
        return False

    return True

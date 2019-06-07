# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
#    Fusion SAN Managers UI page. """
#    added HP switch 5900 info """


from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.san.san_elements import FusionSANPage
from FusionLibrary.ui.sanmanager.sanmanagers_elements import FusionSANManagersPage
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from FusionLibrary.ui.business_logic.base import FusionUIBase, SectionType


ROBOT_LIBRARY_VERSION = '0.0'
# #########################################################################
# SAN page general functions (links, actions, tabs)
# #########################################################################


CONF_DICT = {
    'browser_type': None,
    'remote_run': False,
    'timeout': 5,
    'speed': 0.01
}


def navigate_to_san_page(renavigate=False):
    FusionUIBase.navigate_to_section(SectionType.SANS)


def highlight_san(san_value):
    xpath_input = (FusionSANPage.ID_SAN_LIST + "[text()='%s']" % san_value)
    try:
        ui_lib.wait_for_element_visible(xpath_input, 5)
    except:
        pass
    logger._log_to_console_and_log_file("Highlighting san=%s" % san_value)
    ui_lib.wait_for_element_and_click(xpath_input)


def open_san_actions_edit_dialog_page():
    xpath_edit_action = FusionSANPage.ID_SAN_MENU_ACTION_MAIN_BTN
    xpath_edit = FusionSANPage.ID_SAN_MENU_ACTION_EDIT
    xpath_dialog_title = FusionSANPage.ID_SAN_EDIT_PAGE_TITLE

    def is_dialog_open(self):
        if ui_lib.wait_for_element_visible(xpath_dialog_title):
            return True
        try:
            logger._info('Clicking %s' % xpath_edit_action)
            ui_lib.wait_for_element_and_click(xpath_edit_action, 5)
            logger._info('Clicking %s' % xpath_edit)
            ui_lib.wait_for_element_and_click(xpath_edit, 5)
        except:
            return False
        return True
    sl2 = ui_lib.get_s2l()
    timeout = CONF_DICT['timeout'] or 10
    wait = WebDriverWait(sl2._get_current_browser(),
                         timeout,
                         CONF_DICT['speed'],
                         StaleElementReferenceException)
    return wait.until(is_dialog_open)


def san_endpoints_click_update():
    xpath_update = FusionSANPage.ID_SAN_ENDPOINTS_UPDATE
    try:
        ui_lib.wait_for_element_visible(xpath_update, 10)
    except:
        pass

    ui_lib.wait_for_element_and_click(xpath_update)


def open_san_action(action_name):
    xpath_action = FusionSANPage.ID_SAN_MENU_ACTION_MAIN_BTN

    logger._log_to_console_and_log_file("Choose %s from action menu" % action_name)

    if (action_name == 'Edit'):
        xpath_action2 = FusionSANPage.ID_SAN_MENU_ACTION_EDIT
    elif (action_name == 'Refresh'):
        xpath_action2 = FusionSANPage.ID_SAN_MENU_ACTION_REFRESH
    elif (action_name == 'Download'):
        xpath_action2 = FusionSANPage.ID_SAN_MENU_ACTION_DOWNLOAD
    elif (action_name == 'Report'):
        xpath_action2 = FusionSANPage.ID_SAN_MENU_ACTION_REPORT

    else:
        logger._log_to_console_and_log_file("Invalid action requested on san")
        return False
    try:
        ui_lib.wait_for_element_visible(xpath_action, 10)
    except:
        pass

    logger._log_to_console_and_log_file("Open SAN actions menu-%s" % action_name)
    ui_lib.wait_for_element_and_click(xpath_action, 10)
    ui_lib.wait_for_element_and_click(xpath_action2, 10)


def endpoints_click_download():
    xpath_download = FusionSANPage.ID_SAN_DOWNLOAD_ENDPOINTS
    try:
        ui_lib.wait_for_element_visible(xpath_download, 10)
    except:
        pass

    ui_lib.wait_for_element_and_click(xpath_download)


def add_user_input_filter(filter_name, values):
    logger._log_to_console_and_log_file("Adding data to %s filter on san endpoints" % filter_name)
    selenium2lib = ui_lib.get_s2l()
    selenium2lib.maximize_browser_window()

    if (filter_name == 'endpoint'):
        xpath_filter = FusionSANPage.ID_SAN_ENDPOINTS_FILTER_ENDPOINT
    elif (filter_name == 'wwpn'):
        xpath_filter = FusionSANPage.ID_SAN_ENDPOINTS_FILTER_WWPN
    elif (filter_name == 'alias'):
        xpath_filter = FusionSANPage.ID_SAN_ENDPOINTS_FILTER_ALIAS
    elif (filter_name == 'online'):
        xpath_filter = FusionSANPage.ID_SAN_ENDPOINTS_FILTER_ONLINE
    elif (filter_name == 'zone'):
        xpath_filter = FusionSANPage.ID_SAN_ENDPOINTS_FILTER_ZONE

    else:
        logger._log_to_console_and_log_file("Invalid action requested for san endpoints filter")
        return False

    try:
        ui_lib.wait_for_element_visible(xpath_filter, 20)
    except:
        pass

    ui_lib.wait_for_element_and_click(xpath_filter, 20)
    ui_lib.wait_for_element_and_input_text(xpath_filter, values)


def validate_filter(line_count):
    logger._log_to_console_and_log_file("Validating count= %s on san endpoints page is as expected" % line_count)

    xpath_count = FusionSANPage.ID_SAN_ENDPOINTS_COUNT

    try:
        ui_lib.wait_for_element_visible(xpath_count, 20)
    except:
        pass

    BuiltIn().should_be_equal(ui_lib.get_text(xpath_count, 1), line_count)


def validate_filter_message(msg):
    logger._log_to_console_and_log_file("Validating filter message= %s is as expected" % msg)

    xpath_msg = FusionSANPage.ID_SAN_ENDPOINTS_MESSAGE

    try:
        ui_lib.wait_for_element_visible(xpath_msg, 30)
    except:
        pass

    msg = "There are no available SAN endpoints to display."
    BuiltIn().should_be_equal(ui_lib.get_text(xpath_msg, 1), msg)


def validate_default_tab():
    xpath_tab = FusionSANPage.ID_MENU_VIEW_MAIN_BTN

    try:
        ui_lib.wait_for_element_visible(xpath_tab, 10)
    except:
        pass
    logger._log_to_console_and_log_file("Validate default SAN screen tab of General")
    tab_name = "General"
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_tab), tab_name)


def validate_tabs():
    xpath_section = FusionSANPage.ID_MENU_VIEW_MAIN_BTN
    xpath_title1 = FusionSANPage.ID_VIEW_GENERAL_SAN
    xpath_title2 = FusionSANPage.ID_VIEW_ZONINGPOLICY_SAN
    xpath_title3 = FusionSANPage.ID_VIEW_SANENDPOINTS_SAN
    xpath_title4 = FusionSANPage.ID_VIEW_ACTIVITY_SAN
    xpath_title5 = FusionSANPage.ID_VIEW_MAP_SAN
    xpath_title6 = FusionSANPage.ID_VIEW_LABELS_SAN
    try:
        ui_lib.wait_for_element_visible(xpath_section, 10)
    except:
        pass
    ui_lib.wait_for_element_and_click(xpath_section)

    title = "General"
    if ((ui_lib.get_text(xpath_title1, 1)) == title):
        logger._log_to_console_and_log_file(title + " Section found")
    else:
        ui_lib.fail_test("unable to find the " + title + " section")

    title = "Zoning Policy"
    if ((ui_lib.get_text(xpath_title2, 1)) == title):
        logger._log_to_console_and_log_file(title + " Section found")
    else:
        ui_lib.fail_test("unable to find the " + title + " section")

    title = "SAN Endpoints"
    if ((ui_lib.get_text(xpath_title3, 1)) == title):
        logger._log_to_console_and_log_file(title + " Section found")
    else:
        ui_lib.fail_test("unable to find the " + title + " section")

    title = "Activity"
    if ((ui_lib.get_text(xpath_title4, 1)) == title):
        logger._log_to_console_and_log_file(title + " Section found")
    else:
        ui_lib.fail_test("unable to find the " + title + " section")

    title = "Map"
    if ((ui_lib.get_text(xpath_title5, 1)) == title):
        logger._log_to_console_and_log_file(title + " Section found")
    else:
        ui_lib.fail_test("unable to find the " + title + " section")

    title = "Labels"
    if ((ui_lib.get_text(xpath_title6, 1)) == title):
        logger._log_to_console_and_log_file(title + " Section found")
    else:
        ui_lib.fail_test("unable to find the " + title + " section")
    return True


def san_change_tab(tab_name):
    xpath_tab = FusionSANPage.ID_MENU_VIEW_MAIN_BTN

    if (tab_name == "General"):
        xpath_tab_name = FusionSANPage.ID_VIEW_GENERAL_SAN
    elif (tab_name == "Zoning Policy"):
        xpath_tab_name = FusionSANPage.ID_VIEW_ZONINGPOLICY_SAN
    elif (tab_name == "SAN Endpoints"):
        xpath_tab_name = FusionSANPage.ID_VIEW_SANENDPOINTS_SAN
    elif (tab_name == "Activity"):
        xpath_tab_name = FusionSANPage.ID_VIEW_ACTIVITY_SAN
    elif (tab_name == "Map"):
        xpath_tab_name = FusionSANPage.ID_VIEW_MAP_SAN
    elif (tab_name == "Labels"):
        xpath_tab_name = FusionSANPage.ID_VIEW_LABELS_SAN

    try:
        ui_lib.wait_for_element_visible(xpath_tab, 10)

    except:
        pass

    ui_lib.wait_for_element_and_click(xpath_tab)
    ui_lib.wait_for_element_and_click(xpath_tab_name)

# #########################################################################
# SAN screen actions functions
# #########################################################################


def san_actions_validate():
    xpath_action = FusionSANPage.ID_SAN_MENU_ACTION_MAIN_BTN
    xpath_action_option = FusionSANPage.ID_SAN_MENU_ACTION_EDIT

    try:
        ui_lib.wait_for_element_visible(xpath_action, 10)
    except:
        pass
    logger._log_to_console_and_log_file("Validate SAN actions menu")
    ui_lib.wait_for_element_and_click(xpath_action)
    action_name = "Edit"
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_action_option), action_name)


def validate_section_on_san_screen(section_name):
    logger._log_to_console_and_log_file("section_name=%s" % section_name)
    xpath_section = FusionSANPage.ID_SAN_SECTION_NAME

    try:
        ui_lib.wait_for_element_visible(xpath_section, 12)
    except:
        pass
    logger._log_to_console_and_log_file("Validate %s section on SAN screen" % section_name)
    logger._log_to_console_and_log_file("get text value=%s" % ui_lib.get_text(xpath_section, 1))

    if (section_name != "General"):   # and section_name != "SAN Endpoints"):
        BuiltIn().should_be_equal(ui_lib.get_text(xpath_section, 1), (section_name + " Edit"))
    else:
        BuiltIn().should_be_equal(ui_lib.get_text(xpath_section, 1), section_name)


def validate_general_section_titles():
    xpath_section = FusionSANPage.ID_SAN_MENU_ACTION_MAIN_BTN
    xpath_title1 = FusionSANPage.ID_SAN_TYPE
    xpath_title2 = FusionSANPage.ID_SAN_STATE
    xpath_title3 = FusionSANPage.ID_SAN_PRINCIPAL_SWITCH
    xpath_title4 = FusionSANPage.ID_SAN_MANAGER_LINK
    xpath_title5 = FusionSANPage.ID_SAN_ASSOCIATED_NETWORK

    try:
        ui_lib.wait_for_element_visible(xpath_section, 5)
    except:
        pass
    logger._log_to_console_and_log_file("Validate General Section titles")
    title = "Type"
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_title1), title)
    title = "State"
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_title2), title)
    title = "Principal switch"
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_title3), title)
    title = "SAN manager"
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_title4), title)
    title = "Associated network"
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_title5), title)

# #########################################################################
# SAN page activity function
# #########################################################################


def display_san_activity():
    xpath_activity = FusionSANPage.ID_SAN_ACTIVITY
    try:
        ui_lib.wait_for_element_visible(xpath_activity, 10)
    except:
        pass

    logger._log_to_console_and_log_file("Click activity toggle")
    ui_lib.wait_for_element_and_click(xpath_activity, 5)


def check_for_activity(activity):
    xpath_activity = FusionSANPage.ID_SAN_ACTIVITY_MESSAGE
    try:
        ui_lib.wait_for_element_visible(xpath_activity, 10)
    except:
        pass

    logger._log_to_console_and_log_file("Check activity section on screen for '%s'" % activity)
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_activity), activity)

# #########################################################################
# SAN edit page functions
# #########################################################################


def validate_edit_yes_message():
    xpath_message = FusionSANPage.ID_SAN_EDIT_YES_MESSAGE

    try:
        ui_lib.wait_for_element_visible(xpath_message, 5)
    except:
        pass
    logger._log_to_console_and_log_file("Validate Edit SAN Yes message")
    msg = "Enabling automation of zoning will result in the appliance \
    taking full control of the zone naming and contents per specified \
    policies for zones containing server profile initiators."

    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_message), msg)
    if (ui_lib.is_element_enabled(FusionSANPage.ID_SAN_EDIT_OK_BUTTON, 10) is False):
        ui_lib.wait_for_element_and_click(FusionSANPage.ID_SAN_EDIT_CANCEL_BUTTON)
    else:
        ui_lib.wait_for_element_and_click(FusionSANPage.ID_SAN_EDIT_OK_BUTTON)


def validate_edit_no_message():
    xpath_message = FusionSANPage.ID_SAN_EDIT_NO_MESSAGE

    try:
        ui_lib.wait_for_element_visible(xpath_message, 5)
    except:
        pass
    msg = "Disabling automation of zoning implies that the zoning will be performed manually.\
    Until this SAN has been pre-zoned manually for the WWNs of the server hardware and/or\
    the WWNs in the virtual ID pools, SAN volumes attached to server profiles will not\
    be visible to those profiles."
    logger._log_to_console_and_log_file("Validate Edit SAN No message")
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_message), msg)
    if (ui_lib.is_element_enabled(FusionSANPage.ID_SAN_EDIT_OK_BUTTON, 10) is False):
        ui_lib.wait_for_element_and_click(FusionSANPage.ID_SAN_EDIT_CANCEL_BUTTON)
    else:
        ui_lib.wait_for_element_and_click(FusionSANPage.ID_SAN_EDIT_OK_BUTTON)


def edit_san_click_cancel():
    xpath_edit = FusionSANPage.ID_SAN_EDIT_CANCEL_BUTTON
    try:
        ui_lib.wait_for_element_visible(xpath_edit, 10)
    except:
        pass

    ui_lib.wait_for_element_and_click(xpath_edit)


def edit_san_click_ok():
    xpath_edit = FusionSANPage.ID_SAN_EDIT_OK_BUTTON
    try:
        ui_lib.wait_for_element_visible(xpath_edit, 10)
    except:
        pass

    ui_lib.wait_for_element_and_click(xpath_edit)


def open_san_zoning_edit_dialog():
    xpath_action = FusionSANPage.ID_SAN_ZONED_POLICY_EDIT

    try:
        ui_lib.wait_for_element(xpath_action, 10)
    except:
        pass
    logger._log_to_console_and_log_file("Open SAN Zoning Edit Dialog")
    ui_lib.move_to_element_and_click(xpath_action, xpath_action)


def close_edit_san_dialog():
    xpath_action = FusionSANPage.ID_SAN_EDIT_CANCEL_BUTTON

    try:
        ui_lib.wait_for_element_visible(xpath_action, 10)
    except:
        pass
    logger._log_to_console_and_log_file("Close SAN Zoning Edit Dialog")
    ui_lib.wait_for_element_and_click(xpath_action)


def set_edit_san_automate_zoning(zone_value):
    xpath_automate = FusionSANPage.ID_SAN_EDIT_AUTOMATE_ZONING_BTN
    BuiltIn().sleep(5)
    automate_zoning = ui_lib.is_visible(FusionSANPage.ID_SAN_EDIT_YES_MESSAGE, 12)
    logger._log_to_console_and_log_file("Set Edit SAN Automate Zoning value=%s" % zone_value)
    BuiltIn().sleep(5)

    if (zone_value == 'off' and automate_zoning):
        try:
            ui_lib.wait_for_element_and_click(xpath_automate, 12)
        except:
            return False
    elif(zone_value == 'on' and automate_zoning):
        return True
    elif(zone_value == 'off' and automate_zoning is False):
        return True
    elif(zone_value == 'on' and automate_zoning is False):
        try:
            ui_lib.wait_for_element_and_click(xpath_automate, 12)
        except:
            return False


def set_edit_san_zoning_policy(zone_policy):
    xpath_automate = FusionSANPage.ID_SAN_EDIT_ZONING_POLICY_LABEL
    xpath_automate_yes = ui_lib.wait_for_element_visible(FusionSANPage.ID_SAN_EDIT_YES_MESSAGE, 10)

    if not xpath_automate_yes:
        ui_lib.wait_for_element_and_click(xpath_automate, 10)

    try:
        ui_lib.wait_for_element_visible(xpath_automate, 10)
    except:
        pass
    logger._log_to_console_and_log_file("Set Edit SAN Zoning Policy value=%s" % zone_policy)
    ui_lib.wait_for_element_and_click(xpath_automate)
    if (zone_policy == 'Single initiator / single target'):
        ui_lib.wait_for_element_and_click(FusionSANPage.ID_SAN_EDIT_ZONING_POLICY_SELECT, 10)
        ui_lib.wait_for_element_and_click(xpath_automate, 10)

    elif (zone_policy == 'Single initiator / all targets'):
        ui_lib.wait_for_element_and_click(FusionSANPage.ID_SAN_EDIT_ZONING_POLICY_SELECT, 10)
        ui_lib.wait_for_element_and_click(FusionSANPage.ID_SAN_EDIT_ZONING_POLICY_SIAT, 10)

    else:
        ui_lib.wait_for_element_and_click(FusionSANPage.ID_SAN_EDIT_ZONING_POLICY_SELECT, 10)
        ui_lib.wait_for_element_and_click(FusionSANPage.ID_SAN_EDIT_ZONING_POLICY_SISSS, 10)

    if (ui_lib.is_element_enabled(FusionSANPage.ID_SAN_EDIT_OK_BUTTON, 10) is False):
        ui_lib.wait_for_element_and_click(FusionSANPage.ID_SAN_EDIT_CANCEL_BUTTON)
    else:
        ui_lib.wait_for_element_and_click(FusionSANPage.ID_SAN_EDIT_OK_BUTTON)


def set_edit_san_zone_name_format(zone_name):
    xpath_name_label = FusionSANPage.ID_SAN_EDIT_ZONE_NAME_LABEL
    xpath_name = FusionSANPage.ID_SAN_EDIT_ZONE_NAME

    try:
        ui_lib.wait_for_element_and_click(xpath_name_label, 10)
    except:
        return False

    logger._log_to_console_and_log_file("Set Edit SAN Zone name format value=%s" % zone_name)
    if (zone_name != ""):
        ui_lib.wait_for_element_and_input_text(xpath_name, zone_name)

    if (ui_lib.is_element_enabled(FusionSANPage.ID_SAN_EDIT_OK_BUTTON, 10) is False):
        ui_lib.wait_for_element_and_click(FusionSANPage.ID_SAN_EDIT_CANCEL_BUTTON)
    else:
        ui_lib.wait_for_element_and_click(FusionSANPage.ID_SAN_EDIT_OK_BUTTON)


def check_for_error():
    xpath_input_error = FusionSANPage.ID_SAN_EDIT_ERROR_MESSAGE
    try:
        ui_lib.wait_for_element_visible(xpath_input_error, 10)
    except:
        pass
    msg = " "
    logger._log_to_console_and_log_file("Check for error message")
    BuiltIn().should_not_be_true(ui_lib.wait_for_element_visible(xpath_input_error), msg)


def validate_for_edit_san_errors(err_type):
    xpath_unable_to_edit_error = FusionSANPage.ID_SAN_EDIT_ERROR_MESSAGE
    logger._log_to_console_and_log_file("Validate %s error" % err_type)
    msg1 = "Unable to edit SAN."
    msg2 = "This field is required."
    msg3 = "Resolution: "

    if (err_type == 'fielderr'):
        xpath_error_details = FusionSANPage.EDIT_SAN_ERR_ERR_FIELD
        xpath_error_resolution = (FusionSANPage.EDIT_SAN_ERR_ERR_FIELD + FusionSANPage.EDIT_SAN_ERR_RESOLUTION)
        xpath_required = FusionSANPage.EDIT_SAN_REQUIRED_ERR_MSG
        msg = "One or more fields have an invalid value."
    else:
        logger._log_to_console_and_log_file("Unknown error to validate")
        return False
    try:
        ui_lib.wait_for_element_visible(xpath_unable_to_edit_error, 10)
        ui_lib.wait_for_element_visible(xpath_error_details, 10)
        ui_lib.wait_for_element_visible(xpath_error_resolution, 10)

    except:
        pass

    logger._log_to_console_and_log_file("Validate '%s' message" % msg)
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_unable_to_edit_error), msg1)
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_error_details), msg)
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_error_resolution), msg3)
    if (xpath_required != ''):
        BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_required), msg2)


def clear_out_san_edit_input_box(field_name):
    logger._log_to_console_and_log_file("Clear %s textbox on edit san screen" % field_name)
    if (field_name == 'zonename'):
        xpath_name = FusionSANPage.ID_SAN_EDIT_ZONE_NAME
        xpath_name_label = FusionSANPage.ID_SAN_EDIT_ZONE_NAME_LABEL

    elif (field_name == 'initiatoralias'):
        xpath_name = FusionSANPage.ID_SAN_EDIT_INITIATOR_ALIAS
        xpath_name_label = FusionSANPage.ID_SAN_EDIT_INITIATOR_ALIAS_LABEL

    elif (field_name == 'targetalias'):
        xpath_name = FusionSANPage.ID_SAN_EDIT_TARGET_ALIAS
        xpath_name_label = FusionSANPage.ID_SAN_EDIT_TARGET_ALIAS_LABEL

    elif (field_name == 'targetgrpalias'):
        xpath_name = FusionSANPage.ID_SAN_EDIT_TARGET_GRP_ALIAS
        xpath_name_label = FusionSANPage.ID_SAN_EDIT_TARGET_GRP_ALIAS_LABEL

    else:
        return False

    try:
        ui_lib.wait_for_element_visible(xpath_name_label, 10)
    except:
        pass


#    ui_lib.wait_for_element_and_input_text(xpath_name, Keys.CLEAR)
    ui_lib.wait_for_element_and_input_text(xpath_name, Keys.END)
    ui_lib.wait_for_element_and_input_text(xpath_name, Keys.BACKSPACE)
    ui_lib.wait_for_element_and_input_text(xpath_name, Keys.BACKSPACE)
    ui_lib.wait_for_element_and_input_text(xpath_name, Keys.BACKSPACE)


def validate_zoning_policy(zone_policy):
    xpath_policy = FusionSANPage.ID_SAN_ZONING_POLICY
    xpath_label = FusionSANPage.ID_SAN_ZONING_POLICY_LABEL

    try:
        ui_lib.wait_for_element_visible(xpath_label, 10)
    except:
        pass
    logger._log_to_console_and_log_file("Validate Zoning Policy value=%s" % zone_policy)
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_policy), zone_policy)


def validate_automate_zoning(zone_value):
    if (zone_value == 'off'):
        automate = "'No'"
    else:
        automate = "'Yes'"
    xpath_zone = FusionSANPage.ID_SAN_AUTOMATE_ZONING
    xpath_label = FusionSANPage.ID_SAN_AUTOMATE_ZONING_LABEL

    try:
        ui_lib.wait_for_element_visible(xpath_label, 10)
    except:
        pass

    logger._log_to_console_and_log_file("Validate Automate Zoning value=%s" % zone_value)
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_zone), automate)


def validate_default_main_heading(san_value):
    xpath_san = (FusionSANPage.ID_SAN_MAIN_HEADING + " text()='%s']" % san_value)

    try:
        ui_lib.wait_for_element_visible(xpath_san, 10)
    except:
        pass

    logger._info("Validate main header=%s" % san_value)
    BuiltIn().should_be_true(ui_lib.wait_for_element_visible(xpath_san), san_value)


def validate_use_alias(use_alias):
    xpath_alias = FusionSANPage.ID_SAN_USE_ALIASES

    try:
        ui_lib.wait_for_element_visible(xpath_alias, 10)
    except:
        pass
    logger._log_to_console_and_log_file("Validate Use Aliases value=%s" % use_alias)
    BuiltIn().should_be_true(xpath_alias, use_alias)


def set_edit_san_use_alias(use_alias):
    xpath_automate = FusionSANPage.ID_SAN_EDIT_USE_ALIASES

    if (use_alias == 'No'):
        try:
            ui_lib.wait_for_element_and_click(FusionSANPage.ID_SAN_EDIT_USE_ALIASES_NO, 10)
        except:
            return False
    else:
        try:
            ui_lib.wait_for_element_and_click(FusionSANPage.ID_SAN_EDIT_USE_ALIASES_YES, 10)
        except:
            return False
    logger._log_to_console_and_log_file("Set Edit San screen Use Alias value=%s" % use_alias)
    ui_lib.wait_for_element_and_click(xpath_automate, 10)


def verify_san_actions_unauthorized_users(user):
    xpath_tab = FusionSANPage.ID_SAN_MENU_ACTION_MAIN_BTN
    xpath_tab_option1 = FusionSANPage.ID_SAN_MENU_ACTION_NOAUTH
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


def validate_for_report(san_name):
    xpath_heading = FusionSANPage.ID_UNEXPECTED_ZONING_REPORT_HEADING
    xpath_message = FusionSANPage.ID_UNEXPECTED_ZONING_REPORT_MESSAGE
    BuiltIn().sleep(5)
    heading = "Unexpected Zoning Report for %s on 172.18.15.1" % san_name
    message = "No unexpected zoning was found"
    selenium2lib = ui_lib.get_s2l()
    logger._log_to_console_and_log_file("Validate Unexpected Zoning Report for heading and message for %s" % san_name)

    ui_lib.select_window_by_title("OneView", 5)
    BuiltIn().sleep(5)
    if (message == ui_lib.get_text(xpath_message, 1)):
        logger._log_to_console_and_log_file(message + " msg found")
    else:
        ui_lib.fail_test("unable to find the" + message + " msg")
    if (heading == ui_lib.get_text(xpath_heading, 1)):
        logger._log_to_console_and_log_file(heading + " found")
    else:
        ui_lib.fail_test("unable to find the  " + heading + " msg")
        selenium2lib.close_window()


def validate_all_statuses_filter():
    xpath_statuses = FusionSANPage.ID_SAN_ALL_STATUSES
    logger._log_to_console_and_log_file("Validate All Statuses Filter on the SAN Page  %s")
    try:
        ui_lib.wait_for_element_visible(xpath_statuses, 10)
    except:
        pass

    ui_lib.wait_for_element_and_click(xpath_statuses)

    if (ui_lib.get_text(FusionSANPage.ID_SAN_STATUSES_CRITICAL, 1) == "Critical"):
        logger._log_to_console_and_log_file("Status Critical found")
    else:
        ui_lib.fail_test("unable to find the Critical Status, the value is" + ui_lib.get_text(FusionSANPage.ID_SAN_STATUSES_CRITICAL, 1))
    if (ui_lib.get_text(FusionSANPage.ID_SAN_STATUSES_WARNING, 1) == "Warning"):
        logger._log_to_console_and_log_file("Status Warning found")
    else:
        ui_lib.fail_test("unable to find the Warning Status, the value is" + ui_lib.get_text(FusionSANPage.ID_SAN_STATUSES_WARNING, 1))
    if (ui_lib.get_text(FusionSANPage.ID_SAN_STATUSES_OK, 1) == "OK"):
        logger._log_to_console_and_log_file("Status OK found")
    else:
        ui_lib.fail_test("unable to find the OK Status, the value is" + ui_lib.get_text(FusionSANPage.ID_SAN_STATUSES_OK, 1))
    if (ui_lib.get_text(FusionSANPage.ID_SAN_STATUSES_UNKNOWN, 1) == "Unknown"):
        logger._log_to_console_and_log_file("Status Unknown found")
    else:
        ui_lib.fail_test("unable to find the Unknown Status, the value is" + ui_lib.get_text(FusionSANPage.ID_SAN_STATUSES_UNKNOWN, 1))
    if (ui_lib.get_text(FusionSANPage.ID_SAN_STATUSES_DISABLED, 1) == "Disabled"):
        logger._log_to_console_and_log_file("Status Disabled found")
    else:
        ui_lib.fail_test("unable to find the Disabled Status, the value is" + ui_lib.get_text(FusionSANPage.ID_SAN_STATUSES_DISABLED, 1))


def validate_all_states_filter():
    xpath_states = FusionSANPage.ID_SAN_ALL_STATES
    logger._log_to_console_and_log_file("Validate All States Filter on the SAN Page  %s")
    try:
        ui_lib.wait_for_element_visible(xpath_states, 10)
    except:
        pass

    ui_lib.wait_for_element_and_click(xpath_states)

    if (ui_lib.get_text(FusionSANPage.ID_SAN_ALL_STATES_DISCOVERED, 1) == "Discovered"):
        logger._log_to_console_and_log_file("State Discovered found")
    else:
        ui_lib.fail_test("unable to find the Discovered State, the value is" + ui_lib.get_text(FusionSANPage.ID_SAN_ALL_STATES_DISCOVERED, 1))
    if (ui_lib.get_text(FusionSANPage.ID_SAN_ALL_STATES_MANAGED, 1) == "Managed"):
        logger._log_to_console_and_log_file("Status Managed found")
    else:
        ui_lib.fail_test("unable to find the Managed State, the value is" + ui_lib.get_text(FusionSANPage.ID_SAN_ALL_STATES_MANAGED, 1))


def click_san_map_level(maplevel):

    if (maplevel == 'Level2'):
        xpath_level = FusionSANPage.ID_MAP_SECOND_LEVEL
    elif (maplevel == 'Level3'):
        xpath_level = FusionSANPage.ID_MAP_THIRD_LEVEL
    else:
        xpath_level = FusionSANPage.ID_MAP_TOP_LEVEL

    try:
        ui_lib.wait_for_element_visible(xpath_level, 5)
    except:
        pass
    logger._info("Click on Map page level=%s" % maplevel)
    ui_lib.wait_for_element_and_click(xpath_level)


def validate_san_page_title(pagetitle):
    if (pagetitle == 'SAN Managers'):
        xpath_title = FusionSANManagersPage.ID_PAGE_LABEL
    elif (pagetitle == 'SANs'):
        xpath_title = FusionSANPage.ID_PAGE_LABEL
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


def click_san_edit_help():

    xpath_help = FusionSANPage.ID_SAN_EDIT_HELP_LINK

    try:
        ui_lib.wait_for_element_visible(xpath_help, 5)
    except:
        pass

    logger._info("Click on SAN edit help icon")
    ui_lib.wait_for_element_and_click(xpath_help)

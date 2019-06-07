# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Activity Page
"""


from FusionLibrary.ui.business_logic.general.activity_elements import FusionActivityPage
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.business_logic.general.activity import CommonOperationActivity
from FusionLibrary.ui.general import base_page
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.business_logic.base import FusionUIBase, SectionType
import re
import time


def navigate():
    FusionUIBase.navigate_to_section(SectionType.ACTIVITY)


def assign_user(*activities):
    # Assigning user to the activity
    logger._log_to_console_and_log_file("Assigning the user to the Activity starts..")
    selenium2lib = ui_lib.get_s2l()

    # Loads the value from the test data
    if isinstance(activities, test_data.DataObj):
        activities = [activities]
    elif isinstance(activities, tuple):
        activities = list(activities[0])

    ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_TABLE, PerfConstants.DEFAULT_SYNC_TIME)
    logger._log_to_console_and_log_file("Activity Table is loaded with the activities.")
    if not ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_ALL_TYPES, PerfConstants.DEFAULT_SYNC_TIME):
        ui_lib.wait_for_element_and_click(FusionActivityPage.ID_RESET_FILTER)
    ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_ALL_TYPES, PerfConstants.DEFAULT_SYNC_TIME)
    selenium2lib.click_element(FusionActivityPage.ID_FILTER_ALL_TYPES)
    ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_ALERTS, PerfConstants.DEFAULT_SYNC_TIME)
    selenium2lib.click_element(FusionActivityPage.ID_FILTER_ALERTS)
    logger._log_to_console_and_log_file("Activity Table starts loading with the Alert activities only")
    # Loop to upload the list of firmware bundles
    count_fail = 0
    for actname in activities:
        actname.name = actname.name.strip()
        if re.match('^#\d+$', actname.name):
            line_no = actname.name.replace('#', '')
            XPATH_ACTIVITY_SELECT = FusionActivityPage.ID_SELECT_ACTIVITY_BY_ID % line_no
            if ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_ITME_SPAN % XPATH_ACTIVITY_SELECT):
                time.sleep(5)
                actname.name = selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_ITME_SPAN_S1 % XPATH_ACTIVITY_SELECT)
                if ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_ITEM_SPAN_A % XPATH_ACTIVITY_SELECT):
                    actname.name = actname.name + selenium2lib.get_text("%s/p/span/a[1]" % XPATH_ACTIVITY_SELECT)
                if ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_ITEM_SPAN_S2 % XPATH_ACTIVITY_SELECT):
                    actname.name = actname.name + selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_ITEM_SPAN_S2 % XPATH_ACTIVITY_SELECT)
            else:
                actname.name = selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_ITEM_P1 % XPATH_ACTIVITY_SELECT)
        else:
            XPATH_ACTIVITY_SELECT = FusionActivityPage.ID_ACTIVITY_SELECT % (actname.name, actname.resource, actname.date)
        logger._log_to_console_and_log_file("Activity name: %s" % actname.name)

        if ui_lib.wait_for_element_visible(XPATH_ACTIVITY_SELECT, PerfConstants.LOAD_ALERT_ACTIVITY):
            ui_lib.wait_for_element_and_click(XPATH_ACTIVITY_SELECT, PerfConstants.DEFAULT_SYNC_TIME)
            assignuser_name = selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_GET_OWNER % (XPATH_ACTIVITY_SELECT))
            if assignuser_name == actname.assignuser:
                logger._warn("The Activity : '" + actname.name + "' is already assigned with the required owner name : '" + actname.assignuser + "'")
                selenium2lib.capture_page_screenshot()
                count_fail += 1
                continue
            ui_lib.wait_for_element_and_click(FusionActivityPage.ID_ACTION_DROPDOWN, PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTION_DROPDOWN_ASSIGN, PerfConstants.DEFAULT_SYNC_TIME)
            selenium2lib.click_element(FusionActivityPage.ID_ACTION_DROPDOWN_ASSIGN)
            if ui_lib.wait_for_element_visible(FusionActivityPage.ID_ASSIGN_UN_INPUT_BOX, PerfConstants.DEFAULT_SYNC_TIME):
                selenium2lib.input_text(FusionActivityPage.ID_ASSIGN_UN_INPUT_BOX, actname.assignuser)
                ui_lib.wait_for_element_visible(FusionActivityPage.ID_ASSIGN_OK, PerfConstants.DEFAULT_SYNC_TIME)
                selenium2lib.click_element(FusionActivityPage.ID_ASSIGN_OK)
                ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_TABLE, PerfConstants.DEFAULT_SYNC_TIME)
                # Validation if the owner has been assigned successfully
                ui_lib.wait_for_element_and_click(FusionActivityPage.ID_ACTIVITY_SELECT_OWNER % (XPATH_ACTIVITY_SELECT), PerfConstants.DEFAULT_SYNC_TIME)
                assignuser_name = selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_GET_OWNER % (XPATH_ACTIVITY_SELECT))
                if assignuser_name == actname.assignuser:
                    logger._log_to_console_and_log_file("The Activity is successfully assigned with the required owner name : '" + actname.assignuser + "'")
                else:
                    logger._warn("The Activity : '" + actname.name + "' is not assigned with the required owner name : '" + actname.assignuser + "'")
                    selenium2lib.capture_page_screenshot()
                    count_fail += 1
            elif ui_lib.wait_for_element_visible(FusionActivityPage.ID_ASSIGN_ERROR_MSG, PerfConstants.DEFAULT_SYNC_TIME):
                ui_lib.wait_for_element_visible(FusionActivityPage.ID_ASSIGN_ERROR_OK, PerfConstants.DEFAULT_SYNC_TIME)
                selenium2lib.click_element(FusionActivityPage.ID_ASSIGN_ERROR_OK)
                ui_lib.wait_for_element_and_click(XPATH_ACTIVITY_SELECT, PerfConstants.DEFAULT_SYNC_TIME)
                activity_state = selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_STATE % (XPATH_ACTIVITY_SELECT))
                logger._warn("The Activity : '" + actname.name + "' selected cannot be assigned with the owner name : '" + actname.assignuser + "' as the activity is in the state : '" + activity_state + "' And\Or may be the Activity is Tasks and not the Alerts")
                selenium2lib.capture_page_screenshot()
                count_fail += 1
        else:
            logger._warn("The Activity : '" + actname.name + "' is not existing in the activity page or the Activity may be Tasks and not the Alerts")
            selenium2lib.capture_page_screenshot()
            count_fail += 1
    if count_fail > 0:
        return False
    else:
        return True


def clear_activity(*activities):
    # Assigning user to the activity
    logger._log_to_console_and_log_file("Clearing the state of the Activity starts..")
    selenium2lib = ui_lib.get_s2l()

    # Loads the value from the test data
    if isinstance(activities, test_data.DataObj):
        activities = [activities]
    elif isinstance(activities, tuple):
        activities = list(activities[0])

    ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_TABLE, PerfConstants.DEFAULT_SYNC_TIME)
    logger._log_to_console_and_log_file("Activity Table is loaded with the activities.")
    if not ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_ALL_TYPES, PerfConstants.DEFAULT_SYNC_TIME):
        ui_lib.wait_for_element_and_click(FusionActivityPage.ID_RESET_FILTER)
    ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_ALL_TYPES, PerfConstants.DEFAULT_SYNC_TIME)
    selenium2lib.click_element(FusionActivityPage.ID_FILTER_ALL_TYPES)
    ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_ALERTS, PerfConstants.DEFAULT_SYNC_TIME)
    selenium2lib.click_element(FusionActivityPage.ID_FILTER_ALERTS)
    logger._log_to_console_and_log_file("Activity Table starts loading with the Alert activities only")
    # Loop to upload the list of firmware bundles
    count_fail = 0
    for actname in activities:
        actname.name = actname.name.strip()
        if re.match('^#\d+$', actname.name):
            line_no = actname.name.replace('#', '')
            XPATH_ACTIVITY_SELECT = FusionActivityPage.ID_SELECT_ACTIVITY_BY_ID % line_no
            if ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_ITME_SPAN % XPATH_ACTIVITY_SELECT):
                time.sleep(5)
                actname.name = selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_ITME_SPAN_S1 % XPATH_ACTIVITY_SELECT)
                if ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_ITEM_SPAN_A % XPATH_ACTIVITY_SELECT):
                    actname.name = actname.name + selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_ITEM_SPAN_A % XPATH_ACTIVITY_SELECT)
                if ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_ITEM_SPAN_S2 % XPATH_ACTIVITY_SELECT):
                    actname.name = actname.name + selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_ITEM_SPAN_S2 % XPATH_ACTIVITY_SELECT)
            else:
                actname.name = selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_ITEM_P1 % XPATH_ACTIVITY_SELECT)
        else:
            XPATH_ACTIVITY_SELECT = FusionActivityPage.ID_ACTIVITY_SELECT % (actname.name, actname.resource, actname.date)

        if ui_lib.wait_for_element_visible(XPATH_ACTIVITY_SELECT, PerfConstants.LOAD_ALERT_ACTIVITY):
            ui_lib.wait_for_element_and_click(XPATH_ACTIVITY_SELECT, PerfConstants.DEFAULT_SYNC_TIME)
            activity_state = selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_STATE % (XPATH_ACTIVITY_SELECT))
            if activity_state == "Cleared":
                logger._log_to_console_and_log_file("The Activity : '" + actname.name + "' is already cleared")
                continue
            ui_lib.wait_for_element_and_click(FusionActivityPage.ID_ACTION_DROPDOWN, PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTION_DROPDOWN_CLEAR, PerfConstants.DEFAULT_SYNC_TIME)
            selenium2lib.click_element(FusionActivityPage.ID_ACTION_DROPDOWN_CLEAR)
            if ui_lib.wait_for_element_visible(FusionActivityPage.ID_CLEAR_ERROR_MSG, PerfConstants.DEFAULT_SYNC_TIME):
                ui_lib.wait_for_element_visible(FusionActivityPage.ID_CLEAR_ERROR_OK, PerfConstants.DEFAULT_SYNC_TIME)
                selenium2lib.click_element(FusionActivityPage.ID_CLEAR_ERROR_OK)
                ui_lib.wait_for_element_and_click(XPATH_ACTIVITY_SELECT, PerfConstants.DEFAULT_SYNC_TIME)
                activity_state = selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_STATE % (XPATH_ACTIVITY_SELECT))
                if activity_state == "Cleared":
                    logger._log_to_console_and_log_file("The Activity : '" + actname.name + "' is already cleared")
                else:
                    logger._warn(" The Activity : '" + actname.name + "' selected cannot be Cleared and holds the state : '" + activity_state + "' as the activity may be Tasks and not the Alerts")
                    selenium2lib.capture_page_screenshot()
                    count_fail += 1
            elif ui_lib.wait_for_element_visible(XPATH_ACTIVITY_SELECT, PerfConstants.LOAD_ALERT_ACTIVITY):
                ui_lib.wait_for_element_and_click(XPATH_ACTIVITY_SELECT, PerfConstants.DEFAULT_SYNC_TIME)
                activity_state = selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_STATE % (XPATH_ACTIVITY_SELECT))
                if activity_state == "Cleared":
                    logger._log_to_console_and_log_file("The Activity : '" + actname.name + "' is cleared")
                else:
                    logger._warn("The Activity : '" + actname.name + "' selected cannot be Cleared and holds the state : '" + activity_state + "' as the activity may be Tasks and not the Alerts")
                    selenium2lib.capture_page_screenshot()
                    count_fail += 1
        else:
            logger._warn("The Activity : '" + actname.name + "' is not existing in the activity page And/or the Activity may be Tasks and not the Alerts")
            selenium2lib.capture_page_screenshot()
            count_fail += 1
    if count_fail > 0:
        return False
    else:
        return True


def restore_activity(*activities):
    # Assigning user to the activity
    logger._log_to_console_and_log_file("Restoring the state of the Activity starts..")
    selenium2lib = ui_lib.get_s2l()

    # Loads the value from the test data
    if isinstance(activities, test_data.DataObj):
        activities = [activities]
    elif isinstance(activities, tuple):
        activities = list(activities[0])

    ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_TABLE, PerfConstants.DEFAULT_SYNC_TIME)
    logger._log_to_console_and_log_file("Activity Table is loaded with the activities.")
    if not ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_ALL_TYPES, PerfConstants.DEFAULT_SYNC_TIME):
        ui_lib.wait_for_element_and_click(FusionActivityPage.ID_RESET_FILTER)
    ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_ALL_TYPES, PerfConstants.DEFAULT_SYNC_TIME)
    selenium2lib.click_element(FusionActivityPage.ID_FILTER_ALL_TYPES)
    ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_ALERTS, PerfConstants.DEFAULT_SYNC_TIME)
    selenium2lib.click_element(FusionActivityPage.ID_FILTER_ALERTS)
    logger._log_to_console_and_log_file("Activity Table starts loading with the Alert activities only")
    # Loop to upload the list of firmware bundles
    for actname in activities:
        actname.name = actname.name.strip()
        if re.match('^#\d+$', actname.name):
            line_no = actname.name.replace('#', '')
            XPATH_ACTIVITY_SELECT = FusionActivityPage.ID_SELECT_ACTIVITY_BY_ID % line_no
            if ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_ITME_SPAN % XPATH_ACTIVITY_SELECT):
                time.sleep(5)
                actname.name = selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_ITME_SPAN_S1 % XPATH_ACTIVITY_SELECT)
                if ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_ITEM_SPAN_A % XPATH_ACTIVITY_SELECT):
                    actname.name = actname.name + selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_ITEM_SPAN_A % XPATH_ACTIVITY_SELECT)
                if ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_ITEM_SPAN_S2 % XPATH_ACTIVITY_SELECT):
                    actname.name = actname.name + selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_ITEM_SPAN_S2 % XPATH_ACTIVITY_SELECT)
            else:
                actname.name = selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_ITEM_P1 % XPATH_ACTIVITY_SELECT)
        else:
            XPATH_ACTIVITY_SELECT = FusionActivityPage.ID_ACTIVITY_SELECT % (actname.name, actname.resource, actname.date)
        if ui_lib.wait_for_element_visible(XPATH_ACTIVITY_SELECT, PerfConstants.LOAD_ALERT_ACTIVITY):
            ui_lib.wait_for_element_and_click(XPATH_ACTIVITY_SELECT, PerfConstants.DEFAULT_SYNC_TIME)
            activity_state = selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_STATE % (XPATH_ACTIVITY_SELECT))
            if activity_state == "Active":
                logger._log_to_console_and_log_file("The Activity : '" + actname.name + "' is already Restored and is in the 'Active' State")
                continue
            ui_lib.wait_for_element_and_click(FusionActivityPage.ID_ACTION_DROPDOWN, PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTION_DROPDOWN_RESTORE, PerfConstants.DEFAULT_SYNC_TIME)
            selenium2lib.click_element(FusionActivityPage.ID_ACTION_DROPDOWN_RESTORE)
            if ui_lib.wait_for_element_visible(FusionActivityPage.ID_RESTORE_ERROR_MSG, PerfConstants.DEFAULT_SYNC_TIME):
                ui_lib.wait_for_element_visible(FusionActivityPage.ID_RESTORE_ERROR_OK, PerfConstants.DEFAULT_SYNC_TIME)
                selenium2lib.click_element(FusionActivityPage.ID_RESTORE_ERROR_OK)
                ui_lib.wait_for_element_and_click(XPATH_ACTIVITY_SELECT, PerfConstants.DEFAULT_SYNC_TIME)
                activity_state = selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_STATE % (XPATH_ACTIVITY_SELECT))
                if activity_state == "Active":
                    logger._log_to_console_and_log_file("The Activity : '" + actname.name + "' is already Restored and is in the 'Active' State")
                else:
                    logger._warn(" The Activity : '" + actname.name + "' selected cannot be Restored and holds the state : '" + activity_state + "' as the activity may be Tasks and not the Alerts")
            elif ui_lib.wait_for_element_visible(XPATH_ACTIVITY_SELECT, PerfConstants.LOAD_ALERT_ACTIVITY):
                ui_lib.wait_for_element_and_click(XPATH_ACTIVITY_SELECT, PerfConstants.DEFAULT_SYNC_TIME)
                activity_state = selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_STATE % (XPATH_ACTIVITY_SELECT))
                if activity_state == "Active":
                    logger._log_to_console_and_log_file("The Activity : '" + actname.name + "' is Restored back to 'Active' State")
                else:
                    logger._warn(" The Activity : '" + actname.name + "' selected cannot be Restored and holds the state : '" + activity_state + "' as the activity may be Tasks and not the Alerts")
        else:
            logger._warn("The Activity : '" + actname.name + "' is not existing in the activity page And/or the Activity may be Tasks and not the Alerts")


def _assignuser_name(actname, resource, timestamp, assignusername):
    """ This function is to assign the user to the given activity.
    This function is written wrt E2E UC3.it will work only when we pass all the four parameters.
        Example:
        _assignuser_name('Update started for interconnect CC-2-LI', 'CC-2-LI', 'Today 10.45 am', 'NetAdmin')
    """
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionActivityPage.ID_PAGE_LABEL):
        navigate()

    ui_lib.wait_for_element_and_click(FusionActivityPage.ID_SELECT_ACTIVITY_OWNER % (actname, resource, timestamp))
    ui_lib.wait_for_element(FusionActivityPage.ID_ACTION_DROPDOWN, PerfConstants.DEFAULT_SYNC_TIME)
    ui_lib.wait_for_element_and_click(FusionActivityPage.ID_ACTION_DROPDOWN, PerfConstants.DEFAULT_SYNC_TIME)
    ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTION_DROPDOWN_ASSIGN, PerfConstants.DEFAULT_SYNC_TIME)
    selenium2lib.click_element(FusionActivityPage.ID_ACTION_DROPDOWN_ASSIGN)
    if not selenium2lib._is_element_present(FusionActivityPage.ID_ASSIGN_ERROR_MSG):
        selenium2lib.input_text(FusionActivityPage.ID_ASSIGN_UN_INPUT_BOX, assignusername)
        ui_lib.wait_for_element_visible(FusionActivityPage.ID_ASSIGN_OK, PerfConstants.DEFAULT_SYNC_TIME)
        selenium2lib.click_element(FusionActivityPage.ID_ASSIGN_OK)
        ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_TABLE, PerfConstants.ASSIGN_USER_TIME)
        logger._log_to_console_and_log_file("The Activity : '" + actname + "' selected is assigned to : '" + assignusername)
    elif ui_lib.wait_for_element_visible(FusionActivityPage.ID_ASSIGN_ERROR_MSG, PerfConstants.DEFAULT_SYNC_TIME):
        ui_lib.wait_for_element_visible(FusionActivityPage.ID_ASSIGN_ERROR_OK, PerfConstants.DEFAULT_SYNC_TIME)
        selenium2lib.click_element(FusionActivityPage.ID_ASSIGN_ERROR_OK)
        logger._warn("The Activity : '" + actname + "' selected not able to assigned to : '" + assignusername)


def _verify_activity_owner(actname, resource, timestamp, assignusername):
    """ This function is to verify the user name once the activity is assigned to any user.
    This function is written wrt E2E UC3.it will work only when we pass all the four parameters.
        Example:
        _verify_activity_owner('Update started for interconnect CC-2-LI', 'CC-2-LI', 'Today 10.45 am', 'NetAdmin')
    """
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionActivityPage.ID_PAGE_LABEL):
        selenium2lib.click_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL)
        ui_lib.wait_for_element_visible(FusionUIBaseElements.ID_MENU_LINK_ACTIVITY, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_MENU_LINK_ACTIVITY)
        ui_lib.wait_for_element_visible(FusionActivityPage.ID_PAGE_LABEL)

        actavailable = _is_element_present_activity_page_without_time(actname, resource)
        if actavailable:
            assignuser_name = selenium2lib.get_text(FusionActivityPage.ID_ASSIGNED_OWNER % (actname, resource, timestamp))
            if assignuser_name == assignusername:
                logger._log_to_console_and_log_file("Activity is available with assigned user name only")
            else:
                logger._warn("Activity is not available with assigned user name")
        else:
            logger._warn("Assigned activity is not visible to this user %s" % assignusername)


def _is_element_present_activity_page_without_time(elementtocheck, message):
    """ This function is to verify the activity in activity page.
    This function is written wrt E2E UC3.it will work only when we pass all the two parameters.
        Example:
        _is_element_present_activity_page_without_time('Firmware Update success', 'CC-2-LI')
    """
    selenium2lib = ui_lib.get_s2l()
    ui_lib.wait_for_element_visible(FusionActivityPage.ID_MSG_AVAILABLE % (elementtocheck, message), PerfConstants.PROFILE_POWER_VALIDATION)
    if selenium2lib._is_element_present(FusionActivityPage.ID_MSG_AVAILABLE % (elementtocheck, message)):
        logger._log_to_console_and_log_file("'%s' is present in Activity page" % elementtocheck)
        return True
    else:
        logger._warn("'%s' is not present in Activity page" % elementtocheck)
        selenium2lib.capture_page_screenshot()
        return False


def verify_alert_page_details(activityname, resource, owner):
    """
        This function is to verify activity page details.
        Example:
        verify_alert_page_details()
    """
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionActivityPage.ID_PAGE_LABEL):
        navigate()

    """  Validating activity fields like Name, Resource, Time, State and user      """
    item_min_val = 3
    item_max_val = 8
    statelist = ['Active', 'Locked', 'Cleared', 'Pending', 'Running', 'Completed', 'Interrupted', 'Error', 'Warning']

    ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_TABLE, PerfConstants.DEFAULT_SYNC_TIME)
    logger._log_to_console_and_log_file("Activity Table is loaded with the activities.")
    if not ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_ALL_TYPES, PerfConstants.DEFAULT_SYNC_TIME):
        ui_lib.wait_for_element_and_click(FusionActivityPage.ID_RESET_FILTER)
    ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_ALL_TYPES, PerfConstants.DEFAULT_SYNC_TIME)

    selenium2lib.click_element(FusionActivityPage.ID_FILTER_ALL_TYPES)
    ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_TASKS, PerfConstants.DEFAULT_SYNC_TIME)
    selenium2lib.click_element(FusionActivityPage.ID_FILTER_TASKS)

    logger._log_to_console_and_log_file("Validating activity details")
    for intcount in range(item_min_val, item_max_val):
        if intcount == 3:
            ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_DETAILS % intcount, PerfConstants.DEFAULT_SYNC_TIME)
            logger._log_to_console_and_log_file("Validating Activity name")
            if selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_DETAILS % intcount) == activityname:
                logger._log_to_console_and_log_file("Activity has proper name i.e : '%s'" % activityname)
        elif intcount == 4:
            ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_DETAILS % intcount, PerfConstants.DEFAULT_SYNC_TIME)
            logger._log_to_console_and_log_file("Validating Activity resource")
            if selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_DETAILS % intcount) == resource:
                logger._log_to_console_and_log_file("Activity has proper resource i.e : '%s'" % resource)
        elif intcount == 5:
            ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_DETAILS % intcount, PerfConstants.DEFAULT_SYNC_TIME)
            logger._log_to_console_and_log_file("Validating Activity Date")
            logger._log_to_console_and_log_file(selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_DETAILS % intcount))
        elif intcount == 6:
            ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_DETAILS % intcount, PerfConstants.DEFAULT_SYNC_TIME)
            logger._log_to_console_and_log_file("Validating Activity State")
            activity_state = str(selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_DETAILS % intcount))
            state_count = 0
            for state_count in range(0, len(statelist)):
                if activity_state.find(statelist[state_count]) > -1:
                    logger._log_to_console_and_log_file("Activity state '%s' returned is expected one" % statelist[state_count])
                    break
        elif intcount == 7:
            ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_DETAILS % intcount, PerfConstants.DEFAULT_SYNC_TIME)
            logger._log_to_console_and_log_file("Validating Activity assigned user")
            activity_user = str(selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_DETAILS % intcount))
            if activity_user.lower() == "unassigned" or activity_user.lower() == owner.lower():
                logger._log_to_console_and_log_file("Activity assigned user '%s' is as per expected" % activity_user)

    """ Filtering activities by State and validating the listed activities      """
    logger._log_to_console_and_log_file("Filtering activities by State")
    activity_state = ['Active', 'Locked', 'Cleared', 'Pending', 'Running', 'Completed', 'Interrupted', 'Error', 'Warning']
    state_order = 0
    for state_order in range(0, len(activity_state)):
        logger._log_to_console_and_log_file("Filtering alerts by status: '%s'" % activity_state[state_order])
        if not ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_ALL_STATES, PerfConstants.DEFAULT_SYNC_TIME):
            ui_lib.wait_for_element_and_click(FusionActivityPage.ID_RESET_FILTER)
        ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_ALL_STATES, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_and_click(FusionActivityPage.ID_FILTER_ALL_STATES)
        ui_lib.wait_for_element_and_click(FusionActivityPage.ID_FILTER_BY_STATE % activity_state[state_order])

        ui_lib.refresh_browser(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.BROWSER_REFRESH)
        ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_FILTER_COUNT, PerfConstants.DEFAULT_SYNC_TIME)
        acitivity_count = selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_FILTER_COUNT)
        status_count = 0
        if int(acitivity_count) > 6:
            for status_count in range(0, 6):
                ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_STATE_DETAILS % (status_count + 1), PerfConstants.DEFAULT_SYNC_TIME)
                state_ui = selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_STATE_DETAILS % (status_count + 1))
                if not ((state_ui.lower()).find(activity_state[state_order].lower())) == 0:
                    logger._warn("Listed activities for status filter '%s' in not as per expected" % activity_state[state_order])
                    break
            logger._log_to_console_and_log_file("Activities are filtered as per status filter: '%s' " % activity_state[state_order])
        elif int(acitivity_count) > 0 and int(acitivity_count) < 6:
            for status_count in range(0, int(acitivity_count)):
                ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_STATE_DETAILS % (status_count + 1), PerfConstants.DEFAULT_SYNC_TIME)
                state_ui = selenium2lib.get_text(FusionActivityPage.ID_ACTIVITY_STATE_DETAILS % (status_count + 1))
                if not (state_ui.lower() == activity_state[state_order].lower()):
                    logger._warn("Listed activities for status filter '%s' in not as per expected" % activity_state[state_order])
                    break
        else:
            logger._log_to_console_and_log_file("No activity available for the status: '%s'" % activity_state[state_order])


def change_activity_state_in_activity_page(activity_obj):
    """
    This function is to change activity state from 'active' to 'Cleared' State in Activity Page
    """
    if not ui_lib.wait_for_element(FusionActivityPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(activity_obj, test_data.DataObj):
        activity_obj = [activity_obj]
    elif isinstance(activity_obj, tuple):
        activity_obj = list(activity_obj)

    for activity in activity_obj:
        if not _is_element_present_activity_page_without_time(activity.name, activity.resource):
            logger._warn("Activity '{0}' is not present in appliance".format(activity.name))
            return False
        else:
            ui_lib.wait_for_element_visible(FusionActivityPage.ID_MSG_AVAILABLE % (activity.name, activity.resource) + "/descendant::div[@class='hp-state hp-select']", 20)
            ui_lib.wait_for_element_and_click(FusionActivityPage.ID_MSG_AVAILABLE % (activity.name, activity.resource) + "/descendant::div[@class='hp-state hp-select']")
            ui_lib.wait_for_element_and_click(FusionActivityPage.ID_MSG_AVAILABLE % (activity.name, activity.resource) + "/descendant::li[text()='Cleared']")
        if ui_lib.wait_for_element(FusionActivityPage.ID_MSG_AVAILABLE % (activity.name, activity.resource) + "/descendant::li[@class='hp-selected' and text()='Cleared']"):
            logger._log_to_console_and_log_file("Activity '{0}' state successfully changed to '{1}'".format(activity.name, activity.state))
            return True
        else:
            logger._warn("Failed to change activity '{0}' status to '{1}'".format(activity.name, activity.state))
            return False


def verify_alertpage_information(activity_obj):
    """
    This function is displays the critical Alerts with user provided state(Active or locked or cleared...). Then Verifies Alert name, Owner and Resource in displayed alerts
    in Activity Page
    """
    if not ui_lib.wait_for_element(FusionActivityPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(activity_obj, test_data.DataObj):
        activity_obj = [activity_obj]
    elif isinstance(activity_obj, tuple):
        activity_obj = list(activity_obj)

    err_val = 0

    ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_TABLE, PerfConstants.DEFAULT_SYNC_TIME)
    logger.info("Activity Table is loaded with the activities.")
    if not ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_ALL_TYPES, PerfConstants.DEFAULT_SYNC_TIME):
        ui_lib.refresh_browser(FusionBasePage.ID_MENU_ONE_VIEW, PerfConstants.DEFAULT_SYNC_TIME)
    ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_ALL_TYPES, PerfConstants.DEFAULT_SYNC_TIME)

    ui_lib.wait_for_element_and_click(FusionActivityPage.ID_FILTER_ALL_TYPES, PerfConstants.DEFAULT_SYNC_TIME)

    ui_lib.wait_for_element_and_click(FusionActivityPage.ID_FILTER_ON_TYPE, PerfConstants.DEFAULT_SYNC_TIME)
    # Clicking on Critical status
    ui_lib.wait_for_element_and_click(FusionActivityPage.ID_FILTER_ALL_STATUS, PerfConstants.DEFAULT_SYNC_TIME)
    ui_lib.wait_for_element_and_click(FusionActivityPage.ID_FILTER_ON_STATUSTYPE, PerfConstants.DEFAULT_SYNC_TIME)

    # Displays all critical alerts based on state
    activity_states = ['Active', 'Locked', 'Cleared', 'Pending', 'Running', 'Completed', 'Interrupted', 'Error', 'Warning']
    list_entries = []
    for activity in activity_obj:

        for order in range(0, len(activity_states)):
            if (activity_states[order] == activity.state):
                if order not in list_entries:
                    state = activity.state

                    no_of_alrets = display_alerts_on_activity_state(state)
                    error = validate_displayed_alert_info_on_activity_state(activity, no_of_alrets)
                    list_entries.append(order)
                else:
                    error = validate_displayed_alert_info_on_activity_state(activity, no_of_alrets)

        if (error > 0):
            err_val += 1

    if (err_val > 0):
        message = "One or more Alert validations failed"
        raise AssertionError(message)
    else:
        return True


def display_alerts_on_activity_state(state):

    logger.info("Filtering and displaying based on the Activity state i.e %s " % state)

    if not ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_STATES, PerfConstants.DEFAULT_SYNC_TIME):
        ui_lib.refresh_browser(FusionBasePage.ID_MENU_ONE_VIEW, PerfConstants.DEFAULT_SYNC_TIME)
    ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_STATES, PerfConstants.DEFAULT_SYNC_TIME)
    ui_lib.wait_for_element_and_click(FusionActivityPage.ID_FILTER_STATES, PerfConstants.DEFAULT_SYNC_TIME)
    ui_lib.wait_for_element_and_click(FusionActivityPage.ID_FILTER_STATES_ALL, PerfConstants.DEFAULT_SYNC_TIME)
    ui_lib.wait_for_element_and_click(FusionActivityPage.ID_FILTER_BY_STATE % state, PerfConstants.DEFAULT_SYNC_TIME)
    ui_lib.refresh_browser(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.BROWSER_REFRESH)
    ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_FILTER_COUNT, PerfConstants.DEFAULT_SYNC_TIME)
    activity_count = int(ui_lib.get_text(FusionActivityPage.ID_ACTIVITY_FILTER_COUNT, PerfConstants.DEFAULT_SYNC_TIME))
    logger.info("No of %s Alerts :%s" % (state, activity_count))
    for i in range(1, activity_count + 1):

        if i <= activity_count:

            ui_lib.wait_for_element_and_click(FusionActivityPage.ID_LABEL_PAGE_CLICK_ERROR % i, PerfConstants.DEFAULT_SYNC_TIME)

            if ui_lib.wait_for_element(FusionActivityPage.ID_LABEL_PAGE_ERROR % (i), PerfConstants.DEFAULT_SYNC_TIME):
                error_msg1 = ui_lib.get_text(FusionActivityPage.ID_LABEL_PAGE_ERROR % (i), PerfConstants.DEFAULT_SYNC_TIME)
            if ui_lib.wait_for_element(FusionActivityPage.ID_LABEL_PAGE_ERROR_FULL % (i + 1), PerfConstants.DEFAULT_SYNC_TIME):
                error_msg2 = ui_lib.get_text(FusionActivityPage.ID_LABEL_PAGE_ERROR_FULL % (i + 1), PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_element_and_click(FusionActivityPage.ID_LABEL_EVENT_CLICK_ERROR % (i + 1), PerfConstants.DEFAULT_SYNC_TIME)
            event_msg = ui_lib.get_text(FusionActivityPage.ID_EVENT_MESSAGE % (i + 1), PerfConstants.DEFAULT_SYNC_TIME)
            logger.info("---------------------------------------\n")
            logger.info("%d. Alert: %s \n" % (i, error_msg1))
            logger.info("%s \n" % error_msg2)
            logger.info("%s \n" % event_msg)
            logger.info("---------------------------------------\n")
            ui_lib.wait_for_element_and_click(FusionActivityPage.ID_LABEL_EVENT_CLICK_ERROR % (i + 1), PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_element_and_click(FusionActivityPage.ID_LABEL_PAGE_UNCLICK_ERROR % i, PerfConstants.DEFAULT_SYNC_TIME)

    return activity_count


def validate_displayed_alert_info_on_activity_state(activity, count):
    """ After the display, Validating activity page fields like Name, Resource, Time, State and user  """

    logger.info("Validating the alert information")
    valid_name = 0
    valid_resource = 0
    valid_owner = 0
    activity_count = count
    # This is index position in Activity page table
    index = 3
    error = 0
    '''
    Previous function captures and displays all critical alerts based on activity state driven in data file. In captured alerts it checks whether data driven alert name
    is present or not, If yes, valid owner and resource is present or not.
    '''
    if (activity_count != 0):
        # looping here to check valid alert present or not in displayed critical alerts based on activity state .If present set valid_name bit to 1. Similar way it sets valid_owner, valid_resource also...
        for i in range(1, activity_count + 1):

            if i <= activity_count:
                if(activity.has_property("name")):
                    if compare_name(i, activity):
                        valid_name = 1
                    else:
                        error += 1

                if(activity.has_property("resource")):
                    if compare_resource(i, activity):
                        valid_resource = 1
                    else:
                        error += 1

                if(activity.has_property("owner")):
                    if compare_owner(i, activity):
                        valid_owner = 1
                    else:
                        error += 1
        '''
        After bit set, Here it checks and displays to console everything is matched as per data file or not. If anything is wrong from
        data file displays the same on console...
        '''
        if error >= 0:
            if(activity.has_property("name")):
                if (valid_name == 0):
                    logger._warn("Failed to validate the Activity name")
                    logger._warn("Activity Name from data file : %s " % (activity.name))

                else:
                    logger.info("Validation of expected alert is successful : %s" % (activity.name))

            if(activity.has_property("resource") and valid_name > 0):
                if (valid_resource > 0):
                    logger.info("Validation of expected resource for above alert is successful : %s" % (activity.resource))

                else:
                    logger._warn("Failed to validate the Activity resource")
                    logger._warn(" Resource from data file: %s" % (activity.resource))

            if(activity.has_property("owner") and valid_name > 0):
                if (valid_owner > 0):
                    logger.info("Validation of expected owner for above alert is successful : %s" % (activity.owner))

                else:
                    logger._warn("Failed to validate the Activity assigned user")
                    logger._warn("Owner from data file %s" % (activity.owner))
    else:
        logger.info("No %s Alerts present in Activity page" % activity.state)
        logger.info("But Alert present in Data file is %s" % activity.name)

    return error


def compare_name(loop_cnt, activity):
    '''Compares the Activity name'''

    if ui_lib.wait_for_element(FusionActivityPage.ID_ACTIVITY_NAME_DETAILS % (loop_cnt), PerfConstants.DEFAULT_SYNC_TIME):

        if ui_lib.get_text(FusionActivityPage.ID_ACTIVITY_NAME_DETAILS % (loop_cnt), PerfConstants.DEFAULT_SYNC_TIME) == activity.name:

            return True
        else:
            return False


def compare_resource(loop_cnt, activity):
    '''For particular Activity name, checks Resource field correct or not'''
    if ui_lib.wait_for_element(FusionActivityPage.ID_ACTIVITY_SOURCE_DETAILS % (loop_cnt), PerfConstants.DEFAULT_SYNC_TIME):

        if ui_lib.get_text(FusionActivityPage.ID_ACTIVITY_SOURCE_DETAILS % (loop_cnt), PerfConstants.DEFAULT_SYNC_TIME) == activity.resource:

            return True
        else:
            return False


def compare_owner(loop_cnt, activity):
    '''For particular Activity name, checks Owner field is correct or not'''
    if ui_lib.wait_for_element(FusionActivityPage.ID_ACTIVITY_OWNER_DETAILS % (loop_cnt), PerfConstants.DEFAULT_SYNC_TIME):

        activity_user = str(ui_lib.get_text(FusionActivityPage.ID_ACTIVITY_OWNER_DETAILS % (loop_cnt), PerfConstants.DEFAULT_SYNC_TIME))
        if activity_user.lower() == "unassigned" or activity_user.lower() == activity.owner.lower():
            return True
        else:
            return False


def get_latest_activity():
    """
    This function gets the message of activities and returns
    in Activity Page and returns it to script
    """
    if not ui_lib.wait_for_element(FusionActivityPage.ID_PAGE_LABEL):
        navigate()
    return CommonOperationActivity.get_latest_activity()

"""
    Reports page.
"""

from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from RoboGalaxyLibrary.keywords.native import NativeOsKeywords
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.general.reports_elements import FusionReportsPage
from FusionLibrary.ui.general import activity
from FusionLibrary.ui.business_logic.general.activity_elements import FusionActivityPage
from FusionLibrary.ui.business_logic.base import FusionUIBase, SectionType
import os
from datetime import datetime


def navigate():
    FusionUIBase.navigate_to_section(SectionType.REPORTS)


def export_and_verify_inventory_reports(inventory_path, inventory_name):
    """ Export and verify the inventory reports
        Exports the inventory and verifies the file at destination
    Example:
    |    Fusion UI Export And Verify Inventory Reports    |    ${inventory_path}    |    ${inventory_name}
    """

    s2l = ui_lib.get_s2l()
    if not s2l._is_element_present(FusionReportsPage.ID_PAGE_LABEL):
        navigate()

    logger._log_to_console_and_log_file("Create inventory")
    # CODE TO CREATE DOWNLOAD DIRECTORY AND DELETE FILES INSIDE, IF DIRECTORY EXISTS
    if not os.path.exists(inventory_path):
        os.makedirs(inventory_path)
    for root, dirs, files in os.walk(inventory_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    ui_lib.wait_for_element_and_click(FusionReportsPage.ID_SELECT_INVENTORY_NAME % (inventory_name), PerfConstants.DEFAULT_SYNC_TIME)
    s2l.click_element(FusionReportsPage.ID_MENU_ACTION_BTN)
    s2l.click_element(FusionReportsPage.ID_MENU_ACTION_SAVE_AS)
    ui_lib.wait_for_element_and_click(FusionReportsPage.ID_BTN_SAVE_AS_OK, PerfConstants.DEFAULT_SYNC_TIME)

    logger._log_to_console_and_log_file("Save the inventory to the specified folder path")
    BuiltIn().sleep(5)
    window_name = "Opening"    # Name of the Window
    NativeOsKeywords().find_native_window(window_name)
    NativeOsKeywords().send_keys_to_native_window(window_name, "{DOWN}")
    NativeOsKeywords().send_keys_to_native_window(window_name, "{ENTER}")
    # ui_lib.MyLib().handle_windows(windowname, keys)
    # while os.listdir(inventory_path) == []:
    BuiltIn().sleep(2)
    # CODE TO WAIT TILL THE DOWNLOAD IS IN PROGRESS
    for files in os.listdir(inventory_path):
        filesize = os.path.getsize(os.path.join(inventory_path, files))
        logger._log_to_console_and_log_file("initial file size %s" % filesize)
        finalfilesize = 0
        start = datetime.now()
        while filesize != finalfilesize:
            BuiltIn().sleep(1)
            if not os.path.exists(os.path.join(inventory_path, files)):
                files = files.split(".part")[0]
            finalfilesize = os.path.getsize(os.path.join(inventory_path, files))
            if(datetime.now() - start).total_seconds() > PerfConstants.DOWNLOAD_BACKUP_TIMEOUT:
                if finalfilesize == 0:
                    logger._warn("final file size is 0, inventory with no data is created")
                else:
                    logger._log_to_console_and_log_file("final file size %s" % finalfilesize)
                    return False
                    break
    ui_lib.wait_for_element_and_click(FusionReportsPage.ID_SELECT_INVENTORY_NAME % (inventory_name), PerfConstants.DEFAULT_SYNC_TIME)
    return True


def verify_reports_page_alerts_data_against_activity_page():
    """
        Verifies the alerts data present in reports and activity page are same or not
        Example:
        |Fusion UI Verify Alerts Data Against Activity Page|
    """

    s2l = ui_lib.get_s2l()
    # Navigate to Reports page
    if not navigate():
        ui_lib.fail_test("Fail: failed to navigate reports page")

    report_page_alert_details = []
    fail_count = 0

    if not ui_lib.wait_for_element_visible(FusionReportsPage.ID_ELEMENT_ALERTS_TITLE):
        ui_lib.wait_for_element_and_click(FusionReportsPage.ID_ELEMENT_ACTIVE_ALERTS)

    ui_lib.wait_for_element_visible(FusionReportsPage.ID_TABLE_REPORT_RESOURCES)
    alerts_list = [ui_lib.get_text(el) for el in s2l._element_find(FusionReportsPage.ID_ACTIVE_ALERTS_LIST, False, False)]

    # capturing alert details from reports page
    for index in range(1, len(alerts_list)):
        report_page_alert_details.append(_report_page_alert_dateils(index))

    # Removing repeated alerts
    for j in report_page_alert_details:
        count = 0
        for i in report_page_alert_details:
            if j['name'] == i['name'] and j['resource'] == i['resource']:
                count = count + 1
                if count > 1:
                    report_page_alert_details.remove(i)

    # Navigating to Activity page
    if not ui_lib.wait_for_element_visible(FusionActivityPage.ID_PAGE_LABEL):
        activity.navigate()

    # Filtering active alerts
    logger._log_to_console_and_log_file("Activity Table starts loading with the Alert activities only")
    if ui_lib.wait_for_element_visible(FusionActivityPage.ID_RESET_FILTER):
        ui_lib.wait_for_element_and_click(FusionActivityPage.ID_RESET_FILTER)

    if not ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_ALL_TYPES, PerfConstants.DEFAULT_SYNC_TIME):
        ui_lib.refresh_browser(FusionUIBaseElements.ID_MENU_ONE_VIEW, PerfConstants.DEFAULT_SYNC_TIME)
    ui_lib.wait_for_element_visible(FusionActivityPage.ID_FILTER_ALL_TYPES, PerfConstants.DEFAULT_SYNC_TIME)
    ui_lib.wait_for_element_and_click(FusionActivityPage.ID_FILTER_ALL_TYPES)
    ui_lib.wait_for_element_and_click(FusionActivityPage.ID_FILTER_ALERTS, PerfConstants.DEFAULT_SYNC_TIME)

    logger._log_to_console_and_log_file("Filtering alerts by status: 'Active' and 'Locked'")
    ui_lib.wait_for_element_and_click(FusionActivityPage.ID_FILTER_ALL_STATES)
    ui_lib.wait_for_element_and_click(FusionActivityPage.ID_FILTER_BY_STATE % "Active")
    ui_lib.wait_for_element_and_click(FusionActivityPage.ID_FILTER_BY_STATE % "Locked")
    ui_lib.refresh_browser(FusionUIBaseElements.ID_MENU_ONE_VIEW, PerfConstants.DEFAULT_SYNC_TIME)

    for item in report_page_alert_details:
        severity = item["severity"].lower()
        name = item["name"].split('[')[0]
        resource = item["resource"]
        resource_type = item["resource_type"].replace('-', ' ')
        resolution = item["resolution"]

        alert = FusionActivityPage.ID_ELEMENT_ALERT % (severity, name, resource)
        if ui_lib.wait_for_element_visible(alert):
            ui_lib.wait_for_element_and_click(alert + "/td[1]/div")
            if not ui_lib.wait_for_element(FusionReportsPage.ID_ELEMENT_CORRECTIVEACTION):
                ui_lib.wait_for_element_and_click(FusionReportsPage.ID_ELEMENT_EVENT_DETAILS)
            alert_resolution = ui_lib.get_text(FusionReportsPage.ID_ELEMENT_RESOLUTION)
            alert_resource_type = ui_lib.get_text(alert + "/td[4]/span")
            ui_lib.wait_for_element_and_click(alert + "/td[1]/div")
            if alert_resource_type.title() != resource_type.title():
                logger._warn("Fail: Hardware type of alert '{0}' is mismatching".format(name))
                fail_count += 1
                continue
            if resolution != alert_resolution:
                logger._warn("Fail: Corrective action for alert '{0}' is mismatching".format(name))
                fail_count += 1
                continue
        else:
            logger._log_to_console_and_log_file("Failed to select alert: %s".format(alert))
            fail_count += 1

    if fail_count == 0:
        logger._log_to_console_and_log_file("SUCESS: Data present in reports page and activity page for alerts is same")
        return True
    else:
        ui_lib.fail_test("FAIL: '{0}' alerts data is mismatching from reports and activity page" .format(fail_count))


def _report_page_alert_dateils(index):
    alert_details = {}
    alert_details["severity"] = ui_lib.get_text(FusionReportsPage.ID_ACTIVE_ALERT_DETAILS % index + "/td[2]")
    if alert_details["severity"] == "Critical":
        alert_details["severity"] = "error"
    alert_details["name"] = ui_lib.get_text(FusionReportsPage.ID_ACTIVE_ALERT_DETAILS % index + "/td[5]")
    alert_details["resolution"] = ui_lib.get_text(FusionReportsPage.ID_ACTIVE_ALERT_DETAILS % index + "/td[9]")
    alert_details["resource"] = ui_lib.get_text(FusionReportsPage.ID_ACTIVE_ALERT_DETAILS % index + "/td[6]")
    alert_details["resource_type"] = ui_lib.get_text(FusionReportsPage.ID_ACTIVE_ALERT_DETAILS % index + "/td[7]")
    return alert_details

# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Interconnects Page
"""

from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.data import test_data
from FusionLibrary.ui.business_logic.base import SectionType
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.servers import enclosures
from FusionLibrary.ui.servers import serverprofiles
from FusionLibrary.ui.networking import networks
from FusionLibrary.ui.servers.enclosures_elements import FusionEnclosuresPage
from FusionLibrary.ui.usersandgroups.usersandgroups_elements import FusionUserandGroupsPage
from RoboGalaxyLibrary.cli.blade_info import blade_info
from RoboGalaxyLibrary.utilitylib import logging
from FusionLibrary.ui.business_logic.servers.enclosures import _BaseCommonOperationEnclosures
from FusionLibrary.ui.business_logic.servers.enclosures import TBirdVerifyEnclosures
from FusionLibrary.ui.business_logic.networking.interconnects import *
from FusionLibrary.ui.business_logic.networking.interconnects import EditScopeForInterconnect, _BaseEditScopeForInterconnect
from FusionLibrary.ui.business_logic.usersandgroups.usersandgroups import GeneralUserandGroups
from FusionLibrary.cli.em import em_operation
import sys
import paramiko
import re
import time

# import pysftp


def navigate():
    FusionUIBase.navigate_to_section(SectionType.INTERCONNECTS)


def get_data_from_switch(switch_ip, commands, uname, pwd):
    ''' This Function logs into the switch and runs the commands passed. Commands here is a list of commands.
        The output will be a list of the return value and return code after command execution in the same order
        that the commands were passed '''

    logging._info("\nConnecting to %s and run command %s" % (switch_ip, commands))
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    port = 22
    errorcodelist = []
    datalist = []
    logging._info("Password is %s" % pwd)
    client.connect(switch_ip, port=port, username=uname, password=pwd)
    i = 0
    for command in commands:
        print "executing command %s" % command
        input, output, error = client.exec_command(command)
        errorcodelist.insert(i, output.channel.recv_exit_status())
        datalist.insert(i, output.read())
        i = i + 1
    return (datalist, errorcodelist)


def validate_c7000_pause_flood_alert(alert_message, interconnect_obj):
    """
        This function verifies the pause flood alert on the interconnect page. If  port or Interconnect
        status is red or warning, captures Alerts present in activity page and validates the same.

        * required arguments:
        <interconnects>
            <interconnect name="VC-CRM1, interconnect 1"  enclosure="VC-CRM1" activity="">
                <activity state ="Active" />
            </interconnect>
        </interconnects>
    """
    error = 0

    error_string = []
    FusionUIBase.navigate_to_section(SectionType.INTERCONNECTS)
    for interconnect in interconnect_obj:
        alert_msgs = []
        # select the given interconnect

        if not VerifyInterconnects.verify_interconnect_exist(interconnect.name, timeout=5, fail_if_false=False):
            logger.warn("interconnect '%s' does not exist" % interconnect.name)

            continue

        CommonOperationInterconnects.click_interconnect(interconnect.name, timeout=5)

        logger.info("Expected Alert message is: %s" % alert_message)
        alert_msgs.append(alert_message)
        # Function to capture the alerts present in Activity Page
        if not _capture_alerts(interconnect, alert_msgs, 15):
            error += 1
            error_string.append("Pause Flood Alert validation failed for interconnect:{}".format(interconnect.name))

    if error > 0:
        return FusionUIBase.fail_test_or_return_false("Either interconnect state is ok or Pause Flood Alert validation failed", False)
    else:
        return True


def edit_interconnect(*interconnect_obj):
    """ edit_interconnect
        Example:
        | `Edit Interconnect`      |     |
    """
    """below part of checking for single/multiple/named instance is yet to be implemented"""
    if isinstance(interconnect_obj, test_data.DataObj):
        interconnect_obj = [interconnect_obj]
    elif isinstance(interconnect_obj, tuple):
        interconnect_obj = list(interconnect_obj[0])
    fail_time = 0
    for interconnect in interconnect_obj:
        if not select_interconnect(interconnect.name):
            logger.warn("Exiting Edit Interconnect Function, Not selected Interconnect %s" % interconnect.name)
            fail_time += 1
            continue
        EditInterconnects.select_actions_edit()
        EditInterconnects.wait_edit_interconnect_dialog_shown()
        # CODE TO EDIT UPLINK PORTS AND DOWNLINK PORTS OF INTERCONNECTS
        if not EditInterconnects.wait_edit_interconnect_dialog_shown(5, False):
            logger.info("dint open the edit interconnects page even after clicking edit button")
            fail_time += 1
        else:
            EditInterconnects.wait_edit_interconnect_uplink_ports_load()
            EditInterconnects.wait_edit_interconnect_downlink_ports_load()
            if interconnect.UplinkPortstoCheck != '':
                EditInterconnects.select_interconnect_uplink_ports()
                UplinkList = interconnect.UplinkList.split(',')
                UplinkPortstoCheck = interconnect.UplinkPortstoCheck.split(',')
                for Uplink in UplinkList:
                    if Uplink in UplinkPortstoCheck:
                        EditInterconnects.tick_enable_uplink_ports(Uplink)
                    else:
                        EditInterconnects.untick_enable_uplink_ports(Uplink)
            else:
                logger.info("No Uplink ports are selected to edit for the interconnect %s" % interconnect.name)
            if interconnect.DownlinkportstoCheck != '':
                EditInterconnects.select_interconnect_downlink_ports()
                DownlinkList = interconnect.DownlinkList.split(',')
                DownlinkportstoCheck = interconnect.DownlinkportstoCheck.split(',')
                for Downlink in DownlinkList:
                    if Downlink in DownlinkportstoCheck:
                        EditInterconnects.tick_enable_downlink_ports(Downlink)
                    else:
                        EditInterconnects.untick_enable_downlink_ports(Downlink)
            else:
                logger.info("No Downlink ports are selected to edit for the interconnect %s" % interconnect.name)
            EditInterconnects.click_ok_button()
            EditInterconnects.wait_edit_interconnect_dialog_disappear()
            FusionUIBase.show_activity_sidebar()
            if CommonOperationInterconnects.wait_activity_action_ok(interconnect.name, "Update interconnects", 60, False):
                logger.info("The interconnect is edited successfully %s" % interconnect.name)
                # return False
            else:
                logger.warn("The interconnect is not edited successfully %s" % interconnect.name)
                fail_time += 1
    if fail_time > 0:
        return False
    else:
        return True


def power_on_interconnect(*interconnect_obj):
    """ power_on_interconnect
        Example:
        | `Power On Interconnect`      |     |
    """
    """below part of checking for single/multiple/named instance is yet to be implemented"""
    if isinstance(interconnect_obj, test_data.DataObj):
        interconnect_obj = [interconnect_obj]
    elif isinstance(interconnect_obj, tuple):
        interconnect_obj = list(interconnect_obj[0])

    fail_time = 0
    for interconnect in interconnect_obj:
        if not select_interconnect(interconnect.name):
            logger.warn("Exiting Power On Interconnect Function, Not selected Interconnect %s" % interconnect.name)
            fail_time += 1
            continue

        if not VerifyInterconnects.verify_overview_power_off(fail_if_false=False):
            logger.info("the interconnect %s is not in power-off status" % interconnect.name)
            fail_time += 1

        else:
            PowerOnInterconnects.select_actions_power_on()
            if not PowerOnInterconnects.wait_power_on_ok(interconnect.name):
                fail_time += 1
                logger.warn("The interconnect cannot be powered on %s" % interconnect.name)
                continue
            FusionUIBase.show_activity_sidebar()
            VerifyInterconnects.verify_overview_power_on(timeout=30, fail_if_false=False)

    if fail_time > 0:
        return False
    else:
        return True


def power_off_interconnect(*interconnect_obj):
    """ power_off_interconnect
        Example:
        | `Power Off Interconnect`      |     |
    """
    """below part of checking for single/multiple/named instance is yet to be implemented"""
    if isinstance(interconnect_obj, test_data.DataObj):
        interconnect_obj = [interconnect_obj]
    elif isinstance(interconnect_obj, tuple):
        interconnect_obj = list(interconnect_obj[0])

    fail_time = 0
    for interconnect in interconnect_obj:
        if not select_interconnect(interconnect.name):
            logger.warn("Exiting Power Off Interconnect Function, Not selected Interconnect %s" % interconnect.name)
            fail_time += 1
            continue

        if not VerifyInterconnects.verify_overview_power_on(fail_if_false=False):
            logger.info("the interconnect %s is not in power-on status" % interconnect.name)
            fail_time += 1

        else:
            PowerOffInterconnects.select_actions_power_off()
            PowerOffInterconnects.wait_power_off_dialog_shown()
            PowerOffInterconnects.click_yes_power_off_button()
            PowerOffInterconnects.wait_power_off_dialog_disappear()

            if not PowerOffInterconnects.wait_power_off_ok(interconnect.name):
                fail_time += 1
                logger.warn("The interconnect cannot be powered off %s" % interconnect.name)
                continue
            FusionUIBase.show_activity_sidebar()
            VerifyInterconnects.verify_overview_power_off(timeout=30, fail_if_false=False)

    if fail_time > 0:
        return False
    else:
        return True


def reset_interconnect(*interconnect_obj):
    """ reset_interconnect
        Example:
        | `Reset Interconnect`      |     |
    """
    """below part of checking for single/multiple/named instance is yet to be implemented"""
    if isinstance(interconnect_obj, test_data.DataObj):
        interconnect_obj = [interconnect_obj]
    elif isinstance(interconnect_obj, tuple):
        interconnect_obj = list(interconnect_obj[0])
    fail_time = 0
    for interconnect in interconnect_obj:
        if not select_interconnect(interconnect.name):
            logger.warn("Exiting Reset Interconnect Function, Not selected Interconnect %s" % interconnect.name)
            fail_time += 1
            continue
        if not VerifyInterconnects.verify_overview_power_on():
            logger.info("the interconnect %s is not in power-on status" % interconnect.name)
            fail_time += 1
        else:
            ResetInterconnects.select_actions_reset()
            if not ResetInterconnects.wait_reset_ok(interconnect.name):
                fail_time += 1
                logger.warn("The interconnect cannot be reset %s" % interconnect.name)
    if fail_time > 0:
        return False
    else:
        return True


def reset_C7000_interconnect_loop_and_pause_flood_protection(*interconnect_obj):
    """ reset loop and pause protection interconnect
        Example:
        | `Reset Loop And Pause Protection Interconnect`      |     |

        * required arguments:
        <interconnects>
            <interconnect name="VC-CRM1, interconnect 1"  enclosure="VC-CRM1" interconnect_power="On">
            </interconnect>
        </interconnects>
    """
    if isinstance(interconnect_obj, test_data.DataObj):
        interconnect_obj = [interconnect_obj]
    elif isinstance(interconnect_obj, tuple):
        interconnect_obj = list(interconnect_obj[0])
    fail_time = 0
    for interconnect in interconnect_obj:
        if not select_interconnect(interconnect.name):
            logger.warn("Exiting Reset Loop And Pause Protection Interconnect Function, Not selected Interconnect %s" % interconnect.name)
            fail_time += 1
            continue
        if not VerifyInterconnects.verify_overview_power_on(fail_if_false=False):
            logger.info("the interconnect %s is not in power-on status" % interconnect.name)
            fail_time += 1
        else:
            ResetLoopAndPauseFloodProtection.select_actions_reset_loop_and_pause_flood_protection()
            if not ResetLoopAndPauseFloodProtection.wait_reset_loop_and_pause_flood_protection_ok(interconnect.name):
                fail_time += 1
                logger.warn("The interconnect cannot be reset %s" % interconnect.name)
    if fail_time > 0:
        ui_lib.fail_test('The interconnect cannot be reset %s' % interconnect.name)
    else:
        return True


def soft_reset_natasha_interconnect(*interconnect_obj):
    """ soft_reset_natasha_interconnect
        Example:
        | `Soft Reset Natasha Interconnect`      | @{IC Data} |
    """
    """below part of checking for single/multiple/named instance is yet to be implemented"""
    if isinstance(interconnect_obj, test_data.DataObj):
        interconnect_obj = [interconnect_obj]
    elif isinstance(interconnect_obj, tuple):
        interconnect_obj = list(interconnect_obj[0])

    for interconnect in interconnect_obj:
        if not select_interconnect(interconnect.name):
            ui_lib.fail_test("Exiting Reset Interconnect Function, Not selected Interconnect %s" % interconnect.name)

        if not VerifyInterconnects.verify_overview_power_on():
            ui_lib.fail_test("the interconnect %s is not in power-on status" % interconnect.name)

        else:
            ResetInterconnects.select_actions_reset()
            ResetInterconnects.wait_reset_dialog_shown()
            ResetInterconnects.click_soft_reset_button()
            ResetInterconnects.wait_reset_dialog_disappear()

            if not ResetInterconnects.wait_soft_reset_ok(interconnect.name):
                ui_lib.fail_test("The interconnect [ %s ] cannot be reset." % interconnect.name)

            if ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_PANEL_RIGHT_SIDEBAR):
                ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_RIGHT_SIDEBAR_ACTIVITY)
                ui_lib.wait_for_element_notvisible(GeneralInterconnectsElements.ID_PANEL_RIGHT_SIDEBAR)


def hard_reset_natasha_interconnect(*interconnect_obj):
    """ hard_reset_natasha_interconnect
        Example:
        | `Hard Reset Natasha Interconnect`      | @{IC Data} |
    """
    """below part of checking for single/multiple/named instance is yet to be implemented"""
    if isinstance(interconnect_obj, test_data.DataObj):
        interconnect_obj = [interconnect_obj]
    elif isinstance(interconnect_obj, tuple):
        interconnect_obj = list(interconnect_obj[0])

    for interconnect in interconnect_obj:
        if not select_interconnect(interconnect.name):
            ui_lib.fail_test("Exiting Reset Interconnect Function, Not selected Interconnect %s" % interconnect.name)

        if not VerifyInterconnects.verify_overview_power_on():
            ui_lib.fail_test("the interconnect %s is not in power-on status" % interconnect.name)

        else:
            ResetInterconnects.select_actions_reset()
            ResetInterconnects.wait_reset_dialog_shown()
            ResetInterconnects.click_hard_reset_button()
            ResetInterconnects.wait_reset_dialog_disappear()

            if not ResetInterconnects.wait_hard_reset_ok(interconnect.name):
                ui_lib.fail_test("The interconnect [ %s ] cannot be reset." % interconnect.name)

            if ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_PANEL_RIGHT_SIDEBAR):
                ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_RIGHT_SIDEBAR_ACTIVITY)
                ui_lib.wait_for_element_notvisible(GeneralInterconnectsElements.ID_PANEL_RIGHT_SIDEBAR)


def turn_on_interconnect_uid(*interconnect_obj):
    """ turn_on_interconnect_uid
        Example:
        | `Turn On interconnect uid`      |     |
    """
    """below part of checking for single/multiple/named instance is yet to be implemented"""
    if isinstance(interconnect_obj, test_data.DataObj):
        interconnect_obj = [interconnect_obj]
    elif isinstance(interconnect_obj, tuple):
        interconnect_obj = list(interconnect_obj[0])

    fail_time = 0
    for interconnect in interconnect_obj:
        if not select_interconnect(interconnect.name):
            logger.warn("Exiting Turn On UID Interconnect Function, Not selected Interconnect %s" % interconnect.name)
            fail_time += 1
            continue

        if not VerifyInterconnects.verify_uid_light_off(fail_if_false=False):
            logger.info("the interconnect %s UID light is not in off status" % interconnect.name)
            fail_time += 1

        else:
            CommonOperationInterconnects.click_uid_light()
            VerifyInterconnects.verify_uid_light_on(fail_if_false=True)

    if fail_time > 0:
        return False
    else:
        return True


def turn_off_interconnect_uid(*interconnect_obj):
    """ turn_off_interconnect_uid
        Example:
        | `Turn Off interconnect uid`      |     |
    """
    """below part of checking for single/multiple/named instance is yet to be implemented"""
    if isinstance(interconnect_obj, test_data.DataObj):
        interconnect_obj = [interconnect_obj]
    elif isinstance(interconnect_obj, tuple):
        interconnect_obj = list(interconnect_obj[0])

    fail_time = 0
    for interconnect in interconnect_obj:
        if not select_interconnect(interconnect.name):
            logger.warn("Exiting Turn Off UID Interconnect Function, Not selected Interconnect %s" % interconnect.name)
            fail_time += 1
            continue

        if not VerifyInterconnects.verify_uid_light_on(fail_if_false=False):
            logger.info("the interconnect %s UID light is not in on status" % interconnect.name)
            fail_time += 1

        else:
            CommonOperationInterconnects.click_uid_light()
            VerifyInterconnects.verify_uid_light_off(fail_if_false=True)

    if fail_time > 0:
        return False
    else:
        return True


def clear_port_counters(*interconnect_obj):
    """ Clear Port Counters
        Example:
        | `Clear Port Counters`      |     |
    """
    failed_times = 0

    selenium2lib = ui_lib.get_s2l()
    if isinstance(interconnect_obj, test_data.DataObj):
        interconnect_obj = [interconnect_obj]
    elif isinstance(interconnect_obj, tuple):
        interconnect_obj = list(interconnect_obj[0])

    for interconnect in interconnect_obj:
        if not select_interconnect(interconnect.name):
            logger.warn("Exiting clear port counter     , Not selected Interconnect %s" % interconnect.name)
            selenium2lib.capture_page_screenshot()
            failed_times = failed_times + 1
            continue
        # Wait for ICM to load
        BuiltIn().sleep(2)
        ClearPortList = interconnect.ClearPortList.split(',')

        # Navigate to the section of the Interconnects page we care about
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_OVERVIEW)
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_UPLINK_PORTS)

        # Expand all the information for the uplink ports we need to check
        for uplinkport in ClearPortList:
            logger.info("Expand information for port %s" % uplinkport)
            # Pull-down element is hidden by UI decoration, so scroll up just a bit by finding offsetHeight of each uplink row
            ui_lib.scroll_to_xpath((FusionInterconnectPage.XP_PORT_ROW % uplinkport), FusionInterconnectPage.XP_PORT_TABLE, FusionInterconnectPage.XP_UPLINK_PORTS_LABEL, FusionInterconnectPage.RAW_ID_CONTAINER_DIV)
            # Open port panel
            PORT_SELECTOR = ((FusionInterconnectPage.XP_PORT_ROW + FusionInterconnectPage.XP_PORT_OPENCLOSE) % uplinkport)
            ui_lib.wait_for_element_and_click(PORT_SELECTOR)

        xpathIndex = 0    # List index
        # Iterate through each informational <tr> that we just opened to make sure no TX/RX errors were seen
        for uplinkport in ClearPortList:
            xpathIndex += 1    # xpath indices always start with 1
            PORT_SELECTOR = FusionInterconnectPage.XP_PORT_STATISTICS % xpathIndex
            # Scroll to the information row
            ui_lib.wait_for_element_and_click(PORT_SELECTOR)
            # TODO: Verify that PORT_SELECTOR is the following-sibling of the desired uplink port's <tr>
            # Open the statistics for the current uplink port
            ui_lib.wait_for_element_and_click(PORT_SELECTOR + FusionInterconnectPage.XP_PORT_STATS_OPENCLOSE)
            # If the desired statistics fields exist,
            if ui_lib.wait_for_element(PORT_SELECTOR + FusionInterconnectPage.XP_PORT_STATS_XMT_ERRORS):
                logger.info("Making sure port %s did not get any Transmit or Receive errors..." % uplinkport)
                # Get Transmitted Errors
                ui_lib.wait_for_element(PORT_SELECTOR + FusionInterconnectPage.XP_PORT_STATS_XMT_ERRORS)
                transmittedErrors = selenium2lib._get_text(PORT_SELECTOR + FusionInterconnectPage.XP_PORT_STATS_XMT_ERRORS)
                # Get Received Errors
                ui_lib.wait_for_element(PORT_SELECTOR + FusionInterconnectPage.XP_PORT_STATS_RCV_ERRORS)
                receivedErrors = selenium2lib._get_text(PORT_SELECTOR + FusionInterconnectPage.XP_PORT_STATS_RCV_ERRORS)
                # logger.info("TX errors: '%s' RX errors: '%s'" % (transmittedErrors, receivedErrors))
                if transmittedErrors == "0" and receivedErrors == "0":
                    logger.info("Clear port Counter is successful for the given interconnect %s" % interconnect.name)
                else:
                    logger.warn("Clear port Counter is not successful for Interconnect %s Port %s: found %s transmit errors and %s receive errors" % (interconnect.name, uplinkport, transmittedErrors, receivedErrors))
                    selenium2lib.capture_page_screenshot()
                    failed_times = failed_times + 1
            else:
                logger.info("Failed to see the statistics for uplink %s.  Element was not found: %s" % (uplinkport, PORT_SELECTOR + FusionInterconnectPage.XP_PORT_STATS_XMT_ERRORS))
                selenium2lib.capture_page_screenshot()
                failed_times = failed_times + 1
            selenium2lib.capture_page_screenshot()

    if failed_times > 0:
        return False
    else:
        return True


def reapply_configuration(*interconnect_obj):
    """ Reapply Configuration
        Example:
        | `Reapply Configuration`      |     |
    """
    failed_times = 0
    StatusList = {"X1": "", "X2": "", "X3": "", "X4": "", "X5": "", "X6": "", "X7": "", "X8": ""}
    selenium2lib = ui_lib.get_s2l()
    if isinstance(interconnect_obj, test_data.DataObj):
        interconnect_obj = [interconnect_obj]
    elif isinstance(interconnect_obj, tuple):
        interconnect_obj = list(interconnect_obj[0])

    for interconnect in interconnect_obj:
        if not select_interconnect(interconnect.name):
            logger.warn("Exiting clear port counter     , Not selected Interconnect %s" % interconnect.name)
            continue
        # Wait for ICM to load
        BuiltIn().sleep(2)
        UplinkPortList = interconnect.UplinkList.split(',')
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_OVERVIEW)
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_UPLINK_PORTS)
        if ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_LINK_GENERAL, PerfConstants.DEFAULT_SYNC_TIME):
            ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_GENERAL)
            ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_UPLINK_PORTS)
        for UplinkPort in UplinkPortList:
            PORT_SELECTOR = FusionInterconnectPage.XP_PORT_ROW % UplinkPort
            PORT_STATUS = PORT_SELECTOR + FusionInterconnectPage.XP_PORT_STATUS_TEMPLATE
            if selenium2lib._is_element_present(PORT_STATUS % 'error'):
                strTemp = "error"
                StatusList[UplinkPort] = strTemp
            elif selenium2lib._is_element_present(PORT_STATUS % 'disabled'):
                strTemp = "disabled"
                StatusList[UplinkPort] = strTemp
            elif selenium2lib._is_element_present(PORT_STATUS % 'ok'):
                strTemp = "ok"
                StatusList[UplinkPort] = strTemp
            else:
                logger.warn("There is no proper status for the given port %s" % UplinkPort)

        if not select_interconnect(interconnect.name):
            logger.warn("Exiting clear port counter , Not selected Interconnect %s" % interconnect.name)
            selenium2lib.capture_page_screenshot()
            failed_times = failed_times + 1
            continue
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_ACTION_MAIN_BTN)
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_MENU_ACTION_REAPPLY_CONF)
        ui_lib.wait_for_element_and_click("//div/button[text()='Yes, reapply']")
        if ui_lib.wait_for_element(FusionInterconnectPage.ID_LABEL_STATUS, PerfConstants.EDIT_INTERCONNECTS):
            logger.info("The reapply configuration is successful to the given interconnect - %s" % interconnect.name)

        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_OVERVIEW)
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_UPLINK_PORTS)
        blnTemp = True
        for UplinkPort in UplinkPortList:
            PORT_SELECTOR = FusionInterconnectPage.XP_PORT_ROW % UplinkPort
            PORT_STATUS = PORT_SELECTOR + FusionInterconnectPage.XP_PORT_STATUS_TEMPLATE
            if selenium2lib._is_element_present(PORT_STATUS % 'disabled'):
                if StatusList[UplinkPort] != 'disabled':
                    blnTemp = False
            elif selenium2lib._is_element_present(PORT_STATUS % 'ok'):
                if StatusList[UplinkPort] != 'ok':
                    blnTemp = False
            else:
                blnTemp = False
                logger.warn("After reapply configuration the uplink port %s is still not changed" % UplinkPort)
                selenium2lib.capture_page_screenshot()
                failed_times = failed_times + 1

        if blnTemp:
            logger.info("The reapply configuration is successful for the given interconnect - %s" % interconnect.name)
        else:
            logger.warn("The reapply configuration is not successful for the given interconnect - %s" % interconnect.name)
            selenium2lib.capture_page_screenshot()
            return False

    if failed_times > 0:
        return False
    else:
        return True


def select_interconnect(interconnectName, timeout=5, fail_if_false=False):
    """ Select Interconnect
        Example:
        | `Select Interconnect`      |     |
    """
    navigate()
    CommonOperationInterconnects.click_interconnect(interconnectName)
    if CommonOperationInterconnects.wait_interconnect_selected(interconnectName, timeout, fail_if_false):
        logger.info("The given interconnect is selected - %s" % interconnectName)
        return True
    else:
        logger.info("The given interconnect is not selected - %s" % interconnectName)
        return False


def validate_interconnect(interconnects_obj):
    navigate()

    count = 0
    ret = True

    for n, ic_obj in enumerate(interconnects_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(interconnects_obj), '-' * 14))
        logger.info("Verifying an interconnect with name %s" % ic_obj.name)
        if not select_interconnect(ic_obj.name):
            continue

        # overview
        FusionUIBase.select_view_by_name('Overview')
        logger.info("Verifying configuration in Overview view...")

        # overview - General
        if hasattr(ic_obj, "logical_interconnect"):
            VerifyInterconnects.verify_overview_logical_interconnect(ic_obj.logical_interconnect)

        if hasattr(ic_obj, "interconnect_power"):
            VerifyInterconnects.verify_overview_power(ic_obj.interconnect_power)

        if hasattr(ic_obj, "state"):
            VerifyInterconnects.verify_overview_state(ic_obj.state)

        if hasattr(ic_obj, "installed_firmware_version"):
            VerifyInterconnects.verify_overview_installed_firmware_version(ic_obj.installed_firmware_version)

        # overview - Hardware
        if hasattr(ic_obj, "hardware"):
            hardware_obj = ic_obj.hardware[0]

            if hasattr(hardware_obj, "product_name"):
                VerifyInterconnects.verify_overview_product_name(hardware_obj.product_name)

            if hasattr(hardware_obj, "location"):
                VerifyInterconnects.verify_overview_location(hardware_obj.location)

            if hasattr(hardware_obj, "serial_number"):
                VerifyInterconnects.verify_overview_serial_number(hardware_obj.serial_number)

            if hasattr(hardware_obj, "part_number"):
                VerifyInterconnects.verify_overview_part_number(hardware_obj.part_number)

        # General
        FusionUIBase.select_view_by_name('General')
        if hasattr(ic_obj, "logical_interconnect"):
            VerifyInterconnects.verify_general_logical_interconnect(ic_obj.logical_interconnect)

        if hasattr(ic_obj, "interconnect_power"):
            VerifyInterconnects.verify_general_power(ic_obj.interconnect_power)

        if hasattr(ic_obj, "state"):
            VerifyInterconnects.verify_general_state(ic_obj.state)

        if hasattr(ic_obj, "installed_firmware_version"):
            VerifyInterconnects.verify_general_installed_firmware_version(ic_obj.installed_firmware_version)

        if hasattr(ic_obj, "ipv4"):
            VerifyInterconnects.verify_general_ipv4(ic_obj.ipv4)

        if hasattr(ic_obj, "ipv6"):
            VerifyInterconnects.verify_general_ipv6(ic_obj.ipv6)

        # Hardware
        FusionUIBase.select_view_by_name('Hardware')
        if hasattr(ic_obj, "hardware"):
            hardware_obj = ic_obj.hardware[0]

            if hasattr(hardware_obj, "product_name"):
                VerifyInterconnects.verify_hardware_product_name(hardware_obj.product_name)

            if hasattr(hardware_obj, "location"):
                VerifyInterconnects.verify_hardware_location(hardware_obj.location)

            if hasattr(hardware_obj, "serial_number"):
                VerifyInterconnects.verify_hardware_serial_number(hardware_obj.serial_number)

            if hasattr(hardware_obj, "part_number"):
                VerifyInterconnects.verify_hardware_part_number(hardware_obj.part_number)

        # TODO: Uplink ports
        if hasattr(ic_obj, "uplink_ports"):
            FusionUIBase.select_view_by_name('Uplink ports')

        # TODO: Downlink ports
        if hasattr(ic_obj, "downlink_ports"):
            FusionUIBase.select_view_by_name('Downlink ports')

        count += 1

    if count == 0:
        msg = "no target interconnect configuration exists!"
        logger.warn(msg)
        logger.warn("Return Value = False")
        return False

    if count != len(interconnects_obj):
        logger.warn("Not able to verify all interconnect configuration of enclosure!")
        logger.warn("Return Value = False")
        return False

    logger.debug("Return Value = True")
    return ret


def validate_interconnect_old(*interconnect_obj):
    """ Validate Interconnect Data
        Example:
        | 'Validate Interconnect' |    |
    """
    valid = True
    selenium2lib = ui_lib.get_s2l()
    if isinstance(interconnect_obj, test_data.DataObj):
        interconnect_obj = [interconnect_obj]
    elif isinstance(interconnect_obj, tuple):
        interconnect_obj = list(interconnect_obj[0])

    for interconnect in interconnect_obj:
        if not select_interconnect(interconnect.name):
            logger.warn("Exiting.  Not selected Interconnect %s" % interconnect.name)
            valid = False
            continue
        if hasattr(interconnect, 'uplinkport'):
            if ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_LINK_GENERAL, PerfConstants.DEFAULT_SYNC_TIME):
                ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_OVERVIEW)
            ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_UPLINK_PORTS)
            up = interconnect.uplinkport
            selenium2lib.capture_page_screenshot()
            for port in up:
                state = "unknown"
                if selenium2lib._is_element_present(FusionInterconnectPage.ID_STATUS_ACTIVE % port.name):
                    state = "active"
                elif selenium2lib._is_element_present(FusionInterconnectPage.ID_STATUS_STANDBY % port.name):
                    state = "standby"
                elif selenium2lib._is_element_present(FusionInterconnectPage.ID_STATUS_UNLINKED % port.name):
                    state = "unlinked"
                else:
                    logger.warn("The is no proper state for the given port %s" % port.name)

                if (state == port.state):
                    logger.info("Validated:  " + state + " = " + port.state + " for port " + port.name)
                else:
                    logger.info("Invalid:  " + state + " != " + port.state + " for port " + port.name)
                    valid = False
    return valid


def verify_interconnect_general_view(interconnectname, enclname, *enc_obj):
    """ This function is to verify interconnect through general view

        Example:
       verify_interconnect_general_view(CC-2, interconnect 1)
    """

    selenium2lib = ui_lib.get_s2l()

    if not selenium2lib._is_element_present(FusionInterconnectPage.ID_PAGE_LABEL):
        navigate()

    if not select_interconnect(interconnectname):
        logger.info("Failed to select interconnect '%s' " % interconnectname)

    ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_OVERVIEW)
    ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_GENERAL)

    """ dictionary to store interconnect details of the given interconnect name """
    generaldict = {'Logical interconnect': [], 'Interconnect power': [], 'State': [], 'Firmware baseline': [], 'Installed firmware version': [], 'Product name': [],
                   'Location': [], 'Serial number': [], 'Part number': []}

    """ Loop to retrieve the interconnect details under General menu."""
    for obj in generaldict:
        ui_lib.wait_for_element(FusionInterconnectPage.ID_GENERAL_VIEW % obj)
        appval = ui_lib.get_text(FusionInterconnectPage.ID_GENERAL_VIEW % obj)
        generaldict[obj] = appval.encode('utf8')

    """ Navigating to enclosure page to get Logical interconnect name,bay number and encl ip """
    logger.info("This interconnect %s belongs to enclosure %s " % (interconnectname, enclname))
    enclosures.navigate()
    enclosureObj = FusionEnclosuresPage.ID_LINK_ENCLOSURE_NAME % enclname
    ui_lib.wait_for_element_and_click(enclosureObj)
    ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_CLICK_LOGICAL_ENCLOSURE, PerfConstants.DEFAULT_SYNC_TIME)
    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_CLICK_LOGICAL_ENCLOSURE)
#    ui_lib.wait_for_element(FusionEnclosuresPage.ID_GENERAL_VIEW % 'Logical interconnect', PerfConstants.DEFAULT_SYNC_TIME)
#    ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_GENERAL_VIEW % 'Logical interconnect', PerfConstants.DEFAULT_SYNC_TIME)
#    strlogicalinterconnectval = ui_lib.get_text(FusionEnclosuresPage.ID_GENERAL_VIEW % 'Logical interconnect')
    ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_GENERAL_VIEW, PerfConstants.DEFAULT_SYNC_TIME)
    strlogicalinterconnectval = ui_lib.get_text(FusionEnclosuresPage.ID_GENERAL_VIEW)
    strlogicalinterconnect = str(strlogicalinterconnectval)
    enclosures.navigate()
    BuiltIn().sleep(2)
    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_CLICK_OVERVIEW)
    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_SELECT_INTERCONNECTBAYS)
    if ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_SELECT_INTERCONNECT % interconnectname):
        ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_BAY_NUMBER, PerfConstants.DEFAULT_SYNC_TIME)
    strlocation = ui_lib.get_text(FusionEnclosuresPage.ID_BAY_NUMBER)
    logging._log_to_console_and_log_file("This interconnect %s is available in enclosure %s in location %s " % (interconnectname, enclname, strlocation))
    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_MENU_SELECTOR)
    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_DROPDOWN_SELECT)

    ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_OA_IP, PerfConstants.DEFAULT_SYNC_TIME * 3)
    ipval = ui_lib.get_text(FusionEnclosuresPage.ID_OA_IP)
    interconnectlocation = enclname + ", interconnect bay " + strlocation

    """ Getting the enclosure details from data sheet with the given encl ip."""
    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])

    for enclosure in enc_obj:
        if enclosure.oa1hostname == ipval:
            oainfo = blade_info(ipval, enclosure.oa1username, enclosure.oa1password)

            """ retrieving OA info through oa functions """
            logger.info("-------- Retrieving OA information--------")
            strvcstatus = oainfo.get_vc_status(strlocation)
            strvcfirmwareversion = oainfo.get_firmware_version_for_vc(strlocation)
            strvcproductname = oainfo.get_vc_product_name(strlocation)
            strvcserialnumber = oainfo.get_vc_serial_number(strlocation)
            strvcpartnumber = oainfo.get_vc_part_number(strlocation)

            blncomparisonflag = False
            if (strvcstatus[0] and strvcfirmwareversion[0] and strvcproductname[0] and strvcserialnumber[0] and strvcpartnumber[0]):
                oadict = {'Logical interconnect': strlogicalinterconnect, 'Interconnect power': strvcstatus[1], 'Installed firmware version': strvcfirmwareversion[1], 'Product name': strvcproductname[1],
                          'Location': interconnectlocation, 'Serial number': strvcserialnumber[1], 'Part number': strvcpartnumber[1]}
                logger.info("############# Data comparison,OA with fusion appliance data #################### ")
                for key in oadict:
                    if str(oadict[key]).lstrip() != str(generaldict[key]).lstrip():
                        logger.warn("Data %s comparison with OA %s failed against appliance data %s" % (key, oadict[key], generaldict[key]))
                    else:
                        blncomparisonflag = True
                if blncomparisonflag:
                    logger.info("Comparison for values in General drop down, -verification passed for all values")
            else:
                logger.warn("Fail to retrieve data from OA")

    logger.info("############# Now verify the other drop down Menus of the given interconnect #################### ")


def verify_interconnect_uplinkport_view(*inc_obj):
    """ This function is to verify interconnect Up link port information

        Example:
       verify_interconnect_uplinkport_view(*interconnect_obj)
    """
    FusionUIBase.navigate_to_section(SectionType.INTERCONNECTS)

    if isinstance(inc_obj, test_data.DataObj):
        inc_obj = [inc_obj]
    elif isinstance(inc_obj, tuple):
        inc_obj = list(inc_obj[0])

    total = len(inc_obj)
    not_exists = 0
    verified_pass = 0

    for n, inc in enumerate(inc_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("verifying uplink port info of interconnect named '%s'" % inc.name)

        if not VerifyInterconnects.verify_interconnect_exist(inc.name, timeout=5, fail_if_false=False):
            logger.warn("interconnect '%s' does not exist" % inc.name)
            not_exists += 1
            continue

        CommonOperationInterconnects.click_interconnect(inc.name, timeout=5)

        FusionUIBase.select_view_by_name(view_name="Uplink Ports", timeout=5, fail_if_false=False)

        result = {}

        uplink_list = inc.uplinkport
        for m, uplink in enumerate(uplink_list):
            num = m + 1
            if hasattr(uplink, 'Port'):
                if not VerifyInterconnects.verify_port_in_uplink_port(uplink.Port, num):
                    logger.warn("'Uplink Port' of interconnect '%s' is not '%s', verification failed." % (inc.name, uplink.Port))
                    result['uplink_port_%d' % num] = False
                else:
                    result['uplink_port_%d' % num] = True

            if hasattr(uplink, 'Type'):
                if not VerifyInterconnects.verify_type_in_uplink_port(uplink.Type, num):
                    logger.warn("'Uplink type' of interconnect '%s' is not '%s', verification failed." % (inc.name, uplink.Type))
                    result['uplink_type_%d' % num] = False
                else:
                    result['uplink_type_%d' % num] = True

            if hasattr(uplink, 'State'):
                if not VerifyInterconnects.verify_status_in_uplink_port(uplink.State, num):
                    logger.warn("'Uplink status' of interconnect '%s' is not '%s', verification failed." % (inc.name, uplink.State))
                    result['uplink_status_%d' % num] = False
                else:
                    result['uplink_status_%d' % num] = True

            if hasattr(uplink, 'Speed'):
                if not VerifyInterconnects.verify_speed_in_uplink_port(uplink.Speed, num):
                    logger.warn("'Uplink speed' of interconnect '%s' is not '%s', verification failed." % (inc.name, uplink.Speed))
                    result['uplink_speed_%d' % num] = False
                else:
                    result['uplink_speed_%d' % num] = True

            if hasattr(uplink, 'uplink_set'):
                if not VerifyInterconnects.verify_uplink_set_in_uplink_port(uplink.uplink_set, num):
                    logger.warn("'Uplink sets' of interconnect '%s' is not '%s', verification failed." % (inc.name, uplink.uplink_set))
                    result['uplink_uplink_set_%d' % num] = False
                else:
                    result['uplink_uplink_set_%d' % num] = True

            if hasattr(uplink, 'Connected_to'):
                if not VerifyInterconnects.verify_connect_to_in_uplink_port(uplink.Connected_to, num):
                    logger.warn("'Uplink Connected To' of interconnect '%s' is not '%s', verification failed." % (inc.name, uplink.uplink_set))
                    result['uplink_connected_to_%d' % num] = False
                else:
                    result['uplink_connected_to_%d' % num] = True

        verified_pass += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no interconnect to verify uplink ports info against! all %s interconnect(s) is NOT existing, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if verified_pass < total:
            logger.warn("not all of the uplink port(s) is successfully verified PASS - %s out of %s passed " % (verified_pass, total))
            if verified_pass + not_exists == total:
                # logger.warn("%s not-existing server profile(s) is skipped, test is considered FAIL" % not_exists)
                logger.warn("%s not-existing uplink port(s) is skipped, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s not-existing uplink port(s) is skipped, "
                            "%s uplink port(s) left is failed being verified PASS " % (not_exists, total - verified_pass - not_exists))
                return False

    logger.info("all of the uplink port(s) is successfully verified PASS - %s out of %s " % (verified_pass, total))
    return True


def verify_interconnect_downlinkport_view_tbird(*inc_obj):
    """ This function is to verify interconnect Downlink port information

        Example:
       verify_interconnect_downlinkport_view(*interconnect_obj)
    """
    FusionUIBase.navigate_to_section(SectionType.INTERCONNECTS)

    if isinstance(inc_obj, test_data.DataObj):
        inc_obj = [inc_obj]
    elif isinstance(inc_obj, tuple):
        inc_obj = list(inc_obj[0])

    total = len(inc_obj)
    not_exists = 0
    verified_pass = 0

    for n, inc in enumerate(inc_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("verifying Downlink port info of interconnect named '%s'" % inc.name)

        if not VerifyInterconnects.verify_interconnect_exist(inc.name, timeout=5, fail_if_false=False):
            logger.warn("interconnect '%s' does not exist" % inc.name)
            not_exists += 1
            continue

        CommonOperationInterconnects.click_interconnect(inc.name, timeout=5)

        FusionUIBase.select_view_by_name(view_name="Downlink Ports", timeout=5, fail_if_false=False)

        result = {}

        downlink_list = inc.downlinkport
        for m, downlink in enumerate(downlink_list):
            num = m + 1
            if hasattr(downlink, 'State'):
                if not VerifyInterconnects.verify_status_in_downlink_port(downlink.State, downlink.Port):
                    logger.warn("'Downlink status' of interconnect '%s' is not '%s', verification failed." % (inc.name, downlink.State))
                    result['downlink_status_%d' % num] = False
                else:
                    result['downlink_status_%d' % num] = True

            if hasattr(downlink, 'Port'):
                if not VerifyInterconnects.verify_port_in_downlink_port(downlink.Port, downlink.Port):
                    logger.warn("'Downlink port' of interconnect '%s' is not '%s', verification failed." % (inc.name, downlink.Port))
                    result['downlink_port_%d' % num] = False
                else:
                    result['downlink_port_%d' % num] = True

            if hasattr(downlink, 'Hardware'):
                if not VerifyInterconnects.verify_serverhardware_in_downlink_port(downlink.Hardware, downlink.Port):
                    logger.warn("'Downlink Hardware' of interconnect '%s' is not '%s', verification failed." % (inc.name, downlink.Hardware))
                    result['downlink_port_%d' % num] = False
                else:
                    result['downlink_port_%d' % num] = True

            if hasattr(downlink, 'AdapterPort'):
                if not VerifyInterconnects.verify_AdapterPorts_in_downlink_port(downlink.AdapterPort, downlink.Port):
                    logger.warn("'Downlink Adapter' of interconnect '%s' is not '%s', verification failed." % (inc.name, downlink.AdapterPort))
                    result['downlink_port_%d' % num] = False
                else:
                    result['downlink_port_%d' % num] = True

            if hasattr(downlink, 'Profile'):
                if not VerifyInterconnects.verify_ServerProfile_in_downlink_port(downlink.Profile, downlink.Port):
                    logger.warn("'Downlink ServerProfile' of interconnect '%s' is not '%s', verification failed." % (inc.name, downlink.Profile))
                    result['downlink_port_%d' % num] = False
                else:
                    result['downlink_port_%d' % num] = True

        verified_pass += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no interconnect to verify downlink ports info against! all %s interconnect(s) is NOT existing, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if verified_pass < total:
            logger.warn("not all of the downlink port(s) is successfully verified PASS - %s out of %s passed " % (verified_pass, total))
            if verified_pass + not_exists == total:
                # logger.warn("%s not-existing server profile(s) is skipped, test is considered FAIL" % not_exists)
                logger.warn("%s not-existing downlink port(s) is skipped, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s not-existing downlink port(s) is skipped, "
                            "%s downlink port(s) left is failed being verified PASS " % (not_exists, total - verified_pass - not_exists))
                return False

    logger.info("all of the downlink port(s) is successfully verified PASS - %s out of %s " % (verified_pass, total))
    return True


def verify_interconnect_downlinkport_view(interconnectname, enclname, *enc_obj):
    "[LEGACY]"
    """ This function is to verify interconnect down link port information

        Example:
       verify_interconnect_downlinkport_view(CC-2, interconnect 1)
    """
    s2l = ui_lib.get_s2l()

    """ retrieve server hardware assigned to each profile """
    server_profile = serverprofiles._get_assigned_server_for_profile()

    """ retrieve networks from appliance """
    networklist = networks._list_networks()
    networkdict = {}

    """ Getting the enclosure details from data sheet """
    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])

    for enclosure in enc_obj:
        if enclosure.name == enclname:
            oainfo = blade_info(enclosure.oa1hostname, enclosure.oa1username, enclosure.oa1password)

            """ retrieve port information from OA """
            logger.info("-------- Retieving OA port information--------")
            conn_list = oainfo.get_server_port_information(enclname)

            if conn_list[0]:
                logger.info("Verify these connection values in %s Down link port information " % interconnectname)
                if not s2l._is_element_present(FusionInterconnectPage.ID_PAGE_LABEL):
                    navigate()
                    navigate_to_dropdown_menus(interconnectname, 'Downlink Ports')
                    ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_INTERCONNECTS_COUNT, PerfConstants.FUSION_PAGE_SYNC)

                    """ verifying the profile and server hardware in interconnect down link port  """
                    for k, v in server_profile.items():
                        ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_DOWNLINK_PORT_PATH % (v, k), PerfConstants.DEFAULT_SYNC_TIME)

                        if s2l._is_element_present(FusionInterconnectPage.ID_DOWNLINK_PORT_PATH % (v, k)):
                            logger.info("Verifying the profile %s,hardware %s for the interconnect %s " % (k, v, interconnectname))
                            ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_DOWNLINK_COLLAPSE % (v, k))
                            portnum = s2l._get_text(FusionInterconnectPage.ID_DOWNLINK_PORT % (v, k, v, v))
                            logger.info("Portnum is %s" % portnum)

                            """ Retrieving the each row data of a port """
                            rowcount = 1
                            row_path = "//*[@id='cic-ic-more-connectivity-downlinks-table']/tbody/tr[%s]" % portnum
                            logger.info("row_path is %s" % row_path)
                            while (s2l._is_element_present(row_path)):
                                # - TC 25 Implementation -
                                strstate = str(ui_lib.get_text("//*[@id='cic-ic-more-connectivity-downlinks-table']/tbody/tr[%s]/td[4]" % portnum))
                                logger.info("Value of strstate %s" % strstate)

                                """ Verifying the downlink port state when Server Power ON and OFF """
                                if (enclosure.has_property("state")):
                                    if (strstate == enclosure.state):
                                        logger.info("The interconnect downlink port " + portnum + " status is in " + strstate + " state")
                                        return strstate

                                    else:
                                        logger.info("The interconnect downlink port is not as expected")
                                        return strstate
                                else:
                                    strflexnic = str(s2l._get_text("//*[@id='cic-interconnect-downlink-panel-" + portnum + "']/div[2]//tr[@class='cic-tr-row'][" + str(rowcount) + "]/td[3]"))
                                    strtype = str(s2l._get_text("//*[@id='cic-interconnect-downlink-panel-" + portnum + "']/div[2]//tr[@class='cic-tr-row'][" + str(rowcount) + "]/td[4]"))
                                    strnetwork = str(s2l._get_text("//*[@id='cic-interconnect-downlink-panel-" + portnum + "']/div[2]//tr[@class='cic-tr-row'][" + str(rowcount) + "]/td[6]"))
                                    straddress = str(s2l._get_text("//*[@id='cic-interconnect-downlink-panel-" + portnum + "']/div[2]//tr[@class='cic-tr-row'][" + str(rowcount) + "]/td[8]"))

                                    networkdict[strnetwork] = strtype
                                    if networklist[strnetwork] != networkdict[strnetwork]:
                                        logger.warn("Network %s comparison with type %s in down link failed against type available in Networks page %s" % (strnetwork, networkdict[strnetwork], networklist[strnetwork]))
                                    else:
                                        searchlist = [strflexnic, strtype, straddress]

                                    """comparing the above retrieved row data with the data retrieved from OA """
                                    logger.info("comparing the above retrieved row data with the data retrieved from OA ")
                                    blnflag = False
                                    for listobj in conn_list[1]:
                                        lowersearchlist = map(lambda x: x.lower(), searchlist)
                                        lowerlistobj = map(lambda x: x.lower(), listobj)
                                        if lowersearchlist == lowerlistobj:
                                            blnflag = True
                                            break
                                    if blnflag:
                                        logger.info("Verification for interconnect %s pass for port %s data address %s,flexnic %s,network %s" % (interconnectname, portnum, straddress, strflexnic, strnetwork))
                                    else:
                                        logger.warn("Verification for interconnect %s fail for port %s data address %s,flexnic %s,network %s,data didn't match with OA data" % (interconnectname, portnum, straddress, strflexnic, strnetwork))
                                    row_path = "//*[@id='cic-interconnect-downlink-panel-" + portnum + "']/div[2]//tr[@class='cic-tr-row'][" + str(rowcount + 1) + "]"
                                    rowcount = rowcount + 1

                            else:
                                if rowcount == 1:
                                    logger.info("No connections exist for this interconnect %s to validate" % interconnectname)
                                else:
                                    logger.info("Now Validate the down link info for other port in interconnect %s or other interconnect in encl" % interconnectname)

                        else:
                            logger.info("Not able to find downlink port info for interconnect %s ,with hardware %s ,and profile %s " % (interconnectname, v, k))
            else:
                logger.warn("Fail to retrieve OA port information")


def navigate_to_dropdown_menus(interconnect, dropdownmenu):
    """ This function is to navigate to drop down menus in interconnects page
        Example:
        | _navigate_to_dropdown_menus(CC-2, interconnect 2, Up link ports)     |     |
    """

    selenium2lib = ui_lib.get_s2l()

    if not selenium2lib._is_element_present(FusionInterconnectPage.ID_PAGE_LABEL):
        navigate()

    if not select_interconnect(interconnect):
        ui_lib.fail_test("Exiting navigate to drop down menus function, as the Interconnect %s is not selected " % interconnect)
        selenium2lib.capture_page_screenshot()
        return False
    else:
        ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_INTERCONNECTS_COUNT, PerfConstants.FUSION_PAGE_SYNC)
        strtitle = selenium2lib._get_text(FusionInterconnectPage.ID_TITLE_DETAILS)
        if strtitle.strip() != interconnect.strip():
            logger.warn("Expected interconnect - %s is not selected" % interconnect)
            selenium2lib.capture_page_screenshot()
            return False
        else:
            strdropdownmenu = selenium2lib._get_text(FusionInterconnectPage.ID_MENU_SELECTOR)
            if strdropdownmenu.lower() != dropdownmenu.lower():
                ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_MENU_SELECTOR)

                """ parameterize the x path. """
                dropdownlist = ['General', 'Uplink Ports', 'Downlink Ports']
                ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_INTERCONNECTS_COUNT, PerfConstants.FUSION_PAGE_SYNC)
                if dropdownmenu in dropdownlist:

                    """ for up link and down link,direct selection is not happening.so first select General and then select up link or down link """
                    if dropdownmenu == "Uplink ports" or dropdownmenu == "Downlink ports":
                        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_DROPDOWN_SUBOPTIONS_SELECT % 'General')
                        ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_INTERCONNECTS_COUNT, PerfConstants.FUSION_PAGE_SYNC)
                        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_MENU_SELECTOR)
                    ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_DROPDOWN_SUBOPTIONS_SELECT % dropdownmenu)
                else:
                    ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_DROPDOWN_SELECT % dropdownmenu)

            ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_INTERCONNECTS_COUNT, PerfConstants.DEFAULT_SYNC_TIME)
            if selenium2lib._get_text(FusionInterconnectPage.ID_MENU_SELECTOR) == dropdownmenu:

                """ dictionary to create xpath for the drop down menu verification """
                datadict = {'General': "//*[@id='cic-interconnect-general-selector']/label", 'Uplink Ports': ".//*[@id='cic-interconnect-uplink-selector']/label",
                            'Downlink Ports': "//*[@id='cic-interconnect-downlink-selector']/label", 'Activity': "//*[@id='hp-activity-meta-filter']/div",
                            'Map': "//div//ol/li/label[text()='Interconnects']"}

                if dropdownmenu.strip() in datadict:
                    if selenium2lib._is_element_present(datadict[dropdownmenu]):
                        logger.info("Expected drop down %s is selected  for interconnect %s" % (dropdownmenu, interconnect))
                        return True
                    else:
                        logger.warn("Fail in selecting the expected drop down - %s for interconnect %s " % (dropdownmenu, interconnect))
                        selenium2lib.capture_page_screenshot()
                        return False
            else:
                logger.warn("Fail in selecting the expected drop down - %s for interconnect %s " % (dropdownmenu, interconnect))
                selenium2lib.capture_page_screenshot()
                return False


def verify_interconnect_activity_view(interconnectname):
    """ This function is to navigate to drop down menus in interconnects page
        Example:
        | _navigate_to_dropdown_menus(CC-2, interconnect 2, Up link ports)     |     |
    """

    selenium2lib = ui_lib.get_s2l()

    if not selenium2lib._is_element_present(FusionInterconnectPage.ID_PAGE_LABEL):
        navigate()

    if not select_interconnect(interconnectname):
        ui_lib.fail_test("Exiting navigate to drop down menus function, as the Interconnect %s is not selected " % interconnectname)
        selenium2lib.capture_page_screenshot()
        return False

    navigate_to_dropdown_menus(interconnectname, 'Activity')
    if not selenium2lib._is_element_present(FusionInterconnectPage.ID_ACTIVITY_VIEW):
        logger.warn("Fail to load activity view ")
        selenium2lib.capture_page_screenshot()
        return False

    item_min_val = 3
    item_max_val = 7
    statelist = ['Active', 'Locked', 'Cleared', 'Pending', 'Running', 'Completed', 'Interrupted', 'Error', 'Warning']
    activity_details = ['Activity Name', 'Date', 'Status', 'Owner']

    for intcount in range(item_min_val, item_max_val):
        activity_obj = FusionInterconnectPage.ID_ACTIVITY_DETAILS + "/span[1]"
        activity_name = ""
        ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_ACTIVITY_DETAILS % intcount, PerfConstants.FUSION_PAGE_SYNC)
        if(selenium2lib._is_element_present(activity_obj % intcount)):
            activity_name = selenium2lib._get_text(activity_obj % intcount)
        elif selenium2lib._is_element_present(FusionInterconnectPage.ID_ACTIVITY_DETAILS % intcount):
            activity_name = selenium2lib._get_text(FusionInterconnectPage.ID_ACTIVITY_DETAILS % intcount)
        if intcount == 5:
            activity_status = str(activity_name.split()[0])
            if not (activity_status in statelist):
                logger.warn(" Activity state '%s' returned is not the expected one" % activity_status)
                selenium2lib.capture_page_screenshot()
                return False

        if not activity_name == "":
            logger.info("Value for '%s' is '%s' " % (activity_details[intcount - 3], activity_name))
        else:
            logger.warn(" '%s' should not be null" % activity_details[intcount - 3])
            selenium2lib.capture_page_screenshot()
            return False


def verify_interconnect_downlinkport_view_cisco(*interconnect_obj):
    """ This function is to verify interconnect down link port information for cisco FEX modules
        This  test requires Server profile to be applied and the server should be powered on.
        Example:
       verify_interconnect_downlinkport_view(CC-2, interconnect 1)
       Sample imput data mentioned in veify_interconnect_uplink_port_view function.
    """
    s2l = ui_lib.get_s2l()

    """ retrieve server hardware assigned to each profile """
    server_profile = serverprofiles._get_assigned_server_for_profile()
    """ retrieve networks from appliance """
    networklist = networks._list_networks_vlan()

    datadict = {}
    switchdict = {}
    fail = 0
    suboptions_count = 7
    """ Getting the enclosure details from data sheet """
    if isinstance(interconnect_obj, test_data.DataObj):
        interconnect_obj = [interconnect_obj]
    elif isinstance(interconnect_obj, tuple):
        interconnect_obj = list(interconnect_obj[0])

    for net in interconnect_obj:
        logging._log_to_console_and_log_file("Selecting first interconnect object ")
        if hasattr(net, "type"):
            if net.type != "fex":
                logging._log_to_console_and_log_file("%s is a non fex module. Skipping the test" % net.name)
                return True
        else:
            logging._log_to_console_and_log_file("%s is a non fex module. Skipping the test" % net.name)
            return True
        interconnectname = net.name

        logging._log_to_console_and_log_file("Verify these connection values in %s Down link port information " % interconnectname)
        if not s2l._is_element_present(FusionInterconnectPage.ID_PAGE_LABEL):
            navigate()
        if not navigate_to_dropdown_menus(interconnectname, 'Downlink ports'):
            return False
        ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_INTERCONNECTS_COUNT, PerfConstants.FUSION_PAGE_SYNC)

        """ verifying the profile and server hardware in interconnect down link port  """
        for k, v in server_profile.items():

            switchdict.clear()
            datadict.clear()
            ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_DOWNLINK_PORT_PATH % (v, k), PerfConstants.DEFAULT_SYNC_TIME)
            if s2l._is_element_present(FusionInterconnectPage.ID_DOWNLINK_PORT_PATH % (v, k)):
                logging._log_to_console_and_log_file("verifying the profile %s,hardware %s for the interconnect %s " % (k, v, interconnectname))
                portnum = int(ui_lib.get_text(FusionInterconnectPage.ID_DOWNLINK_PORT % (v, k)))
                logging._log_to_console_and_log_file("Port num is %s" % portnum)

                ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_DOWNLINK_COLLAPSE % (v, k))

                """ Retrieving the each row data of a port """
                suboptions_count = len(s2l._current_browser().find_elements_by_xpath(".//*[@id='cic-ic-more-connectivity-downlinks-table']/tbody/tr[%s]/td/div" % (portnum + 1)))
                strflexnic = ui_lib.get_text(FusionInterconnectPage.ID_DOWNLINK_PORT_DETAILS % (portnum, 6))
                datadict["State"] = ui_lib.get_text(FusionInterconnectPage.ID_DOWNLINK_PORT_DETAILS % (portnum, 4))
                color = get_downlinkport_color(portnum)

                for i in range(3, suboptions_count + 1):
                    subopt_label = FusionInterconnectPage.ID_DOWNLINKS_SUBOPTIONS + "/label"
                    ui_lib.wait_for_element_and_click(subopt_label % (portnum + 1, i))
                    dataP = ui_lib.get_text(FusionInterconnectPage.ID_DOWNLINKS_SUBOPTIONS % (portnum + 1, i))
                    rowdata = dataP.split("\n")
                    if len(rowdata) <= 1:
                        logging._warn("Failed to select suboption")
                        fail = 1
                        continue

                    if rowdata[0].strip() == "Statistics":
                        if rowdata[1] == "No statistics":
                            fail = 1
                            continue

                        m = re.search("Transmitted errors (.*)", dataP)
                        if m:
                            datadict["Transmitted errors"] = m.group(1).strip()

                        m = re.search("Received errors (.*)", dataP)
                        if m:
                            datadict["Received errors"] = m.group(1).strip()

                    elif rowdata[0].strip() == "Advanced statistics":
                        if rowdata[1] == "No advanced statistics":
                            fail = 1
                            continue
                        m = re.search("input packets (.*)", dataP)
                        if m:
                            datadict["input packets"] = m.group(1).strip()
                        m = re.search("output packets (.*)", dataP)
                        if m:
                            datadict["output packets"] = m.group(1).strip()

                    elif rowdata[0].strip() == "VLAN IDs":
                        if rowdata[1] == "No VLAN IDs":
                            fail = 1
                            continue
                        comparedata = (rowdata[1].strip()).split()
                        if len(comparedata) == 2:
                            datadict["vlan"] = comparedata[1]
                            datadict["net"] = comparedata[0]
                        else:
                            datadict["vlan"] = comparedata[0]
                    ui_lib.wait_for_element_and_click(subopt_label % (portnum + 1, i))

            fex_port = net.fex + "/1/" + str(portnum)
            command = ["show interface ethernet " + fex_port, "show interface brief | grep " + fex_port]
            (fexdata, errorcode) = get_data_from_switch(net.switchip, command, net.username, net.password)
            if (errorcode[0] != 0 or errorcode[1] != 0):
                logging._warn("Failure when executing fex commands")
                fail = 1
            else:
                idx = 0
                for data in fexdata:

                    portdetail = "Ethernet" + fex_port
                    dataarray = data.split("\n")
                    match_string = ".*" + portdetail + " is (.*)"
                    m = re.match(match_string, dataarray[0])
                    if m:
                        if m.group(1).strip() == "up":
                            switchdict["State"] = "linked"
                        else:
                            switchdict["State"] = "unlinked"

                    if idx == 0:
                        for line in dataarray[19:]:
                            m = re.match("(.*)input packets", line)
                            if m:
                                print "matched input pkt"
                                switchdict["input packets"] = (m.group(1)).strip()

                            m = re.match("(.*)output packets", line)
                            if m:
                                print "matched output pkt"
                                switchdict["output packets"] = (m.group(1)).strip()

                            m = re.match("(.*)input error", line)
                            if m:
                                switchdict["Received errors"] = (m.group(1)).strip()

                            m = re.match("(.*)output error", line)
                            if m:
                                switchdict["Transmitted errors"] = (m.group(1)).strip()

                        idx = idx + 1
                    elif idx == 1:
                        vlan = dataarray[0].split()
                        switchdict["vlan"] = vlan[1]

            if (datadict["State"] == "linked" and color == "ok"):
                logging._log_to_console_and_log_file("The interconnect downlink port status color is set as expected")
            else:
                logging._warn("The interconnect downlink port status color is not set as expected")
                fail = 1

            if "net" in datadict.keys():
                if datadict["vlan"] != networklist[datadict["net"]]:
                    fail = 1

            for key in switchdict.keys():
                if key in datadict.keys():
                    if key == "input packets" or key == "output packets":
                        if (int(switchdict[key]) - int(datadict[key]) > 4000):
                            logging._warn("Value of %s from Switch (%s) does not match the value form One View (%s)" % (key, switchdict[key], datadict[key]))
                            fail = 1
                        else:
                            logging._log_to_console_and_log_file("Values of %s from  Switch (%s) approximately matches the value from One View (%s)" % (key, switchdict[key], datadict[key]))
                    else:
                        if datadict[key] == switchdict[key]:
                            logging._log_to_console_and_log_file("Values of %s from  Switch (%s) matches value from One View (%s)" % (key, switchdict[key], datadict[key]))

                        else:
                            logging._log_to_console_and_log_file("Values of %s from  Switch (%s) did not match value from One View (%s)" % (key, switchdict[key], datadict[key]))
                            fail = 1
                else:
                    logging._log_to_console_and_log_file("Obtained the value of %s from the Switch. One view does not display this information" % key)
                    fail = 1

            ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_DOWNLINK_COLLAPSE % (v, k))

    if fail != 0:
        logging._warn("One or more errors occured in the previous steps.")
        logging._log_to_console_and_log_file("\n-------------------")
        logging._warn("Test Failed :-(")
        logging._log_to_console_and_log_file("\n-------------------")
        return False
    else:
        logging._log_to_console_and_log_file("-------------------")
        logging._log_to_console_and_log_file("Test case successful!!")
        return True


def get_downlinkport_color(port_num):

    color_xpath = str("//*[@id='cic-ic-more-connectivity-downlinks-table']/tbody/tr[%s]/td[2]/div/span" % port_num)
    s2l = ui_lib.get_s2l()
    ui_lib.wait_for_element(color_xpath)
    el = s2l._element_find(color_xpath, True, True)
    color = ui_lib.get_webelement_attribute("innerHTML", el)
    return color


def verify_interconnect_uplink_port_view(*interconnect_obj):
    """ This function is to verify the uplink ports in interconnects page. As of now it has been tested only with FEX modules.
        For other interconnects, few validations may have to be changed.
        Example:
        | verify_interconnect_uplink_port_view(interconnect_obj)
        Input required to be provided in interconnect object :
        type [optional]   : fex/no fex [default : no fex]
        name              : Name of the interconenct
        portdata          : Which uplink is connected to which switch
        username/password : Switch username and password
        server            : List of server to which the interconnect is connected to. Separated by '|'
                            [as visible in the downlink supoption in uplink port]
        downlinkport      : List of Downlink ports connected to the interconnect. Separated by ','
                            [as visible in the downlink supoption in uplink port]

        Sample data :
        <interconnects>
        <interconnect name="SGH450X92W, interconnect 1" fex="190"
            server="SGH450X92W, bay 1|SGH450X92W, bay 2|SGH450X92W, bay 8" username="admin" password="Welcome@123" type="fex" enclname="SGH450X92W" downlinkport="9,10,16">
            <portdata>
            <uport port="1" switch="10.10.3.14"></uport>
            <uport port="2" switch="10.10.3.13"></uport>
            </portdata>
        </interconnect>
    </interconnects>
    """
    ''' Set the failure flag in the beginning to 0'''
    fail = 0
    selenium2lib = ui_lib.get_s2l()

    if not selenium2lib._is_element_present(FusionInterconnectPage.ID_PAGE_LABEL):
        navigate()
    for net in interconnect_obj:
        if hasattr(net, "type"):
            if net.type != "fex":
                logging._log_to_console_and_log_file("%s is a non fex module. Skipping the test" % net.name)
                return True
        else:
            logging._log_to_console_and_log_file("%s is a non fex module. Skipping the test" % net.name)
            return True
        if not select_interconnect(net.name):
            ui_lib.fail_test("Exiting  function, as the Interconnect %s is not selected " % net.name)
            return False
        if ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_LINK_GENERAL, PerfConstants.DEFAULT_SYNC_TIME):
            ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_OVERVIEW)
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_UPLINK_PORTS)

        ''' Populate the '''
        uplink_start = 1
        if ui_lib.wait_for_element(FusionInterconnectPage.ID_UPLINK_EXPANDER, 5):
            total_uplinks = int(len(selenium2lib._current_browser().find_elements_by_xpath(".//*[@id='cic-ic-more-connectivity-uplinks-table']//div[contains(@class, 'cic-li-more-connectivity-uplink-port-collapser')]")))
        datastore = ['Port', 'Type', 'State', 'Speed', 'Uplink Set', 'Connected To', 'Connector Type', 'Extended Identifier',
                     'Vendor', 'Part Number', 'Revision', 'RCType', 'RCPortType', 'PortID', 'Port description', 'System Name',
                     'System Description', 'System Capabilities', 'Transmitted errors', 'Received errors', 'btrt', 'btrr',
                     'ptrt', 'ptrr', 'output packets', 'input packets']
        suboptions = [('Connector', 1), ('Remote connection', 3), ('Downlinks', 4), ('Statistics', 7), ('Advanced statistics', 8)]
        dataoffset = {'Connector': 11, 'Remote connection': 18, 'Downlinks': 18, 'Statistics': 24, 'Advanced statistics': 26}
        datadict = {}
        downlinks = {}
        switchdict = {}
        fexdict = {}
        server = {}
        switchcon = {}
        for switchdata in net.portdata:
            switchcon[switchdata.port.strip()] = switchdata.switch.strip()

        command1 = "show fex " + net.fex + " transceiver"
        command = [command1]

        for uplinkport in range(uplink_start, total_uplinks + 1):

            switchdict.clear()
            datadict.clear()
            """Click on the port expander."""
            ui_lib.scroll_to_xpath((FusionInterconnectPage.XP_PORT_ROW % uplinkport), FusionInterconnectPage.XP_PORT_TABLE, FusionInterconnectPage.XP_UPLINK_PORTS_LABEL, FusionInterconnectPage.RAW_ID_CONTAINER_DIV)
            PORT_SELECTOR = ((FusionInterconnectPage.XP_PORT_ROW + FusionInterconnectPage.XP_PORT_OPENCLOSE) % uplinkport)
            ui_lib.wait_for_element_and_click(PORT_SELECTOR, PerfConstants.DEFAULT_SYNC_TIME)
            i = 0
            """ Extract the first row of port information after expanding. """
            color = get_color(uplinkport)

            for y in range(3, 9):
                PORT_DATA = ((FusionInterconnectPage.XP_PORT_ROW + FusionInterconnectPage.XP_PORT_DETAILS_TEMPLATE) % (uplinkport, y))
                data = ui_lib.get_text(PORT_DATA)
                datadict[datastore[i]] = data
                i = i + 1

            """ Click on the suboptions after selecting the port """
            for key, value in suboptions:

                ui_lib.wait_for_element_and_click((FusionInterconnectPage.XP_PORT_SUBOPTIONS % (uplinkport + 1, key)), PerfConstants.DEFAULT_SYNC_TIME)

                read_table = (FusionInterconnectPage.XP_PORT_DETAILS_ROW % (uplinkport + 1, value))
                ui_lib.wait_for_element_visible(read_table)
                dataP = ui_lib.get_text(read_table)
                dataP = dataP.strip()
                rowdata = str(dataP).split("\n")

                ''' If no data appears in UI '''
                if len(rowdata) <= 1:
                    logging._warn("Failed to select suboption %s" % key)
                    fail = 1
                    ''' Shift the index to capture the next option data'''
                    i = dataoffset[key]
                    ui_lib.wait_for_element_and_click((FusionInterconnectPage.XP_PORT_SUBOPTIONS % (uplinkport + 1, key)), PerfConstants.DEFAULT_SYNC_TIME)
                    continue

                ''' If the port is not linked, data will not be populates. Look for No connector etc '''
                match_text = r".*No " + key.lower()
                m = re.match(match_text, rowdata[1])
                if m:

                    if datadict["State"] == "linked":
                        logging._warn("Failed to display %s details of port %d" % (key, uplinkport))
                        fail = 1
                        i = dataoffset[key]
                    ui_lib.wait_for_element_and_click((FusionInterconnectPage.XP_PORT_SUBOPTIONS % (uplinkport + 1, key)), PerfConstants.DEFAULT_SYNC_TIME)
                    continue
                '''The below lines of code will extract the second line of data from the output and store it in datadict in the same
                order that is mentioned in datastore list.
                eg : For connector , the second line of data will be like. : "FET_10G 4 CISCO-TYCO 2231256-3 B"
                The same applies for Remote connection as well. But there is some more data to be validated also. '''

                if (key == 'Connector' or key == 'Remote connection'):
                    comparedata = rowdata[2].split(" ")
                    if key == 'Remote connection':
                        comparedata[3:5] = [" ".join(comparedata[3:5])]
                    for data in comparedata:
                        datadict[datastore[i]] = data
                        i = i + 1
                    if key == 'Remote connection':
                        ''' Store the System name, System Description, System Capabilities. '''
                        for index in range(3, 6):
                            comparedata = rowdata[index].split(" ")
                            datadict[datastore[i]] = " ".join(comparedata[2:])
                            i = i + 1
                if key == 'Downlinks':
                    ''' Store the port number and the Server bay information '''
                    if rowdata[1].strip() != "No downlinks":
                        for comparedata in rowdata[2:]:
                            downlinkdata = comparedata.split(" ")
                            downlinks[downlinkdata[0]] = " ".join(downlinkdata[1:])

                    else:
                        logging._log_to_console_and_log_file("No downlinks found!")
                if key == 'Statistics':
                    ''' Store the following values : Transmitted errors,Received errors,btrt, btrr, ptrt, ptrr '''
                    comparedata = rowdata[1].split(" ")
                    datadict[datastore[i]] = comparedata[2]
                    i = i + 1
                    comparedata = rowdata[2].split(" ")
                    datadict[datastore[i]] = comparedata[2]
                    i = i + 1
                    for index in [4, 5, 9, 10]:
                        comparedata = rowdata[index].split(" ")
                        datadict[datastore[i]] = comparedata[3]
                        i = i + 1

                if key == 'Advanced statistics':
                    ''' Store output and input packets'''
                    m = re.search("input packets (.*)", dataP)
                    if m:
                        datadict["input packets"] = m.group(1).strip()
                    m = re.search("output packets (.*)", dataP)
                    if m:
                        datadict["output packets"] = m.group(1).strip()
                    i = i + 2

                ui_lib.wait_for_element_and_click((FusionInterconnectPage.XP_PORT_SUBOPTIONS % (uplinkport + 1, key)), PerfConstants.DEFAULT_SYNC_TIME)
            if str(uplinkport) in switchcon.keys():
                (fexdata, errorcode) = get_data_from_switch(switchcon[str(uplinkport)], command, net.username, net.password)

                if errorcode[0] != 0:
                    logging._warn("Failure when executing show fex command")
                    fail = 1
                for key in fexdata:
                    fexdataarray = key.split("\n\n")
                fexdict = get_connector_data(fexdataarray[uplinkport - 1])
            else:
                fexdict['PortID'] = ""
                fexdict['Port'] = str(uplinkport)
            if datadict['Connected To'] != "":
                m = re.match(".* \((.*)\)", datadict['Connected To'])
                portdetail = m.group(1)
            else:
                portdetail = fexdict['PortID']
            ''' Collect the data from the switch into the switchdict dictionary'''
            if portdetail != "":
                switchdict = get_fex_data_from_switch_and_store(switchcon[str(uplinkport)], portdetail, net.fex, net.username, net.password)
            else:
                switchdict['State'] = "unlinked"
            switchdict = dict(switchdict.items() + fexdict.items())
            ''' Match the values from switch and one view'''

            logging._log_to_console_and_log_file("\n-------------------")
            logging._log_to_console_and_log_file("Validating Port %d" % uplinkport)
            logging._log_to_console_and_log_file("\n-------------------")
            for key1 in datastore:
                if (key1 in switchdict.keys() and key1 in datadict.keys()):
                    if (key1 == "output packets" or key1 == "input packets"):
                        if (int(datadict[key1]) - int(switchdict[key1]) > 1000):
                            logging._warn("Value of %s from Switch (%s) does not match the value form One View (%s)" % (key1, switchdict[key1], datadict[key1]))
                        else:
                            logging._log_to_console_and_log_file("Values of %s from  Switch (%s) approximately matches the value from One View (%s)" % (key1, switchdict[key1], datadict[key1]))
                    elif switchdict[key1].lower() != datadict[key1].lower():
                        logging._warn("Value of %s from Switch (%s) does not match the value form One View (%s)" % (key1, switchdict[key1], datadict[key1]))
                        fail = 1
                    else:
                        logging._log_to_console_and_log_file("Values of %s from  Switch (%s) matches value from One View (%s)" % (key1, switchdict[key1], datadict[key1]))

            ''' Compare downlink port values '''
            if ((datadict["State"] == "linked" and color == "ok") or (datadict["State"] == "unlinked" and color == "disabled")):
                logging._log_to_console_and_log_file("The interconnect port status color is set as expected")
            else:
                logging._warn("The interconnect port status color is not set as expected")
                fail = 1
            if (net.server != "" and datadict["State"] == "linked"):
                downlink = 1
                portlist = net.downlinkport.split(",")
                serverlist = net.server.split("|")
                ind = 0
                for downlinkport in portlist:
                    server[downlinkport.strip()] = serverlist[ind].strip()
                    ind = ind + 1
                for key1 in downlinks:
                    if key1 in server.keys():
                        if downlinks[key1] != server[key1]:
                            fail = 1
                            downlink = (downlink and 0)
                        else:
                            downlink = (downlink and 1)
                    else:
                        downlink = (downlink and 0)
                        fail = 1
                if downlink != 1:
                    logging._warn("The value of downlink ports shown by One View did not match the expected value")
                    fail = 1
                else:
                    logging._log_to_console_and_log_file("Downlink ports from One View matched the expected value")

            ''' Close the port '''

            ui_lib.scroll_to_xpath((FusionInterconnectPage.XP_PORT_ROW % uplinkport), FusionInterconnectPage.XP_PORT_TABLE, FusionInterconnectPage.XP_UPLINK_PORTS_LABEL, FusionInterconnectPage.RAW_ID_CONTAINER_DIV)
            ui_lib.wait_for_element_and_click(PORT_SELECTOR, PerfConstants.DEFAULT_SYNC_TIME)
            BuiltIn().sleep(5)
        if fail != 0:
            logging._warn("One or more errors occured in the previous steps.")
            logging._log_to_console_and_log_file("\n-------------------")
            logging._warn("Test Failed :-(")
            logging._log_to_console_and_log_file("\n-------------------")
            return False
        else:
            logging._log_to_console_and_log_file("-------------------")
            logging._log_to_console_and_log_file("Test case successful!!")
            logging._log_to_console_and_log_file("-------------------")
            return True


def get_connector_data(fexarray):
    ''' Get the connector details ans store it in the dictionary '''
    fexdict = {}
    uplinkdata = fexarray.split("\n")
    for line in uplinkdata:
        line = line.strip()
        if line:
            fexdata = line.split(" ")
            if fexdata[1] == 'Uplink:':
                fexdict["Port"] = fexdata[-1]
            elif fexdata[0] == 'Fabric':
                fexdict["PortID"] = fexdata[-1]
                if fexdict["PortID"] == "--":
                    fexdict["PortID"] = ""
            elif fexdata[0] == 'type':
                fexdict["Connector type"] = fexdata[-1]
            elif fexdata[0] == 'name':
                fexdict["Vendor"] = fexdata[-1]
            elif fexdata[0] == 'Part':
                fexdict["Part Number"] = fexdata[-1]
            elif fexdata[0] == 'revision':
                fexdict["Revision"] = fexdata[-1]
            elif fexdata[1] == 'extended':
                fexdict["Extended Identifier"] = fexdata[-1]
    return fexdict


def get_color(port_num):

    color_xpath = str("//*[@id='cic-ic-more-connectivity-uplinks-table']/tbody/tr[%d]/td[2]/div/span" % port_num)
    s2l = ui_lib.get_s2l()
    ui_lib.wait_for_element(color_xpath)
    el = s2l._element_find(color_xpath, True, True)
    color = ui_lib.get_webelement_attribute("innerHTML", el)
    return color


def get_fex_data_from_switch_and_store(switchip, portdetail, fexnum, uname, pwd):
    ''' Login to the switch and collect the port data of a required interconnect. Following command is run :
    show interface <interface>
    We collect the statistics like port state, input and output packets, Transmitted and received errors.
    Some data that are static in UI are populated directly. eg : RC Type, System Name etc
    input : switch ip, fex port for which details are required, Fex association of interconenct, switch username and password
    Return : A dictionary with data collected from switch
    '''
    switchdict = {}
    command1 = "show interface " + portdetail
    commands = [command1]
    (datalist, errorcodelist) = get_data_from_switch(switchip, commands, uname, pwd)
    for data in datalist:
        dataarray = data.split("\n")
        match_string = ".*" + portdetail + " is (.*)"
        m = re.match(match_string, dataarray[0])
        if m:
            if (m.group(1)).strip() == 'up':
                switchdict["State"] = "linked"
            else:
                switchdict["State"] = "unlinked"
        m = re.match(".* (.*?), address: (.*?) ", dataarray[2])
        if m:
            print "Matched address and type "
            switchdict["RCPortType"] = "Ethernet"
            mac = m.group(2).replace(".", "")
            final_mac = ":".join(mac[i:i + 2] for i in range(0, len(mac), 2))

            final_mac = final_mac + " (" + portdetail + ")"
            print "final mac is %s" % final_mac
            switchdict["Connected To"] = final_mac

        for line in dataarray[3:]:
            m = re.match(".*Port mode is (.*)", line)
            if m:
                if (m.group(1)).strip() == 'fex-fabric':
                    switchdict["Type"] = "Fabric Extender"
                    switchdict["RCType"] = "External"
                    switchdict["System Name"] = "Cisco"
                    switchdict["System Capabilities"] = "bridge,router"
            m = re.match(".* (.*) Gb/s, media type", line)
            if m:
                print "Matched speed %s" % m.group(1)
                switchdict["Speed"] = (m.group(1)).strip()
            m = re.match("(.*)input packets", line)
            if m:
                print "matched input pkt"
                switchdict["input packets"] = (m.group(1)).strip()
            m = re.match("(.*)output packets", line)
            if m:
                print "matched output pkt"
                switchdict["output packets"] = (m.group(1)).strip()
            m = re.match("(.*)input error", line)
            if m:
                print "matched imput error"
                switchdict["Received errors"] = (m.group(1)).strip()
                print line
                print m.group(1)
            m = re.match("(.*)output error", line)
            if m:
                print "matched output error"
                switchdict["Transmitted errors"] = (m.group(1)).strip()
                print line
                print m.group(1)
    return switchdict


def add_label_to_interconnect(*interconnect_list):
    """ add label to Interconnect
        This function is to add label to Interconnect
        Example:
            add_label_to_interconnect(*interconnect_list)
    """
    s2l = ui_lib.get_s2l()
    logger._log_to_console_and_log_file("Function call to add label to logical interconnect ")

    if isinstance(interconnect_list, test_data.DataObj):
        interconnect_list = [interconnect_list]
    elif isinstance(interconnect_list, tuple):
        interconnect_list = list(interconnect_list)[0]

    if not ui_lib.wait_for_element(FusionInterconnectPage.ID_PAGE_LABEL):
        navigate()

    for interconnect_label in interconnect_list:
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_RESET)
        if not select_interconnect(interconnect_label.interconnect):
            return False

        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_DROPDOWN)
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_DROPDOWN_SELECT_LABEL)

        logger._log_to_console_and_log_file("Adding label to logicalinterconnect '{0}'".format(interconnect_label.interconnect))
        if ui_lib.wait_for_element(FusionInterconnectPage.ID_EDIT_LABEL):
            ui_lib.move_to_element_and_click(FusionInterconnectPage.ID_LABEL, FusionInterconnectPage.ID_EDIT_LABEL)
            if ui_lib.wait_for_element(FusionInterconnectPage.ID_EDIT_LABEL_PANEL):
                ui_lib.wait_for_element_and_input_text(FusionInterconnectPage.ID_LABEL_NAME, interconnect_label.name)
                ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_ADD_LABEL_BTN)
                ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_OK_LABEL_BTN)
            else:
                logger.warn("Failed to navigate edit label panel")
                return False
        else:
            logger.warn("Could not find Edit button to add label")

        if ui_lib.wait_for_element(FusionInterconnectPage.ID_ADDED_LABEL % interconnect_label.name):
            ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_ADDED_LABEL % interconnect_label.name)
            interconnect_lists = []
            ui_lib.wait_for_element(FusionInterconnectPage.ID_ALL_INTERCONNECT_LIST, PerfConstants.FUSION_PAGE_SYNC)
            interconnect_lists = [ui_lib.get_text(s) for s in s2l._element_find(FusionInterconnectPage.ID_ALL_INTERCONNECT_LIST, False, False)]
            for interconnect in interconnect_lists:
                if interconnect == interconnect_label.interconnect:
                    logger._log_to_console_and_log_file("Label {0} is successfully added to the logicalinterconnect '{1}'".format(interconnect_label.name, interconnect_label.interconnect))
        else:
            logger.warn("Failed to add label to the selected logicalinterconnect")
            return False
    return True


def verify_interconnect_recent_activity(interconnectname, message_list):
    '''
    Function to verify if all the activity messages passed in the message list are seen in the Interconnect activity page
    returns false if any one of the messages are not found
    Returns true if all messages are found
    '''
    found = 0
    timeago = ''
    num_message = len(message_list)
    logger.info("length of the message count in the message list is %s" % num_message)
    logger.info("interconnect name %s " % interconnectname)
    logger.info("message list '%s' " % message_list)

    # if not in Interconnects page navigate
    navigate()

    # select the given interconnect
    if not select_interconnect(interconnectname, timeout=30):
        ui_lib.fail_test("Exiting navigate to drop down menus function, as the Interconnect %s is not present " % interconnectname)
        return False

    FusionUIBase.select_view_by_name('Activity', timeout=30)
    # filter 'todays' activity messages and check
    CommonOperationInterconnects.click_activity_filter_all_time()
    CommonOperationInterconnects.select_activity_filter_date("today", 10)
    CommonOperationInterconnects.click_activity_resource_view()

    for message in message_list:
        logger.info("message is %s " % message)
        timeago = ''
        CommonOperationInterconnects.click_activity_resource_view(25)
        # look for the activity message in last two hours
        if CommonOperationInterconnects.click_activity_message(message, 20, fail_if_false=False):
            # mouse over the event time to make it visible
            timeago = CommonOperationInterconnects.get_time_activity_message(message)
            timeago = timeago.split(' ')
            logger.info("\nTime of Event -  '%s'" % ' '.join(timeago))
            found += 1
            logger.info("found message count %s" % found)
            logger.info("Activity : '%s'  found in IC activity page" % message)
            # check if the time the event was generated is within the last 2 hours , else discard it
            if timeago[1].lower() == "hours" and int(timeago[0]) > 2:
                logger.warn("Expected message %s found is not within  last 2 hours!! Discarding Old activity Message" % message)
                continue
            elif timeago[1].lower() in ("months", "year", "years"):
                logger.warn("Expected message '{}' found is of '{}'!!".format(message, timeago))
                continue
        else:
            logger.warn("Expected message '%s' is not found in activity page:" % message)

    # return true if all messages are found else return false
    if found == num_message:
        logger.info("All the expected messages are found in Interconnect Activity page")
        return True
    else:
        logger.warn("One or more messages not found in Interconnect Activity page ")
        ui_lib.fail_test("All expected messages are not found in ICM activity page", True)


def get_interconnect_state(icname):
    '''
    function to get the IC state
    Takes the ic name as input
    Retunrs None if the IC is not found OR if the State cannot be retrieved
    '''
    # navigate to interconnects page
    navigate()
    # select the given interconnect
    if not select_interconnect(icname, timeout=60):
        ui_lib.fail_test("Exiting navigate to drop down menus function, as the Interconnect %s is not present " % icname)
    # goto general section of the IC , if not already there
    FusionUIBase.select_view_by_name('General', timeout=30)
    # get the IC state
    ic_state = CommonOperationInterconnects.get_overview_ic_state()
    return ic_state


def get_ic_stacking_domain_role(icname):
    '''
    function to get the stacking domain role of the IC
    '''
    ic_stacking_domain_role = None
    if not ui_lib.wait_for_element(FusionInterconnectPage.ID_PAGE_LABEL):
        navigate()

    # select the given interconnect
    if not select_interconnect(icname):
        ui_lib.fail_test("Exiting navigate to drop down menus function, as the Interconnect %s is not present " % icname)
        return None

    # goto general section of the IC , if not already there
    if not ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_IC_GENERAL_SECTION, PerfConstants.DEFAULT_SYNC_TIME):
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_OVERVIEW, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_GENERAL, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_IC_GENERAL_SECTION, 20)

    if ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_IC_STACKING_DOMAIN_ROLE):
        ic_stacking_domain_role = ui_lib.get_text(FusionInterconnectPage.ID_IC_STACKING_DOMAIN_ROLE, PerfConstants.DEFAULT_SYNC_TIME)
    else:
        logging._warn("No Stacking Role found for ic : {}".format(icname))
    return ic_stacking_domain_role


def get_ic_ipv4_address(icname):
    '''
    Function to ge the ipv4 address assigned to the IC
    returns None if not found and logs error message
    '''

    ipv4_address = None
    # interconnects page navigation
    navigate()
    # select the given interconnect
    if not select_interconnect(icname):
        return None
    # goto general section of the IC , if not already there
    FusionUIBase.select_view_by_name('General', timeout=30)
    ipv4_address = CommonOperationInterconnects.get_ic_ipv4_addr()
    if ipv4_address:
        logger.info("ipv4 address of the selected interconnect %s" % ipv4_address)
    else:
        logger.warn("No ipv4 address found for ic : {}".format(icname))
    return ipv4_address


def fusion_ui_chloride_power_off(*chl_obj):
    "[LEGACY]"
    """
        This function perform power off of the Chloride ICM on Synergy 12000 Frames.
    """

    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionInterconnectPage.ID_PAGE_LABEL):
        base_page.navigate_base(FusionInterconnectPage.ID_PAGE_LABEL,
                                FusionInterconnectPage.ID_LINK_INTERCONNECT,
                                "css=span.hp-page-item-count")

    if isinstance(chl_obj, test_data.DataObj):
        chl_obj = [chl_obj]
    elif isinstance(chl_obj, tuple):
        chl_obj = list(chl_obj[0])
    errorcount = 0
    for chl in chl_obj:
        logging._info("\nPerforming operation on Interconnect %s..." % chl.name)
        if(chl.name == ""):
            logging._warn("Mandatory field - name can't be empty")
            continue
        if ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_ELEMENT_IC_LIST % chl.name):
            logging._info("Valid Interconnect Module%s" % chl.name)
        else:
            logging._warn("Not able to locate Interconnect Module %s" % chl.name)
            continue

        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_IC_ACTION_MAIN_BTN, 15)
        if not ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_MENU_ACTION_POWEROFF, 15):
            logging._info("Power Off option is not visible")
            return False
        if ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_IC_INTERCONNECT_POPUP_CONFIRM_BOX, 10):
            logging._warn("Confirming power off step")
            ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_IC_CONFRIM_POWER_OFF)
        wait_time = 30 * 1

        if ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_IC_PAGE_TOP_MESSAGE_HEADER, wait_time):
            message = selenium2lib.get_text(FusionInterconnectPage.ID_IC_PAGE_TOP_MESSAGE_DETAIL)
            logging._info("\nPower off action message - %s" % message)

        else:
            ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_IC_PAGE_TOP_MESSAGE_SUMMARY)
            message = selenium2lib.get_text(FusionInterconnectPage.ID_IC_MESSAGE_ERROR)
            logging._info("\nPower off action message - %s" % message)
            return False

        wait_time = 30
        # Check ICM is off in general section
        logging._info("Verifying ICM power status in general page")
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_MENU_SELECTOR, wait_time)
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_IC_MENU_GENERAL, wait_time)
        ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_IC_GENERAL_CONTENT, wait_time)

        if not ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_MENU_ACTION_POWERON, wait_time):
            logging._warn("Power Off option is visible")
            errorcount = errorcount + 1

        power_state = selenium2lib.get_text(FusionInterconnectPage.ID_IC_POWER_STATE)
        module_state = selenium2lib.get_text(FusionInterconnectPage.ID_IC_STATE)
        logging._info("\nInterconnect power state - %s \nInterconnect state - %s" % (power_state, module_state))

        # Check Power off link in action menu
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_MENU_ACTION_MAIN_BTN, wait_time)
        if power_state is "On":
            logging._warn("Interconnect Power state in general view is wrong")
            errorcount = errorcount + 1
        logging._info("Verifying Interconnect power state in EM")
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        port = 22  # SSH Port to establish connection
        client.connect(chl.appip, port, chl.appuname, chl.apppassw)
        channel = client.invoke_shell()
        stdin = channel.makefile('wb')
        stdout = channel.makefile('rb')

        # For DCS
        if chl.dcs.lower() == 'yes':
            cmd = "curl -ik https://%s/rest/v1/Managers/20%s | grep } | python -m json.tool" % (chl.EMipv6, chl.ICBay)
        else:
            # Get XAUTH token of EM to use with EM RIS request
            xauth_cmd = "/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s %s -o t" % (chl.enclosurename)
            XAUTH = execute_cmd(chl.appip, 22, chl.appuname, chl.apppassw, xauth_cmd)
            logging._info("\n XAUTH is [%s]" % (XAUTH.rstrip()))
        # For real Em
            cmd = 'curl --globoff -ki -x "" --request GET --header "x-auth-token:%s" https://%s/rest/v1/InterconnectManager/%s | grep } | python -m json.tool' % (XAUTH.rstrip(), chl.EMipv6, chl.ICBay)
            logging._info("\n cmd is [%s]" % (cmd))
        input, output, error = client.exec_command(cmd)
        data = output.read()
        data = data.split("\n")

        em_power_state = ""
        for line in data:
            if '"PowerState":' in line:
                temp, em_power_state = line.split(":")
        if em_power_state is "On":
            logging._warn("Interconnect Power state in EM is wrong")
            errorcount = errorcount + 1
        else:
            logging._info("Interconnect Power state in EM is matching with OneView")
        # Check the Color/health status of interconnect
        ui_lib.refresh_browser(FusionInterconnectPage.ID_IC_UID_OFF, 15)
        if ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_HEALTH_COLOR, 18):
            logging._info("Interconnect Health changed to Red")
        else:
            logging._warn("Interconnect Health did not change to Red. It is Green")
            errorcount = errorcount + 1
        this_message = 'Interconnect ' + chl.name + ' has been powered off'
        a_data = list_active_events()
        if this_message in a_data:
            logging._info("Respective alert is found")
        else:
            logging._warn("Respective alert is not found")
    if errorcount > 0:
        return False
    return True


def fusion_ui_chloride_reset(*chl_obj):
    "[LEGACY]"
    """
        This function reset the Chloride ICM on Synergy 12000 Frame
    """

    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionInterconnectPage.ID_PAGE_LABEL):
        base_page.navigate_base(FusionInterconnectPage.ID_PAGE_LABEL,
                                FusionInterconnectPage.ID_LINK_INTERCONNECT,
                                "css=span.hp-page-item-count")

    if isinstance(chl_obj, test_data.DataObj):
        chl_obj = [chl_obj]
    elif isinstance(chl_obj, tuple):
        chl_obj = list(chl_obj[0])

    errorcount = 0
    # selenium2lib._current_browser().refresh()
    selenium2lib.reload_page()

    for chl in chl_obj:
        logging._info("\nPerforming operation on Interconnect %s..." % chl.name)

        if(chl.name == ""):
            logging._warn("Mandatory field - name can't be empty")
            continue
        if ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_ELEMENT_IC_LIST % chl.name):
            logging._info("Valid Interconnect %s" % chl.name)
        else:
            logging._warn("Not able to locate Interconnect %s" % chl.name)
            errorcount += 1
            continue

        # Issue Reset request
        # Wait for a while to make sure the page is loaded with selected Interconnect. This is to give enough time to
        # display action menu items correctly

        wait_time = 10
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_MENU_ACTION_MAIN_BTN, wait_time)
        if not ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_IC_ACTION_RESET):
            logging._info("Reset option is not visible")
            return False
        else:
            wait_time = 10
            if ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_IC_RESET_STATUS, wait_time):
                logging._info("Retset action is successfull")
            else:
                logging._info("Reset failed")
                errorcount += 1
            if ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_IC_RESET_MESSAGE, wait_time):
                if ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_IC_PROGRESS_BAR, wait_time):
                    logging._warn("Reset Action is in progress from a long time ")
                    logging._warn("Reset Action failed")
                    errorcount += 1
                else:
                    ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_MESSAGE_SUMMARY_TEXT)
                    ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_MESSAGE_DEATILS_TEXT, 2)
                    message = selenium2lib.get_text(FusionInterconnectPage.ID_MESSAGE_DEATILS_TEXT)
                    logging._info("Reset Action message - %s" % message)

            ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_MENU_ACTION_MAIN_BTN)
            if not ui_lib.wait_for_element_visible("link=Reset", 3):
                logging._warn("Reset option is not visible")
                logging._warn("Wrong behavior of reset request, possibly the interconnect went down-Powered off")
                errorcount += 1

    if errorcount > 0:
        return False
    return True


def fusion_ui_chloride_power_on(*chl_obj):
    "[LEGACY]"
    """
        This function perform power off of the Chloride ICM on Synergy 12000 Frame
    """

    selenium2lib = ui_lib.get_s2l()

    if not selenium2lib._is_element_present(FusionInterconnectPage.ID_PAGE_LABEL):
        base_page.navigate_base(FusionInterconnectPage.ID_PAGE_LABEL,
                                FusionInterconnectPage.ID_LINK_INTERCONNECT,
                                "css=span.hp-page-item-count")

    if isinstance(chl_obj, test_data.DataObj):
        chl_obj = [chl_obj]
    elif isinstance(chl_obj, tuple):
        chl_obj = list(chl_obj[0])

    errorcount = 0

    for chl in chl_obj:
        logging._info("\nPerforming operation on Interconnect %s..." % chl.name)

        if(chl.name == ""):
            logging._warn("Mandatory field - name can't be empty")
            continue

        if ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_ELEMENT_IC_LIST % chl.name):
            logging._info("Valid Interconnect %s" % chl.name)
        else:
            logging._warn("Not able to locate Interconnect %s" % chl.name)
            continue

        # Issue power On request to Interconnect (Chloride/Potash)

        wait_time = 30
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_MENU_ACTION_MAIN_BTN, wait_time)
        if not ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_MENU_ACTION_POWERON, wait_time):
            logging._info("Power On option is not visible")
            return False
        if ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_POWER_ON_MESSAGE, wait_time):
            if ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_IC_UID_STATUS_COMPLETE, wait_time):
                ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_MESSAGE_SUMMARY_TEXT, wait_time)
                ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_MESSAGE_DEATILS_TEXT, wait_time)
                message = selenium2lib.get_text(FusionInterconnectPage.ID_MESSAGE_DEATILS_TEXT)
                logging._info("Power On Action successful")
                logging._info("Power On Action message - %s" % message)
            else:
                ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_MESSAGE_SUMMARY_TEXT, wait_time)
                message = selenium2lib.get_text(FusionInterconnectPage.ID_MESSAGE_DEATILS_TEXT)
                logging._info("Power On Action failed")
                logging._info("Power On Action message - %s" % message)
                errorcount = errorcount + 1
        # Check ICM is ON in general section
        logging._info("Verifying ICM power status in general page")
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_MENU_SELECTOR_1, wait_time)
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_IC_MENU_GENERAL, wait_time)
        ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_IC_GENERAL_CONTENT, wait_time)

        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_MENU_ACTION_MAIN_BTN, wait_time)
        if not ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_MENU_ACTION_POWEROFF, wait_time):
            logging._warn("Power ON option is visible")
            errorcount = errorcount + 1

        power_state = selenium2lib.get_text(FusionInterconnectPage.ID_IC_POWER_STATE)
        module_state = selenium2lib.get_text(FusionInterconnectPage.ID_IC_STATE)
        logging._info("Interconnect Power state - %s \nInterconnect state - %s" % (power_state, module_state))

        if power_state is 'Off':
            logging._warn("Interconnect Power state in general view is wrong")
            errorcount = errorcount + 1

        logging._info("Verifying ICM power status in EM")
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        port = 22  # SSH Port to establish connection
        client.connect(chl.appip, port, chl.appuname, chl.apppassw)
        channel = client.invoke_shell()
        stdin = channel.makefile('wb')
        stdout = channel.makefile('rb')

        # To get Power status from EM
        if chl.dcs.lower() == 'yes':
            # For DCS EM
            cmd = "curl -ik https://%s/rest/v1/Managers/20%s | grep } | python -m json.tool" % (chl.EMipv6, chl.ICBay)
        else:
            # Get XAUTH of EM to use with EM RIS request
            xauth_cmd = '/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s %s -o t' % (chl.enclosurename)
            XAUTH = execute_cmd(chl.appip, 22, chl.appuname, chl.apppassw, xauth_cmd)
            logging._info("\n XAUTH is %s" % (XAUTH))
        # For Real EM
            cmd = 'curl --globoff -ki -x "" --request GET --header "x-auth-token:%s" https://%s/rest/v1/InterconnectManager/%s | grep } | python -m json.tool' % (XAUTH.rstrip(), chl.EMipv6, chl.ICBay)
        input, output, error = client.exec_command(cmd)
        data = output.read()
        data = data.split("\n")
        EmPowerState = ""
        for line in data:
            if '"PowerState":' in line:
                temp, EmPowerState = line.split(":")
        if EmPowerState is 'Off':
            logging._warn("\nInterconnect Power state in EM is wrong")
            errorcount = errorcount + 1
        else:
            logging._warn("\nInterconnect Power state in EM is matching with OneView")
        ui_lib.refresh_browser(FusionInterconnectPage.ID_IC_UID_ON, 15)
        if ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_HEALTH_GREEN_COLOR, 13):
            logging._info("Interconnect Health changed to Green")
        else:
            logging._warn("\nInterconnect Health did not change to Green. It is Red")
            errorcount = errorcount + 1
    if errorcount > 0:
        return False
    return True


def fusion_ui_chloride_uid_action(*chl_obj):
    "[LEGACY]"
    """
        This function perform UID LED off and ON of the Chloride ICM on Synergy 12000 Frame
    """

    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionInterconnectPage.ID_PAGE_LABEL):
        base_page.navigate_base(FusionInterconnectPage.ID_PAGE_LABEL,
                                FusionInterconnectPage.ID_LINK_INTERCONNECT,
                                "css=span.hp-page-item-count")

    if isinstance(chl_obj, test_data.DataObj):
        chl_obj = [chl_obj]
    elif isinstance(chl_obj, tuple):
        chl_obj = list(chl_obj[0])

    selenium2lib.reload_page()
    errorcount = 0
    message = ""

    for chl in chl_obj:
        logging._info("\nPerforming operation on Interconnect %s..." % chl.name)

        if(chl.name == ""):
            logging._warn("Mandatory field - name can't be empty")
            continue

        if ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_ELEMENT_IC_LIST % chl.name):
            logging._info("Valid Interconnect %s" % chl.name)
        else:
            logging._warn("Not able to locate Interconnect %s" % chl.name)
            continue
        # Wait for a while to load page content
        # Collect current UID stattus
        # ui_lib.refresh_browser(FusionInterconnectPage.ID_IC_UID_ON, 15)
        ui_lib.refresh_browser(FusionInterconnectPage.ID_IC_UID_CONTROL, 15)
        if ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_IC_UID_ON, 15):
            Current_UID_State = 'Lit'
            Expected_UID_State = 'Off'
            logging._info("Performing UID Off operation")
        elif ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_IC_UID_OFF, 15):
            Current_UID_State = 'Off'
            Expected_UID_State = 'Lit'
            logging._info("Performing UID On operation")
        else:
            Current_UID_State = 'Unknown'
        wait_time = 30
        if ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_IC_UID_CONTROL, wait_time):
            logging._info("UID Action successful")
        else:
            logging._info("UID action failed")
            return False
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        port = 22  # SSH Port to establish connection
        client.connect(chl.appip, port, chl.appuname, chl.apppassw)
        channel = client.invoke_shell()
        stdin = channel.makefile('wb')
        stdout = channel.makefile('rb')
        if chl.dcs.lower() == 'yes':
            # For DCS EM
            cmd = "curl -ik https://%s/rest/v1/Managers/20%s | grep } | python -m json.tool" % (chl.EMipv6, chl.ICBay)
        else:
            # Get XAUTH of EM to use with EM RIS request
            xauth_cmd = '/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s %s -o t' % (chl.enclosurename)
            XAUTH = execute_cmd(chl.appip, 22, chl.appuname, chl.apppassw, xauth_cmd)
            logging._info("\n XAUTH is %s" % (XAUTH))
        # For real EM
            cmd = 'curl --globoff -ki -x "" --request GET --header "x-auth-token:%s" https://%s/rest/v1/InterconnectManager/%s | grep } | python -m json.tool' % (XAUTH.rstrip(), chl.EMipv6, chl.ICBay)
        input, output, error = client.exec_command(cmd)
        data = output.read()
        data = data.split("\n")
        for line in data:
            if '"IndicatorLED":' in line:
                temp, EmIndicatorLED = line.split(":")

        if Current_UID_State is 'Off':
            if Expected_UID_State in EmIndicatorLED:
                logging._info("\nUID Status in EM is matching with OneView")
            else:
                logging._warn("UID Status %s in UI is not matching with EM status %s" % (Current_UID_State, EmIndicatorLED[2:5]))
                errorcount = errorcount + 1

        if Current_UID_State is 'Lit':
            if Expected_UID_State in EmIndicatorLED:
                logging._info("\nUID Status in EM is matching with OneView")
            else:
                logging._warn("UID Status %s in UI is not matching with EM status %s" % (Current_UID_State, EmIndicatorLED[2:5]))
                errorcount = errorcount + 1
    if errorcount > 0:
        return False
    return True


def chloride_extender_ports(interconnect_obj):
    """
        This function perform chloride interconnect CXP port validation on Synergy 12000 Frame
    """

    FusionUIBase.navigate_to_section(SectionType.INTERCONNECTS)
    fail_time = 0
    for interconnect in interconnect_obj:
        logger.info("\nPerforming operation on Interconnect %s..." % interconnect.name)

        if(interconnect.name is ""):
            FusionUIBase.fail_test_or_return_false("Mandatory field - name can't be empty", False)
            fail_time += 1
            continue
        if not VerifyInterconnects.verify_interconnect_exist(interconnect.name, timeout=5, fail_if_false=False):
            FusionUIBase.fail_test_or_return_false("interconnect '%s' does not exist" % interconnect.name, False)
            fail_time += 1
            continue
        else:
            logger.info("interconnect '%s' exist" % interconnect.name)

        if not select_interconnect(interconnect.name):
            FusionUIBase.fail_test_or_return_false("Exiting  function, as the Interconnect %s is not selected " % interconnect.name, False)
            fail_time += 1
            continue

        # Collect extender port information
        prod_name = CommonOperationInterconnects.get_overview_product_name(5, False)
        logger.info("Product Name is: %s" % prod_name)

        # to get power state
        power_state = CommonOperationInterconnects.get_overview_power_state(5, False)
        logger.info("Power state is: %s" % power_state)
        ports = []
        linked = []
        unlinked = []

        ports_to_check = []
        linked_ports = []
        unlinked_ports = []
        total_no_of_ports = []
        order_of_ports = []
        alert_msgs = []
        port_count = 0
        mouse_over_status = {}
        mouse_over_connected_to = {}
        mouse_over_state = {}

        ui_dict = {"Color": [], "Port": [], "State": [],
                   "Type": [], "Connected To": [],
                   "Speed": [], "Vendor": [], "Vendor OUI": [],
                   "Part number": [], "Revision": [], "Serial number": []}
        ic_dict = {"Type": [], "Speed": [], "Vendor": [], "Vendor OUI": [],
                   "Part number": [], "Revision": [], "Serial number": []}

        logging.info("Clicking Extender port")
        FusionUIBase.select_view_by_name('Interconnect Link Ports')
        if VerifyInterconnects.verify_interconnect_link_ports_label():

            logging.info("Getting ports information")
            ports_data = InterconnectLinkPorts.get_port_table_information(5, False)
            linked, unlinked, ports_to_check = _get_linked_unlinked_ports_information(ports_data, order_of_ports, port_count)
            logger.info("linked ports are %s" % linked)
            logger.info("Unlinked ports are %s" % unlinked)
            logger.info("order of ports are %s" % ports_to_check)
            port_count = -1
            for item in ports_to_check:
                port_count = port_count + 1
                sub_port = int(item)
                logging._info("ports_to_check %s" % ports_to_check)
                i = 1
                (port_status, connected, connector_present_ov, connectedport, ui_dict) = _get_connector_information_from_ov(sub_port, i, 5, False)
                logger.info("connected port %s " % connectedport)
                i = 0

                for element in ui_dict:
                    logging._info("\t%s - %s " % (element, ui_dict[element]))
                # Get CXP port details from Interconnect
                #
                blk = str(163 + port_count)
                print blk
                connector_present = ""
                encl_name = []
                bay_no = interconnect.ICBay
                encl_name = interconnect.enclosurename

                cls = em_operation.EMCLIKeywords()
                (connector_present, ic_dict) = cls.get_connector_information_from_em(interconnect.dcs, encl_name, interconnect.appip, interconnect.appuname, interconnect.apppassw, interconnect.EMipv6, bay_no, blk, power_state, prod_name, port_count)
                logging.info('connector_present %s' % connector_present)
                if connector_present is "0":
                    printline = "\n------------------------------------------------------------------"
                    for key in ui_dict:
                        if key in ic_dict:
                            if(ui_dict[key] != ic_dict[key]):
                                logging._info(printline)
                                logging._warn("Following paramters are not matching with EM-Interconnects data")
                                logging._warn("EM IC parameter    - %s and value - %s" % (key, ic_dict[key]))
                                logging._warn("Appliance parameter - %s and value - %s" % (key, ui_dict[key]))
                            else:
                                logging._info(printline)
                                logging._info("\nPassed: EM Data and Appliance parameter %s is matching " % key)
                                logging._info(printline)
                elif(connector_present_ov == 1):
                    logger.info("Expected froM OV and EM:There is no connector is inserted into port %s" % port_dct["Port"])
                else:
                    logging._warn("There is no connector is inserted into port %s" % ui_dict["Port"])

    if (fail_time > 0):
        raise AssertionError("failed to perform CXP port validation on Synergy 12000 Frame for one or more interconnects")
    else:
        return True


def execute_cmd(appip, port, appuname, apppassw, cmd):
    """
        This function establishes SSH session with target system
        and executes given commands. This returns the output of the
        command
    """
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    port = 22  # SSH Port to establish connection
    client.connect(appip, port, appuname, apppassw)
    channel = client.invoke_shell()
    stdin = channel.makefile('wb')
    stdout = channel.makefile('rb')
    input, output, error = client.exec_command(cmd)
    data = output.read()
    return data


def get_canmic_block(appip, port, appuname, apppassw, cmd):
    """
        This function reads CANMIC blocks from EM using EM IPV6
    """
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    port = 22  # SSH Port to establish connection
    client.connect(appip, port, appuname, apppassw)
    channel = client.invoke_shell()
    stdin = channel.makefile('wb')
    stdout = channel.makefile('rb')
    logging._info("cmd %s" % cmd)
    input, output, error = client.exec_command(cmd)
    data = output.read()
    d = data.split("\n")
    mdata = []

    for k in d:
        head, sep, tail = k.partition('|')
        head = head[10:].split(" ")
        mdata = mdata + head
    return filter(None, mdata)


def list_active_events():
    """
    This function will return list of alerts messages which is marked as active

    """
    logging._info("\nNow collecting the alerts ")

    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionInterconnectPage.ID_DASHBOARD_ACTIVITY):
        base_page.navigate_base(FusionInterconnectPage.ID_DASHBOARD_ACTIVITY,
                                FusionInterconnectPage.ID_LINK_ACTIVITY,
                                "css=span.hp-page-item-count")

    ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_ACTIVITY_FILTER, 5)
    # Select Active filter and read all listed active alerts
    ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_ACTIVITY_FILTER_ACTIVE, 5)
    activity_data = ui_lib.get_text(FusionInterconnectPage.ID_ACTIVITY_FILTERED_CONTENT,)
    return activity_data


def fusion_ui_collect_le_support_dump(*le_obj):
    "[LEGACY]"
    """
        This function perform collects LE support dump on Synergy 12000 Frame

    """
    logging._info("Create and download Logical Enclosure Support Dump")

    if isinstance(le_obj, test_data.DataObj):
        le_obj = [le_obj]
    elif isinstance(le_obj, tuple):
        le_obj = list(le_obj[0])

    wait_time = 20
    for le in le_obj:
        if not fusion_ui_select_logical_enclosure(le.name):
            logging._warn("Given logical enclosure is not selected %s" % le.name)
            continue
        dump_status = False
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_IC_ACTION_MAIN_BTN, 3)
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_LE_SUPPORT_DUMP, 3)
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LE_CREATE_DUMP_CONFIRMATION_WINDOW, 5)
        if (le.encryption.lower() is "yes"):
            ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LE_DUMP_ENABLE_ENCRYPTION, 5)
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LE_MENU_ACTION_CREATE_SUPPORT_DUMP, 3)
        # ui_lib.wait_for_element_and_click("//*[@id='hp-activity-control']/div[1]")
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_IC_CLICK_ACTIVITY, wait_time)
        # PerfConstants.LOGICALINTERCONNECT_SUPPORT_DUMP
        if ui_lib.wait_for_element(FusionInterconnectPage.ID_IC_TIMESTAMP_SUPPORT_DUMP, wait_time):
            logging._info("Creation of support dump started")
            if ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_IC_VALIDATE_SUCCESS, 700):
                logging._info("Support dump created successfully")
                logging._info("Validating created LE support dump")
                dump_status = validate_support_dump(le.uname, le.password, le.appip, le.icmbay, le.scriptpath)
            else:
                logging._info("Creation of Support dump failed")
        else:
            logging._info("Support dump not yet started")
    return dump_status


def fusion_ui_select_logical_enclosure(lename):
    """
        Tis function Selects Logical Enclosure
    """
    logging._info("Selecting Logical Enclosures - %s" % lename)

    selenium2lib = ui_lib.get_s2l()

    if not selenium2lib._is_element_present(FusionInterconnectPage.ID_LE_PAGE_LABEL):
        base_page.navigate_base(FusionInterconnectPage.ID_LE_PAGE_LABEL,
                                FusionInterconnectPage.ID_LINK_LE,
                                "css=span.hp-page-item-count")

    if ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_ELEMENT_LE_SELECT_NAME % lename, PerfConstants.DEFAULT_SYNC_TIME):
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_ELEMENT_LE_SELECT_NAME % lename)
        return True
    else:
        logging._warn("Logical Enclosures - %s is not present at Logical Enclosures Page" % lename)
        return False


def fusion_ui_chloride_general_view(*chl_obj):
    """
        This function perform validation of general view attributes of Chloride on Synergy 12000 Frame
    """
    if isinstance(chl_obj, test_data.DataObj):
        chl_obj = [chl_obj]
    elif isinstance(chl_obj, tuple):
        chl_obj = list(chl_obj[0])

    navigate()

    ui_dict = {"Product name": [], "Location": [],
               "Serial number": [], "Part number": [], "Firmware Version": []}
    switch_dict = {"Product name": [], "Location": [],
                   "Serial number": [], "Part number": [], "Firmware Version": []}

    for chl in chl_obj:
        if select_interconnect(chl.name):
            logger.info("Selecting Interconnect - %s" % chl.name)
        else:
            logger.info("Not able to locate Interconnect %s" % chl.name)
            continue

        logger.info("clicking Hardware view to get the hardware details ")
        FusionUIBase.select_view_by_name('Hardware')
        # Get Product name
        ui_dict["Product name"] = CommonOperationInterconnects.get_overview_product_name()
        # Get Serial Number
        ui_dict["Serial number"] = CommonOperationInterconnects.get_hardware_serial_number()
        # Get Part number
        ui_dict["Part number"] = CommonOperationInterconnects.get_hardware_part_number()
        # Get Firmware version detail
        logger.info("clicking general view to get firmware version ")
        FusionUIBase.select_view_by_name('General')
        ui_dict["Firmware Version"] = CommonOperationInterconnects.get_hardware_firmware_version()

        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        port = 22  # SSH Port to establish connection
        client.connect(chl.appip, port, chl.appuname, chl.apppassw)
        channel = client.invoke_shell()
        stdin = channel.makefile('wb')
        stdout = channel.makefile('rb')

        if hasattr(chl, 'dcs'):
            if chl.dcs.lower() == 'yes':
                # For DCS EM
                cmd = "curl -ik https://%s/rest/v1/Interconnects/%s/InterconnectFru | grep } | python -m json.tool" % (chl.EMipv6, chl.ICBay)
            else:
                # For real EM
                xauth_cmd = '/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s %s -o t' % (chl.enclosurename)
                input1, output1, error1 = client.exec_command('/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s %s' % (chl.enclosurename))
                XAUTH = execute_cmd(chl.appip, 22, chl.appuname, chl.apppassw, xauth_cmd)
                cmd = 'curl --globoff -ki -x "" --header "x-auth-token:%s" https://%s/rest/v1/InterconnectFru/%s | grep } | python -m json.tool' % (XAUTH.rstrip(), str.strip(output1.read() + "%bond0"), chl.ICBay)
        input, output, error = client.exec_command(cmd)
        data = output.read()
        data = data.split("\n")
        for line in data:
            if '"SerialNumber":' in line:
                temp, SerilaNumber = line.split(":")
                switch_dict["Serial number"] = SerilaNumber

            if '"PartNumber":' in line:
                temp, PartNumber = line.split(":")
                switch_dict["Part number"] = PartNumber

            if '"Model":' in line:
                temp, PartName = line.split(":")
                switch_dict["Product name"] = PartName.strip(' "')

        # Get Firmware version
        if hasattr(chl, 'dcs'):
            if chl.dcs.lower() == 'yes':
                # For DCS EM
                cmd = "curl -ik https://%s/rest/v1/Managers/20%s | grep } | python -m json.tool" % (chl.EMipv6, chl.ICBay)
            else:
                # For real EM
                xauth_cmd = '/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s %s -o t' % (chl.enclosurename)
                input1, output1, error1 = client.exec_command('/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s %s' % (chl.enclosurename))
                XAUTH = execute_cmd(chl.appip, 22, chl.appuname, chl.apppassw, xauth_cmd)
                cmd = 'curl --globoff -ki -x "" --header "x-auth-token:%s" https://%s/rest/v1/InterconnectManager/%s | grep } | python -m json.tool' % (XAUTH.rstrip(), str.strip(output1.read() + "%bond0"), chl.ICBay)
        input, output, error = client.exec_command(cmd)
        logger.info("cmd %s" % cmd)
        data = output.read()
        logger.info("data %s" % data)
        data = data.split("\n")
        for line in data:
            if '"FirmwareVersion":' in line:
                parts = line.split(":")
                switch_dict["Firmware Version"] = (parts[1].split(" ")[1])[1:].strip('",')
        # switch_dict["Location"] = chl.name

        for key in ui_dict:
            if not ui_dict[key] in switch_dict[key]:
                logger.warn("Parameter is not matching")
                logger.warn("UI Parameter - %s value - %s" % (key, ui_dict[key]))
                logger.warn("Switch Parameter - %s value - %s" % (key, switch_dict[key]))
                ui_lib.fail_test("failing the test since attributes are not matching", True)


def fusion_ui_chloride_check_priv(*chl_obj):
    """
        This function checks the capabilities of different user
    """
    if isinstance(chl_obj, test_data.DataObj):
        chl_obj = [chl_obj]
    elif isinstance(chl_obj, tuple):
        chl_obj = list(chl_obj[0])

    action_menu = ""
    power_off = ""
    power_on = ""
    reset = ""
    errorcount = 0
    message = ""
    # Check session user name
    logger.info("checking the User name")
    current_user = GeneralUserandGroups.get_current_username(10, fail_if_false=False)
    logger.debug("current user is %s" % current_user)
    if (current_user == "backupadmin" or current_user == "serveradmin"):
        status = navigate()
        logger.info("status - %s" % status)
        if (status is False):
            errorcount = errorcount + 1
            logger.warn("Failed - %s do not have permission to access Interconnect" % current_user)
        else:
            logger.info("Passed - %s have permission to access Interconnect" % current_user)

        for chl in chl_obj:
            logger.info("\nChecking permission for Interconnect -  %s..." % chl.name)

            if select_interconnect(chl.name):
                logger.info("Selecting Interconnect - %s" % chl.name)
            else:
                logger.info("Not able to locate Interconnect %s" % chl.name)
                continue
            CommonOperationInterconnects.click_logical_interconnect_action_button()
            status = VerifyInterconnects.verify_actions_noauthorization()
            if (status is True):
                logger.info("Passed - User do not have permission to perform power on/off/reset operations")
                action_menu = "Failed"
            else:
                logger.warn("Failed - Action Button is visible for this user")
                errorcount = errorcount + 1
                action_menu = "Passed"
            # return the action menu data for the user backupadmin or networkadmin
            return_data = [action_menu]

    if (current_user == "networkadmin"):
        status = navigate()
        logger.info("status - %s" % status)
        if (status is False):
            errorcount = errorcount + 1
            logger.warn("Failed - %s do not have permission to access Interconnect" % current_user)
        else:
            logger.info("Passed - %s have permission to access Interconnect" % current_user)

        for chl in chl_obj:
            logger.info("\nChecking permission for Interconnect -  %s..." % chl.name)

            if select_interconnect(chl.name):
                logger.info("Selecting Interconnect - %s" % chl.name)
            else:
                logger.info("Not able to locate Interconnect %s" % chl.name)
                continue

            if CommonOperationInterconnects.click_logical_interconnect_action_button():
                logger.info("Passed - Action Button is visible for this user")
                action_menu = "Passed"
            else:
                logger.info("Passed - Action Button is not visible for this user")
                errorcount = errorcount + 1
                action_menu = "Failed"

            if VerifyInterconnects.verify_actions_power_off_button():
                logger.info("Passed - Power Off option is visible for this user")
                power_off = "Passed"
            else:
                logger.warn("Failed - Power Off option is not visible for this user")
                errorcount = errorcount + 1
                power_off = "Failed"

            if VerifyInterconnects.verify_actions_reset_button():
                logger.info("Passed - Reset option is visible for this user")
                reset = "Passed"
            else:
                logger.warn("Failed - Reset option is not visible for this user")
                errorcount = errorcount + 1
                reset = "Failed"

            if VerifyInterconnects.verify_actions_power_button():
                logger.info("Passed - Power on option is visible for this user")
                power_on = "Passed"
            else:
                logger.warn("Failed - Power on option is not visible for this user")
                errorcount = errorcount + 1
                power_on = "Failed"

            # return the action menu poweroff rest refresh data for the user serveradmin
    return_data = [action_menu, power_on, power_off, reset]
    if errorcount > 0:
        return False, return_data
    return True, return_data


def validate_support_dump(uname, psword, hostip, baynumber, script_path):
    """
    This function validates generated support dump on Appliance
    The argument it expects are
        - uname = "root"           -- Appliance user name
        - hostip = "15.212.160.224"-- Appliance IP
        - psword = "hpvse1"        -- Appliance pswd
        - baynumber = 6            -- ICM Bay
    """
    validated = False  # Initially assume the support dump file is not valid

    f1 = script_path + '\\' + 'decrypt-support-dump.sh'
    f2 = script_path + '\\' + 'private.key'
    f3 = script_path + '\\' + 'check_dump.py'
    f4 = script_path + '\\' + 'do_cleanup.py'
    f5 = script_path + '\\' + 'EncryptionUtil-0.0.1-SNAPSHOT.jar'

    sftp = pysftp.Connection(host=hostip, port=22, username=uname, password=psword)
    with sftp.cd('/var/'):
        sftp.mkdir('ledump', mode=777)
        with sftp.cd('/var/ledump/'):
            sftp.put(f1)
            sftp.put(f2)
            sftp.put(f3)
            sftp.put(f5)
        with sftp.cd('/var/'):
            sftp.put(f4)
            sftp.chmod('/var/ledump/decrypt-support-dump.sh', 777)
            sftp.chmod('/var/ledump/check_dump.py', 777)
            sftp.chmod('/var/do_cleanup.py', 777)
    cmd = "python /var/ledump/check_dump.py " + str(baynumber)
    data = execute_cmd(hostip, 22, uname, psword, cmd)
    logging._info("---------------------Checking decrypted dump file-------------------------------")
    d = sftp.listdir("/var/ledump/")
    sftp.close()
    for i in d:
        if "validated_support_dump" in i:
            validated = True
        if "multiple_sdmp_files" in i:
            logging._info("There are multiple sdmp files")
            validate = False
    if validated is True:
        logging._info("Validation of support dump successeded")
        result = True
    else:
        logging._info("Validation of support dump failed")
        result = False

    data = execute_cmd(hostip, 22, uname, psword, "python /var/do_cleanup.py")
    return result


def verify_tbird_ic_version(em_ipv6addresses, em_serial_number, interconnect_bay, cim_ipv4_address, cim_uname="root", cim_psswd="hpvse1", dcs=False):
    '''
    Function to connect to CI Manager/Oneview and get the firmware version of the interconect bay specified.

    Function get the authentication token from the EM and gets the firmware of the interconnect bay specified.

    Returns NOne if no data is retrieved else returns the IC firmware version installed

    -- Pass Active,standby EM ipv6 ips as comma seperated string .This is when user is not aware of the active and standby EM
    --Command is run on either to get the version info.Only Active EM returns output.
    '''

    # ssh to the Oneview/CIM IP specified
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    port = 22  # SSH Port to establish connection
    client.connect(cim_ipv4_address, port, username=cim_uname, password=cim_psswd)
    channel = client.invoke_shell()
    stdin = channel.makefile('wb')
    stdout = channel.makefile('rb')

    # check if dcs or real hardware
    if bool(dcs):
        # provide the dcs EM ipv6 ips as a comma seperated string
        # For DCS EM
        em_ip_list = em_ipv6addresses.split(',')
        cmd_to_run = r"curl --tlsv1.2 -ik https://%s/rest/v1/Managers/20%s | grep } | python -m json.tool | grep FirmwareVersion"
        # form a comand list to run on each EM
        cmd_list = [cmd_to_run % (em_ipv6, str(interconnect_bay)) for em_ipv6 in em_ip_list]

    else:
        # For real hardware
        # Connect to the CImanager and generate Authentication token for the EM
        getAuth_token = r"/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s  %s -o t" % em_serial_number
        logging._log_to_console_and_log_file("Generating Authentication token using command - '{}'".format(getAuth_token))
        input, output, error = client.exec_command(getAuth_token)
        auth_token = output.read()

        logging._log_to_console_and_log_file("Authentication Token Generated for EM {} - {}".format(em_serial_number, auth_token))
        em_ip_list = em_ipv6addresses.split(',')
        cmd_to_run = r'curl --tlsv1.2 -ik -H "x-auth-token:%s" https://%s/rest/v1/InterconnectManager/%s | grep } | python -m json.tool | grep FirmwareVersion'
        # form a comand list to run on each EM
        cmd_list = [cmd_to_run % (auth_token.strip().strip('\n'), em_ipv6, str(interconnect_bay)) for em_ipv6 in em_ip_list]

    data = ''
    for cmd in cmd_list:
        # execute each command and check output
        input, output, error = client.exec_command(cmd)
        data = output.read()
        data = data.strip()
        # if output is not empty store and break
        if data not in (None, ''):
            logging._log_to_console_and_log_file("Running Command '{}' on IC bay - {}".format(cmd, interconnect_bay))
            break
    logging._log_to_console_and_log_file("Command Output is - '%s'" % data)
    client.close()
    m = re.match("\"FirmwareVersion\": \"(.*)\",", data)
    if m:
        logging._log_to_console_and_log_file("Firmware version returned from IC is : %s" % (m.group(1)))
        return m.group(1).strip()
    return None


def verify_ic_installed_baseline_firmware_versions(interconnectname):
    '''
    Function to check ifthe installed version and the baselined versions displayed in the IC page are the same.
    Returns boolean True/False
    '''
    ic_installed_firmware = None
    ic_baseline_firmware = None

    # if not in Interconnects page navigate
    if not ui_lib.wait_for_element(FusionInterconnectPage.ID_PAGE_LABEL):
        navigate()

    # select the given interconnect
    if not select_interconnect(interconnectname):
        logging._warn("Exiting navigate to drop down menus function, as the Interconnect %s is not present " % interconnectname)
        return False

    # goto general section of the IC , if not already there
    if not ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_IC_GENERAL_SECTION, 10):
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_OVERVIEW, 10)
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_GENERAL, 10)
        ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_IC_GENERAL_SECTION, 20)

    if not ui_lib.wait_for_element(FusionInterconnectPage.ID_IC_GENERAL_SECTION):
        logging._warn("Failed to load General section for interconnect - {}".format(interconnectname))
        return False

    # get the ic installed firmware version
    ic_installed_firmware = ui_lib.get_text(FusionInterconnectPage.ID_IC_INSTALLED_FIRMWARE, PerfConstants.DEFAULT_SYNC_TIME)
    # get the ic baseline version
    ic_baseline_firmware = ui_lib.get_text(FusionInterconnectPage.ID_IC_INSTALLED_FIRMWARE, PerfConstants.DEFAULT_SYNC_TIME)

    # compare the two
    if ic_baseline_firmware and ic_installed_firmware:
        if ic_installed_firmware.lower() in ic_baseline_firmware.lower():
            logging._log_to_console_and_log_file("The installed and Baseline Firmware Version for IC {} are same : {}".format(interconnectname, ic_installed_firmware))
        else:
            logging._warn("The installed firmware version '{}' and Baseline firmware Version '{}' for IC {} are Not same!".format(ic_installed_firmware, ic_baseline_firmware, interconnectname))
            return False
    else:
        logging._warn("Unable to get the Installed and Baseline firmware version for ic {}".format(interconnectname))
        return False

    return True


def get_icm_data_from_em(*inc_obj):
    """
        This function establishes ssh session to EM and retrieves InterconnectFRU and general data into a dictionary
        The curl commands are executed on a target machine EM in this case, after establishing ssh session to EM through OV appliance
    """
    if isinstance(inc_obj, test_data.DataObj):
        inc_obj = [inc_obj]
    elif isinstance(inc_obj, tuple):
        inc_obj = list(inc_obj[0])
    selenium2lib = ui_lib.get_s2l()
    switch_dict = {"Productname": [],
                   "Serialnumber": [], "Partnumber": [], "FirmwareVersion": [],
                   "PowerState": [], "UidState": []}
    for inc in inc_obj:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        port = 22
        client.connect(inc.appip, port, inc.appuname, inc.apppassw)
        channel = client.invoke_shell()
        stdin = channel.makefile('wb')
        stdout = channel.makefile('rb')
        if inc.dcs == 'yes':
            # For DCS EM
            cmd = "curl -ik https://%s/rest/v1/Interconnects/%s/InterconnectFru | grep } | python -m json.tool" % (inc.emipv6, inc.icbay)
        else:
            # For real EM
            xauth_cmd = '/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s %s -o t' % (inc.enclosurename)
            xauth = execute_cmd(inc.appip, 22, inc.appuname, inc.apppassw, xauth_cmd)
            cmd = 'curl --globoff -ki -x "" --header "x-auth-token:%s" https://%s/rest/v1/InterconnectFru/%s | grep } | python -m json.tool' % (xauth.rstrip(), inc.emipv6, inc.icbay)
            input, output, error = client.exec_command(cmd)
            data = output.read()
            data = data.split("\n")
            for line in data:
                if '"SerialNumber":' in line:
                    temp, SerialNumber = line.split(":")
                    switch_dict["Serialnumber"] = SerialNumber.strip(' "')
                    logger.info("Serialnumber %s " % line)
                if '"PartNumber":' in line:
                    parts = line.split(":")
                    switch_dict["Partnumber"] = (parts[1].split(" ")[1])[1:].strip('",')
                    logger.info("Partnumber %s" % line)
                if '"Model":' in line:
                    temp, PartName = line.split(":")
                    switch_dict["Productname"] = PartName.strip(' "')
                    logger.info("Productname %s" % line)
            # Get Firmware version, powerstate and UID state
            if inc.dcs.lower() == 'yes':
                # For DCS EM
                cmd = "curl -ik https://%s/rest/v1/Managers/20%s | grep } | python -m json.tool" % (inc.emipv6, inc.icbay)
            else:
                # For real EM
                xauth_cmd = '/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s %s -o t' % (inc.enclosurename)
                xauth = execute_cmd(inc.appip, 22, inc.appuname, inc.apppassw, xauth_cmd)
                cmd = 'curl --globoff -ki -x "" --header "x-auth-token:%s" https://%s/rest/v1/InterconnectManager/%s | grep } | python -m json.tool' % (xauth.rstrip(), inc.emipv6, inc.icbay)
            input, output, error = client.exec_command(cmd)
            data = output.read()
            data = data.split("\n")
            for line in data:
                if '"FirmwareVersion":' in line:
                    parts = line.split(":")
                    switch_dict["FirmwareVersion"] = (parts[1].split(" ")[1])[1:].strip('",')
                    logger.info("line %s " % line)
                if '"PowerState":' in line:
                    temp, EmPowerState = line.split(":")
                    EmPowerState = EmPowerState.split(",")
                    switch_dict["PowerState"] = str(EmPowerState[0])
                    logger.info("line %s " % line)
                if '"IndicatorLED":' in line:
                    temp, EmIndicatorLED = line.split(":")
                    EmIndicatorLED = EmIndicatorLED.split(",")
                    switch_dict["UidState"] = str(EmIndicatorLED[0])
            logger._log_to_console_and_log_file("Switch Dict is %s" % switch_dict)
    return switch_dict


def get_ic_power_state(interconnectname):
    '''
    function to get the interconnect power state
    Returns None if not found
    '''
    # if not in Interconnects page navigate
    if not ui_lib.wait_for_element(FusionInterconnectPage.ID_PAGE_LABEL):
        navigate()

    # select the given interconnect
    if not select_interconnect(interconnectname):
        logging._warn("Exiting navigate to drop down menus function, as the Interconnect %s is not present " % interconnectname)
        return None

    ic_power_state = None

    # goto general section of the IC , if not already there
    if not ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_IC_GENERAL_SECTION, 10):
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_OVERVIEW, 10)
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_LINK_GENERAL, 10)
        ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_IC_GENERAL_SECTION, 20)

    if not ui_lib.wait_for_element(FusionInterconnectPage.ID_IC_GENERAL_SECTION):
        logging._warn("Failed to load General section for interconnect - {}".format(interconnectname))
        return None

    ic_power_state = ui_lib.get_text(FusionInterconnectPage.ID_IC_POWER_STATE, PerfConstants.DEFAULT_SYNC_TIME)

    return ic_power_state


def verify_interconnect_hyperlinks(interconnects_obj):
    """
        This function will validate all of the hyperlinks between the interconnect and the enclosure that it is
        installed in.

        Arguments:
            <interconnects>
                <interconnect>
                    name*                           -- In Interconnects Table, name of Interconnect
                    enclosure*                      -- In Interconnects Overview/Hardware view, name of enclosure minus
                                                       interconnect bay #
                    logical_interconnect            -- In Interconnects OverView view, Logical interconnect field
                    interconnect_power              -- In Interconnects Overview/General view, Interconnect power field
                    state                           -- In Interconnects Overview/General view, State field
                    installed_firmware_version      -- In Interconnects Overview/General view, Installed firmware
                                                       version field
                    ipv4                            -- In Interconnects General view, IPv4 field
                    ipv6                            -- In Interconnects General view, IPv6 field
                    <hardware>
                        product_name                -- In Interconnects Overview/Hardware view, Product name field
                        location*                   -- In Interconnects Overview/Hardware view, Location field
                        serial_number               -- In Interconnects Overview/Hardware view, Serial number field
                        part_number                 -- In Interconnects Overview/Hardware view, Part number field
                        bay*                        -- In Interconnects Overview/Hardware view, Location bay number
                    <internal_ports>
                        <port>
                            number                  -- In Interconnects Internal ports view, Port number
                            state                   -- In Interconnects Internal ports view, State field
                            connects_to             -- In Interconnects Internal ports view, Connects to field
                            model                   -- In Interconnects Internal ports view, Model field
                            profile                 -- In Interconnects Internal ports view, Server profile field


        *Required Arguments

        Example:
            <interconnects>
                <interconnect name="0000A66101, interconnect 1"
                              enclosure="0000A66101"
                              logical_interconnect="none"
                              interconnect_power="On"
                              state="Monitored"
                              installed_firmware_version="0.1.7.31"
                              ipv4=" 172.18.9.101 static"
                              ipv6=" fe80::5265:f3ff:fedf:248 link-local ">
                    <hardware product_name="HPE Synergy 12Gb SAS Connection Module"
                              location="0000A66101, interconnect bay 1"
                              serial_number="2M220100SL"
                              part_number="752953-001"
                              bay="1"/>
                    <internal_ports>
                        <port number="1" state="Linked" connects_to="0000A66101, bay1, I/O Adapter 1:1" model="HPE Synergy D3940 Storage Module" profile="n/a"/>
                        <port number="2" state="Linked" connects_to="0000A66101, bay1, I/O Adapter 1:2" model="HPE Synergy D3940 Storage Module" profile="n/a"/>
                        <port number="3" state="Unlinked" connects_to="" model="" profile="n/a"/>
                        <port number="4" state="Unlinked" connects_to="" model="" profile="n/a"/>
                        <port number="5" state="Unlinked" connects_to="" model="" profile="n/a"/>
                        <port number="6" state="Unlinked" connects_to="" model="" profile="n/a"/>
                        <port number="7" state="Unlinked" connects_to="" model="" profile="n/a"/>
                        <port number="8" state="Unlinked" connects_to="" model="" profile="n/a"/>
                        <port number="9" state="Unlinked" connects_to="" model="" profile="n/a"/>
                        <port number="10" state="Unlinked" connects_to="" model="" profile="n/a"/>
                        <port number="11" state="Unlinked" connects_to="" model="" profile="n/a"/>
                        <port number="12" state="Unlinked" connects_to="" model="" profile="n/a"/>
                    </internal_ports>
                </interconnect>
            </interconnects>

    """
    logger.info("\nVerify Interconnect Hyperlinks")

    navigate()

    for n, ic_obj in enumerate(interconnects_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(interconnects_obj), '-' * 14))
        logger.info("Verifying hyperlinks for an interconnect with name %s" % ic_obj.name)
        if not select_interconnect(ic_obj.name):
            ui_lib.fail_test("Interconnect [ %s ] not selected" % ic_obj.name)

        if hasattr(ic_obj, "hardware"):
            hardware_obj = ic_obj.hardware[0]
            if hasattr(hardware_obj, "location") and hasattr(ic_obj, "enclosure"):

                # Verify Interconnects Overview Location Hyperlink
                FusionUIBase.select_view_by_name('Overview')
                logger.info("Verify Interconnect Overview Location hyperlink, expected value %s" % hardware_obj.location)

                if VerifyInterconnects.verify_hardware_location(hardware_obj.location):
                    logger.info("Interconnect Overview Location verified, navigate to enclosure %s" % ic_obj.enclosure)

                # Click Interconnects Overview Location Hyperlink
                CommonOperationInterconnects.click_enclosure()

                if _BaseCommonOperationEnclosures.wait_enclosure_selected(ic_obj.enclosure, timeout=10):
                    logger.info("Interconnect Overview Location hyperlink verified successfully")

                # Verify Enclosures Overview Rear View Hyperlink and click
                logger.info("Verify Enclosure Rear view Hyperlink")
                FusionUIBase.wait_for_element_and_click("link=%s" % ic_obj.name, timeout=5, fail_if_false=True)

                if CommonOperationInterconnects.wait_interconnect_selected(ic_obj.name, timeout=10):
                    logger.info("Enclosure Overview Rear view hyperlink verified successfully")

                # Verify Interconnects Hardware Location Hyperlink
                FusionUIBase.select_view_by_name("Hardware")
                logger.info("Verify Interconnect Hardware Location hyperlink, expected value %s" % hardware_obj.location)

                if VerifyInterconnects.verify_hardware_location(hardware_obj.location):
                    logger.info("Interconnect Hardware Location verified, navigate to enclosure %s" % ic_obj.enclosure)

                # Click Interconnects Hardware Location Hyperlink
                CommonOperationInterconnects.click_enclosure()

                if _BaseCommonOperationEnclosures.wait_enclosure_selected(ic_obj.enclosure, timeout=10):
                    logger.info("Interconnect Hardware Location hyperlink verified successfully")

                # Verify Enclosure Interconnects Hyperlink
                if hasattr(hardware_obj, "bay"):
                    FusionUIBase.select_view_by_name("Interconnects")
                    logger.info("Verify Enclosures Interconnect hyperlink, expected value %s" % ic_obj.name)

                    if TBirdVerifyEnclosures.verify_interconnect_interconnect(hardware_obj.bay, ic_obj.name):
                        logger.info("Enclosure Interconnect hyperlink verified, navigate to Interconnect %s" % ic_obj.name)

                    # Click Enclosure Interconnects Hyperlink
                    _BaseCommonOperationEnclosures.click_interconnect_interconnect(hardware_obj.bay)

                    if CommonOperationInterconnects.wait_interconnect_selected(ic_obj.name, timeout=10):
                        logger.info("Enclosure Interconnect hyperlink verified successfully")
                else:
                    ui_lib.fail_test("No attribute 'bay' found, ensure attribute is present")
            else:
                ui_lib.fail_test("Attributes not found, ensure attributes 'location' and 'enclosure' are present")
        else:
            ui_lib.fail_test("No list object 'hardware' present, ensure list object is present")


def validate_natasha_interconnect_user_permissions(user_role, interconnects_obj):
    """
        The function will validate the user permissions for Natasha Interconnects in the Action Menu based on the user
        role that is passed in.

        Arguments:
            user_role*                               -- In User and Groups, User role field

            <interconnects>
                <interconnect>
                    name*                           -- In Interconnects Table, name of Interconnect
                    enclosure                       -- In Interconnects Overview/Hardware view, name of enclosure minus
                                                       interconnect bay #
                    logical_interconnect            -- In Interconnects OverView view, Logical interconnect field
                    interconnect_power              -- In Interconnects Overview/General view, Interconnect power field
                    state                           -- In Interconnects Overview/General view, State field
                    installed_firmware_version      -- In Interconnects Overview/General view, Installed firmware
                                                       version field
                    ipv4                            -- In Interconnects General view, IPv4 field
                    ipv6                            -- In Interconnects General view, IPv6 field
                    <hardware>
                        product_name                -- In Interconnects Overview/Hardware view, Product name field
                        location                    -- In Interconnects Overview/Hardware view, Location field
                        serial_number               -- In Interconnects Overview/Hardware view, Serial number field
                        part_number                 -- In Interconnects Overview/Hardware view, Part number field
                        bay                         -- In Interconnects Overview/Hardware view, Location bay number
                    <internal_ports>
                        <port>
                            number                  -- In Interconnects Internal ports view, Port number
                            state                   -- In Interconnects Internal ports view, State field
                            connects_to             -- In Interconnects Internal ports view, Connects to field
                            model                   -- In Interconnects Internal ports view, Model field
                            profile                 -- In Interconnects Internal ports view, Server profile field


        *Required Arguments

        Example:
            user_role="Storage administrator"

            <interconnects>
                <interconnect name="0000A66101, interconnect 1"
                              enclosure="0000A66101"
                              logical_interconnect="none"
                              interconnect_power="On"
                              state="Monitored"
                              installed_firmware_version="0.1.7.31"
                              ipv4="none"
                              ipv6="none">
                    <hardware product_name="HPE Synergy 12Gb SAS Connection Module"
                              location="0000A66101, interconnect bay 1"
                              serial_number="2M220100SL"
                              part_number="752953-001"
                              bay="1"/>
                    <internal_ports>
                        <port number="1" state="Linked" connects_to="0000A66101, bay1, I/O Adapter 1:1" model="HPE Synergy D3940 Storage Module" profile="n/a"/>
                        <port number="2" state="Linked" connects_to="0000A66101, bay1, I/O Adapter 1:2" model="HPE Synergy D3940 Storage Module" profile="n/a"/>
                        <port number="3" state="Unlinked" connects_to="" model="" profile="n/a"/>
                        <port number="4" state="Unlinked" connects_to="" model="" profile="n/a"/>
                        <port number="5" state="Unlinked" connects_to="" model="" profile="n/a"/>
                        <port number="6" state="Unlinked" connects_to="" model="" profile="n/a"/>
                        <port number="7" state="Unlinked" connects_to="" model="" profile="n/a"/>
                        <port number="8" state="Unlinked" connects_to="" model="" profile="n/a"/>
                        <port number="9" state="Unlinked" connects_to="" model="" profile="n/a"/>
                        <port number="10" state="Unlinked" connects_to="" model="" profile="n/a"/>
                        <port number="11" state="Unlinked" connects_to="" model="" profile="n/a"/>
                        <port number="12" state="Unlinked" connects_to="" model="" profile="n/a"/>
                    </internal_ports>
                </interconnect>
            </interconnects>

    """

    logger.info("\nVerify Actions Menu for %s" % user_role)

    navigate()

    # Select Interconnect
    for n, ic_obj in enumerate(interconnects_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(interconnects_obj), '-' * 14))
        logger.info("Verifying User Permissions for an interconnect with name %s" % ic_obj.name)
        select_interconnect(ic_obj.name)

        # Verify user permissions
        logger.info("Verifying Permissions")
        if user_role == "Infrastructure administrator" or user_role == "Server administrator" or user_role == "Full":
            # Open Action Menu
            logger.info("Clicking Action Button")
            CommonOperationInterconnects.click_natasha_logical_interconnect_action_button()

            # Check that Actions are visible
            logger.info("Verifying 'Power' Action visible")
            if not (ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_DFRM_SELECT_ACTION_POWER_OFF) or ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_SELECT_ACTION_POWER_ON)):
                ui_lib.fail_test("'Power' Action not visible for user %s" % user_role)

            logger.info("Verifying 'Reset' Action visible")
            if ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_DFRM_SELECT_ACTION_POWER_OFF):
                ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_DFRM_SELECT_ACTION_RESET, timeout=5, fail_if_false=True)

            logger.info("Verifying 'Refresh' Action visible")
            ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_DFRM_SELECT_ACTION_REFRESH, timeout=5, fail_if_false=True)
        else:
            # Open Action Menu
            logger.info("Clicking Action Button")
            CommonOperationInterconnects.click_natasha_logical_interconnect_action_button()

            # Check that user has No authorization
            logger.info("Verifying there is no authorization for user: %s" % user_role)
            ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_DFRM_TEXT_ACTION_NO_AUTHORIZATION, timeout=5, fail_if_false=True)

        logger.info("Permissions Verified")


def validate_sylvite_interconnect_user_permissions(user_role, interconnects_obj):
    """
        The function will validate the user permissions for Sylvite Interconnects in the Action Menu based on the user
        role that is passed in. Sylvite is Unmanaged interconnect and  with Downlink Edit permissions

        Arguments:
            user_role*                               -- In User and Groups, User role field
            Interconnect Object

    """
    logger.info("\nVerify Actions Menu for %s" % user_role)
    navigate()
    # Select Interconnect
    for n, ic_obj in enumerate(interconnects_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(interconnects_obj), '-' * 14))
        logger.info("Verifying User Permissions for an interconnect with name %s" % ic_obj.name)
        if user_role == "Network administrator":
            select_interconnect(ic_obj.name)
        # Verify user permissions
        logger.info("Verifying Permissions")
        if user_role == "Network administrator":
            # Open Action Menu
            logger.info("Clicking Action Button")
            CommonOperationInterconnects.click_logical_interconnect_action_button()
            # Check that Action button is visible
            logger.info("Verifying 'Power' Action visible")
            VerifyInterconnects.verify_actions_power_button()
            if VerifyInterconnects.verify_actions_power_off_button():
                logger.info("Verifying 'Reset' Action visible")
                VerifyInterconnects.verify_actions_reset_button()
                logger.info("Verifying 'Edit' Action visible")
                VerifyInterconnects.verify_actions_edit()
        elif user_role == "Server administrator" or user_role == "Storage administrator" or user_role == "Backup administrator":
            select_interconnect(ic_obj.name)
            logger.info("Clicking Action Button")
            CommonOperationInterconnects.click_logical_interconnect_action_button()
            # Check that user has No authorization visible when clicked on Action
            logger.info("Verifying there is no authorization for user: %s" % user_role)
            VerifyInterconnects.verify_actions_noauthorization()
        logger.info("Permissions Verified")


def validate_tbird_interconnect_connector_info(inc_obj):
    """ This function is to verify Tbird interconnect connection information
        Compares the ui values returned as dictionary against the values returned after converting the CANMIC block data from EM

        Example:
       validate_tbird_interconnect_connector_info(*interconnect_obj)
    """
    FusionUIBase.navigate_to_section(SectionType.INTERCONNECTS)
    ic_dict = {"Type": [],
               "Vendor": [], "vendorOUI": [],
               "Part number": [], "Revision": [], "Serial number": []
               }
    for n, inc in enumerate(inc_obj):
        logger.info("verifying uplink port info of interconnect named '%s'" % inc.name)
        if not VerifyInterconnects.verify_interconnect_exist(inc.name, timeout=5, fail_if_false=False):
            logger.warn("interconnect '%s' does not exist" % inc.name)
            continue
        CommonOperationInterconnects.click_interconnect(inc.name, timeout=5)
        FusionUIBase.select_view_by_name(view_name="Uplink Ports", timeout=5, fail_if_false=False)
        result = {}
        # Collect uplink port information
        ports = []
        port_count = 0
        Linked = []
        Unlinked = []
        ports_to_check = []
        ui_dict = {"Type": [],
                   "Vendor": [], "Vendor OUI": [],
                   "Part number": [], "Revision": [], "Serial number": []
                   }
        logging._warn("Clicking Connector port")
        ports_data = FusionUIBase.get_text(GeneralInterconnectsElements.ID_PANEL_UPLINK_PORTS, timeout=10, fail_if_false=False)
        logger.info("Text is %s" % ports_data)
        ports = ports_data.split(' ')
        for item in ports:
            if item == "Linked":
                port_count += 1
                Linked.append(port_count)
            if item == "Unlinked":
                port_count += 1
                Unlinked.append(port_count)
        ports_to_check = Linked + Unlinked
        # CLick on Uplink expander
        for x in range(1, port_count):
            logger.info("Clicking on port %d" % x)
            CommonOperationInterconnects.click_port_button(int(x), timeout=5)
            CommonOperationInterconnects.click_port_sub_button()
            connector_info = FusionUIBase.get_text(GeneralInterconnectsElements.ID_UPLINK_CONNECTOR_INFO % int(x + 1))
            logger.info("Connector Info is %s" % connector_info)
            if 'No connector' in connector_info:
                logging.info('\nNo connector found \n')
            else:
                data = connector_info.split(" ")
                temp = data[8].split("\n")
                ui_dict["Type"] = temp[1]
                ui_dict["Vendor"] = data[9]
                ui_dict["Vendor OUI"] = data[10]
                ui_dict["Part number"] = data[11]
                ui_dict["Revision"] = data[12]
                ui_dict["Serial number"] = data[13]
                logger.info("ui_dict is %s" % ui_dict)
            logger.info("Collapsing")
            CommonOperationInterconnects.click_port_button(int(x), timeout=5)
            blk = 200 + (x - 1)
            ic_dict = _get_sylvite_connector_info_em(inc.dcs, inc.enclosurename, inc.appip, inc.appuname, inc.apppassw, inc.emipv6, inc.icbay, blk)
            if ic_dict:
                for key in ui_dict:
                    if key in ic_dict:
                        if not ui_dict[key] in ic_dict[key]:
                            logger.warn("Following paramters are not matching with EM-Interconnects data")
                            logger.warn("EM IC parameter    - %s and value - %s" % (key, ic_dict[key]))
                            logger.warn("Appliance parameter - %s and value - %s" % (key, ui_dict[key]))
                            ui_lib.fail_test("Parameters are not matching as expected")
                        else:
                            logger.info("\nPassed: Data from EM compared with UI parameter %s and is matching " % key)
            else:
                logger.info("There is no connector inserted in port number %s" % x)
    return True


def _get_sylvite_connector_info_em(dcs, enclosurename, appip, appuname, apppassw, emipv6, icbay, blk):
    ic_dict = {"Type": [],
               "Vendor": [], "Vendor OUI": [],
               "Part number": [], "Revision": [], "Serial number": []}
    logger.info("Entering em operation")
    if dcs.lower() == 'yes':
        cmd = 'curl -ik --request POST https://%s/rest/v1/Managers/20%s -H \'Content-Type: application/json\' -d \'{ "Action": "ReadCanmicBlocks","List": [%s]}\' | grep } | python -m json.tool | grep Data | cut -d "\\"" -f 4 | base64 -d | hexdump -C' % (emipv6, icbay, blk)
    else:
        xauth_cmd = '/ci/bin/tbird/appliance-hal.sh get-enclosure-credentials -s %s -o t' % (enclosurename)
        port = 22
        xauth = execute_cmd(appip, port, appuname, apppassw, xauth_cmd)
        logger.info("\n XAUTH is %s" % (xauth))
        cmd = 'curl --globoff -ki -x ""     --request POST --header "x-auth-token:%s" https://%s/rest/v1/InterconnectManager/%s -H \'Content-Type: application/json\' -d \'{ "Action": "ReadCanmicBlocks","List": [%s]}\' | grep } | python -m json.tool | grep Data | cut -d "\\"" -f 4 | base64 -d | hexdump -C' % (xauth.rstrip(), emipv6, icbay, blk)
    port = 22
    connectordata = get_canmic_block(appip, port, appuname, apppassw, cmd)
    logger.info("connectordata data is %s" % connectordata)
    if connectordata[0] != "00":
        logger.info("Connector present")
        logger.info("connectordata data is %s" % connectordata)
        connectortype_temp = int(connectordata[54], 16)
        if connectortype_temp == 254:
            connectortype = "ILP"
        if connectortype_temp == 255:
            connectortype = "Unknown"
        if connectortype_temp == 64:
            connectortype = "10GBASE-T"
        if connectortype_temp == 43:
            connectortype = "Active DAC"
        if connectortype_temp == 42:
            connectortype = "Passive DAC"
        if connectortype_temp == 4:
            connectortype = "SFP"
        if connectordata[0] == '00':
            connectorvendor = "Vendor"
        if connectordata[0] == '43':
            connectorvendor = "Cisco"
        if connectordata[0] == '4e':
            connectorvendor = "HP Network"
        if connectordata[0] == '53':
            connectorvendor = "none"
        i = 4
        partnumber = ''
        while i < 20:
            if connectordata[i] != "" and connectordata[i] != "20":
                partnumber = partnumber + chr(int(connectordata[i], 16))
            i = i + 1
        i = 20
        revision = ''
        while i < 22:
            revision = revision + chr(int(connectordata[i], 16))
            i = i + 1
        i = 24
        serialnumber = ''
        while i < 38:
            if connectordata[i] != "" and connectordata[i] != "20":
                serialnumber = serialnumber + chr(int(connectordata[i], 16))
            i = i + 1
        ic_dict["Type"] = connectortype
        ic_dict["Vendor"] = connectorvendor
        ic_dict["Vendor OUI"] = "00-17-6A"
        ic_dict["Part number"] = partnumber
        ic_dict["Revision"] = revision
        ic_dict["Serial number"] = serialnumber
        logger.info("ic_dict %s" % ic_dict)
        return ic_dict
    else:
        logger.info("There is no connector inserted")


def verify_c7k_ic_version(icbay, appip, appuname, appasswd, dcs="No"):
    """
    This  function  will log in to OA and returns different interconnect module firmware version value
    """
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    port = 22  # SSH Port to establish connection
    client.connect(appip, port, username=appuname, password=appasswd)
    channel = client.invoke_shell()
    stdin = channel.makefile('wb')
    stdout = channel.makefile('rb')

    if dcs == 'yes':
        cmd = "show interconnect info " + str(icbay)
        input, output, error = client.exec_command(cmd)
        data = output.read()
        logger.info("data is %s" % data)
        data = data.strip()
        m = re.search('Firmware Version: (.*)', data)
        if m:
            logger.info("match found !")
            logger.info("Value of firmware version: %s" % (m.group(1)))

            return m.group(1)
    else:
        cmd = "show interconnect info " + str(icbay)
        input, output, error = client.exec_command(cmd)
        data = output.read()
        logger.info("data is %s" % data)
        data = data.strip()
        m = re.search('Firmware Version: (.*)', data)
        if m:
            logger.info("Firmware version match found !")
            logger.info("Value of firmware version is : %s" % (m.group(1)))

            return m.group(1)


def tbird_validate_interconnect_link_ports_information_and_alerts(interconnect_obj):
    """
        This function displays the Extender Ports information. If port or Interconnect
        status is red, captures Alerts present in activity page and validates the same.

        * required arguments:
        <interconnects_dcs>
            <interconnect name="0000A66101, interconnect 6"  EMipv6="fe80::2:0:9:1%eth2" appip="15.212.161.161" username="root" password="hpvse1" dcs ="yes">
                <hardware product_name="Synergy 10Gb Interconnect Link Module"/>
            </interconnect>
            <interconnect name="0000A66102, interconnect 6"  EMipv6="fe80::2:0:9:3%eth2" appip="15.212.161.161" username="root" password="hpvse1" dcs ="yes">
                <hardware product_name="Virtual Connect SE 40Gb F8 Module for Synergy"/>
                <activity state ="Active" />
                <activity state = "Locked" />
            </interconnect>

        </interconnects_dcs>
    """

    error = 0

    port_dct = {"Port": [], "Status": [], "State": [],
                            "Connected To": " ", "Type": [],
                            "Speed": [], "Vendor": [], "Vendor OUI": [],
                            "Part number": [], "Revision": [], "Serial number": []}
    key_list = ["State",
                "Connected To", "Status", "Type",
                "Speed", "Vendor", "Vendor OUI",
                "Part number", "Revision", "Serial number"]
    cmp_list = ["Type",
                "Speed", "Vendor", "Vendor OUI",
                "Part number", "Revision", "Serial number"]
    ic_dict = {"Type": [], "Speed": [], "Vendor": [], "Vendor OUI": [],
               "Part number": [], "Revision": [], "Serial number": []}

    expected_product_name = False

    error_string = []
    FusionUIBase.navigate_to_section(SectionType.INTERCONNECTS)
    for interconnect in interconnect_obj:
        linked_ports = []
        unlinked_ports = []
        total_no_of_ports = []
        order_of_ports = []
        alert_msgs = []
        port_count = 0
        mouse_over_status = {}
        mouse_over_connected_to = {}
        mouse_over_state = {}
        # select the given interconnect

        if not VerifyInterconnects.verify_interconnect_exist(interconnect.name, timeout=5, fail_if_false=False):
            logger.warn("interconnect '%s' does not exist" % interconnect.name)

            continue

        CommonOperationInterconnects.click_interconnect(interconnect.name, timeout=5)

        logger.info("\nPerforming operation on Interconnect %s..." % interconnect.name)

        # Get the bay no and enclosure name from interconnect name
        name = interconnect.name
        bay_no = name.split(" ")
        encl_name = bay_no[0].split(',')

        # Navigate to overview page
        FusionUIBase.select_view_by_name('Overview')

        # to get product name
        prod_name = CommonOperationInterconnects.get_overview_product_name(5, False)
        logger.info("Product Name is: %s" % prod_name)

        # to get power state
        power_state = CommonOperationInterconnects.get_overview_power_state(5, False)

        # to get logical interconnect
        logical_ic = CommonOperationInterconnects.get_overview_logical_interconnect(5, False)

        # to get interconnect state
        state = CommonOperationInterconnects.get_overview_ic_state(5, False)
        logger.info("Power state is : %s" % power_state)
        logger.info("Logical Interconnect is :%s" % logical_ic)
        logger.info("Interconnect state is : %s" % state)
        overview_port_infor = {}
        # overview - Hardware
        if hasattr(interconnect, "hardware"):
            hardware_obj = interconnect.hardware[0]

            # to  verify the product name
            if hasattr(hardware_obj, "product_name"):
                if VerifyInterconnects.verify_overview_product_name(hardware_obj.product_name, 5, False):
                    expected_product_name = True

        if (state == "Absent"):
            # if the state is absent expected alert on Activity page is after LE creation...
            logger.info("ICM state is :%s" % state)
            expected_alert_msg = "The interconnect module is absent. A " + hardware_obj.product_name + " is expected."
            logger.info("Expected Alert message is: %s" % expected_alert_msg)
            alert_msgs.append(expected_alert_msg)
        else:
            # hover the virtual interconnect to display state, connected to information
            if ("Virtual Connect SE 40Gb F8 Module for Synergy" in prod_name) or ("Synergy 40Gb F8 Switch Module" in prod_name):

                # Mouse over to each port and capture the state, connected and port status..
                for i in range(1, 5):

                    port = InterconnectLinkPorts.get_overview_mouseover_port_information(i, 5, False)
                    status = InterconnectLinkPorts.get_overview_mouseover_port_status(i, 5, False)
                    state = InterconnectLinkPorts.get_overview_mouseover_port_state(i, 5, False)
                    connected_to = InterconnectLinkPorts.get_overview_mouseover_port_connectedto(i, 5, False)
                    logger.info("hovered over cxp port information")
                    logger.info("port - %s status is - %s" % (port, status))
                    logger.info("State - %s" % state)
                    logger.info("Connected to - %s" % connected_to)
                    mouse_over_status["port_no_{}".format(i)] = status
                    mouse_over_state["port_no_{}".format(i)] = state
                    mouse_over_connected_to["port_no_{}".format(i)] = connected_to
            # hover the extender interconnect to display state, connected to information
            elif(("Synergy 20Gb Interconnect Link Module" in prod_name)):
                # Mouse over to each port and capture the state, connected and port status..
                for i in range(1, 3):

                    port = InterconnectLinkPorts.get_overview_mouseover_port_information_of_extender_interconnect(i, 5, False)
                    status = InterconnectLinkPorts.get_overview_mouseover_port_status_of_extender_interconnect(i, 5, False)
                    state = InterconnectLinkPorts.get_overview_mouseover_port_state_of_extender_interconnect(i, 5, False)
                    connected_to = InterconnectLinkPorts.get_overview_mouseover_port_connectedto_of_extender_interconnect(i, 5, False)
                    loger.info("hovered over cxp port information")
                    logger.info("port - %s status is - %s" % (port, status))
                    logger.info("State - %s" % state)
                    logger.info("Connected to - %s" % connected_to)
                    mouse_over_status["port_no_{}".format(i)] = status
                    mouse_over_state["port_no_{}".format(i)] = state
                    mouse_over_connected_to["port_no_{}".format(i)] = connected_to
            # hover the extender interconnect to display state, connected to information
            elif(("Synergy 10Gb Interconnect Link Module" in prod_name)):
                # Mouse over to each port and capture the state, connected and port status..
                for i in range(1, 2):

                    port = InterconnectLinkPorts.get_overview_mouseover_port_information_of_extender_interconnect(i, 5, False)
                    status = InterconnectLinkPorts.get_overview_mouseover_port_status_of_extender_interconnect(i, 5, False)
                    state = InterconnectLinkPorts.get_overview_mouseover_port_state_of_extender_interconnect(i, 5, False)
                    connected_to = InterconnectLinkPorts.get_overview_mouseover_port_connectedto_of_extender_interconnect(i, 5, False)
                    logger.info("hovered over cxp port information")
                    logger.info("port - %s status is - %s" % (port, status))
                    logger.info("State - %s" % state)
                    logger.info("Connected to - %s" % connected_to)
                    mouse_over_status["port_no_{}".format(i)] = status
                    mouse_over_state["port_no_{}".format(i)] = state
                    mouse_over_connected_to["port_no_{}".format(i)] = connected_to
            # Navigate to Interconnect Link Ports page
            FusionUIBase.select_view_by_name('Interconnect Link Ports')
            if VerifyInterconnects.verify_interconnect_link_ports_label():
                logging._info("Displaying the cxp ports information")

                # try to get port table information and displays linked and unlinked ports

                port_table_information = InterconnectLinkPorts.get_port_table_information(5, False)
                linked_ports, unlinked_ports, order_of_ports = _get_linked_unlinked_ports_information(port_table_information, order_of_ports, port_count)
                total_no_of_ports = len(linked_ports) + len(unlinked_ports)
                logger.info("total No. of ports is %s" % total_no_of_ports)
                logger.info("linked ports are %s" % linked_ports)
                logger.info("Unlinked ports are %s" % unlinked_ports)
                logger.info("order of ports are %s" % order_of_ports)

                port_count = -1
                # capture port status, state, connected to information from Interconnect Link Ports page
                for item in order_of_ports:
                    port_count = port_count + 1
                    port = int(item)
                    logger.info("\n---------------------------------------------------------------------")
                    logger.info("Displaying %s port information from Interconnect Link ports view" % port)
                    logger.info("\n---------------------------------------------------------------------")
                    i = 1
                    (port_status, connected, connector_present_ov, connectedport, port_dct) = _get_connector_information_from_ov(port, i, 5, False)
                    logger.info("connected port %s " % connectedport)
                    i = 0
                    logger.info(mouse_over_state)
                    if (mouse_over_connected_to["port_no_{}".format(port)] == connected):
                        logger.info("Port connected to information is matching from Oneview")
                    else:
                        error += 1
                        logger.warn("Port connected to information is not matching from ILP and mouser over")

                    if (mouse_over_state["port_no_{}".format(port)] == port_dct["State"]):
                        logger.info("Port State information is matching from Oneview")
                    else:
                        error += 1
                        logger.warn("Port State information is not matching from ILP and mouser over")

                    if (mouse_over_status["port_no_{}".format(port)] == port_dct["Status"]):
                        logger.info("Port Status information is matching from Oneview")
                    else:
                        error += 1
                        logger.warn("Port Status information is not matching from ILP and mouser over")

                    (expected_alert_msg, expected_alert_msg_li) = _frame_expected_alert_message(interconnect.name, power_state, port_status, connected, connector_present_ov, connectedport, port_dct, expected_product_name, logical_ic)

                    if (expected_alert_msg is not None):
                        alert_msgs.append(expected_alert_msg)
                        logger.info(expected_alert_msg)
                    if (expected_alert_msg_li is not None):
                        alert_msgs.append(expected_alert_msg_li)
                        logger.info(expected_alert_msg_li)

                    # Capture the port connector information by logging into EM
                    blk = str(163 + port_count)  # To read CXP C1 port
                    logger.info("block no is : %s" % blk)
                    connector_present = ""
                    (connector_present, ic_dict) = em_operation._get_connector_information_from_em(interconnect.dcs, encl_name[0], interconnect.appip, interconnect.username, interconnect.password, interconnect.EMipv6, bay_no[2], blk, power_state, prod_name, port_count)
                    if connector_present is "0":

                        for key in cmp_list:
                            printline = "\n------------------------------------------------------------------"
                            if key in ic_dict:
                                if not (port_dct[key] == ic_dict[key]):
                                    logger.info(printline)
                                    if(("Synergy 20Gb Interconnect Link Module" in prod_name) or ("Synergy 10Gb Interconnect Link Module" in prod_name)):
                                        logger.warn("Following paramters are not matching with EM-Interconnects data")
                                        logger.warn("EM IC parameter    - %s and value - %s" % (key, ic_dict[key]))
                                        logger.warn("Appliance parameter - %s and value - %s" % (key, port_dct[key]))
                                else:
                                    logger.info(printline)
                                    logger.info("\nPassed: EM Data and Appliance parameter %s is matching " % key)
                                    logger.info(printline)

                    elif(connector_present_ov == 1):
                        logger.info("Expected froM OV and EM:There is no connector is inserted into port %s" % port_dct["Port"])
                    else:
                        logger.warn("Connector information is not matching")
                        error += 1

        # Function to capture the alerts present in Activity Page
        if _capture_alerts(interconnect, alert_msgs):
            error += 1
            error_string.append("Alert validation failed for interconnect:{}".format(interconnect.name))

    if (error > 0):
        raise AssertionError("Alert validation or Validation of port connector information is failed")
    else:
        return True


def _frame_expected_alert_message(interconnect, power_state, port_status, connected, connector_present_ov, connectedport, port_dct, expected_product_name, logical_ic):
    logger.info("Function to frame the alert message if Port status is error/disabled")
    expected_alert_msg = None
    expected_alert_msg_li = None
    logger.info(logical_ic)
    # if the port status is error,  no connector information and no LI/LI frame the expected alert
    if (port_status == "error" and connected == "none" and connector_present_ov == 1 and expected_product_name):
        logger.info("Port status is %s" % port_dct["Status"])
        expected_alert_msg = "Interconnect port " + port_dct["Port"] + " is not cabled"
        logger.info("Expected Alert message is: %s" % expected_alert_msg)

        if not (logical_ic == "none"):
            expected_alert_msg_li = "Downlink ports are down due to absence of cable in interconnect port " + port_dct["Port"]
            logger.info("Expected Alert message is: %s" % expected_alert_msg_li)

    # if the port status is error,  onnector information is present and no LI/LI frame the expected alert
    elif (port_status == "error" and connected == "none" and connector_present_ov == 0 and expected_product_name):
        logger.info("Port status is %s" % port_dct["Status"])
        expected_alert_msg = "Interconnect port " + port_dct["Port"] + " is either disconnected or connected to an outside management ring."
        logger.info("Expected Alert message is: %s" % expected_alert_msg)

    # if the port status is error, expected product name is matching ...
    elif (port_status == "error" and (expected_product_name is not True)):
        logger.info("Port status is %s" % port_dct["Status"])
        expected_alert_msg = "Interconnect is invalid and makes port " + port_dct["Port"] + " critical."
        logger.info("Expected Alert message is: %s" % expected_alert_msg)

    # if the status is error,  connector information is present and no LI/LI frame the expected alert
    elif (port_status == "error"):
        connected_inc_name = connectedport[0] + "," + connectedport[1]
        CommonOperationInterconnects.click_interconnect(connected_inc_name, timeout=5)
        power_state_of_connected_ic = CommonOperationInterconnects.get_overview_power_state(5, False)
        logger.info("power state of connected ic is %s" % power_state_of_connected_ic)
        CommonOperationInterconnects.click_interconnect(interconnect, timeout=5)
        FusionUIBase.select_view_by_name('Interconnect Link Ports')
        if (power_state_of_connected_ic == "Off"):
            expected_alert_msg = "The connected port " + port_dct["Port"] + " is on an interconnect " + connected_inc_name + " that is powered off."
        else:
            expected_alert_msg = "Interconnect port " + port_dct["Port"] + " is incorrectly connected to " + connectedport[0] + "," + connectedport[1] + ", port" + connectedport[2]
        logger.info("Expected Alert message is: %s" % expected_alert_msg)

        if not (logical_ic == "none"):
            expected_alert_msg_li = "Downlink ports are down due to invalid cabling of interconnect port " + port_dct["Port"]

    elif (port_status == "disabled" and power_state == "Off"):
        expected_alert_msg = "Interconnect " + interconnect + " has been powered off"
        logger.info("Port status is %s" % port_dct["Status"])
    else:
        logger.info("Port status is %s" % port_dct["Status"])

    return (expected_alert_msg, expected_alert_msg_li)


def _get_connector_information_from_ov(port, i, timeout=5, fail_if_false=False):
    logger.info("Function to get connector information from OV")
    connector_present_ov = 0
    port_dct = {"Port": [], "Status": [], "State": [],
                            "Connected To": " ", "Type": [],
                            "Speed": [], "Vendor": [], "Vendor OUI": [],
                            "Part number": [], "Revision": [], "Serial number": []}
    key_list = ["State",
                "Connected To", "Status", "Type",
                "Speed", "Vendor", "Vendor OUI",
                "Part number", "Revision", "Serial number"]
    port_status = InterconnectLinkPorts.get_cxpport_status_from_interconnect_link_ports(port, 5, False)
    cxpport_data = InterconnectLinkPorts.get_port_information_from_interconnect_link_ports(port, 5, False)
    cxpport_connector_info = InterconnectLinkPorts.get_cxpport_connector_information_from_interconnect_link_ports(port, 5, False)
    ui_lib.refresh_browser(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.BROWSER_REFRESH)
    cxpport_data = cxpport_data.split("\n")

    port_dct["Port"] = cxpport_data[0]
    for key in key_list:
        if (i < len(cxpport_data)):
            port_dct[key] = cxpport_data[i]
            i += 1
    connected = port_dct["Connected To"]
    port_dct["Status"] = port_status
    connectedport = connected.split(',')

    # if there is no connector display the same
    if ("No connector" in cxpport_connector_info):
        logging._info("No connector is present")
        connector_present_ov = 1
        port_dct["Type"] = None
        port_dct["Speed"] = None
        port_dct["Vendor"] = None
        port_dct["Vendor OUI"] = None
        port_dct["Part number"] = None
        port_dct["Revision"] = None
        port_dct["Serial number"] = None

    # if the connector information is present capture the same from OneView
    else:
        data = cxpport_connector_info.split(" ")
        data_len = len(data)
        temp = data[10].split("\n")
        port_dct["Type"] = temp[1]
        port_dct["Speed"] = data[11]
        port_dct["Vendor"] = data[12]
        port_dct["Vendor OUI"] = data[13]
        port_dct["Part number"] = data[14]
        port_dct["Revision"] = data[15]
        port_dct["Serial number"] = data[16]
    i = 0
    port_name = port_dct["Port"]
    # Display the captured information
    for key in key_list:
        if not (port_dct[key] is None):
            logging._info("%s port %s is - %s" % (port_name, key, port_dct[key]))

    return (port_status, connected, connector_present_ov, connectedport, port_dct)


def _capture_alerts(interconnect, alert_msgs, timeout=5):
    '''
      If port or interconnect status is error,
      this function displays and validate the alerts
      present in Interconnect Activity page.
    '''
    interconnect_status = CommonOperationInterconnects.get_interconnect_status_in_interconnectlinktopology(interconnect.name, 5, False)

    if not hasattr(interconnect, "activity"):
        logger.warn("no activity child elements in <interconnect> node(%s)" % interconnect.name)
        return False

    # activity_state = ['Active', 'Locked']
    alerts_msgs_ov = []
    logger.info("Interconnect Status is %s" % interconnect_status)
    if (interconnect_status == "error" or interconnect_status == "warning"):
        logger.info("capturing the alerts")
        # Navigate to Activity Page
        FusionUIBase.select_view_by_name('Activity')
        # Filter Active Alerts
        CommonOperationInterconnects.click_filter_all_states(timeout, False)
        for activity_obj in interconnect.activity:
            CommonOperationInterconnects.click_filter_activity_state(activity_obj.state, timeout, False)
        CommonOperationInterconnects.refresh_current_page(timeout, False)

        # Display the error count

        error_count = CommonOperationInterconnects.get_error_count_in_invalid_interonnect_link_topology(5, False)

        import re
        error_count = re.sub(r'\s', '', error_count)

        if (error_count == "1"):
            no_of_alerts = 1
        else:
            no_of_alerts = int(error_count)

        # Display the Active alerts on Console
        k = 1

        for k in range(1, no_of_alerts + 1):

            if k <= no_of_alerts:

                CommonOperationInterconnects.click_alert_label_collapser(k, 5, False)
                alert_msg = CommonOperationInterconnects.get_activity_text(k, 5, False)
                resolution_msg = CommonOperationInterconnects.get_resolution_text(k + 1, 5, False)
                CommonOperationInterconnects.click_event_details_collapser(k + 1, 5, False)
                event_msg = CommonOperationInterconnects.get_event_text(k + 1, 5, False)
                logger.info("---------------------------------------\n")
                logger.info("%d. Alert: %s \n" % (k, alert_msg))
                logger.info("%s \n" % resolution_msg)
                logger.info("%s \n" % event_msg)
                logger.info("---------------------------------------\n")
                CommonOperationInterconnects.click_event_details_collapser(k + 1, 5, False)
                CommonOperationInterconnects.click_alert_label_collapser(k, 5, False)
                alerts_msgs_ov.append(alert_msg)

        # Compare expected and OV alerts
        k = 1
        for alert in alert_msgs:
            count = 0
            logger.info(alert)
            for k in alerts_msgs_ov:

                if (alert in k):
                    logger.info("Expected and Actual Alert message is proper")
                    count += 1
                else:
                    pass
            if (count == 0) or (len(alert_msgs) != len(alerts_msgs_ov)):
                logger.warn("Verify the alerts, expected and actual alert count is not matching !! or Expected alerts are not present in Activity")
                return False

        FusionUIBase.select_view_by_name('Overview')
        return True

    else:
        logger.info("%s  status is %s" % (interconnect.name, interconnect_status))
        return False


def _get_linked_unlinked_ports_information(port_table, ports_order, port_count, timeout=5):
    '''
      This function provides information of Linked and unlinked ports
      from total ports present in table
    '''
    logger.info("Function to get Linked and Unlinked Ports")
    ports = []
    ports = port_table.split('\n')
    linked = []
    unlinked = []

    for item in ports:
        if item == "Linked":
            port_count += 1
            linked.append(port_count)
            ports_order.append(port_count)

        elif item == "Unlinked":
            port_count += 1
            unlinked.append(port_count)
            ports_order.append(port_count)

    return linked, unlinked, ports_order


def sylvite_downlink_edit(interconnect_obj):
    """ sylvite_downlink_edit
      Function to edit the Downlinks of Sylvite.There is no uplink edit provision for Sylvite
    """
    fail_time = 0
    for interconnect in interconnect_obj:
        if not select_interconnect(interconnect.name):
            logger.warn("Exiting Edit Interconnect Function, Not selected Interconnect %s" % interconnect.name)
            fail_time += 1
            continue
        EditInterconnects.select_actions_edit()
        EditInterconnects.wait_edit_interconnect_dialog_shown()
        # CODE TO EDIT  DOWNLINK PORTS OF SYLVITE
        if not EditInterconnects.wait_edit_interconnect_dialog_shown(5, False):
            logger.info("dint open the edit interconnects page even after clicking edit button")
            fail_time += 1
        else:
            if interconnect.DownlinkportstoCheck != '':
                DownlinkList = interconnect.DownlinkList.split(',')
                DownlinkportstoCheck = interconnect.DownlinkportstoCheck.split(',')
                for Downlink in DownlinkList:
                    if Downlink in DownlinkportstoCheck:
                        EditInterconnects.tick_enable_downlink_ports(Downlink, timeout=10)
                    else:
                        EditInterconnects.untick_enable_downlink_ports(Downlink, timeout=10)
            else:
                logger.info("No Downlink ports are selected to edit for the interconnect %s" % interconnect.name)
            EditInterconnects.click_ok_button()
            EditInterconnects.wait_edit_interconnect_dialog_disappear()
            FusionUIBase.show_activity_sidebar()
            if CommonOperationInterconnects.wait_activity_action_ok(interconnect.name, "Update", 60, False):
                logger.info("The interconnect is edited successfully %s" % interconnect.name)
                # return False
            else:
                logger.warn("The interconnect is not edited successfully %s" % interconnect.name)
                fail_time += 1
    if fail_time > 0:
        raise AssertionError("Downlink Port edit failed")
    else:
        return True


def verify_fex_interconnect_uplinkport_editable(*interconnect_obj):
    """
       Verify FEX interconnects port are not editable
    """
    if isinstance(interconnect_obj, test_data.DataObj):
        interconnect_obj = [interconnect_obj]
    elif isinstance(interconnect_obj, tuple):
        interconnect_obj = list(interconnect_obj[0])

    for interconnect in interconnect_obj:
        if not select_interconnect(interconnect.name):
            FusionUIBase.fail_test_or_return_false("Exiting,[Interconnect %s] is not selected" % interconnect.name)
        EditInterconnects.select_actions_edit()
        EditInterconnects.wait_edit_interconnect_dialog_shown()
        # CODE TO EDIT UPLINK PORTS AND DOWNLINK PORTS OF INTERCONNECTS
        if not EditInterconnects.wait_edit_interconnect_dialog_shown(5, False):
            FusionUIBase.fail_test_or_return_false("didnt open the edit interconnects page even after clicking edit button")
        else:
            if VerifyInterconnects.verify_interconnect_uplinkport_label_not_exist() is True:
                logger.info("Verified in [ INTERCONNECT %s ] uplink Ports are not editable" % interconnect.name)
            if EditInterconnects.click_ok_button() is True:
                EditInterconnects.wait_edit_interconnect_dialog_disappear()
            else:
                FusionUIBase.fail_test_or_return_false("Edit dialog is still open")
    return True


def edit_scope_for_interconnects(interconnect_list):
    """ edit scope for interconnect
        This function is to edit scope for interconnects
        Example:
            edit_scope_for_interconnects(interconnect_list)
    """
    logger.info("Function call to edit scope for interconnects ")
    navigate()
    for interconnect in interconnect_list:
        if not select_interconnect(interconnect.name):
            FusionUIBase.fail_test_or_return_false("Failed to find target Interconnects")
        FusionUIBase.select_view_by_name("Scopes")
        EditScopeForInterconnect.click_edit_scope_button()
        EditScopeForInterconnect.wait_edit_scope_dialog_open()
        if interconnect.has_property("scopes"):
            scope_list = interconnect.scopes.split(',')
            for scope in scope_list:
                if not VerifyInterconnects.verify_scope_should_exist_in_edit_page(scope, 2, fail_if_false=False):
                    EditScopeForInterconnect.click_assign_button()
                    EditScopeForInterconnect.wait_assign_scope_dialog_open()
                    EditScopeForInterconnect.input_scope_name(scope)
                    EditScopeForInterconnect.click_scope_name(scope)
                    EditScopeForInterconnect.click_add_button()
                    EditScopeForInterconnect.wait_assign_scope_dialog_close()
        if interconnect.has_property("remove_scopes"):
            remove_scope_list = interconnect.remove_scopes.split(',')
            for scope in remove_scope_list:
                if VerifyInterconnects.verify_scope_should_exist_in_edit_page(scope, timeout=5):
                    EditScopeForInterconnect.click_remove_scope_icon(scope)
        EditScopeForInterconnect.click_ok_button()
        EditScopeForInterconnect.wait_edit_scope_dialog_close()
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(interconnect.name, 'Update', timeout=60, fail_if_false=True)
        FusionUIBase.show_activity_sidebar()
    return True


def validate_uplinkport_qosstatistics(*interconnect_obj):
    """
      Function to get the uplink linked ports and to verify quality of service statistics information is visible
          Example:
        | validate_uplinkport_qosstatistics(interconnect_obj)
        Input required to be provided in interconnect object :
        quality os service information   : qos statistics
        Sample data :
        <interconnects>
                        <QoS_c7k>
                                <value qosStatistics = "cosq%s_ucast_DroppedPkts,cosq%s_ucast_OutBytes,cosq%s_ucast_OutPkts" />
                        </QoS_c7k>
                </interconnects>
    """
    if isinstance(interconnect_obj, test_data.DataObj):
        interconnect_obj = [interconnect_obj]
    elif isinstance(interconnect_obj, tuple):
        interconnect_obj = list(interconnect_obj[0])
    if FusionUIBase.select_view_by_name('Uplink Ports'):
        for interconnects in interconnect_obj:
            count = 0
            flag = True
            while (flag and count < 35):
                count += 1
                linkedPort = InterconnectLinkPorts.get_uplink_linked_port(count, fail_if_false=False)
                if linkedPort == "Linked" or linkedPort == "Linkedunknown":
                    if InterconnectLinkPorts.click_uplink_linked_port_details(count):
                        if InterconnectLinkPorts.click_qos_statistics_uplink():
                            element_list = [item.strip() for item in interconnects.qosStatistics.split(',')]
                            for j in range(8):
                                for i in element_list:
                                    value1 = (i % j)
                                    if not VerifyInterconnects.verify_qos_statistics_uplink(value1):
                                        ui_lib.fail_test("Failed to verify downlink port QoS Statistics information")
                                    logger.debug("Verifying uplink port QoS Statistics information")
                            return True
                        else:
                            ui_lib.fail_test("Uplink port QoS Statistics information is not available")
                    else:
                        ui_lib.fail_test("Uplink linked port details is not available")
                else:
                    logger.info("No linked ports are available")
    else:
        ui_lib.fail_test("Interconnect uplink port view is not available to select")
    return True


def validate_downlinkport_qosstatistics(*interconnect_obj):
    """
      Function to get the downlink linked ports and to verify quality of service statistics information is visible
          Example:
        | validate_downlinkport_qosstatistics(interconnect_obj)
        Input required to be provided in interconnect object :
        quality os service information   : qos statistics
        Sample data :
        <interconnects>
                        <QoS_c7k>
                                <value qosStatistics = "cosq%s_ucast_DroppedPkts,cosq%s_ucast_OutBytes,cosq%s_ucast_OutPkts" />
                        </QoS_c7k>
                </interconnects>
    """
    if isinstance(interconnect_obj, test_data.DataObj):
        interconnect_obj = [interconnect_obj]
    elif isinstance(interconnect_obj, tuple):
        interconnect_obj = list(interconnect_obj[0])
    if FusionUIBase.select_view_by_name('Downlink Ports'):
        for interconnects in interconnect_obj:
            count = 0
            flag = True
            while (flag and count < 35):
                count += 1
                linkedPort = InterconnectLinkPorts.get_downlink_linked_port(count, fail_if_false=False)
                if linkedPort == "Linked":
                    flag = False
                    if InterconnectLinkPorts.click_downlink_linked_port_details(count):
                        if InterconnectLinkPorts.click_qos_statistics_downlink():
                            element_list = [item.strip() for item in interconnects.qosStatistics.split(',')]
                            for j in range(8):
                                for i in element_list:
                                    value1 = (i % j)
                                    if not VerifyInterconnects.verify_qos_statistics_downlink(value1):
                                        ui_lib.fail_test("Failed to verify downlink port QoS Statistics information")
                                    logger.debug("Verifying downlink port QoS Statistics information")
                            return True
                        else:
                            ui_lib.fail_test("Downlink port QoS Statistics information is not available")
                    else:
                        ui_lib.fail_test("Downlink linked port details is not available")
                else:
                    logger.info("No linked ports are available")
    else:
        ui_lib.fail_test("Interconnect downlink port view is not available to select")
    return True


def get_interconnects_error_message(interconnect_name):
    """ This function gets the interconnect error message
        Example:
        <interconnect_error_details>
            <interconnect name="CN7545061V, interconnect 3" />
        </interconnect_error_details>
    """
    navigate()
    logger.info("name is %s" % interconnect_name)
    if not select_interconnect(interconnect_name):
        ui_lib.fail_test("Failed to select the interconnect %s" % interconnect_name)
    else:
        return CommonOperationInterconnects.get_interconnect_error_message(timeout=20)


def c7000_clear_port_counters(interconnect_obj):
    """ clear_port_counters_interconnect
        Example:
        | `C7000 Clear Port Counters`      |     |
        Sample Data:
        <interconnects>
            <interconnect name="Titan, interconnect 1"
                          enclosure="Titan"
                          interconnect_power="On"
                          state="Configured"
                          DownlinkportstoCheck=""
                          UplinkPortstoCheck=""
                          DownlinkList=""
                          UplinkList="X1,X2"
                          >
            </interconnect>
        </interconnects>
    """
    fail_time = 0
    for interconnect in interconnect_obj:
        if not select_interconnect(interconnect.name):
            logger.warn("Exiting Clear Port Counter Interconnect Function, Not selected Interconnect %s" % interconnect.name)
            fail_time += 1
            continue

        ClearPortCounters.select_actions_clear_port_counters()
        if not ClearPortCounters.wait_clear_port_counters_ok(interconnect.name, fail_if_false=False):
            fail_time += 1
            logger.warn("Clear port Counter is not successful for the given interconnect - %s" % interconnect.name)
            continue
        FusionUIBase.show_activity_sidebar()

    if fail_time > 0:
        ui_lib.fail_test('The Clear port Counter cannot be done on %s' % interconnect.name)
    else:
        return True


def c7000_reapply_configuration(interconnect_obj):
    """ reapply_configuration_interconnect
        Example:
        | `C7000 Reapply Configuration`      |     |
        Sample Data:
        <interconnects>
            <interconnect name="Titan, interconnect 1"
                          enclosure="Titan"
                          interconnect_power="On"
                          state="Configured"
                          DownlinkportstoCheck=""
                          UplinkPortstoCheck=""
                          DownlinkList=""
                          UplinkList="X1,X2"
                          >
            </interconnect>
        </interconnects>
    """
    fail_time = 0
    for interconnect in interconnect_obj:
        if not select_interconnect(interconnect.name):
            logger.warn("Exiting Reapply Configuration Interconnect Function, Not selected Interconnect %s" % interconnect.name)
            fail_time += 1
            continue

        ReapplyConfiguration.select_actions_reapply_configuration()
        ReapplyConfiguration.wait_reapply_configuration_dialog_shown()
        ReapplyConfiguration.click_yes_reapply_button()
        ReapplyConfiguration.wait_reapply_configuration_dialog_disappear()

        if not ReapplyConfiguration.wait_reapply_configuration_ok(interconnect.name, fail_if_false=False):
            fail_time += 1
            logger.warn("The reapply configuration is not successful for the given interconnect - %s" % interconnect.name)
            continue
        FusionUIBase.show_activity_sidebar()

    if fail_time > 0:
        ui_lib.fail_test('The reapply configuration cannot be done on %s' % interconnect.name)
    else:
        return True


def get_tbird_interconnect_uplink_port_speed(inc_obj):
    """ This function is to get the Tbird Interconnect uplink port speed
    Example:
        get_tbird_interconnect_uplink_port_speed(*interconnect_obj)
    """
    FusionUIBase.navigate_to_section(SectionType.INTERCONNECTS)
    for inc in inc_obj:
        logger.info("verifying Uplink port info of interconnect named '%s'" % inc.name)
        if not VerifyInterconnects.verify_interconnect_exist(inc.name, timeout=5, fail_if_false=False):
            ui_lib.fail_test("interconnect '%s' does not exist" % inc.name)
        CommonOperationInterconnects.click_interconnect(inc.name, timeout=5)
        if not FusionUIBase.select_view_by_name(view_name="Uplink Ports", timeout=20, fail_if_false=False):
            ui_lib.fail_test("Uplink ports overview is not changed")
        logger.info("uplink ports are %s " % inc.uplinkport)
        return CommonOperationInterconnects.get_interconnect_uplink_port_speed(inc.uplinkport)


def get_tbird_interconnect_fc_port_statistics(inc_obj):
    """ This function is to get the Tbird interconnect fc port statistics
    Example:
        get_tbird_interconnect_fc_port_statistics(*interconnect_obj)
    """
    FusionUIBase.navigate_to_section(SectionType.INTERCONNECTS)
    for inc in inc_obj:
        logger.info("Verifying uplink port info of interconnect named '%s'" % inc.name)
        if not VerifyInterconnects.verify_interconnect_exist(inc.name, timeout=5, fail_if_false=False):
            ui_lib.fail_test("interconnect '%s' does not exist" % inc.name)
        CommonOperationInterconnects.click_interconnect(inc.name, timeout=5)
        FusionUIBase.select_view_by_name(view_name="Uplink Ports", timeout=10, fail_if_false=False)
        logger.info("uplink ports are %s " % inc.uplinkport)
        return CommonOperationInterconnects.get_fc_port_advanced_statistics(inc.uplinkport)

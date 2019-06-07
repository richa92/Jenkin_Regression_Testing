# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
""" Fusion Server Hardware UI page. """


from datetime import datetime
import sys
import threading

from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.cli.blade_info import blade_info

from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.business_logic.general.activity_elements import FusionActivityPage
from FusionLibrary.ui.servers.serverhardware_elements import FusionServerHardwarePage
from FusionLibrary.ui.business_logic.servers.serverhardware import CommonOperationServerHardware
from FusionLibrary.ui.business_logic.servers.serverhardware import AddHardware
from FusionLibrary.ui.business_logic.servers.serverhardware import RemoveHardware
from FusionLibrary.ui.business_logic.servers.serverhardware import ResetHardware
from FusionLibrary.ui.business_logic.servers.serverhardware import RefreshHardware
from FusionLibrary.ui.business_logic.servers.serverhardware import VerifyHardware
from FusionLibrary.ui.business_logic.servers.serverhardware import PowerOnHardware
from FusionLibrary.ui.business_logic.servers.serverhardware import PowerOffHardware
from FusionLibrary.ui.business_logic.servers.serverhardware import EditScopeForHardwares
from FusionLibrary.ui.business_logic.base import FusionUIBase
from FusionLibrary.ui.business_logic.base import SectionType
from FusionLibrary.libs.api.ilo.ilo_client import IloClient
from FusionLibrary.ui.business_logic.general.dashboard_elements import FusionDashboardPage
from FusionLibrary.ui.general.login_elements import FusionLoginPage
from FusionLibrary.ui.general import activity

ROBOT_LIBRARY_VERSION = '0.0'


def navigate():
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE)


def wait_until_page_load():
    """ Wait Until Page Load  """
    s2l = ui_lib.get_s2l()
    el = s2l._element_find("DataTables_Table_0_wrapper", True, True)
    cur_width = el.size["width"]
    width_changing = True
    start = datetime.now()
    while width_changing and (datetime.now() - start).total_seconds() < 5:
        BuiltIn().sleep(0.1)
        if el.size["width"] != cur_width:
            cur_width = el.size["width"]
        else:
            width_changing = False


def add_server_hardware(server_obj):
    """ Add Server Hardware

    Arguments:
      name*             --  Name of server hardware as a string.
      server*           --  hostname of the iLO of the server hardware.
      iloIP*            --  IP address/hostname of the iLO of the server hardware.
      iloUserName*      --  iLO's Admin username.
      iloPassword*      --  iLO's Admin password.
      mgmtType*         --  what type the server hardware will be added as, Managed/Monitored.
      Licensing*        --  Licensing type, 'HP OneView Advanced'/'HP OneView Advanced w/o iLO'.
      force*            --  Force add the server hardware if it's being managed by another system

    * Required Arguments

    Example:
        data/servers/dlserver -> @{TestData.servers.DLServers}
        <servers>
            <DLServers>
                <server name="wpstdl19-ilo" server="wpstdl19-ilo.vse.rdlabs.hpecorp.net" iloIP="wpstdl19-ilo.vse.rdlabs.hpecorp.net" iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Managed" Licensing="HP OneView Advanced" force="true" />
                <server name="wpstdl39-ilo" server="wpstdl39-ilo.vse.rdlabs.hpecorp.net" iloIP="wpstdl39-ilo.vse.rdlabs.hpecorp.net" iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Managed" Licensing="HP OneView Advanced" force="true" />
            </DLServers>
        </servers>

        or:

        data/servers -> @{TestData.servers}
        <servers>
            <server name="wpstdl19-ilo" server="wpstdl19-ilo.vse.rdlabs.hpecorp.net" iloIP="wpstdl19-ilo.vse.rdlabs.hpecorp.net" iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Managed" Licensing="HP OneView Advanced" force="true" />
            <server name="wpstdl39-ilo" server="wpstdl39-ilo.vse.rdlabs.hpecorp.net" iloIP="wpstdl39-ilo.vse.rdlabs.hpecorp.net" iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Managed" Licensing="HP OneView Advanced" force="true" />
        </servers>

    """
    logger.info("======= ----- start adding server hardware for servers %s ----- ======" % [server.name for server in server_obj])
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)

    total = len(server_obj)
    already_exists = 0
    added = 0

    for n, server in enumerate(server_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(server_obj), '-' * 14))

        logger.info("adding a server hardware with name '{0}'".format(server.name))
        if VerifyHardware.verify_server_hardware_not_exist(server.name, fail_if_false=False) is False:
            logger.warn("server '{0}' already exists".format(server.name))
            already_exists += 1
            continue

        AddHardware.click_add_server_hardware_button()
        AddHardware.wait_add_server_hardware_dialog_shown()
        AddHardware.input_ilo_ip(server.iloIP)

        FusionUIBase.para_should_be_in_list(["managed", "monitored"], server.mgmtType.lower())
        if server.mgmtType.lower() == 'managed':
            AddHardware.tick_add_server_hardware_as_managed()
        else:
            AddHardware.tick_add_server_hardware_as_monitored()

        AddHardware.input_ilo_username(server.iloUserName)
        AddHardware.input_ilo_password(server.iloPassword)

        if server.mgmtType.lower() == 'managed':
            FusionUIBase.para_should_be_in_list(["HPE OneView Advanced", "HPE OneView Advanced w/o iLO"], server.Licensing)
            logger.debug("Licensing is [ %s ]" % server.Licensing)
            if server.Licensing == "HPE OneView Advanced":
                AddHardware.tick_licensing_as_hp_oneview_advanced()
            else:
                AddHardware.tick_licensing_as_hp_oneview_advanced_without_ilo()

        AddHardware.click_add_button()

        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
        if status is True:
            if ('being managed by another' in msg) or ('being monitored by another ' in msg):
                logger.warn(msg)
                if server.force.lower() == "true":
                    AddHardware.tick_force_add_option()
                    AddHardware.click_add_button()
                else:
                    logger.warn("Force-Add is not set to 'true', test will be FAILED.")
                    ui_lib.fail_test(msg)
            else:
                logger.warn("Unexpected error occurred: ")
                logger.warn(msg)
                ui_lib.fail_test(msg)

        if AddHardware.wait_add_server_hardware_dialog_disappear(timeout=20, fail_if_false=False) is True:
            FusionUIBase.show_activity_sidebar()
            # FusionUIBase.wait_activity_action_ok(server.name, 'Add', timeout=300, fail_if_false=False)
            timeout = int(getattr(server, 'timeout', "300"))
            if FusionUIBase.wait_activity_action_ok_or_warn(server.name, 'Add', timeout=timeout, fail_if_false=False) is True:
                FusionUIBase.show_activity_sidebar()
                if CommonOperationServerHardware.wait_server_hardware_status_ok_or_warn(server.name, timeout=180, fail_if_false=False) is True:
                    logger.info("Add server hardware {0} successfully".format(server.name))
                    added += 1
                else:
                    logger.warn("'wait_server_hardware_status_ok_or_warn' = FALSE, skip to next server ...")
                    continue
            else:
                logger.warn("'wait_activity_action_ok_or_warn' = FALSE, skip to next server ...")
                FusionUIBase.show_activity_sidebar()
                continue
        else:
            logger.warn("'wait_add_server_hardware_dialog_disappear' = FALSE, skip to next server ...")
            AddHardware.click_cancel_button()
            continue

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - already_exists == 0:
        logger.warn("no server hardware to add! all %s server(s) is already existing in Fusion, keyword '%s' returns TRUE" % (already_exists, sys._getframe().f_code.co_name))
        return True
    else:
        if added < total:
            logger.warn("not all of the server hardware is successfully added - %s out of %s added " % (added, total))
            if added + already_exists == total:
                logger.warn("%s already-existing server(s) is skipped, keyword '%s' returns TRUE" % (already_exists, sys._getframe().f_code.co_name))
                return True
            else:
                logger.warn("%s already-existing server(s) is skipped, "
                            "%s server(s) left is failed being added, "
                            "keyword '%s' returns FALSE" % (already_exists, total - already_exists - added, sys._getframe().f_code.co_name))
                return False

    logger.info("all of the server(s) is successfully added - %s out of %s " % (added, total))
    return True


def launch_console(iloIP):
    """ Launch Console    """
    raise NotImplementedError


def power_on_server_by_name(server_name):
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    #   check if server hardware exists
    if VerifyHardware.verify_server_hardware_exist(server_name, fail_if_false=False) is False:
        logger.warn("server '%s' does not exists" % server_name)
        return False
    CommonOperationServerHardware.click_server_hardware(server_name=server_name, time_for_loading=2)
    FusionUIBase.select_view_by_name(view_name='Hardware', timeout=5, fail_if_false=False)
    #   check if the server state is 'Unsupported' in which POWER ON action is not available
    if VerifyHardware.verify_hardware_state_for_exclusion(excluded_value='Unsupported', timeout=5, fail_if_false=False) is False:
        logger.warn("server '%s' is in 'Unsupported' state, POWER ON action is unavailable" % server_name)
        return False
    #   check if already powered on
    if VerifyHardware.verify_hardware_server_power(expect_value='Off', timeout=5, fail_if_false=False) is False:
        logger.warn("server '%s' is already powered on or in 'None/Unknown' power state, not applicable to perform Power On action. Test is considered PASS" % server_name)
        return True
    #   start performing power on action
    PowerOnHardware.select_action_power_on()
    FusionUIBase.show_activity_sidebar()
    FusionUIBase.wait_activity_action_ok(server_name, 'Power on', timeout=300, fail_if_false=False)
    FusionUIBase.show_activity_sidebar()
    CommonOperationServerHardware.wait_server_hardware_status_ok_or_warn(server_name, timeout=180, fail_if_false=False)
    FusionUIBase.select_view_by_name(view_name='Hardware', timeout=5, fail_if_false=False)
    #   verify the power state is changed to expected 'On'
    if VerifyHardware.verify_hardware_server_power(expect_value='On', timeout=15, fail_if_false=False):
        logger.info("server '%s' is successfully powered on" % server_name)
        return True
    else:
        logger.warn("server '%s' is NOT successfully powered on or timeout for changing power state to 'On'." % server_name)
        return False


def power_on_servers(server_obj):
    """ Power on 1 or multiple Server Hardware

    Arguments:
      name*             --  Name of server hardware as a string.
      ...               --  ...
      ...               --  ...
    * Required Arguments


    Example: - data structure is same as the one used for Add Server Hardware, but only server.name is required


    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)

    total = len(server_obj)
    already_on_or_not_exists = 0
    powered_on = 0

    for n, server in enumerate(server_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(server_obj), '-' * 14))
        logger.info("powering on a server hardware named '%s'" % server.name)
        if VerifyHardware.verify_server_hardware_exist(server.name, fail_if_false=False) is False:
            logger.warn("server '%s' does not exists" % server.name)
            already_on_or_not_exists += 1
            continue
        CommonOperationServerHardware.click_server_hardware(server_name=server.name, time_for_loading=2)
        if VerifyHardware.verify_hardware_server_power(expect_value='Off', timeout=5, fail_if_false=False) is False:
            logger.warn("power state of server '%s' is not 'Off', 'POWER ON' action is unavailable." % server.name)
            already_on_or_not_exists += 1
        else:
            if power_on_server_by_name(server.name) is False:
                logger.warn("server '%s' is NOT powered on successfully" % server.name)
                continue
            else:
                powered_on += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - already_on_or_not_exists == 0:
        logger.warn("no server hardware to power on! all %s server(s) is NOT applicable to power on (already powered on, or not existing), keyword '%s' returns FALSE" % (already_on_or_not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if powered_on < total:
            logger.warn("not all of the server hardware is successfully powered on - %s out of %s powered on " % (powered_on, total))
            if powered_on + already_on_or_not_exists == total:
                logger.warn("%s already-on-or-not-existing server(s) is skipped, keyword '%s' returns FALSE" % (already_on_or_not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s already-on-or-not-existing server(s) is skipped, "
                            "%s server(s) left is failed being powered on " % (already_on_or_not_exists, total - powered_on - already_on_or_not_exists))
                return False

    logger.info("all of the server(s) is successfully powered on - %s out of %s " % (powered_on, total))
    return True


def power_off_server_by_name(server_name, momentary_press=False):
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    #   check if server hardware exists
    if not VerifyHardware.verify_server_hardware_exist(server_name, fail_if_false=False):
        logger.warn("server '%s' does not exists" % server_name)
        return False
    CommonOperationServerHardware.click_server_hardware(server_name=server_name)
    FusionUIBase.select_view_by_name(view_name='Hardware', timeout=5, fail_if_false=False)
    #   check if the server state is 'Unsupported' in which POWER OFF action is not available
    if VerifyHardware.verify_hardware_state_for_exclusion(excluded_value='Unsupported', timeout=5, fail_if_false=False) is False:
        logger.warn("server '%s' is in 'Unsupported' state, POWER OFF action is unavailable" % server_name)
        return False
    #   check if already powered off
    if VerifyHardware.verify_hardware_server_power(expect_value='On', timeout=5, fail_if_false=False) is False:
        logger.warn("server '%s' is already powered off or in 'None/Unknown' power state, not applicable to perform Power Off action, keyword '%s' returns TRUE." % (server_name, sys._getframe().f_code.co_name))
        return True
    #   start performing power off action
    PowerOffHardware.select_action_power_off()
    if momentary_press is False:
        PowerOffHardware.click_press_and_hold_button()
    else:
        PowerOffHardware.click_momentary_press_button()
    FusionUIBase.show_activity_sidebar()
    FusionUIBase.wait_activity_action_ok(server_name, 'Power off', timeout=300, fail_if_false=False)
    FusionUIBase.show_activity_sidebar()
    CommonOperationServerHardware.wait_server_hardware_status_ok_or_warn(server_name, timeout=180, fail_if_false=False)
    FusionUIBase.select_view_by_name(view_name='Hardware', timeout=5, fail_if_false=False)
    #   verify the power state is changed to expected 'Off'
    if VerifyHardware.verify_hardware_server_power(expect_value='Off', timeout=5, fail_if_false=False):
        logger.info("server '%s' is successfully powered off" % server_name)
        return True
    else:
        logger.warn("server '%s' is NOT successfully powered off or timeout for changing power state to 'Off'." % server_name)
        return False


def power_off_servers(server_obj):
    """ Power off 1 or multiple Server Hardware

    Arguments:
      name*             --  Name of server hardware as a string.
      ...               --  ...
      ...               --  ...
    * Required Arguments


    Example: - data structure is same as the one used for Add Server Hardware, but only server.name is required


    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)

    total = len(server_obj)
    already_off_or_not_exists = 0
    powered_off = 0

    for n, server in enumerate(server_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(server_obj), '-' * 14))
        logger.info("powering off a server hardware named '%s'" % server.name)
        if VerifyHardware.verify_server_hardware_exist(server.name, fail_if_false=False) is False:
            logger.warn("server '%s' does not exists" % server.name)
            already_off_or_not_exists += 1
            continue
        CommonOperationServerHardware.click_server_hardware(server_name=server.name, time_for_loading=2)
        if VerifyHardware.verify_hardware_server_power(expect_value='On', timeout=5, fail_if_false=False) is False:
            logger.warn("power state of server '%s' is not 'On', 'POWER OFF' action is unavailable." % server.name)
            already_off_or_not_exists += 1
        else:
            if power_off_server_by_name(server.name, (getattr(server, 'MomentaryPressForPowerOff', '').lower() == 'true')) is False:
                logger.warn("server '%s' is NOT powered off successfully" % server.name)
                continue
            else:
                powered_off += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - already_off_or_not_exists == 0:
        logger.warn("no server hardware to power off! all %s server(s) is NOT applicable to power off (already powered off, or not existing), keyword '%s' returns FALSE" % (already_off_or_not_exists, sys._getframe().f_code.co_name))
        return True
    else:
        if powered_off < total:
            logger.warn("not all of these server hardware is successfully powered off - %s out of %s powered off " % (powered_off, total))
            if powered_off + already_off_or_not_exists == total:
                logger.warn("%s already-off-or-not-existing server(s) is skipped, keyword '%s' returns FALSE" % (already_off_or_not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s already-off-or-not-existing server(s) is skipped, "
                            "%s server(s) left is failed being powered off " % (already_off_or_not_exists, total - powered_off - already_off_or_not_exists))
                return False

    logger.info("all of the server(s) is successfully powered off - %s out of %s " % (powered_off, total))
    return True


def power_off_all_server_hardware():
    """ Power Off All Servers    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    server_name_list = CommonOperationServerHardware.get_server_hardware_list()

    total = len(server_name_list)
    off_or_unsupported = 0
    powered_off = 0

    if total == 0:
        logger.warn("no server hardware is added in Fusion, will exit execution")
        return True

    for n, server_name in enumerate(server_name_list):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(server_name_list), '-' * 14))
        logger.info("powering off a server hardware named '%s'" % server_name)
        CommonOperationServerHardware.click_server_hardware(server_name=server_name, time_for_loading=2)
        if VerifyHardware.verify_hardware_server_power(expect_value='On', timeout=5, fail_if_false=False) is False:
            logger.warn("power state of server '%s' is not 'On', nothing needs to be done." % server_name)
            off_or_unsupported += 1
        else:
            if power_off_server_by_name(server_name) is False:
                logger.warn("server '%s' is NOT powered off successfully" % server_name)
                continue
            else:
                powered_off += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - off_or_unsupported == 0:
        logger.warn("no server hardware to power off! all %s server(s) is NOT applicable to power off (already powered off or unsupported), test is considered PASS" % off_or_unsupported)
        return True
    else:
        if powered_off < total:
            logger.warn("not all of these server hardware is successfully powered off - %s out of %s powered off " % (powered_off, total))
            if powered_off + off_or_unsupported == total:
                logger.warn("%s off-or-unsupported server(s) is skipped, test is considered PASS" % off_or_unsupported)
                return True
            else:
                logger.warn("%s off-or-unsupported server(s) is skipped, %s server(s) left is failed being powered off " % (off_or_unsupported, total - powered_off - off_or_unsupported))
                return False

    logger.info("all of the server(s) is successfully powered off - %s out of %s " % (powered_off, total))
    return True


def validate_server_hardware_task_status_from_activity_view(server_name, activity_task, action_name, expect_task_status):
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    #   check if server hardware exists
    VerifyHardware.verify_server_hardware_exist(server_name)
    CommonOperationServerHardware.click_server_hardware(server_name)
    FusionUIBase.select_view_by_name('Activity')
    return VerifyHardware.verify_server_hardware_task_status_from_activity_view(server_name, activity_task, action_name, expect_task_status)


def validate_reset_ilo_was_blocked(server_name, msg):
    """ Validate reset ilo was blocked with the given msg
    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    #   check if server hardware exists
    VerifyHardware.verify_server_hardware_exist(server_name)
    CommonOperationServerHardware.click_server_hardware(server_name)
    FusionUIBase.select_view_by_name('Hardware')
    #   check if the server state is 'Unsupported' in which RESET action is not available
    VerifyHardware.verify_hardware_state_for_exclusion('Unsupported')
    #   start performing reset ilo action
    ResetHardware.select_action_reset_ilo()
    ResetHardware.wait_reset_ilo_dialog_open()
    if ResetHardware.verify_reset_ilo_dialog_msg(msg, fail_if_false=False):
        logger.info("reset ilo was blocked as expected with msg %s" % msg)
        ResetHardware.click_close_reset_ilo_button()
    else:
        ui_lib.fail_test("reset ilo was not blocked as expected msg '%s'" % msg)


def reset_ilo(server_obj):
    """ Reset 1 or multiple Server Hardware ILO

    Arguments:
      name*             --  Name of server hardware as a string.
      wait_complete*     --  If wait_complete is false, do not wait for the whole task to be finished, else opposite
      ...               --  ...
      ...               --  ...
    * Required Arguments


    Example: - data structure is same as the one used for Add Server Hardware, but only server.name is required

    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)

    total = len(server_obj)
    not_support = 0

    for n, server in enumerate(server_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(server_obj), '-' * 14))
        logger.info("reset ilo for server hardware named '%s'" % server.name)
        VerifyHardware.verify_server_hardware_exist(server.name)
        CommonOperationServerHardware.click_server_hardware(server.name)
        FusionUIBase.select_view_by_name('Hardware')
        #   check if the server state is 'Unsupported' in which RESET action is not available
        if VerifyHardware.verify_hardware_state_for_exclusion(excluded_value='Unsupported', timeout=5, fail_if_false=False) is False:
            logger.warn("server '%s' is in 'Unsupported' state, RESET iLO action is unavailable." % server.name)
            not_support += 1
        else:
            ResetHardware.select_action_reset_ilo()
            ResetHardware.wait_reset_ilo_dialog_open()
            ResetHardware.click_yes_reset_ilo_button()
            ResetHardware.wait_reset_ilo_dialog_close(timeout=180, fail_if_false=True)
            if server.wait_complete.lower() == "true":
                FusionUIBase.show_activity_sidebar()
                FusionUIBase.wait_activity_action_ok(server.name, 'Reset iLO', timeout=300, fail_if_false=True)
                FusionUIBase.show_activity_sidebar()
                CommonOperationServerHardware.wait_server_hardware_status_ok_or_warn(server.name, timeout=300, fail_if_false=True)
                logger.info("server '%s' is successfully refreshed" % server.name)
            if server.wait_complete.lower() == "false":
                logger.info("reset ilo action  of '%s' is successfully but no need to wait for task complete" % server.name)

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_support == 0:
        logger.warn("no server hardware to reset ilo! all %s server(s) is NOT supported, test is considered PASS" % not_support)
        return True

    logger.info("%s server's iLO have been successfully reset and %s servers were not supported." % ((total - not_support), not_support))
    return True


def reset_server_by_name(server_name):
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    #   check if server hardware exists
    if not VerifyHardware.verify_server_hardware_exist(server_name, fail_if_false=False):
        logger.warn("server '%s' does not exists" % server_name)
        return False
    CommonOperationServerHardware.click_server_hardware(server_name=server_name)
    FusionUIBase.select_view_by_name(view_name='Hardware', timeout=5, fail_if_false=False)
    #   check if the server state is 'Unsupported' in which RESET action is not available
    if VerifyHardware.verify_hardware_state_for_exclusion(excluded_value='Unsupported', timeout=5, fail_if_false=False) is False:
        logger.warn("server '%s' is in 'Unsupported' state, RESET action is unavailable." % server_name)
        return False
    #   check if powered on, reset/cold boot is only doable when server is powered on
    if VerifyHardware.verify_hardware_server_power(expect_value='On', timeout=5, fail_if_false=False) is False:
        logger.warn("server '%s' is not powered on, RESET action is unavailable." % server_name)
        return False
    #   start performing reset action
    ResetHardware.select_action_reset()
    ResetHardware.click_reset_button()
    FusionUIBase.show_activity_sidebar()
    FusionUIBase.wait_activity_action_ok(server_name, 'Reset', timeout=300, fail_if_false=False)
    FusionUIBase.show_activity_sidebar()
    CommonOperationServerHardware.wait_server_hardware_status_ok_or_warn(server_name, timeout=180, fail_if_false=False)
    FusionUIBase.select_view_by_name(view_name='Hardware', timeout=5, fail_if_false=False)
    #   verify the power state is changed to expected 'On'
    if VerifyHardware.verify_hardware_server_power(expect_value='On', timeout=5, fail_if_false=False):
        logger.info("server '%s' is successfully performed reset." % server_name)
        return True
    else:
        logger.warn("server '%s' is NOT successfully performed reset or timeout for changing power state to 'On'." % server_name)
        return False


def reset_servers(server_obj):
    """ Reset 1 or multiple Server Hardware

    Arguments:
      name*             --  Name of server hardware as a string.
      ...               --  ...
      ...               --  ...
    * Required Arguments


    Example: - data structure is same as the one used for Add Server Hardware, but only server.name is required


    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)

    total = len(server_obj)
    off_or_unsupported = 0
    done_reset = 0

    for n, server in enumerate(server_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(server_obj), '-' * 14))
        logger.info("reset a server hardware named '%s'" % server.name)
        CommonOperationServerHardware.click_server_hardware(server_name=server.name, time_for_loading=2)
        if VerifyHardware.verify_hardware_server_power(expect_value='On', timeout=5, fail_if_false=False) is False:
            logger.warn("Power state of server '%s' is not 'On', RESET action is unavailable." % server.name)
            off_or_unsupported += 1
        else:
            if reset_server_by_name(server.name) is False:
                logger.warn("server '%s' is NOT reset successfully" % server.name)
                continue
            else:
                done_reset += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - off_or_unsupported == 0:
        logger.warn("no server hardware to reset! all %s server(s) is NOT applicable to reset (already powered off or unsupported), test is considered PASS" % off_or_unsupported)
        return True
    else:
        if done_reset < total:
            logger.warn("not all of these server hardware is successfully reset - %s out of %s reset " % (done_reset, total))
            if done_reset + off_or_unsupported == total:
                logger.warn("%s off-or-unsupported server(s) is skipped, test is considered PASS" % off_or_unsupported)
                return True
            else:
                logger.warn("%s off-or-unsupported server(s) is skipped, %s server(s) left is failed being reset " % (off_or_unsupported, total - done_reset - off_or_unsupported))
                return False

    logger.info("all of the server(s) is successfully done reset - %s out of %s " % (done_reset, total))
    return True


def cold_boot_server_by_name(server_name):
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    #   check if server hardware exists
    if not VerifyHardware.verify_server_hardware_exist(server_name, fail_if_false=False):
        logger.warn("server '%s' does not exists" % server_name)
        return False
    CommonOperationServerHardware.click_server_hardware(server_name=server_name)
    FusionUIBase.select_view_by_name(view_name='Hardware', timeout=5, fail_if_false=False)
    #   check if the server state is 'Unsupported' in which COLD BOOT action is not available
    if VerifyHardware.verify_hardware_state_for_exclusion(excluded_value='Unsupported', timeout=5, fail_if_false=False) is False:
        logger.warn("server '%s' is in 'Unsupported' state, RESET action is unavailable" % server_name)
        return False
    #   check if powered on, reset/cold boot is only doable when server is powered on
    if VerifyHardware.verify_hardware_server_power(expect_value='On', timeout=5, fail_if_false=False) is False:
        logger.warn("server '%s' is not powered on, or its power state is unknown, COLD BOOT action cannot be performed." % server_name)
        return False
    #   start performing cold boot action
    ResetHardware.select_action_reset()
    ResetHardware.click_cold_boot_button()
    FusionUIBase.show_activity_sidebar()
    FusionUIBase.wait_activity_action_ok(server_name, 'Reset', timeout=300, fail_if_false=False)
    FusionUIBase.show_activity_sidebar()
    CommonOperationServerHardware.wait_server_hardware_status_ok_or_warn(server_name, timeout=180, fail_if_false=False)
    FusionUIBase.select_view_by_name(view_name='Hardware', timeout=5, fail_if_false=False)
    #   verify the power state is changed to expected 'On'
    if VerifyHardware.verify_hardware_server_power(expect_value='On', timeout=5, fail_if_false=False) is True:
        logger.info("server '%s' is successfully performed cold boot" % server_name)
        return True
    else:
        logger.warn("server '%s' is NOT successfully performed cold boot or timeout for changing power state to 'On'." % server_name)
        return False


def cold_boot_servers(server_obj):
    """ Cold boot 1 or multiple Server Hardware

    Arguments:
      name*             --  Name of server hardware as a string.
      ...               --  ...
      ...               --  ...
    * Required Arguments


    Example: - data structure is same as the one used for Add Server Hardware, but only server.name is required


    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)

    total = len(server_obj)
    off_or_unsupported = 0
    done_cold_boot = 0

    for n, server in enumerate(server_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(server_obj), '-' * 14))
        logger.info("cold boot a server hardware named '%s'" % server.name)
        CommonOperationServerHardware.click_server_hardware(server_name=server.name, time_for_loading=2)
        if VerifyHardware.verify_hardware_server_power(expect_value='On', timeout=5, fail_if_false=False) is False:
            logger.warn("Power state of server '%s' is not 'On', 'RESET -> COLD BOOT' action is unavailable." % server.name)
            off_or_unsupported += 1
        else:
            if cold_boot_server_by_name(server.name) is False:
                logger.warn("server '%s' is NOT done cold boot successfully" % server.name)
                continue
            else:
                done_cold_boot += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - off_or_unsupported == 0:
        logger.warn("no server hardware to cold boot! all %s server(s) is NOT applicable to cold boot (already powered off or unsupported), test is considered PASS" % off_or_unsupported)
        return True
    else:
        if done_cold_boot < total:
            logger.warn("not all of these server hardware is successfully done cold boot - %s out of %s done cold boot " % (done_cold_boot, total))
            if done_cold_boot + off_or_unsupported == total:
                logger.warn("%s off-or-unsupported server(s) is skipped, test is considered PASS" % off_or_unsupported)
                return True
            else:
                logger.warn("%s off-or-unsupported server(s) is skipped, %s server(s) left is failed to cold boot " % (off_or_unsupported, total - done_cold_boot - off_or_unsupported))
                return False

    logger.info("all of the server(s) is successfully done cold boot - %s out of %s " % (done_cold_boot, total))
    return True


def refresh_server_by_name(server_name):
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    #   check if server hardware exists
    if not VerifyHardware.verify_server_hardware_exist(server_name, fail_if_false=False):
        logger.warn("server '%s' does not exists" % server_name)
        return False
    CommonOperationServerHardware.click_server_hardware(server_name=server_name)
    FusionUIBase.select_view_by_name(view_name='Hardware', timeout=5, fail_if_false=False)
    #   check if the server state is 'Unsupported' in which REFRESH action is not available
    if VerifyHardware.verify_hardware_state_for_exclusion(excluded_value='Unsupported', timeout=5, fail_if_false=False) is False:
        logger.warn("server '%s' is in 'Unsupported' state, 'REFRESH' action is unavailable" % server_name)
        return False
    #   start performing refresh action
    RefreshHardware.select_action_refresh()
    FusionUIBase.show_activity_sidebar()
    if FusionUIBase.wait_activity_action_ok_or_warn(server_name, 'Refresh', timeout=300, fail_if_false=False) is True:
        FusionUIBase.show_activity_sidebar()
        if CommonOperationServerHardware.wait_server_hardware_status_ok_or_warn(server_name, timeout=180, fail_if_false=False) is True:
            logger.info("server '%s' is successfully refreshed" % server_name)
            return True
        else:
            logger.warn("server '%s' is NOT successfully refreshed or error occurred due to its status is neither 'ok' nor 'warn'" % server_name)
            return False
    else:
        logger.warn("server '%s' is NOT successfully refreshed" % server_name)
        return False


def refresh_servers(server_obj):
    """ Cold boot 1 or multiple Server Hardware

    Arguments:
      name*             --  Name of server hardware as a string.
      ...               --  ...
      ...               --  ...
    * Required Arguments


    Example: - data structure is same as the one used for Add Server Hardware, but only server.name is required


    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)

    total = len(server_obj)
    unsupported = 0
    refreshed = 0

    for n, server in enumerate(server_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(server_obj), '-' * 14))
        logger.info("refresh a server hardware named '%s'" % server.name)
        CommonOperationServerHardware.click_server_hardware(server_name=server.name, time_for_loading=2)
        FusionUIBase.select_view_by_name(view_name='Hardware', timeout=5, fail_if_false=False)
        #   check if the server state is 'Unsupported' in which REFRESH action is not available
        if VerifyHardware.verify_hardware_state_for_exclusion(excluded_value='Unsupported', timeout=5, fail_if_false=False) is False:
            logger.warn("server '%s' is in 'Unsupported' state, 'REFRESH' action is unavailable" % server.name)
            unsupported += 1
        else:
            if refresh_server_by_name(server.name) is False:
                logger.warn("server #%s '%s' is NOT successfully refreshed" % (n, server.name))
                continue
            else:
                refreshed += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - unsupported == 0:
        logger.warn("no server hardware to refresh! all %s server(s) is NOT applicable to refresh (already powered off or unsupported), test is considered PASS" % unsupported)
        return True
    else:
        if refreshed < total:
            logger.warn("not all of these server hardware is successfully refreshed - %s out of %s done refresh " % (refreshed, total))
            if refreshed + unsupported == total:
                logger.warn("%s unsupported server(s) is skipped, test is considered PASS" % unsupported)
                return True
            else:
                logger.warn("%s unsupported server(s) is skipped, %s server(s) left is failed to refresh " % (unsupported, total - refreshed - unsupported))
                return False

    logger.info("all of the server(s) is successfully done refresh - %s out of %s " % (refreshed, total))
    return True


def force_refresh_server(server_obj):
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)

    servers_failed = []

    for n, server in enumerate(server_obj):
        #   check if server hardware exists
        if not VerifyHardware.verify_server_hardware_exist(server.name, fail_if_false=False):
            logger.warn("server '%s' does not exists" % server.name)
            return False
        CommonOperationServerHardware.click_server_hardware(server.name)
        FusionUIBase.select_view_by_name(view_name='Hardware', timeout=5, fail_if_false=False)
        # start performing refresh action
        RefreshHardware.select_action_refresh()

        RefreshHardware.wait_until_refresh_dialog_is_visible(timeout=10)
        if RefreshHardware.is_refresh_dialog_visible():
            RefreshHardware.input_ilo_hostname(server.iloIP)
            RefreshHardware.input_ilo_username(server.iloUserName)
            RefreshHardware.input_ilo_password(server.iloPassword)
            RefreshHardware.click_ok_button()
            RefreshHardware.wait_until_refresh_dialog_is_closed(timeout=10)

        FusionUIBase.show_activity_sidebar()
        if FusionUIBase.wait_activity_action_ok(server.name, 'Refresh', timeout=300, fail_if_false=False):
            logger.info("server '%s' is successfully refreshed." % server.name)
            FusionUIBase.show_activity_sidebar()
        else:
            logger.warn("server '%s' is NOT successfully refreshed or timeout for changing status to 'Ok'." % server.name)
            FusionUIBase.show_activity_sidebar()
            servers_failed.append(server.name)

    if servers_failed:
        return False

    return True


def remove_server_by_name(server_name, fail_if_false=True):
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    #   check if server hardware exists
    if not VerifyHardware.verify_server_hardware_exist(server_name, fail_if_false=False):
        logger.warn("Server '%s' does not exists" % server_name)
        return True
    CommonOperationServerHardware.click_server_hardware(server_name=server_name)
    #   start performing remove action
    RemoveHardware.select_action_remove()
    RemoveHardware.click_yes_remove_button()

    FusionUIBase.show_activity_sidebar()
    FusionUIBase.wait_activity_action_ok(server_name, 'Remove', timeout=240, fail_if_false=False)
    FusionUIBase.show_activity_sidebar()

    #   verify server hardware is not existing after being removed
    start = datetime.now()
    timeout = 180  # 5 minutes
    while (datetime.now() - start).total_seconds() < timeout:
        if CommonOperationServerHardware.wait_server_hardware_show_not_found(server_name, timeout=5, fail_if_false=False):
            logger.info("server '%s' status appears as 'not found' - successfully removed." % server_name)
            return True
        elif VerifyHardware.verify_server_hardware_not_exist(server_name, timeout=5, fail_if_false=False):
            logger.info("server '%s' is successfully removed." % server_name)
            return True
    else:
        msg = "server '%s' is NOT successfully removed or timeout issue occurred." % server_name
        return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)


def remove_servers(server_obj):
    """ Remove Server Hardware

    Arguments:
      name*             --  Name of server hardware as a string.
      server            --  hostname of the iLO of the server hardware.
      iloIP             --  IP address/hostname of the iLO of the server hardware.
      iloUserName       --  iLO's Admin username.
      iloPassword       --  iLO's Admin password.
      mgmtType          --  what type the server hardware will be added as, Managed/Monitored.
      Licensing         --  Licensing type, 'HP OneView Advanced'/'HP OneView Advanced w/o iLO'.
      force             --  Force add the server hardware if it's being managed by another system

    * Required Arguments


    Example: - data structure is same as the one used for Add Server Hardware, but only server.name is required
        data/servers/dlserver -> @{TestData.servers.DLServers}
        <servers>
            <DLServers>
                <server name="wpstdl19-ilo" server="wpstdl19-ilo.vse.rdlabs.hpecorp.net" iloIP="wpstdl19-ilo.vse.rdlabs.hpecorp.net" iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Managed" Licensing="HP OneView Advanced" force="true" />
                <server name="wpstdl39-ilo" server="wpstdl39-ilo.vse.rdlabs.hpecorp.net" iloIP="wpstdl39-ilo.vse.rdlabs.hpecorp.net" iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Managed" Licensing="HP OneView Advanced" force="true" />
            </DLServers>
        </servers>

        or:

        data/servers -> @{TestData.servers}
        <servers>
            <server name="wpstdl19-ilo" server="wpstdl19-ilo.vse.rdlabs.hpecorp.net" iloIP="wpstdl19-ilo.vse.rdlabs.hpecorp.net" iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Managed" Licensing="HP OneView Advanced" force="true" />
            <server name="wpstdl39-ilo" server="wpstdl39-ilo.vse.rdlabs.hpecorp.net" iloIP="wpstdl39-ilo.vse.rdlabs.hpecorp.net" iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Managed" Licensing="HP OneView Advanced" force="true" />
        </servers>

    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)

    total = len(server_obj)
    not_exists = 0
    removed = 0

    for n, server in enumerate(server_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(server_obj), '-' * 14))
        logger.info("removing a server hardware named '%s'" % server.name)
        if VerifyHardware.verify_server_hardware_exist(server.name, fail_if_false=False) is False:
            logger.warn("server '%s' does not exists" % server.name)
            not_exists += 1
        else:
            if not remove_server_by_name(server.name, fail_if_false=False):
                logger.warn("server '%s' is NOT removed successfully." % server.name)
                continue
            else:
                removed += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no server hardware to delete! all %s server hardware is NOT existing, keyword '%s' returns TRUE" % (not_exists, sys._getframe().f_code.co_name))
        return True
    else:
        if removed < total:
            logger.warn("not all of the server hardware is successfully removed - %s out of %s removed " % (removed, total))
            if removed + not_exists == total:
                logger.warn("%s non-existing server hardware is skipped, keyword '%s' returns TRUE" % (not_exists, sys._getframe().f_code.co_name))
                return True
            else:
                logger.warn("%s non-existing server hardware is skipped, "
                            "%s server hardware left is failed being removed, "
                            "keyword '%s' returns FALSE " % (not_exists, total - removed - not_exists, sys._getframe().f_code.co_name))
                return False

    logger.info("all of the server hardware is successfully removed - %s out of %s " % (removed, total))
    return True


def get_type_of_server_hardware(server_name):
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    #   check if server hardware exists
    if not VerifyHardware.verify_server_hardware_exist(server_name, fail_if_false=False):
        logger.warn("Server '%s' does not exists" % server_name)
        return 'None'
    CommonOperationServerHardware.click_server_hardware(server_name=server_name)
    FusionUIBase.select_view_by_name(view_name='Hardware', timeout=8, fail_if_false=False)
    ret = CommonOperationServerHardware.get_server_hardware_type(server_name=server_name, fail_if_false=False)

    if ret is not None:
        return ret
    else:
        logger.warn("'None' is returned -- failed to get hardware type of server '%s'" % server_name)
        return 'None'


def select_server(serverName):
    """ Select Server    """
    """ This function is to select a particular server
    Example:
       select_server(serverName)
    """
    ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_SERVER_COUNT, PerfConstants.FUSION_PAGE_SYNC)
    if ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_TABLE_SERVER_NAME % serverName):
        logger.info("The given server is selected - %s" % serverName)
        return True
    else:
        logger.info("The given server is not present - %s" % serverName)
        return False


def get_server_powerstatus(serverName):
    """ Get Server Powerstatus    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)

    if VerifyHardware.verify_server_hardware_exist(serverName, fail_if_false=False) is False:
        logger.warn("Server '%s' does not exists" % serverName)
        return False

    select_server(serverName)
    FusionUIBase.select_view_by_name(view_name='Overview', timeout=5, fail_if_false=False)

    return CommonOperationServerHardware.get_server_hardware_power_state(serverName)


def get_profilename_associated_to_server(serverName):
    """ Get Profile name Associated To Server    """
    navigate()
    Selenium2lib = ui_lib.get_s2l()
    profileStatus = Selenium2lib.get_text(FusionServerHardwarePage.ID_ELEMENT_SERVER_PROFILE_BASE % serverName)
    return profileStatus


def _verify_server_in_activity(LicenseName, ServeriloIP, strTimeStamp, ServerName):
    """ _verify_server_in_activity

        Example:
        | _verify_server_in_activity("HP OneView",'172.24.121.32',"Today 6.40 PM","ILOMXQ2210413")
    """

    """ Verify the ADD server Hardware Activity in Activity Page """
    s2l = ui_lib.get_s2l()

    if not s2l._is_element_present(FusionActivityPage.ID_PAGE_LABEL):
        base_page.navigate_base(FusionActivityPage.ID_PAGE_LABEL, FusionUIBaseElements.ID_MENU_LINK_ACTIVITY, "css=span.hp-page-item-count")

    """Validating the creation of server Hardware with time stamp and activity """
    ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_ACTIVITY_COLLAPSE % (strTimeStamp, ServerName))

    """ Click on collapse button and check the license and validate """
    if s2l._is_element_present(FusionServerHardwarePage.ID_ACTIVITY_NOTIFY_CONTAINER):
        logger.info("Check the license information in the Activity notification")
        strmsg = s2l._get_text(FusionServerHardwarePage.ID_ACTIVITY_NOTIFY_DETAILS)

        """ Verifying the license name in activity notification """
        if (LicenseName.lower() in strmsg.lower()):
            logger.info("Server %s is added with selected license HP %s" % (ServeriloIP, LicenseName))
        else:
            logger.info("Activity notify message %s" % strmsg)

    else:
        logger.warn("Fail to select the Add Server Hardware activity for %s in Activity Page" % ServeriloIP)


def _get_server_hardware_info(serverName, attributes="all"):
    """ This function will get server hardware info
    from appliance hardware dropdown

     Example:
        | get server hardware info      | ${serverName}    |
        | get server hardware info      | ${serverName}    |  ServerHardawreType    |
        | get server hardware info      | ${serverName}    |  ServerHardawreType,PoweredBy    |
    """
    s2l = ui_lib.get_s2l()
    dict_hardware_data = {}
    if not s2l._is_element_present(FusionServerHardwarePage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()
    rc = select_server(serverName)
    if (not rc):
        logger.warn("Failed to select Server Hardware '%s'" % serverName)

    ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_ELEMENT_SERVER_OVERVIEW)
    ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_OVERVIEW_LINK_HARDWARE)
    ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_ELEMENT_SERVER_STATE)
    ui_lib.wait_for_element(FusionServerHardwarePage.ID_ELEMENT_SERVER_STATE)

    xpaths = {
        "ServerState": FusionServerHardwarePage.ID_ELEMENT_SERVER_STATE,
        "ServerProfile": FusionServerHardwarePage.ID_ELEMENT_SERVER_PROFILE,
        "ServerPowerOn": FusionServerHardwarePage.ID_ELEMENT_SERVER_POWER_ON,
        "ServerModel": FusionServerHardwarePage.ID_SERVER_MODEL,
        "ServerHardwareType": FusionServerHardwarePage.ID_SERVER_HARDWARE_TYPE,
        "ServerProductId": FusionServerHardwarePage.ID_SERVER_PRODUCT_ID,
        "ServerSerialNo": FusionServerHardwarePage.ID_SERVER_SER_NUM,
        "ServerSerialUid": FusionServerHardwarePage.ID_SER_UID,
        "ServerLicense": FusionServerHardwarePage.ID_SERVER_LICENSE,
        "IloHostName": FusionServerHardwarePage.ID_ILO_HOST_NAME,
        "IloIpv4": FusionServerHardwarePage.ID_ILO_IPV4,
        "ServerLocation": FusionServerHardwarePage.ID_LINK_SERVER_LOCATION,
        "PoweredBy": FusionServerHardwarePage.ID_LINK_POWEREDBY,
        "AssetTag": FusionServerHardwarePage.ID_LINK_ASSETTAG,
        "MaxPower": FusionServerHardwarePage.ID_LINK_MAX_POWER,
        "PowerUnit": FusionServerHardwarePage.ID_LINK_POWER_UNIT,
        "Cpu": FusionServerHardwarePage.ID_LINK_CPU,
        "Memory": FusionServerHardwarePage.ID_LINK_MEMORY,
        "RomVersion": FusionServerHardwarePage.ID_LINK_ROM_VERSION,
        "IloVersion": FusionServerHardwarePage.ID_LINK_ILO_VERSION,
    }

    if attributes.lower() == "all":
        # Default value will get all information
        attributes = xpaths.keys()
    elif ',' in attributes:
        # Multiple specified attributes. eg: "MaxPower,Cpu"
        attributes = attributes.split(",")
    else:
        # Single specified attribute. eg: "ServerHardwareType"
        attributes = [attributes]

    for attribute in attributes:
        logger.info("Fetching '%s' server hardware info from appliance" % attribute)
        if ui_lib.wait_for_element_visible(xpaths[attribute], PerfConstants.DEFAULT_SYNC_TIME):
            val = str(ui_lib.ignore_staleElementRefException("get_text", xpaths[attribute]))
            dict_hardware_data[attribute] = val
            logger.info("added %s" % attribute)
        else:
            logger.warn("not able to find %s" % attribute)

    return dict_hardware_data


def _get_server_port_info(serverName):
    """ This function will get server port info
    from appliance ports dropdown

     Example:
        | get server port info      | ${serverName}    |
    """
    s2l = ui_lib.get_s2l()
    if not s2l._is_element_present(FusionServerHardwarePage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()
    dict_port_data = {}
    select_server(serverName)
    s2l.maximize_browser_window()
    ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_ELEMENT_SERVER_OVERVIEW)
    ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_LINK_PORTS, PerfConstants.DEFAULT_SYNC_TIME)
    rowcount = 1
    ui_lib.wait_for_element(FusionServerHardwarePage.ID_TABLE_SERVER_HARDWARE_PORT_ROW % (rowcount, 1), PerfConstants.DEFAULT_SYNC_TIME)
    logger.info("Fetching server port info from appliance")

    slot = str(ui_lib.get_text(FusionServerHardwarePage.ID_TABLE_SERVER_HARDWARE_PORT_ROW % (rowcount, 1)))
    if slot != "" or slot != "empty":
        dict_port_data["slot" + str(rowcount)] = slot
    else:
        dict_port_data["slot" + str(rowcount)] = ""

    model = ui_lib.get_text(FusionServerHardwarePage.ID_TABLE_SERVER_HARDWARE_PORT_ROW % (1, 2))
    if model != "" or model != "empty":
        dict_port_data["model1"] = model
    else:
        dict_port_data["model1"] = ""

    while (s2l._is_element_present(FusionServerHardwarePage.ID_TABLE_SERVER_HARDWARE_ADDRESS_ROW % (rowcount * 2 + 1, 1))):
        port = str(ui_lib.get_text(FusionServerHardwarePage.ID_TABLE_SERVER_HARDWARE_PORT_ROW % (rowcount * 2, 1)))
        port = port.split()
        if port != "" or port != "empty":
            dict_port_data["port" + str(rowcount)] = port[1]
        else:
            dict_port_data["port" + str(rowcount)] = ""

        address = str(ui_lib.get_text(FusionServerHardwarePage.ID_TABLE_SERVER_HARDWARE_ADDRESS_ROW % ((rowcount * 2 + 1), 1)))
        if address != "" or address != "empty":
            dict_port_data["address" + str(rowcount)] = address
        else:
            dict_port_data["address" + str(rowcount)] = ""

        interconnect = str(ui_lib.get_text(FusionServerHardwarePage.ID_TABLE_SERVER_HARDWARE_INTERCONNECT_DOWNLINK_ROW % ((rowcount * 2 + 1), 1)))
        interconnect = interconnect.split(", ")
        if interconnect != "" or interconnect != "empty":
            dict_port_data["interconnect" + str(rowcount)] = interconnect[0] + ", " + interconnect[1]
        else:
            dict_port_data["interconnect" + str(rowcount)] = ""

        downlink = str(ui_lib.get_text(FusionServerHardwarePage.ID_TABLE_SERVER_HARDWARE_INTERCONNECT_DOWNLINK_ROW % ((rowcount * 2 + 1), 1)))
        downlink = downlink.split(", ")
        if downlink != "" or downlink != "empty":
            dict_port_data["downlink" + str(rowcount)] = downlink[2]
        else:
            dict_port_data["downlink" + str(rowcount)] = ""

        rowcount = rowcount + 1

    return dict_port_data


def _retrieve_server_data(bay_no, encl_ip, encl_usrname, encl_passwd):
    """ This function will return a dictionary of server info retrieved from OA
        Example:
        _get_server_info(bay_no, encl_ip, encl_usrname, encl_passwd)
    """
    server_info = {}
    oainfo = blade_info(encl_ip, encl_usrname, encl_passwd)
    server_oa_info = oainfo.get_server_info_from_oa(bay_no)
    server_info["ServerModel"] = server_oa_info["model"]
    server_info["ServerSerialNo"] = server_oa_info["SerialNo"]
    server_info["ServerSerialUid"] = server_oa_info["uuid"]
    server_info["IloHostName"] = server_oa_info["hostname"]
    server_info["IloIpv4"] = server_oa_info["ip"]
    return server_info


def validate_server_hardware_page_hardware(server_obj, compare_with_ilo=False):
    """ Validate hardware attributes on server hardware page.

    Arguments:
      server_object
        name*        --  Name of server hardware as a string.
        server*      --  hostname of the iLO of the server hardware.
        iloIP*       --  IP address/hostname of the iLO of the server hardware.
        iloUserName* --  iLO's Admin username.
        iloPassword* --  iLO's Admin password.
        mgmtType*    --  what type the server hardware will be added as, Managed/Monitored.
        Licensing*   --  Licensing type, 'HP OneView Advanced'/'HP OneView Advanced w/o iLO'/'HP OneView Standard'.
        force*       --  Force add the server hardware if it's being managed by another system
        Hardware*
          State*
          ServerProfile*
          ServerPower
          Model
          ServerHardwareType
          ProductID
          SerialNumber
          License*
          UUID
          iLO*
          Location
          PoweredBy
          AssetTag
          MaximumPower
          CPU
          Memory
          RomVersion
          iLOVersion
          IntelligentProvisioningVersion
      compare_with_ilo    --  if set to "True", compares with the values retrieved from iLO.

    * Required Arguments

    Example:
        data/RackServersForMonitoring -> @{TestData.RackServersForMonitoring}
        <RackServersForMonitoring>
            <server name="wpstdl41-ilo" server="16.125.77.18" iloIP="16.125.77.18" iloUserName="Administrator"
            iloPassword="hpvse1-ilo" mgmtType="Monitored" Licensing="HP OneView Standard">
                <Hardware>
                    <State expected_value="Monitored"/>
                    <ServerProfile expected_value="n/a">
                    <ServerPower expected_value="">
                    <Model expected_value="">
                    <ServerHardwareType expected_value="">
                    <ProductID expected_value="">
                    <SerialNumber expected_value="">
                    <License expected_value="HP OneView Standard">
                    <UUID expected_value="">
                    <iLO expected_value="">
                    <Location expected_value="">
                    <PoweredBy expected_value="">
                    <AssetTag expected_value="">
                    <MaximumPower expected_value="">
                    <CPU expected_value="">
                    <Memory expected_value="">
                    <RomVersion expected_value="">
                    <iLOVersion expected_value="">
                    <IntelligentProvisioningVersion expected_value="">
                </Hardware>
            </server>
            <server name="wpstdl16-ilo" server="wpstdl16-ilo.vse.rdlabs.hpecorp.net" iloIP="16.125.68.91"
            iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Monitored" Licensing="HP OneView Standard"/>
        </RackServersForMonitoring>

    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)

    attributes_not_match = ''

    for n, server in enumerate(server_obj):
        # Stop validation if no expected value defined in node "Hardware"
        if not server.has_property('Hardware'):
            logger.warn("did not find node 'Hardware' in %s" % server.name)
            return False

        # Get actual hardware information on server hardware page
        actual_hardware_info = _get_server_hardware_info(server.name)

        # Get expected value from test data
        expected_hardware_info = _get_hardware_info_from_test_data(server.Hardware)

        if compare_with_ilo:
            # Get expected value through iLO cli and update the expected value
            # ToDo
            pass

        # Compare if match. When Business logical functions get ready, replace with them
        for key, value in expected_hardware_info.items():

            # skip attributes that may be changed
            # TODO: use iLO CLI/API method to get ServerPower/ROM/MaxPower/iLOVersion info as validating seed data instead of static data in data fifle
            if key in ['ServerPowerOn', 'MaxPower', 'RomVersion', 'IloVersion']:
                logger.warn("Skip validation for hardware attributes: %s" % key)
                continue

            if key in actual_hardware_info:
                if value == actual_hardware_info[key]:
                    logger.info("%s: [%s] is correct" % (key, value))
                elif key == 'ServerHardwareType':
                    if actual_hardware_info[key].startswith(value) is True:
                        logger.info("%s: [%s] is correct" % (key, value))
                else:
                    attributes_not_match += "%s: " % server.name
                    attributes_not_match += "%s " % key
                    attributes_not_match += "[expceted: <%s>] " % value
                    attributes_not_match += "[actual: <%s>]" % actual_hardware_info[key]
                    attributes_not_match += "\n"

    # Fail this validation if there are attributes not matched
    if attributes_not_match:
        logger.warn(attributes_not_match)
        ui_lib.fail_test(attributes_not_match)

    return True


def _get_hardware_info_from_test_data(hardware_obj):
    hardware_info = {}
    for key in dir(hardware_obj):
        if not isinstance(hardware_obj.get_property(key), test_data.DataObj):
            continue

        if not hardware_obj.get_property(key).has_property('expected_value'):
            hardware_info[key] = ''
            continue

        hardware_info[key] = hardware_obj.get_property(key).get_property('expected_value')

    return hardware_info


def _get_hardware_info_from_ilo(server_obj):
    pass


def validate_server_hardware_page_ports():
    pass


def validate_server_hardware_utilization(server_obj, compare_with_ilo=False):
    """ Validate utilization attributes on server hardware page.

    Arguments:
      server_object
        name*        --  Name of server hardware as a string.
        server*      --  hostname of the iLO of the server hardware.
        iloIP*       --  IP address/hostname of the iLO of the server hardware.
        iloUserName* --  iLO's Admin username.
        iloPassword* --  iLO's Admin password.
        mgmtType*    --  what type the server hardware will be added as, Managed/Monitored.
        Licensing*   --  Licensing type, 'HP OneView Advanced'/'HP OneView Advanced w/o iLO'/'HP OneView Standard'.
        force*       --  Force add the server hardware if it's being managed by another system
        Utilization Attributes
          CPU
          Power
          Temperature
      compare_with_ilo    --  if set to "True", compares with the values retrieved from iLO.

    * Required Arguments

    Example:
    Note: if power meter is collected, set expected_value to 'collected'
        data/RackServersForMonitoring -> @{TestData.RackServersForMonitoring}
        <RackServersForMonitoring>
            <server name="wpstdl41-ilo" server="16.125.77.18" iloIP="16.125.77.18" iloUserName="Administrator"
            iloPassword="hpvse1-ilo" mgmtType="Monitored" Licensing="HP OneView Standard">
                <Utilization>
                    <Cpu expected_value="not supported"><None/></Cpu>
                    <Power expected_value="not supported"><None/></Power>
                    <Temperature expected_value="not supported"><None/></Temperature>
                </Utilization>>
            </server>
            <server name="wpstdl16-ilo" server="wpstdl16-ilo.vse.rdlabs.hpecorp.net" iloIP="16.125.68.91"
            iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Monitored" Licensing="HP OneView Standard"/>
        </RackServersForMonitoring>

    """

    attributes_not_match = ''

    for n, server in enumerate(server_obj):
        # Stop validation if no expected value defined in node "Utilization"
        if not server.has_property('Utilization'):
            logger.warn("did not find node 'Utilization'" % server.name)
            return False

        # Get expected value from test data
        expected_utilization_info = _get_utilization_info_from_test_data(server.Utilization)

        if compare_with_ilo:
            # Get expected value through iLO cli and update the expected value
            # ToDo
            pass

        # Select the server
        CommonOperationServerHardware.click_server_hardware(server.name)

        # Compare if match.
        for key, value in expected_utilization_info.items():
            validate_function = eval('VerifyHardware.verify_hardware_utilization_' + key.lower())
            if validate_function(value):
                logger.info("%s: [%s] is correct" % (key, value))
            else:
                attributes_not_match += "%s: " % server.name
                attributes_not_match += "%s " % key
                attributes_not_match += "[%s] " % value
                attributes_not_match += "\n"

    # Fail this validation if there are attributes not matched
    if attributes_not_match:
        logger.warn(attributes_not_match)
        ui_lib.fail_test(attributes_not_match)


def _get_utilization_info_from_test_data(utilization_obj):
    utilization_info = {}
    for key in dir(utilization_obj):
        if not isinstance(utilization_obj.get_property(key), test_data.DataObj):
            continue

        if not utilization_obj.get_property(key).has_property('expected_value'):
            utilization_info[key] = ''
            continue

        utilization_info[key] = utilization_obj.get_property(key).get_property('expected_value')

    return utilization_info


def validate_server_hardware_monitored_by_own(server_obj):
    """ Validate error message when server is already monitored by own.

    Arguments:
      server_object
        name*        --  Name of server hardware as a string.
        server*      --  hostname of the iLO of the server hardware.
        iloIP*       --  IP address/hostname of the iLO of the server hardware.
        iloUserName* --  iLO's Admin username.
        iloPassword* --  iLO's Admin password.
        mgmtType*    --  what type the server hardware will be added as, Managed/Monitored.
        Licensing*   --  Licensing type, 'HP OneView Advanced'/'HP OneView Advanced w/o iLO'/'HP OneView Standard'.
        force       --  Force add the server hardware if it's being managed by another system

    * Required Arguments

    Example:
    Note: if power meter is collected, set expected_value to 'collected'
        data/RackServersForMonitoring -> @{TestData.RackServersForMonitoring}
        <RackServersForMonitoring>
            <server name="wpstdl41-ilo" server="16.125.77.18" iloIP="16.125.77.18" iloUserName="Administrator"
            iloPassword="hpvse1-ilo" mgmtType="Monitored" Licensing="HP OneView Standard">
            </server>
            <server name="wpstdl16-ilo" server="wpstdl16-ilo.vse.rdlabs.hpecorp.net" iloIP="16.125.68.91"
            iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Monitored" Licensing="HP OneView Standard"/>
        </RackServersForMonitoring>

    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)

    msg_not_match = ''

    for n, server in enumerate(server_obj):
        AddHardware.click_add_server_hardware_button()
        # Trying to add server as monitored
        AddHardware.tick_add_server_hardware_as_monitored()
        AddHardware.input_ilo_ip(server.iloIP)
        AddHardware.input_ilo_username(server.iloUserName, server.iloPassword)
        AddHardware.input_ilo_password(server.iloPassword)
        AddHardware.click_add_button()
        if not VerifyHardware.verify_server_hardware_is_monitored_by_own():
            msg_not_match += "Incorrect error message when trying to monitor %s \n" % server.name
        logger.info('Expected error message: This server is already being monitored by this appliance.')
        AddHardware.click_cancel_button()

        # Trying to add server as managed
        AddHardware.click_add_server_hardware_button()
        AddHardware.tick_add_server_hardware_as_managed()
        AddHardware.input_ilo_ip(server.iloIP)
        AddHardware.input_ilo_username(server.iloUserName, server.iloPassword)
        AddHardware.input_ilo_password(server.iloPassword)
        AddHardware.tick_licensing_as_hp_oneview_advanced()
        AddHardware.click_add_button()
        if not VerifyHardware.verify_server_hardware_is_monitored_by_own():
            msg_not_match += "Incorrect error message when trying to manage %s \n" % server.name
        logger.info('Expected error message: This server is already being monitored by this appliance.')

    if msg_not_match:
        logger.warn(msg_not_match)
        ui_lib.fail_test(msg_not_match)
        return False
    else:
        return True


def validate_server_hardware_meet_minimum_ilo4(server_obj):
    """ Validate error message when ilo4 fw is below minimum supported

    Arguments:
      server_object
        name*        --  Name of server hardware as a string.
        server*      --  hostname of the iLO of the server hardware.
        iloIP*       --  IP address/hostname of the iLO of the server hardware.
        iloUserName* --  iLO's Admin username.
        iloPassword* --  iLO's Admin password.
        mgmtType*    --  what type the server hardware will be added as, Managed/Monitored.
        Licensing*   --  Licensing type, 'HP OneView Advanced'/'HP OneView Advanced w/o iLO'/'HP OneView Standard'.
        force       --  Force add the server hardware if it's being managed by another system

    * Required Arguments

    Example:
    Note: if power meter is collected, set expected_value to 'collected'
        data/RackServersForMonitoring -> @{TestData.RackServersForMonitoring}
        <RackServersForMonitoring>
            <server name="wpstdl41-ilo" server="16.125.77.18" iloIP="16.125.77.18" iloUserName="Administrator"
            iloPassword="hpvse1-ilo" mgmtType="Monitored" Licensing="HP OneView Standard">
            </server>
            <server name="wpstdl16-ilo" server="wpstdl16-ilo.vse.rdlabs.hpecorp.net" iloIP="16.125.68.91"
            iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Monitored" Licensing="HP OneView Standard"/>
        </RackServersForMonitoring>

    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)

    msg_not_match = ''

    for n, server in enumerate(server_obj):
        AddHardware.click_add_server_hardware_button()
        # Trying to add server as monitored
        AddHardware.tick_add_server_hardware_as_monitored()
        AddHardware.input_ilo_ip(server.iloIP)
        AddHardware.input_ilo_username(server.iloUserName, server.iloPassword)
        AddHardware.input_ilo_password(server.iloPassword)
        AddHardware.click_add_button()
        if not VerifyHardware.verify_server_hardware_minimum_supported_ilo4():
            msg_not_match += "Incorrect error message when trying to monitor %s \n" % server.name
        logger.info('Expected error message: Supported firmware versions are 1.30 or higher.')
        AddHardware.click_cancel_button()

    if msg_not_match:
        logger.warn(msg_not_match)
        ui_lib.fail_test(msg_not_match)
        return False
    else:
        return True


def validate_server_hardware_managed_by_own(server_obj):
    """ Validate error message when trying to monitor server is already managed by own.

    Arguments:
      server_object
        name*        --  Name of server hardware as a string.
        server*      --  hostname of the iLO of the server hardware.
        iloIP*       --  IP address/hostname of the iLO of the server hardware.
        iloUserName* --  iLO's Admin username.
        iloPassword* --  iLO's Admin password.
        mgmtType*    --  what type the server hardware will be added as, Managed/Monitored.
        Licensing*   --  Licensing type, 'HP OneView Advanced'/'HP OneView Advanced w/o iLO'/'HP OneView Standard'.
        force       --  Force add the server hardware if it's being managed by another system

    * Required Arguments

    Example:
        data/RackServersForMonitoring -> @{TestData.RackServersForMonitoring}
        <RackServersForMonitoring>
            <server name="wpstdl41-ilo" server="16.125.77.18" iloIP="16.125.77.18" iloUserName="Administrator"
            iloPassword="hpvse1-ilo" mgmtType="Monitored" Licensing="HP OneView Standard">
            </server>
            <server name="wpstdl16-ilo" server="wpstdl16-ilo.vse.rdlabs.hpecorp.net" iloIP="16.125.68.91"
            iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Monitored" Licensing="HP OneView Standard"/>
        </RackServersForMonitoring>

    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)

    msg_not_match = ''

    for n, server in enumerate(server_obj):
        AddHardware.click_add_server_hardware_button()
        # Trying to add server as monitored
        AddHardware.tick_add_server_hardware_as_monitored()
        AddHardware.input_ilo_ip(server.iloIP)
        # AddHardware.input_ilo_username(server.iloUserName, server.iloPassword)
        # 2015-07-15 Alex Ma commented
        AddHardware.input_ilo_username(server.iloUserName)

        AddHardware.input_ilo_password(server.iloPassword)
        AddHardware.click_add_button()
        if not VerifyHardware.verify_server_hardware_monitor_already_managed():
            msg_not_match += "Incorrect error message when trying to monitor %s \n" % server.name
        logger.info('Expected error message: This server is already being managed by this appliance.')
        AddHardware.click_cancel_button()

        # Trying to add server as managed
        AddHardware.click_add_server_hardware_button()
        AddHardware.tick_add_server_hardware_as_managed()
        AddHardware.input_ilo_ip(server.iloIP)
        AddHardware.input_ilo_username(server.iloUserName, server.iloPassword)
        AddHardware.input_ilo_password(server.iloPassword)
        AddHardware.tick_licensing_as_hp_oneview_advanced()
        AddHardware.click_add_button()
        if not VerifyHardware.verify_server_hardware_manage_already_managed():
            msg_not_match += "Incorrect error message when trying to manage %s \n" % server.name
        logger.info('Expected error message: This server is already being managed by this appliance.')

    if msg_not_match:
        logger.warn(msg_not_match)
        ui_lib.fail_test(msg_not_match)
        return False
    else:
        return True


def validate_server_hardware_manage_single_blade(server_obj):
    """ Validate error message when trying to monitor server is already managed by own.

    Arguments:
      server_object
        name*        --  Name of server hardware as a string.
        server*      --  hostname of the iLO of the server hardware.
        iloIP*       --  IP address/hostname of the iLO of the server hardware.
        iloUserName* --  iLO's Admin username.
        iloPassword* --  iLO's Admin password.
        mgmtType*    --  what type the server hardware will be added as, Managed/Monitored.
        Licensing*   --  Licensing type, 'HP OneView Advanced'/'HP OneView Advanced w/o iLO'/'HP OneView Standard'.
        force       --  Force add the server hardware if it's being managed by another system

    * Required Arguments

    Example:
        data/RackServersForMonitoring -> @{TestData.RackServersForMonitoring}
        <RackServersForMonitoring>
            <server name="wpstdl41-ilo" server="16.125.77.18" iloIP="16.125.77.18" iloUserName="Administrator"
            iloPassword="hpvse1-ilo" mgmtType="Monitored" Licensing="HP OneView Standard">
            </server>
            <server name="wpstdl16-ilo" server="wpstdl16-ilo.vse.rdlabs.hpecorp.net" iloIP="16.125.68.91"
            iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Monitored" Licensing="HP OneView Standard"/>
        </RackServersForMonitoring>

    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)

    total = len(server_obj)
    error_msg_matched = 0
    error_msg_not_matched = 0

    for n, server in enumerate(server_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("adding a server named '%s'" % server.name)
        # Trying to add server as managed
        AddHardware.click_add_server_hardware_button()
        AddHardware.tick_add_server_hardware_as_managed()
        AddHardware.input_ilo_ip(server.iloIP)
        # AddHardware.input_ilo_username(server.iloUserName, server.iloPassword)
        # 2015-07-15 Alex Ma commented
        AddHardware.input_ilo_username(server.iloUserName)
        AddHardware.input_ilo_password(server.iloPassword)
        AddHardware.tick_licensing_as_hp_oneview_advanced()
        AddHardware.click_add_button()
        if VerifyHardware.verify_server_hardware_manage_single_blade(ilo_ip=server.iloIP, timeout=10, fail_if_false=False) is True:
            logger.info("correct error message found with server '%s'" % server.name)
            error_msg_matched += 1
        else:
            logger.warn("incorrect error message found with server '%s'" % server.name)
            error_msg_not_matched += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if error_msg_matched == 0:
        logger.warn("all %s server(s)' adding action did NOT show the expected error message! keyword '%s' returns a 'False'" % (total, sys._getframe().f_code.co_name))
        return False
    else:
        if total != error_msg_matched:
            logger.warn("not all of %s server(s)' adding action showed the expected error message - %s matched, %s not matched" % (total, error_msg_matched, error_msg_not_matched))
            return False

    logger.info("all %s server(s)' adding action showed the expected error message" % error_msg_matched)
    return True


def validate_server_power(server_obj):
    """ Validate power action (on or off) and UI elements according to server's power state.

    Arguments:
      server_object
        name*        --  Name of server hardware as a string.
        server*      --  hostname of the iLO of the server hardware.
        iloIP*       --  IP address/hostname of the iLO of the server hardware.
        iloUserName* --  iLO's Admin username.
        iloPassword* --  iLO's Admin password.
        mgmtType*    --  what type the server hardware will be added as, Managed/Monitored.
        Licensing*   --  Licensing type, 'HP OneView Advanced'/'HP OneView Advanced w/o iLO'/'HP OneView Standard'.
        force       --  Force add the server hardware if it's being managed by another system

    * Required Arguments

    Example:
        data/RackServersForMonitoring -> @{TestData.RackServersForMonitoring}
        <RackServersForMonitoring>
            <server name="wpstdl41-ilo" server="16.125.77.18" iloIP="16.125.77.18" iloUserName="Administrator"
            iloPassword="hpvse1-ilo" mgmtType="Monitored" Licensing="HP OneView Standard">
            </server>
            <server name="wpstdl16-ilo" server="wpstdl16-ilo.vse.rdlabs.hpecorp.net" iloIP="16.125.68.91"
            iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Monitored" Licensing="HP OneView Standard"/>
        </RackServersForMonitoring>

    """
    logger.info("--> ======= ----- start validating server power on servers %s ----- ======" % [server.name for server in server_obj])
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)

    total = len(server_obj)
    not_exists_or_initial_power_on_failed = 0
    validated_pass = 0
    result = {}
    for n, server in enumerate(server_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("validating a server named '%s'" % server.name)
        result[server.name] = {}
        if VerifyHardware.verify_server_hardware_exist(server.name, fail_if_false=False) is False:
            logger.warn("server hardware '%s' does not exist" % server.name)
            not_exists_or_initial_power_on_failed += 1
            result[server.name] = 'not exists'
            continue

        CommonOperationServerHardware.click_server_hardware(server_name=server.name, timeout=5, time_for_loading=5)
        FusionUIBase.select_view_by_name(view_name='Hardware', timeout=5, fail_if_false=False)
        if CommonOperationServerHardware.get_server_hardware_power_state(server_name=server.name, timeout=5, fail_if_false=False) != 'On':
            if power_on_server_by_name(server_name=server.name) is False:
                logger.warn("server hardware '%s' is FAILED to initially set its power on" % server.name)
                not_exists_or_initial_power_on_failed += 1
                result[server.name] = 'failed to initially set its power on'
                continue

        # data_obj = test_data.DataObj()
        # data_obj.add_property('name', server.name)
        # data_obj.add_property('iloIP', server.iloIP)
        # data_obj.add_property('iloUserName', server.iloUserName)
        # data_obj.add_property('iloPassword', server.iloPassword)

        result[server.name]['power_state_between_fusion_and_ilo'] = False \
            if validate_power_state_between_fusion_and_ilo(server) is False else True

        result[server.name]['power_state_change_after_power_off_from_ilo'] = False \
            if validate_power_state_change_after_power_off_from_ilo(server) is False else True

        result[server.name]['power_action_availability_when_power_off'] = False \
            if validate_power_action_availability(server_name=server.name) is False else True

        result[server.name]['power_state_change_after_power_on_from_fusion'] = False \
            if validate_power_state_change_after_power_on_from_fusion(server) is False else True

        result[server.name]['power_action_availability_when_power_on'] = False \
            if validate_power_action_availability(server_name=server.name) is False else True

        result[server.name]['power_action_not_allowed_during_profile_being_deleted'] = False \
            if validate_power_action_not_allowed_during_profile_being_deleted_by_another_user(server_name=server.name, second_username=server.SecondUsername) is False else True

        result[server.name]['power_action_not_available_for_network_administrator_privilege'] = False \
            if validate_power_action_not_available_for_network_administrator_privilege(server_name=server.name, network_admin_username=server.NetworkAdminUsername) is False else True

        if all(result[server.name].values()) is True:
            validated_pass += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if validated_pass == 0:
        logger.warn("all %s server(s)' failed the power on/off action or power state validation! keyword '%s' returns a 'False'" % (total, sys._getframe().f_code.co_name))
        return False
    else:
        if total != validated_pass:
            logger.warn("not all of %s server(s)' passed the power on/off action or power state validation - %s passed, %s failed, keyword '%s' returns a 'False'" % (total, validated_pass, total - validated_pass, sys._getframe().f_code.co_name))
            return False

    logger.info("all %s server(s) passed the power on/off action and power state validation!" % validated_pass)
    return True


def validate_power_state_between_fusion_and_ilo(server_obj):
    server_name = getattr(server_obj, 'name', 'None')
    ilo_hostname = getattr(server_obj, 'iloIP', 'None')
    ilo_login = getattr(server_obj, 'iloUserName', 'None')
    ilo_password = getattr(server_obj, 'iloPassword', 'None')
    logger.info("--> ======= start validating power state of server '%s' should be consistent between iLO and HP OneView  ======" % server_name)
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    if VerifyHardware.verify_server_hardware_exist(server_name=server_name, fail_if_false=False) is False:
        logger.warn("server hardware '%s' does not exist" % server_name)
        return False

    CommonOperationServerHardware.click_server_hardware(server_name=server_name, timeout=5, time_for_loading=5)
    FusionUIBase.select_view_by_name(view_name='Hardware', timeout=5, fail_if_false=False)
    state_fusion = CommonOperationServerHardware.get_server_hardware_power_state(server_name=server_name, timeout=5).upper()
    ilo_client = IloClient(hostname=ilo_hostname, login=ilo_login, password=ilo_password)
    # ilo_client.press_pwr_btn()
    # ilo_client.set_host_power(True)
    state_ilo = ilo_client.get_host_power_status().upper()
    # state_ilo = None

    if state_fusion == state_ilo:
        logger.info("power state of server '%s' is '%s' in Fusion, same as the state in iLO '%s'" % (server_name, state_fusion, state_ilo))
        return True
    else:
        logger.warn("power state of server '%s' is '%s' in Fusion,  NOT same as the state in iLO '%s'" % (server_name, state_fusion, state_ilo))
        return False


def validate_power_state_change_after_power_off_from_ilo(server_obj):

    server_name = getattr(server_obj, 'name', 'None')
    ilo_hostname = getattr(server_obj, 'iloIP', 'None')
    ilo_login = getattr(server_obj, 'iloUserName', 'None')
    ilo_password = getattr(server_obj, 'iloPassword', 'None')

    logger.info("--> ======= start validating power state change of server '%s' after powering off from iLO  ======" % server_name)
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    if VerifyHardware.verify_server_hardware_exist(server_name=server_name, fail_if_false=False) is False:
        logger.warn("server hardware '%s' does not exist" % server_name)
        return False

    CommonOperationServerHardware.click_server_hardware(server_name=server_name, timeout=5, time_for_loading=8)
    FusionUIBase.select_view_by_name(view_name='Hardware', timeout=5, fail_if_false=False)
    state_fusion = CommonOperationServerHardware.get_server_hardware_power_state(server_name=server_name, timeout=8).upper()
    ilo_client = IloClient(hostname=ilo_hostname, login=ilo_login, password=ilo_password)

    if state_fusion != 'ON':
        logger.warn("server hardware '%s' power state is not 'On', now trying to power it on via iLO CLI ..." % server_name)
        ilo_client.set_host_power(True)
        CommonOperationServerHardware.wait_for_server_power_change_to(power_state='On', timeout=30, fail_if_false=False)
        logger.debug("get power state of server '%s' via iLO CLI ..." % server_name)
        state_ilo = ilo_client.get_host_power_status().upper()
        logger.debug("get power state of server '%s' via from Fusion UI ..." % server_name)
        state_fusion = CommonOperationServerHardware.get_server_hardware_power_state(server_name=server_name, timeout=5).upper()
        if state_ilo != 'ON':
            logger.warn("'ilo_client.get_host_power_status().upper()' returns '%s', failed to power on server '%s' via iLO CLI, keyword/function '%s' returns FALSE" % (state_ilo, server_name, sys._getframe().f_code.co_name))
            return False
        if state_fusion != 'ON':
            logger.warn("'CommonOperationServerHardware.get_server_hardware_power_state' returns '%s', failed to power on server '%s' via iLO CLI, keyword/function '%s' returns FALSE" % (state_fusion, server_name, sys._getframe().f_code.co_name))
            return False

    logger.debug("set power state of server '%s' to 'OFF' via iLO CLI ..." % server_name)
    ilo_client.set_host_power(False)
    CommonOperationServerHardware.wait_for_server_power_change_to(power_state='Off', timeout=90, fail_if_false=False)
    logger.debug("get power state of server '%s' via iLO CLI after being powered off ..." % server_name)
    state_ilo = ilo_client.get_host_power_status().upper()
    logger.debug("get power state of server '%s' via from Fusion UI after being powered off ..." % server_name)
    state_fusion = CommonOperationServerHardware.get_server_hardware_power_state(server_name=server_name, timeout=5).upper()

    if state_ilo != 'OFF':
        logger.warn("'ilo_client.get_host_power_status().upper()' returns '%s', "
                    "might be failed to power off server '%s' via iLO CLI, keyword/function '%s' returns FALSE" % (state_ilo, server_name, sys._getframe().f_code.co_name))
        return False
    if state_fusion != 'OFF':
        logger.warn("'CommonOperationServerHardware.get_server_hardware_power_state' returns '%s', "
                    "Fusion failed to change power state of server '%s' automatically, keyword/function '%s' returns FALSE" % (state_fusion, server_name, sys._getframe().f_code.co_name))
        return False

    logger.info("---> power state change of server '%s' after powering off from iLO is verified as expected, iLO power state is '%s', Fusion power state is '%s' " % (server_name, state_ilo, state_fusion))
    return True


def validate_power_action_availability(server_name):
    logger.info("--> ======= start validating power actions' availability of server '%s'  ======" % server_name)
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    if VerifyHardware.verify_server_hardware_exist(server_name=server_name, fail_if_false=False) is False:
        logger.warn("server hardware '%s' does not exist" % server_name)
        return False

    CommonOperationServerHardware.click_server_hardware(server_name=server_name, timeout=5, time_for_loading=5)
    FusionUIBase.select_view_by_name(view_name='Hardware', timeout=5, fail_if_false=False)
    state_fusion = CommonOperationServerHardware.get_server_hardware_power_state(server_name=server_name, timeout=5).upper()
    # ilo_client = IloClient(hostname=ilo_hostname, login=ilo_login, password=ilo_password)

    if state_fusion == 'OFF':
        logger.debug("server hardware '%s' power state is 'Off', "
                     "now checking 'Power on' should be available and 'Power off/Reset' should be unavailable ..." % server_name)

        CommonOperationServerHardware.click_action_button(timeout=5)
        if VerifyHardware.is_power_on_button_available(timeout=5, fail_if_false=False) is False:
            logger.warn("'Power on' button is not verified as AVAILABLE for server '%s' when its power state is 'Off', keyword/function '%s' returns FALSE" % (server_name, sys._getframe().f_code.co_name))
            return False
        logger.info("'Power on' button is verified as AVAILABLE for server '%s' when its power state is 'Off', " % server_name)

        if VerifyHardware.is_power_off_button_not_available(timeout=5, fail_if_false=False) is False:
            logger.warn("'Power off' button is not verified as UNAVAILABLE for server '%s' when its power state is 'Off', keyword/function '%s' returns FALSE" % (server_name, sys._getframe().f_code.co_name))
            return False
        logger.info("'Power off' button is verified as UNAVAILABLE for server '%s' when its power state is 'Off', " % server_name)

        if VerifyHardware.is_reset_button_not_available(timeout=5, fail_if_false=False) is False:
            logger.warn("'Reset' button is not verified as UNAVAILABLE for server '%s' when its power state is 'Off', keyword/function '%s' returns FALSE" % (server_name, sys._getframe().f_code.co_name))
            return False
        logger.info("'Reset' button is verified as UNAVAILABLE for server '%s' when its power state is 'Off', " % server_name)

        logger.info("'Power on' is AVAILABLE and 'Power off/Reset' is UNAVAILABLE for server '%s' when its power state is 'Off', keyword/function '%s' returns TRUE" % (server_name, sys._getframe().f_code.co_name))
        return True

    elif state_fusion == 'ON':
        logger.debug("server hardware '%s' power state is 'On', "
                     "now checking 'Power off/Reset' should be available and 'Power on' should be unavailable ..." % server_name)

        CommonOperationServerHardware.click_action_button(timeout=5)
        if VerifyHardware.is_power_off_button_available(timeout=5, fail_if_false=False) is False:
            logger.warn("'Power off' button is not verified as AVAILABLE for server '%s' when its power state is 'On', keyword/function '%s' returns FALSE" % (server_name, sys._getframe().f_code.co_name))
            return False
        logger.info("'Power off' button is verified as AVAILABLE for server '%s' when its power state is 'On', " % server_name)

        if VerifyHardware.is_reset_button_available(timeout=5, fail_if_false=False) is False:
            logger.warn("'Reset' button is not verified as AVAILABLE for server '%s' when its power state is 'On', keyword/function '%s' returns FALSE" % (server_name, sys._getframe().f_code.co_name))
            return False
        logger.info("'Reset' button is verified as AVAILABLE for server '%s' when its power state is 'On', " % server_name)

        if VerifyHardware.is_power_on_button_not_available(timeout=5, fail_if_false=False) is False:
            logger.warn("'Power on' button is not verified as UNAVAILABLE for server '%s' when its power state is 'On', keyword/function '%s' returns FALSE" % (server_name, sys._getframe().f_code.co_name))
            return False
        logger.info("'Power on' button is verified as UNAVAILABLE for server '%s' when its power state is 'On', " % server_name)

        logger.info("'Power off/Reset' is AVAILABLE and 'Power on' is UNAVAILABLE for server '%s' when its power state is 'On', keyword/function '%s' returns TRUE" % (server_name, sys._getframe().f_code.co_name))
        return True

    else:
        logger.debug("server hardware '%s' power state is not either 'On' or 'Off', may be 'Unknown', 'N/A', or 'Not supported', "
                     "keyword/function '%s' returns FALSE" % (server_name, sys._getframe().f_code.co_name))
        return False


def validate_server_hardware_monitored(*server_obj):
    """ Validate state when server is already monitored by own.

    Arguments:
      server_object
        name*        --  Name of server hardware as a string.

    * Required Arguments

    Example:
    Note: if power meter is collected, set expected_value to 'collected'
        data/RackServersForMonitoring -> @{TestData.RackServersForMonitoring}
        <RackServersForMonitoring>
            <server name="wpstdl41-ilo"/>
        </RackServersForMonitoring>

    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)

    if isinstance(server_obj, test_data.DataObj):
        server_obj = [server_obj]
    elif isinstance(server_obj, tuple):
        server_obj = list(server_obj[0])

    count = 0
    server_len = len(server_obj)

    for n, server in enumerate(server_obj):
        rc = select_server(server.name)
        if not rc:
            logger.warn("Failed to select Server Hardware '%s'" % server.name)
            continue
        BuiltIn().sleep(3)
        VerifyHardware.verify_hardware_state("Monitored")
        count += 1

    if count == 0:
        logger.warn("no server state verified!")
        return False

    if count != server_len:
        logger.warn("error encounter when verify server state")
        return False

    return True


def validate_server_hardware_managed(*server_obj):
    """ Validate status when server is already managed
    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    if isinstance(server_obj, test_data.DataObj):
        server_obj = [server_obj]
    elif isinstance(server_obj, tuple):
        server_obj = list(server_obj[0])

    count = 0
    server_len = len(server_obj)

    for n, server in enumerate(server_obj):
        rc = select_server(server.name)
        if not rc:
            logger.warn("Failed to select Server Hardware '%s'" % server.name)
            continue
        ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_ELEMENT_SERVER_STATE)
        if VerifyHardware.verify_hardware_state_for_exclusion("Monitored") and VerifyHardware.verify_hardware_state_for_exclusion("Unmanaged"):
            count += 1

    if count == 0:
        logger.warn("no server state verified!")
        return False

    if count != server_len:
        logger.warn("error encounter when verify server state")
        return False

    return True


def validate_power_state_change_after_power_on_from_fusion(server_obj):
    server_name = getattr(server_obj, 'name', 'None')
    ilo_hostname = getattr(server_obj, 'iloIP', 'None')
    ilo_login = getattr(server_obj, 'iloUserName', 'None')
    ilo_password = getattr(server_obj, 'iloPassword', 'None')
    logger.info("--> ======= start validating power state change of server '%s' after powering on from HP OneView  ======" % server_name)
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    if VerifyHardware.verify_server_hardware_exist(server_name=server_name, fail_if_false=False) is False:
        logger.warn("server hardware '%s' does not exist" % server_name)
        return False

    CommonOperationServerHardware.click_server_hardware(server_name=server_name, timeout=5, time_for_loading=5)
    state_fusion = CommonOperationServerHardware.get_server_hardware_power_state(server_name=server_name, timeout=5).upper()
    ilo_client = IloClient(hostname=ilo_hostname, login=ilo_login, password=ilo_password)

    if state_fusion != 'OFF':
        logger.warn("<pre-condition: power-off> server hardware '%s' power state is not 'Off', now trying to power it off via iLO CLI ..." % server_name)
        ilo_client.set_host_power(False)
        CommonOperationServerHardware.wait_for_server_power_change_to(power_state='Off', timeout=30, fail_if_false=False)
        logger.debug("<pre-condition: power-off> get power state of server '%s' via iLO CLI ..." % server_name)
        state_ilo = ilo_client.get_host_power_status().upper()
        logger.debug("<pre-condition: power-off> get power state of server '%s' via from Fusion UI ..." % server_name)
        state_fusion = CommonOperationServerHardware.get_server_hardware_power_state(server_name=server_name, timeout=5).upper()
        if state_ilo != 'OFF':
            logger.warn("<pre-condition: power-off> 'ilo_client.get_host_power_status().upper()' returns '%s', failed to power off server '%s' via iLO CLI, keyword/function '%s' returns FALSE" % (state_ilo, server_name, sys._getframe().f_code.co_name))
            return False
        if state_fusion != 'OFF':
            logger.warn("<pre-condition: power-off> 'CommonOperationServerHardware.get_server_hardware_power_state' returns '%s', failed to power off server '%s' via iLO CLI, keyword/function '%s' returns FALSE" % (state_fusion, server_name, sys._getframe().f_code.co_name))
            return False

    logger.debug("power on server '%s' from HP OneView ..." % server_name)
    power_on_server_by_name(server_name=server_name)

    CommonOperationServerHardware.wait_for_server_power_change_to(power_state='On', timeout=30, fail_if_false=False)
    logger.debug("get power state of server '%s' via iLO CLI after being powered on ..." % server_name)
    state_ilo = ilo_client.get_host_power_status().upper()
    logger.debug("get power state of server '%s' via from Fusion UI after being powered on ..." % server_name)
    state_fusion = CommonOperationServerHardware.get_server_hardware_power_state(server_name=server_name, timeout=5).upper()

    if state_ilo != 'ON':
        logger.warn("'ilo_client.get_host_power_status().upper()' returns '%s', "
                    "might be failed to power on server '%s' via iLO CLI, keyword/function '%s' returns FALSE" % (state_ilo, server_name, sys._getframe().f_code.co_name))
        return False
    if state_fusion != 'ON':
        logger.warn("'CommonOperationServerHardware.get_server_hardware_power_state' returns '%s', "
                    "Fusion failed to change power state of server '%s' automatically, keyword/function '%s' returns FALSE" % (state_fusion, server_name, sys._getframe().f_code.co_name))
        return False

    logger.info("---> power state change of server '%s' after powering on from Fusion is verified as expected, iLO power state is '%s', Fusion power state is '%s', keyword/function '%s' returns TRUE" % (server_name, state_ilo, state_fusion, sys._getframe().f_code.co_name))
    return True


def validate_power_action_not_allowed_during_profile_being_deleted_by_another_user(server_name, second_username):
    condition = threading.Condition()
    logger.info("--> ======= start validating power action on server '%s' is not allowed during server profile being deleted by another user  ======" % server_name)
    profile_name = 'SP_%s' % server_name
    from FusionLibrary.ui.servers import serverprofiles
    logger.info("start creating a simple profile for server '%s' ..." % server_name)
    if serverprofiles.create_simple_server_profile_by_server_hardware(profile_name=profile_name, server_name=server_name) is False:
        logger.warn("failed to create a simple server profile '%s' for validating power action when server profile is being deleted, '%s' returns FALSE" % (profile_name, sys._getframe().f_code.co_name))
        return False

    global expected_error_captured
    global sub_thread_exit

    expected_error_captured = False
    sub_thread_exit = False

    def press_power_action_button():
        global expected_error_captured
        global sub_thread_exit

        if condition.acquire():
            logger.info("-------- start waiting for clicking power action button 'Momentary press/Press and hold' (thread 't_press_power_action_button') ...")
            FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
            CommonOperationServerHardware.click_server_hardware(server_name=server_name, timeout=5, time_for_loading=5)
            FusionUIBase.select_view_by_name(view_name='Hardware', timeout=5, fail_if_false=False)
            current_state = CommonOperationServerHardware.get_server_hardware_power_state(server_name=server_name, timeout=5, fail_if_false=False).upper()
            action = ['ON', 'OFF'][current_state == 'ON']
            logger.info("-------- power action is '%s' --------" % action)
            if action == 'ON':
                logger.info("-------- click 'Actions' menu to stand by for clicking Power on button --------")
                CommonOperationServerHardware.click_action_button()
            elif action == 'OFF':
                logger.info("-------- server '%s' power state is '%s', not 'OFF' to power it on when deleting its server profile, "
                            "only powering ON a server during deleting its profile can capture the error message, "
                            "function '%s' sets 'expected_error_captured' as FALSE and releases thread" % (server_name, current_state, sys._getframe().f_code.co_name))
                sub_thread_exit = True
                condition.release()
                return
                # 2015-08-05 Alex Ma commented below part to skip POWER OFF action due to not applicable to capture the error message
                # PowerOffHardware.select_action_power_off()

            condition.notifyAll()
            condition.wait()

            logger.info("-------- sub thread '%s' is notified to wake up --------" % sys._getframe().f_code.co_name)
            s2l = ui_lib.get_s2l()
            s2l.switch_browser(index_or_alias='1')
            logger.info("-------- current_browser_url is '%s'" % s2l._current_browser().get_current_url())
            if action == 'OFF':
                # {     2015-08-05 Alex Ma commented below part
                #                   since it's hard to capture any error message when powering OFF a server during its profile is being deleted,
                #                   so only support capturing error message when powering ON a server in the same scenario.
                #                   but keep this code here for future possible use if it becomes supportable.
                # logger.info("try 'PowerOffHardware.click_press_and_hold_button()' to capture error message ...")
                # PowerOffHardware.click_press_and_hold_button()
                # if VerifyHardware.is_power_off_error_visible_during_deleting_profile(timeout=5, fail_if_false=False) is False:
                #     logger.info("-------- failed to capture the expected error message for powering off server '%s' during deleting its profile, "
                #                 "function '%s' returns FALSE ..." % (server_name, sys._getframe().f_code.co_name))
                #     sub_thread_exit = True
                # else:
                #     logger.info("-------- successfully captured the expected error message for powering off server '%s' during deleting its profile, "
                #                 "function '%s' returns TRUE ..." % (server_name, sys._getframe().f_code.co_name))
                #     expected_error_captured = True
                # }
                logger.info("-------- only powering ON a server during deleting its profile can capture the error message! function '%s' returns FALSE" % sys._getframe().f_code.co_name)
                sub_thread_exit = True
            elif action == 'ON':
                logger.info("-------- try 'PowerOnHardware.click_power_on_button()' to capture error message ...")
                PowerOnHardware.click_power_on_button()
                if VerifyHardware.is_power_on_error_visible_during_deleting_profile(timeout=5, fail_if_false=False) is False:
                    logger.info("-------- failed to capture the expected error message for powering on server '%s' during deleting its profile, function '%s' returns FALSE ..." % (server_name, sys._getframe().f_code.co_name))
                    sub_thread_exit = True
                else:
                    logger.info("-------- successfully captured the expected error message for powering on server '%s' during deleting its profile, function '%s' returns TRUE ..." % (server_name, sys._getframe().f_code.co_name))
                    expected_error_captured = True

            condition.release()

    def delete_profile():
        if condition.acquire():
            if sub_thread_exit is True:
                logger.info("-------- thread 't_delete_profile' is exiting due to 'sub_thread_exit' is TRUE ...")
                condition.release()
                return

            logger.info("-------- start deleting server profile (thread 't_delete_profile') ...")
            s2l = ui_lib.get_s2l()
            import re
            appliance_url = re.findall(r'^https://[\d.]*', s2l._current_browser().get_current_url())[0]
            # s2l = ui_lib.get_s2l()
            logger.info("-------- Appliance URL retrieved by s2l._current_browser().get_current_url() is '%s' --------" % appliance_url)
            s2l.open_browser(appliance_url, 'firefox', alias='DeleteSP')

            s2l.maximize_browser_window()

            login(s2l, second_username)

            from FusionLibrary.ui.business_logic.servers.serverprofiles import CommonOperationServerProfile
            from FusionLibrary.ui.business_logic.servers.serverprofiles import DeleteServerProfile

            FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
            CommonOperationServerProfile.click_server_profile(profile_name=profile_name, timeout=5, time_for_loading=4, fail_if_false=False)
            condition.notifyAll()
            DeleteServerProfile.select_action_delete()
            DeleteServerProfile.tick_force_delete_checkbox()
            DeleteServerProfile.click_yes_delete_button()
            s2l.close_browser()
            condition.release()

    def login(selenium2library, username):
        # logger.info('Login status = {0}'.format(str(ui_lib.logged_in())))
        logger.info('Login status = {0}'.format(str(FusionUIBase.logged_in())))
        user = test_data.get_user_by_name(username)

        selenium2library.wait_until_page_contains_element(FusionLoginPage.ID_BTN_LOGIN_BUTTON)
        selenium2library.input_text(FusionLoginPage.ID_INPUT_LOGIN_USER, user.name)
        selenium2library.input_text(FusionLoginPage.ID_INPUT_LOGIN_PASSWORD, user.password)
        selenium2library.click_button(FusionLoginPage.ID_BTN_LOGIN_BUTTON)
        # These elements may not exist if the login page is transitioning to the dashboard
        # page.  In order to avoid failing conditions, we will catch any exceptions
        try:
            selenium2library.element_should_not_be_visible(FusionLoginPage.ID_ALL_ERROR_FIELDS)
            selenium2library.element_text_should_be(FusionLoginPage.ID_LABEL_LOGIN_STATUS, "")
        except:
            pass
        selenium2library.wait_until_page_contains_element(FusionDashboardPage.ID_PAGE_LABEL,
                                                          PerfConstants.FUSION_LOGIN_TIME,
                                                          "Failed to load the Login Page")
        # ui_lib.set_login_status(True)
        FusionUIBase.set_login_status(True)

    logger.info("start 2-user-operating-in-parallel for profile and power on server '%s' ..." % server_name)
    logger.info("prepare for clicking 'Momentary press/Press and hold' button to power off, or 'Power on' directly to power on instead ...")

    t_press_power_action_button = threading.Thread(target=press_power_action_button, name='t_press_power_action_button', args=())
    t_press_power_action_button.start()
    BuiltIn().sleep(3)

    t_delete_profile = threading.Thread(target=delete_profile, name='t_delete_profile', args=())
    t_delete_profile.setDaemon(True)
    # use .setDaemon(True) before .start(), then this sub thread will be terminated
    # when the main thread (calling thread/parent thread) ends
    t_delete_profile.start()

    timeout = 180
    i = 0
    while i < timeout:
        if expected_error_captured is False:
            if t_press_power_action_button.isAlive() is True:
                BuiltIn().sleep(1)
                logger.info("-------- main thread is waiting for sub threads (t_press_power_action_button/t_delete_profile) returning result ...  %s (timeout = 180) --------" % i)
                i += 1
            else:
                logger.warn("-------- sub thread 't_press_power_action_button' is NOT alive - released due to not-applicable scenario, or exception encountered, "
                            "keyword/function '%s' returns FALSE" % sys._getframe().f_code.co_name)
                return False
        else:
            logger.info("-------- expected error message captured successfully!")
            PowerOnHardware.click_close_button_of_error_dialog()
            return expected_error_captured

    logger.warn("-------- failed to see the expected error message with in %s seconds for powering on server '%s' during its profile is being deleted" % (timeout, server_name))
    return False


def validate_power_action_not_available_for_network_administrator_privilege(server_name, network_admin_username):
    logger.info("--> ======= start validating power action on server '%s' is not allowed for network administrator privilege user '%s'  ======" % (server_name, network_admin_username))
    condition = threading.Condition()

    global check_na_user_passed

    check_na_user_passed = False

    def check_network_admin_user():
        global check_na_user_passed
        if condition.acquire():
            logger.info("-------- start checking if power actions are UNAVAILABLE for user '%s' on server '%s' (thread 't_check_network_admin_user') ..." % (network_admin_username, server_name))
            s2l = ui_lib.get_s2l()
            import re
            appliance_url = re.findall(r'^https://[\d.]*', s2l._current_browser().get_current_url())[0]
            # s2l = ui_lib.get_s2l()
            logger.info("-------- Appliance URL retrieved by s2l._current_browser().get_current_url() is '%s' --------" % appliance_url)
            s2l.open_browser(appliance_url, 'firefox', alias='DeleteSP')

            s2l.maximize_browser_window()

            login(s2l, network_admin_username)

            FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
            CommonOperationServerHardware.click_server_hardware(server_name=server_name, timeout=5, time_for_loading=4)
            CommonOperationServerHardware.click_action_button()
            if VerifyHardware.is_power_on_button_not_available() is True:
                logger.info("-------- 'Power on' button is successfully verified as UNAVAILABLE for user '%s' on server '%s'" % (network_admin_username, server_name))
                if VerifyHardware.is_power_off_button_not_available() is True:
                    logger.info("-------- 'Power off' button is successfully verified as UNAVAILABLE for user '%s' on server '%s'" % (network_admin_username, server_name))
                    if VerifyHardware.is_reset_button_not_available() is True:
                        logger.info("-------- 'Reset' button is successfully verified as UNAVAILABLE for user '%s' on server '%s', "
                                    "all 'Power on/Power off/Reset' buttons are verified as UNAVAILABLE, function '%s' returns TRUE" % (network_admin_username, server_name, sys._getframe().f_code.co_name))
                        check_na_user_passed = True
                    else:
                        logger.info("-------- 'Reset' button is NOT successfully verified as UNAVAILABLE for user '%s' on server '%s', function '%s' returns FALSE" % (network_admin_username, server_name, sys._getframe().f_code.co_name))
                else:
                    logger.info("-------- 'Power off' button is NOT successfully verified as UNAVAILABLE for user '%s' on server '%s', function '%s' returns FALSE" % (network_admin_username, server_name, sys._getframe().f_code.co_name))
            else:
                logger.info("-------- 'Power on' button is not successfully verified as UNAVAILABLE for user '%s' on server '%s', function '%s' returns FALSE" % (network_admin_username, server_name, sys._getframe().f_code.co_name))

            s2l.close_browser()
            s2l.switch_browser(index_or_alias='1')
            condition.release()

    def login(selenium2library, username):
        # logger.info('Login status = {0}'.format(str(ui_lib.logged_in())))
        logger.info('Login status = {0}'.format(str(FusionUIBase.logged_in())))

        user = test_data.get_user_by_name(username)

        selenium2library.wait_until_page_contains_element(FusionLoginPage.ID_BTN_LOGIN_BUTTON)
        selenium2library.input_text(FusionLoginPage.ID_INPUT_LOGIN_USER, user.name)
        selenium2library.input_text(FusionLoginPage.ID_INPUT_LOGIN_PASSWORD, user.password)
        selenium2library.click_button(FusionLoginPage.ID_BTN_LOGIN_BUTTON)
        # These elements may not exist if the login page is transitioning to the dashboard
        # page.  In order to avoid failing conditions, we will catch any exceptions
        try:
            selenium2library.element_should_not_be_visible(FusionLoginPage.ID_ALL_ERROR_FIELDS)
            selenium2library.element_text_should_be(FusionLoginPage.ID_LABEL_LOGIN_STATUS, "")
        except:
            pass
        selenium2library.wait_until_page_contains_element(FusionDashboardPage.ID_PAGE_LABEL,
                                                          PerfConstants.FUSION_LOGIN_TIME,
                                                          "Failed to load the Login Page")
        # ui_lib.set_login_status(True)
        FusionUIBase.set_login_status(True)

    logger.info("-------- start logging in as network admin user '%s' to check power action availability on server '%s' ..." % (network_admin_username, server_name))

    t_check_network_admin_user = threading.Thread(target=check_network_admin_user, name='t_check_network_admin_user', args=())
    t_check_network_admin_user.start()
    # user .join() to make the main thread (calling thread/parent thread) wait for this sub thread to finish before continue
    t_check_network_admin_user.join()

    if check_na_user_passed is False:
        logger.warn("-------- unavailability of power actions for network admin user '%s' is NOT successfully verified on server '%s', keyword/function '%s' returns FALSE" % (network_admin_username, server_name, sys._getframe().f_code.co_name))
    else:
        logger.info("-------- unavailability of power actions for network admin user '%s' is successfully verified on server '%s'! keyword/function '%s' returns TRUE" % (network_admin_username, server_name, sys._getframe().f_code.co_name))

    return check_na_user_passed


def validate_monitored_server_no_profile(server_obj):
    """ Validate that, if a DL server is added as 'Monitored', then there is no "Create server profile" function for it.

    Arguments:
      server_object
        name*        --  Name of server hardware as a string.
        server*      --  hostname of the iLO of the server hardware.
        iloIP*       --  IP address/hostname of the iLO of the server hardware.
        iloUserName* --  iLO's Admin username.
        iloPassword* --  iLO's Admin password.
        mgmtType*    --  what type the server hardware will be added as, Managed/Monitored.
        Licensing*   --  Licensing type, 'HP OneView Advanced'/'HP OneView Advanced w/o iLO'/'HP OneView Standard'.
        force       --  Force add the server hardware if it's being managed by another system

    * Required Arguments

    Example:
        data/RackServersForMonitoring -> @{TestData.RackServersForMonitoring}
        <RackServersForMonitoring>
            <server name="wpstdl41-ilo" server="16.125.77.18" iloIP="16.125.77.18" iloUserName="Administrator"
            iloPassword="hpvse1-ilo" mgmtType="Monitored" Licensing="HP OneView Standard">
            </server>
            <server name="wpstdl16-ilo" server="wpstdl16-ilo.vse.rdlabs.hpecorp.net" iloIP="16.125.68.91"
            iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Monitored" Licensing="HP OneView Standard"/>
        </RackServersForMonitoring>

    """
    logger.info("--> ======= ----- start validating 'Monitored server cannot be selected when creating/editing server profile' on servers %s ----- ======" % [server.name for server in server_obj])
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)

    total = len(server_obj)
    not_exists_or_initial_power_on_failed = 0
    validated_pass = 0
    result = {}
    for n, server in enumerate(server_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("validating a server named '%s'" % server.name)
        result[server.name] = {}
        if VerifyHardware.verify_server_hardware_exist(server.name, fail_if_false=False) is False:
            logger.warn("server hardware '%s' does not exist" % server.name)
            not_exists_or_initial_power_on_failed += 1
            result[server.name] = 'not exists'
            continue

        result[server.name]['server_profile_is_na'] = False \
            if validate_hardware_server_profile_is_na(server.name) is False else True

        result[server.name]['cannot_select_monitored_dl_when_creating_profile'] = False \
            if validate_cannot_select_monitored_dl_when_creating_profile(server.name) is False else True

        result[server.name]['cannot_select_monitored_dl_when_editing_profile'] = False \
            if validate_cannot_select_monitored_dl_when_editing_profile(server_name=server.name, reference_server_name=server.ReferenceServer) is False else True

        if all(result[server.name].values()) is True:
            validated_pass += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if validated_pass == 0:
        logger.warn("all %s server(s)' failed the validation of 'Monitored server cannot be selected when creating/editing server profile'! keyword '%s' returns a 'False'" % (total, sys._getframe().f_code.co_name))
        return False
    else:
        if total != validated_pass:
            logger.warn("not all of %s server(s)' passed the validation 'Monitored server cannot be selected when creating/editing server profile' - %s passed, %s failed, keyword '%s' returns a 'False'" % (total, validated_pass, total - validated_pass, sys._getframe().f_code.co_name))
            return False

    logger.info("all %s server(s) passed the validation 'Monitored server cannot be selected when creating/editing server profile'!" % validated_pass)
    return True


def validate_hardware_server_profile_is_na(server_name):
    logger.info("--> ======= start validating server '%s' that its 'Server profile' should be 'n/a'  ======" % server_name)
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    if VerifyHardware.verify_server_hardware_exist(server_name=server_name, fail_if_false=False) is False:
        logger.warn("server hardware '%s' does not exist" % server_name)
        return False

    CommonOperationServerHardware.click_server_hardware(server_name=server_name, timeout=5, time_for_loading=5)
    FusionUIBase.select_view_by_name(view_name='Hardware', timeout=5, fail_if_false=False)
    if VerifyHardware.is_server_profile_displayed_as_na(timeout=5, fail_if_false=False) is True:
        logger.info("server '%s' is successfully verified that 'Server profile' is 'n/a'" % server_name)
        return True
    else:
        logger.warn("failed to verify 'Server profile' as 'n/a' for server '%s', function/keyword '%s' return FALSE" % (server_name, sys._getframe().f_code.co_name))
        return False


def validate_cannot_select_monitored_dl_when_creating_profile(server_name):
    logger.info("--> ======= start validating server '%s' that it should be not-selectable during creating profile  ======" % server_name)
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    if VerifyHardware.verify_server_hardware_exist(server_name=server_name, fail_if_false=False) is False:
        logger.warn("server hardware '%s' does not exist" % server_name)
        return False

    if VerifyHardware.is_server_hardware_not_selectable_when_creating_profile(server_name=server_name, fail_if_false=False) is True:
        logger.info("server '%s' is successfully verified as NOT selectable when creating profile, function/keyword '%s' returns TRUE" % (server_name, sys._getframe().f_code.co_name))
        return True
    else:
        logger.warn("failed to verify server '%s' as NOT selectable when creating profile, function/keyword '%s' returns FALSE" % (server_name, sys._getframe().f_code.co_name))
        return False


def validate_cannot_select_monitored_dl_when_editing_profile(server_name, reference_server_name):
    logger.info("--> ======= start validating server '%s' that it should be not-selectable during editing profile  ======" % server_name)
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    if VerifyHardware.verify_server_hardware_exist(server_name=server_name, fail_if_false=False) is False:
        logger.warn("server hardware '%s' does not exist" % server_name)
        return False

    if VerifyHardware.verify_server_hardware_exist(server_name=reference_server_name, fail_if_false=False) is False:
        logger.warn("server hardware (reference server) '%s' does not exist" % server_name)
        return False

    from FusionLibrary.ui.servers import serverprofiles
    logger.info("start creating a simple profile for server '%s' ..." % reference_server_name)

    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
    profile_name_of_ref_server = 'SP_ref_%s' % reference_server_name
    from FusionLibrary.ui.business_logic.servers.serverprofiles import VerifyServerProfile
    if VerifyServerProfile.verify_server_profile_not_exist(profile_name=profile_name_of_ref_server, timeout=5, fail_if_false=False) is True:
        if serverprofiles.create_simple_server_profile_by_server_hardware(profile_name=profile_name_of_ref_server, server_name=reference_server_name, return_true_if_exists=True) is False:
            logger.warn("failed to create a simple server profile '%s' for validating if server '%s' is not selectable when editing profile, function/keyword '%s' returns FALSE" % (profile_name_of_ref_server, server_name, sys._getframe().f_code.co_name))
            FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
            return False
    else:
        logger.warn("server profile '%s' already exists, no need to create, test will continue ..." % profile_name_of_ref_server)

    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    if VerifyHardware.is_server_hardware_not_selectable_when_editing_profile(server_name=server_name, profile_name=profile_name_of_ref_server, fail_if_false=False) is True:
        logger.info("server '%s' is successfully verified as NOT selectable when editing profile, function/keyword '%s' returns TRUE" % (server_name, sys._getframe().f_code.co_name))
        ret = True
    else:
        logger.warn("failed to verify server '%s' as NOT selectable when editing profile, function/keyword '%s' returns FALSE" % (server_name, sys._getframe().f_code.co_name))
        ret = False

    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    return ret


def delete_monitor_account(server_obj):
    monitor_account = '_HPOneViewMonitor'
    servers_have_monitor_account = []

    for n, server in enumerate(server_obj):
        ilo_client = IloClient(server.iloIP, server.iloUserName, server.iloPassword)
        # iLO account for monitoring
        users = ilo_client.get_all_users()

        if monitor_account not in users:
            continue

        ilo_client.delete_user(monitor_account)
        users = ilo_client.get_all_users()

        if monitor_account in users:
            logger.warn("%s is not removed from iLO" % monitor_account)
            servers_have_monitor_account.append(server.name)

        logger.info("%s is removed from iLO" % monitor_account)

    if servers_have_monitor_account:
        return False

    return True


def validate_server_hardware_page(*enc_obj):
    """ This function is to verify server hardware info

        Example:
       verify_server_hardware_info(CC-2)
    """
    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])

    return_val = True
    selenium2lib = ui_lib.get_s2l()
    # verifying the server hardware type page is opened or not and opening it if not.
    if not selenium2lib._is_element_present(FusionServerHardwarePage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()

    for enclosure in enc_obj:
        server_list = _list_servers(enclosure.name)
        if (len(server_list) == 0):
            logger.warn("No servers are available in the give enclosure %s" % enclosure.name)
        for server in server_list:

            server_ui_info = _get_server_hardware_info(server)
            bay = server.split("bay")
            bay_no = str(bay[1].strip(' ').strip('\r').strip('\t'))
            server_info = _retrieve_server_data(int(bay_no), enclosure.oa1hostname, enclosure.oa1username, enclosure.oa1password)
            flag = False
            logger.info("Comparing the data in hardware drop down")
            for key in server_info:
                for key1 in server_ui_info:
                    if key == key1:
                        if(server_info[key].strip() != server_ui_info[key].strip()):
                            logger.warn("Data %s comparison with OA %s failed against appliance data %s" % (key, server_info[key], server_ui_info[key]))
                        else:
                            flag = True
            if flag:
                logger.info("Verification passed for specified values in Hardware dropdown")
            else:
                logger.warn("Verification failed for one/some values in Hardware dropdown")

            port_ui_info = _get_server_port_info(server)
            port_info = _retrieve_port_info(bay_no, enclosure.oa1hostname, enclosure.oa1username, enclosure.oa1password)
            flag1 = False
            for k1 in port_info:
                for k2 in port_ui_info:
                    if k1 == k2:
                        if 'model' in k1:
                            if (port_ui_info[k1].strip(".") in port_info[k1]):
                                flag1 = True
                            else:
                                flag1 = False
                        elif port_info[k1].strip() != port_ui_info[k2].strip():
                            flag1 = False
                        else:
                            flag1 = True
            if flag1:
                logger.info("Verification passed for specified values in Ports drop down")
            else:
                logger.warn("Verification failed for one/some values in Port drop down")

            if _is_activity_availabe("Add"):
                logger.info("Verification passed for activity in server activity tab")
            else:
                logger.warn("Verification failed for activity in server activity tab")

            if not flag1 and not flag:
                return_val = False

    return return_val


def _is_activity_availabe(activity):
    """ This function will check for the activity in server activity tab
        Example:
        _is_activity_availabe(activity_name)
    """
    s2l = ui_lib.get_s2l()
    # Verify activity  in server page Activity
    ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_ELEMENT_SERVER_OVERVIEW)
    ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_ELEMENT_SERVER_OVERVIEW)
    ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_SELECT_ACTIVITY)
    ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_SELECT_ACTIVITY)

    ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_SERVER_TAB_ACTIVITY % activity, PerfConstants.DEFAULT_SYNC_TIME)
    if s2l._is_element_present(FusionServerHardwarePage.ID_SERVER_TAB_ACTIVITY % activity):
        return True
    s2l.capture_page_screenshot()
    return False


def _list_servers(encl_name):
    """ This function is to list the servers of a particular enclosure
        Example:
       _list_server(CC-2)
    """
    s2l = ui_lib.get_s2l()
    listserver = []
    if not s2l._is_element_present(FusionServerHardwarePage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()
    server_list = [el.text for el in s2l._element_find(FusionServerHardwarePage.ID_TABLE_SERVER_NAME_LIST, False, False)]
    for serverobj in server_list:
        encllist = serverobj.split(',')
        strenclosurename = encllist[0]
        if encl_name == strenclosurename:
            listserver.append(serverobj)
    return listserver


def _retrieve_port_info(bay_no, encl_ip, encl_usrname, encl_passwd):
    """ This function will return a dictionary of server port info retrieved from OA
        Example:
        _get_port_info(bay_no, encl_ip, encl_usrname, encl_passwd)
    """
    ports = {}
    oainfo = blade_info(encl_ip, encl_usrname, encl_passwd)
    try:
        ports = oainfo.get_server_port_data(bay_no)
    except Exception as e:
        logger.warn("Exception while fetching data from OA")
        logger.warn(e)
    return ports


def _compare_two_dictionaries(dict1, dict2):
    """ This function will return a the result of comparison of two dictionary
           Example:
        _compare_two_dictionaries(@{dict1}, @{dict2})
    """

    for oneval in dict1.keys():
        if dict2[oneval] == dict1[oneval]:
            logger.info("The value of %s is %s and is same after the deployment" % (oneval, dict1[oneval]))
        else:
            logger.warn("The value of %s is %s and is not same after the deployment" % (oneval, dict1[oneval]))


def validate_server_hardware_meet_minimum_ilo_firmware_version(server_obj, fail_if_false=False):
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    attributes_not_match = ''
    for n, server in enumerate(server_obj):
        select_server(server.name)
        if server.has_property('expectedStatus'):
            expected_status = server.expectedStatus.lower().split('|')
            result = False
            for status in expected_status:
                result = (result or VerifyHardware.verify_server_hardware_status(server.name, status.strip()))
            if not result:
                attributes_not_match += "status: not as expected, expecting '%s' \n" % expected_status
            if getattr(server, 'expectedNotifyMessage', '') != '':
                notify_message = CommonOperationServerHardware.get_page_notify_message()
                # if not (server.expectedNotifyMessage in notify_message):
                # 2015-11-04 Alex Ma changed, since get_page_notify_message() returns None if no notify message occurs.
                if notify_message is None or server.expectedNotifyMessage not in notify_message:
                    logger.warn("Couldn't find expected notify message '%s' from page. (%s)"
                                % (server.expectedNotifyMessage, notify_message))
                    attributes_not_match += "notify message not match: Got '%s', expecting '%s' \n" \
                                            % (notify_message, server.expectedNotifyMessage)
        if not server.has_property('Hardware'):
            logger.warn("did not find node 'Hardware'" % server.name)
            return False

        # Get actual hardware information on server hardware page
        actual_hardware_info = _get_server_hardware_info(server.name)

        # Get expected value from test data
        expected_hardware_info = _get_hardware_info_from_test_data(server.Hardware)

        # Compare if match. When Business logical functions get ready, replace with them
        for key, value in expected_hardware_info.items():

            # skip attributes that may be changed
            # if key in ['ServerPowerOn', 'MaxPower', 'RomVersion', 'IloVersion']:
            #     logger.warn("Skip validation for hardware attributes: %s" % key)
            #     continue
            logger.info(actual_hardware_info)
            if key in actual_hardware_info:
                if value == actual_hardware_info[key]:
                    logger.info("%s: [%s] is correct" % (key, value))
                else:
                    attributes_not_match += "%s: " % server.name
                    attributes_not_match += "%s " % key
                    attributes_not_match += "[%s] " % value
                    attributes_not_match += "[%s]" % actual_hardware_info[key]
                    attributes_not_match += "\n"

    # Fail this validation if there are attributes not matched
    if attributes_not_match:

        # if fail_if_false is False:
        #    logger.warn(attributes_not_match)
        #   return False
        # else:
        #    ui_lib.fail_test(attributes_not_match)
        return FusionUIBase.fail_test_or_return_false(attributes_not_match, fail_if_false=fail_if_false)
    return True


def power_off_server(server_name):
    """ Power Off Server     """
    navigate()
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionServerHardwarePage.ID_PAGE_LABEL):
        navigate()
    if ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_ELEMENT_SERVER_BASE % server_name):
        logger._log_to_console_and_log_file("Valid server %s" % server_name)
    else:
        logger._warn("Invalid server %s" % server_name)
        return False
    ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_MENU_ACTION_MAIN_BTN)
    if selenium2lib._is_visible(FusionServerHardwarePage.ID_MENU_ACTION_POWEROFF):
        logger._log_to_console_and_log_file("Powering off server '%s'" % server_name)
        selenium2lib.click_element(FusionServerHardwarePage.ID_MENU_ACTION_POWEROFF)
        ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_BTN_POWER_PRESS_AND_HOLD)
        ui_lib.wait_for_element(FusionServerHardwarePage.ID_SERVER_POWER_OFF_VALIDATE, PerfConstants.SERVER_POWER_OFF)
        ui_lib.wait_for_element(FusionServerHardwarePage.ID_MENU_ACTION_MAIN_BTN)
        selenium2lib.click_element(FusionServerHardwarePage.ID_MENU_ACTION_MAIN_BTN)
        if selenium2lib._is_visible(FusionServerHardwarePage.ID_MENU_ACTION_POWEROFF):
            logger._warn("Failed to power off the server %s" % server_name)
            return False
        else:
            logger._log_to_console_and_log_file("Successfully server %s is powered off" % server_name)
            return True
    else:
        logger._log_to_console_and_log_file("'%s' is already powered off" % server_name)
    return True


def get_server_firmware_version(server_name):
    """ Get Server Firmware Version """
    if not ui_lib.wait_for_element(FusionServerHardwarePage.ID_PAGE_LABEL):
        navigate()

    if not select_server(server_name):
        return False

    """  Capturing Server Hardware Firmware Version details from server hardware page """
    server_firmware = {}
    ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_ELEMENT_SERVER_OVERVIEW)
    ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_LINK_HARDWARE)
    if ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_LINK_ROM_VERSION):
        server_firmware["ROM version"] = ui_lib.get_text(FusionServerHardwarePage.ID_LINK_ROM_VERSION)
        server_firmware["ILO_Version"] = ui_lib.get_text(FusionServerHardwarePage.ID_LINK_ILO_VERSION)
        logger._log_to_console_and_log_file(server_firmware)

    return server_firmware


def power_on_all_servers():
    """ Power On All Servers    """
    selenium2lib = ui_lib.get_s2l()
    """ Navigate to Server Hardware Page """
    if not selenium2lib._is_element_present(FusionServerHardwarePage.ID_PAGE_LABEL):
        navigate()

    # get the list of networks
    ui_lib.wait_for_element(FusionServerHardwarePage.ID_SERVER_LIST)
    server_names = ([ui_lib.get_text(el) for el in selenium2lib._element_find(FusionServerHardwarePage.ID_SERVER_LIST_NAMES, False, False)])
    count = 0
    for server_name in server_names:
        status = power_on_server(server_name)
        if status:
            count = count + 1
    if len(server_names) == count:
        return True
    else:
        return False


def power_on_server(server_name):
    """ Power On Server    """
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionServerHardwarePage.ID_PAGE_LABEL):
        navigate()
    if ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_ELEMENT_SERVER_BASE % server_name):
        logger._log_to_console_and_log_file("Valid server %s" % server_name)
    else:
        logger._warn("Invalid server %s" % server_name)
        return False
    ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_MENU_ACTION_MAIN_BTN)
    if selenium2lib._is_visible(FusionServerHardwarePage.ID_MENU_ACTION_POWERON):
        logger._log_to_console_and_log_file("Powering on server '%s'" % server_name)
        selenium2lib.click_element(FusionServerHardwarePage.ID_MENU_ACTION_POWERON)
        # ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_BTN_POWER_PRESS_AND_HOLD)
        ui_lib.wait_for_element(FusionServerHardwarePage.ID_SERVER_POWER_ON_VALIDATE, PerfConstants.SERVER_POWER_ON)
        ui_lib.wait_for_element(FusionServerHardwarePage.ID_MENU_ACTION_MAIN_BTN)
        selenium2lib.click_element(FusionServerHardwarePage.ID_MENU_ACTION_MAIN_BTN)
        if selenium2lib._is_visible(FusionServerHardwarePage.ID_MENU_ACTION_POWERON):
            logger._warn("Failed to power on the server %s" % server_name)
            return False
        else:
            logger._log_to_console_and_log_file("Successfully server %s is powered on" % server_name)
            return True
    else:
        logger._log_to_console_and_log_file("'%s' is already powered on" % server_name)
    return True


def power_of_all_servers():
    """ Power Off All Servers    """
    selenium2lib = ui_lib.get_s2l()
    """ Navigate to Server Hardware Page """
    if not selenium2lib._is_element_present(FusionServerHardwarePage.ID_PAGE_LABEL):
        navigate()

    # get the list of networks
    ui_lib.wait_for_element(FusionServerHardwarePage.ID_SERVER_LIST)
    server_names = ([el.text for el in selenium2lib._element_find(FusionServerHardwarePage.ID_SERVER_LIST_NAMES, False, False)])

    for server_name in server_names:
        power_off_server(server_name)


def validate_server_utilization_panel(*serverhardware_obj):
    """
        Description: This function will check the existence of ILO advanced license for server hardware,
                     based on this utilization panel validation will be done.
    """

    if not ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_PAGE_LABEL):
        navigate()

    if not ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_PAGE_LABEL):
        logger._warn("Unable to open server hardware page")
        return False

    if isinstance(serverhardware_obj, test_data.DataObj):
        serverhardware_obj = [serverhardware_obj]
    elif isinstance(serverhardware_obj, tuple):
        serverhardware_obj = list(serverhardware_obj[0])

    for server in serverhardware_obj:
        logger._log_to_console_and_log_file("Selecting server: {0}".format(server.name))
        if not select_server(server.name):
            return False

        logger._log_to_console_and_log_file("Checking the power status and powering off the server {0} if not powered off".format(server.name))
        if not power_on_server(server.name):
            return False

        logger._log_to_console_and_log_file("Retrieving server license from OA")
        oainfo_server = blade_info(server.hostname, server.username, server.password)
        server_license = oainfo_server.get_server_license()
        logger._log_to_console_and_log_file("'{0}' server ILO license: {1}".format(server.name, server_license))

        if len(server_license) == 1 and ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_NO_ILO_LICENSE):
            logger._log_to_console_and_log_file("'{0}' does't have ILO advanced license".format(server.name))
            logger._log_to_console_and_log_file("Capturing the Utilization panel message for servers which doesn't have ILO advance license")
            ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_NO_ILO_LICENSE, PerfConstants.DEFAULT_SYNC_TIME)
            no_license_msg = ui_lib.get_text(FusionServerHardwarePage.ID_NO_ILO_LICENSE)
            logger._log_to_console_and_log_file(no_license_msg)
            return False
        elif ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_CPU_METER):
            logger._log_to_console_and_log_file("'{0}' is having ILO advanced license".format(server.name))
            logger._log_to_console_and_log_file("Utilization panel is visible for Server '{0}' ".format(server.name))
            return True


def validate_sever_temperature(*hw_obj):
    """
        This function will compare temperature values captured from UI and OA
        Example: Validate_Severer_hardware_temperature(@{enclosure details})
    """
    if not ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_PAGE_LABEL):
        navigate()

    if isinstance(hw_obj, test_data.DataObj):
        hw_obj = [hw_obj]
    elif isinstance(hw_obj, tuple):
        hw_obj = list(hw_obj[0])

    for hardware in hw_obj:
        logger._log_to_console_and_log_file("Selecting server: {0}".format(hardware.server))
        if not select_server(hardware.server):
            return False

        logger._log_to_console_and_log_file("Checking the power status and powering off the server {0} if not powered off".format(hardware.server))
        if not power_on_server(hardware.server):
            return False

        if not ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_NO_ILO_LICENSE, PerfConstants.DEFAULT_SYNC_TIME):
            ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_PANEL)
            ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_LINK_UTILIZATION)
            ui_lib.wait_for_element_and_click("id=temp-collapsible")
            ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_ELEMENT_TEMPERATURE)
            temp_from_ui = ui_lib.get_text(FusionServerHardwarePage.ID_ELEMENT_TEMPERATURE)
            oainfo_enclr = blade_info(hardware.enclr_hostname, hardware.enclr_username, hardware.enclr_password)
            bay_no = hardware.server.split()[2]
            temp_from_oa = oainfo_enclr.get_server_temp(bay_no)
            if int(temp_from_oa.split()[0]) in range(int(temp_from_ui.split()[0]) - 10, int(temp_from_ui.split()[0]) + 10):
                logger._log_to_console("Temperature values displayed in appliance and OA for server '{0}' are same".format(hardware.server))
                return True
            else:
                logger._warn("Temperature values displayed in appliance and OA for server '{0}' are different".format(hardware.server))
                return False
        else:
            ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_NO_ILO_LICENSE, PerfConstants.DEFAULT_SYNC_TIME)
            logger._warn(ui_lib.get_text(FusionServerHardwarePage.ID_NO_ILO_LICENSE))
            return False


def verify_alert_generated_in_appliance(*activity_obj):
    """
        This function verifies whether the alert is generated in the appliance
        Example:
        verify_alert_generated_in_appliance('Firmware Update success', 'CC-2-LI')
    """
    s2l = ui_lib.get_s2l()
    if not s2l._is_element_present(FusionActivityPage.ID_PAGE_LABEL):
        logger._log_to_console("\n")
        activity.navigate()

    if isinstance(activity_obj, test_data.DataObj):
        activity_obj = [activity_obj]
    elif isinstance(activity_obj, tuple):
        activity_obj = list(activity_obj[0])

    """ Verify specific alert in alert page """
    for alert in activity_obj:
        activity_status = activity._is_element_present_activity_page_without_time(alert.name, alert.resource)
        if activity_status:
            logger._log_to_console("Alert received in appliance for device '{0}'".format(alert.resource))
        else:
            logger._warn("Failed to receive alert in appliance for device '{0}'".format(alert.resource))
            return False
    return True


def validate_server_health_status(*server_obj):

    if isinstance(server_obj, test_data.DataObj):
        server_obj = [server_obj]
    elif isinstance(server_obj, tuple):
        server_obj = list(server_obj[0])

    """ Navigate to server Page """
    if not ui_lib.wait_for_element(FusionServerHardwarePage.ID_PAGE_LABEL):
        navigate()

    for server in server_obj:
        if not select_server(server.name):
            return False

        logger._log_to_console_and_log_file("Verifying the server {0} status".format(server.name))
        if ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_SERVER_STATUS_OK, PerfConstants.DEFAULT_SYNC_TIME):
            if server.expectedstatus.lower() == 'ok':
                logger._log_to_console_and_log_file("Server '{0}' health status is 'OK' as expected".format(server.name))
            else:
                logger._warn("Server '{0}' health status is not 'OK' as per expected".format(server.name))
                return False
        elif ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_SERVER_STATUS_ERROR, PerfConstants.DEFAULT_SYNC_TIME):
            ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_ERROR_WARN_MSG, PerfConstants.DEFAULT_SYNC_TIME)
            err_msg = ui_lib.get_text(FusionServerHardwarePage.ID_ERROR_WARN_MSG)
            logger._log_to_console_and_log_file("Server '{0}' health status is 'ERROR' as expected, with the error msg : '{1}'".format(server.name, err_msg))
            if server.expectedstatus.lower() == 'error':
                logger._log_to_console_and_log_file("Server '{0}' health status is 'ERROR' as expected".format(server.name))
            else:
                logger._warn("Server '{0}' health status is not 'ERROR' as per expected".format(server.name))
                return False
        else:
            if server.expectedstatus.lower() == 'warning':
                logger._log_to_console_and_log_file("Server '{0}' health status is 'WARNING' as expected".format(server.name))
            else:
                logger._warn("Server '{0}' health status is not 'WARNING' as per expected".format(server.name))
                return False
    return True


def create_labels_for_server_hardware(serverhardware_obj):

    s2l = ui_lib.get_s2l()
    """ Navigate to Server Hardware Page """
    logger._log_to_console_and_log_file("Function call to add label for server hardware ")
    if not ui_lib.wait_for_element(FusionServerHardwarePage.ID_PAGE_LABEL):
        navigate()

    if isinstance(serverhardware_obj, test_data.DataObj):
        serverhardware_obj = [serverhardware_obj]
    elif isinstance(serverhardware_obj, tuple):
        serverhardware_obj = list(serverhardware_obj)

    for server in serverhardware_obj:
        ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_LINK_RESET)
        if not select_server(server.serverhardwarename):
            return False

        ui_lib.wait_for_element(FusionServerHardwarePage.ID_SERVER_LIST)

        ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_PANEL)
        ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_DROPDOWN_SELECTION)
        if ui_lib.wait_for_element(FusionServerHardwarePage.ID_EDIT_LABEL):
            ui_lib.move_to_element_and_click(FusionServerHardwarePage.ID_LABEL, FusionServerHardwarePage.ID_EDIT_LABEL)
            if ui_lib.wait_for_element(FusionServerHardwarePage.ID_EDIT_LABEL_PANEL):
                ui_lib.wait_for_element_and_input_text(FusionServerHardwarePage.ID_LABEL_NAME, server.lname, 20)
                ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_ADD_LABEL_BTN)
                ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_OK_LABEL_BTN)
            else:
                raise AssertionError("Failed to navigate edit label panel")
        else:
            logger._warn("Could not find Edit button to add label")

        if ui_lib.wait_for_element(FusionServerHardwarePage.ID_ADDED_LABEL % server.lname):
            ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_ADDED_LABEL % server.lname)
            serverhardware_list = []
            ui_lib.wait_for_element(FusionServerHardwarePage.ID_SERVER_LIST_NAMES)
            serverhardware_list = [ui_lib.get_text(s) for s in s2l._element_find(FusionServerHardwarePage.ID_SERVER_LIST_NAMES, False, False)]
            for serverhardware in serverhardware_list:
                if serverhardware.lower() == server.serverhardwarename.lower():
                    logger._log_to_console_and_log_file("Label {0} is successfully added to the server hardware '{1}'".format(server.lname, server.serverhardwarename))
                else:
                    raise AssertionError("Failed to add label to the selected server hardware")
    return True


def edit_scope_for_server_hardware(server_hardware_list):
    """ edit scope for server hardware
        This function is to edit scope for server hardware
        Example:
            edit_scope_for_server_hardware(server_hardware_list)
    """
    logger.info("Function call to edit scope for server hardware")

    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE)

    for server_hardware in server_hardware_list:
        if not select_server(server_hardware.name):
            ui_lib.fail_test("Failed to find target server hardware")

        FusionUIBase.select_view_by_name("Scopes")
        EditScopeForHardwares.click_edit_scope_button()
        EditScopeForHardwares.wait_edit_scope_dialog_open()
        scope_list = server_hardware.scopes.split(',')
        for scope in scope_list:
            if not VerifyHardware.verify_scope_should_exist_in_edit_page(scope, 2):
                EditScopeForHardwares.click_assign_button()
                EditScopeForHardwares.wait_assign_scope_dialog_open()
                EditScopeForHardwares.input_scope_name(scope)
                EditScopeForHardwares.click_scope_name(scope)
                EditScopeForHardwares.click_add_button()
                EditScopeForHardwares.wait_assign_scope_dialog_close()

        if server_hardware.has_property("remove_scopes"):
            remove_scope_list = server_hardware.remove_scopes.split(',')
            for scope in remove_scope_list:
                if VerifyHardware.verify_scope_should_exist_in_edit_page(scope, timeout=5, fail_if_false=True):
                    EditScopeForHardwares.click_remove_scope_icon(scope)

        EditScopeForHardwares.click_ok_button()
        EditScopeForHardwares.wait_edit_scope_dialog_close()

        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(server_hardware.name, 'Update', timeout=60, fail_if_false=True)
        FusionUIBase.show_activity_sidebar()

    return True


def validate_scope_can_be_assigned_for_server_hardware(server_hardware_list):
    """ validate scope can be assigned for server hardware
        This function is to validate can be assigned for server hardware
        Example:
            validate_scope_can_be_assigned_for_server_hardware(server_hardware_list)
    """
    logger.info("Function call to validate scope can be assigned for server hardware")

    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE)

    for server_hardware in server_hardware_list:
        if not select_server(server_hardware.name):
            ui_lib.fail_test("Failed to find target server hardware")

        FusionUIBase.select_view_by_name("Overview")
        FusionUIBase.select_view_by_name("Scopes")
        EditScopeForHardwares.click_edit_scope_button()
        EditScopeForHardwares.wait_edit_scope_dialog_open()
        scope_list = server_hardware.scopes.split(',')
        for scope in scope_list:
            if not VerifyHardware.verify_scope_should_exist_in_edit_page(scope):
                EditScopeForHardwares.click_assign_button()
                EditScopeForHardwares.wait_assign_scope_dialog_open()
                EditScopeForHardwares.input_scope_name(scope)
                EditScopeForHardwares.click_scope_name(scope)
                EditScopeForHardwares.click_add_button()
                EditScopeForHardwares.wait_assign_scope_dialog_close()

        EditScopeForHardwares.click_cancel_button()
        EditScopeForHardwares.wait_edit_scope_dialog_close()

    return True


def validate_scope_assign_for_server_hardware(server_hardware_list):
    """ validate scope assign for server hardware
        This function is to validate scope assign for server hardware
        Example:
            validate_scope_assign_for_server_hardware(server_hardware_list)
    """
    logger.info("Function call to validate scope assign for server hardware")

    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE)

    for server_hardware in server_hardware_list:
        if not select_server(server_hardware.name):
            ui_lib.fail_test("Failed to find target server hardware")

        FusionUIBase.select_view_by_name("Scopes")
        if server_hardware.has_property("scopes"):
            scope_list = server_hardware.scopes.split(',')
            for scope in scope_list:
                if scope != "":
                    VerifyHardware.verify_scope_should_exist(scope)
        if server_hardware.has_property("removed_scopes"):
            scope_list = server_hardware.removed_scopes.split(',')
            for scope in scope_list:
                if scope != "":
                    VerifyHardware.verify_scope_should_not_exist(scope)

    return True


def validate_no_license_on_server_hardware(server_hardware_obj):
    """ validate no licenses info on server hardware page
        This function is to make sure that no license assign for server hardware
        Example:
            validate_no_license_on_server_hardware(serverhardware_obj)
    """
    logger.info("Function call to validate no licenses assign for server hardware")

    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE)

    for server_hardware in server_hardware_obj:
        CommonOperationServerHardware.click_server_hardware(server_hardware.name)
        CommonOperationServerHardware.wait_server_hardware_selected(server_hardware.name)
        if not VerifyHardware.verify_server_hardware_no_license_info(server_hardware.licenses):
            ui_lib.fail_test("Find unexpected licenses info on server hardware page")
    return True


def verify_add_server_hardware_button_notvisible():
    """ Add Server Hardware Button Visibility Check"""
    return VerifyHardware.verify_add_server_hardware_button_notvisible()


def validate_privileges_edit_serverhardware(obj):
    """
        The function will validate the user permissions for serverhardware in the Action Menu based.
        Arguments:
            serverhardware object
    """
    logger.info("\nVerify Actions Menu for users")
    navigate()
    for serverhardware_obj in enumerate(obj):
        CommonOperationServerHardware.click_action_button()
        logger.info("Verifying 'Edit' Action visible")
        if hasattr(serverhardware_obj, "NoAuthorization"):
            exp_msg = getattr(serverhardware_obj, "NoAuthorization")
            logger.info("Expected message for users with no authorization is %s" % exp_msg)
            return VerifyHardware.verify_actions_noauthorization(exp_msg)
        else:
            return VerifyHardware.verify_actions_add()


def validate_server_sub_task(server_obj):
    """ Validate server add/edit task text

    Arguments:
      name*             --  Name of server as a string.
      task*             --  Name of server task as a string.
      subtask*          --  Name of sub task as a string.
      source*           --  Name of task source as a string.
      status            --  Status of task as a string.
      validate_timeout  --  Timeout.

    * Required Arguments

    Example:
    Example:
        data/servers -> @{TestData.servers.Add}
            <servers>
                <Add>
                    <server name="wpstdl2-ilo" task="Add" subtask="Update iLO firmware" source="wpstdl2-ilo" status="OK"/>
                </Add>
            </servers>

    """

    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    total = len(server_obj)
    not_exists = 0
    verified = 0

    for n, server in enumerate(server_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("Validate server <%s> task contains <%s>" % (server.name, server.subtask))
        if not VerifyHardware.verify_server_hardware_exist(server.name, fail_if_false=False):
            logger.warn("server '%s' does not exist" % server.name)
            not_exists += 1
            continue

        CommonOperationServerHardware.click_server_hardware(server.name)
        FusionUIBase.select_view_by_name(view_name='Activity', timeout=5)
        CommonOperationServerHardware.click_activity_collapser(server.task)
        timeout = int(getattr(server, 'validate_timeout', '5'))
        status = getattr(server, 'status', 'ok').lower()
        ret = VerifyHardware.verify_activity_contains_subtask(subtask=server.subtask, source=server.source, status=status, timeout=timeout, fail_if_false=False)
        # Verify step text not exist in steps
        if getattr(server, 'exist', '').lower() == 'false':
            if ret is True:
                ui_lib.fail_test("%s should not exist in task" % server.subtask)
        elif ret is False:
            ui_lib.fail_test("%s should exist in task" % server.subtask)

        logger.info("server '%s' got the correct sub task" % server.name)
        verified += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no server to view! all %s server(s) is NOT existing, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if verified < total:
            logger.warn("not all of task for the server(s) is successfully verified - %s out of %s verified " % (verified, total))
            if verified + not_exists == total:
                logger.warn("%s not-existing server(s) is skipped, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s not-existing server(s) is skipped, %s profile(s) left is failed being verified " % (not_exists, total - verified - not_exists))
                return False

    logger.info("all of the server(s) is successfully verified - %s out of %s " % (verified, total))
    return True


# begin - keywords especial for uid light(F136)
def turn_on_server_uid(*server_obj):
    """ turn_on_uid_server
        Example:
        | `Turn On server UID `      |     |
    """
    logger.info("Function call to turn on uid light for server hardware")

    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE)

    if isinstance(server_obj, test_data.DataObj):
        server_obj = [server_obj]
    elif isinstance(server_obj, tuple):
        server_obj = list(server_obj[0])

    fail_time = 0
    for server in server_obj:
        if not select_server(server.name):
            logger.warn("Exiting Turn On UID server Function, Not selected server %s" % server.name)
            fail_time += 1
            continue

        CommonOperationServerHardware.verify_uid_light_off()
        CommonOperationServerHardware.click_uid_light()
        CommonOperationServerHardware.verify_uid_light_on()

    if fail_time > 0:
        return False
    else:
        return True


def turn_off_server_uid(*server_obj):
    """ turn_off_uid_server
        Example:
        | `Turn Off server UID`      |     |
    """
    logger.info("Function call to turn off uid light for server hardware")

    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE)

    if isinstance(server_obj, test_data.DataObj):
        server_obj = [server_obj]
    elif isinstance(server_obj, tuple):
        server_obj = list(server_obj[0])

    fail_time = 0
    for server in server_obj:
        if not select_server(server.name):
            logger.warn("Exiting Turn Off UID server Function, Not selected server %s" % server.name)
            fail_time += 1
            continue

        CommonOperationServerHardware.verify_uid_light_on()
        CommonOperationServerHardware.click_uid_light()
        CommonOperationServerHardware.verify_uid_light_off()

    if fail_time > 0:
        return False
    else:
        return True


def validate_server_uid_light_off(*server_obj):
    """ verify whether the uid(s) of server(s) are in off status.
        Example:
        | `validate_server_uid_light_off`    | @(IC data) |
    """
    logger.info("Function call to validate uid light off for server hardware")

    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE)

    if isinstance(server_obj, test_data.DataObj):
        server_obj = [server_obj]
    elif isinstance(server_obj, tuple):
        server_obj = list(server_obj[0])

    fail_time = 0
    for server in server_obj:
        if not select_server(server.name):
            logger.warn("Exiting Turn On UID server Function, Not selected server %s" % server.name)
            fail_time += 1
            continue

        CommonOperationServerHardware.verify_uid_light_off()

    if fail_time > 0:
        return False
    else:
        return True
# end - keywords especial for uuid light(F136)

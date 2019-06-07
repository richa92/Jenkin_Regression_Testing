# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.

"""
    Logical Switches page/sets
"""

from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.business_logic.base import SectionType
from FusionLibrary.ui.business_logic.networking.logicalswitchgroups import CommonOperationLogicalSwitchGroups
from FusionLibrary.ui.business_logic.networking.logicalswitches import (
    CommonOperationLogicalSwitches,
    CreateLogicalSwitches,
    DeleteLogicalSwitches,
    EditLogicalSwitches,
    VerifyLogicalSwitches,
)
from FusionLibrary.ui.business_logic.networking.logicalswitches_elements import FusionLogicalSwitchPage
from FusionLibrary.ui.business_logic.networking.logicalswitches_elements import GeneralLogicalSwitchesElements
from RoboGalaxyLibrary.utilitylib import logging
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.business_logic.base import FusionUIBase
from RoboGalaxyLibrary.data import test_data
from FusionLibrary.ui.usersandgroups.usersandgroups_elements import FusionUserandGroupsPage
from datetime import datetime
import paramiko
import re
import sys


def navigate():
    FusionUIBase.navigate_to_section(SectionType.LOGICAL_SWITCHES, time_for_loading=1)


def create_logical_switches(ls_obj):
    """ Create Logical Switches
        Usage:
            ${data} =       | Get Data By Xpath                         | //LogicalSwitches/Create/ls
            ${result} =     | Fusion UI Create Logical Switches         | @{data.ls}
            Should Be True  | ${result}                                 | msg=Failed to create logical switches


        Test data example:
            1. data -> LogicalSwitches -> Create, place your LS list like below

            <LogicalSwitches>
                <Create>
                    <ls name="LS-CiscoNexus56xx" add_ls_as="Monitored" lsg="LSG-CiscoNexus56xx" >
                        <switch1 ip_or_host_name="172.18.16.91" user_name="dcs" password="hpinvent!" snmp_port="161" snmp_version="v1/v2c" community_string="public" />
                        <switch2 ip_or_host_name="172.18.16.92" user_name="dcs" password="hpinvent!" snmp_port="161" snmp_version="v1/v2c" community_string="public" />
                    </ls>
                    <ls name="LS-CiscoNexus600x" add_ls_as="Monitored" lsg="LSG-CiscoNexus600x" >
                        <switch1 ip_or_host_name="172.18.17.1" user_name="dcs" password="hpinvent!" snmp_port="161" snmp_version="v1/v2c" community_string="public" />
                        <switch2 ip_or_host_name="172.18.17.2" use_same_credentials="true" />
                    </ls>
                </Create>
            </LogicalSwitches>
    """

    navigate()
    logger.info("creating Logical Switches ...")

    total = len(ls_obj)
    created = 0
    already_exists = 0

    for n, ls in enumerate(ls_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("creating a Logical Switch with name '%s' ..." % ls.name)
        # checking if the Logical Switch is already existing
        if not VerifyLogicalSwitches.verify_logical_switch_should_not_exist(ls.name, fail_if_false=False):
            logger.warn("Logical Switch '%s' already exists" % ls.name)
            already_exists += 1
            continue

        CreateLogicalSwitches.click_create_logical_switch_button()
        CreateLogicalSwitches.wait_create_logical_switch_dialog_open()
        CreateLogicalSwitches.input_name(ls.name)
        CreateLogicalSwitches.tick_add_logical_switch_as_monitored() if getattr(ls, 'add_ls_as', '').lower() == 'monitored' else None
        CreateLogicalSwitches.tick_add_logical_switch_as_managed() if getattr(ls, 'add_ls_as', '').lower() == 'managed' else None
        CreateLogicalSwitches.input_select_logical_switch_group(ls.lsg)

        switch1 = ls.switch1[0]
        CreateLogicalSwitches.input_switch1_ip_address_or_host_name(ip_or_host_name=switch1.ip_or_host_name)
        CreateLogicalSwitches.input_switch1_user_name(user_name=switch1.user_name)
        CreateLogicalSwitches.input_switch1_password(password=switch1.password)
        CreateLogicalSwitches.input_switch1_snmp_port(port=switch1.snmp_port)
        CreateLogicalSwitches.select_switch1_snmp_version(version=switch1.snmp_version)
        CreateLogicalSwitches.input_switch1_community_string(community_string=switch1.community_string)

        lsg_count = CommonOperationLogicalSwitchGroups.get_ls_count_of_lsg(lsg_name=ls.lsg)
        if lsg_count == 2:
            switch2 = ls.switch2[0]
            CreateLogicalSwitches.input_switch2_ip_address_or_host_name(ip_or_host_name=switch2.ip_or_host_name)
            if getattr(switch2, 'use_same_credentials', 'false').lower() == 'true':
                CreateLogicalSwitches.tick_switch2_use_same_credentials_as_switch1()
            else:
                CreateLogicalSwitches.untick_switch2_use_same_credentials_as_switch1()
                # TODO: Add logic for dealing with the extra fields of SNMP Version = v3
                CreateLogicalSwitches.input_switch2_user_name(user_name=switch2.user_name)
                CreateLogicalSwitches.input_switch2_password(password=switch2.password)
                CreateLogicalSwitches.input_switch2_snmp_port(port=switch2.snmp_port)
                CreateLogicalSwitches.select_switch2_snmp_version(version=switch2.snmp_version)
                CreateLogicalSwitches.input_switch2_community_string(community_string=switch2.community_string)

        CreateLogicalSwitches.click_create_button()

        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
        if status is True:
            logger.warn("unexpected error occurred: %s" % msg)
            ui_lib.fail_test(msg)

        if CreateLogicalSwitches.wait_create_logical_switch_dialog_close(timeout=10, fail_if_false=False) is True:
            FusionUIBase.show_activity_sidebar()
            timeout = int(getattr(ls, 'timeout', "240"))
            if FusionUIBase.wait_activity_action_ok(ls.name, 'Create', timeout=timeout, fail_if_false=False) is True:
                FusionUIBase.show_activity_sidebar()
                logger.info("successfully created Logical Switch '%s'" % ls.name)
                created += 1
            else:
                logger.warn("'wait_activity_action_ok' = FALSE, skip to next Logical Switch ... ")
                FusionUIBase.show_activity_sidebar()
                continue
        else:
            logger.warn("'wait_create_logical_switch_dialog_close' = FALSE, skip to next Logical Switch ... ")
            CreateLogicalSwitches.click_cancel_button()
            continue

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - already_exists == 0:
        logger.warn("no Logical Switch Group to create! all %s Logical Switch(es) is already existing, test is considered PASS" % already_exists)
        return True
    else:
        if created < total:
            logger.warn("not all of the Logical Switch(es) is successfully created - %s out of %s created " % (created, total))
            if created + already_exists == total:
                logger.warn("%s already existing Logical Switch(es) is skipped, test is considered PASS" % already_exists)
                return True
            else:
                ui_lib.fail_test("%s already existing Logical Switch(es) is skipped, %s Logical Switch(es) left is failed being created " % (already_exists, total - created - already_exists))

    logger.info("all of the Logical Switch(es) is successfully created - %s out of %s " % (created, total))
    return True


def edit_logical_switches(ls_obj):
    """ Edit Logical Switches
        Usage:
            ${data} =       | Get Data By Xpath                         | //LogicalSwitches/Edit/ls             | eliminate_same_node=False
            ${result} =     | Fusion UI Edit Logical Switches           | @{data.ls}
            Should Be True  | ${result}                                 | msg=Failed to edit logical switches


        Test data example:
            1. data -> LogicalSwitches -> Edit, place your LS list like below
            2. You have to give "eliminate_same_node=False" parameter to keyword "Get Data By Xpath" for loading test data,
                otherwise the node "Remove", "Add", or "Edit" will not be located by "ls.Remove", "ls.Add", or "ls.Edit"

            <LogicalSwitches>
                <Edit>
                    <ls name="LS-CiscoNexus56xx" add_ls_as="Monitored" lsg="LSG-CiscoNexus56xx" >
                        <Remove>
                            <switch ip_or_host_name="172.18.16.91" />
                        </Remove>
                        <Add>
                            <switch ip_or_host_name="172.18.16.91" user_name="dcs" password="hpinvent!" snmp_port="161" snmp_version="v1/v2c" community_string="public" />
                        </Add>
                        <Edit>
                            <switch ip_or_host_name="172.18.16.92" user_name="dcs" password="hpinvent!" snmp_port="161" snmp_version="v1/v2c" community_string="public_test" />
                        </Edit>
                    </ls>
                    <ls name="LS-CiscoNexus600x" add_ls_as="Monitored" lsg="LSG-CiscoNexus600x" >
                        <Remove>
                            <switch ip_or_host_name="172.18.17.2" />
                        </Remove>
                        <Add>
                            <switch ip_or_host_name="172.18.17.2" use_same_credentials="true" />
                        </Add>
                        <Edit>
                            <switch ip_or_host_name="172.18.17.1" user_name="dcs" password="hpinvent!" snmp_port="161" snmp_version="v1/v2c" community_string="public_test" />
                            <switch ip_or_host_name="172.18.17.2" user_name="dcs" password="hpinvent!" snmp_port="162" snmp_version="v1/v2c" community_string="public_test" />
                        </Edit>
                    </ls>
                </Edit>
            </LogicalSwitches>
    """

    navigate()
    logger.info("editing Logical Switches ...")

    total = len(ls_obj)
    edited = 0
    not_exists = 0

    for n, ls in enumerate(ls_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("editing a Logical Switch with name '%s' ..." % ls.name)
        # checking if the Logical Switch is already existing
        if not VerifyLogicalSwitches.verify_logical_switch_should_exist(ls.name, fail_if_false=False):
            logger.warn("Logical Switch '%s' does NOT exist!" % ls.name)
            not_exists += 1
            continue

        CommonOperationLogicalSwitches.click_logical_switch(ls_name=ls.name)
        #   start performing edit action
        EditLogicalSwitches.select_actions_edit()
        EditLogicalSwitches.wait_edit_logical_switch_dialog_open()
        EditLogicalSwitches.input_name(ls.name)
        EditLogicalSwitches.tick_add_logical_switch_as_monitored() if getattr(ls, 'add_ls_as', '').lower() == 'monitored' else None
        EditLogicalSwitches.tick_add_logical_switch_as_managed() if getattr(ls, 'add_ls_as', '').lower() == 'managed' else None

        if getattr(ls, 'Remove', None):
            # under node 'Remove', only 1 item of SWITCH node will be used,
            # since editing LS would not allow removing all 2 switches
            EditLogicalSwitches.click_remove_switch_icon(ls.Remove.switch[0].ip_or_host_name)

        if getattr(ls, 'Add', None):
            EditLogicalSwitches.click_add_switch_button()
            EditLogicalSwitches.wait_edit_or_add_switch_dialog_open()

            # under node 'Add', only 1 item of SWITCH node will be used,
            # since editing LS would not allow removing all 2 switches hence there will always be 1 switch there already
            # and only 1 switch can be added
            switch = ls.Add.switch[0]

            EditLogicalSwitches.input_switch_ip_address_or_host_name(ip_or_host_name=switch.ip_or_host_name)
            if getattr(switch, 'use_same_credentials', 'false').lower() == 'true':
                EditLogicalSwitches.tick_use_same_credentials()
            else:
                # TODO: Add logic for dealing with the extra fields of SNMP Version = v3
                EditLogicalSwitches.untick_use_same_credentials()
                EditLogicalSwitches.input_switch_user_name(user_name=switch.user_name)
                EditLogicalSwitches.input_switch_password(password=switch.password)
                EditLogicalSwitches.input_switch_snmp_port(port=switch.snmp_port)
                EditLogicalSwitches.select_switch_snmp_version(version=switch.snmp_version)
                EditLogicalSwitches.input_switch_community_string(community_string=switch.community_string)

            EditLogicalSwitches.click_ok_button_on_edit_or_add_switch_dialog()
            EditLogicalSwitches.wait_edit_or_add_switch_dialog_close()

        if getattr(ls, 'Edit', None):
            for i, sw in enumerate(ls.Edit.switch):

                logger.info("{2} <Editing Switches> No: {0} --- Total: {1} {2}".format((i + 1), len(ls.Edit.switch), '-' * 14))
                logger.info("editing a Logical Switch with name '%s' ..." % ls.name)

                EditLogicalSwitches.click_edit_switch_icon(switch_ip_or_host_name=sw.ip_or_host_name)
                EditLogicalSwitches.wait_edit_or_add_switch_dialog_open()

                EditLogicalSwitches.input_switch_ip_address_or_host_name(ip_or_host_name=sw.ip_or_host_name)
                # TODO: Add logic for dealing with the extra fields of SNMP Version = v3
                EditLogicalSwitches.input_switch_user_name(user_name=sw.user_name)
                EditLogicalSwitches.input_switch_password(password=sw.password)
                EditLogicalSwitches.input_switch_snmp_port(port=sw.snmp_port)
                EditLogicalSwitches.select_switch_snmp_version(version=sw.snmp_version)
                EditLogicalSwitches.input_switch_community_string(community_string=sw.community_string)

                EditLogicalSwitches.click_ok_button_on_edit_or_add_switch_dialog()
                EditLogicalSwitches.wait_edit_or_add_switch_dialog_close()

        EditLogicalSwitches.click_ok_button()

        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
        if status is True:
            logger.warn("unexpected error occurred: %s" % msg)
            ui_lib.fail_test(msg)

        if EditLogicalSwitches.wait_edit_logical_switch_dialog_close(timeout=10, fail_if_false=False) is True:
            FusionUIBase.show_activity_sidebar()
            timeout = int(getattr(ls, 'timeout', "240"))
            if FusionUIBase.wait_activity_action_ok(ls.name, 'Update', timeout=timeout, fail_if_false=False) is True:
                FusionUIBase.show_activity_sidebar()
                logger.info("successfully created Logical Switch '%s'" % ls.name)
                edited += 1
            else:
                logger.warn("'wait_activity_action_ok' = FALSE, skip to next Logical Switch ... ")
                FusionUIBase.show_activity_sidebar()
                continue
        else:
            logger.warn("'wait_create_logical_switch_dialog_close' = FALSE, skip to next Logical Switch ... ")
            EditLogicalSwitches.click_cancel_button()
            continue

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no Logical Switch to edit! all %s Logical Switch(es) is NOT existing, test is considered FAIL" % not_exists)
        return False
    else:
        if edited < total:
            logger.warn("not all of the Logical Switch(es) is successfully edited - %s out of %s edited " % (edited, total))
            if edited + not_exists == total:
                logger.warn("%s non-existing Logical Switch(es) is skipped, test is considered FAIL" % not_exists)
                return False
            else:
                ui_lib.fail_test("%s non-existing Logical Switch(es) is skipped, %s Logical Switch(es) left is failed being edited " % (not_exists, total - edited - not_exists))

    logger.info("all of the Logical Switch(es) is successfully edited - %s out of %s " % (edited, total))
    return True


def delete_logical_switch_by_name(ls_name):
    """ Delete Logical Switch by given LS name
        Usage:
            Fusion UI Delete Logical Switch By Name  |   LS-CiscoNexus50xx
    """

    navigate()
    logger.info("deleting Logical Switch '%s' ..." % ls_name)
    #   check if Logical Switch exists
    if not VerifyLogicalSwitches.verify_logical_switch_should_exist(ls_name, fail_if_false=False):
        logger.warn("Logical Switch '%s' does NOT exist! keyword '%s' returns a 'False'" % (ls_name, sys._getframe().f_code.co_name))
        return False
    CommonOperationLogicalSwitches.click_logical_switch(ls_name=ls_name)
    #   start performing delete action
    DeleteLogicalSwitches.select_actions_delete()
    DeleteLogicalSwitches.click_yes_delete_button()
    DeleteLogicalSwitches.wait_delete_logical_switch_dialog_close()
    #   verify Logical Switch Group is not existing after being deleted

    start = datetime.now()
    timeout = 60  #
    while (datetime.now() - start).total_seconds() < timeout:
        if CommonOperationLogicalSwitches.wait_logical_switch_status_not_found(ls_name, timeout=5, fail_if_false=False):
            logger.info("Logical Switch status is 'not found', successfully deleted '%s'." % ls_name)
            break
        elif VerifyLogicalSwitches.verify_logical_switch_should_not_exist(ls_name, timeout=5, fail_if_false=False):
            logger.info("Logical Switch '%s' is successfully deleted." % ls_name)
            break
    else:
        logger.warn("Logical Switch '%s' is NOT successfully deleted or timeout issue occurred." % ls_name)
        return False

    FusionUIBase.show_activity_sidebar()
    if FusionUIBase.wait_activity_action_ok(ls_name, 'Delete', timeout=30, fail_if_false=False) is False:
        return False
    FusionUIBase.show_activity_sidebar()

    return True


def delete_logical_switches(ls_obj):
    """ Delete Logical Switch by given LS list
        Usage:
            ${data} =       | Get Data By Xpath                         | //LogicalSwitches/Delete/ls
            ${result} =     | Fusion UI Delete Logical Switches         | @{data.ls}
            Should Be True  | ${result}                                 | msg=Failed to delete logical switches

        Test data example:
            1. data -> LogicalSwitches -> Delete, place your LS list like below

            <LogicalSwitches>
                <Delete>
                    <ls name="LS-CiscoNexus56xx" />
                    <ls name="LS-CiscoNexus600x" />
                </Delete>
            </LogicalSwitches>
    """
    navigate()
    logger.info("deleting Logical Switch '%s' ..." % [x.name for x in ls_obj])

    total = len(ls_obj)
    not_exists = 0
    deleted = 0

    for n, ls in enumerate(ls_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("deleting a Logical Switch named '%s'" % ls.name)
        if not VerifyLogicalSwitches.verify_logical_switch_should_exist(ls.name, fail_if_false=False):
            logger.warn("Logical Switch '%s' does not exist" % ls.name)
            not_exists += 1
        else:
            if delete_logical_switch_by_name(ls.name) is False:
                logger.warn("Logical Switch '%s' is NOT deleted successfully, or 'Delete' action is not found in right-side-bar list." % ls.name)
                continue
            else:
                deleted += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no Logical Switch to delete! all %s Logical Switch(es) is NOT existing, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if deleted < total:
            logger.warn("not all of the Logical Switch(es) is successfully deleted - %s out of %s deleted " % (deleted, total))
            if deleted + not_exists == total:
                logger.warn("%s not-existing Logical Switch(es) is skipped, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s not-existing Logical Switch(es) is skipped, %s Logical Switch(es) left is failed being deleted " % (not_exists, total - deleted - not_exists))
                return False

    logger.info("all of the Logical Switch(es) is successfully deleted - %s out of %s " % (deleted, total))
    return True


def edit_ls(*ls_obj):
    """
    !!! Deprecated !!!
        please DO NOT change/maintain this keyword anymore, instead using/improving the keyword
          "Fusion UI Edit Logical Switches"
    """
    """
        This function can modify attributes of already created LS in appliance. The list of the Logical Switch
        objects that should be modified should be in LS array with its attributes.
    """

    selenium2lib = ui_lib.get_s2l()

    if not selenium2lib._is_element_present(FusionLogicalSwitchPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(ls_obj, test_data.DataObj):
        ls_obj = [ls_obj]
    elif isinstance(ls_obj, tuple):
        ls_obj = list(ls_obj[0])

        IP_1 = ""
        IP_2 = ""
        error = 0

        switch_index1 = 0
        switch_index2 = 0
        switch_index = 0

    for ls in ls_obj:
        logger._log_to_console_and_log_file("\nEditing Logical Switch %s..." % ls.name)

        if(ls.name == ""):
            logger._warn("Mandatory field - name can't be empty")
            continue

        if ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_ELEMENT_SERVER_BASE % ls.name):
            logger._log_to_console_and_log_file("Valid Logical Switch %s" % ls.name)
        else:
            logger._warn("Not able to locate Logical switch %s" % ls.name)
            continue
        #
        # Collect associated switch information from LS
        #
        ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_MENU_ACTION_MAIN_BTN)
        ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_LS)

        if hasattr(ls, 'state'):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.ID_TEXT_LS_STATE % ls.state)

        IP_1 = ""
        IP_2 = ""
        error = 0

        switch_index1 = 0
        switch_index2 = 0
        switch_index = 0

        if ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_SWITCH1_SEARCH):
            IP_1 = ui_lib.get_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_SWITCH1_SEARCH)
            logging._log_to_console_and_log_file("First Switch IP is...")
            logging._log_to_console_and_log_file(IP_1)
            switch_index1 = 1

        if ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_SWITCH2_SEARCH):
            IP_2 = ui_lib.get_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_SWITCH2_SEARCH)
            logging._log_to_console_and_log_file("Second Switch IP is...")
            logging._log_to_console_and_log_file(IP_2)
            switch_index2 = 2

        switch_list = [(IP_1, switch_index1), (IP_2, switch_index2)]
        #
        # Continue with switch edit operation
        #
        if hasattr(ls, 'new_name'):
            ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_LS_NAME)
            logger._log_to_console_and_log_file("Typing host name/IP..")
            ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_LS_NAME, ls.new_name)

        for switch in ls.switch:
            logger._log_to_console_and_log_file("\nEditing Logical switch - %s..." % switch.name)
            logger._log_to_console_and_log_file("\nNexus switch ip is %s..." % switch.ip)

            # Get switch list from LS and index it for next action
            #
            if (switch_list[0][0] == switch.ip):
                switch_index = switch_list[0][1]
            elif (switch_list[1][0] == switch.ip):
                switch_index = switch_list[1][1]

            # Perform Remove Switch from LS
            #
            if (switch.remove_switch.lower() == "yes"):
                if (switch_index == 1):
                    ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_SWITCH1_SEARCH)
                    ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SWITCH1_REMOVE)
                    logging._log_to_console_and_log_file("Switch %s is removed from logcial switch" % switch.ip)

                elif (switch_index == 2):
                    ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_SWITCH2_SEARCH)
                    status = ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_SWITCH2_REMOVE)
                    logging._log_to_console_and_log_file("status %s " % status)
                    if (status is False):
                        logging._log_to_console_and_log_file("The Nexus switch %s can not be removed" % switch.ip)
                        # continue
                    else:
                        ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SWITCH2_REMOVE)
                        logging._log_to_console_and_log_file("Switch %s is removed " % switch.ip)

            # Perform edit switch
            #
            if (switch.edit_switch.lower() == "yes"):
                if (switch_index == 1):
                    ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SWITCH1_SETTING)
                    logging._log_to_console_and_log_file("Editing Switch1")
                    _fill_switch_data_edit(switch)

                if (switch_index == 2):
                    ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SWITCH2_SETTING)
                    logging._log_to_console_and_log_file("Editing Switch2")
                    _fill_switch_data_edit(switch)

            if (switch.add_switch.lower() == "yes"):
                if (not ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_LS_ADD_MAX_MSG)):

                    if (ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_ADD_SWITCH)):
                        ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_ADD_SWITCH)
                        ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_HOST_NAME)
                        logger._log_to_console_and_log_file("Typing host name/IP..")
                        ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_ADD_SWITCH_HOST, switch.switch_new_ip)

                        if (switch.use_same_credential.lower() == "no"):
                            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_USE_SAME_CREDENTIAL)
                            _fill_switch_data_add(switch)
                else:
                    logger._warn("LS Contains two switches, no more switch can be added..")
                    error = error + 1

            if (switch.add_switch.lower() == "yes" and error == 0):
                if (switch.use_same_credential.lower() == "yes"):
                    ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_ADD_SWITCH_1)
                if (switch.use_same_credential.lower() == "no"):
                    ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_ADD_SWITCH_2)
            else:
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_ADD_SWITCH_CANCEL)
            if (switch.edit_switch.lower() == "yes"):
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SWITCH_OK)

    if (error != 0):
        ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_CANCEL_MAIN)
        return False
    else:
        # Now wait for "Completed" since we have a progress bar
        #
        ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_OK_MAIN)
        ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.ID_CHECKBOX_CONFIRM)
        ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.ID_BUTTON_CONFIRM_OK)
        ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_LS_EDIT_PROGRESS_BAR, GeneralLogicalSwitchesElements.editLSTimeout)
        logger._log_to_console_and_log_file("Waiting for LS edit to complete..")
        if not ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_LS_UPDATE_COMPLETE, GeneralLogicalSwitchesElements.editLSTimeout):
            if ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_LS_EDIT_ERROR, GeneralLogicalSwitchesElements.editLSTimeout):
                logger._warn("Error while updating logical Switch %s " % ls.name)
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_LS_EDIT_PAGE_NOTIFICATION)
                status = ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_LS_EDIT_ERROR_MSG, GeneralLogicalSwitchesElements.editLSTimeout)
                selenium2lib.capture_page_screenshot()
                if (status is False):
                    logger._warn("Not able to capture error message, please check screenshot")
                else:
                    error_msg = ui_lib.get_text(FusionLogicalSwitchPage.CISCO_ID_LS_EDIT_ERROR_MSG)
                    logger._warn("Error message is")
                    logger._warn(error_msg)
                    selenium2lib.capture_page_screenshot()
                return False
            if ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_LS_EDIT_WARNING, GeneralLogicalSwitchesElements.editLSTimeout):
                error_msg = ui_lib.get_text(FusionLogicalSwitchPage.CISCO_ID_LS_EDIT_WARNING)
                logger._warn(error_msg)
                return True

    selenium2lib.capture_page_screenshot()

    return True


def ls_update_from_group(*ls_obj):
    """
        This function perform update from gorup in Logical Switch page.
    """
    selenium2lib = ui_lib.get_s2l()
    error = 0

    if not selenium2lib._is_element_present(FusionLogicalSwitchPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(ls_obj, test_data.DataObj):
        ls_obj = [ls_obj]
    elif isinstance(ls_obj, tuple):
        ls_obj = list(ls_obj[0])

    # Compare input LS objects with the one present in appliance. If it is not present, then
    # continue with the next LS object in the list
    #
    for ls in ls_obj:
        if(ls.name == ""):
            logger._warn("Mandatory field - name can't be empty")
            continue

        if ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_ELEMENT_SERVER_BASE % ls.name):
            logger._log_to_console_and_log_file("Valid Logical Switch %s" % ls.name)
        else:
            logger._warn("Not able to locate Logical switch %s" % ls.name)
            continue

        ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_ELEMENT_SERVER_BASE % ls.name)
        warning_msg = ui_lib.get_text(FusionLogicalSwitchPage.CISCO_ID_WARNING_MSG)
        logging._log_to_console_and_log_file("Warning Message is...")
        logging._log_to_console_and_log_file(warning_msg)
        if ('The logical switch is inconsistent with the logical switch group' in warning_msg) or (warning_msg == ""):
            if(warning_msg != ""):
                logging._log_to_console_and_log_file("Activity message before updating LS from group: " + warning_msg)
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_MENU_ACTION_MAIN_BTN)
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_LS_UPDATE)
                ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_UPDATE_FORM, PerfConstants.DEFAULT_SYNC_TIME)
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_UPDATE_CONFIRM)

                # Wait for update from group operation
                #
                logger._log_to_console_and_log_file("Waiting for LS update from group to complete..")
                ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_UPDATE_WRNING, PerfConstants.DEFAULT_SYNC_TIME)
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_UPDATE_WRNING)
                msg = ui_lib.get_text(FusionLogicalSwitchPage.CISCO_ID_UPDATE_WRNING_MSG)

                if ('Edit the logical switch and specify the address and credentials for all absent switches' in msg):
                    logging._log_to_console_and_log_file(msg)
                    logging._log_to_console_and_log_file("\n Please update Appropriate LS to make it consistent with LSG \n")
                    selenium2lib.capture_page_screenshot()
                    return True
                else:
                    return False
                selenium2lib.capture_page_screenshot()
    if error > 1:
        return False
    return True


def delete_ls(*ls_obj):
    """
    !!! Deprecated !!!
        please DO NOT change/maintain this keyword anymore, instead using/improving the keyword
          "Fusion UI Delete Logical Switches"
    """
    """
        This function deletes LS from appliance. The LS to be deleted should be in LS object
    """

    selenium2lib = ui_lib.get_s2l()
    error = 0

    if not selenium2lib._is_element_present(FusionLogicalSwitchPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(ls_obj, test_data.DataObj):
        ls_obj = [ls_obj]
    elif isinstance(ls_obj, tuple):
        ls_obj = list(ls_obj[0])

    for ls in ls_obj:
        if(ls.name == ""):
            logger._warn("Mandatory field - name can't be empty")
            continue

        if ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_ELEMENT_SERVER_BASE % ls.name):
            logger._log_to_console_and_log_file("Valid Logical Switch %s" % ls.name)
        else:
            logger._warn("Not able to locate Logical switch %s" % ls.name)
            continue

        ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_ELEMENT_SERVER_BASE % ls.name)
        ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_MENU_ACTION_MAIN_BTN)
        ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_DELETE_LS)
        ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_DELETE_LS_CONFIRM, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_DELETE_LS_CONFIRM)

        # Wait for delete operation to complete
        #
        if ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_PROGRESS_BAR, GeneralLogicalSwitchesElements.editLSTimeout):
            ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_PROGRESS_BAR, GeneralLogicalSwitchesElements.editLSTimeout)
            logger._log_to_console_and_log_file("Waiting for LS delete operation to complete..")
            wait_time = 60 * 2  # Delete operation takes mpre time to complete
            ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_LS_UPDATE_COMPLETE, wait_time)
            if not ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_ELEMENT_SERVER_BASE % ls.name):
                logger._log_to_console_and_log_file("Logical Switch deleted successfully..")
            selenium2lib.capture_page_screenshot()
        else:
            ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_DELETE_WARNING, GeneralLogicalSwitchesElements.editLSTimeout)
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_DELETE_WARNING)
            error_msg = ui_lib.get_text(FusionLogicalSwitchPage.CISCO_ID_DELETE_WARNING_MSG)
            selenium2lib.capture_page_screenshot()
            logger._warn(error_msg)
            error = error + 1

    if error > 0:
        logger._warn("Delete operation for one or more LS failed..")
        return False
    return True


def get_ls_attributes(*ls_obj):
    """
        This function returns following attributes

        - Switch type
        - Switch group
        - Switch state
        - Switch vPC domian id
        - Switch MAC id
        - Firmware version

        All of the above data will be returned along with status of the function as a tuple
    """

    selenium2lib = ui_lib.get_s2l()
    error = 0
    return_data = ""

    if not selenium2lib._is_element_present(FusionLogicalSwitchPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(ls_obj, test_data.DataObj):
        ls_obj = [ls_obj]
    elif isinstance(ls_obj, tuple):
        ls_obj = list(ls_obj[0])

    for ls in ls_obj:
        if(ls.name == ""):
            logger._warn("Mandatory field - name can't be empty")
            continue

        if ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_ELEMENT_SERVER_BASE % ls.name):
            logger._log_to_console_and_log_file("Valid Logical Switch %s" % ls.name)
        else:
            logger._warn("Not able to locate Logical switch %s" % ls.name)
            continue

        ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_ELEMENT_SERVER_BASE % ls.name)
        logger._log_to_console_and_log_file("-----------------------------------------------------")
        logger._log_to_console_and_log_file("Logical Switch Details")
        logger._log_to_console_and_log_file("-----------------------------------------------------")
        ls_type = str(ui_lib.get_text(FusionLogicalSwitchPage.CISCO_ID_LS_TYPE))
        logger._log_to_console_and_log_file("Switch type is             - %s" % ls_type)
        ls_group = str(ui_lib.get_text(FusionLogicalSwitchPage.CISCO_ID_LS_LS_GROUP))
        logger._log_to_console_and_log_file("Switch group is            - %s" % ls_group)
        ls_state = ui_lib.get_text(FusionLogicalSwitchPage.CISCO_ID_LS_STATE)
        logger._log_to_console_and_log_file("Logical Switch state is    - %s" % ls_state)
        ls_domain = str(ui_lib.get_text(FusionLogicalSwitchPage.CISCO_ID_LS_VPC_DMAIN_ID))
        logger._log_to_console_and_log_file("Logical Switch domain is   - %s" % ls_domain)
        ls_mac = str(ui_lib.get_text(FusionLogicalSwitchPage.CISCO_ID_LS_VPC_PRIMARY_MAC_ID))
        logger._log_to_console_and_log_file("Switch MAC/SN is           - %s" % ls_mac)

        s_data1 = []
        s_data2 = []
        ip1 = ""
        ip2 = ""

        if ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_LS_SWITCH_1):
            ls_switch_data_1 = ui_lib.get_text(FusionLogicalSwitchPage.CISCO_ID_LS_SWITCH_1)
            s_data1 = ls_switch_data_1.split()
            for index, item in enumerate(s_data1):
                s_data1[index] = str(s_data1[index])
            ip1 = s_data1[0]

        if ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_LS_SWITCH_2):
            ls_switch_data_2 = ui_lib.get_text(FusionLogicalSwitchPage.CISCO_ID_LS_SWITCH_2)
            s_data2 = ls_switch_data_2.split()
            for index, item in enumerate(s_data2):
                s_data2[index] = str(s_data2[index])
            ip2 = s_data2[0]

        vpc_data1 = []
        vpc_data2 = []
        if ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_VPC_1):
            ls_switch_data_1 = ui_lib.get_text(FusionLogicalSwitchPage.CISCO_ID_VPC_1)
            vpc_data1 = ls_switch_data_1.split()
            for index, item in enumerate(vpc_data1):
                vpc_data1[index] = str(vpc_data1[index])

        if ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_VPC_2):
            ls_switch_data_1 = ui_lib.get_text(FusionLogicalSwitchPage.CISCO_ID_VPC_2)
            vpc_data2 = ls_switch_data_1.split()
            for index, item in enumerate(vpc_data2):
                vpc_data2[index] = str(vpc_data2[index])

        ls_switch_data = ui_lib.get_text(FusionLogicalSwitchPage.CISCO_ID_LS_SWITCH)

        data = ls_switch_data.split()
        logger._log_to_console_and_log_file("-----------------------------------------------------")
        logger._log_to_console_and_log_file("Switches Details")
        logger._log_to_console_and_log_file("-----------------------------------------------------")
        logger._log_to_console_and_log_file("Switch IP        - %s " % data[0])
        logger._log_to_console_and_log_file("vPC Member ID    - %s " % data[1])
        logger._log_to_console_and_log_file("vPC Role         - %s " % data[2])
        logger._log_to_console_and_log_file("Switch State     - %s " % data[3])
        logger._log_to_console_and_log_file("Switch Model     - %s " % data[4])
        logger._log_to_console_and_log_file("Switch Firmware  - %s " % data[5])
        logger._log_to_console_and_log_file("-----------------------------------------------------")
        #
        # Return all data collected in a list
        #
        return_data = [ls_type, ls_group, ls_state, ls_domain, ls_mac] + [s_data1] + [s_data2] + [vpc_data1] + [vpc_data2]

        ui_swdict = {"vPC domain ID": [], "vPC primary MAC address": [], "Switch1": [], "vPC Member ID1": [],
                     "vPC Role1": [], "State1": [], "Model1": [], "Firmware1": [],
                     "Switch2": [], "vPC Member ID2": [],
                     "vPC Role2": [], "State2": [], "Model2": [], "Firmware2": []}

        nexus_swdict = {"vPC domain ID": [], "vPC primary MAC address": [], "Switch1": [], "vPC Member ID1": [],
                        "vPC Role1": [], "State1": [], "Model1": [], "Firmware1": [],
                        "Switch2": [], "vPC Member ID2": [],
                        "vPC Role2": [], "State2": [], "Model2": [], "Firmware2": []}

        ui_swdict["vPC domain ID"] = ls_domain
        ui_swdict["vPC primary MAC address"] = ls_mac

        if len(ip1) > 2:
            logger._log_to_console_and_log_file("ip1 - %s" % ip1)
            ui_swdict["Switch1"] = s_data1[0]
            ui_swdict["vPC Member ID1"] = s_data1[1]
            ui_swdict["vPC Role1"] = s_data1[2]
            ui_swdict["State1"] = s_data1[3]
            ui_swdict["Model1"] = s_data1[4]
            ui_swdict["Firmware1"] = s_data1[5]

        if len(ip2) > 2:
            logger._log_to_console_and_log_file("ip2 - %s" % ip2)
            ui_swdict["Switch2"] = s_data2[0]
            ui_swdict["vPC Member ID2"] = s_data2[1]
            ui_swdict["vPC Role2"] = s_data2[2]
            ui_swdict["State1"] = s_data2[3]
            ui_swdict["Model2"] = s_data2[4]
            ui_swdict["Firmware2"] = s_data2[5]

        if ui_swdict["vPC Role1"] is "Primary":
            primary_ip = ui_swdict["Switch1"]
        elif ui_swdict["vPC Role2"] is "Primary":
            primary_ip = ui_swdict["Switch2"]
        else:
            logger._warn("Looks like it is single switch LS with no VPC setup")
            primary_ip = ip1

        for switch in ls.switch:
            if switch.ip == primary_ip:
                user_name = switch.username
                password = switch.password

        if len(ip1) > 2 and len(ip2) > 2:
            data = _get_switch_data(primary_ip, user_name, password, "show interface mgmt0")
            m = re.search("Hardware: GigabitEthernet, address.*: .*", data)
            mac = m.group()
            if mac:
                mac1 = mac.split()[3]  # Get data from vPC system-mac attribute
                sys_mac = mac1[0:2] + ":" + mac1[2:4] + ":" + mac1[5:7] + ":" + mac1[7:9] + ":" + mac1[10:12] + ":" + mac1[12:14]
                nexus_swdict["vPC primary MAC address"] = sys_mac

        data = _get_switch_data(primary_ip, user_name, password, "show vpc brief")
        domainid = re.search("vPC domain id.*: .*", data)
        id = domainid.group()
        if id:
            domain_id = id.split()[4]
            if domain_id == "Not":
                logging._log_to_console_and_log_file("vPC Domain ID is not set")
            else:
                nexus_swdict["vPC domain ID"] = domain_id

        # The "datafilepath" is should be defined as attribute in data abject and it
        # should havepath/folder of file(Should exclude file name)
        # This file contains switch information that will be used as bench mark while comparing with
        # data collected from OneView

        file_path = ls.datafilepath

        # For Switch1
        #
        if len(ip1) > 2:
            file_name = ip1 + ".txt"
            nexus_swdict["Switch1"] = ip1
            with open(file_path + file_name) as fh:
                lines = fh.read().splitlines()
                lines = lines[1:7]
                for line in lines:
                    key, val = line.split(":")
                    if key == "State":
                        nexus_swdict["State1"] = val
                    if key == "Firmware":
                        nexus_swdict["Firmware1"] = val
                    if key == "vPC member ID":
                        nexus_swdict["vPC Member ID1"] = val
                    if key == "vPC role":
                        nexus_swdict["vPC Role1"] = val
                    if key == "Model":
                        nexus_swdict["Model1"] = val

        # Switch 2
        #
        if len(ip2) > 2:
            file_name = ip2 + ".txt"
            nexus_swdict["Switch2"] = ip2
            with open(file_path + file_name) as fh:
                lines = fh.read().splitlines()
                lines = lines[1:7]
                for line in lines:
                    key, val = line.split(":")
                    if key == "State":
                        nexus_swdict["State2"] = val
                    if key == "Firmware":
                        nexus_swdict["Firmware2"] = val
                    if key == "vPC member ID":
                        nexus_swdict["vPC Member ID2"] = val
                    if key == "vPC role":
                        nexus_swdict["vPC Role2"] = val
                    if key == "Model":
                        nexus_swdict["Model2"] = val

        printline = "\n------------------------------------------------------------------"
        logger._log_to_console_and_log_file("Below parameters are not matching with nexus switch")
        for key in ui_swdict:
            if key in nexus_swdict:
                if (ui_swdict[key] != nexus_swdict[key]):
                    logger._log_to_console_and_log_file(printline)
                    logger._warn("Following paramters are not matching with nexus switch")
                    logger._warn("Switch parameter    - %s and value - %s" % (key, nexus_swdict[key]))
                    logger._warn("Appliance parameter - %s and value - %s" % (key, ui_swdict[key]))
                else:
                    logger._log_to_console_and_log_file(printline)
                    logger._log_to_console_and_log_file("\nPassed: Switch and Appliance parameter %s is matching " % key)
                    logger._log_to_console_and_log_file(printline)

    if error > 0:
        return False, return_data
    return True, return_data


def check_privi_ls(*ls_obj):
    """
        This function checks the capabilities of different user
    """
    selenium2lib = ui_lib.get_s2l()

    if isinstance(ls_obj, test_data.DataObj):
        ls_obj = [ls_obj]
    elif isinstance(ls_obj, tuple):
        ls_obj = list(ls_obj[0])

    error = 0
    message = ""
    #
    # Check session user name
    #
    ui_lib.wait_for_element_and_click(FusionUserandGroupsPage.ID_SESSION_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
    current_user = ui_lib.get_text(FusionUserandGroupsPage.ID_CURRENT_SESSION_USER)

    logger._log_to_console_and_log_file("User - %s" % current_user)

    if (current_user == "Administrator"):
        if not selenium2lib._is_element_present(FusionLogicalSwitchPage.ID_PAGE_LABEL):

            ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_element(FusionUIBaseElements.ID_MENU_LINK_DASHBOARD, PerfConstants.DEFAULT_SYNC_TIME)

            status = ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_MENU_LINK_LS, PerfConstants.DEFAULT_SYNC_TIME)

            if (status is False):
                message = "Administrator do not have permission to access LS"
                error = error + 1
                logger._warn("Failed - Administrator do not have permission to access LS")
            else:
                message = "networkadmin have permission to access Logical Switch"
                logger._log_to_console_and_log_file("Passed - Administrator have permission to access Logical Switch")

            for ls in ls_obj:
                logger._log_to_console_and_log_file("\nChecking permission for Logical Switch -  %s..." % ls.name)

                if(ls.name == ""):
                    logger._warn("Mandatory field - name can't be empty")
                    continue

                if ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_ELEMENT_SERVER_BASE % ls.name):
                    logger._log_to_console_and_log_file("Selecting Logical Switch - %s" % ls.name)
                else:
                    logger._log_to_console_and_log_file("Not able to locate Logical switch %s" % ls.name)
                    continue

                if not ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_LINK_CREATE_LS):
                    logger._warn("Failed - Create privilage is not granted for user")
                    error = error + 1
                else:
                    logger._log_to_console_and_log_file("Passed - Create privilage is enabled for user")

                if not ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_MENU_ACTION_MAIN_BTN):
                    logger._warn("Failed - Acttion Button is not visible for this user")
                    error = error + 1
                else:
                    logger._log_to_console_and_log_file("Passed - Acttion Button is visible for this user")

                if not ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_LS):
                    logger._warn("Failed - Edit Button is not visible for this user")
                    error = error + 1
                else:
                    logger._log_to_console_and_log_file("Passed - Edit Button is visible for this user")

                if not ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_DELETE_LS):
                    logger._warn("Failed - Delete Button is not visible for this user")
                    error = error + 1
                else:
                    logger._log_to_console_and_log_file("Passed - Edit Button is visible for this user")

                if not ui_lib.wait_for_element_visible("link=Create"):
                    logger._warn("Failed - Create Button in Action list is not visible for this user")
                    error = error + 1
                else:
                    logger._log_to_console_and_log_file("Passed - Create Button in Action list is visible for this user")

    if (current_user == "backupadmin"):
        if not selenium2lib._is_element_present(FusionLogicalSwitchPage.ID_PAGE_LABEL):

            ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_element(FusionUIBaseElements.ID_MENU_LINK_DASHBOARD, PerfConstants.DEFAULT_SYNC_TIME)

            status = ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_MENU_LINK_LS, PerfConstants.DEFAULT_SYNC_TIME)
            if (status is False):
                message = "backupadmin do not have permission to access Logical Switch"
                error = error + 1
                logger._warn("Failed - backupadmin do not have permission to access Logical Switch")

            else:
                message = "backupadmin have permission to access Logical Switch"
                logger._log_to_console_and_log_file("Passed - backupadmin have permission to access Logical Switch")

            for ls in ls_obj:
                logger._log_to_console_and_log_file("\nChecking permission for Logical Switch -  %s..." % ls.name)

                if(ls.name == ""):
                    logger._warn("Mandatory field - name can't be empty")
                    continue

                if ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_ELEMENT_SERVER_BASE % ls.name):
                    logger._log_to_console_and_log_file("Selecting Logical Switch - %s" % ls.name)
                else:
                    logger._log_to_console_and_log_file("Not able to locate Logical switch %s" % ls.name)
                    continue

                if not ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_LINK_CREATE_LS):
                    logger._log_to_console_and_log_file("Passed - Create privilage is not granted for user")
                    error = error + 1
                else:
                    logger._warn("Failed - Create privilage is enabled for user")

                if not ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_MENU_ACTION_MAIN_BTN):
                    logger._log_to_console_and_log_file("Passed - Acttion Button is not visible for this user")
                    error = error + 1
                else:
                    logger._warn("Failed - Acttion Button is visible for this user")

    if (current_user == "networkadmin"):
        if not selenium2lib._is_element_present(FusionLogicalSwitchPage.ID_PAGE_LABEL):

            ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_element(FusionUIBaseElements.ID_MENU_LINK_DASHBOARD, PerfConstants.DEFAULT_SYNC_TIME)

            status = ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_MENU_LINK_LS, PerfConstants.DEFAULT_SYNC_TIME)

            if (status is False):
                message = "networkadmin do not have permission to access Logical Switch"
                error = error + 1
                logger._warn("Failed - networkadmin do not have permission to access Logical Switch")

            else:
                message = "networkadmin have permission to access Logical Switch"
                logger._log_to_console_and_log_file("Passed - networkadmin have permission to access Logical Switch")

            for ls in ls_obj:
                logger._log_to_console_and_log_file("\nChecking permission for Logical Switch -  %s..." % ls.name)

                if(ls.name == ""):
                    logger._warn("Mandatory field - name can't be empty")
                    continue

                if ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_ELEMENT_SERVER_BASE % ls.name):
                    logger._log_to_console_and_log_file("Selecting Logical Switch - %s" % ls.name)
                else:
                    logger._log_to_console_and_log_file("Not able to locate Logical switch %s" % ls.name)
                    continue

                if not ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_LINK_CREATE_LS):
                    logger._warn("Failed - Create privilage is not granted for user")
                    error = error + 1
                else:
                    logger._log_to_console_and_log_file("Passed - Create privilage is enabled for user")

                if not ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_MENU_ACTION_MAIN_BTN):
                    logger._warn("Failed - Acttion Button is not visible for this user")
                    error = error + 1
                else:
                    logger._log_to_console_and_log_file("Passed - Acttion Button is visible for this user")

                if not ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_LS):
                    logger._warn("Failed - Edit Button is not visible for this user")
                    error = error + 1
                else:
                    logger._log_to_console_and_log_file("Passed - Edit Button is visible for this user")

                if not ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_DELETE_LS):
                    logger._warn("Failed - Delete Button is not visible for this user")
                    error = error + 1
                else:
                    logger._log_to_console_and_log_file("Passed - Edit Button is visible for this user")

                if not ui_lib.wait_for_element_visible("link=Create"):
                    logger._warn("Failed - Create Button in Action list is not visible for this user")
                    error = error + 1
                else:
                    logger._log_to_console_and_log_file("Passed - Create Button in Action list is visible for this user")

    if error > 0:
        return False
    return True


def _fill_switch_data_add(ls):
    """
    Function defnination to fill Nexus switch data

    """
    # Generic code to modify switch parameters
    #
    selenium2lib = ui_lib.get_s2l()

    ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_HOST_NAME)
    logger._log_to_console_and_log_file("Typing host name/IP..")
    ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_HOST_NAME, ls.switch_new_ip)

    ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_ADD_SSH_USER)
    logger._log_to_console_and_log_file("Typing SSH User..")
    ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_ADD_SSH_USER, ls.ssh_new_user_name)

    ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_ADD_SSH_PASSWORD)
    logger._log_to_console_and_log_file("Typing snmp password..")
    ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_ADD_SSH_PASSWORD, ls.ssh_new_password)

    ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNM_PORT)
    logger._log_to_console_and_log_file("Typing snmp port..")
    ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNM_PORT, ls.snmp_port)

    ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNM_STRING)
    logger._log_to_console_and_log_file("Typing snmp community string..")
    ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNM_STRING, ls.snmp_string)

    # Fill the switch1 SNMP details
    # Before selecting SNMP version, fill the port used for SNMP
    #
    ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNM_PORT, ls.snmp_port)
    logger._log_to_console_and_log_file("Switch SNMP version is %s" % ls.snmp_version)

    if (ls.snmp_version == "v1/v2c"):
        ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNM_STRING, ls.snmp_string)

        if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_VERSION_DROPDOWN)):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_VERSION_DROPDOWN)
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_VERSION_DROPDOWN_SELECT % ls.snmp_version)
            logger._log_to_console_and_log_file("SNMP %s is selected" % ls.snmp_version)

    # If SNMP version is v3 then fill security,authorization and privacy details
    #
    if (ls.snmp_version == "v3"):
        logger._log_to_console_and_log_file("SNMP version-1 '%s' is selected" % ls.snmp_version)
        if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_VERSION_DROPDOWN)):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_VERSION_DROPDOWN)
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_VERSION_DROPDOWN_SELECT % ls.snmp_version)
            logger._log_to_console_and_log_file("SNMP version-2 '%s' is selected" % ls.snmp_version)

            # If SNMP version is v3, then fill, username instead of community string
            ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_V3_USER_NAME, ls.v3_user_name)
            logger._log_to_console_and_log_file("SNMP security level is '%s' " % ls.v3_user_name)

        if (ls.security == "None"):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_SECURITY_NONE)
            logger._log_to_console_and_log_file("SNMP V3 None-Authorization selected..")

        if (ls.security == "Authorization"):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION)

            if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PROTO_DROPDOWN)):
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PROTO_DROPDOWN)
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PROTO_DROPDOWN_SELECT % ls.auth_proto)
                logger._log_to_console_and_log_file("Authorization Protocol %s is selected" % ls.auth_proto)

            if (ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PASSWORD)):
                logger._log_to_console_and_log_file("Typing Authorization password..")
                ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PASSWORD, ls.auth_pasword)

        if (ls.security == "Authorization and privacy"):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PRIV)

            if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PROTO_DROPDOWN)):
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PROTO_DROPDOWN)
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PROTO_DROPDOWN_SELECT % ls.auth_proto)
                logger._log_to_console_and_log_file("Authorization Protocol %s is selected" % ls.auth_proto)

            if (ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PASSWORD)):
                logger._log_to_console_and_log_file("Typing Authorization password..")
                ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PASSWORD, ls.auth_pasword)

            if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PRIV_PROTO_DROPDOWN)):
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PRIV_PROTO_DROPDOWN)
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PRIV_PROTO_DROPDOWN_SELECT % ls.privacy_proto)
                logger._log_to_console_and_log_file("Authorization Protocol %s is selected" % ls.auth_proto)

            if (ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PRIV_PASSWORD)):
                logger._log_to_console_and_log_file("Typing Authorization Privacy password..")
                ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PRIV_PASSWORD, ls.auth_priv_pasword)

    return True


def _fill_switch_data_edit(ls):
    """
    Function defination to fill Nexus switch data

    """
    # Generic code to modify switch parameters
    #
    selenium2lib = ui_lib.get_s2l()

    ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_HOST_NAME)
    logger._log_to_console_and_log_file("Typing host name/IP..")
    ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_HOST_NAME, ls.switch_new_ip)

    ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_SSH_USER)
    logger._log_to_console_and_log_file("Typing SSH User..")
    ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_SSH_USER, ls.ssh_new_user_name)

    ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_SSH_PASSWORD)
    logger._log_to_console_and_log_file("Typing snmp password..")
    ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_SSH_PASSWORD, ls.ssh_new_password)

    # Fill the switch SNMP details
    # Before selecting SNMP version, fill the port used for SNMP
    #
    ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNM_PORT)
    logger._log_to_console_and_log_file("Typing snmp port..")
    ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNM_PORT, ls.snmp_new_port)

    if (ls.snmp_version == "v1/v2c"):
        if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_VERSION_DROPDOWN)):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_VERSION_DROPDOWN)
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_VERSION_DROPDOWN_SELECT % ls.snmp_version)
            logger._log_to_console_and_log_file("SNMP %s is selected" % ls.snmp_version)

        ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNM_STRING)
        logger._log_to_console_and_log_file("Typing snmp community string..")
        ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNM_STRING, ls.snmp_new_string)

    # If SNMP version is v3 then fill security,authorization and privacy details
    #

    if (ls.snmp_version == "v3"):
        if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_VERSION_DROPDOWN)):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_VERSION_DROPDOWN)
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_VERSION_DROPDOWN_SELECT % ls.snmp_version)
            logger._log_to_console_and_log_file("SNMP version '%s' is selected" % ls.snmp_version)

            # If SNMP version is v3, then fill, username instead of community string
            ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_V3_USER_NAME, ls.v3_user_name)
            logger._log_to_console_and_log_file("SNMP security level is '%s' " % ls.v3_user_name)

        if (ls.security == "None"):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_SECURITY_NONE)
            logger._log_to_console_and_log_file("SNMP V3 None-Authorization selected..")

        if (ls.security == "Authorization"):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION)

            if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PROTO_DROPDOWN)):
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PROTO_DROPDOWN)
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PROTO_DROPDOWN_SELECT % ls.auth_proto)
                logger._log_to_console_and_log_file("Authorization Protocol %s is selected" % ls.auth_proto)

            if (ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PASSWORD)):
                logger._log_to_console_and_log_file("Typing Authorization password..")
                ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PASSWORD, ls.auth_pasword)

        if (ls.security == "Authorization and privacy"):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PRIV)

            if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PROTO_DROPDOWN)):
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PROTO_DROPDOWN)
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PROTO_DROPDOWN_SELECT % ls.auth_proto)
                logger._log_to_console_and_log_file("Authorization Protocol %s is selected" % ls.auth_proto)

            if (ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PASSWORD)):
                logger._log_to_console_and_log_file("Typing Authorization password..")
                ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PASSWORD, ls.auth_pasword)

            if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PRIV_PROTO_DROPDOWN)):
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PRIV_PROTO_DROPDOWN)
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PRIV_PROTO_DROPDOWN_SELECT % ls.privacy_proto)
                logger._log_to_console_and_log_file("Authorization Privacy Protocol %s is selected" % ls.privacy_proto)

            if (ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PRIV_PASSWORD)):
                logger._log_to_console_and_log_file("Typing Authorization Privacy password..")
                ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_EDIT_SNMP_AUTHORIZATION_PRIV_PASSWORD, ls.auth_priv_pasword)

    return True


def create_ls(*ls_obj):
    """
    !!! Deprecated !!!
        please DO NOT change/maintain this keyword anymore, instead using/improving the keyword
          "Fusion UI Create Logical Switches" which is create_logical_switches() in this file.
    """
    """
        This fucntion creates Logical Switch on applinace with the name
        and attributes passed in as arguments

    """

    selenium2lib = ui_lib.get_s2l()
    error = 0

    if not selenium2lib._is_element_present(FusionLogicalSwitchPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(ls_obj, test_data.DataObj):
        ls_obj = [ls_obj]
    elif isinstance(ls_obj, tuple):
        ls_obj = list(ls_obj[0])

    # Go in loop to create all LS objects in ls list
    #
    for ls in ls_obj:
        logger._log_to_console_and_log_file("\nCreating Logical Switch-  %s..." % ls.name)

        if(ls.name == "" or ls.switchgroup == ""):
            logger._warn("Mandatory fields for adding LS can't be empty")
            continue

        ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_LINK_CREATE_LS)

        if ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_NO_LSG_MSG):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_NO_LSG_CANCEL)
            ui_lib.fail_test("There is no LSG to create LS. Create LSG first")
            return False

        ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_INPUT_LS_NAME)
        logger._log_to_console_and_log_file("Typing lsg name..")
        ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_INPUT_LS_NAME, ls.name)

        # select operational state for LS
        if hasattr(ls, 'state'):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.ID_TEXT_LS_STATE % ls.state)
        # Select required LSG in the dropdown list. If the required LSG is not present, then fail
        #
        ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_LSG_DROPDOWN)
        if(selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_LINK_SEARCH_FOR_ANOTHER)):
            logger._log_to_console_and_log_file("Clicking search another..")
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_LINK_SEARCH_FOR_ANOTHER)

        if ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_ELEMENT_LSG_NAME % ls.switchgroup):
            logger._log_to_console_and_log_file("Selected valid LSG %s" % ls.switchgroup)
        else:
            logger._warn("Specified LSG is not present")
            return False

        switch_count = 1
        #
        # Enter switch1 credential
        #
        for switch in ls.switch:
            logger._log_to_console_and_log_file("\nNexus Switch ip  %s..." % switch.ip)
            if (switch_count == 1):
                ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_LS_SWITCH_IP_1, switch.ip)
                logger._log_to_console_and_log_file("Entering Nexus switch1 credentials")
                _fill_switch_data_create_switch1(switch)

            # Enter switch2 SSH credential
            #
            if (switch_count == 2):  # and (lsg.switch_count == 2)):
                ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_LS_SWITCH_IP_2, switch.ip)
                #
                # Uncheck the check box, if the switch2 credential is not same
                #
                if (switch.use_same_credential.lower() == "no"):
                    ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_LS_SWITCH_IP_SELECT, switch.use_same_credential)
                    logger._log_to_console_and_log_file("Entering Nexus switch2 credentials")
                    _fill_switch_data_create_switch2(switch)

            if (ls.switch_count == "2"):
                switch_count = switch_count + 1
            else:
                switch_count = 0

        if (error > 0):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_CREATE_LS_CANCEL)
        else:
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_CREATE_LS)

        if ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_PROGRESS_BAR, GeneralLogicalSwitchesElements.editLSTimeout):
            logger._log_to_console_and_log_file("Waiting for switch claim operation to complete")
            ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_LS_UPDATE_COMPLETE, GeneralLogicalSwitchesElements.editLSTimeout)
            selenium2lib.capture_page_screenshot()
            return True
        else:
            if ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_ERROR_MSG, GeneralLogicalSwitchesElements.editLSTimeout):
                error_msg = ui_lib.get_text(FusionLogicalSwitchPage.CISCO_ID_ERROR_MSG)
                selenium2lib.capture_page_screenshot()
                logger._warn(error_msg)
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_CREATE_LS_CANCEL)
            else:
                ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_WARNING, GeneralLogicalSwitchesElements.editLSTimeout)
                error_msg = ui_lib.get_text(FusionLogicalSwitchPage.CISCO_ID_WARNING)
                logger._warn(error_msg)
            return False  # Return for both if and else part

    #
    # Return to FOR loop if still there are more LS in list
    #

    return True


def _fill_switch_data_create_switch1(switch):
    """
    This will update Nexus switch SSH and SNMP credentials
    """
    selenium2lib = ui_lib.get_s2l()

    # Enter switch1 SSH credential
    ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_INPUT_SSH_USER_NAME_1, switch.username)
    ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_INPUT_SSH_PASSWORD_1, switch.password)

    # Fill the switch1 SNMP details
    # Before selecting SNMP version, fill the port used for SNMP communication
    #
    ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_INPUT_SNMP_PORT_1, switch.snmp_port)
    logger._log_to_console_and_log_file("Switch SNMP version is %s" % switch.snmp_version)

    # If SNMP version is 1/v2c then fill community string details
    #
    if (switch.snmp_version == "v1/v2c"):
        ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_INPUT_SNMP_STRING_1, switch.snmp_string)

        if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_SNMP_VERSION_DROPDOWN_1)):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_VERSION_DROPDOWN_1)
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_VERSION_DROPDOWN_SELECT_1 % switch.snmp_version)
            logger._log_to_console_and_log_file("SNMP version %s is selected" % switch.snmp_version)
            return True

    # If SNMP version is v3 then fill security,authorization and privacy details
    #
    logger._log_to_console_and_log_file("SNMP %s is selected" % switch.snmp_version)
    if (switch.snmp_version == "v3"):
        if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_SNMP_VERSION_DROPDOWN_1)):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_VERSION_DROPDOWN_1)
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_VERSION_DROPDOWN_SELECT_1 % switch.snmp_version)
            logger._log_to_console_and_log_file("SNMP version '%s' is selected" % switch.snmp_version)

            # If SNMP version is v3, then fill, username instead of community string
            # This also works for SNMP security "None"
            ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_SNMP_V3_USER_NAME_1, switch.v3_user_name)
            logger._log_to_console_and_log_file("SNMP security level is '%s' " % switch.v3_user_name)

        if (switch.security == "Authorization"):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_1)

            if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PROTO_DROPDOWN_1)):
                logger._log_to_console_and_log_file("Selecting Authorization protocol..%s" % switch.auth_proto)
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PROTO_DROPDOWN_1)
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PROTO_DROPDOWN_SELECT_1 % switch.auth_proto)

            if (ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PASSWORD_1)):
                logger._log_to_console_and_log_file("Typing Authorization password..")
                ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PASSWORD_1, switch.auth_pasword)

        if (switch.security == "Authorization and privacy"):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PRIV_1)

            if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PROTO_DROPDOWN_1)):
                logger._log_to_console_and_log_file("Selecting Authorization protocol..%s" % switch.auth_proto)
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PROTO_DROPDOWN_1)
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PROTO_DROPDOWN_SELECT_1 % switch.auth_proto)

            if (ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PASSWORD_1)):
                logger._log_to_console_and_log_file("Typing Authorization password..")
                ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PASSWORD_1, switch.auth_pasword)

            if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PRIV_PROTO_DROPDOWN_1)):
                logger._log_to_console_and_log_file("Selecting Privacy protocol..")
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PRIV_PROTO_DROPDOWN_1)
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PRIV_PROTO_DROPDOWN_SELECT_1 % switch.privacy_proto)

            if (ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PRIV_PASSWORD_1)):
                logger._log_to_console_and_log_file("Typing Authorization privacy password..")
                ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PRIV_PASSWORD_1, switch.auth_priv_pasword)
    return True


def _fill_switch_data_create_switch2(lsg):
    """
    This will update Nexus switch credentials SSH, SNMP.
    """

    selenium2lib = ui_lib.get_s2l()

    # Enter switch1 SSH credential
    #
    if(lsg.username == ""):
        logger._warn("Mandatory fields of switch connection can't be empty")
    else:
        ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_INPUT_SSH_USER_NAME_2, lsg.username)
        ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_INPUT_SSH_PASSWORD_2, lsg.password)

    # Fill the switch1 SNMP details
    # Before selecting SNMP version, fill the port used for SNMP communication
    #
    ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_INPUT_SNMP_PORT_2, lsg.snmp_port)
    logger._log_to_console_and_log_file("Switch-2 SNMP version is %s" % lsg.snmp_version)

    if (lsg.snmp_version == "v1/v2c"):
        ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_INPUT_SNMP_STRING_2, lsg.snmp_string)

        if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_SNMP_VERSION_DROPDOWN_2)):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_VERSION_DROPDOWN_2)
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_VERSION_DROPDOWN_SELECT_2 % lsg.snmp_version)
            logger._log_to_console_and_log_file("SNMP version %s is selected" % lsg.snmp_version)
            return True

    # If SNMP version is v3 then fill security,authorization and privacy details
    #

    if (lsg.snmp_version == "v3"):
        if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_SNMP_VERSION_DROPDOWN_2)):
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_VERSION_DROPDOWN_2)
            ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_VERSION_DROPDOWN_SELECT_2 % lsg.snmp_version)
            logger._log_to_console_and_log_file("SNMP version '%s' is selected" % lsg.snmp_version)

            # If SNMP version is v3, then fill, username instead of community string
            # This also works for SNMP security "None"
            #
            ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_SNMP_V3_USER_NAME_2, lsg.v3_user_name)
            logger._log_to_console_and_log_file("SNMP security level is '%s' " % lsg.v3_user_name)

            if (lsg.security == "Authorization"):
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_2)

                if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PROTO_DROPDOWN_2)):
                    logger._log_to_console_and_log_file("Selecting Authorization protocol..%s" % lsg.auth_proto)
                    ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PROTO_DROPDOWN_2)
                    ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PROTO_DROPDOWN_SELECT_2 % lsg.auth_proto)

                if (ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PASSWORD_2)):
                    logger._log_to_console_and_log_file("Typing Authorization password..")
                    ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PASSWORD_2, lsg.auth_pasword)

            if (lsg.security == "Authorization and privacy"):
                ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PRIV_2)

                if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PROTO_DROPDOWN_2)):
                    logger._log_to_console_and_log_file("Selecting Authorization protocol..%s" % lsg.auth_proto)
                    ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PROTO_DROPDOWN_2)
                    ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PROTO_DROPDOWN_SELECT_2 % lsg.auth_proto)

                if (ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PASSWORD_2)):
                    logger._log_to_console_and_log_file("Typing Authorization password..")
                    ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PASSWORD_2, lsg.auth_pasword)

                if (selenium2lib._is_element_present(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PRIV_PROTO_DROPDOWN_2)):
                    logger._log_to_console_and_log_file("Selecting Privacy protocol..")
                    ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PRIV_PROTO_DROPDOWN_2)
                    ui_lib.wait_for_element_and_click(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PRIV_PROTO_DROPDOWN_SELECT_2 % lsg.privacy_proto)

                if (ui_lib.wait_for_element_visible(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PRIV_PASSWORD_2)):
                    logger._log_to_console_and_log_file("Typing Authorization Privacy password..")
                    ui_lib.wait_for_element_and_input_text(FusionLogicalSwitchPage.CISCO_ID_SNMP_AUTHORIZATION_PRIV_PASSWORD_2, lsg.auth_priv_pasword)

    return True


def switch_ssh(*server_obj):
    """
    This function executes given command on Nexus Switch
    The argument should have all commands separated with ','
    And the commands should be insequence
    """

    if isinstance(server_obj, test_data.DataObj):
        server_obj = [server_obj]
    elif isinstance(server_obj, tuple):
        server_obj = list(server_obj[0])

    for server in server_obj:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        hostname = server.ip
        port = 22  # SSH Port to establish connection
        client.connect(server.ip, port=port, username=server.uname, password=server.pw)
        channel = client.invoke_shell()
        stdin = channel.makefile('wb')
        stdout = channel.makefile('rb')

        logger._log_to_console_and_log_file("Given sequence of command - %s" % server.command)

        stdin.write(server.command.replace(",", "\n") + "\n")

        logger._log_to_console_and_log_file("stdin is %s" % stdout.read())

        stdout.close()
        stdin.close()
        client.close()

    return True


def _get_switch_data(ip, uname, pw, command):
    '''
    Function to get data from Nexus Switch
    '''
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    port = 22  # SSH Port to establish connection
    client.connect(ip, port=port, username=uname, password=pw)
    logger._log_to_console_and_log_file("Executing command - %s" % command)

    input, output, error = client.exec_command(command)

    data = output.read()
    logger._log_to_console_and_log_file("stdout is %s" % data)

    client.close()
    return data


def get_ils_data(*ls_obj):
    '''
    Function to get InternalLink Set data
    '''
    navigate()

    if isinstance(ls_obj, test_data.DataObj):
        ls_obj = [ls_obj]
    elif isinstance(ls_obj, tuple):
        ls_obj = list(ls_obj[0])
    data = []
    for ls in ls_obj:
        if not CommonOperationLogicalSwitches.click_logical_switch(ls.name):
            FusionUIBase.fail_test_or_return_false("Logical Switch doesnt have ILS data")
        CommonOperationLogicalSwitches.click_overview_dropdown()
        CommonOperationLogicalSwitches.click_logical_switch_ils()
        ils = CommonOperationLogicalSwitches.get_ils_data()
        if ils:
            data = ils.split("\n")
    return data


def get_ls_alert_msg(ls_name):
    """
    Function to get InternalLink Set data in Logical Switches.
    """
    navigate()
    if not CommonOperationLogicalSwitches.select_logical_switch(ls_name):
        FusionUIBase.fail_test_or_return_false("Logical Switch doesnt have LS %s" % ls_name)
    if not VerifyLogicalSwitches.verify_warning_msg_exist(timeout=60):
        logger.info("Alert message is not visible.Hence failing the test case...")
        FusionUIBase.fail_test_or_return_false("Warning message is not generated for %s" % ls_name)
    return CommonOperationLogicalSwitches.get_warning_msg(timeout=10)

# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Logical Switch Groups Page
"""

from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.networking.logicalswitchgroups_elements import FusionLSGPage
from FusionLibrary.ui.business_logic.base import FusionUIBase, FusionUIBaseElements, SectionType
from FusionLibrary.ui.business_logic.networking.logicalswitchgroups import (
    CommonOperationLogicalSwitchGroups,
    CreateLogicalSwitchGroups,
    EditLogicalSwitchGroups,
    DeleteLogicalSwitchGroups,
    VerifyLogicalSwitchGroups,
)
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from datetime import datetime
import sys

BW_MIN = 0.1
BW_MAX = 20.0
DEFAULT_PREFERRED_BW = 2.5
LINK_STABILITY_MIN = 1
LINK_STABILITY_MAX = 1800


def navigate():
    FusionUIBase.navigate_to_section(SectionType.LOGICAL_SWITCH_GROUPS, time_for_loading=1)


def create_logical_switch_groups(lsg_obj):
    """ Create Logical Switch Groups
        Usage:
            ${data} =       | Get Data By Xpath                         | //LogicalSwitchGroups/Create/lsg
            ${result} =     | Fusion UI Create Logical Switch Groups    | @{data.lsg}
            Should Be True  | ${result}                                 | msg=Failed to create logical switch groups


        Test data example:
            1. data -> LogicalSwitchGroups -> Create, place your LSG list like below

            <LogicalSwitchGroups>
                <Create>
                    <lsg name="LSG-CiscoNexus50xx" type="Cisco Nexus 50xx" number_of_switches="2" />
                    <lsg name="LSG-CiscoNexus55xx" type="Cisco Nexus 55xx" number_of_switches="2" />
                    <lsg name="LSG-CiscoNexus56xx" type="Cisco Nexus 56xx" number_of_switches="2" />
                    <lsg name="LSG-CiscoNexus600x" type="Cisco Nexus 600x" number_of_switches="2" />
                </Create>
            </LogicalSwitchGroups>
    """

    navigate()
    logger.info("creating Logical Switch Groups ...")

    total = len(lsg_obj)
    created = 0
    already_exists = 0

    for n, lsg in enumerate(lsg_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("creating a Logical Switch Group with name '%s' ..." % lsg.name)
        # checking if the Logical Switch Group is already existing
        if not VerifyLogicalSwitchGroups.verify_logical_switch_group_should_not_exist(lsg.name, fail_if_false=False):
            logger.warn("Logical Switch Group '%s' already exists" % lsg.name)
            already_exists += 1
            continue

        CreateLogicalSwitchGroups.click_create_logical_switch_group_button()
        CreateLogicalSwitchGroups.wait_create_logical_switch_group_dialog_open()
        CreateLogicalSwitchGroups.input_name(lsg.name)
        CreateLogicalSwitchGroups.select_type(lsg.type)
        CreateLogicalSwitchGroups.select_number_of_switches(lsg.number_of_switches)
        CreateLogicalSwitchGroups.click_create_button()

        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
        if status is True:
            logger.warn("unexpected error occurred: %s" % msg)
            ui_lib.fail_test(msg)

        if CreateLogicalSwitchGroups.wait_create_logical_switch_group_dialog_close(timeout=10, fail_if_false=False) is True:
            FusionUIBase.show_activity_sidebar()
            timeout = int(getattr(lsg, 'timeout', "120"))
            if FusionUIBase.wait_activity_action_ok(lsg.name, 'Create', timeout=timeout, fail_if_false=False) is True:
                FusionUIBase.show_activity_sidebar()
                logger.info("successfully created Logical Switch Group '%s'" % lsg.name)
                created += 1
            else:
                logger.warn("'wait_activity_action_ok' = FALSE, skip to next Logical Switch Group ... ")
                FusionUIBase.show_activity_sidebar()
                continue
        else:
            logger.warn("'wait_create_logical_switch_group_dialog_close' = FALSE, skip to next Logical Switch Group ... ")
            CreateLogicalSwitchGroups.click_cancel_button()
            continue

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - already_exists == 0:
        logger.warn("no Logical Switch Group to create! all %s Logical Switch Group(s) is already existing, test is considered PASS" % already_exists)
        return True
    else:
        if created < total:
            logger.warn("not all of the Logical Switch Group(s) is successfully created - %s out of %s created " % (created, total))
            if created + already_exists == total:
                logger.warn("%s already existing Logical Switch Group(s) is skipped, test is considered PASS" % already_exists)
                return True
            else:
                ui_lib.fail_test("%s already existing Logical Switch Group(s) is skipped, %s Logical Switch Group(s) left is failed being created " % (already_exists, total - created - already_exists))

    logger.info("all of the Logical Switch Group(s) is successfully created - %s out of %s " % (created, total))
    return True


def edit_logical_switch_groups(lsg_obj):
    """ Edit Logical Switch Groups
        Usage:
            ${data} =       | Get Data By Xpath                         | //LogicalSwitchGroups/Edit/lsg
            ${result} =     | Fusion UI Edit Logical Switch Groups      | @{data.lsg}
            Should Be True  | ${result}                                 | msg=Failed to edit logical switch groups

        Test data example:
            1. data -> LogicalSwitchGroups -> Edit, place your LSG list like below

            <LogicalSwitchGroups>
                <Edit>
                    <lsg name="LSG-CiscoNexus50xx" new_name="LSG-CiscoNexus50xx_Edited" number_of_switches="2" />
                    <lsg name="LSG-CiscoNexus55xx" new_name="LSG-CiscoNexus55xx_Edited" number_of_switches="2" />
                    <lsg name="LSG-CiscoNexus56xx" new_name="LSG-CiscoNexus56xx_Edited" number_of_switches="2" />
                    <lsg name="LSG-CiscoNexus600x" new_name="LSG-CiscoNexus600x_Edited" number_of_switches="2" />
                </Edit>
            </LogicalSwitchGroups>
    """

    navigate()
    logger.info("editing Logical Switch Groups ...")

    total = len(lsg_obj)
    edited = 0
    not_exists = 0

    for n, lsg in enumerate(lsg_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("editing a Logical Switch Group with name '%s' ..." % lsg.name)
        # checking if the Logical Switch Group is already existing
        if not VerifyLogicalSwitchGroups.verify_logical_switch_group_should_exist(lsg.name, fail_if_false=False):
            logger.warn("Logical Switch Group '%s' does NOT exist!" % lsg.name)
            not_exists += 1
            continue

        CommonOperationLogicalSwitchGroups.click_logical_switch_group(lsg_name=lsg.name)
        EditLogicalSwitchGroups.select_actions_edit()
        EditLogicalSwitchGroups.wait_edit_logical_switch_group_dialog_open()
        EditLogicalSwitchGroups.input_name(lsg.new_name)
        EditLogicalSwitchGroups.select_number_of_switches(lsg.number_of_switches)
        EditLogicalSwitchGroups.click_ok_button()

        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
        if status is True:
            logger.warn("unexpected error occurred: %s" % msg)
            ui_lib.fail_test(msg)

        if EditLogicalSwitchGroups.wait_edit_logical_switch_group_dialog_close(timeout=10, fail_if_false=False) is True:
            FusionUIBase.show_activity_sidebar()
            if FusionUIBase.wait_activity_action_ok(lsg.new_name, 'Update', timeout=10, fail_if_false=False) is True:
                FusionUIBase.show_activity_sidebar()
                logger.info("successfully edited Logical Switch Group '%s'" % lsg.new_name)
                edited += 1
            else:
                logger.warn("'wait_activity_action_ok' = FALSE, skip to next Logical Switch Group ... ")
                FusionUIBase.show_activity_sidebar()
                continue
        else:
            logger.warn("'wait_create_logical_switch_group_dialog_close' = FALSE, skip to next Logical Switch Group ... ")
            EditLogicalSwitchGroups.click_cancel_button()
            continue

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no Logical Switch Group to edit! all %s Logical Switch Group(s) is NOT existing, test is considered FAIL" % not_exists)
        return False
    else:
        if edited < total:
            logger.warn("not all of the Logical Switch Group(s) is successfully edited - %s out of %s edited " % (edited, total))
            if edited + not_exists == total:
                logger.warn("%s non-existing Logical Switch Group(s) is skipped, test is considered FAIL" % not_exists)
                return False
            else:
                ui_lib.fail_test("%s non-existing Logical Switch Group(s) is skipped, %s Logical Switch Group(s) left is failed being edited " % (not_exists, total - edited - not_exists))
        else:
            logger.info("all of the Logical Switch Group(s) is successfully edited - %s out of %s " % (edited, total))
            return True


def delete_logical_switch_group_by_name(lsg_name):
    """ Delete Logical Switch Group by given LSG name
        Usage:
            Fusion UI Delete Logical Switch Group By Name  |   LSG-CiscoNexus50xx
    """

    navigate()
    logger.info("deleting Logical Switch Group '%s' ..." % lsg_name)
    #   check if Logical Switch Group exists
    if not VerifyLogicalSwitchGroups.verify_logical_switch_group_should_exist(lsg_name, fail_if_false=False):
        logger.warn("Logical Switch Group '%s' does NOT exist! keyword '%s' returns a 'False'" % (lsg_name, sys._getframe().f_code.co_name))
        return False
    CommonOperationLogicalSwitchGroups.click_logical_switch_group(lsg_name=lsg_name)
    #   start performing delete action
    DeleteLogicalSwitchGroups.click_actions_delete_button()

    if VerifyLogicalSwitchGroups.is_delete_error_message_present(fail_if_false=False):
        logger.warn("Logical Switch Group '%s' may be in use, failed to delete! keyword '%s' returns a 'False'" % (lsg_name, sys._getframe().f_code.co_name))
        return False

    DeleteLogicalSwitchGroups.click_yes_delete_button()
    DeleteLogicalSwitchGroups.wait_delete_logical_switch_group_dialog_close()
    #   verify Logical Switch Group is not existing after being deleted

    start = datetime.now()
    timeout = 20
    while (datetime.now() - start).total_seconds() < timeout:
        if CommonOperationLogicalSwitchGroups.wait_logical_switch_group_status_not_found(lsg_name, timeout=5, fail_if_false=False):
            logger.info("Logical Switch Group status appear as 'not found', successfully deleted '%s'." % lsg_name)
            break
        elif VerifyLogicalSwitchGroups.verify_logical_switch_group_should_not_exist(lsg_name, timeout=5, fail_if_false=False):
            logger.info("Logical Switch Group '%s' is successfully deleted." % lsg_name)
            break
    else:
        logger.warn("Logical Switch Group '%s' is NOT successfully deleted or timeout issue occurred." % lsg_name)
        return False

    FusionUIBase.show_activity_sidebar()
    if FusionUIBase.wait_activity_action_ok(lsg_name, 'Delete', timeout=30, fail_if_false=False) is False:
        return False
    FusionUIBase.show_activity_sidebar()

    return True


def delete_logical_switch_groups(lsg_obj):
    """ Delete Logical Switch Group by given LSG list
        Usage:
            ${data} =       | Get Data By Xpath                         | //LogicalSwitchGroups/Delete/lsg
            ${result} =     | Fusion UI Delete Logical Switch Groups    | @{data.lsg}
            Should Be True  | ${result}                                 | msg=Failed to delete logical switch groups

        Test data example:
            1. data -> LogicalSwitchGroups -> Delete, place your LSG list like below

            <LogicalSwitchGroups>
                <Delete>
                    <lsg name="LSG-CiscoNexus50xx" />
                    <lsg name="LSG-CiscoNexus55xx" />
                    <lsg name="LSG-CiscoNexus56xx" />
                    <lsg name="LSG-CiscoNexus600x" />
                </Delete>
            </LogicalSwitchGroups>
    """
    navigate()
    logger.info("deleting Logical Switch Group '%s' ..." % [x.name for x in lsg_obj])

    total = len(lsg_obj)
    not_exists = 0
    deleted = 0

    for n, lsg in enumerate(lsg_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("deleting a Logical Switch Group named '%s'" % lsg.name)
        if not VerifyLogicalSwitchGroups.verify_logical_switch_group_should_exist(lsg.name, fail_if_false=False):
            logger.warn("Logical Switch Group '%s' does not exist" % lsg.name)
            not_exists += 1
        else:
            if delete_logical_switch_group_by_name(lsg.name) is False:
                logger.warn("Logical Switch Group '%s' is NOT deleted successfully, or 'Delete' action is not found in right-side-bar list." % lsg.name)
                continue
            else:
                deleted += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no Logical Switch Group to delete! all %s Logical Switch Group(s) is NOT existing, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if deleted < total:
            logger.warn("not all of the Logical Switch Group(s) is successfully deleted - %s out of %s deleted " % (deleted, total))
            if deleted + not_exists == total:
                logger.warn("%s not-existing Logical Switch Group(s) is skipped, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s not-existing Logical Switch Group(s) is skipped, %s Logical Switch Group(s) left is failed being deleted " % (not_exists, total - deleted - not_exists))
                return False

    logger.info("all of the Logical Switch Group(s) is successfully deleted - %s out of %s " % (deleted, total))
    return True


def edit_labels_of_logical_switch_groups(lsg_obj):
    """ Edit Labels Of Logical Switch Groups
        Usage:
            ${data} =       | Get Data By Xpath                                 | //LogicalSwitchGroups/EditLabels/resource     | eliminate_same_node=False
            ${result} =     | Fusion UI Edit Labels Of Logical Switch Groups    | @{data.resource}
            Should Be True  | ${result}                                         | msg=Failed to edit labels of logical switch groups


        Test data example:
            1. data -> LogicalSwitchGroups -> EditLabels, place your RESOURCE list (type="LOGICAL_SWITCH_GROUPS") like below
            2. You have to give "eliminate_same_node=False" parameter to keyword "Get Data By Xpath" for loading test data,
                otherwise the node "Add" or "Remove" will not be located by "Labels.Add" or "Labels.Remove"

            <EditLabels>
                <resource name="LSG-CiscoNexus50xx" type="LOGICAL_SWITCH_GROUPS">
                    <Labels>
                        <Add>
                            <label name="Label_A1" />
                            <label name="Label_A2" />
                            <label name="Label_A3" />
                            <label name="Label_A4" />
                        </Add>
                        <Remove>
                            <label name="Label_A1" />
                            <label name="Label_A3" />
                        </Remove>
                    </Labels>
                </resource>
                <resource name="LSG-CiscoNexus55xx" type="LOGICAL_SWITCH_GROUPS">
                    <Labels>
                        <Add>
                            <label name="Label_B1" />
                            <label name="Label_B2" />
                        </Add>
                    </Labels>
                </resource>
                <resource name="LSG-CiscoNexus50xx">
                    <Labels>
                        <Remove>
                            <label name="Label_A2" />
                            <label name="Label_A4" />
                        </Remove>
                    </Labels>
                </resource>
            </EditLabels>
    """
    return FusionUIBase.edit_labels_of_resources(resource_obj=lsg_obj)


def check_user_privileges(user_name):

    s2l = ui_lib.get_s2l()
    if not ui_lib.wait_for_element(FusionLSGPage.ID_PAGE_LABEL):
        navigate()

    user = test_data.get_privilege_by_name(user_name)

    logger._log_to_console_and_log_file("Create logical switch groups for %s" % user_name)
    if ((user.create).lower() == "yes"):
        logger._info("should pass")
        if ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LINK_CREATE_LOGICAL_SWITCH_GROUP):
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_BTN_CLOSE_LSG)
            ui_lib.wait_for_element_remove(FusionLSGPage.ID_CREATE_LSG_DIALOG)
            logger._log_to_console_and_log_file("Successfully clicked create Logical Switch Groups")
        else:
            return False
    else:
        logger._log_to_console_and_log_file("should fail")
        if not ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LINK_CREATE_LOGICAL_SWITCH_GROUP):
            logger._log_to_console_and_log_file("Create LSG button not visible as expected")
        else:
            return False

    logger._log_to_console_and_log_file("Read logical switch groups for %s" % user_name)
    if ((user.read).lower() == "yes"):
        logger._log_to_console_and_log_file("should pass")
        if ui_lib.wait_for_element_visible(FusionLSGPage.ID_ELEMENT_LSG_NAME_BASE % user.lsgname, PerfConstants.DEFAULT_SYNC_TIME):
            select_lsg(user.lsgname)
            logger._log_to_console_and_log_file("Able to Read logical switch groups for %s" % user.lsgname)
        else:
            return False
    else:
        logger._log_to_console_and_log_file("should fail")
        if not ui_lib.wait_for_element_visible(FusionLSGPage.ID_ELEMENT_LSG_NAME_BASE % user.lsgname, PerfConstants.DEFAULT_SYNC_TIME):
            logger._log_to_console_and_log_file("Unable to Read logical switch groups as expected")
        else:
            return False

    logger._log_to_console_and_log_file("Update logical switch groups for %s" % user_name)
    if ((user.update).lower() == "yes"):
        logger._log_to_console_and_log_file("should pass")
        select_lsg(user.lsgname)
        if ui_lib.wait_for_element_and_click(FusionLSGPage.ID_ACTION_MAIN_BTN):
            if ui_lib.wait_for_element_and_click(FusionLSGPage.ID_ACTION_MENU_EDIT_LSG):
                ui_lib.wait_for_element_and_input_text(FusionLSGPage.ID_INPUT_EDIT_LSGNAME, user.newName)
                ui_lib.wait_for_element_and_click(FusionLSGPage.ID_BTN_EDIT_CANCEL)
                logger._log_to_console_and_log_file("Able to Edit logical switch groups")
            else:
                return False
        else:
            return False
    else:
        logger._log_to_console_and_log_file("should fail")
        if not ui_lib.wait_for_element_and_click(FusionLSGPage.ID_ACTION_MAIN_BTN):
            logger._log_to_console_and_log_file("Unable to Edit logical switch groups as expected")
        else:
            return False

    logger._log_to_console_and_log_file("Delete logical switch groups for %s" % user_name)
    if ((user.delete).lower() == "yes"):
        logger._log_to_console_and_log_file("should pass")
        select_lsg(user.lsgname)
        if ui_lib.wait_for_element_and_click(FusionLSGPage.ID_ACTION_MAIN_BTN):
            if ui_lib.wait_for_element_and_click(FusionLSGPage.ID_ACTION_MENU_DELETE_LSG):
                logger._log_to_console_and_log_file("Able to delete logical switch groups")
            else:
                return False
        else:
            return False
    else:
        logger._log_to_console_and_log_file("should fail")
        if not ui_lib.wait_for_element_and_click(FusionLSGPage.ID_ACTION_MAIN_BTN):
            logger._log_to_console_and_log_file("Unable to delete logical switch groups as expected")
        else:
            return False

    return True


def select_lsg(name):
    """ Select LogicalSwitchGroups  """
    navigate()

    CommonOperationLogicalSwitchGroups.click_logical_switch_group(lsg_name=name, time_for_loading=3)
    return CommonOperationLogicalSwitchGroups.wait_logical_switch_group_selected(lsg_name=name)


def get_all_lsg_switch_type():
    """
    Get all the available switches types in LSG
    """
    navigate()
    CreateLogicalSwitchGroups.click_create_logical_switch_group_button()
    if not CreateLogicalSwitchGroups.click_type_dropdown():
        FusionUIBase.fail_test_or_return_false("Failed to get SWITCH TYPE")
    types = CreateLogicalSwitchGroups.get_text_of_all_types()
    CreateLogicalSwitchGroups.click_cancel_button()
    return types


def filter_by_label_logical_switch_groups(*net_obj):

    s2l = ui_lib.get_s2l()
    if not ui_lib.wait_for_element(FusionLSGPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(net_obj, test_data.DataObj):
        net_obj = [net_obj]
    elif isinstance(net_obj, tuple):
        net_obj = list(net_obj[0])

    for net in net_obj:
        logger._log_to_console_and_log_file("Filtering LSG by label %s" % net.name)
        ui_lib.wait_for_element_and_click(FusionLSGPage.ID_FILTER_RESET)
        ui_lib.wait_for_element_and_click(FusionLSGPage.ID_FILTER_LABEL)
        ui_lib.wait_for_element_and_click("//*[@id='cic-torswitchgroup-labels-filter']/ol/li[contains(.,'%s')]" % net.name)
        if ui_lib.wait_for_element(FusionLSGPage.ID_ELEMENT_LSG_NAME_BASE % net.lsgname):
            logger._log_to_console_and_log_file("LSG '%s' is present" % net.lsgname)
        else:
            return False
        ui_lib.wait_for_element_and_click(FusionLSGPage.ID_FILTER_RESET)
    return True


def add_label_logical_switch_groups(*net_obj):
    """
    !!! Deprecated !!!
        please DO NOT change/maintain this keyword anymore, instead using/improving the keyword
          "Fusion UI Edit Labels Of Logical Switch Groups"
    """

    s2l = ui_lib.get_s2l()
    if not ui_lib.wait_for_element(FusionLSGPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(net_obj, test_data.DataObj):
        net_obj = [net_obj]
    elif isinstance(net_obj, tuple):
        net_obj = list(net_obj[0])

    for net in net_obj:
        logger._log_to_console_and_log_file("Adding label for logical switch group %s" % net.lsgname)
        if select_lsg(net.lsgname):
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_GENERAL_MENU)
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LABEL_MENU)
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LABEL_STRING)
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LABEL_STRING)
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LABEL_EDIT)
            ui_lib.wait_for_element(FusionLSGPage.ID_LABEL_INPUT_NAME)
            # set label name
            ui_lib.wait_for_element_and_input_text(FusionLSGPage.ID_LABEL_INPUT_NAME, net.name)
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LABEL_ADD_BTN)
            # click on the OK Button
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LABEL_EDIT_OK)
        else:
            logger._warn("LSG is not present in the list")
            return False

    return True


def delete_label_logical_switch_groups(*net_obj):
    """
    !!! Deprecated !!!
        please DO NOT change/maintain this keyword anymore, instead using/improving the keyword
          "Fusion UI Edit Labels Of Logical Switch Groups"
    """

    s2l = ui_lib.get_s2l()
    if not ui_lib.wait_for_element(FusionLSGPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(net_obj, test_data.DataObj):
        net_obj = [net_obj]
    elif isinstance(net_obj, tuple):
        net_obj = list(net_obj[0])

    for net in net_obj:
        logger._log_to_console_and_log_file("Deleting label for logical switch group %s" % net.lsgname)
        if select_lsg(net.lsgname):
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_GENERAL_MENU)
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LABEL_MENU)
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LABEL_STRING)
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LABEL_STRING)
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LABEL_EDIT)
            # delete the label
            if ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LABEL_DELETE):
                logger._log_to_console_and_log_file("Deleted the label")
            else:
                logger._log_to_console_and_log_file("Failed to remove the label")
                return False
            # click on the OK Button
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LABEL_EDIT_OK)
        else:
            logger._warn("LSG is not present in the list")
            return False

    return True


def edit_label_logical_switch_groups(*net_obj):
    """
    !!! Deprecated !!!
        please DO NOT change/maintain this keyword anymore, instead using/improving the keyword
          "Fusion UI Edit Labels Of Logical Switch Groups"
    """
    s2l = ui_lib.get_s2l()
    if not ui_lib.wait_for_element(FusionLSGPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(net_obj, test_data.DataObj):
        net_obj = [net_obj]
    elif isinstance(net_obj, tuple):
        net_obj = list(net_obj[0])

    for net in net_obj:
        logger._log_to_console_and_log_file("Deleting label for logical switch group %s" % net.lsgname)
        if select_lsg(net.lsgname):
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_GENERAL_MENU)
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LABEL_MENU)
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LABEL_STRING)
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LABEL_STRING)
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LABEL_EDIT)
            # delete the label
            if ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LABEL_DELETE):
                logger._log_to_console_and_log_file("Deleted the label")
            else:
                logger._log_to_console_and_log_file("Failed to remove the label")
                return False
            ui_lib.wait_for_element_and_input_text(FusionLSGPage.ID_LABEL_INPUT_NAME, net.newName)
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LABEL_ADD_BTN)
            # click on the OK Button
            ui_lib.wait_for_element_and_click(FusionLSGPage.ID_LABEL_EDIT_OK)
        else:
            logger._warn("LSG is not present in the list")
            return False

    return True

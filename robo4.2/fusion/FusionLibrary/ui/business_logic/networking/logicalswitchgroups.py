# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.

"""
    Logical Switch Groups page/screen
"""

from datetime import datetime
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.base import FusionUIBase, FusionUIConst, TakeScreenShotWhenReturnFalseDeco
from FusionLibrary.ui.business_logic.networking.logicalswitchgroups_elements import (
    GeneralLogicalSwitchGroupsElements,
    CreateLogicalSwitchGroupsElements,
    EditLogicalSwitchGroupsElements,
    DeleteLogicalSwitchGroupsElements,
)
from RoboGalaxyLibrary import BuiltIn
from HTMLParser import HTMLParser


class CommonOperationLogicalSwitchGroups(object):

    e = GeneralLogicalSwitchGroupsElements
    html = HTMLParser()

    @classmethod
    def get_logical_switch_group_list(cls, timeout=5, fail_if_false=True):
        logger.debug("Get all Logical Switch Group name(s) from table")
        lsg_list = []
        if ui_lib.wait_for_element(cls.e.ID_TABLE_LOGICAL_SWITCH_GROUP_LIST):
            lsg_list = FusionUIBase.get_multi_elements_text(cls.e.ID_TABLE_LOGICAL_SWITCH_GROUP_LIST, timeout=timeout, fail_if_false=fail_if_false)
        return lsg_list

    @classmethod
    def click_logical_switch_group(cls, lsg_name, timeout=5, time_for_loading=3, fail_if_false=True):
        logger.debug("select Logical Switch Group '%s'" % lsg_name)
        ui_lib.wait_for_element_and_click(cls.e.ID_TABLE_LOGICAL_SWITCH_GROUP % lsg_name, timeout=timeout, fail_if_false=fail_if_false)
        BuiltIn().sleep(time_for_loading)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_logical_switch_group_selected(cls, lsg_name, timeout=5, fail_if_false=True):
        logger.debug("wait for Logical Switch Group '%s' to be selected" % lsg_name)
        if ui_lib.wait_for_element_visible(cls.e.ID_TABLE_LOGICAL_SWITCH_GROUP_SELECTED % lsg_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("Logical Switch Group '%s' is successfully selected" % lsg_name)
            return True
        else:
            msg = "failed to wait for Logical Switch Group '%s' to be selected" % lsg_name
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_logical_switch_group_status_not_found(cls, lsg_name, timeout=5, fail_if_false=True):
        logger.info("wait for Logical Switch Group status to change to 'not found'")
        if ui_lib.wait_for_element_visible(cls.e.ID_TABLE_LOGICAL_SWITCH_GROUP_NOT_FOUND % lsg_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("Logical Switch Group '%s' status successfully changed to 'not found'" % lsg_name)
            return True
        else:
            msg = "failed to wait for Logical Switch Group '%s' status to change to 'not found'" % lsg_name
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def click_actions_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click 'Actions' button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ACTIONS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_logical_switch_group_status_ok(cls, lsg_name, timeout=10, fail_if_false=True):
        start = datetime.now()
        logger.debug("wait for Logical Switch Group '%s' status to change to OK" % lsg_name)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(cls.html.unescape(cls.e.ID_STATUS_LOGICAL_SWITCH_GROUP_OK % lsg_name), timeout=2, fail_if_false=False):
                logger.debug("Logical Switch Group '%s' status is OK as expected." % lsg_name)
                return True
            elif ui_lib.wait_for_element_visible(cls.html.unescape(cls.e.ID_STATUS_LOGICAL_SWITCH_GROUP_WARN % lsg_name), timeout=2, fail_if_false=False):
                err_msg = "Logical Switch Group '%s' status is WARN not as expected." % lsg_name
                return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)
            elif ui_lib.wait_for_element_visible(cls.html.unescape(cls.e.ID_STATUS_LOGICAL_SWITCH_GROUP_ERROR % lsg_name), timeout=2, fail_if_false=False):
                err_msg = "Logical Switch Group '%s' status is ERROR not as expected." % lsg_name
                return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)
            else:
                logger.debug("Logical Switch Group status is UNKNOWN, waiting ...")
                continue
        err_msg = "Timeout waiting for Logical Switch Group '%s' status to change to OK." % lsg_name
        return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_logical_switch_group_status_ok_or_warn(cls, lsg_name, timeout=10, fail_if_false=True):
        start = datetime.now()
        logger.debug("wait for Logical Switch Group '%s' status to change to OK or WARN" % lsg_name)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(cls.html.unescape(cls.e.ID_STATUS_LOGICAL_SWITCH_GROUP_OK % lsg_name), timeout=5, fail_if_false=False):
                logger.debug("Logical Switch Group '%s' status is OK as expected." % lsg_name)
                return True
            elif ui_lib.wait_for_element_visible(cls.html.unescape(cls.e.ID_STATUS_LOGICAL_SWITCH_GROUP_WARN % lsg_name), timeout=5, fail_if_false=False):
                logger.debug("Logical Switch Group '%s' status is WARN as expected." % lsg_name)
                return True
            elif ui_lib.wait_for_element_visible(cls.html.unescape(cls.e.ID_STATUS_LOGICAL_SWITCH_GROUP_ERROR % lsg_name), timeout=5, fail_if_false=False):
                err_msg = "Logical Switch Group '%s' status is ERROR not as expected." % lsg_name
                return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)
            else:
                logger.debug("Logical Switch Group '%s' status is UNKNOWN, waiting ..." % lsg_name)
                continue
        err_msg = "Timeout waiting for Logical Switch Group '%s' status to change to OK or WARN." % lsg_name
        return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_logical_switch_group_status_error(cls, lsg_name, timeout=10, fail_if_false=True):
        start = datetime.now()
        logger.debug("wait for Logical Switch Group '%s' status to change to ERROR" % lsg_name)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(cls.html.unescape(cls.e.ID_STATUS_LOGICAL_SWITCH_GROUP_OK % lsg_name), timeout=5, fail_if_false=False):
                err_msg = "Logical Switch Group '%s' status is OK not as expected." % lsg_name
                return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)
            elif ui_lib.wait_for_element_visible(cls.html.unescape(cls.e.ID_STATUS_LOGICAL_SWITCH_GROUP_WARN % lsg_name), timeout=5, fail_if_false=False):
                logger.debug("Logical Switch Group '%s' status is WARN not as expected." % lsg_name)
                return False
            elif ui_lib.wait_for_element_visible(cls.html.unescape(cls.e.ID_STATUS_LOGICAL_SWITCH_GROUP_ERROR % lsg_name), timeout=5, fail_if_false=False):
                logger.debug("Logical Switch Group '%s' status is ERROR as expected." % lsg_name)
                return True
            else:
                logger.debug("Logical Switch Group '%s' status is UNKNOWN, waiting ..." % lsg_name)
                continue
        err_msg = "Timeout waiting for Logical Switch Group status to change to ERROR."
        return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)

    @classmethod
    def get_ls_count_of_lsg(cls, lsg_name):
        logger.debug("check how many logical switch(es) defined in the LSG '%s' ..." % lsg_name)
        resp = FusionUIBase.APIMethods().get_logical_switch_group(lsg_name=lsg_name)
        logger.debug("LSGs (resp['members'] of LogicalSwitchGroup.get(param=\"?filter='name' = '%s'\")) is: < %s >" % (lsg_name, resp['members']))
        switches = [lsg for lsg in resp['members'] if lsg['name'] == lsg_name][0]['switchMapTemplate']['switchMapEntryTemplates']
        ls_count = len(switches)
        logger.debug("got '< %s >' logical switch(es) defined in the LSG '%s' ..." % (ls_count, lsg_name))
        return ls_count


class CreateLogicalSwitchGroups(object):

    e = CreateLogicalSwitchGroupsElements

    @classmethod
    def click_create_logical_switch_group_button(cls, timeout=5):
        logger.debug("click 'Create logical switch group' button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_LOGICAL_SWITCH_GROUP, timeout=timeout, fail_if_false=True)

    @classmethod
    def select_actions_create(cls, timeout=5, fail_if_false=True):
        logger.debug("select 'Actions -> Create' button")
        ui_lib.wait_for_element_and_click(GeneralLogicalSwitchGroupsElements.ID_BUTTON_ACTIONS, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_ACTIONS_CREATE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_logical_switch_group_dialog_open(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Create Logical Switch Group' to open ...")
        if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_CREATE_LOGICAL_SWITCH_GROUP, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Create Logical Switch Group' successfully opened")
            return True
        else:
            msg = "failed to wait for dialog 'Create Logical Switch Group' to open within %s seconds" % timeout
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def input_name(cls, name, timeout=5, fail_if_false=True):
        logger.debug("input 'Name' as '%s'" % name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NAME, name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_type_dropdown(cls, timeout=5, fail_if_false=True):
        logger.debug("click to drop-down 'Type'")
        return FusionUIBase.wait_for_element_and_click(cls.e.ID_DROPDOWN_TYPE, timeout=timeout, fail_if_false=fail_if_false, js_click=True)

    @classmethod
    def get_text_of_all_types(cls, timeout=5, fail_if_false=True):
        logger.debug("get all Types for Logical Switch Group")
        return ui_lib.get_text(cls.e.ID_TEXT_TYPE_LIST, timeout, fail_if_false)

    @classmethod
    def select_type(cls, type_name, timeout=5, fail_if_false=True):
        logger.debug("select 'Type' as '%s' ..." % type_name)
        return FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_TYPE, type_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_number_of_switches(cls, number_of_switches, timeout=5, fail_if_false=True):
        logger.debug("select 'Number of switches' as '%s' ..." % number_of_switches)
        return FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_NUMBER_OF_SWITCHES, number_of_switches, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_logical_switch_group_dialog_close(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Create Logical Switch Group' to close ...")
        if ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_CREATE_LOGICAL_SWITCH_GROUP, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Create Logical Switch Group' successfully closed")
            return True
        else:
            msg = "failed to wait for dialog 'Create Logical Switch Group' to close"
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def click_create_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click button 'Create'")
        FusionUIBase.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE, timeout=timeout, fail_if_false=fail_if_false, js_click=True)

    @classmethod
    def click_create_plus_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click button 'Create+'")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_PLUS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_error_message_if_create_failed(cls, timeout=5, fail_if_false=True):
        logger.debug("get error message if creation failed")
        return ui_lib.get_text(cls.e.ID_ERROR_CREATE_FAILED, timeout=timeout, fail_if_false=fail_if_false)


class EditLogicalSwitchGroups(object):

    e = EditLogicalSwitchGroupsElements

    @classmethod
    def click_edit_button(cls, timeout=5):
        logger.debug("click 'Edit' button from Actions menu")
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_ACTIONS_EDIT, timeout=timeout, fail_if_false=True)

    @classmethod
    def select_actions_edit(cls, timeout=5):
        logger.debug("click 'Actions -> Edit' button ")
        CommonOperationLogicalSwitchGroups.click_actions_button(timeout=timeout)
        cls.click_edit_button(timeout=timeout)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_logical_switch_group_dialog_open(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Edit Logical Switch Group' to open ...")
        if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_EDIT_LOGICAL_SWITCH_GROUP, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Edit Logical Switch Group' successfully opened")
            return True
        else:
            msg = "failed to wait for dialog 'Edit Logical Switch Group' to open within %s seconds" % timeout
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def input_name(cls, name, timeout=5, fail_if_false=True):
        logger.debug("input 'Name' as '%s'" % name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NAME, name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_number_of_switches(cls, number_of_switches, timeout=5, fail_if_false=True):
        logger.debug("select 'Number of switches' as '%s' ..." % number_of_switches)
        return FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_NUMBER_OF_SWITCHES, number_of_switches, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_logical_switch_group_dialog_close(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Edit Logical Switch Group' to close ...")
        if ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_EDIT_LOGICAL_SWITCH_GROUP, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Edit Logical Switch Group' successfully closed")
            return True
        else:
            msg = "failed to wait for dialog 'Edit Logical Switch Group' to close"
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def click_ok_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click button 'OK'")
        FusionUIBase.wait_for_element_and_click(cls.e.ID_BUTTON_OK, timeout=timeout, fail_if_false=fail_if_false, js_click=True)

    @classmethod
    def click_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_error_message_if_edit_failed(cls, timeout=5, fail_if_false=True):
        logger.debug("get error message if edit failed")
        return ui_lib.get_text(cls.e.ID_ERROR_EDIT_FAILED, timeout=timeout, fail_if_false=fail_if_false)


class DeleteLogicalSwitchGroups(object):

    e = DeleteLogicalSwitchGroupsElements

    @classmethod
    def click_delete_button(cls, timeout=5):
        logger.debug("click 'Delete' button from Actions menu")
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_ACTIONS_DELETE, timeout=timeout, fail_if_false=True)

    @classmethod
    def click_actions_delete_button(cls, timeout=5):
        logger.debug("click 'Actions -> Delete' button ")
        CommonOperationLogicalSwitchGroups.click_actions_button(timeout=timeout)
        cls.click_delete_button(timeout=timeout)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_logical_switch_group_dialog_open(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Delete Logical Switch Group' to open ...")
        if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_DELETE_LOGICAL_SWITCH_GROUP, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Delete Logical Switch Group' successfully opened")
            return True
        else:
            msg = "failed to wait for dialog 'Delete Logical Switch Group' to open within %s seconds" % timeout
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_logical_switch_group_dialog_close(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Delete Logical Switch Group' to close ...")
        if ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_DELETE_LOGICAL_SWITCH_GROUP, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Delete Logical Switch Group' successfully closed")
            return True
        else:
            msg = "failed to wait for dialog 'Delete Logical Switch Group' to close"
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def click_yes_delete_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click button 'Yes, delete' button")
        FusionUIBase.wait_for_element_and_click(cls.e.ID_BUTTON_YES_DELETE, timeout=timeout, fail_if_false=fail_if_false, js_click=True)

    @classmethod
    def click_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_close_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click button 'Close'")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CLOSE, timeout=timeout, fail_if_false=fail_if_false)


class VerifyLogicalSwitchGroups(object):

    e = GeneralLogicalSwitchGroupsElements

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_switch_group_should_not_exist(cls, lsg_name, timeout=5, fail_if_false=True):
        logger.debug("verify Logical Switch Group '%s' should NOT exist ..." % lsg_name)
        if ui_lib.wait_for_element_notvisible(cls.e.ID_TABLE_LOGICAL_SWITCH_GROUP % lsg_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("Logical Switch Group '%s' is successfully verified as invisible within %s second(s)" % (lsg_name, timeout))
            return True
        elif ui_lib.wait_for_element_visible(cls.e.ID_TABLE_LOGICAL_SWITCH_GROUP_NOT_FOUND % lsg_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("Logical Switch Group '%s' was deleted but not de-selected." % lsg_name)
            return True
        else:
            msg = "Logical Switch Group '%s' is failed to be verified as invisible within %s second(s)" % (lsg_name, timeout)
            return FusionUIBase.fail_test_or_return_false(message=msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_switch_group_should_exist(cls, lsg_name, timeout=5, fail_if_false=True):
        logger.debug("verify Logical Switch Group '%s' should exist ..." % lsg_name)
        if ui_lib.wait_for_element_visible(cls.e.ID_TABLE_LOGICAL_SWITCH_GROUP % lsg_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("Logical Switch Group '%s' is successfully verified as visible within %s second(s)" % (lsg_name, timeout))
            return True
        else:
            msg = "Logical Switch Group '%s' is failed to be verified as visible within %s second(s)" % (lsg_name, timeout)
            return FusionUIBase.fail_test_or_return_false(message=msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_delete_error_message_present(cls, timeout=5, fail_if_false=True):
        logger.debug("check if the 'Unable to delete the logical switch group ...' message occurs ...")
        return ui_lib.wait_for_element_visible(DeleteLogicalSwitchGroupsElements.ID_LABEL_DELETE_ERROR_MESSAGE, timeout=timeout, fail_if_false=fail_if_false)

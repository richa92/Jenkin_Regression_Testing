# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
""" Fusion Users and Groups UI page."""

from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.usersandgroups.usersandgroups_elements import *
from FusionLibrary.ui.business_logic.base import FusionUIBase, TakeScreenShotWhenReturnFalseDeco


class GeneralUserandGroups(FusionUIBase):

    @classmethod
    def get_user_list(cls, timeout=5):
        logger.debug("Get all user names from table")
        user_name_list = []
        if ui_lib.wait_for_element(GeneralUserandGroupsElements.ID_USERS_TABLE):
            user_name_list = FusionUIBase.get_multi_elements_text(GeneralUserandGroupsElements.ID_ALL_USERNAME_LIST, timeout, fail_if_false=True)
        return user_name_list

    @classmethod
    def get_current_username(cls, timeout=5, fail_if_false=True):
        logger.debug("Get current username")
        ui_lib.wait_for_element_and_click(EditCurrentSessionUserElements.ID_SESSION_CONTROL, timeout, fail_if_false)
        return FusionUIBase.get_text(EditCurrentSessionUserElements.ID_CURRENT_SESSION_USER, timeout, fail_if_false)

    @classmethod
    def get_user_list_in_group(cls, group, timeout=5):
        logger.debug("Get all user names include a specific group from table")
        user_name_list = []
        if ui_lib.wait_for_element(GeneralUserandGroupsElements.ID_USERS_TABLE):
            user_name_list = FusionUIBase.get_multi_elements_text(GeneralUserandGroupsElements.ID_ALL_USERNAME_LIST_WITH_GROUP % group, timeout, fail_if_false=True)
        return user_name_list

    @classmethod
    def click_user(cls, user_name, directory="Local", verifygroup=False, timeout=5, time_for_loading=3):
        logger.debug("select user %s" % user_name)
        if verifygroup and VerifyGroup.verify_group_mode(5, False):
            ui_lib.wait_for_element_and_click(GeneralUserandGroupsElements.ID_USERS_TABLE_NAME % (user_name, directory), timeout, fail_if_false=True)
        else:
            ui_lib.wait_for_element_and_click(GeneralUserandGroupsElements.ID_USERS_TABLE_NAME_SIMPLE % user_name, timeout, fail_if_false=True)
        BuiltIn().sleep(time_for_loading)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_user_selected(cls, user_name, timeout=5, fail_if_false=True):
        logger.debug("wait user '%s' selected" % user_name)
        return ui_lib.wait_for_element(GeneralUserandGroupsElements.ID_TEXT_USER_NAME % user_name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_user_deleted(cls, user_name, directory="Local", timeout=5, fail_if_false=True):
        logger.info("wait user deleted")
        return ui_lib.wait_for_element_remove(GeneralUserandGroupsElements.ID_USERS_TABLE_NAME % (user_name, directory), timeout, fail_if_false)

    @classmethod
    def click_action_button(cls, timeout=5):
        logger.debug("click 'Action' button")
        ui_lib.wait_for_element_and_click(GeneralUserandGroupsElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_error_message_no_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("verify no error message")
        return ui_lib.wait_for_element_notvisible(GeneralUserandGroupsElements.ID_TEXT_ERROR_MESSAGE, timeout, fail_if_false)


class CreateUser(FusionUIBase):

    @classmethod
    def click_action_add_user_button(cls, timeout=5):
        logger.debug("click 'Add user' button")
        ui_lib.wait_for_element_and_click(GeneralUserandGroupsElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(GeneralUserandGroupsElements.ID_SELECT_ACTION_ADD_USER, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_user_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Add User' to show up ...")
        return ui_lib.wait_for_element_visible(CreateUserElements.ID_DIALOG_ADD_USER, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_user_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Add User' to disappear ...")
        return ui_lib.wait_for_element_notvisible(CreateUserElements.ID_DIALOG_ADD_USER, timeout, fail_if_false)

    @classmethod
    def click_add_button(cls, timeout=5):
        logger.debug("click button 'Add'")
        ui_lib.wait_for_element_and_click(CreateUserElements.ID_BTN_USER_ADD, timeout, fail_if_false=True)

    @classmethod
    def click_add_plus_button(cls, timeout=5):
        logger.debug("click button 'Add+'")
        ui_lib.wait_for_element_and_click(CreateUserElements.ID_BTN_USER_ADD_PLUS, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(CreateUserElements.ID_BTN_USER_ADD_CANCEL, timeout, fail_if_false=True)

    @classmethod
    def input_login_name(cls, name, timeout=5):
        logger.debug("input 'Login name' as '%s'" % name)
        ui_lib.wait_for_element_and_input_text(CreateUserElements.ID_INPUT_USER_LOGIN_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def input_full_name(cls, name, timeout=5):
        logger.debug("input 'Full name' as '%s'" % name)
        ui_lib.wait_for_element_and_input_text(CreateUserElements.ID_INPUT_USER_FULL_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def input_initial_password(cls, password, timeout=5):
        logger.debug("input 'Initial password' as '%s'" % password)
        ui_lib.wait_for_element_and_input_text(CreateUserElements.ID_INPUT_USER_INITIAL_PASSWORD, password, timeout, fail_if_false=True)

    @classmethod
    def input_confirm_password(cls, password, timeout=5):
        logger.debug("input 'Confirm password' as '%s'" % password)
        ui_lib.wait_for_element_and_input_text(CreateUserElements.ID_INPUT_USER_CONFIRM_PASSWORD, password, timeout, fail_if_false=True)

    @classmethod
    def input_email(cls, email, timeout=5):
        logger.debug("input 'Email' as '%s'" % email)
        ui_lib.wait_for_element_and_input_text(CreateUserElements.ID_INPUT_USER_EMAIL, email, timeout, fail_if_false=True)

    @classmethod
    def input_office_phone(cls, phone, timeout=5):
        logger.debug("input 'Office phone' as '%s'" % phone)
        ui_lib.wait_for_element_and_input_text(CreateUserElements.ID_INPUT_USER_OFFICE_PHONE, phone, timeout, fail_if_false=True)

    @classmethod
    def input_mobile_phone(cls, phone, timeout=5):
        logger.debug("input 'Mobile phone' as '%s'" % phone)
        ui_lib.wait_for_element_and_input_text(CreateUserElements.ID_INPUT_USER_MOBILE_PHONE, phone, timeout, fail_if_false=True)

    @classmethod
    def tick_role_specialized(cls, timeout=5):
        logger.debug("choose 'Role' as 'Specialized'")
        ui_lib.wait_for_element_and_click(CreateUserElements.ID_RADIO_ROLE_SPECIALIZED, timeout, fail_if_false=True)

    @classmethod
    def select_role(cls, role, timeout=5):
        logger.debug("select specialized role '%s' option ..." % role)
        ui_lib.wait_for_element_and_click(CreateUserElements.ID_SELECT_ROLES_DROPDOWN, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(CreateUserElements.ID_SELECT_ROLE % role, timeout, fail_if_false=True)

    @classmethod
    def tick_role_full(cls, timeout=5):
        logger.debug("choose 'Role' as 'Full'")
        ui_lib.wait_for_element_and_click(CreateUserElements.ID_RADIO_ROLE_FULL, timeout, fail_if_false=True)

    @classmethod
    def tick_role_read_only(cls, timeout=5):
        logger.debug("choose 'Role' as 'Read only'")
        ui_lib.wait_for_element_and_click(CreateUserElements.ID_RADIO_ROLE_READ_ONLY, timeout, fail_if_false=True)

    @classmethod
    def tick_specialized(cls, role, timeout=5):
        logger.debug("select specialized role '%s' option ..." % role)
        ui_lib.wait_for_element_and_click(CreateUserElements.ID_SELECT_ROLES_DROPDOWN, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(CreateUserElements.ID_CHECKBOX_SPECIALIZED_ROLE % role, timeout,
                                          fail_if_false=True)

    @classmethod
    def untick_specialized(cls, role, timeout=5):
        logger.debug("un-select specialized role '%s' option ..." % role)
        FusionUIBase.wait_for_checkbox_and_unselect(CreateUserElements.ID_CHECKBOX_SPECIALIZED_ROLE % role, timeout,
                                                    fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def varify_add_successful(cls):
        for text in ["This login name is already in use.", "At least one role must be selected."]:
            if ui_lib.page_contains(text):
                logger.warn(text)
                return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_add_plus_ok(cls, timeout=5, fail_if_false=True):
        logger.debug("verify add plus successful")
        return ui_lib.wait_for_element_value(CreateUserElements.ID_INPUT_USER_LOGIN_NAME, "", timeout, fail_if_false)


class RemoveUser(FusionUIBase):

    @classmethod
    def click_action_remove_user_button(cls, timeout=5):
        logger.debug("click 'Remove user' button")
        ui_lib.wait_for_element_and_click(GeneralUserandGroupsElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(GeneralUserandGroupsElements.ID_SELECT_ACTION_REMOVE_USER, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_user_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Remove' to show up ...")
        return ui_lib.wait_for_element_visible(RemoveUserElements.ID_CONFIRM_REMOVE_DIALOG_PROMPT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_user_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Remove' to disappear ...")
        return ui_lib.wait_for_element_notvisible(RemoveUserElements.ID_CONFIRM_REMOVE_DIALOG_PROMPT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_cannot_remove_user_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Remove' to show up ...")
        return ui_lib.wait_for_element_visible(RemoveUserElements.ID_CANNOT_REMOVE_DIALOG_CONTENT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_cannot_remove_user_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Remove' to disappear ...")
        return ui_lib.wait_for_element_notvisible(RemoveUserElements.ID_CANNOT_REMOVE_DIALOG_CONTENT, timeout, fail_if_false)

    @classmethod
    def click_ok_button(cls, timeout=5):
        logger.debug("click button 'OK'")
        ui_lib.wait_for_element_and_click(RemoveUserElements.ID_BTN_OK_CANCEL_REMOVE, timeout, fail_if_false=True)

    @classmethod
    def click_yes_remove_button(cls, timeout=5):
        logger.debug("click button 'Yes, remove'")
        ui_lib.wait_for_element_and_click(RemoveUserElements.ID_BTN_YES_CONFIRM_REMOVE, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click button 'K'")
        ui_lib.wait_for_element_and_click(RemoveUserElements.ID_BTN_CANCEL_CONFIRM_REMOVE, timeout, fail_if_false=True)


class EditUser(FusionUIBase):

    @classmethod
    def edit_role_specialized(cls, role, timeout=5):
        logger.debug("select specialized role '%s' option ..." % role)
        ui_lib.wait_for_element_and_click(EditUserElements.ID_EDIT_ROLE_DROPDOWN, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditUserElements.ID_SELECT_ROLES_DROPDOWN % role, timeout, fail_if_false=True)

    @classmethod
    def click_action_edit_button(cls, timeout=5):
        logger.debug("click 'Edit' button")
        ui_lib.wait_for_element_and_click(GeneralUserandGroupsElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(GeneralUserandGroupsElements.ID_SELECT_ACTION_EDIT_USER, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_user_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Edit User' to show up ...")
        return ui_lib.wait_for_element_visible(EditUserElements.ID_DIALOG_EDIT_USER, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_user_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Edit User' to disappear ...")
        return ui_lib.wait_for_element_notvisible(EditUserElements.ID_DIALOG_EDIT_USER, timeout, fail_if_false)

    @classmethod
    def click_ok_button(cls, timeout=5):
        logger.debug("click button 'ok'")
        ui_lib.wait_for_element_and_click(EditUserElements.ID_BTN_EDIT_OK, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(EditUserElements.ID_BTN_EDIT_CANCEL, timeout, fail_if_false=True)

    @classmethod
    def input_login_name(cls, name, timeout=5):
        logger.debug("input 'Login name' as '%s'" % name)
        ui_lib.wait_for_element_and_input_text(EditUserElements.ID_INPUT_EDIT_LOGIN_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def input_full_name(cls, name, timeout=5):
        logger.debug("input 'Full name' as '%s'" % name)
        ui_lib.wait_for_element_and_input_text(EditUserElements.ID_INPUT_EDIT_FULL_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def input_initial_password(cls, password, timeout=5):
        logger.debug("input 'Initial password' as '%s'" % password)
        ui_lib.wait_for_element_and_input_text(EditUserElements.ID_INPUT_EDIT_INITIAL_PASSWORD, password, timeout, fail_if_false=True)

    @classmethod
    def input_confirm_password(cls, password, timeout=5):
        logger.debug("input 'Confirm password' as '%s'" % password)
        ui_lib.wait_for_element_and_input_text(EditUserElements.ID_INPUT_EDIT_CONFIRM_PASSWORD, password, timeout, fail_if_false=True)

    @classmethod
    def input_email(cls, email, timeout=5):
        logger.debug("input 'Email' as '%s'" % email)
        ui_lib.wait_for_element_and_input_text(EditUserElements.ID_INPUT_EDIT_EMAIL, email, timeout, fail_if_false=True)

    @classmethod
    def input_office_phone(cls, phone, timeout=5):
        logger.debug("input 'Office phone' as '%s'" % phone)
        ui_lib.wait_for_element_and_input_text(EditUserElements.ID_INPUT_EDIT_OFFICE_PHONE, phone, timeout, fail_if_false=True)

    @classmethod
    def input_mobile_phone(cls, phone, timeout=5):
        logger.debug("input 'Mobile phone' as '%s'" % phone)
        ui_lib.wait_for_element_and_input_text(EditUserElements.ID_INPUT_EDIT_MOBILE_PHONE, phone, timeout, fail_if_false=True)

    @classmethod
    def tick_role_specialized(cls, timeout=5):
        logger.debug("choose 'Role' as 'Specialized'")
        ui_lib.wait_for_element_and_click(EditUserElements.ID_RADIO_EDIT_ROLE_SPECIALIZED, timeout, fail_if_false=True)

    @classmethod
    def tick_role_full(cls, timeout=5):
        logger.debug("choose 'Full' as 'Specialized'")
        ui_lib.wait_for_element_and_click(EditUserElements.ID_RADIO_EDIT_ROLE_FULL, timeout, fail_if_false=True)

    @classmethod
    def tick_role_read_only(cls, timeout=5):
        logger.debug("choose 'Role' as 'Read only'")
        ui_lib.wait_for_element_and_click(EditUserElements.ID_RADIO_EDIT_ROLE_READ_ONLY, timeout, fail_if_false=True)

    @classmethod
    def tick_specialized(cls, role, timeout=5):
        logger.debug("select specialized role '%s' option ..." % role)
        FusionUIBase.wait_for_checkbox_and_select(EditUserElements.ID_CHECKBOX_SPECIALIZED_ROLE % role, timeout,
                                                  fail_if_false=True)

    @classmethod
    def untick_specialized(cls, role, timeout=5):
        logger.debug("un-select specialized role '%s' option ..." % role)
        FusionUIBase.wait_for_checkbox_and_unselect(EditUserElements.ID_CHECKBOX_SPECIALIZED_ROLE % role, timeout,
                                                    fail_if_false=True)


class AddDirectoryUserAndGroup(FusionUIBase):

    @classmethod
    def click_action_add_group_button(cls, timeout=5):
        logger.debug("click 'Add group' button")
        ui_lib.wait_for_element_and_click(GeneralUserandGroupsElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(GeneralUserandGroupsElements.ID_SELECT_ACTION_ADD_GROUP, timeout, fail_if_false=True)

    @classmethod
    def select_directory(cls, directory, timeout=5):
        logger.debug("select 'Directory' as %s" % directory)
        if FusionUIBase.get_webelement_attribute(AddDirectoryUserAndGroupElements.ID_INPUT_DIRECTORY_NAME, "value", timeout) == directory:
            return True
        else:
            ui_lib.wait_for_element_and_click(AddDirectoryUserAndGroupElements.ID_DROPDOWN_DIRECTORY, timeout, fail_if_false=True)
            ui_lib.wait_for_element_and_click(AddDirectoryUserAndGroupElements.ID_SELECT_DIRECTORY % directory, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_group_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Add Group' to show up ...")
        return ui_lib.wait_for_element_visible(AddDirectoryUserAndGroupElements.ID_DIALOG_ADD_GOURP, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_group_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Add Group' to disappear ...")
        return ui_lib.wait_for_element_notvisible(AddDirectoryUserAndGroupElements.ID_DIALOG_ADD_GOURP, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_group_credential_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Credential' to show up ...")
        return ui_lib.wait_for_element_visible(AddDirectoryUserAndGroupElements.ID_DIALOG_ADD_GROUP_CREDENTIAL, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_group_credential_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Credential' to disappear ...")
        return ui_lib.wait_for_element_notvisible(AddDirectoryUserAndGroupElements.ID_DIALOG_ADD_GROUP_CREDENTIAL, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_select_group_credential_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Connect to' to show up ...")
        return ui_lib.wait_for_element_visible(AddDirectoryUserAndGroupElements.ID_DIALOG_SELECT_GROUP_CREDENTIAL, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_select_group_credential_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Connect to' to disappear ...")
        return ui_lib.wait_for_element_notvisible(AddDirectoryUserAndGroupElements.ID_DIALOG_SELECT_GROUP_CREDENTIAL, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_select_group_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Select a Group from' to show up ...")
        return ui_lib.wait_for_element_visible(AddDirectoryUserAndGroupElements.ID_DIALOG_SELECT_GROUP, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_select_group_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Select a Group from' to disappear ...")
        return ui_lib.wait_for_element_notvisible(AddDirectoryUserAndGroupElements.ID_DIALOG_SELECT_GROUP, timeout, fail_if_false)

    @classmethod
    def tick_role_specialized(cls, timeout=5):
        logger.debug("choose 'Role' as 'Specialized'")
        ui_lib.wait_for_element_and_click(AddDirectoryUserAndGroupElements.ID_RADIO_GOURP_ROLE_SPECIALIZED, timeout, fail_if_false=True)

    @classmethod
    def tick_role_full(cls, timeout=5):
        logger.debug("choose 'Full' as 'Specialized'")
        ui_lib.wait_for_element_and_click(AddDirectoryUserAndGroupElements.ID_RADIO_GOURP_ROLE_FULL, timeout, fail_if_false=True)

    @classmethod
    def tick_role_read_only(cls, timeout=5):
        logger.debug("choose 'Role' as 'Read only'")
        ui_lib.wait_for_element_and_click(AddDirectoryUserAndGroupElements.ID_RADIO_GOURP_ROLE_READ_ONLY, timeout, fail_if_false=True)

    @classmethod
    def tick_backup_administrator(cls, timeout=5):
        logger.debug("select 'Backup administrator' option ...")
        FusionUIBase.wait_for_checkbox_and_select(AddDirectoryUserAndGroupElements.ID_CHECKBOX_GOURP_BACKUP_ADMINISTRATOR, timeout, fail_if_false=True)

    @classmethod
    def untick_backup_administrator(cls, timeout=5):
        logger.debug("un-select 'Backup administrator' option ...")
        FusionUIBase.wait_for_checkbox_and_unselect(AddDirectoryUserAndGroupElements.ID_CHECKBOX_GOURP_BACKUP_ADMINISTRATOR, timeout, fail_if_false=True)

    @classmethod
    def tick_network_administrator(cls, timeout=5):
        logger.debug("select 'Network administrator' option ...")
        ui_lib.wait_for_element_and_click(AddDirectoryUserAndGroupElements.ID_CHECKBOX_GOURP_NETWORK_ADMINISTRATOR, timeout, fail_if_false=True)

    @classmethod
    def untick_network_administrator(cls, timeout=5):
        logger.debug("un-select 'Network administrator' option ...")
        FusionUIBase.wait_for_checkbox_and_unselect(AddDirectoryUserAndGroupElements.ID_CHECKBOX_GOURP_NETWORK_ADMINISTRATOR, timeout, fail_if_false=True)

    @classmethod
    def tick_server_administrator(cls, timeout=5):
        logger.debug("select 'Server administrator' option ...")
        FusionUIBase.wait_for_checkbox_and_select(AddDirectoryUserAndGroupElements.ID_CHECKBOX_GOURP_SERVER_ADMINISTRATOR, timeout, fail_if_false=True)

    @classmethod
    def untick_server_administrator(cls, timeout=5):
        logger.debug("un-select 'Server administrator' option ...")
        FusionUIBase.wait_for_checkbox_and_unselect(AddDirectoryUserAndGroupElements.ID_CHECKBOX_GOURP_SERVER_ADMINISTRATOR, timeout, fail_if_false=True)

    @classmethod
    def tick_storage_administrator(cls, timeout=5):
        logger.debug("select 'Storage administrator' option ...")
        FusionUIBase.wait_for_checkbox_and_select(AddDirectoryUserAndGroupElements.ID_CHECKBOX_GOURP_STORAGE_ADMINISTRATOR, timeout, fail_if_false=True)

    @classmethod
    def untick_storage_administrator(cls, timeout=5):
        logger.debug("un-select 'Storage administrator' option ...")
        FusionUIBase.wait_for_checkbox_and_unselect(AddDirectoryUserAndGroupElements.ID_CHECKBOX_GOURP_STORAGE_ADMINISTRATOR, timeout, fail_if_false=True)

    @classmethod
    def click_add_button(cls, timeout=5):
        logger.debug("click button 'Add'")
        ui_lib.wait_for_element_and_click(AddDirectoryUserAndGroupElements.ID_BTN_GROUP_ADD, timeout, fail_if_false=True)

    @classmethod
    def click_add_plus_button(cls, timeout=5):
        logger.debug("click button 'Add+'")
        ui_lib.wait_for_element_and_click(AddDirectoryUserAndGroupElements.ID_BTN_GROUP_ADD_PLUS, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(AddDirectoryUserAndGroupElements.ID_BTN_GROUP_ADD_CANCEL, timeout, fail_if_false=True)

    @classmethod
    def input_group_name(cls, name, timeout=5):
        logger.debug("input 'Group' as '%s'" % name)
        ui_lib.wait_for_element_and_input_text(AddDirectoryUserAndGroupElements.ID_INPUT_GROUP_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def input_add_group_user_name(cls, name, timeout=5):
        logger.debug("input 'User name' as '%s'" % name)
        ui_lib.wait_for_element_and_input_text(AddDirectoryUserAndGroupElements.ID_INPUT_ADD_GROUP_USER_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def input_add_group_password(cls, password, timeout=5):
        logger.debug("input 'Password' as '%s'" % password)
        ui_lib.wait_for_element_and_input_text(AddDirectoryUserAndGroupElements.ID_INPUT_ADD_GROUP_PASSWORD, password, timeout, fail_if_false=True)

    @classmethod
    def tick_add_group_show_password(cls, timeout=5):
        logger.debug("select 'Show password' option ...")
        FusionUIBase.wait_for_checkbox_and_select(AddDirectoryUserAndGroupElements.ID_CHECKBOX_ADD_GROUP_SHOW_PASSWORD, timeout, fail_if_false=True)

    @classmethod
    def untick_add_group_show_password(cls, timeout=5):
        logger.debug("un-select 'Show password' option ...")
        FusionUIBase.wait_for_checkbox_and_unselect(AddDirectoryUserAndGroupElements.ID_CHECKBOX_ADD_GROUP_SHOW_PASSWORD, timeout, fail_if_false=True)

    @classmethod
    def click_add_group_ok_button(cls, timeout=5):
        logger.debug("click button 'OK'")
        ui_lib.wait_for_element_and_click(AddDirectoryUserAndGroupElements.ID_BTN_ADD_GROUP_OK, timeout, fail_if_false=True)

    @classmethod
    def click_add_group_cancel_button(cls, timeout=5):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(AddDirectoryUserAndGroupElements.ID_BTN_GROUP_ADD_CANCEL, timeout, fail_if_false=True)

    @classmethod
    def input_select_group_user_name(cls, name, timeout=5):
        logger.debug("input 'User name' as '%s'" % name)
        ui_lib.wait_for_element_and_input_text(AddDirectoryUserAndGroupElements.ID_INPUT_SELECT_GROUP_USER_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def input_select_group_password(cls, password, timeout=5):
        logger.debug("input 'Password' as '%s'" % password)
        ui_lib.wait_for_element_and_input_text(AddDirectoryUserAndGroupElements.ID_INPUT_SELECT_GROUP_PASSWORD, password, timeout, fail_if_false=True)

    @classmethod
    def tick_select_group_show_password(cls, timeout=5):
        logger.debug("select 'Show password' option ...")
        FusionUIBase.wait_for_checkbox_and_select(AddDirectoryUserAndGroupElements.ID_CHECKBOX_SELECT_GROUP_SHOW_PASSWORD, timeout, fail_if_false=True)

    @classmethod
    def untick_select_group_show_password(cls, timeout=5):
        logger.debug("un-select 'Show password' option ...")
        FusionUIBase.wait_for_checkbox_and_unselect(AddDirectoryUserAndGroupElements.ID_CHECKBOX_SELECT_GROUP_SHOW_PASSWORD, timeout, fail_if_false=True)

    @classmethod
    def click_select_group_connect_button(cls, timeout=5):
        logger.debug("click button 'Connect'")
        ui_lib.wait_for_element_and_click(AddDirectoryUserAndGroupElements.ID_BTN_DIRECTORY_CONNECT, timeout, fail_if_false=True)

    @classmethod
    def click_select_group_connect_cancel_button(cls, timeout=5):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(AddDirectoryUserAndGroupElements.ID_BTN_DIRECTORY_CANCEL, timeout, fail_if_false=True)

    @classmethod
    def input_select_group_name(cls, name, timeout=5):
        logger.debug("input 'Group name' as '%s'" % name)
        ui_lib.wait_for_element_and_input_text(AddDirectoryUserAndGroupElements.ID_INPUT_SELECT_GROUP_NAME, name, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_and_click_group(cls, name, timeout=5, time_for_loading=3, fail_if_false=True):
        logger.debug("select group %s" % name)
        BuiltIn().sleep(time_for_loading)
        return ui_lib.wait_for_element_and_click(AddDirectoryUserAndGroupElements.ID_TEXT_SELECT_GROUP_NAME % name, timeout, fail_if_false)

    @classmethod
    def click_select_group_ok_button(cls, timeout=5):
        logger.debug("click button 'OK'")
        ui_lib.wait_for_element_and_click(AddDirectoryUserAndGroupElements.ID_BTN_SELECT_GROUP_OK, timeout, fail_if_false=True)

    @classmethod
    def click_select_group_cancel_button(cls, timeout=5):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(AddDirectoryUserAndGroupElements.ID_BTN_SELECT_GROUP_CANCEL, timeout, fail_if_false=True)


class RemoveDirectoryUserAndGroup(RemoveUser):

    pass


class EditGroup(FusionUIBase):

    @classmethod
    def click_action_edit_button(cls, timeout=5):
        logger.debug("click 'Edit' button")
        ui_lib.wait_for_element_and_click(GeneralUserandGroupsElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(GeneralUserandGroupsElements.ID_SELECT_ACTION_EDIT_USER, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_group_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Edit User' to show up ...")
        return ui_lib.wait_for_element_visible(EditDirectoryUserAndGroupElements.ID_DIALOG_EDIT_GROUP, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_group_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Edit User' to disappear ...")
        return ui_lib.wait_for_element_notvisible(EditDirectoryUserAndGroupElements.ID_DIALOG_EDIT_GROUP, timeout, fail_if_false)

    @classmethod
    def click_ok_button(cls, timeout=5):
        logger.debug("click button 'ok'")
        ui_lib.wait_for_element_and_click(EditDirectoryUserAndGroupElements.ID_BTN_EDIT_OK, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(EditDirectoryUserAndGroupElements.ID_BTN_EDIT_CANCEL, timeout, fail_if_false=True)

    @classmethod
    def tick_role_specialized(cls, timeout=5):
        logger.debug("choose 'Role' as 'Specialized'")
        ui_lib.wait_for_element_and_click(EditDirectoryUserAndGroupElements.ID_RADIO_EDIT_ROLE_SPECIALIZED, timeout, fail_if_false=True)

    @classmethod
    def tick_role_full(cls, timeout=5):
        logger.debug("choose 'Full' as 'Specialized'")
        ui_lib.wait_for_element_and_click(EditDirectoryUserAndGroupElements.ID_RADIO_EDIT_ROLE_FULL, timeout, fail_if_false=True)

    @classmethod
    def tick_role_read_only(cls, timeout=5):
        logger.debug("choose 'Role' as 'Read only'")
        ui_lib.wait_for_element_and_click(EditDirectoryUserAndGroupElements.ID_RADIO_EDIT_ROLE_READ_ONLY, timeout, fail_if_false=True)

    @classmethod
    def tick_backup_administrator(cls, timeout=5):
        logger.debug("select 'Backup administrator' option ...")
        FusionUIBase.wait_for_checkbox_and_select(EditDirectoryUserAndGroupElements.ID_CHECKBOX_EDIT_BACKUP_ADMINISTRATOR, timeout, fail_if_false=True)

    @classmethod
    def untick_backup_administrator(cls, timeout=5):
        logger.debug("un-select 'Backup administrator' option ...")
        FusionUIBase.wait_for_checkbox_and_unselect(EditDirectoryUserAndGroupElements.ID_CHECKBOX_EDIT_BACKUP_ADMINISTRATOR, timeout, fail_if_false=True)

    @classmethod
    def tick_network_administrator(cls, timeout=5):
        logger.debug("select 'Network administrator' option ...")
        FusionUIBase.wait_for_checkbox_and_select(EditDirectoryUserAndGroupElements.ID_CHECKBOX_EDIT_NETWORK_ADMINISTRATOR, timeout, fail_if_false=True)

    @classmethod
    def untick_network_administrator(cls, timeout=5):
        logger.debug("un-select 'Network administrator' option ...")
        FusionUIBase.wait_for_checkbox_and_unselect(EditDirectoryUserAndGroupElements.ID_CHECKBOX_EDIT_NETWORK_ADMINISTRATOR, timeout, fail_if_false=True)

    @classmethod
    def tick_server_administrator(cls, timeout=5):
        logger.debug("select 'Server administrator' option ...")
        FusionUIBase.wait_for_checkbox_and_select(EditDirectoryUserAndGroupElements.ID_CHECKBOX_EDIT_SERVER_ADMINISTRATOR, timeout, fail_if_false=True)

    @classmethod
    def untick_server_administrator(cls, timeout=5):
        logger.debug("un-select 'Server administrator' option ...")
        FusionUIBase.wait_for_checkbox_and_unselect(EditDirectoryUserAndGroupElements.ID_CHECKBOX_EDIT_SERVER_ADMINISTRATOR, timeout, fail_if_false=True)

    @classmethod
    def tick_storage_administrator(cls, timeout=5):
        logger.debug("select 'Storage administrator' option ...")
        FusionUIBase.wait_for_checkbox_and_select(EditDirectoryUserAndGroupElements.ID_CHECKBOX_EDIT_STORAGE_ADMINISTRATOR, timeout, fail_if_false=True)

    @classmethod
    def untick_storage_administrator(cls, timeout=5):
        logger.debug("un-select 'Storage administrator' option ...")
        FusionUIBase.wait_for_checkbox_and_unselect(EditDirectoryUserAndGroupElements.ID_CHECKBOX_EDIT_STORAGE_ADMINISTRATOR, timeout, fail_if_false=True)


class EditCurrentSessionUser(FusionUIBase):

    @classmethod
    def input_login_user_name(cls, name, timeout=50):
        logger.debug("input 'User' as '%s'" % name)
        ui_lib.wait_for_element_and_input_text(EditCurrentSessionUserElements.ID_INPUT_LOGIN_USER, name, timeout, fail_if_false=True)

    @classmethod
    def input_login_password(cls, password, timeout=5):
        logger.debug("input 'Password' as '%s'" % password)
        ui_lib.wait_for_element_and_input_text(EditCurrentSessionUserElements.ID_INPUT_LOGIN_PASSWORD, password, timeout, fail_if_false=True)

    @classmethod
    def click_login_button(cls, timeout=5):
        logger.debug("click button 'Login'")
        ui_lib.wait_for_element_and_click(EditCurrentSessionUserElements.ID_BTN_LOGIN_BUTTON, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_login_dashboard_shown(cls, timeout=30, fail_if_false=True):
        logger.info("waiting for 'Dashboard' to show up ...")
        return ui_lib.wait_for_element_visible(EditCurrentSessionUserElements.ID_PAGE_LABEL, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def login_to_appliance(cls, username, password, timeout=30, fail_if_false=True):
        logger.info("Login to appliance ...")
        cls.input_login_user_name(username)
        cls.input_login_password(password)
        cls.click_login_button()
        return cls.wait_login_dashboard_shown(timeout, fail_if_false)

    @classmethod
    def click_current_session_user_edit_button(cls, timeout=5):
        logger.debug("click button 'hp-session-user-edit'")
        ui_lib.wait_for_element_and_click(EditCurrentSessionUserElements.ID_SESSION_CONTROL, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditCurrentSessionUserElements.ID_BTN_EDIT_CURRENT_SESSION_USER, timeout, fail_if_false=True)

    @classmethod
    def click_logout_button(cls, timeout=5):
        logger.debug("click button 'Logout'")
        ui_lib.wait_for_element_and_click(EditCurrentSessionUserElements.ID_SESSION_CONTROL, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditCurrentSessionUserElements.ID_SESSION_LOGOUT, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_user_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Edit User' to show up ...")
        return ui_lib.wait_for_element_visible(EditCurrentSessionUserElements.ID_DIALOG_EDIT_CURRENT_USER, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_user_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Edit User' to disappear ...")
        return ui_lib.wait_for_element_notvisible(EditCurrentSessionUserElements.ID_DIALOG_EDIT_CURRENT_USER, timeout, fail_if_false)

    @classmethod
    def input_full_name(cls, name, timeout=5):
        logger.debug("input 'Full name' as '%s'" % name)
        ui_lib.wait_for_element_and_input_text(EditCurrentSessionUserElements.ID_INPUT_CURRENT_USER_FULL_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def input_current_password(cls, password, timeout=5):
        logger.debug("input 'Current password' as '%s'" % password)
        ui_lib.wait_for_element_and_input_text(EditCurrentSessionUserElements.ID_INPUT_CURRENT_PASSWORD, password, timeout, fail_if_false=True)

    @classmethod
    def input_new_password(cls, password, timeout=5):
        logger.debug("input 'New password' as '%s'" % password)
        ui_lib.wait_for_element_and_input_text(EditCurrentSessionUserElements.ID_INPUT_NEW_PASSWORD, password, timeout, fail_if_false=True)

    @classmethod
    def input_confirm_password(cls, password, timeout=5):
        logger.debug("input 'Confirm password' as '%s'" % password)
        ui_lib.wait_for_element_and_input_text(EditCurrentSessionUserElements.ID_INPUT_CONFIRM_PASSWORD, password, timeout, fail_if_false=True)

    @classmethod
    def input_email(cls, email, timeout=5):
        logger.debug("input 'Email' as '%s'" % email)
        ui_lib.wait_for_element_and_input_text(EditCurrentSessionUserElements.ID_INPUT_CURRENT_USER_EMAIL, email, timeout, fail_if_false=True)

    @classmethod
    def input_office_phone(cls, phone, timeout=5):
        logger.debug("input 'Office phone' as '%s'" % phone)
        ui_lib.wait_for_element_and_input_text(EditCurrentSessionUserElements.ID_INPUT_CURRENT_USER_OFFICE_PHN, phone, timeout, fail_if_false=True)

    @classmethod
    def input_mobile_phone(cls, phone, timeout=5):
        logger.debug("input 'Mobile phone' as '%s'" % phone)
        ui_lib.wait_for_element_and_input_text(EditCurrentSessionUserElements.ID_INPUT_CURRENT_USER_MOBILE_PHN, phone, timeout, fail_if_false=True)

    @classmethod
    def click_ok_button(cls, timeout=5):
        logger.debug("click button 'OK'")
        ui_lib.wait_for_element_and_click(EditCurrentSessionUserElements.ID_BTN_CONFIRM_EDIT, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click button 'OK'")
        ui_lib.wait_for_element_and_click(EditCurrentSessionUserElements.ID_BTN_CANCEL_EDIT, timeout, fail_if_false=True)


class VerifyUser(FusionUIBase):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_user_exist(cls, user_name, directory="Local", verifygroup=False, timeout=5, fail_if_false=False):
        logger.debug("verify user exist")
        if verifygroup and VerifyGroup.verify_group_mode(5, False):
            return ui_lib.wait_for_element(GeneralUserandGroupsElements.ID_USERS_TABLE_NAME % (user_name, directory), timeout, fail_if_false)
        else:
            return ui_lib.wait_for_element(GeneralUserandGroupsElements.ID_USERS_TABLE_NAME_SIMPLE % user_name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_user_not_exist(cls, user_name, directory="Local", verifygroup=False, timeout=5, fail_if_false=False):
        logger.debug("verify user not exist")
        if verifygroup and VerifyGroup.verify_group_mode(5, False):
            return ui_lib.wait_for_element_remove(GeneralUserandGroupsElements.ID_USERS_TABLE_NAME % (user_name, directory), timeout, fail_if_false)
        else:
            return ui_lib.wait_for_element_remove(GeneralUserandGroupsElements.ID_USERS_TABLE_NAME_SIMPLE % user_name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_user_title(cls, user_name, timeout=5, fail_if_false=True):
        logger.debug("verify user page title")
        return ui_lib.wait_for_element(VerifyUserElements.ID_TEXT_USER_TITLE % user_name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_user_login_name(cls, login_name, timeout=5, fail_if_false=True):
        logger.debug("verify user login name")
        return ui_lib.wait_for_element(VerifyUserElements.ID_TEXT_LOGIN_NAME % login_name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_user_full_name(cls, full_name, timeout=5, fail_if_false=True):
        logger.debug("verify user full name")
        return ui_lib.wait_for_element(VerifyUserElements.ID_TEXT_FULL_NAME % full_name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_user_role(cls, role, timeout=5, fail_if_false=True):
        logger.debug("verify user role")
        return ui_lib.wait_for_element(VerifyUserElements.ID_TEXT_ROLE % role, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_user_email(cls, email, timeout=5, fail_if_false=True):
        logger.debug("verify user email")
        return ui_lib.wait_for_element(VerifyUserElements.ID_TEXT_EMAIL % email, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_user_office_phone(cls, office_phone, timeout=5, fail_if_false=True):
        logger.debug("verify user office phone")
        return ui_lib.wait_for_element(VerifyUserElements.ID_TEXT_OFFICE_PHONE % office_phone, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_user_mobile_phone(cls, mobile_phone, timeout=5, fail_if_false=True):
        logger.debug("verify user mobile phone")
        return ui_lib.wait_for_element(VerifyUserElements.ID_TEXT_MOBILE_PHONE % mobile_phone, timeout, fail_if_false)


class VerifyGroup(FusionUIBase):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_group_mode(cls, timeout=5, fail_if_false=True):
        logger.debug("verify if appliance have directory")
        return ui_lib.wait_for_element(VerifyGroupElements.ID_TEXT_GROUP_MODE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_group_title(cls, user_name, timeout=5, fail_if_false=True):
        logger.debug("verify group page title")
        return ui_lib.wait_for_element(VerifyGroupElements.ID_TEXT_USER_TITLE % user_name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_group_name(cls, name, timeout=5, fail_if_false=True):
        logger.debug("verify group name")
        return ui_lib.wait_for_element(VerifyGroupElements.ID_TEXT_NAME % name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_group_directory(cls, directory, timeout=5, fail_if_false=True):
        logger.debug("verify group directory")
        return ui_lib.wait_for_element(VerifyGroupElements.ID_TEXT_DIRECTORY % directory, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_group_role(cls, role, timeout=5, fail_if_false=True):
        logger.debug("verify group role")
        return ui_lib.wait_for_element(VerifyGroupElements.ID_TEXT_ROLE % role, timeout, fail_if_false)

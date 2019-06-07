# (C) Copyright 2015 Hewlett-Packard Development Company, L.P.
"""
    Network Set Page
"""


from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco
from FusionLibrary.ui.business_logic.networking.networksets_elements import *
from FusionLibrary.ui.business_logic.base import FusionUIBase


class CommonOperationNetworkSets(object):

    @classmethod
    def select_network_set(cls, name, wait_timeout=5, fail_if_false=True):
        logger.debug("select network_set %s" % name)
        if not ui_lib.wait_for_element_and_click(GeneralNetworkSetsElements.ID_TABLE_NETWORK_SET_NAME % name, wait_timeout, fail_if_false):
            return False
        return ui_lib.wait_for_element(GeneralNetworkSetsElements.ID_VERIFY_NETWORK_SET_TITLE % name, wait_timeout, fail_if_false)

    @classmethod
    def get_network_sets_list(cls, timeout=5, fail_if_false=True):
        logger.debug("Get all network sets names from table")
        network_sets_list = []
        if ui_lib.wait_for_element(GeneralNetworkSetsElements.ID_TABLE_NETWORKSET_NAME_LIST, timeout, fail_if_false):
            network_sets_list = FusionUIBase.get_multi_elements_text(GeneralNetworkSetsElements.ID_TABLE_NETWORKSET_NAME_LIST, timeout, fail_if_false)
            logger.debug("network_set list %s" % network_sets_list)
            return network_sets_list
        else:
            logger.debug("failed to get network_set list")
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_network_set_load(cls, wait_timeout=10, fail_if_false=True):
        logger.debug("Determine if network sets load completely")
        return ui_lib.wait_for_element_visible(GeneralNetworkSetsElements.ID_PAGE_OVERVIEW, wait_timeout, fail_if_false)


class CreateNetworkSets(object):

    @classmethod
    def click_create_network_set_button(cls, wait_timeout=5):
        logger.debug("click create networkset button")
        ui_lib.wait_for_element_and_click(CreateNetworkSetsElements.ID_BUTTON_CREATE_NETWORK_SET, wait_timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_network_set_dialog_shown(cls, wait_timeout=5, fail_if_false=True):
        logger.debug('waiting create networkset dialog shown')
        return ui_lib.wait_for_element_visible(CreateNetworkSetsElements.ID_DIALOG_CREATE_NETWORK_SET, wait_timeout, fail_if_false)

    @classmethod
    def input_name(cls, name, wait_timeout=5):
        logger.debug("input networkset name '%s'" % name)
        ui_lib.wait_for_element_and_input_text(CreateNetworkSetsElements.ID_INPUT_NETWORK_SET_NAME, name, wait_timeout, fail_if_false=True)

    @classmethod
    def input_preferred_bandwidth(cls, bandwidth, wait_timeout=5):
        logger.debug("input preferred bandwidth '%s'" % bandwidth)
        ui_lib.wait_for_element_and_input_text(CreateNetworkSetsElements.ID_INPUT_NETWORK_SET_PREF_BANDWIDTH, bandwidth, wait_timeout, fail_if_false=True)

    @classmethod
    def input_maximum_bandwidth(cls, bandwidth, wait_timeout=5):
        logger.debug("input maximum bandwidth '%s'" % bandwidth)
        ui_lib.wait_for_element_and_input_text(CreateNetworkSetsElements.ID_INPUT_NETWORK_SET_MAXS_BANDWIDTH, bandwidth, wait_timeout, fail_if_false=True)

    @classmethod
    def click_add_networks_button(cls, wait_timeout=5):
        logger.debug("click add networks button")
        ui_lib.wait_for_element_and_click(CreateNetworkSetsElements.ID_BUTTON_ADD_NETWORK, wait_timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_network_dialog_shown(cls, wait_timeout=5, fail_if_false=True):
        logger.debug('waiting add networks dialog shown')
        return ui_lib.wait_for_element_visible(CreateNetworkSetsElements.ID_DIALOG_ADD_NETWORK, wait_timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_network_dialog_disappear(cls, wait_timeout=5, fail_if_false=True):
        logger.debug("wait create network dialog disappear")
        return ui_lib.wait_for_element_remove(CreateNetworkSetsElements.ID_DIALOG_ADD_NETWORK, wait_timeout, fail_if_false)

    @classmethod
    def select_untagged_checkbox(cls, name, wait_timeout=5):
        logger.debug("change network %s to untagged" % name)
        FusionUIBase.wait_for_checkbox_and_select(CreateNetworkSetsElements.ID_CHECKBOX_NETWORK_UNTAGGED % name, wait_timeout, fail_if_false=True)

    @classmethod
    def unselect_untagged_checkbox(cls, name, wait_timeout=5):
        logger.debug("change network %s to tagged" % name)
        FusionUIBase.wait_for_checkbox_and_unselect(CreateNetworkSetsElements.ID_CHECKBOX_NETWORK_UNTAGGED % name, wait_timeout, fail_if_false=True)

    @classmethod
    def remove_networks_by_name(cls, name, wait_timeout=5):
        logger.debug("remove network %s" % name)
        ui_lib.wait_for_element_and_click(CreateNetworkSetsElements.ID_BUTTON_REMOVE_NETWORK % name, wait_timeout, fail_if_false=True)

    @classmethod
    def input_network_name(cls, name, wait_timeout=5):
        logger.debug("input network name '%s'" % name)
        ui_lib.wait_for_element_and_input_text(CreateNetworkSetsElements.ID_INPUT_SEARCH_TEXT, name, wait_timeout, fail_if_false=True)

    @classmethod
    def click_network_name(cls, name, wait_timeout=5):
        logger.debug("click network name '%s'" % name)
        ui_lib.wait_for_element_and_click(CreateNetworkSetsElements.ID_TABLE_NETWORK_NAME % name, wait_timeout, fail_if_false=True)

    @classmethod
    def click_add_button(cls, wait_timeout=5):
        logger.debug("click add button")
        ui_lib.wait_for_element_and_click(CreateNetworkSetsElements.ID_BUTTON_ADD, wait_timeout, fail_if_false=True)

    @classmethod
    def click_add_plus_button(cls, wait_timeout=5):
        logger.debug("click add+ button")
        ui_lib.wait_for_element_and_click(CreateNetworkSetsElements.ID_BUTTON_ADD_AGAIN, wait_timeout, fail_if_false=True)

    @classmethod
    def click_cancel_add_network_button(cls, wait_timeout=5):
        logger.debug("click cancel button")
        ui_lib.wait_for_element_and_click(CreateNetworkSetsElements.ID_BUTTON_CANCEL, wait_timeout, fail_if_false=True)

    @classmethod
    def click_create_button(cls, wait_timeout=5):
        logger.debug("click create button")
        ui_lib.wait_for_element_and_click(CreateNetworkSetsElements.ID_BTN_CREATE_NETWORK_SET, wait_timeout, fail_if_false=True)

    @classmethod
    def click_create_plus_button(cls, wait_timeout=5):
        logger.debug("click create+ button")
        ui_lib.wait_for_element_and_click(CreateNetworkSetsElements.ID_BTN_CREATE_NETWORK_SET_PLUS, wait_timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, wait_timeout=5):
        logger.debug("click cancel button")
        ui_lib.wait_for_element_and_click(CreateNetworkSetsElements.ID_BTN_CLOSE_NETWORK_SET, wait_timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_network_set_dialog_disappear(cls, wait_timeout=10, fail_if_false=True):
        logger.debug("wait create network dialog disappear")
        return ui_lib.wait_for_element_remove(CreateNetworkSetsElements.ID_DIALOG_CREATE_NETWORK_SET, wait_timeout, fail_if_false)


class EditNetworkSets(object):

    @classmethod
    def click_edit_network_set_button(cls, wait_timeout=5):
        logger.debug("click edit networkset button")
        ui_lib.wait_for_element_and_click(EditNetworkSetsElements.ID_ACTION_MAIN_BTN, wait_timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditNetworkSetsElements.ID_ACTION_MENU_EDIT_NETWORK_SET, wait_timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_network_set_dialog_shown(cls, wait_timeout=5, fail_if_false=True):
        logger.debug('waiting edit networkset dialog shown')
        return ui_lib.wait_for_element_visible(EditNetworkSetsElements.ID_DIALOG_EDIT_NETWORK_SET, wait_timeout, fail_if_false)

    @classmethod
    def input_name(cls, name, wait_timeout=5):
        logger.debug("input networkset name '%s'" % name)
        ui_lib.wait_for_element_and_input_text(EditNetworkSetsElements.ID_INPUT_NETWORK_SET_NAME, name, wait_timeout, fail_if_false=True)

    @classmethod
    def input_preferred_bandwidth(cls, bandwidth, wait_timeout=5):
        logger.debug("input preferred bandwidth '%s'" % bandwidth)
        ui_lib.wait_for_element_and_input_text(EditNetworkSetsElements.ID_INPUT_NETWORK_SET_PREF_BANDWIDTH, bandwidth, wait_timeout, fail_if_false=True)

    @classmethod
    def input_maximum_bandwidth(cls, bandwidth, wait_timeout=5):
        logger.debug("input maximum bandwidth '%s'" % bandwidth)
        ui_lib.wait_for_element_and_input_text(EditNetworkSetsElements.ID_INPUT_NETWORK_SET_MAXS_BANDWIDTH, bandwidth, wait_timeout, fail_if_false=True)

    @classmethod
    def click_add_networks_button(cls, wait_timeout=5):
        logger.debug("click add networks button")
        ui_lib.wait_for_element_and_click(EditNetworkSetsElements.ID_BUTTON_ADD_NETWORK, wait_timeout, fail_if_false=True)

    @classmethod
    def select_untagged_checkbox(cls, name, wait_timeout=5):
        logger.debug("change network %s to untagged" % name)
        FusionUIBase.wait_for_checkbox_and_select(CreateNetworkSetsElements.ID_CHECKBOX_NETWORK_UNTAGGED % name, wait_timeout, fail_if_false=True)

    @classmethod
    def unselect_untagged_checkbox(cls, name, wait_timeout=5):
        logger.debug("change network %s to tagged" % name)
        FusionUIBase.wait_for_checkbox_and_unselect(EditNetworkSetsElements.ID_CHECKBOX_NETWORK_UNTAGGED % name, wait_timeout, fail_if_false=True)

    @classmethod
    def remove_networks_by_name(cls, name, wait_timeout=5):
        logger.debug("remove network %s" % name)
        ui_lib.wait_for_element_and_click(EditNetworkSetsElements.ID_BUTTON_REMOVE_NETWORK % name, wait_timeout, fail_if_false=True)

    @classmethod
    def input_network_name(cls, name, wait_timeout=5):
        logger.debug("input network name '%s'" % name)
        ui_lib.wait_for_element_and_input_text(EditNetworkSetsElements.ID_INPUT_SEARCH_TEXT, name, wait_timeout, fail_if_false=True)

    @classmethod
    def click_network_name(cls, name, wait_timeout=5):
        logger.debug("click network name '%s'" % name)
        ui_lib.wait_for_element_and_click(EditNetworkSetsElements.ID_TABLE_NETWORK_NAME % name, wait_timeout, fail_if_false=True)

    @classmethod
    def click_add_button(cls, wait_timeout=5):
        logger.debug("click add button")
        ui_lib.wait_for_element_and_click(EditNetworkSetsElements.ID_BUTTON_ADD, wait_timeout, fail_if_false=True)

    @classmethod
    def click_add_plus_button(cls, wait_timeout=5):
        logger.debug("click add+ button")
        ui_lib.wait_for_element_and_click(EditNetworkSetsElements.ID_BUTTON_ADD_AGAIN, wait_timeout, fail_if_false=True)

    @classmethod
    def click_cancel_add_network_button(cls, wait_timeout=5):
        logger.debug("click cancel button")
        ui_lib.wait_for_element_and_click(EditNetworkSetsElements.ID_BUTTON_CANCEL, wait_timeout, fail_if_false=True)

    @classmethod
    def click_ok_button(cls, wait_timeout=5):
        logger.debug("click ok button")
        ui_lib.wait_for_element_and_click(EditNetworkSetsElements.ID_BTN_UPDATE_NETWORK_SET, wait_timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, wait_timeout=5):
        logger.debug("click cancel button")
        ui_lib.wait_for_element_and_click(EditNetworkSetsElements.ID_BTN_CANCEL, wait_timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_network_set_dialog_disappear(cls, wait_timeout=10, fail_if_false=True):
        logger.debug("wait edit network set dialog disappear")
        return ui_lib.wait_for_element_remove(EditNetworkSetsElements.ID_DIALOG_EDIT_NETWORK_SET, wait_timeout, fail_if_false)


class DeleteNetworkSets(object):

    @classmethod
    def click_delete_network_set_button(cls, wait_timeout=5):
        logger.debug("click delete networkset button")
        ui_lib.wait_for_element_and_click(DeleteNetworkSetsElements.ID_ACTION_MAIN_BTN, wait_timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(DeleteNetworkSetsElements.ID_ACTION_MENU_DELETE_NETWORK_SET, wait_timeout, fail_if_false=True)

    @classmethod
    def click_yes_delete_button(cls, wait_timeout=5):
        logger.debug("click 'Yes, delete' button")
        ui_lib.wait_for_element_and_click(DeleteNetworkSetsElements.ID_BTN_DELETE_NETWORK_SET, wait_timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, wait_timeout=5):
        logger.debug("click cancel button")
        ui_lib.wait_for_element_and_click(DeleteNetworkSetsElements.ID_BTN_CANCEL, wait_timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_network_set_dialog_disappear(cls, wait_timeout=10, fail_if_false=True):
        logger.debug("wait delete network set dialog disappear")
        return ui_lib.wait_for_element_remove(DeleteNetworkSetsElements.ID_DIALOG_DELETE_NETWORK_SET, wait_timeout, fail_if_false)


class VerifyNetworkSets(object):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_network_set_existed(cls, name, wait_timeout=5, fail_if_false=True):
        logger.debug("verify networkset '%s' existed ..." % name)
        return ui_lib.wait_for_element(GeneralNetworkSetsElements.ID_TABLE_NETWORK_SET_NAME % name, wait_timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_add_network_existed(cls, name, wait_timeout=5, fail_if_false=False):
        logger.debug("verify network existed")
        if ui_lib.wait_for_element_visible(VerifyNetworkSetsElements.ID_ADD_NETWORKS_TABLE, 2, fail_if_false):
            return ui_lib.wait_for_element(VerifyNetworkSetsElements.ID_ADD_NETWORKS_TABLE_ITEM % name, wait_timeout, fail_if_false)
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_edit_network_existed(cls, name, wait_timeout=5, fail_if_false=False):
        logger.debug("verify network existed")
        if ui_lib.wait_for_element_visible(VerifyNetworkSetsElements.ID_EDIT_NETWORKS_TABLE, 2, fail_if_false):
            return ui_lib.wait_for_element(VerifyNetworkSetsElements.ID_EDIT_NETWORKS_TABLE_ITEM % name, wait_timeout, fail_if_false)
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_network_set_deleted(cls, name, wait_timeout=20, fail_if_false=True):
        logger.debug("verify delete networkset successful")
        return ui_lib.wait_for_element(VerifyNetworkSetsElements.ID_TABLE_NETWORK_SET_DELETED % name, wait_timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_all_network_sets_not_found(cls, wait_timeout=20, fail_if_false=True):
        logger.debug("verify all network sets not found")
        return ui_lib.wait_for_element(VerifyNetworkSetsElements.ID_TABLE_NETWORK_SETS_NOT_FOUND, wait_timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_network_deleted(cls, name, wait_timeout=10, fail_if_false=True):
        logger.debug("verify delete network successful")
        return ui_lib.wait_for_element_remove(VerifyNetworkSetsElements.ID_BUTTON_REMOVE_NETWORK % name, wait_timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_network_set_created(cls, name, wait_timeout=5, fail_if_false=True):
        logger.debug("verify create networkset successful")
        return ui_lib.wait_for_element(VerifyNetworkSetsElements.ID_VERIFY_NETWORK_SET_TITLE % name, wait_timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_network_set_bandwidth(cls, prefb, maxb, wait_timeout=5, fail_if_false=True):
        logger.debug("verify networkset bandwidth")
        if ui_lib.wait_for_element(VerifyNetworkSetsElements.ID_VERIFY_NETWORK_SET_PREF_BANDWIDTH % prefb, wait_timeout, fail_if_false) and ui_lib.wait_for_element(VerifyNetworkSetsElements.ID_VERIFY_NETWORK_SET_MAX_BANDWIDTH % maxb, wait_timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_create_plus_complete(cls, wait_timeout=10, fail_if_false=True):
        logger.debug("verify networkset create+ complete")
        if not ui_lib.wait_for_element_hidden(VerifyNetworkSetsElements.ID_CREATE_NETWORK_SET_FORM_MESSAGE, wait_timeout, False):
            ui_lib.fail_test("Network Set create failed")
        return ui_lib.wait_for_element_text(VerifyNetworkSetsElements.ID_INPUT_NETWORK_SET_NAME, "", wait_timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_network_set_networks(cls, network, wait_timeout=5, fail_if_false=True):
        logger.debug("verify networkset networks")
        return ui_lib.wait_for_element(VerifyNetworkSetsElements.ID_VERIFY_NETWORK_SET_NETWORK_NAME % network, wait_timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_network_set_networksid(cls, network, networkid, wait_timeout=5, fail_if_false=True):
        logger.debug("verify networkset networksid")
        return ui_lib.wait_for_element(VerifyNetworkSetsElements.ID_VERIFY_NETWORK_SET_NETWORK_VLAN % (network, networkid), wait_timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_network_set_network_untagged(cls, network, wait_timeout=5, fail_if_false=True):
        logger.debug("verify networkset networks untagged")
        ui_lib.wait_for_element(VerifyNetworkSetsElements.ID_VERIFY_NETWORK_SET_NETWORK_UNTAGGED % network, wait_timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_scope_should_exist_in_edit_page(cls, name, timeout=5, fail_if_false=True):
        logger.debug("verify [ scope '%s' ] exist in scope edit page" % name)
        return ui_lib.wait_for_element_visible(EditScopeElements.ID_TABLE_SCOPE_NAME % name, timeout, fail_if_false)


class _BaseEditScopeForNetworkSet(object):

    """
    This class holds all edit scope operation of NetworkSet
    It can work with C7000 & TBird
    """

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_edit_scope_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Click [ Edit ] button on enclosure scope page")
        if ui_lib.wait_for_element(EditScopeElements.ID_BUTTON_EDIT, timeout=timeout, fail_if_false=fail_if_false) \
                and ui_lib.wait_for_element_visible(EditScopeElements.ID_HEADER_SCOPE, timeout=timeout, fail_if_false=fail_if_false)\
                and ui_lib.wait_for_element_notvisible(EditScopeElements.ID_TEXT_SCOPE_NOT_LOAD, timeout=timeout, fail_if_false=fail_if_false):
            ui_lib.find_element_and_move(EditScopeElements.ID_HEADER_SCOPE)
            ui_lib.wait_for_element_visible(EditScopeElements.ID_BUTTON_EDIT, timeout=timeout, fail_if_false=fail_if_false)
            ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_EDIT, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_scope_dialog_open(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Edit ] dialog open")
        return ui_lib.wait_for_element_visible(EditScopeElements.ID_DIALOG_EDIT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_scope_dialog_close(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Edit ] dialog close")
        return ui_lib.wait_for_element_notvisible(EditScopeElements.ID_DIALOG_EDIT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_assign_scope_dialog_open(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Assign to Scopes ] dialog open")
        return ui_lib.wait_for_element_visible(EditScopeElements.ID_DIALOG_ASSIGN, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_assign_scope_dialog_close(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Assign to Scopes ] dialog close")
        return ui_lib.wait_for_element_notvisible(EditScopeElements.ID_DIALOG_ASSIGN, timeout, fail_if_false)

    @classmethod
    def click_ok_button(cls, timeout=5):
        logger.debug("click [ OK ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_OK, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    def click_close_button(cls, timeout=5):
        logger.debug("click [ Close ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_CLOSE, timeout, fail_if_false=True)

    @classmethod
    def click_assign_button(cls, timeout=5):
        logger.debug("click [ Assign ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_ASSIGN, timeout, fail_if_false=True)

    @classmethod
    def click_add_button(cls, timeout=5):
        logger.debug("click [ Add ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_ADD, timeout, fail_if_false=True)

    @classmethod
    def click_add_plus_button(cls, timeout=5):
        logger.debug("click [ Add+ ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_ADD_PLUS, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_assign_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_CANCEL_ASSIGN, timeout, fail_if_false=True)

    @classmethod
    def input_scope_name(cls, name, wait_timeout=5):
        logger.debug("input scope name '%s'" % name)
        ui_lib.wait_for_element_and_input_text(EditScopeElements.ID_INPUT_SEARCH_TEXT, name, wait_timeout, fail_if_false=True)

    @classmethod
    def click_scope_name(cls, name, wait_timeout=5):
        logger.debug("click the scope name '%s'" % name)
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_TABLE_SCOPE_NAME % name, wait_timeout, fail_if_false=True)

    @classmethod
    def click_remove_scope_icon(cls, name, wait_timeout=5):
        logger.debug("click to remove scope '%s'" % name)
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_TABLE_REMOVE_SCOPE % name, wait_timeout, fail_if_false=True)


class EditScopeForNetworkSet(_BaseEditScopeForNetworkSet):
    pass


class C7000EditScopeForNetworkSet(_BaseEditScopeForNetworkSet):
    pass


class TBirdEditScopeForNetworkSet(_BaseEditScopeForNetworkSet):
    pass

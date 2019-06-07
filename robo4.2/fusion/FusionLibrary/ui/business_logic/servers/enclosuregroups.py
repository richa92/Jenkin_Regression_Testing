# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
""" Fusion Enclosure Group UI page."""
from FusionLibrary.ui.business_logic.base import FusionUIBase
from datetime import datetime
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib
from robot.libraries.BuiltIn import BuiltIn
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco
from FusionLibrary.ui.business_logic.servers.enclosuregroups_elements import *


class _BaseCommonOperationEnclosureGroups(FusionUIBase):

    """
    This class holds all common operation of enclosure group.
    It also defines abstract methods which the subclass has different implementation for C7000 & TBird
    """
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_enclosure_group_not_exist(cls, enclosuregroup, timeout=5, fail_if_false=True):
        logger.debug("verify [ enclosure group '%s' ] should NOT exist" % enclosuregroup)
        return ui_lib.wait_for_element_notvisible(GeneralEnclosureGroupElements.ID_TABLE_ENCLOSURE_GROUP % enclosuregroup, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_enclosure_group_exist(cls, enclosuregroup, timeout=10, fail_if_false=True):
        logger.debug("verify [ enclosure group '%s' ] should exist" % enclosuregroup)
        return ui_lib.wait_for_element(GeneralEnclosureGroupElements.ID_TABLE_ENCLOSURE_GROUP % enclosuregroup, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_enclosure_group_status_ok(cls, enclosuregroup, timeout=10, fail_if_false=True):
        logger.debug("verify whether [ enclosure group '%s' ] is ok" % enclosuregroup)
        return ui_lib.wait_for_element_visible(GeneralEnclosureGroupElements.ID_STATUS_ENCLOSURE_GROUP_OK % enclosuregroup, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_enclosure_group_warn(cls, enclosuregroup, timeout=10, fail_if_false=True):
        logger.debug("verify whether [ enclosure group '%s' ] is warning" % enclosuregroup)
        return ui_lib.wait_for_element_visible(GeneralEnclosureGroupElements.ID_STATUS_ENCLOSURE_GROUP_WARN % enclosuregroup, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_enclosure_group_error(cls, enclosuregroup, timeout=10, fail_if_false=True):
        logger.debug("verify whether [ enclosure group '%s' ] is error" % enclosuregroup)
        return ui_lib.wait_for_element_visible(GeneralEnclosureGroupElements.ID_STATUS_ENCLOSURE_GROUP_ERROR % enclosuregroup, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_enclosure_group_seleted(cls, enclosuregroup, timeout=10, fail_if_false=True):
        logger.debug("verify whether [ enclosure group '%s' ] is seleted" % enclosuregroup)
        return ui_lib.wait_for_element(GeneralEnclosureGroupElements.ID_TABLE_ENCLOSURE_GROUP_SELECTED % enclosuregroup, timeout, fail_if_false)

    @classmethod
    def get_enclosure_group_list(cls, timeout=5):
        logger.debug("Get all [ enclosure group names ] from table")
        enclosure_group_name_list = []
        if ui_lib.wait_for_element(GeneralEnclosureGroupElements.ID_TABLE_ENCLOSURE_GROUPS):
            enclosure_group_name_list = FusionUIBase.get_multi_elements_text(GeneralEnclosureGroupElements.ID_TABLE_ENCLOSURE_GROUPS, timeout, fail_if_false=True)
        return enclosure_group_name_list

    @classmethod
    def click_enclosure_group(cls, enclosuregroup, timeout=5):
        logger.debug("select [ enclosure group '%s' ]" % enclosuregroup)
        ui_lib.wait_for_element_and_click(GeneralEnclosureGroupElements.ID_TABLE_ENCLOSURE_GROUP % enclosuregroup, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_activity_action_ok(cls, enclosuregroup, timeout=600, fail_if_false=True):
        logger.debug("waiting [ activity action of enclosure group '%s' ] change to ok" % enclosuregroup)
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralEnclosureGroupElements.ID_TEXT_ACTIVITY_ACTION_OK % enclosuregroup, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralEnclosureGroupElements.ID_TEXT_ACTIVITY_ACTION_TITLE % enclosuregroup)
                logger.debug("[ activity action '%s' status ] is ok as expected." % actionname)
                return True
            elif ui_lib.wait_for_element_visible(GeneralEnclosureGroupElements.ID_TEXT_ACTIVITY_ACTION_WARN % enclosuregroup, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralEnclosureGroupElements.ID_TEXT_ACTIVITY_ACTION_TITLE % enclosuregroup)
                logger.debug("[ activity action '%s' status ] is warn not as expected." % actionname)
                ui_lib.wait_for_element_and_click(GeneralEnclosureGroupElements.ID_TEXT_ACTIVITY_ACTION_WARN % enclosuregroup)
                msg = FusionUIBase.get_multi_elements_text(GeneralEnclosureGroupElements.ID_TEXT_ACTIVITY_MESSAGE)
                # bypass specific warning message when delete monitored enclosure
                msg = [s for s in msg if msg != ''][0]
#                 if 'Resolution Delete the HPOneViewMonitor user manually on Onboard Administrator.' in msg:
#                     logger.debug("warning message [ %s ] is expected after deleting monitored enclosure." % msg)
#                     return True
                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            elif ui_lib.wait_for_element_visible(GeneralEnclosureGroupElements.ID_TEXT_ACTIVITY_ACTION_ERROR % enclosuregroup, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralEnclosureGroupElements.ID_TEXT_ACTIVITY_ACTION_TITLE % enclosuregroup)
                logger.debug("[ activity action '%s' status ] is error not as expected." % actionname)
                ui_lib.wait_for_element_and_click(GeneralEnclosureGroupElements.ID_TEXT_ACTIVITY_ACTION_ERROR % enclosuregroup)
                msg = FusionUIBase.get_multi_elements_text(GeneralEnclosureGroupElements.ID_TEXT_ACTIVITY_MESSAGE)
                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            else:
                if ui_lib.wait_for_element_visible(GeneralEnclosureGroupElements.ID_TEXT_ACTIVITY_ACTION_TITLE % enclosuregroup):
                    actionname = FusionUIBase.get_text(GeneralEnclosureGroupElements.ID_TEXT_ACTIVITY_ACTION_TITLE % enclosuregroup)
                else:
                    actionname = 'None'
                logger.debug("[ activity action '%s' status ] is unknown, waiting ..." % actionname)
                continue
        err_msg = "Timeout to waiting [ activity action ] completed."
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    def is_panel_selector_active(cls, timeout=5):
        logger.debug("check [ Panel Selector(General/View) ] is active")
        return ui_lib.is_visible(CreateEnclosureGroupElements.ID_PANEL_SELECTOR_IS_ACTIVE, timeout, fail_if_false=False)

    @classmethod
    def open_panel_selector(cls, timeout=5):
        logger.debug("Open [ Panel Selector(General/View) ]")
        if _BaseCommonOperationEnclosureGroups.is_panel_selector_active():
            return True

        return ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_PANEL_SELECTOR, timeout, fail_if_false=True)

    @classmethod
    def close_panel_selector(cls, timeout=5):
        logger.debug("click [ Panel Selector(General/View) ] if it's active")
        if not _BaseCommonOperationEnclosureGroups.is_panel_selector_active():
            return True

        return ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_PANEL_SELECTOR_IS_ACTIVE, timeout, fail_if_false=True)

    @classmethod
    def click_panel_selector_general(cls, timeout=5):
        _BaseCommonOperationEnclosureGroups.open_panel_selector()
        return ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_PANEL_SELECTOR_GENERAL, timeout, fail_if_false=True)

    @classmethod
    def is_panel_general_active(cls, timeout=5):
        logger.debug("check [ General ] panel active")
        return ui_lib.is_visible(CreateEnclosureGroupElements.ID_PANEL_GENERAL_IS_ACTIVE, timeout, fail_if_false=False)

    @classmethod
    def click_panel_selector_lig(cls, timeout=5):
        _BaseCommonOperationEnclosureGroups.open_panel_selector()
        return ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_PANEL_SELECTOR_LIG, timeout, fail_if_false=True)

    @classmethod
    def is_panel_lig_active(cls, timeout=5):
        logger.debug("check [ Interconnect bay configuration ] panel active")
        return ui_lib.is_visible(CreateEnclosureGroupElements.ID_PANEL_LIG_IS_ACTIVE, timeout, fail_if_false=False)

    @classmethod
    def click_actions_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Action ]  menu")
        ui_lib.wait_for_element_and_click(GeneralEnclosureGroupElements.ID_BUTTON_ACTIONS, timeout, fail_if_false)

    @classmethod
    def get_message_on_action_button(cls, timeout=5, fail_if_false=True):
        logger.debug("get message for after click on [ Action ] button")
        return FusionUIBase.get_text(GeneralEnclosureGroupElements.ID_TEXT_ON_ACTION_ENCLOSURE_GROUP, timeout, fail_if_false)


class C7000CommonOperationEnclosureGroups(_BaseCommonOperationEnclosureGroups):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_enclosure_group_logical_interconnect_group(cls, bay, logical_interconnect_group, timeout=5, fail_if_false=True):
        logger.debug("verify EG logical interconnect group, except value is  bay[%s]  LIG[%s]" % (bay, logical_interconnect_group))
        return ui_lib.wait_for_element(GeneralEnclosureGroupElements.ID_TEXT_C7000_LIG % (bay, logical_interconnect_group), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_enclosure_group_configuration_script(cls, script, timeout=5, fail_if_false=True):
        logger.debug("verify EG configuration script, except value is [%s]" % script)
        return ui_lib.wait_for_element(GeneralEnclosureGroupElements.ID_TEXT_C7000_SCRIPT % script, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_enclosure_group_enclosure_related(cls, enclosure, timeout=5, fail_if_false=True):
        return ui_lib.wait_for_element(GeneralEnclosureGroupElements.ID_TEXT_C7000_ENCLOSURE_RELATED % enclosure, timeout, fail_if_false)

    @classmethod
    def click_panel_selector_configscript(cls, timeout=5):
        logger.debug("click panel selector [Configuration script]")
        _BaseCommonOperationEnclosureGroups.open_panel_selector()
        return ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_PANEL_SELECTOR_CONFIGSCRIPT, timeout, fail_if_false=True)

    @classmethod
    def is_panel_configscript_active(cls, timeout=5):
        logger.debug("check [ Configuration script ] panel active")
        return ui_lib.is_visible(CreateEnclosureGroupElements.ID_PANEL_CONFIGSCRIPT_IS_ACTIVE, timeout, fail_if_false=False)


class CommonOperationEnclosureGroups(_BaseCommonOperationEnclosureGroups):
    pass


class TBirdCommonOperationEnclosureGroups(_BaseCommonOperationEnclosureGroups):
    pass


class _BaseCreateEnclosureGroups(FusionUIBase):

    @classmethod
    def click_create_enclosure_group_button(cls, timeout=5):
        logger.debug("click [ Create enclosure group ] button")
        ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_BUTTON_CREATE_ENCLOSURE_GROUP, timeout, fail_if_false=True)

    @classmethod
    def select_actions_create(cls, timeout=5):
        logger.debug("select [ Create ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralEnclosureGroupElements.ID_BUTTON_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_ACTION_CREATE_ENCLOSURE_GROUP, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_enclosure_group_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Create Enclosure Group] dialog shown")
        return ui_lib.wait_for_element_visible(CreateEnclosureGroupElements.ID_DIALOG_CREATE_ENCLOSURE_GROUP, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_enclosure_group_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Create Enclosure Group] dialog disappear")
        return ui_lib.wait_for_element_notvisible(CreateEnclosureGroupElements.ID_DIALOG_CREATE_ENCLOSURE_GROUP, timeout, fail_if_false)

    @classmethod
    def input_enclosure_group_name(cls, name, timeout=5):
        logger.debug("input [ Enclosure Group name ] '%s'" % name)
        ui_lib.wait_for_element_and_input_text(CreateEnclosureGroupElements.ID_INPUT_ENC_GROUP_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def input_configuration_script(cls, script, timeout=5):
        logger.debug("input [ Configuration script ] '%s'" % script)
        ui_lib.wait_for_element_and_input_text(CreateEnclosureGroupElements.ID_INPUT_CONFIG_SCRIPT, script, timeout, fail_if_false=True)

    @classmethod
    def click_create_button(cls, timeout=5):
        logger.debug("click [ Create ] button")
        ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_BUTTON_ENCLOSURE_GROUP_CREATE, timeout, fail_if_false=True)

    @classmethod
    def click_create_plus_button(cls, timeout=5):
        logger.debug("click [ Create+ ] button")
        ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_BUTTON_ENCLOSURE_GROUP_CREATE_PLUS, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_BUTTON_ENCLOSURE_GROUP_CANCEL, timeout, fail_if_false=True)

    @classmethod
    def is_create_enclosure_group_dialog_open(cls, timeout=5):
        logger.debug("check if [ Create Enclosure Group dialog ] is open")
        if not ui_lib.is_visible(CreateEnclosureGroupElements.ID_DIALOG_CREATE_ENCLOSURE_GROUP, timeout, fail_if_false=False):
            return False

        return True

    @classmethod
    def is_edit_enclosure_group_dialog_open(cls, timeout=5):
        logger.debug("check if [ Edit Enclosure Group dialog ] is open")
        if not ui_lib.is_visible(EditEnclosureGroupElements.ID_DIALOG_EDIT_ENCLOSURE_GROUP, timeout, fail_if_false=False):
            return False

        return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_change_lig_confirm_dialog_visible(cls, timeout=5, fail_if_false=False):
        logger.debug("wait [ Select Logical Interconnect Group ] dialog shown")
        return ui_lib.wait_for_element_visible(CreateEnclosureGroupElements.ID_DIALOG_CHANGE_LIG_CONFIRM, timeout, fail_if_false)

    @classmethod
    def click_select_lig_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Click [ Yes, select ] button")
        return ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_BUTTON_CHANGE_LIG_CONFIRM, timeout, fail_if_false)

    @classmethod
    def click_cancel_select_lig_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Click [ Cancel ] button")
        return ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_BUTTON_CANCEL_CHANGE_LIG_CONFIRM, timeout, fail_if_false)


class CreateEnclosureGroups(_BaseCreateEnclosureGroups):
    pass


class TBirdCreateEnclosureGroups(_BaseCreateEnclosureGroups):

    @classmethod
    def select_enclosure_count(cls, enclosure_count, timeout=5):
        logger.debug("select [ Enclosure count '%s' ] in General view" % enclosure_count)
        FusionUIBase.choose_option_by_text(CreateEnclosureGroupElements.ID_TBIRD_SELECT_ENCLOSURE_COUNT, enclosure_count, timeout, fail_if_false=True)

    @classmethod
    def select_deployment_network_type(cls, deployment_network_type, timeout=5):
        logger.debug("select [ Deployment network type '%s' ] in OS Deployment Settings view" % deployment_network_type)
        FusionUIBase.choose_option_by_text(CreateEnclosureGroupElements.ID_TBIRD_SELECT_DEPLOYMENT_NETWORK_TYPE, deployment_network_type, timeout, fail_if_false=True)

    @classmethod
    def tick_ipv4_addresses_use_address_pool(cls, timeout=5):
        logger.debug("tick option [ Use address pool ] of [ IPv4 addresses ] in General view")
        FusionUIBase.wait_for_checkbox_and_select(CreateEnclosureGroupElements.ID_TBIRD_RADIO_IPV4_ADDRESSES_USE_ADDRESS_POOL, timeout, fail_if_false=True)

    @classmethod
    def tick_ipv4_addresses_use_dhcp(cls, timeout=5):
        logger.debug("tick option [ Use DHCP ] of [ IPv4 addresses ] in General view")
        FusionUIBase.wait_for_checkbox_and_select(CreateEnclosureGroupElements.ID_TBIRD_RADIO_IPV4_ADDRESSES_USE_DHCP, timeout, fail_if_false=True)

    @classmethod
    def tick_ipv4_addresses_manage_externally(cls, timeout=5):
        logger.debug("tick option [ Manage externally ] of [ IPv4 addresses ] in General view")
        FusionUIBase.wait_for_checkbox_and_select(CreateEnclosureGroupElements.ID_TBIRD_RADIO_IPV4_ADDRESSES_USE_MANAGE_EXTERNALLY, timeout, fail_if_false=True)

    @classmethod
    def make_choose_lig_input_into_viewpoint(cls, enc_no, switch_no, timeout=5):
        logger.debug("Get [ Choose LIG input control<enclosure: %s, bay: %s> into view point ]" % (enc_no, switch_no))
        FusionUIBase.scroll_element_into_viewpoint(CreateEnclosureGroupElements.ID_TBIRD_INPUT_CHOOSE_LIG % (enc_no, switch_no))

    @classmethod
    def click_search_combo_box_menu(cls, enc_no, switch_no, timeout=5, fail_if_false=True):
        logger.debug("Click [ Combo box menu for <enclosure: %s, bay %s> to display optional ligs]" % (enc_no, switch_no))
        return ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_TBIRD_EG_LIG_OPTIONS_SEARCH_BUTTON % (enc_no, str(switch_no)), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_search_combo_menu_visible(cls, enc_no, switch_no, timeout=5, fail_if_false=True):
        logger.debug("wait [ Search Combo Menu ] shown")
        return ui_lib.wait_for_element_visible(CreateEnclosureGroupElements.ID_TBIRD_COMBO_ACTIVE_SEARCH_MENU % (enc_no, str(switch_no)), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_search_combo_menu_invisible(cls, enc_no, switch_no, timeout=5, fail_if_false=True):
        logger.debug("wait [ Search combo menu ] disappear")
        return ui_lib.wait_for_element_notvisible(CreateEnclosureGroupElements.ID_TBIRD_COMBO_ACTIVE_SEARCH_MENU % (enc_no, str(switch_no)), timeout, fail_if_false)

    @classmethod
    def input_select_lig(cls, enc_no, switch_no, switch_lig, timeout=5):
        logger.debug("input and select logical interconnect group [ %s ] for <enclosure: %s, bay: %s>" % (switch_lig, enc_no, switch_no))
        ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_COMBO_SEARCH_LIG % (enc_no, switch_no), timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_TBIRD_INPUT_LIG_CLEAR % (enc_no, switch_no), timeout, fail_if_false=True)
        ui_lib.wait_for_element_visible(CreateEnclosureGroupElements.ID_TBIRD_CHOOSE_LIG_LAYER % (enc_no, switch_no), timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_TBIRD_SELECT_OPTION_CHOOSE_LIG % (enc_no, switch_no, switch_lig), timeout, fail_if_false=True, js_click=True)
        ui_lib.wait_for_element_hidden(CreateEnclosureGroupElements.ID_TBIRD_CHOOSE_LIG_LAYER % (enc_no, switch_no), timeout, fail_if_false=True)

    @classmethod
    def select_power_mode(cls, power_mode, timeout=5):
        logger.debug("select [ Power mode '%s' ] in Power view" % power_mode)
        FusionUIBase.choose_option_by_text(CreateEnclosureGroupElements.ID_TBIRD_SELECT_POWER_MODE, power_mode, timeout, fail_if_false=True)

    @classmethod
    def click_panel_selector_power(cls, timeout=5):
        _BaseCommonOperationEnclosureGroups.open_panel_selector()
        return ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_TBIRD_PANEL_SELECTOR_POWER, timeout, fail_if_false=True)

    @classmethod
    def is_panel_power_active(cls, timeout=5):
        logger.debug("check [ Power ] panel active")
        return ui_lib.is_visible(CreateEnclosureGroupElements.ID_TBIRD_PANEL_POWER_IS_ACTIVE, timeout, fail_if_false=False)

    @classmethod
    def input_lig(cls, enc_no, switch_no, switch_lig, timeout=5, fail_if_false=True):
        logger.debug("input logical interconnect group [ %s ] for <enclosure: %s, bay: %s>" % (switch_lig, enc_no, switch_no))
        ui_lib.wait_for_element_and_input_text(CreateEnclosureGroupElements.ID_TBIRD_INPUT_CHOOSE_LIG % (enc_no, switch_no), switch_lig, timeout, fail_if_false)

    @classmethod
    def get_combo_header_for_lig(cls, enc_no, switch_no, timeout=5, fail_if_false=True):
        logger.debug("verify search combo menu for input lig")
        return FusionUIBase.get_text(CreateEnclosureGroupElements.ID_TBIRD_EG_SEARCH_COMBO_MENU_HEADER % (enc_no, str(switch_no)), timeout, fail_if_false)

    @classmethod
    def select_none_for_lig(cls, enc_no, switch_no, timeout=5, fail_if_false=True):
        logger.debug("select None for lig")
        ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_TBIRD_EG_LIG_OPTIONS_SEARCH_BUTTON % (enc_no, str(switch_no)), timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_TBIRD_EG_LIG_DROPDOWN_OPTIONS % (enc_no, str(switch_no), 'None'), timeout, fail_if_false)

    @classmethod
    def select_lig(cls, enc_no, switch_no, switch_lig, timeout=5, fail_if_false=True):
        logger.debug("select %s for lig" % switch_lig)
        # select the existing LIG from dropdown.If not present raise warning
        if ui_lib.wait_for_element_visible(CreateEnclosureGroupElements.ID_TBIRD_SELECT_OPTION_CHOOSE_LIG % (enc_no, switch_no, switch_lig), timeout, fail_if_false):
            ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_TBIRD_SELECT_OPTION_CHOOSE_LIG % (enc_no, switch_no, switch_lig), timeout, fail_if_false=False, js_click=True)
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_add_address_range_button(cls, timeout=5, fail_if_false=True):
        logger.info("click [ Add Address Ranges ] button for IP Range")
        return ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_BUTTON_CREATE_ENCLOSUREGROUP_ADD_ADDRESS_RANGES, timeout, fail_if_false)

    @classmethod
    def get_eg_change_confirm_prompt(cls, new_lig, timeout=5, fail_if_false=True):
        logger.debug("get [ encgroups change prompt ] for lig %s" % new_lig)
        return ui_lib.get_text(CreateEnclosureGroupElements.ID_TEXT_EG_CHANGE_PROMPT, timeout, fail_if_false)


class C7000CreateEnclosureGroups(_BaseCreateEnclosureGroups):

    @classmethod
    def input_select_logical_interconnect_group(cls, bay, logical_interconnect_group, timeout=5):
        logger.debug("choose LIG '%s' for bay '%s'" % (logical_interconnect_group, bay))
        ui_lib.wait_for_element_and_input_text(CreateEnclosureGroupElements.ID_INPUT_C7000_CHOOSE_LIG % bay, "", timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_input_text(CreateEnclosureGroupElements.ID_INPUT_C7000_CHOOSE_LIG % bay, logical_interconnect_group, timeout, fail_if_false=True)
        BuiltIn().sleep(3)
        ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_COMBO_C7000_OPTION_LIG % (bay, logical_interconnect_group), timeout, fail_if_false=True)

    @classmethod
    def input_configuration_script(cls, script, timeout=5):
        logger.debug("input [ Configuration script ] '%s'" % script)
        ui_lib.wait_for_element_and_input_text(CreateEnclosureGroupElements.ID_INPUT_CONFIG_SCRIPT, script, timeout, fail_if_false=True)


class _BaseDeleteEnclosureGroups(FusionUIBase):

    @classmethod
    def select_actions_delete(cls, timeout=5):
        logger.debug("select [ Delete ] action button")
        ui_lib.wait_for_element_and_click(GeneralEnclosureGroupElements.ID_BUTTON_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(DeleteEnclosureGroupElements.ID_MENU_ACTION_ENC_GRP_DELETE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Delete ] dialog shown")
        return ui_lib.wait_for_element_visible(DeleteEnclosureGroupElements.ID_DIALOG_DELETE_ENCLOSURE_GROUP, timeout, fail_if_false)

    @classmethod
    def click_yes_delete_button(cls, timeout=5):
        logger.debug("click [ Yes, delete ] button")
        ui_lib.wait_for_element_and_click(DeleteEnclosureGroupElements.ID_BUTTON_DELETE_ENCGRP_CONFIRM, timeout, fail_if_false=True)

    @classmethod
    def click_close_button(cls, timeout=5):
        logger.debug("click [ Close ] button")
        ui_lib.wait_for_element_and_click(DeleteEnclosureGroupElements.ID_BUTTON_DELETE_ENCGRP_CLOSE, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(DeleteEnclosureGroupElements.ID_BUTTON_DELETE_ENCGRP_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_dialog_disappear(cls, timeout=30, fail_if_false=True):
        logger.debug("wait [ Delete ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(DeleteEnclosureGroupElements.ID_DIALOG_DELETE_ENCLOSURE_GROUP, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_enclosure_group_show_not_found(cls, enclosuregroup, timeout=5, fail_if_false=True):
        logger.info("wait [ Enclosure Group %s status ] change to 'not found'" % enclosuregroup)
        return ui_lib.wait_for_element_visible(DeleteEnclosureGroupElements.ID_ELEMENT_ENC_GRP_DELETED % enclosuregroup, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_all_enclosure_groups_not_found(cls, timeout=5, fail_if_false=True):
        logger.info("wait [ Enclosure Group status ] show 'No enclosure_groups'")
        return ui_lib.wait_for_element_visible(DeleteEnclosureGroupElements.ID_ELEMENT_ENC_GRP_NOT_FOUND, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_enclosure_group_cannot_delete(cls, timeout=5, fail_if_false=True):
        logger.debug("verify [ enclosure group ] can't be deleted")
        return ui_lib.wait_for_element_visible(GeneralEnclosureGroupElements.ID_DIALOG_DELETE_REFUSE, timeout, fail_if_false)

    @classmethod
    def get_delete_error_text(cls, timeout=5, fail_if_false=True):
        logger.debug("Get  [ Delete Enclosure group error ] text")
        return FusionUIBase.get_text(DeleteEnclosureGroupElements.ID_ERROR_MSG_FOR_DELETE_ENCLOSURE_GROUP, timeout, fail_if_false)

    @classmethod
    def get_delete_error_message_confirm_details(cls, timeout=5, fail_if_false=True):
        logger.debug("Get  [ Delete Enclosure group confirm details ] text")
        return FusionUIBase.get_text(GeneralEnclosureGroupElements.ID_DIALOG_DELETE_REFUSE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_error_dialog_disappears(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Delete ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(GeneralEnclosureGroupElements.ID_DIALOG_DELETE_REFUSE, timeout, fail_if_false)


class DeleteEnclosureGroups(_BaseDeleteEnclosureGroups):
    pass


class TBirdDeleteEnclosureGroups(_BaseDeleteEnclosureGroups):
    pass


class C7000DeleteEnclosureGroups(_BaseDeleteEnclosureGroups):
    pass


class _BaseEditEnclosureGroups(FusionUIBase):

    """
    This class holds all operation when editing enclosure.
    It also defines abstract methods which the subclass has different implementation for C7000 & TBird
    """

    @classmethod
    def select_actions_edit(cls, timeout=5):
        logger.debug("select [ Edit ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralEnclosureGroupElements.ID_BUTTON_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditEnclosureGroupElements.ID_ACTION_EDIT_ENCLOSURE_GROUP, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_enclosure_group_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Edit Enclosure Group] dialog shown")
        return ui_lib.wait_for_element_visible(EditEnclosureGroupElements.ID_DIALOG_EDIT_ENCLOSURE_GROUP, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_enclosure_group_confirm_dialog_shown(cls, timeout=5, fail_if_false=False):
        logger.debug("wait [ Select Logical Interconnect Group ] dialog shown")
        return ui_lib.wait_for_element_visible(EditEnclosureGroupElements.ID_DIALOG_EDIT_ENCLOSURE_GROUP_CONFIRM, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_enclosure_group_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Edit Enclosure Group] dialog disappear")
        return ui_lib.wait_for_element_notvisible(EditEnclosureGroupElements.ID_DIALOG_EDIT_ENCLOSURE_GROUP, timeout, fail_if_false)

    @classmethod
    def click_ok_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ OK ] button")
        ui_lib.wait_for_element_and_click(EditEnclosureGroupElements.ID_BUTTON_ENCLOSURE_GROUP_OK, timeout, fail_if_false)

    @classmethod
    def click_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(EditEnclosureGroupElements.ID_BUTTON_ENCLOSURE_GROUP_CANCEL, timeout, fail_if_false)


class EditEnclosureGroups(_BaseEditEnclosureGroups):
    pass


class TBirdEditEnclosureGroups(_BaseEditEnclosureGroups):

    @classmethod
    def click_remove_iprange_option(cls, rangename, timeout=5, fail_if_false=True):
        logger.debug("click [ remove ] option")
        ui_lib.wait_for_element_and_click(EditEnclosureGroupElements.ID_EDIT_EG_REMOVE_IP_RANGE % rangename, timeout, fail_if_false)

    @classmethod
    def click_edit_delete_iprange_confirm(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Yes, delete ] button for IP Range")
        ui_lib.wait_for_element_and_click(EditEnclosureGroupElements.ID_EDIT_DELETE_BUTTON_IPRANGE_CONFIRM, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_add_address_range_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add Address Ranges ] button for IP Range")
        return ui_lib.wait_for_element_and_click(EditEnclosureGroupElements.ID_BUTTON_ENCLOSUREGROUP_EDIT_ADD_ADDRESS_RANGES, timeout, fail_if_false)

    @classmethod
    def click_on_iprange_name(cls, rangename, timeout=5, fail_if_false=True):
        logger.debug("click for [ Range name] in table")
        ui_lib.wait_for_element_and_click(GeneralEnclosureGroupElements.ID_SELECT_ENCLOSUREGROUP_IPRANGE_NAME % rangename, timeout, fail_if_false)

    @classmethod
    def click_add_iprange_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click  [ Add] button")
        ui_lib.wait_for_element_and_click(GeneralEnclosureGroupElements.ID_BUTTON_ENCLOSURE_GROUP_ADD_RANGE, timeout, fail_if_false)

    @classmethod
    def click_cancel_iprange_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click  [ Add] button")
        ui_lib.wait_for_element_and_click(GeneralEnclosureGroupElements.ID_BUTTON_ENCLOSURE_GROUP_CANCEL_RANGE, timeout, fail_if_false)

    @classmethod
    def input_select_lig(cls, enc_no, switch_no, switch_lig, timeout=5):
        logger.debug("input and select logical interconnect group [ %s ] for <enclosure: %s, bay: %s>" % (switch_lig, enc_no, switch_no))
        BuiltIn().sleep(5)
        ui_lib.wait_for_element_and_input_text(CreateEnclosureGroupElements.ID_TBIRD_INPUT_CHOOSE_LIG % (enc_no, switch_no), switch_lig, timeout, fail_if_false=True)
        ui_lib.wait_for_element_visible(CreateEnclosureGroupElements.ID_TBIRD_CHOOSE_LIG_LAYER % (enc_no, switch_no), timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(CreateEnclosureGroupElements.ID_TBIRD_SELECT_OPTION_CHOOSE_LIG % (enc_no, switch_no, switch_lig), timeout, fail_if_false=True, js_click=True)
        if ui_lib.wait_for_element_visible(EditEnclosureGroupElements.ID_TBIRD_TEXT_CHANGE_LIG_NOTIFICATION_HEADER, timeout, fail_if_false=False):
            msg_notification = ui_lib.get_text(EditEnclosureGroupElements.ID_TBIRD_TEXT_CHANGE_LIG_NOTIFICATION, timeout, fail_if_false=True)
            logger.info(msg_notification)
            ui_lib.wait_for_element_and_click(EditEnclosureGroupElements.ID_TBIRD_BUTTON_CHANGE_LIG_CONFIRM, timeout, fail_if_false=True)
        ui_lib.wait_for_element_hidden(CreateEnclosureGroupElements.ID_TBIRD_CHOOSE_LIG_LAYER % (enc_no, switch_no), timeout, fail_if_false=True)


class C7000EditEnclosureGroups(_BaseEditEnclosureGroups):
    @classmethod
    def input_enclosure_group_name(cls, name, timeout=5):
        logger.debug("input [ Enclosure Group name ] '%s'" % name)
        ui_lib.wait_for_element_and_input_text(EditEnclosureGroupElements.ID_INPUT_ENC_GROUP_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def input_select_logical_interconnect_group(cls, bay, logical_interconnect_group, timeout=5):
        logger.debug("- About to choose LIG %s for bay %s" % (logical_interconnect_group, bay))
        BuiltIn().sleep(3)
        ui_lib.wait_for_element_and_input_text(EditEnclosureGroupElements.ID_INPUT_C7000_CHOOSE_LIG % bay, "", timeout, fail_if_false=True)
        BuiltIn().sleep(3)
        ui_lib.wait_for_element_and_input_text(EditEnclosureGroupElements.ID_INPUT_C7000_CHOOSE_LIG % bay, logical_interconnect_group, timeout, fail_if_false=True)
        BuiltIn().sleep(3)
        ui_lib.wait_for_element_and_click(EditEnclosureGroupElements.ID_COMBO_C7000_OPTION_LIG % (bay, logical_interconnect_group), timeout, fail_if_false=True)

    @classmethod
    def input_configuration_script(cls, script, timeout=5):
        logger.debug("input [ Configuration script ] '%s'" % script)
        ui_lib.wait_for_element_and_input_text(EditEnclosureGroupElements.ID_INPUT_CONFIG_SCRIPT, script, timeout, fail_if_false=True)

    @classmethod
    def click_ok_button(cls, timeout=5):
        logger.debug("click [ OK ] button")
        ui_lib.wait_for_element_and_click(EditEnclosureGroupElements.ID_BUTTON_ENCLOSURE_GROUP_OK, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(EditEnclosureGroupElements.ID_BUTTON_ENCLOSURE_GROUP_CANCEL, timeout, fail_if_false=True)

    @classmethod
    def click_select_button(cls, timeout=5):
        logger.debug("click [ Yes, select ] button")
        ui_lib.wait_for_element_and_click(EditEnclosureGroupElements.ID_BUTTON_EDIT_ENCGRP_CONFIRM, timeout, fail_if_false=True)


class _BaseVerifyEnclosureGroups(FusionUIBase):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_edit_button_exists(cls, timeout=5, fail_if_false=True):
        logger.debug("check for [ Edit ] button")
        return ui_lib.wait_for_element_visible(EditEnclosureGroupElements.ID_ACTION_EDIT_ENCLOSURE_GROUP, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_for_search_combo_menu(cls, enc_no, switch_no, timeout=5, fail_if_false=True):
        logger.debug("verify search combo menu for input lig")
        return ui_lib.wait_for_element_visible(CreateEnclosureGroupElements.ID_TBIRD_EG_SEARCH_COMBO_MENU % (enc_no, str(switch_no)), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_action_button_exists(cls, timeout=5, fail_if_false=True):
        logger.debug("check for [ Action menu] button")
        return ui_lib.wait_for_element_visible(GeneralEnclosureGroupElements.ID_BUTTON_ACTIONS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_delete_button_exists(cls, timeout=5, fail_if_false=True):
        logger.debug("check for [ Delete ] button")
        return ui_lib.wait_for_element_visible(DeleteEnclosureGroupElements.ID_MENU_ACTION_ENC_GRP_DELETE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_drop_down_option_for_lig(cls, enc_no, switch_no, switch_lig='None', timeout=5, fail_if_false=True):
        logger.debug("verify search combo menu for input lig contains [ %s ]" % switch_lig)
        return ui_lib.wait_for_element_visible(CreateEnclosureGroupElements.ID_TBIRD_EG_LIG_DROPDOWN_OPTIONS % (enc_no, str(switch_no), switch_lig), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_create_enclosure_group_button_exists(cls, timeout=5, fail_if_false=True):
        logger.debug("check for [ Create enclosure group ] button")
        return ui_lib.wait_for_element_visible(CreateEnclosureGroupElements.ID_BUTTON_CREATE_ENCLOSURE_GROUP, timeout, fail_if_false)


class VerifyEnclosureGroups(_BaseVerifyEnclosureGroups):
    pass


class C7000VerifyEnclosureGroups(_BaseVerifyEnclosureGroups):
    pass


class TBirdVerifyEnclosureGroups(_BaseVerifyEnclosureGroups):
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_range_side_message_present(cls, timeout=5, fail_if_false=True):
        logger.debug("check [ There are no address ranges ] message present")
        return ui_lib.wait_for_element_visible(EditEnclosureGroupElements.ID_EG_EDIT_NO_RANGES_SIDE_MSG, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_edit_eg_add_addressrange_button_present(cls, timeout=5, fail_if_false=True):
        logger.info("verify [ Add Address Ranges ] button present in Edit EG dialog")
        return ui_lib.wait_for_element_visible(EditEnclosureGroupElements.ID_BUTTON_ENCLOSUREGROUP_EDIT_ADD_ADDRESS_RANGES, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_create_eg_add_addressrange_button_present(cls, timeout=5, fail_if_false=True):
        logger.info("verify [ Add Address Ranges ] button present in Create EG dialog")
        return ui_lib.wait_for_element_visible(CreateEnclosureGroupElements.ID_BUTTON_CREATE_ENCLOSUREGROUP_ADD_ADDRESS_RANGES, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_iprange_name_present(cls, rangename, timeout=5, fail_if_false=True):
        logger.debug("click for [ Range name] in table")
        return ui_lib.wait_for_element_visible(GeneralEnclosureGroupElements.ID_EG_SELECT_IPRANGE_NAME % rangename, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_range_name_present_in_table(cls, rangename, timeout=5, fail_if_false=True):
        logger.debug("check [ range is present ] in Address pool")
        return ui_lib.wait_for_element_visible(EditEnclosureGroupElements.ID_EDIT_CHECK_IPRANGE_NAME_IN_TABLE % rangename, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_selected_lig_for_enclosure(cls, enc_no, switch_no, switch_lig, timeout=5, fail_if_false=True):
        logger.debug("check selected [ LIG for <enclosure: %s, bay %s>] is [ %s ]" % (enc_no, switch_no, switch_lig))
        return ui_lib.wait_for_element_value(CreateEnclosureGroupElements.ID_TEXT_TBIRD_SELECTED_LIG % (enc_no, str(switch_no)), switch_lig, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_ipv4_address(cls, expect_value, timeout=5, fail_if_false=True):
        locator = VerifyEnclosureGroupElements.ID_TEXT_GENERAL_IPV4_ADDRESS
        item_name = "IPv4 management address"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_used_by(cls, expect_value, timeout=5, fail_if_false=True):
        locator = VerifyEnclosureGroupElements.ID_TEXT_GENERAL_USED_BY
        item_name = "Used by"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_power_mode(cls, expect_value, timeout=5, fail_if_false=True):
        locator = VerifyEnclosureGroupElements.ID_TEXT_POWER_MODE
        item_name = "Power mode"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_os_deployment_settings_network_type(cls, expect_value, timeout=5, fail_if_false=True):
        locator = VerifyEnclosureGroupElements.ID_TEXT_DEPLOYMENT_NETWORK_TYPE
        item_name = "Deployment network type"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_interconnect_bay_configuration_used_lig(cls, enc_no, switch_no, expect_value, timeout=5, fail_if_false=True):
        locator = VerifyEnclosureGroupElements.ID_TEXT_ENG_SELECTED_LOGICAL_INTERCONNECT_GROUP % (enc_no, switch_no)
        item_name = "Enclosure group logical interconnect group"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_interconnect_bay_configuration_icm_type(cls, enc_no, switch_no, expect_value, timeout=5, fail_if_false=True):
        locator = VerifyEnclosureGroupElements.ID_TEXT_ENG_SELECTED_INTERCONNECT_TYPE % (enc_no, switch_no)
        item_name = "Enclosure group interconnect type"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

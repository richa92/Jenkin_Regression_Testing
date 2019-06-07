import re
import time
from datetime import datetime
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.base import FusionUIBase, TakeScreenShotWhenReturnFalseDeco
from FusionLibrary.ui.business_logic.networking.logicalinterconnectgroups_elements import (GeneralLogicalInterconnectGroupsElements,
                                                                                           C7000GeneralLogicalInterconnectGroupsElements,
                                                                                           TBirdGeneralLogicalInterconnectGroupsElements,
                                                                                           CreateLogicalInterconnectGroupsElements,
                                                                                           C7000CreateLogicalInterconnectGroupsElements,
                                                                                           TBirdCreateLogicalInterconnectGroupsElements,
                                                                                           EditLogicalInterconnectGroupsElements,
                                                                                           C7000EditLogicalInterconnectGroupsElements,
                                                                                           TBirdEditLogicalInterconnectGroupsElements,
                                                                                           DeleteLogicalInterconnectGroupsElements,
                                                                                           C7000DeleteLogicalInterconnectGroupsElements,
                                                                                           TBirdDeleteLogicalInterconnectGroupsElements,
                                                                                           EditScopeElements)


class _BaseCommonOperationLogicalInterconnectGroups(object):

    e = GeneralLogicalInterconnectGroupsElements

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_lig_exist(cls, lig, timeout=10, fail_if_false=True):
        logger.debug("verify [ LIG '%s' ] is not existing" % lig)
        return ui_lib.wait_for_element_visible(cls.e.ID_TABLE_LIG % lig, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_lig_not_exist(cls, lig, timeout=10, fail_if_false=True):
        logger.debug("verify [ lig '%s' ] is not existing" % lig)
        return ui_lib.wait_for_element_notvisible(cls.e.ID_TABLE_LIG % lig, timeout, fail_if_false)

    @classmethod
    def get_lig_list(cls, timeout=5):
        logger.debug("Get all [ lig names ] from table")
        lig_name_list = []
        if ui_lib.wait_for_element(cls.e.ID_TABLE_LIGS, timeout):
            lig_name_list = FusionUIBase.get_multi_elements_text(cls.e.ID_TABLE_LIGS, timeout, fail_if_false=True)
        return lig_name_list

    @classmethod
    def click_lig(cls, lig, timeout=5):
        logger.debug("select [ LIG '%s' ]" % lig)
        ui_lib.wait_for_element_and_click(cls.e.ID_TABLE_LIG % lig, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_lig_selected(cls, lig, timeout=5, fail_if_false=True):
        logger.debug("wait [ LIG '%s' ] selected" % lig)
        return ui_lib.wait_for_element_visible(cls.e.ID_TABLE_LIG_SELECTED % lig, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_activity_action_ok(cls, lig, action_name, timeout=60, fail_if_false=True):
        logger.debug("waiting [ activity action of LIG '%s' ] change to ok" % lig)
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element(cls.e.ID_TEXT_ACTIVITY_ACTION_OK % (lig, action_name), timeout=10, fail_if_false=False):
                actionname = FusionUIBase.get_text(cls.e.ID_TEXT_ACTIVITY_ACTION_TITLE % lig)
                logger.debug("[ activity action '%s' status ] is ok as expected." % actionname)
                return True
            elif ui_lib.wait_for_element(cls.e.ID_TEXT_ACTIVITY_ACTION_WARN % (lig, action_name), timeout=10, fail_if_false=False):
                actionname = FusionUIBase.get_text(cls.e.ID_TEXT_ACTIVITY_ACTION_TITLE % lig)
                logger.debug("[ activity action '%s' status ] is warn not as expected." % actionname)
                ui_lib.wait_for_element_and_click(cls.e.ID_TEXT_ACTIVITY_ACTION_WARN % (lig, action_name))
                msg = FusionUIBase.get_multi_elements_text(cls.e.ID_TEXT_ACTIVITY_MESSAGE)
                msg = [s for s in msg if msg != ''][0]
                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            elif ui_lib.wait_for_element(cls.e.ID_TEXT_ACTIVITY_ACTION_ERROR % (lig, action_name), timeout=10, fail_if_false=False):
                actionname = FusionUIBase.get_text(cls.e.ID_TEXT_ACTIVITY_ACTION_TITLE % lig)
                logger.debug("[ activity action '%s' status ] is error not as expected." % actionname)
                ui_lib.wait_for_element_and_click(cls.e.ID_TEXT_ACTIVITY_ACTION_ERROR % (lig, action_name))
                msg = FusionUIBase.get_multi_elements_text(cls.e.ID_TEXT_ACTIVITY_MESSAGE)
                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            else:
                if ui_lib.wait_for_element(cls.e.ID_TEXT_ACTIVITY_ACTION_TITLE % lig):
                    actionname = FusionUIBase.get_text(cls.e.ID_TEXT_ACTIVITY_ACTION_TITLE % lig)
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
    def click_link_used_by_li(cls, timeout=5, fail_if_false=True):
        logger.debug("click [used by] link for logical interconnects navigation")
        return ui_lib.wait_for_element_and_click(cls.e.ID_LINK_USED_BY_LI, timeout, fail_if_false)

    @classmethod
    def get_text_used_by(cls, timeout=5, fail_if_false=True):
        logger.debug("get [used by] Text in general view")
        used_by_val = ui_lib.get_text(cls.e.ID_TEXT_USED_BY, timeout, fail_if_false)
        logger.info(" used by  value is %s" % used_by_val)
        return used_by_val

    @classmethod
    def click_link_used_by_eg(cls, timeout=5, fail_if_false=True):
        logger.debug("click [used by] link for enclosure group navigation")
        return ui_lib.wait_for_element_and_click(cls.e.ID_LINK_USED_BY_EG, timeout, fail_if_false)

    @classmethod
    def make_uplink_set_panel_into_viewpoint(cls, name):
        logger.debug("Get [ Uplink Set '%s' into view point ]" % name)
        FusionUIBase.scroll_element_into_viewpoint(cls.e.ID_BTN_FOLDING_UPLINK_SET % name)

    @classmethod
    def click_snmpv3_trap_destination_values(cls, trap, timeout=5, fail_if_false=True):
        logger.debug("collapse trap destniation values")
        return ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_SNMPV3_TRAP_DESTINATION_VALUES % trap, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def close_snmpv3_trap_destination_values(cls, trap, timeout=5, fail_if_false=True):
        logger.debug("collapse trap destniation values")
        return ui_lib.wait_for_element_and_click(cls.e.ID_COLLAPSE_SNMPV3_TRAP_DESTINATION_VALUES % trap, timeout=timeout, fail_if_false=fail_if_false)


class CommonOperationLogicalInterconnectGroups(_BaseCommonOperationLogicalInterconnectGroups):
    e = GeneralLogicalInterconnectGroupsElements


class C7000CommonOperationLogicalInterconnectGroups(_BaseCommonOperationLogicalInterconnectGroups):
    pass


class TBirdCommonOperationLogicalInterconnectGroups(_BaseCommonOperationLogicalInterconnectGroups):
    pass


class _BaseCreateLogicalInterconnectGroups(object):

    e = CreateLogicalInterconnectGroupsElements

    @classmethod
    def click_create_logical_interconnect_group(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Create logical interconnect group ] button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_LIG, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_actions_create(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ Create ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectGroupsElements.ID_BUTTON_ACTIONS, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_ACTION_CREATE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_lig_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Create logical interconnect group ] dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_CREATE_LIG, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_lig_dialog_disappear(cls, timeout=25, fail_if_false=True):
        logger.debug("wait [ Create logical interconnect group ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_CREATE_LIG, timeout=timeout, fail_if_false=fail_if_false)

    # { dialog panel select
    @classmethod
    def select_general_section(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ General ] section")
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_PANEL_SELECTOR, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_GENERAL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_logical_interconnect_group_section(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ Logical Interconnect Group ] section")
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_PANEL_SELECTOR, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_LOGICAL_INTERCONNECT_GROUP, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_logical_interconnect_settings_section(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ Interconnect Settings ] section")
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_PANEL_SELECTOR, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_INTERCONNECT_SETTINGS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_logical_snmp_section(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ SNMP ] section")
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_PANEL_SELECTOR, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_SNMP, timeout=timeout, fail_if_false=fail_if_false)
    # }

    @classmethod
    def input_name(cls, lig_name, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] to name textbox" % lig_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NAME, lig_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Create ] button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_plus_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Create + ] button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_PLUS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_verifying_parameters_msg(cls, timeout=10, fail_if_false=True):
        logger.debug('wait message [ Verifying Parameters ]')
        return ui_lib.wait_for_element_visible(cls.e.ID_TEXT_VERIFYING_PARAMETERS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_status_changing_shown(cls, timeout=10, fail_if_false=True):
        return ui_lib.wait_for_element_visible(cls.e.ID_ICON_STATUS_CHANGING, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_status_changing_disappear(cls, timeout=15, fail_if_false=True):
        return ui_lib.wait_for_element_notvisible(cls.e.ID_ICON_STATUS_CHANGING, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_verifying_parameters_msg_disappear(cls, timeout=10, fail_if_false=True):
        logger.debug('wait message [ Verifying Parameters ] disappear')
        return ui_lib.wait_for_element_notvisible(cls.e.ID_TEXT_VERIFYING_PARAMETERS, timeout=timeout, fail_if_false=fail_if_false)

    # { internal network
    @classmethod
    def click_edit_internal_networks_gear(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ gear ] button in create lig dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_INTERNAL_NETWORKS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_internal_networks_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Edit Internal Network ] dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_EDIT_INTERNAL_NETWORKS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_internal_networks_add_networks(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add networks ] button in edit internal networks dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_internal_networks_remove_all(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Remove All ] button in edit internal networks dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_INTERNAL_NETWORKS_REMOVE_ALL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_internal_networks_add_networks_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait edit internal networks > [ Add Networks ] dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_edit_internal_networks_add_networks_search_network(cls, network, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into search network textbox in edit internal networks > add networks" % network)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_SEARCH_NETWORK, network, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_internal_networks_add_networks_table_row_shown(cls, network, timeout=5, fail_if_false=True):
        logger.debug("wait edit internal networks > add networks > table row [ %s ] shown" % network)
        return ui_lib.wait_for_element_visible(cls.e.ID_TABLE_ROW_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS % network, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_internal_networks_add_networks_add(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add ] button in edit internal networks > add networks dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_ADD, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_internal_networks_add_networks_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait edit internal networks > [ Add Networks ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_internal_networks_add_networks_add_plus(cls, timeout=5, fail_if_false=True):
        logger.debug("click [Add plus ] button in edit internal networks > add networks")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_ADD_PLUS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_internal_networks_table_row_shown(cls, network_name, timeout=5, fail_if_false=True):
        logger.debug("wait edit internal networks > table row [ %s ] shown" % network_name)
        return ui_lib.wait_for_element_visible(cls.e.ID_TABLE_ROW_EDIT_INTERNAL_NETWORKS % network_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_internal_networks_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait edit internal networks > [ Edit Internal Networks ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_EDIT_INTERNAL_NETWORKS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_internal_networks_ok(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ OK ] button in edit internal networks")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_INTERNAL_NETWORKS_OK, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_internal_networks_cancel(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button in edit internal networks")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_INTERNAL_NETWORKS_CANCEL, timeout=timeout, fail_if_false=fail_if_false)
    # }

    # { uplink set
    @classmethod
    def click_add_uplink_set(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add uplink set ] button dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_UPLINK_SET, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def verify_add_uplink_set_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("verify [ Add uplink set ] dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_CREATE_UPLINK_SET, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Create uplink set dialog ] shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_CREATE_UPLINK_SET, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Create uplink set dialog ] shown")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_CREATE_UPLINK_SET, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_create_uplink_set_name(cls, uplink_set_name, timeout=5, fail_if_false=True):
        logger.debug("input uplink set name [ %s ] in create uplink set dialog" % uplink_set_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_CREATE_UPLINK_SET_NAME, uplink_set_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_create_uplink_set_type(cls, uplink_set_type, timeout=5, fail_if_false=True):
        logger.debug("select uplink set type [ %s ] in create uplink set dialog" % uplink_set_type)
        FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_CREATE_UPLINK_SET_TYPE, uplink_set_type, timeout=timeout, fail_if_false=fail_if_false)

    # { - fc
    @classmethod
    def select_create_uplink_set_fc_network(cls, network, timeout=5, fail_if_false=True):
        logger.debug("select fc network [ %s ] in create uplink set dialog" % network)
        FusionUIBase.choose_combo_option_by_text(cls.e.ID_COMBO_CREATE_UPLINK_SET_FC_NETWORK, network, timeout_sec=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_uplink_set_add_uplink_ports_to_table_row_carbon(cls, bay_no, port_name, timeout=5, fail_if_false=True):
        logger.debug("select uplink port [ bay%s:port %s] in the uplinkset ports dialog" % (bay_no, port_name))
        FusionUIBase.wait_for_element_and_click(cls.e.ID_TBIRD_TABLE_ROW_CREATE_UPLINK_SET_PORT_CARBON % (bay_no, port_name), timeout=timeout, fail_if_false=fail_if_false)

    # TODO: should remove after QXCR1001428378 get fixed
    # @classmethod
    # def select_create_uplink_set_fc_network_workaround(cls, network, timeout=5, fail_if_false=True):
    #     logger.debug("<workaround> select fc network [ %s ] in create uplink set dialog" % network)
    #     ui_lib.wait_for_element_and_click(cls.e.ID_SEARCH_CREATE_UPLINK_SET_FC_NETWORK, timeout=timeout, fail_if_false=fail_if_false)
    #     ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_CREATE_UPLINK_SET_FC_NETWORK % network, timeout=10, fail_if_false=fail_if_false)

    @classmethod
    def select_create_uplink_set_fc_port_speed(cls, bay_no, port_name, port_speed, timeout=5, fail_if_false=True):
        """
        :param bay_no: bay number as integer.(don't pass bay_no like 'bay1')
        :param port_name:
        :param port_speed:
        :param timeout:
        """
        logger.debug("select port speed [ %s ] for fc port [ %s ] of bay [ %s ] in create uplink set dialog" % (port_speed, port_name, bay_no))
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_CREATE_UPLINK_SET_FC_PORT_SPEED % (bay_no, port_name), timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_CREATE_UPLINK_SET_FC_PORT_SPEED % (bay_no, port_name, port_speed), timeout=timeout, fail_if_false=fail_if_false)
    # - }

    @classmethod
    def get_text_uplink_notification(cls, timeout=5, fail_if_false=True):
        logger.debug("return error and resolution of the Uplinkset ports")
        error = FusionUIBase.get_text(cls.e.ID_TEXT_UPLINK_NOTIFICATION_ERROR, timeout, fail_if_false)
        resolution = FusionUIBase.get_text(cls.e.ID_TEXT_UPLINK_NOTIFICATION_RESOLUTION, timeout, fail_if_false)
        return {"error": error, "resolution": resolution}

    @classmethod
    def tick_create_uplink_set_connection_mode_automatic(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ Automatic (recommended) ] option")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_RADIO_CREATE_UPLINK_SET_CONNECTION_MODE_AUTOMATIC, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_create_uplink_set_lacp_timer(cls, uplink_set_lacp_timer, timeout=5, fail_if_false=True):
        logger.debug("select LACP timer [ %s ]" % uplink_set_lacp_timer)
        FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_CREATE_UPLINK_SET_LACP_TIMER, uplink_set_lacp_timer, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_create_uplink_set_connection_mode_failover(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ Failover ] option")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_RADIO_CREATE_UPLINK_SET_CONNECTION_MODE_FAILOVER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_create_uplink_set_native_network(cls, network_name, timeout=5, fail_if_false=True):
        logger.debug("tick vlan [ %s ] as native network in create uplink set dialog" % network_name)
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_CREATE_UPLINK_SET_ETHERNET_NATIVE % network_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_create_uplink_set_preferred_uplink_port(cls, bay_no, port_name, timeout=5, fail_if_false=True):
        logger.debug("tick [ bay%s:%s ] as preferred uplink port in create uplink set dialog" % (bay_no, port_name))
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_CREATE_UPLINK_SET_ETHERNET_PREFERRED_PORT % (bay_no, port_name), timeout=timeout, fail_if_false=fail_if_false)

    # - { uplink set network
    @classmethod
    def click_create_uplink_set_add_networks(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add networks ] button in create uplink set dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_remove_all_networks(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Remove All ] networks button in create uplink set dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_REMOVE_ALL_ETHERNET_NETWORKS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_remove_all_uplink_ports(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Remove All ] uplink sets button in create uplink set dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_REMOVE_ALL_ETHERNET_PORTS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_networks_to_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set > [ Add networks to ] dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_CREATE_UPLINK_SET_ADD_NETWORKS_TO, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_create_uplink_set_add_networks_to_search_network(cls, network_name, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] to search network textbox in create uplink set > add networks to dialog" % network_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_CREATE_UPLINK_SET_ADD_NETWORKS_TO_SEARCH_NETWORK, network_name, timeout=timeout, fail_if_false=fail_if_false)
        # workaround to fix sometime specific network not show in table list
        time.sleep(1)
        ui_lib.get_s2l().press_key(cls.e.ID_INPUT_CREATE_UPLINK_SET_ADD_NETWORKS_TO_SEARCH_NETWORK, "\\8")
        ui_lib.get_s2l().press_key(cls.e.ID_INPUT_CREATE_UPLINK_SET_ADD_NETWORKS_TO_SEARCH_NETWORK, network_name[-1:])

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_networks_to_table_row_shown(cls, network_name, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set > add networks to [ %s ] table item shown" % network_name)
        return ui_lib.wait_for_element_visible(cls.e.ID_TABLE_ROW_CREATE_UPLINK_SET_ADD_NETWORKS_TO % network_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_networks_to_add(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add ] button in create uplink set > add networks to dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS_TO_ADD, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_networks_to_add_plus(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add plus ] button in create uplink set > add networks to dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS_TO_ADD_PLUS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_networks_to_cancel(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button in create uplink set > add networks to dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS_TO_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_networks_to_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set > [ Add networks to ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_CREATE_UPLINK_SET_ADD_NETWORKS_TO, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_create_uplink_set_tunnel_network(cls, network, timeout=5, fail_if_false=True):
        logger.debug("select tunnel network [ %s ] in create uplink set dialog" % network)
        FusionUIBase.choose_combo_option_by_text(cls.e.ID_COMBO_CREATE_UPLINK_SET_TUNNEL_NETWORK, network, timeout_sec=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_create_uplink_set_untagged_network(cls, network, timeout=5, fail_if_false=True):
        logger.debug("select untagged network [ %s ] in create uplink set dialog" % network)
        FusionUIBase.choose_combo_option_by_text(cls.e.ID_COMBO_CREATE_UPLINK_SET_UNTAGGED_NETWORK, network, timeout_sec=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_network_table_row_shown(cls, network, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set network [ %s ] table row shown" % network)
        return ui_lib.wait_for_element_visible(cls.e.ID_TABLE_ROW_CREATE_UPLINK_SET_NETWORK % network, timeout=timeout, fail_if_false=fail_if_false)
    # - }

    # - { lig uplink set port
    @classmethod
    def click_create_uplink_set_add_uplink_ports(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add uplink ports ] button in create uplink set dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_UPLINK_PORTS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_uplink_ports_to_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set > [ Add uplink ports to ] dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_TO, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_create_uplink_set_add_uplink_ports_to_search_port(cls, port_name, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] to search port textbox in create uplink set > add uplink ports to dialog" % port_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_CREATE_UPLINK_SET_ADD_UPLINK_PORT_SEARCH_PORT, port_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_uplink_ports_to_add(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add ] button in create uplink set > add uplink ports to dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_ADD, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_uplink_ports_to_add_plus(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add plus ] button in create uplink set > add uplink ports to dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_ADD_PLUS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_uplink_ports_to_cancel(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button in create uplink set > add uplink ports to dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_uplink_ports_to_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set > [ Add uplink ports to ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_TO, timeout=timeout, fail_if_false=fail_if_false)
    # - }

    # buttons
    @classmethod
    def click_create_uplink_set_add(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add ] button in create uplink set dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_plus(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add plus ] button in create uplink set dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_PLUS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_cancel(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button in create uplink set dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_CANCEL, timeout=timeout, fail_if_false=fail_if_false)
    # }

    # { SNMP
    @classmethod
    def toggle_snmp_enabled(cls, timeout=5):
        logger.debug("toggle snmp [ Enabled ]")
        FusionUIBase.toggle_button(cls.e.ID_TOGGLE_SNMP, "Enabled", timeout=timeout)

    @classmethod
    def toggle_snmp_disabled(cls, timeout=5):
        logger.debug("toggle snmp [ Disabled ]")
        FusionUIBase.toggle_button(cls.e.ID_TOGGLE_SNMP, "Disabled", timeout=timeout)

    @classmethod
    def toggle_snmpv1v2_enabled(cls, timeout=5):
        logger.debug("toggle snmpv1v2 [ Enabled ]")
        FusionUIBase.toggle_button(cls.e.ID_TOGGLE_SNMPV1V2, True, timeout=timeout)

    @classmethod
    def toggle_snmpv1v2_disabled(cls, timeout=5):
        logger.debug("toggle snmpv1v2 [ Disabled ]")
        FusionUIBase.toggle_button(cls.e.ID_TOGGLE_SNMPV1V2, False, timeout=timeout)

    @classmethod
    def toggle_snmpv3_disabled(cls, timeout=5):
        logger.debug("toggle snmpv3 [ Disabled ]")
        FusionUIBase.toggle_button(cls.e.ID_TOGGLE_SNMPv3, False, timeout=timeout)

    @classmethod
    def toggle_snmpv3_enabled(cls, timeout=5):
        logger.debug("toggle snmpv3 [ Enabled ]")
        FusionUIBase.toggle_button(cls.e.ID_TOGGLE_SNMPv3, True, timeout=timeout)

    @classmethod
    def input_snmp_system_contact(cls, syscontact, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into SNMP System contact" % syscontact)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SYSTEM_CONTACT, syscontact, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_snmp_read_community(cls, readcommunity, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into SNMP Read community" % readcommunity)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_READ_COMMUNITY, readcommunity, timeout=timeout, fail_if_false=fail_if_false)

    # - { SNMP Users
    @classmethod
    def click_add_snmp_user(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ add SNMP user] button ")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_SNMP_USER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_snmp_user_cancel(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ cancel ] button in add snmp user ")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_SNMPV3_USER_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_add_snmp_user_name(cls, username, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [ username ] in Add SNMP user dialog" % username)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ADD_SNMP_USER_NAME, username, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_security_level_none(cls, timeout=5, fail_if_false=True):
        logger.debug("choose option [none] for security level")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SECURITY_LEVEL_NONE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_security_level_authentication(cls, timeout=5, fail_if_false=True):
        logger.debug("choose option [authentication] for security level")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SECURITY_LEVEL_AUTHENTICATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_dropdown_authentication_protocol(cls, timeout=5, fail_if_false=True):
        logger.debug("clicking drop down button to select authentication protocol")
        ui_lib.wait_for_element_and_click(cls.e.ID_COLLAPSE_AUTHENTICATION_PROTOCOL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_authentication_protocols(cls, timeout=5, fail_if_false=True):
        logger.debug("Fetching the available authentication protocol")
        return ui_lib.get_text(cls.e.ID_TEXT_AUTHENTICATION_PROTOCOL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_privacy_protocols(cls, timeout=5, fail_if_false=True):
        logger.debug("Fetching the available privacy protocol")
        return ui_lib.get_text(cls.e.ID_TEXT_PRIVACY_PROTOCOL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_authentication_protocol(cls, protocol, timeout=5, fail_if_false=True):
        logger.debug("selecting authentication protocol %s" % protocol)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_AUTHENTICATION_PROTOCOL % protocol, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_authentication_password(cls, password, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [  Authentication password ] in Add SNMP user dialog" % password)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_AUTHENTICATION_PASSWORD, password, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_confirm_authentication_password(cls, password, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [  confirm password ] in Add SNMP user dialog" % password)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_CONFIRM_AUTHENTICATION_PASSWORD, password, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_dropdown_privacy_protocol(cls, timeout=5, fail_if_false=True):
        logger.debug("clicking drop down button to select privacy protocol")
        ui_lib.wait_for_element_and_click(cls.e.ID_COLLAPSE_AUTHENTICATION_AND_PRIVACY_PROTOCOL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_security_level_authentication_and_privacy(cls, timeout=5, fail_if_false=True):
        logger.debug("choose option [authentication and privacy] for security level")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SECURITY_LEVEL_AUTHENTICATION_AND_PRIVACY, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_authentication_and_privacy_protocol(cls, protocol, timeout=5, fail_if_false=True):
        logger.debug("selecting authenticationandprivacy protocol %s" % protocol)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_AUTHENTICATION_AND_PRIVACY_PROTOCOL % protocol, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_privacy_password(cls, password, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [  privacy password ] in Add SNMP user dialog" % password)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_PRIVACY_PASSWORD, password, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_confirm_privacy_password(cls, password, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [  confirm password ] in Add SNMP user dialog" % password)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_CONFIRM_PRIVACY_PASSWORD, password, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_snmp_user_add(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add ] button in Add SNMP user dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_SNMP_USER_ADD, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_snmp_user_add_plus(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add plus ] button in Add Trap Destination dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_SNMP_USER_ADD_PLUS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_snmp_error_close_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ close] button in error dialog ")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_SNMP_ERROR_DIALOG_CLOSE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_traps_associated(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ collapse ] icon in error dialog ")
        ui_lib.wait_for_element_and_click(cls.e.ID_COLLAPSE_SNMP_ERROR_DIALOG_TRAPS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_text_associated_trap_destination(cls, timeout=5, fail_if_false=True):
        logger.debug("Bring eleemts in to view point in error dialog ")
        FusionUIBase.scroll_element_into_viewpoint(cls.e.ID_TEXT_SNMP_ERROR_DIALOG_TRAPS)
        return ui_lib.get_text(cls.e.ID_TEXT_SNMP_ERROR_DIALOG_TRAPS, timeout=timeout, fail_if_false=fail_if_false)

    # }
    # - { Trap Destinations

    @classmethod
    def click_add_trap_destination(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add trap destination ] button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def wait_add_trap_destination_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add Trap Destination ] dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_ADD_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def wait_add_trap_destination_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add Trap Destination ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_ADD_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_add_trap_destination_trap_destination(cls, trapdestination, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [ Trap destination ] in Add Trap Destination dialog" % trapdestination)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ADD_TRAP_DESTINATION_TRAP_DESTINATION, trapdestination, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_add_trap_destination_community_string(cls, communitystring, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [ Community string ] in Add Trap Destination dialog" % communitystring)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ADD_TRAP_DESTINATION_COMMUNITY_STRING, communitystring, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_add_trap_destination_trap_format_snmpv1(cls, timeout=5, fail_if_false=True):
        logger.debug("tick Trap Format [ SNMPv1 ]")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_ADD_TRAP_DESTINATION_TRAP_FORMAT_SNMPV1, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_add_trap_destination_trap_format_snmpv2(cls, timeout=5, fail_if_false=True):
        logger.debug("tick Trap Format [ SNMPv2 ]")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_ADD_TRAP_DESTINATION_TRAP_FORMAT_SNMPV2, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_add_trap_destination_trap_format_snmpv3(cls, timeout=5, fail_if_false=True):
        logger.debug("tick Trap Format [ SNMPv3 ]")
        return ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_ADD_TRAP_DESTINATION_TRAP_FORMAT_SNMPV3, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_trap_destination_add(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add ] button in Add Trap Destination dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_TRAP_DESTINATION_ADD, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def disable_snmpv3_trap_destination_notification(cls, timeout=5):
        logger.debug("Disable [ Notification Type ] in trap destination view")
        FusionUIBase.toggle_button(cls.e.ID_TOGGLE_TRAP_DESTINATION_NOTIFICATION, False, timeout=timeout)

    @classmethod
    def enable_snmpv3_trap_destination_notification(cls, timeout=5):
        logger.debug("Enable [ Notification Type ] in trap destination view")
        FusionUIBase.toggle_button(cls.e.ID_TOGGLE_TRAP_DESTINATION_NOTIFICATION, True, timeout=timeout)

    @classmethod
    def input_add_trap_destination_engine_id(cls, engineid, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [ Engine ID ] in Add Trap Destination dialog" % engineid)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_TRAP_DESTINATION_ENGINE_ID, engineid, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_dropdown_snmpv3_user_in_trap_destination(cls, timeout=5, fail_if_false=True):
        logger.debug("List Trap destination snmpv3 [ snmp users ]")
        ui_lib.wait_for_element_and_click(cls.e.ID_COLLAPSE_USER_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_snmpv3_user_in_trap_destination(cls, timeout=5, fail_if_false=True):
        logger.debug("Listing all the available snmp users")
        FusionUIBase.scroll_element_into_viewpoint(cls.e.ID_TEXT_SNMPV3_TRAP_DESTINATION_SNMP_USERS)
        return ui_lib.get_text(cls.e.ID_TEXT_SNMPV3_TRAP_DESTINATION_SNMP_USERS, timeout, fail_if_false)

    @classmethod
    def select_snmpv3_user_in_trap_destination(cls, user, timeout=5, fail_if_false=True):
        logger.debug("Select Trap destination snmpv3 [ snmp users ]")
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_SNMPV3_TRAP_DESTINATION_SNMP_USER % user, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_trap_destination_port(cls, port, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [ port] in Add Trap Destination user dialog" % port)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ADD_TRAP_DESTINATION_PORT, port, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_severity(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ severity ] button in Add Trap Destination dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_COLLAPSE_ADD_TRAP_DESTINATION_SEVERITY, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_trap_destination_severity(cls, severity, timeout=5, fail_if_false=True):
        logger.debug("select [ severity ] in Add Trap Destination dialog")
        return FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_BUTTON_ADD_TRAP_DESTINATION_SELECT_SEVERITY % severity, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_vcm_traps(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ VCM traps ] button in Add Trap Destination dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_COLLAPSE_ADD_TRAP_DESTINATION_VCM_TRAPS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_trap_destination_vcm_trap(cls, trap, timeout=5, fail_if_false=True):
        logger.debug("select [ VCM trap ] in Add Trap Destination dialog")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_BUTTON_ADD_TRAP_DESTINATION_SELECT_VCM_TRAP % trap, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_vc_enet_traps(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ VC_ENET trap ] button in Add Trap Destination dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_COLLAPSE_ADD_TRAP_DESTINATION_VC_ENET_TRAPS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_trap_destination_vc_enet_traps(cls, trap, timeout=5, fail_if_false=True):
        logger.debug("select [ VC_ENET trap ] in Add Trap Destination dialog")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_BUTTON_ADD_TRAP_DESTINATION_SELECT_ENET_TRAP % trap, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_vc_fc_traps(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ VC_FC trap] button in Add Trap Destination dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_COLLAPSE_ADD_TRAP_DESTINATION_VC_FC_TRAPS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_trap_destination_vc_fc_traps(cls, trap, timeout=5, fail_if_false=True):
        logger.debug("select [ VC_FC trap] in Add Trap Destination dialog")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_BUTTON_ADD_TRAP_DESTINATION_SELECT_FC_TRAP % trap, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_trap_destination_add_plus(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add plus ] button in Add Trap Destination dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_TRAP_DESTINATION_ADD_PLUS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_trap_destination_cancel(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button in Add Trap Destination dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_TRAP_DESTINATION_CANCEL, timeout=timeout, fail_if_false=fail_if_false)
    # - }

    # - { SNMP Access
    @classmethod
    def click_add_snmp_access(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add SNMP access ] button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_SNMP_ACCESS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def wait_add_snmp_access_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add SNMP Access ] dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_ADD_SNMP_ACCESS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def wait_add_snmp_access_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add SNMP Access ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_ADD_SNMP_ACCESS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_add_snmp_access_ip_or_subnet(cls, iporsubnet, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [ IP or subnet ] in Add SNMP Access dialog" % iporsubnet)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ADD_SNMP_ACCESS_IP_OR_SUBNET, iporsubnet, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_snmp_access_add(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add ] button in Add SNMP Access dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_SNMP_ADD, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_snmp_access_add_plus(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add plus ] button in Add SNMP Access dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_SNMP_ADD_PLUS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_snmp_access_cancel(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button in Add SNMP Access dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_SNMP_CANCEL, timeout=timeout, fail_if_false=fail_if_false)
    # - }
    # }


class CreateLogicalInterconnectGroups(_BaseCreateLogicalInterconnectGroups):
    pass


class C7000CreateLogicalInterconnectGroups(_BaseCreateLogicalInterconnectGroups):
    e = C7000CreateLogicalInterconnectGroupsElements

    @classmethod
    def select_interconnect_type(cls, lig_interconnec_type, timeout=5, fail_if_false=True):
        logger.debug("select 'Interconnect Type' as [ %s ]" % lig_interconnec_type)
        FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_INTERCONNECT_TYPE, lig_interconnec_type, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_bay_type(cls, bay_no, bay_type, timeout=5, fail_if_false=True):
        logger.debug("select bay type [ %s ] for bay [ %s ]" % (bay_type, bay_no))
        # FusionUIBase.choose_option_by_text(CreateLogicalInterconnectGroupsElements.ID_SELECT_BAY_TYPE % bay_no, bay_type, timeout, fail_if_false=True)
        ui_lib.get_s2l().execute_javascript(cls.e.ID_JAVASCRIPT_BAY_TYPE % bay_no)
        time.sleep(1)
        ui_lib.wait_for_element_visible(cls.e.ID_DROPDOWN_BAY_TYPE_OPTION_LAYER % bay_no, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.get_s2l().execute_javascript(cls.e.ID_JAVASCRIPT_SELECT_BAY_TYPE % (bay_no, bay_type))
        ui_lib.wait_for_element_visible(cls.e.ID_SELECTED_BAY_TYPE % (bay_no, bay_type), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_select_interconnects_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Select interconnects ] button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_SELECT_INTERCONNECTS, timeout=timeout, fail_if_false=fail_if_false)

    # { dialog panel select
    @classmethod
    def select_quality_of_service_section(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ Quality of Service ] section")
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_PANEL_SELECTOR, timeout=timeout, fail_if_false=fail_if_false)
        return ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_QUALITY_OF_SERVICE, timeout=timeout, fail_if_false=fail_if_false)
    # }

    # { uplink port related
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_uplink_ports_to_table_row_shown(cls, bay_no, port_name, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set > add uplink ports to [ bay%s:%s ] table item shown" % (bay_no, port_name))
        return ui_lib.wait_for_element_visible(cls.e.ID_TABLE_ROW_CREATE_UPLINK_SET_ADD_UPLINK_PORT.format(bay_no, port_name), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_uplink_ports_to_table_row(cls, bay_no, port_name, timeout=5, fail_if_false=True):
        logger.debug("click [ bay%s:%s ] table item in create uplink set > add uplink ports to dialog" % (bay_no, port_name))
        ui_lib.wait_for_element_and_click(cls.e.ID_TABLE_ROW_CREATE_UPLINK_SET_ADD_UPLINK_PORT.format(bay_no, port_name), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_port_table_row_shown(cls, bay_no, port, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set port [ %s:%s ] table row shown" % (bay_no, port))
        return ui_lib.wait_for_element_visible(cls.e.ID_TABLE_ROW_CREATE_UPLINK_SET_PORT.format(bay_no, port), timeout=timeout, fail_if_false=fail_if_false)
    # }

    # { Interconnect Settings
    @classmethod
    def tick_interconnect_settings_fast_mac_cache_failover(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ Fast MAC cache failover ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_FAST_MAC_CACHE_FAILOVER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def untick_interconnect_settings_fast_mac_cache_failover(cls, timeout=5, fail_if_false=True):
        logger.debug("untick [ Fast MAC cache failover ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_FAST_MAC_CACHE_FAILOVER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_interconnect_settings_mac_refresh_interval(cls, mac_refresh_interval, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [ MAC refresh interval ] in section [ Interconnect Settings ]" % mac_refresh_interval)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_MAC_REFRESH_INTERVAL, mac_refresh_interval, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_interconnect_settings_igmp_snooping(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ IGMP Snooping ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_IGMP_SNOOPING, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def untick_interconnect_settings_igmp_snooping(cls, timeout=5, fail_if_false=True):
        logger.debug("untick [ IGMP Snooping ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_IGMP_SNOOPING, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_interconnect_settings_igmp_idle_timeout_interval(cls, igmp_idle_timeout_interval, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [ IGMP idle timeout interval ] in section [ Interconnect Settings ]" % igmp_idle_timeout_interval)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_IGMP_IDLE_TIMEOUT_INTERVAL, igmp_idle_timeout_interval, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_interconnect_settings_loop_protection(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ Loop protection ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_LOOP_PROTECTION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def untick_interconnect_settings_loop_protection(cls, timeout=5, fail_if_false=True):
        logger.debug("untick [ Loop protection ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_LOOP_PROTECTION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_interconnect_settings_pause_flood_protection(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ Pause flood protection ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_PAUSE_FLOOD_PROTECTION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def untick_interconnect_settings_pause_flood_protection(cls, timeout=5, fail_if_false=True):
        logger.debug("untick [ Pause flood protection ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_PAUSE_FLOOD_PROTECTION, timeout=timeout, fail_if_false=fail_if_false)
    # }
    # { Quality of Service (QoS)

    @classmethod
    def select_qos_configuration_type(cls, qos_configuration_type, timeout=5, fail_if_false=True):
        logger.debug("select QoS configuration type [ %s ]" % qos_configuration_type)
        FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_QOS_CONFIGURATION_TYPE, qos_configuration_type, timeout=timeout, fail_if_false=fail_if_false)
    # }

    @classmethod
    def select_qos_uplink_classfication(cls, qos_uplink_classfication, timeout=5, fail_if_false=True):
        logger.debug("select uplink QoS configuration type [ %s ]" % qos_uplink_classfication)
        FusionUIBase.choose_option_by_text(cls.e.ID_OPTION_UPLINK, qos_uplink_classfication, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_qos_downlink_classfication(cls, qos_downlink_classfication, timeout=5, fail_if_false=True):
        logger.debug("select downlink configuration type [ %s ]" % qos_downlink_classfication)
        FusionUIBase.choose_option_by_text(cls.e.ID_OPTION_DOWNLINK, qos_downlink_classfication, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_uplink_set_ethernet_port_speed(cls, bay_no, port_name, port_speed, timeout=5, fail_if_false=True):
        """
        :param bay_no: bay number as integer.(don't pass bay_no like 'bay1')
        :param port_name:
        :param port_speed:
        :param timeout:
        """
        logger.debug("select port  speed [ %s ] for eth port [ %s ] of bay [ %s ] in create uplink set dialog" % (port_speed, port_name, bay_no))
        ui_lib.wait_for_element_and_click(cls.e.ID_COMBO_UPLINK_ETHERNET_PORT_SPEED % (bay_no, port_name), timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_UPLINK_ETHERNET_PORT_SPEED % (bay_no, port_name, port_speed), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_autonegotiation_text(cls, bay_no, port_name, timeout=5, fail_if_false=True):
        logger.debug("Return Autonegotiation status for selected port [%s]" % port_name)
        return FusionUIBase.get_text(cls.e.ID_TEXT_AUTONEGOTIATION % (bay_no, port_name), timeout, fail_if_false)

    @classmethod
    def click_preferred_port(cls, pref_bay_no, pref_port_list, timeout=5, fail_if_false=True):
        logger.debug("click preferred checkbox")
        return ui_lib.wait_for_element_and_click(cls.e.ID_CHECKBOX_FAILOVER_PREFERRED_PORT % (pref_bay_no, pref_port_list), timeout, fail_if_false)


class TBirdCreateLogicalInterconnectGroups(_BaseCreateLogicalInterconnectGroups):

    e = TBirdCreateLogicalInterconnectGroupsElements

    @classmethod
    def select_logical_interconnect_group_section(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ Logical Interconnect Group ] section")
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_PANEL_SELECTOR, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_LOGICAL_INTERCONNECT_GROUP, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_enclosure_count(cls, timeout=5, fail_if_false=True):
        logger.debug("Getting Enclosure Count")
        return ui_lib.get_text(cls.e.ID_ENCLOSURE_STATIC_COUNT, timeout, fail_if_false)

    @classmethod
    def select_enclosure_count(cls, count, timeout=5, fail_if_false=True):
        logger.debug("select [ Enclosure Count '%s' ] in General dialog" % count)
        ui_lib.select_from_dropdown_by_dataid(cls.e.ID_DROPDOWN_TBIRD_ENCLOSURE_COUNT, count, timeout, fail_if_false)

    @classmethod
    def select_interconnect_type(cls, interconnect_type, timeout=5, fail_if_false=True):
        logger.debug("Selecting Interconnect Type as : {}".format(interconnect_type))
        ui_lib.wait_for_element_and_click(cls.e.ID_INTERCONNECT_TYPE, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_INTERCONNECT_TYPE_OPTION % interconnect_type, timeout, fail_if_false)

    @classmethod
    def select_interconnect_bay_set(cls, count, timeout=5, fail_if_false=True):
        logger.debug("select [ Interconnect bay set '%s' ] in General dialog" % count)
        return ui_lib.select_from_dropdown_by_dataid(cls.e.ID_DROPDOWN_TBIRD_INTERCONNECT_BAY_SET, count, timeout, fail_if_false)

    @classmethod
    def select_bay_type(cls, enclosure_no, bay_no, bay_type, timeout=5, fail_if_false=True):
        logger.debug("select bay type [ %s ] for bay [ %s ] for Enclosure %s" % (bay_type, bay_no, enclosure_no))
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_BAY_TYPE % (enclosure_no, bay_no), fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_BAY_TYPE_VALUE % (enclosure_no, bay_no, bay_type), fail_if_false=fail_if_false)

    @classmethod
    def select_bay_type_fc(cls, enclosure_no, bay_no, bay_type, timeout=5, fail_if_false=True):
        logger.debug("select bay type [ %s ] for bay [ %s ] for Enclosure %s" % (bay_type, bay_no, enclosure_no))
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_BAY_TYPE_FC % (enclosure_no, bay_no), fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_BAY_TYPE_VALUE_FC % (enclosure_no, bay_no, bay_type), fail_if_false=fail_if_false)

    @classmethod
    def select_redundancy(cls, value, timeout=5, fail_if_false=True):
        logger.debug("select [ Redundancy '%s' ] in General dialog" % value)
        return ui_lib.select_from_dropdown_by_text(cls.e.ID_DROPDOWN_TBIRD_REDUNDANCY, value, timeout, fail_if_false)

    @classmethod
    def click_select_interconnects(cls, timeout=5, fail_if_false=True):
        logger.debug("Click [ Select interconnects ] button in General dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_SELECT_INTERCONNECTS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_uplink_ports_to_table_row_shown(cls, enc_no, bay_no, port_name, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set > add uplink ports to [ enc%s:bay%s:%s ] table item shown" % (enc_no, bay_no, port_name))
        return ui_lib.wait_for_element_visible(cls.e.ID_TBIRD_TABLE_ROW_CREATE_UPLINK_SET_ADD_UPLINK_PORT % (enc_no, bay_no, port_name), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_uplink_ports_to_table_row(cls, enc_no, bay_no, port_name, timeout=5, fail_if_false=True):
        logger.debug("click [ enc%s:bay%s:%s ] table item in create uplink set > add uplink ports to dialog" % (enc_no, bay_no, port_name))
        ui_lib.wait_for_element_and_click(cls.e.ID_TBIRD_TABLE_ROW_CREATE_UPLINK_SET_ADD_UPLINK_PORT % (enc_no, bay_no, port_name), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_port_table_row_shown(cls, enc_no, bay_no, port, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set port [ enc%s:%s:%s ] table row shown" % (enc_no, bay_no, port))
        return ui_lib.wait_for_element_visible(cls.e.ID_TBIRD_TABLE_ROW_CREATE_UPLINK_SET_PORT % (enc_no, bay_no, port), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_all_errors_on_create_dialog(cls):
        return FusionUIBase.get_all_error_message_on_form(GeneralLogicalInterconnectGroupsElements.ID_DIALOG_LIG_ADD)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def toggle_sample_collection_enabled(cls, timeout=5, fail_if_false=True):
        logger.debug("toggle sample_collection[ Enabled ]")
        FusionUIBase.toggle_button(cls.e.ID_TOGGLE_SAMPLE_COLLECTION, "Enabled", timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def toggle_sample_collection_disabled(cls, timeout=5, fail_if_false=True):
        logger.debug("toggle sample_collection [ Disabled ]")
        FusionUIBase.toggle_button(cls.e.ID_TOGGLE_SAMPLE_COLLECTION, "Disabled", timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def input_interval_samples(cls, intervalsamples, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into Interval Between samples" % intervalsamples)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_INTERVAL_SAMPLES, intervalsamples, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def input_total_number_of_samples(cls, totalsamples, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into Total number of Samples" % totalsamples)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_TOTAL_SAMPLES, totalsamples, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_port_info(cls, port_tag):
        port_tag = port_tag.split(':')
        if (len(port_tag)) == 5:
            enclosure_no = port_tag[0].lower().replace('enc', '')
            bay_no = port_tag[1].replace('bay', '')
            port_name = port_tag[2] + ':' + port_tag[3]
            port_speed = port_tag[4]
        else:
            enclousre_no, bay_no, port_name, port_speed = port_tag
            enclosure_no = enclousre_no.lower().replace('enc', '')
            bay_no = bay_no.lower().replace('bay', '')
        return enclosure_no, bay_no, port_name, port_speed

    @classmethod
    def select_uplink_set_ethernet_port_speed(cls, enclosure_no, bay_no, port_name, port_speed, timeout=5, fail_if_false=True):
        """
        :param bay_no: bay number as integer.(don't pass bay_no like 'bay1')
        :param port_name:
        :param port_speed:
        :param timeout:
        """
        logger.debug("select port speed [ %s ] for eth port [ %s ] of bay [ %s ] of encl [%s] in create uplink set dialog" % (port_speed, port_name, bay_no, enclosure_no))
        ui_lib.wait_for_element_and_click(cls.e.ID_COMBO_UPLINK_ETHERNET_PORT_SPEED % (enclosure_no, bay_no, port_name), timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_UPLINK_ETHERNET_PORT_SPEED % (enclosure_no, bay_no, port_name, port_speed), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_autonegotiation_text(cls, enclosure_no, bay_no, port_name, timeout=5, fail_if_false=True):
        logger.debug("Return Autonegotiation status for selected port [%s]" % port_name)
        return FusionUIBase.get_text(cls.e.ID_TEXT_AUTONEGOTIATION % (enclosure_no, bay_no, port_name), timeout, fail_if_false)


class _BaseEditLogicalInterconnectGroups(object):

    e = EditLogicalInterconnectGroupsElements

    @classmethod
    def select_actions_edit(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ Edit ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectGroupsElements.ID_BUTTON_ACTIONS, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_ACTION_EDIT, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_lig_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Edit logical interconnect group ] dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_EDIT_LIG, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_lig_dialog_disappear(cls, timeout=15, fail_if_false=True):
        logger.debug("wait [ Edit logical interconnect group ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_EDIT_LIG, timeout=timeout, fail_if_false=fail_if_false)

    # { dialog panel select
    @classmethod
    def select_general_section(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ General ] section")
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_PANEL_SELECTOR, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_GENERAL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_logical_interconnect_group_section(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ Logical Interconnect Group ] section")
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_PANEL_SELECTOR, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_LOGICAL_INTERCONNECT_GROUP, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_logical_interconnect_settings_section(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ Interconnect Settings ] section")
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_PANEL_SELECTOR, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_INTERCONNECT_SETTINGS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_logical_snmp_section(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ SNMP ] section")
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_PANEL_SELECTOR, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_SNMP, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_quality_of_service_section(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ Quality of Service ] section")
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_PANEL_SELECTOR, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_QUALITY_OF_SERVICE, timeout=timeout, fail_if_false=fail_if_false)
    # }

    @classmethod
    def input_name(cls, lig_name, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] to name textbox" % lig_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NAME, lig_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_ok_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ OK ] button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_OK, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_verifying_parameters_msg(cls, timeout=10, fail_if_false=True):
        logger.debug('wait message [ Verifying Parameters ]')
        return ui_lib.wait_for_element_visible(cls.e.ID_TEXT_VERIFYING_PARAMETERS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_status_changing_shown(cls, timeout=10, fail_if_false=True):
        return ui_lib.wait_for_element_visible(cls.e.ID_ICON_STATUS_CHANGING, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_status_changing_disappear(cls, timeout=15, fail_if_false=True):
        return ui_lib.wait_for_element_notvisible(cls.e.ID_ICON_STATUS_CHANGING, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_verifying_parameters_msg_disappear(cls, timeout=10, fail_if_false=True):
        logger.debug('wait message [ Verifying Parameters ] disappear')
        return ui_lib.wait_for_element_notvisible(cls.e.ID_TEXT_VERIFYING_PARAMETERS, timeout=timeout, fail_if_false=fail_if_false)

    # { internal network
    @classmethod
    def click_edit_internal_networks_gear(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ gear ] button in create lig dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_INTERNAL_NETWORKS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_internal_networks_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Edit Internal Network ] dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_EDIT_INTERNAL_NETWORKS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_internal_networks_add_networks(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add networks ] button in edit internal networks dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_internal_networks_remove_all(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Remove All ] button in edit internal networks dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_INTERNAL_NETWORKS_REMOVE_ALL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_internal_networks_add_networks_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait edit internal networks > [ Add Networks ] dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_edit_internal_networks_add_networks_search_network(cls, network, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into search network textbox in edit internal networks > add networks" % network)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_SEARCH_NETWORK, network, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_internal_networks_add_networks_table_row_shown(cls, network, timeout=5, fail_if_false=True):
        logger.debug("wait edit internal networks > add networks > table row [ %s ] shown" % network)
        return ui_lib.wait_for_element_visible(cls.e.ID_TABLE_ROW_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS % network, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_internal_networks_add_networks_add(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add ] button in edit internal networks > add networks dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_ADD, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_internal_networks_add_networks_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait edit internal networks > [ Add Networks ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_internal_networks_add_networks_add_plus(cls, timeout=5, fail_if_false=True):
        logger.debug("click [Add plus ] button in edit internal networks > add networks")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_ADD_PLUS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_internal_networks_table_row_shown(cls, network_name, timeout=5, fail_if_false=True):
        logger.debug("wait edit internal networks > table row [ %s ] shown" % network_name)
        return ui_lib.wait_for_element_visible(cls.e.ID_TABLE_ROW_EDIT_INTERNAL_NETWORKS % network_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_internal_networks_table_header_shown(cls, header_name, timeout=5, fail_if_false=True):
        logger.debug("wait edit internal networks > table row header [ %s ] shown" % header_name)
        return ui_lib.wait_for_element_visible(cls.e.ID_TABLE_ROW_TH_EDIT_INTERNAL_NETWORKS % header_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_internal_networks_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait edit internal networks > [ Edit Internal Networks ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_EDIT_INTERNAL_NETWORKS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_internal_networks_ok(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ OK ] button in edit internal networks")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_INTERNAL_NETWORKS_OK, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_internal_networks_cancel(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button in edit internal networks")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_INTERNAL_NETWORKS_CANCEL, timeout=timeout, fail_if_false=fail_if_false)
    # }

    # { uplink set
    @classmethod
    def click_add_uplink_set(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add uplink set ] button dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_UPLINK_SET, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_remove_all_networks(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Remove All ] networks button in create uplink set dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_REMOVE_ALL_ETHERNET_NETWORKS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_remove_all_uplink_ports(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Remove All ] uplink sets button in create uplink set dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_REMOVE_ALL_ETHERNET_PORTS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Create uplink set dialog ] shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_CREATE_UPLINK_SET, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Create uplink set dialog ] shown")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_CREATE_UPLINK_SET, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_create_uplink_set_name(cls, uplink_set_name, timeout=5, fail_if_false=True):
        logger.debug("input uplink set name [ %s ] in create uplink set dialog" % uplink_set_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_CREATE_UPLINK_SET_NAME, uplink_set_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_create_uplink_set_type(cls, uplink_set_type, timeout=5, fail_if_false=True):
        logger.debug("select uplink set type [ %s ] in create uplink set dialog" % uplink_set_type)
        FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_CREATE_UPLINK_SET_TYPE, uplink_set_type, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_create_uplink_set_connection_mode_automatic(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ Automatic (recommended) ] option")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_RADIO_CREATE_UPLINK_SET_CONNECTION_MODE_AUTOMATIC, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_create_uplink_set_lacp_timer(cls, uplink_set_lacp_timer, timeout=5, fail_if_false=True):
        logger.debug("select LACP timer [ %s ]" % uplink_set_lacp_timer)
        FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_CREATE_UPLINK_SET_LACP_TIMER, uplink_set_lacp_timer, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_create_uplink_set_connection_mode_failover(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ Failover ] option")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_RADIO_CREATE_UPLINK_SET_CONNECTION_MODE_FAILOVER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_create_uplink_set_native_network(cls, network_name, timeout=5, fail_if_false=True):
        logger.debug("tick vlan [ %s ] as native network in create uplink set dialog" % network_name)
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_CREATE_UPLINK_SET_ETHERNET_NATIVE % network_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_create_uplink_set_preferred_uplink_port(cls, bay_no, port_name, timeout=5, fail_if_false=True):
        logger.debug("tick [ bay%s:%s ] as preferred uplink port in create uplink set dialog" % (bay_no, port_name))
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_CREATE_UPLINK_SET_ETHERNET_PREFERRED_PORT % (bay_no, port_name), timeout=timeout, fail_if_false=fail_if_false)

    # - { uplink set network
    @classmethod
    def click_create_uplink_set_add_networks(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add networks ] button in create uplink set dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_networks_to_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set > [ Add networks to ] dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_CREATE_UPLINK_SET_ADD_NETWORKS_TO, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_create_uplink_set_add_networks_to_search_network(cls, network_name, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] to search network textbox in create uplink set > add networks to dialog" % network_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_CREATE_UPLINK_SET_ADD_NETWORKS_TO_SEARCH_NETWORK, network_name, timeout=timeout, fail_if_false=fail_if_false)
        # workaround to fix sometime specific network not show in table list
        time.sleep(1)
        ui_lib.get_s2l().press_key(cls.e.ID_INPUT_CREATE_UPLINK_SET_ADD_NETWORKS_TO_SEARCH_NETWORK, "\\8")
        ui_lib.get_s2l().press_key(cls.e.ID_INPUT_CREATE_UPLINK_SET_ADD_NETWORKS_TO_SEARCH_NETWORK, network_name[-1:])

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_networks_to_table_row_shown(cls, network_name, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set > add networks to [ %s ] table item shown" % network_name)
        return ui_lib.wait_for_element_visible(cls.e.ID_TABLE_ROW_CREATE_UPLINK_SET_ADD_NETWORKS_TO % network_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_networks_to_add(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add ] button in create uplink set > add networks to dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS_TO_ADD, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_networks_to_add_plus(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add plus ] button in create uplink set > add networks to dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS_TO_ADD_PLUS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_networks_to_cancel(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button in create uplink set > add networks to dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS_TO_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_networks_to_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set > [ Add networks to ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_CREATE_UPLINK_SET_ADD_NETWORKS_TO, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_create_uplink_set_tunnel_network(cls, network, timeout=5, fail_if_false=True):
        logger.debug("select tunnel network [ %s ] in create uplink set dialog" % network)
        FusionUIBase.choose_combo_option_by_text(cls.e.ID_COMBO_CREATE_UPLINK_SET_TUNNEL_NETWORK, network, timeout_sec=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_create_uplink_set_untagged_network(cls, network, timeout=5, fail_if_false=True):
        logger.debug("select untagged network [ %s ] in create uplink set dialog" % network)
        FusionUIBase.choose_combo_option_by_text(cls.e.ID_COMBO_CREATE_UPLINK_SET_UNTAGGED_NETWORK, network, timeout_sec=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_network_table_row_shown(cls, network, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set network [ %s ] table row shown" % network)
        return ui_lib.wait_for_element_visible(cls.e.ID_TABLE_ROW_CREATE_UPLINK_SET_NETWORK % network, timeout=timeout, fail_if_false=fail_if_false)
    # - }

    # - { lig uplink set port
    @classmethod
    def click_remove_uplink_set_icon(cls, uplinkset, timeout=5, fail_if_false=True):
        logger.debug("click [ remove icon ] of uplink set [ %s ]" % uplinkset)
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_REMOVE_UPLINK_SET % uplinkset, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_uplink_set_box_disappear(cls, uplinkset, timeout=5, fail_if_false=True):
        logger.debug("verify if uplink set box for [ %s ] disappear in edit lig dialog" % uplinkset)
        return ui_lib.wait_for_element_notvisible(cls.e.ID_TITLE_UPLINK_SET_BOX % uplinkset, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_uplink_set_icon(cls, uplinkset, timeout=5, fail_if_false=True):
        logger.debug("click [ edit icon ] of uplink set [ %s ]" % uplinkset)
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_UPLINK_SET % uplinkset, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_uplink_set_dialog_shown(cls, uplinkset, timeout=5, fail_if_false=True):
        logger.debug("wait [ Edit %s ] dialog shown" % uplinkset)
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_EDIT_UPLINK_SET % uplinkset, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_uplink_ports(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add uplink ports ] button in create uplink set dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_UPLINK_PORTS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_uplink_ports_to_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set > [ Add uplink ports to ] dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_TO, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_create_uplink_set_add_uplink_ports_to_search_port(cls, port_name, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] to search port textbox in create uplink set > add uplink ports to dialog" % port_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_CREATE_UPLINK_SET_ADD_UPLINK_PORT_SEARCH_PORT, port_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_uplink_ports_to_table_row_shown(cls, bay_no, port_name, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set > add uplink ports to [ bay%s:%s ] table item shown" % (bay_no, port_name))
        return ui_lib.wait_for_element_visible(cls.e.ID_TABLE_ROW_CREATE_UPLINK_SET_ADD_UPLINK_PORT.format(bay_no, port_name), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_uplink_ports_to_table_row(cls, bay_no, port_name, timeout=5, fail_if_false=True):
        logger.debug("click [ bay%s:%s ] table item in create uplink set > add uplink ports to dialog" % (bay_no, port_name))
        ui_lib.wait_for_element_and_click(cls.e.ID_TABLE_ROW_CREATE_UPLINK_SET_ADD_UPLINK_PORT.format(bay_no, port_name), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_uplink_ports_to_add(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add ] button in create uplink set > add uplink ports to dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_ADD, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_uplink_ports_to_add_plus(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add plus ] button in create uplink set > add uplink ports to dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_ADD_PLUS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_uplink_ports_to_cancel(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button in create uplink set > add uplink ports to dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_uplink_ports_to_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set > [ Add uplink ports to ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_TO, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_port_table_row_shown(cls, bay_no, port, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set port [ %s:%s ] table row shown" % (bay_no, port))
        return ui_lib.wait_for_element_visible(cls.e.ID_TABLE_ROW_CREATE_UPLINK_SET_PORT.format(bay_no, port), timeout=timeout, fail_if_false=fail_if_false)
    # - }

    # { - fc
    @classmethod
    def select_create_uplink_set_fc_network(cls, network, timeout=5, fail_if_false=True):
        logger.debug("select fc network [ %s ] in create uplink set dialog" % network)
        FusionUIBase.choose_combo_option_by_text(cls.e.ID_COMBO_CREATE_UPLINK_SET_FC_NETWORK, network, timeout_sec=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_create_uplink_set_fc_interconnect(cls, interconnect, timeout=5, fail_if_false=True):
        logger.debug("select fc interconnect [ %s ] in create uplink set dialog" % interconnect)
        FusionUIBase.choose_combo_option_by_text(cls.e.ID_COMBO_CREATE_UPLINK_SET_FC_INTERCONNECT, interconnect, timeout_sec=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_create_uplink_set_fc_port(cls, port, timeout=5, fail_if_false=True):
        logger.debug("tick fc port [ %s ] in create uplink set dialog" % port)
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_CREATE_UPLINK_SET_FC_PORT % port, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_create_uplink_set_fc_port_speed(cls, bay_no, port_name, port_speed, timeout=5, fail_if_false=True):
        """

        :param bay_no: bay number as integer.(don't pass bay_no like 'bay1')
        :param port_name:
        :param port_speed:
        :param timeout:
        """
        logger.debug("select port speed [ %s ] for fc port [ %s ] of bay [ %s ] in create uplink set dialog" % (port_speed, port_name, bay_no))
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_CREATE_UPLINK_SET_FC_PORT_SPEED.format(bay_no, port_name), timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_CREATE_UPLINK_SET_FC_PORT_SPEED.format(bay_no, port_name, port_speed), timeout=timeout, fail_if_false=fail_if_false)
    # - }

    # buttons
    @classmethod
    def click_create_uplink_set_add(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add ] button in create uplink set dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_plus(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add plus ] button in create uplink set dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_PLUS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_cancel(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button in create uplink set dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_UPLINK_SET_ADD_CANCEL, timeout=timeout, fail_if_false=fail_if_false)
    # }

    # { Interconnect Settings
    @classmethod
    def tick_interconnect_settings_fast_mac_cache_failover(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ Fast MAC cache failover ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_FAST_MAC_CACHE_FAILOVER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def untick_interconnect_settings_fast_mac_cache_failover(cls, timeout=5, fail_if_false=True):
        logger.debug("untick [ Fast MAC cache failover ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_FAST_MAC_CACHE_FAILOVER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_interconnect_settings_mac_refresh_interval(cls, mac_refresh_interval, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [ MAC refresh interval ] in section [ Interconnect Settings ]" % mac_refresh_interval)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_MAC_REFRESH_INTERVAL, mac_refresh_interval, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_interconnect_settings_igmp_snooping(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ IGMP Snooping ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_IGMP_SNOOPING, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def untick_interconnect_settings_igmp_snooping(cls, timeout=5, fail_if_false=True):
        logger.debug("untick [ IGMP Snooping ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_IGMP_SNOOPING, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_interconnect_settings_igmp_idle_timeout_interval(cls, igmp_idle_timeout_interval, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [ IGMP idle timeout interval ] in section [ Interconnect Settings ]" % igmp_idle_timeout_interval)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_IGMP_IDLE_TIMEOUT_INTERVAL, igmp_idle_timeout_interval, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_interconnect_settings_loop_protection(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ Loop protection ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_LOOP_PROTECTION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def untick_interconnect_settings_loop_protection(cls, timeout=5, fail_if_false=True):
        logger.debug("untick [ Loop protection ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_LOOP_PROTECTION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_interconnect_settings_pause_flood_protection(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ Pause flood protection ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_PAUSE_FLOOD_PROTECTION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def untick_interconnect_settings_pause_flood_protection(cls, timeout=5, fail_if_false=True):
        logger.debug("untick [ Pause flood protection ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_PAUSE_FLOOD_PROTECTION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_interconnect_settings_lldp_tagging(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ LLDP Tagging ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_LLDP_TAGGING, timeout=timeout, fail_if_false=True)

    @classmethod
    def untick_interconnect_settings_lldp_tagging(cls, timeout=5, fail_if_false=True):
        logger.debug("untick [ LLDP Tagging ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_LLDP_TAGGING, timeout=timeout, fail_if_false=True)

    @classmethod
    def tick_interconnect_settings_lldp_enhancedtlv(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ LLDP Enhaced TLV ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_LLDP_ENHANCED_TLV, timeout=timeout, fail_if_false=True)

    @classmethod
    def untick_interconnect_settings_lldp_enhancedtlv(cls, timeout=5, fail_if_false=True):
        logger.debug("untick [ LLDP Enhaced TLV ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_LLDP_ENHANCED_TLV, timeout=timeout, fail_if_false=True)

    # }

    # { SNMP
    @classmethod
    def toggle_snmp_enabled(cls, timeout=5):
        logger.debug("toggle snmp [ Enabled ]")
        FusionUIBase.toggle_button(cls.e.ID_TOGGLE_SNMP, "Enabled", timeout=timeout)

    @classmethod
    def toggle_snmp_disabled(cls, timeout=5):
        logger.debug("toggle snmp [ Disabled ]")
        FusionUIBase.toggle_button(cls.e.ID_TOGGLE_SNMP, "Disabled", timeout=timeout)

    @classmethod
    def input_snmp_system_contact(cls, syscontact, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into SNMP System contact" % syscontact)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SYSTEM_CONTACT, syscontact, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_snmp_read_community(cls, readcommunity, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into SNMP Read community" % readcommunity)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_READ_COMMUNITY, readcommunity, timeout=timeout, fail_if_false=fail_if_false)

    # - { Snmpv3 users
    @classmethod
    def click_remove_snmp_user_icon(cls, user, timeout=5, fail_if_false=True):
        logger.debug("click [ remove snmp user ] icon ")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_REMOVE_SNMP_USER % user, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_remove_snmp_user_confirm(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ remove trap destination ] icon ")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_REMOVE_SNMP_USER_CONFIRM, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_snmp_user(cls, user, timeout=5, fail_if_false=True):
        logger.debug("click [ Edit snmp user] icon ")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_SNMP_USER % user, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_snmp_user_edit(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ ok button ] icon in edit snmp user")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_OK_EDIT_SNMP_USER, timeout=timeout, fail_if_false=fail_if_false)

    # }
    # - { Trap Destinations
    @classmethod
    def click_add_trap_destination(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add trap destination ] button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def wait_add_trap_destination_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add Trap Destination ] dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_ADD_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def wait_add_trap_destination_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add Trap Destination ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_ADD_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_remove_trap_destination_icon(cls, destination, timeout=5, fail_if_false=True):
        logger.debug("click [ remove trap destination ] icon of %s" % destination)
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_DELETE_TRAP_DESTINATION % destination, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_remove_snmpv3_trap_destination_icon(cls, destination, timeout=5, fail_if_false=True):
        logger.debug("click [ remove trap destination ] icon of %s" % destination)
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_DELETE_SNMPV3_TRAP_DESTINATION % destination, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_trap_destination_table_row_shown(cls, destination, timeout=5, fail_if_false=True):
        logger.debug("wait SNMP trap destination table row [ %s ] shown" % destination)
        return ui_lib.wait_for_element_visible(cls.e.ID_BUTTON_DELETE_TRAP_DESTINATION % destination, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_trap_destination_table_row_disappear(cls, destination, timeout=5, fail_if_false=True):
        logger.debug("wait SNMP trap destination table [ %s ] disappear" % destination)
        return ui_lib.wait_for_element_notvisible(cls.e.ID_BUTTON_DELETE_TRAP_DESTINATION % destination, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_trap_destination_icon(cls, destination, timeout=5, fail_if_false=True):
        logger.debug("click [ edit trap destination ] icon of %s" % destination)
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_TRAP_DESTINATION % destination, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_trap_destination_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add Trap Destination ] dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_EDIT_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_trap_destination_ok(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ edit trap destination ] ok button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_TRAP_DESTINATION_OK, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def wait_edit_trap_destination_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add Trap Destination ] dialog shown")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_EDIT_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_trap_destination_confirm_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait remove trap destination confirm dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_REMOVE_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_remove_trap_destination_yes_remove(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Yes, Remove ] button in remove trap destination confirm dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_REMOVE_TRAP_DESTINATION_YES_REMOVE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_trap_destination_confirm_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait remove trap destination confirm dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_REMOVE_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_add_trap_destination_trap_destination(cls, trapdestination, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [ Trap destination ] in Add Trap Destination dialog" % trapdestination)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ADD_TRAP_DESTINATION_TRAP_DESTINATION, trapdestination, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_add_trap_destination_community_string(cls, communitystring, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [ Community string ] in Add Trap Destination dialog" % communitystring)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ADD_TRAP_DESTINATION_COMMUNITY_STRING, communitystring, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_add_trap_destination_trap_format_snmpv1(cls, timeout=5, fail_if_false=True):
        logger.debug("tick Trap Format [ SNMPv1 ]")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_ADD_TRAP_DESTINATION_TRAP_FORMAT_SNMPV1, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_add_trap_destination_trap_format_snmpv2(cls, timeout=5, fail_if_false=True):
        logger.debug("tick Trap Format [ SNMPv2 ]")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_ADD_TRAP_DESTINATION_TRAP_FORMAT_SNMPV2, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_trap_destination_add(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add ] button in Add Trap Destination dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_TRAP_DESTINATION_ADD, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_trap_destination_add_plus(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add plus ] button in Add Trap Destination dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_TRAP_DESTINATION_ADD_PLUS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_trap_destination_cancel(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button in Add Trap Destination dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_TRAP_DESTINATION_CANCEL, timeout=timeout, fail_if_false=fail_if_false)
    # - }

    # - { SNMP Access
    @classmethod
    def click_add_snmp_access(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add SNMP access ] button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_SNMP_ACCESS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def wait_add_snmp_access_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add SNMP Access ] dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_ADD_SNMP_ACCESS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def wait_add_snmp_access_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add SNMP Access ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_ADD_SNMP_ACCESS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_remove_snmp_access_icon(cls, iporsubnet, timeout=5, fail_if_false=True):
        logger.debug("click [ remove snmp access ] icon of %s" % iporsubnet)
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_DELETE_SNMP_ACCESS % iporsubnet, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_snmp_access_table_row_shown(cls, iporsubnet, timeout=5, fail_if_false=True):
        logger.debug("wait SNMP snmp access table row [ %s ] shown" % iporsubnet)
        return ui_lib.wait_for_element_visible(cls.e.ID_BUTTON_DELETE_SNMP_ACCESS % iporsubnet, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_snmp_access_table_row_disappear(cls, iporsubnet, timeout=5, fail_if_false=True):
        logger.debug("wait SNMP snmp access table [ %s ] disappear" % iporsubnet)
        return ui_lib.wait_for_element_notvisible(cls.e.ID_BUTTON_DELETE_SNMP_ACCESS % iporsubnet, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_snmp_access_icon(cls, iporsubnet, timeout=5, fail_if_false=True):
        logger.debug("click [ edit snmp access ] icon of %s" % iporsubnet)
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_SNMP_ACCESS % iporsubnet, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_snmp_access_confirm_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait remove snmp access confirm dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_REMOVE_SNMP_ACCESS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_remove_snmp_access_yes_remove(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Yes, Remove ] button in remove snmp access confirm dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_REMOVE_SNMP_ACCESS_YES_REMOVE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_snmp_access_confirm_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait remove snmp access confirm dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_REMOVE_SNMP_ACCESS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_add_snmp_access_ip_or_subnet(cls, iporsubnet, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [ IP or subnet ] in Add SNMP Access dialog" % iporsubnet)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ADD_SNMP_ACCESS_IP_OR_SUBNET, iporsubnet, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_snmp_access_add(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add ] button in Add SNMP Access dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_SNMP_ADD, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_snmp_access_add_plus(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add plus ] button in Add SNMP Access dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_SNMP_ADD_PLUS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_snmp_access_cancel(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button in Add SNMP Access dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_SNMP_CANCEL, timeout=timeout, fail_if_false=fail_if_false)
    # - }
    # }

    # { Quality of Service (QoS)
    @classmethod
    def select_qos_configuration_type(cls, qos_configuration_type, timeout=5, fail_if_false=True):
        logger.debug("select QoS configuration type [ %s ]" % qos_configuration_type)
        FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_QOS_CONFIGURATION_TYPE, qos_configuration_type, timeout=timeout, fail_if_false=fail_if_false)
    # }

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_quality_of_service_qos_configuration_type(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ QoS configuration type ] in SNMP view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("QoS configuration type", cls.e.ID_TEXT_QUALITY_OF_SERVICE_QOS_CONFIGURATION_TYPE, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_fcoelosssless_class_exists(cls, classname, timeout=5, fail_if_false=False):
        logger.debug("Checking FCoE Lossless")
        return ui_lib.wait_for_element_visible(cls.e.ID_OPTION_EDITCLASS % classname, timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_fcoe_lossless_class_no_edit_option(cls, classname, timeout=5, fail_if_false=True):
        logger.debug("Checking for the FCOElossless class ")
        if ui_lib.wait_for_element_notvisible(cls.e.ID_OPTION_EDIT % classname, timeout=5, fail_if_false=fail_if_false):
            logger.debug("Successfully verified FCoE lossless class has no edit option")
            return True
        else:
            logger.warn("clicked edit option for %s " % classname)
            return False

    @classmethod
    def get_fcoeshare(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking for FCoELosslessShare ")
        return FusionUIBase.get_text(cls.e.ID_TEXT_SHARE)

    @classmethod
    def get_fcoemaxshare(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking for FCoELosslessmaxShare ")
        return FusionUIBase.get_text(cls.e.ID_TEXT_MAXSHARE)

    @classmethod
    def click_qos_class(cls, timeout=5, fail_if_false=True):
        logger.debug("click Enable button")
        if ui_lib.wait_for_element_visible(cls.e.ID_TEXT_DISABLED, timeout, fail_if_false):
            logger.debug("class is already enabled")
            return False
        else:
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CLASS_ENABLE, timeout, fail_if_false)
            logger.debug("class is enabled")
            return True

    @classmethod
    def input_share_values(cls, share_values, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into Share" % share_values)
        return ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SHAREVALUES, share_values, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_class_ok_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ OK ] button")
        return ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CLASS_OK, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_classname(cls, classname, timeout=5, fail_if_false=True):
        logger.debug("click the class name")
        return ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_EDITCLASS % classname, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_classname(cls, lig_name, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] to name textbox" % lig_name)
        return ui_lib.wait_for_element_and_input_text(cls.e.ID_TEXT_INPUT_NAME, lig_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_error_message(cls, timeout=5, fail_if_false=True, hidden_element=False):
        return ui_lib.get_text(cls.e.ID_TEXT_VALIDATE_MSG, timeout, fail_if_false, hidden_element)

    @classmethod
    def get_share_value(cls, classno, share, timeout=5, fail_if_false=True):
        logger.debug("getting share value for the class %s" % classno)
        return ui_lib.get_text(cls.e.ID_TEXT_SHAREVALUE % (classno, share), timeout, fail_if_false)

    @classmethod
    def get_qos_error_msg(cls, timeout=5, fail_if_false=True):
        logger.debug("getting the error mesg")
        ui_lib.wait_for_element_visible(cls.e.ID_TEXT_QOS_ERROR, timeout, fail_if_false)
        return ui_lib.get_text(cls.e.ID_TEXT_QOS_ERROR, timeout, fail_if_false)

    @classmethod
    def get_uniquename(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking for Unique names ")
        return FusionUIBase.get_multi_elements_text(cls.e.ID_TABLE_CLASS_LIST)

    @classmethod
    def click_max_text(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Max ] text")
        return ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_MAX, timeout, fail_if_false)

    @classmethod
    def click_traffic_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button")
        return ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CLASS_CANCEL, timeout, fail_if_false)

    @classmethod
    def select_editoption(cls, classname, timeout=5, fail_if_false=True):
        logger.debug("Clicking the edit option for %s " % classname)
        if ui_lib.wait_for_element_and_click(EditLogicalInterconnectGroupsElements.ID_OPTION_EDIT % classname, timeout=5, fail_if_false=fail_if_false):
            logger.debug("Clicked the edit option for %s " % classname)
            return True
        else:
            logger.debug("Failed to click edit option for %s " % classname)
            return False

    @classmethod
    def input_shareormax(cls, validateshareor, value, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] to share or Maxshare textbox" % validateshareor)
        return ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SHAREORMAX % validateshareor, value, timeout, fail_if_false)

    @classmethod
    def select_egress_fields(cls, timeout=5, fail_if_false=True):
        logger.debug("click egress mappings")
        return ui_lib.wait_for_element_and_click(cls.e.ID_TEXT_EGRESS_MAPPINGS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_egress_priority_values(cls, timeout=5, fail_if_false=True):
        logger.debug("fetching the Egress priority values")
        ui_lib.wait_for_element_visible(cls.e.ID_TABLE_EGRESS_FIELDS, timeout, fail_if_false)
        return FusionUIBase.get_multi_elements_text(cls.e.ID_TABLE_EGRESS_FIELDS, timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_class_enabled(cls, classno, timeout=5, fail_if_false=True):
        logger.debug("Check for the class %s" % classno)
        return ui_lib.get_text(cls.e.ID_TEXT_CLASS_NAME % classno, timeout=5, fail_if_false=fail_if_false)

    @classmethod
    def click_dot1p_priority_dropdown(cls, timeout=5, fail_if_false=True):
        logger.debug("click dot1p priority dropdown list")
        return ui_lib.wait_for_element_and_click(EditLogicalInterconnectGroupsElements.ID_DOT1P_DROPDOWN_LIST, timeout, fail_if_false)

    @classmethod
    def select_dot1p_priority(cls, i, timeout=5, fail_if_false=True):
        logger.debug("select dot1p priority %s" % i)
        return FusionUIBase.get_text(EditLogicalInterconnectGroupsElements.ID_TEXT_DOT1P_PRIORITY % i, timeout, fail_if_false)

    @classmethod
    def get_text_dot1p_value(cls, i, timeout=5, fail_if_false=True):
        logger.debug("select dot1p priority %s" % i)
        return FusionUIBase.get_text(EditLogicalInterconnectGroupsElements.ID_TABLE_DOT1P_VALUE % i, timeout, fail_if_false)

    @classmethod
    def get_text_dot1p_current(cls, i, timeout=5, fail_if_false=True):
        logger.debug("select dot1p priority %s" % i)
        return FusionUIBase.get_text(EditLogicalInterconnectGroupsElements.ID_TABLE_DOT1P_CURRENT % i, timeout, fail_if_false)

    @classmethod
    def get_text_dscp_value(cls, i, timeout=5, fail_if_false=True):
        logger.debug("select dscp value %s" % i)
        return FusionUIBase.get_text(EditLogicalInterconnectGroupsElements.ID_TEXT_DSCP_VALUE % i, timeout, fail_if_false)

    @classmethod
    def get_text_dscp_current(cls, i, timeout=5, fail_if_false=True):
        logger.debug("select dscp current %s" % i)
        return FusionUIBase.get_text(EditLogicalInterconnectGroupsElements.ID_TEXT_DSCP_CURRENT % i, timeout, fail_if_false)

    @classmethod
    def get_real_time_value_of_class(cls, enableclass, timeout=5, fail_if_false=True):
        logger.debug("The real time is enabled")
        return ui_lib.get_text(cls.e.ID_REAL_TIME_VALUE % enableclass, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_real_time_coloumn_value(cls, classname, timeout=5, fail_if_false=True):
        logger.debug("The real time coloumn value")
        return ui_lib.get_text(cls.e.ID_REAL_TIME_COL % classname, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_realtime_sharevalue(cls, i, share, timeout=5, fail_if_false=True):
        logger.debug("The real time share values")
        return ui_lib.get_text(cls.e.ID_REAL_TIME_SHAREVALUE % (i, share), timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_actions_menu(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectGroupsElements.ID_BUTTON_ACTIONS, timeout=timeout, fail_if_false=fail_if_false)
        return ui_lib.wait_for_element_visible(GeneralLogicalInterconnectGroupsElements.ID_LINK_ACTION_DROPDOWN, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_best_effort_class(cls, timeout=5, fail_if_false=True):
        logger.debug("select the disabled text")
        if ui_lib.wait_for_element_visible(cls.e.ID_TEXT_ENABLED_BESTEFFORT, timeout, fail_if_false):
            logger.warn("class is already enabled")
            return False
        else:
            logger.debug("enabled the selected class ")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CLASS_ENABLE, timeout, fail_if_false)
            return True

    @classmethod
    def input_maxshare_value(cls, text, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] to name textbox" % text)
        return ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_MAXSHARE_VALUES, text, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_dot1p_values(cls, DOT1P, timeout=5, fail_if_false=True):
        logger.debug("tick DOTIP option")
        return FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_DOT1P_VALUES % DOT1P, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def tick_dscp_values(cls, Dscpvalue, timeout=5, fail_if_false=True):
        logger.debug("tick DSCP option")
        ui_lib.wait_for_element_visible(cls.e.ID_CHECKBOX_DSCP_VALUES % Dscpvalue, timeout, fail_if_false)
        return FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_DSCP_VALUES % Dscpvalue, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_egress_priority(cls, priority, timeout=5, fail_if_false=True):
        logger.debug("select QoS configuration type [ %s ]" % priority)
        return ui_lib.select_from_dropdown_by_dataid(cls.e.ID_DROPDOWN_EGRESS_PRIORITY, priority, timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_maxsharevalue(cls, realclass, timeout=5, fail_if_false=True):
        ui_lib.wait_for_element_visible(cls.e.ID_TEXT_MAXSHAREVALUE % realclass, timeout, fail_if_false)
        return ui_lib.get_text(cls.e.ID_TEXT_MAXSHAREVALUE % realclass, timeout, fail_if_false)

    @classmethod
    def get_dot1p_dscp_mapping_values(cls, value, timeout=5, fail_if_false=True):
        logger.debug("Got ingress dot1p & dscp mapping values")
        return ui_lib.get_text(cls.e.ID_TEXT_DOT1P_DSCP_MAPPINGS % value, timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_qos_real_class(cls, timeout=5, fail_if_false=True):
        logger.debug("click Enable button")
        return ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_REALCLASS_ENABLE, timeout, fail_if_false)

    @classmethod
    def click_reset_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click Reset button")
        return ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_RESET, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_besteffort_fcoe_priority(cls, timeout=5, fail_if_false=True):
        besteffort_fcoe_priority = []
        besteffort_fcoe_priority.append(FusionUIBase.get_text(cls.e.ID_BEST_EFFORT_PRIORITY))
        besteffort_fcoe_priority.append(FusionUIBase.get_text(cls.e.ID_FCOE_LOSELESS_PRIORITY))
        return besteffort_fcoe_priority

    @classmethod
    def click_qos_class_disable(cls, timeout=5, fail_if_false=True):
        logger.debug("Disable the class")
        return ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_CLASS_DISABLE, timeout, fail_if_false)

    @classmethod
    def click_button_traffic_class(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CLASS_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_real_time_value_of_class(cls, enableclass, timeout=5, fail_if_false=True):
        logger.debug("The real time is enabled")
        return ui_lib.get_text(cls.e.ID_REAL_TIME_VALUE % enableclass, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_real_time_coloumn_value(cls, i, timeout=5, fail_if_false=True):
        logger.debug("The real time coloumn value")
        return ui_lib.get_text(cls.e.ID_REAL_TIME_COL % i, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_traffic_class_value(cls, i, timeout=5, fail_if_false=True):
        logger.debug("The real time class value")
        return ui_lib.get_text(cls.e.ID_REAL_TIME_CLASSVALUE % i, timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_egress_priority_fields(cls, value, timeout=10, fail_if_false=True):
        logger.debug("Got egress priority values mapping values")
        return ui_lib.get_text(cls.e.ID_TABLE_EGRESS_PRIORITY_VALUES % value, timeout=10, fail_if_false=fail_if_false)


class EditLogicalInterconnectGroups(_BaseEditLogicalInterconnectGroups):
    pass


class C7000EditLogicalInterconnectGroups(_BaseEditLogicalInterconnectGroups):

    e = C7000EditLogicalInterconnectGroupsElements

    @classmethod
    def select_bay_type(cls, bay_no, bay_type, timeout=5, fail_if_false=True):
        logger.debug("select bay type [ %s ] for bay [ %s ]" % (bay_type, bay_no))
        # FusionUIBase.choose_option_by_text(EditLogicalInterconnectGroupsElements.ID_SELECT_BAY_TYPE % bay_no, bay_type, timeout, fail_if_false=True)
        ui_lib.get_s2l().execute_javascript(cls.e.ID_JAVASCRIPT_BAY_TYPE % bay_no)
        time.sleep(1)
        ui_lib.wait_for_element_visible(cls.e.ID_DROPDOWN_BAY_TYPE_OPTION_LAYER % bay_no, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.get_s2l().execute_javascript(cls.e.ID_JAVASCRIPT_SELECT_BAY_TYPE % (bay_no, bay_type))
        ui_lib.wait_for_element_visible(cls.e.ID_SELECTED_BAY_TYPE % (bay_no, bay_type), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_remove_trap_destination_icon(cls, destination, timeout=5, fail_if_false=True):
        logger.debug("click [ remove trap destination ] icon of %s" % destination)
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_DELETE_TRAP_DESTINATION % destination, timeout=timeout, fail_if_false=fail_if_false)


class TBirdEditLogicalInterconnectGroups(_BaseEditLogicalInterconnectGroups):

    e = TBirdEditLogicalInterconnectGroupsElements

    @classmethod
    def select_bay_type(cls, bay_no, bay_type, encl_no=1, timeout=5, fail_if_false=True):
        logger.debug("select bay type [ %s ] for bay [ %s ]" % (bay_type, bay_no))
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_BAY_TYPE % (encl_no, bay_no), timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_BAY_TYPE_VALUE % (encl_no, bay_no, bay_type), timeout=timeout, fail_if_false=fail_if_false)

    def select_bay_type_fc(cls, bay_no, bay_type, encl_no=1, timeout=5, fail_if_false=True):
        logger.debug("select bay type [ %s ] for bay [ %s ]" % (bay_type, bay_no))
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_BAY_TYPE_FC % (encl_no, bay_no), timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_BAY_TYPE_VALUE_FC % (encl_no, bay_no, bay_type), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_actions_edit_dfrm(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ Edit ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ACTIONS_DFRM, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_ACTION_EDIT_DFRM, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_remove_trap_destination_icon_tbird(cls, destination, timeout=5, fail_if_false=True):
        logger.debug("click [ remove trap destination ] icon of %s" % destination)
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_TBIRD_DELETE_TRAP_DESTINATION % destination, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_warning_message_details(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Warning Message ] to shown details")
        return ui_lib.wait_for_element_and_click(TBirdGeneralLogicalInterconnectGroupsElements.ID_TEXT_WARNING_MESSAGE, timeout, fail_if_false)


class _BaseDeleteLogicalInterconnectGroups(object):

    e = DeleteLogicalInterconnectGroupsElements

    @classmethod
    def select_actions_delete(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ Delete ] action button")
        ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectGroupsElements.ID_BUTTON_ACTIONS, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_ACTION_DELETE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_sas_actions_delete(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ Delete ] action button")
        ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectGroupsElements.ID_SAS_BUTTON_ACTIONS, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SAS_SELECT_ACTION_DELETE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Delete ] dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_DELETE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Delete ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_DELETE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_error_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Delete Error ] dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_DELETE_ERROR, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_error_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Delete Error ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_DELETE_ERROR, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_delete_error_text(cls, timeout=5, fail_if_false=True):
        logger.debug("Get error text in delete error dialog")
        return FusionUIBase.get_text(cls.e.ID_TEXT_DELETE_ERROR, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_close(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Delete ] button in delete error dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CLOSE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_yes_delete_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Yes, delete ] button in delete dialog")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_YES_DELETE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_lig_show_not_found(cls, lig_name, timeout=5, fail_if_false=True):
        logger.info("wait [ LIG %s status ] change to 'not found'" % lig_name)
        return ui_lib.wait_for_element_visible(cls.e.ID_TABLE_LIG_DELETED % lig_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_error_displayed(cls, timeout=5, fail_if_false=True):
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_DELETE_LIG_ERROR, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_delete_error_message_on_confirm_dialog(cls, timeout=5, fail_if_false=True):
        return ui_lib.get_text(cls.e.ID_DIALOG_DELETE_LIG_ERROR, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_error_resolution_on_confirm_dialog(cls, timeout=5, fail_if_false=True):
        return ui_lib.get_text(cls.e.ID_DIALOG_DELETE_LIG_ERROR_RESOLUTION, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_error_popup_close(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Cancel button")
        ui_lib.wait_for_element_and_click(cls.e.ID_DIALOG_BUTTON_CANCEL, timeout, fail_if_false)


class DeleteLogicalInterconnectGroups(_BaseDeleteLogicalInterconnectGroups):
    pass


class C7000DeleteLogicalInterconnectGroups(_BaseDeleteLogicalInterconnectGroups):
    pass


class TBirdDeleteLogicalInterconnectGroups(_BaseDeleteLogicalInterconnectGroups):
    pass


class _BaseVerifyLogicalInterconnectGroups(object):
    # { General verification

    e = GeneralLogicalInterconnectGroupsElements

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_lig_not_exist(cls, lig, timeout=10, fail_if_false=True):
        logger.debug("verify [ LIG '%s' ] should NOT exist ..." % lig)
        if ui_lib.wait_for_element_notvisible(cls.e.ID_TABLE_LIG % lig, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("[ LIG '%s' ] successfully verified as invisible" % lig)
            return True
        else:
            logger.warn("failed to verify [ LIG '%s' ] as invisible" % lig)
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_lig_exist(cls, lig, timeout=10, fail_if_false=True):
        logger.debug("verify [ LIG '%s' ] should exist ..." % lig)
        if ui_lib.wait_for_element_visible(cls.e.ID_TABLE_LIG % lig, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("[ LIG '%s' ] successfully verified visible" % lig)
            return True
        else:
            logger.warn("failed to verify [ LIG '%s' ] as visible" % lig)
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_notification_shown(cls, timeout=5, fail_if_false=False):
        logger.debug("verify [ Notification ] display")
        return ui_lib.wait_for_element_visible(cls.e.ID_PANEL_NOTIFICATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_actions_button_available(cls, timeout=5, fail_if_false=True):
        return ui_lib.wait_for_element_visible(GeneralLogicalInterconnectGroupsElements.ID_BUTTON_ACTIONS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_actions_delete_option_available(cls, timeout=5, fail_if_false=True):
        return ui_lib.wait_for_element_visible(DeleteLogicalInterconnectGroupsElements.ID_SELECT_ACTION_DELETE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_scope_should_exist_in_edit_page(cls, name, timeout=5, fail_if_false=True):
        logger.debug("verify [ scope '%s' ] exist in scope edit page" % name)
        return ui_lib.wait_for_element_visible(EditScopeElements.ID_TABLE_SCOPE_NAME % name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_priority_availability(cls, flag, timeout=5, fail_if_false=True):
        if flag:
            logger.debug(" priority is visible")
            return ui_lib.wait_for_element_visible(EditLogicalInterconnectGroupsElements.ID_TABLE_DOT1P_AVAILABILITY)
        else:
            logger.debug(" priority not visible")
            return ui_lib.wait_for_element_notvisible(EditLogicalInterconnectGroupsElements.ID_TABLE_DOT1P_AVAILABILITY)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_dot1p_and_dscp_availability(cls, flag, fail_if_false=True):
        if not flag:
            logger.debug("dot1p and dscp are not visible")
            return ui_lib.wait_for_element_notvisible(EditLogicalInterconnectGroupsElements.ID_TABLE_DOT1P_MAPPING, EditLogicalInterconnectGroupsElements.ID_TABLE_DSCP_MAPPING)
        else:
            logger.debug("dot1p and dscp are visible")
            return ui_lib.wait_for_element_visible(EditLogicalInterconnectGroupsElements.ID_TABLE_DOT1P_MAPPING, EditLogicalInterconnectGroupsElements.ID_TABLE_DSCP_MAPPING)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_realclass_invisibility(cls, timeout=5, fail_if_false=True):
        logger.debug("select the disabled text")
        if ui_lib.wait_for_element_visible(EditLogicalInterconnectGroupsElements.ID_TEXT_DISABLED, timeout, fail_if_false):
            logger.debug("class is already enabled")
            ui_lib.wait_for_element_and_click(EditLogicalInterconnectGroupsElements.ID_TEXT_DISABLED, timeout, fail_if_false)
            return ui_lib.wait_for_element_notvisible(C7000EditLogicalInterconnectGroupsElements.ID_BUTTON_REALCLASS_ENABLE, timeout, fail_if_false)
        else:
            logger.debug("enabled the selected class ")
            ui_lib.wait_for_element_visible(EditLogicalInterconnectGroupsElements.ID_BUTTON_CLASS_ENABLE, timeout, fail_if_false)
            return ui_lib.wait_for_element_notvisible(C7000EditLogicalInterconnectGroupsElements.ID_BUTTON_REALCLASS_ENABLE, timeout, fail_if_false)

    # { General verification

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_interconnect_settings_redundancy(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ redundancy info ] in LOGICAL INTERCONNECT SETTINGS, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Redundancy", cls.e.ID_TEXT_INTERCONNECT_SETTINGS_REDUNDANCY, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_type(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ type ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("State", cls.e.ID_TEXT_GENERAL_TYPE, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_used_by_eg(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Used By EG ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Used by EG", cls.e.ID_TEXT_GENERAL_USED_BY_EG, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_used_by_li(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Used By LI ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Used by LI", cls.e.ID_TEXT_GENERAL_USED_BY_LI, expect_value, timeout=timeout, fail_if_false=fail_if_false)
    # }

    # { Internal networks
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_internal_network_count(cls, expect_value, timeout=5, fail_if_false=True):
        expect_value = "(%d)" % expect_value
        logger.debug("verify [ Internal network count ] in internal network view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Internal network count", cls.e.ID_TEXT_INTERNAL_NETWORKS_COUNT, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_internal_network_name_exist(cls, net_name, timeout=5, fail_if_false=True):
        logger.debug("verify [ name '%s' ] exist in internal network view" % net_name)
        return ui_lib.wait_for_element_visible(cls.e.ID_TEXT_INTERNAL_NETWORKS_ITEM_NAME % net_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_internal_network_vlan(cls, net_name, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ vlan '%s' ] of [ network '%s' ] exist in internal network view" % (expect_value, net_name))
        return FusionUIBase.verify_element_text("Internal network vlan", cls.e.ID_TEXT_INTERNAL_NETWORKS_VLAN % net_name, expect_value, timeout=timeout, fail_if_false=fail_if_false)
    # }

    # { Uplink Sets
    # - fc
    @classmethod
    def make_uplink_set_panel_into_viewpoint(cls, name):
        logger.debug("Get [ Uplink Set '%s' into view point ]" % name)
        FusionUIBase.scroll_element_into_viewpoint(cls.e.ID_BTN_FOLDING_UPLINK_SET % name)
        time.sleep(1)
        FusionUIBase.scroll_element_into_viewpoint(cls.e.ID_PANEL_INTERCONNECT_SETTINGS)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uplink_sets_item_exist(cls, name, timeout=5, fail_if_false=True):
        logger.debug("verify [ Uplink Set '%s' ] exist in Uplink Sets view" % name)
        return ui_lib.wait_for_element_visible(cls.e.ID_TEXT_UPLINK_SETS_ITEM % name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def expand_uplink_set_in_uplink_sets_view(cls, name, timeout=5, fail_if_false=True):
        logger.debug("click [ icon ] beside uplink set name to expand uplink set detail panel")
        ui_lib.wait_for_element_and_click(cls.e.ID_BTN_FOLDING_UPLINK_SET % name, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_visible(cls.e.ID_UPLINK_SET_PANEL % name, timeout, True)

    @classmethod
    def fold_uplink_set_in_uplink_sets_view(cls, name, timeout=5, fail_if_false=True):
        logger.debug("click [ icon ] beside uplink set name to fold uplink set detail panel")
        ui_lib.wait_for_element_and_click(cls.e.ID_BTN_FOLDING_UPLINK_SET % name, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_notvisible(cls.e.ID_UPLINK_SET_PANEL % name, timeout, True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_uplink_sets_panel_shown(cls, name, timeout=5, fail_if_false=True):
        logger.debug("wait [ Uplink Set '%s' panel ] shown in Uplink Sets view" % name)
        return ui_lib.wait_for_element_visible(cls.e.ID_UPLINK_SET_PANEL % name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uplink_set_fc_network_name(cls, uplink_set_name, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ FC network '%s' ] of [ Uplink set '%s' ] in Uplink Sets view" % (expect_value, uplink_set_name))
        return FusionUIBase.verify_element_text("FC network name", cls.e.ID_TEXT_UPLINK_SETS_FC_NETWORK_NAME % uplink_set_name, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uplink_set_fc_network_type(cls, uplink_set_name, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ FC network type '%s' ] of [ Uplink set '%s' ] in Uplink Sets view" % (expect_value, uplink_set_name))
        return FusionUIBase.verify_element_text("FC network type", cls.e.ID_TEXT_UPLINK_SETS_FC_NETWORK_TYPE % uplink_set_name, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uplink_set_fc_network_speed(cls, uplink_set_name, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ FC network speed '%s' ] of [ Uplink set '%s' ] in Uplink Sets view" % (expect_value, uplink_set_name))
        return FusionUIBase.verify_element_text("FC network speed", cls.e.ID_TEXT_UPLINK_SETS_FC_NETWORK_SPEED % uplink_set_name, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uplink_set_fc_port(cls, uplink_set_name, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ FC uplink port '%s' ] of [ Uplink set '%s' ] in Uplink Sets view" % (expect_value, uplink_set_name))
        return ui_lib.wait_for_element_visible(cls.e.ID_TEXT_UPLINK_SETS_FC_PORT % (uplink_set_name, expect_value), timeout=timeout, fail_if_false=fail_if_false)

    # - ethernet
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uplink_set_ethernet_network_connection_mode(cls, uplink_set_name, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Ethernet network connection mode '%s' ] of [ Uplink set '%s' ] in Uplink Sets view" % (expect_value, uplink_set_name))
        return FusionUIBase.verify_element_text("Ethernet network connection mode", cls.e.ID_TEXT_UPLINK_SETS_ETHERNET_CONNECTION_MODE % uplink_set_name, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uplink_set_ethernet_network_lacp_timer(cls, uplink_set_name, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Ethernet network LACP timer '%s' ] of [ Uplink set '%s' ] in Uplink Sets view" % (expect_value, uplink_set_name))
        return FusionUIBase.verify_element_text("Ethernet network LACP timer", cls.e.ID_TEXT_UPLINK_SETS_ETHERNET_LACP_TIMER % uplink_set_name, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uplink_set_ethernet_network_exist(cls, uplink_set_name, network_name, timeout=5, fail_if_false=True):
        logger.debug("verify [ Ethernet network '%s' ] of [ Uplink set '%s' ] in Uplink Sets view" % (network_name, uplink_set_name))
        return ui_lib.wait_for_element_visible(cls.e.ID_TEXT_UPLINK_SETS_ETHERNET_NETWORK_NAME % (uplink_set_name, network_name), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uplink_set_ethernet_network_vlan(cls, uplink_set_name, network_name, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Ethernet network vlan '%s' ] of [ network '%s' ] - [ Uplink set '%s' ] in Uplink Sets view" % (expect_value, network_name, uplink_set_name))
        return FusionUIBase.verify_element_text("Ethernet network vlan", cls.e.ID_TEXT_UPLINK_SETS_ETHERNET_NETWORK_VLAN_ID % (uplink_set_name, network_name), expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uplink_set_ethernet_network_type(cls, uplink_set_name, network_name, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Ethernet network type '%s' ] of [ network '%s' ] - [ Uplink set '%s' ] in Uplink Sets view" % (expect_value, network_name, uplink_set_name))
        return FusionUIBase.verify_element_text("Ethernet network type", cls.e.ID_TEXT_UPLINK_SETS_ETHERNET_NETWORK_TYPE % (uplink_set_name, network_name), expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uplink_set_ethernet_network_port_exist(cls, uplink_set_name, network_port, timeout=5, fail_if_false=True):
        logger.debug("verify [ Ethernet network port '%s' ] of [ Uplink set '%s' ] in Uplink Sets view" % (network_port, uplink_set_name))
        return ui_lib.wait_for_element_visible(cls.e.ID_TEXT_UPLINK_SETS_ETHERNET_NETWORK_PORT % (uplink_set_name, network_port), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uplink_ethernet_network_speed(cls, uplink_set_name, network_port, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ ETHERNET network speed '%s' ] of [ Uplink set '%s' ] in Uplink Sets view" % (expect_value, uplink_set_name))
        return FusionUIBase.verify_element_text("ETHERNET network speed", cls.e.ID_TEXT_UPLINK_SETS_ETHERNET_NETWORK_SPEED % (uplink_set_name, network_port), expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uplink_ethernet_network_auto_negotiation(cls, uplink_set_name, network_port, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ ETHERNET network auto negotiation '%s' ] of [ Uplink set '%s' ] in Uplink Sets view" % (expect_value, uplink_set_name))
        return FusionUIBase.verify_element_text("ETHERNET network auto negotiation", cls.e.ID_TEXT_UPLINK_SETS_ETHERNET_NETWORK_AUTO_NEGOTIATION % (uplink_set_name, network_port), expect_value, timeout=timeout, fail_if_false=fail_if_false)
    # }

    # { Interconnect Settings
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_interconnect_settings_fast_mac_cache_failover(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Fast MAC cache failover ] in interconnect settings view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Fast MAC cache failover", cls.e.ID_TEXT_INTERCONNECT_SETTINGS_FAST_MAC_CACHE_FAILOVER, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_interconnect_settings_mac_refresh_interval(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ MAC refresh interval ] in interconnect settings view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("MAC refresh interval", cls.e.ID_TEXT_INTERCONNECT_SETTINGS_MAC_REFRESH_INTERVAL, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_interconnect_settings_igmp_snooping(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ IGMP Snooping ] in interconnect settings view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("IGMP Snooping", cls.e.ID_TEXT_INTERCONNECT_SETTINGS_IGMP_SNOOPING, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_interconnect_settings_igmp_idle_timeout_interval(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ IGMP idle timeout interval ] in interconnect settings view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("IGMP idle timeout interval", cls.e.ID_TEXT_INTERCONNECT_SETTINGS_IGMP_IDLE_TIMEOUT_INTERVAL, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_interconnect_settings_loop_protection(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Loop protection ] in interconnect settings view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Loop protection", cls.e.ID_TEXT_INTERCONNECT_SETTINGS_LOOP_PROTECTION, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_interconnect_settings_pause_flood_protection(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Pause flood protection ] in interconnect settings view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Pause flood protection", cls.e.ID_TEXT_INTERCONNECT_SETTINGS_PAUSE_FLOOD_PROTECTION, expect_value, timeout=timeout, fail_if_false=fail_if_false)
    # }

    # { Utilization Sampling
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_utilization_sampling_interval_between_samples(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Interval between samples ] in utilization sampling view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Interval between samples", cls.e.ID_TEXT_UTILIZATION_SAMPLING_INTERVAL_BETWEEN_SAMPLES, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_utilization_sampling_total_number_of_samples(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Total number of samples ] in utilization sampling view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Total number of samples", cls.e.ID_TEXT_UTILIZATION_SAMPLING_TOTAL_NUMBER_OF_SAMPLES, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_utilization_sampling_sample_collection_rate(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Sample collection rate ] in utilization sampling view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Sample collection rate", cls.e.ID_TEXT_UTILIZATION_SAMPLING_SAMPLE_COLLECTION_RATE, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_utilization_sampling_total_sampling_history(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Total sampling history ] in utilization sampling view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Total sampling history", cls.e.ID_TEXT_UTILIZATION_SAMPLING_TOTAL_SAMPLING_HISTORY, expect_value, timeout=timeout, fail_if_false=fail_if_false)
    # }

    # { SNMP
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_enabled(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ SNMP enable ] in SNMP view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("SNMP enable", cls.e.ID_TEXT_SNMP_ENABLED, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv1v2_enabled(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ SNMP V1V2 enable ] in SNMP view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("SNMPV1V2 enable", cls.e.ID_TEXT_SNMPV1V2_ENABLED, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_enabled(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ SNMPV3 enable ] in SNMP view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("SNMPV3 enable", cls.e.ID_TEXT_SNMPV3_ENABLED, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_users_user_exist(cls, user, timeout=5, fail_if_false=True):
        logger.debug("verify [ SNMP USER '%s' ] exist in SNMP" % user)
        return ui_lib.wait_for_element_visible(cls.e.ID_TEXT_SNMP_USER % user, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_user_priv_protocol(cls, user, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [privacy protocol '%s' ] of [ snmpv3 user'%s' ] in SNMPv3 users view" % (expect_value, user))
        return FusionUIBase.verify_element_text("SNMPv3 users Privacy protocol", cls.e.ID_TEXT_SNMPV3_USERS_PRIVACY_PROTOCOL % user, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_user_auth_protocol(cls, user, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [authentication protocol '%s' ] of [ snmpv3 user'%s' ] in SNMPv3 users view" % (expect_value, user))
        return FusionUIBase.verify_element_text("SNMPv3 users Authentication protocol", cls.e.ID_TEXT_SNMPV3_USERS_AUTHENTICATION_PROTOCOL % user, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_user_security_level(cls, user, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [security level '%s' ] of [ snmpv3 user'%s' ] in SNMPv3 users view" % (expect_value, user))
        return FusionUIBase.verify_element_text("SNMPv3 users Security Level", cls.e.ID_TEXT_SNMPV3_USERS_SECURITY_LEVEL % user, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_system_contact(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ System contact ] in SNMP view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("System contact", cls.e.ID_TEXT_SNMP_SYSTEM_CONTACT, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_read_community(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Read community ] in SNMP view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Read community", cls.e.ID_TEXT_SNMP_READ_COMMUNITY, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_add_snmp_user_dialog_visible(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add SNMP user ] dialog appear")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_ADD_SNMP_USER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_invalid_authentication_password_error_message(cls, error, timeout=5, fail_if_false=True):
        logger.debug("verifying error message [%s] in authentication password field" % error)
        return FusionUIBase.verify_element_text("Authentication password", cls.e.ID_TEXT_ADD_SNMP_USER_INVALID_AUTH_PASSWORD_ERROR, error, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_invalid_privacy_password_error_message(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verifying error message  [%s] in  privacy password field" % expect_value)
        return FusionUIBase.verify_element_text("Privacy password", cls.e.ID_TEXT_ADD_SNMP_USER_INVALID_PRIV_PASSWORD_ERROR, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_invalid_username_error_message(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verifying if invalid username is passed")
        return FusionUIBase.verify_element_text("User name", cls.e.ID_TEXT_ADD_SNMP_INVALID_USER_USERNAME_ERROR, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_duplicate_username_error_message(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verifying if duplicate username is passed")
        return FusionUIBase.verify_element_text("User name", cls.e.ID_TEXT_ADD_SNMP_DUPLICATE_USER_USERNAME_ERROR, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_snmp_user_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ ADD SNMP USER ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_ADD_SNMP_USER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_add_max_snmp_user_error_message(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verifying error message  when more than permitted number of snmp users are added")
        return FusionUIBase.verify_element_text("User name", cls.e.ID_TEXT_ADD_SNMP_USER_OR_TRAP_ERROR, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_security_level_authentication_and_privacy_visibility(cls, timeout=5, fail_if_false=False):
        logger.debug("verify if[authentication and privacy] for security level is visible")
        return ui_lib.wait_for_element_visible(cls.e.ID_RADIO_SECURITY_LEVEL_AUTHENTICATION_AND_PRIVACY, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_snmp_user_confirm_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait for remove snmp_user dialog to show ")
        ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_REMOVE_SNMP_USER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_snmp_user_confirm_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait for remove snmp_user dialog to disappear ")
        ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_REMOVE_SNMP_USER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_snmp_user_table_disappear(cls, user, timeout=5, fail_if_false=True):
        logger.debug("wait SNMP snmp user table [ %s ] disappear" % user)
        return ui_lib.wait_for_element_notvisible(cls.e.ID_TEXT_SNMP_USER % user, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_remove_snmpv3_user_error(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("get [ error ] in remove snmpv3 user ")
        return FusionUIBase.verify_element_text(" Remove SNMPv3 User", cls.e.ID_TEXT_SNMP_USER_REMOVE_ERROR, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_trap_associated_user(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("get [ associated traps] in remove snmpv3 user ")
        return FusionUIBase.verify_element_text(" Used by Trap Destination", cls.e.ID_TEXT_SNMP_USER_ASSOCITED_TRAPS % expect_value, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_snmp_user_confirm_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait for edit snmp_user dialog to show ")
        ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_EDIT_SNMP_USER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_snmp_user_confirm_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait for edit snmp_user dialog to disappear ")
        ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_EDIT_SNMP_USER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_tbird_snmpv3_enabled(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify snnpv3 is enabled")
        return FusionUIBase.verify_element_text("SNMPv3", cls.e.ID_LABEL_SNMPV3_ENABLED, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    # }

    # { Trap Destinations
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_trap_format_visibility(cls, timeout=5, fail_if_false=False):
        logger.debug("verify if[Trap format] in Trap destination is visible")
        return ui_lib.wait_for_element_visible(cls.e.ID_RADIO_ADD_TRAP_DESTINATION_TRAP_FORMAT_SNMPV2, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_trap_destinations_destination_exist(cls, destination, timeout=5, fail_if_false=True):
        logger.debug("verify [ Trap Destination '%s' ] exist in SNMP Trap Destinations view" % destination)
        return ui_lib.wait_for_element_visible(cls.e.ID_TEXT_SNMP_TRAP_DESTINATIONS_ROW_DESTINATION % destination, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_trap_destinations_community_string(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Community String '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination community string", cls.e.ID_TEXT_SNMP_TRAP_DESTINATIONS_ROW_COMMUNITY_STRING % destination, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_trap_destinations_format(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Format '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination format", cls.e.ID_TEXT_SNMP_TRAP_DESTINATIONS_ROW_FORMAT % destination, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_max_trap_error_message(cls, expect_value, timeout=5, fail_if_false=False):
        logger.debug("verifying error message  when more than permitted number of snmpv3 traps are added")
        return FusionUIBase.verify_element_text("Trap Destination", cls.e.ID_TEXT_ADD_SNMP_USER_OR_TRAP_ERROR, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_no_snmp_user_error_msg(cls, expect_value, timeout=5, fail_if_false=False):
        logger.debug("Verifying Error message while adding trap wihtout snmp user")
        return FusionUIBase.verify_element_text("SNMP user", cls.e.ID_TEXT_ADD_TRAP_NO_USER_ERROR_MSG, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_invalid_port_error(cls, expect_value, timeout=5, fail_if_false=False):
        logger.debug("Verifying Error message for invalid port while adding trap")
        return FusionUIBase.verify_element_text("Port", cls.e.ID_TEXT_ADD_TRAP_ERROR_INVALID_PORT, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_invalid_engine_id_error(cls, expect_value, timeout=5, fail_if_false=False):
        logger.debug("Verifying Error message for invalid engine id while adding trap")
        return FusionUIBase.verify_element_text("Engine ID", cls.e.ID_TEXT_ADD_TRAP_ERROR_INVALID_ENGINEID, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_snmpv3_trap_destination_confirm_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait remove trap destination confirm dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_REMOVE_SNMPV3_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_snmpv3_trap_destination_confirm_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait remove trap destination confirm dialog disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_REMOVE_SNMPV3_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_trap_destinations_community_string(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Community String '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination community string", cls.e.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_ROW_COMMUNITY_STRING % destination, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_trap_destinations_format(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Format '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination format", cls.e.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_ROW_FORMAT % (destination, expect_value), expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_trap_destinations_severity(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Format '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination severity", cls.e.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_SEVERITY, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_trap_destinations_port(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ port '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination Port", cls.e.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_PORT % (destination, expect_value), expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_trap_destinations_username(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ UserName '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination UserName", cls.e.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_USERNAME, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_trap_destinations_engineid(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Engine ID '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination Engine ID", cls.e.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_ENGINEID, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_trap_destinations_notification_type(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Notification Type '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination Notification Type", cls.e.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_NOTIFICATION_TYPE, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_trap_destinations_vcm_traps(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ port '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination Port", cls.e.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_VCM_TRAPS, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_trap_destinations_enet_traps(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ port '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination ENET_Traps", cls.e.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_ENET_TRAPS, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_trap_destinations_fc_traps(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ port '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination FC_Traps", cls.e.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_FC_TRAPS, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_trap_destination_notification_visibility(cls, timeout=5, fail_if_false=True):
        logger.debug("Visible[ Notification Type ] in trap destination view")
        return ui_lib.is_visible(cls.e.ID_TOGGLE_TRAP_DESTINATION_NOTIFICATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def view_snmpv3_trap_destination_snmp_user_visibility(cls, timeout=5, fail_if_false=True):
        logger.debug("View Trap destination snmpv3 [ snmp users ]")
        ui_lib.is_visible(cls.e.ID_TEXT_SNMPV3_TRAP_DESTINATION_SNMP_USERS, timeout=timeout, fail_if_false=fail_if_false)

    # }

    # { SNMP Access
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_access_ip_or_subnet_exist(cls, ip_or_subnet, timeout=5, fail_if_false=True):
        logger.debug("verify [ ip or subnet '%s' ] exist in SNMP Access view" % ip_or_subnet)
        return ui_lib.wait_for_element_visible(cls.e.ID_TEXT_SNMP_SNMP_ACCESS_ROW_IP_OR_SUBNET % ip_or_subnet, timeout=timeout, fail_if_false=fail_if_false)
    # }

    # Quality of Service
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_quality_of_service_qos_configuration_type(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ QoS configuration type ] in SNMP view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("QoS configuration type", cls.e.ID_TEXT_QUALITY_OF_SERVICE_QOS_CONFIGURATION_TYPE, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_traffic_option(cls, traffic, timeout=5, fail_if_false=True):
        logger.debug("Verifying traffic value  [ %s ]" % traffic)
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectGroupsElements.ID_TEXT_TRAFFIC % traffic, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_mappings_visibility(cls, mappings, timeout=5, fail_if_false=True):
        logger.debug("verify the DOTIP and DSCO VALUES for selected Class")
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectGroupsElements.ID_TEXT_MAPPINGS % mappings, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_dot1poption(cls, dot1p_value, timeout=5, fail_if_false=True):
        logger.debug("Checking for the DoIPvalue %s " % dot1p_value)
        if ui_lib.wait_for_element_notvisible(EditLogicalInterconnectGroupsElements.ID_TABLE_DOTIP % dot1p_value, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("Successfully verified DoIPvalue %s is not present in selected QoS type" % dot1p_value)
            return True
        else:
            logger.warn("DOIP values %s is present for the selected QoS type " % dot1p_value)
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_passthrough_options(cls, timeout=5, fail_if_false=True):
        logger.debug("Check for the UPLINKOPTION is not existing ")
        if ui_lib.wait_for_element_notvisible(cls.e.ID_OPTION_UPLINK, timeout, fail_if_false):
            logger.debug("Check for the DOWNLINKOPTION is not existing ")
            if ui_lib.wait_for_element_notvisible(cls.e.ID_OPTION_DOWNLINK, timeout, fail_if_false):
                logger.debug("Check for the RESETOPTION is not existing ")
                if ui_lib.wait_for_element_notvisible(cls.e.ID_OPTION_RESET, timeout, fail_if_false):
                    logger.debug("verified  RESETOPTION is not existing ")
                    return True
                else:
                    logger.warn("UPLINKOPTION is existing")
                    return False
            else:
                logger.warn("DOWNLINKOPTION is existing")
                return False
        else:
            logger.warn("RESETOPTION is existing")
            return False


class VerifyLogicalInterconnectGroups(_BaseVerifyLogicalInterconnectGroups):
    pass


class C7000VerifyLogicalInterconnectGroups(_BaseVerifyLogicalInterconnectGroups):
    pass


class TBirdVerifyLogicalInterconnectGroups(_BaseVerifyLogicalInterconnectGroups):

    e = TBirdGeneralLogicalInterconnectGroupsElements

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_warning_message_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify no [ Warning Message ] shown when edit lig")
        return ui_lib.wait_for_element_visible(cls.e.ID_TEXT_WARNING_MESSAGE, timeout, fail_if_false)


class _BaseEditScopeForLogicalInterconnectGroups(object):

    """
       This class holds all edit scope operation of Logical Interconnect Groups
       It can work with C7000 & TBird
       """

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_edit_scope_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Click [ Edit ] button on logical interconnect groups scope page")
        if ui_lib.wait_for_element(EditScopeElements.ID_BUTTON_EDIT, timeout=timeout, fail_if_false=fail_if_false) \
                and ui_lib.wait_for_element_visible(EditScopeElements.ID_HEADER_SCOPE, timeout=timeout,
                                                    fail_if_false=fail_if_false) \
                and ui_lib.wait_for_element_notvisible(EditScopeElements.ID_TEXT_SCOPE_NOT_LOAD, timeout=timeout,
                                                       fail_if_false=fail_if_false):
            ui_lib.find_element_and_move(EditScopeElements.ID_HEADER_SCOPE)
            ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_EDIT, timeout=timeout,
                                              fail_if_false=fail_if_false)

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
    def click_ok_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ OK ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_OK, timeout, fail_if_false)

    @classmethod
    def click_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_CANCEL, timeout, fail_if_false)

    @classmethod
    def click_close_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Close ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_CLOSE, timeout, fail_if_false)

    @classmethod
    def click_assign_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Assign ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_ASSIGN, timeout, fail_if_false)

    @classmethod
    def click_add_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_ADD, timeout, fail_if_false)

    @classmethod
    def click_add_plus_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add+ ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_ADD_PLUS, timeout, fail_if_false)

    @classmethod
    def click_cancel_assign_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_CANCEL_ASSIGN, timeout, fail_if_false)

    @classmethod
    def input_scope_name(cls, name, wait_timeout=5, fail_if_false=True):
        logger.debug("input scope name '%s'" % name)
        ui_lib.wait_for_element_and_input_text(EditScopeElements.ID_INPUT_SEARCH_TEXT, name, wait_timeout,
                                               fail_if_false)

    @classmethod
    def click_scope_name(cls, name, wait_timeout=5, fail_if_false=True):
        logger.debug("click scope name '%s'" % name)
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_TABLE_SCOPE_NAME % name, wait_timeout,
                                          fail_if_false)

    @classmethod
    def click_remove_scope_icon(cls, name, wait_timeout=5, fail_if_false=True):
        logger.debug("click to remove scopes '%s'" % name)
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_TABLE_REMOVE_SCOPE % name, wait_timeout, fail_if_false)


class EditScopeForLogicalInterconnectGroups(_BaseEditScopeForLogicalInterconnectGroups):
    pass


class C7000EditScopeForLogicalInterconnectGroups(_BaseEditScopeForLogicalInterconnectGroups):
    pass


class TBirdEditScopeForLogicalInterconnectGroups(_BaseEditScopeForLogicalInterconnectGroups):
    pass

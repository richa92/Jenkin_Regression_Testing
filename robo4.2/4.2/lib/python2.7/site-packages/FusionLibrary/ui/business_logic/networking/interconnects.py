# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Interconnects Page
"""

from datetime import datetime
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.networking.interconnects_elements import *
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.base import FusionUIBase, TakeScreenShotWhenReturnFalseDeco
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements


class CommonOperationInterconnects(object):

    @classmethod
    def get_interconnect_list(cls, timeout=5):
        logger.debug("Get all [ Interconnect names ] from table")
        interconnect_name_list = []
        if ui_lib.wait_for_element(GeneralInterconnectsElements.ID_TABLE_INTERCONNECTS, timeout):
            interconnect_name_list = FusionUIBase.get_multi_elements_text(GeneralInterconnectsElements.ID_TABLE_INTERCONNECTS, timeout, fail_if_false=True)
        return interconnect_name_list

    @classmethod
    def click_interconnect(cls, interconnect, timeout=5):
        logger.debug("select [ INTERCONNECT '%s' ]" % interconnect)
        ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_TABLE_INTERCONNECT % interconnect, timeout=20, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_interconnect_selected(cls, interconnect, timeout=5, fail_if_false=True):
        logger.debug("wait [ INTERCONNECT '%s' ] selected" % interconnect)
        return ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_TEXT_INTERCONNECT_TITLE % interconnect, timeout, fail_if_false)

    @classmethod
    def click_uid_light(cls, timeout=5):
        logger.debug("click [ UID Light ] icon")
        ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_BUTTON_UID_LIGHT, timeout, fail_if_false=True)

    @classmethod
    def click_enclosure(cls, timeout=5):
        logger.debug("click [ Enclosure ] link")
        ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_TEXT_LOCATION, timeout, fail_if_false=True)

    @classmethod
    def click_logical_interconnect(cls, timeout=5):
        logger.debug("click [ Logical Interconnect  ] link")
        ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_TEXT_LOGICAL_INTERCONNECT, timeout, fail_if_false=True)

    @classmethod
    def click_logical_interconnect_action_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Logical Interconnect  ] Action Button")
        ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false)

    @classmethod
    def click_natasha_logical_interconnect_action_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Logical Interconnect  ] Action Button")
        ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_DFRM_DROPDOWN_ACTIONS, timeout, fail_if_false)

    @classmethod
    def click_port_button(cls, port_num, timeout=5, fail_if_false=True):
        logger.debug("click [ Interconnect  ] Port ExpansionCollapse Button")
        ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_UPLINK_PORT % port_num, timeout, fail_if_false)

    @classmethod
    def click_port_sub_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Interconnect  ] Port Expansion Collapse SubButton")
        FusionUIBase.scroll_element_into_viewpoint(GeneralInterconnectsElements.ID_UPLINK_CONNECTOR)
        ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_UPLINK_CONNECTOR, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_activity_action_ok(cls, interconnect, action_name, timeout=60, fail_if_false=True):
        logger.debug("waiting [ activity action of INTERCONNECT '%s' ] change to ok" % interconnect)
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element(GeneralInterconnectsElements.ID_TEXT_ACTIVITY_ACTION_OK % (interconnect, action_name), timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralInterconnectsElements.ID_TEXT_ACTIVITY_ACTION_TITLE % interconnect)
                logger.debug("[ activity action '%s' status ] is ok as expected." % actionname)
                return True
            elif ui_lib.wait_for_element(GeneralInterconnectsElements.ID_TEXT_ACTIVITY_ACTION_WARN % (interconnect, action_name), timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralInterconnectsElements.ID_TEXT_ACTIVITY_ACTION_TITLE % interconnect)
                logger.debug("[ activity action '%s' status ] is warn not as expected." % actionname)
                ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_TEXT_ACTIVITY_ACTION_WARN % (interconnect, action_name))
                msg = FusionUIBase.get_multi_elements_text(GeneralInterconnectsElements.ID_TEXT_ACTIVITY_MESSAGE)
                msg = [s for s in msg if msg != ''][0]
                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            elif ui_lib.wait_for_element(GeneralInterconnectsElements.ID_TEXT_ACTIVITY_ACTION_ERROR % (interconnect, action_name), timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralInterconnectsElements.ID_TEXT_ACTIVITY_ACTION_TITLE % interconnect)
                logger.debug("[ activity action '%s' status ] is error not as expected." % actionname)
                ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_TEXT_ACTIVITY_ACTION_ERROR % (interconnect, action_name))
                msg = FusionUIBase.get_multi_elements_text(GeneralInterconnectsElements.ID_TEXT_ACTIVITY_MESSAGE)
                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            else:
                if ui_lib.wait_for_element(GeneralInterconnectsElements.ID_TEXT_ACTIVITY_ACTION_TITLE % interconnect):
                    actionname = FusionUIBase.get_text(GeneralInterconnectsElements.ID_TEXT_ACTIVITY_ACTION_TITLE % interconnect)
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
    def get_overview_product_name(cls, timeout=5, fail_if_false=True):
        logger.debug("get [ interconnect  product name ] in overview")
        if ui_lib.wait_for_element(GeneralInterconnectsElements.ID_TEXT_PRODUCT_NAME, timeout, fail_if_false):
            product_name = FusionUIBase.get_text(GeneralInterconnectsElements.ID_TEXT_PRODUCT_NAME, timeout, fail_if_false)
            return product_name
        else:
            return None

    @classmethod
    def get_hardware_serial_number(cls, timeout=5, fail_if_false=True):
        logger.debug("get [ serial number ] in hardware view")
        return FusionUIBase.get_text(GeneralInterconnectsElements.ID_TEXT_HARDWARE_SERIAL_NUMBER, timeout, fail_if_false)

    @classmethod
    def get_hardware_part_number(cls, timeout=5, fail_if_false=True):
        logger.debug("get [ part number ] in hardware view ")
        return FusionUIBase.get_text(GeneralInterconnectsElements.ID_TEXT_HARDWARE_PART_NUMBER, timeout, fail_if_false)

    @classmethod
    def get_hardware_firmware_version(cls, timeout=5, fail_if_false=True):
        logger.debug("get [ic firmware version] in General view")
        return FusionUIBase.get_text(GeneralInterconnectsElements.ID_TEXT_GENERAL_INSTALLED_FIRMWARE_VERSION, timeout, fail_if_false)

    @classmethod
    def get_overview_power_state(cls, timeout=5, fail_if_false=True):
        logger.debug("get [ Interconnect power ]  state")
        if ui_lib.wait_for_element(GeneralInterconnectsElements.ID_TEXT_POWER, timeout, fail_if_false):
            powerstate = FusionUIBase.get_text(GeneralInterconnectsElements.ID_TEXT_POWER, timeout, fail_if_false)
            return powerstate
        else:
            return None

    @classmethod
    def get_overview_logical_interconnect(cls, timeout=5, fail_if_false=True):
        logger.debug("get [ Logical interconnect ] from overview")
        if ui_lib.wait_for_element(GeneralInterconnectsElements.ID_TEXT_LOGICAL_INTERCONNECT, timeout, fail_if_false):
            logical_ic = FusionUIBase.get_text(GeneralInterconnectsElements.ID_TEXT_LOGICAL_INTERCONNECT, timeout, fail_if_false)
            return logical_ic
        else:
            return None

    @classmethod
    def get_overview_ic_state(cls, timeout=5, fail_if_false=True):
        logger.debug("get [ State ] in Overview ")
        if ui_lib.wait_for_element(GeneralInterconnectsElements.ID_TEXT_STATE, timeout, fail_if_false):
            state = FusionUIBase.get_text(GeneralInterconnectsElements.ID_TEXT_STATE, timeout, fail_if_false)
            return state
        else:
            return None

    @classmethod
    def get_interconnect_status_in_interconnectlinktopology(cls, interconnect, timeout=5, fail_if_false=True):
        logger.debug("get [ interconnect %s status ] in interconnect link topology" % interconnect)
        interconnect_status = FusionUIBase.get_text(GeneralInterconnectsElements.ID_INTERCONNECT_STATUS, timeout, fail_if_false, True)
        return interconnect_status

    @classmethod
    def click_filter_all_states(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Activity Filter ] all states")
        return ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_FILTER_ALL_STATES, timeout, fail_if_false)

    @classmethod
    def click_filter_activity_state(cls, state, timeout=5, fail_if_false=True):
        logger.debug("click [ Filter Activity] based on the state")
        return ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_FILTER_BY_STATE % state, timeout, fail_if_false)

    @classmethod
    def click_alert_label_collapser(cls, count, timeout=5, fail_if_false=True):
        logger.debug("click [ Alert label] collaper")
        return ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_LABEL_PAGE_CLICK_ERROR % count, timeout, False)

    @classmethod
    def click_event_details_collapser(cls, count, timeout=5, fail_if_false=True):
        logger.debug("click [ event label] collaper")
        return ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_LABEL_EVENT_CLICK_ERROR % (count), timeout, False)

    @classmethod
    def get_error_count_in_invalid_interonnect_link_topology(cls, timeout=5, fail_if_false=True):
        logger.debug("get [ error count] on Activity for interconnect link topology ")
        error_count = FusionUIBase.get_text(GeneralInterconnectsElements.ID_LABEL_PAGE_ERROR_COUNT, timeout, fail_if_false, True)
        return error_count

    @classmethod
    def get_activity_text(cls, count, timeout=5, fail_if_false=True):
        logger.debug("get [ alert message] of activity for interconnect")
        activity_msg = FusionUIBase.get_text(GeneralInterconnectsElements.ID_LABEL_PAGE_ERROR % (count), timeout, fail_if_false)
        return activity_msg

    @classmethod
    def get_resolution_text(cls, count, timeout=5, fail_if_false=True):
        logger.debug("get [ resolution message] of activity for interconnect")
        resolution_msg = FusionUIBase.get_text(GeneralInterconnectsElements.ID_LABEL_PAGE_ERROR_FULL % (count), timeout, fail_if_false)
        return resolution_msg

    @classmethod
    def get_event_text(cls, count, timeout=5, fail_if_false=True):
        logger.debug("get [ event message] of activity for interconnect")
        event_msg = FusionUIBase.get_text(GeneralInterconnectsElements.ID_EVENT_MESSAGE % (count), timeout, fail_if_false)
        return event_msg

    @classmethod
    def refresh_current_page(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ refresh ] of browser of interconnect activity")
        ui_lib.refresh_browser(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, timeout)

    @classmethod
    def get_error_notification(cls, timeout=5, fail_if_false=True):
        logger.debug("get [error notification] text")
        ui_lib.wait_for_element_and_click(FusionInterconnectPage.ID_ACTIVITY_ERROR, timeout, fail_if_false)
        return ui_lib.get_text(FusionInterconnectPage.ID_ACTIVITY_ERROR_DETAILS, timeout, fail_if_false)

    @classmethod
    def get_stacking_domain_role(cls, timeout=5, fail_if_false=True):
        logger.debug("Get [Stacking domain role] text")
        if not ui_lib.wait_for_element_visible(FusionInterconnectPage.ID_IC_STACKING_DOMAIN_ROLE, timeout, fail_if_false):
            return False
        return ui_lib.get_text(FusionInterconnectPage.ID_IC_STACKING_DOMAIN_ROLE, timeout, fail_if_false)

    @classmethod
    def get_ic_ipv4_addr(cls, timeout=5, fail_if_false=True):
        logger.debug("get [ IC IPV4 Address ] in general")
        return FusionUIBase.get_text(GeneralInterconnectsElements.ID_TEXT_IC_IPV4_ADDR, timeout, fail_if_false)

    @classmethod
    def click_activity_filter_all_time(cls, timeout=5, fail_if_false=True):
        logger.debug("click Activity [ All time ] filter link")
        return ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_ACTIVITY_DATE_FILTER, timeout, fail_if_false)

    @classmethod
    def select_activity_filter_date(cls, msg, timeout=5, fail_if_false=True):
        logger.debug(" select [ date ] in All time filter link")
        return ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_ACTIVITY_DATE_SELECT % msg, timeout, fail_if_false)

    @classmethod
    def click_activity_resource_view(cls, timeout=5, fail_if_false=True):
        logger.debug(" click [resource view] in ICM Activity")
        return ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_ACTIVITY_VIEW, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_activity_message(cls, message, timeout=5, fail_if_false=True):
        logger.debug("click [ Activity  message ] in the resource view")
        return ui_lib.wait_for_element(GeneralInterconnectsElements.ID_ACTIVITY_MESSAGE % message, 30, fail_if_false)

    @classmethod
    def get_time_activity_message(cls, message, timeout=5, fail_if_false=True):
        selenium2lib = ui_lib.get_s2l()
        selenium2lib.mouse_over(GeneralInterconnectsElements.ID_SELECT_ACTIVITY_TIMEAGO % message)
        timeago = ui_lib.get_text(GeneralInterconnectsElements.ID_TEXT_ACTIVITY_TIMEAGO % message, 15, hidden_element=True)
        if not timeago:
            timeago = selenium2lib._current_browser().find_element_by_xpath(GeneralInterconnectsElements.ID_ACTIVITY_TIMEAGO % message).text
        return timeago

    @classmethod
    def get_interconnect_error_message(cls, timeout=5, fail_if_false=True):
        logger.debug("get [ error message ] for interconnect")
        return ui_lib.get_text(GeneralInterconnectsElements.ID_TEXT_NOTIFICATION_MESSAGE, timeout, fail_if_false)

    @classmethod
    def get_interconnect_uplink_port_speed(cls, port, timeout=5, fail_if_false=True):
        logger.debug("Uplink Port speed")
        ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_TEXT_PORT_SPEED % port, timeout, fail_if_false)
        return FusionUIBase.get_multi_elements_text(GeneralInterconnectsElements.ID_TEXT_PORT_SPEED % port, timeout, fail_if_false)

    @classmethod
    def get_fc_port_advanced_statistics(cls, port, timeout=5, fail_if_false=True):
        FusionUIBase.scroll_element_into_viewpoint(GeneralInterconnectsElements.ID_EXPAND_UPLINK_PORT % port, align_with_top=True)
        ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_EXPAND_UPLINK_PORT % port, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_EXPAND_ADVANCED_STATISTICS, timeout, fail_if_false)
        FusionUIBase.scroll_element_into_viewpoint(GeneralInterconnectsElements.ID_TEXT_ADVANCED_STATISTICS, align_with_top=True)
        ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_TEXT_ADVANCED_STATISTICS, timeout, fail_if_false)
        return FusionUIBase.get_multi_elements_text(GeneralInterconnectsElements.ID_TEXT_ADVANCED_STATISTICS, timeout, fail_if_false)


class InterconnectLinkPorts(object):

    @classmethod
    def get_overview_mouseover_port_information(cls, number, timeout=5, fail_if_false=True):
        logger.debug("get [ port ] in Overview for virtual connect")
        port = FusionUIBase.get_text(InterconnectLinkportsElements.ID_CXPPORT % (number), timeout, fail_if_false)
        return port

    @classmethod
    def get_overview_mouseover_port_status(cls, number, timeout=5, fail_if_false=True):
        logger.debug("get [ port status] in Overview for virtual connect")
        port_status = FusionUIBase.get_text(InterconnectLinkportsElements.ID_CXPPORT_STATUS % (number), timeout, fail_if_false, True)
        return port_status

    @classmethod
    def get_overview_mouseover_port_state(cls, number, timeout=5, fail_if_false=True):
        logger.debug("get [ port state] in Overview for virtual connect")
        selenium2lib = ui_lib.get_s2l()
        ui_lib.scroll_into_view(InterconnectLinkportsElements.ID_CXPPORT % (number), False)
        selenium2lib.mouse_over(InterconnectLinkportsElements.ID_CXPPORT % (number))
        state = FusionUIBase.get_text(InterconnectLinkportsElements.ID_CXPPORT_STATE % (number), timeout, fail_if_false)
        return state

    @classmethod
    def get_overview_mouseover_port_connectedto(cls, number, timeout=5, fail_if_false=True):
        logger.debug("get [ port connected to] in Overview for virtual connect")
        selenium2lib = ui_lib.get_s2l()
        ui_lib.scroll_into_view(InterconnectLinkportsElements.ID_CXPPORT % (number), False)
        ui_lib.find_element_and_move(InterconnectLinkportsElements.ID_CXPPORT % (number))
        selenium2lib.mouse_over(InterconnectLinkportsElements.ID_CXPPORT % (number))
        connected_to_information = FusionUIBase.get_text(InterconnectLinkportsElements.ID_CXPPORT_CONNECTED % (number), timeout, fail_if_false)
        return connected_to_information

    @classmethod
    def get_overview_mouseover_port_information_of_extender_interconnect(cls, number, timeout=5, fail_if_false=True):
        logger.debug("get [ extender port ] in Overview ")
        port = FusionUIBase.get_text(InterconnectLinkportsElements.ID_CXPPORT_OF_EXTENDER_IC % ((12 + number)), timeout, fail_if_false)
        return port

    @classmethod
    def get_overview_mouseover_port_status_of_extender_interconnect(cls, number, timeout=5, fail_if_false=True):
        logger.debug("get [ port status] in Overview ")
        port_status = FusionUIBase.get_text(InterconnectLinkportsElements.ID_CXPPORT_STATUS_OF_EXTENDER_IC % ((12 + number)), timeout, fail_if_false, True)
        return port_status

    @classmethod
    def get_overview_mouseover_port_state_of_extender_interconnect(cls, number, timeout=5, fail_if_false=True):
        logger.debug("get [ port state of extender interconnect] in Overview ")
        selenium2lib = ui_lib.get_s2l()
        ui_lib.scroll_into_view(InterconnectLinkportsElements.ID_CXPPORT_OF_EXTENDER_IC % ((12 + number)), False)
        ui_lib.find_element_and_move(InterconnectLinkportsElements.ID_CXPPORT_OF_EXTENDER_IC % ((12 + number)))
        state = FusionUIBase.get_text(InterconnectLinkportsElements.ID_CXPPORT_STATE_OF_EXTENDER_IC % ((12 + number)), timeout, fail_if_false)
        return state

    @classmethod
    def get_overview_mouseover_port_connectedto_of_extender_interconnect(cls, number, timeout=5, fail_if_false=True):
        logger.debug("get [ port connected to] in Overview ")
        selenium2lib = ui_lib.get_s2l()
        ui_lib.scroll_into_view(InterconnectLinkportsElements.ID_CXPPORT_OF_EXTENDER_IC % ((12 + number)), False)
        ui_lib.find_element_and_move(InterconnectLinkportsElements.ID_CXPPORT_OF_EXTENDER_IC % ((12 + number)))
        connected_to_information = FusionUIBase.get_text(InterconnectLinkportsElements.ID_CXPPORT_CONNECTED_OF_EXTENDER_IC % ((12 + number)), timeout, fail_if_false)
        return connected_to_information

    @classmethod
    def get_cxpport_status_from_interconnect_link_ports(cls, port, timeout=5, fail_if_false=True):
        logger.debug("get [ cxpport status] in interconnect link ports view ")
        port_status = FusionUIBase.get_text(InterconnectLinkportsElements.ID_CXPPORT_STS_IN_ILP_VIEW % (port), timeout, fail_if_false, True)
        return port_status

    @classmethod
    def get_port_information_from_interconnect_link_ports(cls, port, timeout=5, fail_if_false=True):
        logger.debug("get [ cxpport information] in interconnect link ports view ")
        cxpport_data = FusionUIBase.get_text(InterconnectLinkportsElements.ID_CXPPORT_INFORMATION % port, timeout, fail_if_false)
        return cxpport_data

    @classmethod
    def get_cxpport_connector_information_from_interconnect_link_ports(cls, port, timeout=5, fail_if_false=True):
        logger.debug("get [ cxpport connector information] in interconnect link ports view ")
        # Click on each port to capture the connector information
        ui_lib.wait_for_element_and_click(InterconnectLinkportsElements.ID_CLICKON_EXTENDERPORT_COLLAPSER % port, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(InterconnectLinkportsElements.ID_CLICKON_EXTENDERPORT_CONNECTOR, timeout, fail_if_false)
        get_connector_info = FusionUIBase.get_text(InterconnectLinkportsElements.ID_CXPPORT_CONNECTOR_INFORMATION, timeout, fail_if_false)
        logger.info(get_connector_info)
        ui_lib.wait_for_element_and_click(InterconnectLinkportsElements.ID_CLICKON_EXTENDERPORT_CONNECTOR, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(InterconnectLinkportsElements.ID_CLICKON_EXTENDERPORT_COLLAPSER % port, timeout, fail_if_false)
        return get_connector_info

    @classmethod
    def get_port_table_information(cls, timeout=5, fail_if_false=True):
        logger.debug("get [port table] information for interconnect link ports")
        port_table_information = FusionUIBase.get_text(InterconnectLinkportsElements.ID_EXTENDERPORT_TABLE, timeout)
        return port_table_information

    @classmethod
    def get_uplink_linked_port(cls, count, timeout=5, fail_if_false=True):
        return FusionUIBase.get_text(InterconnectLinkportsElements.ID_TEXT_UPLINK_LINKED_PORT % count, timeout, fail_if_false)

    @classmethod
    def click_uplink_linked_port_details(cls, uplinkLinkedPort, timeout=5, fail_if_false=True):
        return ui_lib.wait_for_element_and_click(InterconnectLinkportsElements.ID_CLICKON_EXTENDERPORT_UPLINK_LINKED_PORT % uplinkLinkedPort, timeout, fail_if_false)

    @classmethod
    def click_qos_statistics_uplink(cls, timeout=5, fail_if_false=True):
        return ui_lib.wait_for_element_and_click(InterconnectLinkportsElements.ID_CLICKON_EXTENDERPORT_QOS_UPLINK, timeout, fail_if_false)

    @classmethod
    def get_downlink_linked_port(cls, count, timeout=5, fail_if_false=True):
        return FusionUIBase.get_text(InterconnectLinkportsElements.ID_TEXT_DOWNLINK_LINKED_PORT % count, timeout, fail_if_false)

    @classmethod
    def click_downlink_linked_port_details(cls, downlinkLinkedPort, timeout=5, fail_if_false=True):
        return ui_lib.wait_for_element_and_click(InterconnectLinkportsElements.ID_CLICKON_EXTENDERPORT_DOWNLINK_LINKED_PORT % downlinkLinkedPort, timeout, fail_if_false)

    @classmethod
    def click_qos_statistics_downlink(cls, timeout=5, fail_if_false=True):
        return ui_lib.wait_for_element_and_click(InterconnectLinkportsElements.ID_CLICKON_EXTENDERPORT_QOS_DOWNLINK, timeout, fail_if_false)


class EditInterconnects(object):

    @classmethod
    def select_actions_edit(cls, timeout=5):
        logger.debug("select [ Edit ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_SELECT_ACTION_EDIT, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_interconnect_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Edit interconnect ] dialog shown")
        return ui_lib.wait_for_element_visible(EditInterconnectsElements.ID_DIALOG_EDIT_INTERCONNECT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_interconnect_dialog_disappear(cls, timeout=60, fail_if_false=True):
        logger.debug("wait [ Edit interconnect ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(EditInterconnectsElements.ID_DIALOG_EDIT_INTERCONNECT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_interconnect_uplink_ports_load(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Interconnect uplink port ] load")
        return ui_lib.wait_for_element_visible(EditInterconnectsElements.ID_CHECKBOX_UPLINK, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_interconnect_downlink_ports_load(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Interconnect downlink port ] load")
        return ui_lib.wait_for_element_visible(EditInterconnectsElements.ID_CHECKBOX_DOWNLINK, timeout, fail_if_false)

    # { dialog panel select
    @classmethod
    def select_interconnect_uplink_ports(cls, timeout=5):
        logger.debug("select [ Logical Interconnect Group ] section")
        ui_lib.wait_for_element_and_click(EditInterconnectsElements.ID_DROPDOWN_PANEL_SELECTOR, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditInterconnectsElements.ID_SELECT_UPLINK_PORT, timeout, fail_if_false=True)

    @classmethod
    def select_interconnect_downlink_ports(cls, timeout=5):
        logger.debug("select [ Interconnect Settings ] section")
        ui_lib.wait_for_element_and_click(EditInterconnectsElements.ID_DROPDOWN_PANEL_SELECTOR, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditInterconnectsElements.ID_SELECT_DOWNLINK_PORT, timeout, fail_if_false=True)

    @classmethod
    def tick_enable_uplink_ports(cls, port, timeout=5):
        logger.debug("select '%s' uplink port ..." % port)
        FusionUIBase.wait_for_checkbox_and_select(EditInterconnectsElements.ID_CHECKBOX_UPLINKPORTS % port, timeout, fail_if_false=True)

    @classmethod
    def untick_enable_uplink_ports(cls, port, timeout=5):
        logger.debug("un-select '%s' uplink port ..." % port)
        FusionUIBase.wait_for_checkbox_and_unselect(EditInterconnectsElements.ID_CHECKBOX_UPLINKPORTS % port, timeout, fail_if_false=True)

    @classmethod
    def tick_enable_downlink_ports(cls, port, timeout=5):
        logger.debug("select '%s' downlink Port ..." % port)
        FusionUIBase.wait_for_checkbox_and_select(EditInterconnectsElements.ID_CHECKBOX_DOWNLINKPORTS % port, timeout, fail_if_false=True)

    @classmethod
    def untick_enable_downlink_ports(cls, port, timeout=5):
        logger.debug("un-select '%s' downlink port ..." % port)
        FusionUIBase.wait_for_checkbox_and_unselect(EditInterconnectsElements.ID_CHECKBOX_DOWNLINKPORTS % port, timeout, fail_if_false=True)

    @classmethod
    def click_ok_button(cls, timeout=5):
        logger.debug("click [ OK ] button")
        if ui_lib.wait_for_element_visible(EditInterconnectsElements.ID_BUTTON_EDIT_OK, 20):
            return ui_lib.wait_for_element_and_click(EditInterconnectsElements.ID_BUTTON_EDIT_OK, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(EditInterconnectsElements.ID_BUTTON_EDIT_CANCEL, timeout, fail_if_false=True)


class ClearPortCounters(object):

    @classmethod
    def select_actions_clear_port_counters(cls, timeout=5):
        logger.debug("select [ Clear port counters ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_SELECT_ACTION_CLEAR_PORT, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_clear_port_counters_ok(cls, interconnect, timeout=60, fail_if_false=True):
        FusionUIBase.show_activity_sidebar()
        return CommonOperationInterconnects.wait_activity_action_ok(interconnect, "Clear port counters", timeout, fail_if_false)


class ResetLoopAndPauseFloodProtection(object):

    @classmethod
    def select_actions_reset_loop_and_pause_flood_protection(cls, timeout=5):
        logger.debug("select [ Reset loop and pause flood protection ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_SELECT_ACTION_RESET_LOOP, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_reset_loop_and_pause_flood_protection_ok(cls, interconnect, timeout=60, fail_if_false=True):
        FusionUIBase.show_activity_sidebar()
        return CommonOperationInterconnects.wait_activity_action_ok(interconnect, "Reset loop and pause flood protection", timeout, fail_if_false)


class ReapplyConfiguration(object):

    @classmethod
    def select_actions_reapply_configuration(cls, timeout=5):
        logger.debug("select [ Reapply Configuration ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_SELECT_ACTION_REAPPLY_CONFIG, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_reapply_configuration_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Reapply Configuration ] dialog shown")
        return ui_lib.wait_for_element_visible(ReapplyConfigurationElements.ID_DIALOG_EDIT_INTERCONNECT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_reapply_configuration_dialog_disappear(cls, timeout=15, fail_if_false=True):
        logger.debug("wait [ Reapply Configuration ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(ReapplyConfigurationElements.ID_DIALOG_EDIT_INTERCONNECT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_reapply_configuration_ok(cls, interconnect, timeout=60, fail_if_false=True):
        FusionUIBase.show_activity_sidebar()
        return CommonOperationInterconnects.wait_activity_action_ok(interconnect, "Reapply configuration", timeout, fail_if_false)

    @classmethod
    def click_yes_reapply_button(cls, timeout=5):
        logger.debug("click [ Yes, reapply ] button")
        ui_lib.wait_for_element_and_click(ReapplyConfigurationElements.ID_BUTTON_YES_REAPPLY, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(ReapplyConfigurationElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)


class PowerOnInterconnects(object):

    @classmethod
    def select_actions_power_on(cls, timeout=5):
        logger.debug("select [ Power on ] item in [ Action ] menu")
        if ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_DROPDOWN_ACTIONS + "-dfrm", timeout, fail_if_false=False) is False:
            ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        if ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_SELECT_ACTION_POWER_ON + "-dfrm", timeout, fail_if_false=False) is False:
            ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_SELECT_ACTION_POWER_ON, timeout, fail_if_false=False)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_power_on_ok(cls, interconnect, timeout=500, fail_if_false=False):
        FusionUIBase.show_activity_sidebar()
        return CommonOperationInterconnects.wait_activity_action_ok(interconnect, "Power on", timeout, fail_if_false)


class PowerOffInterconnects(object):

    @classmethod
    def select_actions_power_off(cls, timeout=5):
        logger.debug("select [ Power off ] item in [ Action ] menu")
        if ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_DROPDOWN_ACTIONS + "-dfrm", timeout, fail_if_false=False) is False:
            ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        if ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_SELECT_ACTION_POWER_OFF + "-dfrm", timeout, fail_if_false=False) is False:
            ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_SELECT_ACTION_POWER_OFF, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_power_off_ok(cls, interconnect, timeout=500, fail_if_false=False):
        FusionUIBase.show_activity_sidebar()
        return CommonOperationInterconnects.wait_activity_action_ok(interconnect, "Power off", timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_power_off_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Edit interconnect ] dialog shown")
        return ui_lib.wait_for_element_visible(PowerOffInterconnectsElements.ID_DIALOG_POWER_OFF, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_power_off_dialog_disappear(cls, timeout=15, fail_if_false=True):
        logger.debug("wait [ Edit interconnect ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(PowerOffInterconnectsElements.ID_DIALOG_POWER_OFF, timeout, fail_if_false)

    @classmethod
    def click_yes_power_off_button(cls, timeout=5):
        logger.debug("click [ Yes, power off ] button")
        ui_lib.wait_for_element_and_click(PowerOffInterconnectsElements.ID_BUTTON_POWER_OFF_OK, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(PowerOffInterconnectsElements.ID_BUTTON_POWER_OFF_CANCEL, timeout, fail_if_false=True)


class ResetInterconnects(object):

    @classmethod
    def select_actions_reset(cls, timeout=5):
        logger.debug("select [ Reset ] item in [ Action ] menu")
        if ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_DROPDOWN_ACTIONS + "-dfrm", timeout, fail_if_false=False) is False:
            ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        if ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_SELECT_ACTION_RESET + "-dfrm", timeout, fail_if_false=False) is False:
            ui_lib.wait_for_element_and_click(GeneralInterconnectsElements.ID_SELECT_ACTION_RESET, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_reset_ok(cls, interconnect, timeout=20, fail_if_false=True):
        FusionUIBase.show_activity_sidebar()
        return CommonOperationInterconnects.wait_activity_action_ok(interconnect, "Reset", timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_soft_reset_ok(cls, interconnect, timeout=500, fail_if_false=True):
        FusionUIBase.show_activity_sidebar()
        return CommonOperationInterconnects.wait_activity_action_ok(interconnect, "Reset", timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_hard_reset_ok(cls, interconnect, timeout=500, fail_if_false=True):
        FusionUIBase.show_activity_sidebar()
        return CommonOperationInterconnects.wait_activity_action_ok(interconnect, "Reset", timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_reset_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Reset ] dialog shown")
        return ui_lib.wait_for_element_visible(ResetInterconnectsElements.ID_DIALOG_RESET, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_reset_dialog_disappear(cls, timeout=15, fail_if_false=True):
        logger.debug("wait [ Reset ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(ResetInterconnectsElements.ID_DIALOG_RESET, timeout, fail_if_false)

    @classmethod
    def click_soft_reset_button(cls, timeout=5):
        logger.debug("click [ Soft Reset ] button")
        ui_lib.wait_for_element_and_click(ResetInterconnectsElements.ID_BUTTON_SOFT_RESET, timeout, fail_if_false=True)

    @classmethod
    def click_hard_reset_button(cls, timeout=5):
        logger.debug("click [ Hard Reset ] button")
        ui_lib.wait_for_element_and_click(ResetInterconnectsElements.ID_BUTTON_HARD_RESET, timeout, fail_if_false=True)


class VerifyInterconnects(object):

    # { General verification

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_interconnect_not_exist(cls, interconnect, timeout=5, fail_if_false=True):
        logger.debug("verify [ INTERCONNECT '%s' ] is not existing" % interconnect)
        if ui_lib.wait_for_element_notvisible(GeneralInterconnectsElements.ID_TABLE_INTERCONNECT % interconnect, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_interconnect_uplinkport_label_not_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify FEX interconnect does not allow us to edit uplink port")
        return ui_lib.wait_for_element_notvisible(GeneralInterconnectsElements.ID_LABEL_UPLINK_PORT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_interconnect_exist(cls, interconnect, timeout=5, fail_if_false=True):
        logger.debug("verify [ INTERCONNECT '%s' ] is existing" % interconnect)
        if ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_TABLE_INTERCONNECT % interconnect, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_notification_shown(cls, timeout=10, fail_if_false=False):
        logger.debug("verify [ Notification ] display")
        return ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_PANEL_NOTIFICATION, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_status_ok(cls, timeout=10, fail_if_false=False):
        logger.debug("verify [ status ] is ok")
        return ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_STATUS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uid_light_on(cls, timeout=60, fail_if_false=True):
        logger.debug("verify [ UID Light ] in on state")
        return ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_STATUS_UID_LIGHT_ON, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uid_light_off(cls, timeout=60, fail_if_false=True):
        logger.debug("verify [ UID Light ] in off state")
        return ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_STATUS_UID_LIGHT_OFF, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_power(cls, expect_value, timeout=10, fail_if_false=True):
        logger.debug("verify [ Interconnect power ] in overview")
        FusionUIBase.verify_element_text("Interconnect power", GeneralInterconnectsElements.ID_TEXT_POWER, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_power_on(cls, timeout=10, fail_if_false=True):
        logger.debug("verify [ Interconnect power ] in on state")
        return ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_TEXT_POWER_ON, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_power_off(cls, timeout=10, fail_if_false=True):
        logger.debug("verify [ Interconnect power ] in off state")
        return ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_TEXT_POWER_OFF, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_logical_interconnect(cls, expect_value, timeout=10, fail_if_false=True):
        logger.debug("verify [ Logical interconnect ] in OverView view, expected value is [ %s ]" % expect_value)
        FusionUIBase.verify_element_text("Logical interconnect", GeneralInterconnectsElements.ID_TEXT_LOGICAL_INTERCONNECT, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_state(cls, expect_value, timeout=10, fail_if_false=True):
        logger.debug("verify [ State ] in OverView view, expected value is [ %s ]" % expect_value)
        FusionUIBase.verify_element_text("State", GeneralInterconnectsElements.ID_TEXT_STATE, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_firmware_baseline(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Firmware baseline ] in OverView view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Firmware baseline", GeneralInterconnectsElements.ID_TEXT_FIRMWARE_BASELINE, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_installed_firmware_version(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Installed firmware version ] in OverView view, expected value is [ %s ]" % expect_value)
        FusionUIBase.verify_element_text("Installed firmware version", GeneralInterconnectsElements.ID_TEXT_INSTALLED_FIRMWARE_VERSION, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_management_interface(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Management interface ] in OverView view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Management interface", GeneralInterconnectsElements.ID_TEXT_MANAGEMENT_INTERFACE, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_product_name(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Product name ] in OverView view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Product name", GeneralInterconnectsElements.ID_TEXT_PRODUCT_NAME, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_location(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Location ] in OverView view, expected value is [ %s ]" % expect_value)
        FusionUIBase.verify_element_text("Location", GeneralInterconnectsElements.ID_TEXT_HARDWARE_LOCATION, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_serial_number(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Serial number ] in OverView view, expected value is [ %s ]" % expect_value)
        FusionUIBase.verify_element_text("Serial number", GeneralInterconnectsElements.ID_TEXT_SERIAL_NUMBER, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_part_number(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Part number ] in OverView view, expected value is [ %s ]" % expect_value)
        FusionUIBase.verify_element_text("Part number", GeneralInterconnectsElements.ID_TEXT_PART_NUMBER, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_actions_power_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ Power On Off ] item in [ Action ] menu")
        return ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_SELECT_ACTION_POWER_OFF, timeout, fail_if_false) or ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_SELECT_ACTION_POWER_ON, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_actions_power_off_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ Power Off ] item in [ Action ] menu")
        return ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_SELECT_ACTION_POWER_OFF, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_actions_reset_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ Power Off ] item in [ Action ] menu")
        return ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_SELECT_ACTION_RESET, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_actions_edit(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ Edit ] item in [ Action ] menu")
        return ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_SELECT_ACTION_EDIT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_actions_noauthorization(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ No Authorization ] item in [ Action ] menu")
        return ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_TEXT_ACTION_NO_AUTHORIZATION, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_power(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Interconnect power ] in general view")
        FusionUIBase.verify_element_text("Interconnect power", GeneralInterconnectsElements.ID_TEXT_POWER, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_power_on(cls, timeout=5, fail_if_false=True):
        logger.debug("verify [ Interconnect power ] in on state")
        return ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_TEXT_GENERAL_POWER_ON, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_power_off(cls, timeout=5, fail_if_false=True):
        logger.debug("verify [ Interconnect power ] in off state")
        return ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_TEXT_GENERAL_POWER_OFF, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_logical_interconnect(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Logical interconnect ] in General view, expected value is [ %s ]" % expect_value)
        FusionUIBase.verify_element_text("Logical interconnect", GeneralInterconnectsElements.ID_TEXT_GENERAL_LOGICAL_INTERCONNECT, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_state(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ State ] in General view, expected value is [ %s ]" % expect_value)
        FusionUIBase.verify_element_text("State", GeneralInterconnectsElements.ID_TEXT_GENERAL_STATE, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_firmware_baseline(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Firmware baseline ] in General view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Firmware baseline", GeneralInterconnectsElements.ID_TEXT_GENERAL_FIRMWARE_BASELINE, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_firmware_version_from_baseline(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Firmware version from baseline ] in General view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Firmware version from baseline", GeneralInterconnectsElements.ID_TEXT_GENERAL_FIRMWARE_VERSION_FROM_BASELINE, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_installed_firmware_version(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Installed firmware version ] in General view, expected value is [ %s ]" % expect_value)
        FusionUIBase.verify_element_text("Installed firmware version", GeneralInterconnectsElements.ID_TEXT_GENERAL_INSTALLED_FIRMWARE_VERSION, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_management_interface(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Management interface ] in OverView view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Management interface", GeneralInterconnectsElements.ID_TEXT_GENERAL_MANAGEMENT_INTERFACE, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_domain_id(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Domain ID ] in OverView view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Domain ID", GeneralInterconnectsElements.ID_TEXT_GENERAL_DOMAIN_ID, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_member_id(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Member ID ] in OverView view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Member ID", GeneralInterconnectsElements.ID_TEXT_GENERAL_MEMBER_ID, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_domain_role(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Domain role ] in OverView view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Domain role", GeneralInterconnectsElements.ID_TEXT_GENERAL_DOMAIN_ROLE, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_interconnect_host_name(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Interconnect host name ] in OverView view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Interconnect host name", GeneralInterconnectsElements.ID_TEXT_GENERAL_INTERCONNECT_HOST_NAME, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_ipv4(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ IPv4 ] in General view, expected value is [ %s ]" % expect_value)
        FusionUIBase.verify_element_text("IPv4", GeneralInterconnectsElements.ID_TEXT_GENERAL_IPV4, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_ipv6(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ IPv6 ] in General view, expected value is [ %s ]" % expect_value)
        FusionUIBase.verify_element_text("IPv6", GeneralInterconnectsElements.ID_TEXT_GENERAL_IPV6, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_product_name(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Product name ] in Hardware view, expected value is [ %s ]" % expect_value)
        FusionUIBase.verify_element_text("Product name", GeneralInterconnectsElements.ID_TEXT_HARDWARE_PRODUCT_NAME, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_location(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Location ] in Hardware view, expected value is [ %s ]" % expect_value)
        FusionUIBase.verify_element_text("Location", GeneralInterconnectsElements.ID_TEXT_HARDWARE_LOCATION, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_management_mac_address(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Management MAC address ] in Hardware view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Management MAC address", GeneralInterconnectsElements.ID_TEXT_HARDWARE_MANAGEMENT_MAC, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_base_wwn(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Base WWN ] in Hardware view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Base WWN", GeneralInterconnectsElements.ID_TEXT_HARDWARE_BASE_WWN, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_serial_number(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Serial number ] in Hardware view, expected value is [ %s ]" % expect_value)
        FusionUIBase.verify_element_text("Serial number", GeneralInterconnectsElements.ID_TEXT_HARDWARE_SERIAL_NUMBER, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_part_number(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Part number ] in Hardware view, expected value is [ %s ]" % expect_value)
        FusionUIBase.verify_element_text("Part number", GeneralInterconnectsElements.ID_TEXT_HARDWARE_PART_NUMBER, expect_value, timeout, fail_if_false)
    # }

    # { Uplink Ports
    #
    @classmethod
    def make_uplink_port_panel_into_viewpoint(cls):
        logger.debug("Get [ Uplink panel into view point ]")
        FusionUIBase.scroll_element_into_viewpoint(GeneralInterconnectsElements.ID_PANEL_UPLINK_PORTS)

    @classmethod
    def make_downlink_port_panel_into_viewpoint(cls):
        logger.debug("Get [ Downlink panel into view point ]")
        FusionUIBase.scroll_element_into_viewpoint(GeneralInterconnectsElements.ID_PANEL_DOWNLINK_PORTS)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_port_in_uplink_port(cls, expect_value, number, timeout=5, fail_if_false=True):
        logger.debug("verify [Port] exist in Uplink Ports view, expected value is [ %s ]" % expect_value)
        item_name = "Uplink Port"
        locator = GeneralInterconnectsElements.ID_TEXT_UPLINK_PORTS_PORT % number
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name, locator, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_type_in_uplink_port(cls, expect_value, number, timeout=5, fail_if_false=True):
        logger.debug("verify [Type] exist in Uplink Ports view, expected value is [ %s ]" % expect_value)
        item_name = "Uplink Type"
        locator = GeneralInterconnectsElements.ID_TEXT_UPLINK_PORTS_TYPE % number
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name, locator, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_status_in_uplink_port(cls, expect_value, number, timeout=5, fail_if_false=True):
        logger.debug("verify [Status] exist in Uplink Ports view, expected value is [ %s ]" % expect_value)
        item_name = "Uplink Status"
        locator = GeneralInterconnectsElements.ID_TEXT_UPLINK_PORTS_STATUS % number
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name, locator, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_status_in_uplink_port_reason_code(cls, expect_value, number, timeout=5, fail_if_false=True):
        logger.debug("Verify [Reason Code] exist in Uplink Ports view, expected value is [ %s ]" % expect_value)
        item_name = "Uplink Status Reason Code"
        locator = GeneralInterconnectsElements.ID_TEXT_UPLINK_PORTS_STATUS_REASON_CODE % number
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name, locator, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_speed_in_uplink_port(cls, expect_value, number, timeout=5, fail_if_false=True):
        logger.debug("verify [Speed] exist in Uplink Ports view, expected value is [ %s ]" % expect_value)
        item_name = "Uplink Speed"
        locator = GeneralInterconnectsElements.ID_TEXT_UPLINK_PORTS_SPEED % number
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name, locator, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uplink_set_in_uplink_port(cls, expect_value, number, timeout=5, fail_if_false=True):
        logger.debug("verify [uplink set] exist in Uplink Ports view, expected value is [ %s ]" % expect_value)
        item_name = "Uplink Set"
        locator = GeneralInterconnectsElements.ID_TEXT_UPLINK_PORTS_UPLINK_SET % number
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name, locator, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connect_to_in_uplink_port(cls, expect_value, number, timeout=5, fail_if_false=True):
        logger.debug("verify [connected to] exist in Uplink Ports view, expected value is [ %s ]" % expect_value)
        item_name = "Connected To"
        locator = GeneralInterconnectsElements.ID_TEXT_UPLINK_PORTS_CONNECTED_TO % number
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name, locator, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uplink_sets_in_uplink_port(cls, set, port, timeout=5, fail_if_false=True):
        logger.debug("verify [ Uplink Set '%s' ] exist in Uplink Ports view" % set)
        return ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_TEXT_UPLINK_PORTS % [set, port], timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_hardware_in_downlink_port(cls, hardware, port, timeout=5, fail_if_false=True):
        logger.debug("verify [ Server Hardware '%s' ] exist in Uplink Ports view" % hardware)
        return ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_TEXT_DOWNLINK_PORTS % [hardware, port], timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_port_in_downlink_port(cls, expect_value, number, timeout=5, fail_if_false=True):
        logger.debug("verify [Port] exist in Uplink Ports view, expected value is [ %s ]" % expect_value)
        item_name = "Downlink Port"
        locator = GeneralInterconnectsElements.ID_TEXT_DOWNLINK_PORTS_PORT % number
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name, locator, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_status_in_downlink_port(cls, expect_value, number, timeout=5, fail_if_false=True):
        logger.debug("verify [Status] exist in Downlink Ports view, expected value is [ %s ]" % expect_value)
        item_name = "Downlink Status"
        locator = GeneralInterconnectsElements.ID_TEXT_DOWNLINK_PORTS_STATUS % number
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name, locator, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_serverhardware_in_downlink_port(cls, expect_value, number, timeout=5, fail_if_false=True):
        logger.debug("verify [ServerHardware] exist in Uplink Ports view, expected value is [ %s ]" % expect_value)
        item_name = "Server Hardware"
        locator = GeneralInterconnectsElements.ID_TEXT_DOWNLINK_PORTS_HARDWARE % number
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name, locator, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_AdapterPorts_in_downlink_port(cls, expect_value, number, timeout=5, fail_if_false=True):
        logger.debug("verify [ServerHardware] exist in Uplink Ports view, expected value is [ %s ]" % expect_value)
        item_name = "Adapter Port"
        locator = GeneralInterconnectsElements.ID_TEXT_DOWNLINK_PORTS_ADAPTERPORT % number
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name, locator, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_ServerProfile_in_downlink_port(cls, expect_value, number, timeout=5, fail_if_false=True):
        logger.debug("verify [ServerHardware] exist in Uplink Ports view, expected value is [ %s ]" % expect_value)
        item_name = "ServerProfile"
        locator = GeneralInterconnectsElements.ID_TEXT_DOWNLINK_PORTS_SERVERPROFILE % number
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name, locator, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_hardwar_and_profile_in_downlink_port(cls, hardware, port, profile, timeout=5, fail_if_false=True):
        logger.debug("verify [ Server Hardware '%s' ] exist in Uplink Ports view" % hardware)
        return ui_lib.wait_for_element_visible(GeneralInterconnectsElements.ID_TEXT_DOWNLINK_PORTS_PROFILE % [hardware, port, profile], timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_interconnect_link_ports_label(cls, timeout=5, fail_if_false=True):
        logger.debug("verify [ Label ] of Interconnect link ports")
        return ui_lib.wait_for_element_visible(InterconnectLinkportsElements.ID_INTERCONNECTLINKPORTS_LABEL, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_scope_should_exist_in_edit_page(cls, name, timeout=5, fail_if_false=True):
        logger.debug("verify [ scope '%s' ] exist in scope edit page" % name)
        return ui_lib.wait_for_element_visible(EditScopeElements.ID_TABLE_SCOPE_NAME % name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_qos_statistics_uplink(cls, qosStatistics, timeout=5, fail_if_false=True):
        logger.debug("verify  Uplink  qos statistics")
        return ui_lib.wait_for_element_visible(InterconnectLinkportsElements.ID_TEXT_QUALITY_OF_SERVICE_STATISTICS_INFO % qosStatistics, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_qos_statistics_downlink(cls, qosStatistics, timeout=5, fail_if_false=True):
        logger.debug("vverify  downlink  qos statistics")
        return ui_lib.wait_for_element_visible(InterconnectLinkportsElements.ID_TEXT_QUALITY_OF_SERVICE_STATISTICS_INFO_DOWNLINK % qosStatistics, timeout, fail_if_false)


class _BaseEditScopeForInterconnect(object):

    """
    This Class holds all edit scope operation of interconnects
    It can work with C7000 & TBird
    """

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_edit_scope_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Click [ Edit ] button on Interconnect scope page")
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
        logger.debug("click Scope name '%s'" % name)
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_TABLE_SCOPE_NAME % name, wait_timeout, fail_if_false=True)

    @classmethod
    def click_remove_scope_icon(cls, name, wait_timeout=5):
        logger.debug("click to remove scopes '%s'" % name)
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_TABLE_REMOVE_SCOPE % name, wait_timeout, fail_if_false=True)


class EditScopeForInterconnect(_BaseEditScopeForInterconnect):
    pass


class C7000EditScopeForInterconnect(_BaseEditScopeForInterconnect):
    pass


class TBirdEditScopeForInterconnect(_BaseEditScopeForInterconnect):
    pass

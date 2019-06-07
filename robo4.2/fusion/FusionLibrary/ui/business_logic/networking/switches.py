import re
import time
from datetime import datetime
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.base import FusionUIBase, TakeScreenShotWhenReturnFalseDeco
from FusionLibrary.ui.business_logic.networking.switches_elements import (GeneralSwitchesElements)


class CommonOperationSwitches(object):

    @classmethod
    def get_switch_list(cls, timeout=5, fail_if_false=True):
        logger.debug("Get all [ SWITCH names ] from table")
        if ui_lib.wait_for_element(GeneralSwitchesElements.ID_TABLE_SWITCHES, timeout):
            return FusionUIBase.get_multi_elements_text(GeneralSwitchesElements.ID_TABLE_SWITCHES, timeout, fail_if_false)

    @classmethod
    def click_general_view(cls, timeout=5):
        logger.debug("Go to GENERAL view")
        ui_lib.wait_for_element_visible(GeneralSwitchesElements.ID_SWITCH_PROGRESS_BAR, 60)
        ui_lib.wait_for_element_visible(GeneralSwitchesElements.ID_SWITCH_CONFIGURE_STATE, 180)
        if not ui_lib.wait_for_element_visible(GeneralSwitchesElements.SWITCH_ID_GENERAL_SECTION):
            ui_lib.wait_for_element_and_click(GeneralSwitchesElements.SWITCH_ID_LINK_OVERVIEW)
            ui_lib.wait_for_element_and_click(GeneralSwitchesElements.SWITCH_ID_LINK_GENERAL)
            ui_lib.wait_for_element_visible(GeneralSwitchesElements.SWITCH_ID_GENERAL_SECTION)
        return True

    @classmethod
    def click_ports_in_dropdown(cls, timeout=5):
        logger.debug("view PORTS")
        if not ui_lib.wait_for_element_visible(GeneralSwitchesElements.SWITCH_ID_PORTS_SECTION):
            ui_lib.wait_for_element_and_click(GeneralSwitchesElements.SWITCH_ID_LINK_OVERVIEW)
            ui_lib.wait_for_element_and_click(GeneralSwitchesElements.SWITCH_ID_LINK_PORTS)
        return ui_lib.wait_for_element_visible(GeneralSwitchesElements.SWITCH_ID_PORTS_SECTION)

    @classmethod
    def get_switch_state_and_model(cls, timeout=5):
        logger.debug("Get all [ SWITCH names ] from table")
        switch_state = ui_lib.get_text(GeneralSwitchesElements.ID_SWITCH_CURRENT_STATE)
        model_no = ui_lib.get_text(GeneralSwitchesElements.ID_SWITCH_MODEL_NUMBER)
        return switch_state, model_no

    @classmethod
    def click_switch(cls, switch, timeout=5, fail_if_false=True):
        logger.debug("select [ SWITCH '%s' ]" % switch)
        ui_lib.wait_for_element_and_click(GeneralSwitchesElements.ID_TABLE_SWITCH % switch, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_table_row_data(cls, index, timeout=5):
        return ui_lib.get_text(GeneralSwitchesElements.ID_SWITCH_TABLE_ROW_COUNT % index)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_port_data(cls, index, timeout=5):
        logger.debug("Get switch port table")
        return ui_lib.get_text(GeneralSwitchesElements.ID_SWITCH_PORT_CHANNEL % index)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_port_vlan_data(cls, index, timeout=5):
        logger.debug("Get Vlan Network data")
        j = index + 1
        ui_lib.wait_for_element_and_click(GeneralSwitchesElements.ID_SWITCH_EXPAND_TABLE_ROW % index, 90)
        if not ui_lib.wait_for_element_and_click(GeneralSwitchesElements.ID_SWITCH_PORT_TABLE_VLAN_LABEL % j, 120):
            ui_lib.fail_test("Vlan ID Lable is not visible")
        vlan_data = ui_lib.get_text(GeneralSwitchesElements.ID_SWITCH_PORT_TABLE_VLAN_DATA % j, 180)
        if not vlan_data:
            vlan_data = ui_lib.get_text(GeneralSwitchesElements.ID_SWITCH_PORT_TABLE_VLAN_DATA % j, 240)
        if not ui_lib.wait_for_element_and_click(GeneralSwitchesElements.ID_SWITCH_PORT_TABLE_VLAN_LABEL % j, 180):
            logger.debug("retrying to collapse the expanded port...")
            ui_lib.wait_for_element_visible(GeneralSwitchesElements.ID_SWITCH_PORT_TABLE_VLAN_LABEL % j, 90)
            ui_lib.wait_for_element_and_click(GeneralSwitchesElements.ID_SWITCH_PORT_TABLE_VLAN_LABEL % j, 150)
        ui_lib.wait_for_element_and_click(GeneralSwitchesElements.ID_SWITCH_EXPAND_TABLE_ROW % index, 90)
        return vlan_data

    @classmethod
    def edit_switch_port(cls, port, timeout=5):
        logger.debug("Enable or Disable switch port ")
        ui_lib.wait_for_element_and_click(GeneralSwitchesElements.ID_SWITCH_ACTION_BTN)
        ui_lib.wait_for_element_and_click(GeneralSwitchesElements.ID_SWITCH_EDIT_BTN)
        if not ui_lib.wait_for_element_visible(GeneralSwitchesElements.ID_SWITCH_EDIT_LABEL, 10):
            return None
        if not ui_lib.wait_for_element_and_click(GeneralSwitchesElements.ID_SWITCH_CHECKBOX % port, 10):
            return ui_lib.get_text(GeneralSwitchesElements.ID_SWITCH_TABLE_ROW_COUNT)
        return True

    @classmethod
    def get_port_status(cls, port, timeout=5):
        logger.debug("Get switch port status")
        ui_lib.wait_for_element_and_click(GeneralSwitchesElements.ID_SWITCH_ACTION_BTN)
        ui_lib.wait_for_element_and_click(GeneralSwitchesElements.ID_SWITCH_EDIT_BTN)
        if not ui_lib.wait_for_element_visible(GeneralSwitchesElements.ID_SWITCH_EDIT_LABEL):
            return None
        status = ui_lib.get_text(GeneralSwitchesElements.ID_SWITCH_PORTSTATUS % port)
        ui_lib.wait_for_element_and_click(GeneralSwitchesElements.ID_SWITCH_OK_BTN)
        return status

    @classmethod
    def click_ok_edit(cls, timeout=5):
        ui_lib.wait_for_element_and_click(GeneralSwitchesElements.ID_SWITCH_OK_BTN, 10)
        logger.debug("Waiting for update to complete...")
        ui_lib.wait_for_element_visible(GeneralSwitchesElements.ID_SWITCH_PROGRESS_BAR, 60)
        ui_lib.wait_for_element_visible(GeneralSwitchesElements.ID_SWITCH_CONFIGURE_STATE, 180)
        logger.debug("checking for configure switches is started...")
        ui_lib.wait_for_element_visible(GeneralSwitchesElements.ID_SWITCH_PROGRESS_BAR, 120)
        ui_lib.wait_for_element_visible(GeneralSwitchesElements.ID_SWITCH_CONFIGURE_STATE, 200)
        return True


class VerifyOperationSwitches(object):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_port_channel_generated(cls, timeout=5):
        logger.debug("Verify [PORT CHANNEL] column got generated")
        return ui_lib.wait_for_element_visible(GeneralSwitchesElements.ID_PORT_CHANNEL, 10)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_vpc_number_generated(cls, timeout=5):
        logger.debug("Verify [vPC NUMBER] column got generated")
        return ui_lib.wait_for_element_visible(GeneralSwitchesElements.ID_VPC_NUMBER, 10)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_switch_notexist(cls, switch, timeout=5):
        logger.debug("Verify [SWITCH %s] is not exist" % switch)
        return ui_lib.wait_for_element_notvisible(GeneralSwitchesElements.ID_TABLE_SWITCH % switch, 10)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_switch_selected(cls, switch, timeout=5, fail_if_false=True):
        logger.debug("wait [ SWITCH '%s' ] selected" % switch)
        return ui_lib.wait_for_element_visible(GeneralSwitchesElements.ID_TEXT_SWITCH_TITLE % switch, 5, False)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_edit_exist(cls, timeout=5):
        logger.debug("Verifying edit option is visible")
        ui_lib.wait_for_element_and_click(GeneralSwitchesElements.ID_SWITCH_ACTION_BTN)
        return ui_lib.wait_for_element_visible(GeneralSwitchesElements.ID_SWITCH_EDIT_BTN)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_edit_notexist(cls, timeout=5):
        logger.debug("Verify Switch doesn't have Action button when LS in Monitor state")
        ui_lib.wait_for_element_and_click(GeneralSwitchesElements.ID_SWITCH_ACTION_BTN)
        return ui_lib.wait_for_element_notvisible(GeneralSwitchesElements.ID_SWITCH_EDIT_BTN)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_refresh_exist(cls, timeout=5):
        logger.debug("Verify REFRESH is exist in SWITCHES")
        ui_lib.wait_for_element_and_click(GeneralSwitchesElements.ID_SWITCH_ACTION_BTN)
        return ui_lib.wait_for_element_visible(GeneralSwitchesElements.ID_SWITCH_REFRESH_BTN)

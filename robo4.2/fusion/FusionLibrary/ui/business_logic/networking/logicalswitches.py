from datetime import datetime
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco, FusionUIBase
from FusionLibrary.ui.business_logic.networking.logicalswitches_elements import (
    GeneralLogicalSwitchesElements,
    CreateLogicalSwitchesElements,
    EditLogicalSwitchesElements,
    DeleteLogicalSwitchesElements,
)
from RoboGalaxyLibrary import BuiltIn
from HTMLParser import HTMLParser


class _BaseCommonOperationLogicalSwitches(object):

    e = GeneralLogicalSwitchesElements
    html = HTMLParser()

    @classmethod
    def get_logical_switch_list(cls, timeout=5, fail_if_false=True):
        logger.debug("Get all Logical Switch name(s) from table")
        ls_list = []
        if ui_lib.wait_for_element(cls.e.ID_TABLE_LOGICAL_SWITCH_LIST):
            ls_list = FusionUIBase.get_multi_elements_text(cls.e.ID_TABLE_LOGICAL_SWITCH_LIST, timeout=timeout, fail_if_false=fail_if_false)
        return ls_list

    @classmethod
    def click_logical_switch(cls, ls_name, timeout=5, time_for_loading=3, fail_if_false=True):
        logger.debug("select Logical Switch '%s'" % ls_name)
        ui_lib.wait_for_element_and_click(cls.e.ID_TABLE_LOGICAL_SWITCH % ls_name, timeout=timeout, fail_if_false=fail_if_false)
        BuiltIn().sleep(time_for_loading)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_logical_switch_selected(cls, ls_name, timeout=5, fail_if_false=True):
        logger.debug("wait for Logical Switch '%s' to be selected" % ls_name)
        if ui_lib.wait_for_element_visible(cls.e.ID_TABLE_LOGICAL_SWITCH_SELECTED % ls_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("Logical Switch '%s' is successfully selected" % ls_name)
            return True
        else:
            msg = "failed to wait for Logical Switch '%s' to be selected" % ls_name
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def select_logical_switch(cls, ls_name, timeout=5, fail_if_false=True):
        cls.click_logical_switch(ls_name=ls_name, timeout=timeout, fail_if_false=fail_if_false)
        return cls.wait_logical_switch_selected(ls_name=ls_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_logical_switch_status_not_found(cls, ls_name, timeout=5, fail_if_false=True):
        logger.info("wait for Logical Switch status to change to 'not found'")
        if ui_lib.wait_for_element_visible(cls.e.ID_TABLE_LOGICAL_SWITCH_NOT_FOUND % ls_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("Logical Switch '%s' status successfully changed to 'not found'" % ls_name)
            return True
        else:
            msg = "failed to wait for Logical Switch '%s' status to change to 'not found'" % ls_name
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def click_actions_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click 'Actions' button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ACTIONS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_logical_switch_status_ok(cls, ls_name, timeout=10, fail_if_false=True):
        start = datetime.now()
        logger.debug("wait for Logical Switch '%s' status to change to OK" % ls_name)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(cls.html.unescape(cls.e.ID_STATUS_LOGICAL_SWITCH_OK % ls_name), timeout=2, fail_if_false=False):
                logger.debug("Logical Switch '%s' status is OK as expected." % ls_name)
                return True
            elif ui_lib.wait_for_element_visible(cls.html.unescape(cls.e.ID_STATUS_LOGICAL_SWITCH_WARN % ls_name), timeout=2, fail_if_false=False):
                err_msg = "Logical Switch '%s' status is WARN not as expected." % ls_name
                return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)
            elif ui_lib.wait_for_element_visible(cls.html.unescape(cls.e.ID_STATUS_LOGICAL_SWITCH_ERROR % ls_name), timeout=2, fail_if_false=False):
                err_msg = "Logical Switch '%s' status is ERROR not as expected." % ls_name
                return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)
            else:
                logger.debug("Logical Switch status is UNKNOWN, waiting ...")
                continue
        err_msg = "Timeout waiting for Logical Switch '%s' status to change to OK." % ls_name
        return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_logical_switch_group_status_ok_or_warn(cls, ls_name, timeout=10, fail_if_false=True):
        start = datetime.now()
        logger.debug("wait for Logical Switch '%s' status to change to OK or WARN" % ls_name)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(cls.html.unescape(cls.e.ID_STATUS_LOGICAL_SWITCH_OK % ls_name), timeout=5, fail_if_false=False):
                logger.debug("Logical Switch '%s' status is OK as expected." % ls_name)
                return True
            elif ui_lib.wait_for_element_visible(cls.html.unescape(cls.e.ID_STATUS_LOGICAL_SWITCH_WARN % ls_name), timeout=5, fail_if_false=False):
                logger.debug("Logical Switch '%s' status is WARN as expected." % ls_name)
                return True
            elif ui_lib.wait_for_element_visible(cls.html.unescape(cls.e.ID_STATUS_LOGICAL_SWITCH_ERROR % ls_name), timeout=5, fail_if_false=False):
                err_msg = "Logical Switch '%s' status is ERROR not as expected." % ls_name
                return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)
            else:
                logger.debug("Logical Switch '%s' status is UNKNOWN, waiting ..." % ls_name)
                continue
        err_msg = "Timeout waiting for Logical Switch '%s' status to change to OK or WARN." % ls_name
        return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_logical_switch_group_status_error(cls, ls_name, timeout=10, fail_if_false=True):
        start = datetime.now()
        logger.debug("wait for Logical Switch '%s' status to change to ERROR" % ls_name)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(cls.html.unescape(cls.e.ID_STATUS_LOGICAL_SWITCH_OK % ls_name), timeout=5, fail_if_false=False):
                err_msg = "Logical Switch '%s' status is OK not as expected." % ls_name
                return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)
            elif ui_lib.wait_for_element_visible(cls.html.unescape(cls.e.ID_STATUS_LOGICAL_SWITCH_WARN % ls_name), timeout=5, fail_if_false=False):
                logger.debug("Logical Switch '%s' status is WARN not as expected." % ls_name)
                return False
            elif ui_lib.wait_for_element_visible(cls.html.unescape(cls.e.ID_STATUS_LOGICAL_SWITCH_ERROR % ls_name), timeout=5, fail_if_false=False):
                logger.debug("Logical Switch '%s' status is ERROR as expected." % ls_name)
                return True
            else:
                logger.debug("Logical Switch '%s' status is UNKNOWN, waiting ..." % ls_name)
                continue
        err_msg = "Timeout waiting for Logical Switch status to change to ERROR."
        return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)

    @classmethod
    def get_warning_msg(cls, timeout=5, fail_if_false=True):
        logger.debug("Get warning message in Logical Switches")
        return ui_lib.get_text(GeneralLogicalSwitchesElements.ID_WARNING_MSG, timeout, fail_if_false)

    @classmethod
    def click_overview_dropdown(cls, timeout=5, fail_if_false=True):
        logger.debug("select [OVER VIEW] dropdown")
        return ui_lib.wait_for_element_and_click(GeneralLogicalSwitchesElements.ID_OVERVIEW_DROPDOWN, timeout, fail_if_false)

    @classmethod
    def click_logical_switch_ils(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ILS] in dropdown list")
        return ui_lib.wait_for_element_and_click(GeneralLogicalSwitchesElements.ID_ILS_OPTION, timeout, fail_if_false)

    @classmethod
    def get_ils_data(cls, timeout=5, fail_if_false=True):
        logger.debug("Get [ILS] data")
        return ui_lib.get_text(GeneralLogicalSwitchesElements.ID_ILS_DATA, timeout, fail_if_false)


class CommonOperationLogicalSwitches(_BaseCommonOperationLogicalSwitches):
    pass


class C7000CommonOperationLogicalSwitches(_BaseCommonOperationLogicalSwitches):
    pass


class TBirdCommonOperationLogicalSwitches(_BaseCommonOperationLogicalSwitches):
    pass


class _BaseCreateLogicalSwitches(object):

    e = CreateLogicalSwitchesElements

    @classmethod
    def click_create_logical_switch_button(cls, timeout=5):
        logger.debug("click 'Create logical switch' button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_LOGICAL_SWITCH, timeout=timeout, fail_if_false=True)

    @classmethod
    def select_actions_create(cls, timeout=5, fail_if_false=True):
        logger.debug("select 'Actions -> Create' button")
        ui_lib.wait_for_element_and_click(GeneralLogicalSwitchesElements.ID_BUTTON_ACTIONS, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_ACTIONS_CREATE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_logical_switch_dialog_open(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Create Logical Switch' to open ...")
        if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_CREATE_LOGICAL_SWITCH, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Create Logical Switch' successfully opened")
            return True
        else:
            msg = "failed waiting for dialog 'Create Logical Switch' to open within %s seconds" % timeout
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def input_name(cls, name, timeout=5, fail_if_false=True):
        logger.debug("input 'Name' as '%s'" % name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NAME, name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_add_logical_switch_as_monitored(cls, timeout=5, fail_if_false=True):
        logger.debug("tick 'Add logical switch as' type as 'Monitored'")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_ADD_LOGICAL_SWITCH_AS_MONITORED, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_add_logical_switch_as_managed(cls, timeout=5, fail_if_false=True):
        logger.debug("tick 'Add logical switch as' type as 'Managed'")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_ADD_LOGICAL_SWITCH_AS_MANAGED, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def input_select_logical_switch_group(cls, lsg_name, timeout=5, fail_if_false=True):
        logger.debug("input and select 'Logical switch group' as '%s'" % lsg_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_LOGICAL_SWITCH_GROUP, lsg_name, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_LOGICAL_SWITCH_GROUP % lsg_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch1_ip_address_or_host_name(cls, ip_or_host_name, timeout=5, fail_if_false=True):
        logger.debug("input 'IP address or host name' of 'Switch 1' as '%s'" % ip_or_host_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH1_IP_ADDRESS_OR_HOST_NAME, ip_or_host_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch1_user_name(cls, user_name, timeout=5, fail_if_false=True):
        logger.debug("input 'User name' of 'Switch 1' as '%s'" % user_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH1_USER_NAME, user_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch1_password(cls, password, timeout=5, fail_if_false=True):
        logger.debug("input 'Password' of 'Switch 1' as '%s'" % password)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH1_PASSWORD, password, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch1_snmp_port(cls, port, timeout=5, fail_if_false=True):
        logger.debug("input 'SNMP port' of 'Switch 1' as '%s'" % port)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH1_SNMP_PORT, port, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_switch1_snmp_version(cls, version, timeout=5, fail_if_false=True):
        logger.debug("select 'SNMP version' of 'Switch 1' as '%s'" % version)
        FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_SWITCH1_SNMP_VERSION, version, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch1_snmp_user_name(cls, snmp_user_name, timeout=5, fail_if_false=True):
        logger.debug("input 'SNMP User name' of 'Switch 1' as '%s'" % snmp_user_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH1_SNMP_USER_NAME, snmp_user_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_switch1_security_level_as_authorization(cls, timeout=5, fail_if_false=True):
        logger.debug("tick 'Security Level' as 'Authorization' for 'Switch 1'")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SWITCH1_AUTHORIZATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_switch1_security_level_as_authorization_and_privacy(cls, timeout=5, fail_if_false=True):
        logger.debug("tick 'Security Level' as 'Authorization and privacy' for 'Switch 1")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SWITCH1_AUTHORIZATION_AND_PRIVACY, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_switch1_authorization_protocol(cls, protocol, timeout=5, fail_if_false=True):
        logger.debug("select 'Authorization protocol' of 'Switch 1' as '%s'" % protocol)
        FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_SWITCH1_AUTHORIZATION_PROTOCOL, protocol, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch1_snmp_authorization_password(cls, snmp_user_name, timeout=5, fail_if_false=True):
        logger.debug("input 'SNMP Authorization password' of 'Switch 1' as '%s'" % snmp_user_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH1_AUTHORIZATION_PASSWORD, snmp_user_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch1_community_string(cls, community_string, timeout=5, fail_if_false=True):
        logger.debug("input 'Community string' of 'Switch 1' as '%s'" % community_string)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH1_COMMUNITY_STRING, community_string, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch1_snmp_user_name(cls, snmp_user_name, timeout=5, fail_if_false=True):
        logger.debug("input 'SNMP User name' of 'Switch 1' as '%s'" % snmp_user_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH1_SNMP_USER_NAME, snmp_user_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_switch1_security_level_as_authorization(cls, timeout=5, fail_if_false=True):
        logger.debug("tick 'Security Level' as 'Authorization' for 'Switch 1'")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SWITCH1_AUTHORIZATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_switch1_security_level_as_authorization_and_privacy(cls, timeout=5, fail_if_false=True):
        logger.debug("tick 'Security Level' as 'Authorization and privacy' for 'Switch 1")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SWITCH1_AUTHORIZATION_AND_PRIVACY, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_switch1_authorization_protocol(cls, protocol, timeout=5, fail_if_false=True):
        logger.debug("select 'Authorization protocol' of 'Switch 1' as '%s'" % protocol)
        FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_SWITCH1_AUTHORIZATION_PROTOCOL, protocol, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch1_snmp_authorization_password(cls, snmp_user_name, timeout=5, fail_if_false=True):
        logger.debug("input 'SNMP Authorization password' of 'Switch 1' as '%s'" % snmp_user_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH1_AUTHORIZATION_PASSWORD, snmp_user_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch2_ip_address_or_host_name(cls, ip_or_host_name, timeout=5, fail_if_false=True):
        logger.debug("input 'IP address or host name' of 'Switch 2' as '%s'" % ip_or_host_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH2_IP_ADDRESS_OR_HOST_NAME, ip_or_host_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_switch2_use_same_credentials_as_switch1(cls, timeout=5, fail_if_false=True):
        logger.debug("turn on Switch2's 'Use same credentials as Switch 1' option ...")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_SWITCH2_USE_SAME_CREDENTIALS_AS_SWITCH1, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def untick_switch2_use_same_credentials_as_switch1(cls, timeout=5, fail_if_false=True):
        logger.debug("turn off Switch2's 'Use same credentials as Switch 1' option ...")
        FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_SWITCH2_USE_SAME_CREDENTIALS_AS_SWITCH1, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch2_user_name(cls, user_name, timeout=5, fail_if_false=True):
        logger.debug("input 'User name' of 'Switch 2' as '%s'" % user_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH2_USER_NAME, user_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch2_password(cls, password, timeout=5, fail_if_false=True):
        logger.debug("input 'Password' of 'Switch 2' as '%s'" % password)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH2_PASSWORD, password, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch2_snmp_port(cls, port, timeout=5, fail_if_false=True):
        logger.debug("input 'SNMP port' of 'Switch 2' as '%s'" % port)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH2_SNMP_PORT, port, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_switch2_snmp_version(cls, version, timeout=5, fail_if_false=True):
        logger.debug("select 'SNMP version' of 'Switch 2' as '%s'" % version)
        FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_SWITCH2_SNMP_VERSION, version, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch2_snmp_user_name(cls, snmp_user_name, timeout=5, fail_if_false=True):
        logger.debug("input 'SNMP User name' of 'Switch 2' as '%s'" % snmp_user_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH2_SNMP_USER_NAME, snmp_user_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_switch2_security_level_as_authorization(cls, timeout=5, fail_if_false=True):
        logger.debug("tick 'Security Level' as 'Authorization' for 'Switch 2'")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SWITCH2_AUTHORIZATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_switch2_security_level_as_authorization_and_privacy(cls, timeout=5, fail_if_false=True):
        logger.debug("tick 'Security Level' as 'Authorization and privacy' for 'Switch 2")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SWITCH2_AUTHORIZATION_AND_PRIVACY, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_switch2_authorization_protocol(cls, protocol, timeout=5, fail_if_false=True):
        logger.debug("select 'Authorization protocol' of 'Switch 2' as '%s'" % protocol)
        FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_SWITCH2_AUTHORIZATION_PROTOCOL, protocol, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch2_snmp_authorization_password(cls, snmp_user_name, timeout=5, fail_if_false=True):
        logger.debug("input 'SNMP Authorization password' of 'Switch 2' as '%s'" % snmp_user_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH2_AUTHORIZATION_PASSWORD, snmp_user_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch2_community_string(cls, community_string, timeout=5, fail_if_false=True):
        logger.debug("input 'Community string' of 'Switch 2' as '%s'" % community_string)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH2_COMMUNITY_STRING, community_string, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch2_snmp_user_name(cls, snmp_user_name, timeout=5, fail_if_false=True):
        logger.debug("input 'SNMP User name' of 'Switch 2' as '%s'" % snmp_user_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH2_SNMP_USER_NAME, snmp_user_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_switch2_security_level_as_authorization(cls, timeout=5, fail_if_false=True):
        logger.debug("tick 'Security Level' as 'Authorization' for 'Switch 2'")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SWITCH2_AUTHORIZATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_switch2_security_level_as_authorization_and_privacy(cls, timeout=5, fail_if_false=True):
        logger.debug("tick 'Security Level' as 'Authorization and privacy' for 'Switch 2")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SWITCH2_AUTHORIZATION_AND_PRIVACY, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_switch2_authorization_protocol(cls, protocol, timeout=5, fail_if_false=True):
        logger.debug("select 'Authorization protocol' of 'Switch 2' as '%s'" % protocol)
        FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_SWITCH2_AUTHORIZATION_PROTOCOL, protocol, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch2_snmp_authorization_password(cls, snmp_user_name, timeout=5, fail_if_false=True):
        logger.debug("input 'SNMP Authorization password' of 'Switch 2' as '%s'" % snmp_user_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH2_AUTHORIZATION_PASSWORD, snmp_user_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_logical_switch_dialog_close(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Create Logical Switch' to close ...")
        if ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_CREATE_LOGICAL_SWITCH, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Create Logical Switch' successfully closed")
            return True
        else:
            msg = "failed waiting for dialog 'Create Logical Switch' to close"
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


class CreateLogicalSwitches(_BaseCreateLogicalSwitches):
    pass


class C7000CreateLogicalSwitches(_BaseCreateLogicalSwitches):
    pass


class TBirdCreateLogicalSwitches(_BaseCreateLogicalSwitches):
    pass


class _BaseEditLogicalSwitches(object):

    e = EditLogicalSwitchesElements

    @classmethod
    def click_edit_button(cls, timeout=5):
        logger.debug("click 'Edit' button from Actions menu")
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_ACTIONS_EDIT, timeout=timeout, fail_if_false=True)

    @classmethod
    def select_actions_edit(cls, timeout=5):
        logger.debug("click 'Actions -> Edit' button ")
        CommonOperationLogicalSwitches.click_actions_button(timeout=timeout)
        cls.click_edit_button(timeout=timeout)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_logical_switch_dialog_open(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Edit Logical Switch' to open ...")
        if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_EDIT_LOGICAL_SWITCH, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Edit Logical Switch' successfully opened")
            return True
        else:
            msg = "failed to wait for dialog 'Edit Logical Switch' to open within %s seconds" % timeout
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def input_name(cls, name, timeout=5, fail_if_false=True):
        logger.debug("input 'Name' as '%s'" % name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NAME, name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_add_logical_switch_as_monitored(cls, timeout=5, fail_if_false=True):
        logger.debug("tick 'Add logical switch as' type as 'Monitored'")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_ADD_LOGICAL_SWITCH_AS_MONITORED, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_add_logical_switch_as_managed(cls, timeout=5, fail_if_false=True):
        logger.debug("tick 'Add logical switch as' type as 'Managed'")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_ADD_LOGICAL_SWITCH_AS_MANAGED, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_existing_switch_list(cls, timeout=5, fail_if_false=True):
        logger.debug("get all existing Switch name(s) from editing Logical Switch dialog")
        switch_list = []
        if ui_lib.wait_for_element(cls.e.ID_TABLE_EXISTING_SWITCH_LIST):
            switch_list = FusionUIBase.get_multi_elements_text(cls.e.ID_TABLE_EXISTING_SWITCH_LIST, timeout=timeout, fail_if_false=fail_if_false)
        return switch_list

    @classmethod
    def click_remove_switch_icon(cls, switch_ip_or_host_name, timeout=5, fail_if_false=True):
        logger.debug("click the REMOVE icon to remove the switch '%s'" % switch_ip_or_host_name)
        ui_lib.wait_for_element_and_click(cls.e.ID_ICON_REMOVE_SWITCH % switch_ip_or_host_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_switch_icon(cls, switch_ip_or_host_name, timeout=5, fail_if_false=True):
        logger.debug("click the EDIT icon to edit the switch '%s'" % switch_ip_or_host_name)
        ui_lib.wait_for_element_and_click(cls.e.ID_ICON_EDIT_SWITCH % switch_ip_or_host_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_switch_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click 'Add switch' button to add switch")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_SWITCH, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_or_add_switch_dialog_open(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Edit Switch Credentials' to open ...")
        if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_EDIT_OR_ADD_SWITCH, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Edit Switch Credentials' successfully opened")
            return True
        else:
            msg = "failed to wait for dialog 'Edit Switch Credentials' to open within %s seconds" % timeout
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def input_switch_ip_address_or_host_name(cls, ip_or_host_name, timeout=5, fail_if_false=True):
        logger.debug("input 'IP address or host name' of 'Switch' as '%s'" % ip_or_host_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH_IP_ADDRESS_OR_HOST_NAME, ip_or_host_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_use_same_credentials(cls, timeout=5, fail_if_false=True):
        logger.debug("turn on 'Use same credentials as ...' option ...")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_USE_SAME_CREDENTIALS_AS_ANOTHER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def untick_use_same_credentials(cls, timeout=5, fail_if_false=True):
        logger.debug("turn off 'Use same credentials as ...' option ...")
        FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_USE_SAME_CREDENTIALS_AS_ANOTHER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch_user_name(cls, user_name, timeout=5, fail_if_false=True):
        logger.debug("input 'User name' of 'Switch' as '%s'" % user_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH_USER_NAME, user_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch_password(cls, password, timeout=5, fail_if_false=True):
        logger.debug("input 'Password' of 'Switch' as '%s'" % password)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH_PASSWORD, password, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch_snmp_port(cls, port, timeout=5, fail_if_false=True):
        logger.debug("input 'SNMP port' of 'Switch' as '%s'" % port)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH_SNMP_PORT, port, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_switch_snmp_version(cls, version, timeout=5, fail_if_false=True):
        logger.debug("select 'SNMP version' of 'Switch' as '%s'" % version)
        FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_SWITCH_SNMP_VERSION, version, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch_snmp_user_name(cls, snmp_user_name, timeout=5, fail_if_false=True):
        logger.debug("input 'SNMP User name' as '%s'" % snmp_user_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH_SNMP_USER_NAME, snmp_user_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_switch_security_level_as_authorization(cls, timeout=5, fail_if_false=True):
        logger.debug("tick 'Security Level' as 'Authorization'")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SWITCH_AUTHORIZATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_switch_security_level_as_authorization_and_privacy(cls, timeout=5, fail_if_false=True):
        logger.debug("tick 'Security Level' as 'Authorization and privacy'")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SWITCH_AUTHORIZATION_AND_PRIVACY, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_switch_authorization_protocol(cls, protocol, timeout=5, fail_if_false=True):
        logger.debug("select 'Authorization protocol' as '%s'" % protocol)
        FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_SWITCH_AUTHORIZATION_PROTOCOL, protocol, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch_snmp_authorization_password(cls, snmp_user_name, timeout=5, fail_if_false=True):
        logger.debug("input 'SNMP Authorization password' as '%s'" % snmp_user_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH_AUTHORIZATION_PASSWORD, snmp_user_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_switch_community_string(cls, community_string, timeout=5, fail_if_false=True):
        logger.debug("input 'Community string' of 'Switch' as '%s'" % community_string)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SWITCH_COMMUNITY_STRING, community_string, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_or_add_switch_dialog_close(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Edit Switch Credentials' to close ...")
        if ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_EDIT_OR_ADD_SWITCH, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Edit Switch Credentials' successfully closed")
            return True
        else:
            msg = "failed to wait for dialog 'Edit Switch Credentials' to close"
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def click_ok_button_on_edit_or_add_switch_dialog(cls, timeout=5, fail_if_false=True):
        logger.debug("click button 'OK'")
        FusionUIBase.wait_for_element_and_click(cls.e.ID_BUTTON_OK_FOR_EDIT_OR_ADD_SWITCH, timeout=timeout, fail_if_false=fail_if_false, js_click=True)

    @classmethod
    def click_cancel_button_on_edit_or_add_switch_dialog(cls, timeout=5, fail_if_false=True):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL_FOR_EDIT_OR_ADD_SWITCH, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_ok_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click button 'OK'")
        FusionUIBase.wait_for_element_and_click(cls.e.ID_BUTTON_OK, timeout=timeout, fail_if_false=fail_if_false, js_click=True)

    @classmethod
    def click_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_logical_switch_dialog_close(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Edit Logical Switch' to close ...")
        if ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_EDIT_LOGICAL_SWITCH, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Edit Logical Switch' successfully closed")
            return True
        else:
            msg = "failed to wait for dialog 'Edit Logical Switch' to close"
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def get_error_message_if_edit_failed(cls, timeout=5, fail_if_false=True):
        logger.debug("get error message if edit failed")
        return ui_lib.get_text(cls.e.ID_ERROR_EDIT_FAILED, timeout=timeout, fail_if_false=fail_if_false)


class EditLogicalSwitches(_BaseEditLogicalSwitches):
    pass


class C7000EditLogicalSwitches(object):
    pass


class TBirdEditLogicalSwitches(object):
    pass


class _BaseDeleteLogicalSwitches(object):

    e = DeleteLogicalSwitchesElements

    @classmethod
    def click_delete_button(cls, timeout=5):
        logger.debug("click 'Delete' button from Actions menu")
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_ACTIONS_DELETE, timeout=timeout, fail_if_false=True)

    @classmethod
    def select_actions_delete(cls, timeout=5):
        logger.debug("click 'Actions -> Delete' button ")
        CommonOperationLogicalSwitches.click_actions_button(timeout=timeout)
        cls.click_delete_button(timeout=timeout)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_logical_switch_dialog_open(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Delete Logical Switch' to open ...")
        if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_DELETE_LOGICAL_SWITCH, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Delete Logical Switch' successfully opened")
            return True
        else:
            msg = "failed to wait for dialog 'Delete Logical Switch' to open within %s seconds" % timeout
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_logical_switch_dialog_close(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Delete Logical Switch' to close ...")
        if ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_DELETE_LOGICAL_SWITCH, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Delete Logical Switch' successfully closed")
            return True
        else:
            msg = "failed to wait for dialog 'Delete Logical Switch' to close"
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def click_yes_delete_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click button 'Yes, delete' button")
        FusionUIBase.wait_for_element_and_click(cls.e.ID_BUTTON_YES_DELETE, timeout=timeout, fail_if_false=fail_if_false, js_click=True)

    @classmethod
    def click_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout=timeout, fail_if_false=fail_if_false)


class DeleteLogicalSwitches(_BaseDeleteLogicalSwitches):
    pass


class C7000DeleteLogicalSwitches(_BaseDeleteLogicalSwitches):
    pass


class TBirdDeleteLogicalSwitches(_BaseDeleteLogicalSwitches):
    pass


class _BaseVerifyLogicalSwitches(object):

    e = GeneralLogicalSwitchesElements

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_warning_msg_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("verifying the warning message visibility")
        return ui_lib.wait_for_element_visible(GeneralLogicalSwitchesElements.ID_WARNING_MSG, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_switch_should_not_exist(cls, ls_name, timeout=5, fail_if_false=True):
        logger.debug("verify Logical Switch '%s' should NOT exist ..." % ls_name)
        if ui_lib.wait_for_element_notvisible(cls.e.ID_TABLE_LOGICAL_SWITCH % ls_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("Logical Switch '%s' is successfully verified as invisible within %s second(s)" % (ls_name, timeout))
            return True
        elif ui_lib.wait_for_element_visible(cls.e.ID_TABLE_LOGICAL_SWITCH_NOT_FOUND % ls_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("Logical Switch '%s' was deleted but not de-selected." % ls_name)
            return True
        else:
            msg = "Logical Switch '%s' is failed to be verified as invisible within %s second(s)" % (ls_name, timeout)
            return FusionUIBase.fail_test_or_return_false(message=msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_switch_should_exist(cls, ls_name, timeout=5, fail_if_false=True):
        logger.debug("verify Logical Switch '%s' should exist ..." % ls_name)
        if ui_lib.wait_for_element_visible(cls.e.ID_TABLE_LOGICAL_SWITCH % ls_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("Logical Switch '%s' is successfully verified as visible within %s second(s)" % (ls_name, timeout))
            return True
        else:
            msg = "Logical Switch '%s' is failed to be verified as visible within %s second(s)" % (ls_name, timeout)
            return FusionUIBase.fail_test_or_return_false(message=msg, fail_if_false=fail_if_false)


class VerifyLogicalSwitches(_BaseVerifyLogicalSwitches):
    pass


class C7000VerifyLogicalSwitches(_BaseVerifyLogicalSwitches):
    pass


class TBirdVerifyLogicalSwitches(_BaseVerifyLogicalSwitches):
    pass

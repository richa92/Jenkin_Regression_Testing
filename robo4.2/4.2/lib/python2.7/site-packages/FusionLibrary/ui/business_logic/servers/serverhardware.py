from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.servers.serverhardware_elements import GeneralServerHardwareElements
from FusionLibrary.ui.business_logic.servers.serverhardware_elements import AddServerHardwareElements
from FusionLibrary.ui.business_logic.servers.serverhardware_elements import PowerOnHardwareElements
from FusionLibrary.ui.business_logic.servers.serverhardware_elements import PowerOffHardwareElements
from FusionLibrary.ui.business_logic.servers.serverhardware_elements import ResetHardwareElements
from FusionLibrary.ui.business_logic.servers.serverhardware_elements import RefreshHardwareElements
from FusionLibrary.ui.business_logic.servers.serverhardware_elements import RemoveHardwareElements
from FusionLibrary.ui.business_logic.servers.serverhardware_elements import VerifyHardwareElements
from FusionLibrary.ui.business_logic.servers.serverhardware_elements import EditScopeElements
from FusionLibrary.ui.business_logic.servers.serverhardware_elements import UtilizationElements
from FusionLibrary.ui.business_logic.base import FusionUIBase, TakeScreenShotWhenReturnFalseDeco
from RoboGalaxyLibrary.utilitylib import logging as logger
from datetime import datetime
from RoboGalaxyLibrary import BuiltIn
import types
import sys


class CommonOperationServerHardware(object):

    @classmethod
    def get_server_hardware_list(cls, timeout=5, fail_if_false=True):
        logger.debug("get all server hardware names from table")
        server_hardware_list = []
        if ui_lib.wait_for_element(GeneralServerHardwareElements.ID_TABLE_SERVER_HARDWARE_LIST):
            server_hardware_list = FusionUIBase.get_multi_elements_text(GeneralServerHardwareElements.ID_TABLE_SERVER_HARDWARE_LIST, timeout=timeout, fail_if_false=fail_if_false)
        return server_hardware_list

    @classmethod
    def get_server_hardware_type(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("get 'Server hardware type' of server '%s' ..." % server_name)
        server_hardware_type = None
        if ui_lib.wait_for_element(GeneralServerHardwareElements.ID_TEXT_HARDWARE_SERVER_HARDWARE_TYPE):
            server_hardware_type = FusionUIBase.get_text(GeneralServerHardwareElements.ID_TEXT_HARDWARE_SERVER_HARDWARE_TYPE, timeout=timeout, fail_if_false=fail_if_false)
            logger.debug("retrieved 'Server hardware type' of server '%s' is '%s'" % (server_name, server_hardware_type))
        else:
            logger.warn("unable to locate element xpath of 'Server hardware type' of server '%s', function 'get_server_hardware_type' failed" % server_name)
        return server_hardware_type

    @classmethod
    def get_server_hardware_power_state(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("Get 'Server hardware power state' of server '%s' ..." % server_name)
        server_hardware_power_state = None
        locator = GeneralServerHardwareElements.ID_TEXT_HARDWARE_SERVER_POWER
        if ui_lib.wait_for_element(locator):
            server_hardware_power_state = FusionUIBase.get_text(locator, timeout=timeout, fail_if_false=fail_if_false)
            logger.debug("retrieved 'Server power' state of server '%s' is '%s'" % (server_name, server_hardware_power_state))
        else:
            logger.warn("unable to locate element xpath of 'Server hardware power state' of server '%s', function 'get_server_hardware_power_state' failed" % server_name)
            server_hardware_power_state = "XPATH failed: '%s'" % locator
        return server_hardware_power_state

    @classmethod
    def click_server_hardware(cls, server_name, timeout=5, time_for_loading=3):
        logger.debug("click server hardware '%s'" % server_name)
        locator = GeneralServerHardwareElements.ID_TABLE_SERVER_HARDWARE % server_name
        ui_lib.scroll_into_view(locator)
        ui_lib.wait_for_element_and_click(GeneralServerHardwareElements.ID_TABLE_SERVER_HARDWARE % server_name, timeout, fail_if_false=True)
        BuiltIn().sleep(time_for_loading)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_server_hardware_selected(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("wait server hardware '%s' selected" % server_name)
        if ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_TABLE_SERVER_HARDWARE_SELECTED % server_name, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_server_hardware_show_not_found(cls, server_name, timeout=5, fail_if_false=True):
        logger.info("wait server hardware status change to 'not found'")
        if ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_TABLE_SERVER_HARDWARE_DELETED % server_name, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def click_action_button(cls, timeout=5):
        logger.debug("click action button")
        locator = GeneralServerHardwareElements.ID_DROPDOWN_ACTIONS
        el_class = FusionUIBase.get_webelement_attribute(locator, 'class', timeout=5, fail_if_false=False)
        logger.debug("'Actions' button class is [ %s ]" % el_class)
        if 'hp-active' not in el_class:
            logger.debug("click 'Actions' button since 'hp-active' not found, means it's not clicked to open the action menu")
            BuiltIn().sleep(5)
            # logger.debug("111111111111")
            ui_lib.wait_for_element_and_click(locator, timeout, fail_if_false=True)
            # logger.debug("222222222222")
            BuiltIn().sleep(5)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_server_hardware_status_ok(cls, server_name, timeout=10, fail_if_false=True):
        start = datetime.now()
        logger.debug("waiting for server hardware '%s' status change to 'ok' ..." % server_name)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_STATUS_SERVER_HARDWARE_OK % server_name, timeout=2, fail_if_false=False):
                logger.debug("server hardware '%s' status is 'ok' as expected." % server_name)
                return True
            elif ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_STATUS_SERVER_HARDWARE_WARN % server_name, timeout=2, fail_if_false=False):
                err_msg = "server hardware '%s' status is 'warn' not as expected." % server_name
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            elif ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_STATUS_SERVER_HARDWARE_ERROR % server_name, timeout=2, fail_if_false=False):
                err_msg = "server hardware '%s' status is 'error' not as expected." % server_name
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            else:
                logger.debug("server hardware status is unknown, waiting ...")
                continue
        err_msg = "Timeout to waiting server hardware '%s' status change to 'ok'." % server_name
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)
        return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_server_hardware_status_ok_or_warn(cls, server_name, timeout=10, fail_if_false=True):
        start = datetime.now()
        # logger.warn("________________________________")
        logger.debug("waiting for server hardware '%s' status change to 'ok' or 'warn' ..." % server_name)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_STATUS_SERVER_HARDWARE_OK % server_name, timeout=5, fail_if_false=False):
                logger.debug("server hardware '%s' status is 'ok' as expected." % server_name)
                return True
            elif ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_STATUS_SERVER_HARDWARE_WARN % server_name, timeout=5, fail_if_false=False):
                logger.debug("server hardware '%s' status is 'warn' as expected." % server_name)
                return True
            elif ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_STATUS_SERVER_HARDWARE_ERROR % server_name, timeout=5, fail_if_false=False):
                err_msg = "server hardware '%s' status is 'error' not as expected." % server_name
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            else:
                logger.debug("server hardware '%s' status is unknown, waiting ..." % server_name)
                continue
        err_msg = "Timeout to waiting server hardware '%s' status change to 'ok' or 'warn'." % server_name
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_server_hardware_status_error(cls, server_name, timeout=10, fail_if_false=True):
        start = datetime.now()
        logger.debug("waiting server hardware '%s' status change to error" % server_name)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_STATUS_SERVER_HARDWARE_OK % server_name, timeout=5, fail_if_false=False):
                err_msg = "server hardware '%s' status is ok not as expected." % server_name
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            elif ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_STATUS_SERVER_HARDWARE_WARN % server_name, timeout=5, fail_if_false=False):
                logger.debug("server hardware '%s' status is warning not as expected." % server_name)
                return False
            elif ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_STATUS_SERVER_HARDWARE_ERROR % server_name, timeout=5, fail_if_false=False):
                logger.debug("server hardware '%s' status is error as expected." % server_name)
                return True
            else:
                logger.debug("server hardware '%s' status is unknown, waiting ..." % server_name)
                continue
        err_msg = "Timeout to waiting server hardware status change to error."
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    def get_page_notify_message(cls, timeout=5, fail_if_false=True):
        logger.debug('get notify message on the page')
        if ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_PAGE_NOTIFICATION_MESSAGE, timeout, fail_if_false=False):
            return FusionUIBase.get_text(GeneralServerHardwareElements.ID_PAGE_NOTIFICATION_MESSAGE, timeout, fail_if_false)
        else:
            logger.warn("Could not find element of notify message: %s" % GeneralServerHardwareElements.ID_PAGE_NOTIFICATION_MESSAGE)
            return None

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_server_power_change_to(cls, power_state, timeout=10, fail_if_false=True):
        logger.debug("waiting for server power changing to '%s' within at longest %s seconds ..." % (power_state, timeout))
        start = datetime.now()
        locator = GeneralServerHardwareElements.ID_TEXT_HARDWARE_SERVER_POWER
        if ui_lib.wait_for_element_text_match(locator=locator, regex=power_state, timeout=timeout, fail_if_false=fail_if_false) is True:
            logger.debug("'Server power' is successfully changed to '%s' within %s seconds" % (power_state, (datetime.now() - start).total_seconds()))
            return True
        else:
            logger.warn("'Server power' is NOT changed to '%s' within %s seconds" % (power_state, (datetime.now() - start).total_seconds()))
            return False

    @classmethod
    def click_create_profile_link(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("click 'Create profile' link for server hardware '%s' ..." % server_name)
        FusionUIBase.wait_for_element_and_click(GeneralServerHardwareElements.ID_TEXT_HARDWARE_SERVER_PROFILE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_uid_light(cls, timeout=5):
        logger.debug("click [ UID Light ] icon")
        ui_lib.wait_for_element_and_click(GeneralServerHardwareElements.ID_BUTTON_UID_LIGHT, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uid_light_on(cls, timeout=60, fail_if_false=True):
        logger.debug("verify [ UID Light ] in on state")
        return ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_STATUS_UID_LIGHT_ON, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uid_light_off(cls, timeout=60, fail_if_false=True):
        logger.debug("verify [ UID Light ] in off state")
        return ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_STATUS_UID_LIGHT_OFF, timeout, fail_if_false)

    @classmethod
    def click_activity_collapser(cls, activity_name, timeout=10, fail_if_false=True):
        logger.debug("click to expand activity '%s'" % activity_name)
        ui_lib.wait_for_element_and_click(GeneralServerHardwareElements.ID_ICON_ACTIVITY_COLLAPSER % activity_name, timeout=timeout, fail_if_false=fail_if_false)


class AddHardware(object):

    @classmethod
    def click_add_server_hardware_button(cls, timeout=5):
        logger.debug("click 'add server hardware' button")
        ui_lib.wait_for_element_and_click(AddServerHardwareElements.ID_BUTTON_ADD_SERVER_HARDWARE, timeout, fail_if_false=True)

    @classmethod
    def select_action_add(cls, timeout=5):
        logger.debug("select action 'add'")
        ui_lib.wait_for_element_and_click(GeneralServerHardwareElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(AddServerHardwareElements.ID_SELECT_ACTION_ADD, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_server_hardware_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'add server hardware' to show up ...")
        if ui_lib.wait_for_element_visible(AddServerHardwareElements.ID_DIALOG_ADD_SERVER_HARDWARE, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def input_ilo_ip(cls, ilo_ip, timeout=5):
        logger.debug("input 'iLO IP address or hostname' as '%s'" % ilo_ip)
        ui_lib.wait_for_element_and_input_text(AddServerHardwareElements.ID_INPUT_ILO_IP, ilo_ip, timeout, fail_if_false=True)

    @classmethod
    def tick_add_server_hardware_as_managed(cls, timeout=5):
        logger.debug("choose 'add server hardware as' as 'Managed'")
        ui_lib.wait_for_element_and_click(AddServerHardwareElements.ID_RADIO_ADD_SERVER_HARDWARE_AS_MANAGED, timeout, fail_if_false=True)

    @classmethod
    def tick_add_server_hardware_as_monitored(cls, timeout=5):
        logger.debug("choose 'add server hardware as' as 'Monitored'")
        ui_lib.wait_for_element_and_click(AddServerHardwareElements.ID_RADIO_ADD_SERVER_HARDWARE_AS_MONITORED, timeout, fail_if_false=True)

    @classmethod
    def input_ilo_username(cls, ilo_username, timeout=5):
        logger.debug("input 'iLO username' as '%s'" % ilo_username)
        ui_lib.wait_for_element_and_input_text(AddServerHardwareElements.ID_INPUT_USER_NAME, ilo_username, timeout, fail_if_false=True)

    @classmethod
    def input_ilo_password(cls, ilo_password, timeout=5):
        logger.debug("input 'iLO password' as '%s'" % ilo_password)
        ui_lib.wait_for_element_and_input_text(AddServerHardwareElements.ID_INPUT_PASSWORD, ilo_password, timeout, fail_if_false=True)

    @classmethod
    def tick_licensing_as_hp_oneview_advanced(cls, timeout=5):
        logger.debug("choose 'Licensing' as 'HPE OneView Advanced'")
        ui_lib.wait_for_element_and_click(AddServerHardwareElements.ID_RADIO_LICENSING_HP_ONEVIEW_ADVANCED, timeout, fail_if_false=True)

    @classmethod
    def tick_licensing_as_hp_oneview_advanced_without_ilo(cls, timeout=5):
        logger.debug("choose 'Licensing' as 'HPE OneView Advanced w/o iLO'")
        ui_lib.wait_for_element_and_click(AddServerHardwareElements.ID_RADIO_LICENSING_HP_ONEVIEW_ADVANCED_WO_ILO, timeout, fail_if_false=True)

    @classmethod
    def click_add_button(cls, timeout=5):
        logger.debug("click button 'Add'")
        ui_lib.wait_for_element_and_click(AddServerHardwareElements.ID_BUTTON_ADD, timeout, fail_if_false=True)

    @classmethod
    def click_add_plus_button(cls, timeout=5):
        logger.debug("click button 'Add+'")
        ui_lib.wait_for_element_and_click(AddServerHardwareElements.ID_BUTTON_ADD_PLUS, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(AddServerHardwareElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    def tick_force_add_option(cls, timeout=5):
        logger.debug("tick 'force-add'")
        ui_lib.wait_for_element_and_click(AddServerHardwareElements.ID_CHECKBOX_FORCE_ADD, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_server_hardware_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Add server hardware' to disappear ...")
        # ui_lib.wait_for_element_notvisible(AddServerHardwareElements.ID_DIALOG_ADD_SERVER_HARDWARE, timeout, fail_if_false)
        if ui_lib.wait_for_element_notvisible(AddServerHardwareElements.ID_DIALOG_ADD_SERVER_HARDWARE, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Add server hardware' successfully disappeared")
            return True
        else:
            msg = "failed to wait for dialog 'Add server hardware' to disappear"
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)


class PowerOnHardware(object):

    @classmethod
    def select_action_power_on(cls, timeout=5):
        logger.debug("click 'Actions' menu and select 'Power on'")
        ui_lib.wait_for_element_and_click(GeneralServerHardwareElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(PowerOnHardwareElements.ID_SELECT_ACTION_POWER_ON, timeout, fail_if_false=True)

    @classmethod
    def click_power_on_button(cls, timeout=5):
        logger.debug("click 'Power on' button ...")
        ui_lib.wait_for_element_and_click(PowerOnHardwareElements.ID_SELECT_ACTION_POWER_ON, timeout, fail_if_false=True)

    @classmethod
    def click_close_button_of_error_dialog(cls, timeout=5):
        logger.debug("click 'Close' button of error message dialog ...")
        ui_lib.wait_for_element_and_click(PowerOnHardwareElements.ID_BUTTON_CLOSE_ERROR_DIALOG, timeout, fail_if_false=True)


class PowerOffHardware(object):

    @classmethod
    def select_action_power_off(cls, timeout=5):
        logger.debug("select action 'Power off'")
        ui_lib.wait_for_element_and_click(GeneralServerHardwareElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(PowerOffHardwareElements.ID_SELECT_ACTION_POWER_OFF, timeout, fail_if_false=True)

    @classmethod
    def click_press_and_hold_button(cls, timeout=5):
        logger.debug("click button 'Press and hold'")
        ui_lib.wait_for_element_and_click(PowerOffHardwareElements.ID_BUTTON_PRESS_AND_HOLD, timeout, fail_if_false=True)

    @classmethod
    def click_momentary_press_button(cls, timeout=5):
        logger.debug("click button 'Momentary press'")
        ui_lib.wait_for_element_and_click(PowerOffHardwareElements.ID_BUTTON_MOMENTARY_PRESS, timeout, fail_if_false=True)

    @classmethod
    def click_close_button(cls, timeout=5):
        logger.debug("click button 'Close'")
        ui_lib.wait_for_element_and_click(PowerOffHardwareElements.ID_BUTTON_CLOSE, timeout, fail_if_false=True)


class ResetHardware(object):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_reset_ilo_dialog_open(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Reset iLO] dialog open")
        return ui_lib.wait_for_element_visible(ResetHardwareElements.ID_DIALOG_RESET_ILO, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_reset_ilo_dialog_close(cls, timeout=15, fail_if_false=True):
        logger.debug("wait [ Reset iLO] dialog close")
        return ui_lib.wait_for_element_notvisible(ResetHardwareElements.ID_DIALOG_RESET_ILO, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_reset_ilo_dialog_msg(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify reset ilo msg, expect value is [ %s ]" % expect_value)
        actual_value = FusionUIBase.get_text(ResetHardwareElements.ID_TEXT_REST_ILO_WARN_MSG, timeout, fail_if_false)
        if actual_value.strip() == expect_value.strip():
            logger.debug("reset ilo msg is '%s' as expected" % actual_value)
            return True
        else:
            msg = "reset ilo msg is '%s' not as expected" % actual_value
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def select_action_reset_ilo(cls, timeout=5):
        logger.debug("select action 'Reset iLO'")
        ui_lib.wait_for_element_and_click(GeneralServerHardwareElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(ResetHardwareElements.ID_SELECT_ACTION_RESET_ILO, timeout, fail_if_false=True)

    @classmethod
    def click_yes_reset_ilo_button(cls, timeout=5):
        logger.debug("click button 'Yes,reset'")
        ui_lib.wait_for_element_and_click(ResetHardwareElements.ID_BUTTON_YES_RESET, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_reset_ilo_button(cls, timeout=5):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(ResetHardwareElements.ID_BUTTON_CANCEL_RESET_ILO, timeout=timeout, fail_if_false=True)

    @classmethod
    def click_close_reset_ilo_button(cls, timeout=5):
        logger.debug("click button 'Close'")
        ui_lib.wait_for_element_and_click(ResetHardwareElements.ID_BUTTON_CLOSE_RESET_ILO, timeout=timeout, fail_if_false=True)

    @classmethod
    def select_action_reset(cls, timeout=5):
        logger.debug("select action 'Reset'")
        ui_lib.wait_for_element_and_click(GeneralServerHardwareElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(ResetHardwareElements.ID_SELECT_ACTION_RESET, timeout, fail_if_false=True)

    @classmethod
    def click_reset_button(cls, timeout=5):
        logger.debug("click button 'Reset'")
        ui_lib.wait_for_element_and_click(ResetHardwareElements.ID_BUTTON_RESET, timeout, fail_if_false=True)

    @classmethod
    def click_cold_boot_button(cls, timeout=5):
        logger.debug("click button 'Cold boot'")
        ui_lib.wait_for_element_and_click(ResetHardwareElements.ID_BUTTON_COLD_BOOT, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(ResetHardwareElements.ID_BUTTON_CANCEL, timeout=timeout, fail_if_false=True)


class RefreshHardware(object):

    @classmethod
    def select_action_refresh(cls, timeout=5):
        logger.debug("select action 'Refresh'")
        ui_lib.wait_for_element_and_click(GeneralServerHardwareElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(RefreshHardwareElements.ID_SELECT_ACTION_REFRESH, timeout, fail_if_false=True)

    @classmethod
    def wait_until_refresh_dialog_is_visible(cls, timeout=5):
        logger.debug("wait until the refresh server hardware dialog open")
        ui_lib.wait_for_element_visible(RefreshHardwareElements.ID_TITLE_FORCE_REFRESH_DIALOG, timeout)

    @classmethod
    def wait_until_refresh_dialog_is_closed(cls, timeout=5):
        logger.debug("wait until the refresh server hardware dialog closed")
        ui_lib.wait_for_element_notvisible(RefreshHardwareElements.ID_TITLE_FORCE_REFRESH_DIALOG, timeout)

    @classmethod
    def is_refresh_dialog_visible(cls, timeout=5):
        logger.debug("wait until the refresh server hardware dialog open")
        cls.wait_until_refresh_dialog_is_visible(timeout)
        if not ui_lib.is_visible(RefreshHardwareElements.ID_TITLE_FORCE_REFRESH_DIALOG):
            return False

        return True

    @classmethod
    def input_ilo_hostname(cls, hostname, timeout=5):
        logger.debug("Input iLO hostname")
        ui_lib.wait_for_element_and_input_text(RefreshHardwareElements.ID_INPUT_HOSTNAME_FORCE_REFRESH,
                                               hostname, timeout)

    @classmethod
    def input_ilo_username(cls, username, timeout=5):
        logger.debug("Input iLO username")
        ui_lib.wait_for_element_and_input_text(RefreshHardwareElements.ID_INPUT_USERNAME_FORCE_REFRESH,
                                               username, timeout)

    @classmethod
    def input_ilo_password(cls, password, timeout=5):
        logger.debug("Input iLO password")
        ui_lib.wait_for_element_and_input_text(RefreshHardwareElements.ID_INPUT_PASSWORD_FORCE_REFRESH,
                                               password, timeout)

    @classmethod
    def click_ok_button(cls, timeout=5):
        logger.debug("click OK button")
        ui_lib.wait_for_element_and_click(RefreshHardwareElements.ID_BUTTON_ADD_FORCE_REFRESH, timeout)


class RemoveHardware(object):

    @classmethod
    def select_action_remove(cls, timeout=5):
        logger.debug("select action 'Remove'")
        ui_lib.wait_for_element_and_click(GeneralServerHardwareElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(RemoveHardwareElements.ID_SELECT_ACTION_REMOVE, timeout, fail_if_false=True)

    @classmethod
    def click_yes_remove_button(cls, timeout=5):
        logger.debug("click button 'Yes, remove'")
        ui_lib.wait_for_element_and_click(RemoveHardwareElements.ID_BUTTON_YES_REMOVE, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(RemoveHardwareElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)


class VerifyHardware(object):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_hardware_task_status_from_activity_view(cls, server_name, activity_task, action_name, expected_task_status, timeout=5, fail_if_false=True):
        logger.debug("verify [ activity task '%s'  ] change to '%s' status" % (activity_task, expected_task_status))
        activity_time_org = GeneralServerHardwareElements.ID_TEXT_SIDEBAR_ACTIVITY_TIME % (server_name, action_name)
        activity_time = ui_lib.get_webelement_attribute('title', activity_time_org)
        base_time = activity_time[:-1].replace("-", '').replace('T', '').replace(':', '')
        logger.debug("The time baseline is %s" % base_time)
        locator = GeneralServerHardwareElements.ID_TEXT_VIEW_ACTIVITY % (base_time, activity_task, expected_task_status)
        return ui_lib.wait_for_element_visible(locator, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_hardware_not_exist(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("verify that server hardware '%s' should NOT exist ..." % server_name)
        if ui_lib.wait_for_element_notvisible(GeneralServerHardwareElements.ID_TABLE_SERVER_HARDWARE % server_name, timeout, fail_if_false):
            logger.debug("server hardware '%s' is successfully verified as invisible within %s seconds" % (server_name, timeout))
            return True
        else:
            msg = "server hardware '%s' is NOT successfully verified as invisible within %s seconds" % (server_name, timeout)
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_hardware_exist(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("verify that server hardware '%s' should exist ..." % server_name)
        if ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_TABLE_SERVER_HARDWARE % server_name, timeout, fail_if_false):
            logger.debug("server hardware '%s' is successfully verified as visible within %s seconds" % (server_name, timeout))
            return True
        else:
            msg = "server hardware '%s' is NOT successfully verified as visible within %s seconds" % (server_name, timeout)
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_hardware_status_ok(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("verify that server hardware '%s' status should be 'OK'" % server_name)
        if ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_STATUS_SERVER_HARDWARE_OK % server_name, timeout, fail_if_false):
            logger.debug("server hardware '%s' status is successfully verified as 'OK' within %s seconds" % (server_name, timeout))
            return True
        else:
            msg = "server hardware '%s' status is NOT successfully verified as 'OK' within %s seconds" % (server_name, timeout)
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_hardware_warn(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("verify that server hardware '%s' status should be 'WARN'" % server_name)
        if ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_STATUS_SERVER_HARDWARE_WARN % server_name, timeout, fail_if_false):
            logger.debug("server hardware '%s' status is successfully verified as 'WARN' within %s seconds" % (server_name, timeout))
            return True
        else:
            msg = "server hardware '%s' status is NOT successfully verified as 'WARN' within %s seconds" % (server_name, timeout)
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_hardware_error(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("verify that server hardware '%s' status should be 'ERROR'" % server_name)
        if ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_STATUS_SERVER_HARDWARE_ERROR % server_name, timeout, fail_if_false):
            logger.debug("server hardware '%s' status is successfully verified as 'ERROR' within %s seconds" % (server_name, timeout))
            return True
        else:
            msg = "server hardware '%s' status is NOT successfully verified as 'ERROR' within %s seconds" % (server_name, timeout)
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_hardware_unknown(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("verify whether server hardware %s is unknown" % server_name)
        if ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_STATUS_SERVER_HARDWARE_UNKNOWN % server_name, timeout, fail_if_false):
            return True
        else:
            msg = "server hardware '%s' status is NOT successfully verified as 'UNKNOWN' within %s seconds" % (server_name, timeout)
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_hardware_status(cls, server_name, expect_status, timeout=5, fail_if_false=False):
        logger.debug("verify server hardware status, expecting '%s'" % expect_status)
        if expect_status.lower() == "ok":
            return ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_STATUS_SERVER_HARDWARE_OK % server_name, timeout, fail_if_false)
        elif expect_status.lower() == "warn":
            return ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_STATUS_SERVER_HARDWARE_WARN % server_name, timeout, fail_if_false)
        elif expect_status.lower() == "error":
            return ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_STATUS_SERVER_HARDWARE_ERROR % server_name, timeout, fail_if_false)
        elif expect_status.lower() == "unknown":
            return ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_STATUS_SERVER_HARDWARE_UNKNOWN % server_name, timeout, fail_if_false)
        else:
            msg = "Unidentified value: 'expect_status': '%s', expecting 'OK', 'WARN', 'ERROR' or 'UNKNOWN'" % expect_status
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_state(cls, expect_value, timeout=5, fail_if_false=True):
        locator = GeneralServerHardwareElements.ID_TEXT_HARDWARE_STATE
        item_name = "State"
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_state_for_exclusion(cls, excluded_value, timeout=5, fail_if_false=True):
        locator = GeneralServerHardwareElements.ID_TEXT_HARDWARE_STATE
        item_name = "State"
        return FusionUIBase.verify_element_text_for_exclusion(item_name=item_name, locator=locator, excluded_value=excluded_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_server_profile(cls, expect_value, timeout=5, fail_if_false=True):
        # TODO: update element definition for server hardware
        actual_value = FusionUIBase.get_text(GeneralServerHardwareElements.ID_TEXT_GENERAL_VLAN, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("network vlan is '%s' as expected" % actual_value)
            return True
        else:
            msg = "network vlan is '%s' not as expected" % actual_value
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_server_power(cls, expect_value, timeout=5, fail_if_false=True):
        locator = GeneralServerHardwareElements.ID_TEXT_HARDWARE_SERVER_POWER
        item_name = "Server power"
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_server_power_for_exclusion(cls, excluded_value, timeout=5, fail_if_false=True):
        locator = GeneralServerHardwareElements.ID_TEXT_HARDWARE_SERVER_POWER
        item_name = "Server power"
        return FusionUIBase.verify_element_text_for_exclusion(item_name=item_name, locator=locator, excluded_value=excluded_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_model(cls, expect_value, timeout=5, fail_if_false=True):
        # TODO: update element definition for server hardware
        actual_value = FusionUIBase.get_text(GeneralServerHardwareElements.ID_TEXT_GENERAL_PREFERRED_BANDWIDTH, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("network preferred bandwidth is '%s' as expected" % actual_value)
            return True
        else:
            msg = "network preferred bandwidth is '%s' not as expected" % actual_value
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_server_hardware_type(cls, expect_value, timeout=5, fail_if_false=True):
        # TODO: update element definition for server hardware
        actual_value = FusionUIBase.get_text(GeneralServerHardwareElements.ID_TEXT_GENERAL_MAXIMUM_BANDWIDTH, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("network maximum bandwidth is '%s' as expected" % actual_value)
            return True
        else:
            msg = "network maximum bandwidth is '%s' not as expected" % actual_value
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_serial_number(cls, expect_value, timeout=5, fail_if_false=True):
        # TODO: update element definition for server hardware
        actual_value = FusionUIBase.get_text(GeneralServerHardwareElements.ID_TEXT_GENERAL_SMART_LINK, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("network smart link is '%s' as expected" % actual_value)
            return True
        else:
            msg = "network smart link is '%s' not as expected" % actual_value
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_license(cls, expect_value, timeout=5, fail_if_false=True):
        # TODO: update element definition for server hardware
        actual_value = FusionUIBase.get_text(GeneralServerHardwareElements.ID_TEXT_GENERAL_PRIVATE_NETWORK, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("network private network is '%s' as expected" % actual_value)
            return True
        else:
            msg = "network private network is '%s' not as expected" % actual_value
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_uuid(cls, expect_value, timeout=5, fail_if_false=True):
        # TODO: update element definition for server hardware
        actual_value = FusionUIBase.get_text(GeneralServerHardwareElements.ID_TEXT_GENERAL_PRIVATE_NETWORK, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("network private network is '%s' as expected" % actual_value)
            return True
        else:
            msg = "network private network is '%s' not as expected" % actual_value
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_ilo_address(cls, expect_value, timeout=5, fail_if_false=True):
        # TODO: update element definition for server hardware
        actual_value = FusionUIBase.get_text(GeneralServerHardwareElements.ID_TEXT_GENERAL_UPLINK_SET, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("network uplink set is '%s' as expected" % actual_value)
            return True
        else:
            msg = "network uplink set is '%s' not as expected" % actual_value
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_location(cls, expect_list, timeout=5, fail_if_false=True):
        # TODO: update element definition for server hardware
        actual_list = FusionUIBase.get_multi_elements_text(GeneralServerHardwareElements.ID_TEXT_GENERAL_USED_BY_SERVER_PROFILES, timeout, fail_if_false)
        if (expect_list is None) or len(expect_list) == 0:
            expect_list = ['no server profiles']
        expect_list = [expect_list] if not isinstance(types.ListType, expect_list) else expect_list
        match_count = 0
        for expect_value in expect_list:
            for actual_value in actual_list:
                if actual_value.lower().strip() == expect_value.lower().strip():
                    match_count += 1
        if match_count == len(actual_list) == len(expect_list):
            logger.debug("network is used by server profile(s) '%s' as expected" % actual_list)
            return True
        else:
            msg = "network is used by server profile(s) '%s' not as expected" % actual_list
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_powered_by(cls, expect_list, timeout=5, fail_if_false=True):
        # TODO: update element definition for server hardware
        actual_list = FusionUIBase.get_multi_elements_text(GeneralServerHardwareElements.ID_TEXT_GENERAL_USED_BY_STORAGE_SYSTEMS, timeout, fail_if_false)
        if (expect_list is None) or len(expect_list) == 0:
            expect_list = ['no storage systems']
        expect_list = [expect_list] if not isinstance(types.ListType, expect_list) else expect_list
        match_count = 0
        for expect_value in expect_list:
            for actual_value in actual_list:
                if actual_value.lower().strip() == expect_value.lower().strip():
                    match_count += 1
        if match_count == len(actual_list) == len(expect_list):
            logger.debug("network is used by storage system(s) '%s' as expected" % actual_list)
            return True
        else:
            msg = "network is used by storage system(s) '%s' not as expected" % actual_list
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_cpu(cls, expect_list, timeout=5, fail_if_false=True):
        # TODO: update element definition for server hardware
        actual_list = FusionUIBase.get_multi_elements_text(GeneralServerHardwareElements.ID_TEXT_GENERAL_MEMBER_OF, timeout, fail_if_false)
        if (expect_list is None) or len(expect_list) == 0:
            expect_list = ['none']
        expect_list = [expect_list] if not isinstance(types.ListType, expect_list) else expect_list
        match_count = 0
        for expect_value in expect_list:
            for actual_value in actual_list:
                if actual_value.lower().strip() == expect_value.lower().strip():
                    match_count += 1
        if match_count == len(actual_list) == len(expect_list):
            logger.debug("network is member of '%s' as expected" % actual_list)
            return True
        else:
            msg = "network is member of '%s' not as expected" % actual_list
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_memory(cls, expect_value, timeout=5, fail_if_false=True):
        # TODO: update element definition for server hardware
        actual_value = FusionUIBase.get_text(GeneralServerHardwareElements.ID_TEXT_GENERAL_ASSOCIATE_WITH_SAN, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("network is associate with san '%s' as expected" % actual_value)
            return True
        else:
            msg = "network is associate with san '%s' not as expected" % actual_value
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_utilization_cpu(cls, expect_value, timeout=5, fail_if_false=True):
        # verify whether utilization cpu is expected or not.
        # It's hard to validate the graphical bar when utilization is collected for server hardware, so pass
        # 'expect_value' as 'collected' to this function.

        # power meter is collected
        if 'collected' == expect_value.lower().strip():
            # return true if the utilization graphical bar is visible
            return ui_lib.is_visible(UtilizationElements.ID_TEXT_UTI_COLLECTED_CPU, timeout)

        # power meter is not collected
        actual_value = FusionUIBase.get_text(UtilizationElements.ID_TEXT_UTI_NOTCOLLECTED_CPU,
                                             timeout,
                                             fail_if_false)
        if actual_value == expect_value:
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_utilization_power(cls, expect_value, timeout=5, fail_if_false=True):
        # verify whether utilization power is expected or not.
        # It's hard to validate the graphical bar when utilization is collected for server hardware, so pass
        # 'expect_value' as 'collected' to this function.

        # power meter is collected
        if 'collected' == expect_value.lower().strip():
            # return true if the utilization graphical bar is visible
            return ui_lib.is_visible(UtilizationElements.ID_TEXT_UTI_COLLECTED_POWER, timeout)

        # power meter is not collected
        actual_value = FusionUIBase.get_text(UtilizationElements.ID_TEXT_UTI_NOTCOLLECTED_POWER,
                                             timeout,
                                             fail_if_false)
        if actual_value == expect_value:
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_utilization_temperature(cls, expect_value, timeout=5, fail_if_false=True):
        # verify whether utilization power is expected or not.
        # It's hard to validate the graphical bar when utilization is collected for server hardware, so pass
        # 'expect_value' as 'collected' to this function.

        # power meter is collected
        if 'collected' == expect_value.lower().strip():
            # return true if the utilization graphical bar is visible
            return ui_lib.is_visible(UtilizationElements.ID_TEXT_UTI_COLLECTED_TEMPERATURE, timeout)

        # power meter is not collected
        actual_value = FusionUIBase.get_text(UtilizationElements.ID_TEXT_UTI_NOTCOLLECTED_TEMPERATURE,
                                             timeout,
                                             fail_if_false)
        if actual_value == expect_value:
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_hardware_is_monitored_by_own(cls, timeout=40, fail_if_false=True):
        # Verify the error message when server is already monitored by own
        ui_lib.wait_for_element_visible(AddServerHardwareElements.ID_ERR_MSG_ALREADY_MONITORED,
                                        timeout, fail_if_false=True)
        if not ui_lib.is_visible(AddServerHardwareElements.ID_ERR_MSG_ALREADY_MONITORED, timeout):
            return False
        else:
            return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_hardware_minimum_supported_ilo4(cls, timeout=40, fail_if_false=True):
        # Verify the error message when iLO4 is below than minimum supported version
        ui_lib.wait_for_element_visible(AddServerHardwareElements.ID_ERR_MSG_MINIMUM_FW_ILO4,
                                        timeout, fail_if_false=True)
        if not ui_lib.is_visible(AddServerHardwareElements.ID_ERR_MSG_MINIMUM_FW_ILO4, timeout):
            return False
        else:
            return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_hardware_minimum_supported_ilo3(cls, timeout=40, fail_if_false=True):
        # Verify the error message when iLO4 is below than minimum supported version
        ui_lib.wait_for_element_visible(AddServerHardwareElements.ID_ERR_MSG_MINIMUM_FW_ILO3,
                                        timeout, fail_if_false=True)
        if not ui_lib.is_visible(AddServerHardwareElements.ID_ERR_MSG_MINIMUM_FW_ILO3, timeout):
            return False
        else:
            return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_hardware_minimum_supported_ilo2(cls, timeout=40, fail_if_false=True):
        # Verify the error message when iLO4 is below than minimum supported version
        ui_lib.wait_for_element_visible(AddServerHardwareElements.ID_ERR_MSG_MINIMUM_FW_ILO2,
                                        timeout, fail_if_false=True)
        if not ui_lib.is_visible(AddServerHardwareElements.ID_ERR_MSG_MINIMUM_FW_ILO2, timeout):
            return False
        else:
            return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_hardware_monitor_already_managed(cls, timeout=40, fail_if_false=True):
        # Verify the error message when trying to monitor a server which is already being managed
        ui_lib.wait_for_element_visible(AddServerHardwareElements.ID_ERR_MSG_MONITOR_ALREADY_MANAGED,
                                        timeout, fail_if_false=True)
        if not ui_lib.is_visible(AddServerHardwareElements.ID_ERR_MSG_MONITOR_ALREADY_MANAGED, timeout):
            return False
        else:
            return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_hardware_manage_already_managed(cls, timeout=40, fail_if_false=True):
        # Verify the error message when trying to manage a server which is already being managed
        ui_lib.wait_for_element_visible(AddServerHardwareElements.ID_ERR_MSG_MANAGE_ALREADY_MANAGED,
                                        timeout, fail_if_false=fail_if_false)
        if not ui_lib.is_visible(AddServerHardwareElements.ID_ERR_MSG_MANAGE_ALREADY_MANAGED, timeout):
            return False
        else:
            return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_hardware_manage_single_blade(cls, ilo_ip, timeout=40, fail_if_false=True):
        # Verify the error message when trying to manage a single blade server which is part of an enclosure
        locator = AddServerHardwareElements.ID_ERR_MSG_MANAGE_SINGLE_BLADE.format(ilo_ip)
        if ui_lib.wait_for_element_visible(locator, timeout=timeout, fail_if_false=fail_if_false) is False:
            logger.warn("below xpath of the expected error message for server '%s' is not verified VISIBLE within %s second(s):\n[ %s ]" % (ilo_ip, timeout, locator))
            return False
        else:
            logger.debug("below xpath of the expected error message for server '%s' is successfully verified VISIBLE within %s second(s):\n[ %s ]" % (ilo_ip, timeout, locator))
            return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_power_on_button_available(cls, timeout=5, fail_if_false=True):
        CommonOperationServerHardware.click_action_button(timeout=timeout)
        if ui_lib.wait_for_element_visible(PowerOnHardwareElements.ID_SELECT_ACTION_POWER_ON, timeout=timeout, fail_if_false=fail_if_false) is True:
            logger.debug("'Power on' button is successfully verified as VISIBLE within %s seconds, '%s' returns TRUE" % (timeout, sys._getframe().f_code.co_name))
            return True
        else:
            logger.warn("'Power on' button is NOT verified as VISIBLE within %s seconds, '%s' returns FALSE" % (timeout, sys._getframe().f_code.co_name))
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_power_off_button_available(cls, timeout=5, fail_if_false=True):

        if ui_lib.wait_for_element_visible(PowerOffHardwareElements.ID_SELECT_ACTION_POWER_OFF, timeout=timeout, fail_if_false=fail_if_false) is True:
            logger.debug("'Power off' button is successfully verified as VISIBLE within %s seconds, '%s' returns TRUE" % (timeout, sys._getframe().f_code.co_name))
            return True
        else:
            logger.warn("'Power off' button is NOT verified as VISIBLE within %s seconds, '%s' returns FALSE" % (timeout, sys._getframe().f_code.co_name))
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_reset_button_available(cls, timeout=5, fail_if_false=True):
        # CommonOperationServerHardware.click_action_button(timeout=timeout)
        locator = ResetHardwareElements.ID_SELECT_ACTION_RESET
        if ui_lib.wait_for_element_visible(locator, timeout=timeout, fail_if_false=fail_if_false) is True:
            logger.debug("'Reset' button is successfully verified as VISIBLE within %s seconds, '%s' returns TRUE" % (timeout, sys._getframe().f_code.co_name))
            return True
        else:
            logger.warn("'Reset' button [%s] is NOT verified as VISIBLE within %s seconds, '%s' returns FALSE" % (locator, timeout, sys._getframe().f_code.co_name))
            BuiltIn().sleep(60)
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_power_on_button_not_available(cls, timeout=5, fail_if_false=True):
        # CommonOperationServerHardware.click_action_button(timeout=timeout)
        if ui_lib.wait_for_element_notvisible(PowerOnHardwareElements.ID_SELECT_ACTION_POWER_ON, timeout=timeout, fail_if_false=fail_if_false) is True:
            logger.debug("'Power on' button is successfully verified as INVISIBLE within %s seconds, '%s' returns TRUE" % (timeout, sys._getframe().f_code.co_name))
            return True
        else:
            logger.warn("'Power on' button is NOT verified as INVISIBLE within %s seconds, '%s' returns FALSE" % (timeout, sys._getframe().f_code.co_name))
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_power_off_button_not_available(cls, timeout=5, fail_if_false=True):
        # CommonOperationServerHardware.click_action_button(timeout=timeout)
        if ui_lib.wait_for_element_notvisible(PowerOffHardwareElements.ID_SELECT_ACTION_POWER_OFF, timeout=timeout, fail_if_false=fail_if_false) is True:
            logger.debug("'Power off' button is successfully verified as INVISIBLE within %s seconds, '%s' returns TRUE" % (timeout, sys._getframe().f_code.co_name))
            return True
        else:
            logger.warn("'Power off' button is NOT verified as INVISIBLE within %s seconds, '%s' returns FALSE" % (timeout, sys._getframe().f_code.co_name))
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_reset_button_not_available(cls, timeout=5, fail_if_false=True):
        # CommonOperationServerHardware.click_action_button(timeout=timeout)
        if ui_lib.wait_for_element_notvisible(ResetHardwareElements.ID_SELECT_ACTION_RESET, timeout=timeout, fail_if_false=fail_if_false) is True:
            logger.debug("'Reset' button is successfully verified as INVISIBLE within %s seconds, '%s' returns TRUE" % (timeout, sys._getframe().f_code.co_name))
            return True
        else:
            logger.warn("'Reset' button is NOT verified as INVISIBLE within %s seconds, '%s' returns FALSE" % (timeout, sys._getframe().f_code.co_name))
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_create_profile_link_available(cls, timeout=5, fail_if_false=True):
        logger.debug("verify that 'Server profile' should contain 'Create profile' link ...")
        text_server_profile = FusionUIBase.get_text(GeneralServerHardwareElements.ID_TEXT_HARDWARE_SERVER_PROFILE, timeout=timeout, fail_if_false=fail_if_false).strip()
        if 'create profile' in text_server_profile.lower():
            logger.debug("'Server profile' displays '%s', '%s' returns TRUE" % (text_server_profile, sys._getframe().f_code.co_name))
            return True
        else:
            logger.warn("'Server profile' does NOT display 'Create profile' but '%s', '%s' returns FALSE" % (text_server_profile, sys._getframe().f_code.co_name))
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_power_on_error_visible_during_deleting_profile(cls, timeout=5, fail_if_false=True):
        logger.debug("verify that an error message 'The power operation is not allowed while configuration changes for server profile xxx are being made.' "
                     "should occur when powering on a server during its server profile is being deleted ...")
        locator = PowerOnHardwareElements.ID_ERROR_MSG_POWER_ON_DURING_DELETING_PROFILE
        if ui_lib.wait_for_element_visible(locator, timeout=timeout, fail_if_false=fail_if_false) is True:
            logger.debug("-------- element for expected error message found by xpath '%s'" % locator)
            text = FusionUIBase.get_multi_elements_text(locator)
            search = []
            search.append({'ERROR_MSG': "The power operation is not allowed while configuration changes for server profile",
                           'CAPTURED': False})
            search.append({'ERROR_MSG': "are being made.",
                           'CAPTURED': False})
            search.append({'ERROR_MSG': "Resolution:",
                           'CAPTURED': False})
            search.append({'ERROR_MSG': "Try the operation later after the profile configuration has completed.",
                           'CAPTURED': False})

            # captured = [False] * len(search)

            # logger.debug("___<%s>_____" % text)

            for s in search:
                if s['ERROR_MSG'] in str(text):
                    s['CAPTURED'] = True

            logger.debug("-------- search is '%s'" % search)

            if all([s['CAPTURED'] for s in search]) is True:
                logger.debug("-------- all expected error message is found!\n"
                             "-------- comparison result: \n"
                             "-------- '%s', \n"
                             "-------- function '%s' returns TRUE" % (repr(search).replace('},', '},\n-------- '), sys._getframe().f_code.co_name))
                return True
            else:
                # why logger.warn not working? no anything output?
                # logger.warn("not all expected error message is found!\n"
                logger.debug("-------- not all expected error message is found!\n"
                             "-------- comparison result: \n'"
                             "-------- %s', \n"
                             "-------- function '%s' returns FALSE" % (repr(search).replace('},', '},\n-------- '), sys._getframe().f_code.co_name))
                return False
        else:
            msg = "-------- expected error message element NOT found with xpath %s, function '%s' returns FALSE" % (locator, sys._getframe().f_code.co_name)
            logger.debug(msg)
            # logger.warn(msg)
            if fail_if_false is True:
                ui_lib.fail_test(msg)
            else:
                return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_create_profile_link_not_available(cls, timeout=5, fail_if_false=True):
        logger.debug("verify that 'Server profile' should NOT contain 'Create profile' link ...")
        text_server_profile = FusionUIBase.get_text(GeneralServerHardwareElements.ID_TEXT_HARDWARE_SERVER_PROFILE, timeout=timeout, fail_if_false=fail_if_false).strip()
        if 'create profile' not in text_server_profile.lower():
            logger.debug("'Server profile' displays '%s', '%s' returns TRUE" % (text_server_profile, sys._getframe().f_code.co_name))
            return True
        else:
            logger.warn("'Server profile' displays '%s', '%s' returns FALSE" % (text_server_profile, sys._getframe().f_code.co_name))
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_server_profile_displayed_as_na(cls, timeout=5, fail_if_false=True):
        logger.debug("verify that 'Server profile' should contain 'n/a' ...")
        text_server_profile = FusionUIBase.get_text(GeneralServerHardwareElements.ID_TEXT_HARDWARE_SERVER_PROFILE, timeout=timeout, fail_if_false=fail_if_false).strip()
        if 'n/a' in text_server_profile.lower():
            logger.debug("'Server profile' displays '%s', '%s' returns TRUE" % (text_server_profile, sys._getframe().f_code.co_name))
            return True
        else:
            logger.warn("'Server profile' does NOT display 'n/a' but '%s', '%s' returns FALSE" % (text_server_profile, sys._getframe().f_code.co_name))
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_server_hardware_not_selectable_when_creating_profile(cls, server_name, timeout=5, fail_if_false=True):
        from FusionLibrary.ui.business_logic.base import SectionType
        from FusionLibrary.ui.business_logic.servers.serverprofiles import CreateServerProfile

        FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
        CreateServerProfile.click_create_profile_button(timeout=timeout, fail_if_false=fail_if_false)
        CreateServerProfile.wait_create_server_profile_dialog_shown(timeout=timeout, fail_if_false=fail_if_false)
        CreateServerProfile.click_server_hardware_search_combo(timeout=timeout, fail_if_false=fail_if_false)
        if CreateServerProfile.wait_server_hardware_not_visible(server_name=server_name, timeout=timeout, fail_if_false=fail_if_false) is True:
            logger.debug("server hardware '%s' is successfully verified as INVISIBLE in drop-down list within %s seconds, function '%s' returns TRUE" % (server_name, timeout, sys._getframe().f_code.co_name))
            CreateServerProfile.click_cancel_button()
            return True
        else:
            logger.warn("server hardware '%s' is NOT verified as INVISIBLE in drop-down list within %s seconds, function '%s' returns FALSE" % (server_name, timeout, sys._getframe().f_code.co_name))
            CreateServerProfile.click_cancel_button()
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_server_hardware_not_selectable_when_editing_profile(cls, server_name, profile_name, timeout=5, fail_if_false=True):
        from FusionLibrary.ui.business_logic.base import SectionType
        from FusionLibrary.ui.business_logic.servers.serverprofiles import CommonOperationServerProfile
        from FusionLibrary.ui.business_logic.servers.serverprofiles import EditServerProfile
        from FusionLibrary.ui.business_logic.servers.serverprofiles import VerifyServerProfile

        FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

        if VerifyServerProfile.verify_server_profile_exist(profile_name, fail_if_false=False) is False:
            logger.warn("server profile '%s' does not exist" % profile_name)
            return False

        CommonOperationServerProfile.click_server_profile(profile_name=profile_name, timeout=timeout, time_for_loading=3, fail_if_false=fail_if_false)
        EditServerProfile.select_action_edit(timeout=timeout, fail_if_false=fail_if_false)
        EditServerProfile.wait_edit_server_profile_dialog_shown(timeout=timeout, fail_if_false=fail_if_false)
        BuiltIn().sleep(2)
        EditServerProfile.click_server_hardware_search_combo(timeout=timeout, fail_if_false=fail_if_false)
        if EditServerProfile.wait_server_hardware_not_visible(server_name=server_name, timeout=timeout, fail_if_false=fail_if_false) is True:
            logger.debug("server hardware '%s' is successfully verified as INVISIBLE in drop-down list within %s seconds, function '%s' returns TRUE" % (server_name, timeout, sys._getframe().f_code.co_name))
            EditServerProfile.click_cancel_button()
            return True
        else:
            logger.warn("server hardware '%s' is NOT verified as INVISIBLE in drop-down list within %s seconds, function '%s' returns TRUE" % (server_name, timeout, sys._getframe().f_code.co_name))
            EditServerProfile.click_cancel_button()
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_scope_should_exist(cls, name, timeout=5, fail_if_false=True):
        logger.debug("verify [ scope '%s' ] exist in scopes view" % name)
        return ui_lib.wait_for_element_visible(GeneralServerHardwareElements.ID_TEXT_SCOPE % name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_scope_should_not_exist(cls, name, timeout=5, fail_if_false=True):
        logger.debug("verify [ scope '%s' ] not exist in scopes view" % name)
        return ui_lib.wait_for_element_notvisible(GeneralServerHardwareElements.ID_TEXT_SCOPE % name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_scope_should_exist_in_edit_page(cls, name, timeout=5, fail_if_false=False):
        logger.debug("verify [ scope '%s' ] exist in scope edit page" % name)
        return ui_lib.wait_for_element_visible(EditScopeElements.ID_TABLE_SCOPE_NAME % name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_hardware_no_license_info(cls, license_info):
        logger.debug("verify [ license info '%s' ] not exist in server hardware page" % license_info)
        return not ui_lib.page_contains(license_info)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_add_server_hardware_button_notvisible(cls, timeout=5, fail_if_false=True):
        logger.debug("Verifying Add server hardware button not exists")
        return ui_lib.wait_for_element_notvisible(AddServerHardwareElements.ID_BUTTON_ADD_SERVER_HARDWARE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_actions_noauthorization(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("Verifying for 'user authorization' ...\nExpected message: '%s'" % expect_value)
        return FusionUIBase.verify_element_text("Actions", VerifyHardwareElements.ID_TEXT_ACTION_NO_AUTHORIZATION, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_actions_add(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ Add ] item in [ Action ] menu")
        return ui_lib.wait_for_element_visible(AddServerHardwareElements.ID_SELECT_ACTION_ADD, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_activity_contains_subtask(cls, subtask, source, status, timeout=5, fail_if_false=True):
        logger.debug("Verifying sub task '%s' from '%s' is in '%s' status" % (subtask, source, status))
        return ui_lib.wait_for_element(GeneralServerHardwareElements.ID_TEXT_ACTIVITY_SUB_TASK % (status, subtask, source), timeout, fail_if_false)


class EditScopeForHardwares(object):

    """
    This class holds all edit scope operation of enclosure
    It can work with C7000 & TBird
    """

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_edit_scope_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Click [ Edit ] button on server hardware scope page")
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
        logger.debug("click scope name '%s'" % name)
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_TABLE_SCOPE_NAME % name, wait_timeout, fail_if_false=True)

    @classmethod
    def click_remove_scope_icon(cls, name, wait_timeout=5):
        logger.debug("click to remove scope '%s'" % name)
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_TABLE_REMOVE_SCOPE % name, wait_timeout, fail_if_false=True)

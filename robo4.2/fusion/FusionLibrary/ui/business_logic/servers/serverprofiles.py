# -*- coding: UTF-8 -*-
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.servers.serverprofiles_elements import GeneralServerProfilesElements
from FusionLibrary.ui.business_logic.servers.serverprofiles_elements import ServerProfilesPage
from FusionLibrary.ui.business_logic.servers.serverprofiles_elements import CreateServerProfilesElements
from FusionLibrary.ui.business_logic.servers.serverprofiles_elements import EditServerProfilesElements
from FusionLibrary.ui.business_logic.servers.serverprofiles_elements import CopyServerProfilesElements
from FusionLibrary.ui.business_logic.servers.serverprofiles_elements import DeleteServerProfilesElements
from FusionLibrary.ui.business_logic.servers.serverprofiles_elements import PowerOnServerProfilesElements
from FusionLibrary.ui.business_logic.servers.serverprofiles_elements import PowerOffServerProfilesElements
from FusionLibrary.ui.business_logic.servers.serverprofiles_elements import ResetServerProfilesElements
from FusionLibrary.ui.business_logic.storage.drive_enclosures_elements import DriveEnclosuresElements
from FusionLibrary.ui.business_logic.base import FusionUIBase, FusionUIConst, TakeScreenShotWhenReturnFalseDeco
from RoboGalaxyLibrary.utilitylib import logging as logger
from datetime import datetime
from RoboGalaxyLibrary import BuiltIn
from HTMLParser import HTMLParser
import xml.dom.minidom
import sys
import re
import json


class _BaseCommonOperationServerProfile(object):

    """
    This class holds all common operation of server profile.
    It also defines abstract methods which the subclass has different implementation for C7000 & TBird
    """
    html = HTMLParser()

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_dialog_title(cls, timeout=5, fail_if_false=True):
        logger.debug("get Server Profile dialog's title (one of 'Create Server Profile / Edit / Copy / Delete') ... ")
        return ui_lib.get_text(GeneralServerProfilesElements.ID_DIALOG_DETAILS_TITLE, timeout=timeout, fail_if_false=fail_if_false, hidden_element=False)

    @classmethod
    def get_server_profile_action(cls, timeout=5, fail_if_false=True):
        logger.debug("get the action of server profile, should be one of 'CREATE', 'EDIT', 'COPY', and 'DELETE' ...")
        dialog_title = cls.get_dialog_title(timeout=timeout, fail_if_false=fail_if_false)
        if 'CREATE' in dialog_title.upper():
            action = 'CREATE'
        elif 'EDIT' in dialog_title.upper():
            action = 'EDIT'
        elif 'COPY' in dialog_title.upper():
            action = 'COPY'
        elif 'DELETE' in dialog_title.upper():
            action = 'DELETE'
        else:
            action = None
        if action is None:
            msg = "failed to get the action type of Server Profile from the dialog title: <%s>" % dialog_title
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)
        else:
            logger.debug("got server profile action as: <%s> according to the dialog title: <%s>" % (action, dialog_title))
            return action

    @classmethod
    def get_server_hardware_of_server_profile(cls, profile_name, timeout=5, fail_if_false=True):
        logger.debug("get server hardware of server profile '%s'" % profile_name)
        FusionUIBase.select_view_by_name('General')
        return FusionUIBase.get_text(GeneralServerProfilesElements.ID_TEXT_GENERAL_SERVER_HARDWARE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_server_hardware_type_of_server_profile(cls, profile_name, timeout=5, fail_if_false=True):
        logger.debug("get server hardware type of server profile '%s'" % profile_name)
        FusionUIBase.select_view_by_name('General')
        return FusionUIBase.get_text(GeneralServerProfilesElements.ID_TEXT_GENERAL_SERVER_HARDWARE_TYPE, timeout, fail_if_false)

    @classmethod
    def select_overview_view(cls):
        logger.debug("change to 'Overview' view ...")
        FusionUIBase.select_view_by_name('Overview')

    @classmethod
    def select_general_panel(cls):
        logger.debug("change to 'General' view ...")
        FusionUIBase.select_view_by_name('General')

    @classmethod
    def select_firmware_panel(cls):
        logger.debug("change to 'General' view ...")
        FusionUIBase.select_view_by_name('General')

    @classmethod
    def select_connections_panel(cls):
        logger.debug("change to 'Connections' view ...")
        FusionUIBase.select_view_by_name('Connections')

    @classmethod
    def select_local_storage_panel(cls):
        logger.debug("change to 'Local Storage' view ...")
        FusionUIBase.select_view_by_name('Local Storage')

    @classmethod
    def select_san_storage_panel(cls):
        logger.debug("change to 'SAN Storage' view ...")
        FusionUIBase.select_view_by_name('SAN Storage')

    @classmethod
    def select_boot_settings_panel(cls):
        logger.debug("change to 'Boot Settings' view ...")
        FusionUIBase.select_view_by_name('Boot Settings')

    @classmethod
    def select_bios_settings_panel(cls):
        logger.debug("change to 'BIOS Settings' view ...")
        FusionUIBase.select_view_by_name('BIOS Settings')

    @classmethod
    def select_advanced_panel(cls):
        logger.debug("change to 'Advanced' view ...")
        FusionUIBase.select_view_by_name('Advanced')

    @classmethod
    def select_activity_panel(cls):
        logger.debug("change to 'Activity' view ...")
        FusionUIBase.select_view_by_name('Activity')

    @classmethod
    def select_map_panel(cls):
        logger.debug("change to 'Map' view ...")
        FusionUIBase.select_view_by_name('Map')

    @classmethod
    def select_labels_panel(cls):
        logger.debug("change to 'Labels' view ...")
        FusionUIBase.select_view_by_name('Labels')

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_server_profile_task_complete(cls, timeout=3600, fail_if_false=False):
        logger.debug("wait for all profiles task reach the end state")
        if not ui_lib.wait_for_element_notvisible(GeneralServerProfilesElements.ID_ICON_PROFILE_TASK_RUNNING, timeout=timeout, fail_if_false=fail_if_false):
            logger.warn("Failed to wait for all profiles task reach the end state in %ss", str(timeout))
            return False
        return True

    @classmethod
    def get_server_profile_list(cls, timeout=5, fail_if_false=True):
        logger.debug("Get all server profile names from table")
        server_profile_list = []
        if ui_lib.wait_for_element(GeneralServerProfilesElements.ID_TABLE_SERVER_PROFILE_LIST):
            server_profile_list = FusionUIBase.get_multi_elements_text(GeneralServerProfilesElements.ID_TABLE_SERVER_PROFILE_LIST, timeout=timeout, fail_if_false=fail_if_false)
        return server_profile_list

    @classmethod
    def click_server_profile(cls, profile_name, timeout=5, time_for_loading=3, fail_if_false=True):
        logger.debug("select server profile '%s'" % profile_name)
        ui_lib.wait_for_element_and_click(GeneralServerProfilesElements.ID_TABLE_SERVER_PROFILE % profile_name, timeout=timeout, fail_if_false=fail_if_false)
        BuiltIn().sleep(time_for_loading)

    @classmethod
    def click_activity_collapser(cls, activity_name, timeout=10, fail_if_false=True):
        logger.debug("click to expand activity '%s'" % activity_name)
        ui_lib.wait_for_element_and_click(GeneralServerProfilesElements.ID_ICON_ACTIVITY_COLLAPSER % activity_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_server_profile_selected(cls, profile_name, timeout=5, fail_if_false=True):
        logger.debug("wait server profile '%s' selected" % profile_name)
        if ui_lib.wait_for_element_visible(GeneralServerProfilesElements.ID_TABLE_SERVER_PROFILE_SELECTED % profile_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("server profile '%s' is successfully selected" % profile_name)
            return True
        else:
            msg = "failed to wait for server profile '%s' to be selected" % profile_name
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_server_profile_power_state_loaded(cls, timeout=10, fail_if_false=True):
        logger.debug("wait server profile power status loaded complete")
        if ui_lib.wait_for_element_visible(GeneralServerProfilesElements.ID_LABEL_SERVER_POWER, timeout=timeout, fail_if_false=fail_if_false):
            return ui_lib.wait_for_element_notvisible(GeneralServerProfilesElements.ID_TEXT_SERVER_POWER_UNSET, timeout=timeout, fail_if_false=fail_if_false)
        else:
            logger.warn("Cannot find server power label!")
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_to_show_server_profile_error_details(cls, profile_name, timeout=5, fail_if_false=True):
        logger.info("try to showing error details in server profile '%s' page" % profile_name)
        if ui_lib.wait_for_element_and_click(ServerProfilesPage.ID_ERROR_WARN_MSG, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("Correctly to show the error details for server profile '%s'" % profile_name)
            return True
        else:
            msg = "Failed to show the error error details for server profile '%s'" % profile_name
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_server_profile_error_details(cls, profile_name, timeout=5, fail_if_false=True):
        logger.info("get error details from server profile '%s'" % profile_name)
        return ui_lib.get_text(ServerProfilesPage.ID_ERROR_WARN_DETAILS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_server_profile_show_not_found(cls, profile_name, timeout=5, fail_if_false=True):
        logger.info("wait server profile status change to 'not found'")
        if ui_lib.wait_for_element_visible(GeneralServerProfilesElements.ID_TABLE_SERVER_PROFILE_DELETED % profile_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("server profile '%s' status successfully changed to 'not found'" % profile_name)
            return True
        else:
            msg = "failed to wait for server profile '%s' status change to 'not found'" % profile_name
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def click_action_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click 'Action' button")
        ui_lib.wait_for_element_and_click(GeneralServerProfilesElements.ID_DROPDOWN_ACTIONS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_server_profile_status_ok(cls, profile_name, timeout=10, fail_if_false=True):
        start = datetime.now()
        logger.debug("waiting server profile '%s' status change to ok" % profile_name)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(cls.html.unescape(GeneralServerProfilesElements.ID_STATUS_SERVER_PROFILE_OK % profile_name), timeout=2, fail_if_false=False):
                logger.debug("server profile '%s' status is ok as expected." % profile_name)
                return True
            elif ui_lib.wait_for_element_visible(cls.html.unescape(GeneralServerProfilesElements.ID_STATUS_SERVER_PROFILE_WARN % profile_name), timeout=2, fail_if_false=False):
                err_msg = "server profile '%s' status is warning not as expected." % profile_name
                return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)
            elif ui_lib.wait_for_element_visible(cls.html.unescape(GeneralServerProfilesElements.ID_STATUS_SERVER_PROFILE_ERROR % profile_name), timeout=2, fail_if_false=False):
                err_msg = "server profile '%s' status is error not as expected." % profile_name
                return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)
            else:
                logger.debug("server profile status is unknown, waiting ...")
                continue
        err_msg = "Timeout to waiting server profile '%s' status change to ok." % profile_name
        return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_server_profile_status_ok_or_warn(cls, profile_name, timeout=10, fail_if_false=True):
        start = datetime.now()
        logger.debug("waiting server profile '%s' status change to ok or warning" % profile_name)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(cls.html.unescape(GeneralServerProfilesElements.ID_STATUS_SERVER_PROFILE_OK % profile_name), timeout=5, fail_if_false=False):
                logger.debug("server profile '%s' status is ok as expected." % profile_name)
                return True
            elif ui_lib.wait_for_element_visible(cls.html.unescape(GeneralServerProfilesElements.ID_STATUS_SERVER_PROFILE_WARN % profile_name), timeout=5, fail_if_false=False):
                logger.debug("server profile '%s' status is warning as expected." % profile_name)
                return True
            elif ui_lib.wait_for_element_visible(cls.html.unescape(GeneralServerProfilesElements.ID_STATUS_SERVER_PROFILE_ERROR % profile_name), timeout=5, fail_if_false=False):
                err_msg = "server profile '%s' status is error not as expected." % profile_name
                return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)
            else:
                logger.debug("server profile '%s' status is unknown, waiting ..." % profile_name)
                continue
        err_msg = "Timeout to waiting server profile '%s' status change to ok or warn." % profile_name
        return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_server_profile_status_error(cls, profile_name, timeout=10, fail_if_false=True):
        start = datetime.now()
        logger.debug("waiting server profile '%s' status change to error" % profile_name)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(cls.html.unescape(GeneralServerProfilesElements.ID_STATUS_SERVER_PROFILE_OK % profile_name), timeout=5, fail_if_false=False):
                err_msg = "server profile '%s' status is ok not as expected." % profile_name
                return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)
            elif ui_lib.wait_for_element_visible(cls.html.unescape(GeneralServerProfilesElements.ID_STATUS_SERVER_PROFILE_WARN % profile_name), timeout=5, fail_if_false=False):
                logger.debug("server profile '%s' status is warning not as expected." % profile_name)
                return False
            elif ui_lib.wait_for_element_visible(cls.html.unescape(GeneralServerProfilesElements.ID_STATUS_SERVER_PROFILE_ERROR % profile_name), timeout=5, fail_if_false=False):
                logger.debug("server profile '%s' status is error as expected." % profile_name)
                return True
            else:
                logger.debug("server profile '%s' status is unknown, waiting ..." % profile_name)
                continue
        err_msg = "Timeout to waiting server profile status change to error."
        return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_general_server_power_turned_on(cls, profile_name, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.ID_TEXT_GENERAL_SERVER_POWER
        start = datetime.now()
        ret = False
        while (datetime.now() - start).total_seconds() < timeout:
            if FusionUIBase.get_text(locator, timeout=timeout, fail_if_false=fail_if_false) == 'On':
                logger.debug("'Server power' of server profile '%s' is turned 'On' as expected" % profile_name)
                ret = True
                break
            else:
                logger.debug("'Server power' of server profile '%s' is not 'On', waiting ..." % profile_name)

        logger.debug("'Server power' of server profile '%s' is not turned 'On' with in %s second(s), waiting ..." % (profile_name, timeout)) if ret is False else None
        return ret

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_general_server_power_turned_off(cls, profile_name, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.ID_TEXT_GENERAL_SERVER_POWER
        start = datetime.now()
        ret = False
        while (datetime.now() - start).total_seconds() < timeout:
            if FusionUIBase.get_text(locator, timeout=timeout, fail_if_false=fail_if_false) == 'Off':
                logger.debug("'Server power' of server profile '%s' is turned 'Off' as expected" % profile_name)
                ret = True
                break
            else:
                logger.debug("'Server power' of server profile '%s' is not 'Off', waiting ..." % profile_name)

        logger.debug("'Server power' of server profile '%s' is not turned 'Off' with in %s second(s), waiting ..." % (profile_name, timeout)) if ret is False else None
        return ret

    @classmethod
    def get_profile_error_message(cls, timeout=5, fail_if_false=True):
        logger.debug("Get error message for server profile")
        return ui_lib.get_text(GeneralServerProfilesElements.ID_TEXT_PROFILE_ERROR, timeout, fail_if_false)

    @classmethod
    class Firmware(object):

        e = GeneralServerProfilesElements.Firmware

        @classmethod
        def set(cls, firmware, timeout=5, fail_if_false=True):
            if getattr(firmware, 'FirmwareBaseline', None) is not None:
                logger.info("selecting 'Firmware baseline ...")
                cls.select_firmware_baseline_by_text(firmware.FirmwareBaseline)
                if firmware.FirmwareBaseline.lower() != 'managed manually':
                    logger.info("setting 'Installation Method' ...")
                    if firmware.InstallationMethod.lower() == 'firmware and os drivers using hpe smart update tools':
                        cls.tick_installation_method_as_firmware_and_os_drivers_using_sut(timeout=timeout, fail_if_false=fail_if_false)
                    elif firmware.InstallationMethod.lower() == 'firmware only using hpe smart update tools':
                        cls.tick_installation_method_as_firmware_only_using_sut(timeout=timeout, fail_if_false=fail_if_false)
                    elif firmware.InstallationMethod.lower() == 'firmware only':
                        cls.tick_installation_method_as_firmware_only(timeout=timeout, fail_if_false=fail_if_false)
                    else:
                        logger.warn("test data for 'Installation Method' might be wrong: '%s'" % firmware.InstallationMethod)
                        return False

                    if getattr(firmware, 'ForceInstallation', 'None').lower() == 'true':
                        cls.tick_firmware_force_installation(timeout=timeout, fail_if_false=fail_if_false)
            else:
                msg = "<test data attribute missing>: test data attribute 'FirmwareBaseline' is NOT found in '<%s>' -- might be not defined, or wrong spelling (case sensitive)" % firmware
                logger.warn(msg)
                if fail_if_false:
                    ui_lib.fail_test(msg)
                else:
                    return False

            return True

        @classmethod
        def select_firmware_baseline_managed_manually(cls, timeout=5, fail_if_false=True):
            logger.debug("select 'Firmware baseline' as 'managed manually' ...")
            cls.select_firmware_baseline_by_text('managed manually', timeout=timeout, fail_if_false=fail_if_false)
            # ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_FIRMWARE_BASELINE, timeout=timeout, fail_if_false=fail_if_false)
            # ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_FIRMWARE_BASELINE_BY_TEXT % 'managed manually', timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def select_firmware_baseline_by_text(cls, firmware_baseline, timeout=5, fail_if_false=True):
            # logger.debug("select 'Firmware baseline' as '%s' ..." % firmware_baseline)
            # ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_FIRMWARE_BASELINE, timeout=timeout, fail_if_false=fail_if_false)
            # ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_FIRMWARE_BASELINE_BY_TEXT % firmware_baseline, timeout=timeout, fail_if_false=fail_if_false)

            logger.debug("validating test data '%s' for 'Firmware baseline' ..." % firmware_baseline)
            if FusionUIBase.is_test_data_valid(firmware_baseline, 'Firmware_Baseline', fail_if_false=False):
                logger.debug("select 'Firmware baseline' as '%s' ..." % firmware_baseline)
                FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_FIRMWARE_BASELINE, firmware_baseline, timeout=timeout, fail_if_false=fail_if_false)
            else:
                msg = "<test data invalid>: '%s' for 'Firmware baseline' is NOT valid" % firmware_baseline
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

            return True

        @classmethod
        def tick_installation_method_as_firmware_and_os_drivers_using_sut(cls, timeout=5, fail_if_false=True):
            logger.debug("set 'Installation Method' as 'Firmware and OS Drivers using HP Smart Update Tools' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_INSTALLATION_METHOD_FW_AND_OS_DRIVERS_USING_SUT, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_installation_method_as_firmware_only_using_sut(cls, timeout=5, fail_if_false=True):
            logger.debug("set 'Installation Method' as 'Firmware only using HP Smart Update Tools' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_INSTALLATION_METHOD_FW_ONLY_USING_SUT, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_installation_method_as_firmware_only(cls, timeout=5, fail_if_false=True):
            logger.debug("set 'Installation Method' as 'Firmware only' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_INSTALLATION_METHOD_FW_ONLY, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_firmware_force_installation(cls, timeout=5, fail_if_false=True):
            logger.debug("turn on 'Force installation' option ...")
            FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_FORCE_INSTALLATION, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def untick_firmware_force_installation(cls, timeout=5, fail_if_false=True):
            logger.debug("turn off 'Force installation' option ...")
            FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_FORCE_INSTALLATION, timeout=timeout, fail_if_false=fail_if_false)

    class Connection(object):

        e = GeneralServerProfilesElements.Connection
        saved_connection_list = []
        used_server = None
        used_eg = None
        sp_action = None

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def verify_connection_exist(cls, connection_name, timeout=5, fail_if_false=True):
            logger.debug("verify connection '%s' is existing" % connection_name)
            if ui_lib.wait_for_element_visible(cls.e.ID_TABLE_CONNECTION % connection_name, timeout=timeout, fail_if_false=fail_if_false):
                logger.debug("connection '%s' is successfully verified as visible within %s second(s)" % (connection_name, timeout))
                return True
            else:
                msg = "connection '%s' is failed to be verified as visible within %s second(s)" % (connection_name, timeout)
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def verify_connection_not_exist(cls, connection_name, timeout=5, fail_if_false=True):
            logger.debug("verify connection '%s' is not existing" % connection_name)
            if ui_lib.wait_for_element_notvisible(cls.e.ID_TABLE_CONNECTION % connection_name, timeout=timeout, fail_if_false=fail_if_false):
                logger.debug("connection '%s' is successfully verified as invisible within %s second(s)" % (connection_name, timeout))
                return True
            else:
                msg = "connection '%s' is failed to be verified as invisible within %s second(s)" % (connection_name, timeout)
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        @classmethod
        def get_saved_connection_list(cls, timeout=5, fail_if_false=True):
            logger.debug("Get all saved connections' names from table")
            saved_connection_list = []
            if ui_lib.wait_for_element(cls.e.ID_TABLE_CONNECTION_LIST):
                logger.debug("'GeneralServerProfilesElements.Connection.ID_TABLE_CONNECTION_LIST' is found: <%s>" % cls.e.ID_TABLE_CONNECTION_LIST)
                saved_connection_list = FusionUIBase.get_multi_elements_text(cls.e.ID_TABLE_CONNECTION_LIST, timeout=timeout, fail_if_false=fail_if_false)
                logger.debug("'saved_connection_list' is retrieved as '<%s>'" % saved_connection_list)
            return saved_connection_list

        @classmethod
        def get_connection_from_connection_view(cls, timeout=5, fail_if_false=True):
            logger.debug("Get all saved connections' names from table")
            saved_connection_list = []
            if ui_lib.wait_for_element(cls.e.ID_TABLE_PROFILE_CONNECTION):
                logger.debug("'GeneralServerProfilesElements.Connection.ID_TABLE_PROFILE_CONNECTION' is found: <%s>" % cls.e.ID_TABLE_PROFILE_CONNECTION)
                saved_connection_list = FusionUIBase.get_multi_elements_text(cls.e.ID_TABLE_PROFILE_CONNECTION, timeout, fail_if_false)
                del saved_connection_list[-1]
                logger.debug("'saved_connection_list' is retrieved as '<%s>'" % saved_connection_list)
            return saved_connection_list

        @classmethod
        def get_connection_port(cls, timeout=5, fail_if_false=True):
            logger.debug("Get connection port")
            return ui_lib.get_multi_elements_text(cls.e.ID_TEXT_CONNECT_PORT, timeout, fail_if_false)

        @classmethod
        def click_expand_connections(cls, i, timeout=5, fail_if_false=False):
            logger.debug("Expand/Close the connection")
            if ui_lib.wait_for_element_visible(cls.e.ID_EXPAND_CONNECTIONS % i, timeout, fail_if_false):
                return ui_lib.wait_for_element_and_click(cls.e.ID_EXPAND_CONNECTIONS % i, timeout, fail_if_false)

        @classmethod
        def get_mac_address(cls, timeout=5, fail_if_false=True):
            logger.debug("Get mac address from connection")
            return ui_lib.get_text(cls.e.ID_TEXT_CONNECT_MAC_ADDRESS, timeout, fail_if_false)

        @classmethod
        def click_add_connection_button(cls, timeout=5):
            logger.debug("click button 'Add Connection'")
            FusionUIBase.scroll_element_into_viewpoint(cls.e.ID_BUTTON_ADD_CONNECTION)
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_CONNECTION, timeout=timeout, fail_if_false=True)

        @classmethod
        def click_yes_remove_button(cls, timeout=5):
            logger.debug("click button 'Yes, Remove'")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_YES_REMOVE, timeout=timeout, fail_if_false=True)

        @classmethod
        def click_cancel_remove_button(cls, timeout=5):
            logger.debug("click button 'Cancel'")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL_REMOVE, timeout=timeout, fail_if_false=True)

        @classmethod
        def click_edit_connection_button(cls, connection_name, timeout=5):
            logger.debug("click button 'Edit' gear of Connection '%s'" % connection_name)
            locator = cls.e.ID_BUTTON_EDIT_CONNECTION % connection_name
            FusionUIBase.scroll_element_into_viewpoint(locator)
            ui_lib.wait_for_element_and_click(locator, timeout=timeout, fail_if_false=True)

        @classmethod
        def click_delete_connection_button(cls, connection_name, timeout=5):
            logger.debug("click button 'Remove' icon of Connection '%s'" % connection_name)
            locator = cls.e.ID_BUTTON_DELETE_CONNECTION % connection_name
            FusionUIBase.scroll_element_into_viewpoint(locator)
            ui_lib.wait_for_element_and_click(locator, timeout=timeout, fail_if_false=True)

        @classmethod
        def set(cls, connections_obj):
            t = cls.get_saved_connection_list()
            cls.saved_connection_list = list(x.strip() for x in t)
            cls.sp_action = _BaseCommonOperationServerProfile.get_server_profile_action()
            if cls.sp_action == 'CREATE':
                cls.used_server = _BaseCreateServerProfile.get_selected_server_hardware()
                cls.used_eg = _BaseCreateServerProfile.get_selected_enclosure_group(server_name=cls.used_server)
            elif cls.sp_action == 'EDIT':
                cls.used_server = _BaseEditServerProfile.get_selected_server_hardware()
                cls.used_eg = _BaseEditServerProfile.get_selected_enclosure_group(server_name=cls.used_server)
            elif cls.sp_action == 'COPY':
                cls.used_server = _BaseCopyServerProfile.get_selected_server_hardware()
                cls.used_eg = _BaseCopyServerProfile.get_selected_enclosure_group(server_name=cls.used_server)

            logger.debug("****** 'cls.saved_connection_list' is: <%s>" % cls.saved_connection_list)
            logger.debug("connections_obj is {%s}" % connections_obj, also_console=False)

            cls.add(connections_obj.Add) if str(getattr(connections_obj, 'Add', [])) != '[]' else None
            cls.edit(connections_obj.Edit) if str(getattr(connections_obj, 'Edit', [])) != '[]' else None
            cls.delete(connections_obj.Delete) if str(getattr(connections_obj, 'Delete', [])) != '[]' else None

        @classmethod
        def add(cls, connections, fail_if_false=True):
            logger.info("change to 'Connections' view ...")
            FusionUIBase.select_view_by_name('Connections')
            logger.info("start adding connections ...")
            total = len(connections)
            added = 0
            already_exists = 0
            for n, connection in enumerate(connections):
                logger.info("--- <connections> ---: {2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
                logger.info("adding a connection with name '%s' ..." % connection.name)
                logger.debug("test data for connection '<%s>' is found: '<%s>'" % (connection.name, connection), also_console=False)
                if cls.verify_connection_not_exist(connection.name, fail_if_false=False) is False:
                    logger.warn("connection '%s' already exists, skipped ..." % connection.name)
                    already_exists += 1
                    continue

                cls.click_add_connection_button()
                cls.wait_add_connection_dialog_shown(time_for_loading=3)

                cls.input_name(connection.name)
                cls.select_function_type_by_text(connection.FunctionType, timeout=10, fail_if_false=True)
                cls.input_select_network(connection.network)
                cls.input_select_port(connection.port)
                if getattr(connection, 'RequestedVirtualFunctions', '').lower() in ('none', 'custom', 'auto'):
                    cls.tick_requested_virtual_functions_as_none() if connection.RequestedVirtualFunctions.lower() == 'none' else None
                    cls.tick_requested_virtual_functions_as_auto() if connection.RequestedVirtualFunctions.lower() == 'auto' else None
                    cls.tick_requested_virtual_functions_as_custom() if connection.RequestedVirtualFunctions.lower() == 'custom' else None
                    cls.input_requested_virtual_functions_custom(connection.CustomValue) if connection.RequestedVirtualFunctions.lower() == 'custom' and hasattr(connection, 'CustomValue') else None
                # cls.input_requested_bandwidth(connection.RequestedBandwidth) if connection.FunctionType.lower() in ('ethernet', 'fibre channel') else None
                # if the <input> type field is visible, then call input_requested_bandwidth
                cls.input_requested_bandwidth(connection.RequestedBandwidth) if ui_lib.is_visible(cls.e.ID_INPUT_REQUESTED_BANDWIDTH) else None
                # cls.select_requested_bandwidth_by_text(connection.RequestedBandwidth) if connection.FunctionType.lower() == 'fibre channel' else None
                # if the <select> type field is visible, then call select_requested_bandwidth_by_text
                cls.select_requested_bandwidth_by_text(connection.RequestedBandwidth) if ui_lib.is_visible(cls.e.ID_SELECTBOX_REQUESTED_BANDWIDTH) else None
                support_boot_select_list = ["Auto", "None", "FlexibleLOM 1:1 (Auto)", "FlexibleLOM 1:2 (Auto)", "FlexibleLOM 1:2-a"]
                if connection.FunctionType.lower() == 'fibre channel' or (connection.port in support_boot_select_list):
                    cls.select_boot_by_text(connection.boot, fail_if_false=True)
                if connection.FunctionType.lower() == 'fibre channel' and connection.boot.lower() != 'not bootable':
                    cls.set_boot_radio_option(connection.BootOption)
                    if connection.BootOption.lower() == 'specify boot target':
                        cls.input_wwpn(connection.WWPN)
                        cls.input_lun(connection.LUN)

                if connection.FunctionType.lower() != 'fibre channel' and (connection.boot.lower() == 'iscsi primary' or connection.boot.lower() == 'iscsi secondary'):
                    cls.set_iscsi_boot_options(connection)

                if getattr(connection, 'UseUserSpecifiedIDs', 'None').lower() == 'true':
                    cls.tick_use_user_specified_ids(connection.UseUserSpecifiedIDs)
                    if connection.FunctionType.lower() == 'fibre channel':
                        cls.input_wwpn_user_specified(connection.WWPN_UserSpecified)
                        cls.input_wwnn_user_specified(connection.WWNN_UserSpecified)
                    if getattr(connection, 'MACAddress_UserSpecified', 'None').lower() != 'none':
                        cls.input_mac_address_user_specified(connection.MACAddress_UserSpecified)
                    else:
                        if connection.FunctionType.lower() == 'ethernet' or connection.FunctionType.lower() == 'iscsi':
                            msg = "<test data missing>: 'MAC address' is required when 'Function Type' = 'Ethernet' or 'iSCSI' and 'Use user-specified IDs' is turned on"
                            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

                cls.click_add_button()
                cls.wait_add_connection_dialog_disappear(timeout=10)

                if cls.verify_connection_exist(connection.name, fail_if_false=False) is False:
                    msg = "failed for adding connection '%s'" % connection.name
                    return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)
                else:
                    logger.info("connection '%s' is successfully added" % connection.name)
                    added += 1

            logger.info("{0} == Summary == {0}".format('-' * 14))
            if total - already_exists == 0:
                logger.warn("no connection to add! all %s connection(s) is already existing, test is considered PASS" % already_exists)
                return True
            else:
                if added < total:
                    logger.warn("not all of the connection(s) is successfully added - %s out of %s added " % (added, total))
                    if added + already_exists == total:
                        logger.warn("%s already existing connection(s) is skipped, test is considered PASS" % already_exists)
                        return True
                    else:
                        logger.warn("%s already existing connection(s) is skipped, %s left is failed being added " % (already_exists, total - added - already_exists))
                        return False

            logger.info("all connection(s) is successfully added - %s out of %s " % (added, total))
            return True

        @classmethod
        def edit(cls, connections, timeout=5, fail_if_false=True):
            logger.info("change to 'Connections' view ...")
            FusionUIBase.select_view_by_name('Connections')
            logger.info("start editing connections ...")
            total = len(connections)
            not_exists = 0
            edited = 0

            for n, connection in enumerate(connections):
                logger.info("--- <connections> ---: {2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
                logger.info("editing a connection with name '%s' ..." % connection.name)
                logger.debug("test data for connection '<%s>' is found: '<%s>'" % (connection.name, connection), also_console=False)
                # verify if connection is existing to edit
                if cls.verify_connection_exist(connection.name, fail_if_false=False) is False:
                    logger.warn("connection '%s' does NOT exist, skipped ..." % connection.name)
                    not_exists += 1
                    continue

                FusionUIBase.scroll_element_into_viewpoint(cls.e.ID_BUTTON_EDIT_CONNECTION % connection.name)

                function_type = getattr(connection, 'FunctionType', '')
                boot = getattr(connection, 'boot', '')
                boot_option = getattr(connection, 'BootOption', '')

                cls.click_edit_connection_button(connection.name, timeout=timeout)
                cls.wait_edit_connection_dialog_shown()
                BuiltIn().sleep(2)
                cls.input_name(connection.newName) if getattr(connection, 'newName', None) is not None else None
                cls.verify_function_type_by_text(connection.FunctionType) if getattr(connection, 'FunctionType', None) is not None else None
                cls.input_select_network(connection.network) if getattr(connection, 'network', None) is not None else None
                cls.input_select_port(connection.port) if getattr(connection, 'port', None) is not None else None
                if getattr(connection, 'RequestedVirtualFunctions', '').lower() in ('none', 'custom', 'auto'):
                    cls.tick_requested_virtual_functions_as_none() if connection.RequestedVirtualFunctions.lower() == 'none' else None
                    cls.tick_requested_virtual_functions_as_auto() if connection.RequestedVirtualFunctions.lower() == 'auto' else None
                    cls.tick_requested_virtual_functions_as_custom() if connection.RequestedVirtualFunctions.lower() == 'custom' else None
                    cls.input_requested_virtual_functions_custom(connection.CustomValue) if connection.RequestedVirtualFunctions.lower() == 'custom' and hasattr(connection, 'CustomValue') else None

                if getattr(connection, 'RequestedBandwidth', None) is not None:
                    cls.input_requested_bandwidth(connection.RequestedBandwidth) if ui_lib.is_visible(cls.e.ID_INPUT_REQUESTED_BANDWIDTH) else None
                    cls.select_requested_bandwidth_by_text(connection.RequestedBandwidth) if ui_lib.is_visible(cls.e.ID_SELECTBOX_REQUESTED_BANDWIDTH) else None
                if not (ui_lib.is_visible(cls.e.ID_TEXT_BOOT_MANAGED_MANUALLY)):
                    cls.select_boot_by_text(connection.boot, fail_if_false=True) if boot is not None else None

                if function_type.lower() == 'fibre channel' and boot.lower() != 'not bootable':
                    cls.set_boot_radio_option(connection.BootOption) if boot_option is not None else None
                    if boot_option.lower() == 'specify boot target':
                        cls.input_wwpn(connection.WWPN) if getattr(connection, 'WWPN', None) is not None else None
                        cls.input_lun(connection.LUN) if getattr(connection, 'LUN', None) is not None else None

                if connection.FunctionType.lower() != 'fibre channel' and (connection.boot.lower() == 'iscsi primary' or connection.boot.lower() == 'iscsi secondary'):
                    cls.set_iscsi_boot_options(connection, timeout)

                logger.debug("****** 'cls.saved_connection_list' is: <%s>" % cls.saved_connection_list)
                if connection.name not in cls.saved_connection_list:
                    # 'connection.name not in cls.saved_connections_list'
                    #       -- means editing a newly added connection during either creating or editing an SP,
                    # then 'Use user-specified IDs' is available
                    if getattr(connection, 'UseUserSpecifiedIDs', '').lower() == 'true':
                        cls.tick_use_user_specified_ids(connection.UseUserSpecifiedIDs)
                        if function_type.lower() == 'fibre channel':
                            cls.input_wwpn_user_specified(connection.WWPN_UserSpecified) if getattr(connection, 'WWPN_UserSpecified', None) is not None else None
                            cls.input_wwnn_user_specified(connection.WWNN_UserSpecified) if getattr(connection, 'WWNN_UserSpecified', None) is not None else None
                        # 'MAC Address (user-specified)' is NOT required when Function Type == Fibre Channel
                        # 'MAC Address (user-specified)' is required when Function Type == Ethernet
                        if getattr(connection, 'MACAddress_UserSpecified', '').lower() != '':
                            cls.input_mac_address_user_specified(connection.MACAddress_UserSpecified)
                        else:
                            if function_type.lower() == 'ethernet':
                                msg = "<test data missing>: 'MAC address' is required when 'Function Type' = 'Ethernet' and 'Use user-specified IDs' is turned on"
                                logger.warn(msg)
                                if fail_if_false:
                                    ui_lib.fail_test(msg)
                                else:
                                    return False

                cls.click_ok_button()
                cls.wait_edit_connection_dialog_disappear(timeout=10)

                if cls.verify_connection_exist(connection.newName if getattr(connection, 'newName', None) is not None else connection.name) is False:
                    msg = "failed to edit connection '%s'" % connection.name
                    logger.warn(msg)
                    if fail_if_false:
                        ui_lib.fail_test(msg)
                    else:
                        return False
                else:
                    logger.info("connection '%s' is successfully edited" % connection.name)
                    edited += 1

            logger.info("{0} == Summary == {0}".format('-' * 14))
            if total - not_exists == 0:
                logger.warn("no connection to edit! all %s connection(s) is NOT existing, test is considered PASS" % not_exists)
                return True
            else:
                if edited < total:
                    logger.warn("not all of the connection(s) is successfully edited - %s out of %s edited" % (edited, total))
                    if edited + not_exists == total:
                        logger.warn("%s not-existing connection(s) is skipped, test is considered PASS" % not_exists)
                        return True
                    else:
                        logger.warn("%s not-existing connection(s) is skipped, %s left is failed being edited" % (not_exists, total - edited - not_exists))
                        return False

            logger.info("all connection(s) is successfully edited - %s out of %s " % (edited, total))
            return True

        @classmethod
        def delete(cls, connections, timeout=5, fail_if_false=True):
            logger.info("change to 'Connections' view ...")
            FusionUIBase.select_view_by_name('Connections')
            logger.info("start deleting connections ...")
            total = len(connections)
            not_exists = 0
            deleted = 0

            for n, connection in enumerate(connections):
                logger.info("--- <delete connection(s)> ---: {2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
                logger.info("deleting volume '%s' ..." % connection.name)
                if cls.verify_connection_exist(connection.name, fail_if_false=False) is False:
                    logger.warn("connection '%s' does NOT exist, skipped ..." % connection.name)
                    not_exists += 1
                    continue

                logger.debug("click delete button for removing connection '%s' ..." % connection.name)
                ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_DELETE_CONNECTION.format(connection.name), timeout=timeout, fail_if_false=fail_if_false)

                if cls.wait_remove_connection_dialog_open() is True:
                    cls.click_yes_remove_button()
                    cls.wait_remove_connection_dialog_closed()

                if cls.verify_connection_not_exist(connection.name, fail_if_false=False) is True:
                    logger.debug("connection '%s' is successfully deleted" % connection.name)
                    deleted += 1
                else:
                    msg = "failed to delete connection '%s'" % connection.name
                    return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

            logger.info("{0} == Summary == {0}".format('-' * 14))
            if total - not_exists == 0:
                logger.warn("no connection to delete! all %s connection(s) is NOT existing, test is considered PASS" % not_exists)
                return True
            else:
                if deleted < total:
                    logger.warn("not all of the connection(s) is successfully deleted - %s out of %s deleted" % (deleted, total))
                    if deleted + not_exists == total:
                        logger.warn("%s not-existing connection(s) is skipped, test is considered PASS" % not_exists)
                        return True
                    else:
                        logger.warn("%s not-existing connection(s) is skipped, %s left is failed being deleted" % (not_exists, total - deleted - not_exists))
                        return False

            logger.info("all connection(s) is successfully deleted - %s out of %s " % (deleted, total))
            return True

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def wait_add_connection_dialog_shown(cls, timeout=5, time_for_loading=0, fail_if_false=True):
            logger.info("waiting for dialog 'Add Connection' to show up ...")
            if ui_lib.wait_for_element_visible(cls.e.ID_ADD_CONNECTION_DIALOG, timeout=timeout, fail_if_false=fail_if_false):
                logger.debug("dialog 'Add Connection' successfully showed up")
                BuiltIn().sleep(time_for_loading)
                return True
            else:
                msg = "failed to wait for dialog 'Add Connection' to show up"
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def wait_add_connection_dialog_disappear(cls, timeout=5, fail_if_false=True):
            logger.info("waiting for dialog 'Add Connection' to disappear ...")
            if ui_lib.wait_for_element_notvisible(cls.e.ID_ADD_CONNECTION_DIALOG, timeout=timeout, fail_if_false=fail_if_false):
                logger.debug("dialog 'Add Connection' successfully disappeared")
                return True
            else:
                msg = "failed to wait for dialog 'Add Connection' to disappear"
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def wait_remove_connection_dialog_open(cls, timeout=5, fail_if_false=False):
            logger.info("waiting for dialog 'Remove Connection' to show up ...")
            return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_REMOVE_CONNECTION, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def wait_remove_connection_dialog_closed(cls, timeout=5, fail_if_false=True):
            logger.info("waiting for dialog 'Remove Connection' to disappear ...")
            return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_REMOVE_CONNECTION, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def wait_edit_connection_dialog_shown(cls, timeout=5, fail_if_false=True):
            logger.info("waiting for dialog 'Edit Connection' to show up ...")
            if ui_lib.wait_for_element_visible(cls.e.ID_EDIT_CONNECTION_DIALOG, timeout=timeout, fail_if_false=fail_if_false):
                logger.debug("dialog 'Edit Connection' successfully showed up")
                return True
            else:
                msg = "failed to wait for dialog 'Edit Connection' to show up"
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def wait_edit_connection_dialog_disappear(cls, timeout=5, fail_if_false=True):
            logger.info("waiting for dialog 'Edit Connection' to disappear ...")
            if ui_lib.wait_for_element_notvisible(cls.e.ID_EDIT_CONNECTION_DIALOG, timeout=timeout, fail_if_false=fail_if_false):
                logger.debug("dialog 'Edit Connection' successfully disappeared")
                return True
            else:
                msg = "failed to wait for dialog 'Edit Connection' to disappear"
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def get_dialog_title(cls, timeout=5, fail_if_false=True):
            logger.debug("get Connection dialog's title ... ")
            return ui_lib.get_text(cls.e.ID_DIALOG_TITLE, timeout=timeout, fail_if_false=fail_if_false, hidden_element=False)

        @classmethod
        def input_name(cls, name, timeout=5):
            logger.debug("input Connection's 'Name' as '%s'" % name)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NAME, name, timeout=timeout, fail_if_false=True)

        @classmethod
        def select_function_type_ethernet(cls, timeout=5, fail_if_false=True):
            cls.select_function_type_by_text('Ethernet', timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def select_function_type_fibre_channel(cls, timeout=5, fail_if_false=True):
            cls.select_function_type_by_text('Fibre Channel', timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def select_function_type_by_text(cls, connection_function_type, timeout=5, fail_if_false=True):
            logger.debug("validating test data '%s' for Connection's 'Function Type' ..." % connection_function_type)
            if FusionUIBase.is_test_data_valid(connection_function_type, 'Connection_Function_Type', fail_if_false=False):
                logger.debug("select Connection's 'Function type' as '%s' ..." % connection_function_type)
                dialog_title = cls.get_dialog_title(timeout=timeout, fail_if_false=fail_if_false)
                ui_lib.fail_test("failed to get current Connection dialog's title") if dialog_title is None else None
                logger.debug("got current Connection dialog's title is <%s>" % dialog_title)
                if VerifyServerProfile.is_connection_function_type_disabled(time_for_loading=3, timeout=5, fail_if_false=True) is True:
                    # when ADD or EDIT a connection, 'Function Type' may be disabled and fixed,
                    # so need to check:
                    #   if Function Type is disabled:
                    #       - the fixed Function Type should be the value provided in data file (FunctionType)
                    #       - if current dialog is ADD CONNECTION:
                    #           - Carbon IC should be included in EG
                    if 'ADD CONNECTION' in dialog_title.upper():
                        # check if Carbon IC is included in EG, and if non-Carbon is included in EG
                        has_carbon, has_non_carbon = FusionUIBase.APIMethods().check_carbon_against_enclosure_group(eg_name=cls.used_eg)
                        if has_carbon:
                            logger.debug('Carbon <%s> found in the used Enclosure Group <%s> of server hardware <%s>' % (FusionUIConst.CONST_CARBON, cls.used_eg, cls.used_server))
                        else:
                            msg = "'Function Type' is disabled, but Carbon <%s> is not found in the used Enclosure Group <%s> of server hardware <%s>, " \
                                  "please check if test data is incorrect or any product issue" % (FusionUIConst.CONST_CARBON, cls.used_eg, cls.used_server)
                            ui_lib.fail_test(msg)

                    elif 'EDIT CONNECTION' in dialog_title.upper():
                        logger.debug("'Edit Connection' found in the title of current dialog, only need to verify the selected 'Function Type' is same as test data <%s>" % connection_function_type)

                    cls.verify_function_type_by_text(connection_function_type, timeout=timeout)
                else:
                    FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_FUNCTION_TYPE, connection_function_type, timeout=timeout, fail_if_false=fail_if_false)

            else:
                msg = "<test data invalid> '%s' for Connection's 'Function Type' is NOT valid" % connection_function_type
                return FusionUIBase.fail_test_or_return_false(msg)

            return True

        @classmethod
        def verify_function_type_by_text(cls, connection_function_type, timeout=5):
            logger.debug("validating test data '%s' for Connection's 'Function Type' ..." % connection_function_type)
            if FusionUIBase.is_test_data_valid(connection_function_type, 'Connection_Function_Type',
                                               fail_if_false=True):
                logger.debug("Verifying Connection's 'Function type' is '%s' ..." % connection_function_type)
                ui_lib.wait_for_element_visible(cls.e.ID_TEXT_FUNCTION_TYPE % connection_function_type, timeout=timeout, fail_if_false=True)

        @classmethod
        def input_network(cls, network_name, timeout=5, fail_if_false=True):
            logger.debug("input Connection's 'Network' as '%s'" % network_name)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NETWORK, network_name, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def input_select_network(cls, network_name, timeout=5, fail_if_false=True):
            logger.debug("input and select Connection's 'Network' as '%s'" % network_name)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NETWORK, network_name, timeout=timeout, fail_if_false=fail_if_false)
            if ui_lib.is_visible(cls.e.ID_OPTION_NETWORK):
                ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_NETWORK, timeout=timeout, fail_if_false=fail_if_false)
                return True
            else:
                return ui_lib.is_visible(cls.e.ID_OPTION_NETWORK, fail_if_false)

        @classmethod
        def input_port(cls, port, timeout=5):
            logger.debug("input Connection's 'Port' as '%s'" % port)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_PORT, port, timeout=timeout, fail_if_false=True)

        @classmethod
        def input_select_port(cls, port, timeout=5, fail_if_false=True):
            logger.debug("input and select Connection's 'Port' as '%s'" % port)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_PORT, port, timeout=timeout, fail_if_false=fail_if_false)
            if ui_lib.is_visible(cls.e.ID_OPTION_PORT % port):
                ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_PORT % port, timeout=timeout, fail_if_false=fail_if_false)
                return True
            else:
                msg = "No port named '%s' for adding connection" % port
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        @classmethod
        def tick_requested_virtual_functions_as_none(cls, timeout=5, fail_if_false=True):
            logger.debug("tick 'Requested virtual functions' type as 'None'")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_REQUESTED_VIRTUAL_FUNCTIONS_NONE, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_requested_virtual_functions_as_auto(cls, timeout=5, fail_if_false=True):
            logger.debug("tick 'Requested virtual functions' type as 'Auto'")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_REQUESTED_VIRTUAL_FUNCTIONS_AUTO, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_requested_virtual_functions_as_custom(cls, timeout=5, fail_if_false=True):
            logger.debug("tick 'Requested virtual functions' type as 'Custom'")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_REQUESTED_VIRTUAL_FUNCTIONS_CUSTOM, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def input_requested_virtual_functions_custom(cls, custom_value, timeout=5):
            logger.debug("input Connection's 'Requested virtual functions' Custom value  as '%s'" % custom_value)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_REQUESTED_VIRTUAL_FUNCTIONS_CUSTOM, custom_value, timeout=timeout, fail_if_false=True)

        @classmethod
        def input_requested_bandwidth(cls, bandwidth, timeout=5):
            logger.debug("input Connection's 'Requested bandwidth (Gb/s)' as '%s'" % bandwidth)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_REQUESTED_BANDWIDTH, bandwidth, timeout=timeout, fail_if_false=True)

        @classmethod
        def select_requested_bandwidth_by_text(cls, bandwidth, timeout=5, fail_if_false=True):
            logger.debug("validating test data '%s' for Connection's 'Requested bandwidth (Gb/s)' ..." % bandwidth)
            if FusionUIBase.is_test_data_valid(bandwidth, 'Connection_Requested_Bandwidth', fail_if_false=False):
                logger.debug("select Connection's 'Requested bandwidth (Gb/s)' as '%s' ..." % bandwidth)
                FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_REQUESTED_BANDWIDTH, bandwidth, timeout=timeout)
            else:
                msg = "<test data invalid> '%s' for Connection's 'Requested bandwidth (Gb/s) ' is NOT valid" % bandwidth
                return FusionUIBase.fail_test_or_return_false(msg)

        @classmethod
        def select_boot_not_bootable(cls, timeout=5, fail_if_false=True):
            cls.select_boot_by_text('Not bootable', timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def select_boot_primary(cls, timeout=5, fail_if_false=True):
            cls.select_boot_by_text('Primary', timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def select_boot_secondary(cls, timeout=5, fail_if_false=True):
            cls.select_boot_by_text('Secondary', timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def select_boot_by_text(cls, connection_boot, timeout=5, fail_if_false=True):
            logger.debug("validating test data '%s' for Connection's 'Boot' ..." % connection_boot)
            if FusionUIBase.is_test_data_valid(connection_boot, 'Connection_Boot', fail_if_false=False):
                logger.debug("select Connection's 'Boot' as '%s' ..." % connection_boot)
                FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_BOOT, connection_boot, timeout=timeout)
            else:
                msg = "<test data invalid> '%s' for Connection's 'Boot' is NOT valid" % connection_boot
                return FusionUIBase.fail_test_or_return_false(msg)

        @classmethod
        def set_boot_radio_option(cls, connection_boot_option, timeout=5):
            logger.debug("validating test data '%s' for Connection's 'Boot option (radio button)' ..." % connection_boot_option)
            logger.debug("select Connection's 'Boot' as '%s' ..." % connection_boot_option)
            if connection_boot_option.lower() == 'managed volume':
                cls.tick_managed_volume(timeout=timeout)
            elif connection_boot_option.lower() == 'specify boot target':
                cls.tick_specify_boot_target(timeout=timeout)
            elif connection_boot_option.lower() == 'use adapter bios':
                cls.tick_use_adapter_bios(timeout=timeout)
            elif connection_boot_option.lower() == 'profile initiator name':
                cls.tick_profile_initiator_name(timeout=timeout)
            elif connection_boot_option.lower() == 'user specified':
                cls.tick_user_specified_initiator_name(timeout=timeout)
            else:
                msg = "<test data issue>: '%s' for Connection's 'Boot option (radio button)' is NOT in ('Specify boot target', 'Use Adapter BIOS'), " \
                      "it might be a newly added item, which is already defined in FusionUITestDataValidate.ReferenceData but keyword's coding is not yet updated as well. test will be failed" % connection_boot_option
                logger.warn(msg)
                ui_lib.fail_test(msg)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def validate_help_text_on_add_connection_dialog(cls, connections):
            logger.info("Validating help text for managed volume on add connection dialog.")
            for connection in connections:
                cls.click_add_connection_button()
                cls.wait_add_connection_dialog_shown(time_for_loading=3)
                cls.input_name(connection.name)
                cls.select_function_type_by_text(connection.FunctionType, timeout=10, fail_if_false=True)
                cls.input_select_network(connection.network)
                cls.input_select_port(connection.port)
                cls.select_boot_by_text(connection.boot, fail_if_false=True)
                if not (cls.get_help_text_for_boot_radio_option("Use adapter BIOS") and cls.get_help_text_for_boot_radio_option("Specify boot target")):
                    if not cls.get_help_text_for_boot_radio_option("managed volume") == connection.expected_help_text_for_boot_raido_option:
                        logger.info("Help Text is different from the expected text in Test Data: '%s'." % connection.expected_help_text_for_boot_raido_option)
                        logger.info("Validating the help text for radio boot managed volume failed.")
                        return False
                    else:
                        logger.info("Help Text is different from the expected text in Test Data: '%s'." % connection.expected_help_text_for_boot_raido_option)
                        logger.info("Validating the help text for radio boot managed volume successfully")
                        return True
                else:
                    logger.warn("Help Text for raido boot 'Use Adapter BIOS' and 'Specify boot target' should not appear.")
                    return False

        @classmethod
        def get_help_text_for_boot_radio_option(cls, boot_option):
            logger.debug("Getting help text for boot radio option: '%s'" % boot_option)
            cls.set_boot_radio_option(boot_option)
            help_text = FusionUIBase.get_text(cls.e.ID_TEXT_HELP_RADIO_BOOT)
            logger.info("Help Text for '%s' is '%s' ..." % (boot_option, help_text))
            return help_text

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def verify_user_specified_initiator_existing(cls, timeout=5):
            logger.debug("Verify user specified initiator existing ...")
            if ui_lib.wait_for_element_visible(cls.e.ID_RADIO_USER_SPECIFIED, timeout=timeout, fail_if_false=False):
                logger.info("User specified initiator is visiable on edit connection.")
                return True
            else:
                logger.warn("User specified initiator is not visiable on edit connection.")
                return False

        @classmethod
        def set_chap_radio_option(cls, connection_chap_lvl, timeout=5):
            logger.debug("Setting 'CHAP Level' to '%s'" % connection_chap_lvl)
            if connection_chap_lvl == 'None':
                cls.tick_chap_lvl_none(timeout)
            elif connection_chap_lvl == 'CHAP':
                cls.tick_chap_lvl_chap(timeout)
            elif connection_chap_lvl == 'Mutual CHAP':
                cls.tick_chap_lvl_mchap(timeout)
            else:
                ui_lib.fail_test("<test data issue>: '%s' does not match any expected value for the Connection's 'CHAP level'. "
                                 "Expected values are ('None', 'CHAP', 'Mutual CHAP'), " % connection_chap_lvl)

        @classmethod
        def tick_managed_volume(cls, timeout=5):
            logger.debug("choose Connection's boot option 'Managed volume' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_MANAGED_VOLUME, timeout=timeout, fail_if_false=True)

        @classmethod
        def tick_specify_boot_target(cls, timeout=5):
            logger.debug("choose Connection's boot option 'Specify boot target' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SPECIFY_BOOT_TARGET, timeout=timeout, fail_if_false=True)

        @classmethod
        def tick_use_adapter_bios(cls, timeout=5):
            logger.debug("choose Connection's boot option 'Use Adapter BIOS' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_USE_ADAPTER_BIOS, timeout=timeout, fail_if_false=True)

        @classmethod
        def tick_profile_initiator_name(cls, timeout=5):
            logger.debug("choose Connection's iSCSI initiator name 'Profile initiator name' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_PROFILE_INITIATOR_NAME, timeout=timeout, fail_if_false=True)

        @classmethod
        def tick_user_specified_initiator_name(cls, timeout=5):
            logger.debug("choose Connection's iSCSI initiator name 'User specified' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_USER_SPECIFIED, timeout=timeout, fail_if_false=True)

        @classmethod
        def tick_chap_lvl_none(cls, timeout=5):
            logger.debug("Clicking radio button 'None' for Connection's 'CHAP level' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_CHAP_LVL_NONE, timeout)

        @classmethod
        def tick_chap_lvl_chap(cls, timeout=5):
            logger.debug("Clicking radio button 'CHAP' for Connection's 'CHAP level' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_CHAP_LVL_CHAP, timeout)

        @classmethod
        def tick_chap_lvl_mchap(cls, timeout=5):
            logger.debug("Clicking radio button 'Mutual CHAP' for Connection's 'CHAP level' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_CHAP_LVL_MCHAP, timeout)

        @classmethod
        def input_wwpn(cls, connection_wwpn, timeout=5, fail_if_false=True):
            logger.debug("input Connection's 'WWPN' as '%s'" % connection_wwpn)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_WWPN, connection_wwpn, timeout=timeout, fail_if_false=True)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_WWPN, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_ERR_MSG_WWPN, timeout=1):
                    msg = "<entry invalid>: entered value '%s' for Connection's 'WWPN' is INVALID, " \
                          "error message from UI is: \n" \
                          "<%s>" % (connection_wwpn, FusionUIBase.get_text(cls.e.ID_ERR_MSG_WWPN))
                else:
                    msg = "<entry invalid>: entered value '%s' for Connection's 'WWPN' is INVALID, " \
                          "this could be caused by giving an empty value to a required field" % connection_wwpn

                return FusionUIBase.fail_test_or_return_false(msg)

            return True

        @classmethod
        def input_lun(cls, connection_lun, timeout=5, fail_if_false=True):
            logger.debug("input Connection's 'LUN' as '%s'" % connection_lun)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_LUN, connection_lun, timeout=timeout, fail_if_false=True)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_LUN, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_ERR_MSG_WWPN, timeout=1):
                    msg = "<entry invalid>: entered value '%s' for Connection's 'LUN' is INVALID, " \
                          "error message from UI is: \n" \
                          "<%s>" % (connection_lun, FusionUIBase.get_text(cls.e.ID_ERR_MSG_LUN))
                else:
                    msg = "<entry invalid>: entered value '%s' for Connection's 'LUN' is INVALID, " \
                          "this could be caused by giving an empty value to a required field" % connection_lun

                return FusionUIBase.fail_test_or_return_false(msg)

            return True

        @classmethod
        def input_iscsi_initiator_name(cls, iscsi_initiator_name, timeout=5, fail_if_false=True):
            logger.debug("input Connection's 'iSCSI Initiator name' as '%s'" % iscsi_initiator_name)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ISCSI_INITIATOR_NAME, iscsi_initiator_name, timeout=timeout, fail_if_false=fail_if_false)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_ISCSI_INITIATOR_NAME, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_TEXT_ERROR_ISCSI_INITIATOR_NAME, timeout=1):
                    ui_lib.fail_test("<entry invalid>: entered value '%s' for Connection's 'iSCSI Initiator name' is "
                                     "INVALID, error message from UI is: \n<%s>"
                                     % (iscsi_initiator_name, FusionUIBase.get_text(cls.e.ID_TEXT_ERROR_ISCSI_INITIATOR_NAME)))

        @classmethod
        def input_iscsi_initiator_ipv4_address(cls, iscsi_initiator_ipv4_address, timeout=5, fail_if_false=True):
            logger.debug("input Connection's 'iSCSI Initiator IPv4 address' as '%s'" % iscsi_initiator_ipv4_address)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ISCSI_INITIATOR_IPV4_ADDRESS, iscsi_initiator_ipv4_address, timeout=timeout, fail_if_false=fail_if_false)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_ISCSI_INITIATOR_IPV4_ADDRESS, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_TEXT_ERROR_ISCSI_INITIATOR_IPV4_ADDRESS, timeout=1):
                    ui_lib.fail_test("<entry invalid>: entered value '%s' for Connection's 'iSCSI Initiator IPv4 "
                                     "address' is INVALID, error message from UI is: \n<%s>"
                                     % (iscsi_initiator_ipv4_address, FusionUIBase.get_text(cls.e.ID_TEXT_ERROR_ISCSI_INITIATOR_IPV4_ADDRESS)))

        @classmethod
        def input_iscsi_initiator_subnet_mask(cls, iscsi_subnet_mask, timeout=5, fail_if_false=True):
            logger.debug("input Connection's 'iSCSI Initiator Subnet mask' as '%s'" % iscsi_subnet_mask)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ISCSI_SUBNET_MASK, iscsi_subnet_mask, timeout=timeout, fail_if_false=fail_if_false)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_ISCSI_SUBNET_MASK, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_TEXT_ERROR_ISCSI_SUBNET_MASK, timeout=1):
                    ui_lib.fail_test("<entry invalid>: entered value '%s' for Connection's 'iSCSI Initiator Subnet mask'"
                                     " is INVALID, error message from UI is: \n<%s>"
                                     % (iscsi_subnet_mask, FusionUIBase.get_text(cls.e.ID_TEXT_ERROR_ISCSI_SUBNET_MASK)))

        @classmethod
        def input_iscsi_initiator_vlan_id(cls, iscsi_vlan_id, timeout=5, fail_if_false=True):
            logger.debug("input Connection's 'iSCSI Initiator VLAN ID' as '%s'" % iscsi_vlan_id)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ISCSI_VLAN_ID, iscsi_vlan_id, timeout=timeout, fail_if_false=fail_if_false)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_ISCSI_VLAN_ID, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_TEXT_ERROR_ISCSI_VLAN_ID, timeout=1):
                    ui_lib.fail_test("<entry invalid>: entered value '%s' for Connection's 'iSCSI Initiator VLAN ID' is "
                                     "INVALID, error message from UI is: \n<%s>"
                                     % (iscsi_vlan_id, FusionUIBase.get_text(cls.e.ID_TEXT_ERROR_ISCSI_VLAN_ID)))

        @classmethod
        def input_iscsi_initiator_gateway(cls, iscsi_gateway, timeout=5, fail_if_false=True):
            logger.debug("input Connection's 'iSCSI Initiator Gateway' as '%s'" % iscsi_gateway)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ISCSI_GATEWAY, iscsi_gateway, timeout=timeout, fail_if_false=fail_if_false)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_ISCSI_GATEWAY, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_TEXT_ERROR_ISCSI_GATEWAY, timeout=1):
                    ui_lib.fail_test("<entry invalid>: entered value '%s' for Connection's 'iSCSI Initiator Gateway' is "
                                     "INVALID, error message from UI is: \n<%s>"
                                     % (iscsi_gateway, FusionUIBase.get_text(cls.e.ID_TEXT_ERROR_ISCSI_GATEWAY)))

        @classmethod
        def input_iscsi_boot_target_name(cls, iscsi_target_name, timeout=5, fail_if_false=True):
            logger.debug("input Connection's 'iSCSI Boot Target name' as '%s'" % iscsi_target_name)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ISCSI_TARGET_NAME, iscsi_target_name, timeout=timeout, fail_if_false=fail_if_false)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_ISCSI_TARGET_NAME, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_TEXT_ERROR_ISCSI_TARGET_NAME, timeout=1):
                    ui_lib.fail_test("<entry invalid>: entered value '%s' for Connection's 'iSCSI Boot Target name' is "
                                     "INVALID, error message from UI is: \n<%s>"
                                     % (iscsi_target_name, FusionUIBase.get_text(cls.e.ID_TEXT_ERROR_ISCSI_TARGET_NAME)))

        @classmethod
        def input_iscsi_boot_target_lun(cls, iscsi_target_lun, timeout=5, fail_if_false=True):
            logger.debug("input Connection's 'iSCSI Boot Target name' as '%s'" % iscsi_target_lun)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ISCSI_TARGET_LUN, iscsi_target_lun, timeout=timeout, fail_if_false=fail_if_false)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_ISCSI_TARGET_LUN, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_TEXT_ERROR_ISCSI_TARGET_LUN, timeout=1):
                    ui_lib.fail_test("<entry invalid>: entered value '%s' for Connection's 'iSCSI Boot Target name' is "
                                     "INVALID, error message from UI is: \n<%s>"
                                     % (iscsi_target_lun, FusionUIBase.get_text(cls.e.ID_TEXT_ERROR_ISCSI_TARGET_LUN)))

        @classmethod
        def input_iscsi_boot_target_ip(cls, iscsi_target_ip, timeout=5, fail_if_false=True):
            logger.debug("input Connection's 'iSCSI Boot Target IP address' as '%s'" % iscsi_target_ip)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ISCSI_TARGET_IP, iscsi_target_ip, timeout=timeout, fail_if_false=fail_if_false)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_ISCSI_TARGET_IP, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_TEXT_ERROR_ISCSI_TARGET_IP, timeout=1):
                    ui_lib.fail_test("<entry invalid>: entered value '%s' for Connection's 'iSCSI Boot Target IP "
                                     "address' is INVALID, error message from UI is: \n<%s>"
                                     % (iscsi_target_ip, FusionUIBase.get_text(cls.e.ID_TEXT_ERROR_ISCSI_TARGET_IP)))

        @classmethod
        def input_iscsi_boot_target_port(cls, iscsi_target_port, timeout=5, fail_if_false=True):
            logger.debug("input Connection's 'iSCSI Boot Target port' as '%s'" % iscsi_target_port)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ISCSI_TARGET_PORT, iscsi_target_port, timeout=timeout, fail_if_false=fail_if_false)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_ISCSI_TARGET_PORT, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_TEXT_ERROR_ISCSI_TARGET_PORT, timeout=1):
                    ui_lib.fail_test("<entry invalid>: entered value '%s' for Connection's 'iSCSI Boot Target port' is "
                                     "INVALID, error message from UI is: \n<%s>"
                                     % (iscsi_target_port, FusionUIBase.get_text(cls.e.ID_TEXT_ERROR_ISCSI_TARGET_PORT)))

        @classmethod
        def input_iscsi_boot_target_second_ip(cls, iscsi_target_second_ip, timeout=5, fail_if_false=True):
            logger.debug("input Connection's 'iSCSI Boot Target Second IP address' as '%s'" % iscsi_target_second_ip)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ISCSI_SECOND_IP, iscsi_target_second_ip, timeout=timeout, fail_if_false=fail_if_false)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_ISCSI_SECOND_IP, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_TEXT_ERROR_ISCSI_SECOND_IP, timeout=1):
                    ui_lib.fail_test("<entry invalid>: entered value '%s' for Connection's 'iSCSI Boot Target Second IP "
                                     "address' is INVALID, error message from UI is: \n<%s>"
                                     % (iscsi_target_second_ip, FusionUIBase.get_text(cls.e.ID_TEXT_ERROR_ISCSI_SECOND_IP)))

        @classmethod
        def input_iscsi_boot_target_second_port(cls, iscsi_target_second_port, timeout=5, fail_if_false=True):
            logger.debug("input Connection's 'iSCSI Boot Target port' as '%s'" % iscsi_target_second_port)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ISCSI_SECOND_PORT, iscsi_target_second_port, timeout=timeout, fail_if_false=fail_if_false)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_ISCSI_SECOND_PORT, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_TEXT_ERROR_ISCSI_SECOND_PORT, timeout=1):
                    ui_lib.fail_test("<entry invalid>: entered value '%s' for Connection's 'iSCSI Boot Target port' is "
                                     "INVALID, error message from UI is: \n<%s>"
                                     % (iscsi_target_second_port, FusionUIBase.get_text(cls.e.ID_TEXT_ERROR_ISCSI_SECOND_PORT)))

        @classmethod
        def input_iscsi_chap_name(cls, chap_name, timeout=5):
            logger.debug("Setting 'CHAP Name' to '%s'" % chap_name)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_CHAP_NAME, chap_name, timeout)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_CHAP_NAME, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_TEXT_ERROR_CHAP_NAME, timeout=1):
                    ui_lib.fail_test("<entry invalid>: entered value '%s' for Connection's 'CHAP Name' is "
                                     "INVALID, error message from UI is: \n<%s>"
                                     % (chap_name, FusionUIBase.get_text(cls.e.ID_TEXT_ERROR_CHAP_NAME)))

        @classmethod
        def input_iscsi_chap_secret(cls, chap_secret, timeout=5):
            logger.debug("Setting 'CHAP Secret' to '%s'" % chap_secret)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_CHAP_SECRET, chap_secret, timeout)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_CHAP_SECRET, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_TEXT_ERROR_CHAP_SECRET, timeout=1):
                    ui_lib.fail_test("<entry invalid>: entered value '%s' for Connection's 'CHAP Secret' is "
                                     "INVALID, error message from UI is: \n<%s>"
                                     % (chap_secret, FusionUIBase.get_text(cls.e.ID_TEXT_ERROR_CHAP_SECRET)))

        @classmethod
        def input_iscsi_mchap_name(cls, mchap_name, timeout=5):
            logger.debug("Setting 'Mutual CHAP Name' to '%s'" % mchap_name)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_MCHAP_NAME, mchap_name, timeout)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_MCHAP_NAME, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_TEXT_ERROR_MCHAP_NAME, timeout=1):
                    ui_lib.fail_test("<entry invalid>: entered value '%s' for Connection's 'Mutual CHAP Name' is "
                                     "INVALID, error message from UI is: \n<%s>"
                                     % (mchap_name, FusionUIBase.get_text(cls.e.ID_TEXT_ERROR_MCHAP_NAME)))

        @classmethod
        def input_iscsi_mchap_secret(cls, mchap_secret, timeout=5):
            logger.debug("Setting 'Mutual CHAP Secret' to '%s'" % mchap_secret)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_MCHAP_SECRET, mchap_secret, timeout)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_MCHAP_SECRET, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_TEXT_ERROR_MCHAP_SECRET, timeout=1):
                    ui_lib.fail_test("<entry invalid>: entered value '%s' for Connection's 'Mutual CHAP Secret' is "
                                     "INVALID, error message from UI is: \n<%s>"
                                     % (mchap_secret, FusionUIBase.get_text(cls.e.ID_TEXT_ERROR_MCHAP_SECRET)))

        @classmethod
        def tick_use_user_specified_ids(cls, timeout=5, fail_if_false=True):
            logger.debug("turn on Connection's 'Use user-specified IDs' option ...")
            FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_USE_USER_SPECIFIED_IDS, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def input_wwpn_user_specified(cls, connection_wwpn_user_specified, timeout=5, fail_if_false=True):
            logger.debug("input Connection's 'WWPN' as '%s'" % connection_wwpn_user_specified)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_WWPN_USER_SPECIFIED, connection_wwpn_user_specified, timeout=timeout, fail_if_false=fail_if_false)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_WWPN_USER_SPECIFIED, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_ERR_MSG_WWPN_USER_SPECIFIED, timeout=1):
                    msg = "<entry invalid>: entered value '%s' for Connection's user-specified 'WWPN' is INVALID, " \
                          "error message from UI is: \n" \
                          "<%s>" % (connection_wwpn_user_specified, FusionUIBase.get_text(cls.e.ID_ERR_MSG_WWPN_USER_SPECIFIED))
                else:
                    msg = "<entry invalid>: entered value '%s' for Connection's user-specified 'WWPN' is INVALID, " \
                          "this could be caused by giving an empty value to a required field" % connection_wwpn_user_specified

                return FusionUIBase.fail_test_or_return_false(msg)

            return True

        @classmethod
        def input_wwnn_user_specified(cls, connection_wwnn_user_specified, timeout=5, fail_if_false=True):
            logger.debug("input Connection's user-specified 'WWNN' as '%s'" % connection_wwnn_user_specified)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_WWNN_USER_SPECIFIED, connection_wwnn_user_specified, timeout=timeout, fail_if_false=True)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_WWNN_USER_SPECIFIED, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_ERR_MSG_WWNN_USER_SPECIFIED, timeout=1):
                    msg = "<entry invalid>: entered value '%s' for Connection's user-specified 'WWNN' is INVALID, " \
                          "error message from UI is: \n" \
                          "<%s>" % (connection_wwnn_user_specified, FusionUIBase.get_text(cls.e.ID_ERR_MSG_WWNN_USER_SPECIFIED))
                else:
                    msg = "<entry invalid>: entered value '%s' for Connection's user-specified 'WWNN' is INVALID, " \
                          "this could be caused by giving an empty value to a required field" % connection_wwnn_user_specified

                return FusionUIBase.fail_test_or_return_false(msg)

            return True

        @classmethod
        def input_mac_address_user_specified(cls, connection_mac_address_user_specified, timeout=5, fail_if_false=True):
            logger.debug("input Connection's user-specified 'MAC Address' as '%s'" % connection_mac_address_user_specified)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_MAC_ADDRESS_USER_SPECIFIED, connection_mac_address_user_specified, timeout=timeout, fail_if_false=True)
            cls.click_dialog_title(timeout=2)
            if ui_lib.wait_for_element_class(cls.e.ID_INPUT_MAC_ADDRESS_USER_SPECIFIED, 'hp-error', timeout=1):
                if ui_lib.is_visible(cls.e.ID_ERR_MSG_MAC_ADDRESS_USER_SPECIFIED, timeout=1):
                    msg = "<entry invalid>: entered value '%s' for Connection's user-specified 'MAC Address' is INVALID, " \
                          "error message from UI is: \n" \
                          "<%s>" % (connection_mac_address_user_specified, FusionUIBase.get_text(cls.e.ID_ERR_MSG_MAC_ADDRESS_USER_SPECIFIED))
                else:
                    msg = "<entry invalid>: entered value '%s' for Connection's user-specified 'MAC Address' is INVALID, " \
                          "this could be caused by giving an empty value to a required field" % connection_mac_address_user_specified

                return FusionUIBase.fail_test_or_return_false(msg)

            return True

        @classmethod
        def click_dialog_title(cls, timeout=5):
            logger.debug("click dialog title 'Add Connection' to blur out of input control to let entry-validate-error-msg show up ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_DIALOG_TITLE, timeout=timeout, fail_if_false=True)

        @classmethod
        def click_add_button(cls, timeout=5):
            logger.debug("click button 'Add' (Add Connection) ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD, timeout=timeout, fail_if_false=True)

        @classmethod
        def click_add_plus_button(cls, timeout=5):
            logger.debug("click button 'Add+' (Add Connection) ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_PLUS, timeout=timeout, fail_if_false=True)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def verify_add_plus_button_existing(cls, timeout=5):
            logger.debug("Verify button 'Add+' (Add Connection) existing...")
            if ui_lib.wait_for_element_visible(cls.e.ID_BUTTON_ADD_PLUS, timeout=timeout, fail_if_false=False):
                logger.info("The 'Add+' button is visible on add connection dialog.")
                return True
            else:
                logger.warn("The 'Add+' button is not visible on add connection dialog.")
                return False

        @classmethod
        def click_cancel_button(cls, timeout=5):
            logger.debug("click button 'Cancel' (Add Connection) ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout=timeout, fail_if_false=True)

        @classmethod
        def click_ok_button(cls, timeout=5):
            logger.debug("click button 'OK' (Edit Connection) ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_OK, timeout=timeout, fail_if_false=True)

        @classmethod
        def verify_edited_connection(cls, connection, timeout=5):
            # TODO: make this function intact for verifying the edited connection if it's updated as expected
            logger.debug("verifying the edited connection '%s' (Edit Connection) ..." % connection, also_console=False)
            return True

        @classmethod
        def verify_iscsi_initiator_name_error_message(cls, expected_message, timeout=5):
            logger.debug("Verifying error message for 'iSCSI Initiator Name' ...\nExpected message: '%s'" % expected_message)
            if expected_message == '':
                return ui_lib.wait_for_element_notvisible(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_INITIATOR_NAME, timeout, fail_if_false=True)
            if not FusionUIBase.verify_element_text("iSCSI Initiator Name", GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_INITIATOR_NAME, expected_message, timeout, fail_if_false=False):
                ui_lib.fail_test("Unexpected error message for 'iSCSI Initiator name'.\nActual message: '%s'\nExpected message: '%s'"
                                 % (FusionUIBase.get_text(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_INITIATOR_NAME, timeout), expected_message))

        @classmethod
        def verify_iscsi_initiator_ip_error_message(cls, expected_message, timeout=5):
            logger.debug("Verifying error message for 'iSCSI Initiator IPv4 Address' ...\nExpected message: '%s'" % expected_message)
            if expected_message == '':
                return ui_lib.wait_for_element_notvisible(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_INITIATOR_IPV4_ADDRESS, timeout, fail_if_false=True)
            if not FusionUIBase.verify_element_text("iSCSI Initiator IPv4 Address", GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_INITIATOR_IPV4_ADDRESS, expected_message, timeout, fail_if_false=False):
                ui_lib.fail_test("Unexpected error message for 'iSCSI Initiator IPv4 Address'.\nActual message: '%s'\nExpected message: '%s'"
                                 % (FusionUIBase.get_text(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_INITIATOR_IPV4_ADDRESS, timeout), expected_message))

        @classmethod
        def verify_iscsi_subnet_error_message(cls, expected_message, timeout=5):
            logger.debug("Verifying error message for 'iSCSI Subnet Mask' ...\nExpected message: '%s'" % expected_message)
            if expected_message == '':
                return ui_lib.wait_for_element_notvisible(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_SUBNET_MASK, timeout, fail_if_false=True)
            if not FusionUIBase.verify_element_text("iSCSI Subnet Mask", GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_SUBNET_MASK, expected_message, timeout, fail_if_false=False):
                ui_lib.fail_test("Unexpected error message for 'iSCSI Subnet Mask'.\nActual message: '%s'\nExpected message: '%s'"
                                 % (FusionUIBase.get_text(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_SUBNET_MASK, timeout), expected_message))

        @classmethod
        def verify_iscsi_gateway_error_message(cls, expected_message, timeout=5):
            logger.debug("Verifying error message for 'iSCSI Gateway' ...\nExpected message: '%s'" % expected_message)
            if expected_message == '':
                return ui_lib.wait_for_element_notvisible(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_GATEWAY, timeout, fail_if_false=True)
            if not FusionUIBase.verify_element_text("iSCSI Gateway", GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_GATEWAY, expected_message, timeout, fail_if_false=False):
                ui_lib.fail_test("Unexpected error message for 'iSCSI Gateway'.\nActual message: '%s'\nExpected message: '%s'"
                                 % (FusionUIBase.get_text(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_GATEWAY, timeout), expected_message))

        @classmethod
        def verify_iscsi_vlan_id_error_message(cls, expected_message, timeout=5):
            logger.debug("Verifying error message for 'iSCSI VLAN ID' ...\nExpected message: '%s'" % expected_message)
            if expected_message == '':
                return ui_lib.wait_for_element_notvisible(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_VLAN_ID, timeout, fail_if_false=True)
            if not FusionUIBase.verify_element_text("iSCSI VLAN ID", GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_VLAN_ID, expected_message, timeout, fail_if_false=False):
                ui_lib.fail_test("Unexpected error message for 'iSCSI VLAN ID'.\nActual message: '%s'\nExpected message: '%s'"
                                 % (FusionUIBase.get_text(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_VLAN_ID, timeout), expected_message))

        @classmethod
        def verify_iscsi_target_name_error_message(cls, expected_message, timeout=5):
            logger.debug("Verifying error message for 'iSCSI Target Name' ...\nExpected message: '%s'" % expected_message)
            if expected_message == '':
                return ui_lib.wait_for_element_notvisible(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_TARGET_NAME, timeout, fail_if_false=True)
            if not FusionUIBase.verify_element_text("iSCSI Target Name", GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_TARGET_NAME, expected_message, timeout, fail_if_false=False):
                ui_lib.fail_test("Unexpected error message for 'iSCSI Target Name'.\nActual message: '%s'\nExpected message: '%s'"
                                 % (FusionUIBase.get_text(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_TARGET_NAME, timeout), expected_message))

        @classmethod
        def verify_iscsi_target_lun_error_message(cls, expected_message, timeout=5):
            logger.debug("Verifying error message for 'iSCSI Target LUN' ...\nExpected message: '%s'" % expected_message)
            if expected_message == '':
                return ui_lib.wait_for_element_notvisible(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_TARGET_LUN, timeout, fail_if_false=True)
            if not FusionUIBase.verify_element_text("iSCSI Target LUN", GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_TARGET_LUN, expected_message, timeout, fail_if_false=False):
                ui_lib.fail_test("Unexpected error message for 'iSCSI Target LUN'.\nActual message: '%s'\nExpected message: '%s'"
                                 % (FusionUIBase.get_text(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_TARGET_LUN, timeout), expected_message))

        @classmethod
        def verify_iscsi_target_ip_error_message(cls, expected_message, timeout=5):
            logger.debug("Verifying error message for 'iSCSI Target IP Address' ...\nExpected message: '%s'" % expected_message)
            if expected_message == '':
                return ui_lib.wait_for_element_notvisible(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_TARGET_IP, timeout, fail_if_false=True)
            if not FusionUIBase.verify_element_text("iSCSI Target IP Address", GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_TARGET_IP, expected_message, timeout, fail_if_false=False):
                ui_lib.fail_test("Unexpected error message for 'iSCSI Target IP Address'.\nActual message: '%s'\nExpected message: '%s'"
                                 % (FusionUIBase.get_text(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_TARGET_IP, timeout), expected_message))

        @classmethod
        def verify_iscsi_target_port_error_message(cls, expected_message, timeout=5):
            logger.debug("Verifying error message for 'iSCSI Target Port' ...\nExpected message: '%s'" % expected_message)
            if expected_message == '':
                return ui_lib.wait_for_element_notvisible(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_TARGET_PORT, timeout, fail_if_false=True)
            if not FusionUIBase.verify_element_text("iSCSI Target Port", GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_TARGET_PORT, expected_message, timeout, fail_if_false=False):
                ui_lib.fail_test("Unexpected error message for 'iSCSI Target Port'.\nActual message: '%s'\nExpected message: '%s'"
                                 % (FusionUIBase.get_text(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_TARGET_PORT, timeout), expected_message))

        @classmethod
        def verify_iscsi_second_ip_error_message(cls, expected_message, timeout=5):
            logger.debug("Verifying error message for 'iSCSI Second IP Address' ...\nExpected message: '%s'" % expected_message)
            if expected_message == '':
                return ui_lib.wait_for_element_notvisible(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_SECOND_IP, timeout, fail_if_false=True)
            if not FusionUIBase.verify_element_text("iSCSI Second IP Address", GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_SECOND_IP, expected_message, timeout, fail_if_false=False):
                ui_lib.fail_test("Unexpected error message for 'iSCSI Second IP Address'.\nActual message: '%s'\nExpected message: '%s'"
                                 % (FusionUIBase.get_text(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_SECOND_IP, timeout), expected_message))

        @classmethod
        def verify_iscsi_second_port_error_message(cls, expected_message, timeout=5):
            logger.debug("Verifying error message for 'iSCSI Second Port' ...\nExpected message: '%s'" % expected_message)
            if expected_message == '':
                return ui_lib.wait_for_element_notvisible(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_SECOND_PORT, timeout, fail_if_false=True)
            if not FusionUIBase.verify_element_text("iSCSI Second Port", GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_SECOND_PORT, expected_message, timeout, fail_if_false=False):
                ui_lib.fail_test("Unexpected error message for 'iSCSI Second Port'.\nActual message: '%s'\nExpected message: '%s'"
                                 % (FusionUIBase.get_text(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_ISCSI_SECOND_PORT, timeout), expected_message))

        @classmethod
        def verify_iscsi_chap_name_error_message(cls, expected_message, timeout=5):
            logger.debug("Verifying error message for 'iSCSI CHAP Name' ...\nExpected message: '%s'" % expected_message)
            if expected_message == '':
                return ui_lib.wait_for_element_notvisible(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_CHAP_NAME, timeout, fail_if_false=True)
            if not FusionUIBase.verify_element_text("iSCSI CHAP Name", GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_CHAP_NAME, expected_message, timeout, fail_if_false=False):
                ui_lib.fail_test("Unexpected error message for 'iSCSI CHAP Name'.\nActual message: '%s'\nExpected message: '%s'"
                                 % (FusionUIBase.get_text(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_CHAP_NAME, timeout), expected_message))

        @classmethod
        def verify_iscsi_chap_secret_error_message(cls, expected_message, timeout=5):
            logger.debug("Verifying error message for 'iSCSI CHAP Secret' ...\nExpected message: '%s'" % expected_message)
            if expected_message == '':
                return ui_lib.wait_for_element_notvisible(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_CHAP_SECRET, timeout, fail_if_false=True)
            if not FusionUIBase.verify_element_text("iSCSI CHAP Secret", GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_CHAP_SECRET, expected_message, timeout, fail_if_false=False):
                ui_lib.fail_test("Unexpected error message for 'iSCSI CHAP Secret'.\nActual message: '%s'\nExpected message: '%s'"
                                 % (FusionUIBase.get_text(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_CHAP_SECRET, timeout), expected_message))

        @classmethod
        def verify_iscsi_mchap_name_error_message(cls, expected_message, timeout=5):
            logger.debug("Verifying error message for 'iSCSI Mutual CHAP Name' ...\nExpected message: '%s'" % expected_message)
            if expected_message == '':
                return ui_lib.wait_for_element_notvisible(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_MCHAP_NAME, timeout, fail_if_false=True)
            if not FusionUIBase.verify_element_text("iSCSI Mutual CHAP Name", GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_MCHAP_NAME, expected_message, timeout, fail_if_false=False):
                ui_lib.fail_test("Unexpected error message for 'iSCSI Mutual CHAP Name'.\nActual message: '%s'\nExpected message: '%s'"
                                 % (FusionUIBase.get_text(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_MCHAP_NAME, timeout), expected_message))

        @classmethod
        def verify_iscsi_mchap_secret_error_message(cls, expected_message, timeout=5):
            logger.debug("Verifying error message for 'iSCSI Mutual CHAP Secret' ...\nExpected message: '%s'" % expected_message)
            if expected_message == '':
                return ui_lib.wait_for_element_notvisible(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_MCHAP_SECRET, timeout, fail_if_false=True)
            if not FusionUIBase.verify_element_text("iSCSI Mutual CHAP Secret", GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_MCHAP_SECRET, expected_message, timeout, fail_if_false=False):
                ui_lib.fail_test("Unexpected error message for 'iSCSI Mutual CHAP Secret'.\nActual message: '%s'\nExpected message: '%s'"
                                 % (FusionUIBase.get_text(GeneralServerProfilesElements.Connection.ID_TEXT_ERROR_MCHAP_SECRET, timeout), expected_message))

        @classmethod
        def set_iscsi_boot_options(cls, connection, timeout=5):
            logger.debug("Setting 'iSCSI initiator to %s" % connection.BootOption)
            cls.set_boot_radio_option(connection.BootOption, timeout)
            if hasattr(connection, 'initiatorName') and connection.BootOption.lower() == 'user specified':
                logger.debug("Setting 'User specified iSCSI initiator name' to '%s'" % connection.initiatorName)
                cls.input_iscsi_initiator_name(connection.initiatorName, timeout)
            logger.debug("Setting 'iSCSI initiator IPv4 Address' to '%s'" % connection.initiatorIpv4)
            cls.input_iscsi_initiator_ipv4_address(connection.initiatorIpv4, timeout)
            logger.debug("Setting 'iSCSI initiator Subnet Mask' to '%s'" % connection.subnetMask)
            cls.input_iscsi_initiator_subnet_mask(connection.subnetMask, timeout)
            if hasattr(connection, 'gateway'):
                logger.debug("Setting 'iSCSI initiator Gateway' to '%s'" % connection.gateway)
                cls.input_iscsi_initiator_gateway(connection.gateway, timeout)
            if hasattr(connection, 'vlanId'):
                logger.debug("Setting 'iSCSI initiator VLAN ID' to '%s'" % connection.vlanId)
                cls.input_iscsi_initiator_vlan_id(connection.vlanId, timeout)
            logger.debug("Setting 'iSCSI Boot Target Name' to '%s'" % connection.targetName)
            cls.input_iscsi_boot_target_name(connection.targetName, timeout)
            logger.debug("Setting 'iSCSI Boot Target LUN' to '%s'" % connection.targetLun)
            cls.input_iscsi_boot_target_lun(connection.targetLun, timeout)
            logger.debug("Setting 'iSCSI Boot Target IP Address' to '%s'" % connection.targetIp)
            cls.input_iscsi_boot_target_ip(connection.targetIp, timeout)
            if hasattr(connection, 'targetPort'):
                logger.debug("Setting 'iSCSI Boot Target Port' to '%s'" % connection.targetPort)
                cls.input_iscsi_boot_target_port(connection.targetPort, timeout)
            if hasattr(connection, 'secondIp'):
                logger.debug("Setting 'iSCSI Boot Target Second IP' to '%s'" % connection.secondIp)
                cls.input_iscsi_boot_target_second_ip(connection.secondIp, timeout)
            if hasattr(connection, 'secondPort'):
                logger.debug("Setting 'iSCSI Boot Target Second Port' to '%s'" % connection.secondPort)
                cls.input_iscsi_boot_target_second_port(connection.secondPort, timeout)
            if hasattr(connection, 'chapLvl'):
                cls.set_chap_radio_option(connection.chapLvl, timeout)
                if connection.chapLvl == 'CHAP':
                    cls.input_iscsi_chap_name(connection.chapName, timeout)
                    cls.input_iscsi_chap_secret(connection.chapSecret, timeout)
                if connection.chapLvl == 'Mutual CHAP':
                    cls.input_iscsi_chap_name(connection.chapName, timeout)
                    cls.input_iscsi_chap_secret(connection.chapSecret, timeout)
                    cls.input_iscsi_mchap_name(connection.mchapName, timeout)
                    cls.input_iscsi_mchap_secret(connection.mchapSecret, timeout)

    class LocalStorage(object):
        e = GeneralServerProfilesElements.LocalStorage

        @classmethod
        def set(cls, local_storage, fail_if_false=True):
            logger.info("change to 'Local Storage' view and start setting options and creating logical drives ...")
            FusionUIBase.select_view_by_name('Local Storage')

            if getattr(local_storage, 'integratedController', "False").lower() == 'true':
                cls.click_integrated_local_storage_edit()
                if getattr(local_storage, 'integratedControllerMode').lower() == 'managed manually':
                    cls.select_controller_mode(local_storage.integratedControllerMode, fail_if_false=True)
                elif getattr(local_storage, 'integratedControllerMode').lower() == 'raid':
                    cls.select_controller_mode(local_storage.integratedControllerMode, fail_if_false=True)
                    if getattr(local_storage, 'Re-initialize', '').lower() == 'true':
                        logger.info("'Re-initialize internal storage' is set to 'true', this will disable the option 'Import existing logical drives'")
                        cls.tick_reinitialize_internal_storage()
                    else:
                        logger.info("'Re-initialize internal storage' is set to 'false', this will disable the option 'Import existing logical drives'")
                        cls.untick_reinitialize_internal_storage()

                    if getattr(local_storage, 'ImportExistingLogicalDrives', '').lower() == 'true':
                        logger.info("'Import existing logical drives' is set to 'true', this will disable the option 'Re-initialize internal storage'")
                        if getattr(local_storage, 'Re-initialize', '').lower() == 'true':
                            logger.warn("<test data violates business logic>: 'Re-initialize internal storage' is set to 'true', ""'Import existing logical drives' will be ignored!")
                        else:
                            cls.tick_import_existing_logical_drives()
                    if getattr(local_storage, 'LogicalDrives', None) is not None:
                        # add logical drives
                        logger.debug("list of local drive <LocalDrives/> found: <%s>" % local_storage.LogicalDrives, also_console=False)
                        cls.LogicalDrive.set(local_storage.LogicalDrives, fail_if_false=fail_if_false)
                elif getattr(local_storage, 'integratedControllerMode').lower() == 'hba':
                    cls.select_controller_mode(local_storage.integratedControllerMode, fail_if_false=True)
                    if getattr(local_storage, 'Re-initialize', '').lower() == 'true':
                        logger.info("'Re-initialize internal storage' is set to 'true', this will disable the option 'Import existing logical drives'")
                        cls.tick_reinitialize_internal_storage()
                    else:
                        logger.info("'Re-initialize internal storage' is set to 'false', this will disable the option 'Import existing logical drives'")
                        cls.untick_reinitialize_internal_storage()
                cls.click_ok_button()
                if ui_lib.wait_for_element_visible(cls.e.LogicalDrive.ID_TITLE_CHANGE_CONTROLLER_MODE_CONFIRM, timeout=10, fail_if_false=False):
                    ui_lib.wait_for_element_and_click(cls.e.LogicalDrive.ID_BUTTON_CHANGE_CONTROLLER_MODE_OK, timeout=10, fail_if_false=True)

            if getattr(local_storage, 'mezzController', "False").lower() == 'true':
                cls.click_mezz_local_storage_edit(local_storage.mezzControllerID)
                if getattr(local_storage, 'mezzControllerMode').lower() == 'managed manually':
                    cls.select_controller_mode(local_storage.mezzControllerMode, fail_if_false=True)
                    if getattr(local_storage, 'LogicalJBODs', None) is not None:
                        # add logical drives
                        logger.debug("list of local JBODs <LocalDrives/> found: <%s>" % local_storage.LogicalJBODs, also_console=False)
                        cls.LogicalDrive.set_jbod(local_storage.LogicalJBODs, fail_if_false=fail_if_false)
                elif getattr(local_storage, 'mezzControllerMode').lower() == 'raid':
                    cls.select_controller_mode(local_storage.mezzControllerMode, fail_if_false=True)
                    if getattr(local_storage, 'LogicalJBODs', None) is not None:
                        # add logical drives
                        logger.debug("list of local JBODs <LocalDrives/> found: <%s>" % local_storage.LogicalJBODs, also_console=False)
                        cls.LogicalDrive.set_jbod(local_storage.LogicalJBODs, fail_if_false=fail_if_false)
                elif getattr(local_storage, 'mezzControllerMode').lower() == 'hba':
                    cls.select_controller_mode(local_storage.mezzControllerMode, fail_if_false=True)
                    if getattr(local_storage, 'LogicalJBODs', None) is not None:
                        # add logical drives
                        logger.debug("list of local JBODs <LocalDrives/> found: <%s>" % local_storage.LogicalJBODs, also_console=False)
                        cls.LogicalDrive.set_jbod(local_storage.LogicalJBODs, fail_if_false=fail_if_false)
                cls.click_ok_button()
                if ui_lib.wait_for_element_visible(cls.e.LogicalJbod.ID_LABEL_CHANGE_CONTROLLER_MODE, timeout=10, fail_if_false=False):
                    ui_lib.wait_for_element_and_click(cls.e.LogicalJbod.ID_BUTTON_OK_CHANGE_CONTROLLER, timeout=10, fail_if_false=True)
                elif ui_lib.wait_for_element_visible(cls.e.LogicalJbod.ID_LABEL_CHANGE_CONTROLLER_MODE_MANUALLY, timeout=10, fail_if_false=False):
                    ui_lib.wait_for_element_and_click(cls.e.LogicalJbod.ID_BUTTON_OK_CHANGE_CONTROLLER, timeout=10, fail_if_false=True)

            # if getattr(local_storage, 'LogicalDrive', None) is not None:
            # add logical drives
            #     logger.debug("list of LocalDrive found: <%s>" % local_storage.LogicalDrive, also_console=False)
            #     cls.LogicalDrive.create(local_storage.LogicalDrive, fail_if_false=fail_if_false)

            # set Boot drive
            if getattr(local_storage, 'BootDrive', None) is not None:
                cls.select_boot_drive_by_text(local_storage.BootDrive, fail_if_false=True)

        @classmethod
        def click_ok_button(cls, timeout=5, fail_if_false=True):
            logger.debug("click button 'OK' Edit local storage")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_OK, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def click_cancel_button(cls, timeout=5, fail_if_false=True):
            logger.debug("click button 'Cancel' Edit local storage")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def click_integrated_local_storage_edit(cls, fail_if_false=True):
            logger.debug("Clicking Integrated storage edit option")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_INTEGRATED_CONTROLLER, 10, fail_if_false)

        @classmethod
        def click_mezz_local_storage_edit(cls, mezzControllerID, fail_if_false=True):
            logger.debug("Clicking Mezz storage edit option")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_MEZZ_CONTROLLER % (mezzControllerID), 10, fail_if_false)

        @classmethod
        def select_controller_mode(cls, controller_mode, fail_if_false=True):
            logger.debug("select Local Storage's 'Controller mode' as '%s' ..." % controller_mode)
            FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_CONTROLLER_MODE, controller_mode, timeout=10, fail_if_false=fail_if_false)
            if ui_lib.wait_for_element_visible(cls.e.LogicalDrive.ID_TITLE_CHANGE_CONTROLLER_MODE_CONFIRM, timeout=10, fail_if_false=False):
                ui_lib.wait_for_element_and_click(cls.e.LogicalDrive.ID_BUTTON_CHANGE_CONTROLLER_MODE_OK, timeout=10, fail_if_false=True)

        @classmethod
        def tick_manage_local_storage(cls, timeout=5, fail_if_false=True):
            logger.debug("turn on Local Storage's 'Manage local storage' option ...")
            FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_MANAGE_LOCAL_STORAGE, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def untick_manage_local_storage(cls, timeout=5, fail_if_false=True):
            logger.debug("turn off Local Storage's 'Manage local storage' option ...")
            FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_MANAGE_LOCAL_STORAGE, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_manage_integrated_controller(cls, timeout=5, fail_if_false=True):
            logger.debug("turn on Local Storage's 'Manage integrated controller' option ...")
            FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_MANAGE_INTEGRATED_CONTROLLER, timeout=timeout, fail_if_false=fail_if_false)
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_MANAGE_LOCAL_STORAGE_CONTROLLER_ALERT_CLOSE, timeout=timeout, fail_if_false=False)

        @classmethod
        def untick_manage_integrated_controller(cls, timeout=5, fail_if_false=True):
            logger.debug("turn off Local Storage's 'Manage integrated controller' option ...")
            FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_MANAGE_INTEGRATED_CONTROLLER, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_reinitialize_internal_storage(cls, timeout=5, fail_if_false=True):
            logger.debug("turn on Local Storage's 'Re-initialize internal storage' option ...")
            FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_REINITIALIZE_INTERNAL_STORAGE, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def untick_reinitialize_internal_storage(cls, timeout=5, fail_if_false=True):
            logger.debug("turn off Local Storage's 'Re-initialize internal storage' option ...")
            FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_REINITIALIZE_INTERNAL_STORAGE, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def select_controller_mode_by_text(cls, controller_mode, timeout=5, fail_if_false=True):
            logger.debug("validating test data '%s' for Local Storage's 'Controller mode' ..." % controller_mode)
            if FusionUIBase.is_test_data_valid(controller_mode, 'Local_Storage_Controller_Mode', fail_if_false=False):
                logger.debug("select Local Storage's 'Controller mode' as '%s' ..." % controller_mode)
                FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_CONTROLLER_MODE, controller_mode, timeout=timeout, fail_if_false=fail_if_false)
            else:
                msg = "<test data invalid> '%s' for Local Storage's 'Controller mode' is NOT valid" % controller_mode
                logger.warn(msg)
                if fail_if_false:
                    ui_lib.fail_test(msg)

        @classmethod
        def tick_import_existing_logical_drives(cls, timeout=5, fail_if_false=True):
            logger.debug("turn on Local Storage's 'Import existing logical drives' option ...")
            FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_IMPORT_EXISTING_LOGICAL_DRIVES, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def untick_import_existing_logical_drives(cls, timeout=5, fail_if_false=True):
            logger.debug("turn off Local Storage's 'Import existing logical drives' option ...")
            FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_IMPORT_EXISTING_LOGICAL_DRIVES, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def select_boot_drive_by_text(cls, boot_drive, timeout=5, fail_if_false=True):
            logger.debug("select Local Storage's 'Boot drive' as '%s' ..." % boot_drive)
            locator = cls.e.ID_CHECKBOX_LOCAL_BOOT_DRIVE % boot_drive
            ui_lib.scroll_into_view(locator)
            FusionUIBase.wait_for_checkbox_and_select(locator, timeout=timeout, fail_if_false=fail_if_false)
            # skipped validating test data since candidate values of 'Boot drive' can be dynamically added by Create Logical Drive
            # logger.debug("validating test data '%s' for Local Storage's 'Boot drive' ..." % boot_drive)
            # if FusionUIBase.is_test_data_valid(boot_drive, 'Local_Storage_Boot_Drive'):
            #     logger.debug("select Local Storage's 'Boot drive' as '%s' ..." % boot_drive)
            #     FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_BOOT_DRIVE, boot_drive, timeout=timeout)
            # else:
            #     msg = "<test data invalid> '%s' for Local Storage's 'Boot drive' is NOT valid" % boot_drive
            #     logger.warn(msg)
            #     ui_lib.fail_test(msg)

        class LogicalDrive(object):
            e = GeneralServerProfilesElements.LocalStorage.LogicalDrive

            @classmethod
            def verify_logical_drive_exist(cls, drive_name, timeout=5, fail_if_false=True):
                logger.debug("verify if logical drive '%s' already exists ..." % drive_name)
                if ui_lib.is_visible(cls.e.ID_TABLE_LOGICAL_DRIVE.format(drive_name), timeout=timeout):
                    logger.debug("logical drive '%s' is successfully verified visible with in %s second(s)" % (drive_name, timeout))
                    return True
                else:
                    msg = "logical drive '%s' is NOT successfully verified visible with in %s second(s)" % (drive_name, timeout)
                    logger.warn(msg)
                    if fail_if_false:
                        ui_lib.fail_test(msg)
                    else:
                        return False

            @classmethod
            def verify_logical_drive_not_exist(cls, drive_name, timeout=5, fail_if_false=True):
                logger.debug("verify if logical drive '%s' does NOT exist ..." % drive_name)
                if not ui_lib.is_visible(cls.e.ID_TABLE_LOGICAL_DRIVE.format(drive_name), timeout=timeout):
                    logger.debug("logical drive '%s' is successfully verified invisible with in %s second(s)" % (drive_name, timeout))
                    return True
                else:
                    msg = "logical drive '%s' is NOT successfully verified invisible with in %s second(s)" % (drive_name, timeout)
                    logger.warn(msg)
                    if fail_if_false:
                        ui_lib.fail_test(msg)
                    else:
                        return False

            @classmethod
            def click_create_logical_drive_button(cls, timeout=5, fail_if_false=True):
                logger.debug("click button 'Create logical drive' ...")
                ui_lib.move_to_element_and_click(GeneralServerProfilesElements.LocalStorage.ID_TITLE_EDIT_INTEGRATED_CONTROLLER, GeneralServerProfilesElements.LocalStorage.ID_TITLE_EDIT_INTEGRATED_CONTROLLER)
                ui_lib.wait_for_element_visible(cls.e.ID_BUTTON_CREATE_LOGICAL_DRIVE, timeout=timeout, fail_if_false=True)
                ui_lib.move_to_element_and_click(cls.e.ID_BUTTON_CREATE_LOGICAL_DRIVE, cls.e.ID_BUTTON_CREATE_LOGICAL_DRIVE)

            @classmethod
            def set(cls, logical_drives_obj, fail_if_false=True):
                cls.create(logical_drives_obj.Create, fail_if_false=fail_if_false) if str(getattr(logical_drives_obj, 'Create', [])) != '[]' else None
                cls.delete(logical_drives_obj.Delete, fail_if_false=fail_if_false) if str(getattr(logical_drives_obj, 'Delete', [])) != '[]' else None

            @classmethod
            def set_jbod(cls, logical_jbod_obj, fail_if_false=True):
                cls.create_jbod(logical_jbod_obj.Create, fail_if_false=fail_if_false) if str(getattr(logical_jbod_obj, 'Create', [])) != '[]' else None
                cls.delete_jbod(logical_jbod_obj.Delete, fail_if_false=fail_if_false) if str(getattr(logical_jbod_obj, 'Delete', [])) != '[]' else None

            @classmethod
            def create_jbod(cls, jbods, fail_if_false=True):
                logger.info("start creating logical jbod ...")
                logger.debug("start creating logical jbod for '<%s>' ..." % jbods, also_console=False)
                total = len(jbods)
                for n, jbod in enumerate(jbods):
                    logger.info("--- <logical jbod> ---: {2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
                    logger.info("adding a logical jbod with name '%s' ..." % jbod.name)
                    logger.debug("test data for logical jbod '<%s>' is found: '<%s>'" % (jbod.name, jbod), also_console=False)

                    if cls.verify_logical_drive_not_exist(jbod.name, fail_if_false=False) is False:
                        logger.warn("logical jbod '%s' already exists, skipped ..." % jbod.name)
                        continue

                    cls.click_create_logical_drive_button()
                    cls.wait_create_logical_drive_dialog_shown()

                    cls.input_name(jbod.name)
                    if getattr(jbod, 'RAIDLevel', None) is not None:
                        cls.select_raid_level_by_text(jbod.RAIDLevel, fail_if_false=True)
                    cls.input_number_of_physical_drives(jbod.NumberOfPhysicalDrives)
                    cls.input_max_drive_size(jbod.maxSize, fail_if_false=True)
                    cls.input_min_drive_size(jbod.minSize, fail_if_false=True)
                    cls.select_drive_technology_by_text(jbod.DriveTechnology, fail_if_false=True)
                    cls.click_create_button(timeout=5)

            @classmethod
            def delete_jbod(cls, jbods, timeout=5, fail_if_false=True):
                logger.debug("start deleting logical jbod ...")
                logger.debug("start deleting logical jbod for '<%s>' ..." % jbods, also_console=False)
                total = len(jbods)
                for n, drive in enumerate(jbods):
                    logger.info("--- <delete logical jbod> ---: {2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
                    logger.info("deleting a logical jbod with name '%s' ..." % drive.name)
                    logger.debug("test data for logical drive '<%s>' is found: '<%s>'" % (drive.name, drive), also_console=False)

                    if cls.verify_logical_drive_exist(drive.name) is False:
                        logger.warn("logical jbod '%s' does NOT exist, skipped ..." % drive.name)
                        continue
                    logger.debug("deleting logical jbod %s " % drive.name)
                    ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_DELETE_LOGICAL_DRIVE_BY_NAME % drive.name, timeout=timeout, fail_if_false=fail_if_false)
                    if cls.verify_logical_drive_not_exist(drive.name) is True:
                        logger.debug("logical drive '%s' is successfully deleted" % drive.name)
                    else:
                        msg = "failed to delete logical drive '%s'" % drive.name
                        ui_lib.fail_test(msg)

            @classmethod
            def input_min_drive_size(cls, size, timeout=10, fail_if_false=True):
                logger.debug("input Logical JBOD's 'minimum size' as '%s'" % size)
                ui_lib.wait_for_element_and_click(cls.e.ID_INPUT_MIN_DRIVE_SIZE, timeout, fail_if_false)
                ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_MIN_DRIVE_SIZE, size, timeout=timeout, fail_if_false=fail_if_false)
                cls.click_dialog_title(timeout=2)
                if ui_lib.wait_for_element_class(cls.e.ID_INPUT_MIN_DRIVE_SIZE, 'hp-error', timeout=1):
                    msg = "<entry invalid>: entered value '%s' for Logical JBOD's 'minimum size' is INVALID, \n" % size
                    if ui_lib.is_visible(cls.e.ID_ERR_MSG_NUMBER_OF_PHYSICAL_DRIVES, timeout=1):
                        msg += "error message from UI is: \n<%s>" % FusionUIBase.get_text(cls.e.ID_ERR_MSG_NUMBER_OF_PHYSICAL_DRIVES)
                    else:
                        msg += "this could be caused by giving an empty value to a required field"
                    logger.warn(msg)
                    ui_lib.fail_test(msg)

            @classmethod
            def input_max_drive_size(cls, size, timeout=10, fail_if_false=True):
                logger.debug("input Logical Drive's 'maximum size' as '%s'" % size)
                ui_lib.wait_for_element_and_click(cls.e.ID_INPUT_MAX_DRIVE_SIZE, timeout, fail_if_false)
                ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_MAX_DRIVE_SIZE, size, timeout=timeout, fail_if_false=fail_if_false)
                cls.click_dialog_title(timeout=2)
                if ui_lib.wait_for_element_class(cls.e.ID_INPUT_MAX_DRIVE_SIZE, 'hp-error', timeout=1):
                    msg = "<entry invalid>: entered value '%s' for Logical JBOD's 'maximum size' is INVALID, \n" % size
                    if ui_lib.is_visible(cls.e.ID_ERR_MSG_NUMBER_OF_PHYSICAL_DRIVES, timeout=1):
                        msg += "error message from UI is: \n<%s>" % FusionUIBase.get_text(cls.e.ID_ERR_MSG_NUMBER_OF_PHYSICAL_DRIVES)
                    else:
                        msg += "this could be caused by giving an empty value to a required field"
                    logger.warn(msg)
                    ui_lib.fail_test(msg)

            @classmethod
            def create(cls, drives, fail_if_false=True):
                logger.info("start creating logical drives ...")
                logger.debug("start creating logical drives for '<%s>' ..." % drives, also_console=False)
                total = len(drives)
                created = 0
                already_exists = 0
                for n, drive in enumerate(drives):
                    logger.info("--- <logical drives> ---: {2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
                    logger.info("adding a logical drive with name '%s' ..." % drive.name)
                    logger.debug("test data for logical drive '<%s>' is found: '<%s>'" % (drive.name, drive), also_console=False)

                    if cls.verify_logical_drive_not_exist(drive.name, fail_if_false=False) is False:
                        logger.warn("logical drive '%s' already exists, skipped ..." % drive.name)
                        already_exists += 1
                        continue

                    cls.click_create_logical_drive_button()
                    cls.wait_create_logical_drive_dialog_shown()

                    cls.input_name(drive.name)
                    cls.select_raid_level_by_text(drive.RAIDLevel, fail_if_false=True)
                    cls.input_number_of_physical_drives(drive.NumberOfPhysicalDrives)
                    cls.select_drive_technology_by_text(drive.DriveTechnology, fail_if_false=True)

                    cls.click_create_button(timeout=5)

                    if cls.verify_created_logical_drive(drive) is False:
                        msg = "failed for creating Logical Drive '%s'" % drive.name
                        return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)
                    else:
                        created += 1
                        logger.info("logical drive '%s' is successfully created" % drive.name)

                logger.info("{0} == Summary == {0}".format('-' * 14))
                if total - already_exists == 0:
                    logger.warn("no logical drives to create! all %s logical drive(s) is already existing, test is considered PASS" % already_exists)
                    return True
                else:
                    if created < total:
                        logger.warn("not all of the logical drive(s) is successfully created - %s out of %s created " % (created, total))
                        if created + already_exists == total:
                            logger.warn("%s already existing logical drive(s) is skipped, test is considered PASS" % already_exists)
                            return True
                        else:
                            logger.warn("%s already existing logical drive(s) is skipped, %s logical drive(s) left is failed being created " % (already_exists, total - created - already_exists))
                            return False

                logger.info("all logical drive(s) is successfully created - %s out of %s " % (created, total))
                return True

            @classmethod
            def delete(cls, drives, timeout=5, fail_if_false=True):
                logger.debug("start deleting logical drives ...")
                logger.debug("start deleting logical drives for '<%s>' ..." % drives, also_console=False)
                total = len(drives)
                deleted = 0
                not_exists = 0
                for n, drive in enumerate(drives):
                    logger.info("--- <delete logical drives> ---: {2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
                    logger.info("adding a logical drive with name '%s' ..." % drive.name)
                    logger.debug("test data for logical drive '<%s>' is found: '<%s>'" % (drive.name, drive), also_console=False)

                    if cls.verify_logical_drive_exist(drive.name) is False:
                        logger.warn("logical drive '%s' does NOT exist, skipped ..." % drive.name)
                        not_exists += 1
                        continue

                    ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_DELETE_LOGICAL_DRIVE_BY_NAME % drive.name, timeout=timeout, fail_if_false=fail_if_false)
                    if cls.verify_logical_drive_not_exist(drive.name) is True:
                        logger.debug("logical drive '%s' is successfully deleted" % drive.name)
                        deleted += 1
                    else:
                        msg = "failed to delete logical drive '%s'" % drive.name
                        return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

                logger.info("{0} == Summary == {0}".format('-' * 14))
                if total - not_exists == 0:
                    logger.warn("no logical drive to delete! all %s logical drive(s) is NOT existing, test is considered PASS" % not_exists)
                    return True
                else:
                    if deleted < total:
                        logger.warn("not all of the logical drive(s) is successfully deleted - %s out of %s deleted" % (deleted, total))
                        if deleted + not_exists == total:
                            logger.warn("%s not-existing logical drive(s) is skipped, test is considered PASS" % not_exists)
                            return True
                        else:
                            logger.warn("%s not-existing logical drive(s) is skipped, %s left is failed being deleted" % (not_exists, total - deleted - not_exists))
                            return False

                logger.info("all logical drive(s) is successfully deleted - %s out of %s " % (deleted, total))
                return True

            @classmethod
            @TakeScreenShotWhenReturnFalseDeco
            def wait_create_logical_drive_dialog_shown(cls, timeout=5, fail_if_false=True):
                logger.debug("waiting for dialog 'Create Logical Drive' to show up ...")
                if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG, timeout=timeout, fail_if_false=fail_if_false):
                    logger.debug("dialog 'Create Logical Drive' successfully showed up")
                    return True
                else:
                    msg = "failed to wait for dialog 'Create Logical Drive' to show up"
                    return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

            @classmethod
            def input_name(cls, logical_drive_name, timeout=5, fail_if_false=True):
                logger.debug("input Logical Drive's 'Name' as '%s'" % logical_drive_name)
                ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NAME, logical_drive_name, timeout=timeout, fail_if_false=fail_if_false)
                cls.click_dialog_title(timeout=2)
                if ui_lib.wait_for_element_class(cls.e.ID_INPUT_NAME, 'hp-error', timeout=1):
                    msg = "<entry invalid>: entered value '%s' for Logical Drive's 'Name' is INVALID, \n" % logical_drive_name
                    if ui_lib.is_visible(cls.e.ID_ERR_MSG_NAME, timeout=1):
                        msg += "error message from UI is: \n<%s>" % FusionUIBase.get_text(cls.e.ID_ERR_MSG_NAME)
                    else:
                        msg += "this could be caused by giving an empty value to a required field"

                    logger.warn(msg)
                    if fail_if_false:
                        ui_lib.fail_test(msg)
                    else:
                        return False
                return True

            @classmethod
            def select_raid_level_0(cls, timeout=5, fail_if_false=True):
                cls.select_raid_level_by_text('RAID 0', timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def select_raid_level_1(cls, timeout=5, fail_if_false=True):
                cls.select_raid_level_by_text('RAID 1', timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def select_raid_level_by_text(cls, raid_level, timeout=5, fail_if_false=True):
                logger.debug("validating test data '%s' for Logical Drive's 'RAID level' ..." % raid_level)
                if FusionUIBase.is_test_data_valid(raid_level, 'Logical_Drive_RAID_Level', fail_if_false=False):
                    logger.debug("select Logical Drive's 'Raid level' as '%s' ..." % raid_level)
                    FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_RAID_LEVEL, raid_level, timeout=timeout, fail_if_false=fail_if_false)
                else:
                    msg = "<test data invalid> '%s' for Logical Drive's 'RAID level' is NOT valid" % raid_level
                    logger.warn(msg)
                    if fail_if_false:
                        ui_lib.fail_test(msg)

            @classmethod
            def input_number_of_physical_drives(cls, number_of_drives, timeout=5, fail_if_false=True):
                logger.debug("input Logical Drive's 'Number of physical drives' as '%s'" % number_of_drives)
                ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NUMBER_OF_PHYSICAL_DRIVES, number_of_drives, timeout=timeout, fail_if_false=fail_if_false)
                cls.click_dialog_title(timeout=2)
                if ui_lib.wait_for_element_class(cls.e.ID_INPUT_NUMBER_OF_PHYSICAL_DRIVES, 'hp-error', timeout=1):
                    msg = "<entry invalid>: entered value '%s' for Logical Drive's 'Number of physical drives' is INVALID, \n" % number_of_drives
                    if ui_lib.is_visible(cls.e.ID_ERR_MSG_NUMBER_OF_PHYSICAL_DRIVES, timeout=1):
                        msg += "error message from UI is: \n<%s>" % FusionUIBase.get_text(cls.e.ID_ERR_MSG_NUMBER_OF_PHYSICAL_DRIVES)
                    else:
                        msg += "this could be caused by giving an empty value to a required field"

                    logger.warn(msg)
                    if fail_if_false:
                        ui_lib.fail_test(msg)
                    else:
                        return False
                return True

            @classmethod
            def select_drive_technology_not_specified(cls, timeout=5, fail_if_false=True):
                cls.select_drive_technology_by_text('Not specified', timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def select_drive_technology_sas_hdd(cls, timeout=5, fail_if_false=True):
                cls.select_drive_technology_by_text('SAS HDD', timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def select_drive_technology_sata_hdd(cls, timeout=5, fail_if_false=True):
                cls.select_drive_technology_by_text('SATA HDD', timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def select_drive_technology_sas_ssd(cls, timeout=5, fail_if_false=True):
                cls.select_drive_technology_by_text('SAS SSD', timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def select_drive_technology_sata_ssd(cls, timeout=5, fail_if_false=True):
                cls.select_drive_technology_by_text('SATA SSD', timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def select_drive_technology_by_text(cls, drive_technology, timeout=5, fail_if_false=True):
                logger.debug("validating test data '%s' for Logical Drive's 'Drive technology' ..." % drive_technology)
                if FusionUIBase.is_test_data_valid(drive_technology, 'Logical_Drive_Drive_Technology', fail_if_false=False):
                    logger.debug("select Logical Drive's 'Drive technology' as '%s' ..." % drive_technology)
                    FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_DRIVE_TECHNOLOGY, drive_technology, timeout=timeout, fail_if_false=fail_if_false)
                else:
                    msg = "<test data invalid> '%s' for Logical Drive's 'Drive technology' is NOT valid" % drive_technology
                    logger.warn(msg)
                    if fail_if_false:
                        ui_lib.fail_test(msg)

            @classmethod
            def click_dialog_title(cls, timeout=5, fail_if_false=True):
                logger.debug("click dialog title 'Create Logical Drive' to blur out of input control to let entry-validate-error-msg show up ...")
                ui_lib.wait_for_element_and_click(cls.e.ID_DIALOG_TITLE, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def click_create_button(cls, timeout=5, fail_if_false=True):
                logger.debug("click button 'Create' (Create Logical Drive) ...")
                ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def click_create_plus_button(cls, timeout=5, fail_if_false=True):
                logger.debug("click button 'Create+' (Create Logical Drive) ...")
                ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_PLUS, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def click_cancel_button(cls, timeout=5, fail_if_false=True):
                logger.debug("click button 'Cancel' (Create Logical Drive) ...")
                ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def verify_created_logical_drive(cls, logical_drive, timeout=5, fail_if_false=True):
                logger.debug("verifying the created logical drive '%s' (Create Logical Drive) ..." % logical_drive, also_console=False)
                return True

    class SANStorage(object):
        e = GeneralServerProfilesElements.SANStorage

        @classmethod
        def tick_manage_san_storage(cls, timeout=5, fail_if_false=True):
            logger.debug("turn on SAN Storage's 'Manage SAN Storage' option ...")
            FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_MANAGE_SAN_STORAGE, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def untick_manage_san_storage(cls, timeout=5, fail_if_false=True):
            logger.debug("turn off SAN Storage's 'Manage SAN Storage' option ...")
            FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_MANAGE_SAN_STORAGE, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def select_host_os_type_by_text(cls, os_type, timeout=5, fail_if_false=True):
            logger.debug("validating test data '%s' for SAN Storage's 'Host OS Type' ..." % os_type)
            if FusionUIBase.is_test_data_valid(os_type, 'SAN_Storage_Host_OS_Type', fail_if_false=False):
                logger.debug("select SAN Storage's 'Host OS Type' as '%s' ..." % os_type)
                FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_HOST_OS_TYPE, os_type, timeout=timeout, fail_if_false=fail_if_false)
            else:
                msg = "<test data invalid> '%s' for SAN Storage's 'Host OS Type' is NOT valid" % os_type
                logger.warn(msg)
                if fail_if_false:
                    ui_lib.fail_test(msg)

        @classmethod
        def set(cls, san_storage, fail_if_false=True):
            logger.info("change to 'SAN Storage' view and start setting options and adding volumes ...")
            FusionUIBase.select_view_by_name('SAN Storage')

            if getattr(san_storage, 'Manage', None) is not None:
                if san_storage.Manage.lower() == 'false':
                    cls.untick_manage_san_storage()
                    return
            cls.tick_manage_san_storage()
            cls.select_host_os_type_by_text(san_storage.osType, fail_if_false=True) if getattr(san_storage, 'osType', None) is not None else None

            if getattr(san_storage, 'Volumes', None) is not None:
                logger.debug("list of volume <Volumes/> found: <%s>" % san_storage.Volumes, also_console=False)
                cls.Volume.set(san_storage.Volumes, fail_if_false=fail_if_false)

        class Volume(object):
            e = GeneralServerProfilesElements.SANStorage.Volume

            @classmethod
            def verify_volume_exist(cls, volume_name, timeout=5, fail_if_false=True):
                logger.debug("verify volume '%s' should exist ..." % volume_name)
                if ui_lib.is_visible(cls.e.ID_TABLE_VOLUME.format(volume_name), timeout=timeout, fail_if_false=fail_if_false):
                    logger.debug("volume '%s' is successfully verified visible with in %s second(s)" % (volume_name, timeout))
                    return True
                else:
                    msg = "volume '%s' is NOT successfully verified visible with in %s second(s)" % (volume_name, timeout)
                    return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

            @classmethod
            def verify_volume_not_exist(cls, volume_name, timeout=5, fail_if_false=True):
                logger.debug("verify volume '%s' should NOT exist ..." % volume_name)
                if not ui_lib.is_visible(cls.e.ID_TABLE_VOLUME.format(volume_name), timeout=timeout, fail_if_false=fail_if_false):
                    logger.debug("volume '%s' is successfully verified invisible with in %s second(s)" % (volume_name, timeout))
                    return True
                else:
                    msg = "volume '%s' is NOT successfully verified invisible with in %s second(s)" % (volume_name, timeout)
                    return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

            @classmethod
            def set(cls, volumes_obj, fail_if_false=True):
                cls.add(volumes_obj.Add, fail_if_false=fail_if_false) if str(getattr(volumes_obj, 'Add', [])) != '[]' else None
                cls.edit(volumes_obj.Edit, fail_if_false=fail_if_false) if str(getattr(volumes_obj, 'Edit', [])) != '[]' else None
                cls.delete(volumes_obj.Delete, fail_if_false=fail_if_false) if str(getattr(volumes_obj, 'Delete', [])) != '[]' else None

            @classmethod
            def click_add_volume_button(cls, timeout=5, fail_if_false=True):
                logger.debug("click button 'Add Volume' ...")
                ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_VOLUME, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def add(cls, volumes, timeout=8, fail_if_false=True):
                logger.debug("start adding volumes ...")
                total = len(volumes)
                added = 0
                already_exists = 0
                for n, volume in enumerate(volumes):
                    logger.info("--- <add volumes> ---: {2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
                    logger.info("adding a volume with name '%s' ..." % volume.name)
                    logger.debug("test data for volume '<%s>' is found: '<%s>'" % (volume.name, volume), also_console=False)
                    if cls.verify_volume_not_exist(volume.name, fail_if_false=False) is False:
                        logger.warn("volume '%s' already exists, skipped ..." % volume.name)
                        already_exists += 1
                        continue

                    cls.click_add_volume_button()
                    cls.wait_add_or_edit_volume_dialog_shown()

                    if getattr(volume, 'type', None) is not None:
                        cls.select_type_by_text(volume.type, fail_if_false=True)
                    else:
                        msg = "<test data missing>: attribute 'type' missing for volume '%s'" % volume.name
                        return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

                    boot = getattr(volume, 'boot', '')
                    lun = getattr(volume, 'LUN', '')
                    if FusionUIBase.is_test_data_valid(getattr(volume, 'LUN', ''), 'SAN_Storage_Volume_LUN', fail_if_false=False) is False:
                        msg = "<test data invalid> '%s' for Volume's 'LUN' is NOT valid - " \
                              "should be either 'Auto' or 'Manual' (and put numeric value in attribute 'LUNManual', LUNManual = '1/2/3', if LUN = 'Manual')" % lun
                        logger.warn(msg)
                        if fail_if_false:
                            ui_lib.fail_test(msg)

                    if volume.type.lower() == 'existing volume':
                        cls.input_select_existing_volume_name(getattr(volume, 'name', ''), timeout=timeout, fail_if_false=fail_if_false)
                        cls.select_boot_as_true(timeout=timeout, fail_if_false=fail_if_false) if boot.lower() == 'true' else None
                        cls.select_boot_as_false(timeout=timeout, fail_if_false=fail_if_false) if boot.lower() == 'false' else None
                        cls.tick_lun_as_auto(timeout=timeout, fail_if_false=fail_if_false) if lun.lower() == 'auto' else None
                        cls.tick_lun_as_manual(timeout=timeout, fail_if_false=fail_if_false) if lun.lower() == 'manual' else None
                        cls.input_lun_manual(getattr(volume, 'LUNManual', ''), timeout=timeout, fail_if_false=fail_if_false) if lun.lower() == 'manual' else None
                        cls.StoragePath.set(volume.StoragePaths, fail_if_false=fail_if_false) if str(getattr(volume, 'StoragePaths', '[]')) != '[]' else None
                    elif volume.type.lower() == 'new volume':
                        cls.input_new_volume_name(getattr(volume, 'name', ''), timeout=timeout, fail_if_false=fail_if_false)
                        cls.input_new_volume_description(getattr(volume, 'Description', ''), timeout=timeout, fail_if_false=fail_if_false)
                        cls.tick_lun_as_auto(timeout=timeout, fail_if_false=fail_if_false) if lun.lower() == 'auto' else None
                        cls.tick_lun_as_manual(timeout=timeout, fail_if_false=fail_if_false) if lun.lower() == 'manual' else None
                        cls.input_lun_manual(getattr(volume, 'LUNManual', ''), timeout=timeout, fail_if_false=fail_if_false) if lun.lower() == 'manual' else None
                        cls.input_select_new_volume_storage_pool(getattr(volume, 'StoragePool', ''), timeout=timeout, fail_if_false=fail_if_false)
                        cls.input_new_volume_capacity(getattr(volume, 'Capacity', ''), timeout=timeout, fail_if_false=fail_if_false)
                        cls.select_new_volume_provisioning_thin(timeout=timeout, fail_if_false=fail_if_false) if getattr(volume, 'Provisioning', '').lower() == 'thin' else None
                        cls.select_new_volume_provisioning_full(timeout=timeout, fail_if_false=fail_if_false) if getattr(volume, 'Provisioning', '').lower() == 'full' else None
                        cls.tick_new_volume_permanent(timeout=timeout, fail_if_false=fail_if_false) if getattr(volume, 'Permanent', '').lower() == 'true' else None
                        cls.untick_new_volume_permanent(timeout=timeout, fail_if_false=fail_if_false) if getattr(volume, 'Permanent', '').lower() == 'false' else None
                        cls.StoragePath.set(volume.StoragePaths, fail_if_false=fail_if_false) if str(getattr(volume, 'StoragePaths', '[]')) != '[]' else None

                    cls.click_add_button()

                    status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10, form_id=cls.e.ID_FORM_VOLUME)
                    if status is True:
                        logger.warn("unexpected warning occurred: %s" % msg)
                        logger.warn("Clicking OK to proceed with warnings")
                        cls.click_add_button()
                        logger.warn(msg)

                    if cls.verify_added_volume(volume) is False:
                        msg = "failed to add volume '%s'" % volume.name
                        logger.warn(msg)
                        if fail_if_false:
                            ui_lib.fail_test(msg)
                        else:
                            return False
                    else:
                        added += 1
                        logger.info("volume '%s' is successfully added" % volume.name)

                    if getattr(volume, 'boot', '').lower() == 'true':
                        cls.tick_boot_option_by_given_volume_name(volume.name, volume.type, timeout=timeout, fail_if_false=fail_if_false)
                    elif getattr(volume, 'boot', '').lower() == 'false':
                        cls.untick_boot_option_by_given_volume_name(volume.name, volume.type, timeout=timeout, fail_if_false=fail_if_false)

                logger.info("{0} == Summary == {0}".format('-' * 14))
                if total - already_exists == 0:
                    logger.warn("no volumes to add! all %s volume(s) is already existing, test is considered PASS" % already_exists)
                    return True
                else:
                    if added < total:
                        logger.warn("not all of the volume(s) is successfully added - %s out of %s added " % (added, total))
                        if added + already_exists == total:
                            logger.warn("%s already existing volume(s) is skipped, test is considered PASS" % already_exists)
                            return True
                        else:
                            logger.warn("%s already existing volume(s) is skipped, %s left is failed being added " % (already_exists, total - added - already_exists))
                            return False

                logger.info("all volume(s) is successfully added - %s out of %s " % (added, total))
                return True

            @classmethod
            def click_delete_volume_button(cls, volume_name, timeout=5, fail_if_false=True):
                logger.debug("click delete button for removing volume '%s' ..." % volume_name)
                ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_DELETE_VOLUME_BY_NAME.format(volume_name), timeout=timeout, fail_if_false=fail_if_false)

                if ui_lib.is_visible(cls.e.ID_BUTTON_DELETE_CONFIRM):
                    cls.click_delete_confirm_button()

            @classmethod
            def click_delete_confirm_button(cls, timeout=5):
                logger.debug("select option 'Yes, delete'")
                FusionUIBase.wait_for_element_and_click(cls.e.ID_BUTTON_DELETE_CONFIRM, timeout)

            @classmethod
            def delete(cls, volumes, timeout=5, fail_if_false=True):
                logger.debug("start deleting volumes ...")
                total = len(volumes)
                deleted = 0
                not_exists = 0
                for n, volume in enumerate(volumes):
                    logger.info("--- <delete volume(s)> ---: {2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
                    logger.info("deleting volume '%s' ..." % volume.name)
                    logger.debug("test data for volume '%s' is found: '<%s>'" % (volume.name, volume), also_console=False)
                    if cls.verify_volume_exist(volume.name, fail_if_false=False) is False:
                        logger.warn("volume '%s' does NOT exist, skipped ..." % volume.name)
                        not_exists += 1
                        continue

                    cls.click_delete_volume_button(volume.name, timeout=timeout, fail_if_false=fail_if_false)

                    if cls.verify_volume_not_exist(volume.name, fail_if_false=False) is True:
                        logger.debug("volume '%s' is successfully deleted" % volume.name)
                        deleted += 1
                    else:
                        msg = "failed to delete volume '%s'" % volume.name
                        return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

                logger.info("{0} == Summary == {0}".format('-' * 14))
                if total - not_exists == 0:
                    logger.warn("no volume to delete! all %s volume(s) is NOT existing, test is considered PASS" % not_exists)
                    return True
                else:
                    if deleted < total:
                        logger.warn("not all of the volume(s) is successfully deleted - %s out of %s deleted" % (deleted, total))
                        if deleted + not_exists == total:
                            logger.warn("%s not-existing volume(s) is skipped, test is considered PASS" % not_exists)
                            return True
                        else:
                            logger.warn("%s not-existing volume(s) is skipped, %s left is failed being deleted" % (not_exists, total - deleted - not_exists))
                            return False

                logger.info("all volume(s) is successfully deleted - %s out of %s " % (deleted, total))
                return True

            @classmethod
            def click_edit_volume_button(cls, volume_name, timeout=5, fail_if_false=True):
                logger.debug("click edit button for editing volume '%s' ..." % volume_name)
                ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_VOLUME_BY_NAME % volume_name, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def edit(cls, volumes, timeout=5, fail_if_false=True):

                logger.debug("start editing volumes ...")
                total = len(volumes)
                edited = 0
                not_exists = 0
                for n, volume in enumerate(volumes):
                    logger.info("--- <edit volumes> ---: {2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
                    logger.info("adding a volume with name '%s' ..." % volume.name)
                    logger.debug("test data for volume '<%s>' is found: '<%s>'" % (volume.name, volume), also_console=False)
                    if cls.verify_volume_exist(volume.name, fail_if_false=False) is False:
                        logger.warn("volume '%s' does NOT exist, skipped ..." % volume.name)
                        not_exists += 1
                        continue

                    cls.click_edit_volume_button(volume.name, timeout=timeout, fail_if_false=fail_if_false)
                    cls.wait_add_or_edit_volume_dialog_shown()

                    cls.tick_lun_as_auto(timeout=timeout, fail_if_false=fail_if_false) if getattr(volume, 'LUN', '').lower() == 'auto' else None
                    cls.tick_lun_as_manual(timeout=timeout, fail_if_false=fail_if_false) if getattr(volume, 'LUN', '').lower() == 'manual' else None
                    cls.input_lun_manual(getattr(volume, 'LUNManual', ''), timeout=timeout, fail_if_false=fail_if_false) if getattr(volume, 'LUN', '').lower() == 'manual' else None
                    cls.StoragePath.set(volume.StoragePaths, fail_if_false=fail_if_false) if str(getattr(volume, 'StoragePaths', '[]')) != '[]' else None

                    cls.click_ok_button()
                    if getattr(volume, 'one_path', '').lower() == "true":
                        logger.debug("There is only one path as expected, click [ OK ] button again")
                        cls.click_ok_button()

                    status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10, form_id=cls.e.ID_FORM_VOLUME)
                    if status is True:
                        logger.warn("unexpected error occurred: %s" % msg)
                        ui_lib.fail_test(msg)

                    if cls.verify_added_volume(volume) is False:
                        msg = "failed to add volume '%s'" % volume.name
                        return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)
                    else:
                        edited += 1
                        logger.info("volume '%s' is successfully edited" % volume.name)

                logger.info("{0} == Summary == {0}".format('-' * 14))
                if total - not_exists == 0:
                    logger.warn("no volumes to add! all %s volume(s) is NOT existing, test is considered PASS" % not_exists)
                    return True
                else:
                    if edited < total:
                        logger.warn("not all of the volume(s) is successfully edited - %s out of %s edited " % (edited, total))
                        if edited + not_exists == total:
                            logger.warn("%s not-existing volume(s) is skipped, test is considered PASS" % not_exists)
                            return True
                        else:
                            logger.warn("%s not-existing volume(s) is skipped, %s left is failed being edited " % (not_exists, total - edited - not_exists))
                            return False

                logger.info("all volume(s) is successfully edited - %s out of %s " % (edited, total))
                return True

            @classmethod
            @TakeScreenShotWhenReturnFalseDeco
            def wait_add_or_edit_volume_dialog_shown(cls, timeout=5, fail_if_false=True):
                logger.info("waiting for dialog 'Add/Edit Volume' to show up ...")
                if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG, timeout=timeout, fail_if_false=fail_if_false):
                    logger.debug("dialog 'Add/Edit Volume' successfully showed up")
                    return True
                else:
                    msg = "failed to wait for dialog 'Add/Edit Volume' to show up"
                    return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

            @classmethod
            def select_type_existing_volume(cls, timeout=5, fail_if_false=True):
                cls.select_type_by_text('Existing volume', timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def select_type_new_volume(cls, timeout=5, fail_if_false=True):
                cls.select_type_by_text('New volume', timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def select_type_by_text(cls, volume_type, timeout=5, fail_if_false=True):
                logger.debug("validating test data '%s' for Volume's 'Type' ..." % volume_type)
                if FusionUIBase.is_test_data_valid(volume_type, 'SAN_Storage_Volume_Type', fail_if_false=False):
                    logger.debug("select Volume's 'Type' as '%s' ..." % volume_type)
                    FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_TYPE, volume_type, timeout=timeout, fail_if_false=fail_if_false)
                else:
                    msg = "<test data invalid> '%s' for Volume's 'Type' is NOT valid" % volume_type
                    logger.warn(msg)
                    if fail_if_false:
                        ui_lib.fail_test(msg)

            @classmethod
            def input_new_volume_name(cls, volume_name, timeout=5, fail_if_false=True):
                logger.debug("input Volume's 'Volume name' as '%s'" % volume_name)
                ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NEW_VOLUME_NAME, volume_name, timeout=timeout, fail_if_false=fail_if_false)
                cls.click_dialog_title(timeout=2)
                if ui_lib.wait_for_element_class(cls.e.ID_INPUT_NEW_VOLUME_NAME, 'hp-error', timeout=1):
                    msg = "<entry invalid>: entered value '%s' for Volume's 'Volume name' is INVALID, \n" % volume_name
                    if ui_lib.is_visible(cls.e.ID_ERR_MSG_NEW_VOLUME_NAME, timeout=1):
                        msg += "error message from UI is: \n<%s>" % FusionUIBase.get_text(cls.e.ID_ERR_MSG_NEW_VOLUME_NAME)
                    else:
                        msg += "this could be caused by giving an empty value to a required field"

                    return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)
                return True

            @classmethod
            def input_new_volume_description(cls, volume_description, timeout=5, fail_if_false=True):
                logger.debug("input Volume's 'Description' as '%s'" % volume_description)
                ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NEW_VOLUME_DESCRIPTION, volume_description, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            @TakeScreenShotWhenReturnFalseDeco
            def input_select_existing_volume_name(cls, volume_name, timeout=5, fail_if_false=True):
                logger.debug("input and select 'Volume name' of existing volume as '%s'" % volume_name)

                counter = 0
                while counter < 3:
                    ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_EXISTING_VOLUME_NAME, volume_name, timeout=timeout, fail_if_false=fail_if_false)

                    if ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_EXISTING_VOLUME_NAME % volume_name, timeout=timeout + counter, fail_if_false=False):
                        logger.debug("selected '%s' in existing volumes' drop-down list as 'Volume name'" % volume_name)
                        break
                    else:
                        logger.warn("not able to see '%s' in existing volumes' drop-down list within %s second(s), retrying ..." % (volume_name, timeout + counter))
                        counter += 1
                else:
                    return FusionUIBase.fail_test_or_return_false("failed %s times to wait for '%s' to show up in existing volumes' drop-down list" % (counter + 1, volume_name), fail_if_false=fail_if_false)

                return True

            @classmethod
            def select_boot_as_true(cls, timeout=5, fail_if_false=True):
                logger.debug("select Volume's 'Boot' as 'True' ...")
                ui_lib.wait_for_element_and_click(cls.e.ID_INPUT_BOOT_TRUE, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def select_boot_as_false(cls, timeout=5, fail_if_false=True):
                logger.debug("select Volume's 'Boot' as 'False' ...")
                ui_lib.wait_for_element_and_click(cls.e.ID_INPUT_BOOT_FALSE, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def tick_lun_as_auto(cls, timeout=5, fail_if_false=True):
                logger.debug("select Volume's 'LUN' as 'Auto' ...")
                ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_LUN_AUTO, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def tick_lun_as_manual(cls, timeout=5, fail_if_false=True):
                logger.debug("select Volume's 'LUN' as 'Manual' ...")
                ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_LUN_MANUAL, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def input_lun_manual(cls, volume_lun_manual, timeout=5, fail_if_false=True):
                logger.debug("input Volume's 'LUN - Manual' as '%s'" % volume_lun_manual)
                ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_LUN_MANUAL, volume_lun_manual, timeout=timeout, fail_if_false=fail_if_false)
                cls.click_dialog_title(timeout=2)
                if ui_lib.wait_for_element_class(cls.e.ID_INPUT_LUN_MANUAL, 'hp-error', timeout=1):
                    msg = "<entry invalid>: entered value '%s' for Volume's 'LUN - Manual' is INVALID, \n" % volume_lun_manual
                    if ui_lib.is_visible(cls.e.ID_ERR_MSG_LUN_MANUAL, timeout=1):
                        msg += "error message from UI is: \n<%s>" % FusionUIBase.get_text(cls.e.ID_ERR_MSG_LUN_MANUAL)
                    else:
                        msg += "this could be caused by giving an empty value to a required field"

                    return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)
                return True

            @classmethod
            @TakeScreenShotWhenReturnFalseDeco
            def input_select_new_volume_storage_pool(cls, pool_name, timeout=5, fail_if_false=True):
                logger.debug("input and select 'Storage pool' of new volume as '%s'" % pool_name)
                ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NEW_VOLUME_STORAGE_POOL, pool_name, timeout=timeout, fail_if_false=fail_if_false)
                BuiltIn().sleep(3)
                if ui_lib.is_visible(cls.e.ID_OPTION_NEW_VOLUME_STORAGE_POOL % pool_name):
                    logger.debug("select '%s' in existing storage pools' drop-down list as 'Storage pool'" % pool_name)
                    ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_NEW_VOLUME_STORAGE_POOL % pool_name, timeout=timeout, fail_if_false=fail_if_false)
                else:
                    msg = "No existing storage pool named '%s' for adding volume during creating server profile" % pool_name
                    return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

                return True

            @classmethod
            def input_new_volume_capacity(cls, volume_capacity, timeout=5, fail_if_false=True):
                logger.debug("input Volume's 'Capacity' as '%s'" % volume_capacity)
                ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NEW_VOLUME_CAPACITY, volume_capacity, timeout=timeout, fail_if_false=fail_if_false)
                cls.click_dialog_title(timeout=2)
                if ui_lib.wait_for_element_class(cls.e.ID_INPUT_NEW_VOLUME_CAPACITY, 'hp-error', timeout=1):
                    msg = "<entry invalid>: entered value '%s' for Volume's 'Capacity' is INVALID, \n" % volume_capacity
                    if ui_lib.is_visible(cls.e.ID_ERR_MSG_NEW_VOLUME_CAPACITY, timeout=1):
                        msg += "error message from UI is: \n<%s>" % FusionUIBase.get_text(cls.e.ID_ERR_MSG_NEW_VOLUME_CAPACITY)
                    else:
                        msg += "this could be caused by giving an empty value to a required field"

                    return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)
                return True

            @classmethod
            def select_new_volume_provisioning_thin(cls, timeout=5, fail_if_false=True):
                cls.select_new_volume_provisioning_by_text('Thin', timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def select_new_volume_provisioning_full(cls, timeout=5, fail_if_false=True):
                cls.select_new_volume_provisioning_by_text('Full', timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def select_new_volume_provisioning_by_text(cls, volume_provisioning, timeout=5, fail_if_false=True):
                logger.debug("validating test data '%s' for Volume's 'Provisioning' ..." % volume_provisioning)
                if FusionUIBase.is_test_data_valid(volume_provisioning, 'SAN_Storage_Volume_Provisioning', fail_if_false=False):
                    logger.debug("select Volume's 'Provisioning' as '%s' ..." % volume_provisioning)
                    FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_NEW_VOLUME_PROVISIONING, volume_provisioning, timeout=timeout, fail_if_false=fail_if_false)
                else:
                    msg = "<test data invalid> '%s' for Volume's 'Provisioning' is NOT valid" % volume_provisioning
                    logger.warn(msg)
                    if fail_if_false:
                        ui_lib.fail_test(msg)

            @classmethod
            def tick_new_volume_permanent(cls, timeout=5, fail_if_false=True):
                logger.debug("turn on Volume's 'Permanent' option ...")
                FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_NEW_VOLUME_PERMANENT, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def untick_new_volume_permanent(cls, timeout=5, fail_if_false=True):
                logger.debug("turn off Volume's 'Permanent' option ...")
                FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_NEW_VOLUME_PERMANENT, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def tick_boot_option_by_given_volume_name(cls, volume_name, volume_type, timeout=5, fail_if_false=True):
                logger.debug("turn on 'Boot' option of the volume with volume name '%s' and volume type '%s'..." % (volume_name, volume_type))
                # new volume has different element path to existing volume
                if volume_type.lower() == "existing volume":
                    locator = (cls.e.ID_CHECKBOX_BOOT_BY_EXISTING_VOLUME_NAME % volume_name)
                elif volume_type.lower() == "new volume":
                    locator = (cls.e.ID_CHECKBOX_BOOT_BY_NEW_VOLUME_NAME % volume_name)
                ui_lib.scroll_into_view(locator)
                FusionUIBase.wait_for_checkbox_and_select(locator, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def untick_boot_option_by_given_volume_name(cls, volume_name, volume_type, timeout=5, fail_if_false=True):
                logger.debug("turn off 'Boot' option of the volume with volume name '%s' and volume type '%s'..." % (volume_name, volume_type))
                # new volume has different element path to existing volume
                if volume_type.lower() == "existing volume":
                    locator = (cls.e.ID_CHECKBOX_BOOT_BY_EXISTING_VOLUME_NAME % volume_name)
                else:
                    locator = (cls.e.ID_CHECKBOX_BOOT_BY_NEW_VOLUME_NAME % volume_name)
                ui_lib.scroll_into_view(locator)
                FusionUIBase.wait_for_checkbox_and_unselect(locator, timeout=timeout, fail_if_false=fail_if_false)

            class StoragePath(object):
                e = GeneralServerProfilesElements.SANStorage.Volume.StoragePath

                @classmethod
                def verify_storage_path_exist(cls, network_name, timeout=5, fail_if_false=True):
                    logger.debug("verify if storage path with network name '%s' already exists ..." % network_name)
                    if ui_lib.is_visible(cls.e.ID_BUTTON_DELETE_STORAGE_PATH_BY_NETWORK_NAME % network_name, timeout=timeout):
                        logger.debug("storage path with network name '%s' is successfully verified visible with in %s second(s)" % (network_name, timeout))
                        return True
                    else:
                        msg = "storage path with network name '%s' is NOT successfully verified visible with in %s second(s)" % (network_name, timeout)
                        return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

                @classmethod
                def verify_storage_path_not_exist(cls, network_name, timeout=5, fail_if_false=True):
                    logger.debug("verify if storage path with network name '%s' does NOT exist ..." % network_name)
                    if not ui_lib.is_visible(cls.e.ID_BUTTON_DELETE_STORAGE_PATH_BY_NETWORK_NAME % network_name, timeout=timeout):
                        logger.debug("storage path with network name '%s' is successfully verified invisible with in %s second(s)" % (network_name, timeout))
                        return True
                    else:
                        msg = "storage path with network name '%s' is NOT successfully verified invisible with in %s second(s)" % (network_name, timeout)
                        return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

                @classmethod
                def set(cls, storage_paths_obj, fail_if_false=True):
                    # logger.debug("____________storage_paths_obj is:<%s>" % storage_paths_obj)
                    if str(getattr(storage_paths_obj, 'Add', '[]')) != '[]':
                        if not ui_lib.is_visible(cls.e.ID_BUTTON_ADD_STORAGE_PATH_DISABLED):
                            cls.add(storage_paths_obj.Add, fail_if_false=fail_if_false)
                        else:
                            # By default on UI page, there's no need to proactively add storage path for volume since they'll be automatically generated,
                            # then setting the storage path's port assignment is separated as a second step:
                            #   - click Edit button (gear icon) to open "Edit Storage Targets xxx" dialog
                            #   - select "Auto",
                            #   - or "Select target ports" and select 1 or 2 of the ports, as manual selection of target port assignment
                            cls.edit(storage_paths_obj.Add, fail_if_false=fail_if_false) if str(getattr(storage_paths_obj, 'Add', '[]')) != '[]' else None

                    cls.edit(storage_paths_obj.Edit, fail_if_false=fail_if_false) if str(getattr(storage_paths_obj, 'Edit', '[]')) != '[]' else None
                    cls.delete(storage_paths_obj.Delete, fail_if_false=fail_if_false) if str(getattr(storage_paths_obj, 'Delete', '[]')) != '[]' else None

                @classmethod
                def click_add_storage_path_button(cls, timeout=5, fail_if_false=True):
                    logger.debug("click button 'Add storage path' ...")
                    ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_STORAGE_PATH, timeout=timeout, fail_if_false=fail_if_false)

                @classmethod
                def click_remove_all_storage_path_button(cls, timeout=5, fail_if_false=True):
                    logger.debug("click button 'Remove all' ...")
                    ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_REMOVE_ALL_STORAGE_PATH, timeout=timeout, fail_if_false=fail_if_false)

                @classmethod
                def add(cls, storage_paths, timeout=5, fail_if_false=True):
                    logger.debug("start adding storage path(s) ...")
                    total = len(storage_paths)
                    already_exists = 0
                    added = 0

                    # Remove all storage path before addition
                    cls.click_remove_all_storage_path_button()

                    for n, storage_path in enumerate(storage_paths):
                        logger.info("--- <adding storage paths> ---: {2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
                        logger.info("adding a storage path with network name '%s' ..." % storage_path.network)
                        logger.debug("test data for storage path '<%s>' is found: '<%s>'" % (storage_path.network, storage_path), also_console=False)

                        if not cls.verify_storage_path_not_exist(storage_path.network):
                            logger.warn("storage path with network name '%s' already exists, skipped ..." % storage_path.network)
                            already_exists += 1
                            continue
                        cls.click_add_storage_path_button()
                        cls.wait_add_storage_path_dialog_shown()
                        cls.input_select_network(storage_path.network)
                        cls.click_add_button()
                        cls.tick_enabled_by_given_network_name(storage_path.network, timeout=timeout, fail_if_false=fail_if_false) if getattr(storage_path, 'enabled', '').lower() == 'true' else None
                        cls.untick_enabled_by_given_network_name(storage_path.network, timeout=timeout, fail_if_false=fail_if_false) if getattr(storage_path, 'enabled', '').lower() == 'false' else None
                        cls.set_target_port_assignment(storage_path) if getattr(storage_path, 'TargetPortAssignment', '').lower() in ('auto', 'manual') else None

                        if cls.verify_added_storage_path(storage_path) is False:
                            msg = "failed for adding storage path with network name '%s'" % storage_path.network
                            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)
                        else:
                            added += 1
                            logger.info("storage path with network name '%s' is successfully added" % storage_path.network)

                    logger.info("{0} == Summary == {0}".format('-' * 14))
                    if total - already_exists == 0:
                        logger.warn("no storage path to add! all %s storage path(s) is already existing, test is considered PASS" % already_exists)
                        return True
                    else:
                        if added < total:
                            logger.warn("not all of the storage path(s) is successfully added - %s out of %s added" % (added, total))
                            if added + already_exists == total:
                                logger.warn("%s already-existing storage path(s) is skipped, test is considered PASS" % already_exists)
                                return True
                            else:
                                logger.warn("%s already-existing storage path(s) is skipped, %s left is failed being added" % (already_exists, total - added - already_exists))
                                return False

                    logger.info("all storage path(s) is successfully added - %s out of %s " % (added, total))
                    return True

                @classmethod
                def verify_added_storage_path(cls, storage_path, timeout=5, fail_if_false=False):
                    logger.debug("verify if storage path with network name '%s' is successfully added ..." % storage_path.network)
                    return cls.verify_storage_path_exist(storage_path.network, timeout=timeout, fail_if_false=fail_if_false)

                @classmethod
                def edit(cls, storage_paths, timeout=5, fail_if_false=True):
                    logger.debug("start editing storage path(s) ...")
                    total = len(storage_paths)
                    not_exists = 0
                    edited = 0
                    for n, storage_path in enumerate(storage_paths):
                        logger.info("--- <editing storage paths> ---: {2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
                        logger.info("editing a storage path with network name '%s' to set its target port assignment ..." % storage_path.network)
                        logger.debug("test data for storage path '<%s>' is found: '<%s>'" % (storage_path.network, storage_path), also_console=False)

                        if not cls.verify_storage_path_exist(storage_path.network):
                            msg = "storage path with network name '%s' does NOT exist, failed to set its target port assignment" % storage_path.network
                            logger.warn(msg)
                            if fail_if_false:
                                ui_lib.fail_test(msg)
                            else:
                                not_exists += 1
                                continue

                        cls.tick_enabled_by_given_network_name(storage_path.network, timeout=timeout, fail_if_false=fail_if_false) if getattr(storage_path, 'enabled', '').lower() == 'true' else None
                        cls.untick_enabled_by_given_network_name(storage_path.network, timeout=timeout, fail_if_false=fail_if_false) if getattr(storage_path, 'enabled', '').lower() == 'false' else None
                        cls.set_target_port_assignment(storage_path) if getattr(storage_path, 'TargetPortAssignment', '').lower() in ('auto', 'manual') else None

                        if cls.verify_edited_storage_path(storage_path) is False:
                            msg = "failed to edit storage path with network name '%s' to set its target port assignment" % storage_path.network
                            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)
                        else:
                            edited += 1
                            logger.info("storage path with network name '%s' is successfully edited" % storage_path.network)

                    logger.info("{0} == Summary == {0}".format('-' * 14))
                    if total - not_exists == 0:
                        logger.warn("no storage path to edit! all %s storage path(s) is NOT existing, test is considered PASS" % not_exists)
                        return True
                    else:
                        if edited < total:
                            logger.warn("not all of the storage path(s) is successfully edited - %s out of %s edited" % (edited, total))
                            if edited + not_exists == total:
                                logger.warn("%s not-existing storage path(s) is skipped, test is considered PASS" % not_exists)
                                return True
                            else:
                                logger.warn("%s not-existing storage path(s) is skipped, %s left is failed being edited" % (not_exists, total - edited - not_exists))
                                return False

                    logger.info("all storage path(s) is successfully edited - %s out of %s " % (edited, total))
                    return True

                @classmethod
                def verify_edited_storage_path(cls, storage_path, timeout=5, fail_if_false=True):
                    # TODO: finish the verification function
                    return True

                @classmethod
                def delete(cls, storage_paths, timeout=5, fail_if_false=True):
                    logger.debug("start deleting storage path(s) ...")
                    total = len(storage_paths)
                    deleted = 0
                    not_exists = 0
                    for n, storage_path in enumerate(storage_paths):
                        logger.info("--- <deleting storage path(s)> ---: {2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
                        logger.info("deleting storage path with network name '%s' ..." % storage_path.network)
                        logger.debug("test data for storage path with network name '%s' is found: '<%s>'" % (storage_path.network, storage_path), also_console=False)
                        if not cls.verify_storage_path_exist(storage_path.network):
                            logger.warn("storage path with network name '%s' does NOT exist, skipped ..." % storage_path.network)
                            not_exists += 1
                            continue

                        cls.click_delete_button_by_given_network_name(storage_path.network, timeout=timeout, fail_if_false=fail_if_false)
                        if cls.verify_storage_path_not_exist(storage_path.network):
                            logger.debug("storage path with network name '%s' is successfully deleted" % storage_path.network)
                            deleted += 1
                        else:
                            msg = "failed to delete storage path with network name '%s'" % storage_path.network
                            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

                    logger.info("{0} == Summary == {0}".format('-' * 14))
                    if total - not_exists == 0:
                        logger.warn("no storage path to delete! all %s storage path(s) is NOT existing, test is considered PASS" % not_exists)
                        return True
                    else:
                        if deleted < total:
                            logger.warn("not all of the storage path(s) is successfully deleted - %s out of %s deleted" % (deleted, total))
                            if deleted + not_exists == total:
                                logger.warn("%s not-existing storage path(s) is skipped, test is considered PASS" % not_exists)
                                return True
                            else:
                                logger.warn("%s not-existing storage path(s) is skipped, %s left is failed being deleted" % (not_exists, total - deleted - not_exists))
                                return False

                    logger.info("all storage path(s) is successfully deleted - %s out of %s " % (deleted, total))
                    return True

                @classmethod
                def set_target_port_assignment(cls, storage_path, timeout=5, fail_if_false=True):
                    logger.debug("edit storage path with network name '%s' to set its target port assignment ..." % storage_path.network)
                    cls.click_edit_button_by_given_network_name(storage_path.network, timeout=timeout, fail_if_false=fail_if_false)
                    cls.wait_edit_storage_path_dialog_shown(storage_path.network, timeout=timeout, fail_if_false=fail_if_false)
                    cls.tick_target_port_assignment_as_auto() if getattr(storage_path, 'TargetPortAssignment', '').lower() == 'auto' else None
                    cls.tick_target_port_assignment_as_manual() if getattr(storage_path, 'TargetPortAssignment', '').lower() in ('manual', 'select target ports') else None
                    if getattr(storage_path, 'TargetPortAssignment', '').lower() in ('manual', 'select target ports'):
                        if getattr(storage_path, 'Port', None) is not None:
                            total = len(storage_path.Port)
                            for n, port in enumerate(storage_path.Port):
                                logger.info("--- <storage path's port> ---: {2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
                                logger.info("setting target port assignment for port name '%s' ..." % port.PortName)
                                logger.debug("test data for target port '%s' of storage path '<%s>' is found: '<%s>'" % (port.PortName, storage_path.network, port), also_console=False)
                                cls.tick_target_port_by_port_name(port.PortName, timeout=timeout, fail_if_false=fail_if_false) if getattr(port, 'selected', '').lower() == 'true' else None
                                cls.untick_target_port_by_port_name(port.PortName, timeout=timeout, fail_if_false=fail_if_false) if getattr(port, 'selected', '').lower() == 'false' else None
                        else:
                            msg = "<test data inconsistent>: No '<Port />' node(s) defined in test data for setting target port assignment of storage path '%s'" % storage_path.network
                            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

                    cls.click_ok_button(timeout=timeout, fail_if_false=fail_if_false)
                    status, msg = FusionUIBase.get_error_message_from_dialog(timeout=6, form_id=cls.e.ID_FORM_EDIT_STORAGE_PATH)
                    if status is True:
                        logger.warn("unexpected error occurred: %s" % msg)
                        ui_lib.fail_test(msg)

                    return True

                @classmethod
                def click_edit_button_by_given_network_name(cls, network_name, timeout=5, fail_if_false=True):
                    logger.debug("click edit button (gear icon) of the storage path with network name '%s' to edit it ..." % network_name)
                    FusionUIBase.scroll_element_into_viewpoint(cls.e.ID_BUTTON_EDIT_STORAGE_PATH_BY_NETWORK_NAME % network_name)
                    ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_STORAGE_PATH_BY_NETWORK_NAME % network_name, timeout=timeout, fail_if_false=fail_if_false)

                @classmethod
                def click_delete_button_by_given_network_name(cls, network_name, timeout=5, fail_if_false=True):
                    logger.debug("click delete button of the storage path with network name '%s' to remove it ..." % network_name)
                    FusionUIBase.scroll_element_into_viewpoint(cls.e.ID_BUTTON_DELETE_STORAGE_PATH_BY_NETWORK_NAME % network_name)
                    ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_DELETE_STORAGE_PATH_BY_NETWORK_NAME % network_name, timeout=timeout, fail_if_false=fail_if_false)

                @classmethod
                def tick_enabled_by_given_network_name(cls, network_name, timeout=5, fail_if_false=True):
                    logger.debug("turn on 'Enabled' option of the storage path with network name '%s' ..." % network_name)
                    FusionUIBase.scroll_element_into_viewpoint(cls.e.ID_CHECKBOX_ENABLE_STORAGE_PATH_BY_NETWORK_NAME % network_name)
                    FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_ENABLE_STORAGE_PATH_BY_NETWORK_NAME % network_name, timeout=timeout, fail_if_false=fail_if_false)

                @classmethod
                def untick_enabled_by_given_network_name(cls, network_name, timeout=5, fail_if_false=True):
                    logger.debug("turn off 'Enabled' option of the storage path with network name '%s' ..." % network_name)
                    FusionUIBase.scroll_element_into_viewpoint(cls.e.ID_CHECKBOX_ENABLE_STORAGE_PATH_BY_NETWORK_NAME % network_name)
                    FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_ENABLE_STORAGE_PATH_BY_NETWORK_NAME % network_name, timeout=timeout, fail_if_false=fail_if_false)

                @classmethod
                @TakeScreenShotWhenReturnFalseDeco
                def wait_add_storage_path_dialog_shown(cls, timeout=5, fail_if_false=True):
                    logger.info("waiting for dialog 'Add Storage Path' to show up ...")
                    if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_ADD, timeout=timeout, fail_if_false=fail_if_false):
                        return True
                    else:
                        msg = "failed to wait for dialog 'Add Storage Path' to show up within %s second(s)" % timeout
                        return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

                @classmethod
                @TakeScreenShotWhenReturnFalseDeco
                def wait_edit_storage_path_dialog_shown(cls, network_name, timeout=5, fail_if_false=True):
                    logger.info("waiting for dialog 'Edit Storage Targets %s' to show up ..." % network_name)
                    if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_EDIT, timeout=timeout, fail_if_false=fail_if_false):
                        return True
                    else:
                        msg = "failed to wait for dialog 'Edit Storage Targets %s' to show up within %s second(s)" % (network_name, timeout)
                        return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

                @classmethod
                def tick_target_port_assignment_as_auto(cls, timeout=5, fail_if_false=True):
                    logger.debug("select storage path's 'Targets (Port Assignment)' as 'Auto' ...")
                    ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_TARGET_PORT_ASSIGNMENT_AUTO, timeout=timeout, fail_if_false=fail_if_false)

                @classmethod
                def tick_target_port_assignment_as_manual(cls, timeout=5, fail_if_false=True):
                    logger.debug("select storage path's 'Targets (Port Assignment)' as 'Select target ports' (Manual) ...")
                    ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_TARGET_PORT_ASSIGNMENT_MANUAL, timeout=timeout, fail_if_false=fail_if_false)

                @classmethod
                def tick_target_port_by_port_name(cls, port_name, timeout=5, fail_if_false=True):
                    logger.debug("turn on 'Selected' option of target port '%s' ..." % port_name)
                    FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_PORT_SELECTED_BY_PORT_NAME % port_name, timeout=timeout, fail_if_false=fail_if_false)

                @classmethod
                def untick_target_port_by_port_name(cls, port_name, timeout=5, fail_if_false=True):
                    logger.debug("turn off 'Selected' option of target port '%s' ..." % port_name)
                    FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_PORT_SELECTED_BY_PORT_NAME % port_name, timeout=timeout, fail_if_false=fail_if_false)

                @classmethod
                def click_ok_button(cls, timeout=5, fail_if_false=True):
                    logger.debug("click 'OK' button (Edit Storage Target) ...")
                    ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_OK, timeout=timeout, fail_if_false=fail_if_false)

                @classmethod
                def click_cancel_button_for_edit_storage_path(cls, timeout=5, fail_if_false=True):
                    logger.debug("click 'Cancel' button (Edit Storage Target) ...")
                    ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL_FOR_EDIT_STORAGE_PATH, timeout=timeout, fail_if_false=fail_if_false)

                @classmethod
                def input_network(cls, network_name, timeout=5, fail_if_false=True):
                    logger.debug("input network name to search and select the network for adding storage path ...")
                    ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NETWORK_NAME_FOR_SEARCH, network_name, timeout=timeout, fail_if_false=fail_if_false)

                @classmethod
                def input_select_network(cls, network_name, timeout=5, fail_if_false=True):
                    cls.input_network(network_name=network_name, timeout=timeout, fail_if_false=fail_if_false)
                    if ui_lib.is_visible(cls.e.ID_OPTION_NETWORK_FOR_ADD_STORAGE_PATH % network_name, timeout=timeout):
                        logger.debug("click network '%s' from the search result for adding storage path ..." % network_name)
                        ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_NETWORK_FOR_ADD_STORAGE_PATH % network_name, timeout=timeout, fail_if_false=fail_if_false)
                    else:
                        msg = "No network named '%s' for adding storage path" % network_name
                        return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)
                    return True

                @classmethod
                def click_add_button(cls, timeout=5, fail_if_false=True):
                    logger.debug("click 'Add' button (Add Storage Path) ...")
                    ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD, timeout=timeout, fail_if_false=fail_if_false)

                @classmethod
                def click_add_plus_button(cls, timeout=5, fail_if_false=True):
                    logger.debug("click 'Add +' button (Add Storage Path) ...")
                    ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_PLUS, timeout=timeout, fail_if_false=fail_if_false)

                @classmethod
                def click_cancel_button_for_edit_storage_path(cls, timeout=5, fail_if_false=True):
                    logger.debug("click 'Cancel' button (Add Storage Path) ...")
                    ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL_FOR_ADD_STORAGE_PATH, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def click_dialog_title(cls, timeout=5, fail_if_false=True):
                logger.debug("click dialog title 'Add Volume / Edit XXX (volume name)' to blur out of input control to let entry-validate-error-msg show up ...")
                ui_lib.wait_for_element_and_click(cls.e.ID_DIALOG_TITLE, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def click_add_button(cls, timeout=5, fail_if_false=True):
                logger.debug("click button 'Add' (Add Volume) ...")
                ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def click_add_plus_button(cls, timeout=5, fail_if_false=True):
                logger.debug("click button 'Add+' (Add Volume) ...")
                ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_PLUS, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def click_cancel_button(cls, timeout=5, fail_if_false=True):
                logger.debug("click button 'Cancel' (Add Volume) ...")
                ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def click_ok_button(cls, timeout=5, fail_if_false=True):
                logger.debug("click button 'OK' (Edit Volume) ...")
                ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_OK, timeout=timeout, fail_if_false=fail_if_false)

            @classmethod
            def verify_added_volume(cls, volume, timeout=5, fail_if_false=True):
                logger.debug("verifying the added volume '%s' (Add Volume) ..." % volume, also_console=False)
                # TODO: finish the verification part
                return True

    class BIOSSettings(object):
        e = GeneralServerProfilesElements.BIOSSettings

        @classmethod
        def set(cls, bios_settings_obj):
            logger.debug("bios_settings_obj is {%s}" % bios_settings_obj, also_console=False)
            FusionUIBase.select_view_by_name('BIOS Settings')
            if getattr(bios_settings_obj, 'manageBIOSsettings', '').lower() == 'true':
                cls.tick_manage_bios_settings()
                cls.add(bios_settings_obj.Add) if hasattr(bios_settings_obj, 'Add') else None
                cls.edit(bios_settings_obj.Edit) if hasattr(bios_settings_obj, 'Edit') else None
            else:
                cls.untick_manage_bios_settings()
                msg = "Manage BIOS settings is False, Will not be updating BIOS settings"
                return logger.info(msg)

        @classmethod
        def add(cls, bios_settings, timeout=5, fail_if_false=True):
            cls.click_edit_bios_settings_button()
            cls.wait_for_edit_bios_settings_dialog_open()
            if hasattr(bios_settings, 'ServerAssetInformation'):
                logger.info(bios_settings.ServerAssetInformation)
                cls.update_asset_info(bios_settings.ServerAssetInformation)
            cls.click_ok_bios_settings_button()
            cls.wait_for_edit_bios_settings_dialog_close()

        @classmethod
        def edit(cls, bios_settings):
            cls.click_edit_bios_settings_button()
            cls.wait_for_edit_bios_settings_dialog_open()
            server_type = getattr(bios_settings, 'server_type', '')
            logger.info("Server type is [%s]" % server_type)
            if "gen8" in server_type.lower():
                cls.update_gen8_bios(bios_settings)
            elif "gen9" in server_type.lower():
                cls.update_gen9_bios(bios_settings)
            else:
                logger.warn("Server type [%s] not valid!" % server_type)
            cls.click_ok_bios_settings_button()
            cls.wait_for_edit_bios_settings_dialog_close()

        @classmethod
        def update_gen8_bios(cls, bios_settings):
            # server hardware model and bios file convert map
            get_file = {'bl460c gen8': 'proliant_bl460c_gen8.xml',
                        'bl420c gen8': 'proliant_bl420c_gen8.xml',
                        'bl465c gen8': 'proliant_bl465c_gen8.xml',
                        'bl660c gen8': 'proliant_bl660c_gen8.xml',
                        'dl160 gen8': 'proliant_dl160_gen8.xml',
                        'dl320e gen8': 'proliant_dl320e_gen8.xml',
                        'dl360e gen8': 'proliant_dl360e_gen8.xml',
                        'dl360p gen8': 'proliant_dl360p_gen8.xml',
                        'dl380e gen8': 'proliant_dl380e_gen8.xml',
                        'dl380p gen8': 'proliant_dl380p_gen8.xml',
                        'dl385p gen8': 'proliant_dl385p_gen8.xml',
                        'dl560 gen8': 'proliant_dl560_gen8.xml',
                        'ws460c gen8': 'proliant_ws460c_gen8_ws_blade.xml'}
            file_path = getattr(bios_settings, 'bios_schema_path', '../../../Tools/bios_schema/gen8/')

            server_type = getattr(bios_settings, 'server_type', '')
            bios_file = file_path + get_file.get(server_type.lower())
            logger.debug("BIOS schema file path is [%s]" % bios_file)
            bios_dom = xml.dom.minidom.parse(bios_file)
            feature_list = bios_dom.getElementsByTagName("feature")

            for n, setting in enumerate(bios_settings.setting):
                name = getattr(setting, 'name', '')
                option = getattr(setting, 'option', '')
                logger.debug("Start to set [%s] as [%s]" % (name, option))

                found_feature = cls.find_feature_by_name_in_xml(feature_list, name)
                feature_type = found_feature.attributes["feature_type"].value
                feature_id = found_feature.attributes["feature_id"].value
                if feature_type.lower() == "option":
                    cls.select_setting_option(feature_id, option)
                elif feature_type.lower() == "string" or feature_type.lower() == 'number':
                    cls.input_setting_text(feature_id, option)
                else:
                    logger.warn("Setting type [%s] not supported!" % feature_type)

        @classmethod
        def update_gen9_bios(cls, bios_settings):
            # server hardware model and bios file convert map
            get_file = {'bl460c gen9': 'I36.json',
                        'sy480 gen9': 'I37.json',
                        'bl660c gen9': 'I38.json',
                        'sy660 gen9': 'I39.json',
                        'sy620 gen9': 'I40.json',
                        'sy680 gen9': 'I40.json',
                        'dl560 gen9': 'P85.json',
                        'dl120 gen9': 'P86.json',
                        'dl360 gen9': 'P89.json',
                        'dl380 gen9': 'P89.json',
                        'xl230b gen9': 'U12.json',
                        'xl230a gen9': 'U13.json',
                        'xl250a gen9': 'U13.json',
                        'xl170r gen9': 'U14.json',
                        'xl190r gen9': 'U14.json',
                        'dl60 gen9': 'U15.json',
                        'dl80 gen9': 'U15.json',
                        'dl580 gen9': 'U17.json',
                        'xl420 gen9': 'U19.json',
                        'dl160 gen9': 'U20.json',
                        'dl180 gen9': 'U20.json',
                        'xl450 gen9': 'U21.json',
                        'dl20 gen9': 'U22.json'}
            file_path = getattr(bios_settings, 'bios_schema_path', '../../../Tools/bios_schema/gen9/')

            server_type = getattr(bios_settings, 'server_type', '')
            bios_file = file_path + get_file.get(server_type.lower())
            logger.debug("BIOS schema file path is [%s]" % bios_file)
            fp = open(bios_file)
            bios_obj = json.load(fp)
            feature_list = bios_obj.get("RegistryEntries").get("Attributes")

            for n, setting in enumerate(bios_settings.setting):
                name = getattr(setting, 'name', '')
                option = getattr(setting, 'option', '')
                logger.debug("Start to set [%s] as [%s]" % (name, option))

                found_feature = cls.find_feature_by_name_in_json(feature_list, name)
                feature_type = found_feature.get("Type")
                feature_id = found_feature.get("Name")
                if feature_type.lower() == "enumeration":
                    cls.select_setting_option(feature_id, option)
                elif feature_type.lower() == "string" or feature_type.lower() == 'integer':
                    cls.input_setting_text(feature_id, option)
                else:
                    logger.warn("Setting type [%s] not supported!" % feature_type)

        @classmethod
        def find_feature_by_name_in_xml(cls, feature_list, feature_name):
            for ref in feature_list:
                name = ref.getElementsByTagName("feature_name")[0].childNodes[0]
                if feature_name == name.nodeValue:
                    return ref

        @classmethod
        def find_feature_by_name_in_json(cls, feature_list, feature_name):
            for ref in feature_list:
                name = ref.get("DisplayName")
                if feature_name == name:
                    return ref

        @classmethod
        def update_asset_info(cls, ServerAssetInformation, timeout=10, fail_if_false=True):
            for setting in ServerAssetInformation:
                if hasattr(setting, 'AdminName'):
                    cls.input_setting_info('AdminName', setting.AdminName)
                if hasattr(setting, 'AdminEmail'):
                    cls.input_setting_info('AdminEmail', setting.AdminEmail)
                if hasattr(setting, 'AdminPhone'):
                    cls.input_setting_info('AdminPhone', setting.AdminPhone)
                if hasattr(setting, 'AdminOtherInfo'):
                    cls.input_setting_info('AdminOtherInfo', setting.AdminOtherInfo)

        @classmethod
        def input_setting_info(cls, admin_attribute, new_value, timeout=10, fail_if_false=True):
            logger.debug("Input Administrator info '[%s]" % admin_attribute)
            logger.debug("%s" % cls.e.ID_TEXT_BIOS_SETTINGS_EXPECTED % admin_attribute)
            ui_lib.scroll_into_view(cls.e.ID_INPUT_TEXT_EDIT_BIOS_SETTINGS % admin_attribute)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_TEXT_EDIT_BIOS_SETTINGS % admin_attribute, new_value, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def input_setting_text(cls, setting_name, new_value, timeout=10, fail_if_false=True):
            logger.debug("Input bios setting [%s] as [%s] " % (setting_name, new_value))
            locator = cls.e.ID_INPUT_BIOS_SETTING % setting_name
            ui_lib.scroll_into_view(locator)
            ui_lib.wait_for_element_and_input_text(locator, new_value, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def select_setting_option(cls, setting_name, new_value, timeout=10, fail_if_false=True):
            logger.debug("Input bios setting [%s] as [%s] " % (setting_name, new_value))
            locator = cls.e.ID_SELECT_BIOS_SETTING % setting_name
            ui_lib.scroll_into_view(locator)
            FusionUIBase.choose_option_by_text(locator, new_value, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def verify_administrator_info_expected_value(cls, admin_attribute, expected_value, timeout=5, fail_if_false=True):
            logger.debug("Verifying administrator info [%s] expected value" % admin_attribute)
            FusionUIBase.verify_element_text(admin_attribute, cls.e.ID_TEXT_BIOS_SETTINGS_EXPECTED % admin_attribute, expected_value, timeout, fail_if_false)

        @classmethod
        def verify_administrator_info_actual_value(cls, admin_attribute, actual_value, timeout=5, fail_if_false=True):
            logger.debug("Verifying administrator info [%s] actual value" % admin_attribute)
            FusionUIBase.verify_element_text(admin_attribute, cls.e.ID_TEXT_BIOS_SETTINGS_ACTUAL % admin_attribute, actual_value, timeout, fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def wait_for_edit_bios_settings_dialog_open(cls, timeout=10, fail_if_false=True):
            logger.debug("waiting Edit BIOS Settings Dialog Open.")
            ui_lib.wait_for_element_visible(cls.e.ID_LABEL_DIALOG_EDIT_BIOS_SETTINGS_TITLE, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def wait_for_edit_bios_settings_dialog_close(cls, timeout=10, fail_if_false=True):
            logger.debug("waiting Edit BIOS Settings Dialog Close.")
            ui_lib.wait_for_element_notvisible(cls.e.ID_LABEL_DIALOG_EDIT_BIOS_SETTINGS_TITLE, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def click_edit_bios_settings_button(cls, timeout=10, fail_if_false=True):
            logger.debug("waiting Edit BIOS Settings Dialog.")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_BIOS_SETTINGS, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def tick_manage_bios_settings(cls, timeout=10, fail_if_false=True):
            logger.debug("Select checkbox Manage BIOS.")
            FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_MANAGE_BIOS_SETTINGS, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def untick_manage_bios_settings(cls, timeout=10, fail_if_false=True):
            logger.debug("UnSelect checkbox Manage BIOS.")
            FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_MANAGE_BIOS_SETTINGS, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def click_ok_bios_settings_button(cls, timeout=10, fail_if_false=True):
            logger.debug("Clicking 'OK' button.")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_OK_EDIT_BIOS_SETTINGS, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def click_cancel_bios_settings_button(cls, timeout=10, fail_if_false=True):
            logger.debug("Clicking 'OK' button.")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL_EDIT_BIOS_SETTINGS, timeout=timeout, fail_if_false=fail_if_false)

    class BootSettings(object):
        e = GeneralServerProfilesElements.BootSettings

        @classmethod
        def set(cls, profile, server_hardware_type, timeout=5, fail_if_false=True):
            if getattr(profile, 'BootSettings', None) is not None:
                FusionUIBase.select_view_by_name('Boot Settings')
                # select "Manage boot order" (or "Manage boot mode" when it's Gen 9 server) checkbox
                logger.debug("****** 'server_hardware_type' passed to function '_BaseCommonOperationServerProfile.BootSettings.set' is: <%s>" % server_hardware_type.lower())
                if 'gen9' in server_hardware_type.lower():
                    logger.debug("setting 'Boot mode' for Gen 9 specially ...")
                    if getattr(profile.BootSettings, 'manageBootMode', '').lower() == 'true':
                        # set boot mode if attribute 'manageBootMode' is true - only for Gen 9 (or later) server:
                        cls.tick_manage_boot_mode()
                        cls.select_boot_mode_by_text(profile.BootSettings.bootMode) if hasattr(profile.BootSettings, 'bootMode') else None
                        if getattr(profile.BootSettings, 'bootMode', '').lower() == 'legacy bios':
                            cls.set_legacy_bios_mode_boot_order(profile, timeout=timeout, fail_if_false=fail_if_false)
                        else:
                            cls.set_non_legacy_bios_mode_boot_order(profile, hardware_type=server_hardware_type, timeout=timeout, fail_if_false=fail_if_false)
                    else:
                        cls.untick_manage_boot_mode(timeout=timeout, fail_if_false=fail_if_false)
                else:
                    cls.set_legacy_bios_mode_boot_order(profile, timeout=timeout, fail_if_false=fail_if_false)
            else:
                msg = "<test data missing>: test data node '<BootSettings>' is missing for profile '%s'" % profile.name
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        @classmethod
        def tick_manage_boot_mode(cls, timeout=5, fail_if_false=True):
            logger.debug("turn on 'Manage boot mode' option ...")
            FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_MANAGE_BOOT_MODE, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def untick_manage_boot_mode(cls, timeout=5, fail_if_false=True):
            logger.debug("turn off 'Manage boot mode' option ...")
            FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_MANAGE_BOOT_MODE, timeout=timeout, fail_if_false=fail_if_false)
            if cls.wait_for_unchecking_manage_boot_mode_warning_dialog_shown(timeout=timeout, fail_if_false=False):
                cls.click_ok_button_for_warning()

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def wait_for_unchecking_manage_boot_mode_warning_dialog_shown(cls, timeout=5, fail_if_false=True):
            logger.debug("waiting for 'Warning' dialog to show up for after unchecking the 'Manage boot mode' option ...")
            if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_WARNING_FOR_UNCHECKING_MANAGE_BOOT_MODE, timeout=timeout, fail_if_false=fail_if_false):
                logger.debug("dialog 'Warning' for unchecking 'Manage boot mode' successfully showed up")
                return True
            else:
                msg = "failed to wait for dialog 'Warning' for unchecking 'Manage boot mode' to show up"
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def wait_for_unchecking_manage_boot_order_warning_dialog_shown(cls, timeout=5, fail_if_false=True):
            logger.debug("waiting for 'Warning' dialog to show up for after unchecking the 'Manage boot order' option ...")
            if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_WARNING_FOR_UNCHECKING_MANAGE_BOOT_ORDER, timeout=timeout, fail_if_false=fail_if_false):
                logger.debug("dialog 'Warning' for unchecking 'Manage boot order' successfully showed up")
                return True
            else:
                msg = "failed to wait for dialog 'Warning' for unchecking 'Manage boot order' to show up"
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        @classmethod
        def click_ok_button_for_warning(cls, timeout=5, fail_if_false=True):
            logger.debug("click button 'OK' on the warning dialog for unchecking 'Manage boot mode' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_OK_FOR_WARNING, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def click_cancel_button_for_warning(cls, timeout=5, fail_if_false=True):
            logger.debug("click button 'Cancel' on the warning dialog for unchecking 'Manage boot mode' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL_FOR_WARNING, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def select_boot_mode_uefi(cls, timeout=5, fail_if_false=True):
            logger.debug("select 'Boot mode' as 'UEFI' ...")
            cls.select_boot_mode_by_text('UEFI', timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def select_boot_mode_uefi_optimized(cls, timeout=5, fail_if_false=True):
            logger.debug("select 'Boot mode' as 'UEFI optimized' ...")
            cls.select_boot_mode_by_text('UEFI optimized', timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def select_boot_mode_legacy_bios(cls, timeout=5, fail_if_false=True):
            logger.debug("select 'Boot mode' as 'Legacy BIOS' ...")
            cls.select_boot_mode_by_text('Legacy BIOS', timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def select_boot_mode_select_mode(cls, timeout=5, fail_if_false=True):
            logger.debug("select 'Boot mode' as 'Select mode' ...")
            cls.select_boot_mode_by_text('Select mode', timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def select_boot_mode_by_text(cls, boot_mode, timeout=5, fail_if_false=True):
            # logger.debug("select 'Boot mode' as '%s' ..." % boot_mode)
            # ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_BOOT_MODE, timeout=timeout, fail_if_false=fail_if_false)
            # ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_BOOT_MODE_BY_TEXT % boot_mode, timeout=timeout, fail_if_false=fail_if_false)

            logger.debug("validating test data '%s' for 'Boot mode' ..." % boot_mode)
            if FusionUIBase.is_test_data_valid(boot_mode, 'Boot_Mode', fail_if_false=False):
                logger.debug("select 'Boot mode' as '%s' ..." % boot_mode)
                FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_BOOT_MODE, boot_mode, timeout=timeout, fail_if_false=fail_if_false)
            else:
                msg = "<test data invalid>: '%s' for 'Boot mode' is NOT valid" % boot_mode
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

            return True

        @classmethod
        def tick_manage_boot_order(cls, timeout=5, fail_if_false=True):
            logger.debug("turn on 'Manage boot order' option ...")
            FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_MANAGE_BOOT_ORDER, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def untick_manage_boot_order(cls, timeout=5, fail_if_false=True):
            logger.debug("turn off 'Manage boot order' option ...")
            FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_MANAGE_BOOT_ORDER, timeout=timeout, fail_if_false=fail_if_false)
            if cls.wait_for_unchecking_manage_boot_order_warning_dialog_shown(timeout=timeout, fail_if_false=False):
                cls.click_ok_button_for_warning()

        @classmethod
        def set_legacy_bios_mode_boot_order(cls, profile, timeout=5, fail_if_false=True):
            # set boot order if attribute 'manageBootOrder' is true
            if getattr(profile, 'BootSettings', None) is not None:
                if getattr(profile.BootSettings, 'manageBootOrder', '').lower() == 'true':
                    cls.tick_manage_boot_order()
                    if getattr(profile.BootSettings, 'bootorder', None) is not None:
                        logger.debug("start setting boot orders ...")
                        for index, boot_order in enumerate(profile.BootSettings.bootorder):
                            logger.debug("input '%s' for boot device '%s'" % (index + 1, boot_order.device))
                            ui_lib.wait_for_element_and_input_text("name=%s" % boot_order.device, index + 1)
                    else:
                        msg = "<test data missing>: test data node '<BootSettings><bootorder device=\"xxx\"/></BootSettings>' is missing for profile '%s'" % profile.name
                        return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)
                else:
                    cls.untick_manage_boot_order(timeout=timeout, fail_if_false=fail_if_false)
            else:
                msg = "<test data missing>: test data node '<BootSettings>' is missing for profile '%s'" % profile.name
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        @classmethod
        def set_non_legacy_bios_mode_boot_order(cls, profile, hardware_type, timeout=5, fail_if_false=True):
            # set boot order if attribute 'manageBootOrder' is true
            if getattr(profile, 'BootSettings', None) is not None:
                if hasattr(profile.BootSettings, 'pxeBootPolicy'):
                    logger.debug("set 'PXE boot policy' as '%s' ..." % profile.BootSettings.pxeBootPolicy)
                    FusionUIBase.select_view_by_name('Advanced')
                    FusionUIBase.select_view_by_name('Boot Settings')  # work around for hidden element
                    FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_PXE_BOOT_POLICY, profile.BootSettings.pxeBootPolicy, timeout=timeout, fail_if_false=fail_if_false)
                else:
                    logger.warn("attribute 'pxeBootPolicy' is not set")

                if hasattr(profile.BootSettings, 'manageBootOrder') and profile.BootSettings.manageBootOrder.lower() == 'true':
                    if 'BL' in hardware_type:
                        logger.debug("set 'PXE boot policy' as '%s' ..." % profile.BootSettings.pxeBootPolicy)
                        FusionUIBase.select_view_by_name('Advanced')
                        FusionUIBase.select_view_by_name('Boot Settings')  # work around for hidden element
                        FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_PRIMARY_BOOT_DEVICE, profile.BootSettings.primaryBootDevice, timeout=timeout, fail_if_false=fail_if_false)
                    else:
                        logger.warn("attribute 'manageBootOrder' is set and 'bootMode' is 'UEFI/UEFI optimized', but DL type server is not yet supported setting boot order")
                else:
                    cls.untick_manage_boot_order()
            else:
                msg = "<test data missing>: test data node '<BootSettings>' is missing for profile '%s'" % profile.name
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        @classmethod
        def get_error_message_from_boot_mode(cls, timeout=5, fail_if_false=True):
            logger.debug("get error message for 'Boot mode' that there might be ...")
            if ui_lib.is_visible(cls.e.ID_ERR_BOOT_MODE_IS_BLANK, timeout):
                err_msg = FusionUIBase.get_text(cls.e.ID_ERR_BOOT_MODE_IS_BLANK, timeout=timeout, fail_if_false=fail_if_false)
                logger.warn("error message for 'Boot mode' is found: '%s'" % err_msg)
                ui_lib.get_s2l().capture_page_screenshot()
                return err_msg
            else:
                logger.debug("no error message for 'Boot mode' found")
                return None


class CommonOperationServerProfile(_BaseCommonOperationServerProfile):
    pass


class C7000CommonOperationServerProfile(_BaseCommonOperationServerProfile):
    pass


class TBirdCommonOperationServerProfile(_BaseCommonOperationServerProfile):
    pass


class DLCommonOperationServerProfile(_BaseCommonOperationServerProfile):
    pass


class _BaseCreateServerProfile(object):

    """
    This class holds all operation when create server profile.
    It also defines abstract methods which the subclass has different implementation for C7000 & TBird
    """

    e = CreateServerProfilesElements

    @classmethod
    def click_create_profile_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click 'Create profile' button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_PROFILE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_action_create(cls, timeout=5, fail_if_false=True):
        logger.debug("select action 'Create'")
        ui_lib.wait_for_element_and_click(GeneralServerProfilesElements.ID_DROPDOWN_ACTIONS, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_ACTION_CREATE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_server_profile_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Create server profile' to show up ...")
        if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_CREATE_SERVER_PROFILE, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Create server profile' successfully show up")
            return True
        else:
            msg = "failed to wait for dialog 'Create server profile' to show up"
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def click_dialog_title(cls, timeout=5):
        logger.debug("click dialog title 'Create Server Profile' to blur out of input control to let entry-validate-error-msg show up ...")
        ui_lib.wait_for_element_and_click(cls.e.ID_DIALOG_TITLE, timeout=timeout, fail_if_false=True)

    @classmethod
    def input_name(cls, name, timeout=5, fail_if_false=True):
        logger.debug("input 'Name' as '%s'" % name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NAME, name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_description(cls, description, timeout=5, fail_if_false=True):
        logger.debug("input 'Description' as '%s'" % description)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_DESCRIPTION, description, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_server_hardware(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("input 'Server hardware' as '%s'" % server_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SERVER_HARDWARE, server_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_server_hardware_search_combo(cls, timeout=5, fail_if_false=True):
        logger.debug("click search combo of 'Server Hardware' field")
        ui_lib.wait_for_element_and_click(cls.e.ID_SEARCH_COMBO_SERVER_HARDWARE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_server_hardware_visible(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("wait for server hardware '%s' is visible in drop down list" % server_name)
        if ui_lib.wait_for_element_visible(cls.e.ID_OPTION_SERVER_HARDWARE % server_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("server hardware '%s' is successfully verified as VISIBLE from the drop-down list within %s seconds" % (server_name, timeout))
            return True
        else:
            msg = "failed to verify server hardware '%s' as VISIBLE from the drop-down list within %s seconds" % (server_name, timeout)
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_server_hardware_not_visible(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("wait for server hardware '%s' is not visible in drop down list" % server_name)
        if ui_lib.wait_for_element_notvisible(cls.e.ID_OPTION_SERVER_HARDWARE % server_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("server hardware '%s' is successfully verified as INVISIBLE from the drop-down list within %s seconds" % (server_name, timeout))
            return True
        else:
            msg = "failed to verify server hardware '%s' as INVISIBLE from the drop-down list within %s seconds" % (server_name, timeout)
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def input_select_server_profile_template(cls, prof_temp, timeout=15, fail_if_false=True):
        logger.debug("input and select 'Server profile template' as '%s'" % prof_temp)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SERVER_PROF_TEMP, prof_temp, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_SERVER_PROF_TEMP % prof_temp, timeout=timeout, fail_if_false=fail_if_false)
        logger.debug("server profile template '%s' is successfully selected" % prof_temp)
        return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def input_select_server_hardware(cls, server_name, auto_power_off=True, return_false_if_powered_on=True, timeout=10, fail_if_false=True):
        logger.debug("input and select 'Server hardware' as '%s'" % server_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SERVER_HARDWARE, server_name, timeout=timeout, fail_if_false=fail_if_false)
        if ui_lib.is_visible(cls.e.ID_OPTION_SERVER_HARDWARE % server_name):
            # sht_list = cls.get_list_of_all_server_hardware_type(timeout=timeout, fail_if_false=fail_if_false)
            if server_name.lower() != 'unassigned':
                displayed_sht_from_drop_down = cls.get_listed_server_hardware_type_of_server(server_name, timeout=timeout)
                if displayed_sht_from_drop_down == 'empty':
                    ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_SERVER_HARDWARE % server_name, timeout=timeout, fail_if_false=fail_if_false)
                    logger.debug("sht of selected 'Server hardware' is empty")
                    return True

                if ui_lib.is_visible(cls.e.ID_LABEL_SERVER_HARDWARE_POWER_ERR % server_name, timeout):
                    logger.debug("click server hardware '%s' from the drop-down list ..." % server_name)
                    ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_SERVER_HARDWARE % server_name, timeout=timeout, fail_if_false=fail_if_false)

                    if auto_power_off is True:
                        logger.warn("server hardware '%s' is 'Powered on', trying to power it off ..." % server_name)
                        if VerifyServerProfile.is_power_on_error_visible_when_create_server_profile(server_name=server_name, timeout=timeout, fail_if_false=fail_if_false) is True:
                            if cls.click_power_off_link_from_powered_on_error(server_name=server_name, timeout=timeout, fail_if_false=fail_if_false) is True:
                                logger.debug("successfully powered off server hardware '%s' before creating server profile" % server_name)
                                return True
                            else:
                                logger.warn("failed to power off server hardware '%s' before creating server profile" % server_name)
                                return False
                    else:
                        if return_false_if_powered_on is True:
                            logger.warn("server hardware '%s' is 'Powered on', 'auto_power_off' is defined as 'True', and 'return_false_if_powered_on' is defined as 'True', function '%s' returns FALSE" % (server_name, sys._getframe().f_code.co_name))
                            return False
                        else:
                            logger.warn("server hardware '%s' is 'Powered on', 'auto_power_off' is defined as 'False', and 'return_false_if_powered_on' is defined as 'False', function '%s' returns TRUE" % (server_name, sys._getframe().f_code.co_name))
                            return True

                else:
                    ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_SERVER_HARDWARE % server_name, timeout=timeout, fail_if_false=fail_if_false)
                    if ui_lib.is_visible(cls.e.ID_ERR_SERVER_HARDWARE_INVALID, timeout):
                        msg = cls.get_error_message_from_server_hardware(timeout=timeout, fail_if_false=fail_if_false)
                        logger.warn(msg)
                        return False

                logger.debug("waiting for 'Server hardware type' to be refreshed ...")
                locator = cls.e.ID_TEXT_SERVER_HARDWARE_TYPE_SELECTED
                if ui_lib.wait_for_element_text(locator, displayed_sht_from_drop_down, timeout=timeout, fail_if_false=False) is not True:
                    logger.warn("server hardware type is not refreshed to be consistent with the selected server hardware within %s seconds" % timeout)
                    return True

                displayed_sht_after_selecting = cls.get_selected_server_hardware_type(server_name)
                if displayed_sht_after_selecting != displayed_sht_from_drop_down:
                    logger.warn("displayed server hardware type '%s' after selecting server hardware, "
                                "is NOT the one '%s' that is listed in the drop-down list" % (displayed_sht_after_selecting, displayed_sht_from_drop_down))
                    return False
            else:
                ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_SERVER_HARDWARE % server_name, timeout=timeout, fail_if_false=fail_if_false)
                if ui_lib.is_visible(cls.e.ID_ERR_SERVER_HARDWARE_INVALID, timeout):
                    msg = cls.get_error_message_from_server_hardware(timeout=timeout, fail_if_false=fail_if_false)
                    logger.warn(msg)
                    return False
                else:
                    return True
        else:
            msg = "No server hardware named '%s' for creating server profile" % server_name
            logger.warn(msg)
            # ui_lib.fail_test(msg)
            return False
        return True

    @classmethod
    def get_selected_server_hardware(cls, timeout=5, fail_if_false=True):
        logger.debug("get selected 'Server hardware' ...")
        server = FusionUIBase.get_text(cls.e.ID_TEXT_SERVER_HARDWARE_SELECTED, timeout=timeout, fail_if_false=fail_if_false, hidden_element=True)
        logger.debug("selected 'Server hardware' is '%s'" % server)
        return server

    @classmethod
    def select_powered_on_server_hardware(cls, server_name, timeout=5, fail_if_false=True):
        """This Function just for Select a Power On Server Hardware"""
        logger.debug("input and select Power ON 'Server hardware' as '%s'" % server_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SERVER_HARDWARE, server_name, timeout=timeout, fail_if_false=fail_if_false)
        if ui_lib.is_visible(cls.e.ID_OPTION_SERVER_HARDWARE % server_name):
            if ui_lib.is_visible(cls.e.ID_LABEL_SERVER_HARDWARE_POWER_ERR % server_name, timeout):
                ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_SERVER_HARDWARE % server_name, timeout=timeout, fail_if_false=fail_if_false)
                return True
            else:
                logger.warn("This server '%s' is power off " % server_name)
                return False
        else:
            logger.warn("This server '%s' is not exist" % server_name)
            return False

    @classmethod
    def click_power_off_link_from_powered_on_error(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("click 'Power off' link for server hardware '%s' from the error message displayed on Create Server Profile dialog ..." % server_name)
        if ui_lib.is_visible(cls.e.ID_LINK_POWER_OFF_SERVER_HARDWARE, timeout):
            logger.debug("click link 'Power off'")
            ui_lib.wait_for_element_and_click(cls.e.ID_LINK_POWER_OFF_SERVER_HARDWARE, timeout=timeout, fail_if_false=fail_if_false, js_click=True)
            logger.debug("click button 'Press and hold'")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_PRESS_AND_HOLD, timeout=timeout, fail_if_false=fail_if_false)
            logger.debug("wait for powering off to complete and the error message gone ...")
            ui_lib.wait_for_element_notvisible(cls.e.ID_ERR_SERVER_HARDWARE_POWERED_ON, timeout=20, fail_if_false=fail_if_false)
            return True
        else:
            logger.warn("link 'Power off' is not found, cannot continue to power off server '%s'" % server_name)
            return False

    @classmethod
    def get_error_message_from_server_hardware(cls, timeout=5, fail_if_false=True):
        logger.debug("get error message for 'Server hardware' that there might be")
        cls.click_dialog_title(timeout=2)
        if ui_lib.is_visible(cls.e.ID_ERR_SERVER_HARDWARE_INVALID, timeout):
            return FusionUIBase.get_text(cls.e.ID_ERR_SERVER_HARDWARE_INVALID, timeout=timeout, fail_if_false=fail_if_false)
        elif ui_lib.is_visible(cls.e.ID_ERR_SERVER_HARDWARE_POWERED_ON, timeout):
            return FusionUIBase.get_text(cls.e.ID_ERR_SERVER_HARDWARE_POWERED_ON, timeout=timeout, fail_if_false=fail_if_false)
        else:
            return None

    @classmethod
    def get_listed_server_hardware_type_of_server(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("get listed 'Server Hardware Type' of server: '%s' ..." % server_name)
        sht = FusionUIBase.get_text(cls.e.ID_TEXT_SERVER_HARDWARE_TYPE_LISTED % server_name, timeout=timeout, fail_if_false=fail_if_false)
        logger.debug("listed 'Server Hardware Type' of server: '%s' is '%s'" % (server_name, sht))
        return sht

    @classmethod
    def get_list_of_all_server_hardware_type(cls, timeout=5, fail_if_false=True):
        logger.debug("get a list of all existing 'Server Hardware Type' ... ")
        sht_list = FusionUIBase.get_multi_elements_text(cls.e.ID_TEXT_SERVER_HARDWARE_TYPE_LIST, timeout=timeout, fail_if_false=fail_if_false)
        logger.debug("retrieved list of all existing 'Server Hardware Type' is '%s'" % sht_list)
        return sht_list

    @classmethod
    def get_selected_server_hardware_type(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("get selected 'Server Hardware Type' of server: '%s' ..." % server_name)
        BuiltIn().sleep(2)
        sht = FusionUIBase.get_text(cls.e.ID_TEXT_SERVER_HARDWARE_TYPE_SELECTED, timeout=timeout, fail_if_false=fail_if_false, hidden_element=True)
        logger.debug("selected 'Server Hardware Type' of server: '%s' is '%s'" % (server_name, sht))
        return sht

    @classmethod
    def input_select_server_hardware_type(cls, hardware_type, timeout=5, fail_if_false=True):
        logger.debug("input and select 'Server hardware type' as '%s'" % hardware_type)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SERVER_HARDWARE_TYPE, hardware_type, timeout=timeout, fail_if_false=fail_if_false)
        if ui_lib.wait_for_element_visible(cls.e.ID_OPTION_SERVER_HARDWARE_TYPE % hardware_type, timeout=timeout):
            ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_SERVER_HARDWARE_TYPE % hardware_type, timeout=timeout, fail_if_false=fail_if_false)
            if ui_lib.wait_for_element_visible(cls.e.ID_ERR_SERVER_HARDWARE_TYPE_INVALID, timeout):
                msg = cls.get_error_message_from_server_hardware_type(timeout=timeout, fail_if_false=fail_if_false)
                logger.warn(msg)
                return False
            else:
                return True
        else:
            msg = "No server hardware type named '%s' for creating server profile" % hardware_type
            logger.warn(msg)
            # ui_lib.fail_test(msg)
            return False

    @classmethod
    def get_error_message_from_server_hardware_type(cls, timeout=5, fail_if_false=True):
        logger.debug("get error message for 'Server hardware' that there might be")
        if ui_lib.is_visible(cls.e.ID_ERR_SERVER_HARDWARE_TYPE_INVALID, timeout):
            return FusionUIBase.get_text(cls.e.ID_ERR_SERVER_HARDWARE_TYPE_INVALID, timeout=timeout, fail_if_false=fail_if_false)
        else:
            return None

    @classmethod
    def input_select_enclosure_group(cls, enclosure_group, timeout=5, fail_if_false=True):
        logger.debug("input and select 'Enclosure group' as '%s'" % enclosure_group)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ENCLOSURE_GROUP, enclosure_group, timeout=timeout, fail_if_false=fail_if_false)
        BuiltIn().sleep(2)
        if ui_lib.is_visible(cls.e.ID_OPTION_ENCLOSURE_GROUP % enclosure_group):
            ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_ENCLOSURE_GROUP % enclosure_group, timeout=timeout, fail_if_false=fail_if_false)
            # if ui_lib.is_visible(cls.e.ID_ERR_SERVER_HARDWARE_TYPE_INVALID, timeout):
            #     msg = cls.get_error_message_from_enclosure_group(timeout=timeout, fail_if_false=fail_if_false)
            #     logger.warn(msg)
            #     return False
            # else:
            #     return True
        else:
            msg = "No enclosure group named '%s' for creating server profile" % enclosure_group
            logger.warn(msg)
            # ui_lib.fail_test(msg)
            return False

    @classmethod
    def get_selected_enclosure_group(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("get selected 'Enclosure group' of server: '%s' ..." % server_name)
        eg = FusionUIBase.get_text(cls.e.ID_TEXT_ENCLOSURE_GROUP_SELECTED, timeout=timeout, fail_if_false=fail_if_false, hidden_element=True)
        logger.debug("selected 'Enclosure group' of server: '%s' is '%s'" % (server_name, eg))
        return eg

    @classmethod
    def get_error_message_from_enclosure_group(cls, timeout=5, fail_if_false=True):

        logger.debug("get error message for 'Enclosure group' that there might be")
        if ui_lib.is_visible(CreateServerProfilesElements.ID_ERR_ENCLOSURE_GROUP_INVALID, timeout):
            return FusionUIBase.get_text(CreateServerProfilesElements.ID_ERR_ENCLOSURE_GROUP_INVALID, timeout=timeout, fail_if_false=fail_if_false)
        else:
            return None

    @classmethod
    def select_affinity_device_bay(cls, timeout=5, fail_if_false=True):
        logger.debug("select 'Affinity' as 'Device bay' ...")
        cls.select_affinity_by_text('Device bay', timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_affinity_device_bay_plus_server_hardware(cls, timeout=5, fail_if_false=True):
        logger.debug("select 'Affinity' as 'Device bay + server hardware' ...")
        cls.select_affinity_by_text('Device bay + server hardware', timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_affinity_by_text(cls, affinity, timeout=5, fail_if_false=True):
        logger.debug("validating test data '%s' for 'Affinity' ..." % affinity)
        if FusionUIBase.is_test_data_valid(affinity, 'Affinity', fail_if_false=False):
            logger.debug("select 'Affinity' as '%s' ..." % affinity)
            FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_AFFINITY, affinity, timeout=timeout, fail_if_false=fail_if_false)
        else:
            msg = "<test data invalid>: '%s' for 'Affinity' is NOT valid" % affinity
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        return True

    class Advanced(object):

        e = CreateServerProfilesElements.Advanced

        @classmethod
        def set(cls, profile, timeout=5, fail_if_false=True):
            if getattr(profile, 'Advanced', None) is not None:
                logger.debug("start setting 'Advanced' options for profile '%s' ..." % profile.name)
                CommonOperationServerProfile.select_advanced_panel()
                cls.tick_iscsi_initiator_name_as_virtual(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'iscsi', '').lower() == 'virtual' else None
                if getattr(profile.Advanced, 'iscsi', '').lower() == 'user-specified':
                    cls.tick_iscsi_initiator_name_as_user_specified(timeout=timeout, fail_if_false=fail_if_false)
                    cls.input_user_specified_iscsi_initiator_name(getattr(profile.Advanced, 'iscsiInitiatorName', ''), timeout=timeout, fail_if_false=fail_if_false)
                cls.tick_mac_addresses_as_virtual(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'mac', '').lower() == 'virtual' else None
                cls.tick_mac_addresses_as_physical(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'mac', '').lower() == 'physical' else None
                cls.tick_wwn_addresses_as_virtual(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'wwn', '').lower() == 'virtual' else None
                cls.tick_wwn_addresses_as_physical(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'wwn', '').lower() == 'physical' else None
                cls.tick_serial_number_uuid_as_virtual(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'serial', '').lower() == 'virtual' else None
                cls.tick_serial_number_uuid_as_physical(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'serial', '').lower() == 'physical' else None
                cls.tick_serial_number_uuid_as_user_specified(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'serial', '').lower() == 'user-specified' else None
                cls.input_user_specified_serial_number(getattr(profile.Advanced, 'UserSpecifiedSerialNumber', ''), timeout=timeout, fail_if_false=fail_if_false) \
                    if getattr(profile.Advanced, 'serial', '').lower() == 'user-specified' else None
                cls.input_user_specified_uuid(getattr(profile.Advanced, 'UserSpecifiedUUID', ''), timeout=timeout, fail_if_false=fail_if_false) \
                    if getattr(profile.Advanced, 'serial', '').lower() == 'user-specified' else None
                # TODO: check what is the accurate scenario that 'Hide unused FlexNICs' setting is not present in UI at all. It's is not present in 3.0 DCS PASS94 for all the SHTs (SY 480 Gen9 and SY 660 Gen9)
                cls.tick_hide_unused_flexnics_as_yes(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'HideUnusedFlexNICs', '').lower() == 'yes' else None
                cls.tick_hide_unused_flexnics_as_no(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'HideUnusedFlexNICs', '').lower() == 'no' else None
            else:
                msg = "<test data missing>: test data node '<Advanced/>' is missing for profile '%s'" % profile.name
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

            return True

        @classmethod
        def click_dialog_title(cls, timeout=5):
            logger.debug("click dialog title to blur out of input control to let entry-validate-error-msg show up ...")
            ui_lib.wait_for_element_and_click(CreateServerProfilesElements.ID_DIALOG_TITLE, timeout=timeout, fail_if_false=True)

        @classmethod
        def tick_iscsi_initiator_name_as_virtual(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'iSCSI initiator name' as 'Virtual' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_ISCSI_INITIATOR_NAME_VIRTUAL, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_iscsi_initiator_name_as_user_specified(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'iSCSI initiator name' as 'User-specified' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_ISCSI_INITIATOR_NAME_USER_SPECIFIED, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def input_user_specified_iscsi_initiator_name(cls, user_specified_iscsi_initiator_name, timeout=5, fail_if_false=True):
            logger.debug("input 'Initiator name' when 'Advanced' option 'iSCSI initiator name' is 'User-specified' ...")
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_USER_SPECIFIED_ISCSI_INITIATOR_NAME, user_specified_iscsi_initiator_name, timeout=timeout, fail_if_false=fail_if_false)
            cls.click_dialog_title(timeout=2)
            if ui_lib.is_visible(cls.e.ID_TEXT_ERROR_ISCSI_INITIATOR_NAME, timeout=10):
                ui_lib.fail_test("<entry invalid>: entered value '%s' for Connection's 'iSCSI Initiator name' is "
                                 "INVALID, error message from UI is: \n<%s>"
                                 % (user_specified_iscsi_initiator_name, FusionUIBase.get_text(cls.e.ID_TEXT_ERROR_ISCSI_INITIATOR_NAME)))

        @classmethod
        def tick_mac_addresses_as_virtual(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'MAC addresses' as 'Virtual' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_MAC_ADDRESSES_VIRTUAL, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_mac_addresses_as_physical(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'MAC addresses' as 'Physical' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_MAC_ADDRESSES_PHYSICAL, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_wwn_addresses_as_virtual(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'WWN addresses' as 'Virtual' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_WWN_ADDRESSES_VIRTUAL, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_wwn_addresses_as_physical(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'WWN addresses' as 'Physical' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_WWN_ADDRESSES_PHYSICAL, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_serial_number_uuid_as_virtual(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'Serial number/UUID' as 'Virtual' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SERIAL_NUMBER_UUID_VIRTUAL, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_serial_number_uuid_as_physical(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'Serial number/UUID' as 'Physical' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SERIAL_NUMBER_UUID_PHYSICAL, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_serial_number_uuid_as_user_specified(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'Serial number/UUID' as 'User-specified' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SERIAL_NUMBER_UUID_USER_SPECIFIED, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def input_user_specified_serial_number(cls, user_specified_serial_number, timeout=5, fail_if_false=True):
            logger.debug("input 'Serial number' when 'Advanced' option 'Serial number/UUID' is 'User-specified' ...")
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_USER_SPECIFIED_SERIAL_NUMBER, user_specified_serial_number, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def input_user_specified_uuid(cls, user_specified_uuid, timeout=5, fail_if_false=True):
            logger.debug("input 'UUID' when 'Advanced' option 'Serial number/UUID' is 'User-specified' ...")
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_USER_SPECIFIED_UUID, user_specified_uuid, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_hide_unused_flexnics_as_yes(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'Hide unused FlexNICs' as 'Yes' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_HIDE_UNUSED_FLEXNICS_YES, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_hide_unused_flexnics_as_no(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'Hide unused FlexNICs' as 'No' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_HIDE_UNUSED_FLEXNICS_NO, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_server_profile_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Create server profile' to disappear ...")
        if ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_CREATE_SERVER_PROFILE, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Create server profile' successfully disappeared")
            return True
        else:
            msg = "failed to wait for dialog 'Create server profile' to disappear"
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def click_create_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click button 'Create'")
        # ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE, timeout=timeout, fail_if_false=fail_if_false)
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
    def get_error_message_if_save_create_failed(cls, timeout=5, fail_if_false=True):
        logger.debug("get error message if save create failed")
        return ui_lib.get_text(cls.e.ID_ERROR_SAVE_CREATE, timeout=timeout, fail_if_false=fail_if_false)


class CreateServerProfile(_BaseCreateServerProfile):
    pass


class C7000CreateServerProfile(_BaseCreateServerProfile):
    pass


class TBirdCreateServerProfile(_BaseCreateServerProfile):
    pass


class DLCreateServerProfile(_BaseCreateServerProfile):
    pass


class _BaseEditServerProfile(object):

    """
    This class holds all operation when edit server profile.
    It also defines abstract methods which the subclass has different implementation for C7000 & TBird
    """
    e = EditServerProfilesElements

    @classmethod
    def select_action_edit(cls, timeout=5, fail_if_false=True):
        logger.debug("select action 'Edit'")
        ui_lib.wait_for_element_and_click(GeneralServerProfilesElements.ID_DROPDOWN_ACTIONS, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_ACTION_EDIT, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_link_edit_general_from_pane(cls, timeout=5, fail_if_false=True):
        logger.debug("click link 'Edit' from General pane on Overview")
        ui_lib.wait_for_element_and_click(cls.e.ID_LINK_EDIT_GENERAL_FROM_PANE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_link_edit_general_from_view(cls, timeout=5, fail_if_false=True):
        logger.debug("click link 'Edit' from General view")
        FusionUIBase.select_view_by_name('General')
        ui_lib.wait_for_element_and_click(cls.e.ID_LINK_EDIT_GENERAL_FROM_VIEW, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_link_edit_firmware_from_pane(cls, timeout=5, fail_if_false=True):
        logger.debug("click link 'Edit' from Firmware pane on Overview")
        ui_lib.wait_for_element_and_click(cls.e.ID_LINK_EDIT_FIRMWARE_FROM_PANE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_link_edit_firmware_from_view(cls, timeout=5, fail_if_false=True):
        logger.debug("click link 'Edit' from Firmware view")
        FusionUIBase.select_view_by_name('Firmware')
        ui_lib.wait_for_element_and_click(cls.e.ID_LINK_EDIT_FIRMWARE_FROM_VIEW, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_link_edit_connections_from_pane(cls, timeout=5, fail_if_false=True):
        logger.debug("click link 'Edit' from Connections pane on Overview")
        ui_lib.wait_for_element_and_click(cls.e.ID_LINK_EDIT_CONNECTIONS_FROM_PANE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_link_edit_connections_from_view(cls, timeout=5, fail_if_false=True):
        logger.debug("click link 'Edit' from Connections view")
        FusionUIBase.select_view_by_name('Connections')
        ui_lib.wait_for_element_and_click(cls.e.ID_LINK_EDIT_CONNECTIONS_FROM_VIEW, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_link_edit_san_storage_from_pane(cls, timeout=5, fail_if_false=True):
        logger.debug("click link 'Edit' from SAN Storage pane on Overview")
        ui_lib.wait_for_element_and_click(cls.e.ID_LINK_EDIT_SAN_STORAGE_FROM_PANE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_link_edit_san_storage_from_view(cls, timeout=5, fail_if_false=True):
        logger.debug("click link 'Edit' from SAN Storage view")
        FusionUIBase.select_view_by_name('SAN Storage')
        ui_lib.wait_for_element_and_click(cls.e.ID_LINK_EDIT_SAN_STORAGE_FROM_VIEW, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_link_edit_local_storage_from_pane(cls, timeout=5, fail_if_false=True):
        logger.debug("click link 'Edit' from Local Storage pane on Overview")
        ui_lib.wait_for_element_and_click(cls.e.ID_LINK_EDIT_LOCAL_STORAGE_FROM_PANE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_link_edit_local_storage_from_view(cls, timeout=5, fail_if_false=True):
        logger.debug("click link 'Edit' from Local Storage view")
        FusionUIBase.select_view_by_name('Local Storage')
        ui_lib.wait_for_element_and_click(cls.e.ID_LINK_EDIT_LOCAL_STORAGE_FROM_VIEW, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_link_edit_bios_settings_from_pane(cls, timeout=5, fail_if_false=True):
        logger.debug("click link 'Edit' from BIOS pane on Overview")
        ui_lib.wait_for_element_and_click(cls.e.ID_LINK_EDIT_BIOS_SETTINGS_FROM_PANE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_link_edit_bios_settings_from_view(cls, timeout=5, fail_if_false=True):
        logger.debug("click link 'Edit' from BIOS view")
        FusionUIBase.select_view_by_name('BIOS Settings')
        ui_lib.wait_for_element_and_click(cls.e.ID_LINK_EDIT_BIOS_SETTINGS_FROM_VIEW, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_link_edit_boot_settings_from_view(cls, timeout=5, fail_if_false=True):
        logger.debug("click link 'Edit' from BIOS view")
        FusionUIBase.select_view_by_name('BIOS Settings')
        ui_lib.wait_for_element_and_click(cls.e.ID_LINK_EDIT_BOOT_SETTINGS_FROM_VIEW, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_server_profile_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Edit server profile' to show up ...")
        if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_EDIT_SERVER_PROFILE, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Edit server profile' successfully showed up")
            return True
        else:
            msg = "failed to wait for dialog 'Edit server profile' to show up"
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def input_name(cls, name, timeout=5, fail_if_false=True):
        logger.debug("input 'Name' as '%s'" % name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NAME, name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_description(cls, description, timeout=5, fail_if_false=True):
        logger.debug("input 'Description' as '%s'" % description)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_DESCRIPTION, description, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_server_hardware(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("input 'Server hardware' as '%s'" % server_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SERVER_HARDWARE, server_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_server_hardware_search_combo(cls, timeout=5, fail_if_false=True):
        logger.debug("click search combo of 'Server Hardware' field")
        ui_lib.wait_for_element_and_click(cls.e.ID_SEARCH_COMBO_SERVER_HARDWARE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_server_hardware_visible(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("wait for server hardware '%s' is visible in drop down list" % server_name)
        if ui_lib.wait_for_element_visible(cls.e.ID_OPTION_SERVER_HARDWARE % server_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("server hardware '%s' is successfully verified as VISIBLE from the drop-down list within %s seconds" % (server_name, timeout))
            return True
        else:
            msg = "failed to verify server hardware '%s' as VISIBLE from the drop-down list within %s seconds" % (server_name, timeout)
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_server_hardware_not_visible(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("wait for server hardware '%s' is not visible in drop down list" % server_name)
        if ui_lib.wait_for_element_notvisible(cls.e.ID_OPTION_SERVER_HARDWARE % server_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("server hardware '%s' is successfully verified as INVISIBLE from the drop-down list within %s seconds" % (server_name, timeout))
            return True
        else:
            msg = "failed to verify server hardware '%s' as INVISIBLE from the drop-down list within %s seconds" % (server_name, timeout)
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def input_select_server_hardware(cls, server_name, auto_power_off=True, timeout=5, fail_if_false=True):
        logger.debug("input and select 'Server hardware' as '%s'" % server_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SERVER_HARDWARE, server_name, timeout=timeout, fail_if_false=fail_if_false)
        if ui_lib.is_visible(cls.e.ID_OPTION_SERVER_HARDWARE % server_name):
            if server_name.lower() != 'unassigned':
                if ui_lib.is_visible(cls.e.ID_LABEL_SERVER_HARDWARE_POWER_ERR % server_name, timeout):
                    if auto_power_off is True:
                        logger.warn("Server hardware '%s' is 'Powered on', will try to power it off" % server_name)
                        ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_SERVER_HARDWARE % server_name, timeout=timeout, fail_if_false=fail_if_false)
                        if ui_lib.wait_for_element_visible(cls.e.ID_DIAGLOG_REASSIGN_SERVER_HARDWARE):
                            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_YES_REASSIGN_HARDWARE)
                        if ui_lib.is_visible(cls.e.ID_LINK_POWER_OFF_SERVER_HARDWARE, timeout):
                            logger.debug("click link 'Power off'")
                            ui_lib.wait_for_element_and_click(cls.e.ID_LINK_POWER_OFF_SERVER_HARDWARE, timeout=timeout, fail_if_false=fail_if_false)
                            logger.debug("click button 'Press and hold'")
                            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_PRESS_AND_HOLD, timeout=timeout, fail_if_false=fail_if_false)
                            logger.debug("wait for powering off to complete and the error message gone ...")
                            ui_lib.wait_for_element_notvisible(cls.e.ID_ERR_SERVER_HARDWARE_POWERED_ON, timeout=20, fail_if_false=fail_if_false)
                            return True
                    else:
                        logger.warn("Server hardware '%s' is 'Powered on', and 'auto_power_off' is not set to True, test is going to FAIL")
                        return False
                else:
                    ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_SERVER_HARDWARE % server_name, timeout=timeout, fail_if_false=fail_if_false)
                    if ui_lib.wait_for_element_visible(cls.e.ID_DIAGLOG_REASSIGN_SERVER_HARDWARE):
                        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_YES_REASSIGN_HARDWARE)
                    if ui_lib.is_visible(cls.e.ID_ERR_SERVER_HARDWARE_INVALID, timeout):
                        msg = cls.get_error_message_from_server_hardware(timeout=timeout, fail_if_false=fail_if_false)
                        logger.warn(msg)
                        return False
            else:
                ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_SERVER_HARDWARE % server_name, timeout=timeout, fail_if_false=fail_if_false)
                if ui_lib.is_visible(cls.e.ID_ERR_SERVER_HARDWARE_INVALID, timeout):
                    msg = cls.get_error_message_from_server_hardware(timeout=timeout, fail_if_false=fail_if_false)
                    logger.warn(msg)
                    return False
                else:
                    return True

        else:
            msg = "No server hardware named '%s' for creating server profile" % server_name
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)
        return True

    @classmethod
    def get_selected_server_hardware(cls, timeout=5, fail_if_false=True):
        logger.debug("get selected 'Server hardware' ...")
        server = FusionUIBase.get_text(cls.e.ID_TEXT_SERVER_HARDWARE_SELECTED, timeout=timeout, fail_if_false=fail_if_false, hidden_element=True)
        logger.debug("selected 'Server hardware' is '%s'" % server)
        return server

    @classmethod
    def get_error_message_from_server_hardware(cls, timeout=5, fail_if_false=True):
        logger.debug("get error message for 'Server hardware' that there might be")
        if ui_lib.is_visible(cls.e.ID_ERR_SERVER_HARDWARE_INVALID, timeout):
            return FusionUIBase.get_text(cls.e.ID_ERR_SERVER_HARDWARE_INVALID, timeout=timeout, fail_if_false=fail_if_false)
        elif ui_lib.is_visible(cls.e.ID_ERR_SERVER_HARDWARE_POWERED_ON, timeout):
            return FusionUIBase.get_text(cls.e.ID_ERR_SERVER_HARDWARE_POWERED_ON, timeout=timeout, fail_if_false=fail_if_false)
        else:
            return None

    @classmethod
    def get_listed_server_hardware_type(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("get listed 'Server Hardware Type' of server: '%s' ..." % server_name)
        sht = FusionUIBase.get_text(cls.e.ID_TEXT_SERVER_HARDWARE_TYPE_LISTED % server_name, timeout=timeout, fail_if_false=fail_if_false)
        logger.debug("listed 'Server Hardware Type' of server: '%s' is '%s'" % (server_name, sht))
        return sht

    @classmethod
    def get_selected_server_hardware_type(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("get selected 'Server Hardware Type' of server: '%s' ..." % server_name)
        sht = FusionUIBase.get_text(cls.e.ID_TEXT_SERVER_HARDWARE_TYPE_SELECTED, timeout=timeout, fail_if_false=fail_if_false)
        logger.debug("selected 'Server Hardware Type' of server: '%s' is '%s'" % (server_name, sht))
        return sht

    @classmethod
    def get_selected_enclosure_group(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("get selected 'Enclosure group' of server: '%s' ..." % server_name)
        eg = FusionUIBase.get_text(cls.e.ID_TEXT_ENCLOSURE_GROUP_SELECTED, timeout=timeout, fail_if_false=fail_if_false, hidden_element=True)
        logger.debug("selected 'Enclosure group' of server: '%s' is '%s'" % (server_name, eg))
        return eg

    @classmethod
    class ChangeServerHardwareTypeAndEnclosureGroup(object):

        e = EditServerProfilesElements.ChangeServerHardwareTypeAndEnclosureGroup

        @classmethod
        def is_confirmation_expected(cls, hardware_type=None, enclosure_group=None, timeout=5, fail_if_false=True):
            logger.debug("check if confirmation dialog is expected due to either 'Server hardware type': <%s> or 'Enclosure group': <%s> is being changed to different value ...")
            used_server = EditServerProfile.get_selected_server_hardware(fail_if_false=True)
            previous_sht = EditServerProfile.get_selected_server_hardware_type(server_name=used_server, fail_if_false=True)
            previous_eg = EditServerProfile.get_selected_enclosure_group(server_name=used_server, fail_if_false=True)
            msg = ''
            sht_will_be_changed = (hardware_type is not None and hardware_type != previous_sht)
            eg_will_be_changed = (enclosure_group is not None and enclosure_group != previous_eg)
            if sht_will_be_changed or eg_will_be_changed:
                msg += "\n'Server hardware type' changed to <%s>" % hardware_type if sht_will_be_changed else ''
                msg += "\n'Enclosure group' changed to <%s>" % enclosure_group if eg_will_be_changed else ''
                msg += "\nchange confirmation dialog is expected"
                ret = True
            else:
                msg += "\n'Server hardware type' stays the same <%s>" % hardware_type if hardware_type else ''
                msg += "\n'Enclosure group' stays the same <%s>" % enclosure_group if enclosure_group else ''
                msg += "\nchange confirmation dialog is NOT expected"
                ret = False

            logger.debug(msg)
            return ret

        @classmethod
        def change_server_hardware_type(cls, hardware_type, timeout=5, fail_if_false=True):
            logger.debug("change 'Server Hardware Type' to '%s' ..." % hardware_type)
            confirmation_expected = cls.is_confirmation_expected(hardware_type=hardware_type)
            cls.click_link_change_server_hardware_type()
            cls.wait_for_dialog_appear()
            cls.input_select_server_hardware_type(hardware_type=hardware_type, timeout=timeout, fail_if_false=fail_if_false)
            cls.click_ok_button_and_confirm(confirmation_expected=confirmation_expected, confirm_button='YES')
            cls.wait_for_dialog_disappear()
            if confirmation_expected:
                # after SHT or EG changed, Server Hardware will be changed to 'unassigned',
                # which needs a delay to continue the afterwards action of selecting server hardware, otherwise it'll be inputted as 'unassignedwpst23, bay 1'
                BuiltIn().sleep(1)

        @classmethod
        def change_enclosure_group(cls, enclosure_group, timeout=5, fail_if_false=True):
            logger.debug("change 'Enclosure Group' to '%s' ..." % enclosure_group)
            confirmation_expected = cls.is_confirmation_expected(enclosure_group=enclosure_group)
            cls.click_link_change_enclosure_group()
            cls.wait_for_dialog_appear()
            cls.input_select_enclosure_group(enclosure_group=enclosure_group, timeout=timeout, fail_if_false=fail_if_false)
            cls.click_ok_button_and_confirm(confirmation_expected=confirmation_expected, confirm_button='YES')
            cls.wait_for_dialog_disappear()
            if confirmation_expected:
                # after SHT or EG changed, Server Hardware will be changed to 'unassigned',
                # which needs a delay to continue the afterwards action of selecting server hardware, otherwise it'll be inputted as 'unassignedwpst23, bay 1'
                BuiltIn().sleep(1)

        @classmethod
        def click_link_change_server_hardware_type(cls, timeout=5, fail_if_false=True):
            logger.debug("click link 'Change' to edit 'Server Hardware Type' ...")
            FusionUIBase.wait_for_element_and_click(cls.e.ID_LINK_CHANGE_SERVER_HARDWARE_TYPE_AND_EG, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def click_link_change_enclosure_group(cls, timeout=5, fail_if_false=True):
            logger.debug("click link 'Change' to edit 'Enclosure Group' ...")
            FusionUIBase.wait_for_element_and_click(cls.e.ID_LINK_CHANGE_SERVER_HARDWARE_TYPE_AND_EG, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def wait_for_dialog_appear(cls, timeout=5, fail_if_false=True):
            logger.debug("waiting for dialog 'Change Server Hardware Type and Enclosure Group' to show up ...")
            if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_CHANGE_SERVER_HARDWARE_TYPE_AND_ENCLOSURE_GROUP, timeout=timeout, fail_if_false=fail_if_false):
                logger.debug("dialog 'Change Server Hardware Type and Enclosure Group' successfully showed up")
                return True
            else:
                msg = "failed to wait for dialog 'Change Server Hardware Type and Enclosure Group' to show up"
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        @classmethod
        def input_select_server_hardware_type(cls, hardware_type, timeout=5, fail_if_false=True):
            logger.debug("input and select 'Server hardware type' as '%s'" % hardware_type)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SERVER_HARDWARE_TYPE, hardware_type, timeout=timeout, fail_if_false=fail_if_false)
            if ui_lib.is_visible(cls.e.ID_OPTION_SERVER_HARDWARE_TYPE % hardware_type):
                ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_SERVER_HARDWARE_TYPE % hardware_type, timeout=timeout, fail_if_false=fail_if_false)
                return True
            else:
                msg = "No 'Server hardware type' named '%s' for editing server profile" % hardware_type
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        @classmethod
        def input_select_enclosure_group(cls, enclosure_group, timeout=5, fail_if_false=True):
            logger.debug("input and select 'Enclosure group' as '%s'" % enclosure_group)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ENCLOSURE_GROUP, enclosure_group, timeout=timeout, fail_if_false=fail_if_false)
            if ui_lib.is_visible(cls.e.ID_OPTION_ENCLOSURE_GROUP % enclosure_group):
                ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_ENCLOSURE_GROUP % enclosure_group, timeout=timeout, fail_if_false=fail_if_false)
                return True
            else:
                msg = "No 'Enclosure group' named '%s' for editing server profile" % enclosure_group
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        @classmethod
        def click_ok_button_and_confirm(cls, confirmation_expected=True, confirm_button='Yes', timeout=5, fail_if_false=True):
            logger.info("Click button 'OK'")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_OK, timeout=timeout, fail_if_false=fail_if_false)
            if confirmation_expected:
                logger.info("Click checkbox to confirm.")
                ui_lib.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_CONFIRM, timeout=timeout, fail_if_false=fail_if_false)
                if confirm_button.lower() == 'yes':
                    logger.info("Click button 'Yes, change'")
                    ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_YES_CHANGE, timeout=timeout, fail_if_false=fail_if_false)
                elif confirm_button.lower() == 'cancel':
                    logger.info("Click button 'Cancel'")
                    ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CONFIRM_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def click_cancel_button(cls, timeout=5, fail_if_false=True):
            logger.debug("click button 'Cancel'")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def wait_for_dialog_disappear(cls, timeout=5, fail_if_false=True):
            logger.debug("waiting for dialog 'Change Server Hardware Type and Enclosure Group' to disappear ...")
            if ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_CHANGE_SERVER_HARDWARE_TYPE_AND_ENCLOSURE_GROUP, timeout=timeout, fail_if_false=fail_if_false):
                logger.debug("dialog 'Change Server Hardware Type and Enclosure Group' successfully disappeared")
                return True
            else:
                msg = "failed to wait for dialog 'Change Server Hardware Type and Enclosure Group' to disappear"
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def select_affinity_device_bay(cls, timeout=5, fail_if_false=True):
        logger.debug("select 'Affinity' as 'Device bay' ...")
        cls.select_affinity_by_text('Device bay', timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_affinity_device_bay_plus_server_hardware(cls, timeout=5, fail_if_false=True):
        logger.debug("select 'Affinity' as 'Device bay + server hardware' ...")
        cls.select_affinity_by_text('Device bay + server hardware', timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_affinity_by_text(cls, affinity, timeout=5, fail_if_false=True):
        logger.debug("validating test data '%s' for 'Affinity' ..." % affinity)
        if FusionUIBase.is_test_data_valid(affinity, 'Affinity', fail_if_false=False):
            logger.debug("select 'Affinity' as '%s' ..." % affinity)
            FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_AFFINITY, affinity, timeout=timeout, fail_if_false=fail_if_false)
        else:
            msg = "<test data invalid>: '%s' for 'Affinity' is NOT valid" % affinity
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        return True

    class Advanced(object):
        e = EditServerProfilesElements.Advanced

        @classmethod
        def set(cls, profile, timeout=5, fail_if_false=True):
            if getattr(profile, 'Advanced', None) is not None:
                logger.debug("start setting 'Advanced' options for profile '%s' ..." % profile.name)
                CommonOperationServerProfile.select_advanced_panel()
                # for editing server profile, there's NO 'MAC address/WWN address/Serial number UUID' options available to change,
                # only 'Hide Unused FlexNICs' option for user to change
                cls.tick_iscsi_initiator_name_as_virtual(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'iscsi', '').lower() == 'virtual' else None
                if getattr(profile.Advanced, 'iscsi', '').lower() == 'user-specified':
                    cls.tick_iscsi_initiator_name_as_user_specified(timeout=timeout, fail_if_false=fail_if_false)
                    cls.input_user_specified_iscsi_initiator_name(getattr(profile.Advanced, 'iscsiInitiatorName', ''), timeout=timeout, fail_if_false=fail_if_false)
                cls.tick_hide_unused_flexnics_as_yes(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'HideUnusedFlexNICs', '').lower() == 'yes' else None
                cls.tick_hide_unused_flexnics_as_no(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'HideUnusedFlexNICs', '').lower() == 'no' else None
            else:
                msg = "<test data missing>: test data node '<Advanced/>' is missing for profile '%s'" % profile.name
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

            return True

        @classmethod
        def tick_iscsi_initiator_name_as_virtual(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'iSCSI initiator name' as 'Virtual' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_ISCSI_INITIATOR_NAME_VIRTUAL, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_iscsi_initiator_name_as_user_specified(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'iSCSI initiator name' as 'User-specified' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_ISCSI_INITIATOR_NAME_USER_SPECIFIED, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def input_user_specified_iscsi_initiator_name(cls, user_specified_iscsi_initiator_name, timeout=5, fail_if_false=True):
            logger.debug("input 'Initiator name' when 'Advanced' option 'iSCSI initiator name' is 'User-specified' ...")
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_USER_SPECIFIED_ISCSI_INITIATOR_NAME, user_specified_iscsi_initiator_name, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_hide_unused_flexnics_as_yes(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'Hide unused FlexNICs' as 'Yes' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_HIDE_UNUSED_FLEXNICS_YES, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_hide_unused_flexnics_as_no(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'Hide unused FlexNICs' as 'No' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_HIDE_UNUSED_FLEXNICS_NO, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_server_profile_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Edit server profile' to disappear ...")
        if ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_EDIT_SERVER_PROFILE, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Edit server profile' successfully disappeared")
            return True
        else:
            msg = "failed to wait for dialog 'Edit server profile' to disappear"
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def click_ok_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click button 'OK'")
        # FusionUIBase.wait_for_element_and_click(cls.e.ID_BUTTON_OK, timeout=timeout, fail_if_false=fail_if_false, js_click=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_OK, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout=timeout, fail_if_false=True)

    @classmethod
    def get_error_message_if_save_edit_failed(cls, timeout=5, fail_if_false=True):
        logger.debug("get error message if save edit failed")
        return ui_lib.get_text(cls.e.ID_ERROR_SAVE_EDIT, timeout=timeout, fail_if_false=fail_if_false)


class EditServerProfile(_BaseEditServerProfile):
    pass


class C7000EditServerProfile(_BaseEditServerProfile):
    pass


class TBirdEditServerProfile(_BaseEditServerProfile):
    pass


class DLEditServerProfile(_BaseEditServerProfile):
    pass


class _BaseCopyServerProfile(object):

    """
    This class holds all operation when edit server profile.
    It also defines abstract methods which the subclass has different implementation for C7000 & TBird
    """
    e = CopyServerProfilesElements

    @classmethod
    def select_action_copy(cls, timeout=5, fail_if_false=True):
        logger.debug("select action 'Copy'")
        ui_lib.wait_for_element_and_click(GeneralServerProfilesElements.ID_DROPDOWN_ACTIONS, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_ACTION_COPY, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_copy_server_profile_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.info("waiting for dialog 'Copy server profile' to show up ...")
        if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_COPY_SERVER_PROFILE, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Copy server profile' successfully showed up")
            return True
        else:
            msg = "failed to wait for dialog 'Copy server profile' to show up"
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def input_name(cls, name, timeout=5, fail_if_false=True):
        logger.debug("input 'Name' as '%s'" % name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NAME, name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_description(cls, description, timeout=5, fail_if_false=True):
        logger.debug("input 'Description' as '%s'" % description)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_DESCRIPTION, description, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_server_hardware(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("input 'Server hardware' as '%s'" % server_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SERVER_HARDWARE, server_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def input_select_server_hardware(cls, server_name, auto_power_off=True, timeout=5, fail_if_false=True):
        logger.debug("input and select 'Server hardware' as '%s'" % server_name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SERVER_HARDWARE, server_name, timeout=timeout, fail_if_false=fail_if_false)
        if ui_lib.wait_for_element_visible(cls.e.ID_OPTION_SERVER_HARDWARE % server_name):
            if server_name.lower() != 'unassigned':
                if ui_lib.is_visible(cls.e.ID_LABEL_SERVER_HARDWARE_POWER_ERR % server_name, timeout):
                    if auto_power_off is True:
                        logger.warn("Server hardware '%s' is 'Powered on', will try to power it off")
                        ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_SERVER_HARDWARE % server_name, timeout=timeout, fail_if_false=fail_if_false)
                        if ui_lib.is_visible(cls.e.ID_LINK_POWER_OFF_SERVER_HARDWARE, timeout):
                            logger.debug("click link 'Power off'")
                            ui_lib.wait_for_element_and_click(cls.e.ID_LINK_POWER_OFF_SERVER_HARDWARE, timeout=timeout, fail_if_false=fail_if_false)
                            logger.debug("click button 'Press and hold'")
                            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_PRESS_AND_HOLD, timeout=timeout, fail_if_false=fail_if_false)
                            logger.debug("wait for powering off to complete and the error message gone ...")
                            ui_lib.wait_for_element_notvisible(cls.e.ID_ERR_SERVER_HARDWARE_POWERED_ON, timeout=20, fail_if_false=fail_if_false)
                            return True
                    else:
                        logger.warn("Server hardware '%s' is 'Powered on', and 'auto_power_off' is not set to True, test is going to FAIL")
                        return False
                else:
                    ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_SERVER_HARDWARE % server_name, timeout=timeout, fail_if_false=fail_if_false)
                    if ui_lib.is_visible(cls.e.ID_ERR_SERVER_HARDWARE_INVALID, timeout):
                        msg = cls.get_error_message_from_server_hardware(timeout=timeout, fail_if_false=fail_if_false)
                        logger.warn(msg)
                        return False
            else:
                ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_SERVER_HARDWARE % server_name, timeout=timeout, fail_if_false=fail_if_false)
                if ui_lib.is_visible(cls.e.ID_ERR_SERVER_HARDWARE_INVALID, timeout):
                    msg = cls.get_error_message_from_server_hardware(timeout=timeout, fail_if_false=fail_if_false)
                    logger.warn(msg)
                    return False
                else:
                    return True

        else:
            msg = "No server hardware named '%s' for copying server profile" % server_name
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)
        return True

    @classmethod
    def get_selected_server_hardware(cls, timeout=5, fail_if_false=True):
        logger.debug("get selected 'Server hardware' ...")
        server = FusionUIBase.get_text(cls.e.ID_TEXT_SERVER_HARDWARE_SELECTED, timeout=timeout, fail_if_false=fail_if_false, hidden_element=True)
        logger.debug("selected 'Server hardware' is '%s'" % server)
        return server

    @classmethod
    def get_error_message_from_server_hardware(cls, timeout=5, fail_if_false=True):
        logger.debug("get error message for 'Server hardware' that there might be")
        if ui_lib.is_visible(cls.e.ID_ERR_SERVER_HARDWARE_INVALID, timeout):
            return FusionUIBase.get_text(cls.e.ID_ERR_SERVER_HARDWARE_INVALID, timeout=timeout, fail_if_false=fail_if_false)
        elif ui_lib.is_visible(cls.e.ID_ERR_SERVER_HARDWARE_POWERED_ON, timeout):
            return FusionUIBase.get_text(cls.e.ID_ERR_SERVER_HARDWARE_POWERED_ON, timeout=timeout, fail_if_false=fail_if_false)
        else:
            return None

    @classmethod
    def get_selected_server_hardware_type(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("get selected 'Server Hardware Type' of server: '%s' ..." % server_name)
        sht = FusionUIBase.get_text(cls.e.ID_TEXT_SERVER_HARDWARE_TYPE_SELECTED, timeout=timeout, fail_if_false=fail_if_false)
        logger.debug("selected 'Server Hardware Type' of server: '%s' is '%s'" % (server_name, sht))
        return sht

    @classmethod
    def get_selected_enclosure_group(cls, server_name, timeout=5, fail_if_false=True):
        logger.debug("get selected 'Enclosure group' of server: '%s' ..." % server_name)
        eg = FusionUIBase.get_text(cls.e.ID_TEXT_ENCLOSURE_GROUP_SELECTED, timeout=timeout, fail_if_false=fail_if_false, hidden_element=True)
        logger.debug("selected 'Enclosure group' of server: '%s' is '%s'" % (server_name, eg))
        return eg

    @classmethod
    def select_affinity_device_bay(cls, timeout=5, fail_if_false=True):
        logger.debug("select 'Affinity' as 'Device bay' ...")
        cls.select_affinity_by_text('Device bay', timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_affinity_device_bay_plus_server_hardware(cls, timeout=5, fail_if_false=True):
        logger.debug("select 'Affinity' as 'Device bay + server hardware' ...")
        cls.select_affinity_by_text('Device bay + server hardware', timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_affinity_by_text(cls, affinity, timeout=5, fail_if_false=True):
        logger.debug("validating test data '%s' for 'Affinity' ..." % affinity)
        if FusionUIBase.is_test_data_valid(affinity, 'Affinity', fail_if_false=False):
            logger.debug("select 'Affinity' as '%s' ..." % affinity)
            FusionUIBase.choose_option_by_text(cls.e.ID_SELECT_AFFINITY, affinity, timeout=timeout, fail_if_false=fail_if_false)
        else:
            msg = "<test data invalid>: '%s' for 'Affinity' is NOT valid" % affinity
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        return True

    class Advanced(object):
        e = CopyServerProfilesElements.Advanced

        @classmethod
        def set(cls, profile, timeout=5, fail_if_false=True):
            if getattr(profile, 'Advanced', None) is not None:
                # logger.debug("profile.Advanced is <%s>" % profile.Advanced)
                # logger.debug("profile.Advanced is <%s>" % profile.Advanced.mac)
                # logger.debug("profile.Advanced is <%s>" % profile.Advanced.wwn)
                # logger.debug("profile.Advanced is <%s>" % profile.Advanced.serial)
                # logger.debug("profile.Advanced is <%s>" % profile.Advanced.HideUnusedFlexNICs)
                logger.debug("start setting 'Advanced' options for profile '%s' ..." % profile.name)
                CommonOperationServerProfile.select_advanced_panel()
                cls.tick_iscsi_initiator_name_as_virtual(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'iscsi', '').lower() == 'virtual' else None
                if getattr(profile.Advanced, 'iscsi', '').lower() == 'user-specified':
                    cls.tick_iscsi_initiator_name_as_user_specified(timeout=timeout, fail_if_false=fail_if_false)
                    cls.input_user_specified_iscsi_initiator_name(getattr(profile.Advanced, 'iscsiInitiatorName', ''), timeout=timeout, fail_if_false=fail_if_false)
                cls.tick_mac_addresses_as_virtual(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'mac', '').lower() == 'virtual' else None
                cls.tick_mac_addresses_as_physical(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'mac', '').lower() == 'physical' else None
                cls.tick_wwn_addresses_as_virtual(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'wwn', '').lower() == 'virtual' else None
                cls.tick_wwn_addresses_as_physical(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'wwn', '').lower() == 'physical' else None
                cls.tick_serial_number_uuid_as_virtual(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'serial', '').lower() == 'virtual' else None
                cls.tick_serial_number_uuid_as_physical(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'serial', '').lower() == 'physical' else None
                cls.tick_serial_number_uuid_as_user_specified(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'serial', '').lower() == 'user-specified' else None
                cls.tick_hide_unused_flexnics_as_yes(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'HideUnusedFlexNICs', '').lower() == 'yes' else None
                cls.tick_hide_unused_flexnics_as_no(timeout=timeout, fail_if_false=fail_if_false) if getattr(profile.Advanced, 'HideUnusedFlexNICs', '').lower() == 'no' else None
            else:
                msg = "<test data missing>: test data node '<Advanced/>' is missing for profile '%s'" % profile.name
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

            return True

        @classmethod
        def tick_iscsi_initiator_name_as_virtual(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'iSCSI initiator name' as 'Virtual' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_ISCSI_INITIATOR_NAME_VIRTUAL, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_iscsi_initiator_name_as_user_specified(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'iSCSI initiator name' as 'User-specified' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_ISCSI_INITIATOR_NAME_USER_SPECIFIED, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def input_user_specified_iscsi_initiator_name(cls, user_specified_iscsi_initiator_name, timeout=5, fail_if_false=True):
            logger.debug("input 'Initiator name' when 'Advanced' option 'iSCSI initiator name' is 'User-specified' ...")
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_USER_SPECIFIED_ISCSI_INITIATOR_NAME, user_specified_iscsi_initiator_name, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_mac_addresses_as_virtual(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'MAC addresses' as 'Virtual' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_MAC_ADDRESSES_VIRTUAL, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_mac_addresses_as_physical(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'MAC addresses' as 'Physical' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_MAC_ADDRESSES_PHYSICAL, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_wwn_addresses_as_virtual(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'WWN addresses' as 'Virtual' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_WWN_ADDRESSES_VIRTUAL, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_wwn_addresses_as_physical(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'WWN addresses' as 'Physical' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_WWN_ADDRESSES_PHYSICAL, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_serial_number_uuid_as_virtual(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'Serial number/UUID' as 'Virtual' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SERIAL_NUMBER_UUID_VIRTUAL, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_serial_number_uuid_as_physical(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'Serial number/UUID' as 'Physical' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SERIAL_NUMBER_UUID_PHYSICAL, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_serial_number_uuid_as_user_specified(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'Serial number/UUID' as 'User-specified' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SERIAL_NUMBER_UUID_USER_SPECIFIED, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_hide_unused_flexnics_as_yes(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'Hide unused FlexNICs' as 'Yes' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_HIDE_UNUSED_FLEXNICS_YES, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def tick_hide_unused_flexnics_as_no(cls, timeout=5, fail_if_false=True):
            logger.debug("choose 'Advanced' option 'Hide unused FlexNICs' as 'No' ...")
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_HIDE_UNUSED_FLEXNICS_NO, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_copy_server_profile_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Copy server profile' to disappear ...")
        ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_COPY_SERVER_PROFILE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click button 'Create'")
        # FusionUIBase.wait_for_element_and_click(cls.e.ID_BUTTON_OK, timeout=timeout, fail_if_false=fail_if_false, js_click=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_plus_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click button 'Create +'")
        # FusionUIBase.wait_for_element_and_click(cls.e.ID_BUTTON_OK, timeout=timeout, fail_if_false=fail_if_false, js_click=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_PLUS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout=timeout, fail_if_false=fail_if_false)


class CopyServerProfile(_BaseCopyServerProfile):
    pass


class _BaseVerifyServerProfile(object):

    """
    This class holds all operation of server profile when do verification.
    It also defines abstract methods which the subclass has different implementation for C7000 & TBird
    """

    @classmethod
    def verify_sp_table_name(cls):
        pass

    @classmethod
    def verify_general_description(cls):
        pass

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_profile_not_exist(cls, profile_name, timeout=5, fail_if_false=True):
        logger.debug("verify server profile '%s' should NOT exist ..." % profile_name)
        if ui_lib.wait_for_element_notvisible(GeneralServerProfilesElements.ID_TABLE_SERVER_PROFILE % profile_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("server profile '%s' is successfully verified as invisible within %s second(s)" % (profile_name, timeout))
            return True
        elif ui_lib.wait_for_element_visible(GeneralServerProfilesElements.ID_TABLE_SERVER_PROFILE_DELETED % profile_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("server profile '%s' was deleted but not de-selected." % profile_name)
            return True
        else:
            msg = "server profile '%s' is failed to be verified as invisible within %s second(s)" % (profile_name, timeout)
            if fail_if_false:
                ui_lib.fail_test(msg)
            else:
                logger.warn(msg)
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_profile_exist(cls, profile_name, timeout=5, fail_if_false=True):
        logger.debug("verify server profile '%s' should exist ..." % profile_name)
        if ui_lib.wait_for_element_visible(GeneralServerProfilesElements.ID_TABLE_SERVER_PROFILE % profile_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("server profile '%s' is successfully verified as visible within %s second(s)" % (profile_name, timeout))
            return True
        else:
            logger.debug("server profile '%s' is failed to be verified as visible within %s second(s)" % (profile_name, timeout))
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_profile_status_on_details_page(cls, status, timeout=5, fail_if_false=True):
        # This is to check the status icon on the details page (not the status from the main table on the left, not the status from the right sidebar activity list)
        logger.debug("verify server profile should be in status <'%s'>..." % status)
        return ui_lib.wait_for_element_visible(GeneralServerProfilesElements.ID_ICON_SERVER_PROFILE_STATUS % status, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_server_power(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify server profile power on overview page should be in status <'%s'>..." % expect_value)
        locator = GeneralServerProfilesElements.ID_TEXT_OVERVIEW_SERVER_POWER
        item_name = "Server power"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_server_power(cls, expect_value, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.ID_TEXT_GENERAL_SERVER_POWER
        item_name = "Server power"
        # ui_lib.wait_for_element_text(locator=locator, text=expect_value, timeout=timeout, fail_if_false=False)
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_server_power_for_exclusion(cls, excluded_value, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.ID_TEXT_GENERAL_SERVER_POWER
        item_name = "Server power"
        return FusionUIBase.verify_element_text_for_exclusion(item_name=item_name, locator=locator, excluded_value=excluded_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_server_hardware(cls, expect_value, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.ID_TEXT_GENERAL_SERVER_HARDWARE
        item_name = "Server hardware"
        # ui_lib.wait_for_element_text(locator=locator, text=expect_value, timeout=timeout, fail_if_false=False)
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_server_hardware_type(cls, expect_value, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.ID_TEXT_GENERAL_SERVER_HARDWARE_TYPE
        item_name = "Server hardware type"
        # ui_lib.wait_for_element_text(locator=locator, text=expect_value, timeout=timeout, fail_if_false=False)
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value='/^%s/i' % expect_value, timeout=timeout, fail_if_false=fail_if_false)
        # return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_enclosure_group(cls, expect_value, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.ID_TEXT_GENERAL_ENCLOSURE_GROUP
        item_name = "Enclosure group"
        # ui_lib.wait_for_element_text(locator=locator, text=expect_value, timeout=timeout, fail_if_false=False)
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_iscsi_initiator_name(cls, iscsi_initiator_type, iscsi_initiator_name, timeout=5, fail_if_false=True):
        if iscsi_initiator_type.lower() == 'virtual':
            FusionUIBase.verify_element_text('iSCSI initiator name label', GeneralServerProfilesElements.ID_TEXT_GENERAL_ISCSI_INITIATOR_NAME_LABEL, 'iSCSI initiator name (v)', timeout, fail_if_false)
            return ui_lib.wait_for_element_visible(GeneralServerProfilesElements.ID_TEXT_GENERAL_ISCSI_INITIATOR_NAME, timeout, fail_if_false)
        elif iscsi_initiator_type.lower() == 'user-specified':
            FusionUIBase.verify_element_text('iSCSI initiator name label', GeneralServerProfilesElements.ID_TEXT_GENERAL_ISCSI_INITIATOR_NAME_LABEL, 'iSCSI initiator name (u)', timeout, fail_if_false)
            return FusionUIBase.verify_element_text('iSCSI initiator name', GeneralServerProfilesElements.ID_TEXT_GENERAL_ISCSI_INITIATOR_NAME, iscsi_initiator_name, timeout, fail_if_false)
        else:
            return ui_lib.fail_test("'%s' is not a supported option for iSCSI initiator name." % iscsi_initiator_type)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_user_specified_uuid(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify 'UUID' label should contain '(u)', and value should be <%s>..." % expect_value)
        FusionUIBase.verify_element_text('UUID label', GeneralServerProfilesElements.ID_TEXT_GENERAL_UUID_LABEL, 'UUID (u)', timeout, fail_if_false)
        return FusionUIBase.verify_element_text('UUID', GeneralServerProfilesElements.ID_TEXT_GENERAL_UUID, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_user_specified_serial_number(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify 'Serial number' label should contain '(u)', and value should be <%s>..." % expect_value)
        FusionUIBase.verify_element_text('Serial number label', GeneralServerProfilesElements.ID_TEXT_GENERAL_SERIAL_NUMBER_LABEL, 'Serial number (u)', timeout, fail_if_false)
        return FusionUIBase.verify_element_text('Serial number', GeneralServerProfilesElements.ID_TEXT_GENERAL_SERIAL_NUMBER, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_virtual_uuid(cls, timeout=5, fail_if_false=True):
        logger.debug("verify 'UUID' label should contain '(v)'...")
        FusionUIBase.verify_element_text('UUID label', GeneralServerProfilesElements.ID_TEXT_GENERAL_UUID_LABEL, 'UUID (v)', timeout, fail_if_false)
        return ui_lib.wait_for_element_visible(GeneralServerProfilesElements.ID_TEXT_GENERAL_UUID, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_virtual_serial_number(cls, timeout=5, fail_if_false=True):
        logger.debug("verify 'Serial number' label should contain '(v)'...")
        FusionUIBase.verify_element_text('Serial number label', GeneralServerProfilesElements.ID_TEXT_GENERAL_SERIAL_NUMBER_LABEL, 'Serial number (v)', timeout, fail_if_false)
        return ui_lib.wait_for_element_visible(GeneralServerProfilesElements.ID_TEXT_GENERAL_SERIAL_NUMBER, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_physical_uuid(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify 'UUID' label should contain '(p)', and value should be <%s>..." % expect_value)
        FusionUIBase.verify_element_text('UUID label', GeneralServerProfilesElements.ID_TEXT_GENERAL_UUID_LABEL, 'UUID (p)', timeout, fail_if_false)
        return FusionUIBase.verify_element_text('UUID', GeneralServerProfilesElements.ID_TEXT_GENERAL_UUID, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_physical_serial_number(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify 'Serial number' label should contain '(p)', and value should be <%s>..." % expect_value)
        FusionUIBase.verify_element_text('Serial number label', GeneralServerProfilesElements.ID_TEXT_GENERAL_SERIAL_NUMBER_LABEL, 'Serial number (p)', timeout, fail_if_false)
        return FusionUIBase.verify_element_text('Serial number', GeneralServerProfilesElements.ID_TEXT_GENERAL_SERIAL_NUMBER, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_power_on_error_visible_when_create_server_profile(cls, server_name, timeout=5, fail_if_false=False):
        logger.debug("verify that an error message should be visible saying the server hardware is powered on ...")
        if ui_lib.is_visible(CreateServerProfilesElements.ID_ERR_SERVER_HARDWARE_POWERED_ON, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("server hardware '%s' is found 'Powered on', '%s' returns TRUE" % (server_name, sys._getframe().f_code.co_name))
            return True
        else:
            logger.warn("server hardware '%s' is NOT found 'Powered on', '%s' returns FALSE" % (server_name, sys._getframe().f_code.co_name))
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_power_on_error_visible_when_edit_server_profile(cls, server_name, timeout=5, fail_if_false=False):
        logger.debug("verify that an error message should be visible saying the server hardware is powered on ...")
        if ui_lib.is_visible(EditServerProfilesElements.ID_ERR_SERVER_HARDWARE_POWERED_ON, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("server hardware '%s' is 'Powered on', '%s' returns TRUE" % (server_name, sys._getframe().f_code.co_name))
            return True
        else:
            logger.warn("server hardware '%s' is 'Powered off', '%s' returns FALSE" % (server_name, sys._getframe().f_code.co_name))
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_name(cls, expect_value, number, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.Connection.ID_TEXT_CONNECT_DISPLAY_NAME % (number, expect_value)
        item_name = "Connection name"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_port(cls, expect_value, number, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.Connection.ID_TEXT_CONNECT_DISPLAY_PORT % (number, expect_value)
        item_name = "Connection port"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_network(cls, expect_value, number, timeout=5, fail_if_false=True):
        logger.debug("verify Connection network '%s' is in '%d' row" % (expect_value, number))
        locator = GeneralServerProfilesElements.Connection.ID_TEXT_CONNECT_DISPLAY_NETWORK % number
        item_name = "Connection network"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_boot(cls, expect_value, number, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.Connection.ID_TEXT_CONNECT_DISPLAY_BOOT % (number, expect_value)
        item_name = "Connection boot"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connection_type(cls, expect_value, timeout=5, fail_if_false=True):
        return ui_lib.wait_for_element_visible(GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_FUNCTION_TYPE % expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_connection_function_type_disabled(cls, time_for_loading=0, timeout=5, fail_if_false=True):
        logger.debug("check if the dropdown list of 'Function Type' is disabled ...")
        BuiltIn().sleep(time_for_loading)
        locator = GeneralServerProfilesElements.Connection.ID_SELECTBOX_FUNCTION_TYPE
        class_attribute = ui_lib.get_webelement_attribute('class', locator, timeout=timeout, fail_if_false=fail_if_false)
        logger.debug("got attribute 'class' of locator <%s> is <%s>" % (locator, class_attribute))
        if 'disabled' in class_attribute.lower():
            logger.debug("'disabled' found in the class attribute of the dropdown list for 'Function Type'")
            return True
        else:
            logger.debug("'disabled' NOT found in the class attribute of the dropdown list for 'Function Type'")
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_requestedbandwidth(cls, expect_value, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.Connection.ID_TEXT_CONNECT_DISPLAY_BANDWIDTH
        item_name = "Connection requestedbandwidth"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_maxbandwidth(cls, expect_value, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.Connection.ID_TEXT_CONNECT_MAX_BANDWIDTH
        item_name = "Connection maxbandwidth"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_requested_virtual_functions_type(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify if 'Requested virtual functions' type is %s" % expect_value)
        locator = GeneralServerProfilesElements.ID_TEXT_CONNECTIONS_REQUESTED_VIRTUAL_FUNCTIONS
        item_name = "Requested virtual functions"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_interconnect(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify if 'Interconnect' is %s" % expect_value)
        locator = GeneralServerProfilesElements.ID_TEXT_CONNECTIONS_INTERCONNECT
        item_name = "Interconnect"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_allocated_virtual_functions_visible(cls, timeout=5, fail_if_false=True):
        logger.debug("verify if 'Allocated virtual functions' is visible")
        locator = GeneralServerProfilesElements.ID_TEXT_CONNECTIONS_ALLOCATED_VIRTUAL_FUNCTIONS
        return ui_lib.wait_for_element_visible(locator=locator, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_allocated_virtual_functions_not_visible(cls, timeout=5, fail_if_false=True):
        logger.debug("verify if 'Allocated virtual functions' is not visible")
        locator = GeneralServerProfilesElements.ID_TEXT_CONNECTIONS_ALLOCATED_VIRTUAL_FUNCTIONS
        return ui_lib.wait_for_element_notvisible(locator=locator, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_allocated_bandwidth_visible(cls, timeout=5, fail_if_false=True):
        logger.debug("verify if 'Allocated bandwith' is visible")
        locator = GeneralServerProfilesElements.ID_TEXT_CONNECTIONS_ALLOCATED_BANDWIDTH
        return ui_lib.wait_for_element_visible(locator=locator, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_allocated_bandwidth_not_visible(cls, timeout=5, fail_if_false=True):
        logger.debug("verify if 'Allocated bandwith' is not visible")
        locator = GeneralServerProfilesElements.ID_TEXT_CONNECTIONS_ALLOCATED_BANDWIDTH
        return ui_lib.wait_for_element_notvisible(locator=locator, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_max_bandwidth_visible(cls, timeout=5, fail_if_false=False):
        logger.debug("verify if 'Max bandwith' is visible")
        locator = GeneralServerProfilesElements.ID_TEXT_CONNECTIONS_MAX_BANDWIDTH
        return ui_lib.wait_for_element_visible(locator=locator, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_max_bandwidth_not_visible(cls, timeout=5, fail_if_false=False):
        logger.debug("verify if 'Max bandwith' is not visible")
        locator = GeneralServerProfilesElements.ID_TEXT_CONNECTIONS_MAX_BANDWIDTH
        return ui_lib.wait_for_element_notvisible(locator=locator, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_requested_virtual_functions_visible(cls, timeout=5, fail_if_false=False):
        logger.debug("verify if 'Requested virtual functions' is visible")
        locator = GeneralServerProfilesElements.ID_TEXT_CONNECTIONS_REQUESTED_VIRTUAL_FUNCTIONS_LABEL
        return ui_lib.wait_for_element_visible(locator=locator, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_requested_virtual_functions_not_visible(cls, timeout=5, fail_if_false=False):
        logger.debug("verify if 'Requested virtual functions' is not visible")
        locator = GeneralServerProfilesElements.ID_TEXT_CONNECTIONS_REQUESTED_VIRTUAL_FUNCTIONS_LABEL
        return ui_lib.wait_for_element_notvisible(locator=locator, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connection_status(cls, name, expect_value, timeout=15, fail_if_false=True):
        logger.debug("verify connection '%s' status should be '%s'." % (name, expect_value))
        locator = GeneralServerProfilesElements.ID_ICON_CONNECTION_STATUS % (name, expect_value.lower())
        return ui_lib.wait_for_element_visible(locator=locator, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_macaddress_type(cls, expect_value, timeout=15, fail_if_false=True):
        locator = GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_MACADDRESS
        # item_name = "Connection macaddress"
        item_name = "Connection Macaddress"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_wwpn(cls, expect_value, timeout=15, fail_if_false=True):
        logger.info("Verifying connections WWPN should be '%s'" % expect_value)
        locator = GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_WWPN
        item_name = "WWPN"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_wwnn(cls, expect_value, timeout=15, fail_if_false=True):
        logger.info("Verifying connections WWNN should be '%s'" % expect_value)
        locator = GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_WWNN
        item_name = "WWNN"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_boot_volume(cls, expect_value, timeout=15, fail_if_false=True):
        logger.info("Verifying connections Boot volume should be '%s'" % expect_value)
        locator = GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_BOOT_VOLUME
        item_name = "Boot volume"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_boot_target(cls, expect_value, timeout=15, fail_if_false=True):
        logger.info("Verifying connections Boot target should be '%s'" % expect_value)
        locator = GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_BOOT_TARGET
        item_name = "Boot target"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connections_boot_lun(cls, expect_value, timeout=15, fail_if_false=True):
        logger.info("Verifying connections Boot lun should be '%s'" % expect_value)
        locator = GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_BOOT_LUN
        item_name = "Boot LUN"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connection_initiator_name(cls, expect_value, timeout=5):
        if expect_value == 'not set':
            return ui_lib.wait_for_element_visible(GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_INITIATOR_NAME_UNSET, timeout, fail_if_false=True)
        else:
            return ui_lib.wait_for_element_visible(GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_INITIATOR_NAME % expect_value, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connection_initiator_ip(cls, expect_value, timeout=5, fail_if_false=True):
        return ui_lib.wait_for_element_visible(GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_INITIATOR_IP % expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connection_initiator_subnet_mask(cls, expect_value, timeout=5, fail_if_false=True):
        return ui_lib.wait_for_element_visible(GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_INITIATOR_SUBNET_MASK % expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connection_initiator_gateway(cls, expect_value, timeout=5):
        if expect_value == 'not set':
            return ui_lib.wait_for_element_visible(GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_INITIATOR_GATEWAY_UNSET, timeout, fail_if_false=True)
        else:
            return ui_lib.wait_for_element_visible(GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_INITIATOR_GATEWAY % expect_value, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connection_target_name(cls, expect_value, timeout=5, fail_if_false=True):
        return ui_lib.wait_for_element_visible(GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_TARGET_NAME % expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connection_target_lun(cls, expect_value, timeout=5, fail_if_false=True):
        return ui_lib.wait_for_element_visible(GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_TARGET_LUN % expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connection_target_ip(cls, expect_value, timeout=5, fail_if_false=True):
        return ui_lib.wait_for_element_visible(GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_TARGET_IP % expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connection_second_ip(cls, expect_value, timeout=5, fail_if_false=True):
        return ui_lib.wait_for_element_visible(GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_SECOND_IP % expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connection_chap_name(cls, expected_value, timeout=5):
        logger.debug("Verifying iSCSI CHAP Name is '%s' ..." % expected_value)
        if expected_value == 'not set':
            return ui_lib.wait_for_element_visible(GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_CHAP_NAME_NOT_SET, timeout, fail_if_false=True)
        else:
            return ui_lib.wait_for_element_visible(GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_CHAP_NAME % expected_value, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connection_mchap_name(cls, expected_value, timeout=5):
        logger.debug("Verifying iSCSI Mutual CHAP Name is '%s' ..." % expected_value)
        return ui_lib.wait_for_element_visible(GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_MCHAP_NAME % expected_value, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_connection_mchap_name_not_visible(cls, timeout=5):
        logger.debug("Verifying iSCSI Mutual CHAP Name is not visible ...")
        return ui_lib.wait_for_element_notvisible(GeneralServerProfilesElements.Connection.ID_TEXT_CONNECTION_MCHAP_NAME_HEADER, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_advanced_iscsi_initiator_name(cls, expect_value, timeout=5, fail_if_false=True):
        return FusionUIBase.verify_element_text(item_name='iSCSI Initiator Name', locator=GeneralServerProfilesElements.Advanced.ID_TEXT_ISCSI_INITIATOR_NAME,
                                                expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_advance_uuid(cls, expect_value, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.Advanced.ID_TEXT_UUID_DISPLAY_INFO
        item_name = "UUID"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_advance_mac_addresses(cls, expect_value, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.Advanced.ID_TEXT_MAC_MODE_DISPLAY_INFO
        item_name = "MAC addresses"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_advance_wwn_addresses(cls, expect_value, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.Advanced.ID_TEXT_WWN_MODE_DISPLAY_INFO
        item_name = "WWN addresses"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_advance_hide_unused_flexnics(cls, expect_value, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.Advanced.ID_TEXT_HIDE_UNUSED_FLEXNICS_DISPLAY_INFO
        item_name = "Hide unused FlexNICs"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_host_os_type(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify host os type should be '%s'..." % expect_value)
        locator = GeneralServerProfilesElements.SANStorage.ID_TEXT_HOST_OS_TYPE
        item_name = "Host OS type"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_no_volume_attachment_added(cls, timeout=5, fail_if_false=True):
        if ui_lib.wait_for_element_visible(GeneralServerProfilesElements.SANStorage.ID_TEXT_VOL_ATTACHMENT_MESSAGE, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("The message is successfully verified as visible within %s second(s)" % timeout)
            return True
        else:
            logger.debug("The message is failed to be verified as visible within %s second(s)" % timeout)
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_jbod_name(cls, mezzID, expect_value, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_TEXT_LOGICAL_JBOD_NAME % (mezzID, expect_value)
        item_name = "Name"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_jbod_drive_num(cls, mezzID, expect_value, drivename, timeout=5, fail_if_false=True):
        # Temporarily using Static index, working on getting dynamic index to work
        # index_in_table_head = int(ui_lib.get_html_element_index_in_row(
            # GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_ROW_LOGICAL_JBOD_VIEW_TABLE_HEAD,
            # GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_LOGICAL_JBOD_VIEW_RAID_LEVEL_COLUMN_HEAD)) - 2
        locator = GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_TEXT_LOGICAL_JBOD_LOGICAL_DRIVE % (mezzID, drivename, str(1))
        item_name = "Logical Drive"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_jbod_raid_level(cls, mezzID, expect_value, drivename, timeout=5, fail_if_false=True):
        # index_in_table_head = int(ui_lib.get_html_element_index_in_row(
            # GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_ROW_LOGICAL_JBOD_VIEW_TABLE_HEAD,
            # GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_LOGICAL_JBOD_VIEW_RAID_LEVEL_COLUMN_HEAD)) - 2
        locator = GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_TEXT_LOGICAL_JBOD_RAID_LEVEL % (mezzID, drivename, str(2))
        item_name = "RAID Level"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_jbod_num_of_drives(cls, mezzID, expect_value, drivename, timeout=5, fail_if_false=True):
        # index_in_table_head = ui_lib.get_html_element_index_in_row(
            # GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_ROW_LOGICAL_JBOD_VIEW_TABLE_HEAD,
            # GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_LOGICAL_JBOD_VIEW_NUM_OF_DRIVES_COLUMN_HEAD) - 2
        locator = GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_TEXT_LOGICAL_JBOD_NUM_OF_DRIVES % (mezzID, drivename, str(3))
        logger.debug(locator)
        item_name = "Number of Drives"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_jbod_min_gb(cls, mezzID, expect_value, drivename, timeout=5, fail_if_false=True):
        # index_in_table_head = ui_lib.get_html_element_index_in_row(
            # GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_ROW_LOGICAL_JBOD_VIEW_TABLE_HEAD,
            # GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_LOGICAL_JBOD_VIEW_MIN_GB_COLUMN_HEAD) - 2
        locator = GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_TEXT_LOGICAL_JBOD_MIN_GB % (mezzID, drivename, str(4))
        item_name = "Min GB"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_jbod_max_gb(cls, mezzID, expect_value, drivename, timeout=5, fail_if_false=True):
        # index_in_table_head = ui_lib.get_html_element_index_in_row(
            # GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_ROW_LOGICAL_JBOD_VIEW_TABLE_HEAD,
            # GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_LOGICAL_JBOD_VIEW_MAX_GB_COLUMN_HEAD) - 2
        locator = GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_TEXT_LOGICAL_JBOD_MAX_GB % (mezzID, drivename, str(5))
        item_name = "Max GB"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_jbod_drive_tech(cls, mezzID, expect_value, drivename, timeout=5, fail_if_false=True):
        # index_in_table_head = int(ui_lib.get_html_element_index_in_row(
            # GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_ROW_LOGICAL_JBOD_VIEW_TABLE_HEAD,
            # GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_LOGICAL_JBOD_VIEW_DRIVE_TECH_COLUMN_HEAD)) - 2
        locator = GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_TEXT_LOGICAL_JBOD_DRIVE_TECH % (mezzID, drivename, str(6))
        item_name = "Drive Technology"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_jbod_boot(cls, mezzID, expect_value, drivename, timeout=5, fail_if_false=True):
        # index_in_table_head = int(ui_lib.get_html_element_index_in_row(
            # GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_ROW_LOGICAL_JBOD_VIEW_TABLE_HEAD,
            # GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_LOGICAL_JBOD_VIEW_BOOT_COLUMN_HEAD)) - 1
        locator = GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_TEXT_LOGICAL_JBOD_BOOT % (mezzID, drivename, str(7))
        item_name = "Boot"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_jbod_status(cls, mezzID, expect_value, drivename, timeout=5, fail_if_false=True):
        if expect_value.lower() == 'ok':
            if ui_lib.wait_for_element_visible(GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_TEXT_LOGICAL_JBOD_STATUS_OK % (mezzID, drivename), timeout=10, fail_if_false=True):
                msg = "Jbod Drive name %s status is 'OK' as expected" % drivename
                logger.debug(msg)
        elif expect_value.lower() == 'error':
            if ui_lib.wait_for_element_visible(GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_TEXT_LOGICAL_JBOD_STATUS_ERROR % (mezzID, drivename), timeout=10, fail_if_false=True):
                msg = "Jbod Drive name %s status is 'error state' as expected " % drivename
                logger.debug(msg)
        elif expect_value.lower() == 'unknown':
            if ui_lib.wait_for_element_visible(GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_TEXT_LOGICAL_JBOD_UNKNOWN % (mezzID, drivename), timeout=10, fail_if_false=True):
                msg = "Jbod Drive name %s status is 'unknown state' as expected" % drivename
                logger.debug(msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_jbod_pending_state(cls, mezzID, drivename, expect_value='pending', timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_TEXT_LOGICAL_JBOD_PENDING % (mezzID, drivename)
        item_name = "Pending State"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_logical_jbod_expand(cls, mezzID, drivename, timeout=10, fail_if_false=True):
        logger.debug('clicking expand button to expose JBOD details')
        ui_lib.wait_for_element_and_click(GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_BUTTON_JBOD_DETAILS_EXPAND % (mezzID, drivename), timeout, fail_if_false)
        ui_lib.scroll_into_view(GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_TEXT_LOGICAL_JBOD_NAME % (mezzID, drivename))

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_zoned_drive_enclosure_name(cls, mezzID, drivename, drivenumber, timeout=10, fail_if_false=True):
        logger.debug('Getting zoned drive details')
        return ui_lib.get_text(GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_TEXT_ZONED_DRIVE_ENCLOSURE_NAME % (mezzID, drivename, drivenumber), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_zoned_hard_drive_info(cls, mezzID, drivename, drivenumber, profile_name, timeout=10, fail_if_false=True):
        logger.debug('Getting zoned drive details for JBOD name %s' % drivename)
        name = ui_lib.get_text(GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_TEXT_ZONED_HARD_DRIVE_NAME % (mezzID, drivename, drivenumber), timeout, fail_if_false)
        hdd_number = re.findall(r'\d+', name.split(',')[2])
        logger.info("hdd number is %s" % hdd_number)
        drive_enclosure = name.split(',')
        hdd_size = ui_lib.get_text(GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_TEXT_ZONED_HARD_DRIVE_SIZE % (mezzID, drivename, drivenumber), timeout, fail_if_false)
        drive_enclosure = drive_enclosure[0] + ',' + drive_enclosure[1]
        zoned_drive = {'jbod_name': drivename, 'bay_number': hdd_number[0], "drive_encl": drive_enclosure, 'size': hdd_size, 'server_profile': profile_name}
        return zoned_drive

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hdd_view_drive_server_profile(cls, drive):
        drive_bay = drive['bay_number']
        drive_server_profile = drive['server_profile']
        ui_lib.wait_for_element_visible(DriveEnclosuresElements.ID_DRIVES_VIEW_ROW_BY_BAY_NUMBER % drive_bay, timeout=15, fail_if_false=True)

        index_in_table_head = ui_lib.get_html_element_index_in_row(
            DriveEnclosuresElements.ID_ROW_DRIVES_VIEW_TABLE_HEAD,
            DriveEnclosuresElements.ID_DRIVES_VIEW_SERVER_PROFILE_COLUMN_HEAD)

        text = ui_lib.get_text(DriveEnclosuresElements.ID_DRIVES_VIEW_TABLE_CELL %
                               (drive_bay, str(index_in_table_head)), fail_if_false=True)

        if text == drive_server_profile:
            logger.info("Successfully verified that Drive %s has expected Server Profile of '%s'" % (drive_bay, drive_server_profile))
        elif text == drive_server_profile + " power on to see unknown values":
            logger.info("Successfully verified that Drive %s has expected Server Profile of but must power on to see unknown values'%s'" % (drive_bay, drive_server_profile))
        else:
            ui_lib.fail_test("Server Profile: %s of Drive: %s did not match expected Server Profile: '%s'" % (text, drive_bay, drive_server_profile))

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hdd_view_drive_capacity(cls, drive):
        drive_bay = drive['bay_number']
        drive_capacity = drive['size']

        index_in_table_head = ui_lib.get_html_element_index_in_row(
            DriveEnclosuresElements.ID_ROW_DRIVES_VIEW_TABLE_HEAD,
            DriveEnclosuresElements.ID_DRIVES_VIEW_CAPACITY_COLUMN_HEAD)

        text = ui_lib.get_text(DriveEnclosuresElements.ID_DRIVES_VIEW_TABLE_CELL %
                               (drive_bay, str(index_in_table_head)), fail_if_false=True)

        if text == drive_capacity:
            logger.info("Successfully verified that Drive %s has expected Capacity of '%s'" % (drive_bay, drive_capacity))
        else:
            ui_lib.fail_test("Capacity: %s of Drive: %s did not match expected Capacity: '%s'" % (text, drive_bay, drive_capacity))

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hdd_view_drive_logical_jbod(cls, drive):
        drive_bay = drive['bay_number']
        drive_logical_jbod = drive['jbod_name']

        index_in_table_head = ui_lib.get_html_element_index_in_row(
            DriveEnclosuresElements.ID_ROW_DRIVES_VIEW_TABLE_HEAD,
            DriveEnclosuresElements.ID_DRIVES_VIEW_LOGICAL_JBOD_COLUMN_HEAD)

        text = ui_lib.get_text(DriveEnclosuresElements.ID_DRIVES_VIEW_TABLE_CELL %
                               (drive_bay, str(index_in_table_head)), fail_if_false=True)

        if text == drive_logical_jbod:
            logger.info("Successfully verified that Drive %s has expected Logical JBOD of '%s'" % (drive_bay, drive_logical_jbod))
        else:
            ui_lib.fail_test("Logical JBOD: %s of Drive: %s did not match expected Logical JBOD: '%s'" % (text, drive_bay, drive_logical_jbod))

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_on_zoned_drive_link(cls, drivename, drivenumber, timeout=10, fail_if_false=True):
        logger.debug('Getting zoned drive details')
        ui_lib.wait_for_element_and_click(GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_TEXT_ZONED_DRIVE_ENCLOSURE_NAME % (drivename, drivenumber), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_drive_pending_state(cls, drivename, expect_value='pending', timeout=5, fail_if_false=True):
        index_in_table_head = int(ui_lib.get_html_element_index_in_row(
            GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_ROW_LOGICAL_DRIVE_VIEW_TABLE_HEAD,
            GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_LOGICAL_DRIVE_VIEW_LOGICAL_DRIVE_COLUMN_HEAD)) - 2
        locator = GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_TEXT_LOGICAL_DRIVE_PENDING % (drivename, str(index_in_table_head))
        item_name = "Pending State"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_integrated_storage_mode(cls, expect_value, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_TEXT_LOGICAL_DRIVE_MODE
        item_name = "Integrated Storage Mode"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_mezz_storage_mode(cls, mezzID, expect_value, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_TEXT_LOGICAL_JBOD_MODE % (mezzID)
        item_name = "Mezz Storage Mode"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_drive_name(cls, expect_value, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_TEXT_LOGICAL_DRIVE_NAME % expect_value
        item_name = "Name"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_drive_drive_num(cls, expect_value, drivename, timeout=5, fail_if_false=True):
        index_in_table_head = int(ui_lib.get_html_element_index_in_row(
            GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_ROW_LOGICAL_DRIVE_VIEW_TABLE_HEAD,
            GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_LOGICAL_DRIVE_VIEW_NUM_OF_DRIVES_COLUMN_HEAD)) - 2
        locator = GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_TEXT_LOGICAL_DRIVE_NUM_OF_DRIVES % (drivename, str(index_in_table_head))
        item_name = "Logical Drive"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_drive_raid_level(cls, expect_value, drivename, timeout=5, fail_if_false=True):
        index_in_table_head = int(ui_lib.get_html_element_index_in_row(
            GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_ROW_LOGICAL_DRIVE_VIEW_TABLE_HEAD,
            GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_LOGICAL_DRIVE_VIEW_RAID_LEVEL_COLUMN_HEAD)) - 2
        locator = GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_TEXT_LOGICAL_DRIVE_RAID_LEVEL % (drivename, str(index_in_table_head))
        item_name = "RAID level"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_drive_num_of_drives(cls, expect_value, drivename, timeout=5, fail_if_false=True):
        index_in_table_head = int(ui_lib.get_html_element_index_in_row(
            GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_ROW_LOGICAL_DRIVE_VIEW_TABLE_HEAD,
            GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_LOGICAL_DRIVE_VIEW_NUM_OF_DRIVES_COLUMN_HEAD)) - 2
        locator = GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_TEXT_LOGICAL_DRIVE_NUM_OF_DRIVES % (drivename, str(index_in_table_head))
        logger.debug(locator)
        item_name = "Number of Drives"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_drive_min_gb(cls, expect_value, drivename, timeout=5, fail_if_false=True):
        index_in_table_head = int(ui_lib.get_html_element_index_in_row(
            GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_ROW_LOGICAL_DRIVE_VIEW_TABLE_HEAD,
            GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_LOGICAL_DRIVE_VIEW_MIN_GB_COLUMN_HEAD)) - 2
        locator = GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_TEXT_LOGICAL_DRIVE_MIN_GB % (drivename, str(index_in_table_head))
        item_name = "Min GB"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_drive_max_gb(cls, expect_value, drivename, timeout=5, fail_if_false=True):
        index_in_table_head = int(ui_lib.get_html_element_index_in_row(
            GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_ROW_LOGICAL_DRIVE_VIEW_TABLE_HEAD,
            GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_LOGICAL_DRIVE_VIEW_MAX_GB_COLUMN_HEAD)) - 2
        locator = GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_TEXT_LOGICAL_DRIVE_MAX_GB % (drivename, str(index_in_table_head))
        item_name = "Max GB"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_drive_drive_tech(cls, expect_value, drivename, timeout=5, fail_if_false=True):
        index_in_table_head = int(ui_lib.get_html_element_index_in_row(
            GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_ROW_LOGICAL_DRIVE_VIEW_TABLE_HEAD,
            GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_LOGICAL_DRIVE_VIEW_DRIVE_TECH_COLUMN_HEAD)) - 2
        locator = GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_TEXT_LOGICAL_DRIVE_TECH % (drivename, str(index_in_table_head))
        item_name = "Drive Technology"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_drive_boot(cls, expect_value, drivename, timeout=5, fail_if_false=True):
        index_in_table_head = int(ui_lib.get_html_element_index_in_row(
            GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_ROW_LOGICAL_DRIVE_VIEW_TABLE_HEAD,
            GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_LOGICAL_DRIVE_VIEW_BOOT_COLUMN_HEAD)) - 2
        locator = GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_TEXT_LOGICAL_DRIVE_BOOT % (drivename, str(index_in_table_head))
        item_name = "Boot"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_drive_status(cls, expect_value, drivename, timeout=5, fail_if_false=True):
        if expect_value.lower() == 'ok':
            if ui_lib.wait_for_element_visible(GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_TEXT_LOGICAL_DRIVE_STATUS_OK % drivename, timeout=10, fail_if_false=True):
                msg = "Logical Drive name %s status is 'OK' " % drivename
                logger.debug(msg)
        elif expect_value.lower() == 'error':
            if ui_lib.wait_for_element_visible(GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_TEXT_LOGICAL_DRIVE_ERROR % drivename, timeout=10, fail_if_false=True):
                msg = "Logical Drive name %s status is 'error state' " % drivename
                logger.debug(msg)
        elif expect_value.lower() == 'unknown':
            if ui_lib.wait_for_element_visible(GeneralServerProfilesElements.LocalStorage.LogicalDrive.ID_TEXT_LOGICAL_DRIVE_UNKNOWN % drivename, timeout=10, fail_if_false=True):
                msg = "Logical Drive name %s status is 'unknown state' as expected" % drivename
                logger.debug(msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_san_storage_volume_exist(cls, expect_value, number, timeout=5, fail_if_false=True):
        locator = GeneralServerProfilesElements.SANStorage.Volume.ID_TEXT_VOLUME_NAME % number
        item_name = "Volume name"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_san_storage_lun_id(cls, expect_value, number, timeout=5, fail_if_false=True):
        logger.debug("verify storage lun id should be '%s'..." % expect_value)
        locator = GeneralServerProfilesElements.SANStorage.Volume.ID_TEXT_VOLUME_LUN_ID % (number, expect_value)
        item_name = "LUN id"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_san_storage_pool(cls, expect_value, number, timeout=5, fail_if_false=True):
        logger.debug("verify storage pool should be '%s'..." % expect_value)
        locator = GeneralServerProfilesElements.SANStorage.Volume.ID_TEXT_VOLUME_STORAGE_POOL % number
        item_name = "Storage pool"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_san_storage_capacity(cls, expect_value, number, timeout=5, fail_if_false=False):
        logger.debug("verify san storage volume capacity should be '%s' ..." % expect_value)
        locator = GeneralServerProfilesElements.SANStorage.Volume.ID_TEXT_VOLUME_STORAGE_CAPACITY % (number, expect_value)
        actual_value = ui_lib.get_text(locator, timeout=timeout, fail_if_false=fail_if_false).split()[0]

        item_name = "Storage capacity"
        try:
            if float(actual_value) == float(expect_value):
                logger.debug("%s is '%s', same as the expected value - '%s'" % (item_name, actual_value, expect_value))
                return True
            else:
                logger.warn("%s is '%s', NOT same as the expected value - '%s'" % (item_name, actual_value, expect_value))
                return False
        except ValueError:
            logger.warn("The value of capacity must be a digit")
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_san_storage_provisioning(cls, expect_value, number, timeout=5, fail_if_false=True):
        logger.debug("verify storage provisioning should be '%s'..." % expect_value)
        locator = GeneralServerProfilesElements.SANStorage.Volume.ID_TEXT_VOLUME_STORAGE_PROVISIONING % (number, expect_value)
        item_name = "Storage provisioning"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_san_storage_permanent(cls, expect_value, number, timeout=5, fail_if_false=True):
        logger.debug("verify storage permanent should be '%s'..." % expect_value)
        locator = GeneralServerProfilesElements.SANStorage.Volume.ID_TEXT_VOLUME_STORAGE_PERMANENT % number
        item_name = "Storage permanent"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_san_storage_sharing(cls, expect_value, number, timeout=5, fail_if_false=True):
        logger.debug("verify storage sharing should be '%s'..." % expect_value)
        locator = GeneralServerProfilesElements.SANStorage.Volume.ID_TEXT_VOLUME_STORAGE_SHARING % (number, expect_value)
        item_name = "Storage sharing"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_san_storage_network(cls, expect_value, number, sub_number, timeout=5, fail_if_false=True):
        logger.debug("verify storage network should be '%s'..." % expect_value)
        locator = GeneralServerProfilesElements.SANStorage.Volume.ID_TEXT_VOLUME_STORAGE_NETWORK % (number, number, sub_number)
        item_name = "Storage network"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_san_storage_network_status(cls, expect_value, number, sub_number, timeout=5, fail_if_false=True):
        logger.debug("verify storage network status  should be '%s'..." % expect_value)
        locator = GeneralServerProfilesElements.SANStorage.Volume.ID_TEXT_VOLUME_STORAGE_NETWORK_STATUS % (number, number, sub_number, expect_value)
        item_name = "Storage network status"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def verify_legacy_boot_settings(cls, profile, timeout=10, fail_if_false=True):
        if getattr(profile, 'BootSettings', None) is not None:
            logger.debug("Verifying Boot Mode for profile name %s" % profile.name)
            FusionUIBase.verify_element_text('Boot mode', GeneralServerProfilesElements.BootSettings.ID_TEXT_BOOT_MODE, profile.BootSettings.bootMode, timeout=timeout, fail_if_false=fail_if_false)
            if hasattr(profile.BootSettings, 'manageBootOrder') and profile.BootSettings.manageBootOrder.lower() == 'true':
                if getattr(profile.BootSettings, 'bootorder', None) is not None:
                    logger.debug("start setting boot orders ...")
                    boot_sequence = []
                    for index, boot_order in enumerate(profile.BootSettings.bootorder):
                        logger.debug("Boot number '%s' is boot device '%s'" % (index, boot_order.device))
                        boot_sequence.append(boot_order.device)
                    verify_order = ','.join(boot_sequence).replace(',', ', ')
                    logger.debug("Expected Boot Order is %s ..." % verify_order)
                    logger.debug("ActualBoot Order is %s ..." % ui_lib.get_text(GeneralServerProfilesElements.BootSettings.ID_TEXT_BOOT_ORDER, timeout, fail_if_false))
                    FusionUIBase.verify_element_text('Boot Order', GeneralServerProfilesElements.BootSettings.ID_TEXT_BOOT_ORDER, verify_order, timeout=timeout, fail_if_false=fail_if_false)
                else:
                    msg = "<test data missing>: test data node '<BootSettings><bootorder device=\"xxx\"/></BootSettings>' is missing for profile '%s'" % profile.name
                    ui_lib.fail_test(msg)
        else:
            msg = "<test data missing>: test data node '<BootSettings>' is missing for profile '%s'" % profile.name
            return ui_lib.fail_test(msg)

    @classmethod
    def verify_non_legacy_boot_settings(cls, profile, timeout=5, fail_if_false=True):
        # set boot order if attribute 'manageBootOrder' is true
        if getattr(profile, 'BootSettings', None) is not None:
            logger.debug("Verifying Boot Mode for profile name %s" % profile.name)
            FusionUIBase.verify_element_text('Boot mode', GeneralServerProfilesElements.BootSettings.ID_TEXT_BOOT_MODE, profile.BootSettings.bootMode, timeout=timeout, fail_if_false=fail_if_false)
            if getattr(profile.BootSettings, 'pxeBootPolicy', None) is not None:
                logger.debug("Verifying 'PXE boot policy' as '%s' ..." % profile.BootSettings.pxeBootPolicy)
                FusionUIBase.verify_element_text('Boot mode', GeneralServerProfilesElements.BootSettings.ID_TEXT_PXE_BOOT_POLICY, profile.BootSettings.pxeBootPolicy, timeout=timeout, fail_if_false=fail_if_false)
            else:
                msg = "<test data missing>: test data node '<pxeBootPolicy>' is missing for profile '%s'" % profile.name
                return ui_lib.fail_test(msg)
            if hasattr(profile.BootSettings, 'manageBootOrder') and profile.BootSettings.manageBootOrder.lower() == 'true':
                logger.debug("Verifying 'Primary Boot order' as '%s' ..." % profile.BootSettings.primaryBootDevice)
                FusionUIBase.verify_element_text('Boot Order', GeneralServerProfilesElements.BootSettings.ID_TEXT_BOOT_ORDER, profile.BootSettings.primaryBootDevice, timeout=timeout, fail_if_false=fail_if_false)
        else:
            msg = "<test data missing>: test data node '<BootSettings>' is missing for profile '%s'" % profile.name
            return ui_lib.fail_test(msg)

    @classmethod
    def verify_server_asset_info(cls, profile_name, ServerAssetInformation, timeout=10, fail_if_false=True):
        for setting in ServerAssetInformation:
            if setting.validateSettings.lower() == 'inconsistent':
                cls.select_bios_inconsistent_radio()
                cls.verify_server_asset_info_before_power_on(setting)
            elif setting.validateSettings.lower() == 'modified':
                cls.select_bios_modified_radio()
                cls.verify_server_asset_info_after_power_on(setting)
            else:
                msg = "<test data missing>: test data attribute '<validateSettings>' is missing for profile '%s'" % profile_name
                return ui_lib.fail_test(msg)

    @classmethod
    def verify_server_asset_info_before_power_on(cls, setting, timeout=10, fail_if_false=True):
        logger.debug("Verifying server asset before it is Powered on [%s] expected value")
        if hasattr(setting, 'AdminName'):
            cls.verify_administrator_info_expected_value('AdminName', setting.AdminName)
        if hasattr(setting, 'AdminEmail'):
            cls.verify_administrator_info_expected_value('AdminEmail', setting.AdminEmail)
        if hasattr(setting, 'AdminPhone'):
            cls.verify_administrator_info_expected_value('AdminPhone', setting.AdminPhone)
        if hasattr(setting, 'AdminOtherInfo'):
            cls.verify_administrator_info_expected_value('AdminOtherInfo', setting.AdminOtherInfo)

    @classmethod
    def verify_server_asset_info_after_power_on(cls, setting, timeout=10, fail_if_false=True):
        logger.debug("Verifying server asset after it is Powered on")
        if hasattr(setting, 'AdminName'):
            cls.verify_administrator_info_actual_value('AdminName', setting.AdminName)
        if hasattr(setting, 'AdminEmail'):
            cls.verify_administrator_info_actual_value('AdminEmail', setting.AdminEmail)
        if hasattr(setting, 'AdminPhone'):
            cls.verify_administrator_info_actual_value('AdminPhone', setting.AdminPhone)
        if hasattr(setting, 'AdminOtherInfo'):
            cls.verify_administrator_info_actual_value('AdminOtherInfo', setting.AdminOtherInfo)

    @classmethod
    def verify_administrator_info_expected_value(cls, admin_attribute, expected_value, timeout=5, fail_if_false=True):
        logger.debug("Verifying administrator info [%s] expected value" % admin_attribute)
        FusionUIBase.verify_element_text(admin_attribute, GeneralServerProfilesElements.BIOSSettings.ID_TEXT_BIOS_SETTINGS_EXPECTED % admin_attribute, expected_value, timeout, fail_if_false)

    @classmethod
    def verify_administrator_info_actual_value(cls, admin_attribute, actual_value, timeout=5, fail_if_false=True):
        logger.debug("Verifying administrator info [%s] actual value" % admin_attribute)
        FusionUIBase.verify_element_text(admin_attribute, GeneralServerProfilesElements.BIOSSettings.ID_TEXT_BIOS_SETTINGS_ACTUAL % admin_attribute, actual_value, timeout, fail_if_false)

    @classmethod
    def select_bios_inconsistent_radio(cls, timeout=5, fail_if_false=True):
        logger.debug("select_bios_inconsistent_radio")
        ui_lib.wait_for_element_and_click(GeneralServerProfilesElements.BIOSSettings.ID_RADIO_INCONSISTENT, timeout, fail_if_false)

    @classmethod
    def select_bios_modified_radio(cls, timeout=5, fail_if_false=True):
        logger.debug("select_bios_modified_radio")
        ui_lib.wait_for_element_and_click(GeneralServerProfilesElements.BIOSSettings.ID_RADIO_MODIFIED, timeout, fail_if_false)

    @classmethod
    def select_bios_all_radio(cls, timeout=5, fail_if_false=True):
        logger.debug("select_bios_all_radio")
        ui_lib.wait_for_element_and_click(GeneralServerProfilesElements.BIOSSettings.ID_RADIO_ALL, timeout, fail_if_false)


class VerifyServerProfile(_BaseVerifyServerProfile):
    e = GeneralServerProfilesElements.Connection

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_error_message_in_add_connection(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("Verifying error message for 'edit option' ...\nExpected message: '%s'" % expect_value)
        return FusionUIBase.verify_element_text("Actions", CreateServerProfilesElements.ID_CREATION_ERROR, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_bandwidth_error(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("Verifying error message for 'edit option' ...\nExpected message: '%s'" % expect_value)
        return FusionUIBase.verify_element_text("Actions", cls.e.ID_BANDWIDTH_ERROR, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_error_message_for_update_action(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("Verifying error message for update action ...\nExpected message: '%s'" % expect_value)
        return FusionUIBase.verify_element_text("Actions", CreateServerProfilesElements.ID_UPDATE_ERROR, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_activity_contains_text(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("Verifying activity contains: '%s'" % expect_value)
        return ui_lib.wait_for_element(GeneralServerProfilesElements.ID_TEXT_ACTIVITY_CONTENT % expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_profile_consistency_status(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("Verifying server profile consistency state: '%s'" % expect_value)
        locator = GeneralServerProfilesElements.ID_TEXT_GENERAL_CONSISTENCY_STATE
        ui_lib.wait_for_element_visible(locator)
        item_name = "Consistency State"
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)


class C7000VerifyServerProfile(_BaseVerifyServerProfile):
    pass


class TBirdVerifyServerProfile(_BaseVerifyServerProfile):
    pass


class DLVerifyServerProfile(_BaseCommonOperationServerProfile):
    pass


class _BaseDeleteServerProfile(object):
    e = DeleteServerProfilesElements

    @classmethod
    def select_action_delete(cls, timeout=5):
        logger.debug("select action 'Delete'")
        ui_lib.wait_for_element_and_click(GeneralServerProfilesElements.ID_DROPDOWN_ACTIONS, timeout=timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_ACTION_DELETE, timeout=timeout, fail_if_false=True)

    @classmethod
    def tick_force_delete_checkbox(cls, timeout=5):
        logger.debug("select option 'Force delete server profile'")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_FORCE_DELETE, timeout)

    @classmethod
    def untick_force_delete_checkbox(cls, timeout=5):
        logger.debug("un-select option 'Force delete server profile'")
        FusionUIBase.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_FORCE_DELETE, timeout)

    @classmethod
    def click_yes_delete_button(cls, timeout=5):
        logger.debug("click button 'Yes, delete'")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_YES_DELETE, timeout=timeout, fail_if_false=True)

    # 2015-08-10 Alex Ma - accidently added this func but turns out that no need for this,
    #                      since "For delete server profile" is always directly visible to user
    #                       (not like remove Enclosure that if remove failed then show 'Force remove' checkbox)
    # @classmethod
    # @TakeScreenShotWhenReturnFalseDeco
    # def wait_for_force_delete_checkbox_shown(cls, timeout=5, fail_if_false=True):
    #     logger.debug("waiting for option 'Force delete server profile' shown...")
    #     if ui_lib.wait_for_element_visible(cls.e.ID_CHECKBOX_FORCE_DELETE, timeout=timeout, fail_if_false=fail_if_false):
    #         logger.debug("option 'Force delete server profile' successfully showed up")
    #         return True
    #     else:
    #         msg = "failed to wait for option 'Force delete server profile' to show up"
    #         return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_server_profile_dialog_open(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for dialog 'Delete server profile' to show up ...")
        if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_DELETE_SERVER_PROFILE, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Delete server profile' successfully show up")
            return True
        else:
            msg = "failed to wait for dialog 'Delete server profile' to show up"
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_server_profile_dialog_disappear(cls, timeout=300, fail_if_false=True):
        logger.debug("waiting for dialog 'Delete server profile' to disappear ...")
        if ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_DELETE_SERVER_PROFILE, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("dialog 'Delete server profile' successfully disappeared")
            return True
        else:
            msg = "failed to wait for dialog 'Delete server profile' to disappear"
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout=timeout, fail_if_false=True)


class DeleteServerProfile(_BaseDeleteServerProfile):
    pass


class C7000DeleteServerProfile(_BaseDeleteServerProfile):
    pass


class TBirdDeleteServerProfile(_BaseDeleteServerProfile):
    pass


class DLDeleteServerProfile(_BaseDeleteServerProfile):
    pass


class _BasePowerOffServerProfile(object):

    @classmethod
    def select_action_power_off(cls, timeout=5):
        logger.debug("select action 'Power off'")
        ui_lib.wait_for_element_and_click(GeneralServerProfilesElements.ID_DROPDOWN_ACTIONS, timeout=timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(PowerOffServerProfilesElements.ID_SELECT_ACTION_POWER_OFF, timeout=timeout, fail_if_false=True)

    @classmethod
    def click_press_and_hold_button(cls, timeout=5):
        logger.debug("click button 'Press and hold'")
        ui_lib.wait_for_element_and_click(PowerOffServerProfilesElements.ID_BUTTON_PRESS_AND_HOLD, timeout=timeout, fail_if_false=True)

    @classmethod
    def click_momentary_press_button(cls, timeout=5):
        logger.debug("click button 'Momentary press'")
        ui_lib.wait_for_element_and_click(PowerOffServerProfilesElements.ID_BUTTON_MOMENTARY_PRESS, timeout=timeout, fail_if_false=True)

    @classmethod
    def click_close_button(cls, timeout=5):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(PowerOffServerProfilesElements.ID_BUTTON_CLOSE, timeout=timeout, fail_if_false=True)


class PowerOffServerProfile(_BasePowerOffServerProfile):
    pass


class C7000PowerOffServerProfile(_BasePowerOffServerProfile):
    pass


class TBirdPowerOffServerProfile(_BasePowerOffServerProfile):
    pass


class DLPowerOffServerProfile(_BasePowerOffServerProfile):
    pass


class _BasePowerOnServerProfile(object):

    @classmethod
    def select_action_power_on(cls, timeout=5):
        logger.debug("select action 'Power on'")
        ui_lib.wait_for_element_and_click(GeneralServerProfilesElements.ID_DROPDOWN_ACTIONS, timeout=timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(PowerOnServerProfilesElements.ID_SELECT_ACTION_POWER_ON, timeout=timeout, fail_if_false=True)


class PowerOnServerProfile(_BasePowerOnServerProfile):
    pass


class C7000PowerOnServerProfile(_BasePowerOnServerProfile):
    pass


class TBirdPowerOnServerProfile(_BasePowerOnServerProfile):
    pass


class DLPowerOnServerProfile(_BasePowerOffServerProfile):
    pass


class _BaseResetServerProfile(object):

    @classmethod
    def select_action_reset(cls, timeout=5):
        logger.debug("select action 'Reset'")
        ui_lib.wait_for_element_and_click(GeneralServerProfilesElements.ID_DROPDOWN_ACTIONS, timeout=timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(ResetServerProfilesElements.ID_SELECT_ACTION_RESET, timeout=timeout, fail_if_false=True)

    @classmethod
    def click_reset_button(cls, timeout=5):
        logger.debug("click button 'Reset'")
        ui_lib.wait_for_element_and_click(ResetServerProfilesElements.ID_BUTTON_RESET, timeout, fail_if_false=True)

    @classmethod
    def click_cold_boot_button(cls, timeout=5):
        logger.debug("click button 'Cold boot'")
        ui_lib.wait_for_element_and_click(ResetServerProfilesElements.ID_BUTTON_COLD_BOOT, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(ResetServerProfilesElements.ID_BUTTON_CANCEL, timeout=timeout, fail_if_false=True)


class ResetServerProfile(_BaseResetServerProfile):
    pass


class C7000ResetServerProfile(_BaseResetServerProfile):
    pass


class TBirdResetServerProfile(_BaseResetServerProfile):
    pass


class DLResetServerProfile(_BaseResetServerProfile):
    pass

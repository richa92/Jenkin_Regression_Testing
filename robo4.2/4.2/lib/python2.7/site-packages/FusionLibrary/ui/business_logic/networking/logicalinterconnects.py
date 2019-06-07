# (C) Copyright  2013 Hewlett-Packard Development Company, L.P.

"""
    Logical  Interconnect Page
"""

import sys
from datetime import datetime
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.business_logic.base import FusionUIBase, TakeScreenShotWhenReturnFalseDeco
from FusionLibrary.ui.business_logic.networking.logicalinterconnects_elements import *
import re


class _BaseVerifyLogicalInterconnects(object):
    # { General verification

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_notification_shown(cls, timeout=5, fail_if_false=False):
        logger.debug("verify [ Notification ] display")
        return ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_PANEL_NOTIFICATION, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_status_ok(cls, timeout=5, fail_if_false=False):
        logger.debug("verify [ status ] is ok")
        return ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_STATUS, timeout, fail_if_false)
    # }


class C7000VerifyLogicalInterconnects(_BaseVerifyLogicalInterconnects):
    pass


class TbirdVerifyLogicalInterconnects(_BaseVerifyLogicalInterconnects):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_update_firmware_message(cls, update_msg, liname, updateaction):
        if "No update required. Selected firmware is already installed in the logical interconnect %s." \
                % liname in update_msg:
            logger.debug("Firmware already installed.")
            return True
        elif "Stage complete" and "Activate complete" in update_msg:
            logger.debug("%s is successful" % updateaction)
            return True
        elif "Stage complete" in update_msg:
            logger.debug("%s is successful" % updateaction)
            return True
        else:
            logger.debug("error message is:" + update_msg)
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_sas_interconnect_firmware_from_li(cls):
        """
            This Function will compare sas interconnect installed firmware with baseline firmware.
            """
        #
        s2l = ui_lib.get_s2l()
        ic_firm = {}
        ic_installedversion = {}

        error_flag = 0

        logger.debug("Getting the list of interconnects and firmware versions")
        CommonOperationLogicalInterconnect.click_logical_interconnect_firmware()

        length = len(s2l._element_find(GeneralLogicalInterconnectsElements.ID_INTERCONNECT_NATASHA_LIST, False, True))
        logger.debug("The number of ics is %s" % length)
        for index in range(1, length + 1):
            installed_fw = ui_lib.get_text(
                UpdateLogicalInterconnectFirmwareElements.ID_SWITCH_FW_DETAILS % index + '/td[3]')
            baseline_fw = ui_lib.get_text(
                UpdateLogicalInterconnectFirmwareElements.ID_SWITCH_FW_DETAILS % index + '/td[4]')
            ic = ui_lib.get_text(UpdateLogicalInterconnectFirmwareElements.ID_SWITCH_FW_DETAILS % index + '/td[1]')
            ic_model = ui_lib.get_text(UpdateLogicalInterconnectFirmwareElements.ID_SWITCH_FW_DETAILS % index + '/td[2]')
            m = re.match(".*/.*/", installed_fw)
            if m:
                installed_fw = installed_fw.split()[0]
            if baseline_fw != installed_fw:
                logger.warn(
                    "Installed firmware '{0}' on IC '{1}', model: '{3}' is not same as baseline firmware '{2}'".format(
                        installed_fw, ic, baseline_fw, ic_model))
                error_flag = error_flag + 1
                ic_firm[ic] = baseline_fw
                ic_installedversion[ic] = installed_fw
            else:
                logger.debug(
                    "Installed firmware '{0}' on IC '{1}', model: '{3}' is same as baseline firmware '{2}'".format(
                        installed_fw, ic, baseline_fw, ic_model))
                ic_firm[ic] = baseline_fw
                ic_installedversion[ic] = installed_fw

        if error_flag != 0:
            logger.debug("Some mismatch in the versions comparision, please check")
            return False, ic_firm, ic_installedversion
        else:
            logger.debug(" Versions comparisions went well, Firmware activation is successful")
            return True, ic_firm, ic_installedversion


class VerifyLogicalInterconnects(object):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_mac_table_keys_visible(cls, key, timeout=5, fail_if_false=True):
        logger.debug("Verify Mac Table key [%s] is visible" % key)
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_TEXT_MAC_TABLE_KEY % key, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_interconnect_dropdown_default_value(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Interconnect ] value, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Interconnect", EditLogicalInterconnectsElements.ID_COMBO_INTERCONNECT_TYPE, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_mac_address_and_server_port(cls, port, mac_address, timeout=5, fail_if_false=True):
        logger.debug("Verify Mac address appeared for assigned server port")
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_TEXT_MAC_ADDRESS_AND_SERVER_PORT % (port, mac_address), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_mac_download_table_in_mac_address_view(cls, timeout=5, fail_if_false=True):
        logger.debug("Check Mac Table Download visibility")
        return ui_lib.wait_for_element_visible(InterconnectLinkPortsLogicalInterconnectsElements.ID_BUTTON_MAC_TABLE_DOWNLOAD, 15, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_mac_download_table_in_action_menu(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Action ] menu Dropdown")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_ACTION_MAIN_BTN, timeout, fail_if_false)
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_SELECT_ACTION_DOWNLOAD_MAC_TABLE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_interconnect_exist(cls, logical_interconnect, timeout=5, fail_if_false=False):
        logger.debug("verify [ Logical Interconnect '%s' ] is existing" % logical_interconnect)
        if ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_TABLE_LOGICAL_INTERCONNECT % logical_interconnect, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_interconnect_type(cls, logical_interconnect, timeout=5):
        logger.debug("verify [ Logical Interconnect type for '%s' ] " % logical_interconnect)
        if ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_BUTTON_SAS_LI_ACTIONS, timeout=10):
            li_type = 'sas'
        elif ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_BUTTON_ACTIONS, timeout=10):
            li_type = 'nonsas'
        else:
            ui_lib.fail_test('Actions for Logical interconnect [ %s ] not visible  ' % logical_interconnect)
        return li_type

    # Verify pauseFlood status
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_pause_flood_status(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("Validating pause flood status, expected value is [%s]" % expect_value)
        item_name = "Pause flood protection"
        locator = GeneralLogicalInterconnectsElements.ID_TEXT_PAUSEFLOODPROTECTION_STATUS
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name, locator, expect_value, timeout, fail_if_false)

    # F702- Verify status  of  tagged LLDP and Enhanced LLDP
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_taggedlldp_status(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("Validating LLDP Tagging Status, expected value is [%s]" % expect_value)
        item_name = "LLDP tagging"
        locator = GeneralLogicalInterconnectsElements.ID_ELEMENT_LLDPTAGGED_STATUS
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name, locator, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_enhancedlldp_status(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("Validating LLDP Enhanced TLV Status expected value is [%s]" % expect_value)
        item_name = "LLDP enhanced  TLV"
        locator = GeneralLogicalInterconnectsElements.ID_ELEMENT_LLDPTLV_STATUS
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name, locator, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logicalinterconnects_alert_message(cls, expect_value, timeout=10, fail_if_false=True):
        logger.debug("Validating alert message from the Logical Interconnect page [%s]" % expect_value)
        item_name = "Alert"
        locator = GeneralLogicalInterconnectsElements.ID_TEXT_NOTIFICATION_MESSAGE
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name, locator, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_scope_should_exist_in_edit_page(cls, name, timeout=5, fail_if_false=True):
        logger.debug("verify [ scope '%s' ] exist in scope edit page" % name)
        return ui_lib.wait_for_element_visible(EditScopeElements.ID_TABLE_SCOPE_NAME % name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_quality_of_service_qos_configuration_type(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ QoS configuration type ] in SNMP view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("QoS configuration type", GeneralLogicalInterconnectsElements. ID_TEXT_QUALITY_OF_SERVICE_QOS_CONFIGURATION_TYPE, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_passthrough_options(cls, timeout=10, fail_if_false=True):
        logger.debug("Check for the UPLINKOPTION is not existing ")
        if ui_lib.wait_for_element_notvisible(GeneralLogicalInterconnectsElements.ID_OPTION_UPLINK, timeout, fail_if_false):
            logger.debug("Check for the DOWNLINKOPTION is not existing ")
            if ui_lib.wait_for_element_notvisible(GeneralLogicalInterconnectsElements.ID_OPTION_DOWNLINK, timeout, fail_if_false):
                logger.debug("Check for the RESETOPTION is not existing ")
                if ui_lib.wait_for_element_notvisible(GeneralLogicalInterconnectsElements.ID_OPTION_RESET, timeout, fail_if_false):
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

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_traffic_option(cls, traffic, timeout=5, fail_if_false=True):
        logger.debug("Verifying traffic value  [ %s ]" % traffic)
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_TEXT_TRAFFIC % traffic, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_mappings_visibility(cls, mappings, timeout=5, fail_if_false=True):
        logger.debug("verify the DOTIP and DSCO VALUES for selected Class")
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_TEXT_MAPPINGS % mappings, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_dot1poption(cls, dot1p_value, timeout=5, fail_if_false=True):
        logger.debug("Checking for the DoIPvalue %s " % dot1p_value)
        if ui_lib.wait_for_element_notvisible(EditLogicalInterconnectsElements.ID_TABLE_DOTIP % dot1p_value, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("Successfully verified DoIPvalue %s is not present in selected QoS type" % dot1p_value)
            return True
        else:
            logger.warn("DOIP values %s is present for the selected QoS type " % dot1p_value)
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_priority_availability(cls, flag, timeout=5, fail_if_false=True):
        if flag:
            logger.debug(" priority is visible")
            return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_TABLE_DOT1P_AVAILABILITY)
        else:
            logger.debug(" priority not visible")
            return ui_lib.wait_for_element_notvisible(EditLogicalInterconnectsElements.ID_TABLE_DOT1P_AVAILABILITY)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_dot1p_and_dscp_availability(cls, flag, timeout=5, fail_if_false=True):
        if not flag:
            logger.debug("dot1p and dscp are not visible")
            return ui_lib.wait_for_element_notvisible(EditLogicalInterconnectsElements.ID_TABLE_DOT1P_MAPPING, EditLogicalInterconnectsElements.ID_TABLE_DSCP_MAPPING)
        else:
            logger.debug("dot1p and dscp are visible")
            return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_TABLE_DOT1P_MAPPING, EditLogicalInterconnectsElements.ID_TABLE_DSCP_MAPPING)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_realclass_invisibility(cls, timeout=5, fail_if_false=True):
        logger.debug("select the disabled text")
        if ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_TEXT_DISABLED, timeout, fail_if_false):
            logger.debug("class is already enabled")
            ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_TEXT_DISABLED, timeout, fail_if_false)
            return ui_lib.wait_for_element_notvisible(EditLogicalInterconnectsElements.ID_BUTTON_REALCLASS_ENABLE, timeout, fail_if_false)
        else:
            logger.debug("enabled the selected class ")
            ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_BUTTON_CLASS_ENABLE, timeout, fail_if_false)
            return ui_lib.wait_for_element_notvisible(EditLogicalInterconnectsElements.ID_BUTTON_REALCLASS_ENABLE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_interconnect_status_ok(cls, logical_interconnect, timeout=5, fail_if_false=True):
        logger.debug("verify [ Logical Interconnect '%s' ] is existing" % logical_interconnect)
        if ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_TABLE_LOGICAL_INTERCONNECT % logical_interconnect, timeout, fail_if_false):
            return True
        else:
            logger.warn("Failed to verify Logical interconnect '{}' visibility".format(logical_interconnect))
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_update_firmware_started(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify update firmware started")
        return ui_lib.wait_for_element_visible(TBirdUpdateFirmwareElements.ID_UPDATE_STARTED, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_update_firmware_progressbar_is_visible(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify update firmware progress bar")
        return ui_lib.wait_for_element_visible(TBirdUpdateFirmwareElements.ID_TEXT_PROGRESS_BAR, timeout, fail_if_false)

    @classmethod
    def verify_uplinkset_error_message_visible(cls, timeout=5, fail_if_false=True):
        logger.debug("verifing uplinkset error message visible")
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_ERROR_MSG_EDIT_US_APPEAR, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_edit_li_error_message_visible(cls, timeout=5, fail_if_false=True):
        logger.debug("verifing edit LI error message visible")
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_ERROR_MSG_EDIT_LI_APPEAR, timeout, fail_if_false)
    #  -  { SNMPV3 USERS

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_tbird_snmpv3_enabled(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify snnpv3 is enabled")
        return FusionUIBase.verify_element_text("SNMPv3", VerifyLogicalInterconnectElements.ID_LABEL_SNMPV3_ENABLED, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_snmp_user_confirm_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait for remove snmp_user dialog to show ")
        ui_lib.wait_for_element_visible(VerifyLogicalInterconnectElements.ID_DIALOG_REMOVE_SNMP_USER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_snmp_user_confirm_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait for remove snmp_user dialog to disappear ")
        ui_lib.wait_for_element_notvisible(VerifyLogicalInterconnectElements.ID_DIALOG_REMOVE_SNMP_USER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_snmp_user_table_disappear(cls, user, timeout=5, fail_if_false=True):
        logger.debug("wait SNMP snmp user table [ %s ] disappear" % user)
        return ui_lib.wait_for_element_notvisible(VerifyLogicalInterconnectElements.ID_TEXT_SNMP_USER % user, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_remove_snmpv3_user_error(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("get [ error ] in remove snmpv3 user ")
        return FusionUIBase.verify_element_text(" Remove SNMPv3 User", VerifyLogicalInterconnectElements.ID_TEXT_SNMP_USER_REMOVE_ERROR, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_trap_associated_user(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("get [ associated traps] in remove snmpv3 user ")
        return FusionUIBase.verify_element_text(" Used by Trap Destination", VerifyLogicalInterconnectElements.ID_TEXT_SNMP_USER_ASSOCITED_TRAPS % expect_value, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_snmp_user_confirm_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait for edit snmp_user dialog to show ")
        ui_lib.wait_for_element_visible(VerifyLogicalInterconnectElements.ID_DIALOG_EDIT_SNMP_USER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_snmp_user_confirm_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait for edit snmp_user dialog to disappear ")
        ui_lib.wait_for_element_notvisible(VerifyLogicalInterconnectElements.ID_DIALOG_EDIT_SNMP_USER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_add_snmp_user_dialog_visible(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add SNMP user ] dialog appear")
        return ui_lib.wait_for_element_visible(VerifyLogicalInterconnectElements.ID_DIALOG_ADD_SNMP_USER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_snmp_user_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ ADD SNMP USER ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(VerifyLogicalInterconnectElements.ID_DIALOG_ADD_SNMP_USER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_security_level_authentication_and_privacy_visibility(cls, timeout=5, fail_if_false=False):
        logger.debug("verify if[authentication and privacy] for security level is visible")
        return ui_lib.wait_for_element_visible(VerifyLogicalInterconnectElements.ID_RADIO_SECURITY_LEVEL_AUTHENTICATION_AND_PRIVACY, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_add_max_snmp_user_error_message(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verifying error message  when more than permitted number of snmp users are added")
        return FusionUIBase.verify_element_text("User name", VerifyLogicalInterconnectElements.ID_TEXT_ADD_SNMP_USER_OR_TRAP_ERROR, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_invalid_authentication_password_error_message(cls, error, timeout=5, fail_if_false=True):
        logger.debug("verifying if invalid authentication password is passed")
        return FusionUIBase.verify_element_text("Authentication password", VerifyLogicalInterconnectElements.ID_TEXT_ADD_SNMP_USER_INVALID_AUTH_PASSWORD_ERROR, error, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_invalid_privacy_password_error_message(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verifying if invalid privacy password is passed")
        return FusionUIBase.verify_element_text("Privacy password", VerifyLogicalInterconnectElements.ID_TEXT_ADD_SNMP_USER_INVALID_PRIV_PASSWORD_ERROR, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_invalid_username_error_message(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verifying if invalid username is passed")
        return FusionUIBase.verify_element_text("User name", VerifyLogicalInterconnectElements.ID_TEXT_ADD_SNMP_INVALID_USER_USERNAME_ERROR, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_duplicate_username_error_message(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verifying if duplicate username is passed")
        return FusionUIBase.verify_element_text("User name", VerifyLogicalInterconnectElements.ID_TEXT_ADD_SNMP_DUPLICATE_USER_USERNAME_ERROR, expect_value, timeout=timeout, fail_if_false=fail_if_false)

# - { TRAP DESTINATION
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_trap_destination_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add Trap Destination ] dialog shown")
        return ui_lib.wait_for_element_visible(VerifyLogicalInterconnectElements.ID_DIALOG_ADD_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_trap_destination_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add Trap Destination ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(VerifyLogicalInterconnectElements.ID_DIALOG_ADD_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_trap_destination_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add Trap Destination ] dialog shown")
        return ui_lib.wait_for_element_visible(VerifyLogicalInterconnectElements.ID_DIALOG_EDIT_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_trap_destination_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add Trap Destination ] dialog shown")
        return ui_lib.wait_for_element_notvisible(VerifyLogicalInterconnectElements.ID_DIALOG_EDIT_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_trap_destination_notification_visibility(cls, timeout=5, fail_if_false=True):
        logger.debug("Visible[ Notification Type ] in trap destination view")
        return ui_lib.is_visible(VerifyLogicalInterconnectElements.ID_TOGGLE_TRAP_DESTINATION_NOTIFICATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def view_snmpv3_trap_destination_snmp_user_visibility(cls, timeout=5, fail_if_false=True):
        logger.debug("View Trap destination snmpv3 [ snmp users ]")
        ui_lib.is_visible(VerifyLogicalInterconnectElements.ID_TEXT_SNMPV3_TRAP_DESTINATION_SNMP_USERS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_max_trap_error_message(cls, expect_value, timeout=5, fail_if_false=False):
        logger.debug("verifying error message  when more than permitted number of snmpv3 traps are added")
        return FusionUIBase.verify_element_text("Trap Destination", VerifyLogicalInterconnectElements.ID_TEXT_ADD_SNMP_USER_OR_TRAP_ERROR, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_no_snmp_user_error_msg(cls, expect_value, timeout=5, fail_if_false=False):
        logger.debug("Verifying Error message while adding trap wihtout snmp user")
        return FusionUIBase.verify_element_text("SNMP user", VerifyLogicalInterconnectElements.ID_TEXT_ADD_TRAP_NO_USER_ERROR_MSG, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_invalid_port_error(cls, expect_value, timeout=5, fail_if_false=False):
        logger.debug("Verifying Error message for invalid port while adding trap")
        return FusionUIBase.verify_element_text("Port", VerifyLogicalInterconnectElements.ID_TEXT_ADD_TRAP_ERROR_INVALID_PORT, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_invalid_engine_id_error(cls, expect_value, timeout=5, fail_if_false=False):
        logger.debug("Verifying Error message for invalid engine id while adding trap")
        return FusionUIBase.verify_element_text("Engine ID", VerifyLogicalInterconnectElements.ID_TEXT_ADD_TRAP_ERROR_INVALID_ENGINEID, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_snmpv3_trap_destination_confirm_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait remove trap destination confirm dialog shown")
        return ui_lib.wait_for_element_visible(VerifyLogicalInterconnectElements.ID_DIALOG_REMOVE_SNMPV3_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_snmpv3_trap_destination_confirm_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait remove trap destination confirm dialog disappear")
        return ui_lib.wait_for_element_notvisible(VerifyLogicalInterconnectElements.ID_DIALOG_REMOVE_SNMPV3_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_trap_destination_table_row_disappear(cls, destination, timeout=5, fail_if_false=True):
        logger.debug("wait SNMP trap destination table [ %s ] disappear" % destination)
        return ui_lib.wait_for_element_notvisible(VerifyLogicalInterconnectElements.ID_BUTTON_DELETE_SNMPV3_TRAP_DESTINATION % destination, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_enabled(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify snmpv3 [ Enabled ]")
        return FusionUIBase.verify_element_text("SNMP v3", VerifyLogicalInterconnectElements.ID_TEXT_SNMPV3_ENABLED, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_users_user_visiblity(cls, user, timeout=5, fail_if_false=True):
        logger.debug("verify [ SNMP USER '%s' ] exist in SNMP" % user)
        return ui_lib.is_visible(VerifyLogicalInterconnectElements.ID_TEXT_SNMP_USER % user)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_user_privacy_protocol(cls, user, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [privacy protocol '%s' ] of [ snmpv3 user'%s' ] in SNMPv3 users view" % (expect_value, user))
        return FusionUIBase.verify_element_text("SNMPv3 users Privacy protocol", VerifyLogicalInterconnectElements.ID_TEXT_SNMPV3_USERS_PRIVACY_PROTOCOL % user, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_user_auth_protocol(cls, user, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [authentication protocol '%s' ] of [ snmpv3 user'%s' ] in SNMPv3 users view" % (expect_value, user))
        return FusionUIBase.verify_element_text("SNMPv3 users Authentication protocol", VerifyLogicalInterconnectElements.ID_TEXT_SNMPV3_USERS_AUTHENTICATION_PROTOCOL % user, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmpv3_user_security_level(cls, user, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [security level '%s' ] of [ snmpv3 user'%s' ] in SNMPv3 users view" % (expect_value, user))
        return FusionUIBase.verify_element_text("SNMPv3 users Security Level", VerifyLogicalInterconnectElements.ID_TEXT_SNMPV3_USERS_SECURITY_LEVEL % user, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_trap_destinations_destination_visiblity(cls, destination, timeout=5, fail_if_false=True):
        logger.debug("verify [ Trap Destination '%s' ] exist in SNMP Trap Destinations view" % destination)
        return ui_lib.is_visible(VerifyLogicalInterconnectElements.ID_TEXT_SNMP_TRAP_DESTINATIONS_ROW_DESTINATION % destination)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_trap_destinations_port(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ port '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination Port", VerifyLogicalInterconnectElements.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_PORT % (destination, expect_value), expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_trap_destinations_username(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ UserName '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination UserName", VerifyLogicalInterconnectElements.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_USERNAME, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_trap_destinations_engineid(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Engine ID '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination Engine ID", VerifyLogicalInterconnectElements.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_ENGINEID, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_trap_destinations_notification_type(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Notification Type '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination Notification Type", VerifyLogicalInterconnectElements.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_NOTIFICATION_TYPE, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_trap_destinations_community_string(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Community String '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination community string", VerifyLogicalInterconnectElements.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_ROW_COMMUNITY_STRING % destination, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_trap_destinations_severity(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Format '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination severity", VerifyLogicalInterconnectElements.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_SEVERITY, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_trap_destinations_vcm_traps(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ port '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination Port", VerifyLogicalInterconnectElements.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_VCM_TRAPS, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_trap_destinations_enet_traps(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ port '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination ENET_Traps", VerifyLogicalInterconnectElements.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_ENET_TRAPS, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_trap_destinations_fc_traps(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ port '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination FC_Traps", VerifyLogicalInterconnectElements.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_FC_TRAPS, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_access_ip_or_subnet_visibility(cls, ip_or_subnet, timeout=5, fail_if_false=True):
        logger.debug("verify [ ip or subnet '%s' ] exist in SNMP Access view" % ip_or_subnet)
        return ui_lib.is_visible(cls.e.ID_TEXT_SNMP_SNMP_ACCESS_ROW_IP_OR_SUBNET % ip_or_subnet)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snmp_trap_destinations_format(cls, destination, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Format '%s' ] of [ destination '%s' ] in SNMP Trap Destinations view" % (expect_value, destination))
        return FusionUIBase.verify_element_text("Trap destination format", VerifyLogicalInterconnectElements.ID_TEXT_SNMPV3_TRAP_DESTINATIONS_ROW_FORMAT % (destination, expect_value), expect_value, timeout=timeout, fail_if_false=fail_if_false)


class CommonOperationLogicalInterconnect(object):

    @classmethod
    def click_logical_interconnect(cls, logical_interconnect, timeout=5, fail_if_false=False):
        logger.debug("select [ Logical Interconnect '%s' ]" % logical_interconnect)
        ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectsElements.ID_TABLE_LOGICAL_INTERCONNECT % logical_interconnect, timeout, fail_if_false)

    @classmethod
    def get_li_list(cls, timeout=5):
        logger.debug("Get all [ Logical Interconnect names ] from table")
        li_name_list = []
        if ui_lib.wait_for_element(GeneralLogicalInterconnectsElements.ID_TABLE_LOGICAL_INTERCONNECTS, timeout):
            li_name_list = FusionUIBase.get_multi_elements_text(GeneralLogicalInterconnectsElements.ID_TABLE_LOGICAL_INTERCONNECTS, timeout, fail_if_false=True)
        return li_name_list

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_logical_interconnect_selected(cls, logical_interconnect, timeout=5, fail_if_false=False):
        logger.debug("wait [ Logical Interconnect '%s' ] selected" % logical_interconnect)
        return ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_TEXT_LOGICAL_INTERCONNECT_TITLE % logical_interconnect, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_logical_interconnect_status_ok(cls, li_name, timeout=10, fail_if_false=False):
        start = datetime.now()
        logger.debug("waiting logical interconnect '%s' status change to ok" % li_name)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_STATUS_LOGICAL_INTERCONNECT_OK % li_name, timeout=2, fail_if_false=False):
                logger.debug("logical interconnect '%s' status is ok as expected." % li_name)
                return True
            elif ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_STATUS_LOGICAL_INTERCONNECT_WARN % li_name, timeout=2, fail_if_false=False):
                err_msg = "logical interconnect '%s' status is warning not as expected." % li_name
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            elif ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_STATUS_LOGICAL_INTERCONNECT_ERROR % li_name, timeout=2, fail_if_false=False):
                err_msg = "logical interconnect '%s' status is error not as expected." % li_name
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            else:
                logger.debug("logical interconnect status is unknown, waiting ...")
                continue
        err_msg = "Timeout to waiting logical interconnect '%s' status change to ok." % li_name
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)
        return True

    @classmethod
    def click_logical_interconnect_activity(cls, timeout=5, fail_if_false=False):
        logger.debug("Clicked Activity link to  go to  activity Page ")
        return FusionUIBase.select_view_by_name('Activity')

    @classmethod
    def wait_logical_interconnect_activity_message(cls, message, timeout=5, fail_if_false=False):
        logger.debug("wait for activity element to found in activity Page ")
        if ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_ACTIVITY_MESSAGE % message, timeout, fail_if_false):
            ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectsElements.ID_ACTIVITY_MESSAGE % message, timeout, fail_if_false)

            return True
        else:
            return False

    @classmethod
    def get_logical_interconnect_license_info(cls, timeout=5, fail_if_false=False):
        logger.debug("Get fc license state and license count of Logical Interconnect")
        lic_info = {}
        lic_info["license_state"] = FusionUIBase.get_text(GeneralLogicalInterconnectsElements.ID_LI_LICENSE_STATE)
        lic_info["license_count"] = FusionUIBase.get_text(GeneralLogicalInterconnectsElements.ID_LI_LICENSE_COUNT)
        return lic_info

    @classmethod
    def get_li_consistency_state(cls, timeout=5, fail_if_false=True):
        logger.debug("verify [ li consistency state ] is ok")
        return ui_lib.get_text(GeneralLogicalInterconnectsElements.ID_TEXT_LI_CONSISTENCY_STATE, timeout, fail_if_false)

    @classmethod
    def click_logical_interconnect_general(cls, timeout=5, fail_if_false=False):
        logger.debug("Clicked General link to go to General section ")
        FusionUIBase.select_view_by_name('General')

    @classmethod
    def click_logical_interconnect_firmware(cls, timeout=5, fail_if_false=False):
        logger.debug("Clicked Firmware link to go to Firmware section ")
        FusionUIBase.select_view_by_name('Firmware')

    @classmethod
    def get_interconnect_list_from_firmware_table(cls, timeout=5, fail_if_false=True):
        logger.debug("Get [ Interconnect list] from selected LE")
        ui_lib.wait_for_element(TBirdUpdateFirmwareElements.ID_INTERCONNECT_LIST, timeout, fail_if_false)
        return FusionUIBase.get_multi_elements_text(TBirdUpdateFirmwareElements.ID_INTERCONNECT_LIST, timeout, fail_if_false)

    @classmethod
    def click_logical_interconnect_logical_interconnect(cls, timeout=5, fail_if_false=False):
        logger.debug("Clicked Logical Interconnect link to go to Logical Interconnect section ")
        FusionUIBase.select_view_by_name('Logical Interconnect')

    @classmethod
    def click_logical_interconnect_view(cls, timeout=5, fail_if_false=False):
        logger.debug("Clicked View  [ To Select Activity link ]")
        return ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectsElements.ID_VIEW_SELECTOR, timeout, fail_if_false)

    @classmethod
    def get_li_stacking_health_status(cls, timeout=5, fail_if_false=True):
        logger.debug("Get [ stacking health status ] of the Logical Interconnect")
        return FusionUIBase.get_text(GeneralLogicalInterconnectsElements.ID_TEXT_LI_STACKING_HEALTH_STATUS, timeout, fail_if_false)

    @classmethod
    def get_activity_state_for_reapply(cls, logical_interconnect, timeout=5, fail_if_false=True):
        logger.debug("activity status of [ Logical Interconnect '%s' ]" % logical_interconnect)
        ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_VIEW_REAPPLY_LI_ACTIVITY, timeout, fail_if_false)
        ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_VIEW_REAPPLY_LI_ACTIVITY_MESSAGE, timeout, fail_if_false)
        return ui_lib.get_text(GeneralLogicalInterconnectsElements.ID_TEXT_REAPPLY_LI_ACTIVITY_STATE, timeout, fail_if_false)

    @classmethod
    def click_logical_uplink(cls, timeout=5):
        logger.debug("Click to Logical Uplink Link in Drop down")
        ui_lib.wait_for_element_and_click(InterconnectLinkPortsLogicalInterconnectsElements.ID_DROPDOWN)
        return ui_lib.wait_for_element_and_click(InterconnectLinkPortsLogicalInterconnectsElements.ID_LINK_LOGICAL_UPLINKS)

    @classmethod
    def get_uplinkset_data(cls, timeout=5):
        logger.debug("Read ULS data in LI")
        return ui_lib.get_text(InterconnectLinkPortsLogicalInterconnectsElements.ID_UPLINK_SET_DATA)

    @classmethod
    def verify_alert_msg_exist(cls, timeout=5):
        return ui_lib.wait_for_element_visible(InterconnectLinkPortsLogicalInterconnectsElements.ID_ERROR_WARN_MSG)

    @classmethod
    def get_alert_msg(cls, timeout=5):
        return ui_lib.get_text(InterconnectLinkPortsLogicalInterconnectsElements.ID_ERROR_WARN_MSG)

    @classmethod
    def expand_uplinkset_name(cls, uplink, timeout=5, fail_if_false=True):
        if ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_EXPAND_UPLINKSET_NAME % uplink, timeout, fail_if_false):
            ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectsElements.ID_EXPAND_UPLINKSET_NAME % uplink, timeout, fail_if_false)

    @classmethod
    def get_uplink_portspeed(cls, uplink, port, timeout=5, fail_if_false=True, hidden_element=False):
        ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_TEXT_PORT_SPEED % (uplink, port), timeout, fail_if_false)
        return ui_lib.get_multi_elements_text(GeneralLogicalInterconnectsElements.ID_TEXT_PORT_SPEED % (uplink, port), timeout, fail_if_false, hidden_element)

    @classmethod
    def get_fc_port_login(cls, uplink, port, timeout=5, fail_if_false=True, hidden_element=False):
        ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_TEXT_FC_PORT_LOGIN % (uplink, port), timeout, fail_if_false)
        return ui_lib.get_multi_elements_text(GeneralLogicalInterconnectsElements.ID_TEXT_FC_PORT_LOGIN % (uplink, port), timeout, fail_if_false, hidden_element)

    @classmethod
    def get_li_active_message_list(cls, timeout=5, fail_if_false=True):
        logger.debug("Get message and state list of activity in LI")
        ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_TEXT_LI_ACTIVITIY_MESSAGE, timeout, fail_if_false)
        msg_list = FusionUIBase.get_multi_elements_text(GeneralLogicalInterconnectsElements.ID_TEXT_LI_ACTIVITIY_MESSAGE, timeout, fail_if_false)
        ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_TEXT_LI_ACTIVITY_STATE, timeout, fail_if_false)
        state_list = FusionUIBase.get_multi_elements_text(GeneralLogicalInterconnectsElements.ID_TEXT_LI_ACTIVITY_STATE, timeout, fail_if_false)
        return msg_list, state_list

    @classmethod
    def get_uplink_set_data(cls, uplink, timeout=5, fail_if_false=True):
        logger.debug("Get uplinks data for '%s' from LI" % uplink)
        ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_TEXT_UPLINKSET_DATA % uplink, timeout, fail_if_false)
        data_list = FusionUIBase.get_multi_elements_text(GeneralLogicalInterconnectsElements.ID_TEXT_UPLINKSET_DATA % uplink, timeout, fail_if_false)
        # remove the empty spaces in the list by below
        data_list1 = [data for data in data_list if data]
        return data_list1

    @classmethod
    def get_uplink_set_port_data(cls, uplink, port, timeout=5, fail_if_false=True):
        logger.debug("Get uplink '%s' port '%s' data in uplinkset of LI" % (uplink, port))
        ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_TEXT_UPLINKSET_PORT_DATA % (uplink, port), timeout, fail_if_false)
        data_list = FusionUIBase.get_multi_elements_text(GeneralLogicalInterconnectsElements.ID_TEXT_UPLINKSET_PORT_DATA % (uplink, port), timeout, fail_if_false)
        data_list1 = [data for data in data_list if data]
        return data_list1

    @classmethod
    def click_li_uplink_set(cls, uplink, timeout=5, fail_if_false=True):
        logger.debug("Perform Click on uplink '%s' in LI" % uplink)
        return ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectsElements.ID_SELECT_UPLINKSET_SECTION % uplink, timeout, fail_if_false)

    @classmethod
    def click_snmpv3_trap_destination_values(cls, trap, timeout=5, fail_if_false=True):
        logger.debug("collapse trap destniation values")
        return ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectsElements.ID_DROPDOWN_SNMPV3_TRAP_DESTINATION_VALUES % trap, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def close_snmpv3_trap_destination_values(cls, trap, timeout=5, fail_if_false=True):
        logger.debug("collapse trap destniation values")
        return ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectsElements.ID_COLLAPSE_SNMPV3_TRAP_DESTINATION_VALUES % trap, timeout=timeout, fail_if_false=fail_if_false)


class UpdateFromGroupOperations(object):

    e = GeneralLogicalInterconnectsElements.UpdateFromGroup

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_and_click_actions_update(cls, timeout=5, fail_if_false=False):
        logger.debug("select [ Update from group ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectsElements.ID_BUTTON_ACTIONS, timeout, True)
        return ui_lib.wait_for_element_and_click(cls.e.ID_ACTION_UPDATE_FROM_GROUP, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_and_click_sas_actions_update(cls, timeout=5, fail_if_false=True):
        logger.debug("select SAS LI [ Update from group ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectsElements.ID_BUTTON_SAS_LI_ACTIONS, timeout, fail_if_false)
        return ui_lib.wait_for_element_and_click(cls.e.ID_ACTION_SAS_UPDATE_FROM_GROUP, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_update_from_group_dialog_shown(cls, timeout=5, fail_if_false=False):
        logger.debug("wait [ Update from Group ] dialog shown")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_UPDATE_FROM_GROUP, timeout, fail_if_false)

    @classmethod
    def click_yes_update_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Yes, update ] button")
        ui_lib.wait_for_element_visible(cls.e.ID_BUTTON_YES_UPDATE, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_YES_UPDATE, timeout, fail_if_false)

    @classmethod
    def click_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout, fail_if_false)

    @classmethod
    def tick_i_have_read_checkbox(cls, timeout=5):
        logger.debug("select option 'I have read and understand all of the implications' checkbox")
        FusionUIBase.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_I_HAVE_READ, timeout)

    @classmethod
    def click_yes_update_button_for_second_confirm(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Yes, update ] button when Second-Confirm")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_YES_UPDATE_SECOND_CONFIRM, timeout, fail_if_false)

    @classmethod
    def click_cancel_button_for_second_confirm(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button when Second-Confirm")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL_SECOND_CONFIRM, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_update_from_group_dialog_disappear(cls, timeout=5, fail_if_false=False):
        logger.debug("wait [ Update from Group ] dialog disappear ")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_UPDATE_FROM_GROUP, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_second_confirm_required(cls, timeout=10, fail_if_false=False):
        logger.debug("check if a Second-Confirm message popped out and requires user to select the agreement ...")
        if ui_lib.is_visible(cls.e.ID_CHECKBOX_I_HAVE_READ, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("'Second Confirm' message is present, '%s' returns TRUE" % sys._getframe().f_code.co_name)
            return True
        else:
            logger.warn("'Second Confirm' message is NOT present, '%s' returns FALSE" % sys._getframe().f_code.co_name)
            return False


class EditLogicalInterconnects(object):

    @classmethod
    def click_logical_mac_address(cls, timeout=5, fail_if_false=True):
        logger.debug("Click to Logical Mac Address in Drop down")
        ui_lib.wait_for_element_and_click(InterconnectLinkPortsLogicalInterconnectsElements.ID_DROPDOWN)
        return ui_lib.wait_for_element_and_click(InterconnectLinkPortsLogicalInterconnectsElements.ID_COMBO_LOGICAL_MAC_ADDRESS)

    @classmethod
    def get_mac_table_entries(cls, index, timeout=5, fail_if_false=True):
        logger.debug("get MAC table entries")
        return ui_lib.get_multi_elements_text(EditLogicalInterconnectsElements.ID_TABLE_MAC_TABLE_ENTRIES % index, timeout, fail_if_false)

    @classmethod
    def select_specific_interconnect(cls, interconnect, timeout=5, fail_if_false=True):
        logger.debug("select Interconnect [%s]" % interconnect)
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_COMBO_INTERCONNECT_TYPE, timeout, fail_if_false)
        return ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_TEXT_INTERCONNECT % interconnect, timeout, fail_if_false)

    @classmethod
    def select_all_interconnect(cls, timeout=5, fail_if_false=True):
        logger.debug("select Interconnect [All]")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_COMBO_INTERCONNECT_TYPE, timeout, fail_if_false)
        return ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_COMBO_INTERCONNECT_ALL, timeout, fail_if_false)

    @classmethod
    def input_and_select_network(cls, network, timeout=5, fail_if_false=True):
        logger.debug("select network [%s]" % network)
        ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_INPUT_VLAN_ID, " ", timeout, fail_if_false)
        ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_INPUT_NETWORK_NAME, network, timeout, fail_if_false)
        return ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_TEXT_NETWORK_OR_VLAN % network, timeout, fail_if_false)

    @classmethod
    def click_update(cls, timeout=5, fail_if_false=True):
        logger.debug("Click Update")
        return ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_UPDATE, timeout, fail_if_false)

    @classmethod
    def get_interconnect_name_list(cls, interconnect, timeout=5, fail_if_false=True):
        logger.debug("Get Interconnect list")
        ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_TABLE_INTERCONNECT % interconnect, 10, fail_if_false)
        return ui_lib.get_multi_elements_text(EditLogicalInterconnectsElements.ID_TABLE_INTERCONNECT % interconnect, timeout, fail_if_false)

    @classmethod
    def get_network_name_list(cls, timeout=5, fail_if_false=True):
        logger.debug("Get network list")
        ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_TABLE_NETWORK, 10, fail_if_false)
        return ui_lib.get_multi_elements_text(EditLogicalInterconnectsElements.ID_TABLE_NETWORK, timeout, fail_if_false)

    @classmethod
    def input_and_select_vlanid(cls, vlanid, timeout=5, fail_if_false=True):
        logger.debug("select Vlan id [%s]" % vlanid)
        ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_INPUT_VLAN_ID, vlanid, timeout=timeout, fail_if_false=fail_if_false)
        return ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_TEXT_NETWORK_OR_VLAN % vlanid, timeout, fail_if_false)

    @classmethod
    def input_mac_address(cls, mac_address, timeout=15, fail_if_false=True):
        logger.debug("Mac address [%s] is entered" % mac_address)
        ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_INPUT_MAC_ADDRESS, mac_address, timeout, fail_if_false)

    @classmethod
    def get_vlan_id_list(cls, timeout=5, fail_if_false=True):
        logger.debug("Get Vlan id list")
        ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_TABLE_VLAN, 10, fail_if_false)
        return ui_lib.get_multi_elements_text(EditLogicalInterconnectsElements.ID_TABLE_VLAN, timeout, fail_if_false)

    @classmethod
    def get_mac_address_list(cls, timeout=5, fail_if_false=True):
        logger.debug("Get mac address list")
        ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_TABLE_MAC_ADDRESS, 10, fail_if_false)
        return ui_lib.get_multi_elements_text(EditLogicalInterconnectsElements.ID_TABLE_MAC_ADDRESS, timeout, fail_if_false)

    # F702 Added lldp elements

    @classmethod
    def tick_interconnect_settings_lldp_tagging(cls, timeout=5):
        logger.debug("tick [ LLDP Tagging ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_select(EditLogicalInterconnectsElements.ID_CHKBOX_LLDP_TAGGING, timeout, fail_if_false=True)

    @classmethod
    def untick_interconnect_settings_lldp_tagging(cls, timeout=5):
        logger.debug("untick [ LLDP Tagging ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_unselect(EditLogicalInterconnectsElements.ID_CHKBOX_LLDP_TAGGING, timeout, fail_if_false=True)

    @classmethod
    def tick_interconnect_settings_lldp_enhancedtlv(cls, timeout=5):
        logger.debug("tick [ LLDP Enhaced TLV ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_select(EditLogicalInterconnectsElements.ID_CHKBOX_ENHANCED_TLV, timeout, fail_if_false=True)

    @classmethod
    def untick_interconnect_settings_lldp_enhancedtlv(cls, timeout=5):
        logger.debug("untick [ LLDP Enhaced TLV ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_unselect(EditLogicalInterconnectsElements.ID_CHKBOX_ENHANCED_TLV, timeout, fail_if_false=True)

    @classmethod
    def tick_interconnect_settings_pause_flood_protection(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ Pause flood protection ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_select(EditLogicalInterconnectsElements.ID_CHECKBOX_PAUSE_FLOOD_PROTECTION, timeout, fail_if_false)

    @classmethod
    def untick_interconnect_settings_pause_flood_protection(cls, timeout=5, fail_if_false=True):
        logger.debug("untick [ Pause flood protection ] in section [ Interconnect Settings ]")
        FusionUIBase.wait_for_checkbox_and_unselect(EditLogicalInterconnectsElements.ID_CHECKBOX_PAUSE_FLOOD_PROTECTION, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_quality_of_service_qos_configuration_type(cls, expect_value, timeout=10, fail_if_false=True):
        logger.debug("verify [ QoS configuration type ] in SNMP view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("QoS configuration type", EditLogicalInterconnectsElements. ID_TEXT_QUALITY_OF_SERVICE_QOS_CONFIGURATION_TYPE, expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def select_qos_configuration_type(cls, qos_configuration_type, timeout=5, fail_if_false=True):
        logger.debug("select QoS configuration type [ %s ]" % qos_configuration_type)
        FusionUIBase.choose_option_by_text(EditLogicalInterconnectsElements.ID_SELECT_QOS_CONFIGURATION_TYPE, qos_configuration_type, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_fcoelosssless_class_exists(cls, classname, timeout=5, fail_if_false=False):
        logger.debug("Checking FCoE Lossless")
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_OPTION_EDITCLASS % classname, timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_fcoe_lossless_class_no_edit_option(cls, classname, timeout=5, fail_if_false=True):
        logger.debug("Checking for the FCOElossless class ")
        if ui_lib.wait_for_element_notvisible(EditLogicalInterconnectsElements.ID_OPTION_EDIT % classname, timeout=5, fail_if_false=fail_if_false):
            logger.debug("Successfully verified FCoE lossless class has no edit option")
            return True
        else:
            logger.warn("clicked edit option for %s " % classname)
            return False

    @classmethod
    def get_fcoeshare(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking for FCoELosslessShare ")
        return FusionUIBase.get_text(EditLogicalInterconnectsElements.ID_TEXT_SHARE)

    @classmethod
    def get_fcoemaxshare(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking for FCoELosslessmaxShare")
        return FusionUIBase.get_text(EditLogicalInterconnectsElements.ID_TEXT_MAXSHARE)

    @classmethod
    def click_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_CANCEL, timeout, fail_if_false)

    @classmethod
    def select_qos_uplink_classfication(cls, qos_uplink_classfication, timeout=5, fail_if_false=True):
        logger.debug("select uplink QoS configuration type [ %s ]" % qos_uplink_classfication)
        FusionUIBase.choose_option_by_text(GeneralLogicalInterconnectsElements.ID_OPTION_UPLINK, qos_uplink_classfication, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_qos_downlink_classfication(cls, qos_downlink_classfication, timeout=5, fail_if_false=True):
        logger.debug("select downlink configuration type [ %s ]" % qos_downlink_classfication)
        FusionUIBase.choose_option_by_text(GeneralLogicalInterconnectsElements.ID_OPTION_DOWNLINK, qos_downlink_classfication, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_qos_class(cls, timeout=5, fail_if_false=True):
        logger.debug("click Enable button")
        if ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_TEXT_DISABLED, timeout, fail_if_false):
            logger.debug("class is already enabled")
            return False
        else:
            ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_CLASS_ENABLE, timeout, fail_if_false)
            logger.debug("class is enabled")
            return True

    @classmethod
    def input_share_values(cls, share_values, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into Share" % share_values)
        return ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_INPUT_SHAREVALUES, share_values, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_dot1p_values(cls, DOT1P, timeout=5, fail_if_false=True):
        logger.debug("tick DOTIP option")
        FusionUIBase.wait_for_checkbox_and_select(EditLogicalInterconnectsElements.ID_CHECKBOX_DOT1P_VALUES % DOT1P, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_dscp_values(cls, Dscpvalue, timeout=5, fail_if_false=True):
        logger.debug("tick DSCP option")
        ui_lib.wait_for_element_visible(cls.e.ID_CHECKBOX_DSCP_VALUES % Dscpvalue, timeout, fail_if_false)
        return FusionUIBase.wait_for_checkbox_and_select(EditLogicalInterconnectsElements.ID_CHECKBOX_DSCP_VALUES % Dscpvalue, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_class_ok_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ OK ] button")
        return ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_CLASS_OK, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_classname(cls, classname, timeout=5, fail_if_false=True):
        logger.debug("click the class name")
        return ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_OPTION_EDITCLASS % classname, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_classname(cls, lig_name, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] to name textbox" % lig_name)
        return ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_TEXT_INPUT_NAME, lig_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_error_message(cls, timeout=5, fail_if_false=True, hidden_element=False):
        return ui_lib.get_text(EditLogicalInterconnectsElements.ID_TEXT_VALIDATE_MSG, timeout, fail_if_false, hidden_element)

    @classmethod
    def get_share_value(cls, classno, share, timeout=5, fail_if_false=True):
        logger.debug("getting share value for the class %s" % classno)
        return ui_lib.get_text(EditLogicalInterconnectsElements.ID_TEXT_SHAREVALUE % (classno, share), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_qos_error_msg(cls, timeout=5, fail_if_false=True):
        logger.debug("getting the error mesg")
        return ui_lib.get_text(EditLogicalInterconnectsElements.ID_TEXT_QOS_ERROR, timeout, fail_if_false)

    @classmethod
    def get_uniquename(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking for Unique names ")
        return FusionUIBase.get_multi_elements_text(EditLogicalInterconnectsElements.ID_TABLE_CLASS_LIST)

    @classmethod
    def select_editoption(cls, classname, timeout=5, fail_if_false=True):
        logger.debug("Clicking the edit option for %s " % classname)
        if ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_OPTION_EDIT % classname, timeout=5, fail_if_false=fail_if_false):
            logger.debug("Clicked the edit option for %s " % classname)
            return True
        else:
            logger.debug("Failed to click edit option for %s " % classname)
            return False

    @classmethod
    def click_traffic_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button")
        return ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_CLASS_CANCEL, timeout, fail_if_false)

    @classmethod
    def select_egress_priority(cls, priority, timeout=5, fail_if_false=True):
        logger.debug("select QoS configuration type [ %s ]" % priority)
        return ui_lib.select_from_dropdown_by_dataid(EditLogicalInterconnectsElements.ID_DROPDOWN_EGRESS_PRIORITY, priority, timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_shareormax(cls, validateshareor, value, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] to share or Maxshare textbox" % validateshareor)
        return ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_INPUT_SHAREORMAX % validateshareor, value, timeout, fail_if_false)

    @classmethod
    def click_max_text(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Max ] text")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_OPTION_MAX, timeout, fail_if_false)

    @classmethod
    def get_class_enabled(cls, classno, timeout=5, fail_if_false=True):
        logger.debug("Check for the class %s" % classno)
        return ui_lib.get_text(EditLogicalInterconnectsElements.ID_TEXT_CLASS_NAME % classno, timeout=5, fail_if_false=fail_if_false)

    @classmethod
    def select_egress_fields(cls, timeout=5, fail_if_false=True):
        logger.debug("click egress mappings")
        return ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_TEXT_EGRESS_MAPPINGS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_egress_priority_values(cls, timeout=5, fail_if_false=True):
        logger.debug("fetching the Egress priority values")
        return FusionUIBase.get_multi_elements_text(EditLogicalInterconnectsElements.ID_TABLE_EGRESS_FIELDS, timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_class_enabled(cls, classno, timeout=5, fail_if_false=True):
        logger.debug("Check for the class %s" % classno)
        return ui_lib.get_text(EditLogicalInterconnectsElements.ID_TEXT_CLASS_NAME % classno, timeout=5, fail_if_false=fail_if_false)

    @classmethod
    def click_dot1p_priority_dropdown(cls, timeout=5, fail_if_false=True):
        logger.debug("click dot1p priority dropdown list")
        return ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_DOT1P_DROPDOWN_LIST, timeout, fail_if_false)

    @classmethod
    def select_dot1p_priority(cls, i, timeout=5, fail_if_false=True):
        logger.debug("select dot1p priority %s" % i)
        return FusionUIBase.get_text(EditLogicalInterconnectsElements.ID_TEXT_DOT1P_PRIORITY % i, timeout, fail_if_false)

    @classmethod
    def get_text_dot1p_value(cls, i, timeout=5, fail_if_false=True):
        logger.debug("select dot1p priority %s" % i)
        return FusionUIBase.get_text(EditLogicalInterconnectsElements.ID_TABLE_DOT1P_VALUE % i, timeout, fail_if_false)

    @classmethod
    def get_text_dot1p_current(cls, i, timeout=5, fail_if_false=True):
        logger.debug("select dot1p priority %s" % i)
        return FusionUIBase.get_text(EditLogicalInterconnectsElements.ID_TABLE_DOT1P_CURRENT % i, timeout, fail_if_false)

    @classmethod
    def get_text_dscp_value(cls, i, timeout=5, fail_if_false=True):
        logger.debug("select dscp value %s" % i)
        return FusionUIBase.get_text(EditLogicalInterconnectsElements.ID_TEXT_DSCP_VALUE % i, timeout, fail_if_false)

    @classmethod
    def get_text_dscp_current(cls, i, timeout=5, fail_if_false=True):
        logger.debug("select dscp current %s" % i)
        return FusionUIBase.get_text(EditLogicalInterconnectsElements.ID_TEXT_DSCP_CURRENT % i, timeout, fail_if_false)

    @classmethod
    def get_real_time_value_of_class(cls, enableclass, timeout=5, fail_if_false=True):
        logger.debug("The real time is enabled")
        return ui_lib.get_text(EditLogicalInterconnectsElements.ID_REAL_TIME_VALUE % enableclass, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_real_time_coloumn_value(cls, i, timeout=5, fail_if_false=True):
        logger.debug("The real time coloumn value")
        return ui_lib.get_text(EditLogicalInterconnectsElements.ID_REAL_TIME_COL % i, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_actions_menu(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Action ] menu Dropdown")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_ACTION_MAIN_BTN, timeout=timeout, fail_if_false=fail_if_false)
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_ACTION_MAIN_DROPDOWN, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_quality_of_service_section(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ Quality of Service ] section")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_DROPDOWN_PANEL_SELECTOR, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_SELECT_QUALITY_OF_SERVICE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_maxshare_value(cls, text, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] to name textbox" % text)
        return ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_INPUT_MAXSHARE_VALUES, text, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_dot1p_values(cls, DOT1P, timeout=5, fail_if_false=True):
        logger.debug("tick DOTIP option")
        return FusionUIBase.wait_for_checkbox_and_select(EditLogicalInterconnectsElements.ID_CHECKBOX_DOT1P_VALUES % DOT1P, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_dscp_values(cls, Dscpvalue, timeout=5, fail_if_false=True):
        logger.debug("tick DSCP option")
        ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_CHECKBOX_DSCP_VALUES % Dscpvalue, timeout, fail_if_false)
        return FusionUIBase.wait_for_checkbox_and_select(EditLogicalInterconnectsElements.ID_CHECKBOX_DSCP_VALUES % Dscpvalue, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_ok_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ OK ] button")
        return ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_OK, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_dot1p_dscp_mapping_values(cls, value, timeout=5, fail_if_false=True):
        logger.debug("Got ingress dot1p & dscp mapping values")
        return ui_lib.get_text(EditLogicalInterconnectsElements.ID_TEXT_DOT1P_DSCP_MAPPINGS % value, timeout=5, fail_if_false=fail_if_false)

    @classmethod
    def click_reset_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click Reset button")
        return ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_OPTION_RESET, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_besteffort_fcoe_priority(cls, timeout=5, fail_if_false=True):
        besteffort_fcoe_priority = []
        besteffort_fcoe_priority.append(FusionUIBase.get_text(EditLogicalInterconnectsElements.ID_BEST_EFFORT_PRIORITY))
        besteffort_fcoe_priority.append(FusionUIBase.get_text(EditLogicalInterconnectsElements.ID_FCOE_LOSELESS_PRIORITY))
        return besteffort_fcoe_priority

    @classmethod
    def click_qos_class_disable(cls, timeout=5, fail_if_false=True):
        logger.debug("Disable the class")
        return ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_OPTION_CLASS_DISABLE, timeout, fail_if_false)

    @classmethod
    def click_button_traffic_class(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_TRAFFIC_CLASS_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_real_time_value_of_class(cls, enableclass, timeout=5, fail_if_false=True):
        logger.debug("The real time is enabled")
        return ui_lib.get_text(EditLogicalInterconnectsElements.ID_REAL_TIME_VALUE % enableclass, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_real_time_coloumn_value(cls, i, timeout=5, fail_if_false=True):
        logger.debug("The real time coloumn value")
        return ui_lib.get_text(EditLogicalInterconnectsElements.ID_REAL_TIME_COL % i, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_traffic_class_value(cls, i, timeout=5, fail_if_false=True):
        logger.debug("The real time class value")
        return ui_lib.get_text(EditLogicalInterconnectsElements.ID_REAL_TIME_CLASSVALUE % i, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_qos_real_class(cls, timeout=5, fail_if_false=True):
        logger.debug("click Enable button")
        return ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_REALCLASS_ENABLE, timeout, fail_if_false)

    @classmethod
    def get_maxsharevalue(cls, realclass, timeout=5, fail_if_false=True):
        ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_TEXT_MAXSHAREVALUE % realclass, timeout, fail_if_false)
        return ui_lib.get_text(EditLogicalInterconnectsElements.ID_TEXT_MAXSHAREVALUE % realclass, timeout, fail_if_false)

    @classmethod
    def click_create_uplink_set_add_networks_to_add_plus(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add plus ] button in create uplink set add networks to dialog")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS_TO_ADD_PLUS, timeout, fail_if_false)

    @classmethod
    def wait_confirmation_dialog_appear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait confirmation dialog box appear")
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_CONFIRMARION_PROMPT, timeout, fail_if_false)

    @classmethod
    def click_perform_action_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Click perform action button")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_CREATE_UPLINK_PERFORM_ACTION_BUTTON, timeout, fail_if_false)

    @classmethod
    def tick_confirmation_checkbox(cls, timeout=5, fail_if_false=True):
        logger.debug("Tick Confirmation checkbox")
        FusionUIBase.wait_for_checkbox_and_select(EditLogicalInterconnectsElements.ID_CONFIRMATION_CHECKBOX, timeout, fail_if_false)

    @classmethod
    def check_correct_confirmation_ask_for(cls, confirmation, timeout=5, fail_if_false=True):
        logger.debug("verify corect confirmation text appear")
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_CONFIRMATION_TEXT % confirmation, timeout, fail_if_false)

    @classmethod
    def click_create_uplink_set_add_plus(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add plus ] button in create uplink set dialog")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_CREATE_UPLINK_SET_ADD_PLUS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_networks(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add networks ] button in create uplink set dialog")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_networks_to_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set > [ Add networks to ] dialog shown")
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_DIALOG_CREATE_UPLINK_SET_ADD_NETWORKS_TO, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_create_uplink_set_add_networks_to_search_network(cls, network_name, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] to search network textbox in create uplink set > add networks to dialog" % network_name)
        ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_INPUT_CREATE_UPLINK_SET_ADD_NETWORKS_TO_SEARCH_NETWORK, network_name, timeout=timeout, fail_if_false=fail_if_false)
        # workaround to fix sometime specific network not show in table list
        ui_lib.get_s2l().press_key(EditLogicalInterconnectsElements.ID_INPUT_CREATE_UPLINK_SET_ADD_NETWORKS_TO_SEARCH_NETWORK, "\\8")
        ui_lib.get_s2l().press_key(EditLogicalInterconnectsElements.ID_INPUT_CREATE_UPLINK_SET_ADD_NETWORKS_TO_SEARCH_NETWORK, network_name[-1:])

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_networks_to_table_row_shown(cls, network_name, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set > add networks to [ %s ] table item shown" % network_name)
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_TABLE_ROW_CREATE_UPLINK_SET_ADD_NETWORKS_TO % network_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_create_uplink_set_add_networks_to_add(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add ] button in create uplink set > add networks to dialog")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS_TO_ADD, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_networks_to_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set > [ Add networks to ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(EditLogicalInterconnectsElements.ID_DIALOG_CREATE_UPLINK_SET_ADD_NETWORKS_TO, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_create_uplink_set_native_network(cls, network_name, timeout=5, fail_if_false=True):
        logger.debug("tick vlan [ %s ] as native network in create uplink set dialog" % network_name)
        FusionUIBase.wait_for_checkbox_and_select(EditLogicalInterconnectsElements.ID_CHECKBOX_CREATE_UPLINK_SET_ETHERNET_NATIVE % network_name, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_network_table_row_shown(cls, network, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set network [ %s ] table row shown" % network)
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_TABLE_ROW_CREATE_UPLINK_SET_NETWORK % network, timeout, fail_if_false)

    @classmethod
    def verify_add_uplink_set_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("verify [ Add uplink set ] dialog shown")
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_DIALOG_CREATE_UPLINK_SET, timeout, fail_if_false)

    @classmethod
    def click_add_uplink_set(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add uplink set ] button dialog")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_ADD_UPLINK_SET, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Create uplink set dialog ] shown")
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_DIALOG_CREATE_UPLINK_SET, timeout, fail_if_false)

    @classmethod
    def input_create_uplink_set_name(cls, uplink_set_name, timeout=5, fail_if_false=True):
        logger.debug("input uplink set name [ %s ] in create uplink set dialog" % uplink_set_name)
        ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_INPUT_CREATE_UPLINK_SET_NAME, uplink_set_name, timeout, fail_if_false)

    @classmethod
    def select_create_uplink_set_type(cls, uplink_set_type, timeout=5, fail_if_false=True):
        logger.debug("select uplink set type [ %s ] in create uplink set dialog" % uplink_set_type)
        FusionUIBase.choose_option_by_text(EditLogicalInterconnectsElements.ID_SELECT_CREATE_UPLINK_SET_TYPE, uplink_set_type, timeout, fail_if_false)

    @classmethod
    def tick_create_uplink_set_connection_mode_automatic(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ Automatic (recommended) ] option")
        FusionUIBase.wait_for_checkbox_and_select(EditLogicalInterconnectsElements.ID_RADIO_CREATE_UPLINK_SET_CONNECTION_MODE_AUTOMATIC, timeout, fail_if_false)

    @classmethod
    def select_create_uplink_set_lacp_timer(cls, uplink_set_lacp_timer, timeout=5, fail_if_false=True):
        logger.debug("select LACP timer [ %s ]" % uplink_set_lacp_timer)
        FusionUIBase.choose_option_by_text(EditLogicalInterconnectsElements.ID_SELECT_CREATE_UPLINK_SET_LACP_TIMER, uplink_set_lacp_timer, timeout, fail_if_false)

    @classmethod
    def tick_create_uplink_set_connection_mode_failover(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ Failover ] option")
        FusionUIBase.wait_for_checkbox_and_select(EditLogicalInterconnectsElements.ID_RADIO_CREATE_UPLINK_SET_CONNECTION_MODE_FAILOVER, timeout, fail_if_false)

    @classmethod
    def select_create_uplink_set_tunnel_network(cls, network, timeout=5, fail_if_false=True):
        logger.debug("select tunnel network [ %s ] in create uplink set dialog" % network)
        FusionUIBase.choose_combo_option_by_text(EditLogicalInterconnectsElements.ID_COMBO_CREATE_UPLINK_SET_TUNNEL_NETWORK, network, timeout, fail_if_false)

    @classmethod
    def click_create_uplink_set_add_uplink_ports(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add uplink ports ] button in create uplink set dialog")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_CREATE_UPLINK_SET_ADD_UPLINK_PORTS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_uplink_ports_to_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set > [ Add uplink ports to ] dialog shown")
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_DIALOG_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_TO, timeout, fail_if_false)

    @classmethod
    def input_create_uplink_set_add_uplink_ports_to_search_port(cls, port_name, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] to search port textbox in create uplink set > add uplink ports to dialog" % port_name)
        ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_INPUT_CREATE_UPLINK_SET_ADD_UPLINK_PORT_SEARCH_PORT, port_name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_uplink_ports_to_table_row_shown(cls, bay_no, port_name, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set > add uplink ports to [ bay%s:%s ] table item shown" % (bay_no, port_name))
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_TABLE_ROW_CREATE_UPLINK_SET_ADD_UPLINK_PORT % (bay_no, port_name), timeout, fail_if_false)

    @classmethod
    def click_create_uplink_set_add_uplink_ports_to_table_row(cls, bay_no, port_name, timeout=5, fail_if_false=True):
        logger.debug("click [ bay%s:%s ] table item in create uplink set > add uplink ports to dialog" % (bay_no, port_name))
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_TABLE_ROW_CREATE_UPLINK_SET_ADD_UPLINK_PORT % (bay_no, port_name), timeout, fail_if_false)

    @classmethod
    def click_create_uplink_set_add_uplink_ports_to_add(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add ] button in create uplink set > add uplink ports to dialog")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_ADD, timeout, fail_if_false)

    @classmethod
    def click_create_uplink_set_add_uplink_ports_to_add_plus(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add plus ] button in create uplink set > add uplink ports to dialog")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_ADD_PLUS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_uplink_ports_to_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set > [ Add uplink ports to ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(EditLogicalInterconnectsElements.ID_DIALOG_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_TO, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_port_table_row_shown(cls, bay_no, port, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set port [ %s:%s ] table row shown" % (bay_no, port))
        return ui_lib.wait_for_element_visible(EditLogicalInterconnectsElements.ID_TABLE_ROW_CREATE_UPLINK_SET_PORT % (bay_no, port), timeout, fail_if_false)

    @classmethod
    def select_create_uplink_set_ethernet_port_speed(cls, port_name, port_speed, timeout=5, fail_if_false=True):
        """
        :param bay_no: bay number as integer.(don't pass bay_no like 'bay1')
        :param port_name:
        :param port_speed:
        :param timeout:
        """
        logger.debug("select port speed [ %s ] for ethernet port [ %s ] in create uplink set dialog" % (port_speed, port_name))
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_SELECT_UPLINK_SET_ETHERNET_PORT_SPEED, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_COMBO_UPLINK_SET_ETHERNET_PORT_SPEED % (port_speed), timeout, fail_if_false)

    @classmethod
    def select_create_uplink_set_untagged_network(cls, network, timeout=5, fail_if_false=True):
        logger.debug("select untagged network [ %s ] in create uplink set dialog" % network)
        FusionUIBase.choose_combo_option_by_text(EditLogicalInterconnectsElements.ID_COMBO_CREATE_UPLINK_SET_UNTAGGED_NETWORK, network, timeout, fail_if_false)

    @classmethod
    def select_create_uplink_set_fc_network(cls, network, timeout=5, fail_if_false=True):
        logger.debug("select fc network [ %s ] in create uplink set dialog" % network)
        FusionUIBase.choose_combo_option_by_text(EditLogicalInterconnectsElements.ID_COMBO_CREATE_UPLINK_SET_FC_NETWORK, network, timeout, fail_if_false)

    @classmethod
    def select_create_uplink_set_fc_port_speed(cls, bay_no, port_name, port_speed, timeout=5, fail_if_false=True):
        """

        :param bay_no: bay number as integer.(don't pass bay_no like 'bay1')
        :param port_name:
        :param port_speed:
        :param timeout:
        """
        logger.debug("select port speed [ %s ] for fc port [ %s ] of bay [ %s ] in create uplink set dialog" % (port_speed, port_name, bay_no))
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_SELECT_CREATE_UPLINK_SET_FC_PORT_SPEED % (bay_no, port_name), timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_DROPDOWN_CREATE_UPLINK_SET_FC_PORT_SPEED % (bay_no, port_name, port_speed), timeout, fail_if_false)

    @classmethod
    def get_uplinkset_error_message(cls, timeout=5, fail_if_false=True):
        logger.debug("getting error message")
        return ui_lib.get_text(EditLogicalInterconnectsElements.ID_ERROR_MSG_EDIT_US, timeout, fail_if_false)

    @classmethod
    def click_create_uplinkset_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click create uplink set cancel button")
        return ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_UPLINK_CANCEL, timeout, fail_if_false)

    @classmethod
    def click_edit_li_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click edit LI cancel button")
        return ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_LI_EDIT_CANCEL_BUTTON, timeout, fail_if_false)

    @classmethod
    def get_edit_li_error_message(cls, timeout=5, fail_if_false=True):
        logger.debug("getting error message")
        return ui_lib.get_text(EditLogicalInterconnectsElements.ID_ERROR_MSG_EDIT_LI, timeout, fail_if_false)

    @classmethod
    def click_create_uplink_set_add_networks_to_cancel(cls, timeout=5, fail_if_false=True):
        logger.debug("click cancel button of add network")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS_CANCEL, timeout, fail_if_false)

    @classmethod
    def click_create_uplink_set_add(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add ] button in create uplink set dialog")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_CREATE_UPLINK_SET_ADD, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_dialog_disappear(cls, timeout=15, fail_if_false=True):
        logger.debug("wait [ Create uplink set dialog ] shown")
        val = ui_lib.wait_for_element_notvisible(EditLogicalInterconnectsElements.ID_DIALOG_CREATE_UPLINK_SET, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_uplink_set_add_networks_to_table_row_not_shown(cls, network_name, flag, timeout=5, fail_if_false=True):
        logger.debug("wait create uplink set add networks to [ %s ] table item not shown" % network_name)
        return ui_lib.wait_for_element_notvisible(EditLogicalInterconnectsElements.ID_TABLE_ROW_CREATE_UPLINK_SET_ADD_NETWORKS_TO % network_name, timeout, fail_if_false)

    @classmethod
    def click_cancel_uplink_set_create(cls, timeout=5, fail_if_false=True):
        logger.debug("click cancel button of create uplinkset")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_CANCEL_UPLINK_SET, timeout, fail_if_false)

# - { Snmpv3 users
    @classmethod
    def toggle_snmpv3_disabled(cls, timeout=5):
        logger.debug("toggle snmpv3 [ Disabled ]")
        FusionUIBase.toggle_button(EditLogicalInterconnectsElements.ID_TOGGLE_SNMPv3, False, timeout=timeout)

    @classmethod
    def toggle_snmpv3_enabled(cls, timeout=5):
        logger.debug("toggle snmpv3 [ Enabled ]")
        FusionUIBase.toggle_button(EditLogicalInterconnectsElements.ID_TOGGLE_SNMPv3, True, timeout=timeout)

    @classmethod
    def click_remove_snmp_user_icon(cls, user, timeout=5, fail_if_false=True):
        logger.debug("click [ remove snmp user ] icon ")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_REMOVE_SNMP_USER % user, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_remove_snmp_user_confirm(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ remove trap destination ] icon ")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_REMOVE_SNMP_USER_CONFIRM, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_snmp_error_close_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ close] button in error dialog ")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_SNMP_ERROR_DIALOG_CLOSE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_snmp_user_delete_error_icon(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ collapse ] icon in error dialog ")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_COLLAPSE_SNMP_ERROR_DIALOG_TRAPS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_text_associated_trap_destination(cls, timeout=5, fail_if_false=True):
        logger.debug("Bring eleemts in to view point in error dialog ")
        FusionUIBase.scroll_element_into_viewpoint(cls.e.ID_TEXT_SNMP_ERROR_DIALOG_TRAPS)
        return ui_lib.get_text(EditLogicalInterconnectsElements.ID_TEXT_SNMP_ERROR_DIALOG_TRAPS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_snmp_user(cls, user, timeout=5, fail_if_false=True):
        logger.debug("click [ Edit snmp user] icon ")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_EDIT_SNMP_USER % user, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_snmp_user_edit(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ ok button ] icon in edit snmp user")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_OK_EDIT_SNMP_USER, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_add_snmp_user_name(cls, username, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [ username ] in Add SNMP user dialog" % username)
        ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_INPUT_ADD_SNMP_USER_NAME, username, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_security_level_none(cls, timeout=5, fail_if_false=True):
        logger.debug("choose option [none] for security level")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_RADIO_SECURITY_LEVEL_NONE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_security_level_authentication(cls, timeout=5, fail_if_false=True):
        logger.debug("choose option [authentication] for security level")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_RADIO_SECURITY_LEVEL_AUTHENTICATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_dropdown_authentication_protocol(cls, timeout=5, fail_if_false=True):
        logger.debug("clicking drop down button to select authentication protocol")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_COLLAPSE_AUTHENTICATION_PROTOCOL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_authentication_protocols(cls, timeout=5, fail_if_false=True):
        logger.debug("Fetching the available authentication protocol")
        return ui_lib.get_text(EditLogicalInterconnectsElements.ID_TEXT_AUTHENTICATION_PROTOCOL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_privacy_protocols(cls, timeout=5, fail_if_false=True):
        logger.debug("Fetching the available privacy protocol")
        return ui_lib.get_text(EditLogicalInterconnectsElements.ID_TEXT_PRIVACY_PROTOCOL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_authentication_protocol(cls, protocol, timeout=5, fail_if_false=True):
        logger.debug("selecting authentication protocol %s" % protocol)
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_SELECT_AUTHENTICATION_PROTOCOL % protocol, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_authentication_password(cls, password, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [  Authentication password ] in Add SNMP user dialog" % password)
        ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_INPUT_AUTHENTICATION_PASSWORD, password, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_confirm_authentication_password(cls, password, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [  confirm password ] in Add SNMP user dialog" % password)
        ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_INPUT_CONFIRM_AUTHENTICATION_PASSWORD, password, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_dropdown_privacy_protocol(cls, timeout=5, fail_if_false=True):
        logger.debug("clicking drop down button to select privacy protocol")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_COLLAPSE_AUTHENTICATION_AND_PRIVACY_PROTOCOL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_security_level_authentication_and_privacy(cls, timeout=5, fail_if_false=True):
        logger.debug("choose option [authentication and privacy] for security level")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_RADIO_SECURITY_LEVEL_AUTHENTICATION_AND_PRIVACY, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_authentication_and_privacy_protocol(cls, protocol, timeout=5, fail_if_false=True):
        logger.debug("selecting authenticationandprivacy protocol %s" % protocol)
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_SELECT_AUTHENTICATION_AND_PRIVACY_PROTOCOL % protocol, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_privacy_password(cls, password, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [  privacy password ] in Add SNMP user dialog" % password)
        ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_INPUT_PRIVACY_PASSWORD, password, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_confirm_privacy_password(cls, password, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [  confirm password ] in Add SNMP user dialog" % password)
        ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_INPUT_CONFIRM_PRIVACY_PASSWORD, password, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_snmp_user_add(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add ] button in Add SNMP user dialog")
        return ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_ADD_SNMP_USER_ADD, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_snmp_user_add_plus(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add plus ] button in Add Trap Destination dialog")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_ADD_SNMP_USER_ADD_PLUS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_snmp_user_cancel(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ cancel ] button in add snmp user ")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_ADD_SNMPV3_USER_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_snmp_user(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ add SNMP user] button ")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_ADD_SNMP_USER, timeout=timeout, fail_if_false=fail_if_false)
    # }
    # { TRAP DESTINATION

    @classmethod
    def click_add_trap_destination(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add trap destination ] button")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_ADD_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_add_trap_destination_trap_destination(cls, trapdestination, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [ Trap destination ] in Add Trap Destination dialog" % trapdestination)
        ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_INPUT_ADD_TRAP_DESTINATION_TRAP_DESTINATION, trapdestination, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_trap_destination_icon(cls, destination, timeout=5, fail_if_false=True):
        logger.debug("click [ edit trap destination ] icon of %s" % destination)
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_EDIT_TRAP_DESTINATION % destination, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_add_trap_destination_community_string(cls, communitystring, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [ Community string ] in Add Trap Destination dialog" % communitystring)
        ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_INPUT_ADD_TRAP_DESTINATION_COMMUNITY_STRING, communitystring, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_add_trap_destination_trap_format_snmpv1(cls, timeout=5, fail_if_false=True):
        logger.debug("tick Trap Format [ SNMPv1 ]")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_RADIO_ADD_TRAP_DESTINATION_TRAP_FORMAT_SNMPV1, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_add_trap_destination_trap_format_snmpv2(cls, timeout=5, fail_if_false=True):
        logger.debug("tick Trap Format [ SNMPv2 ]")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_RADIO_ADD_TRAP_DESTINATION_TRAP_FORMAT_SNMPV2, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_add_trap_destination_trap_format_snmpv3(cls, timeout=5, fail_if_false=True):
        logger.debug("tick Trap Format [ SNMPv3 ]")
        return ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_RADIO_ADD_TRAP_DESTINATION_TRAP_FORMAT_SNMPV3, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_trap_destination_add(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add ] button in Add Trap Destination dialog")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_ADD_TRAP_DESTINATION_ADD, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_edit_trap_destination_ok(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ edit trap destination ] ok button")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_EDIT_TRAP_DESTINATION_OK, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def disable_snmpv3_trap_destination_notification(cls, timeout=5):
        logger.debug("Disable [ Notification Type ] in trap destination view")
        FusionUIBase.toggle_button(EditLogicalInterconnectsElements.ID_TOGGLE_TRAP_DESTINATION_NOTIFICATION, False, timeout=timeout)

    @classmethod
    def enable_snmpv3_trap_destination_notification(cls, timeout=5):
        logger.debug("Enable [ Notification Type ] in trap destination view")
        FusionUIBase.toggle_button(EditLogicalInterconnectsElements.ID_TOGGLE_TRAP_DESTINATION_NOTIFICATION, True, timeout=timeout)

    @classmethod
    def input_add_trap_destination_engine_id(cls, engineid, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [ Engine ID ] in Add Trap Destination dialog" % engineid)
        ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_INPUT_TRAP_DESTINATION_ENGINE_ID, engineid, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_dropdown_snmpv3_user_in_trap_destination(cls, timeout=5, fail_if_false=True):
        logger.debug("List Trap destination snmpv3 [ snmp users ]")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_COLLAPSE_USER_TRAP_DESTINATION, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def get_snmpv3_user_in_trap_destination(cls, timeout=5, fail_if_false=True):
        logger.debug("Listing all the available snmp users")
        return ui_lib.get_text(EditLogicalInterconnectsElements.ID_TEXT_SNMPV3_TRAP_DESTINATION_SNMP_USERS, timeout, fail_if_false)

    @classmethod
    def select_snmpv3_user_in_trap_destination(cls, user, timeout=5, fail_if_false=True):
        logger.debug("Select Trap destination snmpv3 [ snmp users ]")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_SELECT_SNMPV3_TRAP_DESTINATION_SNMP_USER % user, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_trap_destination_port(cls, port, timeout=5, fail_if_false=True):
        logger.debug("input [ %s ] into [ port] in Add Trap Destination user dialog" % port)
        ui_lib.wait_for_element_and_input_text(EditLogicalInterconnectsElements.ID_INPUT_ADD_TRAP_DESTINATION_PORT, port, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_severity(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ severity ] button in Add Trap Destination dialog")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_COLLAPSE_ADD_TRAP_DESTINATION_SEVERITY, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_trap_destination_severity(cls, severity, timeout=5, fail_if_false=True):
        logger.debug("select [ severity ] in Add Trap Destination dialog")
        return FusionUIBase.wait_for_checkbox_and_select(EditLogicalInterconnectsElements.ID_BUTTON_ADD_TRAP_DESTINATION_SELECT_SEVERITY % severity, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_vcm_traps(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ VCM traps ] button in Add Trap Destination dialog")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_COLLAPSE_ADD_TRAP_DESTINATION_VCM_TRAPS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_trap_destination_vcm_trap(cls, trap, timeout=5, fail_if_false=True):
        logger.debug("select [ VCM trap ] in Add Trap Destination dialog")
        FusionUIBase.wait_for_checkbox_and_select(EditLogicalInterconnectsElements.ID_BUTTON_ADD_TRAP_DESTINATION_SELECT_VCM_TRAP % trap, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_vc_enet_traps(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ VC_ENET trap ] button in Add Trap Destination dialog")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_COLLAPSE_ADD_TRAP_DESTINATION_VC_ENET_TRAPS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_trap_destination_vc_enet_traps(cls, trap, timeout=5, fail_if_false=True):
        logger.debug("select [ VC_ENET trap ] in Add Trap Destination dialog")
        FusionUIBase.wait_for_checkbox_and_select(EditLogicalInterconnectsElements.ID_BUTTON_ADD_TRAP_DESTINATION_SELECT_ENET_TRAP % trap, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_vc_fc_traps(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ VC_FC trap] button in Add Trap Destination dialog")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_COLLAPSE_ADD_TRAP_DESTINATION_VC_FC_TRAPS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_trap_destination_vc_fc_traps(cls, trap, timeout=5, fail_if_false=True):
        logger.debug("select [ VC_FC trap] in Add Trap Destination dialog")
        FusionUIBase.wait_for_checkbox_and_select(EditLogicalInterconnectsElements.ID_BUTTON_ADD_TRAP_DESTINATION_SELECT_FC_TRAP % trap, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_trap_destination_add_plus(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Add plus ] button in Add Trap Destination dialog")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_ADD_TRAP_DESTINATION_ADD_PLUS, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_add_trap_destination_cancel(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button in Add Trap Destination dialog")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_ADD_TRAP_DESTINATION_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_remove_snmpv3_trap_destination_icon(cls, destination, timeout=5, fail_if_false=True):
        logger.debug("click [ remove trap destination ] icon of %s" % destination)
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_DELETE_SNMPV3_TRAP_DESTINATION % destination, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_remove_trap_destination_yes_remove(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Yes, Remove ] button in remove trap destination confirm dialog")
        ui_lib.wait_for_element_and_click(EditLogicalInterconnectsElements.ID_BUTTON_REMOVE_TRAP_DESTINATION_YES_REMOVE, timeout=timeout, fail_if_false=fail_if_false)

    # - }


class InterconnectLinkPortsOperations(object):

    @classmethod
    def get_enclosure_list_from_logical_interconnect(cls, timeout=5, fail_if_false=True):
        logger.debug("Get all [ enclosure names ] from table")
        enclosure_list = []
        if ui_lib.wait_for_element(InterconnectLinkPortsLogicalInterconnectsElements.ID_TEXT_ENCLOSURE_LIST, timeout, fail_if_false):
            enclosure_list = FusionUIBase.get_multi_elements_text(InterconnectLinkPortsLogicalInterconnectsElements.ID_TEXT_ENCLOSURE_LIST, timeout, fail_if_false, True)
        return enclosure_list

    @classmethod
    def get_interconnect_bay_list(cls, count, timeout=15, fail_if_false=True):
        logger.debug("Get [ interconnect, bay information] for enclosure")
        ic_bay_list = []
        s2l = ui_lib.get_s2l()
        baylist = s2l._element_find(InterconnectLinkPortsLogicalInterconnectsElements.ID_TEXT_INTERCONNECT_BAY_LIST_INFORMATION % count, False, False)
        for bay in baylist:
            ic_bay = ui_lib.get_text(bay, timeout)
            ic_bay_list.append(ic_bay)
        return ic_bay_list

    @classmethod
    def get_interconnect_bay_label(cls, encl_no, bay_no, timeout=5, fail_if_false=True):
        return FusionUIBase.get_text(InterconnectLinkPortsLogicalInterconnectsElements.ID_ICM_BAY_LABEL % (encl_no, bay_no), timeout, fail_if_false)

    @classmethod
    def get_interconnect_bay_model(cls, encl_no, bay_no, timeout=5, fail_if_false=True):
        return FusionUIBase.get_text(InterconnectLinkPortsLogicalInterconnectsElements.ID_ICM_BAY_MODEL % (encl_no, bay_no), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_overview_mouseover_port_information(cls, count, ic_bay, number, timeout=5, fail_if_false=True):
        logger.debug("get [ port ] in Overview for virtual connect")
        port = FusionUIBase.get_text(InterconnectLinkPortsLogicalInterconnectsElements.ID_CXPPORT % (count, ic_bay, number), timeout, fail_if_false)
        return port

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_overview_mouseover_port_status(cls, count, ic_bay, number, timeout=5, fail_if_false=True):
        logger.debug("get [ port status] in Overview for virtual connect")
        port_status = FusionUIBase.get_text(InterconnectLinkPortsLogicalInterconnectsElements.ID_CXPPORT_STATUS % (count, ic_bay, number), timeout, fail_if_false, True)
        return port_status

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_overview_mouseover_port_state(cls, count, ic_bay, number, timeout=5, fail_if_false=True):
        logger.debug("get [ port state] in Overview for virtual connect")
        selenium2lib = ui_lib.get_s2l()
        ui_lib.scroll_into_view(InterconnectLinkPortsLogicalInterconnectsElements.ID_CXPPORT % (count, ic_bay, number), False)
        selenium2lib.mouse_over(InterconnectLinkPortsLogicalInterconnectsElements.ID_CXPPORT % (count, ic_bay, number))
        state = FusionUIBase.get_text(InterconnectLinkPortsLogicalInterconnectsElements.ID_CXPPORT_STATE % (count, ic_bay, number), timeout, fail_if_false)
        return state

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_overview_mouseover_port_connectedto(cls, count, ic_bay, number, timeout=5, fail_if_false=True):
        logger.debug("get [ port connected to] in Overview for virtual connect")
        selenium2lib = ui_lib.get_s2l()
        ui_lib.scroll_into_view(InterconnectLinkPortsLogicalInterconnectsElements.ID_CXPPORT % (count, ic_bay, number), False)
        ui_lib.find_element_and_move(InterconnectLinkPortsLogicalInterconnectsElements.ID_CXPPORT % (count, ic_bay, number))
        selenium2lib.mouse_over(InterconnectLinkPortsLogicalInterconnectsElements.ID_CXPPORT % (count, ic_bay, number))
        connected_to_information = FusionUIBase.get_text(InterconnectLinkPortsLogicalInterconnectsElements.ID_CXPPORT_CONNECTED % (count, ic_bay, number), timeout, fail_if_false)
        return connected_to_information

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_overview_mouseover_port_information_of_extender_interconnect(cls, count, ic_bay, number, timeout=5, fail_if_false=True):
        logger.debug("get [ extender port ] in Overview ")
        port = FusionUIBase.get_text(InterconnectLinkPortsLogicalInterconnectsElements.ID_CXPPORT_OF_EXTENDER_IC % (count, ic_bay, (12 + number)), timeout, fail_if_false)
        return port

    @classmethod
    def get_overview_mouseover_port_status_of_extender_interconnect(cls, count, ic_bay, number, timeout=5, fail_if_false=True):
        logger.debug("get [ port status] in Overview")
        port_status = FusionUIBase.get_text(InterconnectLinkPortsLogicalInterconnectsElements.ID_CXPPORT_STATUS_OF_EXTENDER_IC % (count, ic_bay, (12 + number)), timeout, fail_if_false, True)
        return port_status

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_overview_mouseover_port_state_of_extender_interconnect(cls, count, ic_bay, number, timeout=5, fail_if_false=True):
        logger.debug("get [ port state of extender interconnect] in Overview ")
        selenium2lib = ui_lib.get_s2l()
        ui_lib.scroll_into_view(InterconnectLinkPortsLogicalInterconnectsElements.ID_CXPPORT_OF_EXTENDER_IC % (count, ic_bay, (12 + number)), False)
        ui_lib.find_element_and_move(InterconnectLinkPortsLogicalInterconnectsElements.ID_CXPPORT_OF_EXTENDER_IC % (count, ic_bay, (12 + number)))
        state = FusionUIBase.get_text(InterconnectLinkPortsLogicalInterconnectsElements.ID_CXPPORT_STATE_OF_EXTENDER_IC % (count, ic_bay, (12 + number)), timeout, fail_if_false)
        return state

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_overview_mouseover_port_connectedto_of_extender_interconnect(cls, count, ic_bay, number, timeout=5, fail_if_false=True):
        logger.debug("get [ port connected to] in Overview")
        selenium2lib = ui_lib.get_s2l()
        ui_lib.scroll_into_view(InterconnectLinkPortsLogicalInterconnectsElements.ID_CXPPORT_OF_EXTENDER_IC % (count, ic_bay, (12 + number)), False)
        ui_lib.find_element_and_move(InterconnectLinkPortsLogicalInterconnectsElements.ID_CXPPORT_OF_EXTENDER_IC % (count, ic_bay, (12 + number)))
        connected_to_information = FusionUIBase.get_text(InterconnectLinkPortsLogicalInterconnectsElements.ID_CXPPORT_CONNECTED_OF_EXTENDER_IC % (count, ic_bay, (12 + number)), timeout, fail_if_false)
        return connected_to_information


class _BaseEditScopeForLogicalInterconnect(object):

    """
    This class holds all edit scope operation of logical interconnect
    IT can work with C7000 & TBird
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
        logger.debug("click scope name '%s'" % name)
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_TABLE_SCOPE_NAME % name, wait_timeout, fail_if_false=True)

    @classmethod
    def click_remove_scope_icon(cls, name, wait_timeout=5):
        logger.debug("click to remove scope '%s'" % name)
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_TABLE_REMOVE_SCOPE % name, wait_timeout, fail_if_false=True)


class EditScopeForLogicalInterconnect(_BaseEditScopeForLogicalInterconnect):
    pass


class C7000EditScopeForLogicalInterconnect(_BaseEditScopeForLogicalInterconnect):
    pass


class TBirdEditScopeForLogicalInterconnect(_BaseEditScopeForLogicalInterconnect):
    pass


class _BaseReapplyConfiguration(object):

    """
    This class holds the Functions/operations common to both C7000 and T-bird related to reapply configuration of logical interconnect.
    """

    @classmethod
    def click_actions_reapply(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ Reapply configuration ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectsElements.ID_BUTTON_ACTIONS, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectsElements.ID_ACTION_REAPPLY_CONFIGURATION, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_reapply_logical_interconnect_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Reapply configuration ] dialog shown")
        return ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_DIALOG_REAPPLY_CONFIGURATION_LOGICAL_INTERCONNECT, timeout, fail_if_false)

    @classmethod
    def click_ok_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Yes, reapply ] button")
        ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectsElements.ID_BUTTON_REAPPLY_LOGICAL_INTERCONNECT_CONFIRM, timeout, fail_if_false)


class ReapplyConfiguration(_BaseReapplyConfiguration):
    pass


class C7000LogicalInterconnectsUpdateFirmware(object):

    @classmethod
    def select_update_action(cls, activation_type, timeout=5, fail_if_false=True):
        logger.debug("Choosing  Activation type %s " % activation_type)
        ui_lib.wait_for_element_and_click(C7000UpdateFirmwareElements.ID_SELECT_ETHERNET_ACTIVATION, timeout, fail_if_false)
        return ui_lib.wait_for_element_and_click(C7000UpdateFirmwareElements.ID_OPTION_ETHERNET_ACTIVATION % activation_type, timeout, fail_if_false)

    @classmethod
    def input_ethernet_delay(cls, activation_ethernet_delay, timeout=5, fail_if_false=True):
        logger.debug("Entering Ethernet  delay %s " % activation_ethernet_delay)
        return ui_lib.wait_for_element_and_input_text(C7000UpdateFirmwareElements.ID_INPUT_ETHERNET_ACTIVATION_DELAY, activation_ethernet_delay, timeout, fail_if_false)

    @classmethod
    def input_fibre_delay(cls, activation_fibre_delay, timeout=5, fail_if_false=True):
        logger.debug(" entering fc delay %s " % activation_fibre_delay)
        return ui_lib.wait_for_element_and_input_text(C7000UpdateFirmwareElements.ID_INPUT_FIBRE_CHANNEL_ACTIVATION_DELAY, activation_fibre_delay, timeout, fail_if_false)

    @classmethod
    def untick_activation_ethernet_icm(cls, icm_bay, enclosure_name, timeout=5, fail_if_false=True):
        logger.info(" Un selecting  Ethernet icm of bay  : " + str(icm_bay))
        return FusionUIBase.wait_for_checkbox_and_unselect(C7000UpdateFirmwareElements.ID_INPUT_ETHERNET_ACTIVATION_SELECT % ((enclosure_name), (icm_bay)), timeout, fail_if_false)

    @classmethod
    def untick_activation_fc_icm(cls, icm_bay, enclosure_name, timeout=5, fail_if_false=True):
        logger.debug("Un selecting Ethernet icm of bay  : " + str(icm_bay))
        return FusionUIBase.wait_for_checkbox_and_unselect(C7000UpdateFirmwareElements.ID_CHECKBOX_FIBRE_CHANNEL_ACTIVATION % ((enclosure_name), (icm_bay)), timeout, fail_if_false)

    @classmethod
    def select_fibre_channel_activation(cls, activation_type, timeout=5, fail_if_false=True):
        logger.debug(" Choosing Activation type for FC %s " % activation_type)
        ui_lib.wait_for_element_and_click(C7000UpdateFirmwareElements.ID_SELECT_FIBRE_CHANNEL_ACTIVATION, timeout=timeout, fail_if_false=fail_if_false)
        return ui_lib.wait_for_element_and_click(C7000UpdateFirmwareElements.ID_SELECT_FIBRE_ACTIVATION % activation_type, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_ok_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking update firmware 'OK' button")
        return ui_lib.wait_for_element_and_click(C7000UpdateFirmwareElements.ID_BUTTON_OK, timeout, fail_if_false)

    @classmethod
    def get_error_message_from_activation(cls, timeout=5, fail_if_false=True):
        logger.debug("returning error messages while Choosing activation delay for FC and ethernet")
        delay_eth_error_msg = ui_lib.get_text(C7000UpdateFirmwareElements.ID_TEXT_ERROR_FROM_ETHERNET_ACTIVATION, timeout, fail_if_false)
        delay_fc_error_msg = ui_lib.get_text(C7000UpdateFirmwareElements.ID_TEXT_ERROR_FROM_FC_ACTIVATION, timeout, fail_if_false)
        return {'delay_eth_error_msg': delay_eth_error_msg, 'delay_fc_error_msg': delay_fc_error_msg}

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def check_activation_dialog(cls, timeout=5, fail_if_false=True):
        logger.debug("Check Activation firmware page appeared")
        return ui_lib.wait_for_element_visible(C7000UpdateFirmwareElements.ID_DIALOG_UPDATE_FIRMWARE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_update_firmware_success(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify update firmware  is success")
        return ui_lib.wait_for_element_visible(C7000UpdateFirmwareElements.ID_TEXT_UPDATE_SUCCESS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_update_firmware_warning(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify update firmware completed with warning")
        return ui_lib.wait_for_element_visible(C7000UpdateFirmwareElements.ID_TEXT_UPDATE_WARNING, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_update_firmware_error(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify update firmware completed with error")
        return ui_lib.wait_for_element_visible(C7000UpdateFirmwareElements.ID_TEXT_UPDATE_ERROR, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_update_firmware_notvisible(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify update firmware notvisible")
        return ui_lib.wait_for_element_notvisible(C7000UpdateFirmwareElements.ID_DIALOG_UPDATE_FIRMWARE, timeout, fail_if_false)

    @classmethod
    def get_error_on_li_form(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify error on li update firmware page")
        return base_page.get_errors_on_form(C7000UpdateFirmwareElements.ID_DIALOG_UPDATE_FIRMWARE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_error_visible_on_li_form(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify error on li update firmware page")
        return ui_lib.wait_for_element_visible(C7000UpdateFirmwareElements.ID_TEXT_ACTIVITY_ERROR_DETAILS, timeout, fail_if_false)

    @classmethod
    def get_message_summary_on_li_form(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify summary on li update firmware page")
        return ui_lib.get_text(C7000UpdateFirmwareElements.ID_TEXT_ACTIVITY_MESSAGE_SUMMARY, timeout, fail_if_false)

    @classmethod
    def get_message_details_on_li_form(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify message details on li update firmware page")
        return ui_lib.get_text(C7000UpdateFirmwareElements.ID_TEXT_ACTIVITY_MESSAGE_DETAILS, timeout, fail_if_false)

    @classmethod
    def get_firmware_baseline_on_li_form(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify firmware baseline  on li update firmware page")
        return ui_lib.get_text(C7000UpdateFirmwareElements.ID_TEXT_INTERCONNECT_FW_BASELINE, timeout, fail_if_false)

    @classmethod
    def click_select_update_action_on_li(cls, select_update_action, timeout=5, fail_if_false=True):
        logger.debug(" Verify select update action  on li update firmware page")
        return ui_lib.wait_for_element_and_click(C7000UpdateFirmwareElements.ID_SELECT_UPDATE_ACTION % select_update_action, timeout, fail_if_false)

    @classmethod
    def get_firmware_baseline_on_li(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify firmware baseline  on li update firmware page")
        return ui_lib.get_text(C7000UpdateFirmwareElements.ID_TEXT_FWBASELINE_ON_ACTIVATE_FW, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def check_active_firmware_present_on_li(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify active firmware present on li firmware page")
        return ui_lib.wait_for_element(C7000UpdateFirmwareElements.ID_TEXT_ACTIVITY_MESSAGE)

    @classmethod
    def get_error_message_from_li_ethernet_icms(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify get ethernet  icms from li firmware page")
        return ui_lib.get_text(C7000UpdateFirmwareElements.ID_TEXT_ERRORS_ETHERNET_ACTIVATION, timeout, fail_if_false)

    @classmethod
    def get_error_message_from_li_fibre_icms(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify get fc  icms from li firmware page")
        return ui_lib.get_text(C7000UpdateFirmwareElements.ID_TEXT_ERRORS_FIBRE_ACTIVATION, timeout, fail_if_false)

    @classmethod
    def scroll_firmware_ok_button_into_view(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify scroll ok button in to view on Li firmware page")
        return ui_lib.scroll_into_view(C7000UpdateFirmwareElements.ID_BUTTON_OK)

    @classmethod
    def click_update_firmware_on_li(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify click updatefirmware on Li firmware page")
        return ui_lib.wait_for_element_and_click(C7000UpdateFirmwareElements.ID_BUTTON_UPDATE_FIRMWARE, timeout, fail_if_false)

    @classmethod
    def select_firmware_level_from_drowpdown(cls, select_update_firmware, timeout=5, fail_if_false=True):
        logger.debug("selecting  updatefirmware on Li firmware page")
        return ui_lib.wait_for_element_and_click(C7000UpdateFirmwareElements.ID_SELECT_FIRMWARE_DROPDOWN % select_update_firmware, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_activity_updatefirmware_visible_on_li(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify activity update firmware visible on li firmware page")
        return ui_lib.wait_for_element_visible(C7000UpdateFirmwareElements.ID_TEXT_PROGRESS_BAR_ACTVITY, timeout, fail_if_false)

    @classmethod
    def click_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify click cancel button on li firmware page")
        return ui_lib.wait_for_element_and_click(C7000UpdateFirmwareElements.ID_BUTTON_CANCEL, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_progressbar_on_updatefirmware(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify progress bar on Li firmware page")
        return ui_lib.wait_for_element_visible(C7000UpdateFirmwareElements.ID_TEXT_PROGRESS_BAR_FW_UPDATE, timeout, fail_if_false)

    @classmethod
    def click_force_installation_checkbox(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking force installation checkbox")
        ui_lib.wait_for_checkbox_and_select(C7000UpdateFirmwareElements.ID_CHECKBOX_FORCE_INSTALLATION, timeout, fail_if_false)


class TBirdLogicalInterconnectsUpdateFirmware(object):

    @classmethod
    def click_action_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Click action button")
        ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectsElements.ID_BUTTON_ACTIONS, timeout, fail_if_false)

    @classmethod
    def click_action_update_firmware(cls, timeout=5, fail_if_false=True):
        logger.debug("Click Update Firmware from the actions list")
        ui_lib.wait_for_element_and_click(TBirdUpdateFirmwareElements.ID_SELECT_ACTION_UPDATE_FIRMWARE, timeout, fail_if_false)

    @classmethod
    def wait_and_select_update_action(cls, update_action, timeout=5, fail_if_false=True):
        logger.debug("Selecting update action in update firmware dialog '%s'" % update_action)
        ui_lib.wait_for_element_and_click(TBirdUpdateFirmwareElements.ID_COMBO_UPDATE_ACTION, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(TBirdUpdateFirmwareElements.ID_SELECT_UPDATE_ACTION % update_action, timeout, fail_if_false)

    @classmethod
    def select_firmware_baseline(cls, firmware_baseline, timeout=5, fail_if_false=True):
        logger.debug("Selecting firmware baseline '%s'" % firmware_baseline)
        ui_lib.select_from_dropdown_by_text(TBirdUpdateFirmwareElements.ID_SELECT_FIRMWARE_BASELINE_DROPDOWN, firmware_baseline, timeout, fail_if_false)

    @classmethod
    def click_force_installation_checkbox(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking force installation checkbox")
        ui_lib.wait_for_checkbox_and_select(TBirdUpdateFirmwareElements.ID_CHECKBOX_FORCE_INSTALLATION, timeout, fail_if_false)

    @classmethod
    def choose_activation_type_parallel(cls, timeout=5, fail_if_false=True):
        logger.debug("Choosing activation type 'Parallel'")
        ui_lib.wait_for_element_and_click(TBirdUpdateFirmwareElements.ID_RADIO_PARALLEL_UPDATE, timeout, fail_if_false)

    @classmethod
    def choose_activation_type_orchestrated(cls, timeout=5, fail_if_false=True):
        logger.debug("Choosing activation type 'Orchestrated'")
        ui_lib.wait_for_element_and_click(TBirdUpdateFirmwareElements.ID_RADIO_ORCHESTRATED_UPDATE, timeout, fail_if_false)

    @classmethod
    def wait_and_check_module_not_available_warning_exists(self, timeout=5, fail_if_false=True):
        logger.debug("Verify warning message 'no_interconnect_module_available_for_action' is exists")
        return ui_lib.wait_for_element_visible(TBirdUpdateFirmwareElements.ID_TEXT_FWUPDATE_ERROR_MSG)

    @classmethod
    def get_module_not_available_warning(self, timeout=5, fail_if_false=True):
        logger.debug("Get warning text 'no_interconnect_module_available_for_action'")
        return ui_lib.get_text(TBirdUpdateFirmwareElements.ID_TEXT_FWUPDATE_ERROR_MSG)

    @classmethod
    def check_not_supported_for_orchestrated_warning(cls, timeout=5, fail_if_false=True):
        logger.debug("Check warning messages after pressing 'OK' button")
        if ui_lib.wait_for_element_visible(TBirdUpdateFirmwareElements.ID_FIRMWARE_WARNING, timeout, fail_if_false):
            header = ui_lib.get_text(TBirdUpdateFirmwareElements.ID_TEXT_FIRMWARE_WARNING, timeout, fail_if_false)
            detail = ui_lib.get_text(TBirdUpdateFirmwareElements.ID_TEXT_FIRMWARE_WARNING_DETAILS, timeout, fail_if_false)
            logger.debug("Warning Seen - \n {} \n {}".format(header, detail))

            return True
        else:
            return False

    @classmethod
    def click_update_firmware_ok_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Click update firmware 'OK' button")
        ui_lib.wait_for_element_and_click(TBirdUpdateFirmwareElements.ID_BUTTON_OK_FIRWARE_UPDATE, timeout, fail_if_false)

    @classmethod
    def click_update_firmware_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Click update firmware 'Cancel' button")
        ui_lib.wait_for_element_and_click(TBirdUpdateFirmwareElements.ID_BUTTON_CANCEL_FIRMWARE_UPDATE, timeout, fail_if_false)

    @classmethod
    def click_and_expand_update_firmware_status(cls, timeout=5, fail_if_false=True):
        logger.debug("Expand firmware status notification status tab")
        ui_lib.wait_for_element_and_click(TBirdUpdateFirmwareElements.ID_CLICK_MAINPANE, timeout, fail_if_false)

    @classmethod
    def get_update_firmware_progressbar_state_message(cls, timeout=5, fail_if_false=True):
        logger.debug("Getting firmware progress state")
        return ui_lib.get_text(TBirdUpdateFirmwareElements.ID_TEXT_UPDATE_FIRMWARE_PROGRESS_STEP, timeout, fail_if_false)

    @classmethod
    def wait_for_update_firmware_success(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify update firmware notification is success")
        return ui_lib.wait_for_element_visible(TBirdUpdateFirmwareElements.ID_TEXT_UPDATE_SUCCESS, timeout, fail_if_false)

    @classmethod
    def wait_for_update_firmware_warning(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify update firmware notification is warning")
        return ui_lib.wait_for_element_visible(TBirdUpdateFirmwareElements.ID_TEXT_UPDATE_WARNING, timeout, fail_if_false)

    @classmethod
    def wait_for_update_firmware_error(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify update firmware notification is error")
        return ui_lib.wait_for_element_visible(TBirdUpdateFirmwareElements.ID_TEXT_UPDATE_ERROR, timeout, fail_if_false)

    @classmethod
    def get_update_firmware_success_notification(cls, timeout=5, fail_if_false=True):
        logger.debug("Fetch text from update firmware success tab")
        return ui_lib.get_text(TBirdUpdateFirmwareElements.ID_ACTIVITY_SUCCESS_DETAILS, timeout, fail_if_false)

    @classmethod
    def get_update_firmware_warning_notification(cls, timeout=5, fail_if_false=True):
        logger.debug("Fetch text from update firmware warning tab")
        return ui_lib.get_text(TBirdUpdateFirmwareElements.ID_ACTIVITY_WARNING_DETAILS, timeout, fail_if_false)

    @classmethod
    def get_update_firmware_error_notification(cls, timeout=5, fail_if_false=True):
        logger.debug("Fetch text from update firmware warning tab")
        return ui_lib.get_text(TBirdUpdateFirmwareElements.ID_ACTIVITY_ERROR_DETAILS, timeout, fail_if_false)

    @classmethod
    def get_update_firmware_time_taken(cls, timeout=5, fail_if_false=True):
        logger.debug("Fetching update firmware time taken")
        return ui_lib.get_text(TBirdUpdateFirmwareElements.ID_TEXT_UPDATE_SUCCESS, timeout, fail_if_false)

    @classmethod
    def get_timeago_text_from_li_activity_tab(cls, column_string_should_contain, timeout=5, fail_if_false=True):
        logger.debug("Fetching time ago text from the row that contains text '%s'" % column_string_should_contain)
        ui_lib.get_s2l().mouse_over(TBirdUpdateFirmwareElements.ID_ACTIVITY_MESSAGE % column_string_should_contain)
        return (ui_lib.get_text(TBirdUpdateFirmwareElements.ID_ACTIVITY_TIMEAGO_TEXT % column_string_should_contain, timeout, fail_if_false)).split()

    @classmethod
    def get_interconnect_count_from_firmware_table(cls, timeout=5, fail_if_false=True):
        logger.debug("Getting interconnects list count from firmware table")
        return len(ui_lib.get_s2l()._element_find(TBirdUpdateFirmwareElements.ID_INTERCONNECT_LIST, False, True))

    @classmethod
    def get_firmware_details(cls, index, timeout=5, fail_if_false=True):
        logger.debug("Getting interconnects list details from firmware table by given index value")

        interconnect_name = ui_lib.get_text(TBirdUpdateFirmwareElements.ID_INTERCONNECT_NAME % index, timeout, fail_if_false)
        installed_fw = ui_lib.get_text(TBirdUpdateFirmwareElements.ID_INTERCONNECT_INSTALLED_FW % index, timeout, fail_if_false)
        baseline_fw = ui_lib.get_text(TBirdUpdateFirmwareElements.ID_INTERCONNECT_BASELINE_FW % index, timeout, fail_if_false)

        return (interconnect_name, installed_fw, baseline_fw)


class UpdateLogicalInterconnectFirmware(object):
    e = UpdateLogicalInterconnectFirmwareElements

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_sas_actions_update_firmware(cls, timeout=5, fail_if_false=True):
        logger.debug("select SAS LI [ Update firmware ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectsElements.ID_BUTTON_SAS_LI_ACTIONS, timeout,
                                          fail_if_false)
        return ui_lib.wait_for_element_and_click(cls.e.ID_SAS_ACTION_UPDATE_FIRMWARE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def select_update_option(cls, update_action, timeout=10):
        logger.debug("Update LI firmware, select update action: %s" % update_action)
        ui_lib.wait_for_element_and_click(cls.e.ID_UPDATE_ACTION, timeout)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_UPDATE_ACTION % update_action, timeout)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def select_firmware_baseline(cls, basename, timeout=10):
        logger.debug("Update LI firmware, select firmware baseline: %s" % basename)
        ui_lib.wait_for_element_and_click(cls.e.ID_FIRMWARE_BASELINE)
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_SELECT_FIRMWARE_BASELINE % basename, timeout)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def check_force_option(cls, force, timeout=5):
        logger.debug("Update LI firmware, check force option: %s" % force)
        if str(force).lower() == "yes":
            ui_lib.wait_for_checkbox_and_select(cls.e.ID_OPTION_FORCE, timeout)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def select_activation_mode(cls, activation_mode, timeout=5):
        logger.debug("Update LI firmware, select activation mode: %s" % activation_mode)
        if activation_mode.lower() == "parallel":
            ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_ACTIVATION_PARALLEL, timeout, True)
        elif activation_mode.lower() == "orchestrated":
            ui_lib.wait_for_element_and_click(cls.e.ID_OPTION_ACTIVATION_ORCHESTRATED, timeout, True)
        else:
            logger.debug("The activation mode [%s] is not valid, please check the input." % activation_mode)
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_ok_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Update LI firmware, click OK button.")
        return ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_OK, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Update LI firmware, click Cancel button.")
        return ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_sas_li_fw_affected_components_table(cls, timeout=10, fail_if_false=False):
        logger.debug("Update LI firmware, verifying affected components table.")
        if ui_lib.wait_for_element_visible(cls.e.ID_TABLE_NATASHA_LI_UPDATE_FIRMWARE_AFFECTED_COMPONENTS, timeout):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_update_firmware_notification(cls, timeout=20):
        logger.debug("Update LI firmware, verify update firmware started.")
        return ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_NOTIFICATION_NEW_STATE % 'Update firmware', timeout)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_tbird_updatefirmwarealerts_li(cls, message_list):
        """
        This function will navigate to the activity page and will validate the LI related alerts. Input is a list
        of messages that needs to be validated.
        """
        found = 0
        num_message = len(message_list)
        if not CommonOperationLogicalInterconnect.click_logical_interconnect_activity():
            logger.warn("failed to select activity..please check")
            return False

        for message in message_list:
            if ui_lib.wait_for_element(GeneralLogicalInterconnectsElements.ID_ACTIVITY_MESSAGE % message, 15):
                time = (GeneralLogicalInterconnectsElements.ID_ACTIVITY_MESSAGE % message) + "/td[4]/div[2]"
                timeago = (ui_lib.get_text(time, 10, hidden_element=True)).split()
                logger.info("Event found at -  %s" % timeago)

                if timeago:
                    if timeago[1].lower() == "hours" and int(timeago[0]) > 2:
                        logger.warn(
                            "Expected message %s found is not within last 2 hours!! Discarding Old activity Message" % message)
                        continue
                    elif timeago[1].lower() in ("months", "year", "years"):
                        logger.warn("Expected message '{}' found is of '{}'!!".format(message, timeago))
                        continue
                    found += 1
                    logger.debug("\nActivity : '%s'  found in IC activity page" % message)
                else:
                    logger.info("\nMessage %s is found but testscript failed to extract exact time" % message)
                    continue

            else:
                logger.warn("Expected message '%s' is not found in activity page:" % message)

        if found == num_message:
            logger.debug("All the excepted messages found in LI activity page")
            return True
        else:
            logger.debug("All the excepted messages are not found in LI activity page")
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def check_update_firmware_status(cls, logicalconnect):
        selenium2lib = ui_lib.get_s2l()
        error = 0
        error_string = ""
        logger.debug("in the new update started block")
        ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectsElements.ID_NOTIFICATION_TIMESTAMP)
        ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_NOTIFICATION_DETAILS_CONTAINER)
        logger.debug("Checking whether firmware is updated successfully or updated with warnings")

        # count 450 is introduced here as 45mins(2700 seconds) is the maximum timeout for the firmware update code. So one number will
        # be incremented once in every 6 seconds (2700/6 = 450)
        # 15 second a loop, total 15 * 100 seconds
        for icount in range(1, 100):
            logger.debug(icount)
            if ui_lib.wait_for_element_visible(cls.e.ID_NEW_UPDATE_SUCCESS):
                logger.debug(" In the success block")
                state = selenium2lib.get_text(cls.e.ID_NEW_UPDATE_SUCCESS)
                logger.debug(" Firmware update task state for the LI: " + logicalconnect.LIname + " is %s " % state)
                ui_lib.wait_for_element_and_click(cls.e.ID_NEW_SELECT_ALERT)
                ui_lib.wait_for_element_visible(cls.e.ID_ACTIVITY_NEW_SUCCESS_DETAILS)
                update_msg = selenium2lib.get_text(cls.e.ID_ACTIVITY_NEW_SUCCESS_DETAILS)
                logger.debug("update message in success block is: " + update_msg)
                if not update_msg or update_msg == "Firmware update validation success.":
                    if UpdateLogicalInterconnectFirmware.verify_update_firmware_notification():
                        logger.debug("in the new update started block")
                        ui_lib.wait_for_element_and_click(GeneralLogicalInterconnectsElements.ID_NOTIFICATION_TIMESTAMP)
                        ui_lib.wait_for_element_visible(GeneralLogicalInterconnectsElements.ID_NOTIFICATION_DETAILS_CONTAINER)
                        logger.debug("checking whether firmware is updated Successfully or updated with warnings")
                else:
                    if not TbirdVerifyLogicalInterconnects.verify_update_firmware_message(update_msg,
                                                                                          logicalconnect.LIname,
                                                                                          logicalconnect.updateaction):
                        error += 1
                    LImessage_list = ["Update firmware"]
                    alertspresent = UpdateLogicalInterconnectFirmware.verify_tbird_updatefirmwarealerts_li(LImessage_list)
                    if alertspresent:
                        logger.debug("The required alerts are found in LI activity page")
                    else:
                        logger.debug("The required alerts are not found in LI activity page, please check")
                    CommonOperationLogicalInterconnect.click_logical_interconnect_logical_interconnect()

                    TbirdVerifyLogicalInterconnects.verify_sas_interconnect_firmware_from_li()

                    if error > 0:
                        return False
                    return True

            elif ui_lib.wait_for_element_visible(cls.e.ID_NEW_UPDATE_WARNING, 5):
                logger.debug("In the warning block")
                ui_lib.wait_for_element_and_click(cls.e.ID_NEW_CLICK_WARNING)
                logger.debug("Found a warning in the Update firmware action you started,clicking it")
                ui_lib.wait_for_element_and_click(cls.e.ID_NEW_CLICK_WARNING)
                ui_lib.wait_for_element_and_click(cls.e.ID_NEW_SELECT_ALERT)
                ui_lib.wait_for_element_visible(cls.e.ID_NOTIFICATION_NEW_WARNING_SUMMARY)
                update_msg1 = selenium2lib.get_text(cls.e.ID_NOTIFICATION_NEW_WARNING_SUMMARY)
                logger.debug("Firmware Update action you started has some warnings..please check \n")
                logger.debug("\n" + update_msg1)
                error += 1
                return update_msg1

                # return True
            elif ui_lib.wait_for_element_visible(cls.e.ID_NEW_UPDATE_ERROR, 5):
                logger.debug("In the error block")
                logger.debug("Firmware Update is failed")
                ui_lib.wait_for_element_and_click(cls.e.ID_NEW_CLICK_ERROR)
                ui_lib.wait_for_element_and_click(cls.e.ID_NEW_CLICK_ERROR)
                logger.debug("Found a error in the Update firmware action you started,clicking it")
                ui_lib.wait_for_element_and_click(cls.e.ID_NEW_SELECT_ALERT)
                logger.debug("Printing the error message as shown in UI:\n ")
                ui_lib.wait_for_element_visible(cls.e.ID_ACTIVITY_NEW_ERROR_DETAILS)
                error_message = selenium2lib.get_text(cls.e.ID_ACTIVITY_NEW_ERROR_DETAILS)
                logger.warn(error_message)
                return False

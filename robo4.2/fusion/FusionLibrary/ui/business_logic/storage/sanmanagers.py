from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.storage.sanmanagers_elements import GeneralSANMangersElements
from FusionLibrary.ui.business_logic.storage.sanmanagers_elements import AddSANMangersElements
from FusionLibrary.ui.business_logic.storage.sanmanagers_elements import EditSANMangersElements
from FusionLibrary.ui.business_logic.storage.sanmanagers_elements import RemoveSANMangersElements
from FusionLibrary.ui.business_logic.storage.sanmanagers_elements import RefreshSANMangersElements
from FusionLibrary.ui.business_logic.base import FusionUIBase
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco
from RoboGalaxyLibrary.utilitylib import logging as logger
from datetime import datetime


class CommonOperationSANMangers(object):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_san_manager_not_exist(cls, san_manager, timeout=5, fail_if_false=True):
        logger.debug("verify san manager '%s' is not existing" % san_manager)
        if ui_lib.wait_for_element_notvisible(GeneralSANMangersElements.ID_TABLE_SAN_MANAGER % san_manager, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_san_manager_exist(cls, san_manager, timeout=7, fail_if_false=True):
        logger.debug("verify san manager '%s' is existing" % san_manager)
        if ui_lib.wait_for_element_visible(GeneralSANMangersElements.ID_TABLE_SAN_MANAGER % san_manager, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_san_manager_status_ok(cls, san_manager, timeout=5, fail_if_false=True):
        logger.debug("verify whether san manager %s is ok" % san_manager)
        if ui_lib.wait_for_element_visible(GeneralSANMangersElements.ID_STATUS_SAN_MANAGER_OK % san_manager, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_san_manager_status_warn(cls, san_manager, timeout=5, fail_if_false=True):
        logger.debug("verify whether san manager %s is warning" % san_manager)
        if ui_lib.wait_for_element_visible(GeneralSANMangersElements.ID_STATUS_SAN_MANAGER_WARN % san_manager, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_san_manager_status_error(cls, san_manager, timeout=5, fail_if_false=True):
        logger.debug("verify whether san manager %s is error" % san_manager)
        if ui_lib.wait_for_element_visible(GeneralSANMangersElements.ID_STATUS_SAN_MANAGER_ERROR % san_manager, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def get_san_manager_list(cls):
        logger.debug("get all san manager names from table")
        san_manager_list = []
        if ui_lib.wait_for_element(GeneralSANMangersElements.ID_TABLE_SAN_MANAGERS):
            san_manager_list = FusionUIBase.get_multi_elements_text(GeneralSANMangersElements.ID_TABLE_SAN_MANAGERS, fail_if_false=True)
        return san_manager_list

    @classmethod
    def click_san_manager(cls, san_manager, timeout=5):
        logger.debug("select san manager %s" % san_manager)
        ui_lib.wait_for_element_and_click(GeneralSANMangersElements.ID_TABLE_SAN_MANAGER % san_manager, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_san_manager_selected(cls, san_manager, timeout=5, fail_if_false=True):
        logger.debug("waiting for san manager '%s' is selected" % san_manager)
        if ui_lib.wait_for_element_visible(GeneralSANMangersElements.ID_TABLE_SAN_MANAGER_SELECTED % san_manager, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_san_manager_show_not_found(cls, san_manager, timeout=5, fail_if_false=True):
        logger.info("waiting for san_manager status indicates to 'not found'")
        if ui_lib.wait_for_element_visible(GeneralSANMangersElements.ID_TABLE_SAN_MANAGER_REMOVED % san_manager, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def click_action_button(cls, timeout=5):
        logger.debug("click action button")
        ui_lib.wait_for_element_and_click(GeneralSANMangersElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_san_manager_status_ok(cls, san_manager, timeout=10, fail_if_false=True):
        start = datetime.now()
        logger.debug("waiting for san manager '%s' status indicates to ok" % san_manager)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralSANMangersElements.ID_STATUS_SAN_MANAGER_OK % san_manager, timeout=2, fail_if_false=False):
                logger.debug("san manager '%s' status is ok as expected." % san_manager)
                return True
            elif ui_lib.wait_for_element_visible(GeneralSANMangersElements.ID_STATUS_SAN_MANAGER_WARN % san_manager, timeout=2, fail_if_false=False):
                err_msg = "san manager '%s' status is warning not as expected." % san_manager
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            elif ui_lib.wait_for_element_visible(GeneralSANMangersElements.ID_STATUS_SAN_MANAGER_ERROR % san_manager, timeout=2, fail_if_false=False):
                err_msg = "san manager '%s' status is error not as expected." % san_manager
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            else:
                logger.debug("san_manager status is unknown, waiting ...")
                continue
        err_msg = "Timeout to wait for san manager '%s' status indicates to ok." % san_manager
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)
        return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_san_manager_status_ok_or_warn(cls, san_manager, timeout=10, fail_if_false=True):
        start = datetime.now()
        logger.debug("waiting for san manager '%s' status indicates to ok or warning" % san_manager)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralSANMangersElements.ID_STATUS_SAN_MANAGER_OK % san_manager, timeout=5, fail_if_false=False):
                logger.debug("san manager '%s' status is ok as expected." % san_manager)
                return True
            elif ui_lib.wait_for_element_visible(GeneralSANMangersElements.ID_STATUS_SAN_MANAGER_WARN % san_manager, timeout=5, fail_if_false=False):
                logger.debug("san manager '%s' status is warning as expected." % san_manager)
                return True
            elif ui_lib.wait_for_element_visible(GeneralSANMangersElements.ID_STATUS_SAN_MANAGER_ERROR % san_manager, timeout=5, fail_if_false=False):
                err_msg = "san manager '%s' status is error not as expected." % san_manager
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            else:
                logger.debug("san manager '%s' status is unknown, waiting ..." % san_manager)
                continue
        err_msg = "Timeout to wait for san manager '%s' status indicates to ok or warn." % san_manager
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_san_manager_status_error(cls, san_manager, timeout=10, fail_if_false=True):
        start = datetime.now()
        logger.debug("waiting for san manager '%s' status indicates to error" % san_manager)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralSANMangersElements.ID_STATUS_SAN_MANAGER_OK % san_manager, timeout=5, fail_if_false=False):
                err_msg = "san manager '%s' status is ok not as expected." % san_manager
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            elif ui_lib.wait_for_element_visible(GeneralSANMangersElements.ID_STATUS_SAN_MANAGER_WARN % san_manager, timeout=5, fail_if_false=False):
                logger.debug("san manager '%s' status is warning not as expected." % san_manager)
                return False
            elif ui_lib.wait_for_element_visible(GeneralSANMangersElements.ID_STATUS_SAN_MANAGER_ERROR % san_manager, timeout=5, fail_if_false=False):
                logger.debug("san manager '%s' status is error as expected." % san_manager)
                return True
            else:
                logger.debug("san manager '%s' status is unknown, waiting ..." % san_manager)
                continue
        err_msg = "Timeout to wait for san_manager status indicates to error."
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_san_manager_type(cls, expect_value, timeout=5, fail_if_false=True):
        actual_value = FusionUIBase.get_text(GeneralSANMangersElements.ID_TEXT_GENERAL_SAN_MANAGER_TYPE, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("san manager type is '%s' as expected" % actual_value)
            return True
        else:
            msg = "san manager type is '%s' not as expected" % actual_value
            if fail_if_false is True:
                ui_lib.fail_test(msg)
            else:
                logger.warn(msg)
                return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_state(cls, expect_value, timeout=5, fail_if_false=True):
        actual_value = FusionUIBase.get_text(GeneralSANMangersElements.ID_TEXT_GENERAL_STATE, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("san manager state is '%s' as expected" % actual_value)
            return True
        else:
            msg = "san manager state is '%s' not as expected" % actual_value
            if fail_if_false is True:
                ui_lib.fail_test(msg)
            else:
                logger.warn(msg)
                return False


class AddSANMangers(object):

    @classmethod
    def click_add_san_manager_button(cls, timeout=5):
        logger.debug("click add san manager button ")
        ui_lib.wait_for_element_and_click(AddSANMangersElements.ID_BUTTON_ADD_SAN_MANAGER, timeout, fail_if_false=True)

    @classmethod
    def select_action_add(cls, timeout=5):
        logger.debug("select action add")
        ui_lib.wait_for_element_and_click(GeneralSANMangersElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(AddSANMangersElements.ID_SELECT_ACTION_ADD, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_san_manager_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.info('waiting for add san manager dialog to show up')
        if ui_lib.wait_for_element_visible(AddSANMangersElements.ID_DIALOG_ADD_SAN_MANAGER, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def select_san_manager_type(cls, san_manager_type, timeout=5, fail_if_false=True):
        logger.debug("select san manager type '%s'" % san_manager_type)
        FusionUIBase.choose_option_by_text(AddSANMangersElements.ID_SELECT_SAN_MANAGER_TYPE, san_manager_type,
                                           timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_ip_address_or_host_name(cls, host, appversion=0, timeout=5):
        logger.debug("input ip address or hostname '%s'" % host)
        if appversion >= "5.00":
            ui_lib.wait_for_element_and_input_text(AddSANMangersElements.ID_INPUT_IP_ADDRESS_OR_HOST_NAME2, host, timeout, fail_if_false=True)
        else:
            ui_lib.wait_for_element_and_input_text(AddSANMangersElements.ID_INPUT_IP_ADDRESS_OR_HOST_NAME, host, timeout, fail_if_false=True)

    @classmethod
    def input_ip_address_or_host_name_cisco(cls, host, timeout=5):
        logger.debug("input ip address or hostname '%s'" % host)
        ui_lib.wait_for_element_and_input_text(AddSANMangersElements.ID_INPUT_IP_ADDRESS_OR_HOST_NAME_CISCO, host, timeout, fail_if_false=True)

    @classmethod
    def input_ip_address_or_host_name_hpe(cls, host, timeout=5):
        logger.debug("input ip address or hostname '%s'" % host)
        ui_lib.wait_for_element_and_input_text(AddSANMangersElements.ID_INPUT_IP_ADDRESS_OR_HOST_NAME_HPE, host, timeout, fail_if_false=True)

    @classmethod
    def input_port(cls, port, timeout=5):
        logger.debug("input port '%s'" % port)
        ui_lib.wait_for_element_and_input_text(AddSANMangersElements.ID_INPUT_PORT, port, timeout, fail_if_false=True)

    @classmethod
    def tick_use_ssl(cls, appversion=0, timeout=5):
        if appversion >= "5.00":
            logger.debug("check use secure connection (HTTPS) ")
            FusionUIBase.wait_for_checkbox_and_select(AddSANMangersElements.ID_CHECKBOX_USE_SSL2, timeout, fail_if_false=True)
        else:
            logger.debug("check use SSL ")
            FusionUIBase.wait_for_checkbox_and_select(AddSANMangersElements.ID_CHECKBOX_USE_SSL, timeout, fail_if_false=True)

    @classmethod
    def untick_use_ssl(cls, appversion=0, timeout=5):
        if appversion >= "5.00":
            logger.debug("check use secure connection (HTTPS) ")
            FusionUIBase.wait_for_checkbox_and_unselect(AddSANMangersElements.ID_CHECKBOX_USE_SSL2, timeout, fail_if_false=True)
        else:
            logger.debug("check use SSL ")
            FusionUIBase.wait_for_checkbox_and_unselect(AddSANMangersElements.ID_CHECKBOX_USE_SSL, timeout, fail_if_false=True)

    @classmethod
    def input_user_name(cls, username, appversion=0, timeout=5):
        logger.debug("input user name '%s'" % username)
        if appversion >= "5.00":
            ui_lib.wait_for_element_and_input_text(AddSANMangersElements.ID_INPUT_USER_NAME2, username, timeout, fail_if_false=True)
        else:
            ui_lib.wait_for_element_and_input_text(AddSANMangersElements.ID_INPUT_USER_NAME, username, timeout, fail_if_false=True)

    @classmethod
    def input_password(cls, password, appversion=0, timeout=5):
        logger.debug("input password '%s'" % password)
        if appversion >= "5.00":
            ui_lib.wait_for_element_and_input_text(AddSANMangersElements.ID_INPUT_PASSWORD2, password, timeout, fail_if_false=True)
        else:
            ui_lib.wait_for_element_and_input_text(AddSANMangersElements.ID_INPUT_PASSWORD, password, timeout, fail_if_false=True)

    @classmethod
    def input_snmp_user_name(cls, username, timeout=5):
        logger.debug("input user name '%s'" % username)
        ui_lib.wait_for_element_and_input_text(AddSANMangersElements.ID_INPUT_SNMP_USER_NAME, username, timeout, fail_if_false=True)

    @classmethod
    def input_snmp_port(cls, port, timeout=5):
        logger.debug("input SNMP port '%s'" % port)
        ui_lib.wait_for_element_and_input_text(AddSANMangersElements.ID_INPUT_SNMP_PORT, port, timeout, fail_if_false=True)

    @classmethod
    def choose_security_level(cls, level, sm_type, timeout=5):
        logger.debug("check security level '%s'" % level)
        if sm_type.lower() == 'cisco':
            expect_options = ["Authentication", "Authentication and privacy"]
        elif sm_type.lower() == 'hpe':
            expect_options = ["Authentication", "Authentication and privacy", "None"]
        else:
            expect_options = ["Authentication", "Authentication and privacy", "None"]
            ui_lib.fail_test("There should be no fields that names 'security level' on the page if san manager type is '%s'" % sm_type)
        FusionUIBase.para_should_be_in_list(expect_options, level)
        if level.lower().replace(" ", "") == "Authentication".lower().replace(" ", ""):
            ui_lib.wait_for_element_and_click(AddSANMangersElements.ID_RADIO_SECURITY_LEVEL_AUTHENTICATION, timeout, fail_if_false=True)
        elif level.lower().replace(" ", "") == "Authentication and privacy".lower().replace(" ", ""):
            ui_lib.wait_for_element_and_click(AddSANMangersElements.ID_RADIO_SECURITY_LEVEL_AUTHENTICATION_AND_PRIVACY, timeout, fail_if_false=True)
        else:
            ui_lib.wait_for_element_and_click(AddSANMangersElements.ID_RADIO_SECURITY_LEVEL_NONE, timeout, fail_if_false=True)

    @classmethod
    def select_authentication_protocol(cls, protocol, timeout=5):
        logger.debug("select authentication protocol '%s'" % protocol)
        ui_lib.wait_for_element_and_click(AddSANMangersElements.ID_DROPDOWN_AUTHENTICATION_PROTOCOL, timeout, fail_if_false=True)
        if protocol.lower().replace(' ', '') == "SHA".lower().replace(' ', ''):
            ui_lib.wait_for_element_and_click(AddSANMangersElements.ID_SELECT_AUTHENTICATION_PROTOCOL_SHA, timeout, fail_if_false=True)
        elif protocol.lower().replace(' ', '') == "MD5".lower().replace(' ', ''):
            ui_lib.wait_for_element_and_click(AddSANMangersElements.ID_SELECT_AUTHENTICATION_PROTOCOL_MD5, timeout, fail_if_false=True)
        else:
            ui_lib.fail_test("unsupported authentication protocol '%s', please specify 'SHA' or 'MD5'" % protocol)

    @classmethod
    def input_authentication_password(cls, password, timeout=5):
        logger.debug("input authentication password '%s'" % password)
        ui_lib.wait_for_element_and_input_text(AddSANMangersElements.ID_INPUT_AUTHENTICATION_PASSWORD, password, timeout, fail_if_false=True)

    @classmethod
    def select_privacy_protocol(cls, protocol, timeout=5):
        logger.debug("select privacy protocol '%s'" % protocol)
        ui_lib.wait_for_element_and_click(AddSANMangersElements.ID_DROPDOWN_PRIVACY_PROTOCOL, timeout, fail_if_false=True)
        if protocol.lower().replace(' ', '') == "DES-56".lower().replace(' ', ''):
            ui_lib.wait_for_element_and_click(AddSANMangersElements.ID_SELECT_PRIVACY_PROTOCOL_DES56, timeout, fail_if_false=True)
        elif protocol.lower().replace(' ', '') == "AES-128".lower().replace(' ', ''):
            ui_lib.wait_for_element_and_click(AddSANMangersElements.ID_SELECT_PRIVACY_PROTOCOL_AES128, timeout, fail_if_false=True)
        else:
            ui_lib.fail_test("unsupported authentication protocol '%s', please specify 'DES-56' or 'AES-128'" % protocol)

    @classmethod
    def input_privacy_password(cls, password, timeout=5):
        logger.debug("input privacy password '%s'" % password)
        ui_lib.wait_for_element_and_input_text(AddSANMangersElements.ID_INPUT_PRIVACY_PASSWORD, password, timeout, fail_if_false=True)

    @classmethod
    def click_add_button(cls, timeout=5):
        logger.debug("click add")
        ui_lib.wait_for_element_and_click(AddSANMangersElements.ID_BUTTON_ADD, timeout, fail_if_false=True)

    @classmethod
    def click_add_plus_button(cls, timeout=5):
        logger.debug("click add+")
        ui_lib.wait_for_element_and_click(AddSANMangersElements.ID_BUTTON_ADD_PLUS, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click cancel")
        ui_lib.wait_for_element_and_click(AddSANMangersElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_san_manager_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for add san manager dialog to disappear")
        return ui_lib.wait_for_element_notvisible(AddSANMangersElements.ID_DIALOG_ADD_SAN_MANAGER, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_added_message_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for added san manager message to show up")
        if ui_lib.wait_for_element_visible(AddSANMangersElements.ID_TEXT_ADDED_SAN_MANAGER, timeout, fail_if_false):
            return True
        else:
            return False


class EditSANMangers(object):

    @classmethod
    def select_action_edit(cls, timeout=5):
        logger.debug("select edit san manager action")
        ui_lib.wait_for_element_and_click(GeneralSANMangersElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditSANMangersElements.ID_SELECT_ACTION_EDIT, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_san_manager_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for edit san manager dialog to show up")
        ui_lib.wait_for_element_visible(EditSANMangersElements.ID_DIALOG_EDIT_SAN_MANAGER, timeout, fail_if_false)

    @classmethod
    def input_ip_address_or_host_name(cls, host, timeout=5):
        logger.debug("input ip address or hostname '%s'" % host)
        ui_lib.wait_for_element_and_input_text(EditSANMangersElements.ID_INPUT_IP_ADDRESS_OR_HOST_NAME, host, timeout, fail_if_false=True)

    @classmethod
    def input_port(cls, port, timeout=5):
        logger.debug("input port '%s'" % port)
        ui_lib.wait_for_element_and_input_text(EditSANMangersElements.ID_INPUT_PORT, port, timeout, fail_if_false=True)

    @classmethod
    def tick_use_ssl(cls, timeout=5):
        logger.debug("check use SSL ")
        FusionUIBase.wait_for_checkbox_and_select(EditSANMangersElements.ID_CHECKBOX_USE_SSL, timeout, fail_if_false=True)

    @classmethod
    def untick_use_ssl(cls, timeout=5):
        logger.debug("uncheck use SSL ")
        FusionUIBase.wait_for_checkbox_and_unselect(EditSANMangersElements.ID_CHECKBOX_USE_SSL, timeout, fail_if_false=True)

    @classmethod
    def input_user_name(cls, username, timeout=5):
        logger.debug("input user name '%s'" % username)
        ui_lib.wait_for_element_and_input_text(EditSANMangersElements.ID_INPUT_USER_NAME, username, timeout, fail_if_false=True)

    @classmethod
    def input_password(cls, password, timeout=5):
        logger.debug("input password '%s'" % password)
        ui_lib.wait_for_element_and_input_text(EditSANMangersElements.ID_INPUT_PASSWORD, password, timeout, fail_if_false=True)

    @classmethod
    def click_ok_button(cls, timeout=5):
        logger.debug("click ok")
        ui_lib.wait_for_element_and_click(EditSANMangersElements.ID_BUTTON_OK, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click cancel")
        ui_lib.wait_for_element_and_click(EditSANMangersElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_san_manager_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for edit san manager dialog to disappear")
        return ui_lib.wait_for_element_notvisible(EditSANMangersElements.ID_DIALOG_EDIT_SAN_MANAGER, timeout, fail_if_false)


class RemoveSANMangers(object):

    @classmethod
    def select_action_remove(cls, timeout=5):
        logger.debug("select remove san manager action")
        ui_lib.wait_for_element_and_click(GeneralSANMangersElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(RemoveSANMangersElements.ID_SELECT_ACTION_REMOVE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_san_manager_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for remove san manager dialog to show up")
        ui_lib.wait_for_element_visible(RemoveSANMangersElements.ID_DIALOG_REMOVE, timeout, fail_if_false)

    @classmethod
    def click_yes_remove(cls, timeout=5):
        logger.debug("click 'Yes, remove'")
        ui_lib.wait_for_element_and_click(RemoveSANMangersElements.ID_BUTTON_YES_REMOVE, timeout, fail_if_false=True)

    @classmethod
    def click_cancel(cls, timeout=5):
        logger.debug("click 'cancel'")
        ui_lib.wait_for_element_and_click(RemoveSANMangersElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_san_manager_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for remove san manager dialog to disappear")
        return ui_lib.wait_for_element_notvisible(RemoveSANMangersElements.ID_DIALOG_REMOVE, timeout, fail_if_false)


class RefreshSANMangers(object):

    @classmethod
    def select_action_refresh(cls, timeout=5):
        logger.debug("select refresh san manager action")
        ui_lib.wait_for_element_and_click(GeneralSANMangersElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(RefreshSANMangersElements.ID_SELECT_ACTION_REFRESH, timeout, fail_if_false=True)

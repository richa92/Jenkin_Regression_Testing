"""
    SANs Page
"""
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco, FusionUIBase
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.storage.sans_elements import GeneralSANsElements, EditSANsElements
from RoboGalaxyLibrary.utilitylib import logging as logger


class CommonOperationSANs(object):

    @classmethod
    def select_sans(cls, sans, timeout=5, fail_if_false=True):
        logger.debug("select san manager [%s]" % sans)
        ui_lib.wait_for_element_and_click(GeneralSANsElements.ID_SANS % sans, timeout, fail_if_false)

    @classmethod
    def wait_for_sans_shown(cls, sans, timeout=10, fail_if_false=True):
        logger.debug("wait for SANs [%s]" % sans)
        ui_lib.wait_for_element_visible(GeneralSANsElements.ID_SANS % sans, timeout, fail_if_false)

    @classmethod
    def wait_for_sans_title_shown(cls, sans, timeout=10, fail_if_false=True):
        logger.debug("wait for TOP SANs title shown  [%s]" % sans)
        ui_lib.wait_for_element_visible(GeneralSANsElements.ID_SANS % sans, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_sans_title(cls, sans, timeout=10, fail_if_false=True):
        logger.info('verifying [ SANS title= %s ] is visible' % sans)
        ui_lib.wait_for_element_text_match(GeneralSANsElements.ID_SANS_TITLE, sans, timeout=5)


class EditSANs(object):

    @classmethod
    def select_action_edit(cls, timeout=5, fail_if_false=True):
        logger.debug("select action edit")
        ui_lib.wait_for_element_and_click(GeneralSANsElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(EditSANsElements.ID_SELECT_ACTION_EDIT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_sans_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait for SANs Edit dialog show")
        ui_lib.wait_for_element_visible(EditSANsElements.ID_DIALOG_EDIT_SANS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_sans_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait for SANs Edit dialog disappear")
        return ui_lib.wait_for_element_notvisible(EditSANsElements.ID_DIALOG_EDIT_SANS, timeout, fail_if_false)

    @classmethod
    def choose_automate_zoning(cls, automate_zoning, timeout=10):
        FusionUIBase.toggle_button(EditSANsElements.ID_TOGGLE_AUTOMATE_ZONING, automate_zoning, timeout)

    @classmethod
    def click_sans_edit_ok(cls, timeout=5, fail_if_false=True):
        logger.debug("click sans edit ok")
        ui_lib.wait_for_element_and_click(EditSANsElements.ID_BUTTON_OK, timeout, fail_if_false)

    @classmethod
    def add_zone_name_format_token(cls, token, timeout=5, fail_if_false=True):
        logger.debug("Add zone name format token [%s]" % token)
        ui_lib.wait_for_element_and_click(EditSANsElements.ID_ZONE_NAME_FORMAT, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(EditSANsElements.ID_ZONE_NAME_FORMAT_TOKEN % token, timeout, fail_if_false)

    @classmethod
    def choose_sans_zoning_policy(cls, zoning_policy, timeout=5, fail_if_false=True):
        ui_lib.wait_for_element_and_click(EditSANsElements.ID_SELECT_ZONING_POLICY, timeout, fail_if_false)
        if zoning_policy is "SIAT":
            logger.debug("choose sans zoning policy [Single initiator / all targets]")
            ui_lib.wait_for_element_and_click(EditSANsElements.ID_SELECT_ZONING_POLICY_SIAT)
        elif zoning_policy is "SISSS":
            logger.debug("choose sans zoning policy [Single initiator / single storage system]")
            ui_lib.wait_for_element_and_click(EditSANsElements.ID_SELECT_ZONING_POLICY_SISSS)
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_zone_name_format(cls, timeout=5, fail_if_false=True):
        logger.debug("click Zone name Format")
        ui_lib.wait_for_element_and_click(EditSANsElements.ID_ZONE_NAME_FORMAT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def input_text_into_zone_name_format(cls, text):
        logger.debug("input text into Zone Name Format")
        # ui_lib.wait_for_element_and_input_text(EditSANsElements.ID_INPUT_ZONE_NAME_FORMAT, text, timeout, fail_if_false)
        ui_lib.send_keys(EditSANsElements.ID_INPUT_ZONE_NAME_FORMAT, text)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_edit_sans_error_message(cls, error_message, timeout=5, fail_if_false=True):
        logger.debug("Get Error Message From Edit SANs Dialog")
        msg = FusionUIBase.get_text(EditSANsElements.ID_ERROR_MESSAGE_EDIT_SANS, timeout, fail_if_false)
        logger.debug(msg)
        if error_message in msg:
            logger.debug("Verify Error Msg [%s] successfully" % error_message)
            return True

        else:
            logger.debug("Failed to verify Error Msg [%s]" % error_message)
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def check_sans_zone_name_format_token_with_zoning_policy_siat(cls, timeout=5, fail_if_false=True):
        logger.debug("Check sans zone name format with Zoning policy [single initiator / all targets] ")
        logger.debug("Check token [server profile]")
        ui_lib.wait_for_element_visible(EditSANsElements.ID_ZONE_NAME_FORMAT_SERVER_PROFILE, timeout, fail_if_false)
        logger.debug("Check token [server profile connection]")
        ui_lib.wait_for_element_visible(EditSANsElements.ID_ZONE_NAME_FORMAT_SERVER_PROFILE_CONNECTION, timeout, fail_if_false)
        logger.debug("Check token [server initiator WWPN]")
        ui_lib.wait_for_element_visible(EditSANsElements.ID_ZONE_NAME_FORMAT_SERVER_INITIATOR_WWPN, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def check_sans_zone_name_format_token_with_zoning_policy_sisss(cls, timeout=5, fail_if_false=True):
        logger.debug("Check sans zone name format with Zoning policy [single initiator / single storage system] ")
        logger.debug("Check token [server profile]")
        ui_lib.wait_for_element_visible(EditSANsElements.ID_ZONE_NAME_FORMAT_SERVER_PROFILE, timeout, fail_if_false)
        logger.debug("Check token [server profile connection]")
        ui_lib.wait_for_element_visible(EditSANsElements.ID_ZONE_NAME_FORMAT_SERVER_PROFILE_CONNECTION, timeout, fail_if_false)
        logger.debug("Check token [server initiator WWPN]")
        ui_lib.wait_for_element_visible(EditSANsElements.ID_ZONE_NAME_FORMAT_SERVER_INITIATOR_WWPN, timeout, fail_if_false)
        logger.debug("Check token [storage system]")
        ui_lib.wait_for_element_visible(EditSANsElements.ID_ZONE_NAME_FORMAT_STORAGE_SYSTEM, timeout, fail_if_false)
        logger.debug("Check token [storage system port group]")
        ui_lib.wait_for_element_visible(EditSANsElements.ID_ZONE_NAME_FORMAT_STORAGE_PORT_GROUP, timeout, fail_if_false)


class VerifySANs(object):

    @classmethod
    def verify_general_state(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify State ,except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("State", GeneralSANsElements.ID_TEXT_STATE, except_value, timeout,
                                                fail_if_false)

    @classmethod
    def verify_general_type(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify Type ,except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("Type", GeneralSANsElements.ID_TEXT_TYPE, except_value, timeout,
                                                fail_if_false)

    @classmethod
    def verify_principal_switch(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify Principal switch ,except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("Principal switch", GeneralSANsElements.ID_TEXT_PRINCIPAL_SWITCH,
                                                except_value, timeout, fail_if_false)

    @classmethod
    def verify_san_manager(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify SAN manager ,except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("SAN manager", GeneralSANsElements.ID_TEXT_SAN_MANAGER, except_value,
                                                timeout, fail_if_false)

    @classmethod
    def verify_associated_networks(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify Associated networks ,except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("Associated networks", GeneralSANsElements.ID_TEXT_ASSOCIATED_NETWORKS,
                                                except_value, timeout, fail_if_false)

    @classmethod
    def verify_zoned(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify Zoned ,except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("Zoned", GeneralSANsElements.ID_TEXT_ZONED, except_value, timeout,
                                                fail_if_false)

    @classmethod
    def verify_automate_zoning(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify Automate zoning ,except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("Automate zoning", GeneralSANsElements.ID_TEXT_AUTOMATE_ZONING,
                                                except_value, timeout, fail_if_false)

    @classmethod
    def verify_zoning_policy(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify Zoning policy ,except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("Zoning policy", GeneralSANsElements.ID_TEXT_ZONING_POLICY,
                                                except_value, timeout, fail_if_false)

    @classmethod
    def verify_use_aliases(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify Use aliases ,except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("Use aliases", GeneralSANsElements.ID_TEXT_USE_ALIASES, except_value,
                                                timeout, fail_if_false)

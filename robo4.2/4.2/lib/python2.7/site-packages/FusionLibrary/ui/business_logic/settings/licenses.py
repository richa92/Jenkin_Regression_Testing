from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco, FusionUIBase, FusionUIConst
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.settings.licenses_elements import GeneralLicensesElements, AddLicensesElements


class GeneralLicense(object):

    @classmethod
    def click_license_title(cls, timeout=5):
        logger.debug("Click [ license title ]")
        ui_lib.wait_for_element_and_click(GeneralLicensesElements.ID_LINK_LICENSES, timeout, fail_if_false=True)

    @classmethod
    def is_licenses_page(cls, timeout=5):
        logger.debug("Determine if current page is Licenses")
        return ui_lib.wait_for_element_visible(GeneralLicensesElements.ID_PAGE_LICENSES, timeout, fail_if_false=False)


class AddLicense(object):

    @classmethod
    def select_actions_add(cls, timeout=5):
        logger.debug("select [ Add ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralLicensesElements.ID_BUTTON_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(GeneralLicensesElements.ID_OPTION_ACTIONS_ADD, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_license_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add License ] dialog shown")
        return ui_lib.wait_for_element_visible(AddLicensesElements.ID_DIALOG_ADD_LICENSE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_license_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add License ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(AddLicensesElements.ID_DIALOG_ADD_LICENSE, timeout, fail_if_false)

    @classmethod
    def input_license_key(cls, license_key, timeout=5):
        logger.debug("input [ %s ... ] into license key text box" % license_key[0:10])
        ui_lib.wait_for_element_visible(AddLicensesElements.ID_INPUT_LICENSE_KEY, timeout, fail_if_false=True)
        element = ui_lib.get_s2l()._element_find(AddLicensesElements.ID_INPUT_LICENSE_KEY, first_only=True, required=True)
        ui_lib.get_s2l()._current_browser().execute_script("$(arguments[0]).val('%s');return true;" % license_key, element)

    @classmethod
    def click_add_button(cls, timeout=5):
        logger.debug("click [ Add ] button")
        ui_lib.wait_for_element_and_click(AddLicensesElements.ID_BUTTON_ADD, timeout, fail_if_false=True)

    @classmethod
    def click_add_plus_button(cls, timeout=5):
        logger.debug("click [ Add Plus ] button")
        ui_lib.wait_for_element_and_click(AddLicensesElements.ID_BUTTON_ADD_PLUS, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(AddLicensesElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)


class VerifyLicense(object):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_oneview_wo_ilo_license_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify oneview w/o iLo license exist")
        return ui_lib.wait_for_element_visible(GeneralLicensesElements.ID_TEXT_ONEVIEW_WO_ILO_LICENSE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_oneview_license_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify oneview license exist")
        return ui_lib.wait_for_element_visible(GeneralLicensesElements.ID_TEXT_ONEVIEW_LICENSE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_required_server_oneview_wo_ilo_license_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify required server oneview w/o iLo license text exist")
        return ui_lib.wait_for_element_visible(GeneralLicensesElements.ID_TEXT_ONEVIEW_WO_ILO_LICENSE_REQUIRED, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_required_server_oneview_license_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify required server oneview license text exist")
        return ui_lib.wait_for_element_visible(GeneralLicensesElements.ID_TEXT_ONEVIEW_LICENSE_REQUIRED, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_required_server_oneview_wo_ilo_license(cls, number, timeout=5, fail_if_false=True):
        logger.debug("Verify [ server number '%s' ] of required oneview w/o iLo license" % number)
        if number == 1:
            msg = "%s servers needs license"
        else:
            msg = "%s server needs license"
        return FusionUIBase.verify_element_text("Required server licenses number", GeneralLicensesElements.ID_TEXT_ONEVIEW_WO_ILO_LICENSE_REQUIRED, msg % number, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_licensed_server_oneview_wo_ilo_license(cls, number, timeout=5, fail_if_false=True):
        logger.debug("Verify [ server number '%s' ] of licensed oneview w/o iLo license" % number)
        if number == 1:
            msg = "%s servers licensed"
        else:
            msg = "%s server licensed"
        return FusionUIBase.verify_element_text("Licensed server licenses number", GeneralLicensesElements.ID_TEXT_ONEVIEW_WO_ILO_LICENSE_LICENSED, msg % number, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_required_server_oneview_license(cls, number, timeout=5, fail_if_false=True):
        logger.debug("Verify [ server number '%s' ] of required oneview iLo license" % number)
        if number == 1:
            msg = "%s servers needs license"
        else:
            msg = "%s server needs license"
        return FusionUIBase.verify_element_text("Required server licenses number", GeneralLicensesElements.ID_TEXT_ONEVIEW_LICENSE_REQUIRED, msg % number, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_licensed_server_oneview_license(cls, number, timeout=5, fail_if_false=True):
        logger.debug("Verify [ server number '%s' ] of licensed oneview iLo license" % number)
        if number == 1:
            msg = "%s servers licensed"
        else:
            msg = "%s server licensed"
        return FusionUIBase.verify_element_text("Licensed server licenses number", GeneralLicensesElements.ID_TEXT_ONEVIEW_LICENSE_LICENSED, msg % number, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_oneview_fcupgrade_license_exists(cls, timeout=10, fail_if_false=True):
        logger.debug("Verify oneview fcUpgrade license exist")
        return ui_lib.wait_for_element_visible(GeneralLicensesElements.ID_TEXT_ONEVIEW_FCLICENSE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_required_oneview_fcupgrade_license(cls, expected_text, timeout=5, fail_if_false=True):
        logger.debug("verify '%s' license should display '<%s>'" % (FusionUIConst.CONST_LICENSE_ONEVIEW_SYNERGY_FCUPGRADE, expected_text))
        return FusionUIBase.verify_element_text("Synergy 8Gb FC Upgrade", GeneralLicensesElements.ID_TEXT_ONEVIEW_FCLICENSE_REQUIRED, expected_text, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_licensed_interconnect_oneview(cls, expected_text, timeout=5, fail_if_false=True):
        logger.debug("verify '%s' license should display '<%s>'" % (FusionUIConst.CONST_LICENSE_ONEVIEW_SYNERGY_FCUPGRADE, expected_text))
        return FusionUIBase.verify_element_text("Synergy 8Gb FC Upgrade", GeneralLicensesElements.ID_TEXT_ONEVIEW_FCLICENSE_LICENSED, expected_text, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_available_fcupgrade_license(cls, expected_text, timeout=5, fail_if_false=True):
        logger.debug("verify '%s' license should display '<%s>'" % (FusionUIConst.CONST_LICENSE_ONEVIEW_SYNERGY_FCUPGRADE, expected_text))
        return FusionUIBase.verify_element_text("Synergy 8Gb FC Upgrade", GeneralLicensesElements.ID_TEXT_ONEVIEW_FCLICENSE_AVAILABLE, expected_text, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_fc_license_not_exist(cls, timeout=5, fail_if_false=False):
        logger.debug("Verify there is no FCUpgrade license now")
        return ui_lib.wait_for_element_notvisible(GeneralLicensesElements.ID_TEXT_ONEVIEW_FCLICENSE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_add_button_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify there Add button exist")
        return ui_lib.wait_for_element(GeneralLicensesElements.ID_BUTTON_ADD, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_error_message_when_add_invalid_or_duplicated_license(cls, negative_type, timeout=5, fail_if_false=True):
        logger.debug("Verify the error message is correct as input : {}".format(negative_type))
        errtxt_locater = AddLicensesElements.ID_TEXT_ADD_DUPLICATED_ERROR if "DUPLICATE" in negative_type.upper() else AddLicensesElements.ID_TEXT_ADD_INVALID_ERROR
        return ui_lib.get_text(errtxt_locater, timeout, fail_if_false)

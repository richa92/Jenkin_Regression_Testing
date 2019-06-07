"""
    Firmware Bundle Page
"""

from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco, FusionUIBase
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.general.firmwarebundles_elements import FusionFirmwareBundlePage, RemoveFirmwareBundleElements, AddFirmwareBundleElements
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.base import FusionUIBase


class CommonOperationFirmwareBundle(object):
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_firmware_bundle_button_show(cls, timeout=30, fail_if_false=False):
        logger.debug("wait add firmware bundle button show")
        return ui_lib.wait_for_element_visible(FusionFirmwareBundlePage.ID_LINKE_ADD_FW_BUNDLE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def refresh_browser_on_firmware_page(cls, timeout=30, fail_if_false=False):
        logger.debug("refresh browser and wait add firmware bundle button show")
        if not ui_lib.refresh_browser(FusionFirmwareBundlePage.ID_LINKE_ADD_FW_BUNDLE, time=timeout):
            return FusionUIBase.fail_test_or_return_false(message="Browser refresh failed.", fail_if_false=fail_if_false)
        else:
            return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_firmware_bundle(cls, spp_name, firmware_version, timeout=5, fail_if_false=True):
        firmware_bundle_name = spp_name + ', ' + firmware_version
        logger.debug("Select firmware_bundle [%s]" % firmware_bundle_name)
        if not ui_lib.wait_for_element_and_click(FusionFirmwareBundlePage.ID_TABLE_FIRMWARE_BUNDLE % (spp_name, firmware_version), timeout=timeout, fail_if_false=fail_if_false):
            logger.warn("Failed to select firmware bundle")
            return False
        str_title = ui_lib.get_text(FusionFirmwareBundlePage.ID_FWDRIVER_TITLE, timeout=timeout, fail_if_false=fail_if_false)
        if firmware_bundle_name.strip() == str_title.strip():
            logger.info("Selected the Firmware Bundle %s  with version %s successfully" % (spp_name, firmware_version))
            return True
        else:
            msg = "Fail in selecting Firmware Bundle %s  with version %s" % (spp_name, firmware_version)
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def click_activity_collapser(cls, activity_name, timeout=10, fail_if_false=True):
        logger.debug("click to expand activity '%s'" % activity_name)
        ui_lib.wait_for_element_and_click(FusionFirmwareBundlePage.ID_ICON_ACTIVITY_COLLAPSER % activity_name, timeout=timeout, fail_if_false=fail_if_false)


class AddFirmwareBundle(object):
    @classmethod
    def click_add_firmware_bundle_button(cls, timeout=5):
        logger.debug("click [ Add Firmware Bundle ] button")
        ui_lib.wait_for_element_and_click(FusionFirmwareBundlePage.ID_LINKE_ADD_FW_BUNDLE, timeout=timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_firmware_bundle_dialog_open(cls, timeout=5, fail_if_false=True):
        logger.debug("wait add firmware bundle dialog open")
        return ui_lib.wait_for_element_visible(AddFirmwareBundleElements.ID_DIALOG_ADD, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_firmware_bundle_dialog_close(cls, timeout=5, fail_if_false=True):
        logger.debug("wait add firmware bundle dialog close")
        return ui_lib.wait_for_element_notvisible(AddFirmwareBundleElements.ID_DIALOG_ADD, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_form_message_disappear(cls, timeout=5, fail_if_false=False):
        logger.debug("wait form message disappear")
        return ui_lib.wait_for_element_notvisible(AddFirmwareBundleElements.ID_TEXT_FORM_MESSAGE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_upload_error_text(cls, timeout=5, fail_if_false=False):
        logger.debug("get upload error text")
        return ui_lib.get_text(AddFirmwareBundleElements.ID_TEXT_FORM_MESSAGE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_select_file_button(cls, timeout=5):
        logger.debug("click [ Add Firmware Bundle ] button")
        ui_lib.wait_for_element_visible(FusionFirmwareBundlePage.ID_BTN_CHOOSE_FILE, timeout=timeout)
        return ui_lib.get_s2l().click_element(FusionFirmwareBundlePage.ID_BTN_CHOOSE_FILE)

    @classmethod
    def click_ok_button(cls, timeout=5):
        logger.debug("click [ OK ] button")
        ui_lib.wait_for_element_and_click(AddFirmwareBundleElements.ID_BUTTON_OK, timeout=timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_close_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Close ] button")
        ui_lib.wait_for_element_and_click(AddFirmwareBundleElements.ID_BUTTON_CLOSE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(AddFirmwareBundleElements.ID_BUTTON_CANCEL, timeout=timeout, fail_if_false=fail_if_false)


class RemoveFirmwareBundle(object):
    @classmethod
    def select_action_delete(cls, timeout=5):
        logger.debug("click action remove button")
        ui_lib.wait_for_element_and_click(FusionFirmwareBundlePage.ID_MENU_ACTION_MAIN_BTN, timeout=timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(FusionFirmwareBundlePage.ID_MENU_ACTION_ITEM_DELETE, timeout=timeout, fail_if_false=True)

    @classmethod
    def click_remove_bundle_button(cls, timeout=5):
        logger.debug("click remove bundle button")
        ui_lib.wait_for_element_and_click(RemoveFirmwareBundleElements.ID_BUTTON_REMOVE_BUNDLE, timeout=timeout, fail_if_false=True)

    @classmethod
    def click_yes_remove_button(cls, timeout=5):
        logger.debug("click yes remove button")
        ui_lib.wait_for_element_and_click(RemoveFirmwareBundleElements.ID_BUTTON_YES_REMOVE, timeout=timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_yes_remove_button_shown(cls, timeout=5, fail_if_false=False):
        logger.debug("wait yes remove button shown")
        return ui_lib.wait_for_element_visible(RemoveFirmwareBundleElements.ID_BUTTON_YES_REMOVE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_firmware_bundle_dialog_open(cls, timeout=5, fail_if_false=True):
        logger.debug("wait remove firmware bundle dialog open")
        return ui_lib.wait_for_element_visible(RemoveFirmwareBundleElements.ID_DIALOG_REMOVE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_firmware_bundle_dialog_close(cls, timeout=10, fail_if_false=True):
        logger.debug("wait remove firmware bundle dialog close")
        return ui_lib.wait_for_element_notvisible(RemoveFirmwareBundleElements.ID_DIALOG_REMOVE, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_firmware_bundle_removed(cls, sppname, firmwareversion, timeout=10, fail_if_false=True):
        logger.debug("wait firmware bundle remove completly")
        return ui_lib.wait_for_element_notvisible(RemoveFirmwareBundleElements.ID_TITLE_FIRMWARE_BUNDLE % (sppname, firmwareversion), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_remove_error_title(cls, timeout=5):
        logger.debug("click remove failed error message title")
        return ui_lib.wait_for_element_and_click(RemoveFirmwareBundleElements.ID_PANEL_REMOVE_ERROR, timeout=timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_remove_firmware_bundle_error_text(cls, timeout=5, fail_if_false=True):
        logger.debug("wait error message 'This Service Pack for ProLiant (SPP) is being used for firmware installation and/or BIOS/Local storage provisioning on server hardwares. It cannot be removed.' shown")
        return ui_lib.wait_for_element(RemoveFirmwareBundleElements.ID_TEXT_REMOVE_ERROR, timeout=timeout, fail_if_false=fail_if_false)


class VerifyFirmwareBundle(object):
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_activity_contains_text(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("Verifying activity contains: '%s'" % expect_value)
        return ui_lib.wait_for_element(FusionFirmwareBundlePage.ID_TEXT_ACTIVITY_CONTENT % expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_firmware_component(cls, name, version, timeout=5, fail_if_false=True):
        logger.debug("Verifying firmware component named '%s' version is '%s'" % (name, version))
        return ui_lib.wait_for_element(FusionFirmwareBundlePage.ID_TEXT_FIRMWARE_COMPONENT % (name, version), timeout, fail_if_false)

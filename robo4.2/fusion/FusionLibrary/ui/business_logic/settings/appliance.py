"""
    Settings Page
"""
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco, FusionUIBase
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.settings.appliance_elements import Updateapplianceelements
from RoboGalaxyLibrary.utilitylib import logging as logger
import os
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
import re
from FusionLibrary.ui.settings.settings_elements import FusionSettingsPage
from FusionLibrary.ui.general import base_page
from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.data import test_data


class Updateappliance(object):

    @classmethod
    def click_update_appliance(cls, timeout=5, fail_if_false=True):
        logger.debug("click update appliance ")
        return ui_lib.wait_for_element_and_click(Updateapplianceelements.ID_BUTTON_UPDATE_APPLIANCE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_update_appliance_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait update appliance dialog shown")
        return ui_lib.wait_for_element_visible(Updateapplianceelements.ID_DIALOG_UPDATE_APPLIANCE, timeout, fail_if_false)

    @classmethod
    def tick_update_image(cls, timeout=5, fail_if_false=True):
        logger.debug("choose update image option")
        return FusionUIBase.wait_for_checkbox_and_select(Updateapplianceelements.ID_RADIO_SELECT_UPDATE_IMAGE, timeout, fail_if_false)

    @classmethod
    def click_browse_button(cls, timeout=5, fail_if_false=True):
        logger.debug("click Browse button")
        return ui_lib.wait_for_element_and_click(Updateapplianceelements.ID_BUTTON_BROWSE, timeout, fail_if_false)

    @classmethod
    def click_upload_and_install(cls, timeout=5, fail_if_false=True):
        logger.debug("select option[upload and install] ")
        return ui_lib.wait_for_element_and_click(Updateapplianceelements.ID_BUTTON_UPLOAD_AND_INSTALL, timeout, fail_if_false)

    @classmethod
    def click_upload_only(cls, timeout=5, fail_if_false=True):
        logger.debug("select option[upload only] ")
        return ui_lib.wait_for_element_and_click(Updateapplianceelements.ID_BUTTON_UPLOAD_ONLY, timeout, fail_if_false)

    @classmethod
    def click_action_button(cls, timeout=5, fail_if_false=True):
        logger.debug("select option[action only] ")
        logger.info("timout action is %s" % timeout)
        return ui_lib.wait_for_element_and_click(Updateapplianceelements.ID_SELECT_ACTION_MENU, timeout, fail_if_false)

    @classmethod
    def select_update_appliance(cls, timeout=5, fail_if_false=True):
        logger.debug("select option[update app only] ")
        return ui_lib.wait_for_element_and_click(Updateapplianceelements.ID_SELECT_ACTION_UPDATE_APPLIANCE, timeout, fail_if_false)

    @classmethod
    def click_update_option(cls, timeout=5, fail_if_false=True):
        logger.debug("select option[update] ")
        return ui_lib.wait_for_element_and_click(Updateapplianceelements.ID_BUTTON_UPDATE_OPTION, timeout, fail_if_false)

    @classmethod
    def tick_accept_licence(cls, timeout=5, fail_if_false=True):
        logger.debug("select option[accept licence] ")
        return ui_lib.wait_for_element_and_click(Updateapplianceelements.ID_CHECKBOX_TERMS_AND_CONDITIONS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_file_added(cls, timeout=5, fail_if_false=True):
        logger.debug("verify file uploaded or not ")
        return ui_lib.wait_for_element_visible(Updateapplianceelements.ID_TEXT_FILE_VISIBLE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_update_dialog_appear(cls, timeout=5, fail_if_false=True):
        logger.debug("select option [ update ] ")
        return ui_lib.wait_for_element_visible(Updateapplianceelements.ID_DIALOG_WAIT_FOR_UPDATE, timeout, fail_if_false)

    @classmethod
    def tick_accept_agreement(cls, timeout=5, fail_if_false=True):
        logger.debug("select option[accept licence] ")
        return ui_lib.wait_for_checkbox_and_select(Updateapplianceelements.ID_CHECKBOX_AGREEMENT, timeout, fail_if_false)

    @classmethod
    def click_update_button(cls, timeout=5, fail_if_false=True):
        logger.debug("select option [update] ")
        return ui_lib.wait_for_element_and_click(Updateapplianceelements.ID_SELECT_UPLOAD_AND_INSTALL_UPDATE, timeout, fail_if_false)

    @classmethod
    def click_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("select option[cancel] ")
        return ui_lib.wait_for_element_and_click(Updateapplianceelements.ID_BUTTON_CANCEL, timeout, fail_if_false)

    @classmethod
    def tick_uploaded_image(cls, timeout=5, fail_if_false=True):
        logger.debug("choose uploaded image option")
        return FusionUIBase.wait_for_checkbox_and_select(Updateapplianceelements.ID_RADIO_UPDATE_FROM_UPLOADED_IMAGE, timeout, fail_if_false)

    @classmethod
    def get_appliance_version(cls, timeout=5, fail_if_false=True):
        logger.debug("getting the appliance version")
        return FusionUIBase.get_text(Updateapplianceelements.ID_TEXT_APPLIANCE_VERSION, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_settings_page_to_appear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for settings page ")
        return ui_lib.wait_for_element_visible(Updateapplianceelements.ID_VIEW_SETTINGS_PAGE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_progress_bar_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for progress bar to disappear")
        return ui_lib.wait_for_element_remove(Updateapplianceelements.ID_VIEW_UPDATE_PROGRESS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_progress_bar_appear(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting for progress bar to appear")
        return ui_lib.wait_for_element_visible(Updateapplianceelements.ID_VIEW_UPDATE_PROGRESS, timeout, fail_if_false)

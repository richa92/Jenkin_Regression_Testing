# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Settings Page
"""
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco, FusionUIBase
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.settings.timeandlocale_elements import GeneralTimeAndLocaleElements, \
    EditTimeAndLocaleElements


class EditTimeAndLocale(object):

    @classmethod
    def click_time_and_locale(cls, timeout=5):
        logger.debug("click Time and Locale ")
        ui_lib.wait_for_element_and_click(GeneralTimeAndLocaleElements.ID_TIME_AND_LOCALE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_time_and_local_panel_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait for time and local panel shows up")
        ui_lib.wait_for_element_visible(GeneralTimeAndLocaleElements.ID_TEXT_TIME_AND_LOCALE, timeout, fail_if_false)

    @classmethod
    def select_action_edit(cls, timeout=5):
        logger.debug("select action edit")
        ui_lib.wait_for_element_and_click(GeneralTimeAndLocaleElements.ID_DROPDOWN_ACTION, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditTimeAndLocaleElements.ID_SELECT_ACTION_EDIT, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_time_and_locale_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait edit time and locale dialog shown")
        ui_lib.wait_for_element_visible(EditTimeAndLocaleElements.ID_DIALOG_EDIT_TIME_AND_LOCALE, timeout,
                                        fail_if_false)

    @classmethod
    def choose_synchronize_with_vm_host(cls, timeout=5, fail_if_false=True):
        logger.debug("choose Synchronize with VM host")
        ui_lib.wait_for_element_and_click(EditTimeAndLocaleElements.ID_RADIO_SYNCHRONIZE_WITH_VM_HOST, timeout,
                                          fail_if_false)

    @classmethod
    def choose_synchronize_with_time_server(cls, timeout=5, fail_if_false=True):
        logger.debug("choose Synchronize with time server")
        ui_lib.wait_for_element_and_click(EditTimeAndLocaleElements.ID_RADIO_SYNCHRONIZE_WITH_TIME_SERVER, timeout,
                                          fail_if_false)

    @classmethod
    def input_select_default_language_locale(cls, language_locale, timeout=5, fail_if_false=True):
        logger.debug("input Default language / locale %s" % language_locale)

        if "English" in language_locale:
            data_id = "en_US.UTF-8"
        elif "Chinese" in language_locale:
            data_id = "zh_CN.UTF-8"
        elif "Japanese" in language_locale:
            data_id = "ja_JP.UTF-8"
        else:
            ui_lib.fail_test("Invalid value for language and locale: %s" % language_locale)
        # ui_lib.wait_for_element_and_input_text(EditTimeAndLocaleElements.ID_INPUT_DEFAULT_LANGUAGE_LOCALE, language_locale, timeout,
        #                                        fail_if_false)
        ui_lib.wait_for_element_and_click(EditTimeAndLocaleElements.ID_COMBO_SEARCH_DEFAULT_LANGUAGE_AND_LOCALE)
        ui_lib.wait_for_element_and_click(EditTimeAndLocaleElements.ID_SELECT_DEFAULT_LANGUAGE_LOCALE_DATA_ID % data_id, timeout, fail_if_false)

    @classmethod
    def input_network_time_server1(cls, time_server, timeout=5, fail_if_false=True):
        logger.debug("input Network time server 1 %s" % time_server)
        ui_lib.wait_for_element_and_input_text(EditTimeAndLocaleElements.ID_INPUT_NETWORK_TIME_SERVER1, time_server, timeout,
                                               fail_if_false)

    @classmethod
    def input_network_time_server2(cls, time_server, timeout=5, fail_if_false=True):
        logger.debug("input Network time server 2 %s" % time_server)
        ui_lib.wait_for_element_and_input_text(EditTimeAndLocaleElements.ID_INPUT_NETWORK_TIME_SERVER2, time_server, timeout,
                                               fail_if_false)

    @classmethod
    def input_network_time_server3(cls, time_server, timeout=5, fail_if_false=True):
        logger.debug("input Network time server 3 %s" % time_server)
        ui_lib.wait_for_element_and_input_text(EditTimeAndLocaleElements.ID_INPUT_NETWORK_TIME_SERVER3, time_server, timeout,
                                               fail_if_false)

    @classmethod
    def input_network_time_server4(cls, time_server, timeout=5, fail_if_false=True):
        logger.debug("input Network time server 4 %s" % time_server)
        ui_lib.wait_for_element_and_input_text(EditTimeAndLocaleElements.ID_INPUT_NETWORK_TIME_SERVER4, time_server, timeout,
                                               fail_if_false)

    @classmethod
    def click_time_and_locale_edit_ok(cls, timeout=5):
        logger.debug("click Time and Locale edit OK ")
        ui_lib.wait_for_element_and_click(EditTimeAndLocaleElements.ID_BUTTON_OK, timeout, fail_if_false=True)

    @classmethod
    def click_time_and_locale_edit_cancel(cls, timeout=5):
        logger.debug("click Time and Locale edit Cancel ")
        ui_lib.wait_for_element_and_click(EditTimeAndLocaleElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_time_and_locale_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait edit time and locale dialog disappear")
        ui_lib.wait_for_element_notvisible(EditTimeAndLocaleElements.ID_DIALOG_EDIT_TIME_AND_LOCALE, timeout,
                                           fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_update_time_and_local_complete(cls, timeout=5, fail_if_false=True):
        logger.debug("wait progress bar - update time and local completed")
        ui_lib.wait_for_element_visible(EditTimeAndLocaleElements.ID_PROGRESS_BAR_COMPLETED, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_settings(cls, timeout=5):
        logger.debug("click settings back to main page")
        ui_lib.wait_for_element_and_click(EditTimeAndLocaleElements.ID_TEXT_SETTINGS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_time_and_local_panel_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait for time and local panel is disappeared")
        ui_lib.wait_for_element_notvisible(GeneralTimeAndLocaleElements.ID_TEXT_TIME_AND_LOCALE, timeout, fail_if_false)


class VerifyTimeAndLocale(object):

    @classmethod
    def verify_locale(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify locale ,except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("locale", GeneralTimeAndLocaleElements.ID_TEXT_LOCALE, except_value, timeout, fail_if_false)

    @classmethod
    def verify_network_time_server_1(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify Network time server 1,except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("network time server 1", GeneralTimeAndLocaleElements.ID_TEXT_NETWORK_TIME_SERVER_1, except_value, timeout, fail_if_false)

    @classmethod
    def verify_network_time_server_2(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify Network time server 2,except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("network time server 2", GeneralTimeAndLocaleElements.ID_TEXT_NETWORK_TIME_SERVER_2, except_value, timeout, fail_if_false)

    @classmethod
    def verify_network_time_server_3(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify Network time server 3,except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("network time server 3", GeneralTimeAndLocaleElements.ID_TEXT_NETWORK_TIME_SERVER_3, except_value, timeout, fail_if_false)

    @classmethod
    def verify_network_time_server_4(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify Network time server 4,except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("network time server 4", GeneralTimeAndLocaleElements.ID_TEXT_NETWORK_TIME_SERVER_4, except_value, timeout, fail_if_false)

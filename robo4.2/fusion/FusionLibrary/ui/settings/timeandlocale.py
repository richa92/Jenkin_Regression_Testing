# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Time and locale Page
"""
import time
from FusionLibrary.ui.business_logic.base import FusionUIBase
from FusionLibrary.ui.business_logic.base import SectionType
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.settings.timeandlocale import EditTimeAndLocale
from FusionLibrary.ui.business_logic.settings.timeandlocale import VerifyTimeAndLocale


def edit_time_and_locale(time_and_locale_obj):
    """Edit time and locale"""
    FusionUIBase.navigate_to_section(SectionType.SETTINGS)
    EditTimeAndLocale.click_time_and_locale()
    EditTimeAndLocale.wait_time_and_local_panel_shown()
    EditTimeAndLocale.select_action_edit()
    EditTimeAndLocale.wait_edit_time_and_locale_dialog_shown()
    logger.info("Edit time and locale")

    if time_and_locale_obj.synchronizetype.lower().strip() == "vm host":
        EditTimeAndLocale.choose_synchronize_with_vm_host()
    elif time_and_locale_obj.synchronizetype.lower().strip() == "time server":
        EditTimeAndLocale.choose_synchronize_with_time_server()
        if getattr(time_and_locale_obj, 'timeserver1', '') != '':
            EditTimeAndLocale.input_network_time_server1(time_and_locale_obj.timeserver1)
        if getattr(time_and_locale_obj, 'timeserver2', '') != '':
            EditTimeAndLocale.input_network_time_server2(time_and_locale_obj.timeserver2)
        if getattr(time_and_locale_obj, 'timeserver3', '') != '':
            EditTimeAndLocale.input_network_time_server3(time_and_locale_obj.timeserver3)
        if getattr(time_and_locale_obj, 'timeserver4', '') != '':
            EditTimeAndLocale.input_network_time_server4(time_and_locale_obj.timeserver4)

    else:
        logger.warn("the time synchronize type is not correct ")
        return False
    EditTimeAndLocale.input_select_default_language_locale(time_and_locale_obj.defaultlanguagelocale)
    EditTimeAndLocale.click_time_and_locale_edit_ok()
    EditTimeAndLocale.wait_edit_time_and_locale_dialog_disappear(timeout=10)
    EditTimeAndLocale.wait_update_time_and_local_complete(timeout=10)
    EditTimeAndLocale.click_settings()
    EditTimeAndLocale.wait_edit_time_and_locale_dialog_disappear()
    return True


def verify_time_and_locale(time_and_locale_obj):
    """Verify Time And Locale"""
    FusionUIBase.navigate_to_section(SectionType.SETTINGS)
    EditTimeAndLocale.click_time_and_locale()
    EditTimeAndLocale.wait_time_and_local_panel_shown()

    VerifyTimeAndLocale.verify_locale(time_and_locale_obj.defaultlanguagelocale)
    if getattr(time_and_locale_obj, 'timeserver1', '') == '':
        VerifyTimeAndLocale.verify_network_time_server_1("not configured")
    else:
        VerifyTimeAndLocale.verify_network_time_server_1(time_and_locale_obj.timeserver1)

    if getattr(time_and_locale_obj, 'timeserver2', '') != '':
        VerifyTimeAndLocale.verify_network_time_server_2(time_and_locale_obj.timeserver2)

    if getattr(time_and_locale_obj, 'timeserver3', '') != '':
        VerifyTimeAndLocale.verify_network_time_server_3(time_and_locale_obj.timeserver3)

    if getattr(time_and_locale_obj, 'timeserver4', '') != '':
        VerifyTimeAndLocale.verify_network_time_server_4(time_and_locale_obj.timeserver4)

    EditTimeAndLocale.click_settings()
    EditTimeAndLocale.wait_edit_time_and_locale_dialog_disappear()
    return True

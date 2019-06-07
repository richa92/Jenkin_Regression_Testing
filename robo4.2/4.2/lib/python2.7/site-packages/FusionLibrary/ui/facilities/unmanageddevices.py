# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Unmanaged Devices page

"""


from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.business_logic.facilities.unmanageddevices_elements import FusionUnmanagedDevicePage
from FusionLibrary.ui.business_logic.base import FusionUIBase, SectionType


def navigate():
    FusionUIBase.navigate_to_section(SectionType.UNMANAGED_DEVICES)


def add_unmanaged_device(*uds_obj):
    """ Add Unmanaged device to appliance    """

    failed_times = 0
    selenium2lib = ui_lib.get_s2l()
    if not ui_lib.wait_for_element(FusionUnmanagedDevicePage.ID_PAGE_LABEL):
        navigate()

    if isinstance(uds_obj, test_data.DataObj):
        uds_obj = [uds_obj]
    elif isinstance(uds_obj, tuple):
        uds_obj = list(uds_obj[0])

    for uds in uds_obj:
        uds_list = [ui_lib.get_webelement_attribute("text", el) for el in selenium2lib._element_find(FusionUnmanagedDevicePage.ID_UDS_LIST_NAMES, False, False)]
        if uds.name in uds_list:
            logger._warn("Unmanaged device '%s' already exists. Cannot proceed with adding Unmanaged device" % uds.name)
            selenium2lib.capture_page_screenshot()
            failed_times = failed_times + 1
            continue

        if(uds.name == "" or uds.model == "" or uds.maxpower == ""):
            logger._warn("Mandatory fields for adding Unmanaged device can't be empty")
            selenium2lib.capture_page_screenshot()
            failed_times = failed_times + 1
            continue

        logger._log_to_console_and_log_file("Adding Unmanaged device %s" % uds.name)
        logger._log_to_console_and_log_file("-----------------------------")

        ui_lib.wait_for_element_and_click(FusionUnmanagedDevicePage.ID_LINK_CREATE_UD)
        ui_lib.wait_for_element_visible(FusionUnmanagedDevicePage.ID_INPUT_NAME_UNMANAGED_DEVICE)
        ui_lib.wait_for_element_and_input_text(FusionUnmanagedDevicePage.ID_INPUT_NAME_UNMANAGED_DEVICE, uds.name)
        ui_lib.wait_for_element_visible(FusionUnmanagedDevicePage.ID_INPUT_MODEL)
        ui_lib.wait_for_element_and_input_text(FusionUnmanagedDevicePage.ID_INPUT_MODEL, uds.model)
        ui_lib.wait_for_element_visible(FusionUnmanagedDevicePage.ID_COMBO_HEIGHT)
        # ui_lib.wait_for_element_and_click(FusionUnmanagedDevicePage.ID_COMBO_HEIGHT)

#        for i in range(1, 42):
        # selenium2lib.press_key(FusionUnmanagedDevicePage.ID_COMBO_HEIGHT, '\\38')
        # while selenium2lib.get_text(FusionUnmanagedDevicePage.ID_COMBO_HEIGHT) != uds.height:
        #   selenium2lib.press_key(FusionUnmanagedDevicePage.ID_COMBO_HEIGHT, '\\40')
        ui_lib.wait_for_element_and_click(FusionUnmanagedDevicePage.ID_COMBO_HEIGHT)
        ui_lib.wait_for_element_and_click(FusionUnmanagedDevicePage.ID_COMBO_OPTION % uds.height)

        ui_lib.wait_for_element_visible(FusionUnmanagedDevicePage.ID_INPUT_MAXIMUM_POWER)
        ui_lib.wait_for_element_and_input_text(FusionUnmanagedDevicePage.ID_INPUT_MAXIMUM_POWER, uds.maxpower)
        ui_lib.wait_for_element_visible(FusionUnmanagedDevicePage.ID_BTN_ADD_UNMANAGED_DEVICE)
        selenium2lib.click_button(FusionUnmanagedDevicePage.ID_BTN_ADD_UNMANAGED_DEVICE)

        logger._log_to_console_and_log_file("Checking whether Unmanaged device %s is added or not" % uds.name)
        selenium2lib.wait_until_page_contains_element(FusionUnmanagedDevicePage.ID_LINK_CREATE_UD)
        if ui_lib.wait_for_element(FusionUnmanagedDevicePage.ID_LINK_CREATE_UD):
            uds_list = [ui_lib.get_webelement_attribute("text", el) for el in selenium2lib._element_find(FusionUnmanagedDevicePage.ID_UDS_LIST_NAMES, False, False)]
            if uds.name in uds_list:
                logger._log_to_console_and_log_file("Unmanaged device '%s' is added successfully" % uds.name)

    if failed_times > 0:
        return False
    else:
        return True


def edit_unmanaged_device(*uds_obj):
    """ Edit Unmanaged device to appliance    """

    failed_times = 0
    selenium2lib = ui_lib.get_s2l()
    if not ui_lib.wait_for_element(FusionUnmanagedDevicePage.ID_PAGE_LABEL):
        navigate()

    if isinstance(uds_obj, test_data.DataObj):
        uds_obj = [uds_obj]
    elif isinstance(uds_obj, tuple):
        uds_obj = list(uds_obj[0])

    for edit_uds in uds_obj:
        uds_list = [ui_lib.get_webelement_attribute("text", el) for el in selenium2lib._element_find(FusionUnmanagedDevicePage.ID_UDS_LIST_NAMES, False, False)]
        if edit_uds.name not in uds_list:
            ui_lib.fail_test("Unmanaged device '%s' not exists. Cannot proceed with editing" % edit_uds.name)
            selenium2lib.capture_page_screenshot()
            failed_times = failed_times + 1
            continue

        logger._log_to_console_and_log_file("Editing Unmanaged device %s" % edit_uds.name)
        logger._log_to_console_and_log_file("-----------------------------")

        ui_lib.wait_for_element_and_click(FusionUnmanagedDevicePage.ID_ELEMENT_UNAMANGED_DEVICE_BASE % edit_uds.name)
        ui_lib.wait_for_element_and_click(FusionUnmanagedDevicePage.ID_MENU_ACTION_MAIN_BTN)
        ui_lib.wait_for_element_and_click(FusionUnmanagedDevicePage.ID_MENU_ACTION_EDIT)

        if edit_uds.has_property("new_name"):
            ui_lib.wait_for_element_and_input_text(FusionUnmanagedDevicePage.ID_INPUT_NAME_UNMANAGED_DEVICE, edit_uds.new_name)

        if edit_uds.has_property("model"):
            ui_lib.wait_for_element_and_input_text(FusionUnmanagedDevicePage.ID_INPUT_MODEL, edit_uds.model)

        if edit_uds.has_property("height"):
            #            for i in range(1,42):
                # selenium2lib.press_key(FusionUnmanagedDevicePage.ID_COMBO_HEIGHT, '\\38')
                # while selenium2lib.get_text(FusionUnmanagedDevicePage.ID_COMBO_HEIGHT) != edit_uds.height:
                #    selenium2lib.press_key(FusionUnmanagedDevicePage.ID_COMBO_HEIGHT, '\\40')
            ui_lib.wait_for_element_and_click(FusionUnmanagedDevicePage.ID_COMBO_HEIGHT)
            ui_lib.wait_for_element_and_click(FusionUnmanagedDevicePage.ID_COMBO_OPTION % edit_uds.height)

        if edit_uds.has_property("maxpower"):
            ui_lib.wait_for_element_and_input_text(FusionUnmanagedDevicePage.ID_INPUT_MAXIMUM_POWER, edit_uds.maxpower)
#         ui_lib.wait_for_element_visible(FusionUnmanagedDevicePage.ID_INPUT_MODEL)
        selenium2lib.click_button(FusionUnmanagedDevicePage.ID_BTN_UPDATE)

        logger._log_to_console_and_log_file("Checking for Edit status of Unmanaged device %s " % edit_uds.name)
#         ui_lib.wait_for_element_visible(FusionUnmanagedDevicePage.ID_UDS_UPDATE_SUCESS, PerfConstants.UPDATE_UNMANGED_DEVICE_TIME)
        ui_lib.wait_for_element_visible(FusionUnmanagedDevicePage.ID_UDS_UPDATE_SUCESS, PerfConstants.UPDATE_UNMANGED_DEVICE_TIME)
        if ui_lib.wait_for_element(FusionUnmanagedDevicePage.ID_UDS_UPDATE_SUCESS):
            logger._log_to_console_and_log_file("Unmanaged device '%s' is updated successfully" % edit_uds.name)
        else:
            selenium2lib.capture_page_screenshot()
            failed_times = failed_times + 1
            ui_lib.fail_test("Editing Unmanaged device '%s' is Failed" % edit_uds.name)

    if failed_times > 0:
        return False
    else:
        return True


def remove_unmanaged_device(*uds_obj):
    """ Delete Unmanaged device to appliance    """
    failed_times = 0
    selenium2lib = ui_lib.get_s2l()
    if not ui_lib.wait_for_element(FusionUnmanagedDevicePage.ID_PAGE_LABEL):
        navigate()

    if isinstance(uds_obj, test_data.DataObj):
        uds_obj = [uds_obj]
    elif isinstance(uds_obj, tuple):
        uds_obj = list(uds_obj[0])

    for uds in uds_obj:
        uds_list = [ui_lib.get_webelement_attribute("text", el) for el in selenium2lib._element_find(FusionUnmanagedDevicePage.ID_UDS_LIST_NAMES, False, False)]
        if uds.name not in uds_list:
            logger._warn("Unmanaged device '%s' does not exist" % uds.name)
            selenium2lib.capture_page_screenshot()
            failed_times = failed_times + 1
            continue

        logger._log_to_console_and_log_file("-----------------------------")
        logger._log_to_console_and_log_file("Removing Unmanaged device %s" % uds.name)
        logger._log_to_console_and_log_file("-----------------------------")

        ui_lib.wait_for_element_and_click(FusionUnmanagedDevicePage.ID_ELEMENT_UNAMANGED_DEVICE_BASE % uds.name)
        ui_lib.wait_for_element_and_click(FusionUnmanagedDevicePage.ID_MENU_ACTION_MAIN_BTN)
        ui_lib.wait_for_element_and_click(FusionUnmanagedDevicePage.ID_MENU_ACTION_REMOVE)
        ui_lib.wait_for_element_and_click(FusionUnmanagedDevicePage.ID_BTN_REMOVE_UD_CONFIRM)
        ui_lib.wait_for_element_remove(
            FusionUnmanagedDevicePage.ID_ELEMENT_UNAMANGED_DEVICE_BASE % uds.name, PerfConstants.DEFAULT_SYNC_TIME)

        logger._log_to_console_and_log_file("Checking whether Unmanaged device %s is Deleted or not" % uds.name)
        ui_lib.wait_for_element_visible(FusionUnmanagedDevicePage.ID_LINK_CREATE_UD)
        uds_list = [ui_lib.get_webelement_attribute("text", el) for el in selenium2lib._element_find(FusionUnmanagedDevicePage.ID_UDS_LIST_NAMES, False, False)]
        if uds.name not in uds_list:
            logger._log_to_console_and_log_file("Unmanaged device '%s' removed successfully" % uds.name)
        else:
            ui_lib.fail_test(" The Unmanaged device '%s' not removed successfully" % uds.name)
            selenium2lib.capture_page_screenshot()
            failed_times = failed_times + 1

    if failed_times > 0:
        return False
    else:
        return True


# def navigate():
#     base_page.navigate_base(FusionUnmanagedDevicePage.ID_PAGE_LABEL, FusionUIBaseElements.ID_MENU_LINK_UNMANAGED_DEVICES, "css=span.hp-page-item-count")


def add_data_centers(datacenterName, *params):
    raise NotImplementedError


def edit_data_center(datacenterName, *params):
    raise NotImplementedError


def remove_data_center(self, datacenterName):
    raise NotImplementedError


def select_data_center(self, datacenterName):
    raise NotImplementedError

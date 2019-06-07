# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
""" Fusion Logical Enclosure UI page."""
from FusionLibrary.ui.business_logic.base import FusionUIBase
from datetime import datetime
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib
from robot.libraries.BuiltIn import BuiltIn
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco
from FusionLibrary.ui.business_logic.servers.logicalenclosures_elements import *


class _BaseCommonOperationLogicalEnclosures(object):

    """
    This class holds all common operation of logical enclosure.
    It also defines abstract methods which the subclass has different implementation for C7000 & TBird
    """
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_enclosure_status_ok(cls, le_name, timeout=10, fail_if_false=True):
        logger.debug("verify [ logical enclosure '%s' ] status should be OK" % le_name)
        return ui_lib.wait_for_element_visible(GeneralLogicalEnclosureElements.ID_STATUS_LOGICAL_ENCLOSURE_OK % le_name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_enclosure_warn(cls, le_name, timeout=10, fail_if_false=True):
        logger.debug("verify [ logical enclosure '%s' ] status should be WARN" % le_name)
        return ui_lib.wait_for_element_visible(GeneralLogicalEnclosureElements.ID_STATUS_LOGICAL_ENCLOSURE_WARN % le_name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_enclosure_error(cls, le_name, timeout=10, fail_if_false=True):
        logger.debug("verify [ logical enclosure '%s' ] status should be ERROR" % le_name)
        return ui_lib.wait_for_element_visible(GeneralLogicalEnclosureElements.ID_STATUS_LOGICAL_ENCLOSURE_ERROR % le_name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_enclosure_selected(cls, le_name, timeout=10, fail_if_false=True):
        logger.debug("verify [ logical enclosure '%s' ] should be selected" % le_name)
        return ui_lib.wait_for_element(GeneralLogicalEnclosureElements.ID_TABLE_LOGICAL_ENCLOSURE_SELECTED % le_name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_logical_enclosure_status(cls, le_name, timeout=10, fail_if_false=True):
        logger.debug("get [ logical enclosure '%s' ] status" % le_name)
        locator = GeneralLogicalEnclosureElements.ID_STATUS_LOGICAL_ENCLOSURE % le_name

        if ui_lib.wait_for_element(locator, timeout=timeout, fail_if_false=fail_if_false):
            return ui_lib.get_text(locator, fail_if_false=fail_if_false, hidden_element=True)
        else:
            msg = "failed waiting for element present by locator '%s'" % locator
            if fail_if_false:
                ui_lib.fail_test(msg)
            else:
                return None

    @classmethod
    def get_logical_enclosure_list(cls, timeout=5):
        logger.debug("Get all [ logical enclosure names ] from table")
        logical_enclosure_name_list = []
        if ui_lib.wait_for_element(GeneralLogicalEnclosureElements.ID_TABLE_LOGICAL_ENCLOSURES):
            logical_enclosure_name_list = FusionUIBase.get_multi_elements_text(GeneralLogicalEnclosureElements.ID_TABLE_LOGICAL_ENCLOSURES, timeout, fail_if_false=True)
        return logical_enclosure_name_list

    @classmethod
    def get_logical_interconnects_of_le(cls, timeout=5, fail_if_false=True):
        logger.debug("Get [ Logical Interconnect] from selected LE")
        ui_lib.wait_for_element_visible(GeneralLogicalEnclosureElements.ID_TEXT_LOGICAL_INTERCONNECT_DETAILS, timeout, fail_if_false)
        return FusionUIBase.get_multi_elements_text(GeneralLogicalEnclosureElements.ID_TEXT_LOGICAL_INTERCONNECT_DETAILS, timeout, fail_if_false)

    @classmethod
    def click_logical_enclosure(cls, le_name, timeout=5):
        logger.debug("select [ logical enclosure '%s' ]" % le_name)
        ui_lib.wait_for_element_and_click(GeneralLogicalEnclosureElements.ID_TABLE_LOGICAL_ENCLOSURE % le_name, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_sidebar_activity_action_ok(cls, le_name, timeout=600, fail_if_false=True):
        logger.debug("waiting [ activity action of logical enclosure '%s' ] change to ok" % le_name)
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_ACTION_OK % le_name, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_ACTION_TITLE % le_name)
                logger.debug("[ activity action '%s' status ] is ok as expected." % actionname)
                return True
            elif ui_lib.wait_for_element_visible(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_ACTION_WARN % le_name, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_ACTION_TITLE % le_name)
                logger.debug("[ activity action '%s' status ] is warn not as expected." % actionname)
                ui_lib.wait_for_element_and_click(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_ACTION_WARN % le_name)
                msg = FusionUIBase.get_multi_elements_text(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_MESSAGE)
                # bypass specific warning message when delete monitored enclosure
                msg = [s for s in msg if msg != ''][0]
#                 if 'Resolution Delete the HPOneViewMonitor user manually on Onboard Administrator.' in msg:
#                     logger.debug("warning message [ %s ] is expected after deleting monitored enclosure." % msg)
#                     return True
                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            elif ui_lib.wait_for_element_visible(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_ACTION_ERROR % le_name, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_ACTION_TITLE % le_name)
                logger.debug("[ activity action '%s' status ] is error not as expected." % actionname)
                ui_lib.wait_for_element_and_click(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_ACTION_ERROR % le_name)
                msg = FusionUIBase.get_multi_elements_text(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_MESSAGE)
                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            else:
                if ui_lib.wait_for_element_visible(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_ACTION_TITLE % le_name):
                    actionname = FusionUIBase.get_text(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_ACTION_TITLE % le_name)
                else:
                    actionname = 'None'
                logger.debug("[ activity action '%s' status ] is unknown, waiting ..." % actionname)
                continue
        err_msg = "Timeout to waiting [ activity action ] completed."
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_activity_action_ok(cls, timeout=600, fail_if_false=True):
        logger.debug("waiting [ activity action of logical enclosure ] change to ok")
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_OK, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_TITLE)
                logger.debug("[ activity action '%s' status ] is ok as expected." % actionname)
                return True
            elif ui_lib.wait_for_element_visible(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_WARN, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_TITLE)
                logger.debug("[ activity action '%s' status ] is warn not as expected." % actionname)
                ui_lib.wait_for_element_and_click(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_WARN)
                msg = FusionUIBase.get_multi_elements_text(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_MESSAGE)
                msg = [s for s in msg if msg != ''][0]
                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            elif ui_lib.wait_for_element_visible(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_ERROR, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_TITLE)
                logger.debug("[ activity action '%s' status ] is error not as expected." % actionname)
                ui_lib.wait_for_element_and_click(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_ERROR)
                msg = FusionUIBase.get_multi_elements_text(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_MESSAGE)
                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            else:
                if ui_lib.wait_for_element_visible(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_TITLE):
                    actionname = FusionUIBase.get_text(GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_TITLE)
                else:
                    actionname = 'None'
                logger.debug("[ activity action '%s' status ] is unknown, waiting ..." % actionname)
                continue
        err_msg = "Timeout to waiting [ activity action ] completed."
        return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_le_selected(cls, le_name, timeout=5, fail_if_false=True):
        logger.debug("wait [ LE '%s' ] selected" % le_name)
        return ui_lib.wait_for_element_visible(GeneralLogicalEnclosureElements.ID_TABLE_LOGICAL_ENCLOSURE_SELECTED % le_name, timeout, fail_if_false)

    @classmethod
    def get_enclosure_list_from_le(cls, timeout=5, fail_if_false=True):
        logger.debug("Get all [ enclosure names ] from LE")
        enclosure_list = []
        if ui_lib.wait_for_element_visible(GeneralLogicalEnclosureElements.ID_ENCLOSURES_DETAILS, timeout, fail_if_false):
            enclosure_list = FusionUIBase.get_multi_elements_text(GeneralLogicalEnclosureElements.ID_TEXT_ENCLOSURES_IN_LE, timeout, fail_if_false, True)
        return enclosure_list


class CommonOperationLogicalEnclosures(_BaseCommonOperationLogicalEnclosures):
    pass


class C7000CommonOperationLogicalEnclosures(_BaseCommonOperationLogicalEnclosures):
    pass


class TBirdCommonOperationLogicalEnclosures(_BaseCommonOperationLogicalEnclosures):
    pass


class TBirdCreateLogicalEnclosures(object):

    @classmethod
    def click_create_logical_enclosure(cls, timeout=5):
        logger.debug("click [ Create logical enclosure ] button")
        ui_lib.wait_for_element_and_click(CreateLogicalEnclosuresElements.ID_BUTTON_CREATE_LOGICAL_ENCLOSURE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_le_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Create Logical Enclosure ] dialog shown")
        return ui_lib.wait_for_element_visible(CreateLogicalEnclosuresElements.ID_DIALOG_CREATE_LOGICAL_ENCLOSURE, timeout, fail_if_false)

    @classmethod
    def input_name(cls, name, timeout=5):
        logger.debug("input [ %s ] into [ Name ] textbox" % name)
        ui_lib.wait_for_element_and_input_text(CreateLogicalEnclosuresElements.ID_INPUT_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def input_select_enclosures(cls, enclosures, timeout=5):
        logger.debug("input and select [ %s ] into [ Enclosures ] combo box" % enclosures)
        FusionUIBase.choose_combo_option_by_text(CreateLogicalEnclosuresElements.ID_COMBO_ENCLOSURES, enclosures, timeout, fail_if_false=True)

    @classmethod
    def input_select_enclosures_dropdown(cls, enclosures, timeout=5):
        ui_lib.wait_for_element_and_click(CreateLogicalEnclosuresElements.ID_COMBO_ENCLOSURES_SEARCH_BUTTON, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(CreateLogicalEnclosuresElements.ID_COMBO_ENCLOSURES_SELECT % enclosures, 10, fail_if_false=True)

    @classmethod
    def input_select_enclosure_group(cls, encgroup, timeout=5):
        logger.debug("input and select [ %s ] into [ Enclosure group ] text box" % encgroup)
        FusionUIBase.choose_combo_option_by_text(CreateLogicalEnclosuresElements.ID_COMBO_ENCLOSURE_GROUP, encgroup, timeout, fail_if_false=True)

    @classmethod
    def input_select_firmware_baseline(cls, firmware_baseline, timeout=5, fail_if_false=True):
        logger.debug("input and select [ %s ] into [ Firmware Baseline ] text box" % firmware_baseline)
        FusionUIBase.choose_option_by_text(CreateLogicalEnclosuresElements.ID_COMBO_FIRMWARE_BASELINE, firmware_baseline, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def select_force_install(cls, timeout=5, fail_if_false=True):
        logger.debug("Selecting Force install")
        ui_lib.wait_for_checkbox_and_select(CreateLogicalEnclosuresElements.ID_CHECKBOX_FIRMWARE_FORCE_INSTALL, timeout, fail_if_false)

    @classmethod
    def click_create_button(cls, timeout=5):
        logger.debug("click [ Create ] button")
        ui_lib.wait_for_element_and_click(CreateLogicalEnclosuresElements.ID_BUTTON_CREATE, timeout, fail_if_false=True)

    @classmethod
    def click_create_plus_button(cls, timeout=5):
        logger.debug("click [ Create + ] button")
        ui_lib.wait_for_element_and_click(CreateLogicalEnclosuresElements.ID_BUTTON_CREATE_PLUS, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(CreateLogicalEnclosuresElements.ID_BUTTON_CREATE_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_le_dialog_disappear(cls, timeout=60, fail_if_false=True):
        logger.debug("wait [ Create Logical Enclosure ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(CreateLogicalEnclosuresElements.ID_DIALOG_CREATE_LOGICAL_ENCLOSURE, timeout, fail_if_false)


class _BaseUpdateFirmware(object):

    @classmethod
    def click_actions_update_firmware(cls, timeout=5):
        logger.debug("select [ Update Firmware ] action button")
        ui_lib.wait_for_element_and_click(GeneralLogicalEnclosureElements.ID_BUTTON_ACTIONS, timeout=timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(GeneralLogicalEnclosureElements.ID_SELECT_ACTION_UPDATE_FIRMWARE, timeout=timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_update_firmware_dialog_open(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Update Firmware ] dialog shown")
        return ui_lib.wait_for_element_visible(UpdateFirmwareElements.ID_DIALOG_UPDATE_FIRMWARE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_update_firmware_dialog_closed(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Update Firmware ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(UpdateFirmwareElements.ID_DIALOG_UPDATE_FIRMWARE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def select_firmware_baseline(cls, firmware_baseline, timeout=5, fail_if_false=True):
        logger.debug("select [ %s ] in [ Firmware Baseline ] option" % firmware_baseline)
        logger.debug("validating test data '%s' for 'Firmware baseline' ..." % firmware_baseline)
        if FusionUIBase.is_test_data_valid(firmware_baseline, 'Firmware_Baseline', fail_if_false=False):
            return FusionUIBase.choose_option_by_text(UpdateFirmwareElements.ID_OPTION_FIRMWARE_BASELINE, firmware_baseline, timeout=timeout, fail_if_false=fail_if_false)
        else:
            msg = "<test data invalid>: '%s' for 'Firmware baseline' is NOT valid" % firmware_baseline
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def select_firmware_update_for(cls, update_firmware_for, timeout=5, fail_if_false=True):
        logger.debug("select [ %s ] in [ Update firmware for ] option" % update_firmware_for)
        return FusionUIBase.choose_option_by_text(UpdateFirmwareElements.ID_OPTION_UPDATE_FIRMWARE_FOR, update_firmware_for, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def select_force_install(cls, timeout=5, fail_if_false=True):
        logger.debug("Selecting [ Force install ]")
        ui_lib.wait_for_checkbox_and_select(UpdateFirmwareElements.ID_CHECKBOX_FIRMWARE_FORCE_INSTALL, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def select_li_activation_method(cls, method, timeout=5, fail_if_false=True):
        logger.debug("Selecting Logical interconnect activation method as [ %s ]" % method)
        if method.lower() == 'orchestrated':
            cls.tick_activation_method_as_orchestrated(timeout=timeout, fail_if_false=fail_if_false)
        elif method.lower() == 'parallel':
            cls.tick_activation_method_as_parallel(timeout=timeout, fail_if_false=fail_if_false)
        else:
            msg = "test data for 'Logical interconnect activation Method' might be wrong: '%s'" % method
            if fail_if_false is True:
                ui_lib.fail_test(msg)
            else:
                logger.warn(msg)
                return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def tick_activation_method_as_orchestrated(cls, timeout=5, fail_if_false=True):
        logger.debug("Set [ Logical interconnect activation ] as [ Orchestrated ]")
        return ui_lib.wait_for_element_and_click(UpdateFirmwareElements.ID_RADIO_ORCHESTRATED, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def tick_activation_method_as_parallel(cls, timeout=5, fail_if_false=True):
        logger.debug("Set [ Logical interconnect activation ] as [ parallel ]")
        return ui_lib.wait_for_element_and_click(UpdateFirmwareElements.ID_RADIO_PARALLEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_expand_all_link(cls, timeout=5):
        logger.debug("Click [ Expand All ] link")
        ui_lib.wait_for_element_and_click(UpdateFirmwareElements.ID_LINK_EXPAND_ALL, timeout=timeout, fail_if_false=True)

    @classmethod
    def click_collapse_all_link(cls, timeout=5):
        logger.debug("Click [ collapse All ] link")
        ui_lib.wait_for_element_and_click(UpdateFirmwareElements.ID_LINK_COLLAPSE_ALL, timeout=timeout, fail_if_false=True)

    @classmethod
    def click_ok_button(cls, timeout=5):
        logger.debug("click [ OK ] button")
        ui_lib.wait_for_element_and_click(UpdateFirmwareElements.ID_BUTTON_OK, timeout=timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(UpdateFirmwareElements.ID_BUTTON_CANCEL, timeout=timeout, fail_if_false=True)


class UpdateFirmware(_BaseUpdateFirmware):
    pass


class C7000UpdateFirmware(UpdateFirmware):
    pass


class TBirdUpdateFirmware(UpdateFirmware):

    """
    This class holds all operation when firmware update is performed on the Logical Enclosure
    """

    @classmethod
    def click_actions(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralLogicalEnclosureElements.ID_BUTTON_ACTIONS, timeout, fail_if_false)

    @classmethod
    def click_update_firmware(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ Update Firmware ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(LogicalEnclosuresUpdateFirmware.ID_BUTTON_UPDATE_FIRMWARE, timeout, fail_if_false)

    @classmethod
    def input_select_update_firmware_baseline(cls, firmware_baseline, timeout=5, fail_if_false=True):
        logger.debug("input and select [ %s ] into [ Firmware Baseline ] text box" % firmware_baseline)
        ui_lib.wait_for_element_and_click(LogicalEnclosuresUpdateFirmware.ID_BUTTON_FIRMWARE_BASELINE, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(LogicalEnclosuresUpdateFirmware.ID_DROPDOWN_FIRMWARE_BASELINE % firmware_baseline, timeout, fail_if_false)

    @classmethod
    def input_select_update_for(cls, update_mode, timeout=5, fail_if_false=True):
        logger.debug("input and select [ %s ] into [ Update mode ] text box" % update_mode)
        ui_lib.wait_for_element_and_click(LogicalEnclosuresUpdateFirmware.ID_BUTTON_UPDATE_FOR % update_mode, timeout, fail_if_false)

    @classmethod
    def input_select_update_option(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ Update Method ] item from [ Firmware dropdown]")
        ui_lib.wait_for_element_and_click(LogicalEnclosuresUpdateFirmware.ID_DROPDOWN_UPDATE_OPTION, timeout, fail_if_false)

    @classmethod
    def click_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Click [ Cancel Button ]")
        ui_lib.wait_for_element_and_click(LogicalEnclosuresUpdateFirmware.ID_BUTTON_CANCEL, timeout, fail_if_false)

    @classmethod
    def click_ok_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Click [ OK Button ]")
        ui_lib.wait_for_element_and_click(LogicalEnclosuresUpdateFirmware.ID_BUTTON_FIRMWARE_UPDATE_OK, timeout, fail_if_false)

    @classmethod
    def tick_unmanaged_checkbox(cls, timeout=5, fail_if_false=True):
        logger.debug("Select [ Unmanaged Checkbox ]")
        ui_lib.wait_for_checkbox_and_select(LogicalEnclosuresUpdateFirmware.ID_CHECKBOX_UNMANAGED_INTERCONNECT, timeout, fail_if_false)

    @classmethod
    def untick_unmanaged_checkbox(cls, timeout=5, fail_if_false=True):
        logger.debug("Deselect [ Unmanaged Checkbox ]")
        ui_lib.wait_for_checkbox_and_unselect(LogicalEnclosuresUpdateFirmware.ID_CHECKBOX_UNMANAGED_INTERCONNECT, timeout, fail_if_false)

    @classmethod
    def tick_forceinstall_checkbox(cls, timeout=5, fail_if_false=True):
        logger.debug("Select [ Force Install Checkbox]")
        ui_lib.wait_for_checkbox_and_select(LogicalEnclosuresUpdateFirmware.ID_BUTTON_FORCE_INSTALL, timeout, fail_if_false)

    @classmethod
    def untick_forceinstall_checkbox(cls, timeout=5, fail_if_false=True):
        logger.debug("Deselect [ Force Install Checkbox ]")
        ui_lib.wait_for_checkbox_and_unselect(LogicalEnclosuresUpdateFirmware.ID_BUTTON_FORCE_INSTALL, timeout, fail_if_false)

    @classmethod
    def input_select_activate_type(cls, activate_type, timeout=5, fail_if_false=True):
        logger.debug("Select [ Activate Type ] as %s ]" % activate_type)
        ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_TEXT_ACTIVATION_CONTENT, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(LogicalEnclosuresUpdateFirmware.ID_BUTTON_ACTIVATION_TYPE % activate_type, timeout, fail_if_false)

    @classmethod
    def get_errors_on_firmwareupdate_dialog(cls, timeout=5, fail_if_false=True):
        logger.debug("Getting Errors on Firmware Update Dialog")
        return FusionUIBase.get_error_message_from_dialog(LogicalEnclosuresUpdateFirmware.ID_DIALOG_FW_UPDATE_FORM, timeout, fail_if_false)

    @classmethod
    def get_firmware_update_step(cls, timeout=5, fail_if_false=True, ):
        logger.debug("Checking for firmware update step")
        return ui_lib.get_text(LogicalEnclosuresUpdateFirmware.ID_UPDATE_STEP, timeout, fail_if_false)

    @classmethod
    def get_server_hardware_list(cls, name, timeout=5):
        logger.debug("Retrieving server hardware list")
        server_hardware_list = []
        server_hardware_elements = []
        s2l = ui_lib.get_s2l()
        server_hardware_elements = s2l._current_browser().find_elements_by_xpath(LogicalEnclosuresUpdateFirmware.ID_TEXT_LE_SERVER_HARDWARE % name)
        try:
            for sh_element in server_hardware_elements:
                server_hardware_list.append(sh_element.text)
        except:
            server_hardware_elements = s2l._current_browser().find_elements_by_xpath(LogicalEnclosuresUpdateFirmware.ID_TEXT_LE_SERVER_HARDWARE % name)
            for sh_element in server_hardware_elements:
                server_hardware_list.append(sh_element.text)
        return server_hardware_list

    @classmethod
    def get_le_activity_state(cls, activity_label, timeout=5, fail_if_false=True):
        logger.debug("Get LE Activity State")
        if ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_TEXT_LE_UPDATE_ACTIVITY % activity_label, timeout, fail_if_false):
            state = ui_lib.get_text(LogicalEnclosuresUpdateFirmware.ID_TEXT_LE_UPDATE_ACTIVITY_STATE % activity_label, timeout, fail_if_false)
            return (True, state)
        else:
            logger.debug("'%s' is not present in Activity page" % activity_label)
            return (False, '')

    @classmethod
    def get_unmanaged_activity_state(cls, timeout=5, fail_if_false=True):
        logger.debug("Getting Unmananged Activity State")
        if ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_TEXT_UNMANAGED_FW_ACTIVITY_STATE, timeout, fail_if_false):
            return ui_lib.get_text(LogicalEnclosuresUpdateFirmware.ID_TEXT_UNMANAGED_FW_ACTIVITY_STATE, timeout, fail_if_false)
        else:
            return None

    @classmethod
    def click_activity_collapser(cls, timeout=5, fail_if_false=True):
        logger.debug("Click [ Activity Collapser  ]")
        ui_lib.wait_for_element_and_click(LogicalEnclosuresUpdateFirmware.ID_TEXT_ACTIVITY_COLLAPSER, timeout, fail_if_false)

    @classmethod
    def get_activity_details(cls, timeout=5, fail_if_false=True):
        logger.debug("Getting Activity details after firmware update")
        ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_TEXT_LE_ACTIVITY_DETAILS, timeout, fail_if_false)
        return ui_lib.get_text(LogicalEnclosuresUpdateFirmware.ID_TEXT_LE_ACTIVITY_DETAILS, timeout, fail_if_false)

    @classmethod
    def get_activity_issue_details(cls, timeout=5, fail_if_false=True):
        logger.debug("Getting Activity issue details after firmware update")
        if ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_TEXT_LE_ACTIVITY_ISSUE, timeout, fail_if_false):
            return ui_lib.get_text(LogicalEnclosuresUpdateFirmware.ID_TEXT_LE_ACTIVITY_ISSUE, timeout, fail_if_false)
        else:
            return None

    @classmethod
    def get_activity_resolution_details(cls, timeout=5, fail_if_false=True):
        logger.debug("Getting Activity resolution details after firmware update")
        if ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_TEXT_LE_ACTIVITY_RESOLUTION, timeout, fail_if_false):
            return ui_lib.get_text(LogicalEnclosuresUpdateFirmware.ID_TEXT_LE_ACTIVITY_RESOLUTION, timeout, fail_if_false)
        else:
            return None

    @classmethod
    def get_em_activity_details(cls, enclosurename, timeout=5, fail_if_false=True):
        logger.debug("Getting EM Activity details after firmware update")
        if ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_TEXT_EM_ACTIVITY_DETAILS % enclosurename, timeout, fail_if_false):
            return ui_lib.get_text(LogicalEnclosuresUpdateFirmware.ID_TEXT_EM_ACTIVITY_DETAILS % enclosurename, timeout, fail_if_false)
        else:
            return None

    @classmethod
    def get_em_activity_issue_details(cls, enclosurename, timeout=5, fail_if_false=True):
        logger.debug("Getting EM Activity issue details after firmware update")
        if ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_TEXT_EM_ACTIVITY_ISSUE % enclosurename, timeout, fail_if_false):
            return ui_lib.get_text(LogicalEnclosuresUpdateFirmware.ID_TEXT_EM_ACTIVITY_ISSUE % enclosurename, timeout, fail_if_false)
        else:
            return None

    @classmethod
    def get_em_activity_resolution_details(cls, enclosurename, timeout=5, fail_if_false=True):
        logger.debug("Getting EM Activity resolution details after firmware update")
        if ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_TEXT_EM_ACTIVITY_RESOLUTION % enclosurename, timeout, fail_if_false):
            return ui_lib.get_text(LogicalEnclosuresUpdateFirmware.ID_TEXT_EM_ACTIVITY_RESOLUTION % enclosurename, timeout, fail_if_false)
        else:
            return None

    @classmethod
    def get_li_sh_activity_details(cls, name, timeout=5, fail_if_false=True):
        logger.debug("Getting LI Activity details after firmware update")
        if ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_TEXT_LI_SH_ACTIVITY % name, timeout, fail_if_false):
            return ui_lib.get_text(LogicalEnclosuresUpdateFirmware.ID_TEXT_LI_SH_ACTIVITY_DESC % name, timeout, fail_if_false)
        else:
            return None

    @classmethod
    def get_unmanaged_activity_details(cls, name, timeout=5, fail_if_false=True):
        logger.debug("Getting Activity  details for unmanaged ICMS after firmware update")
        if ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_TEXT_UNMANAGED_ACTIVITY_DESC % name, timeout, fail_if_false):
            return ui_lib.get_text(LogicalEnclosuresUpdateFirmware.ID_TEXT_UNMANAGED_ACTIVITY_DESC % name, timeout, fail_if_false)
        else:
            return None

    @classmethod
    def get_li_sh_activity_issue_details(cls, name, timeout=5, fail_if_false=True):
        logger.debug("Getting LI Activity issue details after firmware update")
        if ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_TEXT_LI_SH_ISSUE % name, timeout, fail_if_false):
            return ui_lib.get_text(LogicalEnclosuresUpdateFirmware.ID_TEXT_LI_SH_ISSUE % name, timeout, fail_if_false)
        else:
            return None

    @classmethod
    def get_li_sh_activity_resolution_details(cls, name, timeout=5, fail_if_false=True):
        logger.debug("Getting LI Activity resolution details after firmware update")
        if ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_TEXT_LI_SH_RESOLUTION % name, timeout, fail_if_false):
            return ui_lib.get_text(LogicalEnclosuresUpdateFirmware.ID_TEXT_LI_SH_RESOLUTION % name)
        else:
            return None


class TBirdDeleteLogicalEnclosures(object):

    @classmethod
    def select_actions_delete(cls, timeout=5):
        logger.debug("select [ Delete ] action button")
        ui_lib.wait_for_element_and_click(GeneralLogicalEnclosureElements.ID_BUTTON_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(GeneralLogicalEnclosureElements.ID_SELECT_ACTION_DELETE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Delete ] dialog shown")
        return ui_lib.wait_for_element_visible(DeleteLogicalEnclosuresElements.ID_DIALOG_DELETE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Delete ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(DeleteLogicalEnclosuresElements.ID_DIALOG_DELETE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_error_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Delete Error ] dialog shown")
        return ui_lib.wait_for_element_visible(DeleteLogicalEnclosuresElements.ID_DIALOG_DELETE_ERROR, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_error_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Delete Error ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(DeleteLogicalEnclosuresElements.ID_DIALOG_DELETE_ERROR, timeout, fail_if_false)

    @classmethod
    def get_delete_error_text(cls, timeout=5):
        logger.debug("Get error text in delete error dialog")
        return FusionUIBase.get_text(DeleteLogicalEnclosuresElements.ID_TEXT_DELETE_ERROR, timeout, fail_if_false=True)

    @classmethod
    def click_close(cls, timeout=5):
        logger.debug("click [ Delete ] button in delete error dialog")
        ui_lib.wait_for_element_and_click(DeleteLogicalEnclosuresElements.ID_BUTTON_CLOSE, timeout, fail_if_false=True)

    @classmethod
    def click_yes_delete_button(cls, timeout=5):
        logger.debug("click [ Yes, delete ] button in delete dialog")
        ui_lib.wait_for_element_and_click(DeleteLogicalEnclosuresElements.ID_BUTTON_YES_DELETE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_le_show_not_found(cls, lig_name, timeout=5, fail_if_false=True):
        logger.info("wait [ LE %s status ] change to 'not found'" % lig_name)
        return ui_lib.wait_for_element_visible(DeleteLogicalEnclosuresElements.ID_TABLE_LE_DELETED % lig_name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_checkbox_force_remove_logical_enclosure_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait for [ Force delete logical enclosure ] checkbox shown")

        return ui_lib.wait_for_element_visible(DeleteLogicalEnclosuresElements.ID_CHECKBOX_FORCE_REMOVE_LOGICAL_ENCLOSURE, timeout, fail_if_false)

    @classmethod
    def tick_force_remove_logical_enclosure(cls, timeout=5):
        logger.debug("tick [  Force delete logical enclosure ]")
        ui_lib.wait_for_element_and_click(DeleteLogicalEnclosuresElements.ID_CHECKBOX_FORCE_REMOVE_LOGICAL_ENCLOSURE, timeout, fail_if_false=True)


class _BaseReapplyConfiguration(object):

    """
    This class holds all operation when reapply configuration of logical enclosure.
    It also defines abstract methods which the subclass has different implementation for C7000 & TBird
    Add operation is not applicable for TBird enclosure
    """
    @classmethod
    def click_actions_reapply(cls, timeout=5):
        logger.debug("select [ Reapply configuration ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralLogicalEnclosureElements.ID_BUTTON_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(LogicalEnclosuresReapplyConfiguration.ID_ACTION_REAPPLY_CONFIGURATION, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_reapply_logical_enclosure_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Reapply configuration ] dialog shown")
        return ui_lib.wait_for_element_visible(LogicalEnclosuresReapplyConfiguration.ID_DIALOG_REAPPLY_CONFIGURATION_LOGICAL_ENCLOSURE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_reapply_logical_enclosure_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Reapply configuration] dialog disappear")
        return ui_lib.wait_for_element_notvisible(LogicalEnclosuresReapplyConfiguration.ID_DIALOG_REAPPLY_CONFIGURATION_LOGICAL_ENCLOSURE, timeout, fail_if_false)

    @classmethod
    def click_ok_button(cls, timeout=5):
        logger.debug("click [ Yes, reapply ] button")
        ui_lib.wait_for_element_and_click(LogicalEnclosuresReapplyConfiguration.ID_BUTTON_REAPPLY_LOGICAL_ENCLOSURE_CONFIRM, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(LogicalEnclosuresReapplyConfiguration.ID_BUTTON_REAPPLY_LOGICAL_ENCLOSURE_CANCEL, timeout, fail_if_false=True)


class ReapplyConfiguration(_BaseReapplyConfiguration):
    pass


class TBirdReapplyConfiguration(_BaseReapplyConfiguration):

    pass


class C7000ReapplyConfiguration(_BaseReapplyConfiguration):

    pass


class _BaseUpdateFromGroup(object):

    """
    This class holds all operation when Update from Group.
    It also defines abstract methods which the subclass has different implementation for C7000 & TBird
    Add operation is not applicable for TBird enclosure
    """
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_and_click_actions_update(cls, timeout=5, fail_if_false=True):
        logger.debug("select [ Update from Group ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralLogicalEnclosureElements.ID_BUTTON_ACTIONS, timeout, True)
        return ui_lib.wait_for_element_and_click(LogicalEnclosuresUpdateFromGroup.ID_ACTION_UPDATE_FROM_GROUP, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_update_from_group_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Update from Group ] dialog shown")
        return ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFromGroup.ID_DIALOG_UPDATE_FROM_GROUP, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_update_from_group_dialog_disappear(cls, timeout=20, fail_if_false=True):
        logger.debug("wait [ Update from Group ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(LogicalEnclosuresUpdateFromGroup.ID_DIALOG_UPDATE_FROM_GROUP, timeout, fail_if_false)

    @classmethod
    def click_ok_button(cls, timeout=5):
        logger.debug("click [ Yes, update ] button")
        ui_lib.wait_for_element_and_click(LogicalEnclosuresUpdateFromGroup.ID_BUTTON_UPDATE_FROM_GROUP_CONFIRM, timeout, fail_if_false=True)

    @classmethod
    def tick_update_prompt_checkbox(cls, timeout=5):
        logger.debug("tick [ I have read and understand all the implications] checkbox")
        ui_lib.wait_for_element_and_click(LogicalEnclosuresUpdateFromGroup.ID_CHECKBOX_UPDATE_FROM_GROUP_CONFIRM, timeout, fail_if_false=True)

    @classmethod
    def click_confirm_button(cls, timeout=5):
        logger.debug("click [ Yes, update ] button")
        ui_lib.wait_for_element_and_click(LogicalEnclosuresUpdateFromGroup.ID_BUTTON_UPDATE_FROM_GROUP_CONFIRM_AGAIN, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(LogicalEnclosuresUpdateFromGroup.ID_BUTTON_UPDATE_FROM_GROUP_CANCEL, timeout, fail_if_false=True)


class UpdateFromGroup(_BaseUpdateFromGroup):
    pass


class TBirdUpdateFromGroup(_BaseUpdateFromGroup):

    pass


class C7000UpdateFromGroup(_BaseUpdateFromGroup):

    pass


class _BaseCreateSupportDump(object):

    """
    This class holds all operation when create logical enclosure support dump.
    It also defines abstract methods which the subclass has different implementation for C7000 & TBird
    Add operation is not applicable for TBird enclosure
    """
    @classmethod
    def click_actions_create_support_dump(cls, timeout=5):
        logger.debug("select [ Create Logical Enclosure Support Dump ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralLogicalEnclosureElements.ID_BUTTON_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(CreateLogicalEnclosuresSupportDump.ID_ACTION_CREATE_LOGICAL_ENCLOSURE_SUPPORT_DUMP, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_support_dump_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Create Logical Enclosure Support Dump ] dialog shown")
        return ui_lib.wait_for_element_visible(CreateLogicalEnclosuresSupportDump.ID_DIALOG_CREATE_LOGICAL_ENCLOSURE_SUPPORT_DUMP, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_support_dump_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Create Logical Enclosure Support Dump ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(CreateLogicalEnclosuresSupportDump.ID_DIALOG_CREATE_LOGICAL_ENCLOSURE_SUPPORT_DUMP, timeout, fail_if_false)

    @classmethod
    def tick_disable_encryption(cls, timeout=5):
        logger.debug("tick [ Disable support dump encryption ]")
        ui_lib.wait_for_element_and_click(CreateLogicalEnclosuresSupportDump.ID_CHECKBOX_ENABLE_ENCRYPTION, timeout, fail_if_false=True)

    @classmethod
    def click_ok_button(cls, timeout=5):
        logger.debug("click [ OK ] button")
        ui_lib.wait_for_element_and_click(CreateLogicalEnclosuresSupportDump.ID_BUTTON_CREATE_LOGICAL_ENCLOSURE_SUPPORT_DUMP_CONFIRM, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(CreateLogicalEnclosuresSupportDump.ID_BUTTON_CREATE_LOGICAL_ENCLOSURE_SUPPORT_DUMP_CANCEL, timeout, fail_if_false=True)

    pass


class CreateSupportDump(_BaseCreateSupportDump):
    pass


class TBirdCreateSupportDump(_BaseCreateSupportDump):

    pass


class C7000CreateSupportDump(_BaseCreateSupportDump):

    pass


class _BaseEditLogicalEnclosures(object):

    """
    This class holds all operation when add enclosure.
    It also defines abstract methods which the subclass has different implementation for C7000 & TBird
    Add operation is not applicable for TBird enclosure
    """
    pass


class EditLogicalEnclosures(_BaseEditLogicalEnclosures):
    pass


class TBirdEditLogicalEnclosures(_BaseEditLogicalEnclosures):

    @classmethod
    def click_interconnect_bay_licensing_editbutton(cls, timeout=5):
        logger.debug("click IBL [ EDIT ] link")
        FusionUIBase.wait_for_element_and_click(EditLogicalEnclosureElements.ID_INTERCONNECT_BAY_LICENSING_EDITPANEL, timeout, fail_if_false=True)


class C7000EditLogicalEnclosures(_BaseEditLogicalEnclosures):

    @classmethod
    def click_actions_edit(cls, timeout=5):
        logger.debug("select [ Edit ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralLogicalEnclosureElements.ID_BUTTON_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditLogicalEnclosureElements.ID_ACTION_EDIT_LOGICAL_ENCLOSURE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_logical_enclosure_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Edit Logical Enclosure] dialog shown")
        return ui_lib.wait_for_element_visible(EditLogicalEnclosureElements.ID_DIALOG_EDIT_LOGICAL_ENCLOSURE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_logical_enclosure_dialog_disappear(cls, timeout=30, fail_if_false=True):
        logger.debug("wait [ Edit Logical Enclosure] dialog disappear")
        return ui_lib.wait_for_element_notvisible(EditLogicalEnclosureElements.ID_DIALOG_EDIT_LOGICAL_ENCLOSURE, timeout, fail_if_false)

    @classmethod
    def input_logical_enclosure_name(cls, name, timeout=5):
        logger.debug("input [ Logical Enclosure name ] '%s'" % name)
        ui_lib.wait_for_element_and_input_text(EditLogicalEnclosureElements.ID_INPUT_LOGICAL_ENCLOSURE_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def input_configuration_script(cls, script, timeout=5):
        logger.debug("input [ Configuration script ] '%s'" % script)
        ui_lib.wait_for_element_and_input_text(EditLogicalEnclosureElements.ID_INPUT_CONFIG_SCRIPT, script, timeout, fail_if_false=True)

    @classmethod
    def click_ok_button(cls, timeout=5):
        logger.debug("click [ OK ] button")
        ui_lib.wait_for_element_and_click(EditLogicalEnclosureElements.ID_BUTTON_LOGICAL_ENCLOSURE_OK, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(EditLogicalEnclosureElements.ID_BUTTON_LOGICAL_ENCLOSURE_CANCEL, timeout, fail_if_false=True)


class _BaseVerifyLogicalEnclosures(object):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_enclosure_not_exist(cls, logicalenclosure, timeout=10, fail_if_false=True):
        logger.debug("verify [ logical enclosure '%s' ] is not existing" % logicalenclosure)
        return ui_lib.wait_for_element_notvisible(GeneralLogicalEnclosureElements.ID_TABLE_LOGICAL_ENCLOSURE % logicalenclosure, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_enclosure_exist(cls, logicalenclosure, timeout=10, fail_if_false=True):
        logger.debug("verify [ logical enclosure '%s' ] is existing" % logicalenclosure)
        return ui_lib.wait_for_element(GeneralLogicalEnclosureElements.ID_TABLE_LOGICAL_ENCLOSURE % logicalenclosure, timeout, fail_if_false)

    @classmethod
    def click_expand_firmware_detail_button(cls, timeout=5):
        logger.debug("Click [ Expand all ] to verify firmware details")
        return ui_lib.wait_for_element_and_click(GeneralLogicalEnclosureElements.ID_BUTTON_EXPAND_ALL, timeout=timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_server_hardware_uri_by_name(cls, server_name, timeout=5):
        logger.debug("Get server hardware [ %s ] uri" % server_name)
        return ui_lib.get_webelement_attribute("href", GeneralLogicalEnclosureElements.ID_LINK_SERVER_HARDWARE % server_name, timeout=timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_firmware_installed(cls, server_uri, firmware_name, firmware_installed, timeout=5, fail_if_false=False):
        logger.debug("Verify server hardware [ %s ] firmware [ %s ] installed version is [ %s ]" % (server_uri, firmware_name, firmware_installed))
        return ui_lib.wait_for_element(GeneralLogicalEnclosureElements.ID_TEXT_SERVER_FIRMWARE_INSTALLED % (server_uri, firmware_name, firmware_installed), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_firmware_baseline(cls, server_uri, firmware_name, firmware_baseline, timeout=5, fail_if_false=False):
        logger.debug("Verify server hardware [ %s ] firmware [ %s ] baseline version is [ %s ]" % (server_uri, firmware_name, firmware_baseline))
        return ui_lib.wait_for_element(GeneralLogicalEnclosureElements.ID_TEXT_SERVER_FIRMWARE_BASELINE % (server_uri, firmware_name, firmware_baseline), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_common_firmware_installed(cls, name, firmware_installed, timeout=5, fail_if_false=False):
        logger.debug("Verify hardware [ %s ] firmware installed version is [ %s ]" % (name, firmware_installed))
        return ui_lib.wait_for_element(GeneralLogicalEnclosureElements.ID_TEXT_COMMON_FIRMWARE_INSTALLED % (name, firmware_installed), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_common_firmware_baseline(cls, name, firmware_baseline, timeout=5, fail_if_false=False):
        logger.debug("Verify hardware [ %s ] firmware baseline version is [ %s ]" % (name, firmware_baseline))
        return ui_lib.wait_for_element(GeneralLogicalEnclosureElements.ID_TEXT_COMMON_FIRMWARE_BASELINE % (name, firmware_baseline), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_server_hardware_uri_by_name_when_update_firmware(cls, server_name, timeout=5):
        logger.debug("Get server hardware [ %s ] uri" % server_name)
        return ui_lib.get_webelement_attribute("href", UpdateFirmwareElements.ID_LINK_SERVER_HARDWARE % server_name, timeout=timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_firmware_installed_when_update_firmware(cls, server_uri, firmware_name, firmware_installed, timeout=5, fail_if_false=False):
        logger.debug("Verify server hardware [ %s ] firmware [ %s ] installed version is [ %s ]" % (server_uri, firmware_name, firmware_installed))
        return ui_lib.wait_for_element(UpdateFirmwareElements.ID_TEXT_SERVER_FIRMWARE_INSTALLED % (server_uri, firmware_name, firmware_installed), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_server_firmware_baseline_when_update_firmware(cls, server_uri, firmware_name, firmware_baseline, timeout=5, fail_if_false=False):
        logger.debug("Verify server hardware [ %s ] firmware [ %s ] baseline version is [ %s ]" % (server_uri, firmware_name, firmware_baseline))
        return ui_lib.wait_for_element(UpdateFirmwareElements.ID_TEXT_SERVER_FIRMWARE_BASELINE % (server_uri, firmware_name, firmware_baseline), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_common_firmware_installed_when_update_firmware(cls, name, firmware_installed, timeout=5, fail_if_false=False):
        logger.debug("Verify hardware [ %s ] firmware installed version is [ %s ]" % (name, firmware_installed))
        return ui_lib.wait_for_element(UpdateFirmwareElements.ID_TEXT_COMMON_FIRMWARE_INSTALLED % (name, firmware_installed), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_common_firmware_baseline_when_update_firmware(cls, name, firmware_baseline, timeout=5, fail_if_false=False):
        logger.debug("Verify hardware [ %s ] firmware baseline version is [ %s ]" % (name, firmware_baseline))
        return ui_lib.wait_for_element(UpdateFirmwareElements.ID_TEXT_COMMON_FIRMWARE_BASELINE % (name, firmware_baseline), timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_enclosures_exists(cls, timeout=10, fail_if_false=True):
        logger.debug("verify [ logical enclosures is selected")
        return ui_lib.wait_for_element(GeneralLogicalEnclosureElements.ID_LE_TABLE, timeout, fail_if_false)


class VerifyLogicalEnclosures(_BaseVerifyLogicalEnclosures):
    pass


class C7000VerifyLogicalEnclosures(_BaseVerifyLogicalEnclosures):
    pass


class TBirdVerifyLogicalEnclosures(_BaseVerifyLogicalEnclosures):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_le_interconnect_bay_licensing_intent(cls, interconnectname, enclosure, intent, timeout=5, fail_if_false=True):
        logger.debug("\n verify Bay licensing intent for %s", interconnectname)
        return FusionUIBase.verify_element_text("Interconnect Bay Licensing fcLicense Intent", GeneralLogicalEnclosureElements.ID_INTERCONNECT_BAY_LICENSING_INTENT % (interconnectname, enclosure), intent, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_le_interconnect_bay_licensing_icm_bay(cls, interconnectname, enclosure, bay, timeout=5, fail_if_false=True):
        logger.debug("\n verify Bay number for licensed for  %s", interconnectname)
        return FusionUIBase.verify_element_text("Interconnect Bay Licensing ICM bay ", GeneralLogicalEnclosureElements.ID_INTERCONNECT_BAY_LICENSING_ICM_BAY % (interconnectname, enclosure), bay, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_le_interconnect_bay_licensing_li(cls, interconnectname, enclosure, logicalinterconnect, timeout=5, fail_if_false=True):
        logger.debug("verify interconnect bay licensing logical interconnect for  %s", interconnectname)
        return FusionUIBase.verify_element_text("Interconnect Bay Licensing logical interconnect", GeneralLogicalEnclosureElements.ID_INTERCONNECT_BAY_LICENSING_LI % (interconnectname, enclosure), logicalinterconnect, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_enclosure_consistency_state(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("Verify [ logical enclosure consistency state ] is %s" % expect_value)
        locator = GeneralLogicalEnclosureElements.ID_TEXT_LE_CONSISTENCY_STATE
        item_name = "Logical enclosure consistency state"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_logical_enclosure_warning_message(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("Verify [ logical enclosure warning message ] is %s" % expect_value)
        locator = GeneralLogicalEnclosureElements.ID_TEXT_ACTIVITY_WARN_MESSAGE
        item_name = "Logical enclosure warning message"
        ui_lib.wait_for_element_text_match(locator=locator, regex=expect_value, timeout=timeout, fail_if_false=False)
        return FusionUIBase.verify_element_text(item_name=item_name, locator=locator, expect_value=expect_value, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_le_interconnect_bay_licensing_editpanel_Baydata(cls, enclosure, bay, timeout=5, fail_if_false=True):
        logger.debug("Get interconnect bay licensing row data for given Bay %s under given enclosure", bay)
        return FusionUIBase.get_text(GeneralLogicalEnclosureElements.ID_INTERCONNECT_BAY_LICENSING_EDITPANEL_BAYDATA % (enclosure, bay), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def toggle_le_interconnect_bay_licensing_editpanel_intent(cls, enclosure, bay, timeout=5, fail_if_false=True):
        logger.debug("Toggle ibl editpanel Potassium intent button")
        FusionUIBase.wait_for_element_and_click(GeneralLogicalEnclosureElements.ID_INTERCONNECT_BAY_LICENSING_EDITPANEL_INTENT_TOGGLE % (enclosure, bay), timeout, fail_if_false)

    @classmethod
    def click_le_interconnect_bay_licensing_editpanel_ok_button(cls, timeout=5):
        logger.debug("click ibl editpanel [ OK ] button")
        FusionUIBase.wait_for_element_and_click(GeneralLogicalEnclosureElements.ID_INTERCONNECT_BAY_LICENSING_EDITPANEL_OK, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_le_interconnect_bay_licensing_editpanel_ok_button_invisible(cls, timeout=5):
        logger.debug("wait for ibl editpanel [ OK ] button to dissappear")
        return ui_lib.wait_for_element_notvisible(GeneralLogicalEnclosureElements.ID_INTERCONNECT_BAY_LICENSING_EDITPANEL_OK, timeout, fail_if_false=True)

    @classmethod
    def click_le_interconnect_bay_licensing_editpanel_cancel_button(cls, timeout=5):
        logger.debug("click ibl editpanel [ Cancel ] button")
        FusionUIBase.wait_for_element_and_click(GeneralLogicalEnclosureElements.ID_INTERCONNECT_BAY_LICENSING_EDITPANEL_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_le_consistency_state(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ LE consistency state ] in overview")
        return FusionUIBase.verify_element_text("LE consistency", GeneralLogicalEnclosureElements.ID_TEXT_LE_CONSISTENCY_STATE, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_updatefirmware_button_exists(cls, timeout=5, fail_if_false=True):
        logger.debug("Check [ Update Firmware ] is available in [ Action ] menu")
        return ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_BUTTON_UPDATE_FIRMWARE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_action_button_exists(cls, timeout=5, fail_if_false=True):
        logger.debug("Check [ Action Button Firmware ]is available")
        return ui_lib.wait_for_element_visible(GeneralLogicalEnclosureElements.ID_BUTTON_ACTIONS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_force_install_warning(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking for Force install warning message")
        warning_msg = ui_lib.get_text(LogicalEnclosuresUpdateFirmware.ID_TEXT_WARNING_FORCE_INSTALL, timeout, fail_if_false)
        logger.debug("[ Warning Text ] is %s" % warning_msg)
        return ui_lib.wait_for_element_text(LogicalEnclosuresUpdateFirmware.ID_TEXT_WARNING_FORCE_INSTALL, LogicalEnclosuresUpdateFirmware.ID_TEXT_FW_DOWNGRADE_WARNING_MSG, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_parallel_activation_warning(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking for Parallel activation warning message")
        warning_msg = ui_lib.get_text(LogicalEnclosuresUpdateFirmware.ID_TEXT_WARNING_PARALLEL, timeout, fail_if_false)
        logger.debug("[ Warning Text ] is %s" % warning_msg)
        return ui_lib.wait_for_element_text(LogicalEnclosuresUpdateFirmware.ID_TEXT_WARNING_PARALLEL, LogicalEnclosuresUpdateFirmware.ID_TEXT_PARALLEL_ACTIVATION_WARNING_MSG, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_orchestrated_activation_warning(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking for Orchestrated activation warning message")
        warning_msg = ui_lib.get_text(LogicalEnclosuresUpdateFirmware.ID_TEXT_WARNING_ORCHESTRATED, timeout, fail_if_false)
        logger.debug("[ Warning Text ] is %s" % warning_msg)
        return ui_lib.wait_for_element_text(LogicalEnclosuresUpdateFirmware.ID_TEXT_WARNING_ORCHESTRATED, LogicalEnclosuresUpdateFirmware.ID_TEXT_ORCHESTRATED_ACTIVATION_WARNING_MSG, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_update_form_not_visible(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking for Update form not visible")
        return ui_lib.wait_for_element_notvisible(LogicalEnclosuresUpdateFirmware.ID_DIALOG_FW_UPDATE_FORM, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_error_on_update_form(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking for Error status")
        return ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_TEXT_FW_UPDATE_HP_STATUS_ERROR, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_firmware_update_warning(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking for Warning status")
        return ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_TEXT_UPDATE_STATUS_WARNING, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_firmware_update_error(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking for Error status")
        return ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_TEXT_UPDATE_STATUS_ERROR, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_firmware_update_complete(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking for Complete status")
        return ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_TEXT_UPDATE_STATUS_COMPLETE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_firmware_update_step(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking for firmware update step")
        return ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_TEXT_UPDATE_STEP, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_li_sh_activity(cls, name, timeout=5, fail_if_false=True):
        logger.debug("Checking for LI server hardware Activity being displayed ]")
        return ui_lib.wait_for_element_visible(LogicalEnclosuresUpdateFirmware.ID_TEXT_LI_SH_ACTIVITY % name, timeout, fail_if_false)

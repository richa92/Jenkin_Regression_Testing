import time
from datetime import datetime
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco, FusionUIBase
from FusionLibrary.ui.business_logic.servers.serverhardwaretypes_elements import GeneralServerHardwareTypeElements, \
    EditServerHardwareTypeElements, DeleteServerHardwareTypeElements


class CommonOperationServerHardwareType(object):

    @classmethod
    def get_sht_list(cls, timeout=5):
        logger.debug("Get all [ Server hardware type names ] from table")
        sht_name_list = []
        if ui_lib.wait_for_element(GeneralServerHardwareTypeElements.ID_TABLE_SHTS):
            sht_name_list = FusionUIBase.get_multi_elements_text(GeneralServerHardwareTypeElements.ID_TABLE_SHTS, timeout, fail_if_false=True, hidden_element=True)
        return sht_name_list

    @classmethod
    def click_sht(cls, hardware_type, timeout=5):
        logger.debug("select [ Server hardware type '%s' ]" % hardware_type)
        locator = GeneralServerHardwareTypeElements.ID_TABLE_SHT % hardware_type
        ui_lib.scroll_into_view(locator)
        ui_lib.wait_for_element_and_click(locator, timeout, fail_if_false=True)

    @classmethod
    def click_used_by_server_hardware(cls, timeout=5):
        logger.debug("click [ Used by Server Hardware ] link")
        return ui_lib.wait_for_element_and_click(GeneralServerHardwareTypeElements.ID_TEXT_GENERAL_USED_BY_SH, timeout, fail_if_false=True)

    @classmethod
    def click_used_by_server_profile(cls, timeout=5):
        logger.debug("click [ Used by Server Hardware ] link")
        return ui_lib.wait_for_element_and_click(GeneralServerHardwareTypeElements.ID_TEXT_GENERAL_USED_BY_SP, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_sht_selected(cls, hardware_type, timeout=5, fail_if_false=True):
        logger.debug("wait [ Server hardware type '%s' ] selected" % hardware_type)
        locator = GeneralServerHardwareTypeElements.ID_TABLE_SHT_SELECTED % hardware_type
        ui_lib.scroll_into_view(locator)
        return ui_lib.wait_for_element_visible(locator, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_sht_title_display(cls, hardware_type, timeout=5, fail_if_false=True):
        logger.debug("wait [ Server hardware type '%s' ] title display" % hardware_type)
        locator = GeneralServerHardwareTypeElements.ID_TEXT_SHT_TITLE
        return ui_lib.wait_for_element_text(locator, hardware_type, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_sht_details_load_completed(cls, hardware_type, timeout=5, fail_if_false=True):
        logger.debug("wait [ Server hardware type '%s' ] details load completed" % hardware_type)
        return ui_lib.wait_for_element_visible(GeneralServerHardwareTypeElements.ID_TEXT_DETAILS_STATUS_OK, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_activity_action_ok(cls, hardware_type, action_name, timeout=30, fail_if_false=True):
        logger.debug("waiting [ activity action of Server hardware type '%s' ] change to ok" % hardware_type)
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element(GeneralServerHardwareTypeElements.ID_TEXT_ACTIVITY_ACTION_OK % (hardware_type, action_name), timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralServerHardwareTypeElements.ID_TEXT_ACTIVITY_ACTION_TITLE % hardware_type)
                logger.debug("[ activity action '%s' status ] is ok as expected." % actionname)
                return True
            elif ui_lib.wait_for_element(GeneralServerHardwareTypeElements.ID_TEXT_ACTIVITY_ACTION_WARN % (hardware_type, action_name), timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralServerHardwareTypeElements.ID_TEXT_ACTIVITY_ACTION_TITLE % hardware_type)
                logger.debug("[ activity action '%s' status ] is warn not as expected." % actionname)
                ui_lib.wait_for_element_and_click(GeneralServerHardwareTypeElements.ID_TEXT_ACTIVITY_ACTION_WARN % (hardware_type, action_name))
                msg = FusionUIBase.get_multi_elements_text(GeneralServerHardwareTypeElements.ID_TEXT_ACTIVITY_MESSAGE)
                msg = [s for s in msg if msg != ''][0]
                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            elif ui_lib.wait_for_element(GeneralServerHardwareTypeElements.ID_TEXT_ACTIVITY_ACTION_ERROR % (hardware_type, action_name), timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralServerHardwareTypeElements.ID_TEXT_ACTIVITY_ACTION_TITLE % hardware_type)
                logger.debug("[ activity action '%s' status ] is error not as expected." % actionname)
                ui_lib.wait_for_element_and_click(GeneralServerHardwareTypeElements.ID_TEXT_ACTIVITY_ACTION_ERROR % (hardware_type, action_name))
                msg = FusionUIBase.get_multi_elements_text(GeneralServerHardwareTypeElements.ID_TEXT_ACTIVITY_MESSAGE)
                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            else:
                if ui_lib.wait_for_element(GeneralServerHardwareTypeElements.ID_TEXT_ACTIVITY_ACTION_TITLE % hardware_type):
                    actionname = FusionUIBase.get_text(GeneralServerHardwareTypeElements.ID_TEXT_ACTIVITY_ACTION_TITLE % hardware_type)
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


class EditServerHardwareType(object):

    @classmethod
    def select_actions_edit(cls, timeout=5):
        logger.debug("select [ Edit ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralServerHardwareTypeElements.ID_BUTTON_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditServerHardwareTypeElements.ID_SELECT_ACTION_EDIT, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_sht_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Edit server hardware type ] dialog shown")
        return ui_lib.wait_for_element_visible(EditServerHardwareTypeElements.ID_DIALOG_EDIT_SHT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_sht_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Edit server hardware type ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(EditServerHardwareTypeElements.ID_DIALOG_EDIT_SHT, timeout, fail_if_false)

    @classmethod
    def input_name(cls, sht_name, timeout=5):
        logger.debug("input [ %s ] into [ Name ] textbox" % sht_name)
        ui_lib.wait_for_element_and_input_text(EditServerHardwareTypeElements.ID_INPUT_NAME, sht_name, timeout, fail_if_false=True)

    @classmethod
    def input_description(cls, sht_desc, timeout=5):
        logger.debug("input [ %s ] into [ Description ] textbox" % sht_desc)
        ui_lib.wait_for_element_and_input_text(EditServerHardwareTypeElements.ID_INPUT_DESCRIPTION, sht_desc, timeout, fail_if_false=True)

    @classmethod
    def click_ok_button(cls, timeout=5):
        logger.debug("click [ OK ] button")
        ui_lib.wait_for_element_and_click(EditServerHardwareTypeElements.ID_BUTTON_OK, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(EditServerHardwareTypeElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)


class DeleteServerHardwareType(object):

    @classmethod
    def select_actions_delete(cls, timeout=5):
        logger.debug("select [ Delete ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralServerHardwareTypeElements.ID_BUTTON_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(DeleteServerHardwareTypeElements.ID_SELECT_ACTION_DELETE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Delete server hardware type ] dialog shown")
        return ui_lib.wait_for_element_visible(DeleteServerHardwareTypeElements.ID_DIALOG_DELETE_SHT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Delete server hardware type ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(DeleteServerHardwareTypeElements.ID_DIALOG_DELETE_SHT, timeout, fail_if_false)

    @classmethod
    def click_yes_delete_button(cls, timeout=5):
        logger.debug("click [ Yes, delete ] button")
        ui_lib.wait_for_element_and_click(DeleteServerHardwareTypeElements.ID_BUTTON_YES_DELETE, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(DeleteServerHardwareTypeElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_error_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ delete server hardware type error dialog ] shown")
        return ui_lib.wait_for_element_visible(DeleteServerHardwareTypeElements.ID_DIALOG_DELETE_ERROR, timeout, fail_if_false)

    @classmethod
    def get_delete_error_text(cls, timeout=5):
        logger.debug("get error text in delete error dialog")
        return FusionUIBase.get_text(DeleteServerHardwareTypeElements.ID_TEXT_DELETE_ERROR, timeout, fail_if_false=True)

    @classmethod
    def click_close(cls, timeout=5):
        logger.debug("click [ Close ] button in delete error dialog")
        ui_lib.wait_for_element_and_click(DeleteServerHardwareTypeElements.ID_BUTTON_CLOSE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_error_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ delete server hardware type error dialog ] disappear")
        return ui_lib.wait_for_element_notvisible(DeleteServerHardwareTypeElements.ID_DIALOG_DELETE_ERROR, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_sht_show_not_found(cls, sht_name, timeout=5, fail_if_false=True):
        logger.info("wait [ server hardware type '%s' status ] change to 'not found'" % sht_name)
        return ui_lib.wait_for_element_visible(GeneralServerHardwareTypeElements.ID_TABLE_SHT_DELETED % sht_name, timeout, fail_if_false)


class VerifyServerHardwareType(object):

    # { General verification
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_sht_not_exist(cls, hardware_type, timeout=10, fail_if_false=True):
        logger.debug("verify [ Server hardware type '%s' ] is not existing" % hardware_type)
        locator = GeneralServerHardwareTypeElements.ID_TABLE_SHT % hardware_type
        ui_lib.scroll_into_view(locator)
        if ui_lib.wait_for_element_notvisible(locator, timeout, fail_if_false):
            return True
        else:
            logger.warn("failed to wait for server hardware type '%s' to be invisible within %s second(s)" % (hardware_type, timeout))
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_sht_exist(cls, hardware_type, timeout=10, fail_if_false=True):
        logger.debug("verify [ Server hardware type '%s' ] is existing" % hardware_type)
        locator = GeneralServerHardwareTypeElements.ID_TABLE_SHT % hardware_type
        ui_lib.scroll_into_view(locator)
        if ui_lib.wait_for_element_visible(locator, timeout, fail_if_false):
            return True
        else:
            logger.warn("failed to wait for server hardware type '%s' to be visible within %s second(s)" % (hardware_type, timeout))
            return False
    # }

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_server_model(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Server model ] in general view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Server model", GeneralServerHardwareTypeElements.ID_TEXT_GENERAL_SERVER_MODEL, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_form_factor(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Form factor ] in general view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Form factor", GeneralServerHardwareTypeElements.ID_TEXT_GENERAL_FORM_FACTOR, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_description(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Description ] in general view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Description", GeneralServerHardwareTypeElements.ID_TEXT_GENERAL_DESCRIPTION, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_used_by(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Used by ] in general view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Used by", GeneralServerHardwareTypeElements.ID_TEXT_GENERAL_USED_BY, expect_value, timeout, fail_if_false)

    # adapter information verification
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_adapter_location_exist(cls, location, timeout=5, fail_if_false=True):
        logger.debug("verify [ location '%s' ] exist in adapter view" % location)
        return ui_lib.wait_for_element_visible(GeneralServerHardwareTypeElements.ID_TEXT_ADAPTERS_ROW_LOCATION % location, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_adapter_model(cls, location, expect_value=None, timeout=5, fail_if_false=True):
        logger.debug("verify model of [ location '%s' ] in adapter view, expect value is [ %s ]" % (location, expect_value))
        return FusionUIBase.verify_element_text("Adapter model", GeneralServerHardwareTypeElements.ID_TEXT_ADAPTERS_ROW_MODEL % location, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_adapter_device_type(cls, location, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify device type of [ location '%s' ] in adapter view, expect value is [ %s ]" % (location, expect_value))
        return FusionUIBase.verify_element_text("Adapter device type", GeneralServerHardwareTypeElements.ID_TEXT_ADAPTERS_ROW_DEVICE_TYPE % location, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_adapter_max_port_speed(cls, location, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify max port speed of [ location '%s' ] in adapter view, expect value is [ %s ]" % (location, expect_value))
        return FusionUIBase.verify_element_text("Adapter max port speed", GeneralServerHardwareTypeElements.ID_TEXT_ADAPTERS_ROW_MAX_PORT_SPEED % location, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_adapter_physical_port(cls, location, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify physical port of [ location '%s' ] in adapter view, expect value is [ %s ]" % (location, expect_value))
        return FusionUIBase.verify_element_text("Adapter physical port", GeneralServerHardwareTypeElements.ID_TEXT_ADAPTERS_ROW_PHYSICAL_PORTS % location, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_adapter_virtual_ports(cls, location, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify virtual ports of [ location '%s' ] in adapter view, expect value is [ %s ]" % (location, expect_value))
        return FusionUIBase.verify_element_text("Adapter virtual ports", GeneralServerHardwareTypeElements.ID_TEXT_ADAPTERS_ROW_VIRTUAL_PORTS % location, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_adapter_available_virtual_functions(cls, location, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify available virtual functions of [ location '%s' ] in adapter view, expect value is [ %s ]" % (location, expect_value))
        return FusionUIBase.verify_element_text("Adapter available virtual functions", GeneralServerHardwareTypeElements.ID_TEXT_ADAPTERS_ROW_AVAILABLE_VIRTUAL_FUNCTIONS % location, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_adapter_virtual_function_allocation_increment(cls, location, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify virtual function allocation increment of [ location '%s' ] in adapter view, expect value is [ %s ]" % (location, expect_value))
        return FusionUIBase.verify_element_text("Adapter virtual function allocation increment", GeneralServerHardwareTypeElements.ID_TEXT_ADAPTERS_ROW_VIRTUAL_FUNCTION_ALLOCATION_INCREMENT % location, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_adapter_ethernet(cls, location, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify ethernet of [ location '%s' ] in adapter view, expect value is [ %s ]" % (location, expect_value))
        return FusionUIBase.verify_element_text("Adapter ethernet", GeneralServerHardwareTypeElements.ID_TEXT_ADAPTERS_ROW_ETHERNET % location, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_adapter_fc(cls, location, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify fc of [ location '%s' ] in adapter view, expect value is [ %s ]" % (location, expect_value))
        return FusionUIBase.verify_element_text("Adapter fc", GeneralServerHardwareTypeElements.ID_TEXT_ADAPTERS_ROW_FC % location, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_adapter_iscsi(cls, location, expect_value, timeout=5):
        logger.info(
            "verify iSCSI of [ location '%s' ] in adapter view, expect value is [ %s ]" % (location, expect_value))
        return FusionUIBase.verify_element_text("Adapter iSCSI",
                                                GeneralServerHardwareTypeElements.ID_TEXT_ADAPTERS_ROW_ISCSI % location,
                                                expect_value, timeout, True)

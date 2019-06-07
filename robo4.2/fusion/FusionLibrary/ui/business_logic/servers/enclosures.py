from datetime import datetime
import time
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.base import FusionUIBase, \
    TakeScreenShotWhenReturnFalseDeco
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.servers.enclosures_elements import AddEnclosuresElements, \
    ReapplyEnclosuresElements, RefreshEnclosuresElements
from FusionLibrary.ui.business_logic.servers.enclosures_elements import EditEnclosuresElements
from FusionLibrary.ui.business_logic.servers.enclosures_elements import RemoveEnclosuresElements
from FusionLibrary.ui.business_logic.servers.enclosures_elements import GeneralEnclosuresElements
from FusionLibrary.ui.business_logic.servers.enclosures_elements import EditScopeElements
from FusionLibrary.ui.business_logic.servers.enclosures_elements import *


class _BaseCommonOperationEnclosures(object):

    """
    This class holds all common operation of enclosure
    It also defines abstract methods which the subclass has different implementation for C7000 & TBird
    """

    @classmethod
    def wait_for_activity_control_new_count(cls, timeout=5, fail_if_false=True):
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_ACTIVITY_CONTROL_NEW_COUNT, timeout, fail_if_false)

    @classmethod
    def get_enclosure_list(cls, timeout):
        logger.debug("Get all [ enclosure names ] from table")
        enclosure_name_list = []
        if ui_lib.wait_for_element(GeneralEnclosuresElements.ID_TABLE_ENCLOSURES):
            enclosure_name_list = FusionUIBase.get_multi_elements_text(GeneralEnclosuresElements.ID_TABLE_ENCLOSURES, timeout, fail_if_false=True)
        return enclosure_name_list

    @classmethod
    def click_enclosure(cls, enclosure, timeout=5):
        logger.debug("select [ enclosure '%s' ]" % enclosure)
        ui_lib.wait_for_element_and_click(GeneralEnclosuresElements.ID_TABLE_ENCLOSURE % enclosure, timeout, fail_if_false=True)

    @classmethod
    def click_action_button(cls, timeout=5):
        logger.debug("Click [ Action ] button on enclosure list page")
        ui_lib.wait_for_element_and_click(GeneralEnclosuresElements.ID_BUTTON_ACTIONS, timeout, fail_if_false=True)

    @classmethod
    def click_interconnect_interconnect(cls, bay_no, timeout=5, fail_if_false=True):
        logger.debug("click bay '%s' in interconnect view" % bay_no)
        ui_lib.wait_for_element_and_click(GeneralEnclosuresElements.ID_TEXT_INTERCONNECTS_ROW_INTERCONNECT % bay_no, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_enclosure_selected(cls, enclosure, timeout=5, fail_if_false=True):
        logger.debug("wait [ enclosure '%s' ] selected" % enclosure)
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TABLE_ENCLOSURE_SELECTED % enclosure, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_enclosure_status_ok(cls, enclosure, timeout=10, fail_if_false=True):
        start = datetime.now()
        logger.debug("waiting [ enclosure '%s' status ] change to ok" % enclosure)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_STATUS_ENCLOSURE_OK % enclosure, timeout=2, fail_if_false=False):
                logger.debug("[ enclosure '%s' status ] is ok as expected." % enclosure)
                return True
            elif ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_STATUS_ENCLOSURE_WARN % enclosure, timeout=2, fail_if_false=False):
                warn_msg = "[ enclosure '%s' status ] is warning not as expected." % enclosure
                if fail_if_false is False:
                    logger.warn(warn_msg)
                    return False
                else:
                    ui_lib.fail_test(warn_msg)
            elif ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_STATUS_ENCLOSURE_ERROR % enclosure, timeout=2, fail_if_false=False):
                err_msg = "[ enclosure system '%s' status ] is error not as expected." % enclosure
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            else:
                logger.debug("[ enclosure status ] is unknown, waiting ...")
                continue
        err_msg = "Timeout to waiting [ enclosure '%s' status ] change to ok." % enclosure
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_enclosure_status_ok_or_warn(cls, enclosure, timeout=10, fail_if_false=True):
        start = datetime.now()
        logger.debug("waiting [ enclosure '%s' status ] change to ok or warning" % enclosure)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_STATUS_ENCLOSURE_OK % enclosure, timeout=5, fail_if_false=False):
                logger.debug("[ enclosure '%s' status ] is ok as expected." % enclosure)
                return True
            elif ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_STATUS_ENCLOSURE_WARN % enclosure, timeout=5, fail_if_false=False):
                logger.debug("[ enclosure '%s' status ] is warning as expected." % enclosure)
                return True
            elif ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_STATUS_ENCLOSURE_ERROR % enclosure, timeout=5, fail_if_false=False):
                err_msg = "[ enclosure '%s' status ] is error not as expected." % enclosure
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            else:
                logger.debug("[ enclosure '%s' status ] is unknown, waiting ..." % enclosure)
                continue
        err_msg = "Timeout to waiting [ enclosure '%s' status ] change to ok or warn." % enclosure
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_enclosure_status_error(cls, enclosure, timeout=10, fail_if_false=True):
        start = datetime.now()
        logger.debug("waiting [ enclosure '%s' status ] change to error" % enclosure)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_STATUS_ENCLOSURE_OK % enclosure, timeout=5, fail_if_false=False):
                err_msg = "[ enclosure '%s' status ] is ok not as expected." % enclosure
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            elif ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_STATUS_ENCLOSURE_WARN % enclosure, timeout=5, fail_if_false=False):
                logger.debug("[ enclosure '%s' status ] is warning not as expected." % enclosure)
                return False
            elif ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_STATUS_ENCLOSURE_ERROR % enclosure, timeout=5, fail_if_false=False):
                logger.debug("[ enclosure '%s' status ] is error as expected." % enclosure)
                return True
            else:
                logger.debug("[ enclosure '%s' status ] is unknown, waiting ..." % enclosure)
                continue
        err_msg = "Timeout to [ waiting enclosure status ] change to error."
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_activity_action_ok(cls, enclosure, action_name, timeout=600, fail_if_false=True):
        """ wait specific enclosure operation turn to OK state in right activity panel, be sure to open the right activity panel first

        :param enclosure: enclosure name
        :param action_name:  which action you are interested. E.g. Add, Update, Remove, Refresh
        :param timeout:
        :param fail_if_false:
        :return:
        """
        logger.debug("waiting [ activity action of enclosure '%s' ] change to ok" % enclosure)
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element(GeneralEnclosuresElements.ID_TEXT_ACTIVITY_ACTION_OK % (enclosure, action_name), timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralEnclosuresElements.ID_TEXT_ACTIVITY_ACTION_TITLE % enclosure)
                logger.debug("[ activity action '%s' status ] is ok as expected." % actionname)
                return True
            elif ui_lib.wait_for_element(GeneralEnclosuresElements.ID_TEXT_ACTIVITY_ACTION_WARN % (enclosure, action_name), timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralEnclosuresElements.ID_TEXT_ACTIVITY_ACTION_TITLE % enclosure)
                logger.debug("[ activity action '%s' status ] is warn not as expected." % actionname)
                ui_lib.wait_for_element_and_click(GeneralEnclosuresElements.ID_TEXT_ACTIVITY_ACTION_WARN % (enclosure, action_name))
                msg = FusionUIBase.get_multi_elements_text(GeneralEnclosuresElements.ID_TEXT_ACTIVITY_MESSAGE)
                msg = ''.join(msg)
                # bypass specific warning message when delete monitored enclosure
                if 'Resolution Delete the HPOneViewMonitor user manually on Onboard Administrator.' in msg:
                    logger.debug("warning message [ %s ] is expected after deleting monitored enclosure." % msg)
                    return True

                if 'Experienced problems refreshing the following server hardware' in msg:
                    logger.warn("get warning message [ %s ]. Maybe this is caused by hardware unstable." % msg)
                    return True

                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            elif ui_lib.wait_for_element(GeneralEnclosuresElements.ID_TEXT_ACTIVITY_ACTION_ERROR % (enclosure, action_name), timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralEnclosuresElements.ID_TEXT_ACTIVITY_ACTION_TITLE % enclosure)
                logger.debug("[ activity action '%s' status ] is error not as expected." % actionname)
                ui_lib.wait_for_element_and_click(GeneralEnclosuresElements.ID_TEXT_ACTIVITY_ACTION_ERROR % (enclosure, action_name))
                msg = FusionUIBase.get_multi_elements_text(GeneralEnclosuresElements.ID_TEXT_ACTIVITY_MESSAGE)
                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            else:
                if ui_lib.wait_for_element(GeneralEnclosuresElements.ID_TEXT_ACTIVITY_ACTION_TITLE % enclosure):
                    actionname = FusionUIBase.get_text(GeneralEnclosuresElements.ID_TEXT_ACTIVITY_ACTION_TITLE % enclosure)
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
    def click_uid_light(cls, timeout=5):
        logger.debug("click [ UID Light ] icon")
        ui_lib.wait_for_element_and_click(GeneralEnclosuresElements.ID_BUTTON_UID_LIGHT, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uid_light_on(cls, timeout=60, fail_if_false=True):
        logger.debug("verify [ UID Light ] in on state")
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_STATUS_UID_LIGHT_ON, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_uid_light_off(cls, timeout=60, fail_if_false=True):
        logger.debug("verify [ UID Light ] in off state")
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_STATUS_UID_LIGHT_OFF, timeout, fail_if_false)

    @classmethod
    def click_activity_collapser(cls, activity_name, timeout=10, fail_if_false=True):
        logger.debug("click to expand activity '%s'" % activity_name)
        ui_lib.wait_for_element_and_click(GeneralEnclosuresElements.ID_ICON_ACTIVITY_COLLAPSER % activity_name, timeout=timeout, fail_if_false=fail_if_false)


class C7000CommonOperationEnclosures(_BaseCommonOperationEnclosures):
    pass


class TBirdCommonOperationEnclosures(_BaseCommonOperationEnclosures):
    pass


class _BaseAddEnclosures(object):

    """
    This class holds all operation when add enclosure.
    It also defines abstract methods which the subclass has different implementation for C7000 & TBird
    Add operation is not applicable for TBird enclosure
    """
    pass


class C7000AddEnclosures(_BaseAddEnclosures):

    @classmethod
    def click_add_enclosure_button(cls, timeout=5):
        logger.debug("click [ Add enclosure ] button")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_ADD_ENCLOSURE, timeout, fail_if_false=True)

    @classmethod
    def select_actions_add(cls, timeout=5):
        logger.debug("select [ Add ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralEnclosuresElements.ID_BUTTON_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_SELECT_ACTION_ADD, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_enclosure_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add Enclosure ] dialog shown")
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_DIALOG_ADD_ENCLOSURE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_enclosure_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Add Enclosure ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(AddEnclosuresElements.ID_DIALOG_ADD_ENCLOSURE, timeout, fail_if_false)

    @classmethod
    def tick_action_add_enclosure_for_management(cls, timeout=5):
        logger.debug("tick [ Action ] 'Add enclosure for management'")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_RADIO_ADD_ENCLOSURE_FOR_MANAGEMENT, timeout, fail_if_false=True)

    @classmethod
    def tick_action_add_enclosure_for_monitoring(cls, timeout=5):
        logger.debug("tick [ Action] 'Add enclosure for monitoring'")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_RADIO_ADD_ENCLOSURE_FOR_MONITORING, timeout, fail_if_false=True)

    @classmethod
    def tick_action_migrate_virtual_connect_domain(cls, timeout=5):
        logger.debug("tick [ Action ] 'Migrate Virtual Connect domain'")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_RADIO_MIGRATE_VIRTUAL_CONNECT_DOMAIN, timeout, fail_if_false=True)

    @classmethod
    def tick_force_add_enclosure(cls, timeout=5):
        logger.debug("tick [ Force add enclosure ]")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_CHECKBOX_FORCE_ADD_ENCLOSURE, timeout, fail_if_false=True)

    @classmethod
    def input_oa_ip_address_or_host_name(cls, host, timeout=5):
        logger.debug("input [ OA IP address or host name ] '%s'" % host)
        ui_lib.wait_for_element_and_input_text(AddEnclosuresElements.ID_INPUT_OA_IP_ADDRESS_OR_HOST_NAME, host, timeout, fail_if_false=True)

    @classmethod
    def input_user_name(cls, username, timeout=5):
        logger.debug("input [ User name ] '%s'" % username)
        ui_lib.wait_for_element_and_input_text(AddEnclosuresElements.ID_INPUT_USER_NAME, username, timeout, fail_if_false=True)

    @classmethod
    def input_password(cls, password, timeout=5):
        logger.debug("input [ Password ] '%s'" % password)
        ui_lib.wait_for_element_and_input_text(AddEnclosuresElements.ID_INPUT_PASSWORD, password, timeout, fail_if_false=True)

    @classmethod
    def input_select_enclosure_group(cls, enclosure_group, timeout=5):
        logger.debug("input and select [ Enclosure group ] '%s'" % enclosure_group)
        FusionUIBase.choose_combo_option_by_text(AddEnclosuresElements.ID_COMBO_ENCLOSURE_GROUP, enclosure_group, timeout_sec=timeout, locator=None, fail_if_false=True)

    @classmethod
    def select_create_new_enclosure_group(cls, timeout=5):
        logger.debug("select option [ Create new enclosure group ]")
        FusionUIBase.choose_combo_option_by_text("cic-enclosure-group-select-input", "Create new enclosure group", timeout, fail_if_false=True)

    @classmethod
    def input_enclosure_group_name(cls, enclosure_group, timeout=5):
        logger.debug("input [ Enclosure group name ] '%s'" % enclosure_group)
        ui_lib.wait_for_element_and_input_text(AddEnclosuresElements.ID_INPUT_ENCLOSURE_GROUP_NAME, enclosure_group, timeout, fail_if_false=True)

    @classmethod
    def input_vcm_username(cls, username, timeout=5):
        logger.debug("input [ Vcm user name] '%s'" % username)
        ui_lib.wait_for_element_and_input_text(AddEnclosuresElements.ID_INPUT_VCM_USERNAME, username, timeout, fail_if_false=True)

    @classmethod
    def input_vcm_password(cls, password, timeout=5):
        logger.debug("input [ Vcm password] '%s'" % password)
        ui_lib.wait_for_element_and_input_text(AddEnclosuresElements.ID_INPUT_VCM_PASSWORD, password, timeout, fail_if_false=True)

    @classmethod
    def click_test_compatibility_button(cls, timeout=5):
        logger.debug("click [ Test compatibility ] button")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_TEST_COMPATIBILITY, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_migrate_report_generation(cls, timeout=5, fail_if_false=True):
        logger.debug("waiting [ Migrate compatibility report ] generation")
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_TEXT_MIGRATE_REPORT_SUMMARY, timeout, fail_if_false)

    @classmethod
    def tick_migrate_vc_backup_checkbox(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ Migrate vc backup ] acknowledgement checkbox")
        return ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_CHECKBOX_MIGRATE_VC_BACKUP, timeout, fail_if_false)

    @classmethod
    def tick_resources_not_modified_checkbox(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ Resources not modified ] acknowledgement checkbox")
        return ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_CHECKBOX_RESOURCES_NOT_MODIFIED, timeout, fail_if_false)

    @classmethod
    def tick_profile_not_migrated_checkbox(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ Profile not migrated ] acknowledgement checkbox")
        return ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_CHECKBOX_PROFILE_NOT_MIGRATED, timeout, fail_if_false)

    @classmethod
    def tick_in_service_migration_checkbox(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ In Service not migrated ] acknowledgement checkbox")
        return ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_CHECKBOX_IN_Service_Migration, timeout, fail_if_false)

    @classmethod
    def tick_bios_checkbox(cls, timeout=5, fail_if_false=True):
        logger.debug("tick [ BIOS not migrated ] acknowledgement checkbox")
        return ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_CHECKBOX_BIOS, timeout, fail_if_false)

    @classmethod
    def input_logical_interconnect_group(cls, lig_name, timeout=5):
        logger.debug("input [ Logical interconnect group ] '%s'" % lig_name)
        # ui_lib.wait_for_element_and_input_text(AddEnclosuresElements.ID_INPUT_LOGICAL_INTERCONNECT_GROUP, timeout, fail_if_false=True)
        FusionUIBase.choose_combo_option_by_text(AddEnclosuresElements.ID_COMBO_LOGICAL_INTERCONNECT_GROUP, lig_name, timeout, fail_if_false=True)

    @classmethod
    def tick_licensing_hp_oneview_advanced(cls, timeout=5):
        logger.debug("tick [ Licensing ] 'HPE OneView Advanced'")
        FusionUIBase.wait_for_checkbox_and_select(AddEnclosuresElements.ID_RADIO_LICENSING_HP_ONEVIEW_ADVANCED, timeout, fail_if_false=True)

    @classmethod
    def tick_licensing_hp_oneview_advanced_wo_ilo(cls, timeout=5):
        logger.debug("tick [ Licensing ] 'HPE OneView Advanced w/o iLO'")
        FusionUIBase.wait_for_checkbox_and_select(AddEnclosuresElements.ID_RADIO_LICENSING_HP_ONEVIEW_ADVANCED_WO_ILO, timeout, fail_if_false=True)

    @classmethod
    def select_firmware_baseline(cls, firmware, timeout=5):
        logger.debug("select [ Firmware baseline ] '%s'" % firmware)
        FusionUIBase.choose_option_by_text(AddEnclosuresElements.ID_SELECT_FIRMWARE_BASELINE, firmware, timeout, fail_if_false=True)

    @classmethod
    def tick_firmware_force_install(cls, timeout=5):
        logger.debug("click [ Force installation ]")
        FusionUIBase.wait_for_checkbox_and_select(AddEnclosuresElements.ID_CHECKBOX_FORCE_INSTALLATION, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_verifying_parameters_msg(cls, timeout=10, fail_if_false=True):
        logger.debug('wait message [ Verifying Parameters ]')
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_TEXT_VERIFYING_PARAMETERS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_creating_lig(cls, lig_name, timeout=10, fail_if_false=True):
        logger.debug('wait message [ Creating logical interconnect group %s logical interconnect group ]' % lig_name)
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_TEXT_CREATING_LIG % lig_name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_adding_enclosure_text_in_dialog(cls, timeout=15, fail_if_false=True):
        logger.debug("wait message [ Adding enclosure... ]")
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_TEXT_ADDING_ENCLOSURE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_adding_enclosure_text_disappear_from_dialog(cls, timeout=25, fail_if_false=True):
        logger.debug("wait message [ Adding enclosure... ] disappear")
        return ui_lib.wait_for_element_notvisible(AddEnclosuresElements.ID_TEXT_ADDING_ENCLOSURE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_lig_dialog_shown(cls, timeout=15, fail_if_false=True):
        logger.debug("wait [ Edit logical interconnect group ] dialog shown")
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_DIALOG_EDIT_LIG, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_lig_dialog_disappear(cls, timeout=15, fail_if_false=True):
        logger.debug("wait [ Edit logical interconnect group ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(AddEnclosuresElements.ID_DIALOG_EDIT_LIG, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_adding_enclosure_operation_stage_1(cls, enclosure, add_plus=False, timeout=120, fail_if_false=True):
        """
        Check if add enclosure operation is completed. (stage 1)
        This method must be called before adding & configuring lig during adding enclosure.

        :param enclosure:
        :param add_plus: True to click Add plus button to add enclosure otherwise click Add button
        :param timeout:
        :param fail_if_false:
        :return: True when add enclosure dialog disappeared or create lig dialog shown. False when got timeout or got unexpected error message in dialog.
        """
        start = datetime.now()
        force_add = enclosure.force.lower() == "true"

        while (datetime.now() - start).total_seconds() < timeout:
            if add_plus is False:
                logger.debug("waiting [ Add enclosure dialog ] disappeared or [ Create LIG dialog ] shown -- stage 1")
                if ui_lib.wait_for_element_notvisible(AddEnclosuresElements.ID_DIALOG_ADD_ENCLOSURE, timeout=5, fail_if_false=False) is True:
                    # add enclosure dialog disappear, break loop
                    return True
            ret, err_msg = FusionUIBase.get_error_message_from_dialog(timeout=1)
            # got error message, forcing add if got message "enclosure is already been claimed by another fusion"
            if ret is True:
                if force_add is True:
                    predicted_err_msg_list = ("claimed by another management system",           # adding an enclosure for management, but it is already being managed by others
                                              "managed by Virtual Connect Manager",             # adding an enclosure for management, but it is already being managed by VCM
                                              "managed by another OneView management system",   # adding an enclosure for monitoring, but it is already being managed by others
                                              "monitored by another management system"          # adding an enclosure for monitoring, but it is already being monitored by others
                                              )
                    if map(lambda x: x in err_msg, predicted_err_msg_list).count(True) > 0:
                        logger.debug("forcing add [ enclosure '%s' ] since it is already been monitored/claimed by another management system -- stage 1")
                        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_CHECKBOX_FORCE_ADD_ENCLOSURE, timeout=1, fail_if_false=True)
                        # if give lig in previous step, lig textbox will be emptied, need to re-type it
                        if hasattr(enclosure, "lig"):
                            lig_obj = enclosure.lig[0] if isinstance(enclosure.lig, list) else enclosure.lig
                            if getattr(lig_obj, "create_new", "false").lower() == "false":
                                lig_name = getattr(lig_obj, "name", "")
                                if lig_name != "":
                                    FusionUIBase.choose_combo_option_by_text(AddEnclosuresElements.ID_COMBO_LOGICAL_INTERCONNECT_GROUP, lig_name, fail_if_false=True)
                        if add_plus is False:
                            ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_ADD, timeout=1, fail_if_false=True)
                        else:
                            ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_ADD_PLUS, timeout=1, fail_if_false=True)
                        continue

                err_msg = "got error message '%s' when adding [ enclosure '%s' ] -- stage 1" % (err_msg, enclosure.name)
                return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)

            if add_plus is True:
                logger.debug("waiting enclosure [ %s ] show in table list -- stage 1." % enclosure.name)
                # check if enclosure exists in table list, if it is true, we consider dialog form is ready for adding next enclosure
                if ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TABLE_ENCLOSURE % enclosure.name, timeout=1, fail_if_false=False) is True:
                    return True

            # break loop if edit lig dialog show
            if hasattr(enclosure, "lig"):
                lig_obj = enclosure.lig[0] if isinstance(enclosure.lig, list) else enclosure.lig
                if getattr(lig_obj, "create_new", "false").lower() == "true":
                    lig_name = getattr(lig_obj, "lig_name", "")
                    if lig_name == "":
                        if ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_DIALOG_EDIT_LIG, timeout=5, fail_if_false=False) is True:
                            # get edit lig dialog display
                            return True

        err_msg = "timeout to waiting add [ enclosure '%s' ] operation done -- stage 1." % enclosure.name
        return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_adding_enclosure_operation_stage_2(cls, enclosure, add_plus=False, timeout=200, fail_if_false=True):
        """
        Check if add enclosure operation is completed. (stage 2)
        This method must be called before adding & configuring lig during adding enclosure.

        :param enclosure:
        :param add_plus: True to click Add plus button to add enclosure otherwise click Add button
        :param timeout:
        :param fail_if_false:
        :return: True when add enclosure dialog disappeared. False when got timeout or got unexpected error message in dialog.
        """
        start = datetime.now()
        force_add = enclosure.force.lower() == "true"

        while (datetime.now() - start).total_seconds() < timeout:
            if add_plus is False:
                logger.debug("waiting [ Add enclosure dialog ] disappeared -- stage 2")
                if ui_lib.wait_for_element_notvisible(AddEnclosuresElements.ID_DIALOG_ADD_ENCLOSURE, timeout=5, fail_if_false=False) is True:
                    # add enclosure dialog disappear, break loop
                    return True
            ret, err_msg = FusionUIBase.get_error_message_from_dialog(timeout=1)
            # got error message, forcing add if got message "enclosure is already been claimed by another fusion"
            if ret is True:
                if force_add is True:
                    predicted_err_msg_list = ("claimed by another management system",           # adding an enclosure for management, but it is already being managed by others
                                              "managed by Virtual Connect Manager",             # adding an enclosure for management, but it is already being managed by VCM
                                              "managed by another OneView management system",   # adding an enclosure for monitoring, but it is already being managed by others
                                              "monitored by another management system"          # adding an enclosure for monitoring, but it is already being monitored by others
                                              )
                    if map(lambda x: x in err_msg, predicted_err_msg_list).count(True) > 0:
                        logger.debug("forcing add [ enclosure '%s' ] since it is already been monitored/claimed by another management system -- stage 2")
                        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_CHECKBOX_FORCE_ADD_ENCLOSURE, timeout=1, fail_if_false=True)
                        # if give lig in previous step, lig textbox will be emptied, have to re-type it
                        if hasattr(enclosure, "lig"):
                            lig_obj = enclosure.lig[0] if isinstance(enclosure.lig, list) else enclosure.lig
                            if getattr(lig_obj, "create_new", "false").lower() == "false":
                                lig_name = getattr(lig_obj, "name", "")
                                if lig_name != "":
                                    FusionUIBase.choose_combo_option_by_text(AddEnclosuresElements.ID_COMBO_LOGICAL_INTERCONNECT_GROUP, lig_name, fail_if_false=True)
                        if add_plus is False:
                            ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_ADD, timeout=1, fail_if_false=True)
                        else:
                            ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_ADD_PLUS, timeout=1, fail_if_false=True)
                        continue
                err_msg = "got error message '%s' when adding [ enclosure '%s' ] -- stage 2" % (err_msg, enclosure.name)
                return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)

            if add_plus is True:
                logger.debug("waiting enclosure [ %s ] show in table list -- stage 2." % enclosure.name)
                # check if enclosure exists in table list, if it is true, we consider dialog form is ready for adding next enclosure
                if ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TABLE_ENCLOSURE % enclosure.name, timeout=1, fail_if_false=False) is True:
                    return True

        err_msg = "timeout to waiting add [ enclosure '%s' ] operation done -- stage 2." % enclosure.name
        return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)

    @classmethod
    def click_add_button(cls, timeout=5):
        logger.debug("click [ Add ] button")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_ADD, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    def click_add_plus_button(cls, timeout=5):
        logger.debug("click [ Add plus ] button")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_ADD_PLUS, timeout, fail_if_false=True)

    # lig
    # TODO: checkbox has removed from UI in PB22
    # @classmethod
    # def tick_edit_lig_operating_mode(cls, timeout=5):
    #     logger.debug("tick checkbox [ Operating mode ]")
    #     FusionUIBase.wait_for_checkbox_and_select(AddEnclosuresElements.ID_CHECKBOX_OPERATING_MODE, timeout, fail_if_false=True)

    @classmethod
    def select_bay_type(cls, bay_no, bay_type, timeout=5):
        logger.debug("select bay type [ %s ] for bay [ %s ]" % (bay_type, bay_no))
        # FusionUIBase.choose_option_by_text(CreateLogicalInterconnectGroupsElements.ID_SELECT_BAY_TYPE % bay_no, bay_type, timeout, fail_if_false=True)
        ui_lib.get_s2l().execute_javascript(AddEnclosuresElements.ID_JAVASCRIPT_BAY_TYPE % bay_no)
        time.sleep(1)
        ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_DROPDOWN_BAY_TYPE_OPTION_LAYER % bay_no, fail_if_false=True)
        ui_lib.get_s2l().execute_javascript(AddEnclosuresElements.ID_JAVASCRIPT_SELECT_BAY_TYPE % (bay_no, bay_type))
        ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_SELECTED_BAY_TYPE % (bay_no, bay_type), fail_if_false=True)

    @classmethod
    def click_edit_lig_ok_and_add_enclosure_button(cls, timeout=5):
        logger.debug("Click edit lig [ OK and add enclosure ] button")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_OK_AND_ADD_ENCLOSURE, timeout, fail_if_false=True)

    @classmethod
    def click_edit_lig_cancel_button(cls, timeout=5):
        logger.debug("click edit lig [ Cancel ] button")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_CANCEL, timeout, fail_if_false=True)

    # uplink set
    @classmethod
    def click_edit_lig_add_uplink_set(cls, timeout=5):
        logger.debug("click [ Add uplink set ] button in edit lig dialog")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_ADD_UPLINK_SET, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_lig_create_uplink_set_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Create uplink set dialog ] shown")
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_DIALOG_EDIT_LIG_CREATE_UPLINK_SET, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_lig_create_uplink_set_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Create uplink set dialog ] shown")
        return ui_lib.wait_for_element_notvisible(AddEnclosuresElements.ID_DIALOG_EDIT_LIG_CREATE_UPLINK_SET, timeout, fail_if_false)

    @classmethod
    def input_edit_lig_create_uplink_set_name(cls, uplink_set_name, timeout=5):
        logger.debug("input uplink set name [ %s ] in edit lig create uplink set dialog" % uplink_set_name)
        ui_lib.wait_for_element_and_input_text(AddEnclosuresElements.ID_INPUT_EDIT_LIG_CREATE_UPLINK_SET_NAME, uplink_set_name, timeout, fail_if_false=True)

    @classmethod
    def select_edit_lig_create_uplink_set_type(cls, uplink_set_type, timeout=5):
        logger.debug("select uplink set type [ %s ] in edit lig create uplink set dialog" % uplink_set_type)
        FusionUIBase.choose_option_by_text(AddEnclosuresElements.ID_SELECT_EDIT_LIG_CREATE_UPLINK_SET_TYPE, uplink_set_type, timeout, fail_if_false=True)

    @classmethod
    def tick_edit_lig_create_uplink_set_connection_mode_automatic(cls, timeout=5):
        logger.debug("tick [ Automatic (recommended) ] option")
        FusionUIBase.wait_for_checkbox_and_select(AddEnclosuresElements.ID_RADIO_EDIT_LIG_CREATE_UPLINK_SET_CONNECTION_MODE_AUTOMATIC, timeout, fail_if_false=True)

    @classmethod
    def select_edit_lig_create_uplink_set_lacp_timer(cls, uplink_set_lacp_timer, timeout=5):
        logger.debug("select LACP timer [ %s ]" % uplink_set_lacp_timer)
        FusionUIBase.choose_option_by_text(AddEnclosuresElements.ID_SELECT_EDIT_LIG_CREATE_UPLINK_SET_LACP_TIMER, uplink_set_lacp_timer, timeout, fail_if_false=True)

    @classmethod
    def tick_edit_lig_create_uplink_set_connection_mode_failover(cls, timeout=5):
        logger.debug("tick [ Failover ] option")
        FusionUIBase.wait_for_checkbox_and_select(AddEnclosuresElements.ID_RADIO_EDIT_LIG_CREATE_UPLINK_SET_CONNECTION_MODE_FAILOVER, timeout, fail_if_false=True)

    @classmethod
    def tick_edit_lig_create_uplink_set_native_network(cls, network_name, timeout=5):
        logger.debug("tick vlan [ %s ] as native network in edit lig > create uplink set dialog" % network_name)
        FusionUIBase.wait_for_checkbox_and_select(AddEnclosuresElements.ID_CHECKBOX_EDIT_LIG_CREATE_UPLINK_SET_ETHERNET_NATIVE % network_name, timeout, fail_if_false=True)

    @classmethod
    def tick_edit_lig_create_uplink_set_preferred_uplink_port(cls, bay_no, port_name, timeout=5):
        logger.debug("tick [ bay%s:%s ] as preferred uplink port in edit lig > create uplink set dialog" % (bay_no, port_name))
        FusionUIBase.wait_for_checkbox_and_select(AddEnclosuresElements.ID_CHECKBOX_EDIT_LIG_CREATE_UPLINK_SET_ETHERNET_PREFERRED_PORT % (bay_no, port_name), timeout, fail_if_false=True)

    # lig uplink set network
    @classmethod
    def click_edit_lig_create_uplink_set_add_networks(cls, timeout=5):
        logger.debug("click [ Add networks ] button in edit lig > create uplink set dialog")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_NETWORKS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_lig_create_uplink_set_add_networks_to_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait edit lig > create uplink set > [ Add networks to ] dialog shown")
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_DIALOG_EDIT_LIG_CREATE_UPLINK_SET_ADD_NETWORKS_TO, timeout, fail_if_false)

    @classmethod
    def input_edit_lig_create_uplink_set_add_networks_to_search_network(cls, network_name, timeout=5):
        logger.debug("input [ %s ] to search network textbox in edit lig > create uplink set > add networks to dialog" % network_name)
        ui_lib.wait_for_element_and_input_text(AddEnclosuresElements.ID_INPUT_EDIT_LIG_CREATE_UPLINK_SET_ADD_NETWORKS_TO_SEARCH_NETWORK, network_name, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_lig_create_uplink_set_add_networks_to_table_row_shown(cls, network_name, timeout=5, fail_if_false=True):
        logger.debug("wait edit lig > create uplink set > add networks to [ %s ] table item shown" % network_name)
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_TABLE_ROW_EDIT_LIG_CREATE_UPLINK_SET_ADD_NETWORKS_TO % network_name, timeout, fail_if_false)

    @classmethod
    def click_edit_lig_create_uplink_set_add_networks_to_add(cls, timeout=5):
        logger.debug("click [ Add ] button in edit lig > create uplink set > add networks to dialog")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_NETWORKS_TO_ADD, timeout, fail_if_false=True)

    @classmethod
    def click_edit_lig_create_uplink_set_add_networks_to_add_plus(cls, timeout=5):
        logger.debug("click [ Add plus ] button in edit lig > create uplink set > add networks to dialog")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_NETWORKS_TO_ADD_PLUS, timeout, fail_if_false=True)

    @classmethod
    def click_edit_lig_create_uplink_set_add_networks_to_cancel(cls, timeout=5):
        logger.debug("click [ Cancel ] button in edit lig > create uplink set > add networks to dialog")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_NETWORKS_TO_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_lig_create_uplink_set_add_networks_to_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait edit lig > create uplink set > [ Add networks to ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(AddEnclosuresElements.ID_DIALOG_EDIT_LIG_CREATE_UPLINK_SET_ADD_NETWORKS_TO, timeout, fail_if_false)

    @classmethod
    def select_edit_lig_create_uplink_set_tunnel_network(cls, network, timeout=5):
        logger.debug("select tunnel network [ %s ] in edit lig > create uplink set dialog" % network)
        FusionUIBase.choose_combo_option_by_text(AddEnclosuresElements.ID_COMBO_EDIT_LIG_CREATE_UPLINK_SET_TUNNEL_NETWORK, network, timeout_sec=timeout, fail_if_false=True)

    @classmethod
    def select_edit_lig_create_uplink_set_untagged_network(cls, network, timeout=5):
        logger.debug("select untagged network [ %s ] in edit lig > create uplink set dialog" % network)
        FusionUIBase.choose_combo_option_by_text(AddEnclosuresElements.ID_COMBO_EDIT_LIG_CREATE_UPLINK_SET_UNTAGGED_NETWORK, network, timeout_sec=timeout, fail_if_false=True)

    # lig uplink set port
    @classmethod
    def click_edit_lig_create_uplink_set_add_uplink_ports(cls, timeout=5):
        logger.debug("click [ Add uplink ports ] button in edit lig > create uplink set dialog")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_UPLINK_PORTS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_lig_create_uplink_set_add_uplink_ports_to_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait edit lig > create uplink set > [ Add uplink ports to ] dialog shown")
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_DIALOG_EDIT_LIG_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_TO, timeout, fail_if_false)

    @classmethod
    def input_edit_lig_create_uplink_set_add_uplink_ports_to_search_port(cls, port_name, timeout=5):
        logger.debug("input [ %s ] to search port textbox in edit lig > create uplink set > add uplink ports to dialog" % port_name)
        ui_lib.wait_for_element_and_input_text(AddEnclosuresElements.ID_INPUT_EDIT_LIG_CREATE_UPLINK_SET_ADD_UPLINK_PORT_SEARCH_PORT, port_name, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_lig_create_uplink_set_add_uplink_ports_to_table_row_shown(cls, bay_no, port_name, timeout=5, fail_if_false=True):
        logger.debug("wait edit lig > create uplink set > add uplink ports to [ bay%s:%s ] table item shown" % (bay_no, port_name))
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_TABLE_ROW_EDIT_LIG_CREATE_UPLINK_SET_ADD_UPLINK_PORT % (bay_no, port_name), timeout, fail_if_false)

    @classmethod
    def click_edit_lig_create_uplink_set_add_uplink_ports_to_table_row(cls, bay_no, port_name, timeout=5):
        logger.debug("click [ bay%s:%s ] table item in edit lig > create uplink set > add uplink ports to dialog" % (bay_no, port_name))
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_TABLE_ROW_EDIT_LIG_CREATE_UPLINK_SET_ADD_UPLINK_PORT % (bay_no, port_name), timeout, fail_if_false=True)

    @classmethod
    def click_edit_lig_create_uplink_set_add_uplink_ports_to_add(cls, timeout=5):
        logger.debug("click [ Add ] button in edit lig > create uplink set > add uplink ports to dialog")
        FusionUIBase.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_ADD, timeout, fail_if_false=True, js_click=True)

    @classmethod
    def click_edit_lig_create_uplink_set_add_uplink_ports_to_add_plus(cls, timeout=5):
        logger.debug("click [ Add plus ] button in edit lig > create uplink set > add uplink ports to dialog")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_ADD_PLUS, timeout, fail_if_false=True)

    @classmethod
    def click_edit_lig_create_uplink_set_add_uplink_ports_to_cancel(cls, timeout=5):
        logger.debug("click [ Cancel ] button in edit lig > create uplink set > add uplink ports to dialog")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_lig_create_uplink_set_add_uplink_ports_to_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait edit lig > create uplink set > [ Add uplink ports to ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(AddEnclosuresElements.ID_DIALOG_EDIT_LIG_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_TO, timeout, fail_if_false)

    # fc
    @classmethod
    def select_edit_lig_create_uplink_set_fc_network(cls, network, timeout=5):
        logger.debug("select fc network [ %s ] in edit lig > create uplink set dialog" % network)
        FusionUIBase.choose_combo_option_by_text(AddEnclosuresElements.ID_COMBO_EDIT_LIG_CREATE_UPLINK_SET_FC_NETWORK, network, timeout_sec=timeout, fail_if_false=True)

    @classmethod
    def select_edit_lig_create_uplink_set_fc_interconnect(cls, interconnect, timeout=5):
        logger.debug("select fc interconnect [ %s ] in edit lig > create uplink set dialog" % interconnect)
        FusionUIBase.choose_combo_option_by_text(AddEnclosuresElements.ID_COMBO_EDIT_LIG_CREATE_UPLINK_SET_FC_INTERCONNECT, interconnect, timeout_sec=timeout, fail_if_false=True)

    @classmethod
    def select_edit_lig_create_uplink_set_fc_port_speed(cls, bay_no, port_name, port_speed, timeout=5):
        logger.debug("select port speed [ %s ] for fc port [ %s ] in edit lig > create uplink set dialog" % (port_speed, port_name))
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_SELECT_CREATE_UPLINK_SET_FC_PORT_SPEED % (bay_no, port_name), timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_DROPDOWN_CREATE_UPLINK_SET_FC_PORT_SPEED % (bay_no, port_name, port_speed), timeout, fail_if_false=True)

    # buttons
    @classmethod
    def click_edit_lig_create_uplink_set_add(cls, timeout=5):
        logger.debug("click [ Add ] button in edit lig create uplink set dialog")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD, timeout, fail_if_false=True)

    @classmethod
    def click_edit_lig_create_uplink_set_add_plus(cls, timeout=5):
        logger.debug("click [ Add plus ] button in edit lig create uplink set dialog")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_PLUS, timeout, fail_if_false=True)

    @classmethod
    def click_edit_lig_create_uplink_set_cancel(cls, timeout=5):
        logger.debug("click [ Cancel ] button in edit lig create uplink set dialog")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_CREATE_UPLINK_SET_ADD_CANCEL, timeout, fail_if_false=True)

    # internal network
    @classmethod
    def click_edit_lig_edit_internal_networks_gear(cls, timeout=5):
        logger.debug("click [ gear ] button in edit lig dialog")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_EDIT_INTERNAL_NETWORKS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_lig_edit_internal_networks_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait edit lig [ Edit Internal Network ] dialog shown")
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_DIALOG_EDIT_LIG_EDIT_INTERNAL_NETWORKS, timeout, fail_if_false)

    @classmethod
    def click_edit_lig_edit_internal_networks_add_networks(cls, timeout=5):
        logger.debug("click [ Add networks ] button in edit lig > edit internal networks dialog")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_lig_edit_internal_networks_add_networks_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait edit lig > edit internal networks > [ Add Networks ] dialog shown")
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_DIALOG_EDIT_LIG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS, timeout, fail_if_false)

    @classmethod
    def input_edit_lig_edit_internal_networks_add_networks_search_network(cls, network, timeout=5):
        logger.debug("input [ %s ] into search network textbox in edit lig > edit internal networks > add networks" % network)
        ui_lib.wait_for_element_and_input_text(AddEnclosuresElements.ID_INPUT_EDIT_LIG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_SEARCH_NETWORK, network, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_lig_edit_internal_networks_add_networks_table_row_shown(cls, network, timeout=5, fail_if_false=True):
        logger.debug("wait edit lig > edit internal networks > add networks > table row [ %s ] shown" % network)
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_TABLE_ROW_EDIT_LIG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS % network, timeout, fail_if_false)

    @classmethod
    def click_edit_lig_edit_internal_networks_add_networks_add(cls, timeout=5):
        logger.debug("click [ Add ] button in edit lig > edit internal networks > add networks dialog")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_ADD, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_lig_edit_internal_networks_add_networks_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait edit lig > edit internal networks > [ Add Networks ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(AddEnclosuresElements.ID_DIALOG_EDIT_LIG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS, timeout, fail_if_false)

    @classmethod
    def click_edit_lig_edit_internal_networks_add_networks_add_plus(cls, timeout=5):
        logger.debug("click [Add plus ] button in edit lig > edit internal networks > add networks")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_ADD_PLUS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_lig_edit_internal_networks_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait edit lig > edit internal networks > [ Edit Internal Networks ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(AddEnclosuresElements.ID_DIALOG_EDIT_LIG_EDIT_INTERNAL_NETWORKS, timeout, fail_if_false)

    @classmethod
    def click_edit_lig_edit_internal_networks_ok(cls, timeout=5):
        logger.debug("click [ OK ] button in edit lig > edit internal networks")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_EDIT_INTERNAL_NETWORKS_OK, timeout, fail_if_false=True)

    @classmethod
    def click_edit_lig_edit_internal_networks_cancel(cls, timeout=5):
        logger.debug("click [ Cancel ] button in edit lig > edit internal networks")
        ui_lib.wait_for_element_and_click(AddEnclosuresElements.ID_BUTTON_EDIT_LIG_EDIT_INTERNAL_NETWORKS_CANCEL, timeout, fail_if_false=True)


class _BaseEditEnclosures(object):

    """
    This class holds all operation when edit enclosure.
    It also defines abstract methods which the subclass has different implementation for C7000 & TBird
    """
    pass


class C7000EditEnclosures(_BaseEditEnclosures):

    @classmethod
    def select_actions_edit(cls, timeout=5):
        logger.debug("select [ Edit ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralEnclosuresElements.ID_BUTTON_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditEnclosuresElements.ID_SELECT_ACTION_EDIT, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_enclosure_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Edit enclosure ] dialog shown")
        return ui_lib.wait_for_element_visible(EditEnclosuresElements.ID_DIALOG_EDIT_ENCLOSURE, timeout, fail_if_false)

    @classmethod
    def input_edit_enclosure_enclosure_name(cls, new_name, timeout=5):
        logger.debug("input [ %s ] into edit enclosure > [ Enclosure name ] textbox" % new_name)
        ui_lib.wait_for_element_and_input_text(EditEnclosuresElements.ID_INPUT_EDIT_ENCLOSURE_ENCLOSURE_NAME, new_name, timeout, fail_if_false=True)

    @classmethod
    def click_edit_enclosure_ok(cls, timeout=5):
        logger.debug("click [ OK ] button in edit enclosure dialog")
        ui_lib.wait_for_element_and_click(EditEnclosuresElements.ID_BUTTON_EDIT_ENCLOSURE_OK, timeout, fail_if_false=True)

    @classmethod
    def click_edit_enclosure_cancel(cls, timeout=5):
        logger.debug("click [ Cancel ] button in edit enclosure dialog")
        ui_lib.wait_for_element_and_click(EditEnclosuresElements.ID_BUTTON_EDIT_ENCLOSURE_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_enclosure_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ edit enclosure ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(EditEnclosuresElements.ID_DIALOG_EDIT_ENCLOSURE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_invalid_name_error_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait invalid name error message shown")
        return ui_lib.wait_for_element_visible(EditEnclosuresElements.ID_TEXT_INVALID_NAME_ERROR, timeout, fail_if_false)


class TBirdEditEnclosures(_BaseEditEnclosures):

    pass


class _BaseEnclosuresReapplyConfiguration(object):

    """
    This class holds all operation when reapply enclosure configuration.
    It also defines abstract methods which the subclass has different implementation for C7000 & TBird
    """
    pass


class C7000EnclosuresReapplyConfiguration(_BaseEnclosuresReapplyConfiguration):

    @classmethod
    def select_actions_reapply_configuration(cls, timeout=5):
        logger.debug("select [ Reapply configuration ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralEnclosuresElements.ID_BUTTON_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(ReapplyEnclosuresElements.ID_SELECT_ACTION_REAPPLY_CONFIGURATION, timeout, fail_if_false=True)


class TBirdEnclosuresReapplyConfiguration(_BaseEnclosuresReapplyConfiguration):
    pass


class _BaseEnclosuresInterconnectLinkTopology(object):

    """
    This class holds all operation when enclosure interconnect link topology view is selected.
    Interconnect link topology operation is not applicable for C7000 enclosure
    """
    pass


class TBirdEnclosuresInterconnectLinkTopology(_BaseEnclosuresInterconnectLinkTopology):

    @classmethod
    def get_enclosure_list_from_interconnect_link_topology(cls, timeout=5, fail_if_false=True):
        logger.debug("Get all [ enclosure names ] from table")
        enclosure_list = []
        if ui_lib.wait_for_element(InterconnectLinkTopologyElements.ID_ENCLOSURE_LIST, timeout, fail_if_false):
            enclosure_list = FusionUIBase.get_multi_elements_text(InterconnectLinkTopologyElements.ID_ENCLOSURE_LIST, timeout, fail_if_false, True)
        return enclosure_list

    @classmethod
    def get_interconnect_cxp_bay_from_interconnect_link_topology(cls, count, timeout=5, fail_if_false=True):
        logger.debug("Get [ interconnect, cxpport, bay  information] from enclosure")
        ic_bay_port_list = []
        if ui_lib.wait_for_element(InterconnectLinkTopologyElements.ID_ENCLOSURE_CXPPORT_BAY_INFORMATION % count, timeout, fail_if_false):
            ic_bay_port_list = FusionUIBase.get_multi_elements_text(InterconnectLinkTopologyElements.ID_ENCLOSURE_CXPPORT_BAY_INFORMATION % count, 15, fail_if_false)
        return ic_bay_port_list

    @classmethod
    def click_interconnect_bayset_option(cls, bayset, timeout=5, fail_if_false=True):
        logger.debug("click [ View Interconnect bay set ] option")
        ui_lib.wait_for_element_and_click(InterconnectLinkTopologyElements.ID_DROPDOWN_INTERCONNECT_BAYSET, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(InterconnectLinkTopologyElements.ID_SELECT_INTERCONNECT_BAYSET % bayset, timeout, fail_if_false)

    @classmethod
    def click_view_side_option(cls, viewside, timeout=5, fail_if_false=True):
        logger.debug("click [ View side ] drop down option")
        ui_lib.wait_for_element_and_click(InterconnectLinkTopologyElements.ID_DROPDOWN_VIEWSIDE, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(InterconnectLinkTopologyElements.ID_SELECT_VIEWSIDE % viewside, timeout, fail_if_false)

    @classmethod
    def click_cxpport_interconnect_link_topology(cls, count, bay, port, timeout=15, fail_if_false=True):
        logger.debug("click on [ cxpport ] in interconnect link topology ")
        ui_lib.wait_for_element_and_click(InterconnectLinkTopologyElements.ID_CLICK_ENCLOSURE_CXPPORT % (count, bay, port), timeout, fail_if_false)

    @classmethod
    def get_cxpport_status_interonnect_link_topology(cls, count, bay, port, timeout=5, fail_if_false=True):
        logger.debug("get [ cxpport status] in interconnect link topology ")
        port_status = FusionUIBase.get_text(InterconnectLinkTopologyElements.ID_ENCLOSURE_CXPPORT_STATUS % (count, bay, port), timeout, fail_if_false, True)
        return port_status

    @classmethod
    def get_connected_webelement_link_topology(cls, count, bay, port, timeout=5, fail_if_false=True):
        logger.debug("get [ connected webelement for cxpport] in interconnect link topology ")
        s2l = ui_lib.get_s2l()
        connected_webelement = s2l.get_element_attribute(InterconnectLinkTopologyElements.ID_ENCLOSURE_CXPPORT_CONNECTED_WEBELEMENT % (count, bay, port))
        return connected_webelement

    @classmethod
    def get_connected_cxpport_link_topology(cls, locator, timeout=5, fail_if_false=True):
        logger.debug("get [ connected port to cxpport] in interconnect link topology ")
        ui_lib.scroll_into_view(InterconnectLinkTopologyElements.ID_ENCLOSURE_CXPPORT_CONNECTED_PORT % (locator))
        connected_port = FusionUIBase.get_text(InterconnectLinkTopologyElements.ID_ENCLOSURE_CXPPORT_CONNECTED_PORT % (locator), timeout, fail_if_false, True)
        return connected_port

    @classmethod
    def get_connected_ic_link_topology(cls, locator, timeout=5, fail_if_false=True):
        logger.debug("get [ connected ic to cxpport] in interconnect link topology ")
        ui_lib.scroll_into_view(InterconnectLinkTopologyElements.ID_ENCLOSURE_CXPPORT_CONNECTED_IC % (locator))
        connected_ic = FusionUIBase.get_text(InterconnectLinkTopologyElements.ID_ENCLOSURE_CXPPORT_CONNECTED_IC % (locator), timeout, fail_if_false, True)
        return connected_ic

    @classmethod
    def get_error_count_in_invalid_interonnect_link_topology(cls, timeout=5, fail_if_false=True):
        logger.debug("get [ error count] on Activity for interconnect link topology ")
        error_count = FusionUIBase.get_text(InterconnectLinkTopologyElements.ID_LABEL_PAGE_ERROR_COUNT, timeout, fail_if_false, True)
        return error_count

    @classmethod
    def click_filter_all_states(cls, timeout, fail_if_false=True):
        logger.debug("click [ Activity Filter ] all states")
        return ui_lib.wait_for_element_and_click(InterconnectLinkTopologyElements.ID_FILTER_ALL_STATES, timeout, fail_if_false)

    @classmethod
    def click_filter_activity_state(cls, state, timeout, fail_if_false=True):
        logger.debug("click [ Filter Activity] based on the state")
        return ui_lib.wait_for_element_and_click(InterconnectLinkTopologyElements.ID_FILTER_BY_STATE % state, timeout, fail_if_false)

    @classmethod
    def click_alert_label_collapser(cls, count, timeout, fail_if_false=True):
        logger.debug("click [ Alert label] collaper")
        return ui_lib.wait_for_element_and_click(InterconnectLinkTopologyElements.ID_LABEL_PAGE_CLICK_ERROR % count, timeout, fail_if_false)

    @classmethod
    def click_event_details_collapser(cls, count, timeout, fail_if_false=True):
        logger.debug("click [ event label] collaper")
        return ui_lib.wait_for_element_and_click(InterconnectLinkTopologyElements.ID_LABEL_EVENT_CLICK_ERROR % (count), timeout, fail_if_false)

    @classmethod
    def click_cxpenclosure(cls, enclosure, count, timeout=5, fail_if_false=True):
        logger.debug("select [ cxp enclosure '%s' ]" % enclosure)
        return ui_lib.wait_for_element_and_click(InterconnectLinkTopologyElements.ID_CXPPORT_CXPENCLOSURE % count, timeout, fail_if_false)

    @classmethod
    def get_enclosure_status_in_interconnectlinktopology(cls, enclosure, count, timeout=5, fail_if_false=True):
        logger.debug("get [ enclosure %s status ] in interconnect link topology" % enclosure)
        enclosure_status = FusionUIBase.get_text(InterconnectLinkTopologyElements.ID_CXPPORT_CXPENCLOSURE_STATUS % count, timeout, fail_if_false, True)
        return enclosure_status

    @classmethod
    def click_cxpport_cxp_interconnect(cls, bay_no, interconnect, timeout=5, fail_if_false=True):
        logger.debug("click cxpport cxp '%s' '%s' in interconnect view" % (bay_no, interconnect))
        return ui_lib.wait_for_element_and_click(InterconnectLinkTopologyElements.ID_TEXT_CXPPORT_CXP_INTERCONNECTS % (bay_no, interconnect), timeout, fail_if_false)

    @classmethod
    def get_activity_text(cls, count, timeout=5, fail_if_false=True):
        logger.debug("get [ alert message] of activity for Enclosure")
        activity_msg = FusionUIBase.get_text(InterconnectLinkTopologyElements.ID_LABEL_PAGE_ERROR % (count), timeout, fail_if_false)
        return activity_msg

    @classmethod
    def get_resolution_text(cls, count, timeout=5, fail_if_false=True):
        logger.debug("get [ resolution message] of activity for Enclosure")
        resolution_msg = FusionUIBase.get_text(InterconnectLinkTopologyElements.ID_LABEL_PAGE_ERROR_FULL % (count), timeout, fail_if_false)
        return resolution_msg

    @classmethod
    def get_event_text(cls, count, timeout=5, fail_if_false=True):
        logger.debug("get [ event message] of activity for Enclosure")
        event_msg = FusionUIBase.get_text(InterconnectLinkTopologyElements.ID_EVENT_MESSAGE % (count), timeout, fail_if_false)
        return event_msg

    @classmethod
    def get_alert_text(cls, timeout=5, fail_if_false=True):
        logger.debug("get alert text present in Enclosure Page")
        alert_msg = FusionUIBase.get_text(InterconnectLinkTopologyElements.ID_ALERT_MSG, 10)
        return alert_msg


class _BaseRefreshEnclosures(object):

    """
    This class holds all operation when refresh enclosure configuration.
    It also defines abstract methods which the subclass has different implementation for C7000 & TBird
    """
    pass


class C7000RefreshEnclosures(_BaseRefreshEnclosures):

    @classmethod
    def select_actions_refresh(cls, timeout=5):
        logger.debug("select [ Refresh ] item in [ Action ] menu")
        ui_lib.wait_for_element_and_click(GeneralEnclosuresElements.ID_BUTTON_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(RefreshEnclosuresElements.ID_SELECT_ACTION_REFRESH, timeout, fail_if_false=True)


class TBirdRefreshEnclosures(_BaseRefreshEnclosures):
    pass


class _BaseResetLinkModule(object):

    """
    This class holds the operations when reset link module.
    """
    pass


class TBirdResetLinkModule(_BaseResetLinkModule):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_ok_notification_shown(cls, timeout=300, fail_if_false=True):
        logger.debug("wait notification with ok status show")
        return ui_lib.wait_for_element_visible(ResetLinkModuleElements.ID_STATUS_NOTIFICATION_OK, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_unknown_notification_shown(cls, timeout=300, fail_if_false=True):
        logger.debug("wait notification unknown status show")
        return ui_lib.wait_for_element_visible(ResetLinkModuleElements.ID_STATUS_NOTIFICATION_UNKNOWN, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_warn_notification_shown(cls, timeout=300, fail_if_false=True):
        logger.debug("wait notification warning status show")
        return ui_lib.wait_for_element_visible(ResetLinkModuleElements.ID_STATUS_NOTIFICATION_WARN, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_warn_notification_disappear(cls, timeout=300, fail_if_false=True):
        logger.debug("wait notification warning status not show")
        return ui_lib.wait_for_element_notvisible(ResetLinkModuleElements.ID_STATUS_NOTIFICATION_WARN, timeout, fail_if_false)

    @classmethod
    def select_actions_reset_link_module(cls, timeout=5):
        logger.debug("select [ Reset link module] action button")
        ui_lib.wait_for_element_and_click(GeneralEnclosuresElements.ID_BUTTON_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(ResetLinkModuleElements.ID_SELECT_ACTION_RESET_LINK_MODULE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_reset_link_module_dialog_open(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Reset link module ] dialog open")
        return ui_lib.wait_for_element_visible(ResetLinkModuleElements.ID_DIALOG_RESET_LINK_MODULE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_reset_link_module_dialog_close(cls, timeout=30, fail_if_false=True):
        logger.debug("wait [ Reset link module ] dialog close")
        return ui_lib.wait_for_element_notvisible(ResetLinkModuleElements.ID_DIALOG_RESET_LINK_MODULE, timeout, fail_if_false)

    @classmethod
    def tick_reset_standby(cls, timeout=5):
        logger.debug("tick reset [ standby ] link module")
        ui_lib.wait_for_element_and_click(ResetLinkModuleElements.ID_CHECKBOX_RESET_STANDBY_LINK_MODULE, timeout, fail_if_false=True)

    @classmethod
    def tick_reset_active(cls, timeout=5):
        logger.debug("tick reset [ active ] link module")
        ui_lib.wait_for_element_and_click(ResetLinkModuleElements.ID_CHECKBOX_RESET_ACTIVE_LINK_MODULE, timeout, fail_if_false=True)

    @classmethod
    def click_yes_reset_button(cls, timeout=5):
        logger.debug("click [ Yes, reset ] button")
        ui_lib.wait_for_element_and_click(ResetLinkModuleElements.ID_BUTTON_YES_RESET, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(ResetLinkModuleElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)


class _BaseDeleteEnclosures(object):

    """
    This class holds all operation when remove enclosure configuration.
    It also defines abstract methods which the subclass has different implementation for C7000 & TBird
    """
    pass


class C7000RemoveEnclosures(_BaseDeleteEnclosures):

    @classmethod
    def select_actions_remove(cls, timeout=5):
        logger.debug("select [ Remove ] action button")
        ui_lib.wait_for_element_and_click(GeneralEnclosuresElements.ID_BUTTON_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(RemoveEnclosuresElements.ID_SELECT_ACTION_REMOVE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Remove ] dialog shown")
        return ui_lib.wait_for_element_visible(RemoveEnclosuresElements.ID_DIALOG_REMOVE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_unable_remove_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Remove ] dialog shown and unable remove")
        return ui_lib.wait_for_element_visible(RemoveEnclosuresElements.ID_TEXT_REMOVE_PROFILE, timeout, fail_if_false)

    @classmethod
    def tick_force_remove_enclosure(cls, timeout=5):
        logger.debug("tick [ Force remove enclosure ]")
        ui_lib.wait_for_element_and_click(RemoveEnclosuresElements.ID_CHECKBOX_FORCE_REMOVE_ENCLOSURE, timeout, fail_if_false=True)

    @classmethod
    def click_yes_remove_button(cls, timeout=5):
        logger.debug("click [ Yes, remove ] button")
        ui_lib.wait_for_element_and_click(RemoveEnclosuresElements.ID_BUTTON_YES_REMOVE, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(RemoveEnclosuresElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    def click_close_button(cls, timeout=5):
        logger.debug("click [ Close ] button")
        ui_lib.wait_for_element_and_click(RemoveEnclosuresElements.ID_BUTTON_CLOSE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_checkbox_force_remove_enclosure_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait for [ Force remove enclosure ] checkbox shown")

        return ui_lib.wait_for_element_visible(RemoveEnclosuresElements.ID_CHECKBOX_FORCE_REMOVE_ENCLOSURE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_dialog_disappear(cls, timeout=30, fail_if_false=True):
        logger.debug("wait [ Remove ] dialog disappear")
        return ui_lib.wait_for_element_notvisible(RemoveEnclosuresElements.ID_DIALOG_REMOVE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_enclosure_show_not_found(cls, enclosure, timeout=5, fail_if_false=True):
        logger.info("wait [ Enclosure %s status ] change to 'not found'" % enclosure)
        return ui_lib.wait_for_element_visible(RemoveEnclosuresElements.ID_TABLE_ENCLOSURE_DELETED % enclosure, timeout, fail_if_false)


class TBirdDeleteEnclosures(_BaseDeleteEnclosures):
    pass


class _BaseVerifyEnclosures(object):

    """
    This class holds all operation of enclosure when do verification.
    It also defines abstract methods which the subclass has different implementation for C7000 & TBird
    """
    # { Overview
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_general_state(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ State ] in overview > general view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("State", GeneralEnclosuresElements.ID_TEXT_OVERVIEW_GENERAL_STATE, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_general_model(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Model ] in overview > general view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Model", GeneralEnclosuresElements.ID_TEXT_OVERVIEW_GENERAL_MODEL, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_general_logical_enclosure(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Logical enclosure ] in overview > general view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Model", GeneralEnclosuresElements.ID_TEXT_OVERVIEW_GENERAL_LOGICAL_ENCLOSURE, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_hardware_location(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Location ] in overview > hardware view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Location", GeneralEnclosuresElements.ID_TEXT_OVERVIEW_HARDWARE_LOCATION, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_hardware_powered_by(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Powered by ] in overview > hardware view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Powered by", GeneralEnclosuresElements.ID_TEXT_OVERVIEW_HARDWARE_POWERED_BY, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_hardware_serial_number(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Serial number ] in overview > hardware view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Serial number", GeneralEnclosuresElements.ID_TEXT_OVERVIEW_HARDWARE_SERIAL_NUMBER, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_rear_view_interconnect_name(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Interconnect ] in overview > rear view, expect value is [ %s ]" % expect_value)
        ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_ELEMENT_OVERVIEW_REAR_VIEW_NAME % expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_rear_view_interconnect_model(cls, interconnect, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Model ] in overview > rear view, expect value is [ %s ]" % expect_value)
        ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_ELEMENT_OVERVIEW_REAR_VIEW_MODEL % (interconnect, expect_value), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_rear_view_interconnect_bay(cls, bay, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Bay ] in overview > rear view, expect value is [ %s ]" % bay)
        ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_ELEMENT_OVERVIEW_REAR_VIEW_BAY % (expect_value, bay), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_rear_view_interconnect_status(cls, interconnect, timeout=5, fail_if_false=True):
        logger.debug("verify [ Status ] in overview > rear view, is visible")
        ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_ELEMENT_OVERVIEW_REAR_VIEW_HEALTH_STATUS % interconnect, timeout, fail_if_false)
    # }

    # { General
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_state(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ State ] in general view, expect value is [ %s ]" % expect_value)
        ui_lib.wait_for_element_text(GeneralEnclosuresElements.ID_TEXT_GENERAL_STATE, expect_value, timeout, fail_if_false)
        return FusionUIBase.verify_element_text("State", GeneralEnclosuresElements.ID_TEXT_GENERAL_STATE, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_model(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Model ] in general view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Model", GeneralEnclosuresElements.ID_TEXT_GENERAL_MODEL, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_logical_enclosure(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Logical enclosure ] in general view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Logical enclosure", GeneralEnclosuresElements.ID_TEXT_GENERAL_LOGICAL_ENCLOSURE, expect_value, timeout, fail_if_false)
    # }

    # { Hardware
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_location(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Location ] in hardware view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Location", GeneralEnclosuresElements.ID_TEXT_HARDWARE_LOCATION, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_powered_by(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Powered by ] in hardware view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Powered by", GeneralEnclosuresElements.ID_TEXT_HARDWARE_POWERED_BY, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_serial_number(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Serial number ] in hardware view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Serial number", GeneralEnclosuresElements.ID_TEXT_HARDWARE_SERIAL_NUMBER, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_part_number(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Part number ] in hardware view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Part number", GeneralEnclosuresElements.ID_TEXT_HARDWARE_PART_NUMBER, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_maximum_power(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Maximum power ] in hardware view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Maximum power", GeneralEnclosuresElements.ID_TEXT_HARDWARE_MAXIMUM_POWER, expect_value, timeout, fail_if_false)
    # }

    # { Devices
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_device_bay_exist(cls, bay_no, timeout=5, fail_if_false=True):
        logger.debug("verify [ device bay '%s' ] exist in device view" % bay_no)
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TEXT_DEVICES_ROW_BAY % bay_no, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_device_status(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ device bay status ] of bay '%s' in device view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Bay status", GeneralEnclosuresElements.ID_TEXT_DEVICES_ROW_STATUS % bay_no, expect_value, timeout, fail_if_false, True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_device_server_hardware(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ device bay server hardware ] of bay '%s' in device view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Bay server hardware", GeneralEnclosuresElements.ID_TEXT_DEVICES_ROW_SERVER_HARDWARE % (bay_no, bay_no), expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_device_model(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ device bay model ] of bay '%s' in device view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Bay model", GeneralEnclosuresElements.ID_TEXT_DEVICES_ROW_SERVER_MODEL % bay_no, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_device_server_profile(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ device bay server profile ] of bay '%s' in device view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Bay server profile", GeneralEnclosuresElements.ID_TEXT_DEVICES_ROW_SERVER_PROFILE % (bay_no, bay_no), expect_value, timeout, fail_if_false)
    # }

    # { Interconnects
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_interconnect_bay_exist(cls, bay_no, timeout=5, fail_if_false=True):
        logger.debug("verify [ interconnect bay '%s' ] exist in interconnect view" % bay_no)
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TEXT_INTERCONNECTS_ROW_BAY % bay_no, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_interconnect_bay_empty(cls, bay_no, timeout=5, fail_if_false=False):
        logger.debug("verify [ interconnect bay '%s' ] empty in interconnect view" % bay_no)
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TEXT_INTERCONNECTS_ROW_BAY_EMPTY % bay_no, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_interconnect_status(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ interconnect bay status ] of bay '%s' in interconnect view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Bay status", GeneralEnclosuresElements.ID_TEXT_INTERCONNECTS_ROW_STATUS % bay_no, expect_value, timeout, fail_if_false, True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_interconnect_interconnect(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ bay name ] of bay '%s' in interconnect view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Bay name", GeneralEnclosuresElements.ID_TEXT_INTERCONNECTS_ROW_INTERCONNECT % bay_no, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_interconnect_installed_module(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ installed module ] of bay '%s' in interconnect view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Installed module", GeneralEnclosuresElements.ID_TEXT_INTERCONNECTS_ROW_INSTALLED_MODULE % bay_no, expect_value, timeout, fail_if_false)
    # }

    # { Power Supplies
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_power_supply_bay_exist(cls, bay_no, timeout=5, fail_if_false=True):
        logger.debug("verify [ power supply bay '%s' ] exist in power supply view" % bay_no)
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TEXT_POWER_SUPPLIES_ROW_BAY % bay_no, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_power_supply_status(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ power supply status ] of bay '%s' in power supplies view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Power supply bay status", GeneralEnclosuresElements.ID_TEXT_POWER_SUPPLIES_ROW_STATUS % bay_no, expect_value, timeout, fail_if_false, True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_power_supply_model(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ power supply model ] of bay '%s' in power supplies view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Power supply bay model", GeneralEnclosuresElements.ID_TEXT_POWER_SUPPLIES_ROW_MODEL % bay_no, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_power_supply_serial_number(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ power supply serial number ] of bay '%s' in power supplies view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Power supply serial number", GeneralEnclosuresElements.ID_TEXT_POWER_SUPPLIES_ROW_SERIAL_NUMBER % bay_no, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_power_supply_part_number(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ power supply part number ] of bay '%s' in power supplies view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Power supply serial number", GeneralEnclosuresElements.ID_TEXT_POWER_SUPPLIES_ROW_PART_NUMBER % bay_no, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_power_supply_spare_part_number(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ power supply spare part number ] of bay '%s' in power supplies view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Power supply spare part number", GeneralEnclosuresElements.ID_TEXT_POWER_SUPPLIES_ROW_SPARE_PART_NUMBER % bay_no, expect_value, timeout, fail_if_false)
    # }

    # { Fans
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_fan_bay_exist(cls, bay_no, timeout=5, fail_if_false=True):
        logger.debug("verify [ fan bay '%s' ] exist in power supply view" % bay_no)
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TEXT_FANS_ROW_BAY % bay_no, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_fan_status(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ fan status ] of bay '%s' in fans view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Fan status", GeneralEnclosuresElements.ID_TEXT_FANS_ROW_STATUS % bay_no, expect_value, timeout, fail_if_false, True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_fan_model(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ fan model ] of bay '%s' in fans view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Fan model", GeneralEnclosuresElements.ID_TEXT_FANS_ROW_MODEL % bay_no, expect_value, timeout, fail_if_false)
    # }

    # { Scopes
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_scope_should_exist(cls, name, timeout=5, fail_if_false=True):
        logger.debug("verify [ scope '%s' ] exist in scopes view" % name)
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TEXT_SCOPE % name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_scope_should_not_exist(cls, name, timeout=5, fail_if_false=True):
        logger.debug("verify [ scope '%s' ] not exist in scopes view" % name)
        return ui_lib.wait_for_element_notvisible(GeneralEnclosuresElements.ID_TEXT_SCOPE % name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_scope_should_exist_in_edit_page(cls, name, timeout=5, fail_if_false=False):
        logger.debug("verify [ scope '%s' ] exist in scope edit page" % name)
        return ui_lib.wait_for_element_visible(EditScopeElements.ID_TABLE_SCOPE_NAME % name, timeout, fail_if_false)
    # }

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_enclosure_exist(cls, enclosure, timeout=5, fail_if_false=True):
        logger.debug("verify [ enclosure '%s' ]" % enclosure)
        return ui_lib.wait_for_element(GeneralEnclosuresElements.ID_TABLE_ENCLOSURE % enclosure, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_activity_contains_text(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("Verifying activity contains: '%s'" % expect_value)
        return ui_lib.wait_for_element(GeneralEnclosuresElements.ID_TEXT_ACTIVITY_CONTENT % expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_activity_contains_subtask(cls, subtask, source, status, timeout=5, fail_if_false=True):
        logger.debug("Verifying sub task '%s' from '%s' is in '%s' status" % (subtask, source, status))
        return ui_lib.wait_for_element(GeneralEnclosuresElements.ID_TEXT_ACTIVITY_SUB_TASK % (status, subtask, source), timeout, fail_if_false)


class VerifyEnclosures(_BaseVerifyEnclosures):
    pass


class C7000VerifyEnclosures(_BaseVerifyEnclosures):

    # { Action menu

    @classmethod
    def verify_action_add_button_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify action menu [ Add button ] exist")
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_OPTION_ACTIONS_ADD, timeout, fail_if_false)

    @classmethod
    def verify_action_add_button_not_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify action menu [ Add button ] not exist")
        return ui_lib.wait_for_element_notvisible(GeneralEnclosuresElements.ID_OPTION_ACTIONS_ADD, timeout, fail_if_false)

    @classmethod
    def verify_action_edit_button_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify action menu [ Edit button ] exist")
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_OPTION_ACTIONS_EDIT, timeout, fail_if_false)

    @classmethod
    def verify_action_edit_button_not_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify action menu [ Edit button ] not exist")
        return ui_lib.wait_for_element_notvisible(GeneralEnclosuresElements.ID_OPTION_ACTIONS_EDIT, timeout, fail_if_false)

    @classmethod
    def verify_action_reapply_configuration_button_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify action menu [ Reapply configuration button ] exist")
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_OPTION_ACTIONS_REAPPLY_CONFIGURATION, timeout, fail_if_false)

    @classmethod
    def verify_action_reapply_configuration_button_not_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify action menu [ Reapply configuration button ] not exist")
        return ui_lib.wait_for_element_notvisible(GeneralEnclosuresElements.ID_OPTION_ACTIONS_REAPPLY_CONFIGURATION, timeout, fail_if_false)

    @classmethod
    def verify_action_refresh_button_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify action menu [ Refresh button ] exist")
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_OPTION_ACTIONS_REFRESH, timeout, fail_if_false)

    @classmethod
    def verify_action_remove_button_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify action menu [ Remove button ] exist")
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_OPTION_ACTIONS_REMOVE, timeout, fail_if_false)
    # }

    # { Check UI component
    @classmethod
    def verify_oa_ip_address_or_host_name_input_control_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ OA IP address or host name ] input control exist in page")
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_INPUT_OA_IP_ADDRESS_OR_HOST_NAME, timeout, fail_if_false)

    @classmethod
    def verify_add_enclosure_for_management_raidobox_control_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ Add enclosure for management ] raidobox control exist in page")
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_RADIO_ADD_ENCLOSURE_FOR_MANAGEMENT, timeout, fail_if_false)

    @classmethod
    def verify_add_enclosure_for_monitoring_raidobox_control_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ Add enclosure for monitoring ] raidobox control exist in page")
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_RADIO_ADD_ENCLOSURE_FOR_MONITORING, timeout, fail_if_false)

    @classmethod
    def verify_migrate_virtual_connect_domain_raidobox_control_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ Migrate Virtual Connect domain ] raidobox control exist in page")
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_RADIO_MIGRATE_VIRTUAL_CONNECT_DOMAIN, timeout, fail_if_false)

    @classmethod
    def verify_user_name_input_control_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ User Name ] input control exist in page")
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_INPUT_USER_NAME, timeout, fail_if_false)

    @classmethod
    def verify_password_input_control_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ Password ] input control exist in page")
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_INPUT_PASSWORD, timeout, fail_if_false)

    @classmethod
    def verify_enclosure_group_input_control_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ Enclosure group ] input control exist in page")
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_INPUT_ENCLOSURE_GROUP_NAME, timeout, fail_if_false)

    @classmethod
    def verify_enclosure_group_input_control_not_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ Enclosure group ] input control not exist in page")
        return ui_lib.wait_for_element_notvisible(AddEnclosuresElements.ID_INPUT_ENCLOSURE_GROUP_NAME, timeout, fail_if_false)

    @classmethod
    def verify_licensing_hp_oneview_advanced_raidobox_control_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ HPE OneView Advanced ] raido control exist in page")
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_RADIO_LICENSING_HP_ONEVIEW_ADVANCED, timeout, fail_if_false)

    @classmethod
    def verify_licensing_hp_oneview_advanced_raidobox_control_not_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ HPE OneView Advanced ] raido control not exist in page")
        return ui_lib.wait_for_element_notvisible(AddEnclosuresElements.ID_RADIO_LICENSING_HP_ONEVIEW_ADVANCED, timeout, fail_if_false)

    @classmethod
    def verify_licensing_hp_oneview_advanced_wo_ilo_raidobox_control_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ HPE OneView Advanced w/o iLO ] raido control exist in page")
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_RADIO_LICENSING_HP_ONEVIEW_ADVANCED_WO_ILO, timeout, fail_if_false)

    @classmethod
    def verify_licensing_hp_oneview_advanced_wo_ilo_raidobox_control_not_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ HPE OneView Advanced w/o iLO ] raido control not exist in page")
        return ui_lib.wait_for_element_notvisible(AddEnclosuresElements.ID_RADIO_LICENSING_HP_ONEVIEW_ADVANCED_WO_ILO, timeout, fail_if_false)

    @classmethod
    def verify_firmware_baseline_control_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ Firmware baseline ] control exist in page")
        return ui_lib.wait_for_element_visible(AddEnclosuresElements.ID_SELECT_FIRMWARE_BASELINE_CONTROL, timeout, fail_if_false)

    @classmethod
    def verify_firmware_baseline_control_not_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify [ Firmware baseline ] control not exist in page")
        return ui_lib.wait_for_element_notvisible(AddEnclosuresElements.ID_SELECT_FIRMWARE_BASELINE_CONTROL, timeout, fail_if_false)
    # }

    # { General verification
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_enclosure_not_exist(cls, enclosure, timeout=10, fail_if_false=True):
        logger.debug("verify [ enclosure '%s' ] is not existing" % enclosure)
        if ui_lib.wait_for_element_notvisible(GeneralEnclosuresElements.ID_TABLE_ENCLOSURE % enclosure, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_enclosure_exist(cls, enclosure, timeout=10, fail_if_false=True):
        logger.debug("verify [ enclosure '%s' ] is existing" % enclosure)
        if ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TABLE_ENCLOSURE % enclosure, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_enclosure_status_ok(cls, enclosure, timeout=10, fail_if_false=True):
        logger.debug("verify whether [ enclosure '%s' ] is ok" % enclosure)
        if ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_STATUS_ENCLOSURE_OK % enclosure, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_enclosure_status_warn(cls, enclosure, timeout=10, fail_if_false=True):
        logger.debug("verify whether [ enclosure '%s' ] is warning" % enclosure)
        if ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_STATUS_ENCLOSURE_WARN % enclosure, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_enclosure_status_error(cls, enclosure, timeout=10, fail_if_false=True):
        logger.debug("verify whether [ enclosure '%s' ] is error" % enclosure)
        if ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_STATUS_ENCLOSURE_ERROR % enclosure, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_add_enclosure_button_not_exist(cls, timeout=10, fail_if_false=True):
        logger.debug("verify [ Add enclosure ] is not existing")
        if ui_lib.wait_for_element_notvisible(GeneralEnclosuresElements.ID_BUTTON_ADD_ENCLOSURE, timeout, fail_if_false):
            return True
        else:
            return False
    # }

    # { Overview
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_general_server_licensing_policy(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Server licensing policy ] in overview > general view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Server licensing policy", GeneralEnclosuresElements.ID_TEXT_OVERVIEW_GENERAL_SERVER_LICENSING_POLICY, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_overview_hardware_oa(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ OA ] in overview > hardware view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("OA", GeneralEnclosuresElements.ID_TEXT_OVERVIEW_HARDWARE_OA, expect_value, timeout, fail_if_false)
    # }

    # { General
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_server_licensing_policy(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Server licensing policy ] in general view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Server licensing policy", GeneralEnclosuresElements.ID_TEXT_GENERAL_SERVER_LICENSING_POLICY, expect_value, timeout, fail_if_false)
    # }

    # { Hardware
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_primary_oa_host_name(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Primary OA host name ] in hardware view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Primary OA host name", GeneralEnclosuresElements.ID_TEXT_HARDWARE_PRIMARY_OA_HOST_NAME, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_primary_oa_ipv4(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Primary OA ipv4 ] in hardware view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Primary OA ipv4", GeneralEnclosuresElements.ID_TEXT_HARDWARE_PRIMARY_OA_IPV4, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_hardware_primary_oa_ipv6(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Primary OA ipv6 ] in hardware view, expect value is [ %s ]" % expect_value)
        if expect_value.lower() == 'none':
            return FusionUIBase.verify_element_text("Primary OA ipv6", GeneralEnclosuresElements.ID_TEXT_HARDWARE_PRIMARY_OA_IPV6_NONE, expect_value, timeout, fail_if_false)
        else:
            return FusionUIBase.verify_element_text("Primary OA ipv6", GeneralEnclosuresElements.ID_TEXT_HARDWARE_PRIMARY_OA_IPV6, expect_value, timeout, fail_if_false)

    # }

    # { Firmware
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_firmware_row_exist(cls, name, timeout=5, fail_if_false=True):
        logger.debug("verify [ firmware item '%s' ] exist in firmware view")
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TEXT_FIRMWARE_ROW_NAME % name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_firmware_component_1(cls, name, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Component field 1 ] of [ firmware '%s' ] in firmware view, expect value is [ %s ]" % (name, expect_value))
        return FusionUIBase.verify_element_text("Component field 1", GeneralEnclosuresElements.ID_TEXT_FIRMWARE_ROW_COMPONENT_1 % (name, name), expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_firmware_component_2(cls, name, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Component field 2 ] of [ firmware '%s' ] in firmware view, expect value is [ %s ]" % (name, expect_value))
        return FusionUIBase.verify_element_text("Component field 2", GeneralEnclosuresElements.ID_TEXT_FIRMWARE_ROW_COMPONENT_2, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_firmware_installed_1(cls, name, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Installed field 1 ] of [ firmware '%s' ] in firmware view, expect value is [ %s ]" % (name, expect_value))
        return FusionUIBase.verify_element_text("Installed field 1", GeneralEnclosuresElements.ID_TEXT_FIRMWARE_ROW_INSTALLED_1 % (name, name), expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_firmware_installed_2(cls, name, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Installed field 2 ] of [ firmware '%s' ] in firmware view, expect value is [ %s ]" % (name, expect_value))
        return FusionUIBase.verify_element_text("Installed field 2", GeneralEnclosuresElements.ID_TEXT_FIRMWARE_ROW_INSTALLED_2 % (name, name), expect_value, timeout, fail_if_false)
    # }

    # { Fans
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_fan_fans_required(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Fans required ] in fans view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Fan required", GeneralEnclosuresElements.ID_TEXT_FANS_FANS_REQUIRED, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_fan_device_bays_cooled(cls, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ Fan device bays cooled ] in fans view, expect value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Fan device bays cooled", GeneralEnclosuresElements.ID_TEXT_FANS_DEVICE_BAYS_COOLED, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_fan_model(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ fan model ] of bay '%s' in fans view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Fan model", GeneralEnclosuresElements.ID_TEXT_FANS_ROW_MODEL % bay_no, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_fan_part_number(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ fan part number ] of bay '%s' in fans view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Fan part number", GeneralEnclosuresElements.ID_TEXT_FANS_ROW_PART_NUMBER % bay_no, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_fan_spare_part_number(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ fan spare part number ] of bay '%s' in fans view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Fan spare part number", GeneralEnclosuresElements.ID_TEXT_FANS_ROW_SPARE_PART_NUMBER % bay_no, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_fan_state(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ fan state ] of bay '%s' in fans view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Fan state", GeneralEnclosuresElements.ID_TEXT_FANS_ROW_STATE % bay_no, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_fan_required(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ fan required ] of bay '%s' in fans view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Fan required", GeneralEnclosuresElements.ID_TEXT_FANS_ROW_REQUIRED % bay_no, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_migrate_error_text_not_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("verifying [ Error migration message ] not shown")
        if ui_lib.wait_for_element_notvisible(GeneralEnclosuresElements.ID_TEXT_ERROR_MIGRATE_REPORT_MESSAGE, timeout, fail_if_false):
            return True
        else:
            error_msg = ui_lib.get_text(GeneralEnclosuresElements.ID_TEXT_ERROR_MIGRATE_REPORT_MESSAGE, timeout, fail_if_false)
            return False, error_msg


class TBirdVerifyEnclosures(_BaseVerifyEnclosures):

    # { Fans

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_fan_part_number(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ fan part number ] of bay '%s' in fans view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Fan part number", GeneralEnclosuresElements.ID_TEXT_TBIRD_FANS_ROW_PART_NUMBER % bay_no, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_fan_serial_number(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ fan serial number ] of bay '%s' in fans view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Fan serial number", GeneralEnclosuresElements.ID_TEXT_TBIRD_FANS_ROW_SERIAL_NUMBER % bay_no, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_fan_spare_part_number(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ fan spare part number ] of bay '%s' in fans view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Fan spare part number", GeneralEnclosuresElements.ID_TEXT_TBIRD_FANS_ROW_SPARE_PART_NUMBER % bay_no, expect_value, timeout, fail_if_false)
    # }

    # { cim
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_cim_bay_exist(cls, bay_no, timeout=5, fail_if_false=True):
        logger.debug("verify [ cim bay '%s' ] exist in Composable Infrastructure Appliances view" % bay_no)
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TEXT_TBIRD_CIM_ROW_BAY % bay_no, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_cim_status(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ cim bay status ] of bay '%s' in Composable Infrastructure Appliances view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Bay status", GeneralEnclosuresElements.ID_TEXT_TBIRD_CIM_ROW_STATUS % bay_no, expect_value, timeout, fail_if_false, True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_cim_model(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ cim bay model ] of bay '%s' in Composable Infrastructure Appliances view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Bay model", GeneralEnclosuresElements.ID_TEXT_TBIRD_CIM_ROW_MODEL % bay_no, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_cim_power(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ cim bay power ] of bay '%s' in Composable Infrastructure Appliances view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Bay power", GeneralEnclosuresElements.ID_TEXT_TBIRD_CIM_ROW_POWER % bay_no, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_cim_serial_number(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ cim bay serial number ] of bay '%s' in Composable Infrastructure Appliances view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Bay serial number", GeneralEnclosuresElements.ID_TEXT_TBIRD_CIM_ROW_SERIAL_NUMBER % bay_no, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_cim_part_number(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ cim bay part number ] of bay '%s' in Composable Infrastructure Appliances view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Bay part number", GeneralEnclosuresElements.ID_TEXT_TBIRD_CIM_ROW_PART_NUMBER % bay_no, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_cim_spare_part_number(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ cim bay spare part number ] of bay '%s' in Composable Infrastructure Appliances view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Bay spare part number", GeneralEnclosuresElements.ID_TEXT_TBIRD_CIM_ROW_SPARE_PART_NUMBER % bay_no, expect_value, timeout, fail_if_false)
    # }

    # { link module
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_link_module_bay_empty(cls, bay_no, timeout=5, fail_if_false=True):
        logger.debug("verify [ link module bay '%s' ] empty in Link Modules view" % bay_no)
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TEXT_TBIRD_LINKED_MODULES_BAY_EMPTY % bay_no, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_link_module_bay_ok_status(cls, bay_no, timeout=5, fail_if_false=True):
        logger.debug("verify [ link module bay '%s' ] in Link Modules view is 'ok'" % bay_no)
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TEXT_TBIRD_LINKED_MODULES_BAY_OK_STATUS % bay_no, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_link_module_bay_exist(cls, bay_no, timeout=5, fail_if_false=True):
        logger.debug("verify [ link module bay '%s' ] exist in Link Modules view" % bay_no)
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TEXT_TBIRD_LINKED_MODULES_ROW_BAY % bay_no, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_link_module_status(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ link module bay status ] of bay '%s' in Link Modules view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Bay status", GeneralEnclosuresElements.ID_TEXT_TBIRD_LINKED_MODULES_ROW_STATUS % bay_no, expect_value, timeout, fail_if_false, True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_link_module_model(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ link module bay model ] of bay '%s' in Link Modules view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Bay model", GeneralEnclosuresElements.ID_TEXT_TBIRD_LINKED_MODULES_ROW_MODEL % bay_no, expect_value, timeout, fail_if_false, True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_link_module_state(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ link module bay state ] of bay '%s' in Link Modules view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Bay state", GeneralEnclosuresElements.ID_TEXT_TBIRD_LINKED_MODULES_ROW_STATE % bay_no, expect_value, timeout, fail_if_false, True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_link_module_mgmt_port_state(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ link module bay mgmt port state ] of bay '%s' in Link Modules view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Bay mgmt port state", GeneralEnclosuresElements.ID_TEXT_TBIRD_LINKED_MODULES_ROW_MGMT_PORT_STATE % bay_no, expect_value, timeout, fail_if_false, True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_link_module_link_port_state(cls, bay_no, expect_value, timeout=5, fail_if_false=True):
        logger.debug("verify [ link module bay link port state ] of bay '%s' in Link Modules view, expect value is [ %s ]" % (bay_no, expect_value))
        return FusionUIBase.verify_element_text("Bay link port state", GeneralEnclosuresElements.ID_TEXT_TBIRD_LINKED_MODULES_ROW_LINK_PORT_STATE % bay_no, expect_value, timeout, fail_if_false, True)

    @classmethod
    def verify_interconnect_bayset_option(cls, bayset, timeout=10, fail_if_false=True):
        logger.debug("verify [ interconnect bay set ] value")
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TEXT_INTERCONNECT_BAYSET_DROPDOWN % bayset, timeout, fail_if_false)

    @classmethod
    def verify_view_side_option(cls, viewside, timeout=10, fail_if_false=True):
        logger.debug("verify [ View side ] dropdown value")
        return ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TEXT_VIEWSIDE_DROPDOWN % viewside, timeout, fail_if_false)
    # }


class _BaseEditScopeForEnclosures(object):

    """
    This class holds all edit scope operation of enclosure
    It can work with C7000 & TBird
    """

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_edit_scope_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Click [ Edit ] button on enclosure scope page")
        if ui_lib.wait_for_element(EditScopeElements.ID_BUTTON_EDIT, timeout=timeout, fail_if_false=fail_if_false) \
                and ui_lib.wait_for_element_visible(EditScopeElements.ID_HEADER_SCOPE, timeout=timeout, fail_if_false=fail_if_false)\
                and ui_lib.wait_for_element_notvisible(EditScopeElements.ID_TEXT_SCOPE_NOT_LOAD, timeout=timeout, fail_if_false=fail_if_false):
            ui_lib.find_element_and_move(EditScopeElements.ID_HEADER_SCOPE)
            ui_lib.wait_for_element_visible(EditScopeElements.ID_BUTTON_EDIT, timeout=timeout, fail_if_false=fail_if_false)
            ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_EDIT, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_scope_dialog_open(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Edit ] dialog open")
        return ui_lib.wait_for_element_visible(EditScopeElements.ID_DIALOG_EDIT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_scope_dialog_close(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Edit ] dialog close")
        return ui_lib.wait_for_element_notvisible(EditScopeElements.ID_DIALOG_EDIT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_assign_scope_dialog_open(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Assign to Scopes ] dialog open")
        return ui_lib.wait_for_element_visible(EditScopeElements.ID_DIALOG_ASSIGN, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_assign_scope_dialog_close(cls, timeout=5, fail_if_false=True):
        logger.debug("wait [ Assign to Scopes ] dialog close")
        return ui_lib.wait_for_element_notvisible(EditScopeElements.ID_DIALOG_ASSIGN, timeout, fail_if_false)

    @classmethod
    def click_ok_button(cls, timeout=5):
        logger.debug("click [ OK ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_OK, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    def click_close_button(cls, timeout=5):
        logger.debug("click [ Close ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_CLOSE, timeout, fail_if_false=True)

    @classmethod
    def click_assign_button(cls, timeout=5):
        logger.debug("click [ Assign ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_ASSIGN, timeout, fail_if_false=True)

    @classmethod
    def click_add_button(cls, timeout=5):
        logger.debug("click [ Add ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_ADD, timeout, fail_if_false=True)

    @classmethod
    def click_add_plus_button(cls, timeout=5):
        logger.debug("click [ Add+ ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_ADD_PLUS, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_assign_button(cls, timeout=5):
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_CANCEL_ASSIGN, timeout, fail_if_false=True)

    @classmethod
    def input_scope_name(cls, name, wait_timeout=5):
        logger.debug("input scope name '%s'" % name)
        ui_lib.wait_for_element_and_input_text(EditScopeElements.ID_INPUT_SEARCH_TEXT, name, wait_timeout, fail_if_false=True)

    @classmethod
    def click_scope_name(cls, name, wait_timeout=5):
        logger.debug("click scope name '%s'" % name)
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_TABLE_SCOPE_NAME % name, wait_timeout, fail_if_false=True)

    @classmethod
    def click_remove_scope_icon(cls, name, wait_timeout=5):
        logger.debug("click to remove scope '%s'" % name)
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_TABLE_REMOVE_SCOPE % name, wait_timeout, fail_if_false=True)


class EditScopeForEnclosures(_BaseEditScopeForEnclosures):
    pass


class C7000EditScopeForEnclosures(_BaseEditScopeForEnclosures):
    pass


class TBirdEditScopeForEnclosures(_BaseEditScopeForEnclosures):
    pass

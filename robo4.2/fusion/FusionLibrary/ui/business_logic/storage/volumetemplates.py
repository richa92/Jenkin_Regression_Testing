'''
    Methods used by Volume templates
'''
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.storage.volumetemplates_elements import GeneralVolumeTemplateElements
from FusionLibrary.ui.business_logic.storage.volumetemplates_elements import CreateVolumeTemplateElements
from FusionLibrary.ui.business_logic.storage.volumetemplates_elements import EditVolumeTemplateElements
from FusionLibrary.ui.business_logic.storage.volumetemplates_elements import EditVolumeTemplateSettingsElements
from FusionLibrary.ui.business_logic.storage.volumetemplates_elements import DeleteVolumeTemplateElements
from FusionLibrary.ui.business_logic.base import FusionUIBase
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco
from RoboGalaxyLibrary.utilitylib import logging as logger
from datetime import datetime


class CommonOperationVolumeTemplates(object):
    '''
        Common Volume  methods
    '''
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_volume_template_not_exist(cls, volume_template, timeout=5, fail_if_false=True):
        '''
            Verify that the volume template does not exist
        '''
        logger.debug("verify volume template '%s' is not existing" % volume_template)
        if ui_lib.wait_for_element_notvisible(GeneralVolumeTemplateElements.ID_TABLE_VOLUME_TEMPLATE % volume_template, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_volume_template_exist(cls, volume_template, timeout=5, fail_if_false=True):
        '''
            Verify that the volume template does exist
        '''
        logger.debug("verify volume template '%s' is existing" % volume_template)
        if ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_TABLE_VOLUME_TEMPLATE % volume_template, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_locate_error_exists(cls, timeout=5, fail_if_false=True):
        '''
            Verify unable to locate error exists
        '''
        locateerror = "Unable to locate the item you requested."
        logger.debug("verify if '%s' error exists on the screen" % locateerror)
        if ui_lib.is_visible(GeneralVolumeTemplateElements.UNABLE_TO_LOCATE_ERROR % locateerror, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_volume_template_status_ok(cls, volume_template, timeout=5, fail_if_false=True):
        '''
            Verify that the volume template status is OK
        '''
        logger.debug("verify whether volume template %s is ok" % volume_template)
        if ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_STATUS_VOLUME_TEMPLATE_OK % volume_template, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_volume_template_status_warn(cls, volume_template, timeout=5, fail_if_false=True):
        '''
            Verify that the volume template status is WARN
        '''
        logger.debug("verify whether volume template %s is warning" % volume_template)
        if ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_STATUS_VOLUME_TEMPLATE_WARN % volume_template, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_volume_template_status_error(cls, volume_template, timeout=5, fail_if_false=True):
        '''
            Verify that the volume template status is in error
        '''
        logger.debug("verify whether volume template %s is error" % volume_template)
        if ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_STATUS_VOLUME_TEMPLATE_ERROR % volume_template, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def get_volume_template_list(cls, timeout=5):
        '''
            Get list of all volume templates in table
        '''
        logger.debug("get all volume template names from table")
        volume_template_list = []
        if ui_lib.wait_for_element(GeneralVolumeTemplateElements.ID_TABLE_VOLUME_TEMPLATES, timeout):
            volume_template_list = FusionUIBase.get_multi_elements_text(GeneralVolumeTemplateElements.ID_TABLE_VOLUME_TEMPLATES, timeout, fail_if_false=True)
        return volume_template_list

    @classmethod
    def click_volume_template(cls, volume_template, timeout=5):
        '''
            Select a specific volume template on the Volume template Page
        '''
        logger.debug("select volume template %s" % volume_template)
        ui_lib.wait_for_element_and_click(GeneralVolumeTemplateElements.ID_TABLE_VOLUME_TEMPLATE % volume_template, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_volume_template_selected(cls, volume_template, timeout=5, fail_if_false=True):
        '''
            Wait until the volume template is selected
        '''
        logger.debug("waiting for volume template '%s' is selected" % volume_template)
        if ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_TABLE_VOLUME_TEMPLATE_SELECTED % volume_template, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_volume_template_show_not_found(cls, volume_template, timeout=5, fail_if_false=True):
        '''
            Waiting for volume template status to be not found
        '''
        logger.info("waiting for volume template status indicates to 'not found'")
        if ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_TABLE_VOLUME_TEMPLATE_DELETED % volume_template, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def click_action_button(cls, timeout=5):
        '''
            Clicxk action button
        '''
        logger.debug("click action button")
        ui_lib.wait_for_element_and_click(GeneralVolumeTemplateElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_volume_template_status_ok(cls, volume_template, timeout=10, fail_if_false=True):
        '''
            Wait for volume temp[late status to be OK
        '''
        start = datetime.now()
        logger.debug("waiting volume template '%s' status indicates to ok" % volume_template)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_STATUS_VOLUME_TEMPLATE_OK % volume_template, timeout=2, fail_if_false=False):
                logger.debug("volume template '%s' status is ok as expected." % volume_template)
                return True
            elif ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_STATUS_VOLUME_TEMPLATE_WARN % volume_template, timeout=2, fail_if_false=False):
                err_msg = "volume template '%s' status is warning not as expected." % volume_template
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            elif ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_STATUS_VOLUME_TEMPLATE_ERROR % volume_template, timeout=2, fail_if_false=False):
                err_msg = "volume template '%s' status is error not as expected." % volume_template
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            else:
                logger.debug("volume template status is unknown, waiting ...")
                continue
        err_msg = "Timeout to wait for volume template '%s' status indicates to ok." % volume_template
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_volume_template_status_ok_or_warn(cls, volume_template, timeout=10, fail_if_false=True):
        '''
            wait for volume template status to be ok or warn
        '''
        start = datetime.now()
        logger.debug("waiting volume template '%s' status indicates to ok or warning" % volume_template)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_STATUS_VOLUME_TEMPLATE_OK % volume_template, timeout=5, fail_if_false=False):
                logger.debug("volume template '%s' status is ok as expected." % volume_template)
                return True
            elif ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_STATUS_VOLUME_TEMPLATE_WARN % volume_template, timeout=5, fail_if_false=False):
                logger.debug("volume template '%s' status is warning as expected." % volume_template)
                return True
            elif ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_STATUS_VOLUME_TEMPLATE_ERROR % volume_template, timeout=5, fail_if_false=False):
                err_msg = "volume template '%s' status is error not as expected." % volume_template
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            else:
                logger.debug("volume template '%s' status is unknown, waiting ..." % volume_template)
                continue
        err_msg = "Timeout to wait for volume template '%s' status indicates to ok or warn." % volume_template
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_volume_template_status_error(cls, volume_template, timeout=10, fail_if_false=True):
        '''
            wait for volume template status = error
        '''
        start = datetime.now()
        logger.debug("waiting volume template '%s' status indicates to error" % volume_template)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_STATUS_VOLUME_TEMPLATE_OK % volume_template, timeout=5, fail_if_false=False):
                err_msg = "volume template '%s' status is ok not as expected." % volume_template
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            elif ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_STATUS_VOLUME_TEMPLATE_WARN % volume_template, timeout=5, fail_if_false=False):
                logger.debug("volume template '%s' status is warning not as expected." % volume_template)
                return False
            elif ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_STATUS_VOLUME_TEMPLATE_ERROR % volume_template, timeout=5, fail_if_false=False):
                logger.debug("volume template '%s' status is error as expected." % volume_template)
                return True
            else:
                logger.debug("volume template '%s' status is unknown, waiting ..." % volume_template)
                continue
        err_msg = "Timeout to wait for volume template status indicates to error."
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_activity_action_ok(cls, volume_template, timeout=5, fail_if_false=True):
        '''
            Waiting for activity action on volume template page to indicate ok
        '''
        logger.debug("waiting activity action of volume template '%s' indicates to ok" % volume_template)
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_ACTION_OK % volume_template, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_ACTION_TITLE % volume_template)
                logger.debug("activity action '%s' status is ok as expected." % actionname)
                return True
            elif ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_ACTION_WARN % volume_template, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_ACTION_TITLE % volume_template)
                logger.debug("activity action '%s' status is warn not as expected." % actionname)
                ui_lib.wait_for_element_and_click(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_ACTION_WARN % volume_template)
                msg = FusionUIBase.get_multi_elements_text(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_MESSAGE)
                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            elif ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_ACTION_ERROR % volume_template, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_ACTION_TITLE % volume_template)
                logger.debug("activity action '%s' status is error not as expected." % actionname)
                ui_lib.wait_for_element_and_click(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_ACTION_ERROR % volume_template)
                msg = FusionUIBase.get_multi_elements_text(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_MESSAGE)
                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            else:
                if ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_ACTION_TITLE % volume_template):
                    actionname = FusionUIBase.get_text(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_ACTION_TITLE % volume_template)
                else:
                    action_name = 'None'
                logger.debug("activity action '%s' status is unknown, waiting ..." % action_name)
                continue
        err_msg = "Timeout to wait for activity action indicates to completed."
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_activity_edit_settings_ok(cls, timeout=5, fail_if_false=True):
        '''
            Waiting for activity action on edit volume template dialog to indicate ok
        '''
        logger.debug("waiting activity action edit settings indicates to ok")
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_EDIT_SETTINGS_OK, timeout=5, fail_if_false=False):
                logger.debug("activity edit settings status is ok as expected.")
                return True
            elif ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_EDIT_SETTINGS_WARN, timeout=5, fail_if_false=False):
                logger.debug("activity edit settings status is warn not as expected.")
                ui_lib.wait_for_element_and_click(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_EDIT_SETTINGS_WARN)
                msg = FusionUIBase.get_multi_elements_text(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_MESSAGE)
                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            elif ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_EDIT_SETTINGS_ERROR, timeout=5, fail_if_false=False):
                logger.debug("activity edit settings status is error not as expected.")
                ui_lib.wait_for_element_and_click(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_EDIT_SETTINGS_ERROR)
                msg = FusionUIBase.get_multi_elements_text(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_MESSAGE)
                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            else:
                logger.debug("activity edit settings status is unknown, waiting ...")
                continue
        err_msg = "Timeout to wait for activity edit settings indicates to completed."
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_activity_specify_action_ok(cls, volume_template, action_name, timeout=5, fail_if_false=True):
        '''
            Waiting for activity action on volume template page to indicate ok
        '''
        logger.debug("waiting activity action '%s' of volume template '%s' indicates to ok" % (action_name, volume_template))
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_SPECIFACTION_OK % (action_name, volume_template), timeout=5, fail_if_false=False):
                logger.debug("activity action '%s' status is ok as expected." % action_name)
                return True
            elif ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_SPECIFACTION_WARN % (action_name, volume_template), timeout=5, fail_if_false=False):
                logger.debug("activity action '%s' status is warn not as expected." % action_name)
                ui_lib.wait_for_element_and_click(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_SPECIFACTION_WARN % (action_name, volume_template))
                msg = FusionUIBase.get_multi_elements_text(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_MESSAGE)
                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            elif ui_lib.wait_for_element_visible(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_SPECIFACTION_ERROR % (action_name, volume_template), timeout=5, fail_if_false=False):
                logger.debug("activity action '%s' status is error not as expected." % action_name)
                ui_lib.wait_for_element_and_click(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_SPECIFACTION_ERROR % (action_name, volume_template))
                msg = FusionUIBase.get_multi_elements_text(GeneralVolumeTemplateElements.ID_TEXT_ACTIVITY_MESSAGE)
                if fail_if_false is False:
                    logger.warn(msg)
                    return False
                else:
                    ui_lib.fail_test(msg)
            else:
                logger.debug("activity action '%s' status is unknown, waiting ..." % action_name)
                continue
        err_msg = "Timeout to wait for activity action '%s' indicates to completed." % action_name
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_storage_system_link(cls, timeout=5):
        '''
            Click storage system link on Volume Template Page
        '''
        logger.debug("Click storage system link on volume template screen")
        ui_lib.wait_for_element_and_click(GeneralVolumeTemplateElements.ID_LINK_STORAGE_SYSTEMS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_storage_pool_link(cls, timeout=5):
        '''
            Click storage pool link on Volume Template Page
        '''
        logger.debug("Click storage pool link on volume template screen")
        ui_lib.wait_for_element_and_click(GeneralVolumeTemplateElements.ID_LINK_STORAGE_POOLS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_storage_volume_link(cls, timeout=5):
        '''
            Click storage volume link on Volume Template Page
        '''
        logger.debug("Click storage volume link on volume template screen")
        ui_lib.wait_for_element_and_click(GeneralVolumeTemplateElements.ID_LINK_STORAGE_VOLUMES, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_volume_template_title(cls, volumetemplate, timeout=10, fail_if_false=True):
        '''
            Verify the title of the page is volume templates on Volume Template Page
        '''
        logger.info('verifying [ Volume Template title= %s ] is visible' % volumetemplate)
        ui_lib.wait_for_element(GeneralVolumeTemplateElements.ID_PAGE_LABEL, timeout=timeout, fail_if_false=fail_if_false)


class CreateVolumeTemplates(object):
    '''
            Create Volume Template methods
    '''

    e = CreateVolumeTemplateElements

    @classmethod
    def click_create_volume_template_button(cls, timeout=5):
        '''
            On the Volume Templates Page, click create volume template button
        '''
        logger.debug("click create volume template button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_VOLUME_TEMPLATE, timeout, fail_if_false=True)
        if not cls.wait_create_volume_template_dialog_shown(fail_if_false=False):
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_VOLUME_TEMPLATE, timeout, fail_if_false=True)

    @classmethod
    def select_actions_add(cls, timeout=5):
        '''
            On the Volume Templates Page, in the action menu select add
        '''
        logger.debug("select add")
        ui_lib.wait_for_element_and_click(GeneralVolumeTemplateElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_ACTION_CREATE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_volume_template_dialog_shown(cls, timeout=5, fail_if_false=True):
        '''
            Wait for the create volume template dialog to appear
        '''
        logger.debug("waiting for add volume template dialog to shown up")
        if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_CREATE_VOLUME_TEMPLATE, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def input_name(cls, name, timeout=5):
        '''
            On the Create Volume Templates Dialog, input the volume template name
        '''
        logger.debug("input name '%s'" % name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def input_description(cls, description, timeout=5):
        '''
            On the Create Volume Templates Dialog, input the description
        '''
        logger.debug("input description '%s'" % description)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_DESCRIPTION, description, timeout, fail_if_false=True)

    @classmethod
    def input_select_storage_pool(cls, storage_pool, storage_system='', timeout=5):
        '''
            On the Create Volume Templates Dialog, select the storage pool
        '''
        logger.debug("input storage pool '%s' of storage system '%s' " % (storage_pool, storage_system))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_STORAGE_POOL, storage_pool, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_STORAGE_POOL % (storage_system, storage_pool), timeout, fail_if_false=True)

    @classmethod
    def input_select_snapshot_storage_pool(cls, snapshot_storage_pool, snapshot_storage_system='', timeout=5):
        '''
            On the Create Volume Templates Dialog, select the snapshot pool
        '''
        logger.debug("input snapshot storage pool '%s' of storage system '%s'" % (snapshot_storage_pool, snapshot_storage_system))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SNAPSHOT_STORAGE_POOL, snapshot_storage_pool, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_SNAPSHOT_STORAGE_POOL % (snapshot_storage_system, snapshot_storage_pool), timeout, fail_if_false=True)

    @classmethod
    def select_volume_properties_section(cls, timeout=5):
        '''
            On the Create Volume Templates Dialog, select the volume properties section
        '''
        logger.debug("select volume properties section")
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_PANEL_SELECTOR, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_PANEL_VOLUME_PROPERTIES, timeout, fail_if_false=True)

    @classmethod
    def input_capacity(cls, capacity, timeout=5):
        '''
            On the Create Volume Templates Dialog, input the capacity
        '''
        logger.debug("input capacity '%s'" % capacity)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_CAPACITY, capacity, timeout, fail_if_false=True)

    @classmethod
    def lock_capacity(cls, timeout=5):
        '''
            On the Create Volume Templates Dialog, click the unlock icon for capacity
        '''
        logger.debug("click the 'unlocked' icon of 'Capacity'")
        if ui_lib.wait_for_element_visible(cls.e.ID_ICON_CAPACITY_LOCKED, timeout=timeout, fail_if_false=False):
            logger.warn("the lock icon of 'Capacity' is already 'locked', skipped")
        else:
            ui_lib.wait_for_element_and_click(cls.e.ID_ICON_CAPACITY_UNLOCKED, timeout=timeout, fail_if_false=True)

    @classmethod
    def unlock_capacity(cls, timeout=5):
        '''
            On the Create Volume Templates Dialog, click the lock icon for capacity
        '''
        logger.debug("click the 'locked' icon of 'Capacity'")
        if ui_lib.wait_for_element_visible(cls.e.ID_ICON_CAPACITY_UNLOCKED, timeout=timeout, fail_if_false=False):
            logger.warn("the lock icon of 'Capacity' is already 'unlocked', skipped")
        else:
            ui_lib.wait_for_element_and_click(cls.e.ID_ICON_CAPACITY_LOCKED, timeout=timeout, fail_if_false=True)

    @classmethod
    def lock_sharing(cls, timeout=5):
        '''
            On the Create Volume Templates Dialog, click the unlock icon for sharing
        '''
        logger.debug("click the 'unlocked' icon of 'Sharing'")
        if ui_lib.wait_for_element_visible(cls.e.ID_ICON_SHARING_LOCKED, timeout=timeout, fail_if_false=False):
            logger.warn("the lock icon of 'Sharing' is already 'locked', skipped")
        else:
            ui_lib.wait_for_element_and_click(cls.e.ID_ICON_SHARING_UNLOCKED, timeout=timeout, fail_if_false=True)

    @classmethod
    def unlock_sharing(cls, timeout=5):
        '''
            On the Create Volume Templates Dialog, click the lock icon for sharing
        '''
        logger.debug("click the 'locked' icon of 'Sharing'")
        if ui_lib.wait_for_element_visible(cls.e.ID_ICON_SHARING_UNLOCKED, timeout=timeout, fail_if_false=False):
            logger.warn("the lock icon of 'Sharing' is already 'unlocked', skipped")
        else:
            ui_lib.wait_for_element_and_click(cls.e.ID_ICON_SHARING_LOCKED, timeout=timeout, fail_if_false=True)

    @classmethod
    def lock_provisioning(cls, timeout=5):
        '''
            On the Create Volume Templates Dialog, click the unlock icon for provisioning
        '''
        logger.debug("click the 'unlocked' icon of 'Provisioning'")
        if ui_lib.wait_for_element_visible(cls.e.ID_ICON_PROVISIONING_LOCKED, timeout=timeout, fail_if_false=False):
            logger.warn("the lock icon of 'Provisioning' is already 'locked', skipped")
        else:
            ui_lib.wait_for_element_and_click(cls.e.ID_ICON_PROVISIONING_UNLOCKED, timeout=timeout, fail_if_false=True)

    @classmethod
    def unlock_provisioning(cls, timeout=5):
        '''
            On the Create Volume Templates Dialog, click the lock icon for provisioning
        '''
        logger.debug("click the 'locked' icon of 'Provisioning'")
        if ui_lib.wait_for_element_visible(cls.e.ID_ICON_PROVISIONING_UNLOCKED, timeout=timeout, fail_if_false=False):
            logger.warn("the lock icon of 'Provisioning' is already 'unlocked', skipped")
        else:
            ui_lib.wait_for_element_and_click(cls.e.ID_ICON_PROVISIONING_LOCKED, timeout=timeout, fail_if_false=True)

    @classmethod
    def lock_snapshot_pool(cls, timeout=5):
        '''
            On the Create Volume Templates Dialog, click the unlock icon for snapshot pool
        '''
        logger.debug("click the 'unlocked' icon of 'Snapshot storage pool'")
        if ui_lib.wait_for_element_visible(cls.e.ID_ICON_SNAPSHOT_POOL_LOCKED, timeout=timeout, fail_if_false=False):
            logger.warn("the lock icon of 'Snapshot storage pool' is already 'locked', skipped")
        else:
            ui_lib.wait_for_element_and_click(cls.e.ID_ICON_SNAPSHOT_POOL_UNLOCKED, timeout=timeout, fail_if_false=True)

    @classmethod
    def unlock_snapshot_pool(cls, timeout=5):
        '''
            On the Create Volume Templates Dialog, click the lock icon for snapshot pool
        '''
        logger.debug("click the 'locked' icon of 'Snapshot storage pool'")
        if ui_lib.wait_for_element_visible(cls.e.ID_ICON_SNAPSHOT_POOL_UNLOCKED, timeout=timeout, fail_if_false=False):
            logger.warn("the lock icon of 'Snapshot storage pool' is already 'unlocked', skipped")
        else:
            ui_lib.wait_for_element_and_click(cls.e.ID_ICON_SNAPSHOT_POOL_LOCKED, timeout=timeout, fail_if_false=True)

    @classmethod
    def select_provisioning(cls, provisioning, timeout=5):
        '''
            On the Create Volume Templates Dialog, select provisioning
        '''
        logger.debug("select provisioning '%s'" % provisioning)
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_PROVISIONING, timeout, fail_if_false=True)
        if provisioning.lower() == 'full':
            ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_PROVISIONING_FULL, timeout, fail_if_false=True)
        elif provisioning.lower() == 'thin':
            ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_PROVISIONING_THIN, timeout, fail_if_false=True)
        else:
            ui_lib.fail_test("Invalid provisioning value '%s', please specify 'Thin' or 'Full'" % provisioning)

    @classmethod
    def choose_sharing(cls, sharing, timeout=5):
        '''
            On the Create Volume Templates Dialog, select the shared value of private or shared
        '''
        logger.debug("choose sharing '%s'" % sharing)
        if sharing.lower() == 'private':
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SHARING_PRIVATE, timeout, fail_if_false=True)
        elif sharing.lower() == 'shared':
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SHARING_SHARED, timeout, fail_if_false=True)
        else:
            ui_lib.fail_test("Invalid sharing value '%s', please specify 'Private' or 'Shared'" % sharing)

    @classmethod
    def choose_data_protection_level(cls, data_protection_level, timeout=5):
        '''
            On the Create Volume Templates Dialog, choose the data protection level
        '''
        logger.debug("choose data protection level '%s'" % data_protection_level)
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_DATA_PROTECTION_LEVEL, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_DATA_PROTECTION_LEVEL % data_protection_level, timeout,
                                          fail_if_false=True)

    @classmethod
    def choose_permit_adaptive_optimization(cls, permitAdaptiveOptimization, timeout=10):
        '''
            On the Create Volume Templates Dialog, choose the permit adaptive optimization
        '''
        logger.debug("permit adaptive optimization '%s'" % permitAdaptiveOptimization)
        FusionUIBase.toggle_button(cls.e.ID_TOGGLE_ADAPTIVE_OPTIMIZATION, permitAdaptiveOptimization, timeout)

    @classmethod
    def choose_performance_policy(cls, performance_policy, timeout=5):
        '''
            On the Create Volume Templates Dialog, choose the performance policy
        '''
        logger.debug("choose performance policy '%s'" % performance_policy)
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_PERFORMANCE_POLICY, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_PERFORMANCE_POLICY % performance_policy, timeout,
                                          fail_if_false=True)

    @classmethod
    def choose_volume_set(cls, volume_set, timeout=5):
        '''
            On the Create Volume Templates Dialog, choose the volume set
        '''
        logger.debug("choose volume set '%s'" % volume_set)
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_VOLUME_SET, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_VOLUME_SET % volume_set, timeout, fail_if_false=True)

    @classmethod
    def choose_folder(cls, folder, timeout=5):
        '''
            On the Create Volume Templates Dialog, choose the folder
        '''
        logger.debug("choose folder '%s'" % folder)
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_FOLDER, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_FOLDER % folder, timeout, fail_if_false=True)

    @classmethod
    def click_create_button(cls, timeout=5):
        '''
            On the Create Volume Templates Dialog, click the create button
        '''
        logger.debug("click create button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE, timeout, fail_if_false=True)

    @classmethod
    def click_create_plus_button(cls, timeout=5):
        '''
            On the Create Volume Templates Dialog, click the create plus button
        '''
        logger.debug("click create+ button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_PLUS, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        '''
            On the Create Volume Templates Dialog, click the cancel button
        '''
        logger.debug("click cancel button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_volume_template_dialog_disappear(cls, timeout=5, fail_if_false=True):
        '''
            Wait for the create volume template dialog to disappear
        '''
        logger.debug("waiting for create volume template dialog to disappear")
        if ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_CREATE_VOLUME_TEMPLATE, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_creating_message_shown(cls, timeout=5, fail_if_false=True):
        '''
            Wait for the creating template message to be shown
        '''
        logger.debug("waiting for creating volume template message to show up")
        if ui_lib.wait_for_element_visible(cls.e.ID_TEXT_CREATING_VOLUME_TEMPLATE, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_creating_message_disappear(cls, timeout=5, fail_if_false=True):
        '''
            Wait for the creating volume template message to disappear
        '''
        logger.debug("waiting for creating volume template message disappear")
        if ui_lib.wait_for_element_notvisible(cls.e.ID_TEXT_CREATING_VOLUME_TEMPLATE, timeout, fail_if_false):
            return True
        else:
            return False


class EditVolumeTemplates(object):
    '''
        Edit Volume Template methods
    '''
    e = EditVolumeTemplateElements

    @classmethod
    def select_actions_edit(cls, timeout=5):
        '''
            On the Volume Template page, click the action button and select edit
        '''
        logger.debug("select edit")
        ui_lib.wait_for_element_and_click(GeneralVolumeTemplateElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditVolumeTemplateElements.ID_SELECT_ACTION_EDIT, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_dialog_shown(cls, timeout=5, fail_if_false=True):
        '''
            Wait for the edit volume template dialog to disappear
        '''
        logger.debug("waiting for edit dialog to show up")
        if ui_lib.wait_for_element_visible(EditVolumeTemplateElements.ID_DIALOG_EDIT, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def input_name(cls, name, timeout=5):
        '''
            On the Edit volume template Dialog, input the name
        '''
        logger.debug("input name '%s'" % name)
        ui_lib.wait_for_element_and_input_text(EditVolumeTemplateElements.ID_INPUT_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def input_description(cls, description, timeout=5):
        '''
            On the Edit volume template Dialog, input the description
        '''
        logger.debug("input description '%s'" % description)
        ui_lib.wait_for_element_and_input_text(EditVolumeTemplateElements.ID_INPUT_DESCRIPTION, description, timeout, fail_if_false=True)

    @classmethod
    def input_select_storage_pool(cls, storage_pool, storage_system, timeout=5):
        '''
            On the Edit volume template Dialog, input the storage pool to select
        '''
        logger.debug("input storage pool '%s' of storage system '%s'" % (storage_pool, storage_system))
        ui_lib.wait_for_element_and_input_text(EditVolumeTemplateElements.ID_INPUT_STORAGE_POOL, storage_pool, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditVolumeTemplateElements.ID_SELECT_STORAGE_POOL % (storage_system, storage_pool), timeout, fail_if_false=True)

    @classmethod
    def input_select_snapshot_storage_pool(cls, snapshot_storage_pool, snapshot_storage_system, timeout=5):
        '''
            On the Edit volume template Dialog, input the snapshot pool to select
        '''
        logger.debug("input snapshot storage pool '%s' of storage system '%s'" % (snapshot_storage_pool, snapshot_storage_system))
        ui_lib.wait_for_element_and_input_text(EditVolumeTemplateElements.ID_INPUT_SNAPSHOT_STORAGE_POOL, snapshot_storage_pool, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditVolumeTemplateElements.ID_SELECT_SNAPSHOT_STORAGE_POOL % (snapshot_storage_system, snapshot_storage_pool), timeout, fail_if_false=True)

    @classmethod
    def select_volume_properties_section(cls, timeout=5):
        '''
            On the Edit volume template Dialog, select the volume properties section
        '''
        logger.debug("select volume properties section")
        ui_lib.wait_for_element_and_click(EditVolumeTemplateElements.ID_DROPDOWN_PANEL_SELECTOR, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditVolumeTemplateElements.ID_SELECT_PANEL_VOLUME_PROPERTIES, timeout, fail_if_false=True)

    @classmethod
    def input_capacity(cls, capacity, timeout=5):
        '''
            On the Edit volume template Dialog, input the capacity
        '''
        logger.debug("input capacity '%s'" % capacity)
        ui_lib.wait_for_element_and_input_text(EditVolumeTemplateElements.ID_INPUT_CAPACITY, capacity, timeout, fail_if_false=True)

    @classmethod
    def select_provisioning(cls, provisioning, timeout=5):
        '''
            On the Edit volume template Dialog, select the provisioning
        '''
        logger.debug("select provisioning '%s'" % provisioning)
        ui_lib.wait_for_element_and_click(EditVolumeTemplateElements.ID_DROPDOWN_PROVISIONING, timeout, fail_if_false=True)
        if provisioning.lower() == 'full':
            ui_lib.wait_for_element_and_click(EditVolumeTemplateElements.ID_SELECT_PROVISIONING_FULL, timeout, fail_if_false=True)
        elif provisioning.lower() == 'thin':
            ui_lib.wait_for_element_and_click(EditVolumeTemplateElements.ID_SELECT_PROVISIONING_THIN, timeout, fail_if_false=True)
        else:
            ui_lib.fail_test("Invalid provisioning value '%s', please specify 'Thin' or 'Full'" % provisioning)

    @classmethod
    def choose_sharing(cls, sharing, timeout=5):
        '''
            On the Edit volume template Dialog, choose the sharing of private or shared
        '''
        logger.debug("choose sharing '%s'" % sharing)
        if sharing.lower() == 'private':
            ui_lib.wait_for_element_and_click(EditVolumeTemplateElements.ID_RADIO_SHARING_PRIVATE, timeout, fail_if_false=True)
        elif sharing.lower() == 'shared':
            ui_lib.wait_for_element_and_click(EditVolumeTemplateElements.ID_RADIO_SHARING_SHARED, timeout, fail_if_false=True)
        else:
            ui_lib.fail_test("Invalid sharing value '%s', please specify 'Private' or 'Shared'" % sharing)

    @classmethod
    def choose_data_protection_level(cls, data_protection_level, timeout=5):
        '''
            On the Edit volume template Dialog, choose data protection level
        '''
        logger.debug("choose data protection level '%s'" % data_protection_level)
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_DATA_PROTECTION_LEVEL, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_DATA_PROTECTION_LEVEL % data_protection_level, timeout,
                                          fail_if_false=True)

    @classmethod
    def choose_folder(cls, folder, timeout=5):
        '''
            On the Edit volume template Dialog, choose folder
        '''
        logger.debug("Get [ Folder field into view point ]")
        ui_lib.select_from_dropdown_by_text(cls.e.ID_DROPDOWN_PANEL_SELECTOR, "Advanced")
        logger.debug("choose folder '%s'" % folder)
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_FOLDER, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_FOLDER % folder, timeout,
                                          fail_if_false=True)

    @classmethod
    def choose_performance_policy(cls, performancepolicy, timeout=5):
        '''
            On the Edit volume template Dialog, choose performance policy
        '''
        logger.debug("choose Performance Policy '%s'" % performancepolicy)
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_PERFORMANCE_POLICY, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_PERFORMANCE_POLICY % performancepolicy, timeout,
                                          fail_if_false=True)

    @classmethod
    def choose_volume_set(cls, volumeset, timeout=5):
        '''
            On the Edit volume template Dialog, choose volume set
        '''
        logger.debug("choose volume set '%s'" % volumeset)
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_VOLUMESET, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_VOLUMESET % volumeset, timeout, fail_if_false=True)

    @classmethod
    def choose_permit_adaptive_optimization(cls, permitAdaptiveOptimization, timeout=10):
        '''
            On the Edit volume template Dialog, choose permit adaptive optimization
        '''
        logger.debug("permit adaptive optimization '%s'" % permitAdaptiveOptimization)
        FusionUIBase.toggle_button(cls.e.ID_TOGGLE_ADAPTIVE_OPTIMIZATION, permitAdaptiveOptimization, timeout)

    @classmethod
    def click_ok_button(cls, timeout=5):
        '''
            On the Edit volume template Dialog, click OK button
        '''
        logger.debug("click 'ok' button")
        ui_lib.wait_for_element_and_click(EditVolumeTemplateElements.ID_BUTTON_OK, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        '''
            On the Edit volume template Dialog, click cancel button
        '''
        logger.debug("click 'cancel' button")
        ui_lib.wait_for_element_and_click(EditVolumeTemplateElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_dialog_disappear(cls, timeout=5, fail_if_false=True):
        '''
            wait for the edit volume template dialog to disappear
        '''
        logger.debug("waiting for edit dialog to disappear")
        if ui_lib.wait_for_element_notvisible(EditVolumeTemplateElements.ID_DIALOG_EDIT, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def lock_template_properties(cls, property_name, timeout=5):
        '''
            On the Edit volume template Dialog, lock a template property
        '''
        logger.debug("lock template property  '%s'" % property_name)
        ui_lib.wait_for_element_and_click(EditVolumeTemplateElements.ID_BUTTON_LOCK_SELECT % property_name, timeout, fail_if_false=True)


class DeleteVolumeTemplates(object):
    '''
        Delete Volume Templates dialog
    '''

    @classmethod
    def select_actions_delete(cls, timeout=5):
        '''
            On the Volume Templates Page, click actions and select delete
        '''
        logger.debug("select delete")
        ui_lib.wait_for_element_and_click(GeneralVolumeTemplateElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(DeleteVolumeTemplateElements.ID_SELECT_ACTION_DELETE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_dialog_shown(cls, timeout=5, fail_if_false=True):
        '''
            wait for the delete volume template dialog to be shown
        '''
        logger.debug("waiting for delete dialog to show up ")
        if ui_lib.wait_for_element_visible(DeleteVolumeTemplateElements.ID_DIALOG_DELETE, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def click_yes_delete_button(cls, timeout=5):
        '''
            On the delete volume template dialog, click yes delete button
        '''
        logger.debug("click 'yes, delete'")
        ui_lib.wait_for_element_and_click(DeleteVolumeTemplateElements.ID_BUTTON_YES_DELETE, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        '''
            On the delete volume template dialog, click cancel button
        '''
        logger.debug("click 'cancel'")
        ui_lib.wait_for_element_and_click(DeleteVolumeTemplateElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_dialog_disappear(cls, timeout=5, fail_if_false=True):
        '''
            wait for the delete volume template dialog to disappear
        '''
        logger.debug("waiting for delete dialog to disappear")
        if ui_lib.wait_for_element_notvisible(DeleteVolumeTemplateElements.ID_DIALOG_DELETE, timeout, fail_if_false):
            return True
        else:
            return False


class EditVolumeTemplatesSettings(object):
    '''
         Edit Volume Templates Settings methods
    '''
    @classmethod
    def select_actions_edit_settings(cls, timeout=5):
        '''
            On the volume template page, click action button and select edit
        '''
        logger.debug("select edit settings")
        ui_lib.wait_for_element_and_click(GeneralVolumeTemplateElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditVolumeTemplateSettingsElements.ID_SELECT_ACTION_EDIT_SETTINGS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_settings_dialog_shown(cls, timeout=5, fail_if_false=True):
        '''
            wait for the edit volume template settings dialog to appear
        '''
        logger.debug("waiting for edit setting dialog to show up")
        if ui_lib.wait_for_element_visible(EditVolumeTemplateSettingsElements.ID_DIALOG_EDIT_SETTINGS, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def tick_require_template_for_volume_creation(cls, timeout=5):
        '''
            On the edit volume template dialog, check require template for volume creation
        '''
        logger.debug("check require template for volume creation")
        FusionUIBase.wait_for_checkbox_and_select(EditVolumeTemplateSettingsElements.ID_CHECKBOX_REQUIRE_TEMPLATE_FOR_VOLUME_CREATION, timeout, fail_if_false=True)

    @classmethod
    def not_tick_require_template_for_volume_creation(cls, timeout=5):
        '''
            On the edit volume template dialog, uncheck require template for volume creation
        '''
        logger.debug("uncheck require template for volume creation")
        FusionUIBase.wait_for_checkbox_and_unselect(EditVolumeTemplateSettingsElements.ID_CHECKBOX_REQUIRE_TEMPLATE_FOR_VOLUME_CREATION, timeout, fail_if_false=True)

    @classmethod
    def click_ok(cls, timeout=5):
        '''
            On the edit volume template dialog, click OK button
        '''
        logger.debug("click ok")
        ui_lib.wait_for_element_and_click(EditVolumeTemplateSettingsElements.ID_BUTTON_OK, timeout, fail_if_false=True)

    @classmethod
    def click_cancel(cls, timeout=5):
        '''
            On the edit volume template dialog, click cancel button
        '''
        logger.debug("click cancel")
        ui_lib.wait_for_element_and_click(EditVolumeTemplateSettingsElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_settings_dialog_disappear(cls, timeout=5, fail_if_false=True):
        '''
            Wait for the edit volume template setting dialog to disappear
        '''
        logger.debug("waiting for edit settings dialog to disappear")
        if ui_lib.wait_for_element_notvisible(EditVolumeTemplateSettingsElements.ID_DIALOG_EDIT_SETTINGS, timeout, fail_if_false):
            return True
        else:
            return False

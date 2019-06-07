'''
   storage volumes
'''
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.storage.volumes_elements import GeneralVolumeElements
from FusionLibrary.ui.business_logic.storage.volumes_elements import CreateVolumeElements
from FusionLibrary.ui.business_logic.storage.volumes_elements import EditVolumeElements
from FusionLibrary.ui.business_logic.storage.volumes_elements import AddVolumeElements
from FusionLibrary.ui.business_logic.storage.volumes_elements import RefreshVolumeElements
from FusionLibrary.ui.business_logic.storage.volumes_elements import CreateVolumeSnapshotElements
from FusionLibrary.ui.business_logic.storage.volumes_elements import DeleteVolumeSnapshotElements
from FusionLibrary.ui.business_logic.storage.volumes_elements import RevertVolumeSnapshotElements
from FusionLibrary.ui.business_logic.storage.volumes_elements import CreateVolumeUsingSnapshotElements
from FusionLibrary.ui.business_logic.storage.volumes_elements import DeleteVolumeElements
from FusionLibrary.ui.business_logic.base import FusionUIBase
# from FusionLibrary.ui.settings import settings
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco
from RoboGalaxyLibrary.utilitylib import logging as logger
from datetime import datetime
import re
import types


class CommonOperationVolumes(object):
    '''
        Common storage volumes functions
    '''

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_volume_not_exist(cls, volume, timeout=5, fail_if_false=True):
        '''
            verify that the volume does not exist
        '''
        logger.debug("verify volume '%s' is not existing" % volume)
        if ui_lib.wait_for_element_notvisible(GeneralVolumeElements.ID_TABLE_VOLUME % volume, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_volume_exist(cls, volume, timeout=5, fail_if_false=True):
        '''
            verify the volume does exist
        '''
        logger.debug("verify volume '%s' is existing" % volume)
        if ui_lib.wait_for_element_visible(GeneralVolumeElements.ID_TABLE_VOLUME % volume, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_locate_error_exists(cls, timeout=5, fail_if_false=True):
        '''
            verify that the unable to locate error exists
        '''
        locateerror = "Unable to locate the item you requested."
        logger.debug("verify if '%s' error exists on the screen" % locateerror)
        if ui_lib.is_visible(GeneralVolumeElements.UNABLE_TO_LOCATE_ERROR % locateerror, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_volume_status_ok(cls, volume, timeout=5, fail_if_false=True):
        '''
            On the volume page, verify the volume status = ok
        '''
        logger.debug("verify whether volume %s is ok" % volume)
        if ui_lib.wait_for_element_visible(GeneralVolumeElements.ID_STATUS_VOLUME_OK % volume, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_volume_status_warn(cls, volume, timeout=5, fail_if_false=True):
        '''
            On the volume page, verify the volume status = warn
        '''
        logger.debug("verify whether volume %s is warning" % volume)
        if ui_lib.wait_for_element_visible(GeneralVolumeElements.ID_STATUS_VOLUME_WARN % volume, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_volume_status_error(cls, volume, timeout=5, fail_if_false=True):
        '''
            On the volume page, verify the volume status = error
        '''
        logger.debug("verify whether volume %s is error" % volume)
        if ui_lib.wait_for_element_visible(GeneralVolumeElements.ID_STATUS_VOLUME_ERROR % volume, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def get_volume_list(cls, timeout=5):
        '''
            Get the list of volumes on the volume page in oneview
        '''
        logger.debug("get all volume names from table")
        volume_list = []
        if ui_lib.wait_for_element(GeneralVolumeElements.ID_TABLE_VOLUMES, timeout):
            volume_list = FusionUIBase.get_multi_elements_text(GeneralVolumeElements.ID_TABLE_VOLUMES, timeout, fail_if_false=True)
        return volume_list

    @classmethod
    def click_volume(cls, volume, timeout=5):
        '''
            On the volume page, select a specific volume
        '''
        logger.debug("select volume %s" % volume)
        ui_lib.wait_for_element_and_click(GeneralVolumeElements.ID_TABLE_VOLUME % volume, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_volume_selected(cls, volume, timeout=5, fail_if_false=True):
        '''
            On the volume page, wait for the volume to be selected
        '''
        logger.debug("waiting for volume '%s' is selected" % volume)
        if ui_lib.wait_for_element_visible(GeneralVolumeElements.ID_TABLE_VOLUME_SELECTED % volume, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_volume_show_not_found(cls, volume, timeout=5, fail_if_false=True):
        '''
            On the volume page, wait for the volume status of not found
        '''
        logger.info("waiting for volume status indicates to 'not found'")
        if ui_lib.wait_for_element_visible(GeneralVolumeElements.ID_TABLE_VOLUME_DELETED % volume, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def click_action_button(cls, timeout=5):
        '''
            On the volume page, click the action button
        '''
        logger.debug("click action button")
        ui_lib.wait_for_element_and_click(GeneralVolumeElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_volume_status_ok(cls, volume, timeout=10, fail_if_false=True):
        '''
            On the volume page, wait for volume status = OK
        '''
        start = datetime.now()
        logger.debug("waiting for volume '%s' status changes to ok" % volume)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralVolumeElements.ID_STATUS_VOLUME_OK % volume, timeout=2, fail_if_false=False):
                logger.debug("volume '%s' status is ok as expected." % volume)
                return True
            elif ui_lib.wait_for_element_visible(GeneralVolumeElements.ID_STATUS_VOLUME_WARN % volume, timeout=2, fail_if_false=False):
                err_msg = "volume '%s' status is warning not as expected." % volume
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            elif ui_lib.wait_for_element_visible(GeneralVolumeElements.ID_STATUS_VOLUME_ERROR % volume, timeout=2, fail_if_false=False):
                err_msg = "volume '%s' status is error not as expected." % volume
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            else:
                logger.debug("volume status is unknown, waiting ...")
                continue
        err_msg = "Timeout to wait for volume '%s' status indicates to ok." % volume
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_volume_status_ok_or_warn(cls, volume, timeout=10, fail_if_false=True):
        '''
            On the volume page, wait for volume status = OK or warn
        '''
        start = datetime.now()
        logger.debug("waiting for volume '%s' status indicates to ok or warning" % volume)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralVolumeElements.ID_STATUS_VOLUME_OK % volume, timeout=5, fail_if_false=False):
                logger.debug("volume '%s' status is ok as expected." % volume)
                return True
            elif ui_lib.wait_for_element_visible(GeneralVolumeElements.ID_STATUS_VOLUME_WARN % volume, timeout=5, fail_if_false=False):
                logger.debug("volume '%s' status is warning as expected." % volume)
                return True
            elif ui_lib.wait_for_element_visible(GeneralVolumeElements.ID_STATUS_VOLUME_ERROR % volume, timeout=5, fail_if_false=False):
                err_msg = "volume '%s' status is error not as expected." % volume
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            else:
                logger.debug("volume '%s' status is unknown, waiting ..." % volume)
                continue
        err_msg = "Timeout to wait for volume '%s' status indicates to ok or warn." % volume
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_volume_status_error(cls, volume, timeout=10, fail_if_false=True):
        '''
            On the volume page, wait for volume status = error
        '''
        start = datetime.now()
        logger.debug("waiting for volume '%s' status indicates to error" % volume)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralVolumeElements.ID_STATUS_VOLUME_OK % volume, timeout=5, fail_if_false=False):
                err_msg = "volume '%s' status is ok not as expected." % volume
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            elif ui_lib.wait_for_element_visible(GeneralVolumeElements.ID_STATUS_VOLUME_WARN % volume, timeout=5, fail_if_false=False):
                logger.debug("volume '%s' status is warning not as expected." % volume)
                return False
            elif ui_lib.wait_for_element_visible(GeneralVolumeElements.ID_STATUS_VOLUME_ERROR % volume, timeout=5, fail_if_false=False):
                logger.debug("volume '%s' status is error as expected." % volume)
                return True
            else:
                logger.debug("volume '%s' status is unknown, waiting ..." % volume)
                continue
        err_msg = "Timeout to wait for volume status indicates to error."
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    def select_panel_snapshots(cls, timeout=5):
        '''
            On the volume page, select the snapshot panel
        '''
        logger.debug("select Snapshots panel")
        ui_lib.wait_for_element_and_click(GeneralVolumeElements.ID_DROPDOWN_PANEL_SELECTOR, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(GeneralVolumeElements.ID_SELECT_SNAPSHOTS_PANEL, timeout, fail_if_false=True)

    @classmethod
    def get_all_snapshots(cls, timeout=5):
        '''
            On the volume page, get the name of all the snapshots
        '''
        logger.debug("get all snapshot names")
        snapshots = FusionUIBase.get_multi_elements_text(GeneralVolumeElements.ID_TABLE_SNAPSHOTS, timeout, fail_if_false=True)
        return snapshots

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_snapshots_exists(cls, name, timeout=5, fail_if_false=True):
        '''
            verify the snapshots exist
        '''
        name_variables = re.findall(r'\{(.*?)\}', name)
        if len(name_variables) > 0:
            name_process = re.sub(r'\{\w+\s*\w+\}', '*VAR-#*', name)
            name_process = name_process.split('*')
            expect_list = ["volumename", "timestamp"]
            for var in name_variables:
                FusionUIBase.para_should_be_in_list(expect_list, var)
            rexg = name_process
            m = 0
            for n, variable in enumerate(name_process):
                if variable == "VAR-#":
                    if name_variables[m].lower().replace(' ', '') == "volumename":
                        volume_name = FusionUIBase.get_text(GeneralVolumeElements.ID_TABLE_SELECTED_VOLUME_NAME, timeout, fail_if_false=True)
                        rexg[n] = volume_name
                        m += 1
                    elif name_variables[m].lower().replace(' ', '') == "timestamp":
                        rexg[n] = r'\d{14}'
                        m += 1
            rexg = ''.join(rexg)
            snapshots = FusionUIBase.get_multi_elements_text(GeneralVolumeElements.ID_TABLE_SNAPSHOTS, timeout, fail_if_false=True)
            for snapshot in snapshots:
                if re.match(r'^%s$' % rexg, snapshot):
                    return True
            if fail_if_false is True:
                ui_lib.fail_test("could not find snapshot %s" % rexg)
            else:
                logger.warn("could not find snapshot %s" % rexg)
                return False
        else:
            if ui_lib.wait_for_element_visible(GeneralVolumeElements.ID_TABLE_SNAPSHOT_NAME % name, timeout, fail_if_false):
                return True
            else:
                return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storagevolumes_title(cls, storagevolume, timeout=10, fail_if_false=True):
        '''
            verify the storage volume page title
        '''
        logger.info('verifying [ Volumes title= %s ] is visible' % storagevolume)
        ui_lib.wait_for_element(GeneralVolumeElements.ID_PAGE_LABEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_volume_template_link(cls, timeout=5):
        '''
            click the volume template link  on the volumes page
        '''
        logger.debug("Click storage template link on volumes screen")
        ui_lib.wait_for_element_and_click(GeneralVolumeElements.ID_LINK_VOLUME_TEMPLATE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_storage_system_link(cls, timeout=5):
        '''
            click the storage system link  on the volumes page
        '''
        logger.debug("Click storage system link on volumes screen")
        ui_lib.wait_for_element_and_click(GeneralVolumeElements.ID_LINK_STORAGE_SYSTEMS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_storage_pools_link(cls, timeout=5):
        '''
            click the storage pool link  on the volumes page
        '''
        logger.debug("Click storage pools link on volumes screen")
        ui_lib.wait_for_element_and_click(GeneralVolumeElements.ID_LINK_STORAGE_POOLS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_storage_pool_snapshot_link(cls, timeout=5):
        '''
            click the storage pool snapshot link  on the volumes page
        '''
        logger.debug("Click storage pool snapshot link on volumes screen")
        ui_lib.wait_for_element_and_click(GeneralVolumeElements.ID_LINK_SNAPSHOT_POOLS, timeout, fail_if_false=True)


class CreateVolumes(object):
    '''
        Create Volumes functions
    '''

    e = CreateVolumeElements

    @classmethod
    def click_create_volume_button(cls, timeout=5):
        '''
            On the volumes page, click the create volume button
        '''
        logger.debug("click create volume button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_VOLUME, timeout, fail_if_false=True)
        if not cls.wait_create_volume_dialog_shown(fail_if_false=False):
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_VOLUME, timeout, fail_if_false=True)

    @classmethod
    def select_actions_create(cls, timeout=5):
        '''
            On the volumes page, click action menu and select create
        '''
        logger.debug("select Actions -> create")
        ui_lib.wait_for_element_and_click(GeneralVolumeElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_ACTION_CREATE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_volume_dialog_shown(cls, timeout=5, fail_if_false=True):
        '''
            wait for the create volume dialog to be shown
        '''
        logger.debug("waiting for create volume dialog to show up")
        if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_CREATE_VOLUME, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def input_name(cls, name, timeout=5):
        '''
            On the create Volumes Dialog, input the name
        '''
        logger.debug("input name '%s'" % name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def input_description(cls, description, timeout=5):
        '''
            On the create Volumes Dialog, input the description
        '''
        logger.debug("input description '%s'" % description)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_DESCRIPTION, description, timeout, fail_if_false=True)

    @classmethod
    def input_select_volume_template(cls, volume_template, storage_pool='', timeout=5, fail_if_false=True):
        '''
            On the create Volumes Dialog, input the volume template selected
        '''
        logger.debug("input volume template '%s' " % volume_template)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_VOLUME_TEMPLATE, volume_template, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_VOLUME_TEMPLATE % (volume_template, volume_template, storage_pool), timeout, fail_if_false)

    @classmethod
    def input_select_storage_pool(cls, storage_pool, storage_system='', timeout=5, fail_if_false=True):
        '''
            On the create Volumes Dialog, select the storage pool
        '''
        logger.debug("input storage pool '%s' of storage system '%s' " % (storage_pool, storage_system))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_STORAGE_POOL, storage_pool, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_STORAGE_POOL % (storage_pool, storage_pool, storage_system), timeout, fail_if_false)

    @classmethod
    def input_select_snapshot_storage_pool(cls, snapshot_storage_pool, snapshot_storage_system='', timeout=5, fail_if_false=True):
        '''
            On the create Volumes Dialog, select the snaphot pool
        '''
        logger.debug("input snapshot storage pool '%s' of storage system '%s'" % (snapshot_storage_pool, snapshot_storage_system))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_SNAPSHOT_STORAGE_POOL, snapshot_storage_pool, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_SNAPSHOT_STORAGE_POOL % (snapshot_storage_pool, snapshot_storage_pool, snapshot_storage_system), timeout, fail_if_false)

    @classmethod
    def input_capacity(cls, capacity, timeout=5):
        '''
            On the create Volumes Dialog, input the capacity
        '''
        logger.debug("input capacity '%s'" % capacity)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_CAPACITY, capacity, timeout, fail_if_false=True)

    @classmethod
    def select_provisioning(cls, provisioning, timeout=5):
        '''
            On the create Volumes Dialog, input the provisioning
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
    def select_pefpolicy(cls, perfpolicy, timeout=5):
        '''
            On the create Volumes Dialog, select the performance policy
        '''
        logger.debug("select performance policy '%s'" % perfpolicy)
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_PERFPOLICY, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_PERFPOLICY % perfpolicy, timeout, fail_if_false=True)

    @classmethod
    def select_volset(cls, volset, timeout=5):
        '''
            On the create Volumes Dialog, select a volume set
        '''
        logger.debug("select volume set '%s'" % volset)
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_VOLUMESET, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_VOLUMESET % volset, timeout, fail_if_false=True)

    @classmethod
    def select_folder(cls, folder, timeout=5):
        '''
            On the create Volumes Dialog, select a folder
        '''
        logger.debug("select folder '%s'" % folder)
        ui_lib.wait_for_element_and_click(cls.e.ID_DROPDOWN_FOLDER, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_FOLDER % folder, timeout, fail_if_false=True)

    @classmethod
    def select_toggle_iopslimit(cls, timeout=5):
        '''
            On the create Volumes Dialog, enable the iopslimit toggle
        '''
        logger.debug("Enable iopslimit")
        ui_lib.wait_for_element_and_click(cls.e.ID_TOGGLE_IOPSLIMIT, timeout, fail_if_false=True)

    @classmethod
    def select_toggle_datatransferlimit(cls, timeout=5):
        '''
            On the create Volumes Dialog, enable the datatransferlimit toggle
        '''
        logger.debug("Enable datatransferlimit")
        ui_lib.wait_for_element_and_click(cls.e.ID_TOGGLE_DATATRANSFERLIMIT, timeout, fail_if_false=True)

    @classmethod
    def input_iopslimit(cls, iopslimit, timeout=5):
        '''
            On the create Volumes Dialog, input the iopslimit
        '''
        logger.debug("Input iopslimit '%s'" % iopslimit)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_IOPSLIMIT, iopslimit, timeout, fail_if_false=True)

    @classmethod
    def click_iopslimit_label(cls, timeout=5):
        '''
            click outside the iopslimit box on lable on the volumes page
        '''
        logger.debug("Click outside iopslimit box on label")
        ui_lib.wait_for_element_and_click(cls.e.ID_LABEL_IOPSLIMIT, timeout, fail_if_false=True)

    @classmethod
    def input_datatransferlimit(cls, datatransferlimit, timeout=5):
        '''
            On the create Volumes Dialog, input the datatransferlimit
        '''
        logger.debug("Input datatransferlimit '%s'" % datatransferlimit)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_DATATRANSFERLIMIT, datatransferlimit, timeout, fail_if_false=True)

    @classmethod
    def choose_sharing(cls, sharing, timeout=5):
        '''
            On the create Volumes Dialog, choose sharing of private or shared
        '''
        logger.debug("choose sharing '%s'" % sharing)
        if sharing.lower() == 'private':
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SHARING_PRIVATE, timeout, fail_if_false=True)
        elif sharing.lower() == 'shared':
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SHARING_SHARED, timeout, fail_if_false=True)
        else:
            ui_lib.fail_test("Invalid sharing value '%s', please specify 'Private' or 'Shared'" % sharing)

    @classmethod
    def click_create_button(cls, timeout=5):
        '''
            click create button
        '''
        logger.debug("click create button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE, timeout, fail_if_false=True)

    @classmethod
    def click_create_plus_button(cls, timeout=5):
        '''
            On the create Volumes Dialog, click create plus button
        '''
        logger.debug("click create+ button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CREATE_PLUS, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        '''
            On the create Volumes Dialog, click cancel button
        '''
        logger.debug("click cancel button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_volume_dialog_disappear(cls, timeout=5, fail_if_false=True):
        '''
            Wait for create volume dialog to disappear
        '''
        logger.debug("waiting for create volume dialog to disappear")
        if ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_CREATE_VOLUME, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_creating_message_shown(cls, timeout=5, fail_if_false=True):
        '''
            wait for creating volume message to appear
        '''
        logger.debug("waiting for creating volume message to show up")
        if ui_lib.wait_for_element_visible(cls.e.ID_TEXT_CREATING_VOLUME, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_creating_message_disappear(cls, timeout=5, fail_if_false=True):
        '''
            wait for creating volume message to disappear
        '''
        logger.debug("waiting for creating volume message to disappear")
        if ui_lib.wait_for_element_notvisible(cls.e.ID_TEXT_CREATING_VOLUME, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_create_volume_error(cls, expect_value, volume_name, timeout=5, fail_if_false=True):
        '''
            verify that a create volume error appears
        '''
        logger.debug("verify Create Volume Error [ %s ] appears for [ %s ]" % (expect_value, volume_name))
        return FusionUIBase.verify_element_text("Description", CreateVolumeElements.ID_TEXT_CREATE_ERROR_MESSAGE,
                                                expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_iopslimit_error(cls, expect_value, volume_name, timeout=5, fail_if_false=True):
        '''
            verify the iopslimit error appears
        '''
        logger.debug("verify Iopslimit error [ %s ] appears for [ %s ]" % (expect_value, volume_name))
        return FusionUIBase.verify_element_text("Description", cls.e.ID_TEXT_IOPSLIMIT_ERROR_MESSAGE,
                                                expect_value, timeout, fail_if_false)


class EditVolumes(object):
    '''
        Edit Volumes Dialog
    '''

    @classmethod
    def select_actions_edit(cls, timeout=5):
        '''
            On the volumes page, click action menu and select edit
        '''
        logger.debug("select Actions -> edit")
        ui_lib.wait_for_element_and_click(GeneralVolumeElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditVolumeElements.ID_SELECT_ACTION_EDIT, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_dialog_shown(cls, timeout=5, fail_if_false=True):
        '''
            wait for edit volume dialog to appear
        '''
        logger.debug("waiting for edit dialog to show up")
        if ui_lib.wait_for_element_visible(EditVolumeElements.ID_DIALOG_EDIT, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def input_name(cls, name, timeout=5):
        '''
            On the Edit Volume Dialog, input the name
        '''
        logger.debug("input name '%s'" % name)
        ui_lib.wait_for_element_and_input_text(EditVolumeElements.ID_INPUT_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def input_description(cls, description, timeout=5):
        '''
            On the Edit Volume Dialog, input the description
        '''
        logger.debug("input description '%s'" % description)
        ui_lib.wait_for_element_and_input_text(EditVolumeElements.ID_INPUT_DESCRIPTION, description, timeout, fail_if_false=True)

    @classmethod
    def get_storage_pool(cls, timeout=5):
        '''
            get the storage pool
        '''
        logger.debug("get storage pool")
        poolname = FusionUIBase.get_text(EditVolumeElements.ID_TEXT_STORAGE_POOL, timeout=timeout, fail_if_false=True)
        return poolname

    @classmethod
    def input_select_volume_template(cls, volume_template, storage_pool='', timeout=5, fail_if_false=True):
        '''
            On the Edit Volume Dialog, select the volume template
        '''
        logger.debug("input volume template '%s' using storage pool %s " % (volume_template, storage_pool))
        ui_lib.wait_for_element_and_click(EditVolumeElements.ID_DROPDOWN_VOLUME_TEMPLATE, timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(EditVolumeElements.ID_SELECT_VOLUME_TEMPLATE % volume_template, timeout, fail_if_false=fail_if_false)

    @classmethod
    def input_select_snapshot_storage_pool(cls, snapshot_storage_pool, snapshot_storage_system, timeout=5):
        '''
            On the Edit Volume Dialog, select the snapshot pool
        '''
        logger.debug("input snapshot storage pool '%s' of storage system '%s'" % (snapshot_storage_pool, snapshot_storage_system))
        ui_lib.wait_for_element_and_input_text(EditVolumeElements.ID_INPUT_SNAPSHOT_STORAGE_POOL, snapshot_storage_pool, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditVolumeElements.ID_SELECT_SNAPSHOT_STORAGE_POOL % (snapshot_storage_pool, snapshot_storage_pool, snapshot_storage_system), timeout, fail_if_false=True)

    @classmethod
    def input_capacity(cls, capacity, timeout=5):
        '''
            On the Edit Volume Dialog, input the capacity
        '''
        logger.debug("input capacity '%s'" % capacity)
        ui_lib.wait_for_element_and_input_text(EditVolumeElements.ID_INPUT_CAPACITY, capacity, timeout, fail_if_false=True)

    @classmethod
    def input_iopslimit(cls, iopslimit, timeout=5):
        '''
            On the Edit Volume Dialog, input the iopslimit
        '''
        logger.debug("Input iopslimit '%s'" % iopslimit)
        ui_lib.wait_for_element_and_input_text(EditVolumeElements.ID_INPUT_IOPSLIMIT, iopslimit, timeout, fail_if_false=True)

    @classmethod
    def input_datatranferlimit(cls, datatranferlimit, timeout=5):
        '''
            On the Edit Volume Dialog, input the datatransfermimit
        '''
        logger.debug("Input datatransferlimit '%s'" % datatranferlimit)
        ui_lib.wait_for_element_and_input_text(EditVolumeElements.ID_INPUT_DATATRANFERLIMIT, datatranferlimit, timeout, fail_if_false=True)

    @classmethod
    def get_provisioning(cls, timeout=5):
        '''
            On the Edit Volume Dialog, get the provisioning
        '''
        logger.debug("get provisioning")
        provisioning = FusionUIBase.get_text(EditVolumeElements.ID_TEXT_PROVISIONING, timeout=timeout, fail_if_false=True)
        return provisioning

    @classmethod
    def choose_sharing(cls, sharing, timeout=5):
        '''
            On the Edit Volume Dialog, choose the sharing of private or shared
        '''
        logger.debug("choose sharing '%s'" % sharing)
        if sharing.lower() == 'private':
            ui_lib.wait_for_element_and_click(EditVolumeElements.ID_RADIO_SHARING_PRIVATE, timeout, fail_if_false=True)
        elif sharing.lower() == 'shared':
            ui_lib.wait_for_element_and_click(EditVolumeElements.ID_RADIO_SHARING_SHARED, timeout, fail_if_false=True)
        else:
            ui_lib.fail_test("Invalid sharing value '%s', please specify 'Private' or 'Shared'" % sharing)

    @classmethod
    def select_pefpolicy(cls, perfpolicy, timeout=5):
        '''
            On the Edit Volume Dialog, select a performance policy
        '''
        logger.debug("select performance policy '%s'" % perfpolicy)
        ui_lib.wait_for_element_and_click(EditVolumeElements.ID_DROPDOWN_PERFPOLICY, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditVolumeElements.ID_SELECT_PERFPOLICY % perfpolicy, timeout, fail_if_false=True)

    @classmethod
    def select_volset(cls, volset, timeout=5):
        '''
            On the Edit Volume Dialog, select a volume set
        '''
        logger.debug("select volume set '%s'" % volset)
        ui_lib.wait_for_element_and_click(EditVolumeElements.ID_DROPDOWN_VOLUMESET, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditVolumeElements.ID_SELECT_VOLUMESET % volset, timeout, fail_if_false=True)

    @classmethod
    def select_folder(cls, folder, timeout=5):
        '''
            On the Edit Volume Dialog, select a folder
        '''
        logger.debug("select folder '%s'" % folder)
        ui_lib.wait_for_element_and_click(EditVolumeElements.ID_DROPDOWN_FOLDER, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditVolumeElements.ID_SELECT_FOLDER % folder, timeout, fail_if_false=True)

    @classmethod
    def select_toggle_iopslimit(cls, timeout=5):
        '''
            On the Edit Volume Dialog, enable iopslimit
        '''
        logger.debug("Enable iopslimit")
        ui_lib.wait_for_element_and_click(EditVolumeElements.ID_TOGGLE_IOPSLIMIT, timeout, fail_if_false=True)

    @classmethod
    def select_toggle_datatransferlimit(cls, timeout=5):
        '''
            On the Edit Volume Dialog, enable datatransferlimit
        '''
        logger.debug("Enable datatransferlimit")
        ui_lib.wait_for_element_and_click(EditVolumeElements.ID_TOGGLE_DATATRANSFERLIMIT, timeout, fail_if_false=True)

    @classmethod
    def click_ok_button(cls, timeout=5):
        '''
            On the Edit Volume Dialog, click the OK button
        '''
        logger.debug("click 'ok' button")
        ui_lib.wait_for_element_and_click(EditVolumeElements.ID_BUTTON_OK, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        '''
            On the Edit Volume Dialog, click the cancel button
        '''
        logger.debug("click 'cancel' button")
        ui_lib.wait_for_element_and_click(EditVolumeElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_dialog_disappear(cls, timeout=5, fail_if_false=True):
        '''
            wait for edit volume dialog to disappear
        '''
        logger.debug("waiting for edit dialog to disappear")
        if ui_lib.wait_for_element_notvisible(EditVolumeElements.ID_DIALOG_EDIT, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def get_volume_inconsistent_warning_msg(cls, attribute, timeout=5):
        '''
            On the Edit Volume Dialog, get the volume inconsistent warning message
        '''
        logger.debug("get inconsistent warning msg for volume '%s' " % attribute)
        warning_msg = FusionUIBase.get_text(EditVolumeElements.ID_TEXT_INCONSISTENT_WARNING_MESSAGE % attribute, timeout=timeout, fail_if_false=True)
        return warning_msg


class DeleteVolumes(object):
    '''
        Delete Volume Dialog
    '''
    @classmethod
    def select_actions_delete(cls, timeout=5):
        '''
            On the Volume Page, click action menu and select delete action
        '''
        logger.debug("select Actions -> delete")
        ui_lib.wait_for_element_and_click(GeneralVolumeElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(DeleteVolumeElements.ID_SELECT_ACTION_DELETE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_dialog_shown(cls, timeout=5, fail_if_false=True):
        '''
            wait for the delete volume dialog to be shown
        '''
        logger.debug("waiting for delete dialog to show up")
        if ui_lib.wait_for_element_visible(DeleteVolumeElements.ID_DIALOG_DELETE, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def choose_delete_volume_from(cls, delete_from, timeout=5):
        '''
            On the Delete Volume Dialog, choose delete from
        '''
        logger.debug("check delete volume from '%s'" % delete_from)
        expect_list = ["OneView and the storage system", "OneView only"]
        FusionUIBase.para_should_be_in_list(expect_list, delete_from)
        if delete_from.lower().replace(" ", "") == "OneView and the storage system".lower().replace(" ", ""):
            ui_lib.wait_for_element_and_click(DeleteVolumeElements.ID_RADIO_DELETE_VOLUME_FROM_ONEVIEW_AND_THE_STORAGE_SYSTEM, timeout, fail_if_false=True)
        else:
            ui_lib.wait_for_element_and_click(DeleteVolumeElements.ID_RADIO_DELETE_VOLUME_FROM_ONEVIEW_ONLY, timeout, fail_if_false=True)

    @classmethod
    def click_yes_delete_button(cls, timeout=5):
        '''
            On the Delete Volume Dialog, click the yes delete button
        '''
        logger.debug("click 'yes, delete'")
        ui_lib.wait_for_element_and_click(DeleteVolumeElements.ID_BUTTON_YES_DELETE, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        '''
            On the Delete Volume Dialog, click the cancel button
        '''
        logger.debug("click 'cancel'")
        ui_lib.wait_for_element_and_click(DeleteVolumeElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_dialog_disappear(cls, timeout=5, fail_if_false=True):
        '''
            wait for the delete volume dialog to disappear
        '''
        logger.debug("waiting for delete dialog to disappear")
        if ui_lib.wait_for_element_notvisible(DeleteVolumeElements.ID_DIALOG_DELETE, timeout, fail_if_false):
            return True
        else:
            return False


class AddVolumes(object):
    '''
        Add Volumes Dialog
    '''
    e = AddVolumeElements

    @classmethod
    def click_add_volume_button(cls, timeout=5):
        '''
            On the volumes page, click the add volume button
        '''
        logger.debug("click button '+ Add volume")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_VOLUME, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_volume_dialog_open(cls, timeout=5, fail_if_false=True):
        '''
            wait for the add volume dialog to appear
        '''
        logger.debug("waiting for 'Add volume' dialog to get opened")
        if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_ADD_VOLUME, timeout, fail_if_false):
            logger.debug("'Add volume' dialog is successfully opened")
            return True
        else:
            logger.warn("'Add volume' dialog did NOT get opened")
            return False

    @classmethod
    def input_select_storage_system(cls, storage_system, timeout=5):
        '''
            On the Add Volume Dialog, select the storage system
        '''
        logger.debug("input storage system '%s'" % storage_system)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_STORAGE_SYSTEM, storage_system, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_STORAGE_SYSTEM % storage_system, timeout, fail_if_false=True)

    @classmethod
    def input_storage_system_volume_name(cls, name, timeout=5):
        '''
            On the Add Volume Dialog, input the volume name
        '''
        logger.debug("input storage system volume name '%s'" % name)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_STORAGE_SYSTEM_VOLUME_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def input_description(cls, description, timeout=5):
        '''
            On the Add Volume Dialog, input the description
        '''
        logger.debug("input description '%s'" % description)
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_DESCRIPTION, description, timeout, fail_if_false=True)

    @classmethod
    def choose_sharing(cls, sharing, timeout=5):
        '''
            On the Add Volume Dialog, schoose the sharing of private or shared
        '''
        logger.debug("choose sharing '%s'" % sharing)
        if sharing.lower() == 'private':
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SHARING_PRIVATE, timeout, fail_if_false=True)
        elif sharing.lower() == 'shared':
            ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_SHARING_SHARED, timeout, fail_if_false=True)
        else:
            ui_lib.fail_test("Invalid sharing value '%s', please specify 'Private' or 'Shared'" % sharing)

    @classmethod
    def click_add_button(cls, timeout=5):
        '''
            On the Add Volume Dialog, click the add button
        '''
        logger.debug("click add button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD, timeout, fail_if_false=True)

    @classmethod
    def click_add_plus_button(cls, timeout=5):
        '''
            On the Add Volume Dialog, click the add plus button
        '''
        logger.debug("click add+ button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_PLUS, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        '''
            On the Add Volume Dialog, click the cancel button
        '''
        logger.debug("click cancel button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_volume_dialog_close(cls, timeout=5, fail_if_false=True):
        '''
            wait for the add volume dialog to close
        '''
        logger.debug("waiting for 'Add volume' dialog to to get closed")
        if ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_ADD_VOLUME, timeout, fail_if_false):
            logger.debug("'Add volume' dialog is successfully closed")
            return True
        else:
            logger.warn("'Add volume' dialog did NOT get closed")
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_adding_message_shown(cls, timeout=5, fail_if_false=True):
        '''
            wait for adding volume message to appear
        '''
        logger.debug("waiting for creating volume message to show up")
        if ui_lib.wait_for_element_visible(cls.e.ID_TEXT_ADDING_VOLUME, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_adding_message_disappear(cls, timeout=5, fail_if_false=True):
        '''
            wait for the adding volume message to disappear
        '''
        logger.debug("waiting for creating volume message to disappear")
        if ui_lib.wait_for_element_notvisible(cls.e.ID_TEXT_ADDING_VOLUME, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_add_volume_error(cls, expect_value, volume_name, timeout=5, fail_if_false=True):
        '''
            verify the add volume error appears
        '''
        logger.debug("verify %s error appears for %s" % (expect_value, volume_name))
        if ui_lib.wait_for_element_visible(cls.e.ID_TEXT_ADD_ERROR_MESSAGE, timeout, fail_if_false):
            return True
        else:
            return False


class RefreshVolumes(object):
    '''
        Refresh Volume Dialog
    '''

    @classmethod
    def select_actions_refresh(cls, timeout=5):
        '''
            On the Volume Page, seclect action menu refresh action
        '''
        logger.debug("select Actions -> refresh")
        ui_lib.wait_for_element_and_click(GeneralVolumeElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(RefreshVolumeElements.ID_SELECT_ACTION_REFRESH, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_general_state_refreshing(cls, timeout=5, fail_if_false=True):
        '''
            On the refresh Volume Dialog, wait for state of refreshing to appear
        '''
        logger.debug("waiting for general state indicates to refreshing")
        ui_lib.wait_for_element_text(GeneralVolumeElements.ID_TEXT_GENERAL_STATE, "Refreshing", timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_general_state_managed(cls, timeout=5, fail_if_false=True):
        '''
            On the refresh Volume Dialog, wait for state of managed to appear
        '''
        logger.debug("waiting for general state indicates to configured")
        ui_lib.wait_for_element_text(GeneralVolumeElements.ID_TEXT_GENERAL_STATE, "Managed", timeout, fail_if_false)


class CreateVolumeSnapshot(object):
    '''
        Create volume snapshots dialog
    '''
    @classmethod
    def select_actions_create_snapshot(cls, timeout=5):
        '''
            On the volumes page, click actions, select create snapshot
        '''
        logger.debug("select Actions -> create snapshot")
        ui_lib.wait_for_element_and_click(GeneralVolumeElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(CreateVolumeSnapshotElements.ID_SELECT_ACTION_CREATE_SNAPSHOT, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_snapshot_dialog_shown(cls, timeout=5, fail_if_false=True):
        '''
            wait for the create snapshot dialog to appear
        '''
        logger.debug("waiting for create snapshot dialog to show up")
        if ui_lib.wait_for_element_visible(CreateVolumeSnapshotElements.ID_DIALOG_CREATE_SNAPSHOT, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def _covert_char_to_ascii(cls, n):
        '''

        '''
        return hex(ord(n))

    @classmethod
    def _press_keys(cls, keys):
        '''
           press keys
        '''
        selenium2lib = ui_lib.get_s2l()
        for key in keys:
            key = cls._covert_char_to_ascii(key)
            codes = """e = jQuery.Event("keypress");
    e.which = %s //enter key
    $('span[class="hp-cursor"]').trigger(e);""" % key
            selenium2lib.execute_javascript(codes)

    @classmethod
    def _delete_keys(cls, key_no):
        '''
           press delete keys
        '''
        if not isinstance(key_no, types.IntType):
            ui_lib.fail_test("Error: 'key_no' must be an integer")
        selenium2lib = ui_lib.get_s2l()
        # codes = """$('div[class="hp-form-content"] > div > div[class="hp-tokens"] > span').length;"""
        # key_no = int(selenium2lib.execute_javascript(codes)) - 1
        # logger.info(key_no)
        codes = """e = jQuery.Event("keydown");
e.which = 0x8; //enter key
$('span[class="hp-cursor"]').trigger(e);"""
        for n in range(int(key_no)):     # pylint: disable=W0612
            selenium2lib.execute_javascript(codes)

    @classmethod
    def input_name(cls, name, timeout=5, fail_if_false=True):
        '''
           In the Create Snapshot dialog, input the name of snapshot
        '''
        logger.debug("input name '%s'" % name)
        name_variables = re.findall(r'\{(.*?)\}', name)
        ui_lib.wait_for_element_and_click(CreateVolumeSnapshotElements.ID_INPUT_NAME, timeout, fail_if_false)
        cls._delete_keys(3)
        if len(name_variables) > 0:
            name_process = re.sub(r'\{\w+\s*\w+\}', '*VAR-#*', name)
            name_process = name_process.split('*')
            expect_list = ["volumename", "timestamp"]
            m = 0
            for variable in name_process:
                if variable == "VAR-#":
                    FusionUIBase.para_should_be_in_list(expect_list, name_variables[m])
                    if name_variables[m].lower().replace(' ', '') == "volumename":
                        ui_lib.wait_for_element_and_click(CreateVolumeSnapshotElements.ID_SELECT_NAME_VOLUME_NAME, timeout, fail_if_false)
                        m += 1
                    else:
                        ui_lib.wait_for_element_and_click(CreateVolumeSnapshotElements.ID_SELECT_NAME_TIMESTAMP, timeout, fail_if_false)
                        m += 1
                else:
                    cls._press_keys(variable)
                    # ui_lib.wait_for_element_and_input_text(CreateVolumeSnapshotElements.ID_INPUT_NAME_CURSOR, variable, timeout, fail_if_false=True)

        else:
            cls._press_keys(name)
            # ui_lib.wait_for_element_and_input_text(CreateVolumeSnapshotElements.ID_INPUT_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def input_description(cls, description, timeout=5, fail_if_false=True):
        '''
           In the Create Snapshot dialog, input the description
        '''
        logger.debug("input description '%s'" % description)
        ui_lib.wait_for_element_and_click(CreateVolumeSnapshotElements.ID_INPUT_DESCRIPTION, timeout, fail_if_false)
        ui_lib.wait_for_element_and_input_text(CreateVolumeSnapshotElements.ID_INPUT_DESCRIPTION, description, timeout, fail_if_false)

    @classmethod
    def click_create(cls, timeout=5):
        '''
           In the Create Snapshot dialog, click the create button
        '''
        logger.debug("click create")
        ui_lib.wait_for_element_and_click(CreateVolumeSnapshotElements.ID_BUTTON_CREATE, timeout, fail_if_false=True)

    @classmethod
    def click_cancel(cls, timeout=5):
        '''
           In the Create Snapshot dialog, click the cancel button
        '''
        logger.debug("click cancel")
        ui_lib.wait_for_element_and_click(CreateVolumeSnapshotElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_snapshot_dialog_disappear(cls, timeout=5, fail_if_false=True):
        '''
           wait for the create snapshot dialog to disappear
        '''
        logger.debug("waiting for create snapshot dialog to disappear")
        if ui_lib.wait_for_element_notvisible(CreateVolumeSnapshotElements.ID_DIALOG_CREATE_SNAPSHOT, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_creating_message_disappear(cls, timeout=5, fail_if_false=True):
        '''
           wait for the creating snapshot message to disappear
        '''
        logger.debug("waiting for creating snapshot message to disappear")
        if ui_lib.wait_for_element_notvisible(CreateVolumeSnapshotElements.ID_TEXT_CREATING_SNAPSHOT, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_create_snapshot_error(cls, expect_value, snapshot_name):
        '''
           verify the create snapshot error
        '''
        logger.debug("verify Create Snapshot Error [ %s ] appears for [ %s ]" % (expect_value, snapshot_name))
        error = FusionUIBase.get_all_error_message_on_form(CreateVolumeSnapshotElements.ID_DIALOG_CREATE_SNAPSHOT)
        if error.__contains__(expect_value):
            return True
        else:
            return False


class DeleteVolumeSnapshots(object):
    '''
        Delete Volume snapshots dialog
    '''
    @classmethod
    def select_delete_snapshot_icon(cls, timeout=7):
        '''
           select the delete icon under the snapshot section
        '''
        logger.debug("select delete icon under snapshot section")
        ui_lib.wait_for_element_and_click(DeleteVolumeSnapshotElements.ID_ICON_SNAPSHOT_DELETE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_snapshot_dialog_shown(cls, timeout=7, fail_if_false=True):
        '''
           wait for the delete snapshot dialog to appear
        '''
        logger.debug("waiting for delete snapshot dialog to show up")
        if ui_lib.wait_for_element_visible(DeleteVolumeSnapshotElements.ID_DIALOG_DELETE_SNAPSHOT, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def click_delete_button(cls, timeout=5, appversion=0):
        '''
           on the delete snapshot dialog, click delete button
        '''
        logger.debug("CLICK yes,delete button under snapshot section")
        if appversion >= "5.00":
            ui_lib.wait_for_element_and_click(DeleteVolumeSnapshotElements.ID_BTN_YES_DELETE_2, timeout, fail_if_false=True)
        # all other versions use the old element
        else:
            ui_lib.wait_for_element_and_click(DeleteVolumeSnapshotElements.ID_BTN_YES_DELETE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_snapshot_dialog_disappear(cls, timeout=5, fail_if_false=True):
        '''
           wait for the delete snapshot dialog to disappear
        '''
        logger.debug("waiting for deletesnapshot dialog to disappear")
        if ui_lib.wait_for_element_notvisible(DeleteVolumeSnapshotElements.ID_DIALOG_DELETE_SNAPSHOT, timeout, fail_if_false):
            return True
        else:
            return False


class RevertVolumeSnapshot(object):
    '''
        revert volume snapshots dialog
    '''
    @classmethod
    def click_revert(cls, name, timeout=5):
        '''
           Click revert snapshot
        '''
        logger.debug("Click Revert")
        ui_lib.wait_for_element_visible(RevertVolumeSnapshotElements.ID_BUTTON_REVERT % name, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(RevertVolumeSnapshotElements.ID_BUTTON_REVERT % name, timeout, fail_if_false=True)

    @classmethod
    def click_yes_revert(cls, timeout=5):
        '''
           click yes revert button
        '''
        logger.debug("Click on yes revert button")
        ui_lib.wait_for_element_visible(RevertVolumeSnapshotElements.ID_BUTTON_YES_REVERT, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(RevertVolumeSnapshotElements.ID_BUTTON_YES_REVERT, timeout, fail_if_false=True)


class CreateVolumeUsingSnapshot(object):
    '''
        Create Volume from snapshot dialog
    '''
    @classmethod
    def click_create_volume(cls, name, timeout=5):
        '''
           In the Snapshot section, click create volume
        '''
        logger.debug("Click create volume")
        ui_lib.wait_for_element_visible(CreateVolumeUsingSnapshotElements.ID_BUTTON_CREATE_VOLUME % name, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(CreateVolumeUsingSnapshotElements.ID_BUTTON_CREATE_VOLUME % name, timeout, fail_if_false=True)

    @classmethod
    def input_volume_name(cls, name, timeout=5, fail_if_false=True):
        '''
           In the Create Volume from Snapshot dialog, input the name of volume
        '''
        logger.debug("Enter Volume name")
        ui_lib.wait_for_element_and_click(CreateVolumeUsingSnapshotElements.ID_INPUT_VOLUME_NAME, timeout, fail_if_false)
        ui_lib.wait_for_element_and_input_text(CreateVolumeUsingSnapshotElements.ID_INPUT_VOLUME_NAME, name, timeout, fail_if_false)

    @classmethod
    def input_description(cls, description, timeout=5, fail_if_false=True):
        '''
           In the Create Volume from Snapshot dialog, input the description
        '''
        logger.debug("input description '%s'" % description)
        ui_lib.wait_for_element_and_click(CreateVolumeUsingSnapshotElements.ID_INPUT_DESCRIPTION, timeout, fail_if_false)
        ui_lib.wait_for_element_and_input_text(CreateVolumeUsingSnapshotElements.ID_INPUT_DESCRIPTION, description, timeout, fail_if_false)

    @classmethod
    def choose_sharing(cls, sharing, timeout=5, fail_if_false=True):
        '''
           In the Create Volume from Snapshot dialog, choose sharing of private or shared
        '''
        logger.debug("choose sharing '%s'" % sharing)
        if sharing.lower() == 'private':
            ui_lib.wait_for_element_and_click(CreateVolumeUsingSnapshotElements.ID_RADIO_PRIVATE_VOLUME, timeout, fail_if_false)
        elif sharing.lower() == 'shared':
            ui_lib.wait_for_element_and_click(CreateVolumeUsingSnapshotElements.ID_RADIO_SHARED_VOLUME, timeout, fail_if_false)
        else:
            ui_lib.fail_test("Invalid input: Please specify volume type as either 'Private' or 'Shared'")

    @classmethod
    def input_select_storage_pool(cls, storage_pool, storage_system='', timeout=5, fail_if_false=True):
        '''
           In the Create Volume from Snapshot dialog, select the pool
        '''
        logger.debug("input storage pool '%s' of storage system '%s' " % (storage_pool, storage_system))
        ui_lib.wait_for_element_and_input_text(CreateVolumeUsingSnapshotElements.ID_INPUT_STORAGE_POOL, storage_pool, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(CreateVolumeUsingSnapshotElements.ID_SELECT_STORAGE_POOL % (storage_pool, storage_pool, storage_system), timeout, fail_if_false)

    @classmethod
    def input_select_snapshot_storage_pool(cls, snapshot_storage_pool, snapshot_storage_system='', timeout=5, fail_if_false=True):
        '''
           In the Create Volume from Snapshot dialog, select the snapshot pool
        '''
        logger.debug("input snapshot storage pool '%s' of storage system '%s'" % (snapshot_storage_pool, snapshot_storage_system))
        ui_lib.wait_for_element_and_input_text(CreateVolumeUsingSnapshotElements.ID_INPUT_SNAPSHOT_STORAGE_POOL, snapshot_storage_pool, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(CreateVolumeUsingSnapshotElements.ID_SELECT_SNAPSHOT_STORAGE_POOL % (snapshot_storage_pool, snapshot_storage_pool, snapshot_storage_system), timeout, fail_if_false)

    @classmethod
    def click_create(cls, timeout=5):
        '''
           In the Create Volume from Snapshot dialog, click create
        '''
        logger.debug("click create")
        ui_lib.wait_for_element_and_click(CreateVolumeUsingSnapshotElements.ID_BUTTON_CREATE, timeout, fail_if_false=True)

    @classmethod
    def click_cancel(cls, timeout=5):
        '''
           In the Create Volume from Snapshot dialog, click cancel
        '''
        logger.debug("click cancel")
        ui_lib.wait_for_element_and_click(CreateVolumeUsingSnapshotElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_creating_message_disappear(cls, timeout=5, fail_if_false=True):
        '''
           waiting for the create volume from snapshot message to disappear
        '''
        logger.debug("waiting for creating volume from snapshot message to disappear")
        if ui_lib.wait_for_element_notvisible(CreateVolumeUsingSnapshotElements.ID_TEXT_CREATING_VOLUME, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_create_volume_from_snapshot_error(cls, expect_value, volume_name, timeout=5, fail_if_false=True):
        '''
           verify if an error message appears
        '''
        logger.debug("verify Create Volume from snapshot Error [ %s ] appears for [ %s ]" % (expect_value, volume_name))
        return FusionUIBase.verify_element_text("Description", CreateVolumeUsingSnapshotElements.ID_TEXT_CREATE_ERROR_MESSAGE,
                                                expect_value, timeout, fail_if_false)


class VerifyStorageVolume(object):
    '''
        Verify Storage Volume values
    '''

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storagevolume_title(cls, storagevolume, timeout=10, fail_if_false=True):
        '''
           verify the storage volume title is visible
        '''
        logger.info('verifying [ Storage Volume title %s ] is visible' % storagevolume)
        ui_lib.wait_for_element_visible(GeneralVolumeElements.ID_TITLE_STORAGE_VOLUME_NAME, timeout, fail_if_false)

    # { Overview General/General
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_state(cls, expect_value, timeout=5, fail_if_false=True):
        '''
           verify the state is as expected
        '''
        logger.debug("verify [ state ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("State", GeneralVolumeElements.ID_TEXT_GENERAL_STATE, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storagevolume_Navigation_Tab_Text(cls, expect_value, navigation_type, timeout=10, fail_if_false=True):
        '''
           verify the volume navigation tab text is as expected
        '''
        logger.info('verifying [ Storage Volume Tab text %s ] is visible' % navigation_type)
        return FusionUIBase.verify_element_text('', GeneralVolumeElements.ID_TEXT_TAB_STORAGE_VOLUME_NAVIGATION % navigation_type, expect_value, timeout, fail_if_false)

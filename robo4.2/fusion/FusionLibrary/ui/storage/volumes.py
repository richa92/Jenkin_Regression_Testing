'''
Created on Apr 2, 2014

'''
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.storage.volumes_elements import FusionStorageVolumesPage
# from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.business_logic.storage.volumes import CommonOperationVolumes
from FusionLibrary.ui.business_logic.storage.volumes import CreateVolumes
from FusionLibrary.ui.business_logic.storage.volumes import EditVolumes
from FusionLibrary.ui.business_logic.storage.volumes import DeleteVolumes
from FusionLibrary.ui.business_logic.storage.volumes import AddVolumes
from FusionLibrary.ui.business_logic.storage.volumes import RefreshVolumes
from FusionLibrary.ui.business_logic.storage.volumes import CreateVolumeSnapshot
from FusionLibrary.ui.business_logic.storage.volumes import DeleteVolumeSnapshots
from FusionLibrary.ui.business_logic.storage.volumes import RevertVolumeSnapshot
from FusionLibrary.ui.business_logic.storage.volumes import CreateVolumeUsingSnapshot
from FusionLibrary.ui.business_logic.storage.volumes import VerifyStorageVolume
from FusionLibrary.ui.business_logic.storage.storagepools import CommonOperationStoragePools
from FusionLibrary.ui.business_logic.storage.volumetemplates import CommonOperationVolumeTemplates
from FusionLibrary.ui.business_logic.storage.storagesystems import CommonOperationStorageSystems
from FusionLibrary.ui.business_logic.storage.volumetemplates import EditVolumeTemplates
from FusionLibrary.ui.storage.storagetemplates import select_storage_template
from FusionLibrary.ui.business_logic.base import FusionUIBase
from FusionLibrary.ui.business_logic.base import SectionType
from RoboGalaxyLibrary.utilitylib import logging as logger
import time


def select_storage_volume(storagevolumename):
    '''
           Select a storage volume
    '''
    FusionUIBase.navigate_to_section(SectionType.VOLUMES)
    logger.info("Selecting a storage Volume with name {0}".format(storagevolumename))
    if CommonOperationVolumes.verify_volume_exist(storagevolumename, fail_if_false=False):
        if CommonOperationVolumes.verify_locate_error_exists():
            selenium2lib = ui_lib.get_s2l()
            selenium2lib.reload_page()
        CommonOperationVolumes.click_volume(storagevolumename)
        CommonOperationVolumes.wait_volume_selected(storagevolumename, timeout=30)
        return True
    else:
        logger.warn("Storage volume '{0}' does not exist".format(storagevolumename))
        return False


def create_storage_volumes(*storagevolume_obj):
    '''
            create storage volumes
    '''
    FusionUIBase.navigate_to_section(SectionType.VOLUMES)
    if isinstance(storagevolume_obj, test_data.DataObj):
        storagevolume_obj = [storagevolume_obj]
    elif isinstance(storagevolume_obj, tuple):
        storagevolume_obj = list(storagevolume_obj)
    count = 0
    new_storagevolume_obj = []
    logger.info("{0} PREPARATION  {0}".format('-' * 17))
    for n, volume in enumerate(storagevolume_obj):
        name = volume.name
        if getattr(volume, 'remove_if_exists', 'true').lower() == 'true':
            remove_if_exists = True
        else:
            remove_if_exists = False
        if not CommonOperationVolumes.verify_volume_not_exist(name, fail_if_false=False):
            logger.warn("Volume '{0}' already exists".format(name))
            if remove_if_exists is True:
                logger.info("Removing the volume since 'remove_if_exists' is set to 'True'")
                if not delete_storage_volume(name, deletefrom="OneView and the storage system", fail_if_false=False):
                    count += 1
                else:
                    new_storagevolume_obj.append(volume)
            else:
                logger.warn("Error: Was not able to create the existing volume '%s'." % name)
                count += 1
        else:
            new_storagevolume_obj.append(volume)

    for n, volume in enumerate(new_storagevolume_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(new_storagevolume_obj), '-' * 14))
        name = volume.name
        logger.info("Creating a volume with name '{0}'".format(name))
        if n == 0 or getattr(volume, 'testtype', '') == 'unhappy':
            FusionUIBase.show_activity_sidebar()
            CreateVolumes.click_create_volume_button()
        CreateVolumes.wait_create_volume_dialog_shown()
        CreateVolumes.input_name(name)
        CreateVolumes.input_description(volume.desc)
        if getattr(volume, 'testtype', '') != 'unhappy':  # happy path testing
            if getattr(volume, 'svtname', '') != '' and volume.svtname.lower() != 'none':
                if getattr(volume, 'poolname', '') != '':
                    CreateVolumes.input_select_volume_template(volume.svtname, volume.poolname)
                else:
                    CreateVolumes.input_select_volume_template(volume.svtname, "")
            else:
                CreateVolumes.input_select_volume_template('None', "")
                if getattr(volume, 'poolname', '') != '':
                    if getattr(volume, 'storagename', '') != '':
                        CreateVolumes.input_select_storage_pool(volume.poolname, volume.storagename)
                    else:
                        CreateVolumes.input_select_storage_pool(volume.poolname, "")
                if getattr(volume, 'snapshotpool', '') != '':
                    if getattr(volume, 'storagename', '') != '':
                        CreateVolumes.input_select_snapshot_storage_pool(volume.snapshotpool, volume.storagename)
                    else:
                        logger.warn("user didn't specify 'storagename', choose the default one")
                        CreateVolumes.input_select_snapshot_storage_pool(volume.snapshotpool, "")
                if getattr(volume, 'provisioning', '') != '':
                    CreateVolumes.select_provisioning(volume.provisioning)

            # new nimble related fields
                if getattr(volume, 'perfpolicy', '') != '':
                    CreateVolumes.select_pefpolicy(volume.perfpolicy)
                if getattr(volume, 'volset', '') != '':
                    CreateVolumes.select_volset(volume.volset)
                if getattr(volume, 'iopslimit', '') != '':
                    CreateVolumes.select_toggle_iopslimit()
                    CreateVolumes.input_iopslimit(volume.iopslimit)
                if getattr(volume, 'datatransferlimit', '') != '':
                    CreateVolumes.select_toggle_datatransferlimit()
                    CreateVolumes.input_datatransferlimit(volume.datatransferlimit)
                if getattr(volume, 'folder', '') != '':
                    CreateVolumes.select_folder(volume.folder)

        else:  # negative path testing
            if getattr(volume, 'svtname', '') != '' and volume.svtname.lower() != 'none':
                if getattr(volume, 'poolname', '') != '':
                    CreateVolumes.input_select_volume_template(volume.svtname, volume.poolname, fail_if_false=False)
                else:
                    CreateVolumes.input_select_volume_template(volume.svtname, "", fail_if_false=False)
            else:
                CreateVolumes.input_select_volume_template('None', "")
                if getattr(volume, 'poolname', '') != '':
                    if getattr(volume, 'storagename', '') != '':
                        CreateVolumes.input_select_storage_pool(volume.poolname, volume.storagename, fail_if_false=False)
                    else:
                        CreateVolumes.input_select_storage_pool(volume.poolname, "", fail_if_false=False)
                if getattr(volume, 'snapshotpool', '') != '':
                    if getattr(volume, 'storagename', '') != '':
                        CreateVolumes.input_select_snapshot_storage_pool(volume.snapshotpool, volume.storagename, fail_if_false=False)
                    else:
                        logger.warn("user didn't specify 'storagename', choose the default one")
                        CreateVolumes.input_select_snapshot_storage_pool(volume.snapshotpool, "", fail_if_false=False)
                if getattr(volume, 'provisioning', '') != '':
                    CreateVolumes.select_provisioning(volume.provisioning)

                if getattr(volume, 'iopslimit', '') != '':
                    CreateVolumes.select_toggle_iopslimit()
                    CreateVolumes.input_iopslimit(volume.iopslimit)
                    CreateVolumes.click_iopslimit_label()      # click outside iopslimit box to error
                    CreateVolumes.verify_iopslimit_error('Enter a value greater than or equal to 256.', volume.name)
                if getattr(volume, 'datatransferlimit', '') != '':
                    CreateVolumes.select_toggle_datatransferlimit()
                    CreateVolumes.input_datatransferlimit(volume.datatransferlimit)

        if getattr(volume, 'capacity', '') != '':
            CreateVolumes.input_capacity(volume.capacity)
        if getattr(volume, 'sharing', '') != '':
            CreateVolumes.choose_sharing(volume.sharing)

        if n == (len(new_storagevolume_obj) - 1):
            CreateVolumes.click_create_button()
        else:
            CreateVolumes.click_create_plus_button()

        if CreateVolumes.wait_creating_message_disappear(timeout=20, fail_if_false=False):
            status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
            if getattr(volume, 'testtype', '') == 'unhappy':
                status = False
                if n == (len(new_storagevolume_obj) - 1):
                    CreateVolumes.click_create_button()
                    time.sleep(1)    # reaction of create button is slower and requires a delay
                else:
                    CreateVolumes.click_create_plus_button()
                CreateVolumes.verify_create_volume_error(volume.emsg, name, 1, fail_if_false=True)
                CreateVolumes.click_cancel_button()
            else:
                FusionUIBase.wait_activity_action_ok(name, message='Create', timeout=40)

            if status is True:
                ui_lib.fail_test(msg)

    FusionUIBase.show_activity_sidebar()
    logger.info("{0} VERIFICATION {0}".format('-' * 17))
    for n, volume in enumerate(new_storagevolume_obj):
        if getattr(volume, 'testtype', '') != "unhappy":  # do not verify if unhappy test
            CommonOperationVolumes.wait_volume_status_ok(volume.name)
            logger.info("Created volume {0} successfully".format(volume.name))
        else:
            logger.info("Unhappy path testing, VERIFICATION skipped")
    if count > 0:
        logger.warn("Failure: Not able to create some of volumes, please check all warning messages")
        return False

    return True


def edit_storage_volumes(*storagevolume_obj):
    '''
        edit storage volumes
    '''
    FusionUIBase.navigate_to_section(SectionType.VOLUMES)
    if isinstance(storagevolume_obj, test_data.DataObj):
        storagevolume_obj = [storagevolume_obj]
    elif isinstance(storagevolume_obj, tuple):
        storagevolume_obj = list(storagevolume_obj)
    count = 0

    for n, volume in enumerate(storagevolume_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(storagevolume_obj), '-' * 14))
        name = volume.name
        logger.info("Editing a volume with name '{0}'".format(name))
        if not select_storage_volume(name):
            count += 1
            continue
        EditVolumes.select_actions_edit()
        EditVolumes.wait_edit_dialog_shown()
        if getattr(volume, 'newname', '') != '':
            EditVolumes.input_name(volume.newname)
        if getattr(volume, 'desc', '') != '':
            EditVolumes.input_description(volume.desc)
        if getattr(volume, 'template_name', '') != '':
            EditVolumes.input_select_volume_template(volume.template_name, "")
        if getattr(volume, 'snapshotpool', '') != '':
            if getattr(volume, 'storagename', '') != '':
                EditVolumes.input_select_snapshot_storage_pool(volume.snapshotpool, volume.storagename)
            else:
                EditVolumes.input_select_snapshot_storage_pool(volume.snapshotpool, "")
        if getattr(volume, 'capacity', '') != '':
            EditVolumes.input_capacity(volume.capacity)
        if getattr(volume, 'sharing', '') != '':
            EditVolumes.choose_sharing(volume.sharing)

        # new nimble related fields
        if getattr(volume, 'perfpolicy', '') != '':
            EditVolumes.select_pefpolicy(volume.perfpolicy)
        if getattr(volume, 'volset', '') != '':
            EditVolumes.select_volset(volume.volset)
        if getattr(volume, 'iopslimit', '') != '':
            EditVolumes.select_toggle_iopslimit()
            EditVolumes.input_iopslimit(volume.iopslimit)
        if getattr(volume, 'datatransferlimit', '') != '':
            EditVolumes.select_toggle_datatransferlimit()
            EditVolumes.input_datatransferlimit(volume.datatransferlimit)
        if getattr(volume, 'folder', '') != '':
            EditVolumes.select_folder(volume.folder)

        EditVolumes.click_ok_button()
        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
        if status is True:
            ui_lib.fail_test(msg)
        EditVolumes.wait_edit_dialog_disappear(timeout=10)
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(name, message="Update", timeout=30)
        FusionUIBase.show_activity_sidebar()
        if getattr(volume, 'newname', '') != '':
            CommonOperationVolumes.wait_volume_status_ok(volume.newname)
        else:
            CommonOperationVolumes.wait_volume_status_ok(name)
        logger.info("Edit volume {0} successfully".format(name))
    if count > 0:
        logger.warn("Failure: Not able to edit some of volumes, please check warning messages.")
        return False

    return True


def refresh_storage_volumes(*storagevolume_obj):
    '''
        Refresh storage volumes
    '''
    FusionUIBase.navigate_to_section(SectionType.VOLUMES)
    if isinstance(storagevolume_obj, test_data.DataObj):
        storagevolume_obj = [storagevolume_obj]
    elif isinstance(storagevolume_obj, tuple):
        storagevolume_obj = list(storagevolume_obj)
    count = 0

    for n, volume in enumerate(storagevolume_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(storagevolume_obj), '-' * 14))
        name = volume.name
        logger.info("Refreshing a volume with name '{0}'".format(name))
        if not select_storage_volume(name):
            count += 1
            continue

        RefreshVolumes.select_actions_refresh()
        # RefreshVolumes.wait_general_state_refreshing(timeout=10)
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(name, message="Refresh", timeout=40)
        FusionUIBase.show_activity_sidebar()
        RefreshVolumes.wait_general_state_managed(timeout=15)
        CommonOperationVolumes.wait_volume_status_ok(name)
        logger.info("Refresh volume {0} successfully".format(name))
    if count > 0:
        logger.warn("Failure: Not able to refresh some of volumes, please check warning messages.")
        return False

    return True


def add_storage_volumes(volumes_obj):
    '''
        Add storage volumes
    '''
    FusionUIBase.navigate_to_section(SectionType.VOLUMES)
    count = 0
    new_storagevolume_obj = []
    logger.info("{0} PREPARATION  {0}".format('-' * 17))
    for n, volume in enumerate(volumes_obj):
        name = volume.name
        if getattr(volume, 'remove_if_exists', 'true').lower() == 'true':
            remove_if_exists = True
        else:
            remove_if_exists = False
        if not CommonOperationVolumes.verify_volume_not_exist(name, fail_if_false=False):
            logger.warn("Volume '{0}' already exists".format(name))
            if remove_if_exists is True:
                logger.info("Removing the volume since 'remove_if_exists' is set to 'True'")
                if not delete_storage_volume(name, deletefrom="OneView Only", fail_if_false=False):
                    count += 1
                else:
                    new_storagevolume_obj.append(volume)
            else:
                logger.warn("Error: Would not able to create the existing volume '%s'." % name)
                count += 1
        else:
            new_storagevolume_obj.append(volume)
    for n, volume in enumerate(new_storagevolume_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(new_storagevolume_obj), '-' * 14))
        name = getattr(volume, 'name', '')
        logger.info("Adding a volume with name '{0}'".format(name))
        if n == 0:
            FusionUIBase.show_activity_sidebar()
            volume_list = CommonOperationVolumes.get_volume_list()
            if len(volume_list) > 0:
                CommonOperationVolumes.click_volume(volume_list[0])
        AddVolumes.click_add_volume_button()
        AddVolumes.wait_add_volume_dialog_open()
        AddVolumes.input_select_storage_system(volume.storagename)
        AddVolumes.input_storage_system_volume_name(name)
        AddVolumes.input_description(volume.desc)
        AddVolumes.choose_sharing(volume.sharing)
        if getattr(volume, 'testtype', '') != "unhappy":
            if n == (len(new_storagevolume_obj) - 1):
                AddVolumes.click_add_button()
                AddVolumes.wait_adding_message_shown()
                AddVolumes.wait_adding_message_disappear(timeout=15)
            else:
                AddVolumes.click_add_plus_button()
                status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
                if status is True:
                    ui_lib.fail_test(msg)
                FusionUIBase.wait_activity_action_ok(name, message='Add', timeout=45)
        else:
            if n == (len(new_storagevolume_obj) - 1):
                AddVolumes.click_add_button()
            else:
                AddVolumes.click_add_plus_button()
            status = False
            activity_status = FusionUIBase.get_latest_activity_status("", "Add", fail_if_false=True)
            if activity_status != "error":
                msg = "Activity status of %s discovered instead of error %activity_status"
                ui_lib.fail_test(msg)
            if n != (len(new_storagevolume_obj) - 1):
                AddVolumes.click_cancel_button()
    FusionUIBase.show_activity_sidebar()

    logger.info("{0} VERIFICATION {0}".format('-' * 17))
    for n, volume in enumerate(new_storagevolume_obj):
        if getattr(volume, 'testtype', '') != "unhappy":  # do not verify if unhappy test
            CommonOperationVolumes.wait_volume_status_ok(volume.name)
            logger.info("Added volume {0} successfully".format(volume.name))
        else:
            logger.info("Unhappy path testing, VERIFICATION skipped")
    if count > 0:
        logger.warn("Failure: Not able to create some of volumes, please check all warning messages")
        return False

    return True


def delete_storage_volume(name, deletefrom, fail_if_false=True):
    '''
        Delete a specific storage volume
    '''
    if not select_storage_volume(name):
        ui_lib.fail_test("Couldn't select storage volume {0}".format(name))
    DeleteVolumes.select_actions_delete()
    DeleteVolumes.wait_delete_dialog_shown()
    DeleteVolumes.choose_delete_volume_from(delete_from=deletefrom)
    DeleteVolumes.click_yes_delete_button()
    status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
    if status is True:
        ui_lib.fail_test(msg)
    DeleteVolumes.wait_delete_dialog_disappear()
    FusionUIBase.show_activity_sidebar()
    if CommonOperationVolumes.wait_volume_show_not_found(name, timeout=20, fail_if_false=False):
        logger.info("Volume status appear as 'not found', remove volume {0} successfully.".format(name))
    elif CommonOperationVolumes.verify_volume_not_exist(name, fail_if_false=False):
        logger.info("Remove volume {0} successfully".format(name))
    else:
        msg = "Volume {0} does not disappear in 20s!".format(name)
        if fail_if_false is True:
            ui_lib.fail_test(msg)
        else:
            logger.warn(msg)
            return False
    return True


def delete_storage_volumes(*storagevolumes_obj):
    '''
        Delete all storage volumes in list
    '''
    FusionUIBase.navigate_to_section(SectionType.VOLUMES)
    if isinstance(storagevolumes_obj, test_data.DataObj):
        storagevolumes_obj = [storagevolumes_obj]
    elif isinstance(storagevolumes_obj, tuple):
        storagevolumes_obj = list(storagevolumes_obj)
    count = 0

    for n, volume in enumerate(storagevolumes_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(storagevolumes_obj), '-' * 14))
        name = volume.name
        logger.info("Deleting a volume with name '{0}'".format(name))
        if not select_storage_volume(name):
            count += 1
            continue
        if getattr(volume, 'deletefromoneviewonly', '') != '':
            expect_list = ["true", "false"]
            FusionUIBase.para_should_be_in_list(expect_list, volume.deletefromoneviewonly)
            if volume.deletefromoneviewonly.lower() == 'true':
                delete_storage_volume(name, "OneView only")
            else:
                delete_storage_volume(name, "OneView and the storage system")
        else:
            delete_storage_volume(name, "OneView and the storage system")
    if count > 0:
        logger.warn("Failure: Not able to delete some of volume, please check warning messages.")
        return False
    return True


def verify_volume_links(*storagevolume_links):
    """ Verify storage volume links
    Arguments:
        volumename*              --  Name of storage system
        resourcename*            --  Page Name to verify (i.e. Volumes, Storage Systems, Storage Pools, Networks, SANs)
        viewname                 --  Name of tab view on volumes screen that link is located on

    * Required Argument

    Example:
        tests/strm/GUI/strm_data.xml -> @{TestData.strm.volumeslinks}
            <volumeslinks>
                <link  volumename="Cluster-1" resourcename="Storage Systems" viewname="General"/>
                <link  volumename="Cluster-1" resourcename="Storage Pools" viewname="General"/>
                <link  volumename="ThreePAR-1" resourcename="Volumes" viewname="General"/>
                <link  volumename="ThreePAR-1" resourcename="Storage Pools" viewname="Overview"/>
                <link  volumename="ThreePAR-1" resourcename="Storage Pools" viewname="Advanced"/>
            </volumeslinks>

    """
    FusionUIBase.navigate_to_section(SectionType.VOLUMES)
    if isinstance(storagevolume_links, test_data.DataObj):
        storagevol_obj = [storagevolume_links]
    elif isinstance(storagevolume_links, tuple):
        storagevol_obj = list(storagevolume_links)
    count = 0

    for n, storage in enumerate(storagevol_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(storagevol_obj), '-' * 14))
        if getattr(storage, 'volumename', '') != '':
            storage_volume_name = storage.volumename
        else:
            storage_volume_name = storage.volumename.lower().split('.')[0]
        if getattr(storage, 'resourcename', '') != '':
            storage_resource_name = storage.resourcename
        else:
            storage_resource_name = ""
        if getattr(storage, 'viewname', '') != '':
            storage_view_name = storage.viewname
        else:
            storage_view_name = "General"
        logger.info("Verifying link for {} on volumes '{}' screen".format(storage_resource_name, storage_volume_name))
        if not select_storage_volume(storage_volume_name):
            count += 1
            continue

        FusionUIBase.select_view_by_name(storage_view_name)
        time.sleep(5)
        logger.info("verify volumes link [%s] in %s view. verify count if needed." % (storage_resource_name, storage_view_name))
        if storage_resource_name == "Storage Pools":
            logger.info("Entered resource=%s" % storage_resource_name)
            if storage_view_name == "General":
                CommonOperationVolumes.click_storage_pools_link()
            else:
                CommonOperationVolumes.click_storage_pool_snapshot_link()
            CommonOperationStoragePools.verify_storagepools_title(storage_resource_name, timeout=10, fail_if_false=True)
            FusionUIBase.navigate_to_section(SectionType.VOLUMES)
        elif storage_resource_name == "Storage Systems":
            logger.info("Entered resource=%s" % storage_resource_name)
            CommonOperationVolumes.click_storage_system_link()
            CommonOperationStorageSystems.verify_system_page_title(storage_resource_name, timeout=10, fail_if_false=True)
            FusionUIBase.navigate_to_section(SectionType.VOLUMES)
        elif storage_resource_name == "Volume Templates":
            logger.info("Entered resource=%s" % storage_resource_name)
            CommonOperationVolumes.click_volume_template_link()
            CommonOperationVolumeTemplates.verify_volume_template_title(storage_resource_name, timeout=10, fail_if_false=True)
            FusionUIBase.navigate_to_section(SectionType.VOLUMES)

        else:
            return False


def create_volume_snapshots(*storagevolumesnapshots_obj):
    """ create snapshots volume
        This function is used to create snapshot volume from an existing volume
        Example:
            create_volume_snapshots(*storagevolumesnapshots_obj)

        Arguments:
        name*             --  Name of the storage volume for which snapshot need to be reverted.
        snapshotname*     --  Snapshot name for which revert need be done.
        storagename*      --  Name of the storage system that a volume is on.
        desc*              --  description for the newly creating volume.

        * Required Arguments

        <volumesnapshots>
            <snapshot name="volume" snapshotname="snapshotvol1" storagename="ThreePAR-1"desc="Took Snapshot"/>
        </volumesnapshots>

    """
    FusionUIBase.navigate_to_section(SectionType.VOLUMES)
    if isinstance(storagevolumesnapshots_obj, test_data.DataObj):
        storagevolumesnapshots_obj = [storagevolumesnapshots_obj]
    elif isinstance(storagevolumesnapshots_obj, tuple):
        storagevolumesnapshots_obj = list(storagevolumesnapshots_obj)
    count = 0

    for n, snapshot in enumerate(storagevolumesnapshots_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(storagevolumesnapshots_obj), '-' * 14))
        name = snapshot.name
        logger.info("Creating volume snapshot for a volume with name '{0}'".format(name))
        if not select_storage_volume(name):
            count += 1
            continue
        CreateVolumeSnapshot.select_actions_create_snapshot()
        CreateVolumeSnapshot.wait_create_snapshot_dialog_shown()
        if getattr(snapshot, 'testtype', '') == 'unhappy':      # negative path testing
            CreateVolumeSnapshot.input_description(snapshot.desc, fail_if_false=False)
        else:
            CreateVolumeSnapshot.input_description(snapshot.desc)
        if getattr(snapshot, 'testtype', '') == 'unhappy':      # negative path testing
            CreateVolumeSnapshot.input_name(snapshot.snapshotname, fail_if_false=False)
            CreateVolumeSnapshot.click_create()
        else:
            CreateVolumeSnapshot.input_name(snapshot.snapshotname)
        CreateVolumeSnapshot.click_create()

        if CreateVolumeSnapshot.wait_creating_message_disappear(timeout=20, fail_if_false=False):
            status, msg = FusionUIBase.get_error_message_from_dialog(timeout=7)
            if getattr(snapshot, "testtype", "") == "unhappy":
                status = False
                CreateVolumeSnapshot.click_create()
                CreateVolumeSnapshot.verify_create_snapshot_error(snapshot.emsg, snapshot.snapshotname)
                CreateVolumeSnapshot.click_cancel()
            else:
                FusionUIBase.show_activity_sidebar()
                FusionUIBase.wait_activity_action_ok(name, message="Create snapshot", timeout=20)

        if status is True:
            ui_lib.fail_test(msg)

    FusionUIBase.show_activity_sidebar()
    logger.info("{0} VERIFICATION {0}".format('-' * 17))
    for n, snapshot in enumerate(storagevolumesnapshots_obj):
        if not select_storage_volume(snapshot.name):
            ui_lib.fail_test("Couldn't select storage volume {0}".format(snapshot.name))
        if getattr(snapshot, 'testtype', '') != "unhappy":      # do not verify if unhappy test
            FusionUIBase.select_view_by_name('Snapshots')
            CommonOperationVolumes.verify_snapshots_exists(snapshot.snapshotname)
            logger.info("Create snapshot for volume {0} successfully".format(snapshot.name))
        else:
            logger.info("Unhappy path testing, VERIFICATION skipped")
    if count > 0:
        logger.warn("Failure: Not able to create snapshot for some of volumes, please check warning messages.")
        return False

    return True


def delete_volume_snapshots(version, *volumesnapshots_obj):
    '''
        delete volume snapshots in list
    '''
    FusionUIBase.navigate_to_section(SectionType.VOLUMES)
    if isinstance(volumesnapshots_obj, test_data.DataObj):
        volumesnapshots_obj = [volumesnapshots_obj]
    elif isinstance(volumesnapshots_obj, tuple):
        volumesnapshots_obj = list(volumesnapshots_obj)

    for n, volume in enumerate(volumesnapshots_obj):   # pylint: disable=W0612
        name = volume.name
        logger.info("Deleting volume snapshot for a volume with name '{0}'".format(name))
        if not select_storage_volume(name):
            continue
        FusionUIBase.select_view_by_name('Snapshots')
        DeleteVolumeSnapshots.select_delete_snapshot_icon()
        DeleteVolumeSnapshots.wait_delete_snapshot_dialog_shown()
        DeleteVolumeSnapshots.click_delete_button(appversion=version)
        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
        DeleteVolumeSnapshots.wait_delete_snapshot_dialog_disappear(timeout=10, fail_if_false=True)

        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(name, message="Delete snapshot", timeout=10)

        if status is True:
            ui_lib.fail_test(msg)

    return True


def add_storage_volume(*storagevolume_obj):
    '''
        add storage volumes in the list
    '''
    logger._log_to_console_and_log_file("Function call to add storage volumes ")
    selenium2lib = ui_lib.get_s2l()
    # Navigate to storage volume page
    if not selenium2lib._is_element_present(FusionStorageVolumesPage.ID_PAGE_LABEL):
        if not navigate():
            return False

    if isinstance(storagevolume_obj, test_data.DataObj):
        storagevolume_obj = [storagevolume_obj]
    elif isinstance(storagevolume_obj, tuple):
        storagevolume_obj = list(storagevolume_obj[0])

    for vol in storagevolume_obj:
        ui_lib.wait_for_element_and_click(FusionStorageVolumesPage.ID_LINK_ADD_VOLUME)
        ui_lib.wait_for_element_and_click(FusionStorageVolumesPage.ID_MENU_ACTION_ADD)
        ui_lib.wait_for_element_visible(FusionStorageVolumesPage.ID_INPUT_STORAGE_SYSTEM)

        if vol.has_property("storage_system") and vol.storage_system.strip() != "":
            ui_lib.wait_for_element_and_input_text(FusionStorageVolumesPage.ID_INPUT_STORAGE_SYSTEM, vol.storage_system)
        else:
            ui_lib.fail_test("storage system field should not be empty")

        if vol.has_property("description") and vol.description.strip() != "":
            ui_lib.wait_for_element_and_input_text(FusionStorageVolumesPage.ID_INPUT_ADD_DESCRIPTION, vol.description)

        if vol.has_property("storage_volume") and vol.storage_volume.strip() != "":
            ui_lib.wait_for_element_and_input_text(FusionStorageVolumesPage.ID_INPUT_STORAGE_VOLUME, vol.storage_volume)
        else:
            ui_lib.fail_test("storage volume field should not be empty")

        if vol.has_property("pool_type") and vol.pool_type.lower() == "shared":
            ui_lib.wait_for_element_and_click(FusionStorageVolumesPage.ID_RADIO_SHARED_POOL)

        ui_lib.wait_for_element_and_click(FusionStorageVolumesPage.ID_BTN_ADD_STORAGE_VOL)
        if ui_lib.wait_for_element_visible(FusionStorageVolumesPage.ID_ELEMENT_ADD_VOL_ERR_MSG):
            ui_lib.fail_test(ui_lib.get_text(FusionStorageVolumesPage.ID_ELEMENT_ADD_VOL_ERR_MSG))

        if select_storage_volume(vol.storage_volume):
            logger._log_to_console_and_log_file("Storage volume '{0}' is added successfully".format(vol.storage_volume))
        else:
            ui_lib.fail_test("Failed to add storage volume '{0}'".format(vol.storage_volume))

    storagevolume_list = [s.text.lower() for s in selenium2lib._element_find(FusionStorageVolumesPage.ID_ALL_VOLUMES_LIST, False, False)]
    if len(storagevolume_list) >= len(storagevolume_obj):
        logger._log_to_console_and_log_file("All Storage volumes are added successfully")
        return True
    else:
        ui_lib.fail_test("Failed to add some/all storage volumes")


def select_label_for_volume(volume_name, label):
    '''
        select label for volume
    '''
    logger._log_to_console_and_log_file("Function call to select label to storage volumes ")

    if not ui_lib.wait_for_element(FusionStorageVolumesPage.ID_PAGE_LABEL):
        if not navigate():
            return False

    ui_lib.wait_for_element_and_click(FusionStorageVolumesPage.ID_RESET_FILTER)
    if not select_storage_volume(volume_name):
        return False

    ui_lib.wait_for_element_and_click(FusionStorageVolumesPage.ID_DROPDOWN)
    ui_lib.wait_for_element_and_click(FusionStorageVolumesPage.ID_DROPDOWN_SELECTION)

    if ui_lib.wait_for_element_visible(FusionStorageVolumesPage.ID_ADDED_LABEL % label):
        logger._log_to_console_and_log_file("Storage volume {0} have Label {1}".format(volume_name, label))
        return True
    else:
        logger._warn("Storage volume {0} does not have Label {1}".format(volume_name, label))
        return False


def navigate():
    '''
        navigate to the volumes page
    '''
    FusionUIBase.navigate_to_section(SectionType.VOLUMES)
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionStorageVolumesPage.ID_PAGE_LABEL):
        logger._warn("Failed to navigate to Storage Volumes Page")
        return False
    else:
        return True


def delete_all_storage_volume():
    '''
        delete all storage volumes in oneview
    '''
    selenium2lib = ui_lib.get_s2l()

    if not selenium2lib._is_element_present(FusionStorageVolumesPage.ID_PAGE_LABEL):
        navigate()
    volume_list = [ui_lib.get_text(el) for el in selenium2lib._element_find(FusionStorageVolumesPage.ID_ALL_VOLUMES_LIST, False, False)]
    count = 0
    for volume_name in volume_list:
        if volume_name:
            logger._log_to_console_and_log_file("Deleting Volume: {0}".format(volume_name))

            storagevolume = volume_name
            deletefrom = "OneView and the storage system"
            volume_delete_status = delete_storage_volume(storagevolume, deletefrom)
            if volume_delete_status:
                logger._log_to_console_and_log_file("'{0}' volume is deleted Successfully".format(volume_name))
                count += 1
            else:
                logger._warn("Failed to delete volume: {0}".format(volume_name))

        else:
            count += 1  # volume name is null

    if count == len(volume_list):
        logger._log_to_console_and_log_file("All volumes deleted Successfully from appliance")
        return True
    else:
        logger.warn("Failed to delete {0} volumes: ".format(len(volume_list) - count))
        return False


def add_label_to_volume(*volume_label):
    """ add label to volume
        This function is to add label to volume
        Example:
            add_label_to_volume(*volume_label)
    """
    s2l = ui_lib.get_s2l()
    logger._log_to_console_and_log_file("Function call to add label to storage volumes ")

    if isinstance(volume_label, test_data.DataObj):
        volume_label = [volume_label]
    elif isinstance(volume_label, tuple):
        volume_label = list(volume_label[0])

    if not ui_lib.wait_for_element(FusionStorageVolumesPage.ID_PAGE_LABEL):
        if not navigate():
            return False

    for label in volume_label:
        ui_lib.refresh_browser(FusionUIBaseElements.ID_MENU_ONE_VIEW, PerfConstants.DEFAULT_SYNC_TIME)
        if not select_storage_volume(label.volumename):
            return False

        ui_lib.wait_for_element_and_click(FusionStorageVolumesPage.ID_DROPDOWN_PANEL_SELECTOR)
        ui_lib.wait_for_element_and_click(FusionStorageVolumesPage.ID_DROPDOWN_LABEL_LINK)

        logger._log_to_console_and_log_file("Adding label to volume '{0}'".format(label.volumename))
        if ui_lib.wait_for_element(FusionStorageVolumesPage.ID_EDIT_LABEL):
            ui_lib.move_to_element_and_click(FusionStorageVolumesPage.ID_LABEL, FusionStorageVolumesPage.ID_EDIT_LABEL)
            if ui_lib.wait_for_element(FusionStorageVolumesPage.ID_EDIT_LABEL_PANEL):
                ui_lib.wait_for_element_and_input_text(FusionStorageVolumesPage.ID_LABEL_NAME, label.name)
                ui_lib.wait_for_element_and_click(FusionStorageVolumesPage.ID_ADD_LABEL_BTN)
                if not ui_lib.wait_for_element(FusionStorageVolumesPage.ID_ERROR_MESSAGE):
                    ui_lib.wait_for_element_and_click(FusionStorageVolumesPage.ID_OK_LABEL_BTN)
                else:
                    error_msg = ui_lib.get_text(FusionStorageVolumesPage.ID_ERROR_MESSAGE)
                    logger._warn(error_msg)
                    ui_lib.wait_for_element_and_click(FusionStorageVolumesPage.ID_CANCEL_LABEL_BTN)
            else:
                logger._warn("Failed to navigate edit label panel")
                return False
        else:
            logger._warn("Could not find Edit button to add label")

        if ui_lib.wait_for_element(FusionStorageVolumesPage.ID_ADDED_LABEL % label.name):
            ui_lib.wait_for_element_and_click(FusionStorageVolumesPage.ID_ADDED_LABEL % label.name)
            volume_list = []
            ui_lib.wait_for_element(FusionStorageVolumesPage.ID_ALL_VOLUMES_LIST, PerfConstants.FUSION_PAGE_SYNC)
            volume_list = [ui_lib.get_text(s) for s in s2l._element_find(FusionStorageVolumesPage.ID_ALL_VOLUMES_LIST, False, False)]
            for volume in volume_list:
                if volume.lower() == label.volumename.lower():
                    logger._log_to_console_and_log_file("Label {0} is successfully added to the volume '{1}'".format(label.name, label.volumename))
                else:
                    logger._warn("Failed to add label to the selected volume")
                    return False
    return True


def revert_created_snapshot(*storagevolumesnapshots_obj):
    """ revert created snapshot
        This function is to revert the created snapshot using volume
        Example:
            revert_created_snapshot(*storagevolumesnashots_obj)

        Arguments:
        name*             --  Name of the storage volume for which snapshot need to be reverted.
        snapshotname*     --  Snapshot name for which revert need be done.

        * Required Arguments

        <revertsnapshot>
            <revertsnapshot name="volumename" snapshotname="snapshotname"/>
        </revertsnapshot>

    """
    FusionUIBase.navigate_to_section(SectionType.VOLUMES)
    if isinstance(storagevolumesnapshots_obj, test_data.DataObj):
        storagevolumesnapshots_obj = [storagevolumesnapshots_obj]
    elif isinstance(storagevolumesnapshots_obj, tuple):
        storagevolumesnapshots_obj = list(storagevolumesnapshots_obj)
    count = 0

    for n, volume in enumerate(storagevolumesnapshots_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(storagevolumesnapshots_obj), '-' * 14))
        name = volume.name
        if not select_storage_volume(name):
            count += 1
            continue
        CommonOperationVolumes.verify_snapshots_exists(volume.snapshotname)
        RevertVolumeSnapshot.click_revert(volume.snapshotname)
        RevertVolumeSnapshot.click_yes_revert()
        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
        if status is True:
            ui_lib.fail_test(msg)
        CreateVolumeSnapshot.wait_create_snapshot_dialog_disappear()
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(name, message="Revert", timeout=10)
        FusionUIBase.show_activity_sidebar()
        CommonOperationVolumes.wait_volume_status_ok(name)
        logger.info("Revert snapshot volume {0} successfully".format(name))
    if count > 0:
        ui_lib.fail_test("Failure: Not able to revert snapshot volumes, please check warning messages.")
    else:
        return True


def validate_storage_volume_existing_by_name(volume_name):
    """validate storage volume existing
        Arguments:
        name                --  Name of the storage volume to validate
    """
    FusionUIBase.navigate_to_section(SectionType.VOLUMES)
    if CommonOperationVolumes.verify_volume_exist(volume_name, timeout=5, fail_if_false=False):
        logger.info("Validating the Storage volume: '%s' is existing successfully." % volume_name)
        return True
    else:
        logger.warn("Failed to validate the Storage volume: '%s' is existing." % volume_name)
        return False


def validate_storage_volume_not_existing_by_name(volume_name):
    """validate storage volume not existing"""
    FusionUIBase.navigate_to_section(SectionType.VOLUMES)
    if not CommonOperationVolumes.verify_volume_exist(volume_name, timeout=5, fail_if_false=False):
        logger.info("Validating the Storage volume: '%s' is not existing successfully." % volume_name)
        return True
    else:
        logger.warn("Failed to validate the Storage volume: '%s' is not existing." % volume_name)
        return False


def create_volume_using_snapshot(*storagevolumesnapshots_obj):
    """ create volume using snapshot volume
        This function is to create volume using snapshot volume
        Example:
            create_volume_using_snapshot(*storagevolumesnapshots_obj)

        Arguments:
        name*             --  Name of the storage volume for which snapshot need to be reverted.
        snapshotname*     --  Snapshot name for which revert need be done.
        newvolume*        --  Specifying name for the newly creating volume.
        desc              --  description for the newly creating volume.
        sharing*          --  specifying volume sharing type.
        poolname          --  specifying pool name of the storage system.
        storagename       --  specifying storage name of the storage system.
        snapshotpool      --  specifying snapshotpool name of the storage system.

        * Required Arguments

        <createsnapshotvolume>
            <createsnapshotvolume name="volume" snapshotname="snapshotvol1" newvolume="newvolume" desc="description" sharing="shared" poolname="cosmos-cpg" storagename="P7400-COSMOS" snapshotpool="cosmos-cpg"/>
        </createsnapshotvolume>

    """
    FusionUIBase.navigate_to_section(SectionType.VOLUMES)
    if isinstance(storagevolumesnapshots_obj, test_data.DataObj):
        storagevolumesnapshots_obj = [storagevolumesnapshots_obj]
    elif isinstance(storagevolumesnapshots_obj, tuple):
        storagevolumesnapshots_obj = list(storagevolumesnapshots_obj)
    count = 0

    for n, volume in enumerate(storagevolumesnapshots_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(storagevolumesnapshots_obj), '-' * 14))
        name = volume.name
        if not select_storage_volume(name):
            count += 1
            continue
        FusionUIBase.select_view_by_name('Snapshots')
        # if getattr(volume, 'testtype', '') != 'unhappy':  # happy path
        CommonOperationVolumes.verify_snapshots_exists(volume.snapshotname)
        CreateVolumeUsingSnapshot.click_create_volume(volume.snapshotname)
        CreateVolumeUsingSnapshot.input_volume_name(volume.newvolume)
        CreateVolumeUsingSnapshot.input_description(volume.desc)
        if getattr(volume, 'testtype', '') != 'unhappy':  # happy path
            if getattr(volume, 'poolname', '') != '':
                if getattr(volume, 'storagename', '') != '':
                    CreateVolumeUsingSnapshot.input_select_storage_pool(volume.poolname, volume.storagename)
                else:
                    CreateVolumeUsingSnapshot.input_select_storage_pool(volume.poolname, "")
            if getattr(volume, 'snapshotpool', '') != '':
                if getattr(volume, 'storagename', '') != '':
                    CreateVolumeUsingSnapshot.input_select_snapshot_storage_pool(volume.snapshotpool, volume.storagename)
                else:
                    logger.warn("user didn't specify 'storagename', choose the default one")
                    CreateVolumeUsingSnapshot.input_select_snapshot_storage_pool(volume.snapshotpool, "")

            if getattr(volume, 'sharing', '') != '':
                CreateVolumeUsingSnapshot.choose_sharing(volume.sharing)
        else:
            if getattr(volume, 'poolname', '') != '':
                if getattr(volume, 'storagename', '') != '':
                    CreateVolumeUsingSnapshot.input_select_storage_pool(volume.poolname, volume.storagename,
                                                                        fail_if_false=False)
                else:
                    CreateVolumeUsingSnapshot.input_select_storage_pool(volume.poolname, "", fail_if_false=False)
            if getattr(volume, 'snapshotpool', '') != '':
                if getattr(volume, 'storagename', '') != '':
                    CreateVolumeUsingSnapshot.input_select_snapshot_storage_pool(volume.snapshotpool,
                                                                                 volume.storagename,
                                                                                 fail_if_false=False)
                else:
                    logger.warn("user didn't specify 'storagename', choose the default one")
                    CreateVolumeUsingSnapshot.input_select_snapshot_storage_pool(volume.snapshotpool, "",
                                                                                 fail_if_false=False)

            if getattr(volume, 'sharing', '') != '':
                CreateVolumeUsingSnapshot.choose_sharing(volume.sharing, fail_if_false=False)

        CreateVolumeUsingSnapshot.click_create()
        if CreateVolumeUsingSnapshot.wait_creating_message_disappear(timeout=20, fail_if_false=False):
            status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
            if getattr(volume, 'testtype', '') == 'unhappy':
                status = False
                CreateVolumeUsingSnapshot.click_create()
                CreateVolumeUsingSnapshot.verify_create_volume_from_snapshot_error(volume.emsg, name, 1, True)
                CreateVolumeUsingSnapshot.click_cancel()
            else:
                FusionUIBase.wait_activity_action_ok(name, message='Create', timeout=40)
                CreateVolumeSnapshot.wait_create_snapshot_dialog_disappear()
                FusionUIBase.show_activity_sidebar()
                FusionUIBase.wait_activity_action_ok(volume.newvolume, message="Create", timeout=30)
                FusionUIBase.show_activity_sidebar()
                CommonOperationVolumes.wait_volume_status_ok(volume.newvolume)
                logger.info("Creating volume {0} using snapshot volume is successfully".format(volume.newvolume))

            if status is True:
                ui_lib.fail_test(msg)

    if count > 0:
        ui_lib.fail_test("Failure: Not able to create volume using specified snapshot volume")
    else:
        return True


# begin - verify storage volume
def verify_storage_volume(*storagevolume_obj):
    """validate storage volume existing and navigating to different tabs
        Arguments:
        name                --  Name of the storage volume to validate
    """

    FusionUIBase.navigate_to_section(SectionType.VOLUMES)
    if isinstance(storagevolume_obj, test_data.DataObj):
        storagevolume_obj = [storagevolume_obj]
    elif isinstance(storagevolume_obj, tuple):
        storagevolume_obj = list(storagevolume_obj)
    count = 0

    for n, volume in enumerate(storagevolume_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(storagevolume_obj), '-' * 14))
        name = volume.name
        logger.info("Verifying a volume with name '{0}'".format(name))
        if not select_storage_volume(name):
            count += 1
            continue

        CommonOperationVolumes.verify_volume_exist(volume.name)
        CommonOperationVolumes.click_volume(volume.name)
        VerifyStorageVolume.verify_storagevolume_title(volume.name)
        FusionUIBase.select_view_by_name('General')
        logger.info("Verifying configuration in General view...")
        VerifyStorageVolume.verify_storagevolume_Navigation_Tab_Text('General', 'general')
        time.sleep(5)
        if hasattr(volume, "state"):
            VerifyStorageVolume.verify_general_state(volume.state)

        # Volume Properties
        FusionUIBase.select_view_by_name('Volume Properties')
        VerifyStorageVolume.verify_storagevolume_Navigation_Tab_Text('Volume Properties', 'volume-properties')

        # Advanced
        FusionUIBase.select_view_by_name('Advanced')
        VerifyStorageVolume.verify_storagevolume_Navigation_Tab_Text('Advanced', 'advanced')

        # Snapshots
        if getattr(volume, 'storagename', '') == 'ThreePAR-1':
            FusionUIBase.select_view_by_name('Snapshots')
            VerifyStorageVolume.verify_storagevolume_Navigation_Tab_Text('Snapshots', 'snapshots')

        # Storage Volume Attachments
        FusionUIBase.select_view_by_name("Volume Attachments")
        VerifyStorageVolume.verify_storagevolume_Navigation_Tab_Text('Volume Attachments', 'attachments')


# begin - verify storage volume inconsistent
def verify_storage_volume_inconsistent(*storagevolume_obj):
    """validate storage volume inconsistent with volume template
        Arguments:
        name                --  Name of the storage volume to validate
    """

    if isinstance(storagevolume_obj, test_data.DataObj):
        storagevolume_obj = [storagevolume_obj]
    elif isinstance(storagevolume_obj, tuple):
        storagevolume_obj = list(storagevolume_obj)
    count = 0

    for n, volume in enumerate(storagevolume_obj):
        FusionUIBase.navigate_to_section(SectionType.VOLUME_TEMPLATES)
        if getattr(volume, 'template_name', '') != '':
            template_name = volume.template_name
            logger.info("Editing a volume template with name '{0}'".format(template_name))
            if not select_storage_template(template_name):
                count += 1
                continue
            EditVolumeTemplates.select_actions_edit()
            EditVolumeTemplates.wait_edit_dialog_shown()
            if getattr(volume, 'sharing', '') != '':
                EditVolumeTemplates.lock_template_properties('pool-sharing')
                EditVolumeTemplates.choose_sharing(volume.sharing)
                time.sleep(7)
            if getattr(volume, 'snapshotpool_warning', '') != '':
                EditVolumeTemplates.input_select_snapshot_storage_pool(volume.snapshotpool_warning, volume.storagename)
            if getattr(volume, 'dplevel_warning', '') != '':
                EditVolumeTemplates.choose_data_protection_level(volume.dplevel_warning)
            if getattr(volume, 'folder_warning', '') != '':
                EditVolumeTemplates.choose_folder(volume.folder_warning)
            if getattr(volume, 'performancepolicy_warning', '') != '':
                EditVolumeTemplates.choose_performance_policy(volume.performancepolicy_warning)
            if getattr(volume, 'volumeset_warning', '') != '':
                EditVolumeTemplates.choose_volume_set(volume.volumeset_warning)

            EditVolumeTemplates.click_ok_button()
            status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
            if status is True:
                ui_lib.fail_test(msg)
            EditVolumeTemplates.wait_edit_dialog_disappear(timeout=10)
            FusionUIBase.show_activity_sidebar()
            FusionUIBase.wait_activity_action_ok(template_name, message="Update", timeout=10)
            FusionUIBase.show_activity_sidebar()
            CommonOperationVolumeTemplates.wait_volume_template_status_ok(template_name)
            logger.info("Edit volume template {0} successfully".format(template_name))
            if count > 0:
                logger.warn("Failure: Not able to edit some of storage volume templates, please check all warning messages")
                return False

            logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(storagevolume_obj), '-' * 14))
            name = volume.name
            logger.info("Editing a volume with name '{0}'".format(name))
            if not select_storage_volume(name):
                count += 1
                continue
            EditVolumes.select_actions_edit()
            EditVolumes.wait_edit_dialog_shown()
            if getattr(volume, 'sharing', '') != '':
                actual_msg = EditVolumes.get_volume_inconsistent_warning_msg('shareable')
                expected_msg = "Warning: Shared is inconsistent with the template."
                if actual_msg != expected_msg:
                    ui_lib.fail_test(actual_msg)
            if getattr(volume, 'snapshotpool_warning', '') != '':
                actual_msg = EditVolumes.get_volume_inconsistent_warning_msg('snapshotpool')
                expected_msg = "Warning: FST_CPG1 is inconsistent with the template."
                if actual_msg != expected_msg:
                    ui_lib.fail_test(actual_msg)
            if getattr(volume, 'dplevel_warning', '') != '' and getattr(volume, 'template_name', '') != '':
                actual_msg = EditVolumes.get_volume_inconsistent_warning_msg('networkraid')
                expected_msg = "Warning: Network RAID-10 (2-Way Mirror) is inconsistent with the template."
                if actual_msg != expected_msg:
                    ui_lib.fail_test(actual_msg)
            if getattr(volume, 'folder_warning', '') != '' and getattr(volume, 'template_name', '') != '':
                actual_msg = EditVolumes.get_volume_inconsistent_warning_msg('folder')
                expected_msg = "Warning: folder-2 is inconsistent with the template."
                if actual_msg != expected_msg:
                    ui_lib.fail_test(actual_msg)
            if getattr(volume, 'performancepolicy_warning', '') != '' and getattr(volume, 'template_name', '') != '':
                actual_msg = EditVolumes.get_volume_inconsistent_warning_msg('performancePolicy-warning')
                expected_msg = "Warning: Default is inconsistent with the template."
                if actual_msg != expected_msg:
                    ui_lib.fail_test(actual_msg)
            if getattr(volume, 'volumeset_warning', '') != '' and getattr(volume, 'template_name', '') != '':
                actual_msg = EditVolumes.get_volume_inconsistent_warning_msg('volumeSet')
                expected_msg = "Warning: vol-set-10 is inconsistent with the template."
                if actual_msg != expected_msg:
                    ui_lib.fail_test(actual_msg)
            EditVolumes.click_ok_button()
            status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
            if status is True:
                ui_lib.fail_test(msg)
            EditVolumes.wait_edit_dialog_disappear(timeout=10)
            FusionUIBase.show_activity_sidebar()
            FusionUIBase.wait_activity_action_ok(name, message="Update", timeout=30)
            FusionUIBase.show_activity_sidebar()
            logger.info("Verify volume {0} successfully".format(name))
            FusionUIBase.navigate_to_section(SectionType.VOLUME_TEMPLATES)
            if not select_storage_template(template_name):
                count += 1
                continue
            EditVolumeTemplates.select_actions_edit()
            EditVolumeTemplates.wait_edit_dialog_shown()
            if getattr(volume, 'sharing', '') != '':
                EditVolumeTemplates.lock_template_properties('pool-sharing')
            EditVolumeTemplates.click_ok_button()
    if count > 0:
        ui_lib.fail_test("Failure: Not able to verify volume inconsistent with volume template")
    else:
        return True

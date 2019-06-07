'''
Created on Mar 11, 2014

@author: Administrator
'''


from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.base import SectionType
from FusionLibrary.ui.business_logic.base import FusionUIBase
from robot.libraries.BuiltIn import BuiltIn
from FusionLibrary.ui.business_logic.storage.volumes import CommonOperationVolumes
from FusionLibrary.ui.business_logic.storage.volumetemplates import CommonOperationVolumeTemplates
from FusionLibrary.ui.business_logic.storage.storagesystems import CommonOperationStorageSystems
from RoboGalaxyLibrary.data import test_data
import time
from FusionLibrary.ui.business_logic.storage.storagepools import (CommonOperationStoragePools,
                                                                  EditStoragePools,
                                                                  RefreshStoragePools,
                                                                  )


def navigate():
    '''
        Navigate to the storage pools page
    '''
    FusionUIBase.navigate_to_section(SectionType.STORAGE_POOLS)


def select_storage_pool(storagepoolname, storagesystemname):
    '''
        Select a specific pool on the storage pools page
    '''
    logger.info("Selecting a storage pool with name %s" % storagepoolname)

    # Selecting the storage pool
    if not CommonOperationStoragePools.verify_storage_pool_exist(storagepoolname, storagesystemname, fail_if_false=False):
        logger.warn("System Storage Pool '%s' is not present" % storagepoolname)
        ui_lib.get_s2l().capture_page_screenshot()
        return False
    else:
        CommonOperationStoragePools.click_storage_pool(storagepoolname, storagesystemname)
        CommonOperationStoragePools.wait_storage_pool_selected(storagepoolname, storagesystemname)
        logger.info("Selected the System Storage pool %s successfully" % storagepoolname)
        return True


def edit_storage_pools(storage_pool_obj):
    """ Edit Storage Pools

    Arguments:
      name*           --  Name of storage pool.
      storagename*    --  short name of the storage system where the storage pool is located in, this is displayed on Storage Pools page on the main table list.
      state*          --  storage pool's state that you want to change to.

    * Required Arguments

    Example:
        tests/RIST/OVST/OVAQual_data.xml    -> @{TestData.storagepools}
        <storagepools>
            <storagepool name="FC_OVA_r1" storagename="wpst3par-7200-12-srv" state="Managed" />
            <storagepool name="FC_OVA_r5" storagename="wpst3par-7200-12-srv" state="Discovered" />
            <storagepool name="FC_OVA_r6" storagename="wpst3par-7200-12-srv" state="Managed" />
        </storagepools>

    """
    logger.info("Function call to edit Storage Pool(s)")
    navigate()

    for index, pool in enumerate(storage_pool_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((index + 1), len(storage_pool_obj), '-' * 14))
        logger.info("editing a storage pool with name '%s' ..." % pool.name)
        FusionUIBase.show_activity_sidebar() if index == 0 else None
        CommonOperationStoragePools.click_storage_pool(pool.name, pool.storagename)
        CommonOperationStoragePools.wait_storage_pool_selected(pool.name, pool.storagename)
        state = CommonOperationStoragePools.get_storage_pool_status(pool.name, pool.storagename)
        EditStoragePools.select_action_edit()
        EditStoragePools.wait_edit_storage_pool_dialog_open()
        if getattr(pool, 'state', '').lower() in ('managed', 'discovered'):
            EditStoragePools.tick_state_as_managed() if pool.state.lower() == 'managed' else None
            EditStoragePools.tick_state_as_discovered() if pool.state.lower() == 'discovered' else None
            EditStoragePools.click_ok_button()
            EditStoragePools.wait_edit_storage_pool_dialog_close()

            status, msg = FusionUIBase.get_error_message_from_dialog(timeout=7)
            if status is True:
                logger.warn("Failed to edit storage pool [ %s ] due to error occurred: [ %s ]" % (pool.name, msg))
                ui_lib.fail_test(msg)
                return False

            if state == 'disabled' and pool.state.lower() == 'managed':
                FusionUIBase.wait_activity_action_ok(pool.name, message="Update", timeout=7, fail_if_false=True)
                if CommonOperationStoragePools.wait_storage_pool_status_ok(pool.name, pool.storagename, timeout=5) is True:
                    logger.debug("Successfully edited storage pool [ %s ]" % pool.name)
                else:
                    msg = "Failed to edit storage pool [ %s ]" % pool.name
                    return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=True)
            elif state == 'ok' and pool.state.lower() == 'discovered':
                FusionUIBase.wait_activity_action_ok(pool.name, message="Update", timeout=7, fail_if_false=True)
                if CommonOperationStoragePools.wait_storage_pool_status_disabled(pool.name, pool.storagename, timeout=7) is True:
                    logger.debug("Successfully edited storage pool [ %s ]" % pool.name)
                else:
                    msg = "Failed to edit storage pool [ %s ]" % pool.name
                    return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=True)
            else:
                logger.debug("Successfully edited storage pool [ %s ]" % pool.name)
        else:
            msg = "<test data invalid> attribute 'state' value '%s' of storage pool '%s' is invalid, should be 'Managed' or 'Discovered'" % (getattr(pool, 'state', ''), pool.name)
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=True)

        FusionUIBase.show_activity_sidebar() if index == len(storage_pool_obj) - 1 else None

    logger.info("-" * 24)
    logger.info("Successfully edited all %s storage pool(s)" % len(storage_pool_obj))
    return True


def refresh_storage_pool(storagepoolname, storage_system_name):
    '''
       Refresh the storage pools
    '''
    navigate()
    logger.info("Function call to Refresh a storage pool with name %s" % storagepoolname)
    selenium2lib = ui_lib.get_s2l()
    if not select_storage_pool(storagepoolname, storage_system_name):
        logger.warn("FAILURE :Not able to select the requested storage pool - '%s', Exiting the refresh_storage_pool function" % storagepoolname)
        selenium2lib.capture_page_screenshot()
        return False

    # Action > Refresh
    RefreshStoragePools.select_actions_refresh()

    # check for notification and Status Bar for status.
    if RefreshStoragePools.wait_general_state_refreshing():
        CommonOperationStoragePools.wait_progress_ongoing_disappear()
        BuiltIn().sleep(6)
        logger.info("Status bar update completed -  %s" % storagepoolname)
        CommonOperationStoragePools.wait_progress_ok_shown()
        CommonOperationStoragePools.get_notification_message()
        if RefreshStoragePools.wait_general_state_configured():
            logger.info("SUCCESS : REFRESH completed detected for storage pool -  %s" % storagepoolname)
            return True
        else:
            logger.warn("FAILURE : REFRESH for STORAGE POOL -'%s' did not indiate completed" % storagepoolname)
            selenium2lib.capture_page_screenshot()
            return False
    else:
        logger.warn("FAILURE : Did not detect the pool state after REFRESH for STORAGE POOL -'%s' failed" % storagepoolname)
        selenium2lib.capture_page_screenshot()
        return False


def verify_storage_pool_links(*storagepool_links):
    """ Verify storage pool links
    Arguments:
        poolname*              --  Name of storage pool
        systemname*            --  Name of the storage ssytem that pool is on
        resourcename*          --  Page Name to verify (i.e. Volumes, Storage Systems, Storage Pools, Networks, SANs)
        viewname               --  Name of tab view on storage systems screen that link is located on

    * Required Argument

    Example:
        tests/strm/GUI/strm_data.xml -> @{TestData.strm.poollinks}
            <poollinks>
                <link  poolname="Cluster-1" systemname="Cluster-1" resourcename="Storage Systems" viewname="Overview"/>
                <link  poolname="Cluster-1" systemname="Cluster-1" resourcename="Volumes" viewname="Overview"/>
                <link  poolname="FST_CPG1" systemname="ThreePAR-1" resourcename="Storage Systems" viewname="Overview"/>
                <link  poolname="FST_CPG1" systemname="ThreePAR-1-1" resourcename="Volumes" viewname="Overview"/>
          </poollinks>

    """
    FusionUIBase.navigate_to_section(SectionType.STORAGE_POOLS)
    if isinstance(storagepool_links, test_data.DataObj):
        storagepool_obj = [storagepool_links]
    elif isinstance(storagepool_links, tuple):
        storagepool_obj = list(storagepool_links)
    count = 0

    for n, storage in enumerate(storagepool_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(storagepool_links), '-' * 14))
        if getattr(storage, 'poolname', '') != '':
            storage_pool_name = storage.poolname
        else:
            storage_pool_name = storage.poolname.lower().split('.')[0]
        if getattr(storage, 'systemname', '') != '':
            storage_system_name = storage.systemname
        else:
            storage_system_name = storage.systemname.lower().split('.')[0]
        if getattr(storage, 'resourcename', '') != '':
            storage_resource_name = storage.resourcename
        else:
            storage_resource_name = ""
        if getattr(storage, 'viewname', '') != '':
            storage_view_name = storage.viewname
        else:
            storage_view_name = "Overview"
        logger.info("Verifying link for {} on storage pool '{}' screen".format(storage_resource_name, storage_pool_name))
        if not select_storage_pool(storage_pool_name, storage_system_name):
            count += 1
            continue

        FusionUIBase.select_view_by_name(storage_view_name)
        time.sleep(5)
        logger.info("verify storage pool link [%s] in %s view. verify count if needed." % (storage_resource_name, storage_view_name))
        if storage_resource_name == "Storage Systems":
            logger.info("Entered resource=%s" % storage_resource_name)
            CommonOperationStoragePools.click_storage_system_link()
            CommonOperationStorageSystems.verify_system_page_title(storage_resource_name, timeout=10, fail_if_false=True)
            FusionUIBase.navigate_to_section(SectionType.STORAGE_POOLS)
        elif storage_resource_name == "Volumes":
            logger.info("Entered resource=%s" % storage_resource_name)
            CommonOperationStoragePools.click_used_by_volumes_link()
            CommonOperationVolumes.verify_storagevolumes_title(storage_resource_name, timeout=10, fail_if_false=True)
            FusionUIBase.navigate_to_section(SectionType.STORAGE_POOLS)
        elif storage_resource_name == "Storage Templates":
            logger.info("Entered resource=%s" % storage_resource_name)
            CommonOperationStoragePools.click_used_by_template_link()
            CommonOperationVolumeTemplates.verify_volume_template_title(storage_resource_name, timeout=10, fail_if_false=True)
            FusionUIBase.navigate_to_section(SectionType.STORAGE_POOLS)
        else:
            return False

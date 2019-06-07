'''
Created on Mar 11, 2014

@author: Administrator
'''


from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.base import SectionType
from FusionLibrary.ui.business_logic.base import FusionUIBase
# from robot.libraries.BuiltIn import BuiltIn
from FusionLibrary.ui.business_logic.storage.volumes import CommonOperationVolumes
from FusionLibrary.ui.business_logic.storage.volumetemplates import CommonOperationVolumeTemplates
from FusionLibrary.ui.business_logic.storage.storagesystems import CommonOperationStorageSystems
from FusionLibrary.ui.business_logic.storage.volumesets import CommonOperationVolumeSets
from RoboGalaxyLibrary.data import test_data
import time


def navigate():
    """
        Navigates to the Volume Sets Page
    """
    FusionUIBase.navigate_to_section(SectionType.VOLUME_SETS)


def select_volume_set(volumesetname, storagesystemname):
    """
        On the Volume Sets Page, select a specific volumeset
    """
    logger.info("Selecting a volume set with name %s" % volumesetname)

    # Selecting the volume set
    if not CommonOperationVolumeSets.verify_volumeset_exist(volumesetname, storagesystemname, fail_if_false=False):
        logger.warn("Volume Set '%s' is not present" % volumesetname)
        ui_lib.get_s2l().capture_page_screenshot()
        return False
    else:
        CommonOperationVolumeSets.click_volumeset(volumesetname, storagesystemname)
        CommonOperationVolumeSets.wait_volumeset_selected(volumesetname, storagesystemname)
        logger.info("Selected the Volume Set %s successfully" % volumesetname)
        return True


def verify_no_actions_exist():
    """
        On the Volume Sets Page, verify that the action menu does not exist
    """
    FusionUIBase.navigate_to_section(SectionType.VOLUME_SETS)
    logger.info("Verify action button doesnot exist on volume sets screen")
    status = CommonOperationVolumeSets.verify_no_volumeset_action_menu()
    if status is True:           # should be false for not found
        ui_lib.fail_test("Action button found in error")


def verify_volume_sets(*volumesets_obj):
    """
        On the Volume Sets Page, verify that the volumeset in the datafile exists on the screen
    """
    FusionUIBase.navigate_to_section(SectionType.VOLUME_SETS)
    if isinstance(volumesets_obj, test_data.DataObj):
        sets_obj = [volumesets_obj]
    elif isinstance(volumesets_obj, tuple):
        sets_obj = list(volumesets_obj)

    count = 0
    total_count = len(sets_obj)
    for n, volumeset in enumerate(sets_obj):  # pylint: disable=W0612
        name = volumeset.name
        system = volumeset.system
        logger.info("Verifying that volume set with name '{0}' exists".format(name))
        if not select_volume_set(name, system):
            continue
        else:
            count += 1
    if total_count != count:
        ui_lib.fail_test("Did not find all the volumesets")


def verify_volume_set_links(*volumeset_links):
    """ Verify volume sets links
    Arguments:
        setname*              --  Name of storage pool
        systemname*           --  Name of the storage system that volume set is on
        resourcename*         --  Page Name to verify (i.e. Volume Sets, Storage Systems, Volumes, etc)
        viewname              --  Name of tab view on Volume Sets that link is located on

    * Required Argument

    Example:
        tests/strm/GUI/strm_data.xml -> @{TestData.strm.volumesetslinks}
            <volumesetslink>
                <link setname="vol-set-5" systemname="NSA79-Group" resourcename="Volume Sets" viewname="Overview"/>
                <link setname="vol-set-6" systemname="NSA79-Group" resourcename="Volume Sets" viewname="Overview"/>
            </volumesetslink>

    """
    FusionUIBase.navigate_to_section(SectionType.VOLUME_SETS)
    if isinstance(volumeset_links, test_data.DataObj):
        volumeset_obj = [volumeset_links]
    elif isinstance(volumeset_links, tuple):
        volumeset_obj = list(volumeset_links)
    count = 0

    for n, volumeset in enumerate(volumeset_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(volumeset_links), '-' * 14))
        if getattr(volumeset, 'setname', '') != '':
            volume_set_name = volumeset.setname

        if getattr(volumeset, 'systemname', '') != '':
            storage_system_name = volumeset.systemname
        else:
            storage_system_name = volumeset.systemname.lower().split('.')[0]

        if getattr(volumeset, 'resourcename', '') != '':
            storage_resource_name = volumeset.resourcename
        else:
            storage_resource_name = ""

        if getattr(volumeset, 'viewname', '') != '':
            storage_view_name = volumeset.viewname
        else:
            storage_view_name = "Overview"
        logger.info("Verifying link for {} on '{}' volume sets screen".format(storage_resource_name, volume_set_name))
        if not select_volume_set(volume_set_name, storage_system_name):
            count += 1
            continue

        FusionUIBase.select_view_by_name(storage_view_name)
        time.sleep(3)
        logger.info("verify volume set link [%s] in %s view. verify count if needed." % (storage_resource_name, storage_view_name))
        logger.info("Entered resource=%s" % storage_resource_name)
        if storage_resource_name == "Storage Systems":
            CommonOperationVolumeSets.click_storage_system_link()
            CommonOperationStorageSystems.verify_system_page_title(storage_resource_name, timeout=10, fail_if_false=True)
            FusionUIBase.navigate_to_section(SectionType.VOLUME_SETS)
        elif storage_resource_name == "Volumes":
            CommonOperationVolumeSets.click_volumes_link()
            CommonOperationVolumes.verify_storagevolumes_title(storage_resource_name, timeout=10, fail_if_false=True)
            FusionUIBase.navigate_to_section(SectionType.VOLUME_SETS)
        elif storage_resource_name == "Volume Templates":
            CommonOperationVolumeSets.click_volume_template_link()
            CommonOperationVolumeTemplates.verify_volume_template_title(storage_resource_name, timeout=10, fail_if_false=True)
            FusionUIBase.navigate_to_section(SectionType.VOLUME_SETS)
        else:
            return False

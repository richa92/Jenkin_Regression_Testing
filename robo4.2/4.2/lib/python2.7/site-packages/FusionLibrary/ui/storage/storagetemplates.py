'''
Created on Mar 20, 2014

'''
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.general.base_page import FusionUIBaseElements
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.storage.storagetemplates_elements import FusionStorageTemplatesPage
from FusionLibrary.ui.business_logic.storage.volumetemplates import CommonOperationVolumeTemplates
from FusionLibrary.ui.business_logic.storage.volumetemplates import CreateVolumeTemplates
from FusionLibrary.ui.business_logic.storage.volumetemplates import EditVolumeTemplates
from FusionLibrary.ui.business_logic.storage.volumetemplates import DeleteVolumeTemplates
from FusionLibrary.ui.business_logic.storage.volumetemplates import EditVolumeTemplatesSettings
from FusionLibrary.ui.business_logic.storage.storagesystems import CommonOperationStorageSystems
from FusionLibrary.ui.business_logic.storage.storagepools import CommonOperationStoragePools
from FusionLibrary.ui.business_logic.storage.volumes import CommonOperationVolumes
from FusionLibrary.ui.business_logic.base import FusionUIBase
from FusionLibrary.ui.business_logic.base import SectionType
from RoboGalaxyLibrary.utilitylib import logging as logger
import time


def select_storage_template(volumetemplatename):
    FusionUIBase.navigate_to_section(SectionType.VOLUME_TEMPLATES)
    logger.info("Selecting a volume template with name {0}".format(volumetemplatename))
    if CommonOperationVolumeTemplates.verify_volume_template_exist(volumetemplatename, fail_if_false=False):
        if CommonOperationVolumeTemplates.verify_locate_error_exists():
            selenium2lib = ui_lib.get_s2l()
            selenium2lib.reload_page()
        CommonOperationVolumeTemplates.click_volume_template(volumetemplatename)
        CommonOperationVolumeTemplates.wait_volume_template_selected(volumetemplatename)
        return True
    else:
        logger.warn("Volume template '{0}' does not exist".format(volumetemplatename))
        return False


def create_storage_volume_templates(*volumetemplates_obj):
    FusionUIBase.navigate_to_section(SectionType.VOLUME_TEMPLATES)
    if isinstance(volumetemplates_obj, test_data.DataObj):
        volumetemplates_obj = [volumetemplates_obj]
    elif isinstance(volumetemplates_obj, tuple):
        volumetemplates_obj = list(volumetemplates_obj)
    count = 0
    new_volumetemplates_obj = []
    logger.info("{0} PREPARATION  {0}".format('-' * 17))
    for n, volume_template in enumerate(volumetemplates_obj):
        name = volume_template.name
        if getattr(volume_template, 'remove_if_exists', 'true').lower() == 'true':
            remove_if_exists = True
        else:
            remove_if_exists = False
        if not CommonOperationVolumeTemplates.verify_volume_template_not_exist(name, fail_if_false=False):
            logger.warn("Volume '{0}' already exists".format(name))
            if remove_if_exists is True:
                logger.info("Removing the volume since 'remove_if_exists' is set to 'True'")
                if not delete_storage_volume_template(name, fail_if_false=False):
                    count += 1
                else:
                    new_volumetemplates_obj.append(volume_template)
            else:
                logger.warn("Error: Would not able to create the existing volume '%s'." % name)
                count += 1
        else:
            new_volumetemplates_obj.append(volume_template)

    for n, volume_template in enumerate(new_volumetemplates_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(volumetemplates_obj), '-' * 14))
        name = volume_template.name
        logger.info("Adding a volume template with name '{0}'".format(name))
        if n == 0:
            FusionUIBase.show_activity_sidebar()
            CreateVolumeTemplates.click_create_volume_template_button()
        CreateVolumeTemplates.wait_create_volume_template_dialog_shown()
        CreateVolumeTemplates.input_name(name)
        CreateVolumeTemplates.input_description(volume_template.desc)
        CreateVolumeTemplates.input_select_storage_pool(volume_template.poolname, volume_template.storagename)
        if getattr(volume_template, 'snapshotpool', '') != '':
            CreateVolumeTemplates.input_select_snapshot_storage_pool(volume_template.snapshotpool, volume_template.storagename)
        # CreateVolumeTemplates.select_volume_properties_section()
        CreateVolumeTemplates.input_capacity(volume_template.capacity)
        CreateVolumeTemplates.select_provisioning(volume_template.provisioning)
        CreateVolumeTemplates.choose_sharing(volume_template.sharing)
        if getattr(volume_template, 'data_protection_level', '') != '':
            CreateVolumeTemplates.choose_data_protection_level(volume_template.data_protection_level)
        if getattr(volume_template, 'permitAdaptiveOptimization', '') != '':
            if volume_template.permitAdaptiveOptimization.lower().strip() == "yes":
                logger.debug("choose permit adaptive optimization  Yes")
                CreateVolumeTemplates.choose_permit_adaptive_optimization(permitAdaptiveOptimization=True)
            elif volume_template.permitAdaptiveOptimization.lower().strip() == "no":
                logger.debug("choose permit adaptive optimization  No")
                CreateVolumeTemplates.choose_permit_adaptive_optimization(permitAdaptiveOptimization=False)
            else:
                logger.info("the permit adaptive optimization is not correct ")
                return False
        if getattr(volume_template, "performancepolicy", '') != '':
            CreateVolumeTemplates.choose_performance_policy(volume_template.performancepolicy)
        if getattr(volume_template, "volumeset", '') != '':
            CreateVolumeTemplates.choose_volume_set(volume_template.volumeset)
        if getattr(volume_template, "folder", '') != '':
            CreateVolumeTemplates.choose_folder(volume_template.folder)
        if n == (len(new_volumetemplates_obj) - 1):
            CreateVolumeTemplates.click_create_button()
            if CommonOperationVolumeTemplates.verify_locate_error_exists():
                selenium2lib = ui_lib.get_s2l()
                selenium2lib.reload_page()
        else:
            CreateVolumeTemplates.click_create_plus_button()
            # CreateVolumeTemplates.wait_creating_message_shown()
            # CreateVolumeTemplates.wait_creating_message_disappear(timeout=15)
        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
        if status is True:
            ui_lib.fail_test(msg)
        FusionUIBase.wait_activity_action_ok(name, message="Create", timeout=40)
    CreateVolumeTemplates.wait_create_volume_template_dialog_disappear(timeout=20)
    FusionUIBase.show_activity_sidebar()

    if 'testtype' not in new_volumetemplates_obj:             # unhappy path test does not verify template exists
        logger.info("{0} VERIFICATION {0}".format('-' * 17))
        for n, volume_template in enumerate(new_volumetemplates_obj):
            name = volume_template.name
            CommonOperationVolumeTemplates.wait_volume_template_status_ok(name)
            logger.info("Add volume template {0} successfully".format(name))
    if count > 0:
        logger.warn("Failure: Not able to create some of volume templates, please check all warning messages")
        return False

    return True


def edit_storage_volume_templates(*volumetemplates_obj):
    FusionUIBase.navigate_to_section(SectionType.VOLUME_TEMPLATES)
    if isinstance(volumetemplates_obj, test_data.DataObj):
        volumetemplates_obj = [volumetemplates_obj]
    elif isinstance(volumetemplates_obj, tuple):
        volumetemplates_obj = list(volumetemplates_obj)
    count = 0
    for n, volume_template in enumerate(volumetemplates_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(volumetemplates_obj), '-' * 14))
        name = volume_template.name
        logger.info("Editing a volume template with name '{0}'".format(name))
        if not select_storage_template(name):
            count += 1
            continue
        EditVolumeTemplates.select_actions_edit()
        EditVolumeTemplates.wait_edit_dialog_shown()
        if getattr(volume_template, 'newname', '') != '':
            EditVolumeTemplates.input_name(volume_template.newname)
        EditVolumeTemplates.input_description(volume_template.desc)
        if getattr(volume_template, 'snapshotpool', '') != '':
            EditVolumeTemplates.input_select_snapshot_storage_pool(volume_template.snapshotpool, volume_template.storagename)
        # EditVolumeTemplates.select_volume_properties_section()
        EditVolumeTemplates.input_capacity(volume_template.capacity)
        EditVolumeTemplates.select_provisioning(volume_template.provisioning)
        EditVolumeTemplates.choose_sharing(volume_template.sharing)
        if getattr(volume_template, 'data_protection_level', '') != '':
            EditVolumeTemplates.choose_data_protection_level(volume_template.data_protection_level)
        if getattr(volume_template, 'permitAdaptiveOptimization', '') != '':
            if volume_template.permitAdaptiveOptimization.lower().strip() == "yes":
                logger.debug("choose permit adaptive optimization  Yes")
                EditVolumeTemplates.choose_permit_adaptive_optimization(permitAdaptiveOptimization=True)
            elif volume_template.permitAdaptiveOptimization.lower().strip() == "no":
                logger.debug("choose permit adaptive optimization  No")
                EditVolumeTemplates.choose_permit_adaptive_optimization(permitAdaptiveOptimization=False)
            else:
                logger.info("the permit adaptive optimization is not correct ")
                return False
        EditVolumeTemplates.click_ok_button()
        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
        if status is True:
            ui_lib.fail_test(msg)
        EditVolumeTemplates.wait_edit_dialog_disappear(timeout=10)
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(name, message="Update", timeout=10)
        FusionUIBase.show_activity_sidebar()
        CommonOperationVolumeTemplates.wait_volume_template_status_ok(volume_template.newname)
        logger.info("Edit volume template {0} successfully".format(volume_template.newname))
    if count > 0:
        logger.warn("Failure: Not able to edit some of storage volume templates, please check all warning messages")
        return False

    return True


def edit_settings_storage_volume_template(reqdtemplatevolumecreation):
    FusionUIBase.navigate_to_section(SectionType.VOLUME_TEMPLATES)
    volume_template_list = CommonOperationVolumeTemplates.get_volume_template_list()
    if len(volume_template_list) == 0:
        ui_lib.fail_test("no volume template existing, not able to edit setting for volume template !")
    else:
        name = volume_template_list[0]
    logger.info("Editing settings for a volume template with name '{0}'".format(name))
    select_storage_template(name)
    EditVolumeTemplatesSettings.select_actions_edit_settings()
    EditVolumeTemplatesSettings.wait_edit_settings_dialog_shown()
    if reqdtemplatevolumecreation.lower() == 'true':
        EditVolumeTemplatesSettings.tick_require_template_for_volume_creation()
    elif reqdtemplatevolumecreation.lower() == 'false':
        EditVolumeTemplatesSettings.not_tick_require_template_for_volume_creation()
    else:
        ui_lib.fail_test("Invalid value '%s' for 'reqdtemplatevolumecreation', please specify 'True' or 'False'" % reqdtemplatevolumecreation)
    EditVolumeTemplatesSettings.click_ok()
    EditVolumeTemplatesSettings.wait_edit_settings_dialog_disappear()
    FusionUIBase.show_activity_sidebar()
    CommonOperationVolumeTemplates.wait_activity_edit_settings_ok(timeout=10)
    FusionUIBase.show_activity_sidebar()
    CommonOperationVolumeTemplates.wait_volume_template_status_ok(name)
    logger.info("Edit setting for volume template {0} successfully".format(name))
    return True


def delete_storage_volume_template(volume_template, fail_if_false=True):
    select_storage_template(volume_template)
    DeleteVolumeTemplates.select_actions_delete()
    DeleteVolumeTemplates.wait_delete_dialog_shown()
    DeleteVolumeTemplates.click_yes_delete_button()
    DeleteVolumeTemplates.wait_delete_dialog_disappear()
    FusionUIBase.show_activity_sidebar()
    FusionUIBase.wait_activity_action_ok(volume_template, message="Delete", timeout=20)
    FusionUIBase.show_activity_sidebar()
    if CommonOperationVolumeTemplates.wait_volume_template_show_not_found(volume_template, timeout=15, fail_if_false=False):
        logger.info("Volume template status appear as 'not found', remove storage system {0} successfully.".format(volume_template))
        return True
    elif CommonOperationVolumeTemplates.verify_volume_template_not_exist(volume_template, timeout=5, fail_if_false=False):
        logger.info("Remove volume template {0} successfully".format(volume_template))
        return True
    else:
        if fail_if_false is True:
            ui_lib.fail_test("The volume template does not disappear in 20s!")
        else:
            logger.warn("The volume template does not disappear in 20s!")
            return False


def delete_storage_volume_templates(*volumetemplates_obj):
    FusionUIBase.navigate_to_section(SectionType.VOLUME_TEMPLATES)
    if isinstance(volumetemplates_obj, test_data.DataObj):
        volumetemplates_obj = [volumetemplates_obj]
    elif isinstance(volumetemplates_obj, tuple):
        volumetemplates_obj = list(volumetemplates_obj)
    count = 0
    for n, volume_template in enumerate(volumetemplates_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(volumetemplates_obj), '-' * 14))
        name = volume_template.name
        logger.info("Removing a volume template with name %s" % name)
        if not select_storage_template(name):
            count += 1
            continue

        delete_storage_volume_template(name)
    if count > 0:
        logger.warn("Failure: Not able to delete some of storage volume templates, please check all warning messages")
        return False
    return True


def delete_all_storage_templates():
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionStorageTemplatesPage.ID_PAGE_LABEL):
        navigate()

    storagetemp_list = [ui_lib.get_text(el) for el in selenium2lib._element_find(FusionStorageTemplatesPage.ID_ALL_STORAGE_TEMPLATE_LIST, False, False)]
    count = 0
    for storagetempname in storagetemp_list:
        logger._log_to_console_and_log_file("Deleting storagetemplate: {0}".format(storagetempname))
        storagetemp_delete_status = delete_storage_volume_template(storagetempname)

        if storagetemp_delete_status:
            logger._log_to_console_and_log_file("'{0}' storagetemplate is deleted Successfully".format(storagetempname))
            count += 1
        else:
            logger.warn("Failed to delete storagetemplate: {0}".format(storagetempname))

    if count == len(storagetemp_list):
        logger._log_to_console_and_log_file("All storagetemplates deleted successfully from appliance")
        return True
    else:
        logger.warn("Failed to delete '{0}' storagetemplates from appliance".format(len(storagetemp_list) - count))
        return False


def navigate():
    FusionUIBase.navigate_to_section(SectionType.VOLUME_TEMPLATES)
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionStorageTemplatesPage.ID_PAGE_LABEL):
        logger._warn("Failed to navigate to Storage Templates Page")
        return False
    else:
        return True


def verify_volume_template_links(*volumetemplate_links):
    """ Verify volume template links
    Arguments:
        templatename*            --  Name of volume template
        resourcename*            --  Page Name to verify (i.e. Volumes, Storage Systems, Storage Pools, Networks, SANs)
        viewname                 --  Name of tab view on storage systems screen that link is located on

    * Required Argument

    Example:
        tests/strm/GUI/strm_data.xml -> @{TestData.strm.templatelinks}
           <templatelinks>
                <link  templatename="Cluster-1" resourcename="Storage Systems" viewname="Overview"/>
                <link  templatename="Cluster-1" resourcename="Storage Pools" viewname="Overview"/>
                <link  templatename="ThreePAR-1" resourcename="Storage Pools" viewname="Overview"/>
                <link  templatename="ThreePAR-1" resourcename="Storage Ssytems" viewname="Overview"/>
          </templatelinks>

    """
    FusionUIBase.navigate_to_section(SectionType.VOLUME_TEMPLATES)
    if isinstance(volumetemplate_links, test_data.DataObj):
        storagesys_obj = [volumetemplate_links]
    elif isinstance(volumetemplate_links, tuple):
        storagesys_obj = list(volumetemplate_links)
    count = 0

    for n, storage in enumerate(volumetemplate_links):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(volumetemplate_links), '-' * 14))
        if getattr(storage, 'templatename', '') != '':
            storage_template_name = storage.templatename
        else:
            storage_template_name = storage.templatename.lower().split('.')[0]
        if getattr(storage, 'resourcename', '') != '':
            storage_resource_name = storage.resourcename
        else:
            storage_resource_name = ""
        if getattr(storage, 'viewname', '') != '':
            storage_view_name = storage.viewname
        else:
            storage_view_name = "Overview"
        logger.info("Verifying link for {} on volume template '{}' screen".format(storage_resource_name, storage_template_name))
        if not select_storage_template(storage_template_name):
            count += 1
            continue

        FusionUIBase.select_view_by_name(storage_view_name)
        time.sleep(5)
        logger.info("verify storage system link [%s] in %s view. verify count if needed." % (storage_resource_name, storage_view_name))
        if storage_resource_name == "Storage Pools":
            logger.info("Entered resource=%s" % storage_resource_name)
            CommonOperationVolumeTemplates.click_storage_pool_link()
            CommonOperationStoragePools.verify_storagepools_title(storage_resource_name, timeout=10, fail_if_false=True)
            FusionUIBase.navigate_to_section(SectionType.VOLUME_TEMPLATES)
        elif storage_resource_name == "Storage Systems":
            logger.info("Entered resource=%s" % storage_resource_name)
            CommonOperationVolumeTemplates.click_storage_system_link()
            CommonOperationStorageSystems.verify_system_page_title(storage_resource_name, timeout=10, fail_if_false=True)
            FusionUIBase.navigate_to_section(SectionType.VOLUME_TEMPLATES)
        elif storage_resource_name == "Volumes":
            logger.info("Entered resource=%s" % storage_resource_name)
            CommonOperationVolumeTemplates.click_storage_volume_link()
            CommonOperationVolumes.verify_storagevolumes_title(storage_resource_name, timeout=10, fail_if_false=True)
            FusionUIBase.navigate_to_section(SectionType.VOLUME_TEMPLATES)
        else:
            return False

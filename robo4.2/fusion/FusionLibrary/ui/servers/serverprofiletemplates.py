# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
""" Fusion Server Profile UI page. """

import Selenium2Library
from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.business_logic.servers.serverprofiles_elements import GeneralServerProfilesElements
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.servers.serverprofiletemplates_elements import FusionServerProfileTemplatesPage
from FusionLibrary.ui.business_logic.servers.serverprofiletemplates import CommonOperationServerProfileTemplate, \
    C7000CreateServerProfileFromTemplate
from FusionLibrary.ui.servers import serverprofiles, serverhardware
from FusionLibrary.ui.servers.serverprofiles import FusionServerProfilesPage
from FusionLibrary.ui.servers.serverhardware import get_type_of_server_hardware
from FusionLibrary.ui.business_logic.servers.serverprofiletemplates import CreateServerProfileTemplate
from FusionLibrary.ui.business_logic.servers.serverprofiletemplates import EditServerProfileTemplate
from FusionLibrary.ui.business_logic.servers.serverprofiletemplates import CopyServerProfileTemplate
from FusionLibrary.ui.business_logic.servers.serverprofiletemplates import VerifyServerProfileTemplate
from FusionLibrary.ui.business_logic.servers.serverprofiletemplates import DeleteServerProfileTemplate
from FusionLibrary.ui.business_logic.servers.serverprofiletemplates_elements import GeneralServerProfileTemplatesElements
from FusionLibrary.ui.business_logic.servers.serverprofiles import CommonOperationServerProfile
from FusionLibrary.ui.business_logic.base import FusionUIBase
from FusionLibrary.ui.business_logic.base import SectionType
import time
import sys
from datetime import datetime


selenium2lib = Selenium2Library.Selenium2Library()
editProfileTimeout = 60 * 15     # Need minimum 10 minute timeout for Intelligent Provisioning to complete
verifyProfileTimeout = 60


def navigate():
    # Navigate to server profile templates page
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILE_TEMPLATES)

    # Verify
    if not ui_lib.wait_for_element_visible(FusionServerProfileTemplatesPage.ID_LINK_CREATE_PROFILE_TEMPLATE, PerfConstants.FUSION_PAGE_SYNC):
        logger.warn("Unable to open the server profile templates page")
        return False
    return True


def _verify_profile_template_status(profile_template_obj, timeout_sec=30):
    # 1. wait changing icon appear
    if ui_lib.wait_for_element_visible(FusionServerProfileTemplatesPage.ID_ITEM_STATUS_CHANGING % profile_template_obj.name, timeout=10) is False:
        logger.warn("State changing icon not show up")
        return None
    # 2. wait changing icon disappear
    if ui_lib.wait_for_element_notvisible(FusionServerProfileTemplatesPage.ID_ITEM_STATUS_CHANGING % profile_template_obj.name, timeout=timeout_sec) is False:
        logger.warn("State changing icon not disappear")
        return None
    # 3. get profile template status, return status string
    time.sleep(5)
    s2l = ui_lib.get_s2l()
    state = s2l.get_text(FusionServerProfileTemplatesPage.ID_ITEM_NAME % profile_template_obj.name)

    return state


def validate_server_profile_templates_actions_menu():
    logger.info("Verify the actions menu of SPT contains correct options.")
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILE_TEMPLATES, time_for_loading=5)
    profile_templates_list = CommonOperationServerProfileTemplate.get_server_profile_template_list()

    for n, profile_template_name in enumerate(profile_templates_list):
        logger.info("Verifying actions menu of server profile template with name '%s' ..." % profile_template_name)
        CommonOperationServerProfileTemplate.click_server_profile_template(profile_template_name)
        CommonOperationServerProfileTemplate.click_action_button()

        VerifyServerProfileTemplate.verify_create_button_existing(timeout=5, fail_if_false=True)
        VerifyServerProfileTemplate.verify_edit_button_existing(timeout=5, fail_if_false=True)
        VerifyServerProfileTemplate.verify_copy_button_existing(timeout=5, fail_if_false=True)
        VerifyServerProfileTemplate.verify_create_server_profile_button_existing(timeout=5, fail_if_false=True)
        VerifyServerProfileTemplate.verify_delete_button_existing(timeout=5, fail_if_false=True)

        logger.info("Actions Menu of SPT: %s show correctly." % profile_template_name)

    logger.info("Validate the actions menu of SPTs Successfully.")
    return True


def create_server_profile_template(profile_template_obj):
    """ Create Server Profile Template For BL/DL

    Arguments:
      name*             --  Name of server profile template as a string.
      desc              --  description of this server profile template.
      sp_desc           --  description of server profiles which created base on this profile template
      ref_server*       --  server hardware name which used for getting associated server hardware type
      enclgroup*        --  enclosure group of server profile template
      manageFirmware    --  If setting the firmware baseline when creating this profile (not implemented yet).
      spp               --  SPP name (title displayed on Firmware Bundle page) for setting firmware baseline.
      manageBootMode*   --  Only required if the server is a Gen 9 server, means 'Gen9' in server hardware type string.
      bootMode*         --  Only required if the server is a Gen 9 server, means 'Gen9' in server hardware type string.
      pxeBootPolicy*    --  Only required if the server is a Gen 9 server, and boot mode is not Legacy BIOS.
      manageBootOrder   --  Not yet supported for Gen 9 DL server
      primaryBootDevice --  Not yet supported for Gen 9 DL server, but supported for Gen 9 BL server
      bootorder         --  Not yet supported for Gen 9 DL server with Non-Legacy-BIOS, only supported with Legacy BIOS boot mode


    * Required Arguments

    Example:
        data/servers/BLServerProfiles -> @{TestData.servers.BLServerProfiles.Create}
    <profile_templates>
        <Create>
            <template name="wpst14bay1-template" desc="wpst14bay1-template" sp_desc="wpst14bay1" ref_server="wpst14, bay 1" hardwareType="BL460c Gen8" enclgroup="encgrp14">
                <Firmware FirmwareBaseline="managed manually" InstallationMethod="Firmware only" ForceInstallation="true"><None/></Firmware>
                <Connections>
                    <Add>
                        <connection name="1" FunctionType="Ethernet" network="netset1" port="FlexibleLOM 1:1-a" RequestedBandwidth="10" boot="Not bootable" />
                        <connection name="2" FunctionType="Ethernet" network="netset2" port="FlexibleLOM 1:2-a" RequestedBandwidth="4" boot="Not bootable" />
                    </Add>
                    <Edit><None/></Edit>
                    <Delete><None/></Delete>
                </Connections>
                <BootSettings manageBootMode="false" bootMode="" manageBootOrder="true">
                    <bootorder device="CD" />
                    <bootorder device="Floppy" />
                    <bootorder device="USB" />
                    <bootorder device="HardDisk" />
                    <bootorder device="PXE" />
                </BootSettings>
                <Advanced mac="Physical" wwn="Physical" serial="Physical" HideUnusedFlexNICs="Yes"><None/></Advanced>
            </template>
            <template name="wpst14bay2-template" desc="wpst14bay2-template" sp_desc="wpst14bay2" ref_server="wpst14, bay 2" hardwareType="BL465c Gen8" enclgroup="encgrp14">
                <Firmware FirmwareBaseline="managed manually" InstallationMethod="Firmware only" ForceInstallation="true"><None/></Firmware>
                <Connections>
                    <Add>
                        <connection name="1" FunctionType="Ethernet" network="net10" port="FlexibleLOM 1:1-a" RequestedBandwidth="2.5" boot="Not bootable" />
                        <connection name="2" FunctionType="Ethernet" network="net11" port="FlexibleLOM 1:1-b" RequestedBandwidth="2.5" boot="Not bootable" />
                        <connection name="3" FunctionType="Ethernet" network="net12" port="FlexibleLOM 1:1-c" RequestedBandwidth="2.5" boot="Not bootable" />
                        <connection name="4" FunctionType="Ethernet" network="net13" port="FlexibleLOM 1:1-d" RequestedBandwidth="2.5" boot="Not bootable" />
                        <connection name="5" FunctionType="Ethernet" network="net10" port="FlexibleLOM 1:2-a" RequestedBandwidth="2.5" boot="Not bootable" />
                        <connection name="6" FunctionType="Ethernet" network="net11" port="FlexibleLOM 1:2-b" RequestedBandwidth="2.5" boot="Not bootable" />
                        <connection name="7" FunctionType="Ethernet" network="net12" port="FlexibleLOM 1:2-c" RequestedBandwidth="2.5" boot="Not bootable" />
                        <connection name="8" FunctionType="Ethernet" network="net13" port="FlexibleLOM 1:2-d" RequestedBandwidth="2.5" boot="Not bootable" />
                    </Add>
                    <Edit><None/></Edit>>
                    <Delete><None/></Delete>
                </Connections>
                <BootSettings manageBootMode="false" bootMode="" manageBootOrder="true">
                    <bootorder device="HardDisk" />
                    <bootorder device="USB" />
                    <bootorder device="CD" />
                    <bootorder device="PXE" />
                    <bootorder device="Floppy" />
                </BootSettings>
                <Advanced mac="Virtual" wwn="Virtual" serial="Virtual" HideUnusedFlexNICs="No"><None/></Advanced>
            </template>
        </Create>
    </profile_templates>

    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILE_TEMPLATES, time_for_loading=5)

    total = len(profile_template_obj)
    created = 0
    already_exists = 0

    for n, profile_template in enumerate(profile_template_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("creating a server profile template with name '%s' ..." % profile_template.name)
        # checking if the profile template is already existing
        if not VerifyServerProfileTemplate.verify_server_profile_template_not_exist(profile_template.name, fail_if_false=False):
            logger.warn("server profile '%s' already exists" % profile_template.name)
            already_exists += 1
            continue

        logger.info("getting server hardware type of server hardware '%s'" % profile_template.ref_server)
        from FusionLibrary.ui.servers.serverhardware import get_type_of_server_hardware
        sht_selected = get_type_of_server_hardware(profile_template.ref_server)
        FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILE_TEMPLATES, time_for_loading=5)

        # open Create SP template dialog and enter data ...
        CreateServerProfileTemplate.click_create_server_profile_template_button()
        CreateServerProfileTemplate.wait_create_server_profile_template_dialog_shown()

        CreateServerProfileTemplate.input_name(profile_template.name)
        CreateServerProfileTemplate.input_description(getattr(profile_template, 'desc', ''))
        CreateServerProfileTemplate.input_server_profile_description(getattr(profile_template, 'sp_desc', ''))
        # Input 'Server hardware'
        # - input server name,
        # - select option from the popped out drop-down list,
        # - power off the server if the it is powered on,
        # - verify the server hardware type of the selected one is refreshed to the type name displayed in the drop-down list
        #     for selecting server hardware
        # input 'Server hardware type', 'Enclosure group'
        # TODO: update Edit Server Profile as well
        # input 'Enclosure group'
        CreateServerProfileTemplate.input_select_server_hardware_type(sht_selected)
        CreateServerProfileTemplate.input_select_enclosure_group(profile_template.enclgroup) if getattr(profile_template, 'enclgroup', None) is not None else None

        if getattr(profile_template, 'Firmware', None) is not None:
            logger.info("test data for 'Firmware' is found: <%s>, start setting Firmware Baseline ..." % profile_template.Firmware)
            logger.debug("test data for 'Firmware' is found: <%s>" % profile_template.Firmware, also_console=False)
            # set Firmware Baseline and force-installation option
            CommonOperationServerProfileTemplate.Firmware.set(profile_template.Firmware)

        if getattr(profile_template, 'Connections', None) is not None:
            logger.debug("test data for 'Connections' is found: <%s>" % profile_template.Connections, also_console=False)
            logger.info("test data for 'Connections' is found, start adding connections ...")
            # add connections
            CommonOperationServerProfileTemplate.Connection.set(profile_template.Connections)

        if getattr(profile_template, 'LocalStorage', None) is not None:
            logger.debug("test data for 'Local Storage' is found: <%s>" % profile_template.LocalStorage, also_console=False)
            logger.info("test data for 'Local Storage' is found, start setting local storage options ... ")
            CommonOperationServerProfileTemplate.LocalStorage.set(profile_template.LocalStorage)

        if getattr(profile_template, 'SANStorage', None) is not None:
            logger.debug("test data for 'SAN Storage' is found:<%s>" % profile_template.SANStorage, also_console=False)
            logger.info("test data for 'SAN Storage' is found, start setting SAN storage options and adding volumes ...")
            # select "Manage SAN Storage" checkbox
            CommonOperationServerProfileTemplate.SANStorage.set(profile_template.SANStorage)

        if getattr(profile_template, 'BootSettings', None) is not None:
            logger.debug("test data for 'Boot Settings' is found: <%s>" % profile_template.BootSettings, also_console=False)
            logger.info("test data for 'Boot Settings' is found, start setting its options ...")
            CommonOperationServerProfileTemplate.BootSettings.set(profile_template, server_hardware_type=sht_selected)

        # 'BIOSSettings' part is ignored since BIOS setting is complicated to verify the result, therefor
        #  might be better to use a dedicated tool to do this part automation separately

        if getattr(profile_template, 'Advanced', None) is not None:
            logger.debug("test data for 'Advanced' is found: <%s>" % profile_template.Advanced, also_console=False)
            logger.info("test data for 'Advanced' is found, start setting its options ...")
            # select "MAC/WWN/Serial/Hide unused FlexNICs" radio box
            CreateServerProfileTemplate.Advanced.set(profile_template)

        CreateServerProfileTemplate.click_create_button()
        if CommonOperationServerProfileTemplate.BootSettings.get_error_message_from_boot_mode() is not None:
            logger.warn("test data of server profile '%s' may be wrongly defined for 'Boot mode', which caused an error that blocks profile being created. "
                        "test will skip this profile and continue to create other server profiles" % profile_template.name)
            continue

        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
        if status is True:
            logger.warn("unexpected error occurred: %s" % msg)
            ui_lib.fail_test(msg)

        CreateServerProfileTemplate.wait_create_server_profile_template_dialog_disappear(timeout=180)
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(profile_template.name, 'Create', timeout=720, fail_if_false=True)
        FusionUIBase.show_activity_sidebar()
        CommonOperationServerProfileTemplate.wait_server_profile_template_status_ok(profile_template.name, timeout=180, fail_if_false=True)
        logger.info("created server profile '%s' successfully" % profile_template.name)
        created += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - already_exists == 0:
        logger.warn("no server profile to create! all %s server profile(s) is already existing, test is considered PASS" % already_exists)
        return True
    else:
        if created < total:
            logger.warn("not all of the server profile(s) is successfully created - %s out of %s created " % (created, total))
            if created + already_exists == total:
                logger.warn("%s already existing server profile(s) is skipped, test is considered PASS" % already_exists)
                return True
            else:
                logger.warn("%s already existing server profile(s) is skipped, %s profile(s) left is failed being created " % (already_exists, total - created - already_exists))
                return False

    logger.info("all of the server profile(s) is successfully created - %s out of %s " % (created, total))
    return True


def edit_server_profile_template(profile_template_obj):
    """ Edit Server Profile Template For BL/DL

    Arguments:
      name*             --  Name of server profile template as a string.
      newName           --  New name of server profile template as a string.
      desc              --  description of the iLO of this server profile.
      new_sht_ref_server--  reference server hardware of the server hardware type for which this profile template is about to be created.
      enclgroup         --  enclosure group name of the server hardware type for which this profile template is about to be created.
      hardwaretype*     --  server hardware type of the server, will be used to verify the selected server's SHT is correct.
                            This should be the 'DL380p Gen8' instead of 'DL380p Gen8 1/2' to avoid the mismatching due to Fusion's SHT identifying mechanism.
      manageFirmware    --  If setting the firmware baseline when creating this profile (not implemented yet).
      spp               --  SPP name (title displayed on Firmware Bundle page) for setting firmware baseline.
      manageBootMode*   --  Only required if the server is a Gen 9 server, means 'Gen9' in server hardware type string.
      bootMode*         --  Only required if the server is a Gen 9 server, means 'Gen9' in server hardware type string.
      pxeBootPolicy*    --  Only required if the server is a Gen 9 server, and boot mode is not Legacy BIOS.
      manageBootOrder   --  Not yet supported for Gen 9 DL server
      primaryBootDevice --  Not yet supported for Gen 9 DL server, but supported for Gen 9 BL server
      bootorder         --  Not yet supported for Gen 9 DL server with Non-Legacy-BIOS, only supported with Legacy BIOS boot mode


    * Required Arguments

    Example:
        data/servers/BLServerProfileTemplates -> @{TestData.servers.BLServerProfileTemplates.Edit}
        <servers>
            <BLServerProfileTemplates>
                <Edit>
                    <profile_template name="SP_wpst23bay3_BL465c_Gen8" desc="SP BL465c Gen8" new_sht_ref_server="wpst23, bay 3" hardwareType="BL465c Gen8 1" enclgroup="GRP-wpst23">
                        <Firmware FirmwareBaseline="managed manually" xxx="" />
                        <Connections>
                            <Add>
                                <connection name="CON_FA1" xxx="" />
                                <connection name="CON_FA2" xxx="" />
                                <connection name="CON_ETH" xxx="" />
                            </Add>
                            <Edit>
                                <connection name="CON_FA1" xxx="" />
                                <connection name="CON_FA2" xxx="" />
                            </Edit>
                            <Delete>
                                <connection name="CON_ETH"/>
                            </Delete>
                        </Connections>
                        <LocalStorage xxx="">
                            <LogicalDrive name="d1" xxx=" />
                            <LogicalDrive name="d2" xxx=" />
                        </LocalStorage>
                        <SANStorage>
                            <Volumes>
                                <Add>
                                    <volume name="VOL_1" xxx="" />
                                    <volume name="VOL_1" xxx="">
                                        <StoragePaths>
                                            <Add>
                                                <StoragePath network="" />
                                                <StoragePath network="">
                                                    <Port TargetPort="" PortName="" selected="true">
                                                    <Port TargetPort="" PortName="" selected="false">
                                                </StoragePath>
                                            </Add>
                                            <Edit>
                                                <StoragePath network="" />
                                                <StoragePath network="">
                                                    <Port TargetPort="" PortName="" selected="true">
                                                    <Port TargetPort="" PortName="" selected="false">
                                                </StoragePath>
                                            </Edit>
                                            <Delete><StoragePath network="FA1"></Delete>
                                        </StoragePaths>
                                    </volume>
                                </Add>
                                <Edit><volumes to edit, or None node as '<None/>'/></Edit>
                                <Delete><volumes to delete, or None node as '<None/>'></Delete>
                            </Volumes>
                        </SANStorage>
                        <BootSettings manageBootMode="false" bootMode="Legacy BIOS" manageBootOrder="true">
                            <bootorder device="PXE" />
                            <bootorder device="CD" />
                            <bootorder device="Floppy" />
                            <bootorder device="USB" />
                            <bootorder device="HardDisk" />
                        </BootSettings>
                        <Advanced mac="Physical" wwn="Physical" serial="Physical" HideUnusedFlexNICs="Yes"><None/></Advanced>
                    </profile_template>
                </Edit>
            </BLServerProfileTemplates>
        </servers>

    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILE_TEMPLATES, time_for_loading=5)

    total = len(profile_template_obj)
    not_exists = 0
    edited = 0

    for n, profile_template in enumerate(profile_template_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("editing a server profile template with name '%s' ..." % profile_template.name)
        # checking if the profile is not existing for editing
        if not VerifyServerProfileTemplate.verify_server_profile_template_exist(profile_template.name, fail_if_false=False):
            logger.warn("server profile template '%s' does not exist" % profile_template.name)
            not_exists += 1
            continue

        # get new server hardware type for edit
        enclosure_group = profile_template.enclgroup if getattr(profile_template, 'enclgroup', None) is not None else None
        sht_new = None
        if getattr(profile_template, 'new_sht_ref_server', None) is not None:
            logger.info("getting server hardware type of server hardware '%s'" % profile_template.new_sht_ref_server)
            from FusionLibrary.ui.servers.serverhardware import get_type_of_server_hardware
            sht_new = get_type_of_server_hardware(profile_template.new_sht_ref_server)
            FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILE_TEMPLATES, time_for_loading=5)
        elif getattr(profile_template, 'hardwareType', None) is not None:
            sht_new = profile_template.hardwareType

        # open Edit SPT dialog and enter data ...
        CommonOperationServerProfileTemplate.click_server_profile_template(profile_template.name)

        EditServerProfileTemplate.select_action_edit()
        EditServerProfileTemplate.wait_edit_server_profile_template_dialog_shown()
        BuiltIn().sleep(2)
        EditServerProfileTemplate.input_name(profile_template.newName) if getattr(profile_template, 'newName', None) is not None else None
        EditServerProfileTemplate.input_description(profile_template.desc) if getattr(profile_template, 'desc', None) is not None else None

        sht_selected = EditServerProfileTemplate.get_selected_server_hardware_type()
        if sht_new is not None and sht_new not in sht_selected:
            logger.info("server hardware type '%s' is NOT consistent with current value '%s'" % (sht_new, sht_selected))
            EditServerProfileTemplate.ChangeServerHardwareTypeAndEnclosureGroup.change_server_hardware_type(sht_new, enclosure_group, timeout=5, fail_if_false=False)

        eg_selected = EditServerProfileTemplate.get_selected_enclosure_group()
        if enclosure_group is not None and enclosure_group not in eg_selected:
            logger.warn("enclosure group '%s' is NOT consistent with test data '%s'" % (eg_selected, enclosure_group))
            EditServerProfileTemplate.ChangeServerHardwareTypeAndEnclosureGroup.change_enclosure_group(enclosure_group, timeout=5, fail_if_false=False)

        if getattr(profile_template, 'Affinity', None) is not None:
            logger.info("test data for 'Affinity' is found: <%s>, start setting Affinity ..." % profile_template.Affinity)
            EditServerProfileTemplate.select_affinity_by_text(profile_template.Affinity)

        if getattr(profile_template, 'Firmware', None) is not None:
            logger.info("test data for 'Firmware' is found: <%s>, start setting Firmware Baseline ..." % profile_template.Firmware)
            logger.debug("test data for 'Firmware' is found: <%s>" % profile_template.Firmware, also_console=False)
            # set Firmware Baseline and force-installation option
            CommonOperationServerProfileTemplate.Firmware.set(profile_template.Firmware)

        if getattr(profile_template, 'Connections', None) is not None:
            logger.debug("test data for 'Connections' is found: <%s>" % profile_template.Connections, also_console=False)
            logger.info("test data for 'Connections' is found, start adding connections ...")
            # add connections
            CommonOperationServerProfileTemplate.Connection().set(profile_template.Connections)

        if getattr(profile_template, 'LocalStorage', None) is not None:
            logger.debug("test data for 'Local Storage' is found: <%s>" % profile_template.LocalStorage, also_console=False)
            logger.info("test data for 'Local Storage' is found, start setting local storage options ... ")
            CommonOperationServerProfileTemplate.LocalStorage.set(profile_template.LocalStorage)

        if getattr(profile_template, 'SANStorage', None) is not None:
            BuiltIn().sleep(3)
            logger.debug("test data for 'SAN Storage' is found:<%s>" % profile_template.SANStorage, also_console=False)
            logger.info("test data for 'SAN Storage' is found, start setting SAN storage options and adding volumes ...")
            # select "Manage SAN Storage" checkbox
            CommonOperationServerProfileTemplate.SANStorage.set(profile_template.SANStorage)

        sht_selected = EditServerProfileTemplate.get_selected_server_hardware_type()
        if getattr(profile_template, 'BootSettings', None) is not None:
            logger.debug("test data for 'Boot Settings' is found: <%s>" % profile_template.BootSettings, also_console=False)
            logger.info("test data for 'Boot Settings' is found, start setting its options ...")
            CommonOperationServerProfileTemplate.BootSettings.set(profile_template, server_hardware_type=sht_selected)

        # 'BIOSSettings' part is ignored since BIOS setting is complicated to verify the result, therefor
        #  might be better to use a dedicated tool to do this part automation separately

        if getattr(profile_template, 'Advanced', None) is not None:
            BuiltIn().sleep(3)
            logger.debug("test data for 'Advanced' is found: <%s>" % profile_template.Advanced, also_console=False)
            logger.info("test data for 'Advanced' is found, start setting its options ...")
            # select "MAC/WWN/Serial/Hide unused FlexNICs" radio box
            EditServerProfileTemplate.Advanced.set(profile_template)

        EditServerProfileTemplate.click_ok_button()
        # logger.debug("sleeping for 8 seconds ...")
        # BuiltIn().sleep(8)
        # if EditServerProfileTemplate.get_error_message_from_boot_mode() is not None:
        if CommonOperationServerProfileTemplate.BootSettings.get_error_message_from_boot_mode() is not None:
            logger.warn("test data may be wrongly defined for 'Boot mode', which caused an error that blocks profile being created. "
                        "test will skip this profile '%s' and continue to create other server profiles" % profile_template.name)
            continue

        BuiltIn().sleep(2)
        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
        if status is True:
            logger.warn("unexpected error occurred: %s" % msg)
            ui_lib.fail_test(msg)

        EditServerProfileTemplate.wait_edit_server_profile_template_dialog_disappear(timeout=300)
        FusionUIBase.show_activity_sidebar()
        profile_name = profile_template.newName if getattr(profile_template, 'newName', None) is not None else profile_template.name
        FusionUIBase.wait_activity_action_ok(profile_name, 'Update', timeout=300, fail_if_false=True)
        FusionUIBase.show_activity_sidebar()
        CommonOperationServerProfileTemplate.wait_server_profile_template_status_ok(profile_name, timeout=300, fail_if_false=True)
        logger.info("edited server profile '%s' successfully" % profile_name)
        edited += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no server profile template to edit! all %s server profile template(s) is NOT existing, test is considered FAILED" % not_exists)
        return False
    else:
        if edited < total:
            logger.warn("not all of the server profile template(s) is successfully edited - %s out of %s edited " % (edited, total))
            if edited + not_exists == total:
                logger.warn("%s not-existing server profile template(s) is skipped being edited, test is considered FAILED" % not_exists)
                return False
            else:
                logger.warn("%s not-existing server profile template(s) is skipped being edited, %s profile template(s) left is failed being edited " % (not_exists, total - edited - not_exists))
                return False

    logger.info("all of the server profile template(s) is successfully edited - %s out of %s " % (edited, total))
    return True


def copy_server_profile_template(profile_template_obj):
    """ Copy Server Profile For BL/DL

    Arguments:
      name*             --  Name of server hardware as a string.
      desc              --  description of the iLO of this server profile.
      server*           --  server hardware name of the server for which this profile is about to be created.
      hardwaretype*     --  server hardware type of the server, will be used to verify the selected server's SHT is correct.
                            This should be the 'DL380p Gen8' instead of 'DL380p Gen8 1/2' to avoid the mismatching due to Fusion's SHT identifying mechanism.
      manageFirmware    --  If setting the firmware baseline when creating this profile (not implemented yet).
      spp               --  SPP name (title displayed on Firmware Bundle page) for setting firmware baseline.
      manageBootMode*   --  Only required if the server is a Gen 9 server, means 'Gen9' in server hardware type string.
      bootMode*         --  Only required if the server is a Gen 9 server, means 'Gen9' in server hardware type string.
      pxeBootPolicy*    --  Only required if the server is a Gen 9 server, and boot mode is not Legacy BIOS.
      manageBootOrder   --  Not yet supported for Gen 9 DL server
      primaryBootDevice --  Not yet supported for Gen 9 DL server, but supported for Gen 9 BL server
      bootorder         --  Not yet supported for Gen 9 DL server with Non-Legacy-BIOS, only supported with Legacy BIOS boot mode


    * Required Arguments

    Example:
        data/servers/BLServerProfiles -> @{TestData.servers.BLServerProfiles.Create}
        <servers>
            <BLServerProfiles>
                <Create>
                    <profile name="SP_wpst23bay3_BL465c_Gen8" desc="SP BL465c Gen8" server="wpst23, bay 3" hardwareType="BL465c Gen8" enclgroup="GRP-wpst32">
                        <Firmware FirmwareBaseline="managed manually" xxx="" />
                        <Connections>
                            <Add>
                                <connection name="CON_FA1" xxx="" />
                                <connection name="CON_FA2" xxx="" />
                                <connection name="CON_ETH" xxx="" />
                            </Add>
                            <Edit>
                                <connection name="CON_FA1" xxx="" />
                                <connection name="CON_FA2" xxx="" />
                            </Edit>
                            <Delete>
                                <connection name="CON_ETH"/>
                            </Delete>
                        </Connections>
                        <LocalStorage xxx="">
                            <LogicalDrive name="d1" xxx=" />
                            <LogicalDrive name="d2" xxx=" />
                        </LocalStorage>
                        <SANStorage>
                            <Volumes>
                                <Add>
                                    <volume name="VOL_1" xxx="" />
                                    <volume name="VOL_1" xxx="">
                                        <StoragePaths>
                                            <Add>
                                                <StoragePath network="" />
                                                <StoragePath network="">
                                                    <Port TargetPort="" PortName="" selected="true">
                                                    <Port TargetPort="" PortName="" selected="false">
                                                </StoragePath>
                                            </Add>
                                            <Edit>
                                                <StoragePath network="" />
                                                <StoragePath network="">
                                                    <Port TargetPort="" PortName="" selected="true">
                                                    <Port TargetPort="" PortName="" selected="false">
                                                </StoragePath>
                                            </Edit>
                                            <Delete><StoragePath network="FA1"></Delete>
                                        </StoragePaths>
                                    </volume>
                                </Add>
                                <Edit><volumes to edit, or None node as '<None/>'/></Edit>
                                <Delete><volumes to delete, or None node as '<None/>'></Delete>
                            </Volumes>
                        </SANStorage>
                        <BootSettings manageBootMode="false" bootMode="Legacy BIOS" manageBootOrder="true">
                            <bootorder device="PXE" />
                            <bootorder device="CD" />
                            <bootorder device="Floppy" />
                            <bootorder device="USB" />
                            <bootorder device="HardDisk" />
                        </BootSettings>
                        <Advanced mac="Physical" wwn="Physical" serial="Physical" HideUnusedFlexNICs="Yes"><None/></Advanced>
                    </profile>
                </Create>
                <Edit><profiles to edit, or None node as '<None/>'/></Edit>
                <Delete><profiles to delete, or None node as '<None/>'/></Delete>
            </BLServerProfiles>
        </servers>

    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILE_TEMPLATES, time_for_loading=8)

    total = len(profile_template_obj)
    source_not_exists = 0
    target_already_exists = 0
    copied = 0

    for n, profile_template in enumerate(profile_template_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("copying a server profile template with name '%s' ..." % profile_template.source)
        # checking if the profile is not existing for editing
        if VerifyServerProfileTemplate.verify_server_profile_template_exist(profile_template.source, fail_if_false=False) is False:
            logger.warn("source server profile template '%s' does not exist" % profile_template.source)
            source_not_exists += 1
            continue

        # checking if the profile is not existing for editing
        if VerifyServerProfileTemplate.verify_server_profile_template_not_exist(profile_template.name, fail_if_false=False) is False:
            logger.warn("target server profile template '%s' already exists!" % profile_template.name)
            target_already_exists += 1
            continue

        # open Copy SP dialog and enter data ...
        CommonOperationServerProfileTemplate.click_server_profile_template(profile_template.source)

        CopyServerProfileTemplate.select_action_copy()
        CopyServerProfileTemplate.wait_copy_server_profile_template_dialog_shown()
        BuiltIn().sleep(2)
        CopyServerProfileTemplate.input_name(profile_template.name)
        CopyServerProfileTemplate.input_description(profile_template.desc) if getattr(profile_template, 'desc', None) is not None else None

        sht_selected = CopyServerProfileTemplate.get_selected_server_hardware_type(profile_template.name)
        # if profile_template.hardwareType not in sht_selected:
        #     logger.warn("server hardware type '%s' of server profile template '%s' is NOT consistent with test data '%s'" % (sht_selected, profile_template.name, profile_template.hardwareType))

        if getattr(profile_template, 'Affinity', None) is not None:
            logger.info("test data for 'Affinity' is found: <%s>, start setting Affinity ..." % profile_template.Affinity)
            CopyServerProfileTemplate.select_affinity_by_text(profile_template.Affinity)

        if getattr(profile_template, 'Firmware', None) is not None:
            logger.info("test data for 'Firmware' is found: <%s>, start setting Firmware Baseline ..." % profile_template.Firmware)
            logger.debug("test data for 'Firmware' is found: <%s>" % profile_template.Firmware, also_console=False)
            # set Firmware Baseline and force-installation option
            CommonOperationServerProfileTemplate.Firmware.set(profile_template.Firmware)

        if getattr(profile_template, 'Connections', None) is not None:
            logger.debug("test data for 'Connections' is found: <%s>" % profile_template.Connections, also_console=False)
            logger.info("test data for 'Connections' is found, start adding connections ...")
            # add connections
            CommonOperationServerProfileTemplate.Connection.set(profile_template.Connections)

        if getattr(profile_template, 'LocalStorage', None) is not None:
            logger.debug("test data for 'Local Storage' is found: <%s>" % profile_template.LocalStorage, also_console=False)
            logger.info("test data for 'Local Storage' is found, start setting local storage options ... ")
            CommonOperationServerProfileTemplate.LocalStorage.set(profile_template.LocalStorage)

        if getattr(profile_template, 'SANStorage', None) is not None:
            BuiltIn().sleep(3)
            logger.debug("test data for 'SAN Storage' is found:<%s>" % profile_template.SANStorage, also_console=False)
            logger.info("test data for 'SAN Storage' is found, start setting SAN storage options and adding volumes ...")
            # select "Manage SAN Storage" checkbox
            CommonOperationServerProfileTemplate.SANStorage.set(profile_template.SANStorage)

        if getattr(profile_template, 'BootSettings', None) is not None:
            logger.debug("test data for 'Boot Settings' is found: <%s>" % profile_template.BootSettings, also_console=False)
            logger.info("test data for 'Boot Settings' is found, start setting its options ...")
            CommonOperationServerProfileTemplate.BootSettings.set(profile_template, server_hardware_type=sht_selected)

        # 'BIOSSettings' part is ignored since BIOS setting is complicated to verify the result, therefor
        #  might be better to use a dedicated tool to do this part automation separately

        if getattr(profile_template, 'Advanced', None) is not None:
            BuiltIn().sleep(3)
            logger.debug("test data for 'Advanced' is found: <%s>" % profile_template.Advanced, also_console=False)
            logger.info("test data for 'Advanced' is found, start setting its options ...")
            # select "MAC/WWN/Serial/Hide unused FlexNICs" radio box
            CopyServerProfileTemplate.Advanced.set(profile_template)

        CopyServerProfileTemplate.click_create_button()
        # logger.debug("sleeping for 8 seconds ...")
        # BuiltIn().sleep(8)
        # if EditServerProfileTemplate.get_error_message_from_boot_mode() is not None:
        if CommonOperationServerProfileTemplate.BootSettings.get_error_message_from_boot_mode() is not None:
            logger.warn("test data may be wrongly defined for 'Boot mode', which caused an error that blocks profile being created. "
                        "test will skip this profile '%s' and continue to create other server profiles" % profile_template.name)
            continue

        BuiltIn().sleep(2)
        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
        if status is True:
            logger.warn("unexpected error occurred: %s" % msg)
            ui_lib.fail_test(msg)

        CopyServerProfileTemplate.wait_copy_server_profile_template_dialog_disappear(timeout=300)
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(profile_template.name, 'Create', timeout=300, fail_if_false=True)
        FusionUIBase.show_activity_sidebar()
        CommonOperationServerProfileTemplate.wait_server_profile_template_status_ok(profile_template.name, timeout=300, fail_if_false=True)
        logger.info("successfully copied server profile '%s' to '%s'" % (profile_template.source, profile_template.name))
        copied += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - source_not_exists - target_already_exists == 0:
        logger.warn("no server profile template to copy! all %s server profile template(s) is either source-NOT-existing or target-ALREADY-existing, test is considered FAILED" % (source_not_exists + target_already_exists))
        return False
    else:
        if copied < total:
            logger.warn("not all of the server profile template(s) is successfully copied - %s out of %s copied " % (copied, total))
            if copied + source_not_exists + target_already_exists == total:
                logger.warn("%s source-not-existing template(s) and %s target-already-existing template(s) is skipped being copied, test is considered FAILED" % (source_not_exists, target_already_exists))
                return False
            else:
                logger.warn("%s source-not-existing template(s) and %s target-already-existing template(s) is skipped being copied, %s template(s) left is failed being copied " % (source_not_exists, target_already_exists, total - copied - source_not_exists - target_already_exists))
                return False

    logger.info("all of the server profile template(s) is successfully copied - %s out of %s " % (copied, total))
    return True


def _add_profile_connections(connection, selenium2lib):
    """ Add Profile Connections    """
    logger._log_to_console_and_log_file("Selecting network type...")
    selenium2lib = ui_lib.get_s2l()
    ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_COMBO_NETWORK_ADD_CONNECTION)
    ui_lib.wait_for_element_and_input_text(FusionServerProfileTemplatesPage.ID_INPUT_NETWORK_ADD_CONNECTION, connection.network)
    selenium2lib.press_key(FusionServerProfileTemplatesPage.ID_INPUT_NETWORK_ADD_CONNECTION, '\\13')
    logger._log_to_console_and_log_file("Selecting requested band width...")
    ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_INPUT_REQUESTED_BW_ADD_CONNECTION)
    boot_list = "-1"
    if connection.has_property('band'):
        if(connection.type.upper() == "FIBRE CHANNEL" or connection.type.upper() == "FIBRECHANNEL"):
            if float(connection.band) <= 0 or float(connection.band) > 8:
                logger._warn(" : Failed to add FC Connection to server profile. \
                Required Bandwidth for FC should be in the range 0.1 Gb/s and 10 Gb/s")
                selenium2lib.capture_page_screenshot()
                return False
        else:
            if float(connection.band) <= 0 or float(connection.band) > 10:
                logger._warn(" : Failed to add Ethernet Connection to server profile. \
                Required Bandwidth for Ethernet should be in the range 0.1 Gb/s and 8 Gb/s")
                selenium2lib.capture_page_screenshot()
                return False
        if selenium2lib._is_visible(FusionServerProfileTemplatesPage.XP_CREATE_SP_ADD_CONN_BW_DROPDOWN):
            selenium2lib.press_key(FusionServerProfileTemplatesPage.XP_CREATE_SP_ADD_CONN_BW_DROPDOWN, connection.band)
            selenium2lib.mouse_down(FusionServerProfileTemplatesPage.XP_CREATE_SP_ADD_CONN_BW_DD_SELECT % connection.band)
            selenium2lib.mouse_up(FusionServerProfileTemplatesPage.XP_CREATE_SP_ADD_CONN_BW_DD_SELECT % connection.band)
            boot_list = "-2"
        else:
            ui_lib.wait_for_element_and_input_text(FusionServerProfileTemplatesPage.ID_INPUT_REQUESTED_BW_ADD_CONNECTION, connection.band)

    logger._log_to_console_and_log_file("Selecting FlexNIC...")
    browser = BuiltIn().get_variable_value("${Browser}")

    if browser.lower() == "chrome":
        logger._log_to_console_and_log_file("Chrome not handling FlexNIC or boot order skipping....")
    else:
        ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_COMBO_FLEXNIC_ADD_CONNECTION, fail_if_false=True)
#       2015-03-31 Alex Ma commented below to fix UI change
#        selenium2lib.press_key(FusionServerProfileTemplatesPage.ID_SELECT_PORT_DROP_DOWN, connection.portName)
        ui_lib.wait_for_element_and_input_text(FusionServerProfileTemplatesPage.ID_SELECT_PORT_DROP_DOWN, connection.portName)
        ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.XP_CREATE_SP_ADD_CONN_NIC_DD_SELECT % connection.portName)
        logger._log_to_console_and_log_file("Selecting boot...")
        selenium2lib.press_key(FusionServerProfileTemplatesPage.ID_COMBO_BOOT_ADD_CONNECTION, connection.boot)
#       2015-03-31 Alex Ma commented below to fix UI change
#        selenium2lib.mouse_down(FusionServerProfileTemplatesPage.XP_CREATE_SP_ADD_CONN_BOOT_DD_SELECT % (boot_list, connection.boot))
        selenium2lib.mouse_down(FusionServerProfileTemplatesPage.XP_CREATE_SP_ADD_CONN_BOOT_DD_SELECT % connection.boot)
#       2015-03-31 Alex Ma commented below to fix UI change
#        ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.XP_CREATE_SP_ADD_CONN_BOOT_DD_SELECT % (boot_list, connection.boot))
        selenium2lib.mouse_up(FusionServerProfileTemplatesPage.XP_CREATE_SP_ADD_CONN_BOOT_DD_SELECT % connection.boot)
        BuiltIn().sleep(2)

    return True


def _select_advanced_options(profile, selenium2lib):
    """ Select Advanced Options    """
    ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_COMBO_MENU_VIEW)
    ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_LINK_ADVANCED)
    logger._log_to_console_and_log_file("Setting advanced setup")
    if profile.has_property("mac") and profile.mac != "":
        if(profile.mac == "Physical"):
            ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_RADIO_PHYSICAL_MAC)
        else:
            ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_RADIO_VIRTUAL_MAC)
    if profile.has_property("wwn") and profile.wwn != "":
        if(profile.wwn == "Physical"):
            ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_RADIO_PHYSICAL_WWN)
        else:
            ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_RADIO_VIRTUAL_WWN)
    if profile.has_property("serial") and profile.serial != "":
        if(profile.serial == "Physical"):
            ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_RADIO_PHYSICAL_SERIAL)
        elif(profile.serial == "Virtual"):
            ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_RADIO_VIRTUAL_SERIAL)
        elif(profile.serial == "Userspecified"):
            ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_RADIO_USER_SPECIFIED_SERIAL)
            if profile.has_property("serialnumber") and profile.serialnumber == "":
                logger._warn("Mandatory fields for user specified serial number can't be empty")
                return False
            if profile.has_property("UUID") and profile.UUID == "":
                logger._warn("Mandatory fields for user specified UUID can't be empty")
                return False
            ui_lib.wait_for_element_visible(FusionServerProfileTemplatesPage.ID_INPUT_SERIAL_NUMBER)
            ui_lib.wait_for_element_and_input_text(FusionServerProfileTemplatesPage.ID_INPUT_SERIAL_NUMBER, profile.serialnumber)
            ui_lib.wait_for_element_visible(FusionServerProfileTemplatesPage.ID_INPUT_UUID_NUMBER)
            ui_lib.wait_for_element_and_input_text(FusionServerProfileTemplatesPage.ID_INPUT_UUID_NUMBER, profile.UUID)
    return True


def delete_server_profile_template_by_name(profile_template_name):
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILE_TEMPLATES, time_for_loading=5)
    #   check if server profile template exists
    if not VerifyServerProfileTemplate.verify_server_profile_template_exist(profile_template_name, fail_if_false=False):
        logger.warn("server profile template '%s' does NOT exist! keyword '%s' returns a 'False'" % (profile_template_name, sys._getframe().f_code.co_name))
        return False
    CommonOperationServerProfileTemplate.click_server_profile_template(profile_template_name=profile_template_name)
    #   start performing remove action
    DeleteServerProfileTemplate.select_action_delete()
    DeleteServerProfileTemplate.click_yes_delete_button()
    DeleteServerProfileTemplate.wait_delete_server_profile_template_dialog_disappear(profile_template_name=profile_template_name)
    #   verify server profile template is not existing after being deleted

    start = datetime.now()
    timeout = 300  # 5 minutes
    while (datetime.now() - start).total_seconds() < timeout:
        if CommonOperationServerProfileTemplate.wait_server_profile_template_show_not_found(profile_template_name, timeout=5, fail_if_false=False):
            logger.info("server profile template status appear as 'not found', remove server profile template '%s' successfully." % profile_template_name)
            break
        elif VerifyServerProfileTemplate.verify_server_profile_template_not_exist(profile_template_name, timeout=5, fail_if_false=False):
            logger.info("server profile template '%s' is successfully deleted." % profile_template_name)
            break
    else:
        logger.warn("server profile template '%s' is NOT successfully deleted or timeout issue occurred." % profile_template_name)
        return False

    FusionUIBase.show_activity_sidebar()
    # FusionUIBase.wait_activity_action_ok(profile_name, 'Delete', timeout=300, fail_if_false=False)
    if FusionUIBase.wait_activity_action_ok(profile_template_name, 'Delete', timeout=30, fail_if_false=False) is False:
        return False
    FusionUIBase.show_activity_sidebar()

    return True


def delete_server_profile_template(profile_template_obj):
    """ Delete Server Profile Template

    Arguments:
      name*             --  Name of server hardware as a string.

    * Required Arguments

    Example:
        data/profile_templates/Delete -> @{TestData.profile_templates.Delete}
        <profile_templates>
            <Delete>
                <template name="wpst14bay1-template"/>
                <template name="wpst14bay2-template"/>
            </Delete>
        </profile_templates>
    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILE_TEMPLATES, time_for_loading=5)

    total = len(profile_template_obj)
    not_exists = 0
    deleted = 0

    for n, profile_template in enumerate(profile_template_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("deleting a server profile template named '%s'" % profile_template.name)
        if not VerifyServerProfileTemplate.verify_server_profile_template_exist(profile_template.name, fail_if_false=False):
            logger.warn("server profile template '%s' does not exist" % profile_template.name)
            not_exists += 1
        else:
            if delete_server_profile_template_by_name(profile_template.name) is False:
                logger.warn("server profile template '%s' is NOT deleted successfully, or 'Delete' action is not found in right-side-bar list." % profile_template.name)
                continue
            else:
                deleted += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no server profile template to delete! all %s server profile template(s) is NOT existing, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if deleted < total:
            logger.warn("not all of the server profile template(s) is successfully deleted - %s out of %s deleted " % (deleted, total))
            if deleted + not_exists == total:
                logger.warn("%s not-existing server profile template(s) is skipped, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s not-existing server profile template(s) is skipped, %s profile template(s) left is failed being deleted " % (not_exists, total - deleted - not_exists))
                return False

    logger.info("all of the server profile template(s) is successfully deleted - %s out of %s " % (deleted, total))
    return True


def delete_all_appliance_server_profile_templates():
    """ Delete All Appliance Server Profile Templates

    Arguments: - no arguments needed

    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILE_TEMPLATES, time_for_loading=5)
    profile_template_name_list = CommonOperationServerProfileTemplate.get_server_profile_template_list()

    total = len(profile_template_name_list)
    not_exists = 0
    deleted = 0

    for n, profile_template_name in enumerate(profile_template_name_list):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("deleting a server profile template named '%s'" % profile_template_name)
        if not VerifyServerProfileTemplate.verify_server_profile_template_exist(profile_template_name, fail_if_false=False):
            logger.warn("server profile template '%s' does not exist" % profile_template_name)
            not_exists += 1
        else:
            if not delete_server_profile_template_by_name(profile_template_name):
                logger.warn("server profile template '%s' is NOT deleted successfully." % profile_template_name)
                continue
            else:
                deleted += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no server profile template to delete! all %s server profile template(s) is NOT existing, test is considered PASS" % not_exists)
        return True
    else:
        if deleted < total:
            logger.warn("not all of the server profile template(s) is successfully deleted - %s out of %s deleted " % (deleted, total))
            if deleted + not_exists == total:
                logger.warn("%s non-existing server profile template(s) is skipped being deleted, test is considered PASS" % not_exists)
                return True
            else:
                logger.warn("%s non-existing server profile template(s) is skipped being deleted, %s profile template(s) left is failed being deleted " % (not_exists, total - deleted - not_exists))
                return False

    logger.info("all of the server profile template(s) is successfully deleted - %s out of %s " % (deleted, total))
    return True


def create_server_profile_from_template(profile_obj):
    """

    """
    from FusionLibrary.ui.business_logic.servers.serverprofiles import VerifyServerProfile, CommonOperationServerProfile

    total = len(profile_obj)
    tpl_not_exists = 0
    sp_already_exists = 0
    applied = 0

    for n, profile in enumerate(profile_obj):
        FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILE_TEMPLATES, time_for_loading=5)

        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("creating a server profile '%s' from template '%s' ..." % (profile.name, profile.template_name))
        # checking if the profile template is existing
        if VerifyServerProfileTemplate.verify_server_profile_template_exist(profile.template_name, fail_if_false=False) is False:
            logger.warn("server profile template '%s' does NOT exists" % profile.template_name)
            tpl_not_exists += 1
            continue

        FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
        # checking if the server profile to be created is existing
        if VerifyServerProfile.verify_server_profile_not_exist(profile.name, fail_if_false=False) is False:
            logger.warn("server profile '%s' to be created is already existing!" % profile.template_name)
            sp_already_exists += 1
            continue

        FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILE_TEMPLATES, time_for_loading=5)

        # - By default, this keyword will power off the server if it's powered on -- unless the attribute 'auto_power_off' is explicitly set to 'false'
        auto_power_off = False if getattr(profile, 'auto_power_off', '').lower() == 'false' else True

        CommonOperationServerProfileTemplate.click_server_profile_template(profile_template_name=profile.template_name)
        #   create server profile base on server profile template
        C7000CreateServerProfileFromTemplate.select_action_create_server_profile()
        C7000CreateServerProfileFromTemplate.wait_create_server_profile_dialog_shown()

        # wait some seconds to get textbox 'Name' available
        time.sleep(5)
        C7000CreateServerProfileFromTemplate.input_name(profile.name)
        C7000CreateServerProfileFromTemplate.input_description(profile.desc)
        if C7000CreateServerProfileFromTemplate.input_select_server_hardware(profile.server, auto_power_off=auto_power_off) is False:
            logger.warn("server hardware '%s' is not selected for creating server profile, may be wrong name, or powered on but failed to power it off. "
                        "test will skip this profile '%s' and continue to create other server profiles" % (profile.server, profile.name))
            continue
        msg = C7000CreateServerProfileFromTemplate.get_error_message_from_server_hardware()
        if msg is not None:
            logger.warn("error occurred, server profile can not be created successfully: \n<%s>" % msg)
            ui_lib.fail_test(msg)

        sht_selected = C7000CreateServerProfileFromTemplate.get_selected_server_hardware_type(profile.server)

        # input 'Affinity' for BL server, or when 'server hardware' == 'unassigned'
        if sht_selected[:2:] == 'BL' or profile.server == 'unassigned':
            if getattr(profile, 'Affinity', None) is not None:
                logger.info("test data for 'Affinity' is found: <%s>, start setting Affinity ..." % profile.Affinity)
                C7000CreateServerProfileFromTemplate.select_affinity_by_text(profile.Affinity)

        if getattr(profile, 'Firmware', None) is not None:
            logger.info("test data for 'Firmware' is found: <%s>, start setting Firmware Baseline ..." % profile.Firmware)
            logger.debug("test data for 'Firmware' is found: <%s>" % profile.Firmware, also_console=False)
            # set Firmware Baseline and force-installation option
            CommonOperationServerProfile.Firmware.set(profile.Firmware)

        if getattr(profile, 'Connections', None) is not None:
            logger.debug("test data for 'Connections' is found: <%s>" % profile.Connections, also_console=False)
            logger.info("test data for 'Connections' is found, start adding connections ...")
            # add connections
            CommonOperationServerProfile.Connection.set(profile.Connections)

        if getattr(profile, 'LocalStorage', None) is not None:
            logger.debug("test data for 'Local Storage' is found: <%s>" % profile.LocalStorage, also_console=False)
            logger.info("test data for 'Local Storage' is found, start setting local storage options ... ")
            CommonOperationServerProfile.LocalStorage.set(profile.LocalStorage)

        if getattr(profile, 'SANStorage', None) is not None:
            logger.debug("test data for 'SAN Storage' is found:<%s>" % profile.SANStorage, also_console=False)
            logger.info("test data for 'SAN Storage' is found, start setting SAN storage options and adding volumes ...")
            # select "Manage SAN Storage" checkbox
            CommonOperationServerProfile.SANStorage.set(profile.SANStorage)

        if getattr(profile, 'BootSettings', None) is not None:
            logger.debug("test data for 'Boot Settings' is found: <%s>" % profile.BootSettings, also_console=False)
            logger.info("test data for 'Boot Settings' is found, start setting its options ...")
            CommonOperationServerProfile.BootSettings.set(profile, server_hardware_type=sht_selected)

        # 'BIOSSettings' part is ignored since BIOS setting is complicated to verify the result, therefor
        #  might be better to use a dedicated tool to do this part automation separately

        if getattr(profile, 'Advanced', None) is not None:
            logger.debug("test data for 'Advanced' is found: <%s>" % profile.Advanced, also_console=False)
            logger.info("test data for 'Advanced' is found, start setting its options ...")
            # select "MAC/WWN/Serial/Hide unused FlexNICs" radio box
            C7000CreateServerProfileFromTemplate.Advanced.set(profile)

        C7000CreateServerProfileFromTemplate.click_create_button()
        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
        if status is True:
            logger.warn("unexpected error occurred: %s" % msg)
            ui_lib.fail_test(msg)

        C7000CreateServerProfileFromTemplate.wait_create_server_profile_dialog_disappear(timeout=180)
        # navigate to server profile page even though it automatically goes to SP page in order to make sure we are in SP page
        FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

        # check activity message
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(profile.name, 'Create', timeout=3600, fail_if_false=True)
        FusionUIBase.show_activity_sidebar()
        CommonOperationServerProfile.wait_server_profile_status_ok(profile.name, timeout=180, fail_if_false=True)
        logger.info("created server profile '%s' from template '%s' successfully" % (profile.name, profile.template_name))
        applied += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))

    if tpl_not_exists > 0:
        logger.warn("%s profile template(s) to be used for create server profile not exist, test is considered Failed" % tpl_not_exists)
        return False

    if total - sp_already_exists == 0:
        logger.warn("no server profile applied from template to create! all %s server profile(s) is already existing, test is considered PASS" % sp_already_exists)
        return True
    else:
        if applied < total:
            logger.warn("not all of the server profile(s) is successfully created - %s out of %s created " % (applied, total))
            if applied + sp_already_exists == total:
                logger.warn("%s already existing server profile(s) is skipped, test is considered PASS" % sp_already_exists)
                return True
            else:
                logger.warn("%s already existing server profile(s) is skipped, %s profile(s) left is failed being created " % (sp_already_exists, total - applied - sp_already_exists))
                return False

    logger.info("all of the server profile(s) is successfully created - %s out of %s " % (applied, total))
    return True


def verify_server_profile_template_general_info(profile_template_obj):
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILE_TEMPLATES, time_for_loading=5)

    total = len(profile_template_obj)
    not_exists = 0
    verified_pass = 0

    for n, profile_template in enumerate(profile_template_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("verifying general info of a server profile template named '%s'" % profile_template.name)
        #   check if server profile exists
        if VerifyServerProfileTemplate.verify_server_profile_template_exist(profile_template.name, fail_if_false=False) is False:
            logger.warn("server profile template '%s' does not exist" % profile_template.name)
            not_exists += 1
            continue
        CommonOperationServerProfileTemplate.click_server_profile_template(profile_template_name=profile_template.name, time_for_loading=4)
        #   check if already powered off
        FusionUIBase.select_view_by_name(view_name='General', timeout=5, fail_if_false=False)
        result = {'Server hardware type': None,
                  'Enclosure group': None,
                  }

        logger.info("getting server hardware type of server hardware '%s' to be used for comparison" % profile_template.ref_server)
        from FusionLibrary.ui.servers.serverhardware import get_type_of_server_hardware
        sht_selected = get_type_of_server_hardware(profile_template.ref_server)
        FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILE_TEMPLATES, time_for_loading=5)

        if VerifyServerProfileTemplate.verify_general_server_hardware_type(expect_value=sht_selected, timeout=7, fail_if_false=False) is False:
            logger.warn("'Server hardware type' of server profile template '%s' is not '%s', verification failed." % (profile_template.name, sht_selected))
            result['Server hardware type'] = False
        else:
            result['Server hardware type'] = True

        if VerifyServerProfileTemplate.verify_general_enclosure_group(expect_value=profile_template.enclgroup, timeout=7, fail_if_false=False) is False:
            logger.warn("'Enclosure group' of server profile template '%s' is not '%s', verification failed." % (profile_template.name, profile_template.enclgroup))
            result['Enclosure group'] = False
        else:
            result['Enclosure group'] = True

        # if reduce(lambda x, y: (x and y), result.values()) is not True:
        if all(result.values()) is not True:
            logger.warn("server profile template '%s' is FAIL for general info verification" % profile_template.name)
        else:
            logger.info("server profile template '%s' is PASS for general info verification" % profile_template.name)
            verified_pass += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        # logger.warn("no server profile template to verify general info against! all %s server profile(s) is NOT existing, test is considered FAIL" % not_exists)
        logger.warn("no server profile template to verify general info against! all %s server profile(s) is NOT existing, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if verified_pass < total:
            logger.warn("not all of the server profile template(s) is successfully verified PASS - %s out of %s passed " % (verified_pass, total))
            if verified_pass + not_exists == total:
                # logger.warn("%s not-existing server profile template(s) is skipped, test is considered FAIL" % not_exists)
                logger.warn("%s not-existing server profile template(s) is skipped, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s not-existing server profile template(s) is skipped, "
                            "%s server profile template(s) left is failed being verified PASS " % (not_exists, total - verified_pass - not_exists))
                return False

    logger.info("all of the server profile template(s) is successfully verified PASS - %s out of %s " % (verified_pass, total))
    return True


def verify_server_profile_connections_info(*profile_obj):
    """ Verify the connections information of server profile
    Example:
      <profile name="SP_wpst23bay3_BL465c_Gen8" newName="SP_wpst23bay3_BL465c_Gen8" desc="This profile is an edited one" server="wpst23, bay 3" hardwareType="BL465c Gen8" enclgroup="GRP-wpst32" Affinity="Device bay">
        <Connections>
            <Verify>
                <connection name="CON_Net1_edited" port="FlexibleLOM 1:1-a" network="Net1" boot="Not bootable"/>
                <connection name="CON_Net2_edited" port="FlexibleLOM 1:2-a" network="Net2" boot="Not bootable"/>
            </Verify>
        </Connections>
    </profile>
    """

    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILE_TEMPLATES, time_for_loading=5)

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    total = len(profile_obj)

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("verifying Connections info of a server profile template named '%s'" % profile.name)
        #   check if server profile exists
        if not VerifyServerProfileTemplate.verify_server_profile_template_exist(profile.name, fail_if_false=True):
            ui_lib.fail_test("Server profile template with name '%s' does not exist." % profile.name)

        CommonOperationServerProfileTemplate.click_server_profile_template(profile_template_name=profile.name, time_for_loading=4)
        #   check if already powered off
        FusionUIBase.select_view_by_name(view_name='Connections', timeout=5, fail_if_false=False)
        conn_verify = profile.Connections.Verify

        for m, conn in enumerate(conn_verify):

            conn_num = m + 1

            # Expand the connection to for verification
            FusionUIBase.wait_for_element_and_click(GeneralServerProfileTemplatesElements.Connection.ID_TABLE_CONNECTION_DETAIL_INFO % conn_num, timeout=5, fail_if_false=False)

            if getattr(conn, 'name') is not None:
                logger.info("Verifying 'Connection Name'...")
                if VerifyServerProfileTemplate.verify_connections_name(expect_value=conn.name, number=conn_num, timeout=7):
                    logger.info("'Connection Name' contains expected value '%s'" % conn.name)

            if getattr(conn, 'port') is not None:
                logger.info("Verifying 'Connection Port'...")
                if VerifyServerProfileTemplate.verify_connections_port(expect_value=conn.port, number=conn_num, timeout=7):
                    logger.info("'Connection Port' contains expected value '%s'" % conn.port)

            if getattr(conn, 'network') is not None:
                logger.info("Verifying 'Connection Network'...")
                if VerifyServerProfileTemplate.verify_connections_network(expect_value=conn.network, number=conn_num, timeout=7):
                    logger.info("'Connection Network' contains expected value '%s'" % conn.network)

            if hasattr(conn, 'boot'):
                logger.info("Verifying 'Connection Boot Option'...")
                if VerifyServerProfileTemplate.verify_connections_boot(expect_value=conn.boot, number=conn_num, timeout=7):
                    logger.info("'Connection Boot Option' contains expected value '%s'" % conn.boot)

            if getattr(conn, 'FunctionType') is not None:
                logger.info("Verifying connection '%s' is Type '%s" % (conn.name, conn.FunctionType))
                if VerifyServerProfileTemplate.verify_connection_type(expect_value=conn.FunctionType):
                    logger.info("Connection 'Type' contains expected value '%s'" % conn.FunctionType)

            if hasattr(conn, 'RequestedBandwidth'):
                request_bandwidth = conn.RequestedBandwidth + ' Gb/s'
                logger.info("Verifying 'Requested Bandwidth'...")
                if VerifyServerProfileTemplate.verify_connections_requestedbandwidth(expect_value=request_bandwidth, timeout=7):
                    logger.info("'Requested Bandwidth' contains expected value '%s'" % request_bandwidth)

            if hasattr(conn, 'initiatorName'):
                logger.info("Verifying connection '%s' has Initiator name 'not set'" % conn.name)
                if VerifyServerProfileTemplate.verify_connection_initiator_name("not set"):
                    logger.info("Connection 'Initiator name' contains expected value 'not set'")

            if hasattr(conn, 'initiatorIpv4'):
                logger.info("Verifying connection '%s' has Initiator IP address 'not set'" % conn.name)
                if VerifyServerProfileTemplate.verify_connection_initiator_ip("not set"):
                    logger.info(
                        "Connection 'Initiator IP address' contains expected value 'not set'")

            if hasattr(conn, 'subnetMask'):
                logger.info("Verifying connection '%s' has Initiator subnet mask '%s'" % (conn.name, conn.subnetMask))
                if VerifyServerProfileTemplate.verify_connection_initiator_subnet_mask(conn.subnetMask):
                    logger.info("Connection 'Initiator subnet mask' contains expected value '%s'" % conn.subnetMask)

            if hasattr(conn, 'gateway'):
                if conn.gateway == "":
                    logger.info("Verifying connection '%s' has Initiator gateway 'not set'" % conn.name)
                    if VerifyServerProfileTemplate.verify_connection_initiator_gateway("not set"):
                        logger.info("Connection 'Initiator gateway' contains expected value 'not set'")
                else:
                    logger.info("Verifying connection '%s' has Initiator gateway '%s" % (conn.name, conn.gateway))
                    if VerifyServerProfileTemplate.verify_connection_initiator_gateway(conn.gateway):
                        logger.info("Connection 'Initiator gateway' contains expected value '%s'" % conn.gateway)

            if hasattr(conn, 'targetName'):
                logger.info("Verifying connection '%s' has Target name 'not set'" % conn.name)
                if VerifyServerProfileTemplate.verify_connection_target_name("not set"):
                    logger.info("Connection 'Target name' contains expected value 'not set'")

            if hasattr(conn, 'targetLun'):
                logger.info("Verifying connection '%s' has Target LUN 'not set'" % conn.name)
                if VerifyServerProfileTemplate.verify_connection_target_lun("not set"):
                    logger.info("Connection 'Target LUN' contains expected value 'not set'")

            if hasattr(conn, 'targetIp'):
                if conn.targetIp == "":
                    logger.info("Verifying connection '%s' has Target IP address 'not set'" % conn.name)
                    if VerifyServerProfileTemplate.verify_connection_target_ip("not set"):
                        logger.info("Connection 'Target IP address' contains expected value 'not set'")
                else:
                    target_ip = ':'.join([conn.targetIp, conn.targetPort])
                    logger.info("Verifying connection '%s' has Target IP address '%s'" % (conn.name, target_ip))
                    if VerifyServerProfileTemplate.verify_connection_target_ip(target_ip):
                        logger.info("Connection 'Target IP address' contains expected value '%s'" % target_ip)

            if hasattr(conn, 'secondIp'):
                if conn.secondIp == "":
                    logger.info("Verifying connection '%s' has Second IP address 'not set'" % conn.name)
                    if VerifyServerProfileTemplate.verify_connection_second_ip("not set"):
                        logger.info("Connection 'Second IP address' contains expected value 'not set'")
                else:
                    second_ip = ':'.join([conn.secondIp, conn.secondPort])
                    logger.info("Verifying connection '%s' has Second IP address '%s" % (conn.name, second_ip))
                    if VerifyServerProfileTemplate.verify_connection_second_ip(second_ip):
                        logger.info("Connection 'Second IP address' contains expected value '%s'" % second_ip)

            if hasattr(conn, 'chapLvl'):
                if conn.chapLvl == 'None':
                    VerifyServerProfileTemplate.verify_connection_chap_name("not set")
                    VerifyServerProfileTemplate.verify_connection_mchap_name_not_visible()
                elif conn.chapLvl == 'CHAP':
                    VerifyServerProfileTemplate.verify_connection_chap_name("not set")
                    VerifyServerProfileTemplate.verify_connection_mchap_name_not_visible()
                elif conn.chapLvl == 'Mutual CHAP':
                    VerifyServerProfileTemplate.verify_connection_chap_name("not set")
                    VerifyServerProfileTemplate.verify_connection_mchap_name("not set")

            # Collapse the connection after verification
            FusionUIBase.wait_for_element_and_click(GeneralServerProfileTemplatesElements.Connection.ID_TABLE_CONNECTION_DETAIL_INFO % conn_num, timeout=5, fail_if_false=True)


def verify_server_profile_template_advanced_info(*profile_obj):
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILE_TEMPLATES, time_for_loading=5)

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    total = len(profile_obj)

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("Verifying Advanced info of a server profile template named '%s'" % profile.name)
        #   check if server profile exists
        if not VerifyServerProfileTemplate.verify_server_profile_template_exist(profile.name, fail_if_false=True):
            ui_lib.fail_test("Server profile template with name '%s' does not exist." % profile.name)

        CommonOperationServerProfileTemplate.click_server_profile_template(profile_template_name=profile.name, time_for_loading=4)
        FusionUIBase.select_view_by_name(view_name='Advanced', timeout=5, fail_if_false=True)
        advanced = profile.Advanced

        if hasattr(advanced, 'iscsi'):
            VerifyServerProfileTemplate.verify_advanced_iscsi_initiator_name(expect_value=advanced.iscsi, timeout=7)

        if hasattr(advanced, 'serial'):
            VerifyServerProfileTemplate.verify_advanced_uuid(expect_value=advanced.serial, timeout=7)

        if hasattr(advanced, 'mac'):
            VerifyServerProfileTemplate.verify_advanced_mac_addresses(expect_value=advanced.mac, timeout=7)

        if hasattr(advanced, 'wwn'):
            VerifyServerProfileTemplate.verify_advanced_wwn_addresses(expect_value=advanced.wwn, timeout=7)


def select_profile_template(profiletempname):
    """ Create Server Profile Template   """

    if not navigate():
        return False

    logger._log_to_console_and_log_file("Selecting profile template: '%s'" % profiletempname)
    if ui_lib.wait_for_element_visible(FusionServerProfileTemplatesPage.ID_SELECT_PROFILE_TEMPLATE % profiletempname):
        if ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_SELECT_PROFILE_TEMPLATE % profiletempname):
            logger._log_to_console_and_log_file("Given Profile template  %s is selected" % profiletempname)
            return True
        else:
            logger._warn("Unable to select the profile template: '%s'" % profiletempname)
            return False
    else:
        logger._warn("Profile template '%s' is not present in the appliance" % profiletempname)
        return False


def create_profile_from_template(*template_profile_obj):
    """ Create server profile from profile template """

    logger._log_to_console_and_log_file("Navigating to server profile template page...")
    if not navigate():
        return False

    if isinstance(template_profile_obj, test_data.DataObj):
        template_profile_obj = [template_profile_obj]
    elif isinstance(template_profile_obj, tuple):
        template_profile_obj = list(template_profile_obj[0])

    for prof in template_profile_obj:

        """ Selecting profile template """
        if not select_profile_template(prof.templ_name):
            ui_lib.fail_test("profile template is not present in template list")

        logger._log_to_console_and_log_file("verifying for profile existence before proceeding to create")
        if prof.has_property("prof_name") and prof.prof_name.strip() != "":
            if serverprofiles.select_server_profile(prof.prof_name):
                ui_lib.fail_test("FAIL: Server profile '{0}' is already present".format(prof.prof_name))
        else:
            ui_lib.fail_test("'prof_name' is a mandatory field and should not be empty")

        logger._log_to_console_and_log_file("Powering of server '{0}".format(prof.server))
        if prof.server.strip() != "unassigned" and not (serverhardware.power_off_server(prof.server)):
            ui_lib.fail_test("Can't proceed with server profile creation on server %s" % prof.server)

        if not ui_lib.wait_for_element_visible(FusionServerProfileTemplatesPage.ID_PAGE_LABEL):
            if not navigate():
                ui_lib.fail_test("FAIL: failed to navigate profile template page")

        logger._log_to_console_and_log_file("Selecting Create server profile option from Actions menu")
        ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_MENU_MAIN_ACTION)
        ui_lib.wait_for_element_visible(FusionServerProfileTemplatesPage.ID_MENU_ACTION_CREATE_SERVER_PROFILE, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_MENU_ACTION_CREATE_SERVER_PROFILE)

        ui_lib.wait_for_element_visible(FusionServerProfileTemplatesPage.ID_INPUT_PROFILE_NAME)
        ui_lib.wait_for_element_and_input_text(FusionServerProfileTemplatesPage.ID_INPUT_PROFILE_NAME, prof.prof_name)

        if prof.has_property("prof_description") and prof.prof_description.strip() != "":
            logger._log_to_console_and_log_file("Entering profile description: '{0}'".format(prof.prof_description))
            ui_lib.wait_for_element_and_input_text(FusionServerProfileTemplatesPage.ID_INPUT_PROFILE_DESCRIPTION, prof.prof_description)

        if prof.has_property("server") and prof.server.strip() != "":
            logger._log_to_console_and_log_file("Selecting sever '{0}' to create profile".format(prof.server))
            ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_COMBO_SERVER_HARDWARE_DROPDOWN)
            if ui_lib.wait_for_element_visible(FusionServerProfileTemplatesPage.ID_ELEMENT_SERVER_NAME % prof.server):
                ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_ELEMENT_SERVER_NAME % prof.server)
                logger._log_to_console_and_log_file("Selected valid server hardware")
            else:
                ui_lib.fail_test("Provided server '{0}' is not a valid".format(prof.server))
        else:
            ui_lib.fail_test("'server' name is a mandatory field and should not be empty")

        if prof.has_property("override_temp") and prof.override_temp.lower().strip() == 'false':
            logger._log_to_console_and_log_file("Creating server profile from template without overriding template")
        elif prof.has_property("override_temp") and prof.override_temp.lower().strip() == 'true':
            logger._log_to_console_and_log_file("Creating server profile from template with overriding template")
            ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_CHECKBOX_OVERRIDE_TEMPALTE)
        ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_BTN_CREATE_PROFILE)
        ui_lib.wait_for_element_notvisible(FusionServerProfileTemplatesPage.ID_DIALOG_CREATE_PROFILE, PerfConstants.SELECT_ENCLOSURE * 3)
        ui_lib.wait_for_element_notvisible(FusionServerProfileTemplatesPage.ID_DIALOG_CREATE_PROFILE_ERROR, PerfConstants.SELECT_ENCLOSURE)
        if ui_lib.wait_for_element_visible(FusionServerProfileTemplatesPage.ID_DIALOG_CREATE_PROFILE_ERROR, PerfConstants.WAIT_UNTIL_CONSTANT):
            if ui_lib.wait_for_element_visible(FusionServerProfileTemplatesPage.ID_DIALOG_CREATE_PROFILE_ERROR_WARNING, PerfConstants.WAIT_UNTIL_CONSTANT):
                logger._warn("Profile %s will create with server hardware has health status as WARNING" % prof.prof_name)
                ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_BTN_CREATE_PROFILE)
            else:
                ui_lib.fail_test(ui_lib.get_text(FusionServerProfileTemplatesPage.ID_DIALOG_CREATE_PROFILE_ERROR))

        ui_lib.wait_for_element(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % prof.prof_name, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.ignore_staleElementRefException("_is_visible", FusionServerProfilesPage.ID_PROFILE_CHANGING)
        logger._log_to_console_and_log_file("Waiting for profile creation to complete..")

        logger._log_to_console_and_log_file("Validating profile %s" % prof.prof_name)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ACTVITY_PROFILE)
        if ui_lib.wait_for_element(FusionServerProfileTemplatesPage.ID_ELEMENT_ACTIVITY % prof.prof_name):
            if ui_lib.wait_for_element(FusionServerProfileTemplatesPage.ID_ACTIVITY_STATUS_OK, PerfConstants.CREATE_SERVER_PROFILE_TIME):
                logger._log_to_console_and_log_file("Profile template %s created" % prof.prof_name)
            elif ui_lib.wait_for_element(FusionServerProfileTemplatesPage.ID_ACTIVITY_STATUS_WARNING):
                logger._warn("Profile %s created with warning" % prof.prof_name)
            else:
                logger._warn("Failed to create server profile %s" % prof.prof_name)
                return False

        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ACTVITY_PROFILE)

    return True


def update_profile_template_connections(profile_template_obj):

    s2l = ui_lib.get_s2l()
    flag = None
    if not s2l._is_element_present(FusionServerProfileTemplatesPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(profile_template_obj, test_data.DataObj):
        profile_template_obj = [profile_template_obj]
    elif isinstance(profile_template_obj, tuple):
        profile_template_obj = list(profile_template_obj[0])

    for template in profile_template_obj:
        logger._log_to_console_and_log_file("\nUpdating Server Profile template %s..." % template.templ_name)

        # Check if already exists
        template_list = [el.text for el in s2l._element_find(FusionServerProfileTemplatesPage.ID_TEMPLATE_LIST, False, False)]
        if template.templ_name not in template_list:
            logger._warn("Profile template '%s' not exists. Cannot proceed with template updation" % template.templ_name)
            continue

        ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_MENU_MAIN_ACTION)
        ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_LINK_EDIT_PROFILE_TEMPLATE)
        ui_lib.wait_for_element_visible(FusionServerProfileTemplatesPage.ID_ELEMENT_EDIT_WARNING)
        logger._log_to_console_and_log_file(ui_lib.get_text(FusionServerProfileTemplatesPage.ID_ELEMENT_EDIT_WARNING))

        if (template.has_property("connection") and len(template.connection) > 0):
            ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_COMBO_EDIT_MENU)
            ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_LINK_CONNECTIONS, PerfConstants.DEFAULT_SYNC_TIME)
            s2l.focus(FusionServerProfileTemplatesPage.ID_BTN_ADD_NETWORK_CONNECTION)
            ui_lib.wait_for_element_visible(FusionServerProfileTemplatesPage.ID_BTN_ADD_NETWORK_CONNECTION, PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_element(FusionServerProfileTemplatesPage.ID_BTN_ADD_NETWORK_CONNECTION, PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_BTN_ADD_NETWORK_CONNECTION)
            ui_lib.wait_for_element(FusionServerProfileTemplatesPage.ID_COMBO_DEVICE_TYPE, 120)

            # Adding network connections
            for connection in template.connection:
                if(connection.band == "" or connection.network.strip() == ""):
                    logger._warn("Mandatory fields for adding profile connections can't be empty")
                    continue

                if not s2l._is_element_present(FusionServerProfileTemplatesPage.ID_COMBO_DEVICE_TYPE):
                    logger._warn("Failed to load add network connections page..")
                    continue
                logger._log_to_console_and_log_file("Adding network : %s to profile " % connection.network)
                ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_COMBO_DEVICE_TYPE)
                label = ui_lib.get_text(FusionServerProfileTemplatesPage.ID_COMBO_DEVICE_TYPE)

                # Flag to check any errors occurred at the time of adding connections
                flag = 0
                # Adding FC connection
                if (connection.has_property("type") and
                        (connection.type.upper().strip() == "FIBRE CHANNEL" or connection.type.upper().strip() == "FIBRECHANNEL")):
                    s2l.press_key(FusionServerProfileTemplatesPage.ID_COMBO_DEVICE_TYPE, 'Fibre' + chr(13))
                    if not _add_profile_connections(connection, s2l):
                        logger._warn("Failed to add %s connection to profile" % connection.network)
                        ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_BTN_CANCEL_NETWORK_ADD_CONNECTION)
                        flag = 1
                        break
                    if (connection.has_property('boot') and (connection.boot.strip() == 'Primary' or connection.boot.strip() == 'Secondary')):
                        if connection.has_property('targetwwpn') and connection.has_property('targetlun') and connection.targetwwpn.strip() != "" and connection.targetlun.strip() != "":
                            logger._log_to_console_and_log_file("Specifying boot target ...")
                            ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_RADIO_SPECIFIY_BOOT_TARGET)
                            if(connection.targetwwpn == "" or connection.targetlun == ""):
                                logger._warn("Please provide valid target WWPN and LUN")
                                ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_BTN_CANCEL_NETWORK_ADD_CONNECTION)
                                flag = 1
                                break
                            logger._log_to_console_and_log_file("Typing target WWPN...")
                            ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_INPUT_FIBERCHANNEL_WWN_TARGET)
                            ui_lib.wait_for_element_and_input_text(FusionServerProfileTemplatesPage.ID_INPUT_FIBERCHANNEL_WWN_TARGET,
                                                                   connection.targetwwpn)
                            logger._log_to_console_and_log_file("Typing target LUN...")
                            ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_INPUT_FIBERCHANNEL_LUN_TARGET)
                            ui_lib.wait_for_element_and_input_text(FusionServerProfileTemplatesPage.ID_INPUT_FIBERCHANNEL_LUN_TARGET,
                                                                   connection.targetlun)
                        else:
                            logger._log_to_console_and_log_file("Use bios...")
                            ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_RADIO_USE_BIOS)

                    if connection.has_property('macaddress') and connection.macaddress.strip() != "":
                        logger._log_to_console_and_log_file("Selecting use user specified ids checkbox ...")
                        s2l.select_checkbox(FusionServerProfileTemplatesPage.ID_CHKBOX_USER_SPECIFIED_IDS)
                        if(connection.wwpn.strip() == "" or connection.wwnn.strip() == ""):
                            logger._warn("Please provide valid WWPN, WWNN and MAC address")
                            ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_BTN_CANCEL_NETWORK_ADD_CONNECTION)
                            flag = 1
                            break
                        logger._log_to_console_and_log_file("Typing WWPN ...")
                        ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_INPUT_FIBERCHANNEL_WWPN)
                        ui_lib.wait_for_element_and_input_text(FusionServerProfileTemplatesPage.ID_INPUT_FIBERCHANNEL_WWPN, connection.wwpn)
                        logger._log_to_console_and_log_file("Typing WWNN ...")
                        ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_INPUT_FIBERCHANNEL_WWNN)
                        ui_lib.wait_for_element_and_input_text(FusionServerProfileTemplatesPage.ID_INPUT_FIBERCHANNEL_WWNN, connection.wwnn)
                        logger._log_to_console_and_log_file("Typing mac address...")
                        ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_INPUT_FIBERCHANNEL_MAC)
                        ui_lib.wait_for_element_and_input_text(FusionServerProfileTemplatesPage.ID_INPUT_FIBERCHANNEL_MAC, connection.macaddress)

                elif (connection.has_property("type") and (connection.type.upper().strip() == "ETHERNET")):
                    # Adding ethernet ethernet connections
                    if not label == "Ethernet":
                        s2l.press_key(FusionServerProfileTemplatesPage.ID_COMBO_DEVICE_TYPE, 'Etherne40t' + chr(13))
                    if not _add_profile_connections(connection, s2l):
                        logger._warn(" : Failed to add %s connection to profile" % connection.network)
                        ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_BTN_CANCEL_NETWORK_ADD_CONNECTION)
                        flag = 1
                        break

                logger._log_to_console_and_log_file("Clicking on network add button...")
                ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_BTN_ADD_NETWORK_ADD_PLUS_CONNECTON)
                if(s2l._is_element_present(FusionServerProfileTemplatesPage.ID_CONNECTION_ERROR)):
                    logger._warn("Failed to add connection %s to the profile" % connection.network)
                    ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_BTN_CANCEL_NETWORK_ADD_CONNECTION)
                    flag = 1
                    break

            if(flag != 0):
                logger._warn("Canceling the creation of server profile template %s" % template.templ_name)
                ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_BTN_CANCEL_SERVER_PROFILE)
                continue

            # For closing the add connection page and verifying for the table
            if(s2l._is_element_present(FusionServerProfileTemplatesPage.ID_BTN_ADD_NETWORK_ADD_PLUS_CONNECTON)):
                logger._log_to_console_and_log_file("Close add connection Page")
                ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_BTN_CANCEL_NETWORK_ADD_CONNECTION)
            # verifying for the connections table
            if not s2l._is_element_present(FusionServerProfileTemplatesPage.ID_BTN_EDIT_TEMPLATE_OK):
                logger._warn("Failed to add connection %s to the profile" % connection.network)
                ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_BTN_CANCEL_NETWORK_ADD_CONNECTION)

            ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_BTN_EDIT_TEMPLATE_OK)
            s2l.wait_until_page_contains_element(FusionServerProfileTemplatesPage.ID_ELEMENT_TEMPLATE_NAME_BASE % template.templ_name, PerfConstants.DEFAULT_SYNC_TIME)

    ui_lib.ignore_staleElementRefException("_is_visible", FusionServerProfileTemplatesPage.ID_TEMPLATE_CHANGING)
    logger._log_to_console_and_log_file("Waiting for profile template updation to complete..")

    ui_lib.wait_for_element_and_click(FusionServerProfileTemplatesPage.ID_ELEMENT_RIGHT_PIN)
    if ui_lib.wait_for_element(FusionServerProfileTemplatesPage.ID_ELEMENT_ACTIVITY % template.templ_name):
        if ui_lib.wait_for_element(FusionServerProfileTemplatesPage.ID_ACTIVITY_STATUS_OK, PerfConstants.WAIT_UNTIL_CONSTANT):
            logger._log_to_console_and_log_file("Profile template %s updated" % template.templ_name)
        elif ui_lib.wait_for_element(FusionServerProfileTemplatesPage.ID_ACTIVITY_STATUS_WARNING, PerfConstants.WAIT_UNTIL_CONSTANT):
            logger._warn("Profile template %s updated with warning" % template.templ_name)
        else:
            logger._warn("Failed to update server profile template %s" % template.templ_name)


def validate_server_profile_template_in_use_cannot_be_deleted(profile_template):
    profile_template_name = profile_template.name
    expected_error_message = profile_template.expected_error_message

    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILE_TEMPLATES, time_for_loading=5)
    #   check if server profile template exists
    if VerifyServerProfileTemplate.verify_server_profile_template_exist(profile_template_name, fail_if_false=False) is False:
        logger.warn("server profile template '%s' does NOT exist! keyword '%s' returns a 'False'" % (profile_template_name, sys._getframe().f_code.co_name))
        return False
    CommonOperationServerProfileTemplate.click_server_profile_template(profile_template_name=profile_template_name)

    #   check if the server profile template is truly being used by Server Profile(s)
    if CommonOperationServerProfileTemplate.get_used_by_info_of_server_profile_template(profile_template_name, fail_if_false=False).lower() == 'none':
        logger.warn("server profile template '%s' is not used by any server profile(s), 'Used by' is 'none', which means precondition has not been met, keyword '%s' returns FALSE" % (profile_template_name, sys._getframe().f_code.co_name))
        return False

    #   start performing remove action
    DeleteServerProfileTemplate.select_action_delete()

    if VerifyServerProfileTemplate.verify_error_message_when_deleting_used_server_profile_template(
            expected_error_message=expected_error_message,
            timeout=5,
            fail_if_false=False) is False:
        logger.warn("expected error message not found when deleting used template '%s', keyword '%s' returns FALSE" % (profile_template_name, sys._getframe().f_code.co_name))
        return False
    else:
        logger.info("expected error message successfully found when deleting used template '%s' ..." % profile_template_name)
        if VerifyServerProfileTemplate.verify_used_by_profiles_count_link_when_deleting_used_server_profile_template(
                timeout=5,
                fail_if_false=False) is False:
            logger.warn("expected link 'Used by xxx profile(s)' not found when deleting used template '%s', keyword '%s' returns FALSE" % (profile_template_name, sys._getframe().f_code.co_name))
            return False
        else:
            logger.info("expected link 'Used by xxx profile(s)' successfully found when deleting used template '%s', ..." % profile_template_name)
            if VerifyServerProfileTemplate.verify_close_button_should_exist_when_deleting_used_server_profile_template(timeout=5, fail_if_false=False) is False:
                logger.warn("expected button 'Close' not found when deleting used template '%s', keyword '%s' returns FALSE" % (profile_template_name, sys._getframe().f_code.co_name))
                return False
            else:
                logger.info("expected button 'Close' found when deleting used template '%s', keyword '%s' returns TRUE" % (profile_template_name, sys._getframe().f_code.co_name))
                return True


def _select_value_from_a_profile_combo_box(combo_box_element, combo_box_list_option):
    """
        This function selects the value in a combo box element.
        This is useful when the combo box list is mapped with a string variable (e.g.: "//ul/li/a[text()='%s']")

        Example: _select_value_from_a_profile_combo_box(combo_box_element, combo_box_list_option)
    """
    ui_lib.wait_for_element_and_click(combo_box_element)
    ui_lib.wait_for_element_visible(combo_box_list_option)

    ui_lib.wait_for_element_and_click(combo_box_list_option)


def spt_verify_required_fields_for_iscsi_boot(profile_obj):
    """ Input blank fields for iSCSI boot when adding a connection during Create Server Profile Template and verify required
        fields error message is displayed

    Arguments:
      name*                --  Name of server hardware as a string.
      hardwareType*        --  server hardware type of the server, will be used to verify the selected server's SHT is correct.
      enclgroup*           --  Enclosure Group the server is part of, will be used to verify the selected server's EG is correct.
      manageBoot*          --  Must be set to True for this test to pass
      Connections*         --  List of connections to be added
        connection*        --  Connection object
            name           --  Name of the connection
            FunctionType*  --  Network Function type
            port*          --  Network Port Name
            network*       --  Network Name
            boot*          --  iSCSI boot mode, either "iSCSI primary" or "iSCSI secondary"
            BootOption*    --  iSCSI initiator name option, either "Profile initiator name" or "User specified"
            secondIp       --  Second Boot Target IP Address, value entered to check that second port is required
            subnetMask*    --  iSCSI Subnet mask, left blank
            gateway        --  iSCSI Gateway, left blank
            targetIp       --  iSCSI Target IP address, value entered to check that target port is required
            targetPort     --  iSCSI Target port, left blank
            secondPort     --  iSCSI Second target port
            chapLvl        --  iSCSI Authentication Level

    * Required Arguments

    Example:
        <profile name="Required Fields"
                 profile=""
                 profileName=""
                 hardwareType="SY 660 Gen9 1"
                 enclgroup="EG1">
            <Connections>
                <connection name="Mutual CHAP - iSCSI Boot Ethernet primary"
                            FunctionType = "Ethernet"
                            port = "Mezzanine 3:1-a"
                            network = "Untagged-net"
                            RequestedBandwidth = "1"
                            boot = "iSCSI primary"
                            secondIp="16.114.213.40"
                            BootOption="User specified"
                            subnetMask=""
                            gateway=""
                            targetIp="16.114.213.41"
                            targetPort=""
                            secondPort=""
                            chapLvl="Mutual CHAP"/>
            </Connections>
        </profile >
    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILE_TEMPLATES, time_for_loading=5)

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(profile_obj), '-' * 14))
        logger.info("Creating Server Profile Template | %s | ..." % profile.name)

        # checking if the profile already exists
        if not VerifyServerProfileTemplate.verify_server_profile_template_not_exist(profile.name, fail_if_false=True):
            ui_lib.fail_test("Server Profile Template | %s | already exists" % profile.name)

        # open Create SP dialog and enter data ...
        CreateServerProfileTemplate.click_create_server_profile_template_button()
        CreateServerProfileTemplate.wait_create_server_profile_template_dialog_shown()

        CreateServerProfileTemplate.input_name(profile.name)

        if hasattr(profile, 'ref_server'):
            hardware_type = FusionUIBase.APIMethods().get_server_hardware_type_by_server_hardware_name(profile.ref_server)
            logger.info('For server attribute is %s, hardware type is %s' % (profile.ref_server, hardware_type))
            CreateServerProfileTemplate.input_select_server_hardware_type(hardware_type)
        else:
            CreateServerProfileTemplate.input_select_server_hardware_type(profile.hardwareType)
        CreateServerProfileTemplate.input_select_enclosure_group(profile.enclgroup) if getattr(profile, 'enclgroup', None) is not None else None

        if hasattr(profile, 'Connections'):
            logger.info("test data for 'Connections' is found, start adding connections ...")

            # add connections with blank iSCSI boot data and verify required field error messages
            logger.info("change to 'Connections' view ...")
            FusionUIBase.select_view_by_name('Connections')
            logger.info("start adding connections ...")

            for n, connection in enumerate(profile.Connections):
                logger.info("--- <connections> ---: {2} No: {0} --- Total: {1} {2}".format((n + 1), len(profile.Connections), '-' * 14))
                logger.info("adding a connection with name '%s' ..." % connection.name)
                logger.debug("test data for connection '<%s>' is found: '<%s>'" % (connection.name, connection), also_console=False)

                # Verify the connection does not exist
                CommonOperationServerProfileTemplate.Connection.verify_connection_not_exist(connection.name, fail_if_false=True)

                # Add the connection
                CommonOperationServerProfileTemplate.Connection.click_add_connection_button()
                CommonOperationServerProfileTemplate.Connection.wait_add_connection_dialog_shown()

                CommonOperationServerProfileTemplate.Connection.input_name(connection.name)
                CommonOperationServerProfileTemplate.Connection.select_function_type_by_text(connection.FunctionType, fail_if_false=True)
                CommonOperationServerProfileTemplate.Connection.input_select_network(connection.network)
                CommonOperationServerProfileTemplate.Connection.input_select_port(connection.port)
                CommonOperationServerProfileTemplate.Connection.input_requested_bandwidth(connection.RequestedBandwidth)
                CommonOperationServerProfileTemplate.Connection.select_boot_by_text(connection.boot, fail_if_false=True)

                # Input information for the iSCSI boot connection
                if connection.boot == 'iSCSI primary' or connection.boot == 'iSCSI secondary':
                    CommonOperationServerProfileTemplate.Connection.set_iscsi_boot_options(connection)

                # Click "Add" button
                CommonOperationServerProfileTemplate.Connection.click_add_button()

                # Verify error messages & text field visibility
                CommonOperationServerProfileTemplate.Connection.verify_iscsi_initiator_name_not_visible()
                CommonOperationServerProfileTemplate.Connection.verify_iscsi_initiator_ip_not_visible()
                CommonOperationServerProfile.Connection.verify_iscsi_subnet_error_message("This field is required.")
                CommonOperationServerProfile.Connection.verify_iscsi_gateway_error_message("")
                CommonOperationServerProfileTemplate.Connection.verify_iscsi_vlan_id_not_visible()

                CommonOperationServerProfileTemplate.Connection.verify_iscsi_target_name_not_visible()
                CommonOperationServerProfileTemplate.Connection.verify_iscsi_target_lun_not_visible()
                CommonOperationServerProfile.Connection.verify_iscsi_target_ip_error_message("")

                if getattr(connection, "targetIp", "") is not "" and getattr(connection, "targetPort", "") is "":
                    CommonOperationServerProfile.Connection.verify_iscsi_target_port_error_message("This field is required.")
                else:
                    CommonOperationServerProfile.Connection.verify_iscsi_target_port_error_message("")

                CommonOperationServerProfile.Connection.verify_iscsi_second_ip_error_message("")

                if getattr(connection, "secondIp", "") is not "" and getattr(connection, "secondPort", "") is "":
                    CommonOperationServerProfile.Connection.verify_iscsi_second_port_error_message("This field is required.")
                else:
                    CommonOperationServerProfile.Connection.verify_iscsi_second_port_error_message("")

                if hasattr(connection, "chapLvl"):
                    CommonOperationServerProfileTemplate.Connection.verify_iscsi_chap_name_not_visible()
                    CommonOperationServerProfileTemplate.Connection.verify_iscsi_chap_secret_not_visible()
                    CommonOperationServerProfileTemplate.Connection.verify_iscsi_mchap_name_not_visible()
                    CommonOperationServerProfileTemplate.Connection.verify_iscsi_mchap_secret_not_visible()

                # Click "Cancel" button
                CommonOperationServerProfileTemplate.Connection.click_cancel_button()
        else:
            ui_lib.fail_test("Connections object not present in data file for profile template with name | %s |" % profile.name)

        CreateServerProfileTemplate.click_cancel_button()


def verify_server_profile_template_local_storage_info(*profile_obj):
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILE_TEMPLATES, time_for_loading=5)

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    total = len(profile_obj)
    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("verifying Local storage info of a server profile named '%s'" % profile.name)
        #   check if server profile exists
        if not VerifyServerProfileTemplate.verify_server_profile_template_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' does not exist" % profile.name)
            continue
        CommonOperationServerProfileTemplate.click_server_profile_template(profile_template_name=profile.name, time_for_loading=4)
        FusionUIBase.select_view_by_name(view_name='Local Storage', timeout=5, fail_if_false=False)

        if hasattr(profile, 'LocalStorage'):
            logger.info("test data for 'Local Storage' is found")
            local_storage = profile.LocalStorage
        else:
            msg = "Can not found test data for 'Local Storage', test failed!"
            ui_lib.fail_test(msg)

        if hasattr(local_storage, 'integratedControllerMode'):
            logger.info("Verifying Integrated Controller Mode")
            VerifyServerProfileTemplate.verify_integrated_storage_mode(expect_value=local_storage.integratedControllerMode, timeout=10, fail_if_false=True)
            if hasattr(local_storage, 'LogicalDrives'):
                logger.info("test data for 'Logical Drives' is found")
                local_storage = profile.LocalStorage
                logical_drives = local_storage.LogicalDrives
                if hasattr(logical_drives, 'Verify') and len(logical_drives.Verify) != []:
                    verification = logical_drives.Verify
                    for verify in verification:
                        if hasattr(verify, 'name'):
                            VerifyServerProfileTemplate.verify_logical_drive_name(expect_value=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'RAIDlevel'):
                            VerifyServerProfileTemplate.verify_logical_drive_raid_level(expect_value=verify.RAIDLevel, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'NumberOfPhysicalDrives'):
                            VerifyServerProfileTemplate.verify_logical_drive_num_of_drives(expect_value=verify.NumberOfPhysicalDrives, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'minSize'):
                            VerifyServerProfileTemplate.verify_logical_drive_min_gb(expect_value=verify.minSize, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'maxSize'):
                            VerifyServerProfileTemplate.verify_logical_drive_max_gb(expect_value=verify.maxSize, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'DriveTechnology'):
                            VerifyServerProfileTemplate.verify_logical_drive_drive_tech(expect_value=verify.DriveTechnology, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'boot'):
                            VerifyServerProfileTemplate.verify_logical_drive_boot(expect_value=verify.boot, drivename=verify.name, timeout=10, fail_if_false=True)

                else:
                    msg = "Test data failed, please ensure the 'Verify' node exists and its sub-node is not null in LogicalDrives"
                    ui_lib.fail_test(msg)

        if hasattr(local_storage, 'mezzControllerMode'):
            logger.info("Verifying Mezz Controller Mode")
            VerifyServerProfileTemplate.verify_mezz_storage_mode(mezzID=local_storage.mezzControllerID, expect_value=local_storage.mezzControllerMode, timeout=10, fail_if_false=True)
            if hasattr(local_storage, 'LogicalJBODs'):
                logger.info("test data for 'Logical JBODs' is found")
                local_storage = profile.LocalStorage
                logical_JBODs = local_storage.LogicalJBODs
                if hasattr(logical_JBODs, 'Verify') and len(logical_JBODs.Verify) != []:
                    verification = logical_JBODs.Verify
                    for verify in verification:
                        if hasattr(verify, 'name'):
                            VerifyServerProfileTemplate.verify_logical_jbod_name(mezzID=local_storage.mezzControllerID, expect_value=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'RAIDlevel'):
                            VerifyServerProfileTemplate.verify_logical_jbod_raid_level(mezzID=local_storage.mezzControllerID, expect_value=verify.RAIDLevel, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'NumberOfPhysicalDrives'):
                            VerifyServerProfileTemplate.verify_logical_jbod_num_of_drives(mezzID=local_storage.mezzControllerID, expect_value=verify.NumberOfPhysicalDrives, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'minSize'):
                            VerifyServerProfileTemplate.verify_logical_jbod_min_gb(mezzID=local_storage.mezzControllerID, expect_value=verify.minSize, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'maxSize'):
                            VerifyServerProfileTemplate.verify_logical_jbod_max_gb(mezzID=local_storage.mezzControllerID, expect_value=verify.maxSize, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'DriveTechnology'):
                            VerifyServerProfileTemplate.verify_logical_jbod_drive_tech(mezzID=local_storage.mezzControllerID, expect_value=verify.DriveTechnology, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'boot'):
                            VerifyServerProfileTemplate.verify_logical_jbod_boot(mezzID=local_storage.mezzControllerID, expect_value=verify.boot, drivename=verify.name, timeout=10, fail_if_false=True)

                else:
                    msg = "Test data failed, please ensure the 'Verify' node exists and its sub-node is not null in LogicalJBODs"
                    ui_lib.fail_test(msg)

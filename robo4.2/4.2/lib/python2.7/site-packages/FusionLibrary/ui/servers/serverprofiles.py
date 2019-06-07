# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
""" Fusion Server Profile UI page. """

import types
import os
import json
from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.business_logic.general.dashboard_elements import FusionDashboardPage
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.business_logic.general.activity_elements import FusionActivityPage
from FusionLibrary.ui.servers.serverprofiles_elements import FusionServerProfilesPage, ProfileContainer, ProfileContainerType, VolumeTypes
from FusionLibrary.ui.servers import serverhardware
from FusionLibrary.ui.servers.serverhardware_elements import FusionServerHardwarePage
from FusionLibrary.ui.business_logic.servers.serverprofiles import CommonOperationServerProfile
from FusionLibrary.ui.business_logic.servers.serverprofiles import CreateServerProfile
from FusionLibrary.ui.business_logic.servers.serverprofiles import EditServerProfile
from FusionLibrary.ui.business_logic.servers.serverprofiles import CopyServerProfile
from FusionLibrary.ui.business_logic.servers.serverprofiles import VerifyServerProfile
from FusionLibrary.ui.business_logic.servers.serverprofiles import DeleteServerProfile
from FusionLibrary.ui.business_logic.servers.serverprofiles import PowerOnServerProfile
from FusionLibrary.ui.business_logic.servers.serverprofiles import PowerOffServerProfile
from FusionLibrary.ui.business_logic.servers.serverprofiles import ResetServerProfile
from FusionLibrary.ui.business_logic.servers.serverprofiles_elements import GeneralServerProfilesElements
from FusionLibrary.ui.business_logic.servers.serverhardware import CommonOperationServerHardware
from FusionLibrary.ui.business_logic.servers.serverhardware import VerifyHardware
from FusionLibrary.ui.business_logic.base import FusionUIBase
from FusionLibrary.ui.business_logic.base import SectionType
from FusionLibrary.api.security.login_sessions import LoginSession
from FusionLibrary.api.storage.storage_volumes import StorageVolume
from FusionLibrary.api.storage.storage_pools import StoragePool
from FusionLibrary.ui.business_logic.base import FusionUIBase, SectionType
import time
import sys
from datetime import datetime
from FusionLibrary.ui.business_logic.base import TimeoutChecker


if os.name == 'nt':
    from win32api import keybd_event  # pylint: disable=E0401
    import win32con  # pylint: disable=E0401

editProfileTimeout = 60 * 15     # Need minimum 10 minute timeout for Intelligent Provisioning to complete
verifyProfileTimeout = 60

# Constants for Boot Settings
XML_PROFILE_ATTRIBUTE_BOOT_ORDER = "bootorder"
CONSTANT_LEGACY_BIOS = "Legacy BIOS"
CONSTANT_UEFI = "UEFI"
CONSTANT_UEFI_OPTIMIZED = "UEFI optimized"
XML_MANAGE_BOOT_MODE_ATTRIBUTE = "manageBoot"
XML_BOOT_MODE_ATTRIBUTE = "bootMode"
XML_MANAGE_BOOT_ORDER_ATTRIBUTE = "manageBootOrder"
XML_PRIMARY_BOOT_DEVICE = "primaryBootDevice"
XML_BOOT_POLICY_ATTRIBUTE = "bootPolicy"
PROFILE_BOOT_POLICY_LIST = ["Auto", "IPv4 only", "IPv6 only", "IPv4 then IPv6", "IPv6 then IPv4"]
PROFILE_PRIMARY_BOOT_DEVICE_LIST = ["Hard disk", "PXE"]
XML_BOOLEAN_LIST = ["true", "false"]
PROFILE_BOOT_MODE_LIST = [CONSTANT_LEGACY_BIOS, CONSTANT_UEFI, CONSTANT_UEFI_OPTIMIZED]


def navigate():
    """ Navigate to page """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES)


def _verify_profile_status(profile_obj, timeout_sec=30):
    """ verify the profile status """
    # 1. wait changing icon appear
    if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_ITEM_STATUS_CHANGING % profile_obj.name, timeout=10) is False:
        logger._warn("State changing icon not show up")
        return None
    # 2. wait changing icon disappear
    if ui_lib.wait_for_element_notvisible(FusionServerProfilesPage.ID_ITEM_STATUS_CHANGING % profile_obj.name, timeout=timeout_sec) is False:
        logger._warn("State changing icon not disappear")
        return None
    # 3. get profile status, return status string
    time.sleep(5)
    s2l = ui_lib.get_s2l()
    state = s2l.get_text(FusionServerProfilesPage.ID_ITEM_NAME % profile_obj.name)

    return state


def edit_server_profile_for_dl(profile_obj):
    # This keyword is deprecated, please do not use.
    """ Create Server Profile For DL

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
        data/servers/dlserver -> @{TestData.servers.DLServers}
        <servers>
            <DLServers>
                <server name="wpstdl19-ilo" server="wpstdl19-ilo.vse.rdlabs.hpecorp.net" iloIP="wpstdl19-ilo.vse.rdlabs.hpecorp.net" iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Managed" Licensing="HP OneView Advanced" force="true" />
                <server name="wpstdl39-ilo" server="wpstdl39-ilo.vse.rdlabs.hpecorp.net" iloIP="wpstdl39-ilo.vse.rdlabs.hpecorp.net" iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Managed" Licensing="HP OneView Advanced" force="true" />
            </DLServers>
        </servers>

        or:

        data/servers -> @{TestData.servers}
        <servers>
            <server name="wpstdl19-ilo" server="wpstdl19-ilo.vse.rdlabs.hpecorp.net" iloIP="wpstdl19-ilo.vse.rdlabs.hpecorp.net" iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Managed" Licensing="HP OneView Advanced" force="true" />
            <server name="wpstdl39-ilo" server="wpstdl39-ilo.vse.rdlabs.hpecorp.net" iloIP="wpstdl39-ilo.vse.rdlabs.hpecorp.net" iloUserName="Administrator" iloPassword="hpvse1-ilo" mgmtType="Managed" Licensing="HP OneView Advanced" force="true" />
        </servers>

    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    total = len(profile_obj)
    not_exists = 0
    edited = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))

        logger.info("editing a server profile with name '%s' ..." % profile.name)
        if not VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' does not exist" % profile.name)
            not_exists += 1
            continue
        # - Prep the auto_power_off switch
        # - By default, this keyword will power off the server if it's powered on -- unless the attribute 'auto_power_off' is explicitly set to 'false'
        auto_power_off = False if getattr(profile, 'auto_power_off', '').lower() == 'false' else True
        # open Edit SP dialog and enter data ...
        CommonOperationServerProfile.click_server_profile(profile.name)
        EditServerProfile.select_action_edit()
        EditServerProfile.wait_edit_server_profile_dialog_shown()

        EditServerProfile.input_name(profile.newName)
        EditServerProfile.input_description(profile.desc)
        # Input 'Server hardware'
        # - input server name,
        # - select option from the popped out drop-down list,
        # - verify the server hardware is refreshed to the type name displayed in the drop-down list for selecting server hardware
        if not EditServerProfile.input_select_server_hardware(profile.server, auto_power_off=auto_power_off):
            logger.warn("server hardware '%s' is not selected for editing server profile, may be wrong name, or powered on but failed to power it off. "
                        "test will skip this profile '%s' and continue to edit other server profiles" % (profile.server, profile.name))
            continue
        msg = EditServerProfile.get_error_message_from_server_hardware()
        if msg is not None:
            logger.warn("error occurred, server profile can not be edited successfully")
            ui_lib.fail_test(msg)
        sht_selected = EditServerProfile.get_selected_server_hardware_type(profile.server)
        if profile.hardwaretype not in sht_selected:
            logger.warn("the server hardware type of server '%s' is NOT consistent with test data '%s'" % (sht_selected, profile.hardwaretype))
        # set boot mode if attribute 'manageBootMode' is true - only for Gen 9 (or later) server:
        FusionUIBase.select_view_by_name('Boot Settings')
        if 'gen9' in sht_selected.lower():
            logger.info("setting 'Boot mode' for Gen 9 specially ...")
            if getattr(profile, 'manageBootMode', '').lower() == 'true':
                CommonOperationServerProfile.BootSettings.tick_manage_boot_mode()
                CommonOperationServerProfile.BootSettings.select_boot_mode_by_text(profile.bootMode) if hasattr(profile, 'bootMode') else None
                if getattr(profile, 'bootMode', '').lower() == 'legacy bios':
                    CommonOperationServerProfile.BootSettings.set_legacy_bios_mode_boot_order(profile)
                else:
                    CommonOperationServerProfile.BootSettings.set_non_legacy_bios_mode_boot_order(profile, hardware_type=sht_selected)
            else:
                CommonOperationServerProfile.BootSettings.untick_manage_boot_mode()
        else:
            CommonOperationServerProfile.BootSettings.set_legacy_bios_mode_boot_order(profile)

        EditServerProfile.click_ok_button()
        # if EditServerProfile.get_error_message_from_boot_mode() is not None:
        if CommonOperationServerProfile.BootSettings.get_error_message_from_boot_mode() is not None:
            logger.warn("test data may be wrongly defined for 'Boot mode', which caused an error that blocks profile being edited. "
                        "Test will skip this profile '%s' and continue to edit other server profiles" % profile.name)
            continue

        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
        if status is True:
            logger.warn("unexpected error occurred: %s" % msg)
            ui_lib.fail_test(msg)

        EditServerProfile.wait_edit_server_profile_dialog_disappear(timeout=180)
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(profile.newName, 'Update', timeout=300, fail_if_false=False)
        FusionUIBase.show_activity_sidebar()
        CommonOperationServerProfile.wait_server_profile_status_ok(profile.newName, timeout=180, fail_if_false=False)
        logger.info("edited server profile '%s' successfully" % profile.newName)
        edited += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no server profile to edit! all %s server profile(s) is NOT existing, hence test is considered PASS" % not_exists)
        return True
    else:
        if edited < total:
            logger.warn("not all of the server profile(s) is successfully edited - %s out of %s edited " % (edited, total))
            if edited + not_exists == total:
                logger.warn("%s non-existing server profile(s) is skipped being edited, hence test is considered PASS" % not_exists)
                return True
            else:
                logger.warn("%s non-existing server profile(s) is skipped being edited, but %s profile(s) left is failed being edited " % (not_exists, total - edited - not_exists))
                return False

    logger.info("all of the server profile(s) is successfully edited - %s out of %s " % (edited, total))
    return True


def create_server_profile(profile_obj):
    """ Create Server Profile For BL/DL

    Arguments:
      name*             --  Name of server hardware as a string.
      desc              --  description of the iLO of this server profile.
      server*           --  server hardware name of the server for which this profile is about to be created.
      hardwareType*     --  server hardware type of the server, will be used to verify the selected server's SHT is correct.
                            This should be the 'DL380p Gen8' instead of 'DL380p Gen8 1/2' to avoid the mismatching due to Fusion's SHT identifying mechanism.
      for_server        --  to get server hardware type by the server hardware name when server is unassigned.
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
                        <BIOSSettings manageBIOSsettings="true" bios_schema_path='../../../Tools/bios_schema/gen8/'>
                            <Edit server_type="BL465c Gen8">
                                <setting name="Embedded Serial Port" option="COM 1; IRQ4; I/O: 3F8h-3FFh"/>
                                <setting name="Processor Core Disable (AMD Core Select)" option="4"/>
                                <setting name="Custom POST Message" option="Custom POST Message"/>
                            </Edit>
                        </BIOSSettings>
                        <Advanced mac="Physical" wwn="Physical" serial="Physical" HideUnusedFlexNICs="Yes"><None/></Advanced>
                    </profile>
                </Create>
                <Edit><profiles to edit, or None node as '<None/>'/></Edit>
                <Delete><profiles to delete, or None node as '<None/>'/></Delete>
            </BLServerProfiles>
        </servers>

    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    total = len(profile_obj)
    created = 0
    already_exists = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("creating a server profile with name '%s' ..." % profile.name)
        # checking if the profile is already existing
        if not VerifyServerProfile.verify_server_profile_not_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' already exists" % profile.name)
            already_exists += 1
            continue
        # - Prep the auto_power_off switch
        # - By default, this keyword will power off the server if it's powered on -- unless the attribute 'auto_power_off' is explicitly set to 'false'
        auto_power_off = False if getattr(profile, 'auto_power_off', '').lower() == 'false' else True
        # open Create SP dialog and enter data ...
        CreateServerProfile.click_create_profile_button()
        CreateServerProfile.wait_create_server_profile_dialog_shown()

        CreateServerProfile.input_name(profile.name)
        CreateServerProfile.input_select_server_profile_template(profile.prof_temp)
        CreateServerProfile.input_description(getattr(profile, 'desc', ''))
        # Input 'Server hardware'
        # - input server name,
        # - select option from the popped out drop-down list,
        # - power off the server if the it is powered on,
        # - verify the server hardware type of the selected one is refreshed to the type name displayed in the drop-down list
        #     for selecting server hardware
        if not CreateServerProfile.input_select_server_hardware(profile.server, auto_power_off=auto_power_off):
            logger.warn("server hardware '%s' is not selected for creating server profile, may be wrong name, or powered on but failed to power it off. "
                        "test will skip this profile '%s' and continue to create other server profiles" % (profile.server, profile.name))
            continue
        msg = CreateServerProfile.get_error_message_from_server_hardware()
        if msg is not None:
            logger.warn("error occurred, server profile can not be created successfully: \n<%s>" % msg)
            ui_lib.fail_test(msg)
        # input 'Server hardware type', 'Enclosure group'
        # TODO: update Edit Server Profile as well
        if profile.server != 'unassigned':
            # verify if 'Server hardware type' is automatically set by selecting 'Server hardware'
            sht_selected = CreateServerProfile.get_selected_server_hardware_type(profile.server)
            if sht_selected == '':
                logger.info("'server hardware type' is not selected, select it with name '%s'" % profile.hardwareType)
                CreateServerProfile.input_select_server_hardware_type(profile.hardwareType)
                CreateServerProfile.input_select_enclosure_group(profile.enclgroup) if getattr(profile, 'enclgroup', None) is not None else None
                sht_selected = CreateServerProfile.get_selected_server_hardware_type(profile.server)
            elif profile.hardwareType not in sht_selected:
                msg = "selected server hardware type '%s' of server '%s' is NOT consistent with test data '%s'" % (sht_selected, profile.server, profile.hardwareType)
                logger.warn(msg)
                ui_lib.fail_test(msg)
        else:
            # input 'Enclosure group'
            if hasattr(profile, 'for_server'):
                hardware_type = FusionUIBase.APIMethods().get_server_hardware_type_by_server_hardware_name(profile.for_server)
                logger.info('For server attribute is %s, hardware type is %s' % (profile.for_server, hardware_type))
                CreateServerProfile.input_select_server_hardware_type(hardware_type)
            else:
                CreateServerProfile.input_select_server_hardware_type(profile.hardwareType)
            CreateServerProfile.input_select_enclosure_group(profile.enclgroup) if getattr(profile, 'enclgroup', None) is not None else None
            sht_selected = CreateServerProfile.get_selected_server_hardware_type(profile.server)
        # input 'Affinity' for BL server, or when 'server hardware' == 'unassigned'
        if getattr(profile, 'hardwareType', None) is not None:
            hardware_type = profile.hardwareType

        if str(hardware_type)[:2:] == 'BL' or profile.server == 'unassigned':
            if getattr(profile, 'Affinity', None) is not None:
                logger.info("test data for 'Affinity' is found: <%s>, start setting Affinity ..." % profile.Affinity)
                CreateServerProfile.select_affinity_by_text(profile.Affinity)

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
        if getattr(profile, 'BIOSSettings', None) is not None:
            logger.debug("test data for 'BIOS Settings' is found: <%s>" % profile.BIOSSettings, also_console=False)
            logger.info("test data for 'BIOS Settings' is found, start setting its options ...")
            CommonOperationServerProfile.BIOSSettings.set(profile.BIOSSettings)

        if getattr(profile, 'Advanced', None) is not None:
            logger.debug("test data for 'Advanced' is found: <%s>" % profile.Advanced, also_console=False)
            logger.info("test data for 'Advanced' is found, start setting its options ...")
            # select "MAC/WWN/Serial/Hide unused FlexNICs" radio box
            CreateServerProfile.Advanced.set(profile)

        CreateServerProfile.click_create_button()
        if CommonOperationServerProfile.BootSettings.get_error_message_from_boot_mode() is not None:
            logger.warn("test data of server profile '%s' may be wrongly defined for 'Boot mode', which caused an error that blocks profile being created. "
                        "test will skip this profile and continue to create other server profiles" % profile.name)
            continue

        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
        if status is True:
            if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_DIALOG_CREATE_PROFILE_ERROR_WARNING, PerfConstants.WAIT_UNTIL_CONSTANT):
                logger._warn("Profile %s will create with server hardware has health status as WARNING" % profile.name)
                CreateServerProfile.click_create_button()
            else:
                logger.warn("unexpected error occurred: %s" % msg)
                ui_lib.fail_test(msg)

        if CreateServerProfile.wait_create_server_profile_dialog_disappear(timeout=180, fail_if_false=False) is True:
            if getattr(profile, 'wait_complete', "True").lower() != "false":
                FusionUIBase.show_activity_sidebar()
                timeout = int(getattr(profile, 'timeout', "3600"))
                if FusionUIBase.wait_activity_action_ok(profile.name, 'Create', timeout=timeout, fail_if_false=False) is True:
                    FusionUIBase.show_activity_sidebar()
                    if CommonOperationServerProfile.wait_server_profile_status_ok_or_warn(profile.name, timeout=180, fail_if_false=False) is True:
                        logger.info("created server profile '%s' successfully" % profile.name)
                        created += 1
                    else:
                        logger.warn("'wait_server_profile_status_ok_or_warn' = FALSE, skip to next profile ... ")
                        continue
                else:
                    logger.warn("'wait_activity_action_ok' = FALSE, skip to next profile ... ")
                    FusionUIBase.show_activity_sidebar()
                    continue
            else:
                logger.info("created server profile '%s' successfully but no need to wait for task complete" % profile.name)
                created += 1
        else:
            logger.warn("'wait_create_server_profile_dialog_disappear' = FALSE, skip to next profile ... ")
            CreateServerProfile.click_cancel_button()
            continue

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
                ui_lib.fail_test("%s already existing server profile(s) is skipped, %s profile(s) left is failed being created " % (already_exists, total - created - already_exists))

    logger.info("all of the server profile(s) is successfully created - %s out of %s " % (created, total))
    return True


def create_simple_server_profile_by_server_hardware(profile_name, server_name, return_true_if_exists=False):
    """
    Create Simple Server Profile By Server Hardware
    Date:   2015-07-28
            This is to create a simplest server profile by clicking 'Create profile' link from Server Hardware page,
            entering the least fields (only 'Name', 'Boot mode' maybe), powering off the server hardware if needed, then clicking Create button directly.
            The purpose is for some tests needs that server profile is needed and related to the tested resource like server hardware/server hardware type/volume/enclosure group, etc.
    :param profile_name:
    :type profile_name:
    :param server_name:
    :type server_name:
    :param description:
    :type description:
    :return:
    :rtype:
    """
    logger.info("--> creating a server profile with name '%s' ..." % profile_name)
    # checking if the profile is already existing
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
    if VerifyServerProfile.verify_server_profile_not_exist(profile_name, fail_if_false=False) is False:
        logger.warn("server profile '%s' already exists" % profile_name)
        return return_true_if_exists

    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE, time_for_loading=5)
    if VerifyHardware.verify_server_hardware_exist(server_name=server_name, fail_if_false=False) is False:
        logger.warn("server hardware '%s' does not exist" % server_name)
        return False

    CommonOperationServerHardware.click_server_hardware(server_name=server_name, timeout=5, time_for_loading=5)
    FusionUIBase.select_view_by_name(view_name='Hardware', timeout=5, fail_if_false=False)
    if VerifyHardware.is_create_profile_link_available() is False:
        logger.warn("server hardware '%s' does NOT have 'Create profile' link to perform creating profile" % server_name)
        return False

    CommonOperationServerHardware.click_create_profile_link(server_name=server_name)
    CreateServerProfile.wait_create_server_profile_dialog_shown()

    CreateServerProfile.input_name(name=profile_name)
    # CreateServerProfile.input_description(description=description)

    if VerifyServerProfile.is_power_on_error_visible_when_create_server_profile(server_name=server_name, timeout=5, fail_if_false=False) is True:
        if CreateServerProfile.click_power_off_link_from_powered_on_error(server_name=server_name, timeout=5, fail_if_false=False) is False:
            logger.warn("server hardware '%s' is powered on but failed to power it off, creating simple server profile will FAIL" % server_name)
            return False

    msg = CreateServerProfile.get_error_message_from_server_hardware()
    if msg is not None:
        logger.warn("error occurred, server profile can not be created successfully: \n<%s>" % msg)
        ui_lib.fail_test(msg)

    sht_selected = CreateServerProfile.get_selected_server_hardware_type(server_name)

    if sht_selected[:2:] == 'BL':
        # maybe other needs according to SHT in the future
        pass

    CreateServerProfile.click_create_button()
    err_msg_boot_mode = CommonOperationServerProfile.BootSettings.get_error_message_from_boot_mode()
    if err_msg_boot_mode is not None:
        logger.warn("error message: ['%s'] when creating profile '%s'" % (err_msg_boot_mode, profile_name))
        if 'select a boot mode' in err_msg_boot_mode.strip().lower():
            logger.debug("trying to set 'Boot mode' as 'Legacy BIOS' to remove this error message ...")
            CommonOperationServerProfile.BootSettings.select_boot_mode_legacy_bios()
            CreateServerProfile.click_create_button()
        else:
            logger.warn("unknown error message, cannot continue to create simple server profile")
            return False

    status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
    if status is True:
        logger.warn("unexpected error occurred: %s" % msg)
        return False
        # ui_lib.fail_test(msg)

    if CreateServerProfile.wait_create_server_profile_dialog_disappear(timeout=180) is False:
        return False
    FusionUIBase.show_activity_sidebar()
    if FusionUIBase.wait_activity_action_ok(profile_name, 'Create', timeout=720, fail_if_false=True) is False:
        return False
    FusionUIBase.show_activity_sidebar()
    if CommonOperationServerProfile.wait_server_profile_status_ok(profile_name, timeout=180, fail_if_false=True) is False:
        return False
    logger.info("created simple server profile '%s' successfully" % profile_name)
    return True


def create_server_profile_monitored_bays_should_not_show_in_list(server_blade_bays):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
    profile_name = 'test_profile_%s' % time.strftime('%Y%m%d%H%M%S')
    logger.info("creating a server profile with name '%s' ..." % profile_name)
    # checking if the profile is already existing
    profile_exist = True
    while profile_exist is True:
        if not VerifyServerProfile.verify_server_profile_not_exist(profile_name, fail_if_false=False):
            profile_name_old = profile_name
            profile_name = 'test_profile_%s' % time.strftime('%Y%m%d%H%M%S')
            logger.warn("server profile '%s' already exists, generating another name %s" % (profile_name_old, profile_name))
        else:
            profile_exist = False
    # open Create SP dialog and input data ...
    CreateServerProfile.click_create_profile_button()
    CreateServerProfile.wait_create_server_profile_dialog_shown()
    CreateServerProfile.input_name(profile_name)
    CreateServerProfile.input_description("create_server_profile_monitored_bay_should_not_shows_in_list")
    CreateServerProfile.click_server_hardware_search_combo()
    CreateServerProfile.wait_server_hardware_visible("unassigned")
    unexpected_count = 0
    for bay in server_blade_bays:
        if not CreateServerProfile.wait_server_hardware_not_visible(bay.name, fail_if_false=False):
            logger.warn("Server hardware '%s' is visible in drop down list that not as expected" % bay.name)
            unexpected_count += 1
        else:
            logger.info("Server hardware '%s' is invisible as expected" % bay.name)
    CreateServerProfile.click_server_hardware_search_combo()
    CreateServerProfile.click_cancel_button()
    CreateServerProfile.wait_create_server_profile_dialog_disappear()
    if unexpected_count == 0:
        return True
    else:
        return False


def bak_create_server_profile(*profile_obj):
    """ Create Server Profile    """
    selenium2lib = ui_lib.get_s2l()
    failed_times = 0
    flag = None
    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    for profile in profile_obj:
        logger._log_to_console_and_log_file("\nCreating Server Profile %s..." % profile.name)

        # Check if already exists
        profile_list = [el.text for el in selenium2lib._element_find(FusionServerProfilesPage.ID_PROFILE_LIST_NAMES, False, False)]
        if profile.name in profile_list:
            ui_lib.fail_test("Profile '%s' already exists. Cannot proceed with profile creation" % profile.name)

        # Check for required fields
        if profile.name == "" or profile.server == "":
            logger._warn("Mandatory fields for adding server profile can't be empty")
            selenium2lib.capture_page_screenshot()
            failed_times = failed_times + 1
            continue
        # Checking server power status
        serverhardware_list = []
        if profile.server != "unassigned":
            if not selenium2lib._is_element_present(FusionServerHardwarePage.ID_PAGE_LABEL):
                base_page.navigate_base(FusionServerHardwarePage.ID_PAGE_LABEL,
                                        FusionUIBaseElements.ID_MENU_LINK_SERVER_HARDWARE, "css=span.hp-page-item-count")
                serverhardware_list = [sh.text for sh in selenium2lib._element_find("//table[@id='DataTables_Table_1']/tbody/tr/td[2]", False, False)]
                if profile.server in serverhardware_list:
                    if not serverhardware.power_off_server_by_name(profile.server):
                        logger._warn("Failed to powerOff the server %s" % profile.server)
                        logger._warn("Can't proceed with server profile creation on server %s" % profile.server)
                        selenium2lib.capture_page_screenshot()
                        failed_times = failed_times + 1
                        navigate()
                        continue
                navigate()

        # logger._log_to_console_and_log_file("Creating Server Profile %s" % profile.name)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_CREATE_SERVER_PROFILES)
        ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_INPUT_SERVER_PROFILE_NAME)
        logger._log_to_console_and_log_file("Typing profile name..")
        ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_SERVER_PROFILE_NAME, profile.name)
        if profile.has_property("profile"):
            logger._log_to_console_and_log_file("Typing profile description..")
            ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_INPUT_SERVER_PROFILE_DESCRIPTION)
            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_SERVER_PROFILE_DESCRIPTION, profile.profile)

        # Select hardware
        logger._log_to_console_and_log_file("Selecting Hardware..")
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_SERVER_HARDWARE_DROPDOWN)
        if selenium2lib._is_element_present(FusionServerProfilesPage.ID_LINK_SEARCH_FOR_ANOTHER):
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_SEARCH_FOR_ANOTHER)
        logger._log_to_console_and_log_file("Creating profile for %s" % profile.server)
        if ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % profile.server):
            logger._log_to_console_and_log_file("Selected valid server hardware")
        else:
            logger._log_to_console_and_log_file("Please pass valid server hardware")

        # Check for server hardware
        if profile.server == "unassigned" or profile.server not in serverhardware_list:
            # Select Server Hardware Type and Enclosure Group
            if not hasattr(profile, "hardwaretype") or profile.hardwaretype == "" or profile.enclgroup == "":
                logger._warn("Mandatory fields (hardwaretype, enclgroup) for unassigned profiles can't be empty")
                selenium2lib.capture_page_screenshot()
                failed_times = failed_times + 1
                logger._log_to_console_and_log_file("Select server profile Cancel button")
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_SERVER_PROFILE)
                continue
            else:
                # Select hardware type and enclosure group for unassigned profiles
                logger._log_to_console_and_log_file("No server hardware for unassigned profile")
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_SERVER_HARDWARE_TYPE_DROPDOWN)
                if ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % profile.hardwaretype):
                    logger._log_to_console_and_log_file("Selected valid hardware type")
                else:
                    logger._warn("Please provide valid hardware")
                    selenium2lib.capture_page_screenshot()
                    return False
                if profile.server == "unassigned":
                    logger._log_to_console_and_log_file("Selecting enclosure group for unassigned profile")
                    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_ENCLOSURE_GROUP_DROPDOWN)
                    # if ui_lib.wait_for_element_and_click("//li[@id='cic-profile-panel-add-basic']/fieldset/ol/li[4]/div/div/div[3]/ol[2]/li/span[text()='%s']" % profile.enclgroup):
                    if ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % profile.enclgroup):
                        logger._log_to_console_and_log_file("Selected valid Enclosure Group")
                    else:
                        logger._warn("Invalid Enclosure Group")
                        selenium2lib.capture_page_screenshot()
                        return False
        else:
            # Verify Server Hardware Type
            if hasattr(profile, 'hardwaretype') and profile.hardwaretype:
                logger._log_to_console_and_log_file("Verify server hardware type: %s" % profile.hardwaretype)
                if not ui_lib.wait_for_element_text("//label[@id='cic-profile-add-server-type']", profile.hardwaretype):
                    logger._warn("Failed to verify Server Hardware Type.")
                    selenium2lib.capture_page_screenshot()
                    return False
            else:
                logger._log_to_console_and_log_file("No hardware type, not verifying")
            # Verify Enclosure Group
            logger._log_to_console_and_log_file("Verify enclosure group: %s" % profile.enclgroup)
            if not ui_lib.wait_for_element_text("//label[@id='cic-profile-add-enclosure-group']", profile.enclgroup):
                logger._warn("Failed to verify Enclosure Group.")
                selenium2lib.capture_page_screenshot()
                return False

        # Selecting the Affinity
        if profile.has_property("affinity") and profile.affinity != "":
            logger._log_to_console_and_log_file("Selecting affinity..")
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_AFFINITY_DROP_DOWN)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_AFFINITY_DROP_DOWN_SELECT % profile.affinity)
            selectedAF = selenium2lib.get_text(FusionServerProfilesPage.ID_AFFINITY_DROP_DOWN)
            logger._log_to_console_and_log_file("Selected affinity is %s " % selectedAF)
            if not selectedAF == profile.affinity:
                logger._warn("Failed to select affinity..")
                selenium2lib.capture_page_screenshot()
                failed_times = failed_times + 1

        # Adding firmware baseline
        if profile.has_property("manageFirmware") and profile.manageFirmware == "true":
            logger._log_to_console_and_log_file("Selecting firmware baseline..")
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_FIRMWARE_BASELINE)
            firmwareListObj = FusionServerProfilesPage.ID_COMBO_FIRMWARE_BASELINE_LIST % profile.spp.strip()
            selenium2lib.mouse_over(firmwareListObj)
            selenium2lib.mouse_down(firmwareListObj)
            selenium2lib.mouse_up(firmwareListObj)
            selectedFW = selenium2lib.get_text(FusionServerProfilesPage.ID_COMBO_FIRMWARE_BASELINE)
            logger._log_to_console_and_log_file("Selected firmware is %s " % selectedFW)
            if not selectedFW == profile.spp.strip():
                logger._warn("Failed to select prefered firmware bundle..")
                selenium2lib.capture_page_screenshot()
                failed_times = failed_times + 1

        if profile.has_property("connection") and len(profile.connection) > 0:
            # Adding network connections
            for connection in profile.connection:
                if connection.band == "" or connection.network == "":
                    logger._warn("Mandatory fields for adding profile connections can't be empty")
                    selenium2lib.capture_page_screenshot()
                    failed_times = failed_times + 1
                    continue
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_MENU_VIEW, fail_if_false=True)
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_CONNECTIONS,
                                                  PerfConstants.DEFAULT_SYNC_TIME, fail_if_false=True)
                FusionUIBase.scroll_element_into_viewpoint(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_CONNECTION)
                ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_CONNECTION,
                                                PerfConstants.DEFAULT_SYNC_TIME, fail_if_false=True)
                ui_lib.wait_for_element(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_CONNECTION,
                                        PerfConstants.DEFAULT_SYNC_TIME, fail_if_false=True)
                # ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_CONNECTION)
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_CONNECTION, fail_if_false=True)
                ui_lib.wait_for_element(FusionServerProfilesPage.ID_COMBO_FUNCTION_TYPE, 120, fail_if_false=True)
                if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_COMBO_FUNCTION_TYPE):
                    logger.warn("Failed to load add network connections page..")
                    selenium2lib.capture_page_screenshot()
                    failed_times += 1
                    continue
                logger.info("Adding network : %s to profile " % connection.network)
                # ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_DEVICE_TYPE)
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_FUNCTION_TYPE)
                label = selenium2lib.get_text(FusionServerProfilesPage.ID_COMBO_FUNCTION_TYPE)

                # Flag to check any errors occurred at the time of adding connections
                flag = 0
                # Adding FC connection
                if connection.has_property("type") and (connection.type.upper() == "FIBRE CHANNEL" or connection.type.upper() == "FIBRECHANNEL"):
                    selenium2lib.press_key(FusionServerProfilesPage.ID_COMBO_FUNCTION_TYPE, 'Fibre' + chr(13))
                    # type name
                    ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_CONNECTION_NAME, connection.name)
                    if not _add_profile_connections(connection):
                        logger._warn("Failed to add %s connection to profile" % connection.network)
                        selenium2lib.capture_page_screenshot()
                        failed_times = failed_times + 1
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_NETWORK_ADD_CONNECTION)
                        flag = 1
                        break
                    if connection.has_property('boot') and (connection.boot == 'Primary' or connection.boot == 'Secondary'):
                        if connection.has_property('targetwwpn') and connection.has_property('targetlun') and connection.targetwwpn != "" and connection.targetlun != "":
                            logger._log_to_console_and_log_file("Specifying boot target ...")
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_SPECIFIY_BOOT_TARGET)
                            if connection.targetwwpn == "" or connection.targetlun == "":
                                logger._warn("Please provide valid target WWPN and LUN")
                                selenium2lib.capture_page_screenshot()
                                failed_times = failed_times + 1
                                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_NETWORK_ADD_CONNECTION)
                                flag = 1
                                break
                            logger._log_to_console_and_log_file("Typing target WWPN...")
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWN_TARGET)
                            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWN_TARGET,
                                                                   connection.targetwwpn)
                            logger._log_to_console_and_log_file("Typing target LUN...")
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_LUN_TARGET)
                            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_LUN_TARGET,
                                                                   connection.targetlun)
                        else:
                            logger._log_to_console_and_log_file("Use bios...")
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_USE_BIOS)

                    if connection.has_property('macaddress') and connection.macaddress != "":
                        logger._log_to_console_and_log_file("Selecting use user specified ids checkbox ...")
                        selenium2lib.select_checkbox(FusionServerProfilesPage.ID_CHKBOX_USER_SPECIFIED_IDS)
                        if connection.wwpn == "" or connection.wwnn == "":
                            logger._warn("Please provide valid WWPN, WWNN and MAC address")
                            selenium2lib.capture_page_screenshot()
                            failed_times = failed_times + 1
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_NETWORK_ADD_CONNECTION)
                            flag = 1
                            break
                        logger._log_to_console_and_log_file("Typing WWPN ...")
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWPN)
                        ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWPN, connection.wwpn)
                        logger._log_to_console_and_log_file("Typing WWNN ...")
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWNN)
                        ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWNN, connection.wwnn)
                        logger._log_to_console_and_log_file("Typing mac address...")
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_MAC)
                        ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_MAC, connection.macaddress)
                    logger._log_to_console_and_log_file("Clicking on network add button...")
                    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_CONNECTON)

                    if selenium2lib._is_element_present(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_PLUS_CONNECTON):
                        logger._warn("Failed to add connection %s to the profile" % connection.network)
                        selenium2lib.capture_page_screenshot()
                        failed_times = failed_times + 1
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_NETWORK_ADD_CONNECTION)
                        flag = 1
                        break
                    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_LINK_ADD_PROFILE_CONNECTIONS_TABLE
                                                            % connection.network):
                        logger._warn("Failed to add connection %s to the profile" % connection.network)
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_NETWORK_ADD_CONNECTION)
                        selenium2lib.capture_page_screenshot()
                        failed_times = failed_times + 1
                        flag = 1
                        break

                elif connection.has_property("type") and (connection.type.upper() == "ETHERNET"):
                    # Adding ethernet connections
                    if not label == "Ethernet":
                        selenium2lib.press_key(FusionServerProfilesPage.ID_COMBO_FUNCTION_TYPE, 'Ethernet' + chr(13))
                    # type name
                    ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_CONNECTION_NAME, connection.name)
                    if not _add_profile_connections(connection):
                        logger._warn(" : Failed to add %s connection to profile" % connection.network)
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_NETWORK_ADD_CONNECTION)
                        selenium2lib.capture_page_screenshot()
                        failed_times = failed_times + 1
                        flag = 1
                        break
                    if connection.has_property("macaddress"):
                        logger._log_to_console_and_log_file("Selecting use user specified ids ...")
                        selenium2lib.select_checkbox(FusionServerProfilesPage.ID_CHKBOX_USER_SPECIFIED_IDS)
                        if connection.macaddress == "":
                            logger._warn("Please provide valid MAC")
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_NETWORK_ADD_CONNECTION)
                            selenium2lib.capture_page_screenshot()
                            failed_times = failed_times + 1
                            flag = 1
                            break
                        logger._log_to_console_and_log_file("Typing mac address...")
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_MAC)
                        ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_MAC, connection.macaddress)

                    logger._log_to_console_and_log_file("Clicking on network add button...")
                    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_CONNECTON)
                    if selenium2lib._is_element_present(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_CONNECTON):
                        logger._warn("Failed to add connection %s to the profile" % connection.network)
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_NETWORK_ADD_CONNECTION)
                        selenium2lib.capture_page_screenshot()
                        failed_times = failed_times + 1
                        flag = 1
                        break
                    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_LINK_ADD_PROFILE_CONNECTIONS_TABLE
                                                            % connection.network):
                        logger._warn("Failed to add connection %s to the profile" % connection.network)
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_NETWORK_ADD_CONNECTION)
                        selenium2lib.capture_page_screenshot()
                        failed_times = failed_times + 1
                        flag = 1
                        break
                else:
                    logger._warn("Please provide valid types for adding connections to profile")
                    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_NETWORK_ADD_CONNECTION)
                    selenium2lib.capture_page_screenshot()
                    failed_times = failed_times + 1
                    flag = 1
                    break

        if flag != 0:
            logger._warn("Canceling the creation of server profile %s" % profile.name)
            selenium2lib.capture_page_screenshot()
            failed_times = failed_times + 1
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_SERVER_PROFILE)
            continue
        # For closing the add connection page and verifying for the table
        if selenium2lib._is_element_present(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_PLUS_CONNECTON):
            logger._log_to_console_and_log_file("Close add connection Page")
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_NETWORK_ADD_CONNECTION)
        if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_LINK_ADD_PROFILE_CONNECTIONS_TABLE
                                                % connection.network):
            logger._warn("Failed to add connection %s to the profile" % connection.network)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_NETWORK_ADD_CONNECTION)
            # Adding storage volumes
        if profile.has_property("sanstorage"):
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_MENU_VIEW, fail_if_false=True)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_SANSTORAGE,
                                              PerfConstants.DEFAULT_SYNC_TIME, fail_if_false=True)
            for sanstorage in profile.sanstorage:
                if sanstorage.san == "true":
                    selenium2lib.select_checkbox(FusionServerProfilesPage.ID_CHKBOX_SAN_STORAGE)
                    logger.info("Setting san storage")
                    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_OS_TYPE_DROP_DOWN, fail_if_false=True)
                    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_OS_TYPE_SELECT % sanstorage.ostype, fail_if_false=True)
                    if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_ERROR_NO_STORAGE_VOLUMES):
                        logger.warn("No storage volumes are available for assigning to the servers")
                        selenium2lib.capture_page_screenshot()
                        failed_times += 1
                    ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_BTN_ADD_STORAGE, fail_if_false=False)
                    selenium2lib.focus(FusionServerProfilesPage.ID_BTN_ADD_STORAGE)
                    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_STORAGE, fail_if_false=True)
                    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_VOLUME_SELECT_DROPDOWN, fail_if_false=True)
                    ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_VOLUME_SELECT % sanstorage.sanvolume, fail_if_false=True)
                    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_VOLUME_SELECT % sanstorage.sanvolume, fail_if_false=True)
                    if not ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_RADIO_BTN_AUTO, fail_if_false=False):
                        logger.warn("No storage volumes were selected at add volume page")
                        selenium2lib.capture_page_screenshot()
                        failed_times += 1
                    if sanstorage.has_property('sanlun') and sanstorage.sanlun != "":
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_BTN_MANUAL)
                        ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_TEXT_LUN, sanstorage.sanlun)
                    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_STORAGE_ADD)
                    if selenium2lib._is_element_present(FusionServerProfilesPage.ID_POP_UP_ERROR):
                        errMsg = selenium2lib._get_text(FusionServerProfilesPage.ID_POP_UP_ERROR)
                        logger.info(errMsg)
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_STORAGE_ADD)
        # Setting boot order
        if 'gen9' not in profile.hardwareType.lower():
            if profile.manageBoot == "true":
                ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_CHKBOX_MANAGE_BOOT, fail_if_false=True)
                selenium2lib.select_checkbox(FusionServerProfilesPage.ID_CHKBOX_MANAGE_BOOT)
                #             if profile.has_property('bootorder') and len(profile.bootorder) > 0:
                #                 logger._log_to_console_and_log_file("Setting boot Order" % profile.bootorder)
                #                 ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_CHKBOX_PROFILE_BOOT_LOADER)
                #                 selenium2lib.select_checkbox(FusionServerProfilesPage.ID_CHKBOX_PROFILE_BOOT_LOADER)

                for index, bootorder in enumerate(profile.bootorder):
                    ui_lib.wait_for_element_and_input_text("name=%s" % bootorder.device, index + 1)
            else:
                ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_CHKBOX_MANAGE_BOOT, fail_if_false=True)
                selenium2lib.unselect_checkbox(FusionServerProfilesPage.ID_CHKBOX_MANAGE_BOOT)
        else:
            ui_lib.wait_for_element_visible("id=cic-profile-add-manage-boot-mode", fail_if_false=True)
            FusionUIBase.scroll_element_into_viewpoint("id=cic-profile-add-manage-boot-mode")
            FusionUIBase.wait_for_checkbox_and_unselect("id=cic-profile-add-manage-boot-mode")

        # Manage BIOS
        if profile.has_property('bios'):
            if len(profile.bios) > 0:
                logger._log_to_console_and_log_file("Editing BIOS settings")
                #                 ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_MENU_VIEW)
                #                 ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_BIOS)
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_MENU_VIEW)
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_BIOS)
                selenium2lib.select_checkbox(FusionServerProfilesPage.ID_CHKBOX_PROFILE_MANAGE_BIOS)

                for bios in profile.bios:
                    if selenium2lib._is_element_present(FusionServerProfilesPage.ID_BTN_EDIT_BIOS):
                        #                         ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_EDIT_BIOS)
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_EDIT_BIOS)
                        _edit_bios_setting(bios.name, bios.value)

        # Add Advanced setup
        if not _select_advanced_options(profile):
            logger._warn("Failed to select advanced options")
            logger._warn("Canceling the creation of server profile %s" % profile.name)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_SERVER_PROFILE)
            selenium2lib.capture_page_screenshot()
            return False
            continue

        # Create server profile
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CREATE_SERVER_PROFILE)
        # selenium2lib.page_should_not_contain("Unable to add profile")
        if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_ADD_PROFILE_NOTIFICATION):
            errMsg = selenium2lib._get_text(FusionServerProfilesPage.ID_ADD_PROFILE_NOTIFICATION_CONTENT)
            logger._warn(errMsg)
            logger._warn("Unable to create server profile %s" % profile.name)
            selenium2lib.capture_page_screenshot()
            failed_times = failed_times + 1
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_SERVER_PROFILE)
            continue

        selenium2lib.wait_until_page_contains_element(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % profile.name,
                                                      PerfConstants.DEFAULT_SYNC_TIME)

        ui_lib.ignore_staleElementRefException("_is_visible", FusionServerProfilesPage.ID_PROFILE_CHANGING)
        logger._log_to_console_and_log_file("Waiting for profile creation to complete..")

        @TimeoutChecker(timeout_sec=300, interval_sec=1)
        def check_op_status():
            """ """
            # wait changing status gone
            if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_ITEM_STATUS_CHANGING % profile.name, timeout=1) is True:
                return False
            if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_ITEM_STATUS_OK % profile.name, timeout=1) is True:
                return True
            elif ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_ITEM_STATUS_ERROR % profile.name, timeout=1) is True:
                return "error"  # exit checker loop
            elif ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_ITEM_STATUS_WARN % profile.name, timeout=1) is True:
                return "warn"  # exit checker loop

            return False  # continue checker loop

        if profile.server == "unassigned":
            logger._log_to_console_and_log_file("Validating unassigned profile %s" % profile.name)

            ret = check_op_status()
            if ret is False:
                logger._log_to_console_and_log_file("Can't create unassigned profile %s in 5 mins " % profile.name)
                failed_times = failed_times + 1
            elif ret is True:
                logger._log_to_console_and_log_file("Unassigned profile created %s successfully" % profile.name)
            elif ret == "error":
                logger._log_to_console_and_log_file("Failed to create unassigned profile %s due to error" % profile.name)
                failed_times = failed_times + 1
            elif ret == "warn":
                logger._log_to_console_and_log_file("Failed to create unassigned profile %s due to warning" % profile.name)
                failed_times = failed_times + 1
            else:
                logger._log_to_console_and_log_file("Failed to create unassigned profile %s due to unexpected errors" % profile.name)
                failed_times = failed_times + 1
        else:
            logger._log_to_console_and_log_file("Validating profile %s" % profile.name)

            ret = check_op_status()
            if ret is False:
                logger._warn("Can't create profile %s in 5 mins " % profile.name)
                failed_times = failed_times + 1
            elif ret is True:
                logger._log_to_console_and_log_file("Profile created %s successfully" % profile.name)
            elif ret == "error":
                logger._warn("Failed to create profile %s due to error" % profile.name)
                failed_times = failed_times + 1
            elif ret == "warn":
                logger._warn("Failed to create profile %s due to warning" % profile.name)
                failed_times = failed_times + 1
            else:
                logger._warn("Failed to create profile %s due to unexpected errors" % profile.name)
                failed_times = failed_times + 1

    if failed_times > 0:
        return False
    else:
        return True


def edit_server_profile(profile_obj):
    """ Edit Server Profile For BL/DL

    Arguments:
      name*             --  Name of server hardware as a string.
      desc              --  description of the iLO of this server profile.
      server*           --  server hardware name of the server for which this profile is about to be created.
      IgnoreWaitForStatusOK    --  case will not be interrupted when server profile's status is not ok after editing.
      hardwareType*     --  server hardware type of the server, will be used to verify the selected server's SHT is correct.
                            This should be the 'DL380p Gen8' instead of 'DL380p Gen8 1/2' to avoid the mismatching due to Fusion's SHT identifying mechanism.
      manageFirmware    --  If setting the firmware baseline when creating this profile (not implemented yet).
      spp               --  SPP name (title displayed on Firmware Bundle page) for setting firmware baseline.
      manageBootMode*   --  Only required if the server is a Gen 9 server, means 'Gen9' in server hardware type string.
      bootMode*         --  Only required if the server is a Gen 9 server, means 'Gen9' in server hardware type string.
      pxeBootPolicy*    --  Only required if the server is a Gen 9 server, and boot mode is not Legacy BIOS.
      manageBootOrder   --  Not yet supported for Gen 9 DL server
      primaryBootDevice --  Not yet supported for Gen 9 DL server, but supported for Gen 9 BL server
      bootorder         --  Not yet supported for Gen 9 DL server with Non-Legacy-BIOS, only supported with Legacy BIOS boot mode
      wait_complete     --  If this parameter is False, do not wait for editing SP task finished


    * Required Arguments

    Example:
        data/servers/BLServerProfiles -> @{TestData.servers.BLServerProfiles.Create}
        <servers>
            <BLServerProfiles>
                <Create>
                    <profile name="SP_wpst23bay3_BL465c_Gen8" desc="SP BL465c Gen8" server="wpst23, bay 3" IgnoreWaitForStatusOK="true" hardwareType="BL465c Gen8" enclgroup="GRP-wpst32">
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
                        <BIOSSettings manageBIOSsettings="true" bios_schema_path='../../../Tools/bios_schema/gen8/'>
                            <Edit server_type="BL465c Gen8">
                                <setting name="Embedded Serial Port" option="COM 1; IRQ4; I/O: 3F8h-3FFh"/>
                                <setting name="Processor Core Disable (AMD Core Select)" option="4"/>
                                <setting name="Custom POST Message" option="Custom POST Message"/>
                            </Edit>
                        </BIOSSettings>
                        <Advanced mac="Physical" wwn="Physical" serial="Physical" HideUnusedFlexNICs="Yes"><None/></Advanced>
                    </profile>
                </Create>
                <Edit><profiles to edit, or None node as '<None/>'/></Edit>
                <Delete><profiles to delete, or None node as '<None/>'/></Delete>
            </BLServerProfiles>
        </servers>

    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    total = len(profile_obj)
    not_exists = 0
    edited = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("editing a server profile with name '%s' ..." % profile.name)
        # checking if the profile is not existing for editing
        if not VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' does not exist" % profile.name)
            not_exists += 1
            continue
        # - Prep the auto_power_off switch
        # - By default, this keyword will power off the server if it's powered on -- unless the attribute 'auto_power_off' is explicitly set to 'false'
        auto_power_off = False if getattr(profile, 'auto_power_off', '').lower() == 'false' else True
        # open Edit SP dialog and enter data ...
        CommonOperationServerProfile.click_server_profile(profile.name)
        # { below 3 lines were to avoid a failure caused by 2 CR that had been fixed. leave the 3 lines here as commented in case regression issue in future
        # will remove below once 2 CRs fixed
        # EditServerProfile.select_action_edit()
        # EditServerProfile.wait_edit_server_profile_dialog_shown()
        # EditServerProfile.click_cancel_button()
        # } here is a workaround for 1st time editing server profile (sp template as well) has defect that,
        # can't close dialog by OK/Cancel button, and SAN Storage's OS Type can't be read correctly,
        # so open dialog and use Cancel button to close, then everything goes well when 2nd time open Edit dialog

        EditServerProfile.select_action_edit()
        EditServerProfile.wait_edit_server_profile_dialog_shown()
        BuiltIn().sleep(2)
        EditServerProfile.input_name(profile.newName) if getattr(profile, 'newName', None) is not None else None
        EditServerProfile.input_description(profile.desc) if getattr(profile, 'desc', None) is not None else None

        sht_selected = EditServerProfile.get_selected_server_hardware_type(profile.server)
        # 20151021 Alex Ma - discussed with Tony/Alex C and get below agreed:
        #       - if 'hardwareType' is defined in test data, then will firstly select/change 'Server hardware type' from UI,
        #             then select/change 'Server hardware' if 'server' is defined in test data
        #       - if 'hardwareType' is not defined in test data, then will only check 'server' attribute to decide if select/change 'Server hardware' from UI
        if getattr(profile, 'hardwareType', None) is not None:
            if profile.hardwareType not in sht_selected:
                logger.warn("server hardware type '%s' of server '%s' is NOT consistent with test data '%s'" % (sht_selected, profile.server, profile.hardwareType))
                EditServerProfile.ChangeServerHardwareTypeAndEnclosureGroup.change_server_hardware_type(profile.hardwareType, timeout=5, fail_if_false=False)
        elif getattr(profile, 'ref_sht_server', None) is not None:
            hardware_type = FusionUIBase.APIMethods().get_server_hardware_type_by_server_hardware_name(profile.ref_sht_server)
            if hardware_type not in sht_selected:
                logger.warn("server hardware type '%s' of server '%s' is NOT consistent with test data '%s'" % (sht_selected, profile.server, hardware_type))
                EditServerProfile.ChangeServerHardwareTypeAndEnclosureGroup.change_server_hardware_type(hardware_type, timeout=5, fail_if_false=False)

        eg_selected = EditServerProfile.get_selected_enclosure_group(profile.server)
        if getattr(profile, 'enclgroup', None) is not None:
            if profile.enclgroup not in eg_selected:
                logger.warn("enclosure group '%s' of server '%s' is NOT consistent with test data '%s'" % (eg_selected, profile.server, profile.enclgroup))
                EditServerProfile.ChangeServerHardwareTypeAndEnclosureGroup.change_enclosure_group(profile.enclgroup, timeout=5, fail_if_false=False)

        # Input 'Server hardware'
        # - input server name,
        # - select option from the popped out drop-down list,
        # - power off the server if the it is powered on,
        # - verify the server hardware type of the selected one is refreshed to the type name displayed in the drop-down list
        #     for selecting server hardware
        if not EditServerProfile.input_select_server_hardware(profile.server, auto_power_off=auto_power_off):
            logger.warn("server hardware '%s' is not selected for editing server profile, may be wrong name, or powered on but failed to power it off. "
                        "test will skip this profile '%s' and continue to edit other server profiles" % (profile.server, profile.name))
            continue
        msg = EditServerProfile.get_error_message_from_server_hardware()
        # if not CreateServerProfile.input_select_server_hardware(profile.server, auto_power_off=auto_power_off):
        #     logger.warn("server hardware '%s' is not selected for creating server profile, may be wrong name, or powered on but failed to power it off. "
        #                 "test will skip this profile '%s' and continue to create other server profiles" % (profile.server, profile.name))
        #     continue
        # msg = CreateServerProfile.get_error_message_from_server_hardware()
        if msg is not None:
            logger.warn("error occurred, server profile can not be edited successfully: \n<%s>" % msg)
            ui_lib.fail_test(msg)

        if getattr(profile, 'Affinity', None) is not None:
            logger.info("test data for 'Affinity' is found: <%s>, start setting Affinity ..." % profile.Affinity)
            EditServerProfile.select_affinity_by_text(profile.Affinity)

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
            BuiltIn().sleep(3)
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
        if getattr(profile, 'BIOSSettings', None) is not None:
            logger.debug("test data for 'BIOS Settings' is found: <%s>" % profile.BIOSSettings, also_console=False)
            logger.info("test data for 'BIOS Settings' is found, start setting its options ...")
            CommonOperationServerProfile.BIOSSettings.set(profile.BIOSSettings)

        if getattr(profile, 'Advanced', None) is not None:
            BuiltIn().sleep(3)
            logger.debug("test data for 'Advanced' is found: <%s>" % profile.Advanced, also_console=False)
            logger.info("test data for 'Advanced' is found, start setting its options ...")
            # select "MAC/WWN/Serial/Hide unused FlexNICs" radio box
            EditServerProfile.Advanced.set(profile)

        EditServerProfile.click_ok_button()
        # logger.debug("sleeping for 8 seconds ...")
        # BuiltIn().sleep(8)
        # if EditServerProfile.get_error_message_from_boot_mode() is not None:
        if CommonOperationServerProfile.BootSettings.get_error_message_from_boot_mode() is not None:
            logger.warn("test data may be wrongly defined for 'Boot mode', which caused an error that blocks profile being created. "
                        "test will skip this profile '%s' and continue to create other server profiles" % profile.name)
            continue

        BuiltIn().sleep(2)
        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
        if status is True:
            logger.warn("unexpected error occurred: %s" % msg)
            ui_lib.fail_test(msg)

        if EditServerProfile.wait_edit_server_profile_dialog_disappear(timeout=300) is True:
            if getattr(profile, 'wait_complete', "True").lower() != "false":
                FusionUIBase.show_activity_sidebar()
                profile_name = profile.newName if getattr(profile, 'newName', None) is not None else profile.name
                timeout = int(getattr(profile, 'timeout', "3600"))
                FusionUIBase.wait_activity_action_ok(profile_name, 'Update', timeout=timeout, fail_if_false=True)
                FusionUIBase.show_activity_sidebar()
                fail_if_not_ok = not getattr(profile, 'IgnoreWaitForStatusOK', '').lower() == 'true'
                # control whether to stop the case when server profile status is not ok.
                CommonOperationServerProfile.wait_server_profile_status_ok(profile_name, timeout=500, fail_if_false=fail_if_not_ok)
                logger.info("edited server profile '%s' successfully" % profile_name)
                edited += 1
            else:
                logger.info("edit server profile '%s' successfully but no need to wait for task complete" % profile.name)
                edited += 1
        else:
            logger.warn("'wait_edit_server_profile_dialog_disappear' = FALSE, skip to next profile ... ")
            EditServerProfile.click_cancel_button()
            continue

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no server profile to edit! all %s server profile(s) is NOT existing, test is considered FAILED" % not_exists)
        return False
    else:
        if edited < total:
            logger.warn("not all of the server profile(s) is successfully edited - %s out of %s edited " % (edited, total))
            if edited + not_exists == total:
                logger.warn("%s not-existing server profile(s) is skipped being edited, test is considered FAILED" % not_exists)
                return False
            else:
                ui_lib.fail_test("%s not-existing server profile(s) is skipped being edited, %s profile(s) left is failed being edited " % (not_exists, total - edited - not_exists))

    logger.info("all of the server profile(s) is successfully edited - %s out of %s " % (edited, total))
    return True


def copy_server_profile(profile_obj):
    """ Copy Server Profile For BL/DL

    Arguments:
      name*             --  Name of server hardware as a string.
      desc              --  description of the iLO of this server profile.
      server*           --  server hardware name of the server for which this profile is about to be created.
      hardwareType*     --  server hardware type of the server, will be used to verify the selected server's SHT is correct.
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
                        <BIOSSettings manageBIOSsettings="true" bios_schema_path='../../../Tools/bios_schema/gen8/'>
                            <Edit server_type="BL465c Gen8">
                                <setting name="Embedded Serial Port" option="COM 1; IRQ4; I/O: 3F8h-3FFh"/>
                                <setting name="Processor Core Disable (AMD Core Select)" option="4"/>
                                <setting name="Custom POST Message" option="Custom POST Message"/>
                            </Edit>
                        </BIOSSettings>
                        <Advanced mac="Physical" wwn="Physical" serial="Physical" HideUnusedFlexNICs="Yes"><None/></Advanced>
                    </profile>
                </Create>
                <Edit><profiles to edit, or None node as '<None/>'/></Edit>
                <Delete><profiles to delete, or None node as '<None/>'/></Delete>
            </BLServerProfiles>
        </servers>

    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=8)

    total = len(profile_obj)
    not_exists = 0
    copied = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("copying a server profile with name '%s' ..." % profile.source)
        # checking if the profile is not existing for editing
        if not VerifyServerProfile.verify_server_profile_exist(profile.source, fail_if_false=False):
            logger.warn("server profile '%s' does not exist" % profile.source)
            not_exists += 1
            continue
        # - Prep the auto_power_off switch
        # - By default, this keyword will power off the server if it's powered on -- unless the attribute 'auto_power_off' is explicitly set to 'false'
        auto_power_off = False if getattr(profile, 'auto_power_off', '').lower() == 'false' else True
        # open Edit SP dialog and enter data ...
        CommonOperationServerProfile.click_server_profile(profile.source)
        CopyServerProfile.select_action_copy()
        CopyServerProfile.wait_copy_server_profile_dialog_shown()
        BuiltIn().sleep(2)
        CopyServerProfile.input_name(profile.name)
        CopyServerProfile.input_description(profile.desc) if getattr(profile, 'desc', None) is not None else None
        # Input 'Server hardware'
        # - input server name,
        # - select option from the popped out drop-down list,
        # - power off the server if the it is powered on,
        # - verify the server hardware type of the selected one is refreshed to the type name displayed in the drop-down list
        #     for selecting server hardware

        if not CopyServerProfile.input_select_server_hardware(profile.server, auto_power_off=auto_power_off):
            logger.warn("server hardware '%s' is not selected for copying server profile, may be wrong name, or powered on but failed to power it off. "
                        "test will skip copying profile '%s' and continue to edit other server profiles" % (profile.server, profile.source))
            continue
        msg = CopyServerProfile.get_error_message_from_server_hardware()
        # if not CreateServerProfile.input_select_server_hardware(profile.server, auto_power_off=auto_power_off):
        #     logger.warn("server hardware '%s' is not selected for creating server profile, may be wrong name, or powered on but failed to power it off. "
        #                 "test will skip this profile '%s' and continue to create other server profiles" % (profile.server, profile.name))
        #     continue
        # msg = CreateServerProfile.get_error_message_from_server_hardware()
        if msg is not None:
            logger.warn("error occurred, server profile can not be copied successfully: \n<%s>" % msg)
            ui_lib.fail_test(msg)

        sht_selected = CopyServerProfile.get_selected_server_hardware_type(profile.server)
        if hasattr(profile, 'hardwareType'):
            hardware_type = profile.hardwareType
        else:
            if hasattr(profile, 'for_server'):
                hardware_type = FusionUIBase.APIMethods().get_server_hardware_type_by_server_hardware_name(profile.for_server)
                logger.info('For server attribute is %s, hardware type is %s' % (profile.for_server, hardware_type))
            else:
                hardware_type = FusionUIBase.APIMethods().get_server_hardware_type_by_server_hardware_name(profile.server)

        if str(hardware_type) not in sht_selected:
            logger.warn("server hardware type '%s' of server '%s' is NOT consistent with test data '%s'" % (sht_selected, profile.server, hardware_type))

        if getattr(profile, 'Affinity', None) is not None:
            logger.info("test data for 'Affinity' is found: <%s>, start setting Affinity ..." % profile.Affinity)
            CopyServerProfile.select_affinity_by_text(profile.Affinity)

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
            BuiltIn().sleep(3)
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
        if getattr(profile, 'BIOSSettings', None) is not None:
            logger.debug("test data for 'BIOS Settings' is found: <%s>" % profile.BIOSSettings, also_console=False)
            logger.info("test data for 'BIOS Settings' is found, start setting its options ...")
            CommonOperationServerProfile.BIOSSettings.set(profile.BIOSSettings)

        if getattr(profile, 'Advanced', None) is not None:
            BuiltIn().sleep(3)
            logger.debug("test data for 'Advanced' is found: <%s>" % profile.Advanced, also_console=False)
            logger.info("test data for 'Advanced' is found, start setting its options ...")
            # select "MAC/WWN/Serial/Hide unused FlexNICs" radio box
            CopyServerProfile.Advanced.set(profile)

        CopyServerProfile.click_create_button()
        # logger.debug("sleeping for 8 seconds ...")
        # BuiltIn().sleep(8)
        # if EditServerProfile.get_error_message_from_boot_mode() is not None:
        if CommonOperationServerProfile.BootSettings.get_error_message_from_boot_mode() is not None:
            logger.warn("test data may be wrongly defined for 'Boot mode', which caused an error that blocks profile being created. "
                        "test will skip this profile '%s' and continue to create other server profiles" % profile.name)
            continue

        BuiltIn().sleep(2)
        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
        if status is True:
            logger.warn("unexpected error occurred: %s" % msg)
            ui_lib.fail_test(msg)

        CopyServerProfile.wait_copy_server_profile_dialog_disappear(timeout=300)
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(profile.name, 'Create', timeout=1800, fail_if_false=True)
        FusionUIBase.show_activity_sidebar()
        CommonOperationServerProfile.wait_server_profile_status_ok(profile.name, timeout=300, fail_if_false=True)
        logger.info("successfully copied server profile '%s' to '%s'" % (profile.source, profile.name))
        copied += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no server profile to copy! all %s server profile(s) is NOT existing, test is considered FAILED" % not_exists)
        return False
    else:
        if copied < total:
            logger.warn("not all of the server profile(s) is successfully copied - %s out of %s copied " % (copied, total))
            if copied + not_exists == total:
                logger.warn("%s not-existing server profile(s) is skipped being copied, test is considered FAILED" % not_exists)
                return False
            else:
                logger.warn("%s not-existing server profile(s) is skipped being copied, %s profile(s) left is failed being copied " % (not_exists, total - copied - not_exists))
                return False

    logger.info("all of the server profile(s) is successfully copied - %s out of %s " % (copied, total))
    return True


def _add_profile_connections(connection):
    """ Add Profile Connections    """
    logger._log_to_console_and_log_file("Selecting network type...")
    selenium2lib = ui_lib.get_s2l()
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_NETWORK_ADD_CONNECTION)
    ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_NETWORK_ADD_CONNECTION, connection.network)
    selenium2lib.press_key(FusionServerProfilesPage.ID_INPUT_NETWORK_ADD_CONNECTION, '\\13')
    logger._log_to_console_and_log_file("Selecting requested band width...")
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_REQUESTED_BW_ADD_CONNECTION)
    if connection.has_property('band'):
        if connection.type.upper() == "FIBRE CHANNEL" or connection.type.upper() == "FIBRECHANNEL":
            if float(connection.band) <= 0 or float(connection.band) > 8:
                logger._warn(" : Failed to add FC Connection to server profile. Required Bandwidth for FC should be in the range 0.1 Gb/s and 10 Gb/s")
                selenium2lib.capture_page_screenshot()
                return False
        else:
            if float(connection.band) <= 0 or float(connection.band) > 10:
                logger._warn(" : Failed to add Ethernet Connection to server profile. \
                Required Bandwidth for Ethernet should be in the range 0.1 Gb/s and 8 Gb/s")
                selenium2lib.capture_page_screenshot()
                return False
        if selenium2lib._is_visible(FusionServerProfilesPage.XP_CREATE_SP_ADD_CONN_BW_DROPDOWN):
            selenium2lib.press_key(FusionServerProfilesPage.XP_CREATE_SP_ADD_CONN_BW_DROPDOWN, connection.band)
            selenium2lib.mouse_down(FusionServerProfilesPage.XP_CREATE_SP_ADD_CONN_BW_DD_SELECT % connection.band)
            selenium2lib.mouse_up(FusionServerProfilesPage.XP_CREATE_SP_ADD_CONN_BW_DD_SELECT % connection.band)
        else:
            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_REQUESTED_BW_ADD_CONNECTION, connection.band)

    logger._log_to_console_and_log_file("Selecting FlexNIC...")
    browser = BuiltIn().get_variable_value("${Browser}")

    if browser.lower() == "chrome":
        logger._log_to_console_and_log_file("Chrome not handling FlexNIC or boot order skipping....")
    else:
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_FLEXNIC_ADD_CONNECTION, fail_if_false=True)
        #       2015-03-31 Alex Ma commented below to fix UI change
        #        selenium2lib.press_key(FusionServerProfilesPage.ID_SELECT_PORT_DROP_DOWN, connection.portName)
        ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_SELECT_PORT_DROP_DOWN, connection.portName)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.XP_CREATE_SP_ADD_CONN_NIC_DD_SELECT % connection.portName)
        logger._log_to_console_and_log_file("Selecting boot...")
        selenium2lib.press_key(FusionServerProfilesPage.ID_COMBO_BOOT_ADD_CONNECTION, connection.boot)
        #       2015-03-31 Alex Ma commented below to fix UI change
        #        selenium2lib.mouse_down(FusionServerProfilesPage.XP_CREATE_SP_ADD_CONN_BOOT_DD_SELECT % (boot_list, connection.boot))
        selenium2lib.mouse_down(FusionServerProfilesPage.XP_CREATE_SP_ADD_CONN_BOOT_DD_SELECT % connection.boot)
        #       2015-03-31 Alex Ma commented below to fix UI change
        #        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.XP_CREATE_SP_ADD_CONN_BOOT_DD_SELECT % (boot_list, connection.boot))
        selenium2lib.mouse_up(FusionServerProfilesPage.XP_CREATE_SP_ADD_CONN_BOOT_DD_SELECT % connection.boot)
        BuiltIn().sleep(2)

    return True


def _select_advanced_options(profile):
    """ Select Advanced Options    """
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_MENU_VIEW)
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_ADVANCED)
    logger._log_to_console_and_log_file("Setting advanced setup")
    if profile.has_property("mac") and profile.mac != "":
        if profile.mac == "Physical":
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_PHYSICAL_MAC)
        else:
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_VIRTUAL_MAC)
    if profile.has_property("wwn") and profile.wwn != "":
        if profile.wwn == "Physical":
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_PHYSICAL_WWN)
        else:
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_VIRTUAL_WWN)
    if profile.has_property("serial") and profile.serial != "":
        if profile.serial == "Physical":
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_PHYSICAL_SERIAL)
        elif profile.serial == "Virtual":
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_VIRTUAL_SERIAL)
        elif profile.serial == "Userspecified":
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_USER_SPECIFIED_SERIAL)
            if profile.has_property("serialnumber") and profile.serialnumber == "":
                logger._warn("Mandatory fields for user specified serial number can't be empty")
                return False
            if profile.has_property("UUID") and profile.UUID == "":
                logger._warn("Mandatory fields for user specified UUID can't be empty")
                return False
            ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_INPUT_SERIAL_NUMBER)
            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_SERIAL_NUMBER, profile.serialnumber)
            ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_INPUT_UUID_NUMBER)
            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_UUID_NUMBER, profile.UUID)
    return True


def delete_server_profile_by_name(profile_name, force_delete=True):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
    #   check if server profile exists
    if not VerifyServerProfile.verify_server_profile_exist(profile_name, fail_if_false=False):
        logger.warn("server profile '%s' does NOT exist! keyword '%s' returns a 'False'" % (profile_name, sys._getframe().f_code.co_name))
        return False
    CommonOperationServerProfile.click_server_profile(profile_name=profile_name)
    #   start performing remove action
    DeleteServerProfile.select_action_delete()
    DeleteServerProfile.tick_force_delete_checkbox() if force_delete is True else None
    DeleteServerProfile.click_yes_delete_button()
    DeleteServerProfile.wait_delete_server_profile_dialog_disappear()
    #   verify server profile is not existing after being deleted

    start = datetime.now()
    timeout = 900  # 15 minutes
    while (datetime.now() - start).total_seconds() < timeout:
        if CommonOperationServerProfile.wait_server_profile_show_not_found(profile_name, timeout=40, fail_if_false=False):
            logger.info("server profile status appear as 'not found', remove server profile '%s' successfully." % profile_name)
            break
        elif VerifyServerProfile.verify_server_profile_not_exist(profile_name, timeout=40, fail_if_false=False):
            logger.info("server profile '%s' is successfully deleted." % profile_name)
            break
    else:
        logger.warn("server profile '%s' is NOT successfully deleted or timeout issue occurred." % profile_name)
        return False

    FusionUIBase.show_activity_sidebar()
    # FusionUIBase.wait_activity_action_ok(profile_name, 'Delete', timeout=300, fail_if_false=False)
    if FusionUIBase.wait_activity_action_ok(profile_name, 'Delete', timeout=30, fail_if_false=False) is False:
        return False
    FusionUIBase.show_activity_sidebar()

    return True


def delete_server_profile(profile_obj):
    """ Delete Server Profile

    Arguments:
      name*             --  Name of server hardware as a string.
      server*           --  hostname of the iLO of the server hardware.

    * Required Arguments

    Example: - data structure is same as the one used for Add Server Hardware, but only profile.name, profile.server is required
        data/servers/DLServerProfiles/Delete -> @{TestData.servers.DLServerProfiles.Delete}
        <servers>
            <DLSererProfiles>
                <Delete>
                    <profile name="SP_DL360e_Gen8" server="wpstdl18-ilo" />
                    <profile name="SP_DL380p_Gen8" server="wpstdl18-ilo" />
                    <profile name="SP_DL120_Gen9" server="wpstdl39-ilo" />
                </Delete>
            </DLServerProfiles>
        </servers>
    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    total = len(profile_obj)
    not_exists = 0
    deleted = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("deleting a server profile named '%s'" % profile.name)
        if not VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' does not exist" % profile.name)
            not_exists += 1
        else:
            force_delete = True if profile.force_delete.lower() == 'true' else False
            if delete_server_profile_by_name(profile.name, force_delete=force_delete) is False:
                logger.warn("server profile '%s' is NOT deleted successfully, or 'Delete' action is not found in right-side-bar list." % profile.name)
                continue
            else:
                deleted += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no server profile to delete! all %s server profile(s) is NOT existing, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if deleted < total:
            logger.warn("not all of the server profile(s) is successfully deleted - %s out of %s deleted " % (deleted, total))
            if deleted + not_exists == total:
                logger.warn("%s not-existing server profile(s) is skipped, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s not-existing server profile(s) is skipped, %s profile(s) left is failed being deleted " % (not_exists, total - deleted - not_exists))
                return False

    logger.info("all of the server profile(s) is successfully deleted - %s out of %s " % (deleted, total))
    return True


def delete_all_appliance_server_profiles(wait_ongoing_task_complete=False):
    """ Delete All Applianec Server Profiles

    Arguments: - no arguments needed

    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
    profile_name_list = CommonOperationServerProfile.get_server_profile_list()
    if wait_ongoing_task_complete is True:
        CommonOperationServerProfile.wait_server_profile_task_complete()

    total = len(profile_name_list)
    not_exists = 0
    deleted = 0

    for n, profile_name in enumerate(profile_name_list):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("deleting a server profile named '%s'" % profile_name)
        if not VerifyServerProfile.verify_server_profile_exist(profile_name, fail_if_false=False):
            logger.warn("server profile '%s' does not exist" % profile_name)
            not_exists += 1
        else:
            if not delete_server_profile_by_name(profile_name, force_delete=True):
                logger.warn("server profile '%s' is NOT deleted successfully." % profile_name)
                continue
            else:
                deleted += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no server profile to delete! all %s server profile(s) is NOT existing, test is considered PASS" % not_exists)
        return True
    else:
        if deleted < total:
            logger.warn("not all of the server profile(s) is successfully deleted - %s out of %s deleted " % (deleted, total))
            if deleted + not_exists == total:
                logger.warn("%s non-existing server profile(s) is skipped being deleted, test is considered PASS" % not_exists)
                return True
            else:
                logger.warn("%s non-existing server profile(s) is skipped being deleted, %s profile(s) left is failed being deleted " % (not_exists, total - deleted - not_exists))
                return False

    logger.info("all of the server profile(s) is successfully deleted - %s out of %s " % (deleted, total))
    return True


def bak_delete_server_profile(*profile_obj):
    """ Delete Server Profile
        ProfileObj xml requires the following attributes:
            name - Comma separated string of profile names that should match
                   existing server profiles.
                   eg: <profile name="Server Profile 1, Server Profile 2">
                       <profile name="Server Profile 3">

        Example:
        | `Delete Server Profile`      |  @{profile_obj} |
    """
    selenium2lib = ui_lib.get_s2l()
    error = 0

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
        navigate()

    for profile in profile_obj:
        if profile.has_property("force") and profile.force.lower() == 'true':
            force = 1
        else:
            force = 0
        valid_profiles = []
        server_hardware = []
        excluded_profiles = []
        logger._log_to_console_and_log_file("")
        logger._log_to_console_and_log_file("Deleting server profiles '%s'" % profile.name)

        # Validate server profiles
        logger._log_to_console_and_log_file("Validating Server Profiles")
        profile_names = _split_profile_names(profile.name)
        for profile_name in profile_names:
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_SELECTOR, fail_if_false=True)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_GENERAL, fail_if_false=True)
            profile_attributes = get_server_profile_attributes(profile_name, None)
            if profile_attributes["server hardware"] == "unassigned":
                force = 0
            if profile_attributes is None:
                logger._warn("Server Profile '%s' does not exist" % profile_name)
                selenium2lib.capture_page_screenshot()
                return False
            elif profile_attributes["server power"] == "On" and not force:
                logger._warn("Cannot delete Server Profile '%s' due to being Powered On" % profile_name)
                selenium2lib.capture_page_screenshot()
                error += 1
                excluded_profiles.append(profile_name)
            else:
                valid_profiles.append(profile_name)
                if len(profile_names) == 1:
                    server_hardware.append(profile_attributes["server hardware"])

        if len(valid_profiles) == 0:
            logger._warn("No valid profiles to delete. Maybe specify force?")
            selenium2lib.capture_page_screenshot()
            error += 1
            continue

        # Select Server Profile
        logger._log_to_console_and_log_file("Deleting Server Profiles")
        if not select_server_profile(profile.name):
            logger._warn("Failed to select server profiles '%s'." % profile.name)
            selenium2lib.capture_page_screenshot()
            error += 1
            continue

        # Select Delete option from Action Menu
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_MAIN_ACTION)
        if selenium2lib._is_visible(FusionServerProfilesPage.ID_MENU_ACTION_DELETE):
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_ACTION_DELETE)
            if force:
                ui_lib.wait_for_element(FusionServerProfilesPage.ID_FORCE_DELETE)
                selenium2lib.select_checkbox(FusionServerProfilesPage.ID_FORCE_DELETE)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CONFIRM_DELETE)
        else:
            selenium2lib.capture_page_screenshot()
            logger._log_to_console_and_log_file("Delete option is not available in the Actions menu")
            selenium2lib.capture_page_screenshot()
            error += 1

        for profile_name in valid_profiles:
            if ui_lib.wait_for_element_remove("//tbody/tr/td[text()='%s']" % profile_name, 300.0, True):
                logger._log_to_console_and_log_file("Server profile '%s' is deleted successfully" % profile_name)
            else:
                logger._warn("Deleting profile %s failed" % profile_name)
                selenium2lib.capture_page_screenshot()
                error += 1

        '''
        # Navigating to profile page
        if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
            navigate()
        # Validating profile present in the appliance or not
        if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % profile.name):
            logger._warn("Profile %s is not deleted from appliance" % profile.name)
            selenium2lib.capture_page_screenshot()
            return False
        else:
            logger._log_to_console_and_log_file("Profile %s is deleted successfully" % profile.name)
            continue
        '''

        # Build Activity Message
        args = {}
        args["activity"] = "Delete"
        args["entity"] = profile_names[0] if len(profile_names) == 1 else "%d server profiles" % len(profile_names)
        args["multiple"] = len(profile_names) - 1
        args["message"] = "No messages"
        if args["multiple"]:
            args["completed"] = valid_profiles if len(valid_profiles) > 1 else [valid_profiles[0]]
            if len(excluded_profiles) > 0:
                args["excluded"] = excluded_profiles if len(excluded_profiles) > 1 else [excluded_profiles[0]]
        elif args["message"] == "No messages":
            args["message"] = "No messages"
        else:
            args["message"] = "Set administrative server power lock for the server hardware %s.\n" % server_hardware[0]
            args["message"] += "Remove server personality and connections.\n"
            args["message"] += "Successfully removed server settings for profile : %s.\n" % valid_profiles[0]
            args["message"] += "Release administrative server power lock for the server hardware %s." % server_hardware[0]

        # Verify Activity
        if not _verify_activity(**args):
            logger._warn("Failed to verify Delete Server Profile Activity")
            selenium2lib.capture_page_screenshot()
            error += 1
        else:
            logger._log_to_console_and_log_file("Successfully verified Delete Server Profile Activity")

    if error > 0:
        return False
    return True


def bak_delete_all_appliance_server_profiles():
    """ Delete All Appliance Server Profiles    """
    selenium2lib = ui_lib.get_s2l()
    """ Navigate to Network Page """
    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
        navigate()

    # get the list of networks
    ui_lib.wait_for_element(FusionServerProfilesPage.ID_PROFILE_LIST)
    delete_server_profile([el.text for el in selenium2lib._element_find(FusionServerProfilesPage.ID_PROFILE_LIST_NAMES, False, False)])


def update_server_profile_firmware(*profile_obj):
    """ Update Server Profile Firmware   """
    logger._log_to_console_and_log_file("Update firmware for Server Profiles")

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    for profile in profile_obj:
        selenium2lib = ui_lib.get_s2l()
        if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
            navigate()
        profile_list = [el.text for el in selenium2lib._element_find(FusionServerProfilesPage.ID_PROFILE_LIST_NAMES, False, False)]
        if profile.name not in profile_list:
            logger._warn("Profile '%s' does not exist" % profile.name)
            continue
        # Select & Edit Server Profile
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % profile.name)
        ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_MENU_MAIN_ACTION)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_MAIN_ACTION)
        ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_MENU_ACTION_EDIT)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_ACTION_EDIT)

        # Adding firmware baseline
        if profile.has_property("manageFirmware") and profile.manageFirmware == "true":
            logger._log_to_console_and_log_file("Selecting firmware baseline..")
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_DROPDOWN_BTN_FIRMWARE_BASELINE)
            ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_COMBO_FIRMWARE_BASELINE_LIST % profile.spp)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_FIRMWARE_BASELINE_LIST % profile.spp)
            ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_DROPDOWN_FIRMWARE_BASELINE)
            selectedFW = selenium2lib.get_text(FusionServerProfilesPage.ID_DROPDOWN_FIRMWARE_BASELINE)
            logger._log_to_console_and_log_file("Selected firmware is %s " % selectedFW)
            if not selectedFW == profile.spp:
                logger._warn("Failed to select preferred firmware bundle..'" + profile.spp + "' at the edit page")
                continue
            ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_BTN_CONFIRM_UPDATE_FIRMWARE, PerfConstants.PROFILE_ACTIVITY)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CONFIRM_UPDATE_FIRMWARE)
            if not ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_MAIN_PAGE, PerfConstants.PROFILE_ACTIVITY):
                if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_ERROR_POPUP, PerfConstants.DEFAULT_SYNC_TIME):
                    ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_ERROR_MSG, PerfConstants.DEFAULT_SYNC_TIME)
                    error_msg = selenium2lib.get_text(FusionServerProfilesPage.ID_ERROR_MSG)
                    logger._warn("Selected Bay: '" + profile.name + "' has encountered an error with the message : '" + error_msg + "' , may be the hardware is being managed by another system")
                    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_UPDATE_FIRMWARE)
                    logger._log_to_console_and_log_file("Firmware Update canceled")
                    continue
            if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_STATUS_CHANGING, PerfConstants.PROFILE_ACTIVITY):
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MAIN_PAGE)
                ui_lib.wait_for_element_visible(FusionDashboardPage.ID_LINK_ACTIVITY, PerfConstants.ACTIVITY)
                ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_LINK_ACTIVITY)
                if ui_lib.wait_for_element(FusionServerProfilesPage.ID_NEW_ACTIVITY_PROGRESS % profile.name, PerfConstants.FIRMWARE_VALIDATION):
                    start_time = selenium2lib.get_text(FusionServerProfilesPage.ID_NEW_ACTIVITY_TIMESTAMP % profile.name)
                    logger._log_to_console_and_log_file(start_time)
                    logger._log_to_console_and_log_file("Update Server Profile Firmware %s started......... " % profile.name)
                    if ui_lib.wait_for_element(FusionServerProfilesPage.ID_NEW_ACTIVITY_SUCCESS % (profile.name, start_time), PerfConstants.FIRMWARE_FAIL_PASS_VALIDATION):
                        logger._log_to_console_and_log_file("Updating Server Profile Firmware %s done successfully" % profile.name)
                    elif ui_lib.wait_for_element(FusionServerProfilesPage.ID_NEW_ACTIVITY_ERROR % (profile.name, start_time), PerfConstants.FIRMWARE_ERROR_VALIDATION):
                        logger._log_to_console_and_log_file("Update Server Profile Firmware %s done with errors" % profile.name)
                    else:
                        logger._log_to_console_and_log_file("Update Server Profile Firmware %s done with warnings" % profile.name)
            else:
                logger._log_to_console_and_log_file("Selected Bay: '" + profile.name + "' has already been updated with the firmware baseline : '" + profile.spp + "'")
                continue
        else:
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_UPDATE_FIRMWARE)
            logger._log_to_console_and_log_file("Firmware Update canceled")


def bak_copy_server_profile(*profile_obj):
    """ Copy Server Profile    """

    logger._log_to_console_and_log_file("")
    selenium2lib = ui_lib.get_s2l()
    error = 0

    # Navigating to Server profile page
    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    # Copy server profile to specific server
    for copyprofile in profile_obj:
        profile_list = [ui_lib.get_webelement_attribute("text", el) for el in selenium2lib._element_find(FusionServerProfilesPage.ID_PROFILE_LIST_NAMES, False, False)]
        if copyprofile.profile not in profile_list:
            logger._warn("Profile '%s' does not exist" % copyprofile.profile)
            selenium2lib.capture_page_screenshot()
            error += 1
        if copyprofile.profile == "" or copyprofile.server == "":
            logger._warn("Mandatory fields to copy server profile can't be empty")
            selenium2lib.capture_page_screenshot()
            error += 1
        logger._log_to_console_and_log_file("Found profile %s" % copyprofile.profile)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % copyprofile.profile)
        # ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_OVERVIEW)
        # ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_GENERAL)
        ui_lib.wait_for_element(FusionServerProfilesPage.ID_PROFILE_HARDWARE)
        profilehardwaretype = ui_lib.ignore_staleElementRefException("get_text", FusionServerProfilesPage.ID_PROFILE_HARDWARE)
        logger._log_to_console_and_log_file("profile hardware type is %s" % profilehardwaretype)

        if copyprofile.server != "unassigned":
            # Navigating to server hardware page to power off server
            if not selenium2lib._is_element_present(FusionServerHardwarePage.ID_PAGE_LABEL):
                base_page.navigate_base(FusionServerHardwarePage.ID_PAGE_LABEL,
                                        FusionUIBaseElements.ID_MENU_LINK_SERVER_HARDWARE, "css=span.hp-page-item-count")
            server_list = [ui_lib.get_webelement_attribute("text", element) for element in selenium2lib._element_find(FusionServerHardwarePage.ID_SERVER_LIST_NAMES, False, False)]
            if copyprofile.server not in server_list:
                logger._warn("Server '%s' does not exist" % copyprofile.server)
                selenium2lib.capture_page_screenshot()
                error += 1
            ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_ELEMENT_SERVER_HARDWARE % copyprofile.server)
            ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_LINK_OVERVIEW)
            ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_LINK_HARDWARE)
            ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_SERVER_HARDWARE)
            targethardwaretype = ui_lib.ignore_staleElementRefException("get_text", FusionServerHardwarePage.ID_SERVER_HARDWARE)
            if profilehardwaretype == targethardwaretype and not serverhardware.power_off_server_by_name(copyprofile.server):
                logger._warn("Failed to powerOff the server '%s'" % copyprofile.server)
                logger._warn("Can't proceed with move server profile to server '%s'" % copyprofile.server)
                selenium2lib.capture_page_screenshot()
                error += 1

        # Navigate to Server profile page from server hardware page
        if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
            navigate()
        # creating copy of existing server profile
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % copyprofile.profile)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_MAIN_ACTION)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COPY_SERVER_PROFILE)
        selenium2lib.wait_until_page_contains("Copy %s" % copyprofile.profile)
        ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_SERVER_PROFILE_NAME, copyprofile.changeprofile)

        if copyprofile.has_property("description"):
            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_SERVER_PROFILE_DESCRIPTION, copyprofile.description)

        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_DROPDOWN_SEARCH_SERVER_HARDWARE)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_SEARCH_HARDWARE)

        # Select hardware to move server profile
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_SERVER_HARDWARE_TYPE_DROPDOWN)
        if ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % copyprofile.server):
            logger._log_to_console_and_log_file("Selected Valid Server")
        else:
            logger._log_to_console_and_log_file("Provide valid server")
            selenium2lib.capture_page_screenshot()
            error += 1
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CREATE_SERVER_PROFILE)
        ui_lib.wait_for_element(FusionServerProfilesPage.ID_ADD_PROFILE_NOTIFICATION)
        # New Code
        if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_ADD_PROFILE_NOTIFICATION):
            errMsg = ui_lib.ignore_staleElementRefException("get_text", FusionServerProfilesPage.ID_ADD_PROFILE_NOTIFICATION_CONTENT)
            logger._warn(errMsg)
            logger._warn("Unable to create a copy of server profile %s" % copyprofile.changeprofile)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_SERVER_PROFILE)
            selenium2lib.capture_page_screenshot()
            error += 1
        ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_UPDATE_PROFILE_TIMESTAMP)
        strTimeStamp = ui_lib.ignore_staleElementRefException("get_text", FusionServerProfilesPage.ID_UPDATE_PROFILE_TIMESTAMP)
        logger._log_to_console_and_log_file(strTimeStamp)
        # Verifying profile 'update status' in activity page
        if copyprofile.server == "unassigned":
            logger._log_to_console_and_log_file("Validating unassigned profile %s" % copyprofile.changeprofile)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ACTVITY_PROFILE)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_PROFILE_UNASSIGNED_SELECT % copyprofile.changeprofile)
            if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_PROFILE_UNASSIGNED_SUCCESS % copyprofile.changeprofile, PerfConstants.CREATE_SERVER_PROFILE_TIME):
                logger._log_to_console_and_log_file("copying unassigned profile  %s successfully" % copyprofile.changeprofile)
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ACTVITY_PROFILE)
            elif ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_PROFILE_UNASSIGNED_FAIL % copyprofile.changeprofile, PerfConstants.CREATE_SERVER_PROFILE_TIME):
                logger._log_to_console_and_log_file("copying unassigned profile  %s failed" % copyprofile.changeprofile)
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ACTVITY_PROFILE)
                selenium2lib.capture_page_screenshot()
                error += 1
            elif ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_PROFILE_UNASSIGNED_WARNING % copyprofile.changeprofile, PerfConstants.CREATE_SERVER_PROFILE_TIME):
                logger._log_to_console_and_log_file("copying unassigned profile  %s with warnings" % copyprofile.changeprofile)
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ACTVITY_PROFILE)
        else:
            if _is_element_present_inactivity_page(copyprofile.changeprofile, "Create", time.time()):
                logger._log_to_console_and_log_file("Server profile '%s' is copied successfully to server '%s' as '%s'" % (copyprofile.profile, copyprofile.server, copyprofile.changeprofile,))
            else:
                ui_lib.fail_test("Copying server profile '%s' to server '%s' as '%s' is failed" % (copyprofile.profile, copyprofile.server, copyprofile.changeprofile))
        if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
            navigate()

        BuiltIn().sleep("30 seconds")

    if error > 0:
        return False
    return True


def power_on_server_profile_by_name(profile_name):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
    #   check if server profile exists
    if not VerifyServerProfile.verify_server_profile_exist(profile_name, fail_if_false=False):
        logger.warn("server profile '%s' does not exist" % profile_name)
        return False
    CommonOperationServerProfile.click_server_profile(profile_name=profile_name)
    #   check if already powered on
    FusionUIBase.select_view_by_name(view_name='General', timeout=5, fail_if_false=False)
    if VerifyServerProfile.verify_general_server_power(expect_value='Off', timeout=5, fail_if_false=False) is False:
        logger.warn("power state of server profile '%s' is not 'Off', 'POWER ON' action is unavailable." % profile_name)
        return False
    #   start performing power on action
    PowerOnServerProfile.select_action_power_on()
    FusionUIBase.show_activity_sidebar()
    server_hardware = CommonOperationServerProfile.get_server_hardware_of_server_profile(profile_name)
    FusionUIBase.wait_activity_action_ok(server_hardware, 'Power on', timeout=60, fail_if_false=False)
    FusionUIBase.show_activity_sidebar()
    CommonOperationServerProfile.wait_server_profile_status_ok(profile_name, timeout=180, fail_if_false=False)
    #   verify the power state is changed to expected 'On'
    FusionUIBase.select_view_by_name(view_name='General', timeout=5, fail_if_false=False)
    if CommonOperationServerProfile.wait_general_server_power_turned_on(profile_name, timeout=25, fail_if_false=False):
        logger.info("server profile '%s' is successfully powered on" % profile_name)
        return True
    else:
        logger.warn("server profile '%s' is NOT successfully powered on or timeout for changing power state to 'On'." % profile_name)
        return False


def power_on_server_profile(profile_obj):
    """ Power off 1 or multiple Server Hardware

    Arguments:
      name*             --  Name of server hardware as a string.
      ...               --  ...
      ...               --  ...
    * Required Arguments


    Example: - data structure is same as the one used for Add Server Hardware, but only server.name is required


    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    total = len(profile_obj)
    already_on_or_not_exists = 0
    powered_on = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("powering on a server profile named '%s'" % profile.name)
        #   check if server profile exists
        if not VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' does not exist" % profile.name)
            already_on_or_not_exists += 1
            continue
        CommonOperationServerProfile.click_server_profile(profile_name=profile.name, time_for_loading=4)
        #   check if already powered on
        FusionUIBase.select_view_by_name(view_name='General', timeout=5, fail_if_false=False)
        if VerifyServerProfile.verify_general_server_power(expect_value='Off', timeout=7, fail_if_false=False) is False:
            logger.warn("power state of server profile '%s' is not 'Off', 'POWER ON' action is unavailable." % profile.name)
            already_on_or_not_exists += 1
        else:
            if power_on_server_profile_by_name(profile.name) is False:
                logger.warn("server profile '%s' is NOT powered on successfully" % profile.name)
                continue
            else:
                powered_on += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - already_on_or_not_exists == 0:
        # logger.warn("no server profile to power on! all %s server profile(s) is NOT applicable to power on (already powered on, or not existing), test is considered PASS" % already_on_or_not_exists)
        logger.warn("no server profile to power on! all %s server profile(s) is NOT applicable to power on (already powered on, or not existing), keyword '%s' returns a 'False'" % (already_on_or_not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if powered_on < total:
            logger.warn("not all of the server profile(s) is successfully powered on - %s out of %s powered on " % (powered_on, total))
            if powered_on + already_on_or_not_exists == total:
                # logger.warn("%s already-on-or-not-existing server profile(s) is skipped being powered on, test is considered PASS" % already_on_or_not_exists)
                logger.warn("%s already-on-or-not-existing server profile(s) is skipped being powered on, keyword '%s' returns a 'False'" % (already_on_or_not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s already-on-or-not-existing server profile(s) is skipped being powered on, "
                            "%s server profile(s) left is failed being powered on " % (already_on_or_not_exists, total - powered_on - already_on_or_not_exists))
                return False

    logger.info("all of the server profile(s) is successfully powered on - %s out of %s " % (powered_on, total))
    return True


def power_off_server_profile_by_name(profile_name, momentary_press=False):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
    #   check if server hardware exists
    if not VerifyServerProfile.verify_server_profile_exist(profile_name, fail_if_false=False):
        logger.warn("server profile '%s' does not exist" % profile_name)
        return False
    CommonOperationServerProfile.click_server_profile(profile_name=profile_name, time_for_loading=4)
    #   check if already powered off
    FusionUIBase.select_view_by_name(view_name='General', timeout=5, fail_if_false=False)
    if VerifyServerProfile.verify_general_server_power(expect_value='On', timeout=5, fail_if_false=False) is False:
        logger.warn("power state of server profile '%s' is not 'On', 'Power Off' action is unavailable." % profile_name)
        return False
    #   start performing power off action
    PowerOffServerProfile.select_action_power_off()
    if momentary_press is True:
        PowerOffServerProfile.click_momentary_press_button()
    else:
        PowerOffServerProfile.click_press_and_hold_button()
    FusionUIBase.show_activity_sidebar()
    server_hardware = CommonOperationServerProfile.get_server_hardware_of_server_profile(profile_name)
    FusionUIBase.wait_activity_action_ok(server_hardware, 'Power off', timeout=60, fail_if_false=False)
    FusionUIBase.show_activity_sidebar()
    CommonOperationServerProfile.wait_server_profile_status_ok(profile_name, timeout=180, fail_if_false=False)
    #   verify the power state is changed to expected 'Off'
    FusionUIBase.select_view_by_name(view_name='General', timeout=5, fail_if_false=False)
    if CommonOperationServerProfile.wait_general_server_power_turned_off(profile_name, timeout=15, fail_if_false=False):
        logger.info("server profile '%s' is successfully powered off" % profile_name)
        return True
    else:
        logger.warn("server profile '%s' is NOT successfully powered off or timeout for changing power state to 'Off'." % profile_name)
        return False


def power_off_server_profile(profile_obj):
    """ Power off 1 or multiple Server Hardware

    Arguments:
      name*                               --  Name of server hardware as a string.
      MomentaryPressForPowerOff           --  If it is True, power off server profile in "Momentary press" way else
                                              power off server profile in "Press and hold" way


    * Required Arguments


    Example: - data structure is almost the same as the one used for Create Server profile, but only profile.name is required
               eg: <profile name="Server Profile1"  MomentaryPressForPowerOff="True">


    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    total = len(profile_obj)
    already_off_or_not_exists = 0
    powered_off = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("powering off a server profile named '%s'" % profile.name)
        #   check if server profile exists
        if not VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' does not exist" % profile.name)
            already_off_or_not_exists += 1
            continue
        CommonOperationServerProfile.click_server_profile(profile_name=profile.name, time_for_loading=4)
        #   check if already powered off
        FusionUIBase.select_view_by_name(view_name='General', timeout=5, fail_if_false=False)
        if VerifyServerProfile.verify_general_server_power(expect_value='On', timeout=7, fail_if_false=False) is False:
            logger.warn("power state of server profile '%s' is not 'On', 'POWER OFF' action is unavailable." % profile.name)
            already_off_or_not_exists += 1
        else:
            if power_off_server_profile_by_name(profile.name, (getattr(profile, 'MomentaryPressForPowerOff', '').lower() == 'true')) is False:
                logger.warn("server profile '%s' is NOT powered off successfully" % profile.name)
                continue
            else:
                powered_off += 1
    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - already_off_or_not_exists == 0:
        # logger.warn("no server profile to power off! all %s server profile(s) is NOT applicable to power off (already powered off, or not existing), test is considered PASS" % already_off_or_not_exists)
        logger.warn("no server profile to power off! all %s server profile(s) is NOT applicable to power off (already powered off, or not existing), keyword '%s' returns a 'False'" % (already_off_or_not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if powered_off < total:
            logger.warn("not all of the server profile(s) is successfully powered off - %s out of %s powered off " % (powered_off, total))
            if powered_off + already_off_or_not_exists == total:
                # logger.warn("%s already-off-or-not-existing server profile(s) is skipped being powered off, test is considered PASS" % already_off_or_not_exists)
                logger.warn("%s already-off-or-not-existing server profile(s) is skipped being powered off, keyword '%s' returns a 'False'" % (already_off_or_not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s already-off-or-not-existing server profile(s) is skipped being powered off, "
                            "%s server profile(s) left is failed being powered off " % (already_off_or_not_exists, total - powered_off - already_off_or_not_exists))
                return False

    logger.info("all of the server profile(s) is successfully powered off - %s out of %s " % (powered_off, total))
    return True


def power_off_all_server_profiles():
    """ Power off all existing Server Profile(s)

    Arguments:
      name*             --  Name of server hardware as a string.
      ...               --  ...
      ...               --  ...
    * Required Arguments


    Example: - data structure is same as the one used for Add Server Hardware, but only server.name is required


    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
    profile_name_list = CommonOperationServerProfile.get_server_profile_list()

    total = len(profile_name_list)
    already_off_or_not_supported = 0
    powered_off = 0

    for n, profile_name in enumerate(profile_name_list):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("powering off a server profile named '%s'" % profile_name)
        CommonOperationServerProfile.click_server_profile(profile_name=profile_name, time_for_loading=4)
        #   check if already powered off
        FusionUIBase.select_view_by_name(view_name='General', timeout=5, fail_if_false=False)
        if VerifyServerProfile.verify_general_server_power(expect_value='On', timeout=5, fail_if_false=False) is False:
            logger.warn("power state of server profile '%s' is not 'On' (it's Off, or not supported due to being managed by another system), 'Power Off' action is unavailable." % profile_name)
            already_off_or_not_supported += 1
        else:
            if power_off_server_profile_by_name(profile_name) is False:
                logger.warn("server profile '%s' is NOT powered off successfully" % profile_name)
                continue
            else:
                powered_off += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - already_off_or_not_supported == 0:
        logger.warn("no server profile to power off! all %s server profile(s) is NOT applicable to power off (already powered off, or unknown power state), test is considered PASS" % already_off_or_not_supported)
        return True
    else:
        if powered_off < total:
            logger.warn("not all of the server profile(s) is successfully powered off - %s out of %s powered off " % (powered_off, total))
            if powered_off + already_off_or_not_supported == total:
                logger.warn("%s already-off-or-not-supported server profile(s) is skipped being powered off, test is considered PASS" % already_off_or_not_supported)
                return True
            else:
                logger.warn("%s already-off-or-not-supported server profile(s) is skipped being powered off, "
                            "%s server profile(s) left is failed being powered off " % (already_off_or_not_supported, total - powered_off - already_off_or_not_supported))
                return False

    logger.info("all of the server profile(s) is successfully powered off - %s out of %s " % (powered_off, total))
    return True


def reset_server_profile_by_name(profile_name):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
    #   check if server profile exists
    if not VerifyServerProfile.verify_server_profile_exist(profile_name, fail_if_false=False):
        logger.warn("server profile '%s' does not exists" % profile_name)
        return False
    CommonOperationServerProfile.click_server_profile(profile_name=profile_name)
    FusionUIBase.select_view_by_name(view_name='General', timeout=5, fail_if_false=False)
    #   check if powered on, reset/cold boot is only doable when server is powered on
    if VerifyServerProfile.verify_general_server_power(expect_value='On', timeout=5, fail_if_false=False) is False:
        logger.warn("server profile '%s' is not powered on, RESET action is unavailable." % profile_name)
        return False
    #   start performing reset action
    ResetServerProfile.select_action_reset()
    ResetServerProfile.click_reset_button()
    FusionUIBase.show_activity_sidebar()
    server_hardware = CommonOperationServerProfile.get_server_hardware_of_server_profile(profile_name)
    FusionUIBase.wait_activity_action_ok(server_hardware, 'Reset', timeout=60, fail_if_false=False)
    FusionUIBase.show_activity_sidebar()
    CommonOperationServerProfile.wait_server_profile_status_ok_or_warn(profile_name, timeout=180, fail_if_false=False)
    FusionUIBase.select_view_by_name(view_name='General', timeout=5, fail_if_false=False)
    #   verify the power state is changed to expected 'On'
    if VerifyServerProfile.verify_general_server_power(expect_value='On', timeout=15, fail_if_false=False):
        logger.info("server profile '%s' is successfully performed reset." % profile_name)
        return True
    else:
        logger.warn("server profile '%s' is NOT successfully performed reset or timeout for changing power state to 'On'." % profile_name)
        return False


def reset_server_profiles(profile_obj):
    """ Reset 1 or multiple Server Profile

    Arguments:
      name*             --  Name of server profile as a string.
      ...               --  ...
      ...               --  ...
    * Required Arguments


    Example: - data structure is same as the one used for Create Server Profile, but only server.name is required


    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    total = len(profile_obj)
    off_or_unsupported = 0
    not_exists = 0
    done_reset = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(profile_obj), '-' * 14))
        logger.info("reset a server profile named '%s'" % profile.name)
        if not VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' does not exist" % profile.name)
            not_exists += 1
            continue
        CommonOperationServerProfile.click_server_profile(profile_name=profile.name, time_for_loading=2)
        if VerifyServerProfile.verify_general_server_power(expect_value='On', timeout=5, fail_if_false=False) is False:
            logger.warn("Power state of server profile '%s' is not 'On', 'RESET' action is unavailable." % profile.name)
            off_or_unsupported += 1
        else:
            if reset_server_profile_by_name(profile.name) is False:
                logger.warn("server profile '%s' is NOT done reset successfully" % profile.name)
                continue
            else:
                done_reset += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - off_or_unsupported - not_exists == 0:
        logger.warn("no server profile to reset! all %s server profile(s) is NOT applicable to reset (already powered off/unsupported/not existing), test is considered PASS" % off_or_unsupported)
        return True
    else:
        if done_reset < total:
            logger.warn("not all of these server profile is successfully reset - %s out of %s reset " % (done_reset, total))
            if done_reset + off_or_unsupported + not_exists == total:
                logger.warn("%s off-or-unsupported server profile(s) is skipped, %s not-existing server profile(s) is skipped, test is considered PASS" % (off_or_unsupported, not_exists))
                return True
            else:
                logger.warn("%s off-or-unsupported server profile(s) is skipped, %s not-existing server profile(s) is skipped, "
                            "%s left is failed being reset " % (off_or_unsupported, not_exists, total - done_reset - off_or_unsupported - not_exists))
                return False

    logger.info("all of the server profile(s) is successfully done reset - %s out of %s " % (done_reset, total))
    return True


def cold_boot_server_profile_by_name(profile_name):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
    #   check if server hardware exists
    if not VerifyServerProfile.verify_server_profile_exist(profile_name, fail_if_false=False):
        logger.warn("server profile '%s' does not exists" % profile_name)
        return False
    CommonOperationServerProfile.click_server_profile(profile_name=profile_name)
    FusionUIBase.select_view_by_name(view_name='General', timeout=5, fail_if_false=False)
    #   check if powered on, reset/cold boot is only doable when server is powered on
    if VerifyServerProfile.verify_general_server_power(expect_value='On', timeout=5, fail_if_false=False) is False:
        logger.warn("server profile '%s' is not powered on, or its power state is unknown, COLD BOOT action cannot be performed." % profile_name)
        return False
    #   start performing cold boot action
    ResetServerProfile.select_action_reset()
    ResetServerProfile.click_cold_boot_button()
    FusionUIBase.show_activity_sidebar()
    server_hardware = CommonOperationServerProfile.get_server_hardware_of_server_profile(profile_name)
    FusionUIBase.wait_activity_action_ok(server_hardware, 'Reset', timeout=60, fail_if_false=False)
    FusionUIBase.show_activity_sidebar()
    CommonOperationServerProfile.wait_server_profile_status_ok_or_warn(profile_name, timeout=180, fail_if_false=False)
    FusionUIBase.select_view_by_name(view_name='General', timeout=5, fail_if_false=False)
    #   verify the power state is changed to expected 'On'
    if VerifyServerProfile.verify_general_server_power(expect_value='On', timeout=15, fail_if_false=False) is True:
        logger.info("server profile '%s' is successfully performed cold boot" % profile_name)
        return True
    else:
        logger.warn("server profile '%s' is NOT successfully performed cold boot or timeout for changing power state to 'On'." % profile_name)
        return False


def cold_boot_server_profiles(profile_obj):
    """ Cold boot 1 or multiple Server Profile

    Arguments:
      name*             --  Name of server profile as a string.
      ...               --  ...
      ...               --  ...
    * Required Arguments


    Example: - data structure is same as the one used for Create Server Profile, but only profile.name is required


    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    total = len(profile_obj)
    off_or_unsupported = 0
    not_exists = 0
    done_cold_boot = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(profile_obj), '-' * 14))
        logger.info("cold boot a server profile named '%s'" % profile.name)
        if not VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' does not exist" % profile.name)
            not_exists += 1
            continue
        CommonOperationServerProfile.click_server_profile(profile_name=profile.name, time_for_loading=2)
        if VerifyServerProfile.verify_general_server_power(expect_value='On', timeout=5, fail_if_false=False) is False:
            logger.warn("Power state of server profile '%s' is not 'On', 'RESET -> COLD BOOT' action is unavailable." % profile.name)
            off_or_unsupported += 1
        else:
            if cold_boot_server_profile_by_name(profile.name) is False:
                logger.warn("server profile '%s' is NOT done cold boot successfully" % profile.name)
                continue
            else:
                done_cold_boot += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - off_or_unsupported - not_exists == 0:
        logger.warn("no server profile to cold boot! all %s server profile(s) is NOT applicable to cold boot (already powered off/unsupported/not existing), test is considered PASS" % off_or_unsupported)
        return True
    else:
        if done_cold_boot < total:
            logger.warn("not all of these server profile(s) is successfully done cold boot - %s out of %s done cold boot " % (done_cold_boot, total))
            if done_cold_boot + off_or_unsupported + not_exists == total:
                logger.warn("%s off-or-unsupported server profile(s) is skipped, %s not-existing server profile(s) is skipped, test is considered PASS" % (off_or_unsupported, not_exists))
                return True
            else:
                logger.warn("%s off-or-unsupported server profile(s) is skipped, %s not-existing server profile(s) is skipped, "
                            "%s left is failed to cold boot " % (off_or_unsupported, not_exists, total - done_cold_boot - off_or_unsupported - not_exists))
                return False

    logger.info("all of the server profile(s) is successfully done cold boot - %s out of %s " % (done_cold_boot, total))
    return True


def verify_server_profile_general_info(profile_obj):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    total = len(profile_obj)
    not_exists = 0
    verified_pass = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("verifying general info of a server profile named '%s'" % profile.name)
        #   check if server profile exists
        if VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False) is False:
            logger.warn("server profile '%s' does not exist" % profile.name)
            not_exists += 1
            continue
        CommonOperationServerProfile.click_server_profile(profile_name=profile.name, time_for_loading=4)
        #   check if already powered off
        FusionUIBase.select_view_by_name(view_name='General', timeout=5, fail_if_false=False)
        result = {'Server hardware': None,
                  'Server hardware type': None,
                  'Enclosure group': None,
                  }

        if VerifyServerProfile.verify_general_server_hardware(expect_value=profile.server, timeout=7, fail_if_false=False) is False:
            logger.warn("'Server hardware' of server profile '%s' is not '%s', verification failed." % (profile.name, profile.server))
            result['Server hardware'] = False
        else:
            result['Server hardware'] = True

        if hasattr(profile, 'hardwareType'):
            hardware_type = profile.hardwareType
        else:
            if hasattr(profile, 'for_server'):
                hardware_type = FusionUIBase.APIMethods().get_server_hardware_type_by_server_hardware_name(profile.for_server)
            else:
                hardware_type = FusionUIBase.APIMethods().get_server_hardware_type_by_server_hardware_name(profile.server)

        if VerifyServerProfile.verify_general_server_hardware_type(expect_value=hardware_type, timeout=7, fail_if_false=False) is False:
            logger.warn("'Server hardware type' of server profile '%s' is not '%s', verification failed." % (profile.name, hardware_type))
            result['Server hardware type'] = False
        else:
            result['Server hardware type'] = True

        if VerifyServerProfile.verify_general_enclosure_group(expect_value=profile.enclgroup, timeout=7, fail_if_false=False) is False:
            logger.warn("'Enclosure group' of server profile '%s' is not '%s', verification failed." % (profile.name, profile.enclgroup))
            result['Enclosure group'] = False
        else:
            result['Enclosure group'] = True

        if hasattr(profile, 'Advanced'):
            if hasattr(profile.Advanced, 'iscsi'):
                logger.info("verifying iSCSI initiator name is '%s' and set to '%s'" % (profile.Advanced.iscsi, profile.Advanced.iscsiInitiatorName))
                if VerifyServerProfile.verify_general_iscsi_initiator_name(profile.Advanced.iscsi, profile.Advanced.iscsiInitiatorName):
                    logger.info("verified! iSCSI initiator name is '%s' and contains expected value '%s'" % (profile.Advanced.iscsi, profile.Advanced.iscsiInitiatorName))
            if hasattr(profile.Advanced, 'serial') and (hasattr(profile.Advanced, 'UserSpecifiedUUID') or hasattr(profile.Advanced, 'expectedUUID')):
                if getattr(profile.Advanced, 'serial', '').lower() == "user-specified":
                    logger.info("verifying <%s> UUID is setting  to <%s>" % (profile.Advanced.serial, profile.Advanced.UserSpecifiedUUID))
                    if VerifyServerProfile.verify_general_user_specified_uuid(profile.Advanced.UserSpecifiedUUID):
                        logger.info("verified! 'UUID' type is <%s> and name contains expected value <%s>" % (profile.Advanced.serial, profile.Advanced.UserSpecifiedUUID))
                    logger.info("verifying <%s> SerialNumber is setting to <%s>" % (profile.Advanced.serial, profile.Advanced.UserSpecifiedSerialNumber))
                    if VerifyServerProfile.verify_general_user_specified_serial_number(profile.Advanced.UserSpecifiedSerialNumber):
                        logger.info("verified! 'Serial Number' type is <%s> and name contains expected value <%s>" % (profile.Advanced.serial, profile.Advanced.UserSpecifiedSerialNumber))
                elif getattr(profile.Advanced, 'serial', '').lower() == "virtual":
                    if VerifyServerProfile.verify_general_virtual_uuid():
                        logger.info("verified! 'UUID' type is <%s>" % profile.Advanced.serial)
                    if VerifyServerProfile.verify_general_virtual_serial_number():
                        logger.info("verified! 'Serial Number' type is <%s>" % profile.Advanced.serial)
                elif getattr(profile.Advanced, 'serial', '').lower() == "physical":
                    logger.info("verifying <%s> UUID is setting  to <%s>" % (profile.Advanced.serial, profile.Advanced.expectedUUID))
                    if VerifyServerProfile.verify_general_physical_uuid(profile.Advanced.expectedUUID):
                        logger.info("verified! 'UUID' type is <%s> and name contains expected value <%s>" % (profile.Advanced.serial, profile.Advanced.expectedUUID))
                    logger.info("verifying <%s> Serial Number is setting to <%s>" % (profile.Advanced.serial, profile.Advanced.expectedSerialNumber))
                    if VerifyServerProfile.verify_general_physical_serial_number(profile.Advanced.expectedSerialNumber):
                        logger.info("verified! 'Serial Number' type is <%s> and name contains expected value <%s>" % (profile.Advanced.serial, profile.Advanced.expectedSerialNumber))
                else:
                    logger.info("no supported type option <%s> for 'Serial number/UUID'." % getattr(profile.Advanced, 'serial', ''))
                    return False

        # if reduce(lambda x, y: (x and y), result.values()) is not True:
        if all(result.values()) is not True:
            logger.warn("server profile '%s' is FAIL for general info verification" % profile.name)
        else:
            logger.info("server profile '%s' is PASS for general info verification" % profile.name)
            verified_pass += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        # logger.warn("no server profile to verify general info against! all %s server profile(s) is NOT existing, test is considered FAIL" % not_exists)
        logger.warn("no server profile to verify general info against! all %s server profile(s) is NOT existing, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if verified_pass < total:
            logger.warn("not all of the server profile(s) is successfully verified PASS - %s out of %s passed " % (verified_pass, total))
            if verified_pass + not_exists == total:
                # logger.warn("%s not-existing server profile(s) is skipped, test is considered FAIL" % not_exists)
                logger.warn("%s not-existing server profile(s) is skipped, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s not-existing server profile(s) is skipped, "
                            "%s server profile(s) left is failed being verified PASS " % (not_exists, total - verified_pass - not_exists))
                return False

    logger.info("all of the server profile(s) is successfully verified PASS - %s out of %s " % (verified_pass, total))
    return True


def verify_server_profile_boot_settings_info(*profile_obj):
    """ Verify the boot_settings_info of server profile
    Example:
      <profile name="SP_wpst23bay3_BL465c_Gen8" newName="SP_wpst23bay3_BL465c_Gen8" desc="This profile is an edited one" server="wpst23, bay 3" hardwareType="BL465c Gen8" enclgroup="GRP-wpst32" Affinity="Device bay">
        <BootSettings manageBootMode="false" bootMode="UEFI" manageBootOrder="true">
            <bootorder device="PXE" />
            <bootorder device="CD" />
            <bootorder device="Floppy" />
            <bootorder device="USB" />
            <bootorder device="HardDisk" />
            </BootSettings>
    </profile>
    """

    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    for _, profile in enumerate(profile_obj):
        logger.info("verifying Boot Settings info of a server profile named '%s'" % profile.name)
        #   check if server profile exists
        VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=True)
        CommonOperationServerProfile.click_server_profile(profile_name=profile.name, time_for_loading=10)
        FusionUIBase.select_view_by_name(view_name='Boot Settings', timeout=5, fail_if_false=True)

        if profile.BootSettings.bootMode.lower() == 'legacy bios':
            VerifyServerProfile.verify_legacy_boot_settings(profile, timeout=10, fail_if_false=True)
        else:
            VerifyServerProfile.verify_non_legacy_boot_settings(profile, timeout=10, fail_if_false=True)


def verify_server_profile_bios_settings_info(*profile_obj):
    """ Verify the bios_settings_info of server profile
    Example:
      <profile name="SP_wpst23bay3_BL465c_Gen8" newName="SP_wpst23bay3_BL465c_Gen8" desc="This profile is an edited one" server="wpst23, bay 3" hardwareType="BL465c Gen8" enclgroup="GRP-wpst32" Affinity="Device bay">
        <BIOSSettings manageBIOSsettings='true'>
            <Verify>
            <ServerAssetInformation biossettings='Inconsistent'serverOtherInformation='' powerOnLogo='' customPostMessage='' assetTagProtection='' ServerPrimaryOS='' AdminName='admin name AdminPhone='555-555-5555' AdminEmail='admin@hpe.com' AdminOtherInfo='server setttings test'>
             </ServerAssetInformation>
             <None/>
            </Verify>
    </profile>
    """

    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    for _, profile in enumerate(profile_obj):
        logger.info("verifying server_profile_bios named '%s'" % profile.name)
        #   check if server profile exists
        VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=True)
        CommonOperationServerProfile.click_server_profile(profile_name=profile.name, time_for_loading=10)
        FusionUIBase.select_view_by_name(view_name='BIOS Settings', timeout=10, fail_if_false=True)
        if hasattr(profile.BIOSSettings.Verify, 'ServerAssetInformation'):
            logger.info("verifying server_profile_bios expected values before power on named '%s'" % profile.name)
            VerifyServerProfile.verify_server_asset_info(profile.name, profile.BIOSSettings.Verify.ServerAssetInformation)


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

    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    total = len(profile_obj)
    not_exists = 0
    verified_pass = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("verifying Connections info of a server profile named '%s'" % profile.name)
        #   check if server profile exists
        if not VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' does not exist" % profile.name)
            not_exists += 1
            continue
        CommonOperationServerProfile.click_server_profile(profile_name=profile.name, time_for_loading=4)
        #   check if already powered off
        FusionUIBase.select_view_by_name(view_name='Connections', timeout=5, fail_if_false=False)
        conn_verify = profile.Connections.Verify

        for m, conn in enumerate(conn_verify):

            result = {}
            conn_num = m + 1

            # Expand the connection to for verification
            FusionUIBase.wait_for_element_and_click(GeneralServerProfilesElements.Connection.ID_TABLE_CONNECTION_DETAIL_INFO % conn_num, timeout=5, fail_if_false=False)

            if hasattr(conn, 'name'):
                if not VerifyServerProfile.verify_connections_name(expect_value=conn.name, number=conn_num, timeout=7, fail_if_false=False):
                    logger.warn("'connect name' of server profile '%s' is not '%s', verification failed." % (profile.name, conn.name))
                    result['Connection Name'] = False
                else:
                    result['Connection Name'] = True

            if hasattr(conn, 'port'):
                if not VerifyServerProfile.verify_connections_port(expect_value=conn.port, number=conn_num, timeout=7, fail_if_false=False):
                    logger.warn("'connect port' of server profile '%s' is not '%s', verification failed." % (profile.name, conn.port))
                    result['Connection Port'] = False
                else:
                    result['Connection Port'] = True

            if hasattr(conn, 'network'):
                if not VerifyServerProfile.verify_connections_network(expect_value=conn.network, number=conn_num, timeout=7, fail_if_false=False):
                    logger.warn("'connect network' of server profile '%s' is not '%s', verification failed." % (profile.name, conn.network))
                    result['Connection Network'] = False
                else:
                    result['Connection Network'] = True

            if hasattr(conn, 'boot'):
                if not VerifyServerProfile.verify_connections_boot(expect_value=conn.boot, number=conn_num, timeout=7, fail_if_false=False):
                    logger.warn("'connect boot' of server profile '%s' is not '%s', verification failed." % (profile.name, conn.boot))
                    result['Connection Boot'] = False
                else:
                    result['Connection Boot'] = True

            if hasattr(conn, 'FunctionType'):
                logger.info("Verifying connection '%s' is Type '%s" % (conn.name, conn.FunctionType))
                if VerifyServerProfile.verify_connection_type(conn.FunctionType):
                    logger.info("Connection 'Type' contains expected value '%s'" % conn.FunctionType)

            if hasattr(conn, 'RequestedBandwidth'):
                if not conn.RequestedBandwidth.lower() == "auto":
                    request_bandwidth = conn.RequestedBandwidth + ' Gb/s'
                else:
                    request_bandwidth = conn.RequestedBandwidth
                if not VerifyServerProfile.verify_connections_requestedbandwidth(expect_value=request_bandwidth, timeout=7, fail_if_false=False):
                    logger.warn("'connect RequestedBandwidth' of server profile '%s' is not '%s', verification failed." % (profile.name, request_bandwidth))
                    result['Connection requestedbandwidth'] = False
                else:
                    result['Connection requestedbandwidth'] = True

            if hasattr(conn, 'MaxBandwidth'):
                max_bandwidth = conn.MaxBandwidth + ' Gb/s'
                if not VerifyServerProfile.verify_connections_maxbandwidth(expect_value=max_bandwidth, timeout=7, fail_if_false=False):
                    logger.warn("'connect RequestedBandwidth' of server profile '%s' is not '%s', verification failed." % (profile.name, max_bandwidth))
                    result['Connection requestedbandwidth'] = False
                else:
                    result['Connection requestedbandwidth'] = True

            if hasattr(conn, 'RequestedVirtualFunctions'):
                if not VerifyServerProfile.verify_connections_requested_virtual_functions_type(expect_value=conn.RequestedVirtualFunctions, timeout=15, fail_if_false=False):
                    logger.warn("The expected value '%s' was not found from the attribute 'Requested virtual functions' of connection '%s' of server profile '%s'." % (conn.RequestedVirtualFunctions, conn.name, profile.name))
                    result['Connection RequestedVirtualFunctions'] = False
                else:
                    logger.info("The expected value '%s' was found from the attribute 'Requested virtual functions' of connection '%s' of server profile '%s'." % (conn.RequestedVirtualFunctions, conn.name, profile.name))
                    result['Connection RequestedVirtualFunctions'] = True

            if hasattr(conn, 'Interconnect'):
                if not VerifyServerProfile.verify_connections_interconnect(expect_value=conn.Interconnect, timeout=15, fail_if_false=False):
                    logger.warn("The expected value '%s' was not found from the attribute 'Interconnect' of connection '%s' of server profile '%s'." % (conn.Interconnect, conn.name, profile.name))
                    result['Connection Interconnect'] = False
                else:
                    logger.info("The expected value '%s' was found from the attribute 'Interconnect' of connection '%s' of server profile '%s'." % (conn.Interconnect, conn.name, profile.name))
                    result['Connection Interconnect'] = True

            if hasattr(conn, 'IsRequestedVirtualFunctionsDisplayed'):
                if getattr(conn, 'IsRequestedVirtualFunctionsDisplayed', '').lower() == 'yes':
                    if not VerifyServerProfile.verify_connections_requested_virtual_functions_visible(timeout=15):
                        logger.warn("The attribute 'Requested virtual functions' of connection '%s' of server profile '%s' is not visible" % (conn.name, profile.name))
                        result['Connection IsRequestedVirtualFunctionsDisplayed'] = False
                    else:
                        logger.info("The attribute 'Requested virtual functions' of connection '%s' of server profile '%s' is visible." % (conn.name, profile.name))
                        result['Connection IsRequestedVirtualFunctionsDisplayed'] = True
                if getattr(conn, 'IsRequestedVirtualFunctionsDisplayed', '').lower() == 'no':
                    if not VerifyServerProfile.verify_connections_requested_virtual_functions_not_visible(timeout=15):
                        logger.warn("The attribute 'Requested virtual functions' of connection '%s' of server profile '%s' is visible" % (conn.name, profile.name))
                        result['Connection IsRequestedVirtualFunctionsDisplayed'] = False
                    else:
                        logger.info("The attribute 'Requested virtual functions' of connection '%s' of server profile '%s' is not visible" % (conn.name, profile.name))
                        result['Connection IsRequestedVirtualFunctionsDisplayed'] = True

            if hasattr(conn, 'IsAllocatedVirtualFunctionsDisplayed'):
                if getattr(conn, 'IsAllocatedVirtualFunctionsDisplayed', '').lower() == 'yes':
                    if not VerifyServerProfile.verify_connections_allocated_virtual_functions_visible(timeout=15):
                        logger.warn("The attribute 'Allocated virtual functions' of connection '%s' of server profile '%s' is not visible" % (conn.name, profile.name))
                        result['Connection IsAllocatedVirtualFunctionsDisplayed'] = False
                    else:
                        logger.info("The attribute 'Allocated virtual functions' of connection '%s' of server profile '%s' is visible" % (conn.name, profile.name))
                        result['Connection IsAllocatedVirtualFunctionsDisplayed'] = True
                if getattr(conn, 'IsAllocatedVirtualFunctionsDisplayed', '').lower() == 'no':
                    if not VerifyServerProfile.verify_connections_allocated_virtual_functions_not_visible(timeout=15):
                        logger.warn("The attribute 'Allocated virtual functions' of connection '%s' of server profile '%s' is visible" % (conn.name, profile.name))
                        result['Connection IsAllocatedVirtualFunctionsDisplayed'] = False
                    else:
                        logger.info("The attribute 'Allocated virtual functions' of connection '%s' of server profile '%s' is not visible" % (conn.name, profile.name))
                        result['Connection IsAllocatedVirtualFunctionsDisplayed'] = True

            if hasattr(conn, 'IsAllocatedBandwidthDisplayed'):
                if getattr(conn, 'IsAllocatedBandwidthDisplayed', '').lower() == 'yes':
                    if not VerifyServerProfile.verify_connections_allocated_bandwidth_visible(timeout=15):
                        logger.warn("The attribute 'Allocated bandwidth' of connection '%s' of server profile '%s' is not visible" % (conn.name, profile.name))
                        result['Connection IsAllocatedBandwidthDisplayed'] = False
                    else:
                        logger.info("The attribute 'Allocated bandwidth' of connection '%s' of server profile '%s' is visible" % (conn.name, profile.name))
                        result['Connection IsAllocatedVirtualFunctionsDisplayed'] = True
                if getattr(conn, 'IsAllocatedVirtualFunctionsDisplayed', '').lower() == 'no':
                    if not VerifyServerProfile.verify_connections_allocated_bandwidth_not_visible(timeout=15):
                        logger.warn("The attribute 'Allocated bandwidth' of connection '%s' of server profile '%s' is visible" % (conn.name, profile.name))
                        result['Connection IsAllocatedBandwidthDisplayed'] = False
                    else:
                        logger.info("The attribute 'Allocated bandwidth' of connection '%s' of server profile '%s' is not visible" % (conn.name, profile.name))
                        result['Connection IsAllocatedVirtualFunctionsDisplayed'] = True

            if hasattr(conn, 'IsMaxBandwidthDisplyed'):
                if getattr(conn, 'IsMaxBandwidthDisplyed', '').lower() == 'yes':
                    if not VerifyServerProfile.verify_connections_max_bandwidth_visible(timeout=15):
                        logger.warn("The attribute 'Max bandwidth' of connection '%s' of server profile '%s' is not visible" % (conn.name, profile.name))
                        result['Connection IsMaxBandwidthDisplyed'] = False
                    else:
                        logger.info("The attribute 'Max bandwidth' of connection '%s' of server profile '%s' is visible" % (conn.name, profile.name))
                        result['Connection IsMaxBandwidthDisplyed'] = True
                if getattr(conn, 'IsMaxBandwidthDisplyed', '').lower() == 'no':
                    if not VerifyServerProfile.verify_connections_max_bandwidth_not_visible(timeout=15):
                        logger.warn("The attribute 'Max bandwidth' of connection '%s' of server profile '%s' is visible" % (conn.name, profile.name))
                        result['Connection IsMaxBandwidthDisplyed'] = False
                    else:
                        logger.info("The attribute 'Max bandwidth' of connection '%s' of server profile '%s' is not visible" % (conn.name, profile.name))
                        result['Connection IsMaxBandwidthDisplyed'] = True

            if hasattr(conn, 'ConnectionStatus'):
                if not VerifyServerProfile.verify_connection_status(name=conn.name, expect_value=conn.ConnectionStatus, timeout=15, fail_if_false=False):
                    logger.warn("The connection '%s' of server profile '%s' status is not '%s'." % (conn.name, profile.name, conn.ConnectionStatus))
                    result['Connection ConnectionStatus'] = False
                else:
                    logger.info("The connection '%s' of server profile '%s' status is '%s'." % (conn.name, profile.name, conn.ConnectionStatus))
                    result['Connection ConnectionStatus'] = True

            if hasattr(conn, 'MACAddress'):

                if not VerifyServerProfile.verify_connections_macaddress_type(expect_value=conn.MACAddress, timeout=15, fail_if_false=False):
                    logger.warn("'connect MACAddress' of server profile '%s' is not '%s', verification failed." % (profile.name, conn.MACAddress))
                    result['Connection Macaddress'] = False
                else:
                    logger.info("success")
                    result['Connection Macaddress'] = True

            if hasattr(conn, 'WWPN'):

                if not VerifyServerProfile.verify_connections_wwpn(expect_value=conn.WWPN, timeout=15, fail_if_false=False):
                    logger.warn("'WWPN' of server profile '%s' is not '%s', verification failed." % (profile.name, conn.WWPN))
                    result['WWPN'] = False
                else:
                    logger.info("success")
                    result['WWPN'] = True

            if hasattr(conn, 'WWNN'):

                if not VerifyServerProfile.verify_connections_wwnn(expect_value=conn.WWNN, timeout=15, fail_if_false=False):
                    logger.warn("'WWNN' of server profile '%s' is not '%s', verification failed." % (profile.name, conn.WWNN))
                    result['WWNN'] = False
                else:
                    logger.info("success")
                    result['WWNN'] = True

            if hasattr(conn, 'BootVolume'):

                if not VerifyServerProfile.verify_connections_boot_volume(expect_value=conn.BootVolume, timeout=15, fail_if_false=False):
                    logger.warn("'BOOT volume' of server profile '%s' is not '%s', verification failed." % (profile.name, conn.BootVolume))
                    result['BootVolume'] = False
                else:
                    logger.info("success")
                    result['BootVolume'] = True

            if hasattr(conn, 'BootTarget'):

                if not VerifyServerProfile.verify_connections_boot_target(expect_value=conn.BootTarget, timeout=15, fail_if_false=False):
                    logger.warn("'BootTarget' of server profile '%s' is not '%s', verification failed." % (profile.name, conn.BootTarget))
                    result['BootTarget'] = False
                else:
                    logger.info("success")
                    result['BootTarget'] = True

            if hasattr(conn, 'BootLUN'):

                if not VerifyServerProfile.verify_connections_boot_lun(expect_value=conn.BootLUN, timeout=15, fail_if_false=False):
                    logger.warn("'BootLUN' of server profile '%s' is not '%s', verification failed." % (profile.name, conn.BootLUN))
                    result['BootLUN'] = False
                else:
                    logger.info("success")
                    result['BootLUN'] = True

            if hasattr(conn, 'initiatorName'):
                logger.info("Verifying connection '%s' has Initiator name '%s" % (conn.name, conn.initiatorName))
                if VerifyServerProfile.verify_connection_initiator_name(conn.initiatorName):
                    logger.info("Connection 'Initiator name' contains expected value '%s'" % conn.initiatorName)

            if hasattr(conn, 'initiatorIpv4'):
                logger.info("Verifying connection '%s' has Initiator IP address '%s" % (conn.name, conn.initiatorIpv4))
                if VerifyServerProfile.verify_connection_initiator_ip(conn.initiatorIpv4):
                    logger.info("Connection 'Initiator IP address' contains expected value '%s'" % conn.initiatorIpv4)

            if hasattr(conn, 'subnetMask'):
                logger.info("Verifying connection '%s' has Initiator subnet mask '%s" % (conn.name, conn.subnetMask))
                if VerifyServerProfile.verify_connection_initiator_subnet_mask(conn.subnetMask):
                    logger.info("Connection 'Initiator subnet mask' contains expected value '%s'" % conn.subnetMask)

            if hasattr(conn, 'gateway'):
                logger.info("Verifying connection '%s' has Initiator gateway '%s" % (conn.name, conn.gateway))
                if VerifyServerProfile.verify_connection_initiator_gateway(conn.gateway):
                    logger.info("Connection 'Initiator gateway' contains expected value '%s'" % conn.gateway)

            if hasattr(conn, 'targetName'):
                logger.info("Verifying connection '%s' has Target name '%s" % (conn.name, conn.targetName))
                if VerifyServerProfile.verify_connection_target_name(conn.targetName):
                    logger.info("Connection 'Target name' contains expected value '%s'" % conn.targetName)

            if hasattr(conn, 'targetLun'):
                logger.info("Verifying connection '%s' has Target LUN '%s" % (conn.name, conn.targetLun))
                if VerifyServerProfile.verify_connection_target_lun(conn.targetLun):
                    logger.info("Connection 'Target LUN' contains expected value '%s'" % conn.targetLun)

            if hasattr(conn, 'targetIp'):
                target_ip = ':'.join([conn.targetIp, conn.targetPort])
                logger.info("Verifying connection '%s' has Target IP address '%s'" % (conn.name, target_ip))
                if VerifyServerProfile.verify_connection_target_ip(target_ip):
                    logger.info("Connection 'Target IP address' contains expected value '%s'" % target_ip)

            if hasattr(conn, 'secondIp'):
                second_ip = ':'.join([conn.secondIp, conn.secondPort])
                logger.info("Verifying connection '%s' has Second IP address '%s" % (conn.name, second_ip))
                if VerifyServerProfile.verify_connection_second_ip(second_ip):
                    logger.info("Connection 'Second IP address' contains expected value '%s'" % second_ip)

            if hasattr(conn, 'chapLvl'):
                if conn.chapLvl == 'None':
                    VerifyServerProfile.verify_connection_chap_name("not set")
                    VerifyServerProfile.verify_connection_mchap_name_not_visible()
                elif conn.chapLvl == 'CHAP':
                    VerifyServerProfile.verify_connection_chap_name(conn.chapName)
                    VerifyServerProfile.verify_connection_mchap_name_not_visible()
                elif conn.chapLvl == 'Mutual CHAP':
                    VerifyServerProfile.verify_connection_chap_name(conn.chapName)
                    VerifyServerProfile.verify_connection_mchap_name(conn.mchapName)

            if all(result.values()) is not True:
                logger.warn("server profile '%s' is FAIL for connections info verification" % profile.name)
                return False
            else:
                logger.info("server profile '%s' is PASS for connections info verification" % profile.name)

            # Collapse the connection after verification
            FusionUIBase.wait_for_element_and_click(GeneralServerProfilesElements.Connection.ID_TABLE_CONNECTION_DETAIL_INFO_EXPAND % conn_num, timeout=5, fail_if_false=False)

        verified_pass += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no server profile to verify connections info against! all %s server profile(s) is NOT existing, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if verified_pass < total:
            logger.warn("not all of the server profile(s) is successfully verified PASS - %s out of %s passed " % (verified_pass, total))
            if verified_pass + not_exists == total:
                # logger.warn("%s not-existing server profile(s) is skipped, test is considered FAIL" % not_exists)
                logger.warn("%s not-existing server profile(s) is skipped, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s not-existing server profile(s) is skipped, "
                            "%s server profile(s) left is failed being verified PASS " % (not_exists, total - verified_pass - not_exists))
                return False

    logger.info("all of the server profile(s) is successfully verified PASS - %s out of %s " % (verified_pass, total))
    return True


def verify_server_profile_advanced_info(*profile_obj):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    total = len(profile_obj)
    not_exists = 0
    verified_pass = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("verifying Advanced info of a server profile named '%s'" % profile.name)
        #   check if server profile exists
        if not VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' does not exist" % profile.name)
            not_exists += 1
            continue
        CommonOperationServerProfile.click_server_profile(profile_name=profile.name, time_for_loading=4)
        #   check if already powered off
        FusionUIBase.select_view_by_name(view_name='Advanced', timeout=5, fail_if_false=False)
        advanced = profile.Advanced

        result = {}

        if hasattr(advanced, 'iscsi'):
            VerifyServerProfile.verify_advanced_iscsi_initiator_name(expect_value=advanced.iscsi, timeout=7, fail_if_false=True)

        if hasattr(advanced, 'serial'):
            if not VerifyServerProfile.verify_advance_uuid(expect_value=advanced.serial, timeout=7, fail_if_false=False):
                logger.warn("'UUID' of server profile '%s' is not '%s', verification failed." % (profile.name, advanced.serial))
                result['UUID'] = False
            else:
                result['UUID'] = True

        if hasattr(advanced, 'mac'):
            if not VerifyServerProfile.verify_advance_mac_addresses(expect_value=advanced.mac, timeout=7, fail_if_false=False):
                logger.warn("'MAC addresses' of server profile '%s' is not '%s', verification failed." % (profile.name, advanced.mac))
                result['MAC addresses'] = False
            else:
                result['MAC addresses'] = True

        if hasattr(advanced, 'wwn'):
            if not VerifyServerProfile.verify_advance_wwn_addresses(expect_value=advanced.wwn, timeout=7, fail_if_false=False):
                logger.warn("'WWN addresses' of server profile '%s' is not '%s', verification failed." % (profile.name, advanced.wwn))
                result['WWN addresses'] = False
            else:
                result['WWN addresses'] = True

        if hasattr(advanced, 'HideUnusedFlexNICs'):
            if not VerifyServerProfile.verify_advance_hide_unused_flexnics(expect_value=advanced.HideUnusedFlexNICs, timeout=7, fail_if_false=False):
                logger.warn("'Hide unused FlexNICs' of server profile '%s' is not '%s', verification failed." % (profile.name, advanced.HideUnusedFlexNICs))
                result['Hide unused FlexNICs'] = False
            else:
                result['Hide unused FlexNICs'] = True

        if all(result.values()) is not True:
            logger.warn("server profile '%s' is FAIL for advanced info verification" % profile.name)
        else:
            logger.info("server profile '%s' is PASS for advanced info verification" % profile.name)

        verified_pass += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no server profile to verify advanced info against! all %s server profile(s) is NOT existing, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if verified_pass < total:
            logger.warn("not all of the server profile(s) is successfully verified PASS - %s out of %s passed " % (verified_pass, total))
            if verified_pass + not_exists == total:
                # logger.warn("%s not-existing server profile(s) is skipped, test is considered FAIL" % not_exists)
                logger.warn("%s not-existing server profile(s) is skipped, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s not-existing server profile(s) is skipped, "
                            "%s server profile(s) left is failed being verified PASS " % (not_exists, total - verified_pass - not_exists))
                return False

    logger.info("all of the server profile(s) is successfully verified PASS - %s out of %s " % (verified_pass, total))
    return True


def verify_server_profile_local_storage_info(*profile_obj):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    total = len(profile_obj)
    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("verifying Local storage info of a server profile named '%s'" % profile.name)
        #   check if server profile exists
        if not VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' does not exist" % profile.name)
            continue
        CommonOperationServerProfile.click_server_profile(profile_name=profile.name, time_for_loading=4)
        FusionUIBase.select_view_by_name(view_name='Local Storage', timeout=5, fail_if_false=False)

        if hasattr(profile, 'LocalStorage'):
            logger.info("test data for 'Local Storage' is found")
            local_storage = profile.LocalStorage
        else:
            msg = "Can not found test data for 'Local Storage', test failed!"
            ui_lib.fail_test(msg)

        if hasattr(local_storage, 'integratedControllerMode'):
            logger.info("Verifying Integrated Controller Mode")
            VerifyServerProfile.verify_integrated_storage_mode(expect_value=local_storage.integratedControllerMode, timeout=10, fail_if_false=True)
            if hasattr(local_storage, 'LogicalDrives'):
                logger.info("test data for 'Logical Drives' is found")
                local_storage = profile.LocalStorage
                logical_drives = local_storage.LogicalDrives
                if hasattr(logical_drives, 'Verify') and len(logical_drives.Verify) != []:
                    verification = logical_drives.Verify
                    for verify in verification:
                        if hasattr(verify, 'name'):
                            VerifyServerProfile.verify_logical_drive_name(expect_value=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'LogicalDrive'):
                            VerifyServerProfile.verify_logical_drive_drive_num(expect_value=verify.LogicalDrive, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'RAIDlevel'):
                            VerifyServerProfile.verify_logical_drive_raid_level(expect_value=verify.RAIDLevel, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'NumberOfPhysicalDrives'):
                            VerifyServerProfile.verify_logical_drive_num_of_drives(expect_value=verify.NumberOfPhysicalDrives, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'minSize'):
                            VerifyServerProfile.verify_logical_drive_min_gb(expect_value=verify.minSize, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'maxSize'):
                            VerifyServerProfile.verify_logical_drive_max_gb(expect_value=verify.maxSize, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'DriveTechnology'):
                            VerifyServerProfile.verify_logical_drive_drive_tech(expect_value=verify.DriveTechnology, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'boot'):
                            VerifyServerProfile.verify_logical_drive_boot(expect_value=verify.boot, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'status'):
                            VerifyServerProfile.verify_logical_drive_status(expect_value=verify.status, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'pending') and verify.pending.lower() == 'true':
                            VerifyServerProfile.verify_logical_drive_pending_state(drivename=verify.name, timeout=10, fail_if_false=True)

                else:
                    msg = "Test data failed, please ensure the 'Verify' node exists and its sub-node is not null in LogicalDrives"
                    ui_lib.fail_test(msg)

        if hasattr(local_storage, 'mezzControllerMode'):
            logger.info("Verifying Mezz Controller Mode")
            VerifyServerProfile.verify_mezz_storage_mode(mezzID=local_storage.mezzControllerID, expect_value=local_storage.mezzControllerMode, timeout=10, fail_if_false=True)
            if hasattr(local_storage, 'LogicalJBODs'):
                logger.info("test data for 'Logical JBODs' is found")
                local_storage = profile.LocalStorage
                logical_JBODs = local_storage.LogicalJBODs
                if hasattr(logical_JBODs, 'Verify') and len(logical_JBODs.Verify) != []:
                    verification = logical_JBODs.Verify
                    for verify in verification:
                        if hasattr(verify, 'name'):
                            VerifyServerProfile.verify_logical_jbod_name(mezzID=local_storage.mezzControllerID, expect_value=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'LogicalDrive'):
                            VerifyServerProfile.verify_logical_jbod_drive_num(mezzID=local_storage.mezzControllerID, expect_value=verify.LogicalDrive, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'RAIDlevel'):
                            VerifyServerProfile.verify_logical_jbod_raid_level(mezzID=local_storage.mezzControllerID, expect_value=verify.RAIDLevel, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'NumberOfPhysicalDrives'):
                            VerifyServerProfile.verify_logical_jbod_num_of_drives(mezzID=local_storage.mezzControllerID, expect_value=verify.NumberOfPhysicalDrives, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'minSize'):
                            VerifyServerProfile.verify_logical_jbod_min_gb(mezzID=local_storage.mezzControllerID, expect_value=verify.minSize, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'maxSize'):
                            VerifyServerProfile.verify_logical_jbod_max_gb(mezzID=local_storage.mezzControllerID, expect_value=verify.maxSize, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'DriveTechnology'):
                            VerifyServerProfile.verify_logical_jbod_drive_tech(mezzID=local_storage.mezzControllerID, expect_value=verify.DriveTechnology, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'boot'):
                            VerifyServerProfile.verify_logical_jbod_boot(mezzID=local_storage.mezzControllerID, expect_value=verify.boot, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'status'):
                            VerifyServerProfile.verify_logical_jbod_status(mezzID=local_storage.mezzControllerID, expect_value=verify.status, drivename=verify.name, timeout=10, fail_if_false=True)

                        if hasattr(verify, 'pending') and verify.pending.lower() == 'true':
                            VerifyServerProfile.verify_logical_jbod_pending_state(mezzID=local_storage.mezzControllerID, drivename=verify.name, timeout=10, fail_if_false=True)

                else:
                    msg = "Test data failed, please ensure the 'Verify' node exists and its sub-node is not null in LogicalJBODs"
                    ui_lib.fail_test(msg)


def verify_server_profile_zoned_drive_exist(*profile_obj):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    total = len(profile_obj)
    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("verifying zoned drive exist for server profile named '%s'" % profile.name)
        #   check if server profile exists
        if not VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' does not exist" % profile.name)
            continue
        CommonOperationServerProfile.click_server_profile(profile_name=profile.name, time_for_loading=4)
        FusionUIBase.select_view_by_name(view_name='Local Storage', timeout=5, fail_if_false=False)

        if hasattr(profile, 'LocalStorage'):
            logger.info("test data for 'Local Storage' is found")
            local_storage = profile.LocalStorage
        else:
            msg = "Can not found test data for 'Local Storage', test failed!"
            ui_lib.fail_test(msg)
        if hasattr(local_storage, 'LogicalJBODs'):
            logger.info("test data for 'Logical JBODs' is found")
            local_storage = profile.LocalStorage
            logical_JBODs = local_storage.LogicalJBODs
            if hasattr(logical_JBODs, 'Verify') and len(logical_JBODs.Verify) != []:
                verification = logical_JBODs.Verify
                verify_zoned_drives = []
                for verify in verification:
                    drivenum = 1
                    if hasattr(verify, 'name'):
                        VerifyServerProfile.click_logical_jbod_expand(local_storage.mezzControllerID, verify.name)
                        physical_drives = int(verify.NumberOfPhysicalDrives)
                        FusionUIBase.select_view_by_name(view_name='Local Storage', timeout=5, fail_if_false=False)
                        while drivenum <= physical_drives:
                            driveinfo = VerifyServerProfile.get_zoned_hard_drive_info(local_storage.mezzControllerID, verify.name, str(drivenum), profile.name)
                            verify_zoned_drives.append(driveinfo)
                            drivenum += 1
                FusionUIBase.navigate_to_section(SectionType.DRIVE_ENCLOSURES)
                for zoned_drive in verify_zoned_drives:
                    FusionUIBase.click_item_from_master_table(zoned_drive['drive_encl'])
                    FusionUIBase.select_view_by_name('Drives')
                    logger.debug('Validating zoned drive number %s has server profile -- %s ' % (zoned_drive['bay_number'], zoned_drive['server_profile']))
                    VerifyServerProfile.verify_hdd_view_drive_server_profile(zoned_drive)
                    logger.debug('Validating zoned drive number %s has capacity size %s ' % (zoned_drive['bay_number'], zoned_drive['size']))
                    VerifyServerProfile.verify_hdd_view_drive_capacity(zoned_drive)
                    logger.debug('Validating zoned drive number %s  has Jbod name %s ' % (zoned_drive['bay_number'], zoned_drive['jbod_name']))
                    VerifyServerProfile.verify_hdd_view_drive_logical_jbod(zoned_drive)


def verify_server_profile_zoned_drive_deleted(*zoneddrives):
    """ """
    FusionUIBase.navigate_to_section(SectionType.DRIVE_ENCLOSURES)
    if isinstance(zoneddrives, test_data.DataObj):
        zoneddrives = [zoneddrives]
    elif isinstance(zoneddrives, tuple):
        zoneddrives = list(zoneddrives[0])

    for zoned_drive in zoneddrives:
        for drive in zoned_drive:
            logger.debug('Previous drive server profile is %s and setting to None' % (drive['server_profile']))
            drive['server_profile'] = 'none'
            logger.debug('Previous drive jbod name  is %s and setting to None' % (drive['jbod_name']))
            drive['jbod_name'] = 'none'
            FusionUIBase.click_item_from_master_table(drive['drive_encl'])
            FusionUIBase.select_view_by_name('Drives')
            logger.debug('Validating zoned drive number %s has server profile -- %s ' % (drive['bay_number'], drive['server_profile']))
            VerifyServerProfile.verify_hdd_view_drive_server_profile(drive)
            logger.debug('Validating zoned drive number %s has capacity size %s ' % (drive['bay_number'], drive['size']))
            VerifyServerProfile.verify_hdd_view_drive_capacity(drive)
            logger.debug('Validating zoned drive number %s  has Jbod name %s ' % (drive['bay_number'], drive['jbod_name']))
            VerifyServerProfile.verify_hdd_view_drive_logical_jbod(drive)


def get_zoned_drive_info(*profile_obj):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    total = len(profile_obj)
    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("verifying zoned drive exist for server profile named '%s'" % profile.name)
        #   check if server profile exists
        if not VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' does not exist" % profile.name)
            continue
        CommonOperationServerProfile.click_server_profile(profile_name=profile.name, time_for_loading=4)
        FusionUIBase.select_view_by_name(view_name='Local Storage', timeout=5, fail_if_false=False)

        if hasattr(profile, 'LocalStorage'):
            logger.info("test data for 'Local Storage' is found")
            local_storage = profile.LocalStorage
        else:
            msg = "Can not found test data for 'Local Storage', test failed!"
            ui_lib.fail_test(msg)
        if hasattr(local_storage, 'LogicalJBODs'):
            logger.info("test data for 'Logical JBODs' is found")
            local_storage = profile.LocalStorage
            logical_JBODs = local_storage.LogicalJBODs
            if hasattr(logical_JBODs, 'Verify') and len(logical_JBODs.Verify) != []:
                verification = logical_JBODs.Verify
                zoned_drives_info = []
                for verify in verification:
                    drivenum = 1
                    if hasattr(verify, 'name'):
                        VerifyServerProfile.click_logical_jbod_expand(local_storage.mezzControllerID, verify.name)
                        physical_drives = int(verify.NumberOfPhysicalDrives)
                        FusionUIBase.select_view_by_name(view_name='Local Storage', timeout=5, fail_if_false=False)
                        while drivenum <= physical_drives:
                            driveinfo = VerifyServerProfile.get_zoned_hard_drive_info(local_storage.mezzControllerID, verify.name, str(drivenum), profile.name)
                            zoned_drives_info.append(driveinfo)
                            drivenum += 1
        return zoned_drives_info


def verify_server_profile_san_storage_info(*profile_obj):
    """
    Verify the san storage information, you should modify the data file according to the server profile you created/edited
    Arguments:
      name             --  Name of server hardware as a string.
      LUN              --  The LUN id of volume was allocated.
      StoragePool      --  Storage pool name this volume using.
      Capacity         --  Granted capacity for this volume.
      Provisioning     --  Style of volume storage space pre-allocation
      Permanent        --  The volume will be deleted when permanent was set to "false", otherwise, it will be kept.
      StoragePaths     --  The node used to define paths information need to be validated.
      network          --  Fabric channel name this volume using.
      enabled          --  The FC status, the false means it was not used.

    * Required Arguments

    Example:
    <ServerProfile>
        <Create>
            <profile name="SP_For_SPBLp0014" desc="Create SP for SPBLp0014" server="wpst23, bay 3" hardwareType="BL465c Gen8" enclgroup="GRP-wpst23" Affinity="Device bay">
                <SANStorage osType="Windows 2012 / WS2012 R2">
                    <Volumes>
                        <Add>
                            <volume name="VOLUME_FOR_FA_NEW" type="New volume" LUN="Auto" StoragePool="FC_wpst23_r5" Capacity="10" Provisioning="Thin" Permanent="false">
                                <StoragePaths>
                                    <Add>
                                        <StoragePath network="FA1" TargetPortAssignment="Auto" enabled="true" />
                                        <StoragePath network="FA2" TargetPortAssignment="Auto" enabled="true" />
                                    </Add>
                                    <Edit><None/></Edit>
                                    <Delete><None/></Delete>
                                </StoragePaths>
                            </volume>
                            <volume name="VOLUME_FOR_DA_NEW" type="New volume" LUN="Auto" StoragePool="FC_wpst23_r5" Capacity="10" Provisioning="Thin" Permanent="false">
                                <StoragePaths>
                                    <Add>
                                        <StoragePath network="DA1" enabled="true" />
                                        <StoragePath network="DA2" enabled="true" />
                                    </Add>
                                    <Edit><None/></Edit>
                                    <Delete><None/></Delete>
                                </StoragePaths>
                            </volume>
                        </Add>
                        <Edit><None/></Edit>
                        <Delete><None/></Delete>
                        <Verify>
                             <volume name="VOLUME_FOR_FA_NEW" LUN="0" StoragePool="FC_wpst23_r5" Capacity="10" Provisioning="Thin" Permanent="false" Sharing="Private">
                                <StoragePaths>
                                    <StoragePath network="FA1" enabled="true" />
                                    <StoragePath network="FA2" enabled="true" />
                                </StoragePaths>
                            </volume>
                            <volume name="VOLUME_FOR_DA_NEW" LUN="1" StoragePool="FC_wpst23_r5" Capacity="10" Provisioning="Thin" Permanent="false" Sharing="Private">
                                <StoragePaths>
                                    <StoragePath network="DA1" enabled="true" />
                                    <StoragePath network="DA2" enabled="true" />
                                </StoragePaths>
                            </volume>
                        </Verify>
                    </Volumes>
                </SANStorage>
            </profile>
        </Create>
        <Edit>
            <profile name="SP_For_SPBLp0014" desc="Create SP for SPBLp0014" server="wpst23, bay 3" hardwareType="BL465c Gen8" enclgroup="GRP-wpst23" Affinity="Device bay">
                <SANStorage osType="Windows 2012 / WS2012 R2">
                    <Volumes>
                        <Add><None/></Add>
                        <Edit><None/></Edit>
                        <Delete>
                            <volume name="VOLUME_FOR_FA_NEW" />
                            <volume name="VOLUME_FOR_DA_NEW" />
                        </Delete>
                        <Verify>
                             <volume><None/></volume>
                        </Verify>
                    </Volumes>
                </SANStorage>
            </profile>
        </Edit>
    </ServerProfile>
    """

    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    total = len(profile_obj)
    not_exists = 0
    verified_pass = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("verifying SAN storage info of a server profile named '%s'" % profile.name)
        #   check if server profile exists
        if not VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' does not exist" % profile.name)
            not_exists += 1
            continue
        CommonOperationServerProfile.click_server_profile(profile_name=profile.name, time_for_loading=4)
        FusionUIBase.select_view_by_name(view_name='SAN Storage', timeout=5, fail_if_false=False)

        if hasattr(profile, 'SANStorage'):
            logger.info("test data for 'SAN Storage' is found")
            san_storage = profile.SANStorage
        else:
            msg = "Can not found test data for 'SAN Storage', test failed!"
            ui_lib.fail_test(msg)

        result = {}

        if hasattr(san_storage, 'osType'):
            if not VerifyServerProfile.verify_host_os_type(expect_value=san_storage.osType, timeout=7, fail_if_false=False):
                logger.warn("'osType' of server profile '%s' is not '%s', verification failed." % (profile.name, san_storage.osType))
                result['osType'] = False
            else:
                result['osType'] = True

        if hasattr(san_storage, 'Volumes'):
            logger.info("test data for 'Volumes' is found")
            san_storage = profile.SANStorage
            volumes = san_storage.Volumes

            if VerifyServerProfile.verify_no_volume_attachment_added(timeout=7, fail_if_false=False):
                logger.info("No any volume was added into this server profile")
                result['message'] = True

            elif hasattr(volumes, 'Verify') and len(volumes.Verify) != []:
                verification = volumes.Verify
                for m, verify in enumerate(verification):
                    number = m + 1

                    FusionUIBase.wait_for_element_and_click(GeneralServerProfilesElements.SANStorage.Volume.ID_TABLE_SANStorage_DETAIL_INFO % number, timeout=5, fail_if_false=False)

                    if hasattr(verify, 'name'):
                        if VerifyServerProfile.verify_san_storage_volume_exist(expect_value=verify.name, number=number, timeout=7, fail_if_false=False):
                            result['vol_name_%s' % number] = True
                    else:
                        msg = "No volume name is found, mark the test case to failed"
                        ui_lib.fail_test(msg)

                    if hasattr(verify, 'LUN'):
                        if not VerifyServerProfile.verify_san_storage_lun_id(expect_value=verify.LUN, number=number, timeout=7, fail_if_false=False):
                            logger.warn("'LUN ID' of SAN storage '%s' is not '%s', verification failed." % (verify.name, verify.LUN))
                            result['LUN_%s' % number] = False
                        else:
                            result['LUN_%s' % number] = True

                    if hasattr(verify, 'StoragePool'):
                        if not VerifyServerProfile.verify_san_storage_pool(expect_value=verify.StoragePool, number=number, timeout=7, fail_if_false=False):
                            logger.warn("'StoragePool' of SAN storage '%s' is not '%s', verification failed." % (verify.name, verify.StoragePool))
                            result['StoragePool_%s' % number] = False
                        else:
                            result['StoragePool_%s' % number] = True

                    if hasattr(verify, 'Capacity'):
                        if not VerifyServerProfile.verify_san_storage_capacity(expect_value=verify.Capacity, number=number, timeout=7, fail_if_false=False):
                            logger.warn("'Capacity' of SAN storage '%s' is not '%s', verification failed." % (verify.name, verify.Capacity))
                            result['Capacity_%s' % number] = False
                        else:
                            result['Capacity_%s' % number] = True

                    if hasattr(verify, 'Provisioning'):
                        if not VerifyServerProfile.verify_san_storage_provisioning(expect_value=verify.Provisioning, number=number, timeout=7, fail_if_false=False):
                            logger.warn("'Provisioning' of SAN storage '%s' is not '%s', verification failed." % (verify.name, verify.Provisioning))
                            result['Provisioning_%s' % number] = False
                        else:
                            result['Provisioning_%s' % number] = True

                    if hasattr(verify, 'Permanent'):
                        if verify.Permanent.lower() == 'false':
                            setattr(verify, 'Permanent', 'No')
                        elif verify.Permanent.lower() == 'true':
                            setattr(verify, 'Permanent', 'Yes')

                        if not VerifyServerProfile.verify_san_storage_permanent(expect_value=verify.Permanent, number=number, timeout=7, fail_if_false=False):
                            logger.warn("'Permanent' of SAN storage '%s' is not '%s', verification failed." % (verify.name, verify.Permanent))
                            result['Permanent_%s' % number] = False
                        else:
                            result['Permanent_%s' % number] = True

                    if hasattr(verify, 'Sharing'):
                        if not VerifyServerProfile.verify_san_storage_sharing(expect_value=verify.Sharing, number=number, timeout=7, fail_if_false=False):
                            logger.warn("'Sharing' of SAN storage '%s' is not '%s', verification failed." % (verify.name, verify.Sharing))
                            result['Sharing_%s' % number] = False
                        else:
                            result['Sharing_%s' % number] = True

                    if hasattr(verify, 'StoragePaths'):
                        for num, path in enumerate(verify.StoragePaths):
                            path_num = num + 1
                            if hasattr(path, 'network'):
                                if not VerifyServerProfile.verify_san_storage_network(expect_value=path.network, number=number, sub_number=path_num, timeout=7, fail_if_false=False):
                                    logger.warn("'Storage Path' of SAN storage '%s' is not '%s', verification failed." % (verify.name, path.network))
                                    result['network_%s_%s' % (number, path_num)] = False
                                else:
                                    result['network_%s_%s' % (number, path_num)] = True

                            if hasattr(path, 'enabled'):
                                if path.enabled.lower() == 'false':
                                    setattr(path, 'enabled', 'No')
                                elif path.enabled.lower() == 'true':
                                    setattr(path, 'enabled', 'Yes')

                                if not VerifyServerProfile.verify_san_storage_network_status(expect_value=path.enabled, number=number, sub_number=path_num, timeout=7, fail_if_false=False):
                                    logger.warn("'Status' of SAN storage path '%s' is not '%s', verification failed." % (verify.name, path.enabled))
                                    result['status_%s_%s' % (number, path_num)] = False
                                else:
                                    result['status_%s_%s' % (number, path_num)] = True

            else:
                msg = "Test data failed, please ensure the 'Verify' node exists and its sub-node is not null"
                ui_lib.fail_test(msg)

        if all(result.values()) is not True:
            logger.warn("server profile '%s' is FAIL for san storage info verification" % profile.name)
        else:
            logger.info("server profile '%s' is PASS for san storage info verification" % profile.name)

        verified_pass += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no server profile to verify san storage info against! all %s server profile(s) is NOT existing, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if verified_pass < total:
            logger.warn("not all of the server profile(s) is successfully verified PASS - %s out of %s passed " % (verified_pass, total))
            if verified_pass + not_exists == total:
                # logger.warn("%s not-existing server profile(s) is skipped, test is considered FAIL" % not_exists)
                logger.warn("%s not-existing server profile(s) is skipped, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s not-existing server profile(s) is skipped, "
                            "%s server profile(s) left is failed being verified PASS " % (not_exists, total - verified_pass - not_exists))
                return False

    logger.info("all of the server profile(s) is successfully verified PASS - %s out of %s " % (verified_pass, total))
    return True


def bak_power_on_server_profile(*profile_obj):
    """ Power On Server Profile

        ProfileObj xml requires the following attributes:
            name - Comma separated string of profile names that should match
                   existing server profiles.
                   eg: <profile name="Server Profile 1, Server Profile 2">
                       <profile name="Server Profile 3">

        Example:
        | `Power On Server Profile`      |  @{profile_obj} |
    """
    selenium2lib = ui_lib.get_s2l()
    logger._log_to_console_and_log_file("")
    error = 0

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    for profile in profile_obj:
        valid_profiles = []
        excluded_profiles = []
        logger._log_to_console_and_log_file("")
        logger._log_to_console_and_log_file("Powering on server profiles '%s'" % profile.name)

        # Validate server profiles
        logger._log_to_console_and_log_file("Validating Server Profiles")
        profile_names = _split_profile_names(profile.name)
        for profile_name in profile_names:
            profile_attributes = get_server_profile_attributes(profile_name, None)
            if profile_attributes is None:
                logger._warn("Server Profile '%s' does not exist" % profile_name)
                selenium2lib.capture_page_screenshot()
                return False
            elif profile_attributes["server hardware"] == "unassigned":
                logger._warn("Cannot power on Server Profile '%s' due to unassigned server hardware" % profile_name)
                excluded_profiles.append(profile_name)
            elif profile_attributes["server power"] == "On":
                logger._warn("Server Profile '%s' is already powered on" % profile_name)
                excluded_profiles.append(profile_name)
            else:
                valid_profiles.append(profile_name)

        if len(valid_profiles) == 0:
            logger._warn("All specified Server Profiles are already powered on.")
            selenium2lib.capture_page_screenshot()
            error += 1
            continue

        # Select the profile from the left side table
        logger._log_to_console_and_log_file("Powering on Server Profiles")
        if not select_server_profile(profile.name):
            logger._warn("Failed to select server profiles")
            selenium2lib.capture_page_screenshot()
            error += 1
            continue

        # Select Power off option from Action menu
        ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_MENU_MAIN_ACTION)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_MAIN_ACTION)
        if selenium2lib._is_visible(FusionServerProfilesPage.ID_MENU_ACTION_POWERON):
            logger._log_to_console_and_log_file("Powering on selected server profiles")
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_ACTION_POWERON)
            ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_PROFILE_POWER_STATUS % "On", PerfConstants.PROFILE_POWER_VALIDATION)
            BuiltIn().sleep(10)
            logger._log_to_console_and_log_file("Successfully powered on Server Profiles")
        else:
            selenium2lib.capture_page_screenshot()
            logger._log_to_console_and_log_file("Power on option is not available in the Actions menu")
            selenium2lib.capture_page_screenshot()
            error += 1

        # Build Activity Message
        args = {}
        args["activity"] = "Power On"
        args["entity"] = get_server_profile_attributes(profile_names[0], "server hardware") if len(profile_names) == 1 else "%d server hardware" % len(profile_names)
        args["multiple"] = len(profile_names) - 1
        if args["multiple"]:
            args["completed"] = valid_profiles if len(valid_profiles) > 1 else [valid_profiles[0]]
            if len(excluded_profiles) > 0:
                args["excluded"] = excluded_profiles if len(excluded_profiles) > 1 else [excluded_profiles[0]]

        # Verify Activity
        if not _verify_activity(**args):
            logger._warn("Failed to verify Power On Activity")
            selenium2lib.capture_page_screenshot()
            error += 1
        else:
            logger._log_to_console_and_log_file("Successfully verified Power On Activity for Powering On Profile(s): '%s'" % profile.name)

    if error > 0:
        return False
    return True


def _edit_bios_setting(biossettingname, biossettingvalue):
    ''' Edit Bios Setting
    _edit_bios_setting is a private function called by create server profile function

    I/p: Bios setting names and bios setting value
    for bios in profile.bios:

    _edit_bios_setting(bios.name, bios.value)

    '''
    selenium2lib = ui_lib.get_s2l()

    if biossettingname.strip() == ("Advanced Memory Protection"):
        # if unable to find the drop down control fail the test
        if selenium2lib._is_element_present(FusionServerProfilesPage.ID_COMBO_ADV_MEMORY_PROTECTION):
            _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_ADV_MEMORY_PROTECTION, biossettingvalue)

        else:
            selenium2lib.fail_test("Not able to find the control to select the bios setting " + biossettingvalue, "True")

    #  USB options
    elif biossettingname.strip() == ("USB Boot Support"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_USB_BOOT_SUPPORT, biossettingvalue)

    elif biossettingname.strip() == ("Removable Flash Media Boot Sequence"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_USB_FLASH_MEDIA_SEQUENCE, biossettingvalue)

    # Processor Options

    elif biossettingname.strip() == ("No-Execute Memory Protection"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_NO_EXECUTE_MEM_PROTECTION, biossettingvalue)

    elif biossettingname.strip() == ("Intel(R) Virtualization Technology"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_INTEL_VITULIZATION_TECH, biossettingvalue)

    elif biossettingname.strip() == ("Intel(R) Hyperthreading Options"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_INTEL_HYPER_THREADING_OPTION, biossettingvalue)

    elif biossettingname.strip() == ("Embedded Serial Port"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_EMBEDED_SERIAL_PORT, biossettingvalue)

    # Advanced Option

    elif biossettingname.strip() == ("Video Options"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_VIDEO_OPTION, biossettingvalue)

    elif biossettingname.strip() == ("Thermal Configuration"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_THERMAL_CONFIGURATION, biossettingvalue)

    elif biossettingname.strip() == ("Asset Tag Protection"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_ASSET_TAG, biossettingvalue)

    # Advanced System ROM Options
    elif biossettingname.strip() == ("MPS Table Mode"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_MPS_TABLE_MODE, biossettingvalue)

    elif biossettingname.strip() == ("NMI Debug Button"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_NMI_DEBUG_BUTTON, biossettingvalue)

    elif biossettingname.strip() == ("Virtual Install Disk"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_VIRTUAL_INSTALL_DISK, biossettingvalue)

    elif biossettingname.strip() == ("PCI Bus Padding Options"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_PCI_BUS_PADDING_OPTION, biossettingvalue)

    elif biossettingname.strip() == ("ID_COMBO_F11_BOOT_MENU_PROMPT"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_F11_BOOT_MENU_PROMPT, biossettingvalue)

    # Advanced Performance Tuning Option
    elif biossettingname.strip() == ("HW Prefetcher"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_HW_PREFETCHER, biossettingvalue)

    elif biossettingname.strip() == ("Adjacent Sector Prefetch"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_ADJACENT_SECTOR_PREFETCH, biossettingvalue)

    elif biossettingname.strip() == ("DCU IP Prefetcher"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_DCU_IP_PREFETCHER, biossettingvalue)

    elif biossettingname.strip() == ("Node Interleaving"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_NODE_INTERLEAVING, biossettingvalue)

    elif biossettingname.strip() == ("Memory Channel Mode"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_MEMORY_CHANNEL_MODE, biossettingvalue)

    # Advanced System ROM Option

    elif biossettingname.strip() == ("MPS Table Mode"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_MPS_TABLE_MODE, biossettingvalue)

    elif biossettingname.strip() == ("NMI Debug Button"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_NMI_DEBUG_BUTTON, biossettingvalue)

    elif biossettingname.strip() == ("Virtual Install Disk"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_VIRTUAL_INSTALL_DISK, biossettingvalue)

    elif biossettingname.strip() == ("PCI Bus Padding Options"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_PCI_BUS_PADDING_OPTION, biossettingvalue)

    elif biossettingname.strip() == ("F11 Boot Menu Prompt"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_F11_BOOT_MENU_PROMPT, biossettingvalue)

    # Advanced Performance Tuning Options
    elif biossettingname.strip() == ("HW Prefetcher"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_HW_PREFETCHER, biossettingvalue)

    elif biossettingname.strip() == ("Adjacent Sector Prefetch"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_ADJACENT_SECTOR_PREFETCH, biossettingvalue)

    elif biossettingname.strip() == ("DCU Streamer Prefetcher"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_DCU_STREAMER_PREFETCHER, biossettingvalue)

    elif biossettingname.strip() == ("DCU IP Prefetcher"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_DCU_IP_PREFETCHER, biossettingvalue)

    elif biossettingname.strip() == ("Node Interleaving"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_NODE_INTERLEAVING, biossettingvalue)

    elif biossettingname.strip() == ("Data Direct I/O"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_DATA_DIRECT_IO, biossettingvalue)

    elif biossettingname.strip() == ("Memory Channel Mode"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_MEMORY_CHANNEL_MODE, biossettingvalue)

    # Power Management Options

    elif biossettingname.strip() == ("HP Power Profile"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_HP_POWER_PROFILE, biossettingvalue)

    elif biossettingname.strip() == ("HP Power Regulator"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_HP_POWER_REGULATOR, biossettingvalue)

    # Advanced Power Management Options

    elif biossettingname.strip() == ("Minimum Processor Idle Power Package State"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_MINIMUM_PROC_IDLE_POW_PACKG_STATE, biossettingvalue)

    elif biossettingname.strip() == ("Energy/Performance Bias"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_ENERGY_PERFORMANCE_BIAS, biossettingvalue)

    elif biossettingname.strip() == ("Maximum Memory Bus Frequency"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_MAX_MEMORY_BUS_FREQUENCY, biossettingvalue)

    elif biossettingname.strip() == ("Channel Interleaving"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_CHANNEL_INTERLEAVING, biossettingvalue)

    elif biossettingname.strip() == ("Maximum PCI Express Speed"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_MAXIMUM_PCI_EXPRESS_SPEED, biossettingvalue)
    # BIOS mandatory fileds update
    elif biossettingname.strip() == ("Admin Name Text"):
        ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_ADMIN_NAME_TEXT, biossettingvalue)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_EDIT_BIOS_OK)

        # validate bios setting value is reflected in the create server profile page
        if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_BIOS_UPDATED_VALUE % biossettingvalue):
            logger._log_to_console_and_log_file("failed to update the bios setting value")
            selenium2lib.fail_test("Not able to update the bios setting with value " + biossettingvalue, "True")
        else:
            logger._log_to_console_and_log_file("Bios setting is updated with value " + biossettingvalue)

    elif biossettingname.strip() == ("Admin Phone Number Text"):
        ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_ADMIN_PHONE_NUMBER, biossettingvalue)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_EDIT_BIOS_OK)

        # validate bios setting value is reflected in the create server profile page
        if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_BIOS_UPDATED_VALUE % biossettingvalue):
            logger._log_to_console_and_log_file("failed to update the bios setting value")
            selenium2lib.fail_test("Not able to update the bios setting with value " + biossettingvalue, "True")
        else:
            logger._log_to_console_and_log_file("Bios setting is updated with value " + biossettingvalue)
    # power on logo enabled
    elif biossettingname.strip() == ("Power-On Logo"):
        _edit_bios_setting_dropdownclick(FusionServerProfilesPage.ID_COMBO_POWER_ON_LOGO, biossettingvalue)
    else:
        logger._log_to_console_and_log_file("Not able to find the control and  code to update the bios setting " + biossettingname)
        selenium2lib.fail_test("Not able to find the control and  code to update the bios setting " + biossettingvalue, "True")


def _edit_bios_setting_dropdownclick(dropdownID, biossettingdropdownvalue):
    '''
    _edit_bios_setting_dropdownclick is used by _edit_bios_setting function to select the bios setting drop down values.

    _edit_bios_setting_dropdownclick
    '''

    selenium2lib = ui_lib.get_s2l()
    ui_lib.wait_for_element_and_click(dropdownID)
    label = selenium2lib.get_text(dropdownID)
    if not label == biossettingdropdownvalue:
        selenium2lib.press_key(dropdownID, biossettingdropdownvalue.strip() + chr(13))

    selenium2lib.wait_until_page_contains_element(FusionServerProfilesPage.ID_BIOS_UPDATED_VALUE % biossettingdropdownvalue)

    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_BIOS_UPDATED_VALUE % biossettingdropdownvalue):
        logger._log_to_console_and_log_file("failed to update the bios setting value")
        # as the edit bios setting function used by UI MAT . will not be failing the function incase wrong data is passed from the excel. bios is set to default values
        # selenium2lib.fail_test("Not able to update the bios setting with value " + biossettingdropdownvalue, "True")
        logger._warn("Not able to update the bios setting with value" % biossettingdropdownvalue)
    else:
        logger._log_to_console_and_log_file("Bios setting is updated with value " + biossettingdropdownvalue)


def move_server_profile(*profile_obj):
    """ move Server Profile

        Example:
        | `move Server Profile`      | ${profileNameList}    |
    """

    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    for move_profile in profile_obj:
        profile_list = [el.text for el in selenium2lib._element_find(FusionServerProfilesPage.ID_PROFILE_LIST_NAMES, False, False)]
        if move_profile.profile not in profile_list:
            logger._warn("Profile '%s' does not exist" % move_profile.profile)
            continue

        if move_profile.profile == "" or move_profile.server == "":
            logger._warn("Mandatory fields for adding server profile can't be empty")
            continue
        ui_lib.wait_for_element(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % move_profile.profile)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % move_profile.profile)
        # servername = selenium2lib._get_text("//*[@id='cic-profile-show-server']")
        servername = ui_lib.wait_for_element_text(FusionServerProfilesPage.ID_MOVE_VALIDATION, 15)
        logger._log_to_console_and_log_file("Server profile '%s' is created on server '%s'" % (move_profile.profile, servername))

        if servername == move_profile.server:
            logger._warn("Moving server profile to same server '%s'" % servername)
            continue

        logger._log_to_console_and_log_file("Move server profile '%s' to server '%s" % (move_profile.profile, move_profile.server))
        if move_profile.server != "unassigned":
            if not selenium2lib._is_element_present(FusionServerHardwarePage.ID_PAGE_LABEL):
                base_page.navigate_base(FusionServerHardwarePage.ID_PAGE_LABEL,
                                        FusionUIBaseElements.ID_MENU_LINK_SERVER_HARDWARE, "css=span.hp-page-item-count")
            if selenium2lib._is_visible(FusionServerHardwarePage.ID_ELEMENT_SERVER_BASE % move_profile.server):
                logger._log_to_console_and_log_file("Power off server '%s' to move server profile" % move_profile.server)
                if not serverhardware.power_off_server_by_name(move_profile.server):
                    logger._warn("Failed to powerOff the server '%s'" % move_profile.server)
                    logger._warn("Can't proceed with move server profile to server '%s'" % move_profile.server)
                    continue
            else:
                logger._warn("Server '%s' is not present in appliance" % move_profile.server)
                continue

        logger._log_to_console_and_log_file("Power off server profile")
        if not power_off_server_profile(move_profile.profile):
            ui_lib.fail_test("Unable to power off server profile")

        if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
            navigate()
        """    updating server profile by changing server hardware   """
        # ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % move_profile.profile)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % move_profile.profile)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_MAIN_ACTION)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_SERVER_PROFILE)
        selenium2lib.wait_until_page_contains("Edit %s" % move_profile.profile)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_SERVER_HARDWARE_DROPDOWN)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_DROPDOWN_SEARCH_SERVER_HARDWARE)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_SEARCH_HARDWARE)
        logger._log_to_console_and_log_file("Select hardware to move server profile")
        # New Code
        #         ui_lib.wait_for_element(FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % move_profile.server)
        if ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % move_profile.server):
            logger._log_to_console_and_log_file("Selected valid server %s" % move_profile.server)
        else:
            logger._warn("server %s is invalid " % move_profile.server)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_SERVER_PROFILE)
            continue
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_UPDATE_SERVER_PROFILE)
        ui_lib.wait_for_element(FusionServerProfilesPage.ID_ADD_PROFILE_NOTIFICATION)
        if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_ADD_PROFILE_NOTIFICATION):
            errMsg = ui_lib.ignore_staleElementRefException("get_text", FusionServerProfilesPage.ID_ADD_PROFILE_NOTIFICATION_CONTENT)
            logger._warn(errMsg)
            logger._warn("Unable to move server profile %s" % move_profile.profile)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_SERVER_PROFILE)
            continue
        logger._log_to_console_and_log_file("Waiting for profile to move from one server to another..")
        ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_UPDATE_PROFILE_TIMESTAMP, 15)
        strTimeStamp = ui_lib.ignore_staleElementRefException("get_text", FusionServerProfilesPage.ID_UPDATE_PROFILE_TIMESTAMP)
        logger._log_to_console_and_log_file(strTimeStamp)
        logger._log_to_console_and_log_file("Verifying profile update status in activity page")  # pylint: disable=E1120
        if _is_element_present_inactivity_page(move_profile.profile, "Update", time.time()):
            logger._log_to_console_and_log_file("Server profile '%s' is moved successfully to server '%s'" % (move_profile.profile, move_profile.server))
        else:
            ui_lib.fail_test("Moving server profile '%s' to server '%s' is failed" % (move_profile.profile, move_profile.server))
        if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
            navigate()
        server_hardware = ui_lib.ignore_staleElementRefException("get_text", FusionServerProfilesPage.ID_MOVE_VALIDATION)
        logger._log_to_console_and_log_file(server_hardware)
        if server_hardware == move_profile.server:
            logger._log_to_console_and_log_file("Successfully moved to %s" % move_profile.server)
        else:
            logger._log_to_console_and_log_file("Failed to move %s" % move_profile.server)


def bak_power_off_server_profile(*profile_obj):
    """ Power Off Server Profile

        ProfileObj xml requires the following attributes:
            name - Comma separated string of profile names that should match
                   existing server profiles.
                   eg: <profile name="Server Profile 1, Server Profile 2">
                       <profile name="Server Profile 3">

        Example:
        | `Power Off Server Profile`      |  @{profile_obj} |
    """
    selenium2lib = ui_lib.get_s2l()
    logger._log_to_console_and_log_file("")
    error = 0
    valid_profile_no = 0
    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    for profile in profile_obj:

        logger._log_to_console_and_log_file("")
        logger._log_to_console_and_log_file("Powering off server profile '%s'" % profile.name)

        # Validate server profiles
        logger._log_to_console_and_log_file("Validating Server Profile")
        profile_name = profile.name

        # for profile_name in profile_names:
        profile_attributes = get_server_profile_attributes(profile_name, None)
        if profile_attributes is None:
            selenium2lib.capture_page_screenshot()
            logger._warn("Server Profile '%s' does not exist" % profile_name)
            selenium2lib.capture_page_screenshot()
            error += 1
            continue
        elif profile_attributes["server hardware"] == "unassigned":
            selenium2lib.capture_page_screenshot()
            logger._warn("Cannot power off Server Profile '%s' due to unassigned server hardware" % profile_name)
            continue

        elif profile_attributes["server power"] == "Off":
            selenium2lib.capture_page_screenshot()
            logger._warn("Server Profile '%s' is already powered off" % profile_name)
            selenium2lib.capture_page_screenshot()
            error += 1
            continue
        else:
            valid_profile_no += 1

        # Select the profile from the left side table

        logger._log_to_console_and_log_file("Powering off Server Profile")
        if not select_server_profile(profile.name):
            selenium2lib.capture_page_screenshot()
            logger._warn("Failed to select server profiles")
            selenium2lib.capture_page_screenshot()
            error += 1
            continue

        # Select Power off option from Action menu
        ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_MENU_MAIN_ACTION)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_MAIN_ACTION)
        if selenium2lib._is_visible(FusionServerProfilesPage.ID_MENU_ACTION_POWEROFF):
            logger._log_to_console_and_log_file("Powering off selected server profile")
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_ACTION_POWEROFF)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_POWEROFF_PRESS_HOLD)
            if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_PROFILE_POWER_STATUS % "Off", PerfConstants.PROFILE_POWER_VALIDATION):
                logger._log_to_console_and_log_file("Successfully powered off Server Profile")
            else:
                selenium2lib.capture_page_screenshot()
                logger._warn('Timeout for wait server profile is powered off')
                selenium2lib.capture_page_screenshot()
                error += 1
                continue
        else:
            selenium2lib.capture_page_screenshot()
            logger._warn("Power off option is not available in the Actions menu")
            selenium2lib.capture_page_screenshot()
            error += 1

        # Build Activity Message
        args = {}
        args["activity"] = "Power Off"
        args["entity"] = get_server_profile_attributes(profile_name, "server hardware")
        # logger._log_to_console_and_log_file(args["entity"])
        args["multiple"] = 0

        # Verify Activity
        if not _verify_activity(**args):
            selenium2lib.capture_page_screenshot()
            logger._warn("Failed to verify Power Off Activity")
            selenium2lib.capture_page_screenshot()
            error += 1
        else:
            logger._log_to_console_and_log_file("Successfully verified Power Off Activity for Powering Off Profile(s): '%s'" % profile.name)

    if error > 0:
        return False
    return True


def _is_element_present_inactivity_page(profilename, message, timestamp):
    """ """
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionActivityPage.ID_PAGE_LABEL):
        base_page.navigate_base(FusionActivityPage.ID_PAGE_LABEL, FusionUIBaseElements.ID_MENU_LINK_ACTIVITY, "css=span.hp-page-item-count")
    # Validating the creation of server profile with time stamp and activity progress of the profile
    if ui_lib.wait_for_element(FusionServerProfilesPage.ID_ACTIVITY_PROGRESS_MOVE % (message, profilename), 60):
        start_time = selenium2lib.get_text(FusionServerProfilesPage.ID_ACTIVITY_TIMESTAMP_MOVE % (message, profilename))
        logger._log_to_console_and_log_file(start_time)
        logger._log_to_console_and_log_file(timestamp)
        logger._log_to_console_and_log_file("Operation started on Server Profile %s started " % profilename)
        if ui_lib.wait_for_element(FusionServerProfilesPage.ID_ACTIVITY_SUCCESS_MOVE % (message, profilename, start_time), PerfConstants.CREATE_SERVER_PROFILE_TIME):
            logger._log_to_console_and_log_file("Operation of server profile %s is done successfully" % profilename)
            return True
        elif ui_lib.wait_for_element(FusionServerProfilesPage.ID_ACTIVITY_ERROR_MOVE % (message, profilename, start_time), PerfConstants.CREATE_SERVER_PROFILE_TIME):
            logger._log_to_console_and_log_file("Operation of server profile %s failed with errors" % profilename)
            selenium2lib.capture_page_screenshot()
            return False
    else:
        logger._log_to_console_and_log_file("Failed to operate server profile %s" % profilename)
        selenium2lib.capture_page_screenshot()
        return False

#     ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_STATUS % (timestamp, elementtocheck, message), PerfConstants.PROFILE_POWER_VALIDATION)
#     if ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_STATUS % (timestamp, elementtocheck, message)):
#         logger._log_to_console_and_log_file("'%s' is present in Activity page" % elementtocheck)
#         return True
#     else:
#         logger._warn("'%s' is not present in Activity page" % elementtocheck)
#         return False


def verify_server_status(server_hardware):
    """ Verifying the list of server hardwares present in the server hardware list at the server Profile page """

    logger._log_to_console_and_log_file("Verifying the list of server hardwares present in the server Profile page..")
    selenium2lib = ui_lib.get_s2l()

    if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_PROFILE_LIST, PerfConstants.DEFAULT_SYNC_TIME):
        logger._log_to_console_and_log_file("Sever Profile Page contains a Server Profile List Table and starting to verify the servers status..")
    else:
        logger._warn("Sever Profile Page does not contains a Server Profile List Table and Hence failing the test..")
        selenium2lib.capture_page_screenshot()
        return False

    if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_NO_SERVER_PROFILE, PerfConstants.DEFAULT_SYNC_TIME):
        logger._warn("Sever Profile Page does not contains a any Server and Hence failing the test..")
        selenium2lib.capture_page_screenshot()
        return False
    else:
        logger._log_to_console_and_log_file("Sever Profile Page contains a Servers and starting to verify the servers status..")

    if not ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_SELECT_SERVER % server_hardware, PerfConstants.DEFAULT_SYNC_TIME):
        logger._warn("Server Hardware : " + server_hardware + " is not present in the ServerList of the Server Profile page")
        selenium2lib.capture_page_screenshot()
        return False
    else:
        logger._log_to_console_and_log_file("Server Hardware : " + server_hardware + " is present in the ServerList and Hence verifying for the status..")
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_SELECT_SERVER % server_hardware)
        if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_SERVER_STATUS_OK, PerfConstants.DEFAULT_SYNC_TIME):
            logger._log_to_console_and_log_file("Server status of server : " + server_hardware + " is in state : 'OK'")
        elif ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_SERVER_STATUS_ERROR, PerfConstants.DEFAULT_SYNC_TIME):
            ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_ERROR_WARN_MSG, PerfConstants.DEFAULT_SYNC_TIME)
            err_msg = selenium2lib.get_text(FusionServerProfilesPage.ID_ERROR_WARN_MSG)
            logger._log_to_console_and_log_file("Server status of server : " + server_hardware + " is in state : 'ERROR' with the error msg : '" + err_msg + "'")
        else:
            ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_ERROR_WARN_MSG, PerfConstants.DEFAULT_SYNC_TIME)
            err_msg = selenium2lib.get_text(FusionServerProfilesPage.ID_ERROR_WARN_MSG)
            logger._log_to_console_and_log_file("Server status of server : " + server_hardware + " is in state : 'WARNING' with the warning msg : '" + err_msg + "'")
        return True


def verify_server_profile_status(expectedserverstatus, *profile_obj):
    """ Verifying the list of server hardwares present in the server hardware list at the server Profile page """

    logger._log_to_console_and_log_file("")
    logger._log_to_console_and_log_file("Verifying the list of server hardwares present in the server Profile page..")
    selenium2lib = ui_lib.get_s2l()

    # if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_PROFILE_LIST, PerfConstants.DEFAULT_SYNC_TIME):
    #    logger._log_to_console_and_log_file("Sever Profile Page contains a Server Profile List Table and starting to verify the servers status..")
    # else:
    #    logger._warn("Sever Profile Page does not contains a Server Profile List Table and Hence failing the test..")
    #    return False

    if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_NO_SERVER_PROFILE, PerfConstants.DEFAULT_SYNC_TIME):
        logger._warn("Sever Profile Page does not contains a any Server and Hence failing the test..")
        selenium2lib.capture_page_screenshot()
        return False
    # else:
    #    logger._log_to_console_and_log_file("Sever Profile Page contains a Servers and starting to verify the servers status..")

    # if not ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_SELECT_SERVER % serverhardware, PerfConstants.DEFAULT_SYNC_TIME):
    #    logger._warn("Server Hardware : " + serverhardware + " is not present in the ServerList of the Server Profile page")
    #    return False
    # else:
    #    logger._log_to_console_and_log_file("Server Hardware : " + serverhardware + " is present in the ServerList and Hence verifying for the status..")

    for profile in profile_obj:
        server_hardware = profile.server

        logger._log_to_console_and_log_file("Verifying status for profile %s" % profile.name)

        if server_hardware == 'unassigned':
            logger._log_to_console_and_log_file("Server hardware is unassigned and cannot verify the server's power status")
            continue

        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % profile.name)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % profile.name)
        BuiltIn().sleep(2)  # wait for fields to load

        # ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_SELECT_SERVER % server_hardware)
        if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_SERVER_STATUS_OK, PerfConstants.DEFAULT_SYNC_TIME):
            if expectedserverstatus == 'OK':
                logger._log_to_console_and_log_file("Server status of server : " + server_hardware + " is in state : 'OK' as expected")
            else:
                logger._log_to_console_and_log_file("Server status of server : " + server_hardware + " is in state : 'OK' as NOT expected")
                selenium2lib.capture_page_screenshot()
                return False
        elif ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_SERVER_STATUS_ERROR, PerfConstants.DEFAULT_SYNC_TIME):
            ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_ERROR_WARN_MSG, PerfConstants.DEFAULT_SYNC_TIME)
            err_msg = selenium2lib.get_text(FusionServerProfilesPage.ID_ERROR_WARN_MSG)
            logger._log_to_console_and_log_file("Server status of server : " + server_hardware + " is in state : 'ERROR' with the error msg : '" + err_msg + "'")
            if expectedserverstatus == 'ERROR':
                logger._log_to_console_and_log_file("Server status of server : is in state : 'ERROR' as expected")
            else:
                logger._log_to_console_and_log_file("Server status of server : is in state : 'ERROR' as NOT expected")
                selenium2lib.capture_page_screenshot()
                return False
        else:
            ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_ERROR_WARN_MSG, PerfConstants.DEFAULT_SYNC_TIME)
            err_msg = selenium2lib.get_text(FusionServerProfilesPage.ID_ERROR_WARN_MSG)
            logger._log_to_console_and_log_file("Server status of server : " + server_hardware + " is in state : 'WARNING' with the warning msg : '" + err_msg + "'")
            if expectedserverstatus == 'WARNING':
                logger._log_to_console_and_log_file("Server status of server : is in state : 'WARNING' as expected")
            else:
                logger._log_to_console_and_log_file("Server status of server : is in state : 'WARNING' as NOT expected")
                selenium2lib.capture_page_screenshot()
                return False

    return True


def validate_server_profile_status(status, *profile_obj):
    """ Verifying the list of server profile present in the right status """

    logger.info("Verifying the list of server profile present in the right status..")
    navigate()
    status_list = status.split(',')

    for profile in profile_obj:
        logger.info("Verifying status for profile [ %s ]" % profile.name)
        CommonOperationServerProfile.click_server_profile(profile.name)
        expected_status_found = False
        for sta in status_list:
            expected_status_found = expected_status_found or VerifyServerProfile.verify_server_profile_status_on_details_page(sta.lower(), timeout=5, fail_if_false=False)
        if not expected_status_found:
            ui_lib.fail_test("Profile [ %s ] status varified failed, expected status is: [ %s ]" % (profile.name, status))
    return True


def validate_server_profile_connections_error_state(*profile_obj):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    total = len(profile_obj)
    not_exists = 0
    verified = 0
    selenium2lib = ui_lib.get_s2l()

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("deleting a server profile named '%s'" % profile.name)
        if not VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' does not exist" % profile.name)
            not_exists += 1
            continue

        if CommonOperationServerProfile.wait_server_profile_status_error(profile.name, timeout=5):
            expect_error = 'has been deleted'
            CommonOperationServerProfile.click_server_profile(profile.name)
            CommonOperationServerProfile.click_to_show_server_profile_error_details(profile.name)
            actual_error = CommonOperationServerProfile.get_server_profile_error_details(profile.name)

            if expect_error in actual_error:
                logger.info("Server profile '%s' got the correct error messages after network were deleted" % profile.name)
                verified += 1
            else:
                logger.warn("Failed to get the correct messages for server profile '%s'" % profile.name)
                selenium2lib.capture_page_screenshot()

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no server profile to view! all %s server profile(s) is NOT existing, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if verified < total:
            logger.warn("not all of messages for the server profile(s) is successfully verified - %s out of %s verified " % (verified, total))
            if verified + not_exists == total:
                logger.warn("%s not-existing server profile(s) is skipped, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s not-existing server profile(s) is skipped, %s profile(s) left is failed being verified " % (not_exists, total - verified - not_exists))
                return False

    logger.info("all of the server profile(s) is successfully verified - %s out of %s " % (verified, total))
    return True


def verify_server_profile_power_status(expectedpowerstatus, *profile_obj):
    """ Verifying the power status of list of server hardwares present in the server hardware list at the server Profile page """

    # logger._log_to_console_and_log_file("")
    # logger._log_to_console_and_log_file("Verifying the power status of list of server hardwares present in the server Profile page..")
    selenium2lib = ui_lib.get_s2l()
    error = 0

    for profile in profile_obj:
        logger._log_to_console_and_log_file("")
        logger._log_to_console_and_log_file("Verifying power status for profile %s" % profile.name)

        profile_names = _split_profile_names(profile.name)
        for profile_name in profile_names:
            status = get_server_profile_attributes(profile_name)

            if status["server hardware"] == 'unassigned':
                logger._warn("Server profile '%s' has unassigned server hardware and cannot verify the server's power status, skip" % profile_name)
                selenium2lib.capture_page_screenshot()
                # error += 1
                continue

            if status["server power"].lower() == expectedpowerstatus.lower():
                logger._log_to_console_and_log_file("Successfully verified Server Profile '%s' power status: %s" % (profile_name, status["server power"]))
                continue
            else:
                logger._warn("Failed to verify Server Profile '%s' power status: %s, expect: %s" % (profile_name, status["server power"].lower(), expectedpowerstatus))
                selenium2lib.capture_page_screenshot()
                error += 1

    if error > 0:
        return False
    return True


def validate_server_profile_consistency_state(profile_obj):
    """ Verifying the consistency status of list of server hardware present in the server hardware list at the server profile general page"""
    count = 0
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    for _, profile in enumerate(profile_obj):
        rc = select_server_profile(profile.name)
        if not rc:
            logger.warn("Failed to select server profile '%s'" % profile.name)
            continue
        FusionUIBase.select_view_by_name(view_name='General', timeout=5, fail_if_false=False)
        if VerifyServerProfile.verify_server_profile_consistency_status(profile.expected_state, timeout=5, fail_if_false=False):
            count += 1

    if count == len(profile_obj):
        logger.info("All of the given SPs passes consistency check.")
        return True
    else:
        logger.warn("%s out of %s - the given SPs passes consistency check." % (count, len(profile_obj)))
        return False


def bak_verify_server_profile_general_info(*profile_obj):
    """Verifying the server hardware, hardware type and Enclosure group for server profile"""
    selenium2lib = ui_lib.get_s2l()

    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
        navigate()

    for profile in profile_obj:
        server = profile.server
        hardwaretype = profile.hardwareType
        enclosuregroup = profile.enclgroup

        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % profile.name)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % profile.name)
        BuiltIn().sleep(5)  # wait for fields to load

        logger.info("Verifying server hardware for profile %s" % profile.name)
        if ui_lib.wait_for_element_text(FusionServerProfilesPage.ID_PROFILE_SERVER, server, PerfConstants.DEFAULT_SYNC_TIME) is False:
            txt = ui_lib.get_text(FusionServerProfilesPage.ID_PROFILE_SERVER)
            logger.info("Server hardware of server : %s is not as expected [%s]" % (txt, server))
            selenium2lib.capture_page_screenshot()
            return False

        logger.info("Verifying server hardware type for profile %s" % profile.name)
        if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_PROFILE_HARDWARE, PerfConstants.DEFAULT_SYNC_TIME, fail_if_false=False) is True:
            txt = ui_lib.get_text(FusionServerProfilesPage.ID_PROFILE_HARDWARE)
            if txt.find(hardwaretype) == -1:
                logger.info("Server hardware of server : %s is not as expected [%s]" % (txt, hardwaretype))
                selenium2lib.capture_page_screenshot()
                return False
        else:
            logger.warn("Failed to wait server hardware type field display")
            return False

        logger.info("Verifying enclosure group for profile %s" % profile.name)
        if ui_lib.wait_for_element_text(FusionServerProfilesPage.ID_PROFILE_ENCLOSUREGROUP, enclosuregroup, PerfConstants.DEFAULT_SYNC_TIME) is False:
            txt = ui_lib.get_text(FusionServerProfilesPage.ID_PROFILE_ENCLOSUREGROUP)
            logger.info("Enclosure group of server : %s is not as expected [%s]" % (txt, enclosuregroup))
            selenium2lib.capture_page_screenshot()
            return False

    return True


def select_server_profile(profileNames):
    """ Select server profile

        ProfileNames should be a comma separated string of profile names that should match
        existing server profiles.

        NOTE: Uses windows specific functions.

        Example:
        | `Select Server Profile`      |  @{profileNames} |
        | `Select Server Profile`      |  Server Profile 1, Server Profile 2 |
        | `Select Server Profile`      |  Server Profile 3 |
    """
    selenium2lib = ui_lib.get_s2l()

    error = 0
    count = 0

    profileNames = _split_profile_names(profileNames)
    multipleSelect = len(profileNames) - 1

    # Multi-Select can only be executed on a windows system due to the win32api function
    if multipleSelect and os.name != 'nt':
        logger._warn("Multiple Server Profile selection currently cannot be executed on a Non Windows OS.")
        selenium2lib.capture_page_screenshot()
        return False

    # Verifying profile page is opened or not. Opening if it is not opened
    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_LINK_CREATE_SERVER_PROFILES):
        navigate()

    for profileName in profileNames:
        count += 1

        # Holding down the Control Key for multiple select is using a Windows specific win32api function.
        # This action will likely fail on Unix or Linux platforms.
        # Unable to use selenium actionchain functions for key_up and key_down due to Selenium Bug 16735.
        # https://bugs.webkit.org/show_bug.cgi?id=16735
        if multipleSelect and count == 2:
            logger._log_to_console_and_log_file("Holding down Ctrl Key")
            keybd_event(0xA3, 0, 0, 0)
#             ActionChains(selenium2lib._current_browser()).key_down(Keys.CONTROL).perform()

# Verifying the presence of given profile and selecting
        logger._log_to_console_and_log_file("Selecting profile '%s' :" % profileName)
        if selenium2lib._is_element_present(FusionServerProfilesPage.ID_SELECT_PROFILE % profileName):
            if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_SELECT_PROFILE % profileName):
                logger._warn("Unable to select the profile '%s' :" % profileName)
                selenium2lib.capture_page_screenshot()
                error += 1
            else:
                BuiltIn().sleep(4)  # Wait for data record to load--no way to verify since elements are the same
        else:
            logger._warn("Profile '%s' is not present in the appliance" % profileName)
            selenium2lib.capture_page_screenshot()
            error += 1

    if multipleSelect:
        logger._log_to_console_and_log_file("Releasing Ctrl Key")
        keybd_event(0xA3, 0, win32con.KEYEVENTF_KEYUP, 0)
#         ActionChains(selenium2lib._current_browser()).key_up(Keys.CONTROL).perform()

# Verify
    if multipleSelect:
        if not ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_MULTIPLE_SERVERS_TITLE % len(profileNames), PerfConstants.FUSION_PAGE_SYNC):
            logger._warn("Failed to select %d profiles" % len(profileNames))
            selenium2lib.capture_page_screenshot()
            error += 1

    else:
        if not ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_SELECT_PROFILE % profileNames[0], PerfConstants.FUSION_PAGE_SYNC):
            logger._warn("Failed to select profile '%s'" % profileNames[0])
            selenium2lib.capture_page_screenshot()
            error += 1

    if error > 0:
        return False
    return True


def bak_edit_server_profile(*profile_obj):
    """ Edit Server Profile    """

    selenium2lib = ui_lib.get_s2l()
    error = 0

    # Navigating to 'Server Profiles' page
    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    # Build a list of server profiles present on the left side
    profile_list = [el.text for el in selenium2lib._element_find(FusionServerProfilesPage.ID_PROFILE_LIST_NAMES, False, False)]

    # Edit each server profile
    for editprofile in profile_obj:
        # Check that the profile to be edited is present
        if editprofile.profile not in profile_list:
            logger._warn("Profile '%s' does not exist" % editprofile.profile)
            selenium2lib.capture_page_screenshot()
            error += 1
            continue

        # Select the profile to be edited from the left side table
        logger._log_to_console_and_log_file("Selecting profile %s" % editprofile.profile)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % editprofile.profile)

        # Select 'General'  (make sure we're at the top of the page).
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_GENERAL)
        BuiltIn().sleep(2)

        # Assure Server Profile is powered as requested
        if editprofile.has_property("power"):
            ui_lib.wait_for_element(FusionServerProfilesPage.ID_SERVER_POWER_STATUS)
            power_state = ui_lib.ignore_staleElementRefException("get_text", FusionServerProfilesPage.ID_SERVER_POWER_STATUS)
            if power_state != editprofile.power:
                logger._warn("Server Profile must be powered %s before editing" % editprofile.power)
                selenium2lib.capture_page_screenshot()
                error += 1

        # Let's assume we're going to edit something!
        # Select 'Actions' and 'Edit'
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_MAIN_ACTION)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_SERVER_PROFILE)

        # Wait for 'Edit <profile>' page to appear
        selenium2lib.wait_until_page_contains("Edit %s" % editprofile.profile)

        # Edit General
        if editprofile.has_property("newname") or editprofile.has_property("newdescription") or editprofile.has_property("newServerHardware"):
            logger._log_to_console_and_log_file("Edit General...")
            # Select 'Overview' then 'General'  (make sure we're at the top of the page).
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_OVERVIEW)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_GENERAL)
            # Edit the 'Name' field
            if editprofile.has_property("newname"):
                logger._log_to_console_and_log_file("Setting name to %s" % editprofile.newname)
                ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_EDIT_SERVER_PROFILE_NAME, editprofile.newname)

            # Edit the 'Description' field
            if editprofile.has_property("newdescription"):
                logger._log_to_console_and_log_file("Setting description to %s" % editprofile.newdescription)
                ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_EDIT_SERVER_PROFILE_DESCRIPTION, editprofile.newdescription)

            if editprofile.has_property("newServerHardware"):
                logger._log_to_console_and_log_file("Setting Server Hardware to %s" % editprofile.newServerHardware)
                # ui_lib.wait_for_element_and_click("css=div.hp-close")
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_DROPDOWN_SEARCH_SERVER_HARDWARE)
                if selenium2lib._is_element_present(FusionServerProfilesPage.ID_LINK_SEARCH_FOR_ANOTHER):
                    ui_lib.wait_for_element_and_click("//a[contains(text(),'Search for another')]")
                ui_lib.wait_for_element_and_input_text("//input[@id='cic-profile-edit-server-input']", editprofile.newServerHardware[-6:])
                if ui_lib.wait_for_element_and_click("//span[contains(text(),'%s')]/.." % editprofile.newServerHardware):
                    logger._log_to_console_and_log_file("Selected valid server hardware")
                else:
                    logger._log_to_console_and_log_file("Please pass valid server hardware (%s)" % editprofile.newServerHardware)
            # Don't hit OK just yet! There may be other things to edit

        # Edit Connections
        if editprofile.has_property("connection"):
            logger._log_to_console_and_log_file("Connections...")
            # Select 'Overview' then 'Connections'  (make sure we're at the top of the page).
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_OVERVIEW)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_CONNECTIONS)
            # Editing network connections
            for connection in editprofile.connection:
                if not connection.has_property("network"):
                    logger._warn("Mandatory fields for adding profile connections can't be empty")
                    selenium2lib.capture_page_screenshot()
                    error += 1
                    continue
                if not selenium2lib._is_element_present(
                        "xpath =//*[@id='cic-profile-edit-connections-table']/tbody/tr/td/a[text()='%s']" % connection.network):
                    logger._warn("Can't find connection named %s" % connection.network)
                    selenium2lib.capture_page_screenshot()
                    error += 1
                    continue
                # Click on the edit Icon to get to the Edit Connection page
                ui_lib.wait_for_element_and_click(
                    "xpath = //table[@id='cic-profile-edit-connections-table']//a[contains(text(),%s)]/../../td[9]/div" % connection.network)
                # Wait for 'Edit Connection' page
                selenium2lib.wait_until_page_contains("Edit Connection")
                # Enter the 'bandwidth' field (if present).
                if connection.has_property("bandwidth"):
                    ui_lib.wait_for_element_and_input_text("id=cic-profile-connection-bandwidth", connection.bandwidth)
                # Click OK to get back to the 'Edit' page
                ui_lib.wait_for_element_and_click("id=cic-profile-connection-add")

        # Edit network
        if editprofile.has_property("network"):
            logger._log_to_console_and_log_file("Networks...")
            # Select 'Overview' then 'Connections'  (make sure we're at the top of the page).
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_OVERVIEW)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_CONNECTIONS)
            for network in editprofile.network:
                if not selenium2lib._is_element_present(
                        "xpath =//*[@id='cic-profile-edit-connections-table']/tbody/tr/td/a[text()='%s']" % network.change):
                    logger._warn("Can't find connection named %s" % network.change)
                    selenium2lib.capture_page_screenshot()
                    error += 1
                    continue
                # Click on the 'edit' Icon to get to the Edit Connection page
                ui_lib.wait_for_element_and_click(
                    "xpath = //table[@id='cic-profile-edit-connections-table']//a[contains(text(),%s)]/../../td[9]/div" % network.change)
                # Wait for 'Edit Connection' page
                selenium2lib.wait_until_page_contains("Edit Connection")
                # Enter the updated network name
                ui_lib.wait_for_element_and_input_text("id=cic-profile-connection-network-input", network.to)
                # Click on the 'OK' button to close the dialog and return to 'Edit <server Profile> page
                ui_lib.wait_for_element_and_click("id=cic-profile-connection-add")

        # Edit networksets
        if editprofile.has_property("networkset"):
            logger._log_to_console_and_log_file("NetworkSets...")
            # Select 'Overview' then 'Connections'  (make sure we're at the top of the page).
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_OVERVIEW)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_CONNECTIONS)
            for networkset in editprofile.networkset:
                if not selenium2lib._is_element_present(
                        "xpath =//*[@id='cic-profile-edit-connections-table']/tbody/tr/td/a[text()='%s']" % networkset.change):
                    logger._warn("Can't find connection named %s" % networkset.change)
                    selenium2lib.capture_page_screenshot()
                    error += 1
                    continue
                # Click on the 'edit' Icon to get to the Edit Connection page
                ui_lib.wait_for_element_and_click(
                    "xpath = //table[@id='cic-profile-edit-connections-table']//a[contains(text(),%s)]/../../td[9]/div" % networkset.change)
                # Wait for 'Edit Connection' page
                selenium2lib.wait_until_page_contains("Edit Connection")
                # Enter the updated networkset name
                ui_lib.wait_for_element_and_input_text("id=cic-profile-connection-network-input", networkset.to)
                # Click on the 'OK' button to close the dialog and return to 'Edit <server Profile> page
                ui_lib.wait_for_element_and_click("id=cic-profile-connection-add")

        # Editing fc networks
        if editprofile.has_property("fcnetwork"):
            logger._log_to_console_and_log_file("FcNetworks...")
            # Select 'Overview' then 'Connections'  (make sure we're at the top of the page).
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_OVERVIEW)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_CONNECTIONS)
            for fcnetwork in editprofile.fcnetwork:
                if not selenium2lib._is_element_present(
                        "xpath =//*[@id='cic-profile-edit-connections-table']/tbody/tr/td/a[text()='%s']" % fcnetwork.change):
                    logger._warn("Can't find connection named %s" % fcnetwork.change)
                    selenium2lib.capture_page_screenshot()
                    error += 1
                    continue
                # Click on the 'edit' Icon to get to the Edit Connection page
                ui_lib.wait_for_element_and_click(
                    "xpath = //table[@id='cic-profile-edit-connections-table']//a[contains(text(),%s)]/../../td[9]/div" % fcnetwork.change)
                # Wait for 'Edit Connection' page
                selenium2lib.wait_until_page_contains("Edit Connection")
                # Enter the updated fcnetwork name
                ui_lib.wait_for_element_and_input_text("id=cic-profile-connection-network-input", fcnetwork.to)
                # Click on the 'OK' button to close the dialog and return to 'Edit <server Profile> page
                ui_lib.wait_for_element_and_click("id=cic-profile-connection-add")

        # LOCAL STORAGE
        if editprofile.has_property("managelocalstorage"):
            logger._log_to_console_and_log_file("Managing local storage..")

            # Select 'Overview' then 'Local Storage'  (make sure we're at the top of the page).
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_OVERVIEW)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_LOCAL_STORAGE)

            # Click on the 'Manage Local Storage' checkbox
            logger._log_to_console_and_log_file("Selecting 'Manage Local Storage' if not yet selected")
            selenium2lib.select_checkbox(FusionServerProfilesPage.ID_EDIT_LOCAL_STORAGE)

            # Click on 'Manage integrated controller' checkbox
            selenium2lib.select_checkbox(FusionServerProfilesPage.ID_CHKBOX_MANAGE_INTEGRATED_CONTROLLER)

            # Click on 'Close' button if Initialize Local Storage Warning message dialogue shows up
            # (when first time check 'Manage integrated controller', 'Initialize local storage' checkbox is checked by default, then warning message occurs)
            if ui_lib.is_visible(FusionServerProfilesPage.ID_SELECT_OK_AFTER_INITIALIZE_LOCAL_STORAGE):
                logger._log_to_console_and_log_file("Close [ Manage Local Storage Controller ] dialogue")
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_SELECT_OK_AFTER_INITIALIZE_LOCAL_STORAGE)

            if editprofile.has_property("raid"):
                # Select which RAID level
                logger._log_to_console_and_log_file("RAID to %s" % editprofile.raid)
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_EDIT_CONTROLLER_MODE_DROPDOWN)
                selenium2lib.mouse_up("//a[contains(text(),'%s')]" % editprofile.raid)
                selenium2lib.capture_page_screenshot()

            if editprofile.has_property("disk_initialize"):
                # Click on Disk Initialization
                logger._log_to_console_and_log_file("Disk initialization set to %s" % editprofile.disk_initialize)
                if editprofile.disk_initialize == "1":
                    logger._log_to_console_and_log_file("Check [ Re-initialize internal storage on next application of server profile ]")
                    ui_lib.wait_for_checkbox_and_select(FusionServerProfilesPage.ID_EDIT_INITIALIZE_LOCAL_STORAGE)
                    # Click on 'Close' button if Initialize Local Storage Warning message dialogue shows up
                    if ui_lib.is_visible(FusionServerProfilesPage.ID_SELECT_OK_AFTER_INITIALIZE_LOCAL_STORAGE):
                        logger._log_to_console_and_log_file("Close [ Manage Local Storage Controller ] dialogue")
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_SELECT_OK_AFTER_INITIALIZE_LOCAL_STORAGE)
                    selenium2lib.capture_page_screenshot()
                else:
                    logger._log_to_console_and_log_file("Un-check [ Re-initialize internal storage on next application of server profile ]")
                    ui_lib.wait_for_checkbox_and_unselect(FusionServerProfilesPage.ID_EDIT_INITIALIZE_LOCAL_STORAGE)
                    selenium2lib.capture_page_screenshot()

            if editprofile.has_property("bootable"):
                logger._log_to_console_and_log_file("Setting bootable to %s" % editprofile.bootable)
                # Click on Disk Bootable
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_BOOTABLE)
                selenium2lib.capture_page_screenshot()

        # Click on the 'OK' button to close the dialog and accept the profile edit
        logger._log_to_console_and_log_file("Press OK and wait for profile edit verification and completion")
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_SERVER_PROFILE_OK)
        selenium2lib.capture_page_screenshot()

        # Wait for verification complete
        ui_lib.wait_for_element_remove(FusionServerProfilesPage.ID_PROFILE_EDIT_VERIFY, verifyProfileTimeout)
        selenium2lib.capture_page_screenshot()

        if selenium2lib._is_element_present("//div[@class='hp-progress']"):
            # Now wait for "Completed" since we have a progress bar
            logger._log_to_console_and_log_file("Waiting for profile edit to complete..")
            if not ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_PROFILE_EDIT_COMPLETE, editProfileTimeout):
                logger._warn("Timeout waiting for edit progress completed")
                error += 1
                selenium2lib.capture_page_screenshot()
            else:
                logger._log_to_console_and_log_file('Edit server profile successfully')
    if error:
        selenium2lib.capture_page_screenshot()
        return False

    return True


def get_server_profile_attributes(name, attribute=None):
    """ get server profile attributes

        This function will return attributes from the server profiles page in the UI.
        If an attribute is specified, only the value of that attribute will be returned as a string.
        If no attribute is specified, all attribues in the page will be returned as a dictionary.
        NOTE: Currently only supporting the 'General' Server Profile information

        | ${Server Profile attributes}=  | Get Server Profile Attributes | Encl1 |
        | ${Server Profile description}=  | Get Server Profile Attributes | Encl1 | Description |

    """
    general_xpaths = {
        "name": FusionServerProfilesPage.ID_SERVER_DESCRIPTION,
        "description": FusionServerProfilesPage.ID_SERVER_DESCRIPTION,
        "server hardware": FusionServerProfilesPage.ID_SERVER_HARDWARE_NAME,
        "associated server": FusionServerProfilesPage.ID_ASSOCIATED_SERVER,
        "server hardware type": FusionServerProfilesPage.ID_PROFILE_HARDWARE,
        "enclosure group": FusionServerProfilesPage.ID_SERVER_ENC_GROUP,
        "affinity": FusionServerProfilesPage.ID_SERVER_AFFINITY,
        "server power": FusionServerProfilesPage.ID_SERVER_POWER_STATUS,
        "serial number": FusionServerProfilesPage.ID_SERVER_SERIAL_NUMBER,
        "uuid": FusionServerProfilesPage.ID_SERVER_UUID,
    }

    # Navigate to Server Profile
    if not select_server_profile(name):
        logger._warn("Failed to find Server Profile '%s'" % name)
    BuiltIn().sleep(4)
    # Get attribute data
    if attribute is not None:
        keys = general_xpaths.keys()
        if attribute.lower() not in keys:
            logger._warn("Invalid attribute '%s'." % attribute)
            return None

        # Get specified attribute
        xpath = general_xpaths[attribute.lower()]
        ui_lib.wait_for_element_visible(xpath, timeout=10)
        value = ui_lib.ignore_staleElementRefException("get_text", xpath)

        return value
    else:
        # Get all attributes of Server Profile
        general_data = {}
        for attribute, xpath in general_xpaths.iteritems():
            value = ui_lib.ignore_staleElementRefException("get_text", xpath)
            general_data[attribute] = value
        return general_data

    return None


def _split_profile_names(profile_names):
    """ Split Profile Names

        This function will split multiple profile names from a string containing comma delimited list of
        names and return an array.
    """
    # Split profile names
    if ',' in profile_names:
        profile_names = profile_names.split(',')
    else:
        profile_names = [profile_names]

    # Remove leading and trailing whitespace
    for x in range(0, len(profile_names)):
        profile_names[x] = profile_names[x].strip()
    return profile_names


def _verify_activity(**args):
    """ Verify Activity

    Verifies Activity flyout information. Arguments are case sensitive and should be lower case.

    Arguments:
        activity*  - Activity title
        entity*    - Entity name performing the activity
        status     - Activity status (not implemented). Defaults to 'ok'.
        mulitple   - boolean indicator for number of entities in activity. Defaults to 0.

        message    - Activity Message in a single entity activity. Defaults to 'No message'

        comlpeted* - Array of completed  entities in a multiple entity activity
        excluded   - Array of excluded  entities in a multiple entity activity. Omitted if no exclusions.
        error      - Number of errors in a multiple entity activity. Defaults to 0.
        warning    - Number of warnings in a multiple entity activity. Defaults to 0.

        *Required Arguments
    """

    selenium2lib = ui_lib.get_s2l()
    error = 0

    # Validate Input
    # Set default values
    if "multiple" not in args:
        args["multiple"] = 0
    if "status" not in args:
        args["status"] = "ok"
    if args["multiple"]:
        if "error" not in args:
            args["error"] = 0
        if "warning" not in args:
            args["warning"] = 0
    else:
        if "message" not in args:
            args["message"] = "No message"

    # Verify required parameters
    required_attributes = ["activity", "entity"]
    if args["multiple"]:
        required_attributes.append("completed")
    for attribute in required_attributes:
        if attribute not in args:
            logger._warn("'%s' attribute not specified." % attribute)
            selenium2lib.capture_page_screenshot()
            return False

    # Open Activity Nav Bar
    if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ACTIVITY_BAR):
        logger._warn("Failed to open Activity Bar")
        selenium2lib.capture_page_screenshot()
        error += 1

    # Open Activity Flyout
    if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LAST_ACTIVITY, timeout=7):
        logger._warn("Failed to open Activity Flyout")
        selenium2lib.capture_page_screenshot()
        error += 1
        # TODO: Wait for activity to complete
        # TODO: Verify Activity Status
        # Currently unable to get status from page
        # for x in range(1, 6):
        # value = selenium2lib.get_text(FusionServerProfilesPage.ID_ACTIVITY_STATUS)
        # if value!="changing": break
        # BuiltIn().sleep("10 seconds", "Waiting for Activity to complete")
        # if not ui_lib.wait_for_element_text(FusionServerProfilesPage.ID_ACTIVITY_STATUS, status):
        # logger._warn("Failed to verify '%s' activity status. Got '%s'." % (status, value))
        selenium2lib.capture_page_screenshot()
        # error += 1

    # Verify Activity Name
    value = ui_lib.ignore_staleElementRefException("get_text", FusionServerProfilesPage.ID_ACTIVITY_NAME)
    if not ui_lib.wait_for_element_text(FusionServerProfilesPage.ID_ACTIVITY_NAME, args["activity"]):
        logger._warn("Failed to verify '%s' activity. \nGot '%s'." % (args["activity"], value))
        selenium2lib.capture_page_screenshot()
        error += 1

    # Verify Activity Message
    value = ui_lib.ignore_staleElementRefException("get_text", FusionServerProfilesPage.ID_ACTIVITY_MESSAGE)
    if "message" in args:
        if not ui_lib.wait_for_element_text(FusionServerProfilesPage.ID_ACTIVITY_MESSAGE, args["message"]):
            logger._warn("Failed to verify '%s' activity message. \nGot '%s'." % (args["message"], value))
            selenium2lib.capture_page_screenshot()
            # error += 1
    else:
        msg_lines = str(value).splitlines()
        index = 0

        # Verify Multiple Selected Activity Message
        for attribute in ["completed", "excluded", "error", "warning"]:
            # Ignore optional attributes
            if attribute not in args:
                continue
            value = str(msg_lines[index][len(attribute) + 2:])
            if attribute in ["completed", "excluded"]:
                rc = _compare_lists(value.split(","), args[attribute])
            else:
                rc = (int(value) == int(args[attribute]))
            if not rc:
                logger._warn("Failed to verify '%s' %s message. \nGot '%s'." % (args[attribute], attribute, value))
                selenium2lib.capture_page_screenshot()
                error += 1
            index += 1

    # Verify Activity Entity
    if not args["multiple"]:
        value = ui_lib.ignore_staleElementRefException("get_text", FusionServerProfilesPage.ID_SINGLE_ACTIVITY_ENTITY)
        if not ui_lib.wait_for_element_text(FusionServerProfilesPage.ID_SINGLE_ACTIVITY_ENTITY, args["entity"]):
            logger._warn("Failed to verify '%s' activity entity. \nGot '%s'." % (args["entity"], value))
            selenium2lib.capture_page_screenshot()
            error += 1
    else:
        value = ui_lib.ignore_staleElementRefException("get_text", FusionServerProfilesPage.ID_MULTIPLE_ACTIVITY_ENTITY)
        if not ui_lib.wait_for_element_text(FusionServerProfilesPage.ID_MULTIPLE_ACTIVITY_ENTITY, args["entity"]):
            logger._warn("Failed to verify '%s' activity entity. \nGot '%s'." % (args["entity"], value))
            selenium2lib.capture_page_screenshot()
            error += 1

    # Close Activity Flyout
    value = ui_lib.ignore_staleElementRefException("get_text", FusionServerProfilesPage.ID_ACTIVITY_STATUS)
    if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LAST_ACTIVITY):
        logger._warn("Failed to close Activity Flyout")
        selenium2lib.capture_page_screenshot()
        error += 1

    # Close Activity Nav Bar
    if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ACTIVITY_BAR):
        logger._warn("Failed to close Activity Bar")
        selenium2lib.capture_page_screenshot()
        error += 1

    if error > 0:
        return False
    return True


def _compare_lists(got, expected):
    """ Compare Lists

        Function that will compare two arrays which are specified.
    """

    # Validate Types
    if not isinstance(got, types.ListType) or not isinstance(expected, types.ListType):
        logger._warn("Parameters should be lists")
        logger._warn(type(got))
        logger._warn(type(expected))
        return False

    # Compare size
    if len(got) != len(expected):
        logger._warn("Number of items do not match")
        return False

    # Compare values
    for a in got:
        a = a.strip()
        if a not in expected:
            logger._warn("'%s' not present in expected list" % a)
            return False

    return True


def assign_profile(*profile_obj):
    """ """
    selenium2lib = ui_lib.get_s2l()

    # Navigating to Server profile page
    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    for assignprofile in profile_obj:
        profile_list = [el.text for el in selenium2lib._element_find(FusionServerProfilesPage.ID_PROFILE_LIST_NAMES, False, False)]
        if assignprofile.profiletoassign not in profile_list:
            logger._warn("Profile '%s' does not exist" % assignprofile.profiletoassign)
            continue
        if assignprofile.server == "":
            logger._warn("Mandatory fields to copy server profile can't be empty")
            continue

        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % assignprofile.profiletoassign)
        ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_LINK_OVERVIEW)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_OVERVIEW)
        ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_LINK_GENERAL)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_GENERAL)
        ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_PROFILE_HARDWARE)
        profilehardwaretype = selenium2lib._get_text(FusionServerProfilesPage.ID_PROFILE_HARDWARE)

        # Navigate server hardware page, verify server hardware to assign profile  and power off the server
        if not selenium2lib._is_element_present(FusionServerHardwarePage.ID_PAGE_LABEL):
            base_page.navigate_base(FusionServerHardwarePage.ID_PAGE_LABEL,
                                    FusionUIBaseElements.ID_MENU_LINK_SERVER_HARDWARE, "css=span.hp-page-item-count")
            server_list = [element.text for element in selenium2lib._element_find(FusionServerHardwarePage.ID_SERVER_LIST_NAMES, False, False)]
            # Check for server to copy profile
            if assignprofile.server not in server_list:
                logger._warn("Server '%s' does not exist" % assignprofile.server)
                continue
            # Verify hardware type of server is compatible with profile hardware
            ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_ELEMENT_SERVER_HARDWARE % assignprofile.server)
            ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_LINK_OVERVIEW)
            ui_lib.wait_for_element_and_click(FusionServerHardwarePage.ID_LINK_HARDWARE)
            ui_lib.wait_for_element_visible(FusionServerHardwarePage.ID_SERVER_HARDWARE, PerfConstants.DEFAULT_SYNC_TIME * 2)
            targethardwaretype = selenium2lib._get_text(FusionServerHardwarePage.ID_SERVER_HARDWARE)
            if not profilehardwaretype == targethardwaretype:
                logger._warn("hardware types of profile '%s' and server '%s' doesn't match" % (assignprofile.profiletoassign, targethardwaretype))
                continue

            if not serverhardware.power_off_server_by_name(assignprofile.server):
                logger._warn("Can't proceed with move server profile to server '%s'" % assignprofile.server)
                continue

            # navigate to Server profile page.
            if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
                navigate()

        ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % assignprofile.profiletoassign)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % assignprofile.profiletoassign)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_MAIN_ACTION)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_ACTION_EDIT)

        if assignprofile.has_property("description"):
            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_SERVER_PROFILE_DESCRIPTION, assignprofile.description)

        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_DROPDOWN_SEARCH_SERVER_HARDWARE)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % assignprofile.server)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_UPDATE_SERVER_PROFILE)

        ui_lib.wait_for_element(FusionServerProfilesPage.ID_ADD_PROFILE_NOTIFICATION)

        if CreateServerProfile.wait_create_server_profile_dialog_disappear(timeout=180, fail_if_false=False) is True:
            FusionUIBase.show_activity_sidebar()
            if FusionUIBase.wait_activity_action_ok(assignprofile.name, 'Update', timeout=720, fail_if_false=True) is True:
                FusionUIBase.show_activity_sidebar()
                if CommonOperationServerProfile.wait_server_profile_status_ok(assignprofile.name, timeout=180, fail_if_false=True) is True:
                    logger.info("Assigned profile '%s' successfully to %s hardware" % (assignprofile.name, assignprofile.server))
                else:
                    logger.warn("'wait_server_profile_status_ok' = FALSE, skip to next profile ... ")
                continue
            else:
                logger.warn("'wait_activity_action_ok' = FALSE, skip to next profile ... ")
                FusionUIBase.show_activity_sidebar()
                continue
        else:
            logger.warn("'wait_create_server_profile_dialog_disappear' = FALSE, skip to next profile ... ")
            CreateServerProfile.click_cancel_button()

    return True


def _is_element_present_inactivity_page_with_time(profilename, activity, starttime):
    """ """
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionActivityPage.ID_PAGE_LABEL):
        base_page.navigate_base(FusionActivityPage.ID_PAGE_LABEL, FusionUIBaseElements.ID_MENU_LINK_ACTIVITY, "css=span.hp-page-item-count")

    ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_SELECT % (activity, profilename, starttime), PerfConstants.PROFILE_POWER_VALIDATION)
    if ui_lib.wait_for_element_visible(FusionActivityPage.ID_ACTIVITY_SELECT % (activity, profilename, starttime)):
        logger._log_to_console_and_log_file("'%s' is present in Activity page" % profilename)
        return True
    else:
        logger._warn("'%s' is not present in Activity page" % profilename)
        selenium2lib.capture_page_screenshot()
        return False


def _get_assigned_server_for_profile():
    """ This function is to list the assigned server for profiles in the appliance
        Example:
       _get_assigned_server_for_profile()
    """
    selenium2lib = ui_lib.get_s2l()
    serverprofiledict = {}
    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
        navigate()
    profile_list = [el.text for el in selenium2lib._element_find(FusionServerProfilesPage.ID_PROFILE_LIST_NAMES, False, False)]

    for profobj in profile_list:
        if not select_server_profile(profobj):
            ui_lib.fail_test("Exiting function get assigned server, Not selected profile %s" % profobj)
        else:
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_SELECTOR)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_DROPDOWN_SELECT % 'Overview')
            ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_SERVER_HARDWARE)
            strhardware = selenium2lib._get_text(FusionServerProfilesPage.ID_SERVER_HARDWARE)
            if strhardware != 'unassigned' and ('empty' not in strhardware):
                serverprofiledict[profobj] = strhardware
    return serverprofiledict


def _edit_server_hardware(*profile_obj):
    """
    _edit_server_hardware(profiles)

    This function is to edit the server hardware field of the given server profile.
    """
    selenium2lib = ui_lib.get_s2l()

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    for profile in profile_obj:
        if not selenium2lib._is_element_present(FusionServerHardwarePage.ID_PAGE_LABEL):
            base_page.navigate_base(FusionServerHardwarePage.ID_PAGE_LABEL,
                                    FusionUIBaseElements.ID_MENU_LINK_SERVER_HARDWARE, "css=span.hp-page-item-count")
        if not serverhardware.power_off_server_by_name(profile.server):
            logger._warn("Failed to powerOff the server %s" % profile.server)
            logger._warn("Can't proceed with server profile creation on server %s" % profile.server)
            continue
        # Navigating to Server profile page
        if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
            ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
            navigate()

        profile_list = [el.text for el in selenium2lib._element_find(FusionServerProfilesPage.ID_PROFILE_LIST_NAMES, False, False)]
        if profile.profilename not in profile_list:
            logger._warn("Profile '%s' does not exist" % profile.profilename)
            continue
        if profile.server == "":
            logger._warn("Mandatory fields to edit server hardware can't be empty")
            continue

        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % profile.profilename)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_MAIN_ACTION)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_ACTION_EDIT)

        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_DROPDOWN_SEARCH_SERVER_HARDWARE)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_SEARCH_HARDWARE)
        if profile.unassign == "unassigned":
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % profile.unassign)
            logger._log_to_console_and_log_file("Unassigning the server profile")
        else:
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % profile.server)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_UPDATE_SERVER_PROFILE)

        if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_PROFILE_OFF_ERROR):
            logger._log_to_console_and_log_file("Server is not powered off, and switching off now")
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_PROFILE_OFF_ERROR)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_POWER_PRESS_AND_HOLD)
            ui_lib.wait_for_element(FusionServerProfilesPage.ID_SERVER_POWER_OFF_VALIDATE, PerfConstants.SERVER_POWER_OFF)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_DROPDOWN_SEARCH_SERVER_HARDWARE)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_SEARCH_HARDWARE)
            if profile.unassign == "unassigned":
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % profile.unassign)
                logger._log_to_console_and_log_file("Unassigning the server profile")
            else:
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % profile.server)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_UPDATE_SERVER_PROFILE)

            if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_PROFILE_OFF_ERROR):
                logger._warn("Failed to power off the server %s" % profile.server)
            else:
                logger._log_to_console_and_log_file("Successfully server %s is powered off" % profile.server)

        ui_lib.wait_for_element(FusionServerProfilesPage.ID_ADD_PROFILE_NOTIFICATION)
        # New Code
        if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_ADD_PROFILE_NOTIFICATION):
            errMsg = selenium2lib._get_text(FusionServerProfilesPage.ID_ADD_PROFILE_NOTIFICATION_CONTENT)
            logger._warn(errMsg)
            logger._warn("Unable to edit profile server hardware %s" % profile.profilename)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_SERVER_PROFILE)
            continue
        ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_UPDATE_PROFILE_TIMESTAMP)
        strTimeStamp = selenium2lib._get_text(FusionServerProfilesPage.ID_UPDATE_PROFILE_TIMESTAMP)
        logger._log_to_console_and_log_file(strTimeStamp)

        # Verify profile server hardware updation status in server profile page (Under Activity tab)
        ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_LINK_OVERVIEW)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_OVERVIEW)
        ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_LINK_ACTIVITY)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_ACTIVITY)

        ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_PROFILE_CREATION_STATUS % ("Update", strTimeStamp), PerfConstants.CREATE_SERVER_PROFILE_TIME)

        if selenium2lib._is_element_present(FusionServerProfilesPage.ID_PROFILE_CREATION_STATUS % ("Update", strTimeStamp)):
            logger._log_to_console_and_log_file("Server profile '%s' is edited successfully" % profile.profilename)
        else:
            logger._warn("Failed to edit server profile '%s' hardware" % profile.profilename)


def verify_can_not_create_profile_with_used_specified_ids(profile_obj):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    total = len(profile_obj)
    already_exists = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("creating a server profile with name '%s' ..." % profile.name)
        # checking if the profile is already existing
        if not VerifyServerProfile.verify_server_profile_not_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' already exists" % profile.name)
            already_exists += 1
            continue
        # - Prep the auto_power_off switch
        # - By default, this keyword will power off the server if it's powered on -- unless the attribute 'auto_power_off' is explicitly set to 'false'
        auto_power_off = False if getattr(profile, 'auto_power_off', '').lower() == 'false' else True
        # open Create SP dialog and enter data ...
        CreateServerProfile.click_create_profile_button()
        CreateServerProfile.wait_create_server_profile_dialog_shown()

        CreateServerProfile.input_name(profile.name)
        CreateServerProfile.input_description(getattr(profile, 'desc', ''))
        # Input 'Server hardware'
        # - input server name,
        # - select option from the popped out drop-down list,
        # - power off the server if the it is powered on,
        # - verify the server hardware type of the selected one is refreshed to the type name displayed in the drop-down list
        #     for selecting server hardware
        if not CreateServerProfile.input_select_server_hardware(profile.server, auto_power_off=auto_power_off):
            logger.warn("server hardware '%s' is not selected for creating server profile, may be wrong name, or powered on but failed to power it off. "
                        "test will skip this profile '%s' and continue to create other server profiles" % (profile.server, profile.name))
            continue
        msg = CreateServerProfile.get_error_message_from_server_hardware()
        if msg is not None:
            logger.warn("error occurred, server profile can not be created successfully: \n<%s>" % msg)
            ui_lib.fail_test(msg)
        # input 'Server hardware type', 'Enclosure group'
        # TODO: update Edit Server Profile as well
        if profile.server != 'unassigned':
            # verify if 'Server hardware type' is automatically set by selecting 'Server hardware'
            sht_selected = CreateServerProfile.get_selected_server_hardware_type(profile.server)
            if profile.hardwareType not in sht_selected:
                msg = "selected server hardware type '%s' of server '%s' is NOT consistent with test data '%s'" % (sht_selected, profile.server, profile.hardwareType)
                logger.warn(msg)
                ui_lib.fail_test(msg)
        else:
            # input 'Enclosure group'
            CreateServerProfile.input_select_server_hardware_type(profile.hardwareType)
            CreateServerProfile.input_select_enclosure_group(profile.enclgroup) if getattr(profile, 'enclgroup', None) is not None else None
            sht_selected = CreateServerProfile.get_selected_server_hardware_type(profile.server)
        # input 'Affinity' for BL server, or when 'server hardware' == 'unassigned'
        if profile.hardwareType[:2:] == 'BL' or profile.server == 'unassigned':
            if getattr(profile, 'Affinity', None) is not None:
                logger.info("test data for 'Affinity' is found: <%s>, start setting Affinity ..." % profile.Affinity)
                CreateServerProfile.select_affinity_by_text(profile.Affinity)

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
            CreateServerProfile.Advanced.set(profile)

        CreateServerProfile.click_create_button()
        if CommonOperationServerProfile.BootSettings.get_error_message_from_boot_mode() is not None:
            logger.warn("test data of server profile '%s' may be wrongly defined for 'Boot mode', which caused an error that blocks profile being created. "
                        "test will skip this profile and continue to create other server profiles" % profile.name)
            continue

        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=30)
        if status is True:
            logger.info("error occurred (might be expected error): %s" % msg)
            if "already in use" in msg:
                logger.info("Successfully verified 'can not create profile with used specified ids'")
                ret = True
            else:
                logger.warn("Failed to verify 'can not create profile with used specified ids' -- expected error message 'already in use' not found")
                ret = False
        else:
            logger.warn("Failed to verify 'can not create profile with used specified ids' -- no error message occured at all")
            ret = False

        CreateServerProfile.click_cancel_button(fail_if_false=False)
        CreateServerProfile.wait_create_server_profile_dialog_disappear(fail_if_false=False)
        return ret


def verify_can_not_create_server_profile_when_server_power_on(profile_obj):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    total = len(profile_obj)
    already_exists = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("creating a server profile with name '%s' ..." % profile.name)
        # checking if the profile is already existing
        if not VerifyServerProfile.verify_server_profile_not_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' already exists" % profile.name)
            already_exists += 1
            continue

        # open Create SP dialog and enter data ...
        CreateServerProfile.click_create_profile_button()
        CreateServerProfile.wait_create_server_profile_dialog_shown()

        CreateServerProfile.input_name(profile.name)
        CreateServerProfile.input_description(getattr(profile, 'desc', ''))

        CreateServerProfile.select_powered_on_server_hardware(profile.server, 10, fail_if_false=True)

        CreateServerProfile.get_error_message_from_server_hardware(5, True)
        # Input 'Server hardware'
        # - input server name,
        # - select option from the popped out drop-down list,
        # - power off the server if the it is powered on,
        # - verify the server hardware type of the selected one is refreshed to the type name displayed in the drop-down list
        #     for selecting server hardware

        VerifyServerProfile.is_power_on_error_visible_when_create_server_profile(profile.server, 10)

        # input 'Server hardware type', 'Enclosure group'
        # TODO: update Edit Server Profile as well
        if profile.server != 'unassigned':
            # verify if 'Server hardware type' is automatically set by selecting 'Server hardware'
            sht_selected = CreateServerProfile.get_selected_server_hardware_type(profile.server)
            if profile.hardwareType not in sht_selected:
                msg = "selected server hardware type '%s' of server '%s' is NOT consistent with test data '%s'" % (sht_selected, profile.server, profile.hardwareType)
                logger.warn(msg)
                ui_lib.fail_test(msg)
        else:
            # input 'Enclosure group'
            CreateServerProfile.input_select_server_hardware_type(profile.hardwareType)
            CreateServerProfile.input_select_enclosure_group(profile.enclgroup) if getattr(profile, 'enclgroup', None) is not None else None
            sht_selected = CreateServerProfile.get_selected_server_hardware_type(profile.server)
        # input 'Affinity' for BL server, or when 'server hardware' == 'unassigned'
        if profile.hardwareType[:2:] == 'BL' or profile.server == 'unassigned':
            if getattr(profile, 'Affinity', None) is not None:
                logger.info("test data for 'Affinity' is found: <%s>, start setting Affinity ..." % profile.Affinity)
                CreateServerProfile.select_affinity_by_text(profile.Affinity)

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
            CreateServerProfile.Advanced.set(profile)

        CreateServerProfile.click_create_button()
        if CommonOperationServerProfile.BootSettings.get_error_message_from_boot_mode() is not None:
            logger.warn("test data of server profile '%s' may be wrongly defined for 'Boot mode', which caused an error that blocks profile being created. "
                        "test will skip this profile and continue to create other server profiles" % profile.name)
            continue

        if VerifyServerProfile.is_power_on_error_visible_when_create_server_profile(server_name=profile.server, fail_if_false=False) is True:
            logger.info("successfully verified 'Can not create server profile when server profile is ON' -- expected error message found")
            ret = True
        else:
            logger.warn("failed to verify 'Can not create server profile when server profile is ON' -- expected error message NOT found!")
            ret = False

        CreateServerProfile.click_cancel_button(fail_if_false=False)
        CreateServerProfile.wait_create_server_profile_dialog_disappear(fail_if_false=False)
        return ret


def verify_can_not_create_server_profile_with_bad_server_hardware(profile_obj):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    for _, profile in enumerate(profile_obj):

        logger.info("creating a server profile with name '%s' ..." % profile.name)
        # checking if the profile is already existing
        if not VerifyServerProfile.verify_server_profile_not_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' already exists" % profile.name)
            continue

        CreateServerProfile.click_create_profile_button()
        CreateServerProfile.wait_create_server_profile_dialog_shown()

        CreateServerProfile.input_name(profile.name)
        CreateServerProfile.input_description(getattr(profile, 'desc', ''))

        CreateServerProfile.input_select_server_hardware(profile.server, auto_power_off=False)
        CreateServerProfile.click_create_button()
        err_msg = CreateServerProfile.get_error_message_from_server_hardware(timeout=5, fail_if_false=False)
        if err_msg is not None:
            logger.debug("server hardware '%s' is found with error message ..." % profile.server)
            if 'invalid server hardware' in err_msg.lower():
                logger.debug("server hardware '%s' is found with the expected error message '%s', '%s' returns TRUE" % (profile.server, err_msg, sys._getframe().f_code.co_name))
                logger.info("successfully verified 'can not create server profile with bad server hardware'")
                ret = True
            else:
                logger.warn("server hardware '%s' is NOT found with the expected error message 'invalid server hardware' in '%s', '%s' returns FALSE" % (profile.server, err_msg, sys._getframe().f_code.co_name))
                logger.warn("failed to verify 'can not create server profile with bad server hardware'")
                ret = False
        else:
            logger.warn("server hardware '%s' is NOT found with any error message, '%s' returns FALSE" % (profile.server, sys._getframe().f_code.co_name))
            logger.warn("failed to verify 'can not create server profile with bad server hardware'")
            ret = False

        CreateServerProfile.click_cancel_button(fail_if_false=False)
        CreateServerProfile.wait_create_server_profile_dialog_disappear(fail_if_false=False)
        return ret


def verify_can_not_create_server_profile_with_bad_enclosure_group(profile_obj):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    for _, profile in enumerate(profile_obj):

        logger.info("creating a server profile with name '%s' ..." % profile.name)
        # checking if the profile is already existing
        if not VerifyServerProfile.verify_server_profile_not_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' already exists" % profile.name)

            continue
        # open Create SP dialog and enter data ...

        CreateServerProfile.click_create_profile_button()
        CreateServerProfile.wait_create_server_profile_dialog_shown()

        CreateServerProfile.input_name(profile.name)
        CreateServerProfile.input_description(getattr(profile, 'desc', ''))
        # Input 'Server hardware'
        # - input server name,
        # - select option from the popped out drop-down list,
        # - power off the server if the it is powered on,
        # - verify the server hardware type of the selected one is refreshed to the type name displayed in the drop-down list
        #     for selecting server hardware

        if profile.server != 'unassigned':
            # for this keyword, 'Server hardware' must be 'unassigned',
            # otherwise 'Enclosure group' is not allowed to be inputted with an invalid value
            logger.warn("test data of server profile '%s' may be wrongly defined for 'Server hardware', this makes 'Enclosure group' not editable, keyword '%s' returns FALSE" % (profile.name, sys._getframe().f_code.co_name))
            logger.warn("failed to verify 'can not create server profile with bad enclosure group' -- 'Server hardware' is not 'unassigned'")
            ret = False
        else:
            CreateServerProfile.input_select_server_hardware(profile.server, auto_power_off=False)
            CreateServerProfile.input_select_server_hardware_type(profile.hardwareType)
            # input 'Enclosure group'
            CreateServerProfile.input_select_enclosure_group(profile.enclgroup, timeout=5, fail_if_false=False)
            CreateServerProfile.click_create_button()
            err_msg = CreateServerProfile.get_error_message_from_enclosure_group(timeout=5, fail_if_false=False)
            if err_msg is not None:
                logger.debug("enclosure group '%s' is found with error message ..." % profile.enclgroup)
                if 'invalid enclosure group' in err_msg.lower():
                    logger.debug("enclosure group '%s' is found with the expected error message '%s', '%s' returns TRUE" % (profile.enclgroup, err_msg, sys._getframe().f_code.co_name))
                    logger.info("successfully verified 'can not create server profile with bad enclosure group'")
                    ret = True
                else:
                    logger.warn("enclosure group '%s' is NOT found with the expected error message 'invalid server hardware' in '%s', '%s' returns FALSE" % (profile.enclgroup, err_msg, sys._getframe().f_code.co_name))
                    logger.warn("failed to verify 'can not create server profile with bad enclosure group'")
                    ret = False
            else:
                logger.warn("enclosure group '%s' is NOT found with any error message, '%s' returns FALSE" % (profile.enclgroup, sys._getframe().f_code.co_name))
                logger.warn("failed to verify 'can not create server profile with bad enclosure group'")
                ret = False

        CreateServerProfile.click_cancel_button(fail_if_false=False)
        CreateServerProfile.wait_create_server_profile_dialog_disappear(fail_if_false=False)
        return ret


def verify_server_profile_ui_view_function():
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
    CreateServerProfile.click_create_profile_button()
    CreateServerProfile.wait_create_server_profile_dialog_shown()
    logger.debug("Verify [General] View")
    FusionUIBase.select_view_by_name('General')

    logger.debug("Verify [Firmware] View")
    FusionUIBase.select_view_by_name('Firmware')

    logger.debug("Verify [Connections] View")
    FusionUIBase.select_view_by_name('Connections')

    logger.debug("Verify [Local Storage] View")
    FusionUIBase.select_view_by_name('Local Storage')

    logger.debug("Verify [SAN Storage] View")
    FusionUIBase.select_view_by_name('SAN Storage')

    logger.debug("Verify [Boot Settings] View")
    FusionUIBase.select_view_by_name('Boot Settings')

    logger.debug("Verify [BIOS Settings] View")
    FusionUIBase.select_view_by_name('BIOS Settings')

    logger.debug("Verify [Advanced] View")
    FusionUIBase.select_view_by_name('Advanced')
    return True


def negative_test_for_check_general_session(profile_obj):
    """
        This function will perform some negative tests in the "General" session
    """
    status = True

    logger._log_to_console_and_log_file("### Testing the 'General' session ###")

    # LIST_OF_TESTS specify a list of elements to be validated in the "General" page
    # For each element of the list, we add the following information:
    # [0] = The locator of the field that we'll input the data (e.g. FusionPage.DescriptionEditBox)
    # [1] = The input data (e.g. MyProfile, !@#%&&*, blablabla, etc...)
    # [2] = The locator of the error message (e.g. FusionPage.ErrorMessage)
    # [3] = The Message name that will be displayed at the console and logs
    for profile in profile_obj:
        LIST_OF_TESTS = [[None, "", FusionServerProfilesPage.ID_WARNING_FIELD_REQUIRED, "ID_WARNING_FIELD_REQUIRED"],
                         [FusionServerProfilesPage.ID_SERVER_HARDWARE_TEXT_BOX, "none", FusionServerProfilesPage.ID_WARNING_INVALID_SERVERHARDWARE, "ID_WARNING_INVALID_SERVERHARDWARE"],
                         [FusionServerProfilesPage.ID_INPUT_SERVER_HARDWARE_TYPE, "none", FusionServerProfilesPage.ID_WARNING_INVALID_SERVER_HARDWARE_TYPE, "ID_WARNING_INVALID_SERVER_HARDWARE_TYPE"],
                         [FusionServerProfilesPage.ID_ENCLOSURE_GROUP_TEXT_BOX, "none", FusionServerProfilesPage.ID_WARNING_INVALID_ENCLOSURE_GROUP, "ID_WARNING_INVALID_ENCLOSURE_GROUP"],
                         [FusionServerProfilesPage.ID_SERVER_HARDWARE_TEXT_BOX, profile.invalidChars, FusionServerProfilesPage.ID_WARNING_INVALID_SERVERHARDWARE, "ID_WARNING_INVALID_SERVERHARDWARE"],
                         [FusionServerProfilesPage.ID_INPUT_SERVER_HARDWARE_TYPE, profile.invalidChars, FusionServerProfilesPage.ID_WARNING_INVALID_SERVER_HARDWARE_TYPE, "ID_WARNING_INVALID_SERVER_HARDWARE_TYPE"],
                         [FusionServerProfilesPage.ID_ENCLOSURE_GROUP_TEXT_BOX, profile.invalidChars, FusionServerProfilesPage.ID_WARNING_INVALID_ENCLOSURE_GROUP, "ID_WARNING_INVALID_ENCLOSURE_GROUP"]]
        logger._log_to_console_and_log_file("Testing using MISSING information and with special chars")
        for test in LIST_OF_TESTS:
            # Fill "Server hardware" if needed.
            if test[0] == FusionServerProfilesPage.ID_INPUT_SERVER_HARDWARE_TYPE:
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_SERVER_HARDWARE_DROPDOWN)
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_SERVER_HARDWARE_UNASSIGNED)
                ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_SERVER_PROFILE_NAME, "Name")
            if test[0] is not None:
                ui_lib.wait_for_element_and_input_text(test[0], test[1])
                ui_lib.wait_for_element_and_click(test[0])
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CREATE_SERVER_PROFILE)
            if not correctly_executed(ui_lib.wait_for_element_visible, test[2], test[3]):
                status = False
    if not status:
        ui_lib.fail_test("At least one error message was not displayed")


def correctly_executed(function, parameters, message):
    """ Executes a generic function with parameters and prints a message based on its result """
    if function(parameters):
        logger._log_to_console_and_log_file(message + " was correctly displayed")
        return True
    else:
        logger._log_to_console_and_log_file(message + " was NOT correctly displayed. Failed to access: " + str(parameters))
        selenium2lib = ui_lib.get_s2l()
        selenium2lib.capture_page_screenshot()
        return False


def set_boot_order(profile_obj):
    """
        This function will fill the boot order
    """
    status = True
    logger._log_to_console_and_log_file("")
    logger._log_to_console_and_log_file("### Testing the 'Boot Settings' session ###")
    logger._log_to_console_and_log_file("- Select the 'Legacy BIOS' mode")
    createprofile_elements = ProfileContainer(ProfileContainerType.ADD)
    __select_value_from_a_profile_combo_box(createprofile_elements.ID_COMBO_PROFILE_BOOT_MODE, createprofile_elements.ID_COMBO_PROFILE_BOOT_MODE_LIST % "Legacy BIOS")
    # Set invalid values
    logger._log_to_console_and_log_file("Testing using invalid values")
    for profile in profile_obj:
        items = [["CD", profile.cd], ["USB", profile.usb], ["HardDisk", profile.harddisk]]
        for data in items:
            ui_lib.wait_for_element_and_input_text("name=%s" % data[0], data[1])
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_CREATE_SERVER_PROFILE_FORM)
            if data[0] == "HardDisk":
                data[0] = "Hard Disk"
            if ui_lib.wait_for_element_text(FusionServerProfilesPage.ID_BOOT_ORDER_POSITION % data[0], data[1], timeout=1):
                logger._log_to_console_and_log_file("- " + "'" + data[0] + "'" + " field was not cleared to the default value and persisted as '" + str(data[1]) + "'")
                status = False
            else:
                logger._log_to_console_and_log_file("- " + "'" + data[0] + "'" + " field was correctly cleared to the default value")
    return status


def __select_value_from_a_profile_combo_box(combo_box_element, combo_box_list_option):
    """
        This function selects the value in a combo box element.
        This is useful when the combo box list is mapped with a string variable (e.g.: "//ul/li/a[text()='%s']")

        Example: __select_value_from_a_profile_combo_box(combo_box_element, combo_box_list_option)
    """
    retValue = True
    retValue &= ui_lib.wait_for_element_and_click(combo_box_element)
    retValue &= ui_lib.wait_for_element_visible(combo_box_list_option)
    retValue &= ui_lib.wait_for_element_and_click(combo_box_list_option)

    if retValue is False:
        logger._log_to_console_and_log_file("Error selecting element %s from combo_box %s" % (combo_box_list_option, combo_box_element))
    return retValue


def add_label_to_profile(*profile_label):
    """ This function is to add label to server profile
        Example:
            add_label_to_profile(*profile_label)
    """
    s2l = ui_lib.get_s2l()
    logger._log_to_console_and_log_file("Function call to add label to server profile ")

    if isinstance(profile_label, test_data.DataObj):
        profile_label = [profile_label]
    elif isinstance(profile_label, tuple):
        profile_label = list(profile_label[0])

    if not ui_lib.wait_for_element(FusionServerProfilesPage.ID_PAGE_LABEL):
        if not navigate():
            return False

    for label in profile_label:
        ui_lib.refresh_browser(FusionUIBaseElements.ID_MENU_ONE_VIEW, PerfConstants.DEFAULT_SYNC_TIME)
        if not ui_lib.wait_for_element(FusionServerProfilesPage.ID_SELECT_PROFILE % label.servername):
            return False
        else:
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_SELECT_PROFILE % label.servername)

        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_OVERVIEW)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_LABEL)

        logger._log_to_console_and_log_file("Adding label to profile '{0}'".format(label.servername))
        if ui_lib.wait_for_element(FusionServerProfilesPage.ID_EDIT_LABEL):
            ui_lib.move_to_element_and_click(FusionServerProfilesPage.ID_LABEL, FusionServerProfilesPage.ID_EDIT_LABEL)
            if ui_lib.wait_for_element(FusionServerProfilesPage.ID_EDIT_LABEL_PANEL):
                ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_LABEL_NAME, label.name)
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ADD_LABEL_BTN)
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_OK_LABEL_BTN)
            else:
                logger._warn("Failed to navigate edit label panel")
                return False
        else:
            logger._warn("Could not find Edit button to add label")

        if ui_lib.wait_for_element(FusionServerProfilesPage.ID_ADDED_LABEL % label.name):
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ADDED_LABEL % label.name)
            profile_list = []
            ui_lib.wait_for_element(FusionServerProfilesPage.ID_ALL_PROFILE_LIST, PerfConstants.FUSION_PAGE_SYNC)
            profile_list = [ui_lib.get_text(s) for s in s2l._element_find(FusionServerProfilesPage.ID_ALL_PROFILE_LIST, False, False)]
            for profile in profile_list:
                if profile.lower() == label.servername.lower():
                    logger._log_to_console_and_log_file("Label {0} is successfully added to the profile '{1}'".format(label.name, label.servername))
                else:
                    logger._warn("Failed to add label to the selected profile")
                    return False
    return True


def check_pm_elements(*profile_obj):
    """
        This is a simple check to find all elements.
    """
    profile_elements = ProfileContainer(ProfileContainerType.ADD)
    testResult = True
    logger._log_to_console_and_log_file("########### Start a simple check to find all elements.###########")

    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

        """ Using checkElementsUItbirdPM to verify if the elements were displayed, if not, mark failure as true """
    for profile in profile_obj:
        """ General profile manager """
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_LINK_CREATE_SERVER_PROFILES, " --> ServerProfiles link from Menu ")
        testResult &= correctly_executed(ui_lib.wait_for_element_visible, FusionServerProfilesPage.ID_INPUT_SERVER_PROFILE_NAME, " --> Field Name")
        testResult &= correctly_executed(ui_lib.wait_for_element_visible, FusionServerProfilesPage.ID_INPUT_SERVER_PROFILE_DESCRIPTION, " --> Field description")

        """ Select hardware """
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_COMBO_SERVER_HARDWARE_DROPDOWN, " --> Server Hardware Dropdown ")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % profile.server, " --> '" + profile.server + "' option in 'Server hardware' dropdown")

        """ Select server hardware type """
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_COMBO_SERVER_HARDWARE_TYPE_DROPDOWN, " --> Server Hardware Type Dropdown ")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % profile.hardwaretype, " --> '" + profile.hardwaretype + "' option in 'Server hardware type' dropdown")

        """ Verify Enclosure Group """
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_COMBO_ENCLOSURE_GROUP_DROPDOWN, " --> Enclosure Group Dropdown ")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % profile.enclgroup, " --> Select combo enclosure group dropdown: '" + profile.enclgroup + "'")

        """ Selecting the Affinity """
        logger._log_to_console_and_log_file("########### Selected valid affinity..###########")
        for item in FusionServerProfilesPage.LIST_NAME_AFFINITY:
            testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_AFFINITY_DROP_DOWN, " --> Affinity combobox ")
            testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_COMBO_AFFINITY_ITEM % item, " --> '" + item + "' option in 'Affinity' dropdown")

        """   Firmware Baseline     """
        testResult &= ui_lib.wait_for_element_and_click(profile_elements.ID_COMBO_MENU_VIEW)
        testResult &= ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_FIRMWARE)
        logger._log_to_console_and_log_file("########### Accessing to firmware baseline..###########")

        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_FIRMWARE_BASELINE_DROP_DOWN, " --> Accessing to firmware baseline ")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_LINK_FIRMWARE_BASELINE_ADD, " --> Clicking on 'ADD Firmware Baseline' link")
        testResult &= correctly_executed(ui_lib.wait_for_element_visible, FusionServerProfilesPage.ID_BTN_FIRMWARE_BASELINE_YES_PROCEED, " --> Looking for 'Yes, proceed' button")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_BTN_FIRMWARE_BASELINE_CANCEL, " --> Click on 'Cancel' button")

        """ Add Connections """
        logger._log_to_console_and_log_file("########### Accessing to add connections..###########")
        testResult &= ui_lib.wait_for_element_and_click(profile_elements.ID_COMBO_MENU_VIEW)
        testResult &= ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_CONNECTIONS, " --> Connections Link on Profile Dropdown Menu")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_BTN_ADD_NETWORK_CONNECTION, " --> Clicking on 'Add Connection' button")
        testResult &= correctly_executed(ui_lib.wait_for_element_visible, FusionServerProfilesPage.ID_INPUT_CONNECTION_NAME, " --> Field Name Connection")

        for item in FusionServerProfilesPage.LIST_NAME_FUNCTIONTYPE:
            testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_COMBO_CONNECTION_FUNCTION_TYPE, " --> Function type combobox ")
            testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_SELECT_BOX_GENERIC_ELEMENT % (item, item), " --> '" + item + "' option in 'Function type' dropdown")
        testResult &= correctly_executed(ui_lib.wait_for_element_visible, FusionServerProfilesPage.ID_INPUT_NETWORK_ADD_CONNECTION, " --> Field Network")
        testResult &= correctly_executed(ui_lib.wait_for_element_visible, FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_CONNECTON, " --> Looking for 'Add' button")
        testResult &= correctly_executed(ui_lib.wait_for_element_visible, FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_PLUS_CONNECTON, " --> Looking for 'Add+' button")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_BTN_CANCEL_ADD_CONNECTION, " --> Clicking on 'Cancel' button")

        """ Local storage volumes """
        testResult &= ui_lib.wait_for_element_and_click(profile_elements.ID_COMBO_MENU_VIEW)
        testResult &= ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_LOCAL_STORAGE)
        logger._log_to_console_and_log_file("########### Accessing to Local Storage volumes..###########")
        selenium2lib.select_checkbox(FusionServerProfilesPage.ID_CHKBOX_LOCAL_STORAGE)
        testResult &= correctly_executed(ui_lib.wait_for_checkbox_and_select, FusionServerProfilesPage.ID_CHKBOX_LOCAL_STORAGE, " --> Clicking a checbox of Manage Local Storage")
        testResult &= correctly_executed(ui_lib.wait_for_checkbox_and_select, FusionServerProfilesPage.ID_CHKBOX_MANAGE_INTEGRATED_CONTROLLER, " --> Clicking a checkbox of manage integrated controller")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_BTN_MANAGE_STORAGE_CONTROLLER_CLOSE, " --> Clicking on 'Close' button")
        testResult &= correctly_executed(ui_lib.wait_for_checkbox_and_unselect, FusionServerProfilesPage.ID_EDIT_INITIALIZE_LOCAL_STORAGE, " --> Uncheckbox re-initialize internal storage on next application of server profile")
        testResult &= correctly_executed(ui_lib.wait_for_checkbox_and_select, FusionServerProfilesPage.ID_CHKBOX_IMPORT_EXISTING, " --> Checkbox import exsisting logical drives")
        testResult &= correctly_executed(ui_lib.wait_for_checkbox_and_unselect, FusionServerProfilesPage.ID_CHKBOX_IMPORT_EXISTING, " --> Uncheckbox import exsisting logical drives")
        testResult &= correctly_executed(ui_lib.wait_for_checkbox_and_select, FusionServerProfilesPage.ID_EDIT_INITIALIZE_LOCAL_STORAGE, " --> Checkbox re-initialize internal storage on next application of server profile")

        for item in FusionServerProfilesPage.LIST_NAME_CONTROLLER_MODE:
            if __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_CONTROLLER_MODE, FusionServerProfilesPage.ID_COMBO_DEFAULT_ITEM % item):
                testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_CHKBOX_CONTROLLER_MODE, " --> '" + item + "' option in 'Controller mode' dropdown")
            else:
                logger._log_to_console_and_log_file(" --> Failed to select item %s in controller mode for local storage" % item)
                testResult &= False

        """ Create Logical Drive """
        logger._log_to_console_and_log_file("########### Create Logical Drive..###########")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_BTN_CREATE_LOGICAL_DRIVE, " --> Select button create logical drive")
        testResult &= correctly_executed(ui_lib.wait_for_element_visible, FusionServerProfilesPage.ID_NAME_ADD_LOGICAL_DRIVE, " --> Show a field name in logical drive")
        for item in FusionServerProfilesPage.LIST_NAME_RAID_LEVEL:
            if __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_RAID_LEVEL, FusionServerProfilesPage.ID_COMBO_DEFAULT_ITEM_RAID % item):
                testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_COMBO_ADD_LOGICAL_RAID_LEVEL, " --> '" + item + "' option 'RAID level' dropdown")
            else:
                logger._log_to_console_and_log_file(" --> Failed to select item %s in logical drive combobox" % item)
                testResult &= False
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_LISTBOX_NUMBER_PHYSICAL_DRIVES, " --> Show a number of physical drives")
        for item in FusionServerProfilesPage.LIST_NAME_DRIVE_TECHNOLOGY:
            if __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_NAME_DRIVE_TECHNOLOGY, FusionServerProfilesPage.ID_COMBO_DEFAULT_ITEM_DRIVE % item):
                testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_COMBO_DRIVE_TECHNOLOGY, " --> '" + item + "' option 'Drive technology' dropdown")
            else:
                logger._log_to_console_and_log_file(" --> Failed to select item %s in logical drive type combobox" % item)
                testResult &= False
        testResult &= correctly_executed(ui_lib.wait_for_element_visible, FusionServerProfilesPage.ID_BTN_CREATE_LOGICAL_DRIVE_FORM, " --> Looking for 'Create' button")
        testResult &= correctly_executed(ui_lib.wait_for_element_visible, FusionServerProfilesPage.ID_BTN_CREATE_PLUS_LOGICAL_DRIVE, " --> Looking for 'Create +' button")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_BTN_ADD_LOGICAL_DRIVE_CANCEL, " --> Clicking on 'Cancel' button of screen add logical drive")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_COMBO_BOOT_DRIVE_LOCAL_STORAGE, " --> Select combo boot drive")

        """    SAN Storage     """
        logger._log_to_console_and_log_file("########### Accessing to SAN storage..###########")
        testResult &= ui_lib.wait_for_element_and_click(profile_elements.ID_COMBO_MENU_VIEW)
        testResult &= ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_SANSTORAGE, " --> San Storage Link on Profile Dropdown Menu")
        testResult &= correctly_executed(ui_lib.wait_for_checkbox_and_select, FusionServerProfilesPage.ID_CHKBOX_SAN_STORAGE, " --> Check manage san storage")

        for item in FusionServerProfilesPage.LIST_NAME_HOST_OS_TYPE:
            testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_OS_TYPE_DROP_DOWN, " --> Combobox Host OS type")
            testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_OS_TYPE_SELECT % item, " --> '" + item + "' option 'Host OS type' dropdown")

        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_BTN_ADD_STORAGE, " --> Clicking on 'Add Volume' button")
        logger._log_to_console_and_log_file(" --> Select Existing volume ")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_VOLUME_TYPE, " --> Combobox type")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.GET_TEXT_FROM_SPAN % VolumeTypes.EXISTING_VOLUME, " --> '" + VolumeTypes.EXISTING_VOLUME + "' option 'Type' dropdown")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_VOLUME_NAME_SEARCH, " --> Search name of volume ")

        logger._log_to_console_and_log_file(" --> Select New volume ")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_VOLUME_TYPE, " --> Combobox type")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.GET_TEXT_FROM_SPAN % VolumeTypes.NEW_VOLUME, " --> '" + VolumeTypes.NEW_VOLUME + "' option 'Type' dropdown")
        testResult &= correctly_executed(ui_lib.wait_for_element_visible, FusionServerProfilesPage.ID_NEW_VOLUME_NAME, " --> New volume name")
        testResult &= correctly_executed(ui_lib.wait_for_element_visible, FusionServerProfilesPage.ID_NEW_VOLUME_DESCRIPTION, " --> Description")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_LUN_MANUAL, " --> Check Manual on radiobox")
        testResult &= correctly_executed(ui_lib.wait_for_element_visible, FusionServerProfilesPage.ID_LUN_VALUE, " --> Specify a number between 0 and 16383")
        testResult &= correctly_executed(ui_lib.wait_for_element_visible, FusionServerProfilesPage.ID_STORAGE_POOL_DROPDOWN, " --> Search a storage pool ")
        testResult &= correctly_executed(ui_lib.wait_for_element_visible, FusionServerProfilesPage.ID_CAPACITY_BOX, " --> The capacity GiB")

        for item in FusionServerProfilesPage.LIST_NAME_PROVISIONING:
            testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_PROVISIONING_DROPDOWN, " --> Combobox provisioning")
            testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_SELECT_PROVISIONING % item, " --> '" + item + "' option 'Provisioning' dropdown")
        testResult &= correctly_executed(ui_lib.wait_for_checkbox_and_unselect, FusionServerProfilesPage.ID_CHK_PERMANENT, " --> Uncheck permanent")
        testResult &= correctly_executed(ui_lib.wait_for_element_visible, FusionServerProfilesPage.ID_BTN_STORAGE_ADD, " --> Looking for 'Add' button")
        testResult &= correctly_executed(ui_lib.wait_for_element_visible, FusionServerProfilesPage.ID_BTN_STORAGE_ADD_PLUS, " --> Looking for 'Add+' button")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_CANCEL_BTN, " --> Click on 'Cancel' button")

        """    Setting boot order     """
        logger._log_to_console_and_log_file("########### Accessing to Boot Settings..###########")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, profile_elements.ID_COMBO_MENU_VIEW, " --> Create Profile Dropdown Menu ")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_LINK_BOOTSETTINGS, " --> Boot Settings Link on Profile Dropdown Menu")

        if __fill_boot_settings_fields(profile, profile_elements):
            logger._log_to_console_and_log_file(" --> Fill boot settings executed correctly")
        else:
            testResult = False
            logger._log_to_console_and_log_file(" --> Fill boot settings NOT executed correctly")

        """ Select Advanced Options    """
        logger._log_to_console_and_log_file("########### Accessing to Advanced options..###########")
        logger._log_to_console_and_log_file(" --> Radio each in Advanced Options")
        logger._log_to_console_and_log_file(" --> Clicking each radio in Advanced Options")

        if __select_advanced_options(profile, profile_elements):
            logger._log_to_console_and_log_file(" --> Select advanced options elements were correctly displayed")
        else:
            testResult = False
            logger._log_to_console_and_log_file(" --> Select advanced options elements were NOT correctly displayed")

        """ Click on button Cancel Server Profile"""
        testResult &= correctly_executed(ui_lib.wait_for_element_visible, FusionServerProfilesPage.ID_BTN_CREATE_SERVER_PROFILE, " --> Looking for 'Create' button")
        testResult &= correctly_executed(ui_lib.wait_for_element_visible, FusionServerProfilesPage.ID_BTN_CREATE_PLUS_SERVER_PROFILE, " --> Looking for 'Create +' button")
        logger._log_to_console_and_log_file("########### Click on button Cancel Server Profile..###########")
        testResult &= correctly_executed(ui_lib.wait_for_element_and_click, FusionServerProfilesPage.ID_BTN_CANCEL_SERVER_PROFILE, " --> Clicking on 'Cancel' button of server profile")
    if testResult is True:
        logger._log_to_console_and_log_file("- All the elements were found")
    else:
        logger._log_to_console_and_log_file("When test fails, console logging is not filled")
        ui_lib.fail_test("- At least one element was not found. Please check the 'Overview' page")


def __select_advanced_options(profile, elements):
    """ Select Advanced Options    """

    ui_lib.wait_for_element_and_click(elements.ID_COMBO_MENU_VIEW)
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_ADVANCED)
    logger._log_to_console_and_log_file(" --> Setting advanced setup")
    if profile.has_property("mac") and profile.mac != "":
        if profile.mac == "Physical":
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_PHYSICAL_MAC)
        else:
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_VIRTUAL_MAC)
    if profile.has_property("wwn") and profile.wwn != "":
        if profile.wwn == "Physical":
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_PHYSICAL_WWN)
        else:
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_VIRTUAL_WWN)
    if profile.has_property("serial") and profile.serial != "":
        if profile.serial == "Physical":
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_PHYSICAL_SERIAL)
        elif profile.serial == "Virtual":
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_VIRTUAL_SERIAL)
        elif profile.serial == "Userspecified":
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_USER_SPECIFIED_SERIAL)
            if profile.has_property("serialnumber") and profile.serialnumber == "":
                logger._warn("Mandatory fields for user specified serial number can't be empty")
                return False
            if profile.has_property("UUID") and profile.UUID == "":
                logger._warn("Mandatory fields for user specified UUID can't be empty")
                return False
            ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_INPUT_SERIAL_NUMBER)
            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_SERIAL_NUMBER, profile.serialnumber)
            ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_INPUT_UUID_NUMBER)
            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_UUID_NUMBER, profile.UUID)
    return True


def __fill_boot_settings_fields(profile, profile_elements):
    """
        This internal function validates and applies the boot setting configuration for a server profile.
        profile xml accepts the following attributes:
            manageBoot: Optional. Can be "true" or "false", and refers to "Manage boot mode" checkbox;
            bootMode: Mandatory when manage boot mode is "true", Possible values are: UEFI", "UEFI optimized", or "Legacy BIOS";
                     When bootMode is "UEFI" or "UEFI optimized", the following attributes can be set:
                            bootPolicy: Optional. Possible values are: "Auto", "IPv4 only", "IPv6 only", "IPv4 then IPv6", or "IPv6 than IPv4";
                            manageBootOrder: Optional. Can be "true" or "false", and refers to "Manage boot order" checkbox;
                           primaryBootDevice: Optional. Possible values are: "Hard disk" or "PXE";
                     When bootMode is "Legacy BIOS", the following attributes can be set:
                           <bootorder device="device_name" /> : list of boot order devices. The values for device_name are: "Floppy", "CD", "USB" and "HardDisk". "Floppy" is not valid for Gen9 or later. It refers to the boot order devices, which will be ordered in the same order of the <bootorder> list;

    eg:  profile with boot mode UEFIoptimized and all boot attributes (bootPolicy, manageBootOrder, primaryBootDevice)
        <profile name="TBird Unassigned Profile" profile="TBird Unassigned Profile" profileName="TBird Unassigned Profile"
         server="unassigned" mac="Virtual" serial="Virtual" hardwaretype="BL460t Gen9 1" enclgroup="EG" manageBoot="true"
          bootMode="UEFI optimized" bootPolicy="IPv4 then IPv6" primaryBootDevice="Hard disk"></profile>

        profile with boot mode UEFI and without boot attributes (bootPolicy, manageBootOrder, primaryBootDevice)
        <profile name="TBird Unassigned Profile" profile="TBird Unassigned Profile" profileName="TBird Unassigned Profile"
         server="unassigned" mac="Virtual" serial="Virtual" hardwaretype="BL460t Gen9 1" enclgroup="EG" manageBoot="true"
          bootMode="UEFI"></profile>

        profile with legacy BIOS boot mode and boot order
        <profile name="Encl1-660" profile="Encl1-660" profileName="Encl1-660" server="Encl1, bay 1" mac="Virtual" serial="Virtual"
         manageBoot="true" bootMode="Legacy BIOS">
            <bootorder device="HardDisk" />
            <bootorder device="USB" />
            <bootorder device="CD" />
        </profile>

        Example: __fill_boot_settings_fields(profile, profile_elements)
    """
    result = True
    selenium2lib = ui_lib.get_s2l()
    # Validate the profile in XML file
    __validate_boot_settings_properties_in_xml_file(profile)
    # If XML is fine, go ahead filling Boot Setting UI fields
    result &= ui_lib.wait_for_element_and_click(profile_elements.ID_COMBO_MENU_VIEW)
    result &= ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_BOOTSETTINGS,
                                                PerfConstants.DEFAULT_SYNC_TIME)
    ui_lib.wait_for_element_visible(profile_elements.ID_CHKBOX_MANAGE_BOOT)
    if profile.has_property(XML_MANAGE_BOOT_MODE_ATTRIBUTE) and profile.manageBoot == "false":
        result &= ui_lib.wait_for_checkbox_and_unselect(profile_elements.ID_CHKBOX_MANAGE_BOOT)
    elif profile.has_property(XML_BOOT_MODE_ATTRIBUTE):
        boot_mode_option = profile.bootMode
        logger._log_to_console_and_log_file(" --> Selecting Boot Mode..")
        __select_value_from_a_profile_combo_box(profile_elements.ID_COMBO_PROFILE_BOOT_MODE, profile_elements.ID_COMBO_PROFILE_BOOT_MODE_LIST % boot_mode_option)
        if boot_mode_option == CONSTANT_UEFI or boot_mode_option == CONSTANT_UEFI_OPTIMIZED:
            if profile.has_property(XML_BOOT_POLICY_ATTRIBUTE):
                boot_policy_option = profile.bootPolicy
                result &= __select_value_from_a_profile_combo_box(profile_elements.ID_COMBO_PROFILE_PXE_BOOT_POLICY, profile_elements.ID_COMBO_PROFILE_PXE_BOOT_POLICY_LIST % boot_policy_option)
            result &= ui_lib.wait_for_element_visible(profile_elements.ID_CHKBOX_PROFILE_BOOT_ORDER)
            if profile.has_property(XML_MANAGE_BOOT_ORDER_ATTRIBUTE) and profile.manageBootOrder == "false":
                selenium2lib.unselect_checkbox(profile_elements.ID_CHKBOX_PROFILE_BOOT_ORDER)
            else:
                selenium2lib.select_checkbox(profile_elements.ID_CHKBOX_PROFILE_BOOT_ORDER)
                # Set primary boot device
                if profile.has_property(XML_PRIMARY_BOOT_DEVICE):
                    primary_boot_device = profile.primaryBootDevice
                    result &= __select_value_from_a_profile_combo_box(profile_elements.ID_COMBO_PROFILE_PRIMARY_BOOT_DEVICE, profile_elements.ID_COMBO_PROFILE_PRIMARY_BOOT_DEVICE_LIST % primary_boot_device)
        elif boot_mode_option == CONSTANT_LEGACY_BIOS:
            __fill_boot_order(profile, profile_elements)
    else:
        __fill_boot_order(profile, profile_elements)
    return result


def __validate_boot_settings_properties_in_xml_file(profile):
    """
        This function validates the boot setting properties and its values in XML file,
        according to the boot setting rules. If a property is not defined in XML, the default
        value will be kept in the related field.

        Example: __validate_boot_settings_properties_in_xml_file(profile)
    """
    # TODO: Create a validation for <bootorder> values
    INVALID_ATTRIBUTE_ERROR_MESSAGE = "Invalid value for %s attribute. Valid values are: %s"

    if profile.has_property(XML_MANAGE_BOOT_MODE_ATTRIBUTE):
        if profile.manageBoot not in XML_BOOLEAN_LIST:
            ui_lib.fail_test(INVALID_ATTRIBUTE_ERROR_MESSAGE % (XML_MANAGE_BOOT_MODE_ATTRIBUTE, XML_BOOLEAN_LIST), False)
        elif profile.has_property(XML_BOOT_MODE_ATTRIBUTE):
            if profile.bootMode not in PROFILE_BOOT_MODE_LIST:
                ui_lib.fail_test(INVALID_ATTRIBUTE_ERROR_MESSAGE % (XML_BOOT_MODE_ATTRIBUTE, PROFILE_BOOT_MODE_LIST), False)
            elif profile.bootMode == CONSTANT_UEFI or profile.bootMode == CONSTANT_UEFI_OPTIMIZED:
                if profile.has_property(XML_BOOT_POLICY_ATTRIBUTE):
                    if profile.bootPolicy not in PROFILE_BOOT_POLICY_LIST:
                        ui_lib.fail_test(INVALID_ATTRIBUTE_ERROR_MESSAGE % (XML_BOOT_POLICY_ATTRIBUTE, PROFILE_BOOT_POLICY_LIST), False)
                    elif profile.has_property(XML_MANAGE_BOOT_ORDER_ATTRIBUTE):
                        if profile.manageBootOrder not in XML_BOOLEAN_LIST:
                            ui_lib.fail_test(INVALID_ATTRIBUTE_ERROR_MESSAGE % (XML_MANAGE_BOOT_ORDER_ATTRIBUTE, XML_BOOLEAN_LIST), False)
                        elif profile.has_property(XML_PRIMARY_BOOT_DEVICE):
                            if profile.primaryBootDevice not in PROFILE_PRIMARY_BOOT_DEVICE_LIST:
                                ui_lib.fail_test(INVALID_ATTRIBUTE_ERROR_MESSAGE % (XML_PRIMARY_BOOT_DEVICE, PROFILE_PRIMARY_BOOT_DEVICE_LIST), False)


def __fill_boot_order(profile, profile_elements):
    """ """
    result = True
    selenium2lib = ui_lib.get_s2l()
    if profile.has_property(XML_PROFILE_ATTRIBUTE_BOOT_ORDER) and len(profile.bootorder) > 0:
        logger._log_to_console_and_log_file("Setting boot Order %s" % profile.bootorder)
        result &= ui_lib.wait_for_element_visible(profile_elements.ID_CHKBOX_PROFILE_BOOT_ORDER)
        selenium2lib.select_checkbox(profile_elements.ID_CHKBOX_PROFILE_BOOT_ORDER)
        for index, bootorder in enumerate(profile.bootorder):
            result &= ui_lib.wait_for_element_and_input_text("name=%s" % bootorder.device, index + 1)
    else:
        selenium2lib.unselect_checkbox(profile_elements.ID_CHKBOX_PROFILE_BOOT_ORDER)
    return result


def unselect_and_select_boot_order():
    """
        This function will select/unselect the boot order
    """
    # Unselect and select the "Manage boot order" option
    selenium2lib = ui_lib.get_s2l()
    status = True
    logger._log_to_console_and_log_file("")
    logger._log_to_console_and_log_file("Unselecting and selecting the 'Manage boot order' checkbox")
    ui_lib.wait_for_checkbox_and_unselect(FusionServerProfilesPage.ID_CHKBOX_MANAGE_BOOT_ORDER)
    if not ui_lib.wait_for_element_visible("name=%s" % "CD") and ui_lib.wait_for_element_visible("name=%s" % "USB") and ui_lib.wait_for_element_visible("name=%s" % "HardDisk"):
        logger._log_to_console_and_log_file("- 'Manage boot order' items were correctly hidden")
    else:
        logger._log_to_console_and_log_file("- 'Manage boot order' items are still being displayed")
        selenium2lib.capture_page_screenshot()
        status = False
    ui_lib.wait_for_checkbox_and_select(FusionServerProfilesPage.ID_CHKBOX_MANAGE_BOOT_ORDER)
    if ui_lib.wait_for_element_visible("name=%s" % "CD") and ui_lib.wait_for_element_visible("name=%s" % "USB") and ui_lib.wait_for_element_visible("name=%s" % "HardDisk"):
        logger._log_to_console_and_log_file("- 'Manage boot order' items were correctly displayed")
    else:
        logger._log_to_console_and_log_file("- 'Manage boot order' items were NOT displayed")
        selenium2lib.capture_page_screenshot()
        status = False
    return status


def fill_advanced_session(profile_obj):
    """
        This function will perform some negative tests in the "Advanced" session
    """
    result = True
    for profile in profile_obj:
        # Accessing "User-specified" form
        logger._log_to_console_and_log_file("")
        logger._log_to_console_and_log_file("### Testing the 'Advanced' session ###")
        if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_BOOT_MODE_OPTION):
            ui_lib.wait_for_checkbox_and_unselect(FusionServerProfilesPage.ID_CHKBOX_MANAGE_BOOT_MODE)
        logger._log_to_console_and_log_file("Accessing the 'User-specified'")
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_USER_SPECIFIED_SERIAL)
        if ui_lib.wait_for_element_visible((FusionServerProfilesPage.ID_INPUT_SERIAL_NUMBER) and
                                           (FusionServerProfilesPage.ID_INPUT_UUID_NUMBER)):
            logger._log_to_console_and_log_file("'User-specified' form was correctly displayed")
        else:
            logger._log_to_console_and_log_file("'User-specified' form was NOT displayed")
            logger._log_to_console_and_log_file("Unable to continue the tests in the 'Advanced' session")
            result = False

        # Insert data
        ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_SERIAL_NUMBER, profile.serialnumber)
        ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_UUID_NUMBER, profile.uuid)
    return result


def navigate_through_local_storage():
    """
    This function will navigate through Local Storage until clicks on the 'Create Logical Drive' button.
    """

    logger._log_to_console_and_log_file("\nNavigating through Local Storage initial section")

    if not ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_CHKBOX_LOCAL_STORAGE):
        ui_lib.fail_test("Local Storage section was not released")

    # Select checkbox
    if not ui_lib.wait_for_checkbox_and_select(FusionServerProfilesPage.ID_EDIT_LOCAL_STORAGE):
        ui_lib.fail_test("Fail to select a valid Manage Local Storage")

    # Select checkbox
    if not ui_lib.wait_for_checkbox_and_select(FusionServerProfilesPage.ID_CHKBOX_MANAGE_INTEGRATED_CONTROLLER):
        ui_lib.fail_test("Fail to select a valid Manage Integrated Controller")

    logger._log_to_console_and_log_file("Closing Manage Local Storage form")
    if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_MANAGE_STORAGE_CONTROLLER_CLOSE):
        ui_lib.fail_test("Fail to close Manage Storage Form")

    # Click Create Logical Drive button
    if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CREATE_LOGICAL_DRIVE):
        ui_lib.fail_test("Fail to click on Create Logical Drive button")


def negative_test_for_check_local_storage(profile_obj):
    """
        This function will perform some negative tests in the "Local Storage" session
    """
    status = True
    for profile in profile_obj:
        elements_test_list = [profile.emptyChar, profile.invalidChars]

        """
        Setting invalid values for: "Name" and "Number of physical drivers"
        """
        for element in elements_test_list:
            # Fill Logical Drive form
            if __fill_logical_drive_form(element):
                # Click Logical Drive Create button
                if ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CREATE_LOGICAL_DRIVE_FORM):
                    if element == '':
                        # Check warning messages
                        if not __check_warning_message_form(FusionServerProfilesPage.ID_WARNING_MESSAGE_NAME_FORM) and __check_warning_message_form(FusionServerProfilesPage.ID_WARNING_MESSAGE_PHYSICAL_DRIVES_FORM):
                            logger.warn("At least one of the warning messages was NOT found ")
                            status = False

                    else:
                        # Check warning messages
                        if not __check_warning_message_form(FusionServerProfilesPage.ID_WARNING_MESSAGE_PHYSICAL_DRIVES_FORM):
                            logger.warn("Warning message NOT found")
                            status = False
                else:
                    logger.warn("Logical Drive Form 'Button' returns an error. Please, check the test report for more details")
                    status = False
            else:
                logger.warn("Logical Drive Form returns an error. Please, check the test report for more details")
                status = False

    # Click 'Cancel' form button
    if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_CANCEL_LOCAL_STORAGE_FORM):
        logger.warn("Cancel button element NOT found")
        status = False

    return status


# Fill Logical Drive Form
def __fill_logical_drive_form(element):
    """ """
    result = True
    if ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_ADD_LOCAL_STORAGE_NAME, element):
        logger._log_to_console_and_log_file("Element '" + element + "' inserted for 'Name' filed")
    else:
        logger._warn("Element " + FusionServerProfilesPage.ID_ADD_LOCAL_STORAGE_NAME + " not found")
        result = False

    if ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_LISTBOX_NUMBER_PHYSICAL_DRIVES, element):
        logger._log_to_console_and_log_file("Element '" + element + "' inserted for 'ListBox' field")
    else:
        logger._warn("Element " + FusionServerProfilesPage.ID_LISTBOX_NUMBER_PHYSICAL_DRIVES + " not found")
        result = False
    return result


# Verify warning message found at Logical Drive form
def __check_warning_message_form(element):
    """ """
    result = True
    if ui_lib.wait_for_element_visible(element):
        logger._log_to_console_and_log_file("Warning message form was correctly displayed")
    else:
        logger._warn("Element " + element + " not found")
        result = False

    return result


def negative_test_for_profile_connections(profile_obj):
    """
        This function will perform some negative tests in the "Connections" session
    """
    status = True
    for profile in profile_obj:
        if profile.has_property("connection") and len(profile.connection) > 0:
            logger._log_to_console_and_log_file("\nNavigating through Connections initial section")
            # Click Add Connection button
            if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_CONNECTION):
                ui_lib.fail_test(" Fail to click on Add Connection button")
            for connection in profile.connection:
                if __select_connection_network_type(connection):
                    logger._log_to_console_and_log_file(" Select type for network connection")
                    if connection.type == "Fibre Channel":
                        if connection.has_property('boot') and (connection.boot == 'Primary' or connection.boot == 'Secondary'):
                            if __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_BOOT_ADD_CONNECTION, FusionServerProfilesPage.ID_SELECT_BOX_GENERIC_ELEMENT % (connection.boot, connection.boot)):
                                logger._log_to_console_and_log_file("   - Selecting boot: '%s'." % connection.boot)
                            else:
                                logger._log_to_console_and_log_file("   - Unable selecting boot.")
                                status = False

                            if __connections_negative_test(connection):
                                logger._log_to_console_and_log_file("   - Selecting '%s' to fill all fields empty and invalid onscreen 'Add connection'." % connection.type)
                            else:
                                logger.warn(" Warning message NOT found.")
                                status = False
                    elif connection.type == "Ethernet":
                        # Put this the parameter NetworkType.
                        if __connections_negative_test(connection):
                            logger._log_to_console_and_log_file("   - Selecting '%s' to fill all fields empty and invalid onscreen 'Add connection'." % connection.type)
                        else:
                            logger._log_to_console_and_log_file(" Warning message NOT found.")
                            status = False
                    else:
                        if connection.type != "Ethernet" and connection.type != "Fibre Channel":
                            logger._log_to_console_and_log_file(" Select type for network connection NOT found")
                            status = False
                else:
                    logger._log_to_console_and_log_file("Invalid type for network connection")
                    status = False

    # Click 'Cancel' form button
    if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_ADD_CONNECTION):
        logger.warn("Cancel button element NOT found")
        status = False
    return status


def __select_connection_network_type(connection):
    """
        This function will choose funtion type between Ethernet and Fibre Channel and search a network in the "Connections" session
    """
    # Validating if mandatory fields are in xml
    result = True
    if not connection.has_property("network") or connection.has_property("type"):
        logger._warn("Network name and  Network type are mandatory fields when adding profile connections.")
        result = False
    if connection.type.upper() == "FIBRECHANNEL":
        connection.type = "Fibre Channel"
    if connection.type.upper() in ["FIBRE CHANNEL", "ETHERNET"]:
        logger._log_to_console_and_log_file("   - Connection under test:")
        logger._log_to_console_and_log_file("   - Name: '%s'" % connection.name)
        logger._log_to_console_and_log_file("   - Network: '%s'" % connection.network)
        logger._log_to_console_and_log_file("   - Type: '%s'" % connection.type)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_CONNECTION_NAME)
        ui_lib.wait_for_element_hidden(FusionServerProfilesPage.ID_MESSAGE_CONNECTION_NETWORK)
        ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_CONNECTION_NAME, connection.name)
        result &= __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_CONNECTION_FUNCTION_TYPE, FusionServerProfilesPage.ID_SELECT_BOX_GENERIC_ELEMENT % (connection.type, connection.type))
        result &= __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_NETWORK_ADD_CONNECTION, FusionServerProfilesPage.ID_ELEMENT_NETWORK_ADD_CONNECTION % connection.network)
    else:
        logger._log_to_console_and_log_file("Invalid type for network connection %s." % connection.type)
        result = False
    return result


def __connections_negative_test(connection):
    """
        Setting invalid values for Ethernet: "Name", "Network", "Port", "Requested bandwidth", "MAC"
        and for Fibre Channel: "Name", "Network", "Port", "Requested bandwidth", "WWPN", "LUN", "WWNN", "MAC"
    """
    status = True
    # Fill Connections form
    if ui_lib.wait_for_checkbox_and_select(FusionServerProfilesPage.ID_CHKBOX_USER_SPECIFIED_IDS) and ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_CONNECTON):
        # Fill Connections form
        if __fill_negative_test_connections_form(connection, connection.invalidChars):
            # Click Add Connection button and check warning messages
            status &= __verify_warning_messages_on_connections_form(connection, connection.invalidChars)
        else:
            logger.warn("Add Connection Form returns an error. Please, check the test report for more details")
            status = False

    return status


def __fill_negative_test_connections_form(connection, invalidChars):
    """ """
    result = True
    if ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_CONNECTION_NAME, invalidChars):
        logger._log_to_console_and_log_file("Element '" + invalidChars + "' inserted for 'Name' filed")
    else:
        logger._warn("Element " + FusionServerProfilesPage.ID_INPUT_CONNECTION_NAME + " not found")
        result = False
    if ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_NETWORK_ADD_CONNECTION, invalidChars):
        logger._log_to_console_and_log_file("Element '" + invalidChars + "' inserted for 'Network' field")
    else:
        logger._warn("Element " + FusionServerProfilesPage.ID_INPUT_NETWORK_ADD_CONNECTION + " not found")
        result = False
    if ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_PORT_ADD_CONNECTION, invalidChars):
        logger._log_to_console_and_log_file("Element '" + invalidChars + "' inserted for 'Port' field")
    else:
        logger._warn("Element " + FusionServerProfilesPage.ID_INPUT_PORT_ADD_CONNECTION + " not found")
        result = False
    if ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_REQUESTED_BW_ADD_CONNECTION, invalidChars):
        logger._log_to_console_and_log_file("Element '" + invalidChars + "' inserted for 'Requested bandwidth (Gb/s)' field")
    else:
        logger._warn("Element " + FusionServerProfilesPage.ID_INPUT_REQUESTED_BW_ADD_CONNECTION + " not found")
        result = False

    mandatoryConfiguringMAC = ((connection.type == "Fibre Channel" and invalidChars != "") or (connection.type == "Ethernet"))
    if mandatoryConfiguringMAC:

        if ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_CONNECTION_MAC, invalidChars):
            logger._log_to_console_and_log_file("Element '" + invalidChars + "' inserted for 'MAC address' field")
        else:
            logger._warn("Element " + FusionServerProfilesPage.ID_INPUT_CONNECTION_MAC + " not found")
            result = False

    if connection.type == "Fibre Channel":
        if ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWPN, invalidChars):
            logger._log_to_console_and_log_file("Element '" + invalidChars + "' inserted for 'Specifify boot target - WWPN' field")
        else:
            logger._warn("Element " + FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWPN + " not found")
            result = False
        if ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWNN, invalidChars):
            logger._log_to_console_and_log_file("Element '" + invalidChars + "' inserted for 'Specifify boot target - WWNN' field")
        else:
            logger._warn("Element " + FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWNN + " not found")
            result = False
        if ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWN_TARGET, invalidChars):
            logger._log_to_console_and_log_file("Element '" + invalidChars + "' inserted for 'WWPN' field")
        else:
            logger._warn("Element " + FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWN_TARGET + " not found")
            result = False
        if ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_LUN_TARGET, invalidChars):
            logger._log_to_console_and_log_file("Element '" + invalidChars + "' inserted for 'WWNN' field")
        else:
            logger._warn("Element " + FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_LUN_TARGET + " not found")
            result = False
    return result


def __verify_warning_messages_on_connections_form(connection, invalidChars):
    """ """
    status = True
    if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_CLOSED_NETWORK_ADD_CONNECTION) and ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_CONNECTON) and __check_warning_message_form(FusionServerProfilesPage.ID_WARNING_MESSAGE_NETWORK_CONN):
        logger.warn("At least one of the warning messages was NOT found ")
        status = False
    else:
        # Check warning messages
        if not __check_warning_message_form(FusionServerProfilesPage.ID_WARNING_MESSAGE_NETWORK_CONN):
            logger.warn("Warning message NOT found")
            status = False
        # Check warning messages
    if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_CLOSED_PORT_ADD_CONNECTION) and ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_CONNECTON) and __check_warning_message_form(FusionServerProfilesPage.ID_WARNING_MESSAGE_PORT_CONN):
        logger.warn("At least one of the warning messages was NOT found ")
        status = False
    else:
        # Check warning messages
        if not __check_warning_message_form(FusionServerProfilesPage.ID_WARNING_MESSAGE_PORT_CONN):
            logger.warn("Warning message NOT found")
            status = False
    if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_CONNECTON) and __check_warning_message_form(FusionServerProfilesPage.ID_WARNING_MESSAGE_REQUESTED_CONN):
        logger.warn("At least one of the warning messages was NOT found ")
        status = False
    else:
        # Check warning messages
        if not __check_warning_message_form(FusionServerProfilesPage.ID_WARNING_MESSAGE_REQUESTED_CONN):
            logger.warn("Warning message NOT found")
            status = False

    if connection.type == "Fibre Channel" and invalidChars != "":
        if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_CONNECTON) and __check_warning_message_form(FusionServerProfilesPage.ID_WARNING_MESSAGE_MAC_CONN):
            logger.warn("At least one of the warning messages was NOT found ")
            status = False
        else:
            # Check warning messages
            if not __check_warning_message_form(FusionServerProfilesPage.ID_WARNING_MESSAGE_MAC_CONN):
                logger.warn("Warning message NOT found")
                status = False

    if connection.type == "Fibre Channel":
        if not __check_warning_message_form(FusionServerProfilesPage.ID_WARNING_MESSAGE_ID_WWPN_CONN):
            logger.warn("At least one of the warning messages was NOT found ")
            status = False
        else:
            # Check warning messages
            if not __check_warning_message_form(FusionServerProfilesPage.ID_WARNING_MESSAGE_ID_WWPN_CONN):
                logger.warn("Warning message NOT found")
                status = False
        if not __check_warning_message_form(FusionServerProfilesPage.ID_WARNING_MESSAGE_ID_WWNN_CONN):
            logger.warn("At least one of the warning messages was NOT found ")
            status = False
        else:
            # Check warning messages
            if not __check_warning_message_form(FusionServerProfilesPage.ID_WARNING_MESSAGE_ID_WWNN_CONN):
                logger.warn("Warning message NOT found")
                status = False
    return status


def negative_test_for_SAN(profile_obj):
    """
        This test consists in three parts:
        1. Verify warning message when trying to use a non-existing volume
        2. Verify that there's a warning message for all parameters of a New Volume
        3. Verify that there's an error message if we try to edit the storage path and select no ports for it
    """
    test_result = True

    # First we'll add connection to the profile, so we can associate Storage modules to it
    createprofile_elements = ProfileContainer(ProfileContainerType.ADD)

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    logger._log_to_console_and_log_file("Creating connections for SAN negative tests")
    for profile in profile_obj:
        if not __add_profile_connections(profile, createprofile_elements):
            ui_lib.fail_test("Error adding connections to profile", True)

    # Selecting Manage SAN Storage
    logger._log_to_console_and_log_file("Selecting Manage SAN Storage")
    if not __select_san_storage(createprofile_elements, True):
        ui_lib.fail_test("Error Selecting Manage SAN Storage", True)

    # Clicking Button Add Volume
    logger._log_to_console_and_log_file("Accessing Add Volume Frame")
    if not ui_lib.wait_for_element_and_click(createprofile_elements.ID_ADD_STORAGE):
        ui_lib.fail_test("Error clicking on add volume", True)

    # TC01: Verify error message when trying to add a non-existing volume
    if not __negative_test_SAN_non_existing_volume(profile.stringEmpty):
        logger._warn("Negative test SAN empty existing volume Failed")
        test_result = False

    if not __negative_test_SAN_non_existing_volume(profile.stringInvalid):
        logger._warn("Negative test SAN non existing volume Failed")
        test_result = False

    # TC02: Verify error messages when adding new volume
    if not __negative_test_SAN_new_volume(profile):
        logger._warn("negative_test_SAN_new_volume Failed")
        test_result = False

    # TC03: Verify error messages in storage path
    if not __negative_test_SAN_storage_path(profile):
        logger._warn("negative_test_SAN_storage_path Failed")
        test_result = False

    # Cancel 'Add Volumes'
    logger._log_to_console_and_log_file("Cancel 'Add Volumes'")
    if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_CANCEL_BTN):
        logger._warn("Failed to click on Cancel Add Volumes")
        test_result = False

    # Uncheck Manage SAN Storage
    logger._log_to_console_and_log_file("Unselecting Manage SAN Storage")
    if not __select_san_storage(createprofile_elements, False):
        ui_lib.fail_test("Error Unselecting Manage SAN Storage", True)

    # Return result
    return test_result


def __add_profile_connections(profile, profile_elements):
    """ Add Profile Connections    """

    selenium2lib = ui_lib.get_s2l()
    result = True

    if profile.has_property("connection") and len(profile.connection) > 0:
        ui_lib.wait_for_element_and_click(profile_elements.ID_COMBO_MENU_VIEW)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_CONNECTIONS)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_CONNECTION)

        for connection in profile.connection:
            logger._log_to_console_and_log_file("# Adding profile connection %s of %s." % (str(profile.connection.index(connection) + 1), str(len(profile.connection))))
            # Validating if mandatory fields are in xml
            if not connection.has_property("network") or connection.has_property("type"):
                logger._warn("Network name and  Network type are mandatory fields when adding profile connections.")
                result = False

            if connection.type.upper() == "FIBRECHANNEL":
                connection.type = "Fibre Channel"
            if connection.type.upper() in ["FIBRE CHANNEL", "ETHERNET"]:
                logger._log_to_console_and_log_file("   - Selecting Function type.")
                __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_CONNECTION_FUNCTION_TYPE, FusionServerProfilesPage.ID_SELECT_BOX_GENERIC_ELEMENT % (connection.type, connection.type))
                ui_lib.wait_for_element_hidden(FusionServerProfilesPage.ID_MESSAGE_CONNECTION_NETWORK)
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_CONNECTION_NAME)
                logger._log_to_console_and_log_file("   - Selecting network.")
                __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_NETWORK_ADD_CONNECTION, FusionServerProfilesPage.ID_ELEMENT_NETWORK_ADD_CONNECTION % connection.network)
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_CONNECTION_NAME)
            else:
                logger._log_to_console_and_log_file("Invalid type for network connection %s." % connection.type)
            if connection.has_property("name") and len(connection.name) > 0:
                logger._log_to_console_and_log_file("   - Adding connection name.")
                ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_CONNECTION_NAME, connection.name)

            if connection.has_property('band'):
                if not __validate_requested_bandwidth(connection.band):
                    result = False
                    break

            browser = BuiltIn().get_variable_value("${Browser}")

            if browser == "chrome":
                logger._log_to_console_and_log_file("Chrome not handling FlexNIC or boot order skipping....")
            else:
                if connection.has_property('portName'):
                    logger._log_to_console_and_log_file("   - Selecting port.")
                    __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_FLEXNIC_ADD_CONNECTION, FusionServerProfilesPage.XP_CREATE_SP_ADD_CONN_NIC_DD_SELECT % connection.portName)

                if connection.has_property('boot') and (connection.boot == 'Primary' or connection.boot == 'Secondary'):
                    logger._log_to_console_and_log_file("   - Selecting boot.")
                    __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_BOOT_ADD_CONNECTION, FusionServerProfilesPage.ID_SELECT_BOX_GENERIC_ELEMENT % (connection.boot, connection.boot))

                    if connection.type.upper() == "FIBRE CHANNEL" or connection.type.upper() == "FIBRECHANNEL":
                        if connection.has_property('targetwwpn') and connection.has_property('targetlun') and connection.targetwwpn != "" and connection.targetlun != "":
                            logger._log_to_console_and_log_file("   - Specifying boot target.")
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_SPECIFIY_BOOT_TARGET)
                            logger._log_to_console_and_log_file("   - Typing target WWPN.")
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWN_TARGET)
                            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWN_TARGET, connection.targetwwpn)
                            logger._log_to_console_and_log_file("   - Typing target LUN.")
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_LUN_TARGET)
                            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_LUN_TARGET, connection.targetlun)
                        else:
                            logger._log_to_console_and_log_file("   - Not bootable connection.")
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_USE_BIOS)

                        if connection.has_property('wwpn') and connection.has_property('wwnn') and connection.wwpn != "" and connection.wwnn != "":
                            logger._log_to_console_and_log_file("   - Selecting use user specified IDs checkbox.")
                            selenium2lib.select_checkbox(FusionServerProfilesPage.ID_CHKBOX_USER_SPECIFIED_IDS)
                            logger._log_to_console_and_log_file("   - Typing WWPN.")
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWPN)
                            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWPN, connection.wwpn)
                            logger._log_to_console_and_log_file("   - Typing WWNN.")
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWNN)
                            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWNN, connection.wwnn)
                            if connection.has_property('macaddress') and connection.macaddress != "":
                                logger._log_to_console_and_log_file("   - Typing MAC address.")
                                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_CONNECTION_MAC)
                                ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_CONNECTION_MAC, connection.macaddress)
                    elif connection.type.upper() == "ETHERNET":
                        if connection.has_property('macaddress') and connection.macaddress != "":
                            logger._log_to_console_and_log_file("   - Selecting use user specified IDs checkbox.")
                            selenium2lib.select_checkbox(FusionServerProfilesPage.ID_CHKBOX_USER_SPECIFIED_IDS)
                            logger._log_to_console_and_log_file("   - Typing MAC address.")
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_CONNECTION_MAC)
                            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_CONNECTION_MAC, connection.macaddress)

            if result is True:
                if profile.connection.index(connection) < (len(profile.connection) - 1):
                    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_PLUS_CONNECTON)
                    logger._log_to_console_and_log_file("   - Clicking on connection Add+ button.")
                else:
                    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_CONNECTON)
                    logger._log_to_console_and_log_file("   - Clicking on connection Add button.")
            else:
                break
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_ADD_CONNECTION)
                logger._warn("Failed to add connection %s to the profile" % connection.network)

        # For now, validating the connection with name only
        logger._log_to_console_and_log_file("   - Verifying if connections are correctly displayed (just the connections with name are being verified.")
        for connection in profile.connection:
            if connection.has_property("name"):
                if ui_lib.is_visible(FusionServerProfilesPage.ID_PROFILE_CONNECTION_ELEMENT_BY_NAME % connection.name):
                    logger._log_to_console_and_log_file("    - Connection named '%s' was correctly created" % connection.name)
                else:
                    logger._warn("Connection not found in connections table: %s" % connection.name)
                    result = False

    return result


def __select_san_storage(profile_elements, select):
    """ """
    logger._log_to_console_and_log_file("Accessing SAN Storage")
    ui_lib.wait_for_element_and_click(profile_elements.ID_COMBO_MENU_VIEW)
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_SANSTORAGE)
    if select:
        if not ui_lib.wait_for_element_visible(profile_elements.ID_ADD_STORAGE, 1):
            logger._log_to_console_and_log_file("Selecting SAN Storage")
            if not ui_lib.wait_for_checkbox_and_select(profile_elements.ID_CHKBOX_SAN, 1):
                logger._warn("Unable to check the 'Manage SAN Storage' checkbox")
                return False
    else:
        if ui_lib.wait_for_element_visible(profile_elements.ID_ADD_STORAGE, 1):
            logger._log_to_console_and_log_file("Unselecting SAN Storage")
            if not ui_lib.wait_for_checkbox_and_unselect(profile_elements.ID_CHKBOX_SAN, 1):
                logger._warn("Unable to uncheck the 'Manage SAN Storage' checkbox")
                return False
    return True


def __negative_test_SAN_non_existing_volume(string_invalid):
    """
        SAN Negative Test 1
        Verify warning message when trying to use a non-existing volume
    """
    test_result = True
    logger._log_to_console_and_log_file("TC01: Verify error message when trying to add a non-existing volume as an existing volume\n")

    logger._log_to_console_and_log_file(" - Trying to select non-existing volume %s" % string_invalid)
    test_result &= ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_EXISTING_VOLUME_NAME, string_invalid)

    # Click on Add Storage so the errors will pop out
    __click_on_form_for_add_volume()

    logger._log_to_console_and_log_file(" - Verifying error message")
    if ui_lib.wait_for_element_visible(FusionServerProfilesPage.FOR_WARNING_MESSAGE_EXISTING_VOLUME_MUST_BE_SELECTED):
        logger._log_to_console_and_log_file(" - Warning message for using non-existing volume was correctly presented.")
    else:
        logger._warn("Error! Test will fail because the warning message for using non-existing volume was not found.")
        test_result = False

    logger._log_to_console_and_log_file("TC01: Completed\n")
    return test_result


def __negative_test_SAN_new_volume(profile):
    """
        SAN Negative Test 2
        Verify that there's a warning message for all parameters of a New Volume
    """
    test_result = True
    logger._log_to_console_and_log_file("TC02: Verify error messages when adding new volume\n")

    logger._log_to_console_and_log_file(" - Selecting New Volume")
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_VOLUME_TYPE)
    if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.GET_TEXT_FROM_SPAN % VolumeTypes.NEW_VOLUME):
        ui_lib.fail_test(" - Error clicking on New Volume", True)
    logger._log_to_console_and_log_file("Selecting Manual LUN")
    if not ui_lib.wait_for_checkbox_and_select(FusionServerProfilesPage.ID_LUN_MANUAL):
        ui_lib.fail_test(" - Error selecting Manual LUN configuration", True)

    # This is a list of elements being tested:
    neg_elems = [[FusionServerProfilesPage.ID_NEW_VOLUME_NAME, FusionServerProfilesPage.FOR_WARNING_MESSAGE_NEW_VOLUME_NAME_NEEDED, profile.stringEmpty, "Volume name is required"],
                 [FusionServerProfilesPage.ID_LUN_VALUE, FusionServerProfilesPage.FOR_WARNING_MESSAGE_NEW_VOLUME_LUN_VALUE_OUT_OF_BOUNDS, profile.lunLowerBound, "LUN more or equal to 0"],
                 [FusionServerProfilesPage.ID_LUN_VALUE, FusionServerProfilesPage.FOR_WARNING_MESSAGE_NEW_VOLUME_LUN_VALUE_OUT_OF_BOUNDS, profile.lunHigherBound, "LUN less or equal to 16383"],
                 [FusionServerProfilesPage.ID_STORAGE_POOL_FIELD, FusionServerProfilesPage.FOR_WARNING_MESSAGE_NEW_VOLUME_STORAGE_POOL_NEEDED, profile.stringEmpty, "Storage pool is required"],
                 [FusionServerProfilesPage.ID_STORAGE_POOL_FIELD, FusionServerProfilesPage.FOR_WARNING_MESSAGE_NEW_VOLUME_STORAGE_POOL_NEEDED, profile.stringInvalid, "Storage pool cannot be invalid"],
                 [FusionServerProfilesPage.ID_CAPACITY_BOX, FusionServerProfilesPage.FOR_WARNING_MESSAGE_NEW_VOLUME_CAPACITY_OUT_OF_BOUNDS, profile.capacityLowerBound, "Capacity greater than or equal to 1."],
                 [FusionServerProfilesPage.ID_CAPACITY_BOX, FusionServerProfilesPage.FOR_WARNING_MESSAGE_NEW_VOLUME_CAPACITY_OUT_OF_BOUNDS, profile.capacityHigherBound, "The maximum capacity is 16 TiB."]]

    for neg_element in neg_elems:
        element = neg_element[0]
        error_message_id = neg_element[1]
        invalid_string = neg_element[2]
        error_message_string = neg_element[3]

        logger._log_to_console_and_log_file(" - Writing invalid string \'%s\' into element \'%s\'" % (invalid_string, element))
        if not ui_lib.wait_for_element_and_input_text(element, invalid_string):
            logger._warn("Error! Test will fail because it couldn't write in element")
            test_result = False

        # Click on Add Storage so the errors will pop out
        __click_on_form_for_add_volume()

        logger._log_to_console_and_log_file(" - Verifying error message")
        if ui_lib.wait_for_element_visible(error_message_id):
            logger._log_to_console_and_log_file(" - Warning message \'%s\' was correctly presented." % error_message_string)
        else:
            logger._warn("Error! Test will fail because the warning \'%s\' was not found." % error_message_string)
            test_result = False

    logger._log_to_console_and_log_file("TC02: Completed\n")
    return test_result


def __negative_test_SAN_storage_path(profile):
    """
        SAN Negative Test 3
        Verify that there's an error message if we try to edit the storage path and select no ports for it
    """
    test_result = True
    logger._log_to_console_and_log_file("TC03: Verify error messages in Storage Path\n")

    # Select a storage pool
    test_result &= __fill_sanstorage_volume_properties(profile.sanstorage)
    test_result &= __fill_storage_path(profile.sanstorage)

    # Edit storage Path
    logger._log_to_console_and_log_file(" - Editing Storage Path")
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_EDIT_PATH % profile.sanstorage.connection[0].name)

    logger._log_to_console_and_log_file("   - Setting storage target port for: " + profile.sanstorage.connection[0].name)
    if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_TARGET_MANUAL):
        ui_lib.fail_test(" - Error Selecting Manual Ports", True)

    logger._log_to_console_and_log_file("   - Clicking OK to edit Storage Target")
    test_result &= ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_TARGET_OK)

    # Verify error message 'Select at least one storage target'
    logger._log_to_console_and_log_file(" - Verifying error message")
    if ui_lib.wait_for_element_visible(FusionServerProfilesPage.PATH_ERROR_MESSAGE_NEW_VOLUME_NO_STORAGE_TARGETS):
        logger._log_to_console_and_log_file(" - Warning message \'%s\' was correctly presented." % "Storage Target")
    else:
        logger._warn("Error! Test will fail because the warning \'%s\' was not found." % "Storage Target")
        test_result = False

    # Cancel 'Edit Storage Targets"
    logger._log_to_console_and_log_file("Cancel 'Add Volumes'")
    test_result &= ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_TARGET_CANCEL)

    logger._log_to_console_and_log_file("TC03: Completed\n")
    return test_result


def __validate_requested_bandwidth(requested_bandwidth):
    """ Verifies the profile connection bandwidth  value """

    selenium2lib = ui_lib.get_s2l()

    logger._log_to_console_and_log_file("   - Selecting requested bandwidth.")
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_REQUESTED_BW_ADD_CONNECTION)
    selenium2lib.input_text(FusionServerProfilesPage.ID_INPUT_REQUESTED_BW_ADD_CONNECTION, requested_bandwidth)
    selenium2lib.press_key(FusionServerProfilesPage.ID_INPUT_REQUESTED_BW_ADD_CONNECTION, chr(9))

    if not ui_lib.wait_for_element_hidden(FusionServerProfilesPage.ID_CONNECTION_ERROR):
        logger._warn(selenium2lib.get_text(FusionServerProfilesPage.ID_CONNECTION_ERROR) + " " + selenium2lib.get_text(FusionServerProfilesPage.ID_CONNECTION_BANDWIDTH_HELP))
        return False
    return True


def __click_on_form_for_add_volume():
    """ """
    logger._log_to_console_and_log_file("Clicking Add Volume")
    if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_STORAGE_ADD):
        ui_lib.fail_test("Failed to click on add volume", True)


def __fill_sanstorage_volume_properties(sanstorage):
    """ """
    result = True
    result &= ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_STORAGE_POOL_DROPDOWN)
    if ui_lib.wait_for_element_and_click(FusionServerProfilesPage.GET_TEXT_FROM_SPAN % sanstorage.storagepool):
        logger._log_to_console_and_log_file("   - Select Storage Pool: " + str(sanstorage.storagepool))
    else:
        logger._warn("Please provide valid Storage Pool")
        return False
    # TODO: Validate the SIZE of capacity informed thru XML before input it
    result &= ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_CAPACITY_BOX, sanstorage.capacity)
    result &= ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_PROVISIONING_DROPDOWN)
    result &= ui_lib.wait_for_element_and_click(FusionServerProfilesPage.GET_TEXT_FROM_SPAN % sanstorage.provisioning)
    if sanstorage.has_property("permanent") and sanstorage.permanent.lower() == "true":
        ui_lib.wait_for_checkbox_and_unselect(FusionServerProfilesPage.ID_CHK_PERMANENT)
    return result


def __fill_storage_path(sanstorage):
    """ """
    status = True
    if sanstorage.has_property("connection"):
        for connection in sanstorage.connection:
            if not ui_lib.wait_for_element_text(FusionServerProfilesPage.ID_STORAGE_PATH_GRID, connection.name, 10):
                logger._log_to_console_and_log_file("   - Adding storage path")
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ADD_STORAGE_PATH)
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.GET_TEXT_FROM_TD % connection.name)
                if ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ADD_PATH, 20):
                    if not ui_lib.wait_for_element_text(FusionServerProfilesPage.ID_STORAGE_PATH_GRID, connection.name):
                        logger._warn("Unable to add an storage path")
                        status = False
                else:
                    logger._warn("Unable to acess the storage path dialog")
            status &= __edit_storage_target(connection)
    return status


def __edit_storage_target(connection):
    """ """
    status = True
    if connection.has_property("port"):
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_EDIT_PATH % connection.name)
        logger._log_to_console_and_log_file("   - Setting storage target port for: " + connection.name)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_TARGET_MANUAL)
        for port in connection.port:
            if ui_lib.wait_for_element_text(FusionServerProfilesPage.ID_PORT_TABLE, port.target):
                ui_lib.wait_for_checkbox_and_select(FusionServerProfilesPage.ID_TARGET_PORT % port.target)
            else:
                logger._warn("The specified port '" + str(connection.port) + "' does not exist")
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_PORT_CANCEL_BTN)
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_CANCEL_BTN)
                status = False
        status &= ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_TARGET_OK)
    return status


def access_advanced_settings():
    """ """
    success = True
    success &= ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_CHKBOX_MANAGE_BOOT_MODE, timeout=10)
    success &= ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_USER_SPECIFIED_SERIAL)
    if not success:
        ui_lib.fail_test("Error while accessing profile manager advanced settings", captureScreenshot=True)


def click_create_new_profile_button():
    """ """
    if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_CREATE_SERVER_PROFILES):
        ui_lib.fail_test("Error clicking at the create new profile button", captureScreenshot=True)


def form_click_create_profile_button():
    """ """
    if not ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CREATE_SERVER_PROFILE):
        ui_lib.fail_test("Error clicking at the create new profile button", captureScreenshot=True)


def fill_general_info(profile):
    """
        This function will fill the information of "General" session
        Returns true if general session was correctly filled, false if any inconsistencies/errors were found.
    """
    selenium2lib = ui_lib.get_s2l()
    logger._log_to_console_and_log_file("\nFilling the General form for profile: %s..." % profile.name)
    ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_INPUT_SERVER_PROFILE_NAME)
    logger._log_to_console_and_log_file("Typing profile name..")
    ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_SERVER_PROFILE_NAME, profile.name)
    if profile.has_property("profile"):
        logger._log_to_console_and_log_file("Typing profile description..")
        ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_INPUT_SERVER_PROFILE_DESCRIPTION)
        ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_SERVER_PROFILE_DESCRIPTION, profile.profile)
    else:
        logger._log_to_console_and_log_file("Please, provide a Profile")
        return False

    # Select hardware
    logger._log_to_console_and_log_file("Selecting Hardware..")
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_SERVER_HARDWARE_DROPDOWN)
    logger._log_to_console_and_log_file("Creating profile for %s" % profile.server)
    if ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % profile.server):
        logger._log_to_console_and_log_file("Selected valid server hardware")

        if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_PROFILE_POWER_OFF_LINK):
            # This function will power off the server hardware without navigate to Server Hardware page.
            if not __power_off_server_hardware():
                logger._warn("Unable to verify or power off the selected server hardware")
    else:
        logger._log_to_console_and_log_file("Please pass valid server hardware")
        return False

    # Check for server hardware
    if profile.server == "unassigned":
        # Select Server Hardware Type and Enclosure Group
        if not hasattr(profile, "hardwaretype") or profile.hardwaretype == "" or profile.enclgroup == "":
            logger._warn("Mandatory fields (hardwaretype, enclgroup) for unassigned profiles can't be empty")
            logger._log_to_console_and_log_file("Select server profile Cancel button")
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_SERVER_PROFILE)
            return False
        else:
            # Select hardware type and enclosure group for unassigned profiles
            logger._log_to_console_and_log_file("No server hardware for unassigned profile")
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_SERVER_HARDWARE_TYPE_DROPDOWN)
            if ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % profile.hardwaretype):
                logger._log_to_console_and_log_file("Selected valid hardware type")
            else:
                logger._warn("Please provide valid hardware")
                return False
            if profile.server == "unassigned":
                logger._log_to_console_and_log_file("Selecting enclosure group for unassigned profile")
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_ENCLOSURE_GROUP_DROPDOWN)
                if ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % profile.enclgroup):
                    logger._log_to_console_and_log_file("Selected valid Enclosure Group")
                else:
                    logger._warn("Invalid Enclosure Group")
                    return False
    else:
        # Verify Server Hardware Type
        if hasattr(profile, 'hardwaretype') and profile.hardwaretype:
            logger._log_to_console_and_log_file("Verify server hardware type: %s" % profile.hardwaretype)
            if not ui_lib.wait_for_element_text("//label[@id='cic-profile-add-server-type']", profile.hardwaretype):
                logger._warn("Failed to verify Server Hardware Type.")
                return False
        else:
            logger._log_to_console_and_log_file("No hardware type, not verifying")

        if "DL" not in profile.hardwaretype:
            # Verify Enclosure Group
            logger._log_to_console_and_log_file("Verify enclosure group: %s" % profile.enclgroup)
            if not ui_lib.wait_for_element_text("//label[@id='cic-profile-add-enclosure-group']", profile.enclgroup):
                logger._warn("Failed to verify Enclosure Group.")
                return False

    if "DL" not in profile.hardwaretype:
        # Selecting the Affinity
        if profile.has_property("affinity") and profile.affinity != "":
            logger._log_to_console_and_log_file("Selecting affinity..")
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_AFFINITY_DROP_DOWN)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_AFFINITY_DROP_DOWN_SELECT % profile.affinity)
            selectedAF = selenium2lib.get_text(FusionServerProfilesPage.ID_AFFINITY_DROP_DOWN)
            logger._log_to_console_and_log_file("Selected affinity is %s " % selectedAF)
            if not selectedAF == profile.affinity:
                logger._warn("Failed to select affinity..")
                return False
    return True


def __power_off_server_hardware():
    '''
    Switches off the server hardware when inside Server Profiles page.
    '''
    status = True

    logger._log_to_console_and_log_file("Server is not powered off, switching off now")
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_PROFILE_POWER_OFF_LINK)
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_POWER_PRESS_AND_HOLD)
    status &= ui_lib.wait_for_element_hidden(FusionServerProfilesPage.ID_PROFILE_POWER_OFF_LINK, PerfConstants.SERVER_POWER_OFF)
    status &= (ui_lib.wait_for_element(FusionServerProfilesPage.ID_MSG_VALIDATING_POWER_OFF) or ui_lib.wait_for_element(FusionServerProfilesPage.ID_MSG_VALIDATING_EDIT_POWER_OFF))
    status &= (ui_lib.wait_for_element_hidden(FusionServerProfilesPage.ID_MSG_VALIDATING_POWER_OFF, PerfConstants.SERVER_POWER_OFF) or ui_lib.wait_for_element_hidden(FusionServerProfilesPage.ID_MSG_VALIDATING_EDIT_POWER_OFF, PerfConstants.SERVER_POWER_OFF))
    if status:
        logger._log_to_console_and_log_file("Server was powered off successfully")

    return status


def pmsan_pretest(self, sanvolumes_obj, host, user, password):
    """ """
    # Login
    credentials = {'userName': user, 'password': password}
    self.loginsession = LoginSession(self.fusion_client)
    self.loginsession.login(host, credentials)
    status = True
    for volume in sanvolumes_obj:
        # Get storage pool URI
        self.pool = StoragePool(self.fusion_client)
        storagepool = self.pool.get()
        for item in storagepool['members']:
            if item['name'] == str(volume.storagepool):
                StoragePoolURI = item['uri']
                break

        # Create
        volume_json = json.loads('{"name": "' + str(volume.name) + '","provisioningParameters":{"storagePoolUri": "' + str(StoragePoolURI) + '","requestedCapacity": "10737418240","provisionType": "Full","shareable": true}}')
        self.volume = StorageVolume(self.fusion_client)
        http_response = self.volume.create(volume_json, 200)
        if str(http_response['status_code']) == '202':
            logger._log_to_console_and_log_file("SAN Volume '" + str(volume.name) + "' created")
        else:
            logger._log_to_console_and_log_file("Unable to create SAN Volume '" + str(volume.name) + "'")
            status = False
    return status


def update_profile_from_template(profile):
    """ update profile from profile template """
    selenium2lib = ui_lib.get_s2l()
    if not select_server_profile(profile):
        ui_lib.fail_test("Failed to select profile %s" % profile)

    logger._log_to_console_and_log_file("power off server before updating profile from template")
    profile_attributes = get_server_profile_attributes(profile, None)
    if profile_attributes["server hardware"] == "unassigned":
        selenium2lib.capture_page_screenshot()
        logger._warn("Cannot power off Server Profile '%s' due to unassigned server hardware" % profile)
    elif profile_attributes["server power"].lower() == "on":
        ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_MENU_MAIN_ACTION)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_MAIN_ACTION)
        if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_MENU_ACTION_POWEROFF):
            logger._log_to_console_and_log_file("Powering off selected server profiles")
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_ACTION_POWEROFF)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_POWEROFF_PRESS_HOLD)
            ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_PROFILE_POWER_STATUS % "Off", PerfConstants.PROFILE_POWER_VALIDATION)
            logger._log_to_console_and_log_file("Successfully powered off Server Profiles")
        else:
            selenium2lib.capture_page_screenshot()
            ui_lib.fail_test("Power off option is not available in the Actions menu")

    # Select update from template option from Action menu
    ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_MENU_MAIN_ACTION)
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_MAIN_ACTION)
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_ACTION_UPDATE_FROM_TEMPLATE)
    if not ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_MSG_TO_POWER_OFF_SERVER):
        ui_lib.wait_for_element(FusionServerProfilesPage.ID_BUTTON_PROFILE_UPDATE_CONFIRM)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BUTTON_PROFILE_UPDATE_CONFIRM)
    else:
        ui_lib.fail_test("Server should be powered off to update profile")
    logger.debug("waiting for progress bar indicates to 'ok'")
    if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_STATUS_NOTIFICATION_OK, 300):
        logger._log_to_console_and_log_file("Server profile '%s' updated successfully from template" % profile)
        return True
    else:
        ui_lib.fail_test("Failed to update server profile '%s' from template" % profile)


def verify_can_not_edit_server_profile_with_error_configuration(profile_obj):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    total = len(profile_obj)
    failed = 0
    not_exists = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("Editing a server profile with name '%s' ..." % profile.name)
        # checking if the profile is already existing
        if not VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' does not exists" % profile.name)
            not_exists += 1
            continue

        auto_power_off = False if getattr(profile, 'auto_power_off', '').lower() == 'false' else True
        # open Edit SP dialog and enter data ...
        CommonOperationServerProfile.click_server_profile(profile.name)

        EditServerProfile.select_action_edit()
        EditServerProfile.wait_edit_server_profile_dialog_shown()
        BuiltIn().sleep(2)
        EditServerProfile.input_name(profile.newName) if getattr(profile, 'newName', None) is not None else None
        EditServerProfile.input_description(profile.desc) if getattr(profile, 'desc', None) is not None else None

        if not EditServerProfile.input_select_server_hardware(profile.server, auto_power_off=auto_power_off):
            logger.warn("server hardware '%s' is not selected for editing server profile, may be wrong name, or powered on but failed to power it off. "
                        "test will skip this profile '%s' and continue to edit other server profiles" % (profile.server, profile.name))
            continue
        msg = EditServerProfile.get_error_message_from_server_hardware()
        if msg is not None:
            logger.warn("error occurred, server profile can not be edited successfully: \n<%s>" % msg)
            ui_lib.fail_test(msg)

        sht_selected = EditServerProfile.get_selected_server_hardware_type(profile.server)
        if profile.hardwareType not in sht_selected:
            logger.warn("server hardware type '%s' of server '%s' is NOT consistent with test data '%s'" % (sht_selected, profile.server, profile.hardwareType))
            EditServerProfile.ChangeServerHardwareTypeAndEnclosureGroup.change_server_hardware_type(profile.hardwareType, timeout=5, fail_if_false=False)

        eg_selected = EditServerProfile.get_selected_enclosure_group(profile.server)
        if profile.enclgroup not in eg_selected:
            logger.warn("enclosure group '%s' of server '%s' is NOT consistent with test data '%s'" % (eg_selected, profile.server, profile.enclgroup))
            EditServerProfile.ChangeServerHardwareTypeAndEnclosureGroup.change_enclosure_group(profile.enclgroup, timeout=5, fail_if_false=False)

        if getattr(profile, 'Firmware', None) is not None:
            logger.info("test data for 'Firmware' is found: <%s>, start setting Firmware Baseline ..." % profile.Firmware)
            logger.debug("test data for 'Firmware' is found: <%s>" % profile.Firmware, also_console=False)
            # set Firmware Baseline and force-installation option
            CommonOperationServerProfile.Firmware.set(profile.Firmware)

        # Add multiple networks one a physical port
        if getattr(profile, 'Connections', None) is not None:
            logger.debug("test data for 'Connections' is found: <%s>" % profile.Connections, also_console=False)
            logger.info("test data for 'Connections' is found, start adding connections ...")
            # add connections
            CommonOperationServerProfile.Connection().set(profile.Connections)

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
            CreateServerProfile.Advanced.set(profile)

        EditServerProfile.click_ok_button()
        if CommonOperationServerProfile.BootSettings.get_error_message_from_boot_mode() is not None:
            logger.warn("test data may be wrongly defined for 'Boot mode', which caused an error that blocks profile being created. "
                        "test will skip this profile '%s' and continue to create other server profiles" % profile.name)
            continue

        if not EditServerProfile.wait_edit_server_profile_dialog_disappear(10, False):
            # get error message and compile with expectant value
            actual_error = EditServerProfile.get_error_message_if_save_edit_failed(timeout=10, fail_if_false=False)
            if not hasattr(profile, 'expect_error'):
                logger.warn("No 'expect_value' was set in test data")
                continue
            expect_error = profile.expect_error
            if expect_error in actual_error:
                logger.warn("Can not edit server profile when using error configuration")
                failed += 1
            EditServerProfile.click_cancel_button()
        else:
            logger.warn("The server profile should not be edited when using error configuration")

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if not_exists > 0:
        logger.warn("There are %s server profile(s) are not existing, please remove them before test" % not_exists)
        return False
    else:
        if total - failed == 0:
            logger.warn("All of %s server profiles are not successfully edited using error configuration" % total)
            return True
        else:
            logger.warn("%s server profile(s) is edited or error message is not match with expectant, test is considered FAIlED " % (total - failed))
            return False


def verify_can_not_edit_server_profile_special_info_when_server_power_on(profile_obj):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    total = len(profile_obj)
    failed = 0
    not_exists = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("Editing a server profile with name '%s' ..." % profile.name)
        # checking if the profile is already existing
        if not VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' does not exists" % profile.name)
            not_exists += 1
            continue

        CommonOperationServerProfile.click_server_profile(profile.name)
        EditServerProfile.select_action_edit()
        EditServerProfile.wait_edit_server_profile_dialog_shown()
        BuiltIn().sleep(2)
        EditServerProfile.input_name(profile.newName) if getattr(profile, 'newName', None) is not None else None
        EditServerProfile.input_description(profile.desc) if getattr(profile, 'desc', None) is not None else None

        # Server hardware must be "power" on status
        if not VerifyServerProfile.is_power_on_error_visible_when_edit_server_profile(profile.server, 10):
            logger.warn("Server hardware '%s' is not 'Powered on, please power on it" % profile.server)
            continue

        sht_selected = EditServerProfile.get_selected_server_hardware_type(profile.server)
        if profile.hardwareType not in sht_selected:
            logger.warn("server hardware type '%s' of server '%s' is NOT consistent with test data '%s'" % (sht_selected, profile.server, profile.hardwareType))
            EditServerProfile.ChangeServerHardwareTypeAndEnclosureGroup.change_server_hardware_type(profile.hardwareType, timeout=5, fail_if_false=False)

        eg_selected = EditServerProfile.get_selected_enclosure_group(profile.server)
        if profile.enclgroup not in eg_selected:
            logger.warn("enclosure group '%s' of server '%s' is NOT consistent with test data '%s'" % (eg_selected, profile.server, profile.enclgroup))
            EditServerProfile.ChangeServerHardwareTypeAndEnclosureGroup.change_enclosure_group(profile.enclgroup, timeout=5, fail_if_false=False)

        if getattr(profile, 'Firmware', None) is not None:
            logger.info("test data for 'Firmware' is found: <%s>, start setting Firmware Baseline ..." % profile.Firmware)
            logger.debug("test data for 'Firmware' is found: <%s>" % profile.Firmware, also_console=False)
            # set Firmware Baseline and force-installation option
            CommonOperationServerProfile.Firmware.set(profile.Firmware)

        # Add multiple networks one a physical port
        if getattr(profile, 'Connections', None) is not None:
            logger.debug("test data for 'Connections' is found: <%s>" % profile.Connections, also_console=False)
            logger.info("test data for 'Connections' is found, start adding connections ...")
            # add connections
            CommonOperationServerProfile.Connection().set(profile.Connections)

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
            CreateServerProfile.Advanced.set(profile)

        EditServerProfile.click_ok_button()
        if CommonOperationServerProfile.BootSettings.get_error_message_from_boot_mode() is not None:
            logger.warn("test data may be wrongly defined for 'Boot mode', which caused an error that blocks profile being created. "
                        "test will skip this profile '%s' and continue to create other server profiles" % profile.name)
            continue

        if not EditServerProfile.wait_edit_server_profile_dialog_disappear(10, False):
            # get error message and compile with expectant value
            actual_error = EditServerProfile.get_error_message_if_save_edit_failed(timeout=10, fail_if_false=False)
            if not hasattr(profile, 'expect_error'):
                logger.warn("No 'expect_value' was set in test data")
                continue
            expect_error = profile.expect_error
            if expect_error in actual_error:
                logger.warn("Can not edit server profile when using error configuration")
                failed += 1
            EditServerProfile.click_cancel_button()
        else:
            logger.warn("The server profile should not be edited when using error configuration")

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if not_exists > 0:
        logger.warn("There are %s server profile(s) are not existing, please remove them before test" % not_exists)
        return False
    else:
        if total - failed == 0:
            logger.warn("All of %s server profiles are not successfully edited using error configuration" % total)
            return True
        else:
            logger.warn("%s server profile(s) is edited or error message is not match with expectant, test is considered FAIlED " % (total - failed))
            return False


def verify_can_edit_server_profile_general_info_when_server_power_on(profile_obj):
    """
    The method just used to verify some general info edit when server power on.
    Example: Name/Description/Connection name.

    If some special test data were set, edit will failed.
    Example: Server hardware/Connection Port/Add Connection/Boot Settings/Bios Settings
    """

    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    total = len(profile_obj)
    not_exists = 0
    edited = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("editing a server profile with name '%s' ..." % profile.name)
        # checking if the profile is not existing for editing
        if not VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' does not exist" % profile.name)
            not_exists += 1
            continue
        CommonOperationServerProfile.click_server_profile(profile.name)

        EditServerProfile.select_action_edit()
        EditServerProfile.wait_edit_server_profile_dialog_shown()
        BuiltIn().sleep(2)
        EditServerProfile.input_name(profile.newName) if getattr(profile, 'newName', None) is not None else None
        EditServerProfile.input_description(profile.desc) if getattr(profile, 'desc', None) is not None else None

        # Server hardware must be "power" on status
        if not VerifyServerProfile.is_power_on_error_visible_when_edit_server_profile(profile.server, 10):
            logger.warn("Server hardware '%s' is not 'Powered on, please power on it" % profile.server)
            continue

        sht_selected = EditServerProfile.get_selected_server_hardware_type(profile.server)
        if getattr(profile, 'hardwareType', None) is not None:
            if profile.hardwareType not in sht_selected:
                logger.warn("server hardware type '%s' of server '%s' is NOT consistent with test data '%s'" % (sht_selected, profile.server, profile.hardwareType))
                EditServerProfile.ChangeServerHardwareTypeAndEnclosureGroup.change_server_hardware_type(profile.hardwareType, timeout=5, fail_if_false=False)

        eg_selected = EditServerProfile.get_selected_enclosure_group(profile.server)
        if profile.enclgroup not in eg_selected:
            logger.warn("enclosure group '%s' of server '%s' is NOT consistent with test data '%s'" % (eg_selected, profile.server, profile.enclgroup))
            EditServerProfile.ChangeServerHardwareTypeAndEnclosureGroup.change_enclosure_group(profile.enclgroup, timeout=5, fail_if_false=False)

        # EditServerProfile.input_select_server_hardware(profile.server, auto_power_off=False)

        if getattr(profile, 'Affinity', None) is not None:
            logger.info("test data for 'Affinity' is found: <%s>, start setting Affinity ..." % profile.Affinity)
            EditServerProfile.select_affinity_by_text(profile.Affinity)

        if getattr(profile, 'Firmware', None) is not None:
            logger.info("test data for 'Firmware' is found: <%s>, start setting Firmware Baseline ..." % profile.Firmware)
            logger.debug("test data for 'Firmware' is found: <%s>" % profile.Firmware, also_console=False)
            # set Firmware Baseline and force-installation option
            CommonOperationServerProfile.Firmware.set(profile.Firmware)

        if getattr(profile, 'Connections', None) is not None:
            logger.debug("test data for 'Connections' is found: <%s>" % profile.Connections, also_console=False)
            logger.info("test data for 'Connections' is found, start adding connections ...")
            logger.warn("Only connection name is allowed to modification")
            # add connections
            CommonOperationServerProfile.Connection().set(profile.Connections)

        if getattr(profile, 'LocalStorage', None) is not None:
            logger.warn("Modify the 'BootSettings' section will return error when server power on, so ignore this setting")

        if getattr(profile, 'SANStorage', None) is not None:
            logger.warn("Modify the 'BootSettings' section will return error when server power on, so ignore this setting")

        if getattr(profile, 'BootSettings', None) is not None:
            logger.warn("Modify the 'BootSettings' section will return error when server power on, so ignore this setting")

        if getattr(profile, 'Advanced', None) is not None:
            logger.warn("Modify the 'Advanced' section will return error when server power on, so ignore this setting")

        EditServerProfile.click_ok_button()
        if CommonOperationServerProfile.BootSettings.get_error_message_from_boot_mode() is not None:
            logger.warn("test data may be wrongly defined for 'Boot mode', which caused an error that blocks profile being created. "
                        "test will skip this profile '%s' and continue to create other server profiles" % profile.name)
            continue

        BuiltIn().sleep(2)
        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
        if status is True:
            logger.warn("unexpected error occurred: %s" % msg)
            ui_lib.fail_test(msg)

        EditServerProfile.wait_edit_server_profile_dialog_disappear(timeout=300)
        FusionUIBase.show_activity_sidebar()
        profile_name = profile.newName if getattr(profile, 'newName', None) is not None else profile.name
        FusionUIBase.wait_activity_action_ok(profile_name, 'Update', timeout=300, fail_if_false=True)
        FusionUIBase.show_activity_sidebar()
        CommonOperationServerProfile.wait_server_profile_status_ok(profile_name, timeout=300, fail_if_false=True)
        logger.info("edited server profile '%s' successfully" % profile_name)
        edited += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no server profile to edit! all %s server profile(s) is NOT existing, test is considered FAILED" % not_exists)
        return False
    else:
        if edited < total:
            logger.warn("not all of the server profile(s) is successfully edited - %s out of %s edited " % (edited, total))
            if edited + not_exists == total:
                logger.warn("%s not-existing server profile(s) is skipped being edited, test is considered FAILED" % not_exists)
                return False
            else:
                logger.warn("%s not-existing server profile(s) is skipped being edited, %s profile(s) left is failed being edited " % (not_exists, total - edited - not_exists))
                return False

    logger.info("all of the server profile(s) is successfully edited - %s out of %s " % (edited, total))
    return True


def verify_can_not_create_server_profile_with_error_configuration(profile_obj):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    total = len(profile_obj)
    failed = 0
    already_exists = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("creating a server profile with name '%s' ..." % profile.name)
        # checking if the profile is already existing
        if not VerifyServerProfile.verify_server_profile_not_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' already exists" % profile.name)
            already_exists += 1
            continue

        auto_power_off = False if getattr(profile, 'auto_power_off', '').lower() == 'false' else True
        # open Create SP dialog and enter data ...
        CreateServerProfile.click_create_profile_button()
        CreateServerProfile.wait_create_server_profile_dialog_shown()

        CreateServerProfile.input_name(profile.name)
        CreateServerProfile.input_description(getattr(profile, 'desc', ''))

        if not CreateServerProfile.input_select_server_hardware(profile.server, auto_power_off=auto_power_off):
            logger.warn("server hardware '%s' is not selected for creating server profile, may be wrong name, or powered on but failed to power it off. "
                        "test will skip this profile '%s' and continue to create other server profiles" % (profile.server, profile.name))
            continue
        msg = CreateServerProfile.get_error_message_from_server_hardware()
        if msg is not None:
            logger.warn("error occurred, server profile can not be created successfully: \n<%s>" % msg)
            ui_lib.fail_test(msg)

        if profile.server != 'unassigned':
            # verify if 'Server hardware type' is automatically set by selecting 'Server hardware'
            sht_selected = CreateServerProfile.get_selected_server_hardware_type(profile.server)
            if profile.hardwareType not in sht_selected:
                msg = "selected server hardware type '%s' of server '%s' is NOT consistent with test data '%s'" % (sht_selected, profile.server, profile.hardwareType)
                logger.warn(msg)
                ui_lib.fail_test(msg)
        else:
            # input 'Enclosure group'
            CreateServerProfile.input_select_server_hardware_type(profile.hardwareType)
            CreateServerProfile.input_select_enclosure_group(profile.enclgroup) if getattr(profile, 'enclgroup', None) is not None else None
            CreateServerProfile.get_selected_server_hardware_type(profile.server)

        if getattr(profile, 'Firmware', None) is not None:
            logger.info("test data for 'Firmware' is found: <%s>, start setting Firmware Baseline ..." % profile.Firmware)
            logger.debug("test data for 'Firmware' is found: <%s>" % profile.Firmware, also_console=False)
            # set Firmware Baseline and force-installation option
            CommonOperationServerProfile.Firmware.set(profile.Firmware)

        # Add multiple networks one a physical port
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
            CreateServerProfile.Advanced.set(profile)

        CreateServerProfile.click_create_button()
        if CommonOperationServerProfile.BootSettings.get_error_message_from_boot_mode() is not None:
            logger.warn("test data of server profile '%s' may be wrongly defined for 'Boot mode', which caused an error that blocks profile being created. "
                        "test will skip this profile and continue to create other server profiles" % profile.name)
            continue
        if not CreateServerProfile.wait_create_server_profile_dialog_disappear(10, False):
            # get error message and compile with expectant value
            actual_error = CreateServerProfile.get_error_message_if_save_create_failed(timeout=10, fail_if_false=False)
            if not hasattr(profile, 'expect_error'):
                logger.warn("No 'expect_value' was set in test data")
                continue
            expect_error = profile.expect_error
            if expect_error in actual_error:
                logger.warn("Can not create server profile when using error configuration")
                failed += 1
            CreateServerProfile.click_cancel_button()
        else:
            logger.warn("The server profile should not be created when using error configuration")

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if already_exists > 0:
        logger.warn("There are %s server profile(s) are already existing, please remove them before test" % already_exists)
        return False
    else:
        if total - failed == 0:
            logger.warn("All of %s server profiles are not successfully created using error configuration" % total)
            return True
        else:
            logger.warn("%s server profile(s) is created, test is considered FAIlED " % (total - failed))
            return False


def __get_time_from_timestamp(timestamp):
    """ """
    logger._debug("Splitting the complete timestamp %s by space to fetch only the time " % timestamp)
    t_time = timestamp.split()[1]
    if len(time) > 0:
        logger._debug("after splitting the timestamp, the time obtained is %s" % t_time)
    else:
        logger._warn("after splitting the timestamp, the time obtained is %s" % t_time)
    return t_time


def is_element_present_in_activity_page(profilename, message, start_time):
    """ """
    BuiltIn().sleep(5)  # wait for fields to load

    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionActivityPage.ID_PAGE_LABEL):
        base_page.navigate_base(FusionActivityPage.ID_PAGE_LABEL, FusionUIBaseElements.ID_MENU_LINK_ACTIVITY, "css=span.hp-page-item-count")
    # Validating the creation of server profile with time stamp and activity progress of the profile
    if ui_lib.wait_for_element(FusionServerProfilesPage.ID_ACTIVITY_PROGRESS_MOVE % (message, profilename), PerfConstants.DEFAULT_SYNC_TIME):
        logger._log_to_console_and_log_file("Operation started on Server Profile %s started " % profilename)
    else:
        logger.warn("When we got to the activity page, the profile %s was no longer in progress" % profilename)
    logger._log_to_console_and_log_file(start_time)
    # waits until the task completes
    ui_lib.wait_for_element_notvisible(FusionServerProfilesPage.ID_ACTIVITY_TIMESTAMP_MOVE % (message, profilename), PerfConstants.CREATE_SERVER_PROFILE_TIME)
    if ui_lib.wait_for_element(FusionServerProfilesPage.ID_ACTIVITY_SUCCESS_MOVE % (message, profilename, start_time)):
        logger._log_to_console_and_log_file("Operation of server profile %s is done successfully" % profilename)
        return True
    elif ui_lib.wait_for_element(FusionServerProfilesPage.ID_ACTIVITY_ERROR_MOVE % (message, profilename, start_time)):
        logger._log_to_console_and_log_file("Operation of server profile %s failed with errors" % profilename)
        return False
    else:
        logger.warn("Operation of server profile %s NOT found" % profilename)
        return False


def verify_required_fields_for_iscsi_boot(profile_obj):
    """ Input blank fields for iSCSI boot when adding a connection during Create Server Profile and verify required
        fields error message is displayed

    Arguments:
      name*                --  Name of server hardware as a string.
      server*              --  server hardware name of the server for which this profile is about to be created.
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
            secondIp       --  Second Boot Target IP Address
            initiatorName  --  iSCSI Initiator name, left blank
            initiatorIpv4* --  iSCSI Initiator IP address. left blank
            subnetMask*    --  iSCSI Subnet mask, left blank
            gateway        --  iSCSI Gateway, left blank
            targetName*    --  iSCSI Target name, left blank
            targetLun*     --  iSCSI Target LUN, left blank
            targetIp*      --  iSCSI Target IP address, left blank
            targetPort*    --  iSCSI Target port, left blank
            secondPort     --  iSCSI Second target port
            chapLvl        --  iSCSI Authentication Level
            chapName       --  iSCSI CHAP name, left blank
            chapSecret     --  iSCSI CHAP secret, left blank
            mchapName      --  iSCSI MCHAP name, left blank
            mchapSecret    --  iSCSI MHAP secret, left blank

    * Required Arguments

    Example:
        <profile name="Required Fields"
                 profile=""
                 profileName=""
                 server="unassigned"
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
                            initiatorName=""
                            initiatorIpv4=""
                            subnetMask=""
                            gateway=""
                            targetName=""
                            targetLun=""
                            targetIp=""
                            targetPort=""
                            secondPort=""
                            chapLvl="Mutual CHAP"
                            chapName=""
                            chapSecret=""
                            mchapName=""
                            mchapSecret=""/>
            </Connections>
        </profile >
    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(profile_obj), '-' * 14))
        logger.info("Creating Server Profile for server | %s | ..." % profile.name)

        # checking if the profile already exists
        if not VerifyServerProfile.verify_server_profile_not_exist(profile.name, fail_if_false=False):
            ui_lib.fail_test("Server profile | %s | already exists" % profile.name)

        # - Prep the auto_power_off switch
        # - By default, this keyword will power off the server if it's powered on -- unless the attribute 'auto_power_off' is explicitly set to 'false'
        auto_power_off = False if getattr(profile, 'auto_power_off', '').lower() == 'false' else True
        # open Create SP dialog and enter data ...
        CreateServerProfile.click_create_profile_button()
        CreateServerProfile.wait_create_server_profile_dialog_shown()

        CreateServerProfile.input_name(profile.name)
        CreateServerProfile.input_description(getattr(profile, 'desc', ''))
        # Input 'Server hardware'
        # - input server name,
        # - select option from the popped out drop-down list,
        # - power off the server if the it is powered on,
        # - verify the server hardware type of the selected one is refreshed to the type name displayed in the drop-down list
        #     for selecting server hardware
        if not CreateServerProfile.input_select_server_hardware(profile.server, auto_power_off=auto_power_off):
            logger.warn("server hardware '%s' is not selected for creating server profile, may be wrong name, or powered on but failed to power it off. "
                        "test will skip this profile '%s' and continue to create other server profiles" % (profile.server, profile.name))
            continue
        msg = CreateServerProfile.get_error_message_from_server_hardware()
        if msg is not None:
            logger.warn("error occurred, server profile can not be created successfully: \n<%s>" % msg)
            ui_lib.fail_test(msg)
        # input 'Server hardware type', 'Enclosure group'

        if profile.server != 'unassigned':
            # verify if 'Server hardware type' is automatically set by selecting 'Server hardware'
            sht_selected = CreateServerProfile.get_selected_server_hardware_type(profile.server)
            if sht_selected == '':
                logger.info("'server hardware type' is not selected, select it with name '%s'" % profile.hardwareType)
                CreateServerProfile.input_select_server_hardware_type(profile.hardwareType)
                CreateServerProfile.input_select_enclosure_group(profile.enclgroup) if getattr(profile, 'enclgroup', None) is not None else None
                sht_selected = CreateServerProfile.get_selected_server_hardware_type(profile.server)
            elif profile.hardwareType not in sht_selected:
                msg = "selected server hardware type '%s' of server '%s' is NOT consistent with test data '%s'" % (sht_selected, profile.server, profile.hardwareType)
                logger.warn(msg)
                ui_lib.fail_test(msg)
        else:
            # input 'Enclosure group'
            if hasattr(profile, 'for_server'):
                hardware_type = FusionUIBase.APIMethods().get_server_hardware_type_by_server_hardware_name(
                    profile.for_server)
                logger.info('For server attribute is %s, hardware type is %s' % (profile.for_server, hardware_type))
                CreateServerProfile.input_select_server_hardware_type(hardware_type)
            else:
                CreateServerProfile.input_select_server_hardware_type(profile.hardwareType)
            CreateServerProfile.input_select_enclosure_group(profile.enclgroup) if getattr(profile, 'enclgroup', None) is not None else None
            sht_selected = CreateServerProfile.get_selected_server_hardware_type(profile.server)

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
                CommonOperationServerProfile.Connection.verify_connection_not_exist(connection.name, fail_if_false=True)

                # Add the connection
                CommonOperationServerProfile.Connection.click_add_connection_button()
                CommonOperationServerProfile.Connection.wait_add_connection_dialog_shown()

                CommonOperationServerProfile.Connection.input_name(connection.name)
                CommonOperationServerProfile.Connection.select_function_type_by_text(connection.FunctionType, fail_if_false=True)
                CommonOperationServerProfile.Connection.input_select_network(connection.network)
                CommonOperationServerProfile.Connection.input_select_port(connection.port)
                CommonOperationServerProfile.Connection.input_requested_bandwidth(connection.RequestedBandwidth)
                CommonOperationServerProfile.Connection.select_boot_by_text(connection.boot, fail_if_false=True)

                # Input information for the iSCSI boot connection. Data file should have blanks for all fields except secondIp.
                if connection.boot == 'iSCSI primary' or connection.boot == 'iSCSI secondary':
                    CommonOperationServerProfile.Connection.set_iscsi_boot_options(connection)

                # Click "Add" button
                CommonOperationServerProfile.Connection.click_add_button()

                # Verify error messages
                CommonOperationServerProfile.Connection.verify_iscsi_initiator_name_error_message("This field is required.")
                CommonOperationServerProfile.Connection.verify_iscsi_initiator_ip_error_message("This field is required.")
                CommonOperationServerProfile.Connection.verify_iscsi_subnet_error_message("This field is required.")
                CommonOperationServerProfile.Connection.verify_iscsi_gateway_error_message("")

                if hasattr(connection, "vlanId"):
                    CommonOperationServerProfile.Connection.verify_iscsi_vlan_id_error_message("This field is required.")
                else:
                    CommonOperationServerProfile.Connection.verify_iscsi_vlan_id_error_message("")

                CommonOperationServerProfile.Connection.verify_iscsi_target_name_error_message("This field is required.")
                CommonOperationServerProfile.Connection.verify_iscsi_target_lun_error_message("This field is required.")
                CommonOperationServerProfile.Connection.verify_iscsi_target_ip_error_message("This field is required.")
                CommonOperationServerProfile.Connection.verify_iscsi_target_port_error_message("This field is required.")

                if getattr(connection, "secondIp", "") is not "":
                    CommonOperationServerProfile.Connection.verify_iscsi_second_ip_error_message("")
                    CommonOperationServerProfile.Connection.verify_iscsi_second_port_error_message("This field is required.")
                else:
                    CommonOperationServerProfile.Connection.verify_iscsi_second_ip_error_message("")
                    CommonOperationServerProfile.Connection.verify_iscsi_second_port_error_message("")

                if hasattr(connection, "chapLvl"):
                    if connection.chapLvl == "None":
                        CommonOperationServerProfile.Connection.verify_iscsi_chap_name_error_message("")
                        CommonOperationServerProfile.Connection.verify_iscsi_chap_secret_error_message("")
                        CommonOperationServerProfile.Connection.verify_iscsi_mchap_name_error_message("")
                        CommonOperationServerProfile.Connection.verify_iscsi_mchap_secret_error_message("")
                    elif connection.chapLvl == "CHAP":
                        CommonOperationServerProfile.Connection.verify_iscsi_chap_name_error_message("This field is required.")
                        CommonOperationServerProfile.Connection.verify_iscsi_chap_secret_error_message("This field is required.")
                        CommonOperationServerProfile.Connection.verify_iscsi_mchap_name_error_message("")
                        CommonOperationServerProfile.Connection.verify_iscsi_mchap_secret_error_message("")
                    elif connection.chapLvl == "Mutual CHAP":
                        CommonOperationServerProfile.Connection.verify_iscsi_chap_name_error_message("This field is required.")
                        CommonOperationServerProfile.Connection.verify_iscsi_chap_secret_error_message("This field is required.")
                        CommonOperationServerProfile.Connection.verify_iscsi_mchap_name_error_message("This field is required.")
                        CommonOperationServerProfile.Connection.verify_iscsi_mchap_secret_error_message("This field is required.")

                # Click "Cancel" button
                CommonOperationServerProfile.Connection.click_cancel_button()
        else:
            ui_lib.fail_test("Connections object not present in data file for profile with name | %s |" % profile.name)

        CreateServerProfile.click_cancel_button()


def validate_error_on_create_server_profile(profile_obj):
    """ Create Server Profile For BL/DL to validate errors

    Arguments:
      name*             --  Name of server hardware as a string.
      desc              --  description of the iLO of this server profile.
      server*           --  server hardware name of the server for which this profile is about to be created.
      hardwareType*     --  server hardware type of the server, will be used to verify the selected server's SHT is correct.
                            This should be the 'DL380p Gen8' instead of 'DL380p Gen8 1/2' to avoid the mismatching due to Fusion's SHT identifying mechanism.


    * Required Arguments

    Example:
        data/servers/BLServerProfiles -> @{TestData.servers.BLServerProfiles.Create}
        <servers>
            <BLServerProfiles>
                <Create>
                    <profile name="SP_wpst23bay3_BL465c_Gen8" desc="SP BL465c Gen8" server="wpst23, bay 3" hardwareType="BL465c Gen8" enclgroup="GRP-wpst32">
                        <Firmware FirmwareBaseline="managed manually" xxx="" />
                        <Connections>

                                <connection name="CON_FA1" xxx="" />
                                <connection name="CON_FA2" xxx="" />
                                <connection name="CON_ETH" xxx="" />
                        </Connections>
                     </profile>
                </Create>
            </BLServerProfiles>
        </servers>

    """

    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
    total = len(profile_obj)
    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("creating a server profile with name '%s' ..." % profile.name)
        if not VerifyServerProfile.verify_server_profile_not_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' already exists" % profile.name)
            continue
        auto_power_off = False if getattr(profile, 'auto_power_off', '').lower() == 'false' else True
        CreateServerProfile.click_create_profile_button()
        CreateServerProfile.wait_create_server_profile_dialog_shown()
        CreateServerProfile.input_name(profile.name)
        CreateServerProfile.input_description(getattr(profile, 'desc', ''))
        if not CreateServerProfile.input_select_server_hardware(profile.server, auto_power_off=auto_power_off):
            logger.warn("server hardware '%s' is not selected for creating server profile, may be wrong name, or powered on but failed to power it off. "
                        "test will skip this profile '%s' and continue to create other server profiles" % (profile.server, profile.name))
            continue
        if profile.server != 'unassigned':
            # verify if 'Server hardware type' is automatically set by selecting 'Server hardware'
            sht_selected = CreateServerProfile.get_selected_server_hardware_type(profile.server)
            if sht_selected == '':
                logger.info("'server hardware type' is not selected, select it with name '%s'" % profile.hardwareType)
                CreateServerProfile.input_select_server_hardware_type(profile.hardwareType)

                CreateServerProfile.input_select_enclosure_group(profile.enclgroup) if getattr(profile, 'enclgroup', None) is not None else None
        # input 'Affinity' for BL server, or when 'server hardware' == 'unassigned'
        if hasattr(profile, 'Bandwidth_Error'):
            logger.info("change to 'Connections' view ...")
            FusionUIBase.select_view_by_name('Connections')
            logger.info("start deleting connections ...")
            total = len(profile.Connections)
            cls = CommonOperationServerProfile.Connection
            for n, connection in enumerate(profile.Connections):
                expected_message = profile.Bandwidth_Error
                logger.info("adding a connection with name '%s' ..." % connection.name)
                if cls.verify_connection_not_exist(connection.name, fail_if_false=False) is False:
                    logger.warn("connection '%s' already exists, skipped ..." % connection.name)
                    continue
                cls.click_add_connection_button()
                cls.wait_add_connection_dialog_shown(time_for_loading=3)
                cls.input_name(connection.name)
                cls.select_function_type_by_text(connection.FunctionType, timeout=10, fail_if_false=True)
                logger.info("Expected Error message is '%s' ..." % expected_message)
                cls.input_select_network(connection.network)
                logger.info("n/w selected")
                cls.input_select_port(connection.port)
                cls.input_requested_bandwidth(connection.RequestedBandwidth) if ui_lib.is_visible(cls.e.ID_INPUT_REQUESTED_BANDWIDTH) else None
                cls.select_requested_bandwidth_by_text(connection.RequestedBandwidth) if ui_lib.is_visible(cls.e.ID_SELECTBOX_REQUESTED_BANDWIDTH) else None
                cls.click_add_button()
                if not VerifyServerProfile.verify_bandwidth_error(expected_message, timeout=5, fail_if_false=True):
                    logger.info("Validation failed")
                cls.click_cancel_button()
                logger.info("clicked cancel button")
        else:
            CommonOperationServerProfile.Connection.set(profile.Connections)
        CreateServerProfile.click_create_button()
        status, _ = FusionUIBase.get_error_message_from_dialog(timeout=10)
        if status is True:
            if hasattr(profile, 'update_error'):
                if not VerifyServerProfile.verify_error_message_for_update_action(profile.update_error, timeout=5, fail_if_false=True):
                    logger.info("Validation failed")
                else:
                    logger.info("Error validation successful")
                    CreateServerProfile.click_cancel_button()
            else:
                if not VerifyServerProfile.verify_error_message_in_add_connection(profile.connection_error, timeout=5, fail_if_false=True):
                    logger.info("Validation failed")
                else:
                    logger.info("Error validation successful")
                    CreateServerProfile.click_cancel_button()
        else:
            logger.info("Profile created successfully")
    return True


def validate_help_text_for_managed_volume_on_add_connection_dialog(profile_obj):
    """Validate server profile help text for managed volume on add connection dialog
    Arguments:
        name            -- name of server profile
        server          -- server hardware used to create server profile
        Connections     -- need to add connection to SP
    Returns:
    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
    logger.info("Validating help text for managed volume on add connection ...")
    count = 0
    total = len(profile_obj)
    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        CreateServerProfile.click_create_profile_button()
        CreateServerProfile.wait_create_server_profile_dialog_shown()
        # input parameters for createing profile to enable Add connection button
        CreateServerProfile.input_name(profile.name)
        CreateServerProfile.input_description(getattr(profile, 'desc', ''))
        CreateServerProfile.input_select_server_hardware(profile.server)
        if profile.server == "unassigned":
            CreateServerProfile.input_select_server_hardware_type(profile.hardwareType)
            CreateServerProfile.input_select_enclosure_group(profile.enclgroup)

        FusionUIBase.select_view_by_name('Connections')
        logger.info("Change to 'Connections' view ...")
        if CommonOperationServerProfile.Connection.validate_help_text_on_add_connection_dialog(getattr(profile, 'Connections')):
            count += 1

    if count == total:
        logger.info("Validating help text for managed volume successfully by all server profile.")
        return True
    else:
        logger.warn("'%s' out of '%s': failed to validating help text for managed volume on add connection dialog." % (count, total))
        return False


def validate_add_plus_on_add_connection_dialog(profile_obj):
    """Validate add plus on add connection
        Arguments:
            name            -- name of server profile
            server          -- server hardware used to create server profile
            Connections     -- need to add connection to SP
        Returns:
        """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
    logger.info("Validating help text for managed volume on add connection ...")
    count = 0
    total = len(profile_obj)
    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        CreateServerProfile.click_create_profile_button()
        CreateServerProfile.wait_create_server_profile_dialog_shown()
        # input parameters for createing profile to enable Add connection button
        CreateServerProfile.input_name(profile.name)
        CreateServerProfile.input_description(getattr(profile, 'desc', ''))
        CreateServerProfile.input_select_server_hardware(profile.server)
        if profile.server == "unassigned":
            CreateServerProfile.input_select_server_hardware_type(profile.hardwareType)
            CreateServerProfile.input_select_enclosure_group(profile.enclgroup)

        FusionUIBase.select_view_by_name('Connections')
        logger.info("Change to 'Connections' view ...")
        # verify add plus button visible
        CommonOperationServerProfile.Connection.click_add_connection_button()
        if CommonOperationServerProfile.Connection.verify_add_plus_button_existing():
            count += 1

    if count == total:
        logger.info("Validating add plus on add connection dialog successfully by all server profile.")
        return True
    else:
        logger.warn("'%s' out of '%s': failed to validating add plus on add connection dialog." % (count, total))
        return False


def validate_user_specified_invisible_on_edit_connection_dialog(profile_obj):
    """Validating 'Use user specified IDs' check box invisible during editing boot option on Edit Connection
    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
    logger.info("Validating 'Use user specified IDs' check box invisible during editing boot option on Edit Connection ...")
    count = 0
    total = len(profile_obj)

    for _, profile in enumerate(profile_obj):
        CommonOperationServerProfile.click_server_profile(profile.name)
        EditServerProfile.select_action_edit()
        EditServerProfile.wait_edit_server_profile_dialog_shown()

        logger.info("Change to 'Connection' view ...")
        FusionUIBase.select_view_by_name('Connections')
        logger.info("Open editing connections dialog ...")

        for _, connection in enumerate(getattr(profile, 'Connections', '')):
            logger.info("editing a connection with name '%s' ..." % connection.name)
            if not CommonOperationServerProfile.Connection.verify_connection_exist(connection.name):
                logger.warn("connection '%s' does not exist, skipped ..." % connection.name)
                continue
            CommonOperationServerProfile.Connection.click_edit_connection_button(connection.name)
            CommonOperationServerProfile.Connection.wait_edit_connection_dialog_shown()
            if not CommonOperationServerProfile.Connection.verify_user_specified_initiator_existing():
                count += 1

    if count == total:
        logger.info("Validating user specified invisible on add connection dialog successfully by all server profile.")
        return True
    else:
        logger.warn("'%s' out of '%s': failed to validating user specified invisible on add connection dialog." % (count, total))
        return False


def validate_server_profile_cannot_be_deleted_when_power_on(profile_name):
    """ """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
    #   check if server profile exists
    if not VerifyServerProfile.verify_server_profile_exist(profile_name, fail_if_false=False):
        logger.warn("server profile '%s' does NOT exist! keyword '%s' returns a 'False'" % (profile_name, sys._getframe().f_code.co_name))
        return False
    #   check if power status of server profile
    CommonOperationServerProfile.click_server_profile(profile_name=profile_name)
    FusionUIBase.select_view_by_name(view_name='General', timeout=5, fail_if_false=False)
    if VerifyServerProfile.verify_general_server_power(expect_value='On', timeout=7, fail_if_false=False) is False:
        logger.warn("power status of server profile '%s' is off,should be on." % profile_name)
        power_on_server_profile_by_name(profile_name)
    #   start performing remove action
    DeleteServerProfile.select_action_delete()
    DeleteServerProfile.wait_delete_server_profile_dialog_open()
    DeleteServerProfile.click_yes_delete_button()
    status, msg = FusionUIBase.get_error_message_from_dialog(timeout=30)
    if status is True:
        logger.info("error occurred: %s" % msg)
        if "Unable to delete server profile" and "The profile operation did not succeed because power was not off for server hardware" in msg:
            logger.info("Successfully verified 'can not delete server profile when server power status is on,expected error popped up'")
            ret = True
        else:
            logger.warn("Failed to verify 'can not delete server profile when server power status is on' -- expected error message was not found")
            ret = False
    else:
        logger.warn("Failed to verify 'can not delete server profile when server power status is on' -- no error message occured at all")
        ret = False
    DeleteServerProfile.click_cancel_button()
    DeleteServerProfile.wait_delete_server_profile_dialog_disappear()
    return ret


def validate_server_profile_task_step(profile_obj):
    """ Validate server profile create/edit task text

    Arguments:
      name*             --  Name of server profile as a string.
      task*             --  Name of server profile task as a string.
      method*           --  Text that server profile task steps contain.

    * Required Arguments

    Example:
        data/servers/BLServerProfiles -> @{TestData.servers.BLServerProfiles.Create}
        <servers>
            <BLServerProfiles>
                <Create>
                    <profile name="SP_wpst23bay3_BL465c_Gen8" task="Create" method="HPE Intelligent Provisioning" />
                     </profile>
                </Create>
            </BLServerProfiles>
        </servers>

    """

    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
    total = len(profile_obj)
    not_exists = 0
    verified = 0

    for n, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("Validate server profile <%s> task contains <%s>" % (profile.name, profile.method))
        if not VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False):
            logger.warn("server profile '%s' does not exist" % profile.name)
            not_exists += 1
            continue

        CommonOperationServerProfile.click_server_profile(profile.name)
        FusionUIBase.select_view_by_name(view_name='Activity', timeout=5, fail_if_false=False)
        CommonOperationServerProfile.click_activity_collapser(profile.task)
        timeout = int(getattr(profile, 'validate_timeout', '5'))
        ret = VerifyServerProfile.verify_activity_contains_text(profile.method, timeout=timeout, fail_if_false=False)
        # Verify method text not exist in steps
        if getattr(profile, 'exist', '').lower() == 'false':
            if ret is True:
                ui_lib.fail_test("%s should not exist in task steps" % profile.method)
        elif ret is False:
            ui_lib.fail_test("%s should exist in task steps" % profile.method)

        logger.info("Server profile '%s' got the correct task method" % profile.name)
        verified += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no server profile to view! all %s server profile(s) is NOT existing, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if verified < total:
            logger.warn("not all of task for the server profile(s) is successfully verified - %s out of %s verified " % (verified, total))
            if verified + not_exists == total:
                logger.warn("%s not-existing server profile(s) is skipped, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s not-existing server profile(s) is skipped, %s profile(s) left is failed being verified " % (not_exists, total - verified - not_exists))
                return False

    logger.info("all of the server profile(s) is successfully verified - %s out of %s " % (verified, total))
    return True


def get_server_profile_error_message(profile_name):
    """ This function gets the server profile error message
        Example:
        <server_profile_error>
            <profile name="SP-Enc1-Bay10" />
        </server_profile_error>
    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)
    if not VerifyServerProfile.verify_server_profile_exist(profile_name, fail_if_false=False):
        ui_lib.fail_test("Proflie %s is not present, hence exiting" % profile_name)
    else:
        CommonOperationServerProfile.click_server_profile(profile_name=profile_name, time_for_loading=4)
        return CommonOperationServerProfile.get_profile_error_message(timeout=20, fail_if_false=False)


def get_profile_connection_mac_address_and_port(profile_obj):
    """ Get Mac Address and port information of the given  Profile connection
        Example:
        |Fusion UI Get Profile Connection Mac Address And Port |   |

        Arguments:
        name*             --  Name of server profile as a string.

        * Required Arguments
    """

    FusionUIBase.navigate_to_section(SectionType.SERVER_PROFILES, time_for_loading=5)

    total = len(profile_obj)
    mac_address_list = []

    for profile_count, profile in enumerate(profile_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((profile_count + 1), total, '-' * 14))
        logger.info("Verifying Connections info of a server profile named '%s'" % profile.name)
        #   check if server profile exists
        if not VerifyServerProfile.verify_server_profile_exist(profile.name, fail_if_false=False):
            logger.warn("Server profile '%s' does not exist" % profile.name)
            continue
        CommonOperationServerProfile.click_server_profile(profile_name=profile.name, time_for_loading=4)
        FusionUIBase.select_view_by_name(view_name='Connections', timeout=5, fail_if_false=False)
        connections = CommonOperationServerProfile.Connection.get_connection_from_connection_view()
        port = CommonOperationServerProfile.Connection.get_connection_port()
        for i in range(1, len(connections) + 1):
            CommonOperationServerProfile.Connection.click_expand_connections(i)
            mac = CommonOperationServerProfile.Connection.get_mac_address()
            mac_address_list.append(mac.split()[0])
            CommonOperationServerProfile.Connection.click_expand_connections(i)
        return (mac_address_list, port)

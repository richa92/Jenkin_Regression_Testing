"""
    # (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
    Storage Systems Page
"""

# from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.data import test_data

from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.storage.storagesystems import CommonOperationStorageSystems, \
    VerifyStorageSystem
from FusionLibrary.ui.business_logic.storage.storagesystems import AddStorageSystems
from FusionLibrary.ui.business_logic.storage.storagesystems import EditStorageSystems
from FusionLibrary.ui.business_logic.storage.storagesystems import RemoveStorageSystems
from FusionLibrary.ui.business_logic.storage.storagesystems import RefreshStorageSystems
from FusionLibrary.ui.business_logic.storage.storagesystems import EditStorageSystemCredentials
from FusionLibrary.ui.business_logic.storage.volumes import CommonOperationVolumes
from FusionLibrary.ui.business_logic.storage.storagepools import CommonOperationStoragePools
from FusionLibrary.ui.business_logic.storage.volumesets import CommonOperationVolumeSets
from FusionLibrary.ui.business_logic.networking.networks import CommonOperationNetworks
from FusionLibrary.ui.business_logic.storage.sans import CommonOperationSANs
from FusionLibrary.ui.business_logic.base import FusionUIBase
from FusionLibrary.ui.business_logic.base import SectionType
from FusionLibrary.ui.storage.storagesystems_elements import FusionStorageSystemsPage
# from FusionLibrary.ui.general import base_page
# from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.business_logic.base import FusionUIConst
from RoboGalaxyLibrary.utilitylib import logging as logger
import time
# from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants


def select_storage_system(storagesystemname):
    """
        Select a specific storage system
    """
    logger.info("Selecting a storage system with name {0}".format(storagesystemname))
    if CommonOperationStorageSystems.verify_storage_system_exist(storagesystemname, fail_if_false=False):
        if CommonOperationStorageSystems.verify_locate_error_exists():
            selenium2lib = ui_lib.get_s2l()
            selenium2lib.reload_page()
        CommonOperationStorageSystems.click_storage_system(storagesystemname)
        CommonOperationStorageSystems.wait_storage_system_selected(storagesystemname)
        return True
    else:
        logger.warn("Storage system '{0}' does not exist".format(storagesystemname))
        return False


def add_storage_systems(*storagesys_obj):
    """ Add Storage System

    Arguments:
      name*                 --  Name of storage system.
      StorageSystemType*    --  'StoreServ' or 'StoreVirtual' or 'Nimble'.
      simplename*           --  short name of the storage system.
      userid*               --  username to login to the storage system via 3PAR management console (or other similar tools).
      pswd*                 --  password to login to the storage system via 3PAR management console (or other similar tools).
      domain                --  domain name of the storage system you choose to use, which the storage pools belong to.
      storagepools          --  node name for containing storage pools settings
            name*               --  name of the storage pool
            Manage*             --  whether or not to turn on the 'Manage' checkbox on UI page for the storage pool
      testtype              -- 'unhappy' - this is used to indicate that negative testing is being performed and that the error message needs to appear to be verified. It also allows
                                the test to return to the normal flow of the method after an error is discovered by pressing cancel

    * Required Arguments

    Example:
        tests/RIST/OVST/OVAQual_data.xml    -> @{TestData.storagesystems}
        <storagesystems>
            <storagesystem name="wpst3par-7200-12-srv.vse.rdlabs.hpecorp.net" StorageSystemType="StoreServ" simplename="wpst3par-7200-12-srv" userid="fusionadm" pswd="hpvse1" domain="ova" testtype="unhappy">
                <storagepools>
                    <storagepool name="FC_OVA_r1" Manage="true"/>
                    <storagepool name="FC_OVA_r5" Manage="false"/>
                    <storagepool name="FC_OVA_r6" Manage="true"/>
                </storagepools>
            </storagesystem>
        </storagesystems>

    """
    FusionUIBase.navigate_to_section(SectionType.STORAGE_SYSTEMS)
    if isinstance(storagesys_obj, test_data.DataObj):
        storagesys_obj = [storagesys_obj]
    elif isinstance(storagesys_obj, tuple):
        storagesys_obj = list(storagesys_obj)
    count = 0
    new_storagesys_obj = []
    logger.info("{0} PREPARATION  {0}".format('-' * 17))

    for n, storage in enumerate(storagesys_obj):
        if getattr(storage, 'simplename', '') != '':
            storage_simple_name = storage.simplename
        else:
            storage_simple_name = storage.name.lower().split('.')[0]
        if getattr(storage, 'remove_if_exists', 'true').lower() == 'true':
            remove_if_exists = True
        else:
            remove_if_exists = False
        if not CommonOperationStorageSystems.verify_storage_system_not_exist(storage_simple_name, fail_if_false=False):
            logger.warn("Storage system '{0}' already exists".format(storage_simple_name))
            if remove_if_exists is True:
                logger.info("Removing the storage system since 'remove_if_exists' is set to 'True'")
                if not remove_storage_system(storage_simple_name, fail_if_false=False):
                    count += 1
                else:
                    new_storagesys_obj.append(storage)
            else:
                logger.warn("Error: Was not able to create the existing storage system '%s'." % storage_simple_name)
                count += 1
        else:
            new_storagesys_obj.append(storage)

    for n, storage in enumerate(new_storagesys_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(new_storagesys_obj), '-' * 14))
        if getattr(storage, 'simplename', '') != '':
            storage_simple_name = storage.simplename
        else:
            storage_simple_name = storage.name.lower().split('.')[0]
        logger.info("Adding a storage system with name '{0}'".format(storage_simple_name))
        if n == 0 or getattr(storage, 'testtype', '') == 'unhappy':
            FusionUIBase.show_activity_sidebar()
            AddStorageSystems.click_add_storage_system_button()
        AddStorageSystems.wait_add_storage_system_dialog_shown()
        AddStorageSystems.select_storage_system_type_by_text(storage.StorageSystemType)
        AddStorageSystems.select_storage_credentials_section()
        AddStorageSystems.input_ip_address_or_host_name(storage.name, storage_system_type=storage.StorageSystemType)
        AddStorageSystems.input_user_name(storage.userid, storage_system_type=storage.StorageSystemType)
        AddStorageSystems.input_password(storage.pswd, storage_system_type=storage.StorageSystemType)
        AddStorageSystems.click_connect_button()
        AddStorageSystems.wait_connected_to_storage_system(timeout=45)
        # AddStorageSystems.select_storage_general_section()
        if storage.StorageSystemType.lower() == FusionUIConst.CONST_STORAGE_SYSTEM_TYPE_STORESERV.lower():
            if getattr(storage, 'testtype', '') == 'unhappy':
                AddStorageSystems.input_select_storage_domain(storage.domain, fail_if_false=False)
            else:
                AddStorageSystems.input_select_storage_domain(storage.domain)
        if getattr(storage, 'storagepools', '') != '':
            AddStorageSystems.set_manage_option_for_pools(storage.storagepools, storage.StorageSystemType)
        AddStorageSystems.select_storage_system_ports_section()
        if getattr(storage, 'port', '') != '':
            for portinfos in storage.port:
                AddStorageSystems.input_select_expected_san_network_and_port_group(portinfos.name, portinfos.sanornetwork, portinfos.group)
        if getattr(storage, 'vipnetwork', '') != '':
            if getattr(storage, 'testtype', '') == 'unhappy':
                AddStorageSystems.select_vipnetwork(storage.vipnetwork, fail_if_false=False)
            else:
                AddStorageSystems.select_vipnetwork(storage.vipnetwork)
        if n == (len(new_storagesys_obj) - 1):
            AddStorageSystems.click_add_button()
            if CommonOperationStorageSystems.verify_locate_error_exists():
                selenium2lib = ui_lib.get_s2l()
                selenium2lib.reload_page()
        else:
            AddStorageSystems.click_add_plus_button()
        if getattr(storage, 'testtype', '') != 'unhappy':
            if AddStorageSystems.wait_adding_message_disappear(timeout=40, fail_if_false=False):
                status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
                msg = str(msg).split('[')[0]
        else:
            status = False
            activity_status = FusionUIBase.get_latest_activity_status("", "Update", fail_if_false=True)
            if activity_status != "error":
                msg = "Activity status of %s discovered instead of error %activity_status"
            if n != (len(new_storagesys_obj) - 1):
                AddStorageSystems.click_cancel_button()
            if status is True:
                ui_lib.fail_test(msg)
    time.sleep(4)
    FusionUIBase.show_activity_sidebar()

    logger.info("{0} VERIFICATION {0}".format('-' * 17))
    for n, storage in enumerate(new_storagesys_obj):
        if getattr(storage, 'testtype', '') != "unhappy":      # do not verify if unhappy test
            if getattr(storage, 'simplename', '') != '':
                storage_simple_name = storage.simplename
            else:
                storage_simple_name = storage.name.lower().split('.')[0]
                CommonOperationStorageSystems.wait_storage_system_status_ok(storage_simple_name)
            logger.info("Add storage system {0} successfully".format(storage_simple_name))
        else:
            logger.info("Unhappy path testing, VERIFICATION skipped")

    if count > 0:
        logger.warn("Failure: Not able to add some of storage systems, please check all warning messages")
        return False
    return True


def edit_storage_systems(*storagesys_obj):
    """ Edit Storage System

    Arguments:
      name*                 --  Name of storage system.
      StorageSystemType*    --  'StoreServ' or 'StoreVirtual'.
      simplename*           --  short name of the storage system.
      userid*               --  username to login to the storage system via 3PAR management console (or other similar tools).
      pswd*                 --  password to login to the storage system via 3PAR management console (or other similar tools).
      domain*               --  domain name of the storage system you choose to use, which the storage pools belong to.
      port*                 --  port information= 'name', 'sanornetwork', 'group'
      testtype              -- 'unhappy' - this is used to indicate that negative testing is being performed and that the error message needs to appear
                                to be verified. It also allows the test to return to the normal flow of the method after an error is discovered by
                                pressing cancel

    * Required Arguments

    Example:
        tests/strm/GUI/strn_data.xml    -> @{TestData.storagesystems}
        <storagesystem  name="172.18.11.11"  StorageSystemType="StoreServ"  simplename="ThreePAR-1"
                        userid="dcs" pswd="dcs" domain="TestDomain" testtype="unhappy" >
              <port    name="0:1:2" sanornetwork ="SAN1_1" group="None"/>
        </storagesystem>

    """
    FusionUIBase.navigate_to_section(SectionType.STORAGE_SYSTEMS)
    if isinstance(storagesys_obj, test_data.DataObj):
        storagesys_obj = [storagesys_obj]
    elif isinstance(storagesys_obj, tuple):
        storagesys_obj = list(storagesys_obj)
    count = 0
    for n, storage in enumerate(storagesys_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(storagesys_obj), '-' * 14))
        if getattr(storage, 'simplename', '') != '':
            storage_simple_name = storage.simplename
        else:
            storage_simple_name = storage.name.lower().split('.')[0]
        logger.info("Editing a storage system with name '{0}'".format(storage_simple_name))
        if not select_storage_system(storage_simple_name):
            count += 1
            continue
        EditStorageSystems.select_actions_edit()
        EditStorageSystems.wait_edit_dialog_shown()
        if storage.has_property('port'):
            for portinfos in storage.port:
                EditStorageSystems.input_select_expected_san_network_and_port_group(portinfos.name, portinfos.sanornetwork, portinfos.group)
        if getattr(storage, 'vipnetwork', '') != '':
            if getattr(storage, 'testtype', '') == 'unhappy':
                EditStorageSystems.select_vipnetwork(storage.vipnetwork, fail_if_false=False)
            else:
                EditStorageSystems.select_vipnetwork(storage.vipnetwork)
        EditStorageSystems.click_ok_button()
        if not EditStorageSystems.wait_edit_dialog_disappear(timeout=15, fail_if_false=False):
            status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
            msg = str(msg).split('[')[0]
            if getattr(storage, 'testtype', '') == 'unhappy':
                status = False
                EditStorageSystems.verify_edit_storage_system_error(storage.simplename, 1, True)
                EditStorageSystems.click_cancel_button()
            if status is True:
                ui_lib.fail_test(msg)
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(storage_simple_name, "Update", timeout=10)
        FusionUIBase.show_activity_sidebar()
        CommonOperationStorageSystems.wait_storage_system_status_ok(storage_simple_name)
        logger.info("Edit storage system {0} successfully".format(storage_simple_name))
    if count > 0:
        logger.warn("Failure: Not able to edit some of storage systems, please check all warning messages")
        return False
    return True


def edit_credentials_storage_system(*storagesys_obj):
    """
        Edit Storage System Credentials


    Arguments:


    * Required Arguments

    Example:


    """
    FusionUIBase.navigate_to_section(SectionType.STORAGE_SYSTEMS)
    if isinstance(storagesys_obj, test_data.DataObj):
        storagesys_obj = [storagesys_obj]
    elif isinstance(storagesys_obj, tuple):
        storagesys_obj = list(storagesys_obj)
    count = 0
    for n, storage in enumerate(storagesys_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(storagesys_obj), '-' * 14))
        if getattr(storage, 'simplename', '') != '':
            storage_simple_name = storage.simplename
        else:
            storage_simple_name = storage.name.lower().split('.')[0]
        logger.info("Editing credentials for a storage system with name %s" % storage_simple_name)
        if not select_storage_system(storage_simple_name):
            count += 1
            continue
        EditStorageSystemCredentials.select_actions_edit_credentials()
        EditStorageSystemCredentials.wait_edit_credentials_dialog_shown()
        EditStorageSystemCredentials.input_ip_address_or_host_name(storage.name)
        EditStorageSystemCredentials.input_user_name(storage.username)
        EditStorageSystemCredentials.input_password(storage.password)
        EditStorageSystemCredentials.click_ok()
        if getattr(storage, 'testtype', '') == 'unhappy':
            if EditStorageSystemCredentials.wait_edit_credentials_dialog_disappear(timeout=10, fail_if_false=False):
                status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
                if status is False:
                    ui_lib.fail_test(msg)
                else:
                    ui_lib.fail_test("the edit credentials dialog disappear in 5 seconds")
            EditStorageSystemCredentials.click_cancel(timeout=5)
        else:
            if not EditStorageSystemCredentials.wait_edit_credentials_dialog_disappear(timeout=10, fail_if_false=False):
                status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
                if status is True:
                    ui_lib.fail_test(msg)
                else:
                    ui_lib.fail_test("the edit credentials dialog didn't disappear in 5 seconds")
            FusionUIBase.show_activity_sidebar()
            FusionUIBase.wait_activity_action_ok(storage_simple_name, "Update", timeout=10)
            FusionUIBase.show_activity_sidebar()
        CommonOperationStorageSystems.wait_storage_system_status_ok(storage_simple_name, fail_if_false=False)
        logger.info("Edit credentials of storage system {0} successfully".format(storage_simple_name))

    if count > 0:
        logger.warn("Failure: Not able to edit credential for some storage systems, please check all warning messages")
        return False
    return True


def remove_storage_system(storage_system_name, fail_if_false=True):
    """
        Select a specific storage system to Remove

    Arguments:


    * Required Arguments

    Example:


    """
    select_storage_system(storage_system_name)
    RemoveStorageSystems.select_actions_remove()
    RemoveStorageSystems.wait_remove_dialog_shown()
    RemoveStorageSystems.click_yes_remove_button()
    RemoveStorageSystems.wait_remove_dialog_disappear()
    FusionUIBase.show_activity_sidebar()
    FusionUIBase.wait_activity_action_ok(storage_system_name, "Remove", timeout=50)
    FusionUIBase.show_activity_sidebar()
    if RemoveStorageSystems.wait_storage_system_show_not_found(storage_system_name, timeout=20, fail_if_false=False):
        logger.info("Storage system status appear as 'not found', remove storage system {0} successfully.".format(storage_system_name))
        return True
    elif CommonOperationStorageSystems.verify_storage_system_not_exist(storage_system_name, timeout=10, fail_if_false=False):
        logger.info("Remove storage system {0} successfully".format(storage_system_name))
        return True
    else:
        if fail_if_false is True:
            ui_lib.fail_test("The storage system does not disappear in 10s!")
        else:
            logger.warn("The storage system does not disappear in 10s!")
            return False


def remove_storage_systems(*storagesys_obj):
    """ Remove Storage Systems

    Arguments:


    * Required Arguments

    Example:


    """
    FusionUIBase.navigate_to_section(SectionType.STORAGE_SYSTEMS)
    if isinstance(storagesys_obj, test_data.DataObj):
        storagesys_obj = [storagesys_obj]
    elif isinstance(storagesys_obj, tuple):
        storagesys_obj = list(storagesys_obj)

    count = 0
    for n, storage in enumerate(storagesys_obj):  # pylint: disable=W0612
        if getattr(storage, 'simplename', '') != '':
            storage_simple_name = storage.simplename
        else:
            storage_simple_name = storage.name.lower().split('.')[0]
        logger.info("Removing a storage system with name %s" % storage_simple_name)
        if not select_storage_system(storage_simple_name):
            count += 1
            continue

        # storages_exists = CommonOperationStorageSystems.get_storage_system_list()
        # storages_exclude_self = [storage for storage in storages_exists if storage != storage_simple_name]
        remove_storage_system(storage_simple_name)
    if count > 0:
        logger.warn("Failure: Not able to remove some of storage systems, please check all warning messages")
        return False
    return True


def refresh_storage_systems(*storagesys_obj):
    """ Refresh Storage Systems

    Arguments:


    * Required Arguments

    Example:


    """
    FusionUIBase.navigate_to_section(SectionType.STORAGE_SYSTEMS)
    if isinstance(storagesys_obj, test_data.DataObj):
        storagesys_obj = [storagesys_obj]
    elif isinstance(storagesys_obj, tuple):
        storagesys_obj = list(storagesys_obj)

    count = 0
    for n, storage in enumerate(storagesys_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(storagesys_obj), '-' * 14))
        if getattr(storage, 'simplename', '') != '':
            storage_simple_name = storage.simplename
        else:
            storage_simple_name = storage.name.lower().split('.')[0]
        logger.info("Refreshing a storage system with name %s" % storage_simple_name)
        if not select_storage_system(storage_simple_name):
            count += 1
            continue
        RefreshStorageSystems.select_actions_refresh()
        # RefreshStorageSystems.wait_general_state_refreshing(timeout=8)
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(storage_simple_name, "Refresh", timeout=30)
        FusionUIBase.show_activity_sidebar()
        if storage.StorageSystemType == 'StoreServ':
            RefreshStorageSystems.wait_storeserv_state_managed(timeout=10)
        elif storage.StorageSystemType == 'StoreVirtual':
            RefreshStorageSystems.wait_storevirtual_state_managed(timeout=10)
        else:
            RefreshStorageSystems.wait_nimble_state_managed(timeout=10)
        CommonOperationStorageSystems.wait_storage_system_status_ok(storage_simple_name)
        logger.info("Refresh storage system {0} successfully".format(storage_simple_name))
    if count > 0:
        logger.warn("Failure: Not able to refresh some of storage systems, please check all warning messages")
        return False
    return True


# begin - verify storage system
def verify_storage_system(*storagesys_obj):
    """ Verify storage system

    Arguments:
      <lig>
          name*                     --  In General view. Name of storage system as a string.
          state                     --  In General view. Storage system state as string. e.g. Configured
          username                  --  In General view. User name which is used for importing storage system
          iphostname                --  In General view. Ip or host name of storage system.
          storage_domain            --  In General view. Storage domain name. e.g. wpst32
          model                     --  In General view. Storage system model. e.g. HP_3PAR 7200
          firmware                  --  In General view. Firmware version of storage system.
          wwn                       --  In General view. World wide name of storage system.
          serial_number             --  In General view. Serial number of storage system.
          used_by_pools             --  In General view. Which storage pools are using this storage system. e.g. 3 storage pools
          used_by_volumes           --  In General view. Which storage volumes are using this storage system. e.g. 4 volumes
          used_by_volumesets        --  In General view. Which volume sets are using this storage system
          utilization_total         --  In Utilization view. Total capacity of storage system
          utilization_allocated     --  In Utilization view. Total allocated storage space
          utilization_free          --  In Utilization view. Free space of storage system

          <storage_pools> optional, for verify storage pool configuration (only support 1 node)
              <item> (support multiple nodes)
                name*               --  In Storage pools view. Storage pool name
                state               --  In Storage pools view. Storage pool state. e.g. ok, unknown, warning, error
                allocated_capacity  --  In Storage pools view. Allocated capacity of storage pool
                total_capacity      --  In Storage pools view. Total capacity of storage pool
          <storage_system_ports> optional, for verify storage system port configuration (only support 1 node)
              <item> (support multiple nodes)
                port*                --  In Storage System Ports view. Port name. e.g. 0:1:1
                state                --  In Storage System Ports view. Port state. e.g. ok, unknown, warning, error
                label                --  In Storage System Ports view. Port label. e.g. none
                protocol             --  In Storage System Ports view. Port protocol. e.g. FC
                expected_san_network --  In Storage System Ports view. Expected san network of port as string. e.g. Auto, 'wpstsan14.vse.rdlabs.hpecorp.net-10:00:00:27:f8:fe:0c:55 16.125.65.9'
                actual_san           --  In Storage System Ports view. Actual san of port as string. e.g. none, unknown, 'wpstsan14.vse.rdlabs.hpecorp.net-10:00:00:27:f8:fe:0c:55'
                port_group           --  In Storage System Ports view. Port group. e.g. Auto
                wwpn                 --  In Storage System Ports view. Port WWPN. e.g. 20:11:00:02:AC:00:B2:C7
                partner_port         --  In Storage System Ports view. Port partner port. e.g. 1:1:1
                failover_state       --  In Storage System Ports view. Failover state of port. e.g. none

    * Required Arguments

    Example:
        data/verifystoragesystems -> @{TestData.verifystoragesystems}
        <verifystoragesystems>
            <storagesystem
                    name="wpst3par-7200-7-srv"
                    state="Configured"
                    username="fusionadm"
                    iphostname="wpst3par-7200-7-srv.vse.rdlabs.hpecorp.net"
                    storage_domain="wpst32"
                    model="HP_3PAR 7200"
                    firmware="3.1.3.230"
                    wwn="28:11:00:02:AC:00:B2:C7"
                    serial_number="1645767"
                    used_by_pools="3 storage pools"
                    used_by_volumes="4 volumes"
                    utilization_total="9.56 TiB"
                    utilization_allocated="5.85 TiB"
                    utilization_free="3.71 TiB">

                <storage_pools>
                    <item name="FC_wpst32_r1" state="ok" allocated_capacity="40.00" total_capacity="1939"/>
                    <item name="FC_wpst32_r5" state="ok" allocated_capacity="403.00" total_capacity="3250"/>
                    <item name="FC_wpst32_r6" state="ok" allocated_capacity="44.00" total_capacity="2864"/>
                </storage_pools>

                <storage_system_ports>
                    <item port="0:1:1" state="unknown" label="none" protocol="FC" expected_san_network="Auto" actual_san="none" port_group="Auto" wwpn="20:11:00:02:AC:00:B2:C7" partner_port="1:1:1" failover_state="none" />
                    <item port="0:1:2" state="unknown" label="none" protocol="FC" expected_san_network="Auto" actual_san="unknown" port_group="Auto" wwpn="20:12:00:02:AC:00:B2:C7" partner_port="1:1:2" failover_state="none" />
                    <item port="0:2:1" state="unknown" label="none" protocol="FC" expected_san_network="Auto" actual_san="none" port_group="Auto" wwpn="20:21:00:02:AC:00:B2:C7" partner_port="1:2:1" failover_state="none" />
                    <item port="0:2:2" state="unknown" label="none" protocol="FC" expected_san_network="Auto" actual_san="none" port_group="Auto" wwpn="20:22:00:02:AC:00:B2:C7" partner_port="1:2:2" failover_state="none" />
                    <item port="0:2:3" state="ok" label="none" protocol="FC" expected_san_network="wpstsan14.vse.rdlabs.hpecorp.net-10:00:00:27:f8:fe:0c:55 16.125.65.9" actual_san="wpstsan14.vse.rdlabs.hpecorp.net-10:00:00:27:f8:fe:0c:55" port_group="Auto" wwpn="20:23:00:02:AC:00:B2:C7" partner_port="1:2:3" failover_state="none" />
                    <item port="0:2:4" state="ok" label="none" protocol="FC" expected_san_network="wpstsan14.vse.rdlabs.hpecorp.net-10:00:00:27:f8:fe:0c:56 16.125.65.9" actual_san="wpstsan14.vse.rdlabs.hpecorp.net-10:00:00:27:f8:fe:0c:56" port_group="Auto" wwpn="20:24:00:02:AC:00:B2:C7" partner_port="1:2:4" failover_state="none" />
                    <item port="1:1:1" state="unknown" label="none" protocol="FC" expected_san_network="Auto" actual_san="none" port_group="Auto" wwpn="21:11:00:02:AC:00:B2:C7" partner_port="0:1:1" failover_state="none" />
                    <item port="1:1:2" state="unknown" label="none" protocol="FC" expected_san_network="Auto" actual_san="unknown" port_group="Auto" wwpn="21:12:00:02:AC:00:B2:C7" partner_port="0:1:2" failover_state="none" />
                    <item port="1:2:1" state="unknown" label="none" protocol="FC" expected_san_network="Auto" actual_san="none" port_group="Auto" wwpn="21:21:00:02:AC:00:B2:C7" partner_port="0:2:1" failover_state="none" />
                    <item port="1:2:2" state="unknown" label="none" protocol="FC" expected_san_network="Auto" actual_san="none" port_group="Auto" wwpn="21:22:00:02:AC:00:B2:C7" partner_port="0:2:2" failover_state="none" />
                    <item port="1:2:3" state="ok" label="none" protocol="FC" expected_san_network="wpstsan14.vse.rdlabs.hpecorp.net-10:00:00:27:f8:fe:0c:55 16.125.65.9" actual_san="wpstsan14.vse.rdlabs.hpecorp.net-10:00:00:27:f8:fe:0c:55" port_group="Auto" wwpn="21:23:00:02:AC:00:B2:C7" partner_port="0:2:3" failover_state="none" />
                    <item port="1:2:4" state="ok" label="none" protocol="FC" expected_san_network="wpstsan14.vse.rdlabs.hpecorp.net-10:00:00:27:f8:fe:0c:56 16.125.65.9" actual_san="wpstsan14.vse.rdlabs.hpecorp.net-10:00:00:27:f8:fe:0c:56" port_group="Auto" wwpn="21:24:00:02:AC:00:B2:C7" partner_port="0:2:4" failover_state="none" />

                </storage_system_ports>
            </storagesystem>
        </verifystoragesystems>

    """
    FusionUIBase.navigate_to_section(SectionType.STORAGE_SYSTEMS)
    if isinstance(storagesys_obj, test_data.DataObj):
        storagesys_obj = [storagesys_obj]
    elif isinstance(storagesys_obj, tuple):
        storagesys_obj = list(storagesys_obj)
    count = 0
    for n, storage in enumerate(storagesys_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(storagesys_obj), '-' * 14))
        if getattr(storage, 'simplename', '') != '':
            storage_simple_name = storage.simplename
        else:
            storage_simple_name = storage.name.lower().split('.')[0]
        logger.info("Editing a storage system with name '{0}'".format(storage_simple_name))
        if not select_storage_system(storage_simple_name):
            count += 1
            continue

        # Overview - General
        FusionUIBase.select_view_by_name('Overview')
        logger.info("Verifying configuration in General view...")
        time.sleep(5)
        VerifyStorageSystem.verify_storagesystem_name(storage.simplename, "Storage System")

        if hasattr(storage, "state"):
            VerifyStorageSystem.verify_general_state(storage.state, storage.StorageSystemType.lower())

        if hasattr(storage, "StorageSystemType"):
            VerifyStorageSystem.verify_general_type(storage.StorageSystemType, storage.StorageSystemType.lower())

        if hasattr(storage, "user_name"):
            VerifyStorageSystem.verify_general_user_name(storage.user_name, storage.StorageSystemType.lower())

        if storage.StorageSystemType == "StoreServ":
            if hasattr(storage, "name"):
                VerifyStorageSystem.verify_general_ip_host_name(storage.name)

            if hasattr(storage, "storage_domain"):
                VerifyStorageSystem.verify_general_storage_domain(storage.storage_domain)

            if hasattr(storage, "model"):
                VerifyStorageSystem.verify_general_model(storage.model)

            if hasattr(storage, "firmware"):
                VerifyStorageSystem.verify_general_firmware(storage.firmware)

            if hasattr(storage, "wwn"):
                VerifyStorageSystem.verify_general_wwn(storage.wwn)

            if hasattr(storage, "serial_number"):
                VerifyStorageSystem.verify_general_serial_number(storage.serial_number)

        elif storage.StorageSystemType == "StoreVirtual":
            if hasattr(storage, "name"):
                VerifyStorageSystem.verify_general_cluster_ip_host_name(storage.name)

            if hasattr(storage, "software_version"):
                VerifyStorageSystem.verify_general_software_version(storage.software_version)

            if hasattr(storage, "lun_mode"):
                VerifyStorageSystem.verify_general_lun_mode(storage.lun_mode)

            if hasattr(storage, "simplename"):
                VerifyStorageSystem.verify_general_cluster_name(storage.simplename)

        elif storage.StorageSystemType == "Nimble":
            if hasattr(storage, "name"):
                VerifyStorageSystem.verify_general_mgmt_host_name(storage.name)

            if hasattr(storage, "software_version"):
                VerifyStorageSystem.verify_general_nimble_software_version(storage.software_version)

            if hasattr(storage, "lun_mode"):
                VerifyStorageSystem.verify_general_nimble_lun_mode(storage.lun_mode)

            if hasattr(storage, "array_type"):
                VerifyStorageSystem.verify_general_array_type(storage.array_type)

            if hasattr(storage, "encryption"):
                VerifyStorageSystem.verify_general_encryption(storage.encryption)

            if hasattr(storage, "pools"):
                VerifyStorageSystem.verify_general_nimble_storage_pools(storage.pools)

            if hasattr(storage, "volumes"):
                VerifyStorageSystem.verify_general_nimble_volumes(storage.volumes)

            if hasattr(storage, "volumesets"):
                VerifyStorageSystem.verify_general_nimble_volumesets(storage.volumesets)

        if hasattr(storage, "used_by_pools"):
            VerifyStorageSystem.verify_general_used_by_storage_pools(storage.used_by_pools)

        if hasattr(storage, "used_by_volumes"):
            VerifyStorageSystem.verify_general_used_by_storage_volumes(storage.used_by_volumes)

        # Overview - Utilization
        # if hasattr(storage, "utilization_total"):
        #     VerifyStorageSystem.verify_utilization_total(storage.utilization_total)

        # if hasattr(storage, "utilization_allocated"):
        #     VerifyStorageSystem.verify_utilization_allocated(storage.utilization_allocated)

        # if hasattr(storage, "utilization_free"):
        #     VerifyStorageSystem.verify_utilization_free(storage.utilization_free)

        # General
        FusionUIBase.select_view_by_name('General')

        if hasattr(storage, "state"):
            VerifyStorageSystem.verify_general_state(storage.state, storage.StorageSystemType.lower())

        if hasattr(storage, "StorageSystemType"):
            VerifyStorageSystem.verify_general_type(storage.StorageSystemType, storage.StorageSystemType.lower())

        if hasattr(storage, "user_name"):
            VerifyStorageSystem.verify_general_user_name(storage.user_name, storage.StorageSystemType.lower())

        if storage.StorageSystemType == "StoreServ":
            if hasattr(storage, "name"):
                VerifyStorageSystem.verify_general_ip_host_name(storage.name)

            if hasattr(storage, "storage_domain"):
                VerifyStorageSystem.verify_general_storage_domain(storage.storage_domain)

            if hasattr(storage, "model"):
                VerifyStorageSystem.verify_general_model(storage.model)

            if hasattr(storage, "firmware"):
                VerifyStorageSystem.verify_general_firmware(storage.firmware)

            if hasattr(storage, "wwn"):
                VerifyStorageSystem.verify_general_wwn(storage.wwn)

            if hasattr(storage, "serial_number"):
                VerifyStorageSystem.verify_general_serial_number(storage.serial_number)

        elif storage.StorageSystemType == "StoreVirtual":
            if hasattr(storage, "name"):
                VerifyStorageSystem.verify_general_cluster_ip_host_name(storage.name)

            if hasattr(storage, "software_version"):
                VerifyStorageSystem.verify_general_software_version(storage.software_version)

            if hasattr(storage, "simplename"):
                VerifyStorageSystem.verify_general_cluster_name(storage.simplename)

        elif storage.StorageSystemType == "Nimble":

            if hasattr(storage, "software_version"):
                VerifyStorageSystem.verify_general_nimble_software_version(storage.software_version)

            if hasattr(storage, "lun_mode"):
                VerifyStorageSystem.verify_general_nimble_lun_mode(storage.lun_mode)

            if hasattr(storage, "array_type"):
                VerifyStorageSystem.verify_general_array_type(storage.array_type)

            if hasattr(storage, "encryption"):
                VerifyStorageSystem.verify_general_encryption(storage.encryption)

        if hasattr(storage, "used_by_pools"):
            VerifyStorageSystem.verify_general_used_by_storage_pools(storage.used_by_pools)

        if hasattr(storage, "used_by_volumes"):
            VerifyStorageSystem.verify_general_used_by_storage_volumes(storage.used_by_volumes)

        if hasattr(storage, "used_by_volumesets"):
            VerifyStorageSystem.verify_general_used_by_volumesets(storage.used_by_volumesets)

        # Utilization
        FusionUIBase.select_view_by_name('Utilization')
        # if hasattr(storage, "utilization_total"):
        #     VerifyStorageSystem.verify_utilization_total(storage.utilization_total)

        # if hasattr(storage, "utilization_allocated"):
        #     VerifyStorageSystem.verify_utilization_allocated(storage.utilization_allocated)

        # if hasattr(storage, "utilization_free"):
        #     VerifyStorageSystem.verify_utilization_free(storage.utilization_free)

        # Storage pools

        if hasattr(storage, "storage_pools"):

            storage_pools = storage.storage_pools

            for pool_obj in storage_pools:

                VerifyStorageSystem.verify_storage_pools_name_exist(pool_obj.name)

                if hasattr(pool_obj, "state"):
                    VerifyStorageSystem.verify_storage_pools_state(pool_obj.name, pool_obj.state)

                # if hasattr(pool, "allocated_capacity"):
                #     VerifyStorageSystem.verify_storage_pools_allocated_capacity(pool.name, pool.allocated_capacity)

                # if hasattr(pool, "total_capacity"):
                #     VerifyStorageSystem.verify_storage_pools_total_capacity(pool.name, pool.total_capacity)

        FusionUIBase.select_view_by_name("Storage System Ports")

        if hasattr(storage, "storage_system_ports"):

            storage_ports = storage.storage_system_ports

            for port_obj in storage_ports:

                VerifyStorageSystem.verify_storage_system_path_port_exist(port_obj.port)

                if hasattr(port_obj, 'state'):
                    VerifyStorageSystem.verify_storage_system_path_state(port_obj.port, port_obj.state)

                if hasattr(port_obj, 'label'):
                    VerifyStorageSystem.verify_storage_system_path_label(port_obj.port, port_obj.label)

                if hasattr(port_obj, 'protocol'):
                    VerifyStorageSystem.verify_storage_system_path_protocol(port_obj.port, port_obj.protocol)

                if hasattr(port_obj, 'expected_san_network'):
                    VerifyStorageSystem.verify_storage_system_path_expected_san_network(port_obj.port, port_obj.expected_san_network)

                if hasattr(port_obj, 'actual_san'):
                    VerifyStorageSystem.verify_storage_system_path_actual_san(port_obj.port, port_obj.actual_san)

                if hasattr(port_obj, 'port_group'):
                    VerifyStorageSystem.verify_storage_system_path_port_group(port_obj.port, port_obj.port_group)

                # expand port panel
                VerifyStorageSystem.expand_storage_system_path_detail_panel(port_obj.port)
                VerifyStorageSystem.make_storage_port_panel_into_viewpoint(port_obj.port)

                if hasattr(port_obj, 'wwpn'):
                    VerifyStorageSystem.verify_storage_system_path_wwpn(port_obj.port, port_obj.wwpn)

                if hasattr(port_obj, 'partner_port'):
                    VerifyStorageSystem.verify_storage_system_path_partner_port(port_obj.port, port_obj.partner_port)

                if hasattr(port_obj, 'failover_state'):
                    VerifyStorageSystem.verify_storage_system_path_failover_state(port_obj.port, port_obj.failover_state)

                # folding port panel
                VerifyStorageSystem.fold_storage_system_path_detail_panel(port_obj.port)
# end - verify storage systemG


def verify_storage_system_links(*storagesys_links):
    """ Verify storage system link
    Arguments:
        systemname*              --  Name of storage system
        resourcename*            --  Page Name to verify (i.e. Volumes, Storage Systems, Storage Pools, Networks, SANs)
        viewname                 --  Name of tab view on storage systems screen that link is located on

    * Required Argument

    Example:
        tests/strm/GUI/strm_data.xml -> @{TestData.strm.storagesystemlinks}
           <storagesystemlinks>
                    <link  systemname="Cluster-1" resourcename="Volumes" viewname="Overview"/>
                    <link  systemname="Cluster-1" resourcename="Storage Pools" viewname="Overview"/>
                    <link systemname="Cluster-1" resourcename="Networks" viewname="Storage System Ports"
                    <link  systemname="ThreePAR-1" resourcename="Volumes" viewname="Overview"/>
                    <link  systemname="ThreePAR-1" resourcename="Storage Pools" viewname="Overview"/>
                    <link systemname="ThreePAR-1" resourcename="SANs" viewname="Storage System Ports"/>
          </storagesystemlinks>

    """
    FusionUIBase.navigate_to_section(SectionType.STORAGE_SYSTEMS)
    if isinstance(storagesys_links, test_data.DataObj):
        storagesys_obj = [storagesys_links]
    elif isinstance(storagesys_links, tuple):
        storagesys_obj = list(storagesys_links)
    count = 0

    for n, storage in enumerate(storagesys_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(storagesys_obj), '-' * 14))
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
        logger.info("Verifying link for {} on storage system '{}' screen".format(storage_resource_name, storage_system_name))
        if not select_storage_system(storage_system_name):
            count += 1
            continue

        FusionUIBase.select_view_by_name(storage_view_name)
        time.sleep(5)
        logger.info("verify storage system link [%s] in %s view. verify count if needed." % (storage_resource_name, storage_view_name))
        logger.info("Entered resource=%s" % storage_resource_name)
        if storage_resource_name == "Storage Pools":
            CommonOperationStorageSystems.click_storage_system_pools_link()
            CommonOperationStoragePools.verify_storagepools_title(storage_resource_name, timeout=10, fail_if_false=True)
            FusionUIBase.navigate_to_section(SectionType.STORAGE_SYSTEMS)
        elif storage_resource_name == "Volumes":
            CommonOperationStorageSystems.click_storage_system_volumes_link()
            CommonOperationVolumes.verify_storagevolumes_title(storage_resource_name, timeout=10, fail_if_false=True)
            FusionUIBase.navigate_to_section(SectionType.STORAGE_SYSTEMS)
        elif storage_resource_name == "Networks":
            CommonOperationStorageSystems.click_network_link()
            CommonOperationNetworks.verify_network_title(storage_resource_name, timeout=10, fail_if_false=True)
            FusionUIBase.navigate_to_section(SectionType.STORAGE_SYSTEMS)
        elif storage_resource_name == "SANs":
            CommonOperationStorageSystems.click_sans_link()
            CommonOperationSANs.verify_sans_title(storage_resource_name, timeout=10, fail_if_false=True)
            FusionUIBase.navigate_to_section(SectionType.STORAGE_SYSTEMS)
        elif storage_resource_name == "Volume Sets":
            CommonOperationStorageSystems.click_volumesets_link()
            CommonOperationVolumeSets.verify_volumeset_title(storage_resource_name, timeout=10, fail_if_false=True)
            FusionUIBase.navigate_to_section(SectionType.STORAGE_SYSTEMS)

        else:
            return False


def delete_all_storage_systems():
    """ Delete All Storage Systems

    This method will create a list of all storage systems in Oneview. It then uses the list to delete all storage systems
    in Oneview.
    """
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionStorageSystemsPage.ID_PAGE_LABEL):
        navigate()

    storagesystem_list = [ui_lib.get_text(el) for el in selenium2lib._element_find(FusionStorageSystemsPage.ID_STORAGE_SYSTEMS_LIST, False, False)]
    count = 0
    for storagesystemname in storagesystem_list:
        logger._log_to_console_and_log_file("Deleting storagesystem: {0}".format(storagesystemname))
        storagesystem_obj = test_data.DataObj()
        storagesystem_obj.add_property('simplename', storagesystemname)
        net_obj = (storagesystem_obj)
        storagesystem_delete_status = remove_storage_systems(net_obj)

        if storagesystem_delete_status:
            logger._log_to_console_and_log_file("'{0}' storagesystem is deleted Successfully".format(storagesystemname))
            count += 1
        else:
            logger.warn("Failed to delete storagesystem: {0}".format(storagesystemname))

    if count == len(storagesystem_list):
        logger._log_to_console_and_log_file("All storagesystems deleted successfully from appliance")
        return True
    else:
        logger.warn("Failed to delete '{0}' storagesystems from appliance".format(len(storagesystem_list) - count))
        return False


def navigate():
    """
        Navigates to the Storage System Page
    """
    FusionUIBase.navigate_to_section(SectionType.STORAGE_SYSTEMS)

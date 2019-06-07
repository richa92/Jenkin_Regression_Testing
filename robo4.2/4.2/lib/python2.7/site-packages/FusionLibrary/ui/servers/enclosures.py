"""Library for Fusion Enclosure UI page.

    = Table of contents =

    - `Revision Notes`
    - `Usage`
    - `Valid log levels`
    - `Examples`
    - `Importing`
    - `Shortcuts`
    - `Keywords`

    = Revision Notes =

    | Rev      | Date         |   Originator              |  Comments                      |
    | 0.1     |   07/10/2013  |   Andy Tran               |  Initial version               |



    = Usage =

    This library has keywords for UI interaction with Fusion Enclosure UI page.

    = Valid log levels =

    None

    = Examples =

    Notice how keywords are linked from examples.

    | `Add Enclosure`      | ${myenclosure}    |                |               |
    | `Delete Enclosure` |   ${myenclosure}  |          |        |

"""


from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from robot.libraries.BuiltIn import time
from robot.libraries.BuiltIn import re
import sys

from FusionLibrary.ui.servers.enclosures_elements import FusionEnclosuresPage
from FusionLibrary.ui.business_logic.general.dashboard_elements import FusionDashboardPage
from FusionLibrary.ui.general.base_page import FusionUIBaseElements
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.business_logic.general.activity_elements import FusionActivityPage
from FusionLibrary.ui.general import activity
from FusionLibrary.ui.networking.logicalinterconnects_elements import FusionLogicalInterconnectsPage
from FusionLibrary.ui.business_logic.base import FusionUIBase, SectionType, FusionUIConst
from FusionLibrary.ui.business_logic.servers.enclosures import (C7000AddEnclosures,
                                                                C7000RemoveEnclosures,
                                                                C7000CommonOperationEnclosures,
                                                                C7000EditEnclosures,
                                                                C7000EnclosuresReapplyConfiguration,
                                                                C7000RefreshEnclosures,
                                                                C7000VerifyEnclosures,
                                                                TBirdVerifyEnclosures,
                                                                TBirdCommonOperationEnclosures,
                                                                TBirdEnclosuresInterconnectLinkTopology,
                                                                VerifyEnclosures,
                                                                EditScopeForEnclosures,
                                                                TBirdResetLinkModule)
from FusionLibrary.ui.business_logic.networking.interconnects import CommonOperationInterconnects, VerifyInterconnects, InterconnectLinkPorts
from FusionLibrary.ui.business_logic.networking.logicalinterconnects import C7000VerifyLogicalInterconnects
from FusionLibrary.ui.business_logic.networking.logicalinterconnectgroups import CommonOperationLogicalInterconnectGroups
from FusionLibrary.ui.business_logic.servers.enclosuregroups import C7000CommonOperationEnclosureGroups
from FusionLibrary.ui.business_logic.servers.serverhardware import CommonOperationServerHardware, VerifyHardware
from collections import defaultdict

ROBOT_LIBRARY_VERSION = '0.1'


def navigate():
    FusionUIBase.navigate_to_section(SectionType.ENCLOSURES)


# begin - add enclosure (new layer)
def add_enclosure(enc_obj):
    """ Add Enclosure

    Arguments:
      <enclosure> [1, )
          name*                     --  Name of enclosure as a string.
          create_new_eg*            --  Whether to create new enclosure group when adding enclosure. Only take effect when addas* set to Managed. Possible value: true|false
          encgroup*                 --  Enclosure group name as string. Not applicable when addas* set to Monitored. If create_new_eg* set to false, this value refer to a existing enclousre group.
          force*                    --  Whether to forcible import enclosure if it is managed/monitored by other appliance. Possible value: true|false.
          addas*                    --  Choose the method for importing enclosure. Possible value: Managed|Monitored|Migrate
                                        ** Currently not support 'Migrate' method
          frimwareBaseline*         --  Firmware baseline settings. You need to manually grab from add enclosure dialog. Only take effect when manageFirmware* set to true. Not applicable when addas* set to Monitored.
          licensing*                --  Licensing settings. Possible value: HPE OneViewAdvanced|HPE OneViewAdvanced w/o iLO. Not applicable when addas* set to Monitored.
          manageFirmware*           --  Whether to enable firmware management. Possible value: true|false. Not applicable when addas* set to Monitored.
          oa1hostname*              --  Enclosure's onboard administrator host name or ip. Not applicable when addas* set to Monitored.
          oa1username*              --  Username of enclosure's onboard administrator.
          oa1password*              --  Password of enclosure's onboard administrator.
          vcmusername*              --  Username of enclosure's virtual connect manager.
          vcmpassword*              --  Password of enclosure's virtual connect manager.
          dialog_close_timeout      --  Timeout for add enclosure dialog close.
          spp*
          upDateFor*
          <lig> [0, 1] optional, for create LIG when adding enclosure
            create_new*                 --  Whether to create new logical interconnect group or using existing LIG. Possible value: true|false.
            name*                       --  Logical interconnect group name
            internal_networks*          --  Configure internal networks, can be empty which indicate no need to configure internal networks
              <switch> [2, ) required, for specifying interconnect model
                bay*                    --  Interconnect bay no as integer. e.g. 1
                type*                   --  Interconnect bay model as string. Need to grap from create lig page. e.g. HP VC FlexFabric-20/40 F8 Module|HP VC FlexFabric-20/40 F8 Module
              <lus> [0, )optional, for adding uplink set
                connectionMode*         --  Possible value: Automatic (recommended)|Failover. Only take effect when network type set to Ethernet|Tunnel|Untagged
                lacptimer*              --  Possible value: Short (1s)|Long (30s). Only take effect when network type set to Ethernet|Tunnel|Untagged
                name*                   --  Uplink set name
                native*                 --  Ethernet name. Only take effect when network type set to Ethernet. e.g. dev102-vmmigration
                networkType*            --  Configure network type of uplink set. Possible value: Ethernet|Fibre Channel|Tunnel|Untagged
                networks*               --  Network names separated by comma. Only support specifying 1 network if network type set to Fibre Channel|Tunnel|Untagged. e.g. net14,net15,net16,net17
                ports*                  --  String value. Port configuration. Notice the difference of (Ethernet|Tunnel|Untagged) and (Fibre Cannel)
                                            * For Ethernet|Tunnel|Untagged, bay<bay no.>:<port name> .e.g. bay1:X1,bay1:X2
                                            * For Fibre Channel, bay<bay no.>:<port name>:<port speed>. Possible value of <port speed>: Auto|2 Gb/s|4 Gb/s|8 Gb/s. e.g. X1:Auto,X2:4 Gb/s
                preferredPort*          --  Configure preferred port only when Connection Mode set to Failover. Moreover only take effect when network type set to Ethernet|Tunnel|Untagged

    * Required Arguments

    Example:
        data/enclosure -> @{TestData.enclosures}
        <enclosures>
            <enclosure name="wpst32"
                    create_new_eg="true"
                    encgroup="GRP-wpst32"
                    force="true"
                    addas="Managed"
                    frimwareBaseline="Manage manually"
                    licensing="HPE OneViewAdvanced w/o iLO"
                    manageFirmware="false"
                    oa1hostname="wpst32-oa1.vse.rdlabs.hpecorp.net"
                    oa1password="hpvse14"
                    oa1username="Administrator"
                    vcmusername="Administrator"
                    vcmpassword="CXSLEJKWE"
                    dialog_close_timeout="500"
                    spp=""
                    upDateFor="">
                <lig create_new="true" name="" internal_networks="">
                    <switch bay="1" type="HP VC FlexFabric 10Gb/24-Port Module" />
                    <switch bay="2" type="HP VC FlexFabric 10Gb/24-Port Module" />
                    <switch bay="3" type="HP VC FlexFabric 10Gb/24-Port Module" />
                    <switch bay="4" type="HP VC FlexFabric 10Gb/24-Port Module" />
                    <switch bay="5" type="HP VC 8Gb 20-Port FC Module" />
                    <switch bay="6" type="HP VC 8Gb 20-Port FC Module" />
                    <lus connectionMode="AUTO" lacptimer="30" name="FA-path3" native="" networkType="Fibre Channel" networks="FA3" ports="X1:Auto" preferredPort="" />
                    <lus connectionMode="AUTO" lacptimer="30" name="FA-path4" native="" networkType="Fibre Channel" networks="FA4" ports="X1:Auto" preferredPort="" />
                    <lus connectionMode="AUTO" lacptimer="30" name="FA-path1" native="" networkType="Fibre Channel" networks="FA1" ports="1:Auto" preferredPort="" />
                    <lus connectionMode="AUTO" lacptimer="30" name="FA-path2" native="" networkType="Fibre Channel" networks="FA2" ports="1:Auto" preferredPort="" />
                    <lus connectionMode="AUTO" lacptimer="" name="DA-path1" native="" networkType="Fibre Channel" networks="DA1" ports="X2:Auto" preferredPort="" />
                    <lus connectionMode="AUTO" lacptimer="" name="DA-path2" native="" networkType="Fibre Channel" networks="DA2" ports="X2:Auto" preferredPort="" />
                    <lus connectionMode="AUTO" lacptimer="" name="Pub-net" native="dev100" networkType="Ethernet" networks="dev100" ports="bay1:X3" preferredPort="" />
                    <lus connectionMode="AUTO" lacptimer="" name="FO-net" native="dev102-vmmigration" networkType="Ethernet" networks="dev102-vmmigration" ports="bay3:X3" preferredPort="" />
                    <lus connectionMode="AUTO" lacptimer="" name="PXE-net" native="dev300-pxeboot" networkType="Ethernet" networks="dev300-pxeboot" ports="bay2:X3" preferredPort="" />
                </lig>
            </enclosure>
        </enclosures>

    """
    navigate()

    logger.debug("Adding enclosures...")

    count = 0
    total_len = len(enc_obj)
    add_plus = False

    for n, enclosure in enumerate(enc_obj):
        # check if enclosure is existing
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total_len, '-' * 14))
        logger.info("Adding a enclosure with name '{0}'".format(enclosure.name))
        if not C7000VerifyEnclosures.verify_enclosure_not_exist(enclosure.name, fail_if_false=False):
            logger.warn("Enclosure '{0}' already exists".format(enclosure.name))
            continue

        if not add_plus:
            C7000AddEnclosures.click_add_enclosure_button()

        C7000AddEnclosures.wait_add_enclosure_dialog_shown(timeout=8)
        C7000AddEnclosures.input_oa_ip_address_or_host_name(enclosure.oa1hostname)

        if n < total_len - 1:
            add_plus = True
        else:
            add_plus = False

        if enclosure.addas.lower() == "managed":
            _c7000_add_enclosure_as_management(enclosure, add_plus)
        elif enclosure.addas.lower() == "monitored":
            _c7000_add_enclosure_as_monitoring(enclosure, add_plus)
        elif enclosure.addas.lower() == "migrate":
            _c7000_add_enclosure_migrate_virtual_connect_domain(enclosure, add_plus)
        count += 1

    for n, enclosure in enumerate(enc_obj):
        if enclosure.addas.lower() == "migrate":
            navigate()
            FusionUIBase.show_activity_sidebar()
            FusionUIBase.wait_activity_action_ok_or_warn(enclosure.oa1hostname, "VC Migration: Migrate Enclosure", 7200)
            FusionUIBase.show_activity_sidebar()
        # check enclosure status
        # C7000CommonOperationEnclosures.show_activity_sidebar()
        # C7000CommonOperationEnclosures.wait_activity_action_ok(enclosure.name)
        # C7000CommonOperationEnclosures.show_activity_sidebar()
        timeout = int(getattr(enclosure, 'timeout', "1200"))
        C7000CommonOperationEnclosures.wait_enclosure_status_ok_or_warn(enclosure.name, timeout=timeout)
        logger.info("Add enclosure {0} successfully".format(enclosure.name))

    if count == 0:
        logger.warn("No enclosure added!")
        logger.warn("Return Value = False")
        return False

    if count != total_len:
        logger.warn("Not able to add all enclosures!")
        logger.warn("Return Value = False")
        return False

    logger.debug("Return Value = True")
    return True


def _c7000_add_enclosure_as_management(enclosure, add_plus=False):
    """

    :param enclosure:
    """
    C7000AddEnclosures.tick_action_add_enclosure_for_management()

    C7000AddEnclosures.input_user_name(enclosure.oa1username)
    C7000AddEnclosures.input_password(enclosure.oa1password)

    create_new_eg = getattr(enclosure, "create_new_eg", "false").lower() == "true"

    # create new lig & eg
    if create_new_eg is True:
        if hasattr(enclosure, "lig") is False:
            ui_lib.fail_test("lig node not found in enclosure test data")

        lig_obj = enclosure.lig[0] if isinstance(enclosure.lig, list) else enclosure.lig
        # type new eg
        C7000AddEnclosures.select_create_new_enclosure_group()
        C7000AddEnclosures.input_enclosure_group_name(enclosure.encgroup)

        create_new_lig = getattr(lig_obj, "create_new", "false").lower() == "true"
        if create_new_lig is False:
            # use exiting lig
            C7000AddEnclosures.input_logical_interconnect_group(lig_obj.name)
        else:
            if create_new_eg is False:
                # select create new lig
                C7000AddEnclosures.input_logical_interconnect_group("Create new logical interconnect group")
        # choose license
        _select_enclosure_license(enclosure)
        # choose firmware
        _c7000_select_enclosure_firmware(enclosure)
        # click Add button
        if add_plus is False:
            C7000AddEnclosures.click_add_button()
        else:
            C7000AddEnclosures.click_add_plus_button()
        C7000AddEnclosures.wait_verifying_parameters_msg()
        # wait (stage 1, may got "enclosure is claim by another appliance" error message)
        C7000AddEnclosures.wait_adding_enclosure_operation_stage_1(enclosure, add_plus)

        if create_new_lig is True:
            # create lig
            _c7000_create_lig(lig_obj)
    else:
        # use existing eg
        C7000AddEnclosures.input_select_enclosure_group(enclosure.encgroup)
        # choose license
        _select_enclosure_license(enclosure)
        # choose firmware
        _c7000_select_enclosure_firmware(enclosure)
        if add_plus is False:
            C7000AddEnclosures.click_add_button()
        else:
            C7000AddEnclosures.click_add_plus_button()

    # C7000AddEnclosures.wait_adding_enclosure_text_in_dialog()
    # wait (stage 2, may got "enclosure is claim by another appliance" error message)
    timeout = int(getattr(enclosure, "dialog_close_timeout", "200"))
    C7000AddEnclosures.wait_adding_enclosure_operation_stage_2(enclosure, add_plus, timeout)


def _c7000_select_enclosure_firmware(enclosure):
    if getattr(enclosure, "manageFirmware", "false").lower() == "true":
        if getattr(enclosure, "spp", "") != "":
            C7000AddEnclosures.select_firmware_baseline(enclosure.spp)
        if getattr(enclosure, "forceInstall", "false").lower() == "true":
            C7000AddEnclosures.tick_firmware_force_install()


def _c7000_add_enclosure_as_monitoring(enclosure, add_plus=False):
    """

    :param enclosure:
    """
    C7000AddEnclosures.tick_action_add_enclosure_for_monitoring()

    C7000AddEnclosures.input_user_name(enclosure.oa1username)
    C7000AddEnclosures.input_password(enclosure.oa1password)

    if add_plus is False:
        C7000AddEnclosures.click_add_button()
    else:
        C7000AddEnclosures.click_add_plus_button()
    C7000AddEnclosures.wait_adding_enclosure_operation_stage_2(enclosure, add_plus)


def _c7000_add_enclosure_migrate_virtual_connect_domain(enclosure, add_plus=False):
    """

    :param enclosure:
    """
    # tick "Add enclosure and migrate Virtual Connect domain"
    C7000AddEnclosures.tick_action_migrate_virtual_connect_domain()

    # input OA credential
    C7000AddEnclosures.input_user_name(enclosure.oa1username)
    C7000AddEnclosures.input_password(enclosure.oa1password)

    # input enclosure group information
    if getattr(enclosure, "create_new_eg", "false").lower() == "true":
        # create new eg
        C7000AddEnclosures.select_create_new_enclosure_group()
        C7000AddEnclosures.input_enclosure_group_name(enclosure.encgroup)
    else:
        # select existing eg
        C7000AddEnclosures.input_select_enclosure_group(enclosure.encgroup)

    # choose license
    _select_enclosure_license(enclosure)

    # input vcm credential
    C7000AddEnclosures.input_vcm_username(enclosure.vcmusername)
    C7000AddEnclosures.input_vcm_password(enclosure.vcmpassword)

    # click test compatibility
    C7000AddEnclosures.click_test_compatibility_button()

    # waiting for compatibility report
    if C7000AddEnclosures.wait_migrate_report_generation(timeout=120, fail_if_false=False):
        logger.info("The migrate compatibility report has generated")
        if not C7000VerifyEnclosures.verify_migrate_error_text_not_shown(fail_if_false=False):
            ui_lib.fail_test("The migration report have some errors. View the migration report.")
        C7000AddEnclosures.tick_migrate_vc_backup_checkbox(fail_if_false=False)
        C7000AddEnclosures.tick_resources_not_modified_checkbox(fail_if_false=False)
        C7000AddEnclosures.tick_profile_not_migrated_checkbox(fail_if_false=False)
        C7000AddEnclosures.tick_in_service_migration_checkbox(fail_if_false=False)
        C7000AddEnclosures.tick_bios_checkbox(fail_if_false=False)
    else:
        msg = FusionUIBase.get_error_message_from_dialog()
        ui_lib.fail_test(msg)

    # click migrate enclosure
    if add_plus is False:
        C7000AddEnclosures.click_add_button()
    else:
        C7000AddEnclosures.click_add_plus_button()
    C7000AddEnclosures.wait_adding_enclosure_operation_stage_2(enclosure, add_plus)


def _c7000_create_lig(lig):
    operating_mode = getattr(lig, "operating_mode", "false").lower() == "true"

    # if operating_mode is True:
    #     C7000AddEnclosures.tick_edit_lig_operating_mode()

    internal_networks = getattr(lig, "internal_networks", "")
    if internal_networks != "":
        _create_internal_networks(internal_networks)

    for switch_bay in lig.switch:
        bay_no = switch_bay.bay
        bay_type = switch_bay.type

        C7000AddEnclosures.select_bay_type(bay_no, bay_type)

    if hasattr(lig, 'lus'):
        total_lus = len(lig.lus)
        for i, uplink_set in enumerate(lig.lus):
            if i < total_lus - 1:
                _create_uplink_set(uplink_set, add_plus=True)
            else:
                _create_uplink_set(uplink_set)

    C7000AddEnclosures.click_edit_lig_ok_and_add_enclosure_button()
    C7000AddEnclosures.wait_edit_lig_dialog_disappear()


def _create_internal_networks(networks):
    network_list = [item.strip() for item in networks.split(',')]

    if len(network_list) == 0:
        return

    logger.info("configure internal networks")
    C7000AddEnclosures.click_edit_lig_edit_internal_networks_gear()
    C7000AddEnclosures.wait_edit_lig_edit_internal_networks_dialog_shown()
    C7000AddEnclosures.click_edit_lig_edit_internal_networks_add_networks()
    C7000AddEnclosures.wait_edit_lig_edit_internal_networks_add_networks_dialog_shown()

    network_len = len(network_list)
    for i, network in enumerate(network_list):
        C7000AddEnclosures.input_edit_lig_edit_internal_networks_add_networks_search_network(network)
        C7000AddEnclosures.wait_edit_lig_edit_internal_networks_add_networks_table_row_shown(network)
        if i < network_len - 1:
            C7000AddEnclosures.click_edit_lig_edit_internal_networks_add_networks_add_plus()
        else:
            C7000AddEnclosures.click_edit_lig_edit_internal_networks_add_networks_add()
            C7000AddEnclosures.wait_edit_lig_edit_internal_networks_add_networks_dialog_disappear()

    C7000AddEnclosures.click_edit_lig_edit_internal_networks_ok()
    C7000AddEnclosures.wait_edit_lig_edit_internal_networks_dialog_disappear()


def _create_uplink_set(uplink_set, add_plus=False):
    """

    :param uplink_set:
    :param add_plus: True to hit Add button at last otherwise hit Add plus button
    """
    uplink_set_name = uplink_set.name
    uplink_set_type = uplink_set.networkType

    logger.info("create uplink set [ %s ]" % uplink_set_name)

    # choose connection mode, LACP timer for ethernet, tunnel, untagged
    if uplink_set_type == "Ethernet":
        __add_ethernet_uplink_set(uplink_set)
    elif uplink_set_type == "Tunnel":
        __add_tunnel_uplink_set(uplink_set)
    elif uplink_set_type == "Untagged":
        __add_untagged_uplink_set(uplink_set)
    elif uplink_set_type == "Fibre Channel":
        __add_fc_uplink_set(uplink_set)
    else:
        ui_lib.fail_test("Not support creating uplink set type '%s'" % uplink_set_type)

    # hit add button
    if add_plus is False:  # add
        C7000AddEnclosures.click_edit_lig_create_uplink_set_add()
        C7000AddEnclosures.wait_edit_lig_create_uplink_set_dialog_disappear()
    else:  # add plus
        C7000AddEnclosures.click_edit_lig_create_uplink_set_add_plus()


def __open_dialog_and_set_uplink_set_name_and_type(uplink_set):
    uplink_set_name = uplink_set.name
    uplink_set_type = uplink_set.networkType
    if C7000AddEnclosures.wait_edit_lig_create_uplink_set_dialog_shown(fail_if_false=False) is False:
        C7000AddEnclosures.click_edit_lig_add_uplink_set()
    C7000AddEnclosures.wait_edit_lig_create_uplink_set_dialog_shown()
    C7000AddEnclosures.input_edit_lig_create_uplink_set_name(uplink_set_name)
    C7000AddEnclosures.select_edit_lig_create_uplink_set_type(uplink_set_type)


def __set_connection_mode_and_lacp(uplink_set):
    # choose connection mode, LACP timer for ethernet, tunnel, untagged
    # - connection mode
    connection_mode = uplink_set.connectionMode.lower()
    if connection_mode == "auto":
        uplink_set_lacp_timer = uplink_set.lacptimer.lower()
        C7000AddEnclosures.tick_edit_lig_create_uplink_set_connection_mode_automatic()
        if uplink_set_lacp_timer != "":
            C7000AddEnclosures.select_edit_lig_create_uplink_set_lacp_timer(uplink_set_lacp_timer)
    elif connection_mode == "failover":
        C7000AddEnclosures.tick_edit_lig_create_uplink_set_connection_mode_failover()
    else:
        ui_lib.fail_test(
            "Unexpected ethernet connection mode '%s' of uplink set '%s'" % (connection_mode, uplink_set.name))


def __add_uplink_set_fc_network(uplink_set):
    port_list = [item.strip() for item in uplink_set.ports.split(',')]
    if port_list:
        C7000AddEnclosures.click_edit_lig_create_uplink_set_add_uplink_ports()
        C7000AddEnclosures.wait_edit_lig_create_uplink_set_add_uplink_ports_to_dialog_shown()
        logger.info(port_list)
        for i, port_tag in enumerate(port_list):
            bay_no, port_name, port_speed = port_tag.split(':')
            bay_no = bay_no.lower().replace('bay', '')
            C7000AddEnclosures.input_edit_lig_create_uplink_set_add_uplink_ports_to_search_port(port_name)
            C7000AddEnclosures.wait_edit_lig_create_uplink_set_add_uplink_ports_to_table_row_shown(bay_no, port_name)
            C7000AddEnclosures.click_edit_lig_create_uplink_set_add_uplink_ports_to_table_row(bay_no, port_name)
            if i == len(port_list) - 1:
                C7000AddEnclosures.click_edit_lig_create_uplink_set_add_uplink_ports_to_add()
            else:
                C7000AddEnclosures.click_edit_lig_create_uplink_set_add_uplink_ports_to_add_plus()
        C7000AddEnclosures.wait_edit_lig_create_uplink_set_add_uplink_ports_to_dialog_disappear()
    else:
        ui_lib.fail_test("no [ ports ] attribute specified in data file when create uplink set > add uplink ports")


def __add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set):
    port_list = [item.strip() for item in uplink_set.ports.split(',')]
    if port_list:
        C7000AddEnclosures.click_edit_lig_create_uplink_set_add_uplink_ports()
        C7000AddEnclosures.wait_edit_lig_create_uplink_set_add_uplink_ports_to_dialog_shown()
        for i, port_tag in enumerate(port_list):
            bay_no, port_name = port_tag.split(':')
            bay_no = bay_no.lower().replace('bay', '')
            C7000AddEnclosures.input_edit_lig_create_uplink_set_add_uplink_ports_to_search_port(port_name)
            C7000AddEnclosures.wait_edit_lig_create_uplink_set_add_uplink_ports_to_table_row_shown(bay_no, port_name)
            C7000AddEnclosures.click_edit_lig_create_uplink_set_add_uplink_ports_to_table_row(bay_no, port_name)
            if i == len(port_list) - 1:
                C7000AddEnclosures.click_edit_lig_create_uplink_set_add_uplink_ports_to_add()
            else:
                C7000AddEnclosures.click_edit_lig_create_uplink_set_add_uplink_ports_to_add_plus()
        C7000AddEnclosures.wait_edit_lig_create_uplink_set_add_uplink_ports_to_dialog_disappear()
    else:
        ui_lib.fail_test("no [ ports ] attribute specified in data file when create uplink set > add uplink ports")


def __add_ethernet_uplink_set(uplink_set):
    __open_dialog_and_set_uplink_set_name_and_type(uplink_set)
    __set_connection_mode_and_lacp(uplink_set)

    # - networks
    network_list = [item.strip() for item in uplink_set.networks.split(',')]
    if network_list:
        C7000AddEnclosures.click_edit_lig_create_uplink_set_add_networks()
        C7000AddEnclosures.wait_edit_lig_create_uplink_set_add_networks_to_dialog_shown()
        for i, network_name in enumerate(network_list):
            C7000AddEnclosures.input_edit_lig_create_uplink_set_add_networks_to_search_network(network_name)
            C7000AddEnclosures.wait_edit_lig_create_uplink_set_add_networks_to_table_row_shown(network_name)
            if i == len(network_list) - 1:
                C7000AddEnclosures.click_edit_lig_create_uplink_set_add_networks_to_add()
            else:
                C7000AddEnclosures.click_edit_lig_create_uplink_set_add_networks_to_add_plus()
        C7000AddEnclosures.wait_edit_lig_create_uplink_set_add_networks_to_dialog_disappear()
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set> add networks")
    # - choose native network
    native_network = getattr(uplink_set, "native", "")
    if native_network != "":
        C7000AddEnclosures.tick_edit_lig_create_uplink_set_native_network(native_network)

    # - ports
    __add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set)


def __add_tunnel_uplink_set(uplink_set):
    __open_dialog_and_set_uplink_set_name_and_type(uplink_set)
    __set_connection_mode_and_lacp(uplink_set)

    # - networks
    network = uplink_set.networks
    if network != "":
        C7000AddEnclosures.select_edit_lig_create_uplink_set_tunnel_network(network)
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")

    # - ports
    __add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set)


def __add_untagged_uplink_set(uplink_set):
    __open_dialog_and_set_uplink_set_name_and_type(uplink_set)
    __set_connection_mode_and_lacp(uplink_set)

    # - networks
    network = uplink_set.networks
    if network != "":
        C7000AddEnclosures.select_edit_lig_create_uplink_set_untagged_network(network)
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")

    # - ports
    __add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set)


def __add_fc_uplink_set(uplink_set):
    __open_dialog_and_set_uplink_set_name_and_type(uplink_set)

    # - networks
    network = uplink_set.networks
    if network != "":
        C7000AddEnclosures.select_edit_lig_create_uplink_set_fc_network(network)
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")
    # - ports
    port = uplink_set.ports
    __add_uplink_set_fc_network(uplink_set)
    # -- port & port speed
    port_list = [item.strip() for item in port.split(',')]
    for port_and_speed in port_list:
        bay_no, port_name, port_speed = port_and_speed.split(':')
        bay_no = bay_no.replace('bay', '')
        C7000AddEnclosures.select_edit_lig_create_uplink_set_fc_port_speed(bay_no, port_name, port_speed)
# begin - add enclosure


# begin - edit enclosure
def edit_enclosure(enc_obj):
    """ Edit Enclosure (only can edit enclosure name)

    Arguments:
      <enclosure> [1, )
          name*                     --  Name of enclosure as a string.
          new_name*                 --  New enclosure name to change.

    * Required Arguments

    Example:
        data/editenclosures -> @{TestData.editenclosures}
        <editenclosures>
            <enclosure name="wpst32" new_name="wpst32_new"/>
            <enclosure name="wpst32_new" new_name="wpst32"/>
        </editenclosures>

    """
    navigate()

    count = 0
    enclosure_len = len(enc_obj)
    for n, enclosure in enumerate(enc_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(enc_obj), '-' * 14))
        logger.info("Editing a enclosure with name %s" % enclosure.name)
        if not select_enclosure(enclosure.name):
            continue

        C7000EditEnclosures.select_actions_edit()
        C7000EditEnclosures.wait_edit_enclosure_dialog_shown()
        C7000EditEnclosures.input_edit_enclosure_enclosure_name(enclosure.new_name)
        C7000EditEnclosures.click_edit_enclosure_ok()
        C7000EditEnclosures.wait_edit_enclosure_dialog_disappear(20)

        # simple verify
        FusionUIBase.show_activity_sidebar()
        C7000CommonOperationEnclosures.wait_activity_action_ok(enclosure.name, "Update", timeout=60, fail_if_false=False)
        FusionUIBase.show_activity_sidebar()
        C7000VerifyEnclosures.verify_enclosure_exist(enclosure.new_name)

        count += 1

    if count == 0:
        logger.warn("no enclosure edited!")
        logger.warn("Return Value = False")
        return False

    if count != enclosure_len:
        logger.warn("error encounter when edit enclosure")
        logger.warn("Return Value = False")
        return False

    logger.debug("Return Value = True")
    return True
# end - edit enclosure


# begin - reapply configuration
def reapply_enclosure_configuration(enc_obj):
    """ Reapply Ecnlosure Configuration

    Arguments:
      <enclosure> [1, )
          name*                     --  Name of enclosure as a string.

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.enclosures}
        <enclosures>
            <enclosure name="wpst32" />
            <enclosure name="wpst8" />
        </enclosures>

    """
    navigate()

    count = 0
    enclosure_len = len(enc_obj)
    for n, enclosure in enumerate(enc_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(enc_obj), '-' * 14))
        logger.info("Reapply configuration for a enclosure with name %s" % enclosure.name)
        if not select_enclosure(enclosure.name):
            continue

        C7000EnclosuresReapplyConfiguration.select_actions_reapply_configuration()

        # simple verify
        FusionUIBase.show_activity_sidebar()
        C7000CommonOperationEnclosures.wait_activity_action_ok(enclosure.name, "Reapply configuration", timeout=120)
        FusionUIBase.show_activity_sidebar()
        count += 1

    if count == 0:
        logger.warn("no enclosure to be reapplied configuration!")
        logger.warn("Return Value = False")
        return False

    if count != enclosure_len:
        logger.warn("error encounter when reapply enclosure")
        logger.warn("Return Value = False")
        return False

    logger.debug("Return Value = True")
    return True
# end - reapply configuration


# begin - refresh
def refresh_enclosure(enc_obj):
    """ Refresh Enclosure

    Arguments:
      <enclosure> [1, )
          name*                     --  Name of enclosure as a string.

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.enclosures}
        <enclosures>
            <enclosure name="wpst32" />
            <enclosure name="wpst8" />
        </enclosures>

    """
    navigate()

    count = 0
    enclosure_len = len(enc_obj)
    for n, enclosure in enumerate(enc_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(enc_obj), '-' * 14))
        logger.info("Refresh a enclosure with name %s" % enclosure.name)
        if not select_enclosure(enclosure.name):
            continue

        C7000RefreshEnclosures.select_actions_refresh()

        # simple verify
        FusionUIBase.show_activity_sidebar()
        if enclosure.has_property("refresh_time"):
            C7000CommonOperationEnclosures.wait_activity_action_ok(enclosure.name, "Refresh", enclosure.refresh_time)
        else:
            C7000CommonOperationEnclosures.wait_activity_action_ok(enclosure.name, "Refresh")
        FusionUIBase.show_activity_sidebar()
        count += 1

    if count == 0:
        logger.warn("no enclosure to be refreshed!")
        logger.warn("Return Value = False")
        return False

    if count != enclosure_len:
        logger.warn("error encounter when refresh enclosure")
        logger.warn("Return Value = False")
        return False

    logger.debug("Return Value = True")
    return True


def refresh_enclosure_by_name(enclosure_name, wait_for_refresh_complete=True):
    """ Refresh Enclosure by name

    Arguments:
          enclosure_name                --  Name of the enclosure to be refreshed
          wait_for_refresh_complete     -- True/false. Determines weather the function waits for the task completion or not

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.enclosures}
        <enclosures>
            <enclosure name="wpst32" />
            <enclosure name="wpst8" />
        </enclosures>

    """
    navigate()
    logger.info("Refreshing enclosure - %s" % enclosure_name)
    if not select_enclosure(enclosure_name):
        raise AssertionError("Unable to select enclosure {}".format(enclosure_name))

    C7000RefreshEnclosures.select_actions_refresh()
    C7000CommonOperationEnclosures.wait_for_activity_control_new_count(timeout=25)
    logger.warn("DONE")
    # if wait for refresh complete is true - wait and verify else skip
    if str(wait_for_refresh_complete).lower() == 'true':
        wait_for_enclosure_refresh_complete(enclosure_name, FusionEnclosuresPage.TIMEOUT)
    logger.debug("Return Value = True")
    return True


def wait_for_enclosure_refresh_complete(enc_name, waittime=900):
    ''' Function to wait for enclosure refresh to complete. Monitors the activity in aactivity sidebar

    Return Value:
    Raises and assertionerror if the activity is not found or the activity state is error/warning

    Arguments:
        ennc_name         -- name of the enclosure the task has been triggered on
        waittime           -- time in seconds to wait for the task to complete, defaul is 900 seconds

    '''
    navigate()
    if not select_enclosure(enc_name):
        raise AssertionError("Unable to select enclosure {}".format(enc_name))

    logger.debug("waiting for Enclosure Refresh Activity Completion")
    FusionUIBase.show_activity_sidebar(timeout=20)
    if FusionUIBase.wait_activity_action_ok(enc_name, "Refresh", timeout=int(waittime), fail_if_false=False):
        return True
    else:
        raise AssertionError("Enclosure Refresh did not complete successfully")

# end - refresh


# begin - verify enclosure information
def validate_enclosure_configuration(enclosures_obj):
    """ Add Enclosure

    Arguments:
      <enclosure>   [1, )
          name*                     --  In Overview/General view. Name of enclosure as a string.
          state                     --  In Overview/General view. Enclosure state to be verified in Overview/General view. e.g. Configured
          model                     --  In Overview/General view. Enclosure model. e.g. BladeSystem c7000 Enclosure
          logical_enclosure         --  In Overview/General view. Logical enclosure name assocated with this enclosure. e.g. wpst32
          server_licensing_policy   --  In Overview/General view. e.g. HPE OneViewAdvanced
          oa                        --  In Overview view. OA type. e.g. Primary
          primary_oa_host_name      --  In Hardware view. Primary OA host name as string. e.g. wpst32-oa1.vse.rdlabs.hpecorp.net
          primary_oa_ipv4           --  In Hardware view. Primary OA host ipv4 address. e.g. 16.114.209.54
          primary_oa_ipv6           --  In Hardware view. Primary OA host ipv6 address. e.g. none
          location                  --  In Hardware view. Enclosure location.
          powered_by                --  In Hardware view. Which device give power supply for enclosure.
          serial_number             --  In Hardware view. Enclosure serial number.
          part_number               --  In Hardware view. Enclosure part number.
          maximum_power             --  In Hardware view. Enclosure maximum power. e.g. 1785 Watts
          <firmware> [0, 1] optional, for verify firmware information
              <item> [1, )
                type*               --  In Firmware view. Firmware type of bay. Possible value: oa|server|interconnect
                name*               --  In Firmware view. Name of device bay
                component_1         --  In Firmware view. Name of 1st component to be verified. (For server bay, it has 2 components) e.g. Onboard Administrator|iLO4|HP VC FlexFabric 10Gb/24-Port Module
                installed_1         --  In Firmware view. Version number of 1st installed firmware. (For server bay, it has different version number for 2 component)
                component_2         --  In Firmware view. Name of 2nd component to be verified. (For server bay, it has 2 components) e.g. ROM
                installed_2         --  In Firmware view. Version number of 2nd installed firmware. (For server bay, it has different version number for 2 component)
          <devices> [0, 1] optional, for verify device information
              <item> [1, )
                bay*                --  In Devices view. Device bay number as integer.
                status              --  In Devices view. Device by status Possible value: ok|error|unknown. (support regular expression. e.g. /^warning|ok$/i)
                server_hardware     --  In Devices view. Device bay server hardware name.
                model               --  In Devices view. Device bay model.
                server_profile      --  In Devices view. Server profile associated with this device.
          <interconnects> [0, 1] optional, for verify interconnect information
              <item> [1, )
                bay*                --  In Interconnects view. Interconnect bay number as integer.
                status              --  In Interconnects view. Interconnect bay status. Possible value: ok|error|unknown. (support regular expression. e.g. /^warning|ok$/i)
                interconnect        --  In Interconnects view. Interconnect bay name.
                installed_module    --  In Interconnects view. Module name of installed interconnect
          <power_supplies> [0, 1] optional, for verify power supplies device
              <item> [1, )
                bay*                --  In Power Supplies view. Power supply bay number as integer.
                status              --  In Power Supplies view. Power supply bay status. Possible value: ok|error|unknown. (support regular expression. e.g. /^warning|ok$/i)
                model               --  In Power Supplies view. Power supply bay model.
                serial_number       --  In Power Supplies view. Power supply bay serial number.
                part_number         --  In Power Supplies view. Power supply bay part number.
                spare_part_number   --  In Power Supplies view. Power supply bay spare part number.
          <fans> [0, 1] optional, for verify fan device
              fans_required         --  In Fans view. e.g. 10 (all fan bays)
              device_bays_cooled    --  In Fans view. e.g. All
              <item> [1, )
                bay*                --  In Fans view. Fan bay number as integer.
                status              --  In Fans view. Fan bay status. Possible value: ok|error|unknown. (support regular expression. e.g. /^warning|ok$/i)
                model               --  In Fans view. Fan model name.
                state               --  In Fans view. Fan bay state. e.g. OK
                required            --  In Fans view. Fan bay required attribute. E.g. Yes|No
                part_number         --  In Fans view. Fan bay part number
                spare_part_number   --  In Fans view. Fan bay spare part number

    * Required Arguments

    Example:
        data/enclosure -> @{TestData.verifyenclosures}
        <verifyenclosures>
            <enclosure name="wpst32"
                       state="Configured"
                       model="BladeSystem c7000 Enclosure"
                       logical_enclosure="wpst32"
                       server_licensing_policy="HPE OneViewAdvanced"
                       oa="Primary"
                       primary_oa_host_name="wpst32-oa1.vse.rdlabs.hpecorp.net"
                       primary_oa_ipv4="16.114.209.54"
                       primary_oa_ipv6="none"
                       location="x497s-ExDS-RACK"
                       powered_by="none"
                       serial_number="USE7224LTV"
                       part_number="412152-B21"
                       maximum_power="1785">
                <firmware>
                    <item type="oa" name="wpst32, OA 1" component_1="Onboard Administrator" installed_1="4.31"/>
                    <item type="server" name="wpst32, bay 1" component_1="iLO4" installed_1="2.03" component_2="ROM" installed_2="I31 02/10/2014" />
                    <item type="server" name="wpst32, bay 2" component_1="iLO4" installed_1="1.51" component_2="ROM" installed_2="I31 02/10/2014" />
                    <item type="server" name="wpst32, bay 3" component_1="iLO4" installed_1="2.02" component_2="ROM" installed_2="I31 02/10/2014" />
                    <item type="server" name="wpst32, bay 4" component_1="iLO4" installed_1="1.51" component_2="ROM" installed_2="I31 02/10/2014" />
                    <item type="server" name="wpst32, bay 5" component_1="iLO4" installed_1="2.20" component_2="ROM" installed_2="I36 11/03/2014" />
                    <item type="interconnect" name="wpst32, interconnect 1" component_1="HP VC FlexFabric 10Gb/24-Port Module" installed_1="4.30" />
                    <item type="interconnect" name="wpst32, interconnect 2" component_1="HP VC FlexFabric 10Gb/24-Port Module" installed_1="4.30" />
                    <item type="interconnect" name="wpst32, interconnect 3" component_1="HP VC FlexFabric 10Gb/24-Port Module" installed_1="4.30" />
                    <item type="interconnect" name="wpst32, interconnect 4" component_1="HP VC FlexFabric 10Gb/24-Port Module" installed_1="4.30" />
                    <item type="interconnect" name="wpst32, interconnect 5" component_1="HP VC 8Gb 20-Port FC Module" installed_1="2.02" />
                    <item type="interconnect" name="wpst32, interconnect 6" component_1="HP VC 8Gb 20-Port FC Module" installed_1="2.02" />
                    <item type="interconnect" name="wpst32, interconnect 7" component_1="HP 4Gb Fibre Channel Pass-thru Module for c-Class BladeSystem" installed_1="unknown" />
                    <item type="interconnect" name="wpst32, interconnect 8" component_1="HP 4Gb Fibre Channel Pass-thru Module for c-Class BladeSystem" installed_1="unknown" />
                </firmware>
                <devices>
                    <!--just for testing, so set status to 'error'-->
                    <item bay="1" status="error" server_hardware="wpst32, bay 1" model="ProLiant BL460c Gen8" server_profile="none"/>
                    <item bay="2" status="error" server_hardware="wpst32, bay 2" model="ProLiant BL460c Gen8" server_profile="none"/>
                    <item bay="3" status="error" server_hardware="wpst32, bay 3" model="ProLiant BL460c Gen8" server_profile="none"/>
                    <item bay="4" status="error" server_hardware="wpst32, bay 4" model="ProLiant BL460c Gen8" server_profile="none"/>
                    <item bay="5" status="error" server_hardware="wpst32, bay 5" model="ProLiant BL460c Gen9" server_profile="none"/>
                    <item bay="6" server_hardware="empty" />
                    <item bay="7" server_hardware="empty" />
                    <item bay="8" server_hardware="empty" />
                    <item bay="9" server_hardware="empty" />
                    <item bay="10" server_hardware="empty" />
                    <item bay="11" server_hardware="empty" />
                    <item bay="12" server_hardware="empty" />
                    <item bay="13" server_hardware="empty" />
                    <item bay="14" server_hardware="empty" />
                    <item bay="15" server_hardware="empty" />
                    <item bay="16" server_hardware="empty" />
                </devices>
                <interconnects>
                    <item bay="1" status="ok" interconnect="wpst32, interconnect 1" installed_module="HP VC FlexFabric 10Gb/24-Port Module" />
                    <item bay="2" status="ok" interconnect="wpst32, interconnect 2" installed_module="HP VC FlexFabric 10Gb/24-Port Module" />
                    <item bay="3" status="ok" interconnect="wpst32, interconnect 3" installed_module="HP VC FlexFabric 10Gb/24-Port Module" />
                    <item bay="4" status="ok" interconnect="wpst32, interconnect 4" installed_module="HP VC FlexFabric 10Gb/24-Port Module" />
                    <item bay="5" status="ok" interconnect="wpst32, interconnect 5" installed_module="HP VC 8Gb 20-Port FC Module" />
                    <item bay="6" status="ok" interconnect="wpst32, interconnect 6" installed_module="HP VC 8Gb 20-Port FC Module" />
                    <item bay="7" status="unknown" interconnect="wpst32, interconnect 7" installed_module="HP 4Gb Fibre Channel Pass-thru Module for c-Class BladeSystem" />
                    <item bay="8" status="unknown" interconnect="wpst32, interconnect 8" installed_module="HP 4Gb Fibre Channel Pass-thru Module for c-Class BladeSystem" />
                </interconnects>
                <power_supplies>
                    <item bay="1" status="ok" model="HP BladeSystem c-Class P/S" serial_number="5A22B0EHLV02TR" part_number="412138-B21" spare_part_number="411099-001" />
                    <item bay="2" model="empty" />
                    <item bay="3" model="empty" />
                    <item bay="4" model="empty" />
                    <item bay="5" model="empty" />
                    <item bay="6" status="ok" model="HP BladeSystem c-Class P/S" serial_number="5A22B0EHLVR06Z" part_number="412138-B21" spare_part_number="411099-001" />
                </power_supplies>
                <fans fans_required="10 (all fan bays)" device_bays_cooled="All">
                    <item bay="1" status="ok" model="Active Cool 200 Fan" state="OK" required="Yes" part_number="412140-B21" spare_part_number="413996-001" />
                    <item bay="2" status="ok" model="Active Cool 200 Fan" state="OK" required="Yes" part_number="412140-B21" spare_part_number="413996-001" />
                    <item bay="3" status="ok" model="Active Cool 200 Fan" state="OK" required="Yes" part_number="412140-B21" spare_part_number="413996-001" />
                    <item bay="4" status="ok" model="Active Cool 200 Fan" state="OK" required="Yes" part_number="412140-B21" spare_part_number="413996-001" />
                    <item bay="5" status="ok" model="Active Cool 200 Fan" state="OK" required="Yes" part_number="412140-B21" spare_part_number="413996-001" />
                    <item bay="6" status="ok" model="Active Cool 200 Fan" state="OK" required="Yes" part_number="412140-B21" spare_part_number="413996-001" />
                    <item bay="7" status="ok" model="Active Cool 200 Fan" state="OK" required="Yes" part_number="412140-B21" spare_part_number="413996-001" />
                    <item bay="8" status="ok" model="Active Cool 200 Fan" state="OK" required="Yes" part_number="412140-B21" spare_part_number="413996-001" />
                    <item bay="9" status="ok" model="Active Cool 200 Fan" state="OK" required="Yes" part_number="412140-B21" spare_part_number="413996-001" />
                    <item bay="10" status="ok" model="Active Cool 200 Fan" state="OK" required="Yes" part_number="412140-B21" spare_part_number="413996-001" />
                </fans>
            </enclosure>
        </verifyenclosures>

    """
    navigate()

    count = 0
    ret = True
    for n, enc_obj in enumerate(enclosures_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(enclosures_obj), '-' * 14))
        logger.info("Verifying a enclosure with name %s" % enc_obj.name)
        if not select_enclosure(enc_obj.name):
            continue

        # overview
        FusionUIBase.select_view_by_name('Overview')
        logger.info("Verifying configuration in Overview view...")
        if hasattr(enc_obj, 'state'):
            C7000VerifyEnclosures.verify_overview_general_state(enc_obj.state)

        if hasattr(enc_obj, 'model'):
            C7000VerifyEnclosures.verify_overview_general_model(enc_obj.model)

        if hasattr(enc_obj, 'logical_enclosure'):
            C7000VerifyEnclosures.verify_overview_general_logical_enclosure(enc_obj.logical_enclosure)

        if hasattr(enc_obj, 'server_licensing_policy'):
            C7000VerifyEnclosures.verify_overview_general_server_licensing_policy(enc_obj.server_licensing_policy)

        if hasattr(enc_obj, 'oa'):
            C7000VerifyEnclosures.verify_overview_hardware_oa(enc_obj.oa)

        if hasattr(enc_obj, 'location'):
            C7000VerifyEnclosures.verify_overview_hardware_location(enc_obj.location)

        if hasattr(enc_obj, 'powered_by'):
            C7000VerifyEnclosures.verify_overview_hardware_powered_by(enc_obj.powered_by)

        if hasattr(enc_obj, 'serial_number'):
            C7000VerifyEnclosures.verify_overview_hardware_serial_number(enc_obj.serial_number)

        # general
        FusionUIBase.select_view_by_name('General')
        logger.info("Verifying configuration in General view...")
        if hasattr(enc_obj, 'state'):
            C7000VerifyEnclosures.verify_general_state(enc_obj.state)

        if hasattr(enc_obj, 'model'):
            C7000VerifyEnclosures.verify_general_model(enc_obj.model)

        if hasattr(enc_obj, 'logical_enclosure'):
            C7000VerifyEnclosures.verify_general_logical_enclosure(enc_obj.logical_enclosure)

        if hasattr(enc_obj, 'server_licensing_policy'):
            C7000VerifyEnclosures.verify_general_server_licensing_policy(enc_obj.server_licensing_policy)

        FusionUIBase.select_view_by_name('Hardware')
        logger.info("Verifying Enclosure configuration in Hardware view...")
        if hasattr(enc_obj, 'primary_oa_host_name'):
            C7000VerifyEnclosures.verify_hardware_primary_oa_host_name(enc_obj.primary_oa_host_name)

        if hasattr(enc_obj, 'primary_oa_ipv4'):
            C7000VerifyEnclosures.verify_hardware_primary_oa_ipv4(enc_obj.primary_oa_ipv4)

        if hasattr(enc_obj, 'primary_oa_ipv6'):
            C7000VerifyEnclosures.verify_hardware_primary_oa_ipv6(enc_obj.primary_oa_ipv6)

        if hasattr(enc_obj, 'location'):
            C7000VerifyEnclosures.verify_hardware_location(enc_obj.location)

        if hasattr(enc_obj, 'powered_by'):
            C7000VerifyEnclosures.verify_hardware_powered_by(enc_obj.powered_by)

        if hasattr(enc_obj, 'serial_number'):
            C7000VerifyEnclosures.verify_hardware_serial_number(enc_obj.serial_number)

        if hasattr(enc_obj, 'part_number'):
            C7000VerifyEnclosures.verify_hardware_part_number(enc_obj.part_number)

        if hasattr(enc_obj, 'maximum_power'):
            C7000VerifyEnclosures.verify_hardware_maximum_power(enc_obj.maximum_power)

        # firmware
        if hasattr(enc_obj, 'firmware'):
            FusionUIBase.select_view_by_name('Firmware')
            logger.info("Verifying configuration in Firmware view...")
            for firmware_obj in enc_obj.firmware:
                C7000VerifyEnclosures.verify_firmware_row_exist(firmware_obj.name)
                if hasattr(firmware_obj, 'component_1'):
                    C7000VerifyEnclosures.verify_firmware_component_1(firmware_obj.name, firmware_obj.component_1)

                if hasattr(firmware_obj, 'installed_1'):
                    C7000VerifyEnclosures.verify_firmware_installed_1(firmware_obj.name, firmware_obj.installed_1)

                if firmware_obj.type == 'interconnect' and firmware_obj.type == 'server':
                    if hasattr(firmware_obj, 'component_2'):
                        C7000VerifyEnclosures.verify_firmware_component_2(firmware_obj.name, firmware_obj.component_2)

                    if hasattr(firmware_obj, 'installed_2'):
                        C7000VerifyEnclosures.verify_firmware_installed_2(firmware_obj.name, firmware_obj.installed_2)

        # device
        if hasattr(enc_obj, 'devices'):
            FusionUIBase.select_view_by_name('Devices')
            logger.info("Verifying configuration in Devices view...")

            for device_obj in enc_obj.devices:
                C7000VerifyEnclosures.verify_device_bay_exist(device_obj.bay)
                if hasattr(device_obj, 'status'):
                    C7000VerifyEnclosures.verify_device_status(device_obj.bay, device_obj.status)

                if hasattr(device_obj, 'server_hardware'):
                    C7000VerifyEnclosures.verify_device_server_hardware(device_obj.bay, device_obj.server_hardware)

                if hasattr(device_obj, 'model'):
                    C7000VerifyEnclosures.verify_device_model(device_obj.bay, device_obj.model)

                if hasattr(device_obj, 'server_profile'):
                    C7000VerifyEnclosures.verify_device_server_profile(device_obj.bay, device_obj.server_profile)

        # interconnect
        if hasattr(enc_obj, 'interconnects'):
            FusionUIBase.select_view_by_name('Interconnects')
            logger.info("Verifying configuration in Interconnects view...")
            for interconnect_obj in enc_obj.interconnects:
                C7000VerifyEnclosures.verify_interconnect_bay_exist(interconnect_obj.bay)
                if hasattr(interconnect_obj, 'status'):
                    C7000VerifyEnclosures.verify_interconnect_status(interconnect_obj.bay, interconnect_obj.status)

                if hasattr(interconnect_obj, 'interconnect'):
                    C7000VerifyEnclosures.verify_interconnect_interconnect(interconnect_obj.bay, interconnect_obj.interconnect)

                if hasattr(interconnect_obj, 'installed_module'):
                    C7000VerifyEnclosures.verify_interconnect_installed_module(interconnect_obj.bay, interconnect_obj.installed_module)

        # power supply
        if hasattr(enc_obj, 'power_supplies'):
            FusionUIBase.select_view_by_name('Power Supplies')
            logger.info("Verifying configuration in Power Supplies view...")
            for power_supply_obj in enc_obj.power_supplies:
                C7000VerifyEnclosures.verify_power_supply_bay_exist(power_supply_obj.bay)
                if hasattr(power_supply_obj, 'status'):
                    C7000VerifyEnclosures.verify_power_supply_status(power_supply_obj.bay, power_supply_obj.status)

                if hasattr(power_supply_obj, 'model'):
                    C7000VerifyEnclosures.verify_power_supply_model(power_supply_obj.bay, power_supply_obj.model)

                if hasattr(power_supply_obj, 'serial_number'):
                    C7000VerifyEnclosures.verify_power_supply_serial_number(power_supply_obj.bay, power_supply_obj.serial_number)

                if hasattr(power_supply_obj, 'part_number'):
                    C7000VerifyEnclosures.verify_power_supply_part_number(power_supply_obj.bay, power_supply_obj.part_number)

                if hasattr(power_supply_obj, 'spare_part_number'):
                    C7000VerifyEnclosures.verify_power_supply_spare_part_number(power_supply_obj.bay, power_supply_obj.spare_part_number)

        # fan
        if hasattr(enc_obj, 'fans'):
            FusionUIBase.select_view_by_name('Fans')
            logger.info("Verifying configuration in Fans view...")

            if hasattr(enc_obj.fans, 'fans_required'):
                C7000VerifyEnclosures.verify_fan_fans_required(enc_obj.fans.fans_required)

            if hasattr(enc_obj.fans, 'device_bays_cooled'):
                C7000VerifyEnclosures.verify_fan_device_bays_cooled(enc_obj.fans.device_bays_cooled)

            obj_list = enc_obj.fans.item if hasattr(enc_obj.fans, 'item') else enc_obj.fans

            for fan_obj in obj_list:
                C7000VerifyEnclosures.verify_fan_bay_exist(fan_obj.bay)
                if hasattr(fan_obj, 'status'):
                    C7000VerifyEnclosures.verify_fan_status(fan_obj.bay, fan_obj.status)

                if hasattr(fan_obj, 'model'):
                    C7000VerifyEnclosures.verify_fan_model(fan_obj.bay, fan_obj.model)

                if hasattr(fan_obj, 'state'):
                    C7000VerifyEnclosures.verify_fan_status(fan_obj.bay, fan_obj.state)

                if hasattr(fan_obj, 'required'):
                    C7000VerifyEnclosures.verify_fan_required(fan_obj.bay, fan_obj.required)

                if hasattr(fan_obj, 'part_number'):
                    C7000VerifyEnclosures.verify_fan_part_number(fan_obj.bay, fan_obj.part_number)

                if hasattr(fan_obj, 'spare_part_number'):
                    C7000VerifyEnclosures.verify_fan_spare_part_number(fan_obj.bay, fan_obj.spare_part_number)

        count += 1

    if count == 0:
        msg = "no target enclosure exists!"
        logger.warn(msg)
        logger.warn("Return Value = False")
        return False

    if count != len(enclosures_obj):
        logger.warn("Not able to verify all enclosure!")
        logger.warn("Return Value = False")
        return False

    logger.debug("Return Value = True")
    return ret
# end - verify enclosure information


# begin - verify tbrid enclosure information
def validate_tbird_enclosure_configuration(enclosures_obj):
    """ Validate tbird enclosure configuration

    Arguments:
      <enclosure> [1, )
          name*                     --  In Overview/General view. Name of enclosure as a string.
          state                     --  In Overview/General view. Enclosure state to be verified in Overview/General view. e.g. Configured
          model                     --  In Overview/General view. Enclosure model. e.g. BladeSystem c7000 Enclosure
          logical_enclosure         --  In Overview/General view. Logical enclosure name assocated with this enclosure. e.g. wpst32
          location                  --  In Hardware view. Enclosure location.
          powered_by                --  In Hardware view. Which device give power supply for enclosure.
          serial_number             --  In Hardware view. Enclosure serial number.
          part_number               --  In Hardware view. Enclosure part number.
          maximum_power             --  In Hardware view. Enclosure maximum power. e.g. 1785 Watts
          <devices> [0, 1] optional, for verify device information
              <item> [1, )
                bay*                --  In Devices view. Device bay number as integer.
                status              --  In Devices view. Device by status Possible value: ok|error|unknown. (support regular expression. e.g. /^warning|ok$/i)
                server_hardware     --  In Devices view. Device bay server hardware name.
                model               --  In Devices view. Device bay model.
                server_profile      --  In Devices view. Server profile associated with this device.
          <interconnects> [0, 1] optional, for verify interconnect information
              <item> [1, )
                bay*                --  In Interconnects view. Interconnect bay number as integer.
                status              --  In Interconnects view. Interconnect bay status. Possible value: ok|error|unknown. (support regular expression. e.g. /^warning|ok$/i)
                interconnect        --  In Interconnects view. Interconnect bay name.
                installed_module    --  In Interconnects view. Module name of installed interconnect
          <power_supplies> [0, 1] optional, for verify power supplies device
              <item> [1, )
                bay*                --  In Power Supplies view. Power supply bay number as integer.
                status              --  In Power Supplies view. Power supply bay status. Possible value: ok|error|unknown. (support regular expression. e.g. /^warning|ok$/i)
                model               --  In Power Supplies view. Power supply bay model.
                serial_number       --  In Power Supplies view. Power supply bay serial number.
                part_number         --  In Power Supplies view. Power supply bay part number.
                spare_part_number   --  In Power Supplies view. Power supply bay spare part number.
          <fans> [0, 1] optional, for verify fan device
              <item> [1, )
                bay*                --  In Fans view. Fan bay number as integer.
                status              --  In Fans view. Fan bay status. Possible value: ok|error|unknown. (support regular expression. e.g. /^warning|ok$/i)
                model               --  In Fans view. Fan model name.
                serial_number       --  In Fans view. Fan bay serial number.
                part_number         --  In Fans view. Fan bay part number
                spare_part_number   --  In Fans view. Fan bay spare part number
          <cim> [0, 1] optional, for verify cim device
              <item> [1, )
                bay*                --  In Composable Infrastructure Appliances view. cim bay number as integer.
                status              --  In Composable Infrastructure Appliances view. cim bay status. Possible value: ok|error|unknown. (support regular expression. e.g. /^warning|ok$/i)
                model               --  In Composable Infrastructure Appliances view. cim model name.
                power               --  In Composable Infrastructure Appliances view. cim bay power.
                serial_number       --  In Composable Infrastructure Appliances view. cim bay serial number.
                part_number         --  In Composable Infrastructure Appliances view. cim bay part number
                spare_part_number   --  In Composable Infrastructure Appliances view. cim bay spare part number
          <link_modules> [0, 1] optional, for verify link modules device
              <item> [1, )
                bay*                --  In Link Modules view. Fan bay number as integer.
                status              --  In Link Modules view. Fan bay status. Possible value: ok|error|unknown. (support regular expression. e.g. /^warning|ok$/i)
                model               --  In Link Modules view. Fan model name.
                state               --  In Link Modules view. Link module bay state. Possible value: standby|active
                mgmt_port_state     --  In Link Modules view. Link module bay MGMT Port State. Possible value: active|standby
                link_port_state     --  In Link Modules view. Link module bay LINK Port State. e.g. linked to CN744502F1, link module 2

    * Required Arguments

    Example:
        data/enclosure -> @{TestData.verifyenclosures}
        <verifyenclosures>
            <enclosure name="CN744502F8"
                       state="Monitored"
                       model="Synergy 12000 Frame"
                       logical_enclosure="Create logical enclosure"
                       location="none"
                       powered_by="none"
                       serial_number="CN744502F8"
                       part_number="000000-010"
                       maximum_power="2233">
                <devices>
                    <item bay="1" status="/^warning|ok|error$/i" server_hardware="CN744502F8, bay 1" model="Synergy 480 Gen9" server_profile="none"/>
                    <item bay="2" status="/^warning|ok|error$/i" server_hardware="CN744502F8, bay 2" model="Synergy 480 Gen9" server_profile="none"/>
                    <item bay="3" status="/^warning|ok|error$/i" server_hardware="CN744502F8, bay 3" model="Synergy 480 Gen9" server_profile="none"/>
                    <item bay="4" status="/^warning|ok|error$/i" server_hardware="CN744502F8, bay 4" model="Synergy 480 Gen9" server_profile="none"/>
                </devices>
                <interconnects>
                    <item bay="3" status="/^warning|ok|error$/i" interconnect="CN744502F8, interconnect 3" installed_module="HP VC SE 40Gb F8 Module" />
                    <item bay="6" status="/^warning|ok|error$/i" interconnect="CN744502F8, interconnect 6" installed_module="HP VC SE 40Gb F8 Module" />
                </interconnects>
                <power_supplies>
                    <item bay="1" status="ok" model="2650W AC Titanium Hot Plug Power Supply" serial_number="5EGGNV14D7K0HH" part_number="765878-B21" spare_part_number="TO-BE-DETERMINED" output_capacity="2650" />
                    <item bay="2" status="ok" model="2650W AC Titanium Hot Plug Power Supply" serial_number="5EGGNV14D7K0GY" part_number="765878-B21" spare_part_number="TO-BE-DETERMINED" output_capacity="2650" />
                    <item bay="3" status="ok" model="2650W AC Titanium Hot Plug Power Supply" serial_number="5EGGNV14D7K0HR" part_number="765878-B21" spare_part_number="TO-BE-DETERMINED" output_capacity="2650" />
                    <item bay="4" status="ok" model="2650W AC Titanium Hot Plug Power Supply" serial_number="5EGGNV14D7K0GQ" part_number="765878-B21" spare_part_number="TO-BE-DETERMINED" output_capacity="2650" />
                    <item bay="5" status="ok" model="2650W AC Titanium Hot Plug Power Supply" serial_number="5EGGNV14D7K0GH" part_number="765878-B21" spare_part_number="TO-BE-DETERMINED" output_capacity="2650" />
                    <item bay="6" status="ok" model="2650W AC Titanium Hot Plug Power Supply" serial_number="5EGGNV14D7K0HS" part_number="765878-B21" spare_part_number="TO-BE-DETERMINED" output_capacity="2650" />
                </power_supplies>
                <fans>
                    <item bay="1" status="ok" model="Synergy Fan Module" serial_number="TBS9P5QL8C" part_number="809097-001" spare_part_number="807967-001" />
                    <item bay="2" status="ok" model="Synergy Fan Module" serial_number="GQ7M8M6692" part_number="809097-001" spare_part_number="807967-001" />
                    <item bay="3" status="ok" model="Synergy Fan Module" serial_number="M56FTZVT0Z" part_number="809097-001" spare_part_number="807967-001" />
                    <item bay="4" status="ok" model="Synergy Fan Module" serial_number="YDJ9O5RW6A" part_number="809097-001" spare_part_number="807967-001" />
                    <item bay="5" status="ok" model="Synergy Fan Module" serial_number="WLN7EZH973" part_number="809097-001" spare_part_number="807967-001" />
                    <item bay="6" status="ok" model="Synergy Fan Module" serial_number="4EP90QO6D1" part_number="809097-001" spare_part_number="807967-001" />
                    <item bay="7" status="ok" model="Synergy Fan Module" serial_number="4Q3G52M0W0" part_number="809097-001" spare_part_number="807967-001" />
                    <item bay="8" status="ok" model="Synergy Fan Module" serial_number="Z87J00N7F5" part_number="809097-001" spare_part_number="807967-001" />
                    <item bay="9" status="ok" model="Synergy Fan Module" serial_number="1FU4A1LLOO" part_number="809097-001" spare_part_number="807967-001" />
                    <item bay="10" status="ok" model="Synergy Fan Module" serial_number="Q6WTNRYF2C" part_number="809097-001" spare_part_number="807967-001" />
                </fans>
                <cim>
                    <item bay="1" status="ok" model="Synergy Composer" power="" serial_number="UH4ACP0196" part_number="804353-B21" spare_part_number="807964-001"/>
                </cim>
                <link_modules>
                    <item bay="1" status="ok" model="Synergy Frame Link Module" state="active" mgmt_port_state="active" link_port_state="linked to CN744502F1, link module 2" />
                    <item bay="2" status="standby" model="Synergy Frame Link Module" state="active" mgmt_port_state="disabled" link_port_state="linked to CN744502G1, link module 1" />
                </link_modules>
            </enclosure>
        </verifyenclosures>

    """
    navigate()

    count = 0
    for n, enc_obj in enumerate(enclosures_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(enclosures_obj), '-' * 14))
        logger.info("Verifying a enclosure with name %s" % enc_obj.name)
        if not select_enclosure(enc_obj.name):
            continue

        # overview
        FusionUIBase.select_view_by_name('Overview')
        logger.info("Verifying configuration in Overview view...")
        if hasattr(enc_obj, 'state'):
            TBirdVerifyEnclosures.verify_overview_general_state(enc_obj.state)

        if hasattr(enc_obj, 'model'):
            TBirdVerifyEnclosures.verify_overview_general_model(enc_obj.model)

        if hasattr(enc_obj, 'logical_enclosure'):
            TBirdVerifyEnclosures.verify_overview_general_logical_enclosure(enc_obj.logical_enclosure)

        if hasattr(enc_obj, 'location'):
            TBirdVerifyEnclosures.verify_overview_hardware_location(enc_obj.location)

        if hasattr(enc_obj, 'powered_by'):
            TBirdVerifyEnclosures.verify_overview_hardware_powered_by(enc_obj.powered_by)

        if hasattr(enc_obj, 'serial_number'):
            TBirdVerifyEnclosures.verify_overview_hardware_serial_number(enc_obj.serial_number)

        if hasattr(enc_obj, 'interconnects'):
            for ic_obj in enc_obj.interconnects:
                TBirdVerifyEnclosures.verify_overview_rear_view_interconnect_name(ic_obj.interconnect)
                TBirdVerifyEnclosures.verify_overview_rear_view_interconnect_model(ic_obj.interconnect, ic_obj.installed_module)
                TBirdVerifyEnclosures.verify_overview_rear_view_interconnect_bay(ic_obj.bay, ic_obj.interconnect)
                TBirdVerifyEnclosures.verify_overview_rear_view_interconnect_status(ic_obj.interconnect, ic_obj.status)

        # general
        FusionUIBase.select_view_by_name('General')
        logger.info("Verifying configuration in General view...")
        if hasattr(enc_obj, 'state'):
            TBirdVerifyEnclosures.verify_general_state(enc_obj.state)

        if hasattr(enc_obj, 'model'):
            TBirdVerifyEnclosures.verify_general_model(enc_obj.model)

        if hasattr(enc_obj, 'logical_enclosure'):
            TBirdVerifyEnclosures.verify_general_logical_enclosure(enc_obj.logical_enclosure)

        FusionUIBase.select_view_by_name('Hardware')
        logger.info("Verifying Enclosure configuration in Hardware view...")

        if hasattr(enc_obj, 'location'):
            TBirdVerifyEnclosures.verify_hardware_location(enc_obj.location)

        if hasattr(enc_obj, 'powered_by'):
            TBirdVerifyEnclosures.verify_hardware_powered_by(enc_obj.powered_by)

        if hasattr(enc_obj, 'serial_number'):
            TBirdVerifyEnclosures.verify_hardware_serial_number(enc_obj.serial_number)

        if hasattr(enc_obj, 'part_number'):
            TBirdVerifyEnclosures.verify_hardware_part_number(enc_obj.part_number)

        if hasattr(enc_obj, 'maximum_power'):
            TBirdVerifyEnclosures.verify_hardware_maximum_power(enc_obj.maximum_power)

        # TODO: firmware
        # if hasattr(enc_obj, 'firmware'):
        #     FusionUIBase.select_view_by_name('Firmware')
        #     logger.info("Verifying configuration in Firmware view...")
        #     for firmware_obj in enc_obj.firmware:
        #         C7000VerifyEnclosures.verify_firmware_row_exist(firmware_obj.name)
        #         if hasattr(firmware_obj, 'component_1'):
        #             C7000VerifyEnclosures.verify_firmware_component_1(firmware_obj.name, firmware_obj.component_1)
        #
        #         if hasattr(firmware_obj, 'installed_1'):
        #             C7000VerifyEnclosures.verify_firmware_installed_1(firmware_obj.name, firmware_obj.installed_1)
        #
        #         if firmware_obj.type == 'interconnect' and firmware_obj.type == 'server':
        #             if hasattr(firmware_obj, 'component_2'):
        #                 C7000VerifyEnclosures.verify_firmware_component_2(firmware_obj.name, firmware_obj.component_2)
        #
        #             if hasattr(firmware_obj, 'installed_2'):
        #                 C7000VerifyEnclosures.verify_firmware_installed_2(firmware_obj.name, firmware_obj.installed_2)

        # device
        if hasattr(enc_obj, 'devices'):
            FusionUIBase.select_view_by_name('Devices')
            logger.info("Verifying configuration in Devices view...")

            for device_obj in enc_obj.devices:
                TBirdVerifyEnclosures.verify_device_bay_exist(device_obj.bay)
                if hasattr(device_obj, 'status'):
                    TBirdVerifyEnclosures.verify_device_status(device_obj.bay, device_obj.status)

                if hasattr(device_obj, 'server_hardware'):
                    TBirdVerifyEnclosures.verify_device_server_hardware(device_obj.bay, device_obj.server_hardware)

                if hasattr(device_obj, 'model'):
                    TBirdVerifyEnclosures.verify_device_model(device_obj.bay, device_obj.model)

                if hasattr(device_obj, 'server_profile'):
                    TBirdVerifyEnclosures.verify_device_server_profile(device_obj.bay, device_obj.server_profile)

        # interconnect
        if hasattr(enc_obj, 'interconnects'):
            FusionUIBase.select_view_by_name('Interconnects')
            logger.info("Verifying configuration in Interconnects view...")
            for interconnect_obj in enc_obj.interconnects:
                TBirdVerifyEnclosures.verify_interconnect_bay_exist(interconnect_obj.bay)
                if hasattr(interconnect_obj, 'status'):
                    TBirdVerifyEnclosures.verify_interconnect_status(interconnect_obj.bay, interconnect_obj.status)

                if hasattr(interconnect_obj, 'interconnect'):
                    TBirdVerifyEnclosures.verify_interconnect_interconnect(interconnect_obj.bay, interconnect_obj.interconnect)

                if hasattr(interconnect_obj, 'installed_module'):
                    TBirdVerifyEnclosures.verify_interconnect_installed_module(interconnect_obj.bay, interconnect_obj.installed_module)

        # power supply
        if hasattr(enc_obj, 'power_supplies'):
            FusionUIBase.select_view_by_name('Power Supplies')
            logger.info("Verifying configuration in Power Supplies view...")
            for power_supply_obj in enc_obj.power_supplies:
                TBirdVerifyEnclosures.verify_power_supply_bay_exist(power_supply_obj.bay)
                if hasattr(power_supply_obj, 'status'):
                    TBirdVerifyEnclosures.verify_power_supply_status(power_supply_obj.bay, power_supply_obj.status)

                if hasattr(power_supply_obj, 'model'):
                    TBirdVerifyEnclosures.verify_power_supply_model(power_supply_obj.bay, power_supply_obj.model)

                if hasattr(power_supply_obj, 'serial_number'):
                    TBirdVerifyEnclosures.verify_power_supply_serial_number(power_supply_obj.bay, power_supply_obj.serial_number)

                if hasattr(power_supply_obj, 'part_number'):
                    TBirdVerifyEnclosures.verify_power_supply_part_number(power_supply_obj.bay, power_supply_obj.part_number)

                if hasattr(power_supply_obj, 'spare_part_number'):
                    TBirdVerifyEnclosures.verify_power_supply_spare_part_number(power_supply_obj.bay, power_supply_obj.spare_part_number)

        # fan
        if hasattr(enc_obj, 'fans'):
            FusionUIBase.select_view_by_name('Fans')
            logger.info("Verifying configuration in Fans view...")

            obj_list = enc_obj.fans.item if hasattr(enc_obj.fans, 'item') else enc_obj.fans

            for cim_obj in obj_list:
                TBirdVerifyEnclosures.verify_fan_bay_exist(cim_obj.bay)
                if hasattr(cim_obj, 'status'):
                    TBirdVerifyEnclosures.verify_fan_status(cim_obj.bay, cim_obj.status)

                if hasattr(cim_obj, 'model'):
                    TBirdVerifyEnclosures.verify_fan_model(cim_obj.bay, cim_obj.model)

                if hasattr(cim_obj, 'state'):
                    TBirdVerifyEnclosures.verify_fan_status(cim_obj.bay, cim_obj.state)

                if hasattr(cim_obj, 'serial_number'):
                    TBirdVerifyEnclosures.verify_fan_serial_number(cim_obj.bay, cim_obj.serial_number)

                if hasattr(cim_obj, 'part_number'):
                    TBirdVerifyEnclosures.verify_fan_part_number(cim_obj.bay, cim_obj.part_number)

                if hasattr(cim_obj, 'spare_part_number'):
                    TBirdVerifyEnclosures.verify_fan_spare_part_number(cim_obj.bay, cim_obj.spare_part_number)

        # cim
        if hasattr(enc_obj, 'cim'):
            FusionUIBase.select_view_by_name('Composable Infrastructure Appliances')
            logger.info("Verifying configuration in Composable Infrastructure Appliances view...")

            obj_list = enc_obj.cim.item if hasattr(enc_obj.cim, 'item') else enc_obj.cim

            for cim_obj in obj_list:
                TBirdVerifyEnclosures.verify_cim_bay_exist(cim_obj.bay)
                if hasattr(cim_obj, 'status'):
                    TBirdVerifyEnclosures.verify_cim_status(cim_obj.bay, cim_obj.status)

                if hasattr(cim_obj, 'model'):
                    TBirdVerifyEnclosures.verify_cim_model(cim_obj.bay, cim_obj.model)

                if hasattr(cim_obj, 'power'):
                    TBirdVerifyEnclosures.verify_cim_power(cim_obj.bay, cim_obj.power)

                if hasattr(cim_obj, 'serial_number'):
                    TBirdVerifyEnclosures.verify_cim_serial_number(cim_obj.bay, cim_obj.serial_number)

                if hasattr(cim_obj, 'part_number'):
                    TBirdVerifyEnclosures.verify_cim_part_number(cim_obj.bay, cim_obj.part_number)

                if hasattr(cim_obj, 'spare_part_number'):
                    TBirdVerifyEnclosures.verify_cim_spare_part_number(cim_obj.bay, cim_obj.spare_part_number)

        # link_modules
        if hasattr(enc_obj, 'link_modules'):
            FusionUIBase.select_view_by_name('Frame Link Modules')
            logger.info("Verifying configuration in Link Modules view...")

            obj_list = enc_obj.link_modules.item if hasattr(enc_obj.fans, 'item') else enc_obj.link_modules

            for lm_obj in obj_list:
                TBirdVerifyEnclosures.verify_link_module_bay_exist(lm_obj.bay)
                if hasattr(lm_obj, 'status'):
                    TBirdVerifyEnclosures.verify_link_module_status(lm_obj.bay, lm_obj.status)

                if hasattr(lm_obj, 'model'):
                    TBirdVerifyEnclosures.verify_link_module_model(lm_obj.bay, lm_obj.model)

                if hasattr(lm_obj, 'state'):
                    TBirdVerifyEnclosures.verify_link_module_state(lm_obj.bay, lm_obj.state)

                if hasattr(lm_obj, 'mgmt_port_state'):
                    TBirdVerifyEnclosures.verify_link_module_mgmt_port_state(lm_obj.bay, lm_obj.mgmt_port_state)

                if hasattr(lm_obj, 'link_port_state'):
                    TBirdVerifyEnclosures.verify_link_module_link_port_state(lm_obj.bay, lm_obj.link_port_state)

                # TODO: verify detail information after expand item

        # power
        # TODO: power view

        count += 1

    if count == 0:
        msg = "no target enclosure exists!"
        logger.warn(msg)
        logger.warn("Return Value = False")
        return False

    if count != len(enclosures_obj):
        logger.warn("Not able to verify all enclosure!")
        logger.warn("Return Value = False")
        return False

    logger.debug("Return Value = True")
    return True
# end - verify enclosure information


# begin - delete enclosure
def remove_enclosure(enc_obj):
    """ Delete Enclosure

    Arguments:
      <enclosure> [1, )
          name*                     --  Name of enclosure as a string.

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.enclosures}
        <enclosures>
            <enclosure name="wpst32" />
            <enclosure name="wpst8" />
        </enclosures>

    """
    navigate()

    logger.debug("Deleting enclosures...")

    count = 0
    to_verify = []
    for n, enclosure in enumerate(enc_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(enc_obj), '-' * 14))
        logger.info("Removing a enclosure with name %s" % enclosure.name)
        if not select_enclosure(enclosure.name):
            continue

        C7000RemoveEnclosures.select_actions_remove()
        C7000RemoveEnclosures.wait_remove_dialog_shown()
        if C7000RemoveEnclosures.wait_checkbox_force_remove_enclosure_shown(fail_if_false=False) is True:
            C7000RemoveEnclosures.tick_force_remove_enclosure()
        C7000RemoveEnclosures.click_yes_remove_button()
        C7000RemoveEnclosures.wait_remove_dialog_disappear()
        to_verify.append(enclosure.name)
        count += 1

    if count == 0:
        msg = "no target enclosure exists!"
        logger.warn(msg)
        logger.warn("Return Value = False")
        return False

    time.sleep(15)

    ret = True
    for n, enclosure_name in enumerate(to_verify):
        FusionUIBase.show_activity_sidebar()
        if C7000CommonOperationEnclosures.wait_activity_action_ok(enclosure_name, "Remove", timeout=600, fail_if_false=False) is False:
            ret = False
        FusionUIBase.show_activity_sidebar()

        if C7000VerifyEnclosures.verify_enclosure_not_exist(enclosure_name, fail_if_false=False):
            logger.info("Remove enclosure {0} successfully".format(enclosure_name))
        elif C7000RemoveEnclosures.wait_enclosure_show_not_found(enclosure_name, fail_if_false=False):
            logger.info("Enclosure status appear as 'not found', remove enclosure {0} successfully.".format(enclosure_name))
        else:
            msg = "The enclosure does not disappear in 10min!"
            logger.warn(msg)
            logger.warn("Return Value = False")
            return False

    if count != len(enc_obj):
        logger.warn("Not able to remove all enclosures!")
        logger.warn("Return Value = False")
        return False

    if ret is True:
        logger.debug("Return Value = True")
    else:
        logger.warn("Return Value = False")

    return ret
# end - delete enclosure


# begin - keywords especial for test cases
def validate_should_not_readd_enclosure(enclosures_obj):
    """ Verify if dailog show correct error message when re-add monitored enclosure which already monitored by same appliance

    Arguments:
      <enclosure> [2]
          order*                    --  1 indicates the enclosure will be added as first enclosure
                                        2 indicates the enclosure will be readded
          name*                     --  Name of enclosure as a string.
          encgroup*                 --  Enclosure group name as string. Not applicable when addas* set to Monitored.
          addas*                    --  Choose the method for importing enclosure. Possible value: Managed|Monitored
          licensing*                --  Licensing settings. Possible value: HPE OneViewAdvanced|HPE OneViewAdvanced w/o iLO. Not applicable when addas* set to Monitored.
          oa1hostname*              --  Enclosure's onboard administrator host name or ip. Not applicable when addas* set to Monitored.
          oa1username*              --  Username of enclosure's onboard administrator.
          oa1password*              --  Password of enclosure's onboard administrator.
          remove                    --  A boolean value to determine whether to remove newly added enclosure. (only take effect for 1st enclosure)
          to_add                    --  A boolean value to determine whether to actually add an enclosure. (only take effect for 1st enclosure)

    * Required Arguments

    Note that 2 enclosures' attribute name/oa1hostname/oa1username/oa1password must be same to meet test requirement

    Example:
        data/enclosure -> @{TestData.ENCLn0010}
        <ENCLn0010>
            <enclosure order="1" name="wpst8"
                       force="true"
                       addas="Managed"
                       encgroup="GRP-wpst8"
                       licensing="HPE OneViewAdvanced"
                       oa1hostname="wpst8-oa1.vse.rdlabs.hpecorp.net"
                       oa1password="hpvse14"
                       oa1username="Administrator"
                       remove="true"
                       to_add="true" />
            <enclosure order="2" name="wpst8"
                       force="true"
                       addas="Monitored"
                       oa1hostname="wpst8-oa1.vse.rdlabs.hpecorp.net"
                       oa1password="hpvse14"
                       oa1username="Administrator" />
        </ENCLn0010>
    """
    def remove_single_enclosure(name):
        select_enclosure(name)
        C7000CommonOperationEnclosures.wait_enclosure_selected(name)
        C7000RemoveEnclosures.select_actions_remove()
        C7000RemoveEnclosures.wait_remove_dialog_shown()
        C7000RemoveEnclosures.click_yes_remove_button()
        # wait some seconds to make sure toggle sidebar button to be clickable
        time.sleep(20)
        FusionUIBase.show_activity_sidebar()
        # Enclosure is not successfully removed - 'Remove' action on sidebar is not in OK status
        if FusionUIBase.wait_activity_action_ok(name, "Remove", timeout=600, fail_if_false=False) is False:
            # check if enclosure's status is ERROR
            if C7000VerifyEnclosures.verify_enclosure_status_error(enclosure=name) is True:
                # remove enclosure again by using 'force remove' option
                C7000RemoveEnclosures.select_actions_remove()
                C7000RemoveEnclosures.wait_remove_dialog_shown()
                if C7000RemoveEnclosures.wait_checkbox_force_remove_enclosure_shown():
                    C7000RemoveEnclosures.tick_force_remove_enclosure()
                C7000RemoveEnclosures.click_yes_remove_button()
                FusionUIBase.wait_activity_action_ok(name, "Remove", timeout=600, fail_if_false=False)

        FusionUIBase.show_activity_sidebar()

        if C7000VerifyEnclosures.verify_enclosure_not_exist(name, timeout=20, fail_if_false=False):
            logger.info("Remove enclosure {0} successfully".format(name))
        elif C7000RemoveEnclosures.wait_enclosure_show_not_found(name, timeout=30, fail_if_false=False):
            logger.info("Enclosure status appear as 'not found', remove enclosure {0} successfully.".format(name))
        else:
            err_msg = "The enclosure does not disappear in 10s!"
            logger.warn(err_msg)
            return False

        return True

    navigate()

    if len(enclosures_obj) != 2:
        ui_lib.fail_test("Must provide 2 enclosures node")

    first_enc_obj = [obj for obj in enclosures_obj if obj.order == '1'][0]
    second_enc_obj = [obj for obj in enclosures_obj if obj.order == '2'][0]

    # ===== add first enclosure =====
    if getattr(first_enc_obj, 'to_add', 'true').lower() == 'true':
        logger.info("===== add first enclosure =====")
        if C7000VerifyEnclosures.verify_enclosure_not_exist(first_enc_obj.name, fail_if_false=False) is False:
            # first enclosure already exists, verify if it's the expected state ('Configured' for addas="Managed", 'Monitored' for addas="Monitored")
            C7000CommonOperationEnclosures.click_enclosure(first_enc_obj.name)
            FusionUIBase.select_view_by_name('General')
            if first_enc_obj.addas == 'Managed':
                # expect the existing enclosure was added for Management as the pre-condition, verify if its actual state is 'Configured'
                if C7000VerifyEnclosures.verify_general_state('Configured', fail_if_false=False) is False:
                    ui_lib.fail_test("first enclosure (pre-condition) '%s' already exists, "
                                     "but it's not in the expected state 'Configured' (addas='Managed')" % first_enc_obj.name, captureScreenshot=True)

            if first_enc_obj.addas == 'Monitored':
                # expect the existing enclosure was added for Monitoring as the pre-condition, verify if its actual state is 'Monitored'
                if C7000VerifyEnclosures.verify_general_state('Monitored', fail_if_false=False) is False:
                    ui_lib.fail_test("first enclosure (pre-condition) '%s' already exists, "
                                     "but it's not in the expected state 'Monitored' (addas='Monitored')" % first_enc_obj.name, captureScreenshot=True)

        else:
            C7000AddEnclosures.click_add_enclosure_button()
            C7000AddEnclosures.wait_add_enclosure_dialog_shown()
            C7000AddEnclosures.input_oa_ip_address_or_host_name(first_enc_obj.oa1hostname)
            if first_enc_obj.addas == 'Monitored':
                C7000AddEnclosures.tick_action_add_enclosure_for_monitoring()
            elif first_enc_obj.addas == 'Managed':
                C7000AddEnclosures.tick_action_add_enclosure_for_management()
            else:
                ui_lib.fail_test("Not supported value '%s' of <addas> attribute" % first_enc_obj.addas)

            C7000AddEnclosures.input_user_name(first_enc_obj.oa1username)
            C7000AddEnclosures.input_password(first_enc_obj.oa1password)

            if first_enc_obj.addas == 'Managed':
                if getattr(first_enc_obj, 'create_new_eg', 'false').lower() == 'true':
                    C7000AddEnclosures.input_enclosure_group_name(first_enc_obj.encgroup)
                else:
                    C7000AddEnclosures.input_select_enclosure_group(first_enc_obj.encgroup)
                if first_enc_obj.licensing == 'HPE OneView Advanced':
                    C7000AddEnclosures.tick_licensing_hp_oneview_advanced()
                elif first_enc_obj.licensing == 'HPE OneView Advanced w/o iLO':
                    C7000AddEnclosures.tick_licensing_hp_oneview_advanced_wo_ilo()
                else:
                    ui_lib.fail_test("Not supported value '%s' of <licensing> attribute" % first_enc_obj.licensing)

            C7000AddEnclosures.click_add_button()
            # may got enclosure is already claimed by another appliance, forcible add enclosure if force="true" in test data
            C7000AddEnclosures.wait_adding_enclosure_operation_stage_1(first_enc_obj)
            C7000AddEnclosures.wait_add_enclosure_dialog_disappear(timeout=60)
            FusionUIBase.show_activity_sidebar()
            FusionUIBase.wait_activity_action_ok(first_enc_obj.oa1hostname, "Add", timeout=600, fail_if_false=False)
            FusionUIBase.show_activity_sidebar()
            C7000VerifyEnclosures.verify_enclosure_exist(first_enc_obj.name)

    # ===== re add =====
    logger.info("===== re add (add second enclosure) =====")
    C7000AddEnclosures.click_add_enclosure_button()
    C7000AddEnclosures.wait_add_enclosure_dialog_shown()
    C7000AddEnclosures.input_oa_ip_address_or_host_name(second_enc_obj.oa1hostname)
    if second_enc_obj.addas == 'Monitored':
        C7000AddEnclosures.tick_action_add_enclosure_for_monitoring()
    elif second_enc_obj.addas == 'Managed':
        C7000AddEnclosures.tick_action_add_enclosure_for_management()
    else:
        ui_lib.fail_test("Not supported value '%s' of <addas> attribute" % second_enc_obj.addas)

    C7000AddEnclosures.input_user_name(second_enc_obj.oa1username)
    C7000AddEnclosures.input_password(second_enc_obj.oa1password)

    if second_enc_obj.addas == 'Managed':
        if getattr(second_enc_obj, 'create_new_eg', 'false').lower() == 'true':
            C7000AddEnclosures.input_enclosure_group_name(second_enc_obj.encgroup)
        else:
            C7000AddEnclosures.input_select_enclosure_group(second_enc_obj.encgroup)
        if second_enc_obj.licensing == 'HPE OneView Advanced':
            C7000AddEnclosures.tick_licensing_hp_oneview_advanced()
        elif second_enc_obj.licensing == 'HPE OneView Advanced w/o iLO':
            C7000AddEnclosures.tick_licensing_hp_oneview_advanced_wo_ilo()
        else:
            ui_lib.fail_test("Not supported value '%s' of <licensing> attribute" % second_enc_obj.licensing)
    C7000AddEnclosures.click_add_button()
    C7000AddEnclosures.wait_adding_enclosure_text_in_dialog()
    C7000AddEnclosures.wait_adding_enclosure_text_disappear_from_dialog()
    msg = FusionUIBase.get_error_message_from_dialog()

    if msg[0] is False:
        ui_lib.fail_test("Failed to get error message in dialog")
    else:
        logger.info("Got error message: %s" % msg[1])
        expected_txt = ''
        if first_enc_obj.addas == 'Monitored':
            expected_txt = 'is already being monitored by this appliance.'
        elif first_enc_obj.addas == 'Managed':
            expected_txt = 'is already being managed by this appliance.'

        if re.search(expected_txt, msg[1]) is None:
            ui_lib.fail_test("Error message doesn't contains expected text. Expected text: %s" % expected_txt)
        else:
            logger.info("Successfully got the expected error message '%s'" % expected_txt)

    C7000AddEnclosures.click_cancel_button()
    C7000AddEnclosures.wait_add_enclosure_dialog_disappear()

    # sleep some seconds otherwise we'll get error 'has an ongoing operation' error after hitting 'Yes, delete' button
    time.sleep(20)

    if getattr(first_enc_obj, 'remove', 'true').lower() == 'true':
        logger.info("===== remove first enclosure '%s' =====" % first_enc_obj.name)
        remove_single_enclosure(first_enc_obj.name)

    logger.debug("Return Value = True")
    return True


def validate_ui_component_for_add_enclosure_dialog():
    """
    Verify UI components of add enclosure dialog

    :return:
    """
    navigate()

    C7000AddEnclosures.click_add_enclosure_button()
    C7000AddEnclosures.wait_add_enclosure_dialog_shown()

    C7000VerifyEnclosures.verify_oa_ip_address_or_host_name_input_control_exist()
    C7000VerifyEnclosures.verify_add_enclosure_for_management_raidobox_control_exist()
    C7000VerifyEnclosures.verify_add_enclosure_for_monitoring_raidobox_control_exist()
    C7000VerifyEnclosures.verify_migrate_virtual_connect_domain_raidobox_control_exist()

    # for managed enclosure
    C7000AddEnclosures.tick_action_add_enclosure_for_management()
    C7000VerifyEnclosures.verify_user_name_input_control_exist()
    C7000VerifyEnclosures.verify_password_input_control_exist()
    C7000AddEnclosures.input_select_enclosure_group("Create new enclosure group")
    C7000VerifyEnclosures.verify_enclosure_group_input_control_exist()
    C7000VerifyEnclosures.verify_licensing_hp_oneview_advanced_raidobox_control_exist()
    C7000VerifyEnclosures.verify_licensing_hp_oneview_advanced_wo_ilo_raidobox_control_exist()
    C7000VerifyEnclosures.verify_firmware_baseline_control_exist()

    # for monitored enclosure
    C7000AddEnclosures.tick_action_add_enclosure_for_monitoring()
    C7000VerifyEnclosures.verify_user_name_input_control_exist()
    C7000VerifyEnclosures.verify_password_input_control_exist()
    C7000VerifyEnclosures.verify_enclosure_group_input_control_not_exist()
    C7000VerifyEnclosures.verify_licensing_hp_oneview_advanced_raidobox_control_not_exist()
    C7000VerifyEnclosures.verify_licensing_hp_oneview_advanced_wo_ilo_raidobox_control_not_exist()
    C7000VerifyEnclosures.verify_firmware_baseline_control_not_exist()

    logger.debug("Return Value = True")
    return True


def validate_action_menu_for_monitored_enclosure(enclosures_obj):
    """ Verify action menu item for monitored enclosure

    Arguments:
      <enclosure> [1]
          name*                     --  Name of enclosure as a string.

    * Required Arguments

    Example:
        data/enclosure -> @{TestData.ENCLn0010}
        <ENCLn0010>
            <enclosure name="wpst8" />
        </ENCLn0010>

        * Only support 1 enclosure node
    """
    navigate()

    if len(enclosures_obj) != 1:
        ui_lib.fail_test("Only support 1 enclosure object in enclosures_obj")

    enc_obj = enclosures_obj[0]

    select_enclosure(enc_obj.name)
    C7000CommonOperationEnclosures.wait_enclosure_selected(enc_obj.name)
    C7000CommonOperationEnclosures.click_action_button()
    C7000VerifyEnclosures.verify_action_add_button_exist()
    C7000VerifyEnclosures.verify_action_refresh_button_exist()
    C7000VerifyEnclosures.verify_action_remove_button_exist()
    C7000VerifyEnclosures.verify_action_reapply_configuration_button_not_exist()
    C7000VerifyEnclosures.verify_action_edit_button_not_exist()

    logger.debug("Return Value = True")
    return True


def validate_server_hardware_power_state_after_refresh_enclosure(enclosures_obj):
    """ Verify server hardware power state after refresh enclosure

    * Be sure to add specified enclosure as managed before calling this function

    Arguments:
      <enclosure> [1]
          name*                     --  Name of enclosure as a string.
          create_new_eg*            --  Whether to create new enclosure group when adding enclosure. Only take effect when addas* set to Managed. Possible value: true|false
          encgroup*                 --  Enclosure group name as string. Not applicable when addas* set to Monitored.
          addas*                    --  Choose the method for importing enclosure. Possible value: Managed|Monitored
          licensing*                --  Licensing settings. Possible value: HPE OneViewAdvanced|HPE OneViewAdvanced w/o iLO. Not applicable when addas* set to Monitored.
          oa1hostname*              --  Enclosure's onboard administrator host name or ip. Not applicable when addas* set to Monitored.
          oa1username*              --  Username of enclosure's onboard administrator.
          oa1password*              --  Password of enclosure's onboard administrator.
          <verify_server_power_state>   [1, ) required. Can be multiple. Specify which server blades will be used for verify power state
            bay                     --  name of server bay. E.g. wpst31, bay 1

    * Required Arguments

    Example:
        data/enclosure -> @{TestData.ENCLp0017}
        <ENCLp0017>
            <enclosure name="wpst31"
                       force="true"
                       addas="Managed"
                       create_new_eg="false"
                       encgroup="GRP-wpst31"
                       licensing="HPE OneViewAdvanced"
                       oa1hostname="wpst31-oa1.vse.rdlabs.hpecorp.net"
                       oa1password="hpvse14"
                       oa1username="Administrator">
                <verify_server_power_state>
                    <server bay="wpst31, bay 1" />
                    <server bay="wpst31, bay 2" />
                    <server bay="wpst31, bay 3" />
                </verify_server_power_state>
            </enclosure>
        </ENCLp0017>

        * Only support 1 enclosure node
    """
    from FusionLibrary.ui.servers.serverhardware import get_server_powerstatus
    from FusionLibrary.libs.api.oa.oa_client import OaSoapClient

    navigate()

    if len(enclosures_obj) != 1:
        ui_lib.fail_test("Only support 1 enclosure object in enclosures_obj")

    enc_obj = enclosures_obj[0]

    # get server hardware power state from UI
    verify_sever_power_state_obj = enc_obj.verify_server_power_state
    # get power state of specific server hardwares defined in data file from UI
    old_state_lst = []
    for item in verify_sever_power_state_obj:
        old_state_lst.append((item, get_server_powerstatus(item.bay)))
        # wait page changed so that we can obtain correct power state of specific serve hardware
        time.sleep(5)

    logger.info("Got old power state for target server blade\n%r" % old_state_lst)

    # power on/off server hardwares depend on old state, do reverse operation
    oa_client = OaSoapClient(enc_obj.oa1hostname, enc_obj.oa1username, enc_obj.oa1password)
    for item, status in old_state_lst:
        if status == 'On':
            oa_client.power_off_blade(item.bay.replace('%s, bay ' % enc_obj.name, ''))
        elif status == 'Off':
            oa_client.power_on_blade(item.bay.replace('%s, bay ' % enc_obj.name, ''))

    time.sleep(60)

    select_enclosure(enc_obj.name)
    C7000CommonOperationEnclosures.wait_enclosure_selected(enc_obj.name)
    C7000RefreshEnclosures.select_actions_refresh()
    # page will be frozen for a while, can't click pin to get activity panel appeared
    time.sleep(20)

    FusionUIBase.show_activity_sidebar()
    C7000CommonOperationEnclosures.wait_activity_action_ok(enc_obj.name, 'Refresh')
    FusionUIBase.show_activity_sidebar()

    # compare power state for specified server hardware
    expected_state_list = [(bay, 'On') if state == 'Off' else (bay, 'Off') for bay, state in old_state_lst]

    new_stat_list = []
    for item in verify_sever_power_state_obj:
        new_stat_list.append((item, get_server_powerstatus(item.bay)))
        # wait page changed so that we can obtain correct power state of specific serve hardware
        time.sleep(5)

    ret = True
    for i, item in enumerate(new_stat_list):
        if item[1] == expected_state_list[i][1]:
            logger.info("The server bay %s changed from '%s' to expected power state '%s'" % (item[0], old_state_lst[i][1], expected_state_list[i][1]))
        else:
            ret = False
            logger.warn("The server bay %s didn't change from '%s' to expected power state '%s', current state: '%s'" % (item[0], old_state_lst[i][1], expected_state_list[i][1], item[1]))

    logger.debug("Return Value = %s" % ret)
    return ret


def validate_server_hardware_power_state_after_reapply_enclosure_config(enclosures_obj):
    """ Verify server hardware power state after reapply enclosure configuration

    * Be sure to add specified enclosure as managed before calling this function

    Arguments:
      <enclosure> [1]
          name*                     --  Name of enclosure as a string.
          create_new_eg*            --  Whether to create new enclosure group when adding enclosure. Only take effect when addas* set to Managed. Possible value: true|false
          encgroup*                 --  Enclosure group name as string. Not applicable when addas* set to Monitored.
          addas*                    --  Choose the method for importing enclosure. Possible value: Managed|Monitored
          licensing*                --  Licensing settings. Possible value: HPE OneViewAdvanced|HPE OneViewAdvanced w/o iLO. Not applicable when addas* set to Monitored.
          oa1hostname*              --  Enclosure's onboard administrator host name or ip. Not applicable when addas* set to Monitored.
          oa1username*              --  Username of enclosure's onboard administrator.
          oa1password*              --  Password of enclosure's onboard administrator.
          <verify_server_power_state>   [1, ) required. Can be multiple. Specify which server blades will be used for verify power state
            bay                     --  name of server bay. E.g. wpst31, bay 1

    * Required Arguments

    Example:
        data/enclosure -> @{TestData.ENCLp0018}
        <ENCLp0018>
            <enclosure name="wpst31"
                       force="true"
                       addas="Managed"
                       create_new_eg="false"
                       encgroup="GRP-wpst31"
                       licensing="HPE OneViewAdvanced"
                       oa1hostname="wpst31-oa1.vse.rdlabs.hpecorp.net"
                       oa1password="hpvse14"
                       oa1username="Administrator">
                <verify_server_power_state>
                    <server bay="wpst31, bay 1" />
                    <server bay="wpst31, bay 2" />
                    <server bay="wpst31, bay 3" />
                </verify_server_power_state>
            </enclosure>
        </ENCLp0018>

        * Only support 1 enclosure node
    """
    from FusionLibrary.ui.servers.serverhardware import get_server_powerstatus
    from FusionLibrary.libs.api.oa.oa_client import OaSoapClient

    navigate()

    if len(enclosures_obj) != 1:
        ui_lib.fail_test("Only support 1 enclosure object in enclosures_obj")

    enc_obj = enclosures_obj[0]

    # get server hardware power state from UI
    verify_sever_power_state_obj = enc_obj.verify_server_power_state
    # get power state of specific server hardwares defined in data file from UI
    old_state_lst = []
    for item in verify_sever_power_state_obj:
        old_state_lst.append((item, get_server_powerstatus(item.bay)))
        # wait page changed so that we can obtain correct power state of specific serve hardware
        time.sleep(5)

    logger.info("Got old power state for target server blade\n%r" % old_state_lst)

    # power on/off server hardwares depend on old state, do reverse operation
    oa_client = OaSoapClient(enc_obj.oa1hostname, enc_obj.oa1username, enc_obj.oa1password)
    for item, status in old_state_lst:
        if status == 'On':
            oa_client.power_off_blade(item.bay.replace('%s, bay ' % enc_obj.name, ''))
        elif status == 'Off':
            oa_client.power_on_blade(item.bay.replace('%s, bay ' % enc_obj.name, ''))

    time.sleep(60)

    select_enclosure(enc_obj.name)
    C7000CommonOperationEnclosures.wait_enclosure_selected(enc_obj.name)
    C7000EnclosuresReapplyConfiguration.select_actions_reapply_configuration()
    # page will be frozen for a while, can't click pin to get activity panel appeared
    time.sleep(20)

    FusionUIBase.show_activity_sidebar()
    C7000CommonOperationEnclosures.wait_activity_action_ok(enc_obj.name, 'Reapply configuration')
    FusionUIBase.show_activity_sidebar()

    # compare power state for specified server hardware
    expected_state_list = [(bay, 'On') if state == 'Off' else (bay, 'Off') for bay, state in old_state_lst]

    new_stat_list = []
    for item in verify_sever_power_state_obj:
        new_stat_list.append((item, get_server_powerstatus(item.bay)))
        # wait page changed so that we can obtain correct power state of specific serve hardware
        time.sleep(5)

    ret = True
    for i, item in enumerate(new_stat_list):
        if item[1] == expected_state_list[i][1]:
            logger.info("The server bay %s changed from '%s' to expected power state '%s'" % (item[0], old_state_lst[i][1], expected_state_list[i][1]))
        else:
            ret = False
            logger.warn("The server bay %s didn't change from '%s' to expected power state '%s', current state: '%s'" % (item[0], old_state_lst[i][1], expected_state_list[i][1], item[1]))

    logger.debug("Return Value = %s" % ret)
    return ret

# end - keywords especial for test cases


# begin - keywords especial for uuid light(F136)
def turn_on_enclosure_uid(*enc_obj):
    """ turn_on_enclosure_uid
        Example:
        | `Turn On Enclosure uid`      |     |
    """
    """below part of checking for single/multiple/named instance is yet to be implemented"""
    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])

    fail_time = 0
    for enclosure in enc_obj:
        if not select_enclosure(enclosure.name):
            logger.warn("Exiting Turn On UID enclosure Function, Not selected enclosure %s" % enclosure.name)
            fail_time += 1
            continue

        C7000CommonOperationEnclosures.verify_uid_light_off()
        C7000CommonOperationEnclosures.click_uid_light()
        C7000CommonOperationEnclosures.verify_uid_light_on()

    if fail_time > 0:
        return False
    else:
        return True


def turn_off_enclosure_uid(*enc_obj):
    """ turn_off_enclosure_uid
        Example:
        | `Turn Off enclosure uid`      |     |
    """
    """below part of checking for single/multiple/named instance is yet to be implemented"""
    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])

    fail_time = 0
    for enclosure in enc_obj:
        if not select_enclosure(enclosure.name):
            logger.warn("Exiting Turn Off UID enclosure Function, Not selected enclosure %s" % enclosure.name)
            fail_time += 1
            continue

        C7000CommonOperationEnclosures.verify_uid_light_on()
        C7000CommonOperationEnclosures.click_uid_light()
        C7000CommonOperationEnclosures.verify_uid_light_off()

    if fail_time > 0:
        return False
    else:
        return True


def validate_enclosure_uid_light_off(*enc_obj):
    """ verify whether the uid(s) of enclosure(s) are in off status.
        Example:
        | `validate_enclosure_uid_light_off`    | @(IC data) |
    """
    """below part of checking for single/multiple/named instance is yet to be implemented"""
    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])

    fail_time = 0
    for enclosure in enc_obj:
        if not select_enclosure(enclosure.name):
            logger.warn("Exiting Turn On UID enclosure Function, Not selected enclosure %s" % enclosure.name)
            fail_time += 1
            continue

        C7000CommonOperationEnclosures.verify_uid_light_off()

    if fail_time > 0:
        return False
    else:
        return True
# end - keywords especial for uuid light(F136)


def validate_enclosure_task_step(enc_obj):
    """ Validate enclosure add/edit task text

    Arguments:
      name*             --  Name of enclosure as a string.
      task*             --  Name of enclosure task as a string.
      step*             --  Text that enclosure task steps contain.
      validate_timeout  --  Timeout.
      exist             --  Validate text should not be existed when false.

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.enclosures.Add}
            <enclosures>
                <Add>
                    <enclosure name="wpst22" task="Add" step="Unable to update iLO as no SPP firmware bundle is available
that contains the required iLO firmware version" />
                </Add>
            </enclosures>

    """

    FusionUIBase.navigate_to_section(SectionType.ENCLOSURES, time_for_loading=5)
    total = len(enc_obj)
    not_exists = 0
    verified = 0

    for n, enclosure in enumerate(enc_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("Validate enclosure <%s> task contains <%s>" % (enclosure.name, enclosure.step))
        if not VerifyEnclosures.verify_enclosure_exist(enclosure.name, fail_if_false=False):
            logger.warn("enclosure '%s' does not exist" % enclosure.name)
            not_exists += 1
            continue

        TBirdCommonOperationEnclosures.click_enclosure(enclosure.name)
        FusionUIBase.select_view_by_name(view_name='Activity', timeout=5)
        TBirdCommonOperationEnclosures.click_activity_collapser(enclosure.task)
        timeout = int(getattr(enclosure, 'validate_timeout', '5'))
        ret = VerifyEnclosures.verify_activity_contains_text(enclosure.step, timeout=timeout, fail_if_false=False)
        # Verify step text not exist in steps
        if getattr(enclosure, 'exist', '').lower() == 'false':
            if ret is True:
                ui_lib.fail_test("%s should not exist in task steps" % enclosure.step)
        elif ret is False:
            ui_lib.fail_test("%s should exist in task steps" % enclosure.step)

        logger.info("enclosure '%s' got the correct task step" % enclosure.name)
        verified += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no enclosure to view! all %s enclosure(s) is NOT existing, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if verified < total:
            logger.warn("not all of task for the enclosure(s) is successfully verified - %s out of %s verified " % (verified, total))
            if verified + not_exists == total:
                logger.warn("%s not-existing enclosure(s) is skipped, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s not-existing enclosure(s) is skipped, %s profile(s) left is failed being verified " % (not_exists, total - verified - not_exists))
                return False

    logger.info("all of the enclosure(s) is successfully verified - %s out of %s " % (verified, total))
    return True


def validate_enclosure_sub_task(enc_obj):
    """ Validate enclosure add/edit task text

    Arguments:
      name*             --  Name of enclosure as a string.
      task*             --  Name of enclosure task as a string.
      subtask*          --  Name of sub task as a string.
      source*           --  Name of task source as a string.
      status            --  Status of task as a string.
      validate_timeout  --  Timeout.

    * Required Arguments

    Example:
    Example:
        data/enclosures -> @{TestData.enclosures.Add}
            <enclosures>
                <Add>
                    <enclosure name="wpst26" task="Add" subtask="Update iLO firmware" source="wpst26, bay 5" status="OK"/>
                </Add>
            </enclosures>

    """

    FusionUIBase.navigate_to_section(SectionType.ENCLOSURES, time_for_loading=5)
    total = len(enc_obj)
    not_exists = 0
    verified = 0

    for n, enclosure in enumerate(enc_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("Validate enclosure <%s> task contains <%s>" % (enclosure.name, enclosure.subtask))
        if not VerifyEnclosures.verify_enclosure_exist(enclosure.name, fail_if_false=False):
            logger.warn("enclosure '%s' does not exist" % enclosure.name)
            not_exists += 1
            continue

        TBirdCommonOperationEnclosures.click_enclosure(enclosure.name)
        FusionUIBase.select_view_by_name(view_name='Activity', timeout=5)
        TBirdCommonOperationEnclosures.click_activity_collapser(enclosure.task)
        timeout = int(getattr(enclosure, 'validate_timeout', '5'))
        status = getattr(enclosure, 'status', 'ok').lower()
        ret = VerifyEnclosures.verify_activity_contains_subtask(subtask=enclosure.subtask, source=enclosure.source, status=status, timeout=timeout, fail_if_false=False)
        # Verify step text not exist in steps
        if getattr(enclosure, 'exist', '').lower() == 'false':
            if ret is True:
                ui_lib.fail_test("%s for %s should not exist in task" % (enclosure.subtask, enclosure.source))
        elif ret is False:
            ui_lib.fail_test("%s for %s should exist in task" % (enclosure.subtask, enclosure.source))

        logger.info("enclosure '%s' got the correct sub task" % enclosure.name)
        verified += 1

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no enclosure to view! all %s enclosure(s) is NOT existing, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if verified < total:
            logger.warn("not all of task for the enclosure(s) is successfully verified - %s out of %s verified " % (verified, total))
            if verified + not_exists == total:
                logger.warn("%s not-existing enclosure(s) is skipped, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s not-existing enclosure(s) is skipped, %s profile(s) left is failed being verified " % (not_exists, total - verified - not_exists))
                return False

    logger.info("all of the enclosure(s) is successfully verified - %s out of %s " % (verified, total))
    return True


def update_enclosure_firmware(*enc_obj):
    """ Update Enclosure Firmware

        Example:
        | `Update Enclosure Firmware` |    |
    """
    logger._log_to_console_and_log_file("Update firmware")

    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])
    for enclosure in enc_obj:
        logger._log_to_console_and_log_file("Updating Enclosure Firmware For..... %s" % enclosure.name)
        # Checks whether enclosure present or not

        # if ui_lib.wait_for_element(FusionEnclosuresPage.ID_ENCLOSURE_TITLE %enclosureName.name):
        selenium2lib = ui_lib.get_s2l()
        logger._log_to_console_and_log_file("Selecting Enclosure %s to update firmware  " % enclosure.name)
        # Verifying Enclosures page is opened or not. Open if it is not opened
        if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_ENCLOSURE_ADD_BUTTON):
            logger._log_to_console_and_log_file("Success")
            ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_MENU_ONE_VIEW)
            ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_LINK_ENCLOSURE)
        if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_ENCLOSURE_ADD_BUTTON, PerfConstants.SELECT_ENCLOSURE):
            logger._log_to_console_and_log_file("Unable to open the Enclosures page")
            selenium2lib.capture_page_screenshot()
            return False
        else:
            logger._log_to_console_and_log_file("Enclosures page opened successfully")
            # Verifying the presence of given Enclosure and selecting
            ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enclosure.name, PerfConstants.SELECT_ENCLOSURE)
            if ui_lib.wait_for_element(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enclosure.name):
                ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enclosure.name)
                if ui_lib.wait_for_element(FusionEnclosuresPage.ID_ENCLOSURE_TITLE % enclosure.name, PerfConstants.ENCLOSURE_TITLE):
                    logger._log_to_console_and_log_file("Given Enclosure %s is selected" % enclosure.name)
                    # ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_SELECT_ENCLOSURE %enclosureName.name)
                    FirmwareBaseLine = enclosure.frimwareBaseline
                    logger._log_to_console_and_log_file(FirmwareBaseLine)
                    ui_lib.wait_for_element(FusionEnclosuresPage.ID_ACTION_MAIN_BTN, PerfConstants.SELECT_UPDATE_FIRMWARE_ACTION)
                    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ACTION_MAIN_BTN)
                    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_LINK_CLICK_UPDATE_FIRMWARE)
                    # Update the enclosure firmware manually
                    if (FirmwareBaseLine == 'Manage manually'):
                        ui_lib.wait_for_element(FusionEnclosuresPage.ID_COMBO_BOX_FIRMWARE_BASELINE, PerfConstants.SELECT_COMBO_BOX)
                        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_COMBO_BOX_FIRMWARE_BASELINE)
                        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_COMBO_BOX_SELECT_FIRMWARE % FirmwareBaseLine)
                        ui_lib.wait_for_element(FusionEnclosuresPage.ID_BTN_CONFIRM_UPDATE_FIRMWARE, PerfConstants.SELECT_COMBO_BOX)
                        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_BTN_CONFIRM_UPDATE_FIRMWARE)
                        ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_ACTIVITY_OVERVIEW, PerfConstants . ENCLOSURE_ACTIVITY)
                        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ACTIVITY_OVERVIEW)
                        ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_ACTIVITY_ACTIVITY, PerfConstants . ENCLOSURE_ACTIVITY)
                        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ACTIVITY_ACTIVITY)
                        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_ENCLOSURE_FIRMWARE_STATE_COMPLETE_MANUAL, PerfConstants.FIRMWARE_MANUALLY_VALIDATION):
                            logger._log_to_console_and_log_file("Updating enclosure manually done successfully")
                        else:
                            logger._log_to_console_and_log_file("Update failed")
                    # Updates the enclosure firmware with service pack
                    else:
                        ui_lib.wait_for_element(FusionEnclosuresPage.ID_COMBO_BOX_FIRMWARE_BASELINE, PerfConstants.SELECT_COMBO_BOX)
                        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_COMBO_BOX_FIRMWARE_BASELINE)
                        # Checks whether valid service pack is selected otherwise it will go to else part
                        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_COMBO_BOX_SELECT_FIRMWARE % FirmwareBaseLine, PerfConstants.SELECT_COMBO_BOX):
                            logger._log_to_console_and_log_file("Selected right option")
                            ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_COMBO_BOX_SELECT_FIRMWARE % FirmwareBaseLine)
                            ui_lib.wait_for_element(FusionEnclosuresPage.ID_COMBO_BOX_UPDATE_FIRMWARE_FOR, PerfConstants.SELECT_COMBO_BOX)
                            for key in enclosure.upDateFor:
                                #                                 logger._log_to_console_and_log_file(key)
                                selenium2lib.press_key(FusionEnclosuresPage.ID_COMBO_BOX_UPDATE_FIRMWARE_FOR, key)
                            selenium2lib.press_key(FusionEnclosuresPage.ID_COMBO_BOX_UPDATE_FIRMWARE_FOR, chr(13))
                            value = selenium2lib.get_text(FusionEnclosuresPage.ID_COMBO_BOX_UPDATE_FIRMWARE_FOR)
                            logger._log_to_console_and_log_file(value)
                            # Validates whether we have passed the valid value to update for such as 'Enclosure'
                            if (value == enclosure.upDateFor):
                                logger._log_to_console_and_log_file("Entered Valid value to update for %s" % value)
                                ui_lib.wait_for_element(FusionEnclosuresPage.ID_BTN_CONFIRM_UPDATE_FIRMWARE, PerfConstants.SELECT_COMBO_BOX)
                                ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_BTN_CONFIRM_UPDATE_FIRMWARE)
                                ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_MAIN_PAGE, PerfConstants.ACTIVITY)
                                ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_MAIN_PAGE)
                                ui_lib.wait_for_element_visible(FusionDashboardPage.ID_LINK_ACTIVITY, PerfConstants.ACTIVITY)
                                ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_LINK_ACTIVITY)
                                if ui_lib.wait_for_element(FusionEnclosuresPage.ID_NEW_ACTIVITY_PROGRESS % enclosure.name, PerfConstants.FIRMWARE_VALIDATION):
                                    start_time = selenium2lib.get_text(FusionEnclosuresPage.ID_NEW_ACTIVITY_TIMESTAMP % enclosure.name)
                                    logger._log_to_console_and_log_file(start_time)
                                    logger._log_to_console_and_log_file("Update Enclosure Firmware For %s started......... " % enclosure.name)
                                    if ui_lib.wait_for_element(FusionEnclosuresPage.ID_NEW_ACTIVITY_SUCCESS % (enclosure.name, start_time), PerfConstants.FIRMWARE_SUCCESS_OR_FAILURE):
                                        logger._log_to_console_and_log_file("Updating Enclosure Firmware For %s done successfully" % enclosure.name)
                                    elif ui_lib.wait_for_element(FusionEnclosuresPage.ID_NEW_ACTIVITY_ERROR % (enclosure.name, start_time), PerfConstants.FIRMWARE_SUCCESS_OR_FAILURE):
                                        logger._log_to_console_and_log_file("Update Enclosure Firmware For %s done with errors" % enclosure.name)
                                    else:
                                        logger._log_to_console_and_log_file("Update Enclosure FirmwareFor %s done with warnings" % enclosure.name)
                            else:
                                logger._log_to_console_and_log_file("Valid option to update for %s is not found" % enclosure.upDateFor)
                                ui_lib.wait_for_element(FusionEnclosuresPage.ID_BTN_ENCLOSURE_FIRMWARE_CANCEL)
                                ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_BTN_ENCLOSURE_FIRMWARE_CANCEL)
                        else:
                            '''
                            This block of statements will be executed if we pass invalid service pack
                            '''
                            logger._log_to_console_and_log_file("Firmware baseline with the name %s is not present in the appliance" % FirmwareBaseLine)
                            ui_lib.wait_for_element(FusionEnclosuresPage.ID_BTN_ENCLOSURE_FIRMWARE_CANCEL)
                            ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_BTN_ENCLOSURE_FIRMWARE_CANCEL)
                else:
                    logger._log_to_console_and_log_file("Unable to select the given Enclosure %s :" % enclosure.name)
            else:
                logger._log_to_console_and_log_file("Given Enclosure %s is not present in the Appliance" % enclosure.name)


def _verify_enclosure_in_activity(licensename, enclosureip, enclosurename, s2l):
    """ Verify the server Hardware in Activity Page """

    """ Getting the Baynum from encl page to check the licensing option """
    s2l = ui_lib.get_s2l()

    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_MENU_SELECTOR, fail_if_false=True)
    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_LINK_DEVICE_BAYS, fail_if_false=True)
    BuiltIn().sleep(3)

    logger.info("Get text in first bay of the enclosure %s" % enclosurename)
    s2l.capture_page_screenshot()
    bayname = ui_lib.ignore_staleElementRefException("get_text", FusionEnclosuresPage.ID_FIRST_DEVICE_BAY)
    BuiltIn().should_not_be_empty(bayname, "Failed to get first bay number of enclosure %s" % enclosurename)
    logger._log_to_console_and_log_file("Available bay in enclosure %s is %s Now checking the selected license option" % (enclosurename, bayname))

    if not ui_lib.wait_for_element(FusionActivityPage.ID_PAGE_LABEL):
        base_page.navigate_base(FusionActivityPage.ID_PAGE_LABEL, FusionUIBaseElements.ID_MENU_LINK_ACTIVITY, "css=span.hp-page-item-count")

    """Validating the creation of server Hardware with time stamp and activity """
    blnstatus = activity._is_element_present_activity_page_without_time('Add', enclosurename)
    if blnstatus:

        strtimestamp = s2l.get_text(FusionActivityPage.ID_TIMESTAMP % ('Add', enclosurename))
        ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_ACTIVITY_COLLAPSE % (strtimestamp, enclosurename))
        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ACTIVITY_COLLAPSE % (strtimestamp, enclosurename))
        ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_ACTIVITY_NOTIFY_CONTAINER, PerfConstants.ACTIVITY)
        if licensename:
            if ui_lib.wait_for_element(FusionEnclosuresPage.ID_ACTIVITY_NOTIFY_CONTAINER, fail_if_false=True):
                logger._log_to_console_and_log_file("Check the license information in the Activity notification")
                ui_lib.wait_for_element(FusionEnclosuresPage.ID_ACTIVITY_NOTIFY_DETAILS % bayname.strip())
                strmsg = ui_lib.get_text(FusionEnclosuresPage.ID_ACTIVITY_NOTIFY_DETAILS % bayname.strip())

                """ Verifying the license name in activity notification """
                if (licensename.lower() in strmsg.lower()):
                    logger._log_to_console_and_log_file("Server %s is added with selected license HP %s" % (enclosureip, licensename))
                else:
                    logger._warn("Enclosure is imported not with the given license,The Activity notify message is %s" % strmsg)
                    return False
            elif licensename:
                logger._warn("Fail to select the Added server %s in Activity Page" % enclosureip)
                return False
            else:
                logger._log_to_console_and_log_file('Skip to check license option due to under Monitored state')
    else:
        logger._warn("Add Enclosure Activity ADD is not available Activity Page")
        return False
    return True


def _select_enclosure_license(enclosure):
    if enclosure.licensing.lower() == "hpe oneview advanced":
        C7000AddEnclosures.tick_licensing_hp_oneview_advanced()
        logger.info("Selected licensing for OneView")
    elif enclosure.licensing.lower() == "hpe oneview advanced w/o ilo":
        C7000AddEnclosures.tick_licensing_hp_oneview_advanced_wo_ilo()
        logger.info("Selected licensing for OneView w/o iLO")
    else:
        ui_lib.fail_test("Invalid value is provided for licensing")


def _add_firmware_bundle_to_enclosure(enclosure, s2l):
    logger._log_to_console_and_log_file("Selecting firmware baseline..")
    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_COMBO_FIRMWARE_BASELINE)
    firmwareListObj = FusionEnclosuresPage.ID_COMBO_FIRMWARE_BASELINE_LIST % enclosure.spp.strip()
    s2l.mouse_over(firmwareListObj)
    s2l.mouse_down(firmwareListObj)
    s2l.mouse_up(firmwareListObj)
    selectedFW = s2l.get_text(FusionEnclosuresPage.ID_COMBO_FIRMWARE_BASELINE)
    logger._log_to_console_and_log_file("Selected firmware is %s " % selectedFW.encode('utf8'))
    if not selectedFW == enclosure.spp.strip():
        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_BTN_ENCLOSURE_CANCEL)
        return False
    return True


def _create_new_enclosure_group_for_enclosure(enclosure, s2l):
    logger._log_to_console_and_log_file("Typing new enclosure group name..")
    ui_lib.wait_for_element_and_input_text(FusionEnclosuresPage.ID_INPUT_ENCLOSURE_NEW_GROUP, enclosure.newEncGrpName)
    _select_lig(enclosure, s2l)


def _select_lig(enclosure, s2l):
    # selecting LIG
    logger._log_to_console_and_log_file("selecting LIG..")
    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_COMBO_ENCLOSURE_LIG)
    if(ui_lib.wait_for_element(FusionEnclosuresPage.ID_LINK_SEARCH_FOR_ANOTHER)):
        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_LINK_SEARCH_FOR_ANOTHER)
    ui_lib.wait_for_element_and_input_text(FusionEnclosuresPage.ID_INPUT_ENCLOSURE_LIG, enclosure.lig)
    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_COMBO_ENCLOSUE_LIG_LIST % enclosure.lig)


def validate_enclosure_lig(*enc_obj):
    """
    Validate enclosure lig

    This fucntion is to validate enclosure logical Interconnect Group
    """
    selenium2lib = ui_lib.get_s2l()
    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_LABEL):
        navigate()
    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])
    for enclosure in enc_obj:
        # validating the given enclosure is present in the enslosures page if present selecting the enclosure
        logger._log_to_console_and_log_file("Validate LIG for enclosure %s" % enclosure.name)
        ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enclosure.name, PerfConstants.SELECT_ENCLOSURE)
        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enclosure.name):
            ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enclosure.name)
            if ui_lib.wait_for_element(FusionEnclosuresPage.ID_ENCLOSURE_TITLE % enclosure.name, PerfConstants.ENCLOSURE_TITLE):
                logger._log_to_console_and_log_file("Given Enclosure %s is selected" % enclosure.name)
                ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_LINK_INTERCONNECT_BAYS, PerfConstants.DEFAULT_SYNC_TIME)
                ui_lib.wait_for_element(FusionEnclosuresPage.ID_ELEMENT_LI_NAME % enclosure.name, PerfConstants.DEFAULT_SYNC_TIME)
                ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ELEMENT_LI_NAME % enclosure.name, PerfConstants.DEFAULT_SYNC_TIME)
                if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_PAGE_LABEL, PerfConstants.DEFAULT_SYNC_TIME):
                    if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_ELEMENT_LI_LABEL, PerfConstants.DEFAULT_SYNC_TIME):
                        ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_ELEMENT_LIG_NAME, PerfConstants.DEFAULT_SYNC_TIME)
                        strLSTName = selenium2lib._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_LIG_NAME)
                        if strLSTName == enclosure.lig:
                            logger._log_to_console_and_log_file("Enclosure %s is configured with the expected LIG" % enclosure.name)
                            return True
        else:
            logger._log_to_console_and_log_file("Enclosure %s is not present in the appliance" % enclosure.name)
        selenium2lib.capture_page_screenshot()
        return False


def can_not_remove_enclosure(*enc_obj):
    """ Cannot Delete Enclosure

    Arguments:
      <enclosure>
          name*                     --  Name of enclosure as a string.

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.enclosures}
        <enclosures>
            <enclosure name="wpst32" />
            <enclosure name="wpst8" />
        </enclosures>

    """
    navigate()

    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])

    logger.debug("Deleting enclosures...")

    count = 0

    for n, enclosure in enumerate(enc_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(enc_obj), '-' * 14))
        logger.info("Removing a enclosure with name %s" % enclosure.name)
        if not select_enclosure(enclosure.name):
            continue

        C7000RemoveEnclosures.select_actions_remove()
        C7000RemoveEnclosures.wait_unable_remove_dialog_shown()
        C7000RemoveEnclosures.click_close_button()
        count += 1

    if count == 0:
        msg = "no target enclosure exists!"
        logger.warn(msg)
        return False

    ret = True

    if count != len(enc_obj):
        logger.warn("Not able to remove all enclosures!")
        return False

    return ret


def validate_can_not_add_enclosure():
    """ Verify if enclosure add button show when login as a network administrator
    """

    navigate()

    C7000CommonOperationEnclosures.click_action_button()
    C7000VerifyEnclosures.verify_action_add_button_not_exist()
    C7000VerifyEnclosures.verify_add_enclosure_button_not_exist()

    return True


def validate_can_not_edit_enclosure_as_sta(*enc_obj):
    """ Verify if enclosure edit button show when login as a storage administrator

    Arguments:
      <enclosure>
          name*                     --  Name of enclosure as a string.
          new_name*                 --  New enclosure name to change.

    * Required Arguments

    Example:
        data/editenclosures -> @{TestData.editenclosures}
        <editenclosures>
            <enclosure name="wpst32" new_name="wpst32_new"/>
            <enclosure name="wpst32_new" new_name="wpst32"/>
        </editenclosures>

    """

    navigate()

    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])

    count = 0
    enclosure_len = len(enc_obj)
    for n, enclosure in enumerate(enc_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(enc_obj), '-' * 14))
        logger.info("Editing a enclosure with name %s" % enclosure.name)
        if not select_enclosure(enclosure.name):
            continue

        C7000CommonOperationEnclosures.click_action_button()
        C7000VerifyEnclosures.verify_action_edit_button_not_exist()
        count += 1

    if count == 0:
        logger.warn("no enclosure edit verified!")
        return False

    if count != enclosure_len:
        logger.warn("error encounter when verify edit enclosure")
        return False

    return True


def validate_can_not_edit_enclosure(*enc_obj):
    """ Edit Enclosure with invalid enclosure name

    Arguments:
      <enclosure>
          name*                     --  Name of enclosure as a string.
          new_name*                 --  New enclosure name to change, need to include invalid char.

    * Required Arguments

    Example:
        data/editenclosures -> @{TestData.editenclosures}
        <editenclosures>
            <enclosure name="wpst32" new_name="wpst32_%^&"/>
        </editenclosures>

    """
    navigate()

    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])

    count = 0
    enclosure_len = len(enc_obj)
    for n, enclosure in enumerate(enc_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(enc_obj), '-' * 14))
        logger.info("Editing a enclosure with name %s" % enclosure.name)
        if not select_enclosure(enclosure.name):
            continue

        C7000EditEnclosures.select_actions_edit()
        C7000EditEnclosures.wait_edit_enclosure_dialog_shown()
        C7000EditEnclosures.input_edit_enclosure_enclosure_name(enclosure.new_name)
        C7000EditEnclosures.click_edit_enclosure_ok()
        C7000EditEnclosures.wait_invalid_name_error_shown()
        C7000EditEnclosures.click_edit_enclosure_cancel()

        count += 1

    if count == 0:
        logger.warn("no enclosure edited!")
        return False

    if count != enclosure_len:
        logger.warn("error encounter when edit enclosure")
        return False

    return True


def validate_interconnect_error_state(*enc_obj):
    """ Verify if interconnect which not in OK state has error message

    Arguments:
      <enclosure>
          name*                     --  Name of enclosure as a string.
          ic_count                  --  Enclosure interconnect count.

    * Required Arguments

    Example:
        data/icstateenclosures -> @{TestData.icstateenclosures}
        <icstateenclosures>
            <enclosure name="wpst32"/>
            <enclosure name="wpst22" ic_count="8"/>
        </icstateenclosures>

    """

    navigate()

    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])

    count = 0
    enclosure_len = len(enc_obj)
    for n, enclosure in enumerate(enc_obj):
        logger.info("Verify a enclosure interconnects with name %s" % enclosure.name)
        if not select_enclosure(enclosure.name):
            continue

        FusionUIBase.select_view_by_name('Interconnects')
        bay_count = 8
        if hasattr(enclosure, "ic_count"):
            bay_count = int(enclosure.ic_count)

        for i in range(bay_count):
            bay_num = i + 1
            if not C7000VerifyEnclosures.verify_interconnect_status(bay_num, "ok", 5, False):
                if not C7000VerifyEnclosures.verify_interconnect_bay_empty(bay_num):
                    C7000CommonOperationEnclosures.click_interconnect_interconnect(bay_num)
                    BuiltIn().sleep(3)
                    VerifyInterconnects.verify_notification_shown()
                    CommonOperationInterconnects.click_enclosure()
                    BuiltIn().sleep(5)
                    FusionUIBase.select_view_by_name('Interconnects')

        count += 1

    if count == 0:
        logger.warn("no enclosure interconnect state verified!")
        return False

    if count != enclosure_len:
        logger.warn("error encounter when verify enclosure interconnect state")
        return False

    return True


def validate_interconnect_ok_state(*enc_obj):
    """ Verify if interconnect which in OK state

    Arguments:
      <enclosure>
          name*                     --  Name of enclosure as a string.
          ic_count                  --  Enclosure interconnect count.

    * Required Arguments

    Example:
        data/icstateenclosures -> @{TestData.icstateenclosures}
        <icstateenclosures>
            <enclosure name="wpst32"/>
            <enclosure name="wpst22" ic_count="8"/>
        </icstateenclosures>

    """

    navigate()

    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])

    count = 0
    enclosure_len = len(enc_obj)
    for n, enclosure in enumerate(enc_obj):
        logger.info("Verify a enclosure interconnects with name %s" % enclosure.name)
        if not select_enclosure(enclosure.name):
            continue

        FusionUIBase.select_view_by_name('Interconnects')
        bay_count = 8
        if hasattr(enclosure, "ic_count"):
            bay_count = int(enclosure.ic_count)

        for i in range(bay_count):
            bay_num = i + 1
            if C7000VerifyEnclosures.verify_interconnect_status(bay_num, "ok", 5, False):
                if not C7000VerifyEnclosures.verify_interconnect_bay_empty(bay_num):
                    C7000CommonOperationEnclosures.click_interconnect_interconnect(bay_num)
                    BuiltIn().sleep(3)
                    VerifyInterconnects.verify_status_ok()
                    CommonOperationInterconnects.click_enclosure()
                    BuiltIn().sleep(5)
                    FusionUIBase.select_view_by_name('Interconnects')

        count += 1

    if count == 0:
        logger.warn("no enclosure interconnect state verified!")
        return False

    if count != enclosure_len:
        logger.warn("error encounter when verify enclosure interconnect state")
        return False

    return True


def validate_logical_interconnect_ok_state(*enc_obj):
    """ Verify if logical interconnect which in OK state

    Arguments:
      <enclosure>
          name*                     --  Name of enclosure as a string.
          error_bay*                --  Bays with li in OK state

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.enclosures}
        <enclosures>
            <enclosure name="wpst32" error_bay="1,5"/>
        </enclosures>

    """

    navigate()

    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])

    count = 0
    enclosure_len = len(enc_obj)
    for n, enclosure in enumerate(enc_obj):
        logger.info("Verify a enclosure interconnects with name %s" % enclosure.name)
        if not select_enclosure(enclosure.name):
            continue

        FusionUIBase.select_view_by_name('Interconnects')
        error_bay = enclosure.error_bay.split(',')
        for i in error_bay:
            bay_num = int(i) + 1
            if not C7000VerifyEnclosures.verify_interconnect_bay_empty(bay_num):
                C7000CommonOperationEnclosures.click_interconnect_interconnect(bay_num)
                BuiltIn().sleep(3)
                CommonOperationInterconnects.click_logical_interconnect()
                BuiltIn().sleep(3)
                C7000VerifyLogicalInterconnects.verify_status_ok()
                navigate()
                select_enclosure(enclosure.name)
                FusionUIBase.select_view_by_name('Interconnects')

        count += 1

    if count == 0:
        logger.warn("no enclosure interconnect group state verified!")
        return False

    if count != enclosure_len:
        logger.warn("error encounter when verify enclosure interconnect group state")
        return False

    return True


def validate_logical_interconnect_state(*enc_obj):
    """ Verify logical interconnect state

    Arguments:
      <enclosure>
          name*                     --  Name of enclosure as a string.
          error_bay*                --  Bays with li not in OK state
          ok_bay*                   --  Bays with li in OK state

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.enclosures}
        <enclosures>
            <enclosure name="wpst22" error_bay="1,5" ok_bay="2"/>
        </enclosures>

    """

    navigate()

    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])

    count = 0
    enclosure_len = len(enc_obj)
    for n, enclosure in enumerate(enc_obj):
        logger.info("Verify a enclosure interconnects with name %s" % enclosure.name)
        if not select_enclosure(enclosure.name):
            continue

        FusionUIBase.select_view_by_name('Interconnects')
        error_bay = enclosure.error_bay.split(',')
        ok_bay = enclosure.ok_bay.split(',')
        for i in error_bay:
            if i == "":
                continue
            bay_num = int(i) + 1
            if not C7000VerifyEnclosures.verify_interconnect_bay_empty(bay_num):
                C7000CommonOperationEnclosures.click_interconnect_interconnect(bay_num)
                BuiltIn().sleep(3)
                CommonOperationInterconnects.click_logical_interconnect()
                BuiltIn().sleep(3)
                C7000VerifyLogicalInterconnects.verify_notification_shown()
                navigate()
                select_enclosure(enclosure.name)
                FusionUIBase.select_view_by_name('Interconnects')

        for i in ok_bay:
            if i == "":
                continue
            bay_num = int(i) + 1
            if not C7000VerifyEnclosures.verify_interconnect_bay_empty(bay_num):
                C7000CommonOperationEnclosures.click_interconnect_interconnect(bay_num)
                BuiltIn().sleep(3)
                CommonOperationInterconnects.click_logical_interconnect()
                BuiltIn().sleep(3)
                C7000VerifyLogicalInterconnects.verify_status_ok()
                navigate()
                select_enclosure(enclosure.name)
                FusionUIBase.select_view_by_name('Interconnects')

        count += 1

    if count == 0:
        logger.warn("no enclosure logical interconnect state verified!")
        return False

    if count != enclosure_len:
        logger.warn("error encounter when verify enclosure logical interconnect state")
        return False

    return True


def validate_blade_utilization(*enc_obj):
    """ Verify logical interconnect state

    Arguments:
      <enclosure>
          name*                     --  Name of enclosure as a string.
          error_bay*                --  Bays not have utilization
          ok_bay*                   --  Bays have utilization

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.enclosures}
        <enclosures>
            <enclosure name="wpst22" error_bay="6" ok_bay="1,5"/>
        </enclosures>

    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE)

    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])

    for n, enclosure in enumerate(enc_obj):

        error_bay = enclosure.error_bay.split(',')
        ok_bay = enclosure.ok_bay.split(',')
        for i in error_bay:
            if i == "":
                continue
            bay_name = enclosure.name + ", bay " + i
            CommonOperationServerHardware.click_server_hardware(bay_name)
            BuiltIn().sleep(3)
            if VerifyHardware.verify_hardware_utilization_cpu("collected", 5, False) or VerifyHardware.verify_hardware_utilization_power("collected", 5, False) or VerifyHardware.verify_hardware_utilization_temperature("collected", 5, False):
                return False

        for i in ok_bay:
            if i == "":
                continue
            bay_name = enclosure.name + ", bay " + i
            CommonOperationServerHardware.click_server_hardware(bay_name)
            BuiltIn().sleep(3)
            VerifyHardware.verify_hardware_utilization_cpu("collected")
            VerifyHardware.verify_hardware_utilization_power("collected")
            VerifyHardware.verify_hardware_utilization_temperature("collected")

    return True


def validate_blade_unsupported(*enc_obj):
    """ Verify logical interconnect state

    Arguments:
      <enclosure>
          name*                           --  Name of enclosure as a string.
          unsupported_bay*                --  Bays not supported

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.enclosures}
        <enclosures>
            <enclosure name="wpst22" unsupported_bay="7"/>
        </enclosures>

    """
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE)

    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])

    for n, enclosure in enumerate(enc_obj):
        unsupported_bay = enclosure.unsupported_bay.split(',')
        for i in unsupported_bay:
            if i == "":
                continue
            bay_name = enclosure.name + ", bay " + i
            CommonOperationServerHardware.click_server_hardware(bay_name)
            VerifyHardware.verify_hardware_state("Unsupported")

    return True


def validate_interconnect_group_and_enclosure_group_exist(*enc_obj):
    """ Verify if logical interconnect group and enclosure group exist after enclosure was removed

    Arguments:
      <enclosure>
          name*                     --  Name of enclosure as a string.
          encgroup*                 --  enclosure group name
          lig*                      --  lig name

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.enclosures}
        <enclosures>
            <enclosure name="wpst32" encgroup="wpst32group" lig="wpst32lig"/>
        </enclosures>

    """

    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])

    logger.info("Navigate to EG page")
    FusionUIBase.navigate_to_section(SectionType.ENCLOSURE_GROUPS)
    for n, enclosure in enumerate(enc_obj):
        C7000CommonOperationEnclosureGroups.verify_enclosure_group_exist(enclosure.encgroup)

    logger.info("Navigate to LIG page")
    FusionUIBase.navigate_to_section(SectionType.LOGICAL_INTERCONNECT_GROUPS)
    for n, enclosure in enumerate(enc_obj):
        CommonOperationLogicalInterconnectGroups.verify_lig_exist(enclosure.ligname)

    return True


def validate_interconnect_group_and_enclosure_group_not_exist(*enc_obj):
    """ Verify if logical interconnect group and enclosure group exist after enclosure was removed

    Arguments:
      <enclosure>
          name*                     --  Name of enclosure as a string.
          encgroup*                 --  enclosure group name
          lig*                      --  lig name

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.enclosures}
        <enclosures>
            <enclosure name="wpst32" encgroup="wpst32group" lig="wpst32lig"/>
        </enclosures>

    """

    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])

    logger.info("Navigate to EG page")
    FusionUIBase.navigate_to_section(SectionType.ENCLOSURE_GROUPS)
    for n, enclosure in enumerate(enc_obj):
        C7000CommonOperationEnclosureGroups.verify_enclosure_group_not_exist(enclosure.encgroup)

    logger.info("Navigate to LIG page")
    FusionUIBase.navigate_to_section(SectionType.LOGICAL_INTERCONNECT_GROUPS)
    for n, enclosure in enumerate(enc_obj):
        CommonOperationLogicalInterconnectGroups.verify_lig_not_exist(enclosure.ligname)

    return True


def validate_licensing_policy(enc_obj):
    """ Verify licensing policy

    Arguments:
      <enclosure>
          name*                     --  Name of enclosure as a string.
          licensing*                --  enclosure licensing policy

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.enclosures}
        <enclosures>
            <enclosure name="wpst32" licensing="HPE OneViewAdvanced" />
        </enclosures>

    """

    navigate()
    count = 0
    enclosure_len = len(enc_obj)
    for n, enclosure in enumerate(enc_obj):
        logger.info("Verify a enclosure interconnects with name %s" % enclosure.name)
        if not select_enclosure(enclosure.name):
            continue
        BuiltIn().sleep(5)
        C7000VerifyEnclosures.verify_overview_general_server_licensing_policy(enclosure.licensing)

        count += 1

    if count == 0:
        logger.warn("no enclosure logical interconnect state verified!")
        return False

    if count != enclosure_len:
        logger.warn("error encounter when verify enclosure logical interconnect state")
        return False

    return True


def select_enclosure(enc_name):
    """ Selects the respective enclosure from the enclosure list """
    navigate()

    logger.info("Selecting a enclosure with name '{0}'".format(enc_name))
    if C7000VerifyEnclosures.verify_enclosure_exist(enc_name, fail_if_false=False):
        C7000CommonOperationEnclosures.click_enclosure(enc_name)
        C7000CommonOperationEnclosures.wait_enclosure_selected(enc_name)
        return True
    else:
        logger.warn("Enclosure '{0}' does not exist".format(enc_name))
        ui_lib.get_s2l().capture_page_screenshot()
        return False


def navigate_to_fan_details_page():
    """ Navigate to fan details page """

    flag = False

    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()

    # Verify fan bays link is available under overview combo selection and navigate to FAN UI details page
    # by clicking on the FAN bays link
    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_FAN_LABEL):
        if _fan_link_presence():
            ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_COMBO_MENU_OVERVIEW)
            ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_LINK_FAN_BAYS)
            ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_FAN_LABEL)
            logger._log_to_console_and_log_file('Navigated successfully to FAN details UI Page')
            flag = True
        else:
            ui_lib.fail_test('Failed to navigate to fans details page')
            flag = False
    else:
        logger._log_to_console_and_log_file('Already in FAN details UI page')
        flag = True
    return flag


def _fan_link_presence():

    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_LABEL):
        navigate()
    # This check the fan bays link is available under Combo menu
    if ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ELEMENT_PANEL_SELECTOR):
        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_LINK_FAN_BAYS):
            logger._log_to_console_and_log_file('The fan link is available')
            ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ELEMENT_PANEL_SELECTOR)
            return True
        else:
            ui_lib.fail_test('The fan link is not available')
            return False
    return False


def _convert_fan_list_to_ints(str_type):
    """ This function will handle removing all the regular expressions and converting it into a list for fan rules
    Example:  This function converts regular expression " 8 (fan bays 1, 2, 4, 5, 6, 7, 9 and 10) " into a list like this [8,1,2,4,5,6,7,9,10]
    where 8 indicates the fan rule and numbers in the list indicate the fan bays populated for this fan rule """

    if "and" in str_type:
        temp_list = str_type.split('and')
        reg_exp1 = re.sub(r'\D', "", temp_list[0])
        reg_exp2 = re.sub(r'\D', "", temp_list[1])
        final_list = map(int, reg_exp1)
        final_list.append(int(reg_exp2))
    elif "all" in str_type:
        list1 = str_type.split(" ")
        list2 = list1[1:]
        str1 = " ".join(list2)
        expr1 = re.sub(r'\W', " ", str1).strip()
        final_list = (int(list1[0]), expr1)
    return final_list


def get_fan_rules():
    """ Get fan rules for the selected enclosure """

    s2l = ui_lib.get_s2l()

    rule_dict = {}
    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()

    # This navigates to FAN details UI page
    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_FAN_LABEL):
        navigate_to_fan_details_page()
        ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_FAN_LABEL)

    # This retrieve FAN rules for the selected enclosure
    if ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_FAN_LABEL):
        fan_rule_label = str(s2l.get_text(FusionEnclosuresPage.ID_LABEL_FANS_REQUIRED))
        Device_bay_label = str(s2l.get_text(FusionEnclosuresPage.ID_LABEL_DEVICE_BAYS_COOLED))
        fanrule_number = str(s2l.get_text(FusionEnclosuresPage.ID_ELEMENT_NUMBER_OF_FANS))
        Devicebays_cooled = str(s2l.get_text(FusionEnclosuresPage.ID_ELEMENT_NUMBER_OF_DEVICES))

        if (fanrule_number != "null" and Devicebays_cooled != "null"):
            if "and" in fanrule_number:
                fan_rule_list = _convert_fan_list_to_ints(fanrule_number)
                rule_dict[fan_rule_label] = fan_rule_list
            elif 'all' in fanrule_number:
                fan_rule_list = _convert_fan_list_to_ints(fanrule_number)
                rule_dict[fan_rule_label] = fan_rule_list
            rule_dict[Device_bay_label] = Devicebays_cooled
            logger._log_to_console_and_log_file('Fan rule has been retrieved successfully')
        else:
            logger._log_to_console_and_log_file('Failed to retrieve the fan rules')
    return rule_dict


def mouse_hover_fan_bay(fan_bay):
    """ Mouse hover on fan bay and get fan bay values """

    logger._log_to_console_and_log_file(" Mouse hover on fan bay %s" % fan_bay)
    s2l = ui_lib.get_s2l()

    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()

    # This handles the condition if the current page is not the enclosure overview page for FAN
    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_ELEMENT_OVERVIEW_FAN_TABLE):
        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ELEMENT_PANEL_SELECTOR, PerfConstants.DEFAULT_SYNC_TIME)
        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_LINK_OVERVIEW):
            ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_LINK_OVERVIEW, PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_ELEMENT_OVERVIEW_FAN_TABLE, PerfConstants.DEFAULT_SYNC_TIME)

    # This retrieves the values of the bay after mouse hover on a user selected fan bay
    if ui_lib.wait_for_element(FusionEnclosuresPage.ID_ELEMENT_OVERVIEW_FAN_BAY % fan_bay):
        ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_ELEMENT_OVERVIEW_FAN_BAY % fan_bay, PerfConstants.DEFAULT_SYNC_TIME)
        s2l.mouse_over(FusionEnclosuresPage.ID_ELEMENT_OVERVIEW_FAN_BAY % fan_bay)
        time.sleep(PerfConstants.FAN_DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_ELEMENT_OVERVIEW_FAN_BAY, PerfConstants.DEFAULT_SYNC_TIME)
    # This code is related to workaround for DOM exception, stale element issue
        cnt = 0
        while(cnt < 8):
            try:
                element = ui_lib.wait_for_element_class(FusionEnclosuresPage.ID_ELEMENT_TOOLTIP_FAN_HEALTH_STATUS % fan_bay, True, False)
                values = s2l.get_text(FusionEnclosuresPage.ID_ELEMENT_OVERVIEW_FAN_BAY % fan_bay)
                res_list = values.split('\n')
                temp_status = element.get_attribute('innerHTML')
                cnt = 8
            except:
                cnt = cnt + 1
        res_list.append(temp_status)
        return res_list
    else:
        logger._warn("Failed to mouse hover on bay %s since it is empty,please select a populated bay" % fan_bay)


def navigate_to_fan_details_from_tooltip(fan_bay):
    """ Navigate to fan details page from tooltip in the rear view of the enclosure page """

    flag = False

    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()

    # This handles the condition if the current page is not the enclosure overview page for FAN
    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_ELEMENT_OVERVIEW_FAN_TABLE):
        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ELEMENT_PANEL_SELECTOR, PerfConstants.DEFAULT_SYNC_TIME)
        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_LINK_OVERVIEW):
            ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_LINK_OVERVIEW, PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_ELEMENT_OVERVIEW_FAN_TABLE, PerfConstants.DEFAULT_SYNC_TIME)

    # This checks if the tooltip for the selected bay is available and will click on it
    # and verify navigation to details page.
    if ui_lib.wait_for_element(FusionEnclosuresPage.ID_ELEMENT_OVERVIEW_FAN_BAY % fan_bay):
        time.sleep(PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_ELEMENT_OVERVIEW_FAN_BAY % fan_bay, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ELEMENT_OVERVIEW_FAN_BAY % fan_bay)
        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_LINK_OVERVIEW_TOOLTIP_FAN_BAY % fan_bay):
            ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_LINK_OVERVIEW_TOOLTIP_FAN_BAY % fan_bay, PerfConstants.DEFAULT_SYNC_TIME)
            if ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_FAN_LABEL):
                logger._log_to_console_and_log_file("Navigated successfully to FAN details UI Page from fan bay %s" % fan_bay)
                flag = True
            else:
                ui_lib.fail_test("Failed to navigate to FAN details UI Page from fan bay %s" % fan_bay)
        else:
            ui_lib.fail_test("The fan link is missing for fan bay %s" % fan_bay)
    else:
        logger._warn(' Failed to navigate to FAN details UI since bay %s is empty ' % fan_bay)
    return flag

    # This function is used to get the fan lists by passing the respective element name.


def _get_fanlist(element_name):

    # This code is related to workaround for DOM exception, stale element issue
    cnt = 0
    while(cnt < 8):
        try:
            return [el.get_attribute('innerHTML') for el in ui_lib.wait_for_element_class(element_name, False, False)]
            cnt = 8
        except:
            cnt = cnt + 1

    # This function provides a modified list to workaround the issue where the FAN state gets appended
    # with Fan model name due to same class name for both the UI objects.


def _get_state_list(fan_state_list, value):
    if '' in fan_state_list:
        fan_state_list.remove('')
    if value in fan_state_list:
        fan_state_list.remove(value)
        _get_state_list(fan_state_list, value)       # This function will  be executed recursively to remove multiple occurence of "value"
    return fan_state_list


def get_fan_overview():
    """ Get the fan values from fan overview UI page """

    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()

    # This handles the condition if the current page is not the enclosure overview page for FAN
    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_ELEMENT_OVERVIEW_FAN_TABLE):
        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ELEMENT_PANEL_SELECTOR, PerfConstants.DEFAULT_SYNC_TIME)
        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_LINK_OVERVIEW):
            ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_LINK_OVERVIEW, PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_ELEMENT_OVERVIEW_FAN_TABLE, PerfConstants.DEFAULT_SYNC_TIME)

    logger._log_to_console_and_log_file(" Getting Fan status from overview ")

    table = {}
    inner_table = {}

    # Getting the fan lists using the above function (get_fanlist) for fan bay,state,model and status
    fan_name_list = _get_fanlist(FusionEnclosuresPage.ID_ELEMENT_FAN_NAME_ROW)
    fan_status_list = _get_fanlist(FusionEnclosuresPage.ID_ELEMENT_FAN_STATUS_ROW)
    fan_model_list = _get_fanlist(FusionEnclosuresPage.ID_ELEMENT_FAN_MODEL_ROW)
    fan_state_list = _get_fanlist(FusionEnclosuresPage.ID_ELEMENT_FAN_STATE_ROW)

    # Since class names are same for both fan state and model,fan model data gets appended with fan state data.
    # Hence editing the fan_state list and removing the fan model from it using the function (get_state_list)
    fan_state_list = _get_state_list(fan_state_list, 'Active Cool 200 Fan')

    # This handles the situation of fan state not visible when status is 'ok'
    for index, value in enumerate(fan_status_list):
        if value == 'ok':
            fan_state_list.insert(index, ' ')

    # This handles the situation of fan model not visible when state is 'Missing'
    for index, value in enumerate(fan_state_list):
        if value == 'Missing':
            fan_model_list.insert(index, '')

    # Handling the situation when the fan bay is empty and this will add empty string
    # to the respective index for all the list
    for index, value in enumerate(fan_model_list):
        if value == "empty":
            fan_name_list.insert(index, value)
            fan_status_list.insert(index, value)
            fan_state_list.insert(index, value)

    # Creating a nested dictionary from the above list
    for index in range(len(fan_model_list)):
        inner_table["name"] = fan_name_list[index].strip()
        inner_table["status"] = fan_status_list[index].strip()
        inner_table["state"] = fan_state_list[index].strip()
        inner_table["model"] = fan_model_list[index].strip()
        key = "FAN" + str(index + 1)
        table[key] = inner_table.copy()
    return table


def get_fan_details():
    """ Get the fan values in the table from the fan details UI page """
    s2l = ui_lib.get_s2l()

    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()

    # This navigates to FAN details UI page
    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_FAN_LABEL):
        navigate_to_fan_details_page()
        ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_PAGE_FAN_LABEL, PerfConstants.DEFAULT_SYNC_TIME)

    logger._log_to_console_and_log_file(" Getting Fan Details ")

    table = {}
    inner_table = {}

    # This code is related to workaround for DOM exception, stale element issue
    cnt = 0
    while(cnt < 8):
        try:

            # Getting the row and column list
            fan_model_list = [str(ui_lib.get_webelement_attribute("text", el)) for el in ui_lib.wait_for_element_class(FusionEnclosuresPage.ID_ELEMENT_FAN_MODEL_LIST, False, False)]
            fan_attribute_list = [str(ui_lib.get_webelement_attribute("text", el)).lower() for el in ui_lib.wait_for_element_class(FusionEnclosuresPage.ID_ELEMENT_FAN_HEADER_LIST, False, False)]
            fan_attribute_list[0] = "status"    # Fill in the value for empty UI "Status" field header
            cnt = 8
        except:
            cnt = cnt + 1
    # Creating a nested dictionary by using get_table_cell keyword
    for row in range(len(fan_model_list)):
        for col, header in enumerate(fan_attribute_list):

            # This code is related to workaround for DOM exception, stale element issue
            count = 0
            while (count < 8):
                try:
                    if header == "status":
                        element = ui_lib.wait_for_element_class(FusionEnclosuresPage.ID_ELEMENT_FAN_HLTICON_LIST % (row + 1), True, False)
                        if element is None:
                            inner_table[header] = "empty"
                            count = 8
                        else:
                            inner_table[header] = format(str(element.get_attribute("innerHTML")))
                            count = 8
                    else:
                        inner_table[header] = s2l.get_table_cell(FusionEnclosuresPage.ID_ELEMENT_DETAILS_FAN_TABLE, row + 2, col + 1)
                        count = 8
                except:
                    count = count + 1
        key = "FAN" + str(row + 1)
        table[key] = inner_table.copy()

    return table


def get_fan_attribute(page_name, bay_num, attribute):
    """ Get Fan attribute for the given bay number """

    logger._log_to_console_and_log_file("Getting Fan attribute for bay %s" % bay_num)

    # Getting the specific status attribute value from dictionary either from fan overview/details page
    try:
        if page_name.lower() == "overview":
            fan_dict = get_fan_overview()
        elif page_name.lower() == "details":
            fan_dict = get_fan_details()
        else:
            logger._log_to_console_and_log_file("Failed to retrieve fan attributes.Please provide the correct page")
            return
        key = "FAN" + str(bay_num)
        if attribute.lower() == "all":
            return fan_dict[key]
        else:
            return fan_dict[key][attribute]
    except:
        logger._warn("Failed to retrieve Fan attributes for bay %s" % bay_num)


def get_fan_count(fan_dict, status_type):
    """  Get the fan count for the given status type """

    logger._log_to_console_and_log_file(" Getting the fan Count ")

    status_type.lower()
    total = len(fan_dict)
    status = []
    status_failed = []
    status_ok = []
    status_unknown = []
    status_degraded = []
    status_not_present = []
    status_all = []
    try:
        # Create a list based on the status type
        for k, v in fan_dict.items():
            status.append(v['status'])
        # Getting the fan status for all the fan bay numbers
        for index in range(len(status)):
            index = index + 1
            status_all.append(index)
            key = "FAN" + str(index)
            value = fan_dict[key]['status']
            if value == 'Failed':
                status_failed.append(index)
            elif value == 'ok':
                status_ok.append(index)
            elif value == 'warning':
                status_degraded.append(index)
            elif value == 'unknown':
                status_ok.append(index)
            elif value == 'empty':
                status_not_present.append(index)

        # Getting the fan count for the status type
        if status_type == 'failed':
            count = status.count('Failed')
            status_failed.insert(0, count)
            return status_failed
        elif status_type == 'ok':
            count = status.count('ok')
            status_ok.insert(0, count)
            return status_ok
        elif status_type == 'degraded':
            count = status.count('warning')
            status_degraded.insert(0, count)
            return status_degraded
        elif status_type == 'unknown':
            count = status.count('unknown')
            status_unknown.insert(0, count)
            return status_unknown
        elif status_type == 'not present':
            count = status.count('empty')
            status_not_present.insert(0, count)
            return status_not_present
        elif status_type == 'present':
            count = total - status.count('empty')
            for x in status_not_present:
                status_all.remove(x)
            status_all.insert(0, count)
            return status_all
        elif status_type == 'all':
            count = total
            status_all.insert(0, count)
            return status_all
        else:
            logger._log_to_console_and_log_file("Fail to get the count of FAN.  Invalid parameter passed")

    except:
        logger._log_to_console_and_log_file("Fail to get the count of FAN STATUS")


def get_power_supply_overview(enc_name):
    """ Get the power supply overview values in the enclosure front view on the Enclosures page

    """
    logger._log_to_console_and_log_file(" ")
    table = {}

    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()

    logger._log_to_console_and_log_file("Navigating to Power Supply Overview for enclosure %s" % enc_name)
    ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enc_name, PerfConstants.SELECT_ENCLOSURE)
    if ui_lib.wait_for_element(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enc_name):
        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enc_name)
        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_ENCLOSURE_TITLE % enc_name, PerfConstants.ENCLOSURE_TITLE):
            logger._log_to_console_and_log_file("Given Enclosure %s is selected" % enc_name)
            if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_POWERSUPPLY_BAYS):
                ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ELEMENT_PANEL_SELECTOR, PerfConstants.DEFAULT_SYNC_TIME)
                if ui_lib.wait_for_element(FusionEnclosuresPage.ID_LINK_OVERVIEW):
                    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_LINK_OVERVIEW, PerfConstants.DEFAULT_SYNC_TIME)
                    ui_lib.wait_for_element(FusionEnclosuresPage.ID_POWERSUPPLY_BAYS, PerfConstants.DEFAULT_SYNC_TIME)

            inner_table = {}
            ps_health_list = [el.get_attribute('innerHTML') for el in ui_lib.wait_for_element_class(FusionEnclosuresPage.ID_POWERSUPPLY_HEALTH, False, False)]
            ps_model_list = [el.get_attribute('innerHTML') for el in ui_lib.wait_for_element_class(FusionEnclosuresPage.ID_POWERSUPPLY_MODEL, False, False)]
            ps_name_list = [el.get_attribute('innerHTML') for el in ui_lib.wait_for_element_class(FusionEnclosuresPage.ID_POWERSUPPLY_NAME, False, False)]

            for index, value in enumerate(ps_model_list):
                if value == "empty":
                    ps_health_list.insert(index, 'Power Supply Bay Empty')
                    ps_name_list.insert(index, value)

            for index in range(len(ps_model_list)):
                inner_table["Status"] = ps_health_list[index].strip()
                inner_table["Name"] = ps_name_list[index].strip()
                inner_table["Model"] = ps_model_list[index].strip()
                key = "PS" + str(index + 1)
                table[key] = inner_table.copy()

        else:
            logger._log_to_console_and_log_file("Unable to select enclosure %s" % enc_name)
    else:
        logger._log_to_console_and_log_file("Unable to select enclosure %s" % enc_name)

    return table


def get_power_supply_details(enc_name):
    """ Get the power supply values in the table on the power supply details page

    """
    logger._log_to_console_and_log_file(" ")

    s2l = ui_lib.get_s2l()
    table = {}

    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()

    logger._log_to_console_and_log_file("Navigating to Power Supply Details for enclosure %s" % enc_name)
    ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enc_name, PerfConstants.SELECT_ENCLOSURE)
    if ui_lib.wait_for_element(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enc_name):
        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enc_name)
        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_ENCLOSURE_TITLE % enc_name, PerfConstants.ENCLOSURE_TITLE):
            logger._log_to_console_and_log_file("Given Enclosure %s is selected" % enc_name)
            if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_POWERSUPPLY_BAYS_LABEL):
                ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ELEMENT_PANEL_SELECTOR, PerfConstants.DEFAULT_SYNC_TIME)
                if ui_lib.wait_for_element(FusionEnclosuresPage.ID_POWERSUPPLY_DETAILS_LINK):
                    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_POWERSUPPLY_DETAILS_LINK, PerfConstants.DEFAULT_SYNC_TIME)
                    ui_lib.wait_for_element(FusionEnclosuresPage.ID_POWERSUPPLY_BAYS_LABEL, PerfConstants.DEFAULT_SYNC_TIME, fail_if_false=True)
                else:
                    logger._log_to_console_and_log_file("Unable to navigate to Power Supply Details for enclosure %s" % enc_name)
            inner_table = {}

            ps_model_list = [ui_lib.get_webelement_attribute("text", el) for el in ui_lib.wait_for_element_class(FusionEnclosuresPage.ID_POWERSUPPLY_LIST_MODEL, False, False)]
            ps_attribute_list = [ui_lib.get_webelement_attribute("text", el) for el in ui_lib.wait_for_element_class(FusionEnclosuresPage.ID_POWERSUPPLY_LIST_HEADER, False, False)]
            ps_attribute_list[0] = "Status"       # Fill in value for the empty UI "Status" field header

            for row in range(len(ps_model_list)):
                for col, header in enumerate(ps_attribute_list):
                    if header == "Status":
                        element = ui_lib.wait_for_element_class(FusionEnclosuresPage.ID_POWERSUPPLY_DETAILS_HEALTH_ICON % str(row + 1), True, False)
                        if element is None:
                            inner_table[header] = "Power Supply Bay Empty"
                        else:
                            inner_table[header] = element.get_attribute('innerHTML')
                    else:
                        inner_table[header] = s2l.get_table_cell(FusionEnclosuresPage.ID_POWERSUPPLY_LIST, row + 2, col + 1)
                key = "PS" + str(row + 1)
                table[key] = inner_table.copy()

        else:
            logger._log_to_console_and_log_file("Unable to select enclosure %s" % enc_name)
    else:
        logger._log_to_console_and_log_file("Unable to select enclosure %s" % enc_name)

    return table


def get_power_supply_attribute(enc_name, page, bay_no, attribute):
    """ Get the power supply attribute for the PS in the given bay number

    """
    logger._log_to_console_and_log_file(" Getting Power Supply Attribute ")

    try:

        if page.lower() == "details":
            logger._log_to_console_and_log_file(" Getting Power Supply Attribute from details page for bay %s" % bay_no)
            ps_dict = get_power_supply_details(enc_name)
        elif page.lower() == "overview":
            logger._log_to_console_and_log_file(" Getting Power Supply Attribute from overview page for bay %s" % bay_no)
            ps_dict = get_power_supply_overview(enc_name)
        else:
            logger._log_to_console_and_log_file("Fail to get the Power Supply Attribute for the bay %s.  Provide the correct page") % bay_no
            return
        key = "PS" + str(bay_no)
        if attribute.lower() == "all":
            return ps_dict[key]
        else:
            return ps_dict[key][attribute]

    except:
        logger._log_to_console_and_log_file("Fail to get the Power Supply Attribute for bay %s" % bay_no)


def get_power_supply_count(ps_dict, type):
    """ Get the power supply count for the given type


    """
    logger._log_to_console_and_log_file(" Getting the Power Supply Count ")

    type.lower()
    total = len(ps_dict)
    status = []
    status_failed = []
    status_ok = []
    status_unknown = []
    status_degraded = []
    status_not_present = []
    status_all = []
    try:

        for k, v in ps_dict.items():
            status.append(v['Status'])

        for index in range(len(status)):
            index = index + 1
            status_all.append(index)
            key = "PS" + str(index)
            value = ps_dict[key]['Status']
            if value == 'error':
                status_failed.append(index)
            elif value == 'ok':
                status_ok.append(index)
            elif value == 'warning':
                status_degraded.append(index)
            elif value == 'unknown':
                status_ok.append(index)
            elif value == 'Power Supply Bay Empty':
                status_not_present.append(index)

        if type == 'failed':
            count = status.count('error')
            status_failed.insert(0, count)
            return status_failed
        elif type == 'ok':
            count = status.count('ok')
            status_ok.insert(0, count)
            return status_ok
        elif type == 'degraded':
            count = status.count('warning')
            status_degraded.insert(0, count)
            return status_degraded
        elif type == 'unknown':
            count = status.count('unknown')
            status_unknown.insert(0, count)
            return status_unknown
        elif type == 'not present':
            count = status.count('Power Supply Bay Empty')
            status_not_present.insert(0, count)
            return status_not_present
        elif type == 'present':
            count = total - status.count('Power Supply Bay Empty')
            for x in status_not_present:
                status_all.remove(x)
            status_all.insert(0, count)
            return status_all
        elif type == 'all':
            count = total
            status_all.insert(0, count)
            return status_all
        else:
            logger._log_to_console_and_log_file("Fail to get the count of Power Supply STATUS.  Invalid parameter passed")

    except:
        logger._log_to_console_and_log_file("Fail to get the count of Power Supply STATUS")


def navigate_to_powersupply_details_from_overview_bay_popup(enc_name, bay_no):
    """ Navigate to power supply details page from link in bay hover menu in overview page

    """
    s2l = ui_lib.get_s2l()

    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()

    logger._log_to_console_and_log_file("Navigating to Power Supply Overview for enclosure %s" % enc_name)
    ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enc_name, PerfConstants.SELECT_ENCLOSURE)
    if ui_lib.wait_for_element(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enc_name):
        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enc_name)
        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_ENCLOSURE_TITLE % enc_name, PerfConstants.ENCLOSURE_TITLE):
            logger._log_to_console_and_log_file("Given Enclosure %s is selected" % enc_name)
            if not ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_POWERSUPPLY_BAYS):
                ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ELEMENT_PANEL_SELECTOR, PerfConstants.DEFAULT_SYNC_TIME)
                if ui_lib.wait_for_element(FusionEnclosuresPage.ID_LINK_OVERVIEW):
                    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_LINK_OVERVIEW, PerfConstants.DEFAULT_SYNC_TIME)
                    ui_lib.wait_for_element(FusionEnclosuresPage.ID_POWERSUPPLY_BAYS, PerfConstants.DEFAULT_SYNC_TIME)

            if ui_lib.wait_for_element(FusionEnclosuresPage.ID_POWERSUPPLY_POPUP % bay_no):
                fan_locator = FusionEnclosuresPage.ID_ELEMENT_OVERVIEW_FAN_BAY % 10
                # Due to UI issue with popup window of blades covering PS bays, implementing workaround to move to Fan bay first, then move to PS bay
                s2l.mouse_over(fan_locator)
                ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_POWERSUPPLY_POPUP % str(bay_no))
                if ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_LINK_POWERSUPPLY_DETAILS % bay_no):
                    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_LINK_POWERSUPPLY_DETAILS % bay_no)
                    if ui_lib.wait_for_element(FusionEnclosuresPage.ID_POWERSUPPLY_BAYS_LABEL, PerfConstants.DEFAULT_SYNC_TIME):
                        logger._log_to_console_and_log_file('Navigated successfully to Power Supply details Page')
                        return True
                    else:
                        logger._log_to_console_and_log_file('Failed to navigate to Power Supply details Page ')
                else:
                    logger._log_to_console_and_log_file("The power supply link is missing")
            else:
                logger._log_to_console_and_log_file(" Failed to navigate to Power Supply details due to empty PS bay")
        else:
            logger._log_to_console_and_log_file("Unable to select enclosure %s" % enc_name)
    else:
        logger._log_to_console_and_log_file("Unable to select enclosure %s" % enc_name)

    s2l.capture_page_screenshot()
    return False


def get_powersupply_data_from_mouseover(enc_name, bay_no):
    """ Get Power Supply data from bay hover menu in overview page

       Move the mouse over the PS bay to enable popup and read the data from the popup if it is visible

    """
    logger._log_to_console_and_log_file(" ")
    s2l = ui_lib.get_s2l()
    ps_dict = {}

    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()

    logger._log_to_console_and_log_file("Navigating to Power Supply Overview for enclosure %s" % enc_name)
    ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enc_name, PerfConstants.SELECT_ENCLOSURE)
    if ui_lib.wait_for_element(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enc_name):
        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enc_name)
        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_ENCLOSURE_TITLE % enc_name, PerfConstants.ENCLOSURE_TITLE):
            logger._log_to_console_and_log_file("Given Enclosure %s is selected" % enc_name)
            if not ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_POWERSUPPLY_BAYS):
                ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ELEMENT_PANEL_SELECTOR, PerfConstants.DEFAULT_SYNC_TIME)
                if ui_lib.wait_for_element(FusionEnclosuresPage.ID_LINK_OVERVIEW):
                    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_LINK_OVERVIEW, PerfConstants.DEFAULT_SYNC_TIME)
                    ui_lib.wait_for_element(FusionEnclosuresPage.ID_POWERSUPPLY_BAYS, PerfConstants.DEFAULT_SYNC_TIME)

            if ui_lib.wait_for_element(FusionEnclosuresPage.ID_POWERSUPPLY_POPUP % bay_no):
                # Due to UI issue with popup window of blades covering PS bays, implementing workaround to move to Fan bay first, then move to PS bay
                fan_locator = FusionEnclosuresPage.ID_ELEMENT_OVERVIEW_FAN_BAY % 10
                ui_lib.wait_for_element_visible(fan_locator, PerfConstants.DEFAULT_SYNC_TIME)
                s2l.mouse_over(fan_locator)
                ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_POWERSUPPLY_BAY_NUMBER % bay_no)
                if ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_POWERSUPPLY_NAME_POPUP % bay_no):
                    element1 = ui_lib.wait_for_element_class(FusionEnclosuresPage.ID_POWERSUPPLY_NAME_POPUP % bay_no, True, False)
                    element2 = ui_lib.wait_for_element_class(FusionEnclosuresPage.ID_POWERSUPPLY_MODEL_POPUP % bay_no, True, False)
                    ps_dict["Name"] = element1.get_attribute('innerHTML').strip()
                    ps_dict["Model"] = element2.get_attribute('innerHTML').strip()
                    element = ui_lib.wait_for_element_class(FusionEnclosuresPage.ID_POWERSUPPLY_HEALTH_POPUP % bay_no + '/span', True, False)
                    if element is None:
                        raise ValueError("Element '%s' not found." % (FusionEnclosuresPage.ID_POWERSUPPLY_HEALTH_POPUP % bay_no))
                    ps_dict["Status"] = element.get_attribute('innerHTML').strip()
            else:
                ps_dict["Status"] = 'Power Supply Bay Empty'
                ps_dict["Model"] = 'empty'

        else:
            logger._log_to_console_and_log_file("Unable to select enclosure %s" % enc_name)
    else:
        logger._log_to_console_and_log_file("Unable to select enclosure %s" % enc_name)

    return ps_dict


def create_enclosures_ip_list():
    """ Get all the existing enclosure(s) name and their IP addresses """
    encl_info_dict = {}
    s2l = ui_lib.get_s2l()
    logger._log_to_console_and_log_file(" Should be at Enclosure UI and to get their names ")

    # Get and create list of enclosure name(s)
    # Create element item with the table's object
    element = ui_lib.wait_for_element_class(FusionEnclosuresPage.ID_TABLE_ENCLOSURE_NAMES, True, False)
    tmp_status = element.get_attribute('innerHTML')
    # Loop through the table object and select the enclosure name to add to the list
    encl_list = [str(ui_lib.get_webelement_attribute("text", el)) for el in ui_lib.wait_for_element_class(FusionEnclosuresPage.ID_TABLE_ENCLOSURE_NAMES, False, False)]
    # Looping thru the list and get IP address for each recorded enclosure
    for i in encl_list:
        select_enclosure(i)              # calling selection keyword to select the enclosure
        # navigate to the general view of the selected enclosure
        ui_lib.wait_for_element(FusionEnclosuresPage.ID_BTN_ENCL_VIEW_SELECTORS, PerfConstants.DEFAULT_SYNC_TIME)
        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_BTN_ENCL_VIEW_SELECTORS):
            ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_BTN_ENCL_VIEW_SELECTORS)
            ui_lib.wait_for_element(FusionEnclosuresPage.ID_SEL_ENCL_GENERAL_VIEW, PerfConstants.DEFAULT_SYNC_TIME)
            if ui_lib.wait_for_element(FusionEnclosuresPage.ID_SEL_ENCL_GENERAL_VIEW):
                ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_SEL_ENCL_GENERAL_VIEW)
            else:
                raise ValueError("Enclosure General View button is NOT available for usage.")
        else:
            raise ValueError("Enclosure Overview button is NOT available for usage.")
        #  Get the IP address of the selected enclosure
        ui_lib.wait_for_element(FusionEnclosuresPage.ID_FRAME_ENCL_GENERAL_HARDWARE, PerfConstants.DEFAULT_SYNC_TIME)
        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_FRAME_ENCL_GENERAL_HARDWARE):
            ui_lib.wait_for_element(FusionEnclosuresPage.ID_LINK_ENCL_GENERAL_IPV4, PerfConstants.DEFAULT_SYNC_TIME)
            if ui_lib.wait_for_element(FusionEnclosuresPage.ID_LINK_ENCL_GENERAL_IPV4):
                encl_info_dict[i] = s2l.get_text(FusionEnclosuresPage.ID_LINK_ENCL_GENERAL_IPV4)
            else:
                raise ValueError("IPv4 value is NOT available!!")
        else:
            raise ValueError("Enclosure's Hardware section is NOT available!! Use other area to check.")

    # Return the dictionary
    return encl_info_dict


def check_intermediate(cond, message):
    """ Analyzes cond.  If cond is true, there was an error.
        Log the error as a warning and return is_passing = False.
        Otherwise, return True.
    """
    if cond:
        logger._warn(message)
        return False
    return True


def tbird_verify_front_slot_content(row, bay):
    """ The RG script should have already moused over a blade or CIM bay slot.
        Make sure the blade/CIM is populated if expected, the status appears correctly,
        and the flyover div is displayed with the correct resource information.
        Make sure the elements are sized appropriately.
        Arguments:
            row: Number indicating top (1) or bottom (2) row: there are 2 rows of blades
            bay: Number shown for the desired bay (relative to row) on the OneView UI, one-based
    """
    is_passing = True    # keeps track of any errors encountered
    slot_content = BuiltIn().get_variable_value("${Enclosure}")
    s2l = ui_lib.get_s2l()
    # Calculate where we are based on row & bay information
    # Bay number is relative to the row and should only be 1 through 7; 1 is the CIM & 2-7 are blades
    # So if bay == 1, then the CIM# is the row; if bay > 1, then the blade # is ((row - 1) * 6) + (bay - 1)
    slot = row if bay == 1 else ((row - 1) * 6) + (bay - 1)
    slot -= 1
    # Determine what resource structure to look at
    populated = True
    device = "Blade"
    if bay == 1:
        # This is a CIM bay
        populated = (slot_content["ciManagerBays"][slot]["devicePresence"].lower() == "present")
        device = "CIM"
    else:
        populated = (slot_content["deviceBays"][slot]["devicePresence"].lower() == "present")
    # If the bay is not populated, make sure it does in fact show up empty
    if not populated:
        # Check element CSS class names
        expectedNames = "hp-bay hp-vertical hp-empty"
        classNames = s2l.get_element_attribute('xpath=//div[@id="cic-enclosure-show-bladebays"]/ol[%d]/li[%d]@class' % (row, bay))
        is_passing &= check_intermediate(classNames != expectedNames,
                                         ("%s Bay %d that is supposed to be empty does not exhibit the appropriate CSS styles: expected %s, observed %s." % (device, slot + 1, expectedNames, classNames)))
        # Make sure no popup has appeared
        badStyle = "display: none;"
        style = s2l.get_element_attribute('xpath=//div[@class="hp-flyout-content"]@style')
        is_passing &= check_intermediate(badStyle not in style,
                                         ("The flyout box should not be showing for empty %s Bay %d." % (device, slot + 1)))
        return is_passing
    # If we're here, the device bay is populated
    if device == "CIM":
        # Check that the CIM's link & model are correct
        linkText = "Converged infrastructure manager %d" % (slot + 1)
        modelText = slot_content["ciManagerBays"][slot]["model"]
        # Set element CSS class names that can be checked in common with CIMs
        containerClass = "hp-bay hp-short hp-vertical"
        deviceClass = "hp-device"
    else:
        # Set element CSS class names that can be checked in common with CIMs
        containerClass = "hp-bay hp-vertical"
        deviceClass = "hp-device hp-blade"
    # Check some things that CIMs and blades should have in common
    #    Check CSS class names of the device's container (the <li>)
    classNames = s2l.get_element_attribute('xpath=//div[@id="cic-enclosure-show-bladebays"]/ol[%d]/li[%d]@class' % (row, bay))
    is_passing &= check_intermediate(classNames != containerClass,
                                     ("%s Bay %d's container does not exhibit the appropriate CSS styles: expected %s, observed %s." % (device, slot + 1, containerClass, classNames)))
    #    Check CSS class names of the device itself (the <li>/<div>)
    classNames = s2l.get_element_attribute('xpath=//div[@id="cic-enclosure-show-bladebays"]/ol[%d]/li[%d]/div[1]@class' % (row, bay))
    is_passing &= check_intermediate(classNames != deviceClass,
                                     ("%s Bay %d that is supposed to be populated does not exhibit the appropriate CSS styles: expected %s, observed %s." % (device, slot + 1, deviceClass, classNames)))
    #     The flyout info box should be showing
    # TODO: Make sure the inside text is correct (waiting on development user story completion)
    # TODO: Make sure the flyover text is correct (waiting on development user story completion)
    logger._warn("Verifying data on populated Blade Bays is still a work in progress by development teams.")
    return is_passing


def tbird_verify_back_icm_row(device_no):
    """ The RG script should have already moused over an ICM bay slot.
        Verify the graphics representing the ICMs in the rear of the enclosure.
        Make sure each slot is populated if expected, the status appears correctly,
        and the flyover div is displayed with the correct resource information.
        Make sure the elements are sized appropriately.
        Arguments:
            device_no: ICM bay number, zero-based (0-5)
    """
    is_passing = True    # keeps track of any errors encountered
    slot_content = BuiltIn().get_variable_value("${Enclosure}")
    s2l = ui_lib.get_s2l()
    icmRows = [1, 2, 4, 6, 7, 9]
    root_xpath = 'xpath=//div[@id="cic-enclosure-show-switchbays"]/ol[%d]' % icmRows[device_no]
    # Test some of the common CSS C7000 of all ICM rows
    #    Outer "ol" element (row in enclosure graphic)
    expectedClass = "hp-bays cic-enclosure-switch-row"
    rowClass = s2l.get_element_attribute('%s@class' % root_xpath)
    is_passing &= check_intermediate(rowClass != expectedClass,
                                     ("ICM Bay %d should exhibit the CSS style of a switch row: expected %s, observed %s." % (device_no + 1, expectedClass, rowClass)))
    #    Device label
    # Find out if this actual bay is populated or empty
    populated = ("model" in slot_content["interconnectBays"][device_no])
    # If the bay is not populated, make sure it does in fact show up empty
    if not populated:
        # <li> row item (the box representing a non-existent ICM) should exhibit expected CSS style
        itemClass = s2l.get_element_attribute('%s/li@class' % root_xpath)
        expectedStyle = "hp-bay hp-empty"
        is_passing &= check_intermediate(itemClass != expectedStyle,
                                         ("Absent ICM %d should exhibit CSS styles %s, but instead shows %s." % (device_no + 1, expectedStyle, itemClass)))
        # The div should be of CSS class "hp-empty"
        expectedStyle = "hp-empty"
        deviceClass = s2l.get_element_attribute('%s/li/div@class' % root_xpath)
        is_passing &= check_intermediate(deviceClass != expectedStyle,
                                         ("Absent ICM %d's inner box should exhibit CSS styles %s, but instead shows %s." % (device_no + 1, expectedStyle, deviceClass)))
        # The div's child div should be of class "hp-unset"
        expectedStyle = "hp-unset"
        infoClass = s2l.get_element_attribute('%s/li/div/div@class' % root_xpath)
        is_passing &= check_intermediate(infoClass != expectedStyle,
                                         ("Absent ICM %d's info text should exhibit CSS styles %s, but instead shows %s." % (device_no + 1, expectedStyle, infoClass)))
    else:  # ICM bay is populated
        # <li> row item (the box representing the ICM) should exhibit expected CSS style
        itemClass = s2l.get_element_attribute('%s/li@class' % root_xpath)
        expectedStyle = "hp-bay"
        is_passing &= check_intermediate(itemClass != expectedStyle,
                                         ("ICM %d should exhibit CSS styles %s, but instead shows %s." % (device_no + 1, expectedStyle, itemClass)))
        # The first div should be of CSS class "hp-device hp-switch hp-flyout-wrapper"
        expectedStyle = "hp-device hp-switch hp-flyout-wrapper"
        deviceClass = s2l.get_element_attribute('%s/li/div@class' % root_xpath)
        is_passing &= check_intermediate(deviceClass != expectedStyle,
                                         ("ICM %d's inner box should exhibit CSS styles %s, but instead shows %s." % (device_no + 1, expectedStyle, deviceClass)))

        # Validate the information contained within the HTML elements once it's actually present
        logger._warn("Verifying data on populated ICM Bays is still a work in progress by development teams.")

    return is_passing


def tbird_verify_back_em_fan_row(logical_row):
    """ Verify the graphics representing the EMs & fans in the rear of the enclosure.
        Make sure each slot is populated if expected, the status appears correctly,
        and the flyover div is displayed with the correct resource information.
        Make sure the elements are sized appropriately.
        Arguments:
            logical_row: Zero-based row number relative to EMs/fans (can be 0 or 1)
    """
    is_passing = True    # keeps track of any errors encountered
    slot_content = BuiltIn().get_variable_value("${Enclosure}")
    s2l = ui_lib.get_s2l()
    row = [3, 8]
    root_xpath = 'xpath=//div[@id="cic-enclosure-show-switchbays"]/ol[%d]' % row[logical_row]
    # Test the common CSS C7000 of all EM/fan rows
    #    Outer "ol" element (row in enclosure graphic)
    expectedClass = "hp-bays cic-enclosure-fan-row"
    rowClass = s2l.get_element_attribute('%s@class' % root_xpath)
    is_passing &= check_intermediate(rowClass != expectedClass,
                                     ("EM/Fan Row %d is supposed to exhibit the CSS style of a fan row: expected %s, observed %s." % (logical_row + 1, expectedClass, rowClass)))
    #    The EM module
    populated = (slot_content["managers"][logical_row]["devicePresence"].lower() == "present")
    if populated:
        # <li> row item (the box representing the EM) should exhibit expected CSS style
        itemClass = s2l.get_element_attribute('%s/li[1]@class' % root_xpath)
        expectedStyle = "hp-bay cic-enclosure-tbird-em"
        is_passing &= check_intermediate(itemClass != expectedStyle,
                                         ("EM %d should exhibit CSS styles %s, but instead shows %s." % (logical_row + 1, expectedStyle, itemClass)))
        # Mouse over the EM bay
        s2l.mouse_over('%s/li[1]' % root_xpath)
        # Delay for demo's sake
        BuiltIn().sleep(1)

    # Iterate through the fan bays in this row
    for fan in range(2, 7):
        real_fan_no = (fan - 1) + (5 * (logical_row))
        # Mouse over the fan bay
        s2l.mouse_over('%s/li[%d]' % (root_xpath, fan))
        # Delay for demo's sake
        BuiltIn().sleep(1)
        # Find out if this actual bay is populated or empty
        populated = (slot_content["fanBays"][real_fan_no - 1]["devicePresence"].lower() == "present")
        # If the bay is not populated, make sure it does in fact show up empty
        if not populated:
            # <li> row item (the box representing a non-existent fan) should exhibit expected CSS style
            itemClass = s2l.get_element_attribute('%s/li[%d]@class' % (root_xpath, fan))
            expectedStyle = "hp-bay hp-empty cic-enclosure-fan-bay"
            is_passing &= check_intermediate(itemClass != expectedStyle,
                                             ("Absent fan bay %d should exhibit CSS styles %s, but instead shows %s." % (real_fan_no, expectedStyle, itemClass)))
            # The div should be of CSS class "hp-empty"
            expectedStyle = "hp-empty"
            deviceClass = s2l.get_element_attribute('%s/li[%d]/div@class' % (root_xpath, fan))
            is_passing &= check_intermediate(deviceClass != expectedStyle,
                                             ("Absent fan %d's inner box should exhibit CSS styles %s, but instead shows %s." % (real_fan_no, expectedStyle, deviceClass)))
            # The div's child div should be of class "hp-unset"
            expectedStyle = "hp-unset"
            infoClass = s2l.get_element_attribute('%s/li[%d]/div/div@class' % (root_xpath, fan))
            is_passing &= check_intermediate(infoClass != expectedStyle,
                                             ("Absent fan %d's info text should exhibit CSS styles %s, but instead shows %s." % (real_fan_no, expectedStyle, infoClass)))
        else:  # Fan bay is populated
            # <li> row item (the box representing the fan) should exhibit expected CSS style
            itemClass = s2l.get_element_attribute('%s/li[%d]@class' % (root_xpath, fan))
            expectedStyle = "hp-bay cic-enclosure-fan-bay"
            is_passing &= check_intermediate(itemClass != expectedStyle,
                                             ("Fan bay %d should exhibit CSS styles %s, but instead shows %s." % (real_fan_no, expectedStyle, itemClass)))
            # The first div should be of CSS class "hp-device hp-fan hp-flyout-wrapper"
            expectedStyle = "hp-device hp-fan hp-flyout-wrapper"
            deviceClass = s2l.get_element_attribute('%s/li[%d]/div@class' % (root_xpath, fan))
            is_passing &= check_intermediate(deviceClass != expectedStyle,
                                             ("Fan %d should exhibit CSS styles %s, but instead shows %s." % (real_fan_no, expectedStyle, deviceClass)))
            # The first div should have one child div displaying status
            expectedStyle = "hp-status"
            statusClass = s2l.get_element_attribute('%s/li[%d]/div/div@class' % (root_xpath, fan))
            is_passing &= check_intermediate(expectedStyle not in statusClass,
                                             ("Fan %d's status should exhibit CSS styles %s, but instead shows %s." % (real_fan_no, expectedStyle, statusClass)))
    return is_passing


def tbird_verify_back_power_row(logical_row):
    """ Verify the graphics representing the power supplies in the rear of the enclosure.
        Make sure each slot is populated if expected, the status appears correctly,
        and the flyover div is displayed with the correct resource information.
        Make sure the elements are sized appropriately.
        Arguments:
            logical_row: Zero-based row number relative to power supplies (can be 0 or 1)
    """
    is_passing = True    # keeps track of any errors encountered
    slot_content = BuiltIn().get_variable_value("${Enclosure}")
    s2l = ui_lib.get_s2l()
    row = [5, 10]
    root_xpath = 'xpath=//div[@id="cic-enclosure-show-switchbays"]/ol[%d]' % row[logical_row]
    # Test the common CSS C7000 of all power supply rows
    #    Outer "ol" element (row in enclosure graphic)
    expectedClass = "hp-bays cic-enclosure-power-row"
    rowClass = s2l.get_element_attribute('%s@class' % root_xpath)
    is_passing &= check_intermediate(rowClass != expectedClass,
                                     ("Power supply Row %d is supposed to exhibit the CSS style %s, but %s was observed." % (logical_row + 1, expectedClass, rowClass)))
    # Iterate through the power supplies in this row
    for ps in range(1, 4):
        real_ps_no = ps + (3 * (logical_row))
        # Mouse over the power supply bay
        s2l.mouse_over('%s/li[%d]' % (root_xpath, ps))
        # Delay for demo's sake
        BuiltIn().sleep(1)
        # Find out if this actual bay is populated or empty
        populated = (slot_content["powerSupplyBays"][real_ps_no - 1]["devicePresence"].lower() == "present")
        # If the bay is not populated, make sure it does in fact show up empty
        if not populated:
            # <li> row item (the box representing a non-existent power supply) should exhibit expected CSS style
            itemClass = s2l.get_element_attribute('%s/li[%d]@class' % (root_xpath, ps))
            expectedStyle = "hp-bay hp-empty"
            is_passing &= check_intermediate(itemClass != expectedStyle,
                                             ("Absent power supply bay %d should exhibit CSS styles %s, but instead shows %s." % (real_ps_no, expectedStyle, itemClass)))
            # The div should be of CSS class "hp-empty"
            expectedStyle = "hp-empty"
            deviceClass = s2l.get_element_attribute('%s/li[%d]/div@class' % (root_xpath, ps))
            is_passing &= check_intermediate(deviceClass != expectedStyle,
                                             ("Absent power supply %d's inner box should exhibit CSS styles %s, but instead shows %s." % (real_ps_no, expectedStyle, deviceClass)))
            # The div's child div should be of class "hp-unset"
            expectedStyle = "hp-unset"
            infoClass = s2l.get_element_attribute('%s/li[%d]/div/div@class' % (root_xpath, ps))
            is_passing &= check_intermediate(infoClass != expectedStyle,
                                             ("Absent power supply %d's info text should exhibit CSS styles %s, but instead shows %s." % (real_ps_no, expectedStyle, infoClass)))
        else:  # Power supply bay is populated
            # <li> row item (the box representing the power supply) should exhibit expected CSS style
            itemClass = s2l.get_element_attribute('%s/li[%d]@class' % (root_xpath, ps))
            expectedStyle = "hp-bay"
            is_passing &= check_intermediate(itemClass != expectedStyle,
                                             ("Power supply bay %d should exhibit CSS styles %s, but instead shows %s." % (real_ps_no, expectedStyle, itemClass)))
            # The first div should be of CSS class "hp-device hp-power hp-flyout-wrapper"
            expectedStyle = "hp-device hp-power hp-flyout-wrapper"
            deviceClass = s2l.get_element_attribute('%s/li[%d]/div@class' % (root_xpath, ps))
            is_passing &= check_intermediate(deviceClass != expectedStyle,
                                             ("Power supply %d should exhibit CSS styles %s, but instead shows %s." % (real_ps_no, expectedStyle, deviceClass)))
            # The first div should have one child div displaying status
            expectedStyle = "hp-status"
            statusClass = s2l.get_element_attribute('%s/li[%d]/div/div@class' % (root_xpath, ps))
            is_passing &= check_intermediate(expectedStyle not in statusClass,
                                             ("Power supply %d's status should exhibit CSS styles %s, but instead shows %s." % (real_ps_no, expectedStyle, statusClass)))
    return is_passing


def tbird_verify_device_bay(bay):
    """ Make sure the specified blade is populated if expected,
        and that its properties are displayed appropriately.
        Arguments:
            bay: Number shown for the desired bay (not necessarily row #) on the OneView UI (one-based)
    """
    is_passing = True    # keeps track of any errors encountered
    slot_content = BuiltIn().get_variable_value("${Enc Object}")
    s2l = ui_lib.get_s2l()
    # Consider any sorting:
    # Verify the row corresponding to that actual Bay Number, not Row #[bay]
    bay_row = 'xpath=//table[@id="cic-enclosure-more-devbays-table"]/tbody/tr/td[text()="%d"]/..' % bay
    actual_bay = int(s2l.get_text('%s/td[2]' % bay_row))
    actual_bay -= 1
    # Find out if this actual bay is populated or empty
    populated = (slot_content["deviceBays"][actual_bay]["devicePresence"].lower() == "present")
    # If the bay is not populated, make sure it does in fact show up empty
    if not populated:
        # Column 1 should actually be empty, but with certain CSS style
        classNames = s2l.get_element_attribute('%s/td[1]/div@class' % bay_row)
        is_passing &= check_intermediate(classNames != "hp-status hp-status-null",
                                         ("Blade Bay %d that is supposed to be unpopulated does not exhibit the appropriate CSS styles in column 1: expected %s, observed %s." % (actual_bay + 1, "hp-status hp-status-null", classNames)))
        # Column 3 should say "empty" with certain CSS style
        classNames = s2l.get_element_attribute('%s/td[3]/span@class' % bay_row)
        tdText = s2l.get_text('%s/td[3]/span' % bay_row)
        is_passing &= check_intermediate(classNames != "hp-unset",
                                         ("Blade Bay %d that is supposed to be unpopulated does not exhibit the appropriate CSS styles in column 3: expected %s, observed %s." % (actual_bay + 1, "hp-unset", classNames)))
        is_passing &= check_intermediate(tdText != "empty",
                                         ("Blade Bay %d is supposed to be marked \"empty\" but is shown as %s." % (actual_bay + 1, tdText)))
        # Columns 4 & 5 should be totally devoid of anything
        tdText4 = s2l.get_text('%s/td[4]' % bay_row)
        tdText5 = s2l.get_text('%s/td[5]' % bay_row)
        is_passing &= check_intermediate(tdText4 != "" or tdText5 != "",
                                         ("Blade Bay %d that is supposed to be unpopulated apparently shows some kind of text in either Column 4 or 5." % (actual_bay + 1)))
    else:
        logger._warn("Blade Bays that are populated are still a work in progress.")
    return is_passing


def tbird_verify_interconnect_bay(bay):
    """ Make sure the specified blade is populated if expected,
        and that its properties are displayed appropriately.
        Arguments:
            bay: Number shown for the desired bay (not necessarily row #) on the OneView UI (one-based)
    """
    is_passing = True    # keeps track of any errors encountered
    slot_content = BuiltIn().get_variable_value("${Enc Object}")
    s2l = ui_lib.get_s2l()
    # Consider any sorting:
    # Verify the row corresponding to that actual Bay Number, not Row #[bay]
    bay_row = 'xpath=//table[@id="cic-enclosure-icm-outer-table"]//table/tbody/tr/td[text()="%d"]/..' % bay
    try:
        actual_bay = int(s2l.get_text('%s/td[2]' % bay_row))
    except:
        logger._warn("The Xpath to access ICM bay rows appears to be broken.  Check the page's DOM to see what changed.")
        return False
    actual_bay -= 1
    # Find out if this actual bay is populated or empty
    populated = ("model" in slot_content["interconnectBays"][actual_bay])
    # If the bay is not populated, make sure it does in fact show up empty
    if not populated:
        # Column 1 should actually be empty, but with certain CSS style
        classNames = s2l.get_element_attribute('%s/td[1]/div@class' % bay_row)
        is_passing &= check_intermediate(classNames != "hp-status hp-status-null",
                                         ("Interconnect Bay %d that is supposed to be unpopulated does not exhibit the appropriate CSS styles in column 1: expected %s, observed %s." % (actual_bay + 1, "hp-status hp-status-null", classNames)))
        # Columns 3 & 4 should say "empty" with certain CSS style
        for i in range(3, 5):
            classNames = s2l.get_element_attribute('%s/td[%d]/span@class' % (bay_row, i))
            tdText = s2l.get_text('%s/td[%d]/span' % (bay_row, i))
            is_passing &= check_intermediate(classNames != "hp-unset",
                                             ("Interconnect Bay %d that is supposed to be unpopulated does not exhibit the appropriate CSS styles in column %d: expected %s, observed %s." % (actual_bay + 1, i, "hp-unset", classNames)))
            tdTextShouldBe = ("empty" if i == 3 else "none")
            is_passing &= check_intermediate(tdText != tdTextShouldBe,
                                             ("Interconnect Bay %d column %d is supposed to be marked \"%s\" but is shown as %s." % (actual_bay + 1, i, tdTextShouldBe, tdText)))
    else:
        logger._warn("Interconnect Bays that are populated are still a work in progress.")
    return is_passing


def tbird_verify_cim_bay(bay):
    """ Make sure the specified CIM is populated if expected,
        and that its properties are displayed appropriately.
        Arguments:
            bay: Number shown for the desired bay (not necessarily row #) on the OneView UI (one-based)
    """
    is_passing = True    # keeps track of any errors encountered
    slot_content = BuiltIn().get_variable_value("${Enc Object}")
    s2l = ui_lib.get_s2l()
    # Consider any sorting:
    # Verify the row corresponding to that actual Bay Number, not Row #[bay]
    bay_row = 'xpath=//table[@id="cic-enclosure-more-ci-mgr-bays-table"]/tbody/tr/td[text()="%d"]/..' % bay
    actual_bay = int(s2l.get_text('%s/td[2]' % bay_row))
    actual_bay -= 1
    # Find out if this actual bay is populated or empty
    populated = (slot_content["ciManagerBays"][actual_bay]["devicePresence"] == "Present")
    # If the bay is not populated, make sure it does in fact show up empty
    if not populated:
        # Column 1 should actually be empty, but with certain CSS style
        expectedClass = "hp-status"
        classNames = s2l.get_element_attribute('%s/td[1]/div@class' % bay_row)
        is_passing &= check_intermediate(classNames != expectedClass,
                                         ("CIM Bay %d that is supposed to be unpopulated does not exhibit the appropriate CSS styles in column 1: expected %s, observed %s." % (actual_bay + 1, expectedClass, classNames)))
        # Column 3 should say "empty" with certain CSS style
        classNames = s2l.get_element_attribute('%s/td[3]/span@class' % bay_row)
        tdText = s2l.get_text('%s/td[3]/span' % bay_row)
        is_passing &= check_intermediate(classNames != "hp-unset",
                                         ("CIM Bay %d that is supposed to be unpopulated does not exhibit the appropriate CSS styles in column 3: expected %s, observed %s." % (actual_bay + 1, "hp-unset", classNames)))
        is_passing &= check_intermediate(tdText != "empty",
                                         ("CIM Bay %d is supposed to be marked \"empty\" but is shown as %s." % (actual_bay + 1, tdText)))
        # Columns 4-6 should be totally devoid of anything
        tdText4 = s2l.get_text('%s/td[4]' % bay_row)
        tdText5 = s2l.get_text('%s/td[5]' % bay_row)
        tdText6 = s2l.get_text('%s/td[6]' % bay_row)
        is_passing &= check_intermediate(tdText4 != "" or tdText5 != "" or tdText6 != "",
                                         ("CIM Bay %d that is supposed to be unpopulated apparently shows some kind of text in the columns after Empty." % (actual_bay + 1)))
    else:
        # Column 1 should have a CSS class of hp-status
        classNames = s2l.get_element_attribute('%s/td[1]/div@class' % bay_row)
        is_passing &= check_intermediate("hp-status" not in classNames,
                                         ("CIM Bay %d may not be showing a status as expected in Column 1: its CSS class is %s." % (actual_bay + 1, classNames)))
        # Column 3 should have the model
        observed = s2l.get_text('%s/td[3]' % bay_row)
        expected = slot_content["ciManagerBays"][actual_bay]["model"]
        is_passing &= check_intermediate(observed != expected,
                                         ("CIM Bay %d does not show the expected model; expected '%s', observed '%s'." % (actual_bay + 1, expected, observed)))
        # Column 4 should have the serial number
        observed = s2l.get_text('%s/td[4]' % bay_row)
        expected = slot_content["ciManagerBays"][actual_bay]["serialNumber"]
        is_passing &= check_intermediate(observed != expected,
                                         ("CIM Bay %d does not show the expected serial number; expected '%s', observed '%s'." % (actual_bay + 1, expected, observed)))
        # Column 5 should have the part number
        observed = s2l.get_text('%s/td[5]' % bay_row)
        expected = slot_content["ciManagerBays"][actual_bay]["partNumber"]
        is_passing &= check_intermediate(observed != expected,
                                         ("CIM Bay %d does not show the expected part number; expected '%s', observed '%s'." % (actual_bay + 1, expected, observed)))
        # Column 6 should have the spare part number
        observed = s2l.get_text('%s/td[6]' % bay_row)
        expected = slot_content["ciManagerBays"][actual_bay]["sparePartNumber"]
        is_passing &= check_intermediate(observed != expected,
                                         ("CIM Bay %d does not show the expected spare part number; expected '%s', observed '%s'." % (actual_bay + 1, expected, observed)))
    return is_passing


def tbird_verify_em_bay(bay):
    """ Make sure the specified EM is populated if expected,
        and that its properties are displayed appropriately.
        Arguments:
            bay: Number shown for the desired bay (not necessarily row #) on the OneView UI (one-based)
    """
    is_passing = True    # keeps track of any errors encountered
    slot_content = BuiltIn().get_variable_value("${Enc Object}")
    s2l = ui_lib.get_s2l()
    # Consider any sorting:
    # Verify the row corresponding to that actual Bay Number, not Row #[bay]
    table_xpath = '//table[@id="cic-enclosure-more-em-bays-table"]'
    bay_row = '%s/tbody/tr/td[text()="%d"]/..' % (table_xpath, bay)
    actual_bay = int(s2l.get_text('xpath=%s/td[3]' % bay_row))
    actual_bay -= 1
    # Find out if this actual bay is populated or empty
    populated = (slot_content["managers"][actual_bay]["devicePresence"] == "Present")
    # If the bay is not populated, make sure it does in fact show up empty
    if not populated:
        # Columns 1, 4, 6, & 7 should be totally devoid of anything
        tdText1 = s2l.get_text('xpath=%s/td[1]' % bay_row)
        tdText4 = s2l.get_text('xpath=%s/td[4]' % bay_row)
        tdText6 = s2l.get_text('xpath=%s/td[6]' % bay_row)
        tdText7 = s2l.get_text('xpath=%s/td[7]' % bay_row)
        is_passing &= check_intermediate(
            tdText1 != "" or tdText4 != "" or tdText6 != "" or tdText7 != "",
            ("Table row for EM Bay %d that is supposed to be unpopulated apparently shows some text in at least one column that should show nothing." % (actual_bay + 1)))
        # Column 2 should actually be empty, but with certain CSS style
        expectedClass = "hp-status"
        classNames = s2l.get_element_attribute('xpath=%s/td[2]/div@class' % bay_row)
        is_passing &= check_intermediate(
            classNames != expectedClass,
            ("EM Bay %d that is supposed to be unpopulated does not exhibit the appropriate CSS styles in column 2: expected %s, observed %s." % (actual_bay + 1, expectedClass, classNames)))
        # Column 3 should contain the bay number
        tdText = s2l.get_text('xpath=%s/td[3]' % bay_row)
        is_passing &= check_intermediate(
            tdText != str(actual_bay + 1),
            ("Table row for EM Bay %d actually shows the number %s in the Bay column." % (actual_bay + 1, tdText)))
        # Column 5 should say "empty" with certain CSS style
        classNames = s2l.get_element_attribute('xpath=%s/td[5]/span@class' % bay_row)
        tdText = s2l.get_text('xpath=%s/td[5]/span' % bay_row)
        is_passing &= check_intermediate(
            classNames != "hp-unset",
            ("EM Bay %d that is supposed to be unpopulated does not exhibit the appropriate CSS styles in column 5: expected %s, observed %s." % (actual_bay + 1, "hp-unset", classNames)))
        is_passing &= check_intermediate(
            tdText != "empty",
            ("EM Bay %d is supposed to be marked \"empty\" in Column 5 but is shown as %s." % (actual_bay + 1, tdText)))
    else:
        # Column 1 should contain a pulldown triangle; let's expand it
        classNames = s2l.get_element_attribute('xpath=%s/td[2]/div@class' % bay_row)
        if "hp-active" not in classNames:
            # Use an old trick to scroll exactly where we need to in order to unfurl the details
            ui_lib.scroll_to_xpath(bay_row, table_xpath, '//li[@id="cic-enclosure-more-em-bays"]/label', 'cic-enclosure-more-panels')
            BuiltIn().sleep(1)
            # Now make sure it's visible
            s2l.click_element('xpath=%s/td[1]/div' % bay_row)
            details_visible = s2l._is_visible('xpath=%s/following-sibling::tr[1]' % bay_row)
            is_passing &= check_intermediate(
                not details_visible,
                ("EM bay %d details did not fold down as expected when the arrow was clicked." % (actual_bay + 1)))
        # Column 2 should be showing a status
        classNames = s2l.get_element_attribute('xpath=%s/td[2]/div@class' % bay_row)
        is_passing &= check_intermediate(("hp-status" not in classNames) or ("hp-status-null" in classNames),
                                         ("EM Bay %d may not be showing a status as expected in Column 1: its CSS class is %s." % (actual_bay + 1, classNames)))
        # Column 4 should have the model
        observed = s2l.get_text('xpath=%s/td[4]' % bay_row)
        expected = slot_content["managers"][actual_bay]["model"]
        is_passing &= check_intermediate(observed != expected,
                                         ("EM Bay %d does not show the expected model; expected '%s', observed '%s'." % (actual_bay + 1, expected, observed)))
        # Column 5 should have either an Active or Standby state
        observed = s2l.get_text('xpath=%s/td[5]' % bay_row)
        expected = slot_content["managers"][actual_bay]["role"]
        is_passing &= check_intermediate(observed.lower() != expected.lower(),
                                         ("EM Bay %d does not show the same State as the machine config file expects; expected '%s', observed '%s'." % (actual_bay + 1, expected, observed)))
        is_passing &= check_intermediate(observed.lower() != "active" and observed.lower() != "standby",
                                         ("EM Bay %d does not show a valid State; expected 'Active' or 'Standby', observed '%s'." % (actual_bay + 1, observed)))
        # Column 6 should have one of the states defined in Piano spec F56 030
        if "mgmtPortState" not in slot_content["managers"][actual_bay]:
            logger._warn("Issue AM58 (FRU data): mgmtPortState was not reported for EM Bay %d" % (actual_bay + 1))
            is_passing = False
        else:
            observed = s2l.get_text('xpath=%s/td[6]' % bay_row)
            expected = slot_content["managers"][actual_bay]["mgmtPortState"]
            is_passing &= check_intermediate(observed.lower() != expected.lower(),
                                             ("EM Bay %d does not show the same MGMT Port State as the machine config file expects; expected '%s', observed '%s'." % (actual_bay + 1, expected, observed)))
            mgmtPortStates = ["linked, disabled", "unlinked, disabled", "linked, active", "linked, standby", "unlinked, active", "unlinked, standby"]
            is_passing &= check_intermediate(not observed.lower() in mgmtPortStates,
                                             ("EM Bay %d does not show a valid MGMT Port State. Expected a combination of 'Linked' or 'Unlinked' with 'Active' or 'Standby' or 'Disabled'; observed '%s'." % (actual_bay + 1, observed)))
        # Column 7 should be either Linked or Unlinked
        if "linkPortState" not in slot_content["managers"][actual_bay]:
            logger._warn("Issue AM58 (FRU data): linkPortState was not reported for EM Bay %d" % (actual_bay + 1))
            is_passing = False
        else:
            observed = s2l.get_text('xpath=%s/td[7]' % bay_row)
            expected = slot_content["managers"][actual_bay]["linkPortState"]
            is_passing &= check_intermediate(observed.lower() != expected.lower(),
                                             ("EM Bay %d does not show the same LINK Port State as the machine config file expects; expected '%s', observed '%s'." % (actual_bay + 1, expected, observed)))
            is_passing &= check_intermediate(observed.lower() != "linked" and observed.lower() != "unlinked",
                                             ("EM Bay %d does not show a valid LINK Port State; expected 'linked' or 'unlinked', observed '%s'." % (actual_bay + 1, observed)))
        # Now validate all the extra properties in the dropdown view, starting with the count of items present
        detailsRows = s2l.get_matching_xpath_count('%s/following-sibling::tr[1]/td/div/form/fieldset/ol/li' % bay_row)
        is_passing &= check_intermediate(detailsRows != '7',
                                         ("There should be 7 items listed in the EM details: SN#, PN#, Spare PN#, MGMT & LINK port speeds, and negotiated MGMT & LINK port speeds."))
        # Validate Serial number
        observed = s2l.get_text('xpath=%s/following-sibling::tr[1]//div[@id="cic-enclosure-more-em-details-serial-number"]' % bay_row)
        expected = slot_content["managers"][actual_bay]["serialNumber"]
        if expected is None:
            logger._warn("Issue AM58 or other FRU data problem: serialNumber was not reported for EM Bay %d" % (actual_bay + 1))
            is_passing = False
        else:
            is_passing &= check_intermediate(observed.lower() != expected.lower(),
                                             ("EM Bay %d does not show the same Serial Number as the machine config file expects; expected '%s', observed '%s'." % (actual_bay + 1, expected, observed)))
        # Validate part number
        observed = s2l.get_text('xpath=%s/following-sibling::tr[1]//div[@id="cic-enclosure-more-em-details-part-number"]' % bay_row)
        expected = slot_content["managers"][actual_bay]["partNumber"]
        if expected is None:
            logger._warn("Issue AM58 or other FRU data problem: partNumber was not reported for EM Bay %d" % (actual_bay + 1))
            is_passing = False
        else:
            is_passing &= check_intermediate(observed.lower() != expected.lower(),
                                             ("EM Bay %d does not show the same Part Number as the machine config file expects; expected '%s', observed '%s'." % (actual_bay + 1, expected, observed)))
        # Validate spare part number
        observed = s2l.get_text('xpath=%s/following-sibling::tr[1]//div[@id="cic-enclosure-more-em-details-spare-part-number"]' % bay_row)
        expected = slot_content["managers"][actual_bay]["sparePartNumber"]
        if expected is None:
            logger._warn("Issue AM58 or other FRU data problem: sparePartNumber was not reported for EM Bay %d" % (actual_bay + 1))
            is_passing = False
        else:
            is_passing &= check_intermediate(observed.lower() != expected.lower(),
                                             ("EM Bay %d does not show the same Spare Part Number as the machine config file expects; expected '%s', observed '%s'." % (actual_bay + 1, expected, observed)))
        # Validate MGMT port speed
        if "mgmtPortSpeed" not in slot_content["managers"][actual_bay]:
            logger._warn("FRU data problem: mgmtPortSpeed key was missing for EM Bay %d" % (actual_bay + 1))
            is_passing = False
        elif slot_content["managers"][actual_bay]["mgmtPortSpeed"] is None:
            logger._warn("Issue AM58 (FRU data): mgmtPortSpeed was not reported for EM Bay %d" % (actual_bay + 1))
            is_passing = False
        else:
            observed = s2l.get_text('xpath=%s/following-sibling::tr[1]//div[@id="cic-enclosure-more-em-details-mgmt-port-speed"]' % bay_row)
            expected = str(slot_content["managers"][actual_bay]["mgmtPortSpeed"]) + " Gb/s"
            is_passing &= check_intermediate(observed.lower() != expected.lower(),
                                             ("EM Bay %d does not show the same MGMT Port Speed as the machine config file expects; expected '%s', observed '%s'." % (actual_bay + 1, expected, observed)))
        # Validate negotiated MGMT port speed
        if "negotiatedMgmtPortSpeed" not in slot_content["managers"][actual_bay]:
            logger._warn("Issue AM58 (FRU data): negotiatedMgmtPortSpeed was not reported for EM Bay %d" % (actual_bay + 1))
            is_passing = False
        else:
            observed = s2l.get_text('xpath=%s/following-sibling::tr[1]//div[@id="cic-enclosure-more-em-details-neg-mgmt-port-speed"]' % bay_row)
            expected = str(slot_content["managers"][actual_bay]["negotiatedMgmtPortSpeed"]) + " Gb/s"
            is_passing &= check_intermediate(observed.lower() != expected.lower(),
                                             ("EM Bay %d does not show the same Negotiated MGMT Port Speed as the machine config file expects; expected '%s', observed '%s'." % (actual_bay + 1, expected, observed)))
        # Validate LINK port speed
        if "linkPortSpeed" not in slot_content["managers"][actual_bay]:
            logger._warn("FRU data problem: linkPortSpeed key was missing for EM Bay %d" % (actual_bay + 1))
            is_passing = False
        elif slot_content["managers"][actual_bay]["linkPortSpeed"] is None:
            logger._warn("Issue AM58 (FRU data): linkPortSpeed was not reported for EM Bay %d" % (actual_bay + 1))
            is_passing = False
        else:
            observed = s2l.get_text('xpath=%s/following-sibling::tr[1]//div[@id="cic-enclosure-more-em-details-link-port-speed"]' % bay_row)
            expected = str(slot_content["managers"][actual_bay]["linkPortSpeed"]) + " Gb/s"
            is_passing &= check_intermediate(observed.lower() != expected.lower(),
                                             ("EM Bay %d does not show the same LINK Port Speed as the machine config file expects; expected '%s', observed '%s'." % (actual_bay + 1, expected, observed)))
        # Validate negotiated LINK port speed
        observed = s2l.get_text('xpath=%s/following-sibling::tr[1]//div[@id="cic-enclosure-more-em-details-neg-link-port-speed"]' % bay_row)
        if "negotiatedLinkPortSpeed" not in slot_content["managers"][actual_bay]:
            logger._warn("Issue AM58 (FRU data): negotiatedLinkPortSpeed was not reported for EM Bay %d" % (actual_bay + 1))
            is_passing = False
        elif slot_content["managers"][actual_bay]["negotiatedLinkPortSpeed"] == 0:
            expected = "unlinked"
            is_passing &= check_intermediate(observed.lower() != expected.lower(),
                                             ("EM Bay %d does not show the same Negotiated LINK Port Speed as the machine config file expects; expected '%s', observed '%s'." % (actual_bay + 1, expected, observed)))
        else:
            expected = str(slot_content["managers"][actual_bay]["negotiatedLinkPortSpeed"]) + " Gb/s"
            is_passing &= check_intermediate(observed.lower() != expected.lower(),
                                             ("EM Bay %d does not show the same Negotiated LINK Port Speed as the machine config file expects; expected '%s', observed '%s'." % (actual_bay + 1, expected, observed)))
    return is_passing


def delete_all_appliance_enclosure():
    selenium2lib = ui_lib.get_s2l()
    """ Navigate to enclosure Page """
    if not selenium2lib._is_element_present(FusionEnclosuresPage.ID_PAGE_LABEL):
        navigate()

    enclr_list = [ui_lib.get_text(el) for el in selenium2lib._element_find(FusionEnclosuresPage.ID_ENCLOSURE_LIST_NAMES, False, False)]
    count = 0
    for enclr_name in enclr_list:
        logger._log_to_console_and_log_file("Deleting enclosure: {0}".format(enclr_name))
        enclr_obj = test_data.DataObj()
        enclr_obj.add_property('name', enclr_name)
        net_obj = (enclr_obj,)
        # enclr_delete_status = delete_enclosure(net_obj)
        enclr_delete_status = remove_enclosure(net_obj)

        if enclr_delete_status:
            logger._log_to_console_and_log_file("'{0}' Enclosure is deleted Successfully".format(enclr_name))
            count += 1
        else:
            logger._warn("Failed to delete Enclosure: {0}".format(enclr_name))

    if count == len(enclr_list):
        logger._log_to_console_and_log_file("All Enclosures deleted successfully for appliance")
        return True
    else:
        logger._warn("Failed to delete '{0}' Enclosures from appliance".format(len(enclr_list) - count))
        return False


def delete_enclosure(*enc_obj):
    """ Delete Enclosure

        Example:
        | `Delete Enclosure` |   ${myenclosure}  |
    """
    logger._log_to_console_and_log_file(" ")
    logger._log_to_console_and_log_file("Delete Enclosure")

    s2l = ui_lib.get_s2l()
    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])

    for enclosure in enc_obj:
        # Check whether mandatory fields are empty or not
        if(enclosure.name == ""):
            logger._warn("Mandatory fields for adding enclosure can't be empty")
            continue
        else:
            enclosure_list = [ui_lib.get_webelement_attribute("text", el) for el in s2l._element_find(FusionEnclosuresPage.ID_ENCLOSURE_LIST_NAMES, False, False)]
            if enclosure.name not in enclosure_list:
                logger._warn("Enclosure '%s' not present" % enclosure.name)
                continue

            enclosureObj = FusionEnclosuresPage.ID_LINK_ENCLOSURE_NAME % enclosure.name
            ui_lib.wait_for_element(enclosureObj)
            if (ui_lib.wait_for_element(enclosureObj) and
                ui_lib.wait_for_element(FusionEnclosuresPage.ID_ACTION_MAIN_BTN,
                                        PerfConstants.DEFAULT_SYNC_TIME)):
                ui_lib.wait_for_element_and_click(enclosureObj)
                ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_ACTION_MAIN_BTN)
                ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ACTION_MAIN_BTN)
                ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_MENU_ACTION_REMOVE)
                ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_MENU_ACTION_REMOVE)

                ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_DELETE_ENCLOSURE_NOTIFICATION, PerfConstants.DEFAULT_SYNC_TIME)
                if(ui_lib.wait_for_element(FusionEnclosuresPage.ID_DELETE_ENCLOSURE_NOTIFICATION)):
                    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_BTN_CONFIRM_REMOVE_ENCLOSURE)
                    logger._warn("deleting enclosure and sleeping ~5 mins")
                    BuiltIn().sleep(300)
                else:
                    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_BTN_CONFIRM_REMOVE_ENCLOSURE):
                        logger._warn("Delete enclosure confirmation dialog did not appear")
                        continue
                    ui_lib.wait_for_element(FusionEnclosuresPage.ID_BTN_CONFIRM_REMOVE_ENCLOSURE)
                    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_BTN_CONFIRM_REMOVE_ENCLOSURE)
                    logger._log_to_console_and_log_file("Removing Enclosure")
                    s2l.wait_until_page_contains("Removing", PerfConstants.DEFAULT_SYNC_TIME * 2)

                ui_lib.refresh_browser(FusionUIBaseElements.ID_MENU_ONE_VIEW, PerfConstants.DEFAULT_SYNC_TIME)
                # Wait until enclosure is removed from the appliance
                if not ui_lib.wait_for_element_remove(enclosureObj, PerfConstants.DELETE_ENCLOSURE_TIME):
                    logger._warn("Failed to delete enclosure")
                    return False
                else:
                    logger._log_to_console_and_log_file("Enclosure successfully deleted")
                    return True
            else:
                logger._warn("Enclosure %s is not present in the appliance" % enclosure.name)


def delete_enclosure_label(*enclosure_obj):
    """ delete enclosure label
        This function is to delete enclosure label
        Example:
            delete_enclosure_label(enclosure_obj)
    """
    if isinstance(enclosure_obj, test_data.DataObj):
        enclosure_obj = [enclosure_obj]
    elif isinstance(enclosure_obj, tuple):
        enclosure_obj = list(enclosure_obj)[0]

    logger._log_to_console_and_log_file("Function call to add label to enclosures ")

    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_LABEL):
        navigate()

    for enclosure in enclosure_obj:
        ui_lib.refresh_browser(FusionUIBaseElements.ID_MENU_ONE_VIEW, PerfConstants.DEFAULT_SYNC_TIME)
        if not select_encl(enclosure.enclname):
            return False

        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_DROPDOWN)
        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_DROPDOWN_SELECT_LABEL)

        logger._log_to_console_and_log_file("Deleting label from enclosure'{0}'".format(enclosure.enclname))
        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_EDIT_LABEL):
            ui_lib.move_to_element_and_click(FusionEnclosuresPage.ID_LABEL, FusionEnclosuresPage.ID_EDIT_LABEL)
            if ui_lib.wait_for_element(FusionEnclosuresPage.ID_EDIT_LABEL_PANEL):
                if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_LABEL_SEARCH % enclosure.name):
                    logger._warn("'{0}' label is not found".format(enclosure.name))
                else:
                    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_DELETE_BUTTON % enclosure.name)
                    logger._log_to_console_and_log_file("'{0}' Label is successfully deleted from enclosure '{1}'".format(enclosure.name, enclosure.enclname))
                    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_OK_LABEL_BTN)
            else:
                logger._warn("Failed to navigate edit label panel")
                return False
        else:
            logger._warn("Could not find Edit button to delete label")

        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_EMPTY_LABEL):
            logger._log_to_console_and_log_file("Label is successfully deleted from enclosure '{0}'".format(enclosure.enclname))
            return True
        else:
            logger._warn("Failed to delete from the selected enclosure")
            return False


def select_encl(enc_name):
    """ Selects the respective enclosure from the enclosure list """

    flag = False

    # Checking if already in enclosure page and if not traverse to enclosure page
    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()
        logger._log_to_console_and_log_file("Navigating to Fan Overview for enclosure %s" % enc_name)

    # This handles selection of enclosure
    ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enc_name, PerfConstants.SELECT_ENCLOSURE)
    if ui_lib.wait_for_element(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enc_name):
        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enc_name)
        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_ENCLOSURE_TITLE % enc_name, PerfConstants.ENCLOSURE_TITLE):
            logger._log_to_console_and_log_file("Given Enclosure %s is selected" % enc_name)
            flag = True
        else:
            logger._log_to_console_and_log_file("Unable to select enclosure %s" % enc_name)
    else:
        logger._log_to_console_and_log_file("Unable to select enclosure %s" % enc_name)
    return flag


def add_label_to_enclosure(*enclosure_list):
    """ add label to enclosure
        This function is to add label to enclosure
        Example:
            add_label_to_enclosure(*enclosure_list)
    """
    s2l = ui_lib.get_s2l()
    logger._log_to_console_and_log_file("Function call to add label to enclosures ")

    if isinstance(enclosure_list, test_data.DataObj):
        enclosure_list = [enclosure_list]
    elif isinstance(enclosure_list, tuple):
        enclosure_list = list(enclosure_list)[0]

    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_LABEL):
        navigate()

    for enclosure_label in enclosure_list:
        ui_lib.refresh_browser(FusionUIBaseElements.ID_MENU_ONE_VIEW, PerfConstants.DEFAULT_SYNC_TIME)
        if not select_encl(enclosure_label.enclosure):
            return False

        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_DROPDOWN)
        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_DROPDOWN_SELECT_LABEL)

        logger._log_to_console_and_log_file("Adding label to enclosure '{0}'".format(enclosure_label.enclosure))
        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_EDIT_LABEL):
            ui_lib.move_to_element_and_click(FusionEnclosuresPage.ID_LABEL, FusionEnclosuresPage.ID_EDIT_LABEL)
            if ui_lib.wait_for_element(FusionEnclosuresPage.ID_EDIT_LABEL_PANEL):
                ui_lib.wait_for_element_and_input_text(FusionEnclosuresPage.ID_LABEL_NAME, enclosure_label.name)
                ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ADD_LABEL_BTN)
                ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_OK_LABEL_BTN)
            else:
                logger._warn("Failed to navigate edit label panel")
                return False
        else:
            logger._warn("Could not find Edit button to add label")

        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_ADDED_LABEL % enclosure_label.name):
            ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ADDED_LABEL % enclosure_label.name)
            enclosure_lists = []
            ui_lib.wait_for_element(FusionEnclosuresPage.ID_ALL_ENCLOSURE_LIST, PerfConstants.FUSION_PAGE_SYNC)
            enclosure_lists = [ui_lib.get_text(s) for s in s2l._element_find(FusionEnclosuresPage.ID_ALL_ENCLOSURE_LIST, False, False)]
            for enclosure in enclosure_lists:
                if enclosure.lower() == enclosure_label.enclosure.lower():
                    logger._log_to_console_and_log_file("Label {0} is successfully added to the enclosure '{1}'".format(enclosure_label.name, enclosure_label.enclosure))
        else:
            logger._warn("Failed to add label to the selected enclosure")
            return False
    return True


def edit_scope_for_enclosure(enclosure_list):
    """ edit scope for enclosure
        This function is to edit scope for enclosure
        Example:
            edit_scope_for_enclosure(enclosure_list)
    """
    logger.info("Function call to edit scope for enclosures ")

    navigate()

    for enclosure in enclosure_list:
        if not select_encl(enclosure.name):
            ui_lib.fail_test("Failed to find target enclosure")

        FusionUIBase.select_view_by_name("Scopes")
        EditScopeForEnclosures.click_edit_scope_button()
        EditScopeForEnclosures.wait_edit_scope_dialog_open()
        scope_list = enclosure.scopes.split(',')
        for scope in scope_list:
            if not VerifyEnclosures.verify_scope_should_exist_in_edit_page(scope, 2):
                EditScopeForEnclosures.click_assign_button()
                EditScopeForEnclosures.wait_assign_scope_dialog_open()
                EditScopeForEnclosures.input_scope_name(scope)
                EditScopeForEnclosures.click_scope_name(scope)
                EditScopeForEnclosures.click_add_button()
                EditScopeForEnclosures.wait_assign_scope_dialog_close()

        if enclosure.has_property("remove_scopes"):
            remove_scope_list = enclosure.remove_scopes.split(',')
            for scope in remove_scope_list:
                if VerifyEnclosures.verify_scope_should_exist_in_edit_page(scope, timeout=5, fail_if_false=True):
                    EditScopeForEnclosures.click_remove_scope_icon(scope)

        EditScopeForEnclosures.click_ok_button()
        EditScopeForEnclosures.wait_edit_scope_dialog_close()

        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(enclosure.name, 'Update', timeout=60, fail_if_false=True)
        FusionUIBase.show_activity_sidebar()

    return True


def validate_scope_can_be_assigned_for_enclosure(enclosure_list):
    """ validate scope can be assigned for enclosure
        This function is to validate can be assigned for enclosure
        Example:
            validate_scope_can_be_assigned_for_enclosure(enclosure_list)
    """
    logger.info("Function call to validate scope can be assigned for enclosures ")

    navigate()

    for enclosure in enclosure_list:
        if not select_encl(enclosure.name):
            ui_lib.fail_test("Failed to find target enclosure")

        FusionUIBase.select_view_by_name("Scopes")
        EditScopeForEnclosures.click_edit_scope_button()
        EditScopeForEnclosures.wait_edit_scope_dialog_open()
        scope_list = enclosure.scopes.split(',')
        for scope in scope_list:
            if not VerifyEnclosures.verify_scope_should_exist_in_edit_page(scope):
                EditScopeForEnclosures.click_assign_button()
                EditScopeForEnclosures.wait_assign_scope_dialog_open()
                EditScopeForEnclosures.input_scope_name(scope)
                EditScopeForEnclosures.click_scope_name(scope)
                EditScopeForEnclosures.click_add_button()
                EditScopeForEnclosures.wait_assign_scope_dialog_close()

        EditScopeForEnclosures.click_cancel_button()
        EditScopeForEnclosures.wait_edit_scope_dialog_close()

    return True


def validate_scope_assign_for_enclosure(enclosure_list):
    """ validate scope assign for enclosure
        This function is to validate scope assign for enclosure
        Example:
            validate_scope_assign_for_enclosure(enclosure_list)
    """
    logger.info("Function call to validate scope assign for enclosures ")

    navigate()

    for enclosure in enclosure_list:
        if not select_encl(enclosure.name):
            ui_lib.fail_test("Failed to find target server enclosure")

        FusionUIBase.select_view_by_name("Scopes")
        if enclosure.has_property("scopes"):
            scope_list = enclosure.scopes.split(',')
            for scope in scope_list:
                if scope != "":
                    VerifyEnclosures.verify_scope_should_exist(scope)
        if enclosure.has_property("removed_scopes"):
            scope_list = enclosure.removed_scopes.split(',')
            for scope in scope_list:
                if scope != "":
                    VerifyEnclosures.verify_scope_should_not_exist(scope)

    return True


def update_enclosure_name(enc_name, new_enc_name):
    """ Update enclosure name

        Example:
        | `Update enclosure name`    |    ${enc_name}    |        ${new_enc_name}    |
    """
    logger._log_to_console_and_log_file("Update enclosure name")

    if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_PAGE_LABEL):
        navigate()

    logger._log_to_console_and_log_file("Updating Enclosure name For..... %s" % enc_name)
    # Checks whether enclosure present or not
    if ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_ENCLOSURE_TITLE % enc_name, PerfConstants.ENCLOSURE_TITLE):
        logger._log_to_console_and_log_file("Selecting Enclosure %s to update name  " % enc_name)
        if not ui_lib.wait_for_element(FusionEnclosuresPage.ID_ENCLOSURE_ADD_BUTTON, PerfConstants.SELECT_ENCLOSURE):
            logger._warn("Unable to open the Enclosures page")
            return False
        else:
            logger._log_to_console_and_log_file("Enclosures page opened successfully")
            # Verifying the presence of given Enclosure and selecting
            ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enc_name, PerfConstants.SELECT_ENCLOSURE)
            if ui_lib.wait_for_element(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enc_name):
                ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % enc_name)
                if ui_lib.wait_for_element(FusionEnclosuresPage.ID_ENCLOSURE_TITLE % enc_name, PerfConstants.ENCLOSURE_TITLE):
                    logger._log_to_console_and_log_file("Given Enclosure %s is selected" % enc_name)
                    # ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_SELECT_ENCLOSURE %enclosureName.name)
                    ui_lib.wait_for_element(FusionEnclosuresPage.ID_ACTION_MAIN_BTN, PerfConstants.SELECT_UPDATE_FIRMWARE_ACTION)
                    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ACTION_MAIN_BTN)
                    ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_LINK_ENCLOSURE_EDIT)
                    if ui_lib.wait_for_element(FusionEnclosuresPage.IN_INPUT_ENCLOSURE_NAME_EDIT, PerfConstants.ENCLOSURE_TITLE):
                        logger._log_to_console_and_log_file("Edit Enclosure page is opened")

                        ui_lib.wait_for_element_and_input_text(FusionEnclosuresPage.IN_INPUT_ENCLOSURE_NAME_EDIT, new_enc_name)
                        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_BTN_ENCLOSURE_EDIT_OK)
                        ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % new_enc_name, PerfConstants.SELECT_ENCLOSURE)
                        if ui_lib.wait_for_element(FusionEnclosuresPage.ID_SELECT_ENCLOSURE % new_enc_name):
                            logger._log_to_console_and_log_file("The Enclosure name is updated successfully according to the requirement")
                            return True
                        elif ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_ERR_SPECIAL_ENCL_NAME, PerfConstants.FUSION_PAGE_SYNC):
                            logger._warn("The Enclosure name is not updated with the Error message displaying, '32 or fewer alphanumeric, dash, or underscore characters.'")
                            ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_BTN_ENCLOSURE_EDIT_CANCEL)
                            return False
                        elif ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_ERR_APLHABET_LIMIT_ENCL_NAME, PerfConstants.FUSION_PAGE_SYNC):
                            logger._warn("The Enclosure name is not updated with the Error message displaying, 'Enter no more than 32 characters.'")
                            ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_BTN_ENCLOSURE_EDIT_CANCEL)
                            return False
                        elif ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_ERR_EXISTING_ENCL_NAME_UNABLE, PerfConstants.FUSION_PAGE_SYNC):
                            logger._warn("The Enclosure name is not updated with the Error message displaying, 'Unable to update enclosure. Resolve the following issues to proceed.'")
                            ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_BTN_ENCLOSURE_EDIT_CANCEL)
                            return False
                        elif ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_ERR_ALREADY_INUSE_ENCL_NAME_UNABLE, PerfConstants.FUSION_PAGE_SYNC):
                            logger._log_to_console_and_log_file("The Enclosure name is not updated with the Error message displaying, 'The enclosure name specified is already used by another enclosure.'")
                            return False
                        elif ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_ERR_UNIQUE_ENCL_NAME_UNABLE, PerfConstants.FUSION_PAGE_SYNC):
                            logger._warn("The Enclosure name is not updated with the Error message displaying, 'Please specify a unique enclosure name.'")
                            ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_BTN_ENCLOSURE_EDIT_CANCEL)
                            return False
                        else:
                            logger._warn("The Enclosure name is not updated successfully according to the requirement")
                            ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_BTN_ENCLOSURE_EDIT_CANCEL)
                            return False
                    else:
                        logger._warn("The Enclosure edit page did not appear")
                        return False
            else:
                logger._warn("The Enclosure name specified doesn't not exist in enclosure page, please provide the proper enclosure name")
                return False
    else:
        logger._warn("The Enclosure name specified doesn't not exist in enclosure page, please provide the proper enclosure name")
        return False


def _get_enc_activity_details(*enclosure_list):
    '''
    Get  the  Activity  State of any Enclosure activity
    - Takes the  Activity label as an input parameter
    - returns  True and the state   if the activity is found
      else  returns false and ''
      Update OA firmware
    '''
    flagb = 0
    if isinstance(enclosure_list, test_data.DataObj):
        enclosure_list = [enclosure_list]
    elif isinstance(enclosure_list, tuple):
        enclosure_list = list(enclosure_list)

    if not ui_lib.wait_for_element(FusionLogicalEnclosuresPage.ID_PAGE_LABEL):
        navigate()

    for enclosure in enclosure_list:

        activity_label = "Update enclosure firmware"
        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_MAIN_DASHBOARD_XPATH, 10)
        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ENCLOSURE_LINK_XPATH, 10)
        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_XPATH_FIND_ENCLOSURE_ONE % enclosure.enclosurename)

        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_XPATH_SELECTOR_ENC, 10)
        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_ACTIVITY)
        ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_LE_ACTIVITY_RESOURCE_VIEW, 20)
        # if not in Enclosure activity page navigate

        ui_lib.wait_for_element_visible(FusionEnclosuresPage.XPATH_LE_UPDAtE_ACTIVITY % "Add", PerfConstants.PROFILE_POWER_VALIDATION)
        # expand

        ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_enc_ACTIVITY_COLLAPSER)
        # Negative test
        if enclosure.negbb_flagonly == "Yes":
            neg_msg = ui_lib.get_text(FusionEnclosuresPage.ID_XPATH_NEG_TEXT_ENC, 30)
            logger.info("Message from oneview :" + str(neg_msg))

            ovpm = re.search('No update required. Selected firmware is already installed for the Onboard Administrator', neg_msg)
            if ovpm:
                logger.info("Found the No update required information on activity page")
                return ovpm.group()
            else:
                logger.warn("No update required text not found")
                return neg_msg

        if ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_XPATH_ADD_BUTTON_ACTIVITY_XPATH):
            state = ui_lib.get_text(FusionEnclosuresPage.ID_XPATH_ADD_BTN_TEXT_ENC)
            ui_lib.wait_for_element_and_click(FusionEnclosuresPage.ID_XPATH_ADD_TEXT)

            if 'completed' in state.lower():
                logger.info("Firmware Completed Successfully" + str(state))

            else:
                logger.warn("Firmware Failed and it detailes : \n" + str(state))
                flagb = flagb + 1
                # fail - log state

            # check for over all message
            msg = ui_lib.get_text(FusionEnclosuresPage.ID_XPATH_CHECK_FOR_OVERALL_TEXT)
            logger.info("over all detailes :" + str(msg))

            # Negative test
            neg_msg = ui_lib.get_text(FusionEnclosuresPage.ID_XPATH_NEG_TEXT_ENC)
            logger.info("Message from oneview :" + str(neg_msg))

            ovpm = re.search('No update required. Selected firmware is already installed for the Onboard Administrator', neg_msg)
            if ovpm:
                logger.info("Found the No update required information on activity page\n {}".format(ovpm.group()))
                return ovpm.group()
            else:
                logger.warn("No update required text not found")

            # if issue visible
            if ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_XPATH_ISSUE_VISIBLE_DETAILES, 20):

                issue = ui_lib.get_text(FusionEnclosuresPage.ID_GET_TEXT_ISSUE)
                logger.warn("issue detailes :" + str(issue))
                flagb = flagb + 1
            # if resolution visible
            if ui_lib.wait_for_element_visible(FusionEnclosuresPage.ID_RESOLUTION_XPATH):

                res = ui_lib.get_text(FusionEnclosuresPage.ID_RESOLUTION_XPATH)
                logger.warn("Resolution detailes:" + str(res))
                flagb = flagb + 1
        else:
            logger.warn("Firmware update not found")
            flagb = flagb + 1

    if flagb > 0:
        logger.warn("Enclosure Firmware Failed ")
        return False

    else:
        logger.info("Enclosure Firmware update success")
        return True


def tbird_validate_interconnectbayset_and_viewside_in_interconnectlinktopology(*enc_obj):
    """ Takes bayset, or view as input parameters, selects the same
        and verifys that its properties are displayed appropriately in
        Enclosure interconnect link topology view.
        * Required arguments (bayset or view or both attriutes)
        <enclosures_dcs>
            <enclosure name="0000A66102" bayset="1" view="BOTH" />
        </enclosures_dcs>
    """
    navigate()
    s2l = ui_lib.get_s2l()
    error_string = " "
    error = 0
    bayset = ""
    view = ""
    if isinstance(enc_obj, test_data.DataObj):
        enc_obj = [enc_obj]
    elif isinstance(enc_obj, tuple):
        enc_obj = list(enc_obj[0])

    for enclosure in enc_obj:
        logger.info("Validate View Interconnect bayset and View side for enclosure %s" % enclosure.name)
        if not select_enclosure(enclosure.name):
            continue

        #  select interconnect link topology
        FusionUIBase.select_view_by_name('Interconnect Link Topology')

        # Select interconnect bayset
        if hasattr(enclosure, "bayset"):

            if enclosure.bayset == "All":
                bayset = "4"
            else:
                bayset = enclosure.bayset

            TBirdEnclosuresInterconnectLinkTopology.click_interconnect_bayset_option(bayset, 10, True)

            if TBirdVerifyEnclosures.verify_interconnect_bayset_option(bayset, 10, False):
                logger.info("Interocnnect bay set is selected successfully")
            else:
                error += 1
                error_string = "failed to verify the selected bay set %s for %s enclosure " % (bayset, enclosure) + "\t"
        else:
            # this is the default value displays on Enclosure interconnect link topology page
            bayset = "4"
        # Select View side
        if hasattr(enclosure, "view"):

            if enclosure.view == "A-side":
                view = "1"
            elif enclosure.view == "B-side":
                view = "2"
            elif enclosure.view == "Both":
                view = "3"

            TBirdEnclosuresInterconnectLinkTopology.click_view_side_option(view, 10, True)

            if TBirdVerifyEnclosures.verify_view_side_option(view, 10, False):
                logger.info("View side is selected successfully")
            else:
                error += 1
                error_string = "failed to verify the selected view side %s for %s enclosure" % (enclosure.view, enclosure) + "\t"
        else:
            # this is the default value displays on Enclosure interconnect link topology page
            view = "3"
        encl_list = []
        encl_list = TBirdEnclosuresInterconnectLinkTopology.get_enclosure_list_from_interconnect_link_topology(15)
        encl_count = 1
        for encl in encl_list:
            encl_ic_bay_port_list = TBirdEnclosuresInterconnectLinkTopology.get_interconnect_cxp_bay_from_interconnect_link_topology(encl_count, 15, False)

            for bay_data in encl_ic_bay_port_list:
                bay_data = bay_data.split("\n")

                if _validate_enclosures_show_viewside_bayset(bayset, view, bay_data[0]):
                    logger.info("Enclosure cxpport fabric and viewside is displayed properly")

                else:
                    error += 1
                    error_string = "failed to show fabric and viewside for %s enclosure" % (enclosure) + "\t"
            encl_count += 1
        if error > 0:
            raise AssertionError(error_string)
        else:
            return True


def _validate_enclosures_show_viewside_bayset(bayset, view, bay_info):
    '''
    This functions validates and returns displayed bayset (1 or 2 or 3 or All)
    and view side (A-side or B-side or Both) for TBird Enlcosure
    in interconnect link topology view.
    '''
    logger.debug("validates [ displayed View Interconnect bay set ] option for topology Enclosures")

    valid = False

    if ((bayset == "1") and (view == "3")):

        if (bay_info == "1" or bay_info == "4"):
            valid = True

    elif (bayset == '2' and view == '3'):

        if (bay_info == "2" or bay_info == "5"):
            valid = True

    elif ((bayset == "3") and (view == "3")):

        if (bay_info == "3" or bay_info == "6"):
            valid = True

    elif (bayset == "4" and view == "3"):
        if (bay_info == "1" or bay_info == "4" or bay_info == "2" or bay_info == "5" or bay_info == "3" or bay_info == "6"):
            valid = True

    elif (bayset == "1" and view == "1"):
        if (bay_info == "1"):
            valid = True

    elif (bayset == "2" and view == "1"):
        if (bay_info == "2"):
            valid = True

    elif (bayset == "3" and view == "1"):
        if (bay_info == "3"):
            valid = True

    elif (bayset == "4" and view == "1"):
        if (bay_info == "1" or bay_info == "2" or bay_info == "3"):
            valid = True

    elif (bayset == "1" and view == "2"):
        if (bay_info == "4"):
            valid = True

    elif (bayset == "2" and view == "2"):
        if (bay_info == "5"):
            valid = True

    elif (bayset == "3" and view == "2"):
        if (bay_info == "6"):
            valid = True

    elif (bayset == "4" and view == "2"):
        if (bay_info == "4" or bay_info == "5" or bay_info == "6"):
            valid = True

    return valid


def tbird_validate_interconnect_link_topology_numbering(enc_obj):
    """ Make sure the populated  cxp topology is expected,
        and that its properties are displayed appropriately.
        Arguments:
            Enc obj: displayed on the OneView UI (one-based)

    """
    for enclosure in enc_obj:
        logger.info("Validate cxp topology for enclosure %s" % enclosure.name)
        if not select_enclosure(enclosure.name):
            continue

        # interconnect link topology
        FusionUIBase.select_view_by_name('Interconnect Link Topology')

        # get enclosure list
        encl_list = []
        encl_list = TBirdEnclosuresInterconnectLinkTopology.get_enclosure_list_from_interconnect_link_topology(15)
        no_of_encl = len(encl_list)
        logger.info("Interconnect link topology validation is for %s Enclosures" % (no_of_encl))

        error_string = " "
        port = 1
        d = {}
        error = 0
        if no_of_encl > 1:
            (error, d, encl_no, encl_lst, power_state, data, member_list) = _get_validate_enclosure_numbering(encl_list)
            if error > 0:
                raise AssertionError("Invalid Interconnect Link Topoloy: Enclosure numbering is failed")
            else:
                return True


def _get_validate_enclosure_numbering(encl_list):
    logger.info("validate and get enclosure numbering in interconnect link topology")
    d = {}
    encl_no = {}
    data = defaultdict(list)
    members = defaultdict(list)
    subdata = data["enclosuremembers"]
    member_list = []
    power_state_of_icms = {}
    encl_1 = " "
    encl_2 = " "
    encl_3 = " "
    encl_4 = " "
    encl_5 = " "
    port = 1
    error = 0
    power_state = {}
    count = 1
    encl_len = len(encl_list)
    bside_bay_no = " "
    for encl in encl_list:
        encl_name = encl
        logger.info("enclosure name is %s" % encl_name)
        encl_ic_bay_port_list = []

        encl_ic_bay_port_list = TBirdEnclosuresInterconnectLinkTopology.get_interconnect_cxp_bay_from_interconnect_link_topology(count, 15, False)

        for bay_data in encl_ic_bay_port_list:
            bay_data = bay_data.split("\n")
            # IF Virtual Connect ICM is present in A side bayset try to assign 1 as Enclosre no for that encl otherwise give 2, and get connected port information too
            if any(FusionUIConst.CONST_POTASH in loop for loop in bay_data) or any("FusionUIConst.CONST_HAFNIUM_POTASSIUM" in loop for loop in bay_data):
                power_state["encl_{}_bay_{}".format(encl, bay_data[0])] = get_powerstate_information(bay_data[0], bay_data[3], encl_name)
                logger.info("power state of icm %s is %s" % (bay_data[3], power_state["encl_{}_bay_{}".format(encl, bay_data[0])]))

                if(bay_data[0] == "1" or bay_data[0] == "2" or bay_data[0] == "3"):
                    data["enclosuremembers"].append({"enclname": encl, "enclno": 1})
                    members["list"].append({"enclname": encl, "productname": 'Virtual Connect SE 40Gb F8 Module for Synergy or Synergy 40Gb F8 Switch Module', "bayno": bay_data[0]})
                    aside_bay_no = bay_data[0]

                    i = 1
                    j = 5
                    d = _get_process_connected_port_information(d, count, i, j, encl_name, bay_data, power_state)

                    encl_no[str(encl_name)] = 1

                    logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))

                    encl_1 = encl_name

                else:

                    if(bay_data[0] == "4" or bay_data[0] == "5" or bay_data[0] == "6"):
                        data["enclosuremembers"].append({"enclname": encl, "enclno": 2})
                        members["list"].append({"enclname": encl, "productname": 'Virtual Connect SE 40Gb F8 Module for Synergy or Synergy 40Gb F8 Switch Module', "bayno": bay_data[0]})
                        bside_bay_no = bay_data[0]

                        encl_no[str(encl_name)] = 2
                        logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                        encl_2 = encl_name
                        i = 1
                        j = 5
                        d = _get_process_connected_port_information(d, count, i, j, encl_name, bay_data, power_state)
            # Get connected port information for ICM and check for bay no and encl name
            elif any(FusionUIConst.CONST_CL20 in data for data in bay_data):
                power_state["encl_{}_bay_{}".format(encl, bay_data[0])] = get_powerstate_information(bay_data[0], bay_data[2], encl_name)
                members["list"].append({"enclname": encl, "productname": 'HP Synergy Interconnect Link Module', "bayno": bay_data[0]})

                if(bay_data[0] == "1" or bay_data[0] == "2" or bay_data[0] == "3"):
                    if any((2 not in i.values()) and (3 not in i.values()) for i in subdata):

                        if (encl_1 is not None and d["encl_{!s}_k_bay{}_port1_connectedencl".format(encl_1, aside_bay_no)] is not None):

                            if ((d["encl_{!s}_k_bay{}_port1_connectedencl".format(encl_1, aside_bay_no)] or d["encl_{!s}_k_bay{}_port4_connectedencl".format(encl_1, aside_bay_no)]) == encl_name):
                                data["enclosuremembers"].append({"enclname": encl, "enclno": 2})
                                encl_no[str(encl_name)] = 2
                                logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                encl_2 = encl_name

                            elif ("encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0]) in d):

                                if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] is not None):

                                    if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] or d["encl_{!s}_cl_bay{}_port2_connectedencl".format(encl_name, bay_data[0])] == encl_1):

                                        data["enclosuremembers"].append({"enclname": encl, "enclno": 2})
                                        encl_no[str(encl_name)] = 2
                                        logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                        encl_2 = encl_name
                            else:
                                data["enclosuremembers"].append({"enclname": encl, "enclno": 2})
                                encl_no[str(encl_name)] = 2
                                logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                encl_2 = encl_name
                        if (encl_1 is not None and d["encl_{!s}_k_bay{}_port2_connectedencl".format(encl_1, aside_bay_no)] is not None):

                            if ((d["encl_{!s}_k_bay{}_port2_connectedencl".format(encl_1, aside_bay_no)] or d["encl_{!s}_k_bay{}_port3_connectedencl".format(encl_1, aside_bay_no)]) == encl_name):
                                data["enclosuremembers"].append({"enclname": encl, "enclno": 3})
                                encl_no[str(encl_name)] = 3
                                logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                encl_3 = encl_name

                            elif ("encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0]) in d):

                                if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] is not None):

                                    if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] or d["encl_{!s}_cl_bay{}_port2_connectedencl".format(encl_name, bay_data[0])] == encl_1):

                                        data["enclosuremembers"].append({"enclname": encl, "enclno": 3})
                                        encl_no[str(encl_name)] = 3
                                        logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                        encl_3 = encl_name
                            else:
                                data["enclosuremembers"].append({"enclname": encl, "enclno": 3})
                                encl_no[str(encl_name)] = 3
                                logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                encl_3 = encl_name

                elif (bay_data[0] == "4" or bay_data[0] == "5" or bay_data[0] == "6"):
                    i = 1
                    j = 2
                    d = _get_process_connected_port_information(d, count, i, j, encl_name, bay_data, power_state)
                    if any((1 not in i.values()) and (3 not in i.values()) for i in subdata):
                        if (encl_2 is not None and d["encl_{!s}_k_bay{}_port1_connectedencl".format(encl_2, bside_bay_no)] is not None):

                            if ((d["encl_{!s}_k_bay{}_port1_connectedencl".format(encl_2, bside_bay_no)] or d["encl_{!s}_k_bay{}_port4_connectedencl".format(encl_2, bside_bay_no)]) == encl_name):
                                data["enclosuremembers"].append({"enclname": encl, "enclno": 1})
                                encl_no[str(encl_name)] = 1
                                logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                encl_1 = encl_name

                            elif ("encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0]) in d):

                                if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] is not None):

                                    if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] or d["encl_{!s}_cl_bay{}_port2_connectedencl".format(encl_name, bay_data[0])] == encl_2):

                                        data["enclosuremembers"].append({"enclname": encl, "enclno": 1})
                                encl_no[str(encl_name)] = 1
                                logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                encl_1 = encl_name
                            else:
                                data["enclosuremembers"].append({"enclname": encl, "enclno": 1})
                                encl_no[str(encl_name)] = 1
                                logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                encl_1 = encl_name

                        if (encl_2 is not None and d["encl_{!s}_k_bay{}_port2_connectedencl".format(encl_2, bside_bay_no)] is not None):

                            if ((d["encl_{!s}_k_bay{}_port2_connectedencl".format(encl_2, bside_bay_no)] or d["encl_{!s}_k_bay{}_port3_connectedencl".format(encl_2, bside_bay_no)]) == encl_name):
                                data["enclosuremembers"].append({"enclname": encl, "enclno": 3})
                                encl_no[str(encl_name)] = 3
                                logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                encl_3 = encl_name
                            elif ("encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0]) in d):

                                if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] is not None):

                                    if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] or d["encl_{!s}_cl_bay{}_port2_connectedencl".format(encl_name, bay_data[0])] == encl_2):

                                        data["enclosuremembers"].append({"enclname": encl, "enclno": 3})
                                        encl_no[str(encl_name)] = 3
                                        logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                        encl_3 = encl_name
                            else:
                                data["enclosuremembers"].append({"enclname": encl, "enclno": 3})
                                encl_no[str(encl_name)] = 3
                                logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                encl_3 = encl_name

            # Get connected port information for ICM and check for bay no and encl name
            elif any(FusionUIConst.CONST_CL10 in data for data in bay_data):
                power_state["encl_{}_bay_{}".format(encl, bay_data[0])] = get_powerstate_information(bay_data[0], bay_data[2], encl_name)
                logger.info("power state of icm %s is %s" % (bay_data[2], power_state["encl_{}_bay_{}".format(encl, bay_data[0])]))
                members["list"].append({"enclname": encl, "productname": 'Synergy 10Gb Interconnect Link Module', "bayno": bay_data[0]})
                if(bay_data[0] == "1" or bay_data[0] == "2" or bay_data[0] == "3"):
                    i = 1
                    j = 2
                    d = _get_process_connected_port_information(d, count, i, j, encl_name, bay_data, power_state)
                    if any((1 in i.values()) for i in subdata):

                        if ("encl_{!s}_k_bay{}_port1_connectedencl".format(encl_1, aside_bay_no) in d):
                            if (encl_1 is not None and encl_2 is None and d["encl_{!s}_k_bay{}_port1_connectedencl".format(encl_1, aside_bay_no)] is not None):

                                if (d["encl_{!s}_k_bay{}_port1_connectedencl".format(encl_1, aside_bay_no)] == encl_name):
                                    data["enclosuremembers"].append({"enclname": encl, "enclno": 2})
                                    encl_no[str(encl_name)] = 2
                                    logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                    encl_2 = encl_name
                                elif ("encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0]) in d):

                                    if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] is not None):

                                        if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] == encl_1):

                                            data["enclosuremembers"].append({"enclname": encl, "enclno": 2})
                                            encl_no[str(encl_name)] = 2
                                            logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                            encl_2 = encl_name
                                    else:
                                        data["enclosuremembers"].append({"enclname": encl, "enclno": 2})
                                        encl_no[str(encl_name)] = 2
                                        logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                        encl_2 = encl_name

                        if ("encl_{!s}_k_bay{}_port2_connectedencl".format(encl_1, aside_bay_no) in d):

                            if (encl_1 is not None and d["encl_{!s}_k_bay{}_port2_connectedencl".format(encl_1, aside_bay_no)] is not None):

                                if (d["encl_{!s}_k_bay{}_port2_connectedencl".format(encl_1, aside_bay_no)] == encl_name):
                                    data["enclosuremembers"].append({"enclname": encl, "enclno": 3})
                                    encl_no[str(encl_name)] = 3
                                    logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                    encl_3 = encl_name

                            elif ("encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0]) in d):

                                if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] is not None):

                                    if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] == encl_1):

                                        data["enclosuremembers"].append({"enclname": encl, "enclno": 3})
                                        encl_no[str(encl_name)] = 3
                                        logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                        encl_3 = encl_name
                                else:
                                    data["enclosuremembers"].append({"enclname": encl, "enclno": 3})
                                    encl_no[str(encl_name)] = 3
                                    logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                    encl_3 = encl_name

                        if ("encl_{!s}_k_bay{}_port3_connectedencl".format(encl_1, aside_bay_no) in d and encl_len > 3):
                            if (encl_1 is not None and d["encl_{!s}_k_bay{}_port3_connectedencl".format(encl_1, aside_bay_no)] is not None):

                                if (d["encl_{!s}_k_bay{}_port3_connectedencl".format(encl_1, aside_bay_no)] == encl_name):
                                    data["enclosuremembers"].append({"enclname": encl, "enclno": 4})
                                    encl_no[str(encl_name)] = 4
                                    logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                    encl_4 = encl_name
                            elif ("encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0]) in d):

                                if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] is not None):

                                    if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] == encl_1):

                                        data["enclosuremembers"].append({"enclname": encl, "enclno": 4})
                                        encl_no[str(encl_name)] = 4
                                        logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                        encl_4 = encl_name
                                else:
                                    data["enclosuremembers"].append({"enclname": encl, "enclno": 4})
                                    encl_no[str(encl_name)] = 4
                                    logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                    encl_4 = encl_name

                        if ("encl_{!s}_k_bay{}_port4_connectedencl".format(encl_1, aside_bay_no) in d):
                            if (encl_1 is not None and d["encl_{!s}_k_bay{}_port4_connectedencl".format(encl_1, aside_bay_no)] is not None):

                                if (d["encl_{!s}_k_bay{}_port4_connectedencl".format(encl_1, aside_bay_no)] == encl_name):
                                    data["enclosuremembers"].append({"enclname": encl, "enclno": 5})
                                    encl_no[str(encl_name)] = 5
                                    logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                    encl_5 = encl_name

                            elif ("encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0]) in d):

                                if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] is not None):

                                    if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] == encl_1):

                                        data["enclosuremembers"].append({"enclname": encl, "enclno": 5})
                                        encl_no[str(encl_name)] = 5
                                        logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                        encl_5 = encl_name
                                else:
                                    data["enclosuremembers"].append({"enclname": encl, "enclno": 5})
                                    encl_no[str(encl_name)] = 5
                                    logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                    encl_5 = encl_name

                elif (bay_data[0] == "4" or bay_data[0] == "5" or bay_data[0] == "6"):
                    port = 1
                    i = 1
                    j = 2
                    d = _get_process_connected_port_information(d, count, i, j, encl_name, bay_data, power_state)

                    if any((2 in i.values()) for i in subdata):
                        if ("encl_{!s}_k_bay{}_port1_connectedencl".format(encl_2, bside_bay_no) in d):
                            if (encl_2 is not None and d["encl_{!s}_k_bay{}_port1_connectedencl".format(encl_2, bside_bay_no)] is not None):

                                if (d["encl_{!s}_k_bay{}_port1_connectedencl".format(encl_2, bside_bay_no)] == encl_name):
                                    data["enclosuremembers"].append({"enclname": encl, "enclno": 1})
                                    encl_no[str(encl_name)] = 1
                                    logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                    encl_1 = encl_name
                            elif ("encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0]) in d):
                                if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] is not None):

                                    if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] == encl_2):

                                        data["enclosuremembers"].append({"enclname": encl, "enclno": 1})
                                        encl_no[str(encl_name)] = 1
                                        logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                        encl_1 = encl_name
                                else:
                                    data["enclosuremembers"].append({"enclname": encl, "enclno": 1})
                                    encl_no[str(encl_name)] = 1
                                    logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                    encl_1 = encl_name

                        if ("encl_{!s}_k_bay{}_port2_connectedencl".format(encl_2, bside_bay_no) in d):
                            if (encl_2 is not None and d["encl_{!s}_k_bay{}_port2_connectedencl".format(encl_2, bside_bay_no)] is not None):

                                if ((d["encl_{!s}_k_bay{}_port2_connectedencl".format(encl_2, bside_bay_no)]) == encl_name):
                                    data["enclosuremembers"].append({"enclname": encl, "enclno": 3})
                                    encl_no[str(encl_name)] = 3
                                    logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                    encl_3 = encl_name
                            elif ("encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0]) in d):
                                if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] is not None):

                                    if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] == encl_2):
                                        data["enclosuremembers"].append({"enclname": encl, "enclno": 3})
                                        encl_no[str(encl_name)] = 3
                                        logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                        encl_3 = encl_name
                                else:
                                    data["enclosuremembers"].append({"enclname": encl, "enclno": 3})
                                    encl_no[str(encl_name)] = 3
                                    logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                    encl_3 = encl_name

                        if ("encl_{!s}_k_bay{}_port3_connectedencl".format(encl_2, bside_bay_no) in d and encl_len > 3):
                            if ((encl_2 != " ") and d["encl_{!s}_k_bay{}_port3_connectedencl".format(encl_2, bside_bay_no)] is not None):

                                if (d["encl_{!s}_k_bay{}_port3_connectedencl".format(encl_2, bside_bay_no)] == encl_name):
                                    data["enclosuremembers"].append({"enclname": encl, "enclno": 4})
                                    encl_no[str(encl_name)] = 4
                                    logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                    encl_4 = encl_name
                                elif ("encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0]) in d):
                                    if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] is not None):

                                        if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] == encl_2):
                                            data["enclosuremembers"].append({"enclname": encl, "enclno": 4})
                                            encl_no[str(encl_name)] = 4
                                            logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                            encl_4 = encl_name
                                    else:
                                        data["enclosuremembers"].append({"enclname": encl, "enclno": 4})
                                        encl_no[str(encl_name)] = 4
                                        logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                        encl_4 = encl_name
                        if ("encl_{!s}_k_bay{}_port4_connectedencl".format(encl_2, bside_bay_no) in d):
                            if ((encl_2 != " ") and d["encl_{!s}_k_bay{}_port4_connectedencl".format(encl_2, bside_bay_no)] is not None):

                                if ((d["encl_{!s}_k_bay{}_port4_connectedencl".format(encl_2, bside_bay_no)]) == encl_name):
                                    data["enclosuremembers"].append({"enclname": encl, "enclno": 5})
                                    encl_no[str(encl_name)] = 5
                                    logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                    encl_5 = encl_name
                                elif ("encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0]) in d):
                                    if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] is not None):

                                        if (d["encl_{!s}_cl_bay{}_port1_connectedencl".format(encl_name, bay_data[0])] == encl_2):
                                            data["enclosuremembers"].append({"enclname": encl, "enclno": 5})
                                            encl_no[str(encl_name)] = 5
                                            logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                            encl_5 = encl_name
                                    else:
                                        data["enclosuremembers"].append({"enclname": encl, "enclno": 5})
                                        encl_no[str(encl_name)] = 5
                                        logger.info("encl %s  is %s " % (encl_no[str(encl_name)], encl_name))
                                        encl_5 = encl_name

        count += 1

    encl_lst = []
    logger.info("----------------------------------------")
    logger.info("Enclosure Numering after the validation is")
    logger.info("----------------------------------------")
    if (encl_1 != " "):
        logger.info("encl %s  is %s " % (encl_no[str(encl_1)], encl_1))
        encl_lst.append(encl_1)
    if (encl_2 != " "):
        logger.info("encl %s  is %s " % (encl_no[str(encl_2)], encl_2))
        encl_lst.append(encl_2)
    if (encl_3 != " "):
        logger.info("encl %s  is %s " % (encl_no[str(encl_3)], encl_3))
        encl_lst.append(encl_3)
    if (encl_4 != " "):
        logger.info("encl %s  is %s " % (encl_no[str(encl_4)], encl_4))
        encl_lst.append(encl_4)
    if (encl_5 != " "):
        logger.info("encl %s  is %s " % (encl_no[str(encl_5)], encl_5))
        encl_lst.append(encl_5)
    logger.info("----------------------------------------")

    if ((encl_no[str(encl_1)]) != 1):
        error += 1
        logger.warn("Encl one numbering is not proper please verify Potash is present in Bay 1 or 2 or 3 in Frist Enclosure")
    elif ((encl_no[str(encl_2)]) != 2 and (encl_len >= 2)):
        error += 1
        logger.warn("Encl two numbering is not proper please verify Potash is present in Bay 4 or 5 or 6 in Second Enclosure \n  or Check connectivity of L1 and L4 ports of First Enclosure")
    elif ((encl_len >= 3) and (encl_no[str(encl_3)]) != 3):
        error += 1
        logger.warn("Encl three numbering is not proper")
    elif ((encl_len >= 4) and (encl_no[str(encl_4)]) != 4):
        error += 1
        logger.warn("Encl four numbering is not proper")
    elif ((encl_len >= 5) and (encl_no[str(encl_5)]) != 5):
        error += 1
        logger.warn("Encl five numbering is not proper")

    return (error, d, encl_no, encl_lst, power_state, data, member_list)


def _get_process_connected_port_information(d, count, i, j, encl_name, bay_data, power_state):
    '''
    Function processes the connected port information and displays port and connected
    to information
    '''
    for port in range(i, j):
        (connected_port, connected_ic) = _get_connectedport_information(count, bay_data[0], power_state, port)
        if (connected_port is None):
            d["encl_{!s}_k_bay{}_port{}_connectedencl".format(encl_name, bay_data[0], port)] = None
            d["encl_{!s}_k_bay{}_port{}_connectedport".format(encl_name, bay_data[0], port)] = None
            d["encl_{!s}_k_bay{}_port{}_connected_ic".format(encl_name, bay_data[0], port)] = None
        elif(connected_ic != " " and connected_ic is not None):
            d["encl_{!s}_k_bay{}_port{}_connectedencl".format(encl_name, bay_data[0], port)] = connected_ic.split(",")[0]
            d["encl_{!s}_k_bay{}_port{}_connectedport".format(encl_name, bay_data[0], port)] = connected_port
            d["encl_{!s}_k_bay{}_port{}_connected_ic".format(encl_name, bay_data[0], port)] = connected_ic

            if ('L' + repr(port) == "L1"):
                logger.info("port 1 conneted to is %s" % d["encl_{!s}_k_bay{}_port{}_connectedencl".format(encl_name, bay_data[0], port)])

            elif ('L' + repr(port) == "L4"):
                logger.info("port 4 conneted to is %s" % d["encl_{!s}_k_bay{}_port{}_connectedencl".format(encl_name, bay_data[0], port)])

            elif ('L' + repr(port) == "L2"):
                logger.info("port 2 conneted to is %s" % d["encl_{!s}_k_bay{}_port{}_connectedencl".format(encl_name, bay_data[0], port)])

            else:
                logger.info("port 3 conneted to is %s" % d["encl_{!s}_k_bay{}_port{}_connectedencl".format(encl_name, bay_data[0], port)])
    return d


def _get_connectedport_information(count, bay, power_state, port):
    '''
    Function, clicks on each port and captures the connected port
    information
    '''
    connected_port = " "
    connected_ic = " "
    TBirdEnclosuresInterconnectLinkTopology.click_cxpport_interconnect_link_topology(count, bay, port)
    port_status = TBirdEnclosuresInterconnectLinkTopology.get_cxpport_status_interonnect_link_topology(count, bay, port)
    logger.info("port %s status is %s" % (port, port_status))

    if ((port_status == "ok") or (port_status == "error") or (power_state == "Off")):

        connected_webelement = TBirdEnclosuresInterconnectLinkTopology.get_connected_webelement_link_topology(count, bay, port)

        if connected_webelement is None:
            logger.info("Data connect element in HTML page is not present")
            connected_port = None
            connected_ic = None
        else:
            connected_port = TBirdEnclosuresInterconnectLinkTopology.get_connected_cxpport_link_topology(connected_webelement)

            ele_2 = connected_webelement[:-1] + "-device-name"
            connected_ic = TBirdEnclosuresInterconnectLinkTopology.get_connected_ic_link_topology(ele_2)
            logger.info("connected interconnect is %s" % connected_ic)

    return (connected_port, connected_ic)


def get_powerstate_information(bay_num, interconnect, enclosure, timeout=10):
    '''
        function to get power state information of the ICM
    '''

    TBirdEnclosuresInterconnectLinkTopology.click_cxpport_cxp_interconnect(bay_num, interconnect)
    power_state = CommonOperationInterconnects.get_overview_power_state(5, False)
    logger.info("power state of icm %s is %s" % (interconnect, power_state))
    select_enclosure(enclosure)
    FusionUIBase.select_view_by_name('Interconnect Link Topology')
    return power_state


def validate_link_module_ok_state(enclosure_name):

    FusionUIBase.navigate_to_section(SectionType.ENCLOSURES, time_for_loading=5)
    VerifyEnclosures.verify_enclosure_exist(enclosure_name)
    TBirdCommonOperationEnclosures.click_enclosure(enclosure_name)
    FusionUIBase.select_view_by_name('Link Modules')
    total_bay = 2
    empty_bay = 0
    ok_bay = 0
    for i in range(total_bay):
        bay_num = i + 1
        if not TBirdVerifyEnclosures.verify_link_module_bay_empty(bay_num, fail_if_false=False):
            TBirdVerifyEnclosures.verify_link_module_bay_ok_status(bay_num, fail_if_false=True)
            ok_bay += 1
        else:
            empty_bay += 1
    if ok_bay < total_bay:
        logger.warn("not all of these link modules status is ok - %s out of %s is ok " % (ok_bay, total_bay))
        if ok_bay + empty_bay == total_bay:
            logger.warn("%s empty link module is skipped, test is considered PASS" % empty_bay)
            return True
        else:
            logger.warn("%s empty link module is skipped, %s link module left is not ok status " % (empty_bay, total_bay - ok_bay - empty_bay))
            return False

    logger.info("all of the link module status is ok - %s out of %s " % (ok_bay, total_bay))
    return True


def reset_link_module(enclosure_obj):
    """ Reset link module for 1 or multiple enclosure

    Arguments:
      name*                   --  Name of enclosure as a string.
      link_module_type*       -- Link module type active/standby
      ...               --  ...
    * Required Arguments
    """
    FusionUIBase.navigate_to_section(SectionType.ENCLOSURES, time_for_loading=5)

    total = len(enclosure_obj)
    done_reset = 0

    for n, enclosure in enumerate(enclosure_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(enclosure_obj), '-' * 14))
        logger.info("reset link module for enclosure named '%s'" % enclosure.name)
        if reset_link_module_by_name(enclosure.name, enclosure.link_module_type) is False:
            logger.warn("Enclosure '%s' is not reset link module in '%s' way successfully" % (enclosure.name, enclosure.link_module_type))
            continue
        else:
            done_reset += 1

    if done_reset == 0:
        ui_lib.fail_test("no enclosure to reset link module!")
    if done_reset != total:
        ui_lib.fail_test("error encounter when reset link module")

    logger.info("all of the enclosure(s) is successfully done reset link module - %s out of %s " % (done_reset, total))


def reset_link_module_by_name(enclosure_name, link_module_type):
    """ Reset Link Module

    Arguments:
          name*                     --  Name of enclosure as a string.
          link_module_type*          -- Link module type active/standby

    * Required Arguments
    """
    FusionUIBase.navigate_to_section(SectionType.ENCLOSURES, time_for_loading=5)
    logger.info("Reset link module of enclosure - %s" % enclosure_name)
    VerifyEnclosures.verify_enclosure_exist(enclosure_name)
    TBirdCommonOperationEnclosures.click_enclosure(enclosure_name)
    TBirdResetLinkModule.select_actions_reset_link_module()
    TBirdResetLinkModule.wait_reset_link_module_dialog_open()
    if link_module_type.lower() == "active":
        TBirdResetLinkModule.tick_reset_active()
    if link_module_type.lower() == "standby":
        TBirdResetLinkModule.tick_reset_standby()
    TBirdResetLinkModule.click_yes_reset_button()
    status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
    if status is True:
        logger.warn("unexpected error occurred: %s" % msg)
        ui_lib.fail_test(msg)
    TBirdResetLinkModule.wait_reset_link_module_dialog_close()
    logger.info("waiting for 'Reset Synergy Frame Link Module' Activity Completion")
    FusionUIBase.show_activity_sidebar(timeout=20)
    if TBirdCommonOperationEnclosures.wait_activity_action_ok(enclosure_name, "Reset Synergy Frame Link Module", timeout=300, fail_if_false=False):
        FusionUIBase.show_activity_sidebar()
        if link_module_type.lower() == "active":
            logger.info("waiting for 'Reset Synergy Frame Link Module' refresh task to complete")
            TBirdResetLinkModule.wait_unknown_notification_shown()
            if TBirdCommonOperationEnclosures.wait_enclosure_status_ok_or_warn(enclosure_name, timeout=300, fail_if_false=False) is True:
                logger.info("'Reset Synergy Frame Link Module' refresh task is completed successfully")
                return validate_link_module_ok_state(enclosure_name)
            else:
                ui_lib.fail_test("'Reset Synergy Frame Link Module' refresh task is not completed successfully ")
        if link_module_type.lower() == "standby":
            logger.info("Waiting for the backend task finished")
            TBirdResetLinkModule.wait_warn_notification_shown(fail_if_false=False)
            TBirdResetLinkModule.wait_warn_notification_disappear(fail_if_false=False)
            if TBirdResetLinkModule.wait_ok_notification_shown(fail_if_false=False) is True:
                logger.info("'Reset Synergy Frame Link Module' is compelted with 'OK' status")
                return validate_link_module_ok_state(enclosure_name)
            else:
                ui_lib.fail_test("'Reset Synergy Frame Link Module' is not successfully completed with 'ok' status")
    else:
        FusionUIBase.show_activity_sidebar()
        raise AssertionError(" 'Reset link module' did not complete successfully")

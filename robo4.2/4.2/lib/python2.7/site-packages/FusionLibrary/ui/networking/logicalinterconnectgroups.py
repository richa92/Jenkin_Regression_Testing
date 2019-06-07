# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.

"""
    Logical Interconnect Groups page
"""
from RoboGalaxyLibrary.data.test_data import DataObj
from robot.libraries.BuiltIn import BuiltIn


from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
import time
from FusionLibrary.ui.business_logic.base import FusionUIBase, FusionUIConst
from FusionLibrary.ui.business_logic.base import SectionType
from FusionLibrary.ui.business_logic.servers.enclosuregroups import CommonOperationEnclosureGroups
from FusionLibrary.ui.business_logic.networking.logicalinterconnects import VerifyLogicalInterconnects
from FusionLibrary.ui.business_logic.networking.logicalinterconnectgroups import (CommonOperationLogicalInterconnectGroups,
                                                                                  C7000CommonOperationLogicalInterconnectGroups,
                                                                                  TBirdCommonOperationLogicalInterconnectGroups,
                                                                                  DeleteLogicalInterconnectGroups,
                                                                                  C7000DeleteLogicalInterconnectGroups,
                                                                                  TBirdDeleteLogicalInterconnectGroups,
                                                                                  EditLogicalInterconnectGroups,
                                                                                  C7000EditLogicalInterconnectGroups,
                                                                                  TBirdEditLogicalInterconnectGroups,
                                                                                  VerifyLogicalInterconnectGroups,
                                                                                  C7000VerifyLogicalInterconnectGroups,
                                                                                  TBirdVerifyLogicalInterconnectGroups,
                                                                                  CreateLogicalInterconnectGroups,
                                                                                  C7000CreateLogicalInterconnectGroups,
                                                                                  TBirdCreateLogicalInterconnectGroups,
                                                                                  EditScopeForLogicalInterconnectGroups)
from RoboGalaxyLibrary.utilitylib import logging
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.networking.logicalinterconnectgroups_elements import FusionLogicalInterconnectGroupPage
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.general import base_page
import re


def navigate():
    FusionUIBase.navigate_to_section(SectionType.LOGICAL_INTERCONNECT_GROUPS)


# begin - create LIG (new layer)
def create_logical_interconnect_group(lig_obj):
    """ Create Ethernet Network
    Arguments:
      <lig>
          name*                     --  Name of logical interconnect group as a string.
          fastmaccachefailover*     --  Whether to enable 'Fast MAC cache failover'. Possible value: true|false.
          macrefreshinterval*       --  MAC refresh interval as integer. This setting will not take effect if fastmaccachefailover is set to false
          igmpsnooping*             --  Whether to enable 'IGMP Snooping'. Possible value: true|false.
          igmpidletimeout*          --  IGMP idle timeout interval as integer. This setting will not take effect if igmpsnooping is set to false
          loopprotection*           --  Whether to enable 'Loop protection'. Possible value: true|false.
          pausefloodprotection*     --  Whether to enable 'Pause flood protection'. Possible value: true|false.
                  qos*                      --  check whether Quality of service option is available in dropdown
          verifyqosoption*          --  check different options for QoS configuration type
          qos_configuration_type*   --  Possible value: Passthrough/Custom (with FCoE lossless)|Custom (without FCoE lossless)
          internal_networks*        --  Configure internal networks, can be empty which indicate no need to configure internal networks
          _check_activity           --  Whether to check activity after creating lig. Possible value: true|false.
          <switch> required, for specifying interconnect model
            bay*                    --  Interconnect bay no as integer. e.g. 1
            type*                   --  Interconnect bay model as string. Need to grap from create lig page. e.g. HP VC FlexFabric-20/40 F8 Module|HP VC FlexFabric-20/40 F8 Module
          <lus> optional, for adding uplink set
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
            <snmp> Optional, for configuring snmp related settings. if not present, use default snmp settings

              snmpenabled*          --  Whether to enable snmp settings, possible value: ENABLED|DISABLED
              syscontact*           --  SNMP System contact as string value.
              readcommunity*        --  SNMP Read community as string value.
              <trapdestination> Optional, for configuring snmp trap destination. Accept multiple nodes.
                trapdestination*    --  Trap destination. e.g. 192.168.1.2
                communitystring*    --  Community string as string value.
                trapformat*         --  Trap Format. Possible value: SNMPv1|SNMPv2
                <snmpv3>**          --  Optional, for configuring snmpv3 related settings. if not present, use default snmpv3 settings
                snmpv3enabled***    --  Whether to enable snmpv3 settings, possible value: ENABLED|DISABLED
                adduser              -- Optional,adds snmpv3 users
              syscontact            --  Optional,SNMP System contact as string value.
              readcommunity         --  Optional,SNMP Read community as string value.
              <trapdestination> Optional, for configuring snmp trap destination. Accept multiple nodes.
                trapdestination***    --  Trap destination. e.g. 192.168.1.2
                trapformat***         --  Trap Format. Possible value: SNMPv1|SNMPv2|SNMPv3
                notification_type***  -- Whether to enable notification type, Possible value : TRAP|INFORM.Applicable only for Trap Format snmpv3.
                snmp_user             -- Optional,to choose the snmpv3 user. If not, default user will be selected.Applicable only for Trap Format snmpv3.
                communitystring    --  Optional,Community string as string value. Applicable only for Trap Formats snmpv1 and snmpv2.
              <snmpaccess> Optional, for configuring snmp access. Accpet multiple nodes.
                iporsubnet*         --  IP or subnet for SNMP Access. e.g. 192.168.1.0/24

    * Required Arguments
    ** Applicable only for feature toggle in OVF293
    *** Mandatory arguments, Applicable only for feature toggle in OVF293

    Example:
        data/ligs -> @{TestData.ligs}
        <ligs>
            <lig  name="LIG-wpst32"
                 fastmaccachefailover="TRUE"
                 macrefreshinterval="10"
                 igmpsnooping="TRUE"
                 igmpidletimeout="250"
                 loopprotection="FALSE"
                 pausefloodprotection="FALSE"
                 verifyqosoptions="Passthrough,Custom (with FCoE lossless),Custom (without FCoE lossless)"
                                 uplink="DOT1P,DSCP,DSCP and DOT1P"
                                 downlink="DOT1P,DSCP,DSCP and DOT1P"
                 qos_configuration_type="Custom (with FCoE lossless)"
                 internal_networks="dev101-management, dev103-ft-a">
                <switch bay="1" type="HP VC FlexFabric 10Gb/24-Port Module" />
                <switch bay="2" type="HP VC FlexFabric 10Gb/24-Port Module" />
                <switch bay="3" type="HP VC FlexFabric 10Gb/24-Port Module" />
                <switch bay="4" type="HP VC FlexFabric 10Gb/24-Port Module" />
                <switch bay="5" type="HP VC 8Gb 20-Port FC Module" />
                <switch bay="6" type="HP VC 8Gb 20-Port FC Module" />
                <lus connectionMode="AUTO" lacptimer="30" name="FA-path3" native="" networkType="Fibre Channel" networks="FA3" ports="bay1:X1:Auto" preferredPort="" />
                <lus connectionMode="AUTO" lacptimer="30" name="FA-path4" native="" networkType="Fibre Channel" networks="FA4" ports="bay2:X1:Auto" preferredPort="" />
                <lus connectionMode="AUTO" lacptimer="30" name="FA-path1" native="" networkType="Fibre Channel" networks="FA1" ports="bay5:1:Auto" preferredPort="" />
                <lus connectionMode="AUTO" lacptimer="30" name="FA-path2" native="" networkType="Fibre Channel" networks="FA2" ports="bay6:1:Auto" preferredPort="" />
                <lus connectionMode="AUTO" lacptimer="" name="DA-path1" native="" networkType="Fibre Channel" networks="DA1" ports="bay3:X2:Auto" preferredPort="" />
                <lus connectionMode="AUTO" lacptimer="" name="DA-path2" native="" networkType="Fibre Channel" networks="DA2" ports="bay4:X2:Auto" preferredPort="" />
                <lus connectionMode="AUTO" lacptimer="" name="Pub-net" native="dev100" networkType="Ethernet" networks="dev100" ports="bay1:X3" preferredPort="" />
                <lus connectionMode="AUTO" lacptimer="" name="FO-net" native="dev102-vmmigration" networkType="Ethernet" networks="dev102-vmmigration" ports="bay3:X3" preferredPort="" />
                <lus connectionMode="AUTO" lacptimer="" name="PXE-net" native="dev300-pxeboot" networkType="Ethernet" networks="dev300-pxeboot" ports="bay3:X3" preferredPort="" />
                <snmp snmpenabled="ENABLED" syscontact="None" readcommunity="public">

                    <trapdestination trapdestination="10.0.0.12" communitystring="public1" trapformat="SNMPv2" />
                    <trapdestination trapdestination="172.2.1.3" communitystring="public2" trapformat="SNMPv1" />
                    <snmpaccess iporsubnet="192.168.1.0/24" />
                    <snmpaccess iporsubnet="192.168.1.1/24" />
                </snmp>
                **<snmpv3 snmpv3enabled="Enabled" syscontact="None" readcommunity="public">
                    <adduser username= "user6"
                      security_level="authenticationandprivacy" auth_protocol="MD5"
                      authentication_password="Password1" confirm_auth_password="Password1"
                      priv_protocol="AES-192" privacy_password="Password2"
                      confirm_priv_password="Password2"></adduser>
                    <trapdestination trapdestination= "10.101.11.14"  trapformat="snmpv3" notification_type="Trap"  snmp_user="user5" ></trapdestination>
                    </snmpv3>
                **<snmpv3 snmpv1v2enabled="Disabled" syscontact="None" readcommunity="public">
                  <adduser username= "user1"  security_level="none" ></adduser>
                  </snmpv3>
            </lig>
        </ligs>
    ** Applicable only for feature toggle in OVF293
    """
    navigate()

    logger.info("Adding Logical Interconnect Groups....")

    count = 0
    total_len = len(lig_obj)
    create_lig_list = []
    add_plus = False
    for n, lig in enumerate(lig_obj):
        # check if LIG is existing
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total_len, '-' * 14))
        logger.info("Adding a LIG with name '{0}'".format(lig.name))
        ui_lib.get_s2l().capture_page_screenshot()
        if not C7000VerifyLogicalInterconnectGroups.verify_lig_not_exist(lig.name, fail_if_false=False):
            logger.warn("LIG '{0}' already exists".format(lig.name))
            continue
        create_lig_list.append(lig)
        if add_plus is False:
            C7000CreateLogicalInterconnectGroups.click_create_logical_interconnect_group()
        else:
            logger.info("After clicking 'Create+' button, no need to click 'Create logical interconnect group' button to open the dialog ...")
        C7000CreateLogicalInterconnectGroups.wait_create_lig_dialog_shown()
        C7000CreateLogicalInterconnectGroups.select_general_section()
        C7000CreateLogicalInterconnectGroups.input_name(lig.name)
        C7000CreateLogicalInterconnectGroups.select_interconnect_type(lig.InterconnectType)
        C7000CreateLogicalInterconnectGroups.click_select_interconnects_button()

        # add_plus = False

        if n < total_len - 1:
            add_plus = True
        else:
            add_plus = False

        # choose interconnect bay
        C7000CreateLogicalInterconnectGroups.select_logical_interconnect_group_section()
        for switch_bay in lig.switch:
            _create_lig_add_interconnect_to_lig(switch_bay)

        # configure internal networks
        internal_networks = getattr(lig, "internal_networks", "")
        if internal_networks != "":
            _create_lig_create_internal_networks(internal_networks)
            # checking if Quality of services option is available in dropdown while creating LIG
        if hasattr(lig, 'qos'):
            if not C7000CreateLogicalInterconnectGroups.select_quality_of_service_section():
                logger.info("Quality of service option is not available while creating LIG")
                return False
            logger.info("Verified QoS values successfully ")
        # verifying QOS options
        if hasattr(lig, 'verifyqosoptions'):
            count_qos = 0
            FusionUIBase.select_view_by_name('Quality of Service')
            QOS_list = [item.strip() for item in lig.verifyqosoptions.split(',')]
            uplink_list = [item.strip() for item in lig.uplink.split(',')]
            downlink_list = [item.strip() for item in lig.downlink.split(',')]
            for qos in QOS_list:
                count_uplink = 0
                count_downlink = 0
                C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(qos)
                if qos != QOS_list[0]:
                    for uplink in uplink_list:
                        C7000CreateLogicalInterconnectGroups.select_qos_uplink_classfication(uplink)
                        count_uplink += 1
                    if count_uplink != len(uplink_list):
                        ui_lib.fail_test("failed to verify all the uplink options ")
                    for downlink in downlink_list:
                        C7000CreateLogicalInterconnectGroups.select_qos_downlink_classfication(downlink)
                        count_downlink += 1
                    if count_uplink != len(downlink_list):
                        ui_lib.fail_test("failed to verify all the downlink options")
                count_qos += 1
            C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(lig.lig_QOS_option)
            if count_qos != len(QOS_list):
                ui_lib.fail_test("failed to verify all the QoS configuration options")
        # create uplink sets
        if hasattr(lig, "lus"):
            total_lus = len(lig.lus)
            for i, uplink_set in enumerate(lig.lus):
                logger.info("Add uplink set {2} No: {0} --- Total: {1} {2}".format((i + 1), total_lus, '-' * 14))
                if i < total_lus - 1:
                    _create_lig_create_uplink_set(uplink_set, add_plus=True)
                else:
                    _create_lig_create_uplink_set(uplink_set)
        if getattr(lig, 'InterconnectType', '').lower() != 'fabric extender':
            # Interconnect Settings
            _create_lig_config_interconnect_settings(lig.fastmaccachefailover,
                                                     lig.macrefreshinterval,
                                                     lig.igmpsnooping,
                                                     lig.igmpidletimeout,
                                                     lig.loopprotection,
                                                     lig.pausefloodprotection)
        # SNMP
        if hasattr(lig, 'snmp'):
            _create_lig_config_snmp(lig.snmp)

        # Quality of Service (QoS)
        if hasattr(lig, 'qos_configuration_type'):
            _create_lig_config_qos(lig.qos_configuration_type)

        if add_plus is True:
            C7000CreateLogicalInterconnectGroups.click_create_plus_button()
        else:
            C7000CreateLogicalInterconnectGroups.click_create_button()

        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)

        if status is True:
            logger.warn("unexpected error occurred: %s" % msg)
            ui_lib.fail_test(msg)

        # wait operation done
        # C7000CreateLogicalInterconnectGroups.wait_status_changing_shown()
        # C7000CreateLogicalInterconnectGroups.wait_status_changing_disappear()
        # verify if exist in table list
        C7000VerifyLogicalInterconnectGroups.verify_lig_exist(lig.name, timeout=15)
        count += 1

    if C7000CreateLogicalInterconnectGroups.wait_create_lig_dialog_disappear(fail_if_false=False) is False:
        C7000CreateLogicalInterconnectGroups.click_cancel_button()

        C7000CreateLogicalInterconnectGroups.wait_create_lig_dialog_disappear()

    # basic verification
    for n, lig in enumerate(create_lig_list):
        # check LIG activity
        if getattr(lig, '_check_activity', 'true').lower() == 'true':
            FusionUIBase.show_activity_sidebar()
            CommonOperationLogicalInterconnectGroups.wait_activity_action_ok(lig.name, 'Create')
            FusionUIBase.show_activity_sidebar()

        logger.info("Add LIG {0} successfully".format(lig.name))

    if count == 0:
        logger.warn("No LIGs added!")
        logger.warn("Return value = False")
        return False

    if count != total_len:
        logger.warn("Not able to create all LIGs!")
        logger.warn("Return value = False")
        return False

    logger.debug("Return Value = True")
    return True


def create_natasha_logical_interconnect_group(lig_obj):
    """ Create Natasha Logical Interconnect Groups

    Arguments:
      <lig>
          name*                     --  Name of Natasha logical interconnect group as a string.
          interconnecttype          --   Interconnect Type of the Lig
        <switch> required, for specifying interconnect model
            enclosure               --  Enclosure the Interconnect belongs to
            bay*                    --  Interconnect bay no as integer. e.g. 1
            type*                   --  Interconnect bay model as string. Need to grap from create lig page. e.g. Synergy 12Gb SAS Connection Module
    * Required Arguments
    Example:
        data/natasha_ligs -> @{TestData.natasha_ligs}
        <natasha_ligs>
            <natasha_lig name="LIG_OVAEncICM" utilizationSampling='enable' intervalSamples='300', totalSamples='12'>
                 interconnecttype = "Synergy 12Gb SAS Connection Module"
                <switch enclosure="1" bay="1" type="Synergy 12Gb SAS Connection Module"/>
                <switch enclosure="1" bay="4" type="Synergy 12Gb SAS Connection Module" />
            </natasha_lig>
        </natasha_ligs>

    """
    navigate()
    logger.debug("Adding Natasha Logical Interconnect Groups...")
    total_len = len(lig_obj)
    for n, lig in enumerate(lig_obj):
        # check if LIG is existing
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total_len, '-' * 14))
        logger.info("Adding a Natasha LIG with name '{0}'".format(lig.name))

        if not TBirdCreateLogicalInterconnectGroups.wait_create_lig_dialog_shown(fail_if_false=False):
            TBirdCreateLogicalInterconnectGroups.click_create_logical_interconnect_group()
        TBirdCreateLogicalInterconnectGroups.wait_create_lig_dialog_shown()
        TBirdCreateLogicalInterconnectGroups.select_general_section()
        TBirdCreateLogicalInterconnectGroups.input_name(lig.name)
        TBirdCreateLogicalInterconnectGroups.select_interconnect_type(lig.interconnecttype)
        TBirdCreateLogicalInterconnectGroups.click_select_interconnects()
        TBirdCreateLogicalInterconnectGroups.select_logical_interconnect_group_section()
        for switch_bay in lig.switch:
            _create_tbird_lig_add_interconnect_to_lig(switch_bay)

        # Utilization Sampling
        if hasattr(lig, 'utilizationSampling'):
            if lig.utilizationSampling.lower() == 'enabled':
                TBirdCreateLogicalInterconnectGroups.toggle_sample_collection_enabled
            elif lig.utilizationSampling.lower() == 'disabled':
                TBirdCreateLogicalInterconnectGroups.toggle_sample_collection_disabled
        if hasattr(lig, 'intervalSamples'):
            TBirdCreateLogicalInterconnectGroups.input_interval_samples(lig.intervalSamples)
        if hasattr(lig, 'totalSamples'):
            TBirdCreateLogicalInterconnectGroups.input_total_number_of_samples(lig.totalSamples)
        errors_on_form = TBirdCreateLogicalInterconnectGroups.get_all_errors_on_create_dialog()

        if errors_on_form:
            ui_lib.fail_test("Error Seen on form during Natasha LIG '{}' creation -\n{}".format(lig.name, errors_on_form))
        TBirdCreateLogicalInterconnectGroups.click_create_button()
        error_status, error_msg = FusionUIBase.get_error_message_from_dialog()
        if error_status:
            ui_lib.fail_test("Error for Natasha LIG {} - \n{}".format(lig.name, error_msg))
        TBirdCreateLogicalInterconnectGroups.wait_create_lig_dialog_disappear(timeout=240, fail_if_false=True)
        FusionUIBase.show_activity_sidebar()
        CommonOperationLogicalInterconnectGroups.wait_activity_action_ok(lig.name, 'Create')
        logger.info("Added Natasha LIG {0} successfully".format(lig.name))


def create_tbird_logical_interconnect_group(lig_obj):
    """ Create Logical Interconnect Groups

    Arguments:
      <lig>
          name*                     --  Name of logical interconnect group as a string.
          interconnecttype          --   Interconnect Type of the Lig
          enclosure_count*          --  Enclosure count as number.
          interconnect_bay_set*     --  Interconnect bay set count as number.
          redundancy*               --  Possible value: Highly available/Non-redundant (A-side only)/Non-redundant (B-side only)/Redundant
          igmpsnooping*             --  Whether to enable 'IGMP Snooping'. Possible value: true|false.
          igmpidletimeout*          --  IGMP idle timeout interval as integer. This setting will not take effect if igmpsnooping is set to false
          loopprotection*           --  Whether to enable 'Loop protection'. Possible value: true|false.
          internal_networks*        --  Configure internal networks, can be empty which indicate no need to configure internal networks
          <switch> required, for specifying interconnect model
            enclosure               --  Enclosure the Interconnect belongs to
            bay*                    --  Interconnect bay no as integer. e.g. 1
            type*                   --  Interconnect bay model as string. Need to grap from create lig page. e.g. HP VC FlexFabric-20/40 F8 Module|HP VC FlexFabric-20/40 F8 Module
          <lus> optional, for adding uplink set
            lacptimer*              --  Possible value: Short (1s)|Long (30s). Only take effect when network type set to Ethernet|Tunnel|Untagged
            name*                   --  Uplink set name
            native*                 --  Ethernet name. Only take effect when network type set to Ethernet. e.g. dev102-vmmigration
            networkType*            --  Configure network type of uplink set. Possible value: Ethernet|Tunnel|Untagged
            networks*               --  Network names separated by comma. Only support specifying 1 network if network type set to Fibre Channel|Tunnel|Untagged. e.g. net14,net15,net16,net17
            ports*                  --  String value. Port configuration. Notice the difference of (Ethernet|Tunnel|Untagged) and (Fibre Cannel)
                                        * For Ethernet|Tunnel|Untagged, bay<bay no.>:<port name> .e.g. bay1:X1,bay1:X2
            <snmp> Optional, for configuring snmp related settings. if not present, use default snmp settings
              syscontact*           --  SNMP System contact as string value.
              readcommunity*        --  SNMP Read community as string value.
              <trapdestination> Optional, for configuring snmp trap destination. Accept multiple nodes.
                trapdestination*    --  Trap destination. e.g. 192.168.1.2
                communitystring*    --  Community string as string value.
                trapformat*         --  Trap Format. Possible value: SNMPv1|SNMPv2


                snmpv3enabled**    --  Whether to enable snmpv3 settings, possible value: ENABLED|DISABLED
                adduser              -- Optional,adds snmpv3 users
              syscontact            --  Optional,SNMP System contact as string value.
              readcommunity         --  Optional,SNMP Read community as string value.
              <trapdestination> Optional, for configuring snmp trap destination. Accept multiple nodes.
                trapdestination**    --  Trap destination. e.g. 192.168.1.2
                trapformat         --  Trap Format. Possible value: SNMPv1|SNMPv2|SNMPv3
                notification_type**  -- Whether to enable notification type, Possible value : TRAP|INFORM.Applicable only for Trap Format snmpv3.
                snmp_user             -- Optional,to choose the snmpv3 user. If not, default user will be selected.Applicable only for Trap Format snmpv3.
                communitystring    --  Optional,Community string as string value. Applicable only for Trap Formats snmpv1 and snmpv2.

    * Required Arguments

    ** Required Arguments for OVF292
    Example:   Potash_payload
        data/ligs -> @{TestData.ligs}
        <ligs>
            <lig name="LIG_OVAEncICM"
                 interconnecttype = "Virtual Connect SE 40Gb F8 Module for Synergy"
                 enclosure_count="2"
                 interconnect_bay_set="3"
                 redundancy="Highly available"
                 igmpsnooping="FALSE"
                 igmpidletimeout="250"
                 loopprotection="TRUE"
                 internal_networks="net1,net2">
                <switch enclosure="1" bay="3" type="Virtual Connect SE 40Gb F8 Module for Synergy" />
                <switch enclosure="1" bay="6" type="Synergy 10Gb Interconnect Link Module" />
                <switch enclosure="2" bay="3" type="Synergy 10Gb Interconnect Link Module" />
                <switch enclosure="2" bay="6" type="Virtual Connect SE 40Gb F8 Module for Synergy" />
                <lus>
             <uplink_set id = "1" name = "eth-100"  connectionMode = "AUTO" networkType = "Ethernet" lacptimer = "Long (30s)" networks = "eth-100" native = "" ports = "enc1:bay3:Q1:1,enc2:bay6:Q1:1" preferredPort = "" />
             <uplink_set id = "2" name = "SAN-1-A" networkType = "Fibre Channel"  networks = "SAN-1-A" ports = "enc1:bay3:Q2:1:Auto"/>
             <uplink_set id = "3" name = "SAN-2-A" networkType = "Fibre Channel"  networks = "SAN-2-A" ports = "enc2:bay6:Q2:1:Auto" />
             </lus>

                <snmp syscontact="None" readcommunity="public">
                    <trapdestination trapdestination="10.0.0.12" communitystring="public1" trapformat="SNMPv2" />
                    <trapdestination trapdestination="172.2.1.3" communitystring="public2" trapformat="SNMPv1" />
                </snmp>
            </lig>
        </ligs>

        For Carbon interconnects use below payload
        <ligs_carbon>
       <lig name="LIG-bay-carbon"  type="tbird" interconnecttype = "Virtual Connect SE 16Gb FC Module for Synergy"  fastmaccachefailover="TRUE"
            macrefreshinterval="10" intervalbetweensamples="120"
            totalsamples="20" snmpenabled="ENABLED" syscontact="admin@hp.com" readcommunity="public"
            enclosure_count="1" redundancy="Redundant" interconnect_bay_set="1">
           <switch enclosure="-1" bay="1" type="Virtual Connect SE 16Gb FC Module for Synergy" />
           <switch enclosure="-1" bay="4" type="Virtual Connect SE 16Gb FC Module for Synergy" />
           <lus>

             <uplink_set id = "1" name = "SAN-1-A"  networkType = "Fibre Channel"  networks = "SAN-1-A" ports = "enc1:bay1:1:Auto"/>
             <uplink_set id = "2" name = "SAN-2-A"  networkType = "Fibre Channel"  networks = "SAN-2-A" ports = "enc1:bay4:2:Auto,enc1:bay4:Q2:3:4 Gb/s"/>
             </lus>
        </lig>
     </ligs_carbon>
    **<ligs_snmpv3>
    <lig>
   <snmp snmpv3enabled="enabled" syscontact="None" >
                    <adduser username= "user6"
                      security_level="authenticationandprivacy" auth_protocol="MD5"
                      authentication_password="Password1" confirm_auth_password="Password1"
                      priv_protocol="AES-192" privacy_password="Password2"
                      confirm_priv_password="Password2"></adduser>
                    <add_snmpv3_trapdestination trapdestination= "10.101.11.14"  trapformat="snmpv3" notification_type="trap"  snmp_user="user5" ></add_snmpv3_trapdestination>
                    </snmp>
                **<snmp snmpv1v2enabled="disabled" syscontact="None" readcommunity="public">
                  <adduser username= "user1"  security_level="none" ></adduser>
                  </snmpv3>
            </lig>
        </ligs_snmp>
    ** Applicable only for feature toggle in OVF292

    """
    navigate()
    logger.debug("Adding Tbird Logical Interconnect Groups...")

    count = 0
    total_len = len(lig_obj)
    create_lig_list = []
    error_msg_list = []
    error_flag = 0

    for n, lig in enumerate(lig_obj):
        errors_on_form = []
        error_status = None
        # check if LIG is existing
        if not VerifyLogicalInterconnectGroups.verify_lig_not_exist(lig.name, fail_if_false=False):
            logger.warn("LIG '{0}' already exists".format(lig.name))
            continue
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total_len, '-' * 14))
        logger.info("Adding a LIG with name '{0}'".format(lig.name))

        if not TBirdCreateLogicalInterconnectGroups.wait_create_lig_dialog_shown(fail_if_false=False):
            TBirdCreateLogicalInterconnectGroups.click_create_logical_interconnect_group()
        TBirdCreateLogicalInterconnectGroups.wait_create_lig_dialog_shown()
        TBirdCreateLogicalInterconnectGroups.select_general_section()
        TBirdCreateLogicalInterconnectGroups.input_name(lig.name)

        redundancy_ov = lig.redundancy

        # if interconnect type is 'VC SE 40Gb F8 Module' ie POTASH or 'Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23' i.e HAFNIUM_POTASH select enclosure count , bay set number and redundancy
        if lig.interconnecttype.lower() == FusionUIConst.CONST_POTASH.lower() or lig.interconnecttype.lower() == FusionUIConst.CONST_HAFNIUM_POTASH.lower():
            TBirdCreateLogicalInterconnectGroups.select_interconnect_type(lig.interconnecttype)
            TBirdCreateLogicalInterconnectGroups.select_enclosure_count(lig.enclosure_count)
            TBirdCreateLogicalInterconnectGroups.select_interconnect_bay_set(lig.interconnect_bay_set)
        # if interconnect type is 'Virtual Connect 16Gb FC Module' i.e CARBON , verify that the enclosure count is set to 1 and available bay sets are 1 and 2
        elif lig.interconnecttype.lower() == FusionUIConst.CONST_CARBON.lower():
            TBirdCreateLogicalInterconnectGroups.select_interconnect_type(lig.interconnecttype)
            enclosure_static_count = TBirdCreateLogicalInterconnectGroups.get_enclosure_count(timeout=8)

            # check if the Enclosure count is 1 by default
            if enclosure_static_count:
                if int(enclosure_static_count) == 1:
                    logger._log_to_console_and_log_file("Enclosure Count set to '1' as expected")
                else:
                    logger.warn("Enclosure Count is '{}' but should be set to '1' by default!!".format(enclosure_static_count))
                    error_msg_list.append("Enclosure Count is '{}' but should be set to '1' by default!!".format(enclosure_static_count))
                    error_flag += 1
                    CreateLogicalInterconnectGroups.click_cancel_button()
                    continue
            else:
                logger.warn("Unable to get the Enclosure count!!")
                return False

            # check that the bay set is 1 and 2 and not 3
            if int(lig.interconnect_bay_set) > 2:
                logger.warn("Bay set can be 1 or 2 for Carbon.Invalid Bay set '{}'".format(lig.interconnect_bay_set))
                error_flag += 1
                error_msg_list.append("Bay set can be 1 or 2 for Carbon.Invalid Bayset '{}'".format(lig.interconnect_bay_set))
                logger.debug("Checking if Bay Set {} is visible in the dropdown".format(lig.interconnect_bay_set))
                if TBirdCreateLogicalInterconnectGroups.select_interconnect_bay_set(lig.interconnect_bay_set, fail_if_false=False):
                    logger.warn("Only Bay set 1 and 2 must be displayed in dropdown.But {} is visible as well and selectable!!".format(lig.interconnect_bay_set))
                    error_flag += 1
                    error_msg_list.append("Only Bay set 1 and 2 must be displayed in dropdown.But {} is are visible as well and selectable!!".format(lig.interconnect_bay_set))
                CreateLogicalInterconnectGroups.click_cancel_button()
                CreateLogicalInterconnectGroups.wait_create_lig_dialog_disappear()
                continue

            # check reduncy is not set to HA
            if lig.redundancy.lower() == 'highly available':
                logger.warn("Invalid redundancy for Carbon -- Highly available")
                error_msg_list.append("Invalid redundancy for Carbon -- Highly available")
                error_flag += 1
                logger.debug("Checking if 'Highly Available' is visible in redundancy dropdown")
                if TBirdCreateLogicalInterconnectGroups.select_redundancy(redundancy_ov, fail_if_false=False):
                    logger.warn("Highly Available is seen as option in redundancy dropdown for FC Carbon interconnect type!!")
                    error_flag += 1
                    error_msg_list.append("Highly Available is seen as option in redundancy dropdown for FC Carbon interconnect type!!")
                CreateLogicalInterconnectGroups.click_cancel_button()
                CreateLogicalInterconnectGroups.wait_create_lig_dialog_disappear()
                continue

            TBirdCreateLogicalInterconnectGroups.select_interconnect_bay_set(lig.interconnect_bay_set)

            ''' ADD More elif blocks for any new interconnect types added in FUTURE '''
        else:
            # invalid interconnect type
            logger.warn("Invalid interconnect type - {}.Aborting LIG '{}' Creation".format(lig.interconnecttype, lig.name))
            CreateLogicalInterconnectGroups.click_cancel_button()
            CreateLogicalInterconnectGroups.wait_create_lig_dialog_disappear()
            continue

        # if enclosure count is 1 check that redundancy is not HIGHLY AVAILABLE , if option seen cancel creation
        if int(lig.enclosure_count) == 1 and lig.redundancy.lower() == 'highly available':
            logger.warn("Since Enclosure Count is 1 , redundancy cannot be Highly Available.Check input!!")
            error_msg_list.append("Since Enclosure Count is 1 , redundancy cannot be Highly Available.Check input!!")
            error_flag += 1
            logger.debug("Checking if 'Highly Available' is visible in redundancy dropdown")
            if TBirdCreateLogicalInterconnectGroups.select_redundancy(redundancy_ov, fail_if_false=False):
                logger.warn("Enclosure count is 1 , Highly Available is seen as option in redundancy dropdown!!")
                error_flag += 1
                error_msg_list.append("Enclosure count is 1 , Highly Available is seen as option in redundancy dropdown!!")
            CreateLogicalInterconnectGroups.click_cancel_button()
            CreateLogicalInterconnectGroups.wait_create_lig_dialog_disappear()
            continue

        TBirdCreateLogicalInterconnectGroups.select_redundancy(redundancy_ov)
        TBirdCreateLogicalInterconnectGroups.click_select_interconnects()

        # for multiple LIG creation
        add_plus = False
        if n < total_len - 1:
            add_plus = True

        # choose interconnects for each enclosure in LIG
        TBirdCreateLogicalInterconnectGroups.select_logical_interconnect_group_section()
        for switch_bay in lig.switch:
            _create_tbird_lig_add_interconnect_to_lig(switch_bay)

        # configure internal networks
        internal_networks = getattr(lig, "internal_networks", "")
        if internal_networks != "":
            _create_lig_create_internal_networks(internal_networks)

        # create uplink sets
        if hasattr(lig, "lus"):
            total_lus = len(lig.lus)
            for i, uplink_set in enumerate(lig.lus):
                logger.info("Add uplink set {2} No: {0} --- Total: {1} {2}".format((i + 1), total_lus, '-' * 14))
                if lig.interconnecttype.lower() == FusionUIConst.CONST_CARBON.lower():
                    _create_tbird_carbon_lig_create_uplink_set(uplink_set, add_plus=(i < total_lus - 1))
                else:
                    _create_tbird_lig_create_uplink_set(uplink_set, add_plus=(i < total_lus - 1))

        # Interconnect Settings only for potash and hafnium not carbon
        if lig.interconnecttype.lower() == FusionUIConst.CONST_POTASH.lower() or lig.interconnecttype.lower() == FusionUIConst.CONST_HAFNIUM_POTASH.lower():
            igmpsnooping = getattr(lig, "igmpsnooping", "false")
            igmpidletimeout = getattr(lig, "igmpidletimeout", "260")
            loopprotection = getattr(lig, "loopprotection", "true")
            _create_tbird_lig_config_interconnect_settings(igmpsnooping, igmpidletimeout, loopprotection)

        # SNMP
        if hasattr(lig, 'snmp'):
            _create_tbird_lig_config_snmp(lig.snmp)

        if add_plus is True:
            TBirdCreateLogicalInterconnectGroups.click_create_plus_button()
        else:
            TBirdCreateLogicalInterconnectGroups.click_create_button()

        errors_on_form = TBirdCreateLogicalInterconnectGroups.get_all_errors_on_create_dialog()
        error_status, error_msg = FusionUIBase.get_error_message_from_dialog()

        if errors_on_form or error_status:
            error_flag += 1
            if errors_on_form:
                error_msg_list += errors_on_form
                logger.warn("Error Seen on form during LIG '{}' creation -\n{}".format(lig.name, errors_on_form))
            if error_status:
                logger.warn("Error for LIG {} - \n{}".format(lig.name, error_msg))
                error_msg_list.append(error_msg)
            CreateLogicalInterconnectGroups.click_cancel_button()
            CreateLogicalInterconnectGroups.wait_create_lig_dialog_disappear()
            continue

        # add to creation list for verification
        create_lig_list.append(lig)

        TBirdVerifyLogicalInterconnectGroups.verify_lig_exist(lig.name, timeout=15)
        count += 1

    if CreateLogicalInterconnectGroups.wait_create_lig_dialog_disappear(fail_if_false=False) is False:
        CreateLogicalInterconnectGroups.click_cancel_button()
        CreateLogicalInterconnectGroups.wait_create_lig_dialog_disappear()

    # basic verification
    for n, lig in enumerate(create_lig_list):
        FusionUIBase.show_activity_sidebar()
        CommonOperationLogicalInterconnectGroups.wait_activity_action_ok(lig.name, 'Create')
        FusionUIBase.show_activity_sidebar()
        logger.info("Added LIG {0} successfully".format(lig.name))

    if error_flag > 0:
        logger.warn("Errors Seen during LIG creation.")
        return False

    if count == 0:
        logger.warn("No LIGs added!")
        logger.warn("Return Value = False")
        return False

    if count != total_len:
        logger.warn("Not able to create all LIGs!")
        logger.warn("Return Value = False")
        return False

    logger.debug("Return Value = True")
    return True


def _create_tbird_carbon_lig_create_uplink_set(uplink_set, add_plus=False):
    """
    :param uplink_set:
    :param add_plus: True to hit Add button at last otherwise hit Add plus button
    """
    port_list = [item.strip() for item in uplink_set.ports.split(',')]
    if port_list:
        uplink_set_name = uplink_set.name
        uplink_set_type = uplink_set.networkType
        network = uplink_set.networks

    logger.info("create uplink set [ %s ]" % uplink_set_name)
    if uplink_set_type == "Fibre Channel":
        if TBirdCreateLogicalInterconnectGroups.wait_create_uplink_set_dialog_shown(fail_if_false=False) is False:
            TBirdCreateLogicalInterconnectGroups.click_add_uplink_set()
            TBirdCreateLogicalInterconnectGroups.wait_create_uplink_set_dialog_shown()
        TBirdCreateLogicalInterconnectGroups.input_create_uplink_set_name(uplink_set_name)

        if network != "":
            TBirdCreateLogicalInterconnectGroups.select_create_uplink_set_fc_network(network)
        else:
            ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")
    # - ports
        TBirdCreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports()
        TBirdCreateLogicalInterconnectGroups.wait_create_uplink_set_add_uplink_ports_to_dialog_shown()
        for i, port_tag in enumerate(port_list):
            enclosure_no, bay_no, port_name, port_speed = TBirdCreateLogicalInterconnectGroups.get_port_info(port_tag)
            TBirdCreateLogicalInterconnectGroups.select_uplink_set_add_uplink_ports_to_table_row_carbon(bay_no, port_name)
            if i == len(port_list) - 1:
                TBirdCreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_add()
            else:
                TBirdCreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_add_plus()

        for i, port_tag in enumerate(port_list):
            enclosure_no, bay_no, port_name, port_speed = TBirdCreateLogicalInterconnectGroups.get_port_info(port_tag)
            TBirdCreateLogicalInterconnectGroups.select_create_uplink_set_fc_port_speed(bay_no, port_name, port_speed)

    else:
        ui_lib.fail_test("Not support creating uplink set type '%s'" % uplink_set_type)

    # hit add button
    if add_plus is False:  # add
        CreateLogicalInterconnectGroups.click_create_uplink_set_add()
        CreateLogicalInterconnectGroups.wait_create_uplink_set_dialog_disappear()
    else:  # add plus
        CreateLogicalInterconnectGroups.click_create_uplink_set_add_plus()


def _create_lig_create_internal_networks(networks):
    network_list = [item.strip() for item in networks.split(',')]

    if len(network_list) == 0:
        return

    logger.info("configure internal networks")
    CreateLogicalInterconnectGroups.select_general_section()
    CreateLogicalInterconnectGroups.click_edit_internal_networks_gear()
    CreateLogicalInterconnectGroups.wait_edit_internal_networks_dialog_shown()
    CreateLogicalInterconnectGroups.click_edit_internal_networks_add_networks()
    CreateLogicalInterconnectGroups.wait_edit_internal_networks_add_networks_dialog_shown()

    network_len = len(network_list)
    for i, network in enumerate(network_list):
        CreateLogicalInterconnectGroups.input_edit_internal_networks_add_networks_search_network(network)
        CreateLogicalInterconnectGroups.wait_edit_internal_networks_add_networks_table_row_shown(network)
        if i < network_len - 1:
            CreateLogicalInterconnectGroups.click_edit_internal_networks_add_networks_add_plus()
        else:
            CreateLogicalInterconnectGroups.click_edit_internal_networks_add_networks_add()
            CreateLogicalInterconnectGroups.wait_edit_internal_networks_add_networks_dialog_disappear()

    # verify if present in table list
    for i, network in enumerate(network_list):
        CreateLogicalInterconnectGroups.wait_edit_internal_networks_table_row_shown(network)

    CreateLogicalInterconnectGroups.click_edit_internal_networks_ok()
    CreateLogicalInterconnectGroups.wait_edit_internal_networks_dialog_disappear()


def _create_lig_add_interconnect_to_lig(switch):
    logging.info("Adding interconnect - bay: %s, type: %s " % (switch.bay, switch.type))
    C7000CreateLogicalInterconnectGroups.select_bay_type(switch.bay, switch.type)
    logging.info("Added interconnect at switch bay: %s, type: %s " % (switch.bay, switch.type))


def _create_tbird_lig_add_interconnect_to_lig(switch):
    logging.info("Adding interconnect - enclosure: %s bay: %s, type: %s " % (switch.enclosure, switch.bay, switch.type))
    # For Carbon, the element used to identify module in LIG is different than other modules, hence including the
    # check mechanism to identify Carbon and do accordigly
    if switch.type.lower() == FusionUIConst.CONST_CARBON.lower():
        TBirdCreateLogicalInterconnectGroups.select_bay_type_fc(switch.enclosure, switch.bay, switch.type)
    else:
        TBirdCreateLogicalInterconnectGroups.select_bay_type(switch.enclosure, switch.bay, switch.type)
    logging.info("Added interconnect - enclosure: %s bay: %s, type: %s " % (switch.enclosure, switch.bay, switch.type))


def _create_lig_create_uplink_set(uplink_set, add_plus=False):
    """

    :param uplink_set:
    :param add_plus: True to hit Add button at last otherwise hit Add plus button
    """
    uplink_set_name = uplink_set.name
    uplink_set_type = uplink_set.networkType

    logger.info("create uplink set [ %s ]" % uplink_set_name)

    # choose connection mode, LACP timer for ethernet, tunnel, untagged
    if uplink_set_type == "Ethernet":
        __create_lig_add_ethernet_uplink_set(uplink_set)
    elif uplink_set_type == "Tunnel":
        __create_lig_add_tunnel_uplink_set(uplink_set)
    elif uplink_set_type == "Untagged":
        __create_lig_add_untagged_uplink_set(uplink_set)
    elif uplink_set_type == "Fibre Channel":
        __create_lig_add_fc_uplink_set(uplink_set)
    else:
        ui_lib.fail_test("Not support creating uplink set type '%s'" % uplink_set_type)

    # TODO: simple verify selected networks & uplink ports

    # hit add button
    if add_plus is False:  # add
        C7000CreateLogicalInterconnectGroups.click_create_uplink_set_add()
        C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_dialog_disappear()
    else:  # add plus
        C7000CreateLogicalInterconnectGroups.click_create_uplink_set_add_plus()


def _create_tbird_lig_create_uplink_set(uplink_set, add_plus=False):
    """

    :param uplink_set:
    :param add_plus: True to hit Add button at last otherwise hit Add plus button
    """
    uplink_set_name = uplink_set.name
    uplink_set_type = uplink_set.networkType

    logger.info("create uplink set [ %s ]" % uplink_set_name)

    # choose connection mode, LACP timer for ethernet, tunnel, untagged
    if uplink_set_type == "Ethernet":
        __create_tbird_lig_add_ethernet_uplink_set(uplink_set)
    elif uplink_set_type == "Tunnel":
        __create_tbird_lig_add_tunnel_uplink_set(uplink_set)
    elif uplink_set_type == "Untagged":
        __create_tbird_lig_add_untagged_uplink_set(uplink_set)
    elif uplink_set_type == "Fibre Channel":
        __create_tbird_lig_add_fc_uplink_set(uplink_set)
    else:
        ui_lib.fail_test("Not support creating uplink set type '%s'" % uplink_set_type)

    # TODO: simple verify selected networks & uplink ports

    # hit add button
    if add_plus is False:  # add
        CreateLogicalInterconnectGroups.click_create_uplink_set_add()
        CreateLogicalInterconnectGroups.wait_create_uplink_set_dialog_disappear()
    else:   # add plus
        CreateLogicalInterconnectGroups.click_create_uplink_set_add_plus()


def __create_lig_open_dialog_and_set_uplink_set_name_and_type(uplink_set):
    uplink_set_name = uplink_set.name
    uplink_set_type = uplink_set.networkType
    if C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_dialog_shown(fail_if_false=False) is False:
        C7000CreateLogicalInterconnectGroups.click_add_uplink_set()
    C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_dialog_shown()
    C7000CreateLogicalInterconnectGroups.input_create_uplink_set_name(uplink_set_name)
    # Skip selecting Uplinkset type for Fabric Extender Interconnect Module,because it supports only Ethernet & it is auto selected.
    if (uplink_set_type.lower() == 'ethernet') and (uplink_set.connectionMode.lower() == "da_auto"):
        logger.info("Fabric Extender module has default network type as [ETHERNET]")
    else:
        C7000CreateLogicalInterconnectGroups.select_create_uplink_set_type(uplink_set_type)


def __create_tbird_lig_open_dialog_and_set_uplink_set_name_and_type(uplink_set):
    uplink_set_name = uplink_set.name
    uplink_set_type = uplink_set.networkType
    if TBirdCreateLogicalInterconnectGroups.wait_create_uplink_set_dialog_shown(fail_if_false=False) is False:
        TBirdCreateLogicalInterconnectGroups.click_add_uplink_set()
    TBirdCreateLogicalInterconnectGroups.wait_create_uplink_set_dialog_shown()
    TBirdCreateLogicalInterconnectGroups.input_create_uplink_set_name(uplink_set_name)
    TBirdCreateLogicalInterconnectGroups.select_create_uplink_set_type(uplink_set_type)


def __create_lig_set_connection_mode_and_lacp(uplink_set):
    # choose connection mode, LACP timer for ethernet, tunnel, untagged
    # - connection mode
    connection_mode = uplink_set.connectionMode.lower()
    if connection_mode == "auto":
        uplink_set_lacp_timer = uplink_set.lacptimer
        C7000CreateLogicalInterconnectGroups.tick_create_uplink_set_connection_mode_automatic()
        if uplink_set_lacp_timer != "":
            C7000CreateLogicalInterconnectGroups.select_create_uplink_set_lacp_timer(uplink_set_lacp_timer)
    elif connection_mode == "failover":
        C7000CreateLogicalInterconnectGroups.tick_create_uplink_set_connection_mode_failover()
    elif connection_mode == "da_auto":
        return True
    else:
        ui_lib.fail_test(
            "Unexpected ethernet connection mode '%s' of uplink set '%s'" % (connection_mode, uplink_set.name))


def __create_tbird_lig_set_connection_mode_and_lacp(uplink_set):
    # choose connection mode, LACP timer for ethernet, tunnel, untagged
    # - connection mode
    """
    connection_mode = uplink_set.connectionMode.lower()
    if connection_mode == "auto":
        uplink_set_lacp_timer = uplink_set.lacptimer.lower()
        TbirdCreateLogicalInterconnectGroups.tick_create_uplink_set_connection_mode_automatic()
        if uplink_set_lacp_timer != "":
            TbirdCreateLogicalInterconnectGroups.select_create_uplink_set_lacp_timer(uplink_set_lacp_timer)
    elif connection_mode == "failover":
        TbirdCreateLogicalInterconnectGroups.tick_create_uplink_set_connection_mode_failover()
    else:
        ui_lib.fail_test(
            "Unexpected ethernet connection mode '%s' of uplink set '%s'" % (connection_mode, uplink_set.name))
    """
    uplink_set_lacp_timer = uplink_set.lacptimer
    FusionUIBase.para_should_be_in_list(['Short (1s)', 'Long (30s)'], uplink_set_lacp_timer)
    TBirdCreateLogicalInterconnectGroups.select_create_uplink_set_lacp_timer(uplink_set_lacp_timer)


def __create_lig_add_uplink_set_fc_network(uplink_set):
    port_list = [item.strip() for item in uplink_set.ports.split(',')]
    if port_list:
        C7000CreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports()
        C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_add_uplink_ports_to_dialog_shown()
        for i, port_tag in enumerate(port_list):
            bay_no, port_name, port_speed = port_tag.split(':')
            bay_no = bay_no.lower().replace('bay', '')
            C7000CreateLogicalInterconnectGroups.input_create_uplink_set_add_uplink_ports_to_search_port(port_name)
            C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_add_uplink_ports_to_table_row_shown(bay_no, port_name)
            C7000CreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_table_row(bay_no, port_name)
            if i == len(port_list) - 1:
                C7000CreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_add()
            else:
                C7000CreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_add_plus()
        C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_add_uplink_ports_to_dialog_disappear()
    else:
        ui_lib.fail_test("no [ ports ] attribute specified in data file when create uplink set > add uplink ports")

    # verify if present in table list
    for i, port_tag in enumerate(port_list):
        bay_no, port_name, port_speed = port_tag.split(':')
        bay_no = bay_no.lower().replace('bay', '')
        C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_port_table_row_shown(bay_no, port_name)


def __create_tbird_lig_add_uplink_set_fc_network(uplink_set):
    port_list = [item.strip() for item in uplink_set.ports.split(',')]
    if port_list:
        TBirdCreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports()
        TBirdCreateLogicalInterconnectGroups.wait_create_uplink_set_add_uplink_ports_to_dialog_shown()
        for i, port_tag in enumerate(port_list):
            # updated for extra : for the QX:X ports
            enclosure_no, bay_no, port_name, port_speed = TBirdCreateLogicalInterconnectGroups.get_port_info(port_tag)
            TBirdCreateLogicalInterconnectGroups.input_create_uplink_set_add_uplink_ports_to_search_port(port_name)
            TBirdCreateLogicalInterconnectGroups.wait_create_uplink_set_add_uplink_ports_to_table_row_shown(enclosure_no, bay_no, port_name)
            TBirdCreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_table_row(enclosure_no, bay_no, port_name)
            if i == len(port_list) - 1:
                TBirdCreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_add()
            else:
                TBirdCreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_add_plus()
        TBirdCreateLogicalInterconnectGroups.wait_create_uplink_set_add_uplink_ports_to_dialog_disappear()
    else:
        ui_lib.fail_test("no [ ports ] attribute specified in data file when create uplink set > add uplink ports")

    # verify if present in table list
    for i, port_tag in enumerate(port_list):
        # updated for extra : for the QX:X ports
        enclosure_no, bay_no, port_name, port_speed = TBirdCreateLogicalInterconnectGroups.get_port_info(port_tag)
        TBirdCreateLogicalInterconnectGroups.wait_create_uplink_set_port_table_row_shown(enclosure_no, bay_no, port_name)


def __create_lig_add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set):
    port_list = [item.strip() for item in uplink_set.ports.split(',')]
    if port_list:
        C7000CreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports()
        C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_add_uplink_ports_to_dialog_shown()
        for i, port_tag in enumerate(port_list):
            portsplit = port_tag.split(':')
            if len(portsplit) > 2:
                bay_no, port_name, port_speed = port_tag.split(':')
            else:
                bay_no, port_name = port_tag.split(':')
            bay_no = bay_no.lower().replace('bay', '')
            C7000CreateLogicalInterconnectGroups.input_create_uplink_set_add_uplink_ports_to_search_port(port_name)
            C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_add_uplink_ports_to_table_row_shown(bay_no, port_name)
            C7000CreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_table_row(bay_no, port_name)
            if i == len(port_list) - 1:
                C7000CreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_add()
            else:
                C7000CreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_add_plus()
        C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_add_uplink_ports_to_dialog_disappear()
    else:
        ui_lib.fail_test("no [ ports ] attribute specified in data file when create uplink set > add uplink ports")

    # verify if present in table list
    for i, port_tag in enumerate(port_list):
        portsplit = port_tag.split(':')
        if len(portsplit) > 2:
            bay_no, port_name, port_speed = port_tag.split(':')
        else:
            bay_no, port_name = port_tag.split(':')

        bay_no = bay_no.lower().replace('bay', '')
        C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_port_table_row_shown(bay_no, port_name)
        if len(portsplit) > 2:
            bay_no, port_name, port_speed = port_tag.split(':')
            bay_no = bay_no.lower().replace('bay', '')
            C7000CreateLogicalInterconnectGroups.select_uplink_set_ethernet_port_speed(bay_no, port_name, port_speed)
            Autoneg = C7000CreateLogicalInterconnectGroups.get_autonegotiation_text(bay_no, port_name)
            # to check autonegotioation statusS
            if port_speed == "Auto":
                if Autoneg != "Enabled":
                    ui_lib.fail_test("For Speed=Auto, Auto-negotiation is not Enabled")
                else:
                    logger.info("for speed Auto, Auto-negotiation is Enabled")
            if port_speed == "40 Gb/s":
                if Autoneg != "Disabled":
                    ui_lib.fail_test("For Speed=40Gb/s, Auto-Negotiation is not Disabled")
                else:
                    logger.info("for Speed=40Gb/s,Auto-Negotiation is Disabled")
    # click preferredport checkbox
    if uplink_set.connectionMode == "FAILOVER":
        pref_port_list = uplink_set.preferredPort.split('|')
        pref_bay_no = pref_port_list[0][-1:]
        C7000CreateLogicalInterconnectGroups.click_preferred_port(pref_bay_no, pref_port_list[1])


def __create_tbird_lig_add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set):
    port_list = [item.strip() for item in uplink_set.ports.split(',')]
    if port_list:
        TBirdCreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports()
        TBirdCreateLogicalInterconnectGroups.wait_create_uplink_set_add_uplink_ports_to_dialog_shown()
        for i, port_tag in enumerate(port_list):
            arr_port_tag = port_tag.split(':')
            enclousre_no = arr_port_tag[0]
            bay_no = arr_port_tag[1]
            port_name = arr_port_tag[2]
            if len(arr_port_tag) > 3:

                if (arr_port_tag[3] != "Auto" and arr_port_tag[3] != "40 Gb/s"):
                    port_name = port_name + ':' + arr_port_tag[3]
                else:
                    port_name = arr_port_tag[2]
                    port_speed = arr_port_tag[3]

            # enclousre_no, bay_no, port_name = port_tag.split(':')
            enclosure_no = enclousre_no.lower().replace('enc', '')
            bay_no = bay_no.lower().replace('bay', '')
            TBirdCreateLogicalInterconnectGroups.input_create_uplink_set_add_uplink_ports_to_search_port(port_name)
            TBirdCreateLogicalInterconnectGroups.wait_create_uplink_set_add_uplink_ports_to_table_row_shown(enclosure_no, bay_no, port_name)
            TBirdCreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_table_row(enclosure_no, bay_no, port_name)
            if i == len(port_list) - 1:
                TBirdCreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_add()
            else:
                TBirdCreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_add_plus()
        TBirdCreateLogicalInterconnectGroups.wait_create_uplink_set_add_uplink_ports_to_dialog_disappear()
    else:
        ui_lib.fail_test("no [ ports ] attribute specified in data file when create uplink set > add uplink ports")

    # verify if present in table list
    for i, port_tag in enumerate(port_list):
        arr_port_tag = port_tag.split(':')
        enclousre_no = arr_port_tag[0]
        bay_no = arr_port_tag[1]
        port_name = arr_port_tag[2]
        if len(arr_port_tag) > 3:
            if (arr_port_tag[3] != "Auto" and arr_port_tag[3] != "40 Gb/s"):
                port_name = port_name + ':' + arr_port_tag[3]
            else:
                port_name = arr_port_tag[2]
                port_speed = arr_port_tag[3]
        # enclousre_no, bay_no, port_name = port_tag.split(':')
        enclosure_no = enclousre_no.lower().replace('enc', '')
        bay_no = bay_no.lower().replace('bay', '')
        TBirdCreateLogicalInterconnectGroups.wait_create_uplink_set_port_table_row_shown(enclosure_no, bay_no, port_name)
        if len(arr_port_tag) > 3:
            if (arr_port_tag[3] == "Auto" or arr_port_tag[3] == "40 Gb/s"):
                port_speed = arr_port_tag[3]
                TBirdCreateLogicalInterconnectGroups.select_uplink_set_ethernet_port_speed(enclosure_no, bay_no, port_name, port_speed)
                logger.info("port speed chosen is '%s'" % port_speed)


def __create_lig_add_ethernet_uplink_set(uplink_set):
    __create_lig_open_dialog_and_set_uplink_set_name_and_type(uplink_set)
    __create_lig_set_connection_mode_and_lacp(uplink_set)

    # - networks
    network_list = [item.strip() for item in uplink_set.networks.split(',')]
    if network_list:
        C7000CreateLogicalInterconnectGroups.click_create_uplink_set_add_networks()
        C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_add_networks_to_dialog_shown()
        for i, network_name in enumerate(network_list):
            C7000CreateLogicalInterconnectGroups.input_create_uplink_set_add_networks_to_search_network(network_name)
            C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_add_networks_to_table_row_shown(network_name)
            if i == len(network_list) - 1:
                C7000CreateLogicalInterconnectGroups.click_create_uplink_set_add_networks_to_add()
            else:
                C7000CreateLogicalInterconnectGroups.click_create_uplink_set_add_networks_to_add_plus()
        C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_add_networks_to_dialog_disappear()
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")
    # - choose native network
    native_network = getattr(uplink_set, "native", "")
    if native_network != "":
        C7000CreateLogicalInterconnectGroups.tick_create_uplink_set_native_network(native_network)

    # verify if present in table list
    for network in network_list:
        C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_network_table_row_shown(network)

    # - ports
    __create_lig_add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set)


def __create_tbird_lig_add_ethernet_uplink_set(uplink_set):
    __create_tbird_lig_open_dialog_and_set_uplink_set_name_and_type(uplink_set)
    __create_tbird_lig_set_connection_mode_and_lacp(uplink_set)

    # - networks
    network_list = [item.strip() for item in uplink_set.networks.split(',')]
    if network_list:
        TBirdCreateLogicalInterconnectGroups.click_create_uplink_set_add_networks()
        TBirdCreateLogicalInterconnectGroups.wait_create_uplink_set_add_networks_to_dialog_shown()
        for i, network_name in enumerate(network_list):
            TBirdCreateLogicalInterconnectGroups.input_create_uplink_set_add_networks_to_search_network(network_name)
            TBirdCreateLogicalInterconnectGroups.wait_create_uplink_set_add_networks_to_table_row_shown(network_name)
            if i == len(network_list) - 1:
                TBirdCreateLogicalInterconnectGroups.click_create_uplink_set_add_networks_to_add()
            else:
                TBirdCreateLogicalInterconnectGroups.click_create_uplink_set_add_networks_to_add_plus()
        TBirdCreateLogicalInterconnectGroups.wait_create_uplink_set_add_networks_to_dialog_disappear()
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")
    # - choose native network
    native_network = getattr(uplink_set, "native", "")
    if native_network != "":
        TBirdCreateLogicalInterconnectGroups.tick_create_uplink_set_native_network(native_network)

    # verify if present in table list
    for network in network_list:
        TBirdCreateLogicalInterconnectGroups.wait_create_uplink_set_network_table_row_shown(network)

    # - ports
    __create_tbird_lig_add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set)


def __create_lig_add_tunnel_uplink_set(uplink_set):
    __create_lig_open_dialog_and_set_uplink_set_name_and_type(uplink_set)
    __create_lig_set_connection_mode_and_lacp(uplink_set)

    # - networks
    network = uplink_set.networks
    if network != "":
        C7000CreateLogicalInterconnectGroups.select_create_uplink_set_tunnel_network(network)
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")

    # - ports
    __create_lig_add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set)


def __create_tbird_lig_add_tunnel_uplink_set(uplink_set):
    __create_tbird_lig_open_dialog_and_set_uplink_set_name_and_type(uplink_set)
    __create_tbird_lig_set_connection_mode_and_lacp(uplink_set)

    # - networks
    network = uplink_set.networks
    if network != "":
        TBirdCreateLogicalInterconnectGroups.select_create_uplink_set_tunnel_network(network)
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")

    # - ports
    __create_tbird_lig_add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set)


def __create_lig_add_untagged_uplink_set(uplink_set):
    __create_lig_open_dialog_and_set_uplink_set_name_and_type(uplink_set)
    __create_lig_set_connection_mode_and_lacp(uplink_set)

    # - networks
    network = uplink_set.networks
    if network != "":
        C7000CreateLogicalInterconnectGroups.select_create_uplink_set_untagged_network(network)
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")

    # - ports
    __create_lig_add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set)


def __create_tbird_lig_add_untagged_uplink_set(uplink_set):
    __create_tbird_lig_open_dialog_and_set_uplink_set_name_and_type(uplink_set)
    __create_tbird_lig_set_connection_mode_and_lacp(uplink_set)

    # - networks
    network = uplink_set.networks
    if network != "":
        TBirdCreateLogicalInterconnectGroups.select_create_uplink_set_untagged_network(network)
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")

    # - ports
    __create_tbird_lig_add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set)


def __create_lig_add_fc_uplink_set(uplink_set):
    __create_lig_open_dialog_and_set_uplink_set_name_and_type(uplink_set)

    # - networks
    network = uplink_set.networks
    if network != "":
        C7000CreateLogicalInterconnectGroups.select_create_uplink_set_fc_network(network)
        # logger.warn("temporarily apply workaround for QXCR1001428378")
        # C7000CreateLogicalInterconnectGroups.select_create_uplink_set_fc_network_workaround(network)
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")
    # - ports
    port = uplink_set.ports
    # -- interconnect
    if port == "":
        ui_lib.fail_test("no [ ports ] attribute specified in data file when create uplink set > add networks")

    __create_lig_add_uplink_set_fc_network(uplink_set)
    # CreateLogicalInterconnectGroups.select_create_uplink_set_fc_interconnect(interconnect)
    # -- port & port speed
    port_list = [item.strip() for item in port.split(',')]
    for port_and_speed in port_list:
        bay_no, port_name, port_speed = port_and_speed.split(':')
        bay_no = bay_no.replace('bay', '')
        C7000CreateLogicalInterconnectGroups.select_create_uplink_set_fc_port_speed(bay_no, port_name, port_speed)


def __create_tbird_lig_add_fc_uplink_set(uplink_set):
    __create_tbird_lig_open_dialog_and_set_uplink_set_name_and_type(uplink_set)

    # - networks
    network = uplink_set.networks
    if network != "":
        TBirdCreateLogicalInterconnectGroups.select_create_uplink_set_fc_network(network)
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")
    # - ports
    port = uplink_set.ports
    # -- interconnect
    if port == "":
        ui_lib.fail_test("no [ ports ] attribute specified in data file when create uplink set > add networks")

    __create_tbird_lig_add_uplink_set_fc_network(uplink_set)
    # -- port & port speed
    port_list = [item.strip() for item in port.split(',')]
    for i, port_tag in enumerate(port_list):
        enclosure_no, bay_no, port_name, port_speed = TBirdCreateLogicalInterconnectGroups.get_port_info(port_tag)
        TBirdCreateLogicalInterconnectGroups.select_create_uplink_set_fc_port_speed(bay_no, port_name, port_speed)


def _create_lig_config_interconnect_settings(fast_mac_cache_failover,
                                             mac_refresh_interval,
                                             igmp_snooping,
                                             igmp_idle_timeout_interval,
                                             loop_protection,
                                             pause_flood_protection):
    logger.info("configure Interconnect Settings")

    C7000CreateLogicalInterconnectGroups.select_logical_interconnect_settings_section()

    if fast_mac_cache_failover.lower() == "true":
        C7000CreateLogicalInterconnectGroups.tick_interconnect_settings_fast_mac_cache_failover()
        C7000CreateLogicalInterconnectGroups.input_interconnect_settings_mac_refresh_interval(mac_refresh_interval)
    else:
        C7000CreateLogicalInterconnectGroups.untick_interconnect_settings_fast_mac_cache_failover()

    if igmp_snooping.lower() == "true":
        C7000CreateLogicalInterconnectGroups.tick_interconnect_settings_igmp_snooping()
        C7000CreateLogicalInterconnectGroups.input_interconnect_settings_igmp_idle_timeout_interval(igmp_idle_timeout_interval)
    else:
        C7000CreateLogicalInterconnectGroups.untick_interconnect_settings_igmp_snooping()

    if loop_protection.lower() == "true":
        C7000CreateLogicalInterconnectGroups.tick_interconnect_settings_loop_protection()
    else:
        C7000CreateLogicalInterconnectGroups.untick_interconnect_settings_loop_protection()

    if pause_flood_protection.lower() == "true":
        C7000CreateLogicalInterconnectGroups.tick_interconnect_settings_pause_flood_protection()
    else:
        C7000CreateLogicalInterconnectGroups.untick_interconnect_settings_pause_flood_protection()


def _create_tbird_lig_config_interconnect_settings(igmp_snooping,
                                                   igmp_idle_timeout_interval,
                                                   loop_protection):
    logger.info("configure Interconnect Settings")

    C7000CreateLogicalInterconnectGroups.select_logical_interconnect_settings_section()

    if igmp_snooping.lower() == "true":
        C7000CreateLogicalInterconnectGroups.tick_interconnect_settings_igmp_snooping()
        C7000CreateLogicalInterconnectGroups.input_interconnect_settings_igmp_idle_timeout_interval(igmp_idle_timeout_interval)
    else:
        C7000CreateLogicalInterconnectGroups.untick_interconnect_settings_igmp_snooping()

    if loop_protection.lower() == "true":
        C7000CreateLogicalInterconnectGroups.tick_interconnect_settings_loop_protection()
    else:
        C7000CreateLogicalInterconnectGroups.untick_interconnect_settings_loop_protection()


def __create_lig_add_trap_destination(snmp_obj):
    logger.info("- configure Trap Destination settings")
    td_list = snmp_obj.trapdestination
    td_len = len(td_list)
    CreateLogicalInterconnectGroups.click_add_trap_destination()
    CreateLogicalInterconnectGroups.wait_add_trap_destination_dialog_shown()
    for i, td_obj in enumerate(td_list):
        CreateLogicalInterconnectGroups.input_add_trap_destination_trap_destination(td_obj.trapdestination)
        CreateLogicalInterconnectGroups.input_add_trap_destination_community_string(td_obj.communitystring)
        if td_obj.trapformat.lower() == "snmpv1":
            CreateLogicalInterconnectGroups.tick_add_trap_destination_trap_format_snmpv1()
        elif td_obj.trapformat.lower() == "snmpv2":
            CreateLogicalInterconnectGroups.tick_add_trap_destination_trap_format_snmpv2()
        else:
            ui_lib.fail_test("unexpected trapformation attribute '%s'" % td_obj.trapformat)
        # TODO: implement detail configuration for severity, VCM traps etc

        if i < td_len - 1:
            CreateLogicalInterconnectGroups.click_add_trap_destination_add_plus()
        else:
            CreateLogicalInterconnectGroups.click_add_trap_destination_add()
            CreateLogicalInterconnectGroups.wait_add_trap_destination_dialog_disappear()
        time.sleep(2)


def __create_lig_add_snmpaccess(snmp_obj):
    logger.info("- configure SNMP access settings")
    sa_list = snmp_obj.snmpaccess
    sa_len = len(sa_list)
    CreateLogicalInterconnectGroups.click_add_snmp_access()
    CreateLogicalInterconnectGroups.wait_add_snmp_access_dialog_shown()
    for i, td_obj in enumerate(sa_list):
        CreateLogicalInterconnectGroups.input_add_snmp_access_ip_or_subnet(td_obj.iporsubnet)

        if i < sa_len - 1:
            CreateLogicalInterconnectGroups.click_add_snmp_access_add_plus()
        else:
            CreateLogicalInterconnectGroups.click_add_snmp_access_add()
            CreateLogicalInterconnectGroups.wait_add_snmp_access_dialog_disappear()
        time.sleep(2)


def _create_lig_config_snmp(snmp_obj):
    snmp_obj = snmp_obj if isinstance(snmp_obj, DataObj) else snmp_obj[0]
    logger.info("configure LIG snmp settings")

    C7000CreateLogicalInterconnectGroups.select_logical_snmp_section()
    if hasattr(snmp_obj, "snmpenabled"):
        if snmp_obj.snmpenabled.lower() == 'enabled':
            C7000CreateLogicalInterconnectGroups.toggle_snmp_enabled()
        elif snmp_obj.snmpenabled.lower() == 'Disabled':
            C7000CreateLogicalInterconnectGroups.toggle_snmp_disabled()
        else:
            ui_lib.fail_test("unexpected snmpenabled attribute '%s'" % snmp_obj.snmpenabled)

    # The below 2 variants (snmpv1v2enabled and snmpv3enabled ) are only applicable in feature toggle OVF293
    elif hasattr(snmp_obj, "snmpv1v2enabled"):
        if snmp_obj.snmpv1v2enabled.lower() == 'enabled':
            C7000CreateLogicalInterconnectGroups.toggle_snmpv1v2_enabled()
        elif snmp_obj.snmpv1v2enabled.lower() == 'Disabled':
            C7000CreateLogicalInterconnectGroups.toggle_snmpv1v2_disabled()

    elif hasattr(snmp_obj, "snmpv3enabled"):
        if snmp_obj.snmpv3enabled == 'enabled':
            C7000CreateLogicalInterconnectGroups.toggle_snmpv3_enabled()
            if hasattr(snmp_obj, 'adduser'):
                _add_snmp_v3_user(snmp_obj)

        elif snmp_obj.snmpv3enabled == 'disabled':
            C7000CreateLogicalInterconnectGroups.toggle_snmpv3_disabled()

    C7000CreateLogicalInterconnectGroups.input_snmp_system_contact(snmp_obj.syscontact)
    C7000CreateLogicalInterconnectGroups.input_snmp_read_community(snmp_obj.readcommunity)

    # - Trap Destinations
    if hasattr(snmp_obj, "trapdestination"):
        __create_lig_add_trap_destination(snmp_obj)
    # The below  variant (add_snmpv3_trapdestination)is only applicable in feature toggle OVF293
    if hasattr(snmp_obj, "add_snmpv3_trapdestination"):
        __create_lig_add_snmpv3_trap_destination(snmp_obj)
    #  - SNMP Access
    if hasattr(snmp_obj, "snmpaccess"):
        __create_lig_add_snmpaccess(snmp_obj)


def _create_tbird_lig_config_snmp(snmp_obj):
    snmp_obj = snmp_obj if isinstance(snmp_obj, DataObj) else snmp_obj[0]
    logger.info("configure LIG snmp settings")

    TBirdCreateLogicalInterconnectGroups.select_logical_snmp_section()

    C7000CreateLogicalInterconnectGroups.input_snmp_system_contact(snmp_obj.syscontact)
    C7000CreateLogicalInterconnectGroups.input_snmp_read_community(snmp_obj.readcommunity)

    # - Trap Destinations
    if hasattr(snmp_obj, "trapdestination"):
        __create_lig_add_trap_destination(snmp_obj)

    # The below variant is aplicable for feature toggle in OVF292
    if hasattr(snmp_obj, "snmpv1v2enabled"):
        if snmp_obj.snmpv1v2enabled.lower() == 'enabled':
            C7000CreateLogicalInterconnectGroups.toggle_snmpv1v2_enabled()
        elif snmp_obj.snmpv1v2enabled.lower() == 'disabled':
            C7000CreateLogicalInterconnectGroups.toggle_snmpv1v2_disabled()

    elif hasattr(snmp_obj, "snmpv3enabled"):
        TBirdVerifyLogicalInterconnectGroups.verify_tbird_snmpv3_enabled(snmp_obj.snmpv3enabled)
    if hasattr(snmp_obj, 'adduser'):
        _add_snmp_v3_user(snmp_obj)
    # - Trap Destinations
    if hasattr(snmp_obj, "trapdestination"):
        __create_lig_add_trap_destination(snmp_obj)

    # The below  variant (add_snmpv3_trapdestination)is only applicable in feature toggle OVF292
    if hasattr(snmp_obj, "add_snmpv3_trapdestination"):
        __create_lig_add_snmpv3_trap_destination(snmp_obj)


def _create_lig_config_qos(qos_configuration_type):
    logger.info("configure Quality of Service (QoS)")
    C7000CreateLogicalInterconnectGroups.select_quality_of_service_section()
    C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(qos_configuration_type)
    # TODO: implement qos detail configuration if choose "Custom (with FCoE lossless)", "Custom (without FCoE lossless)"
# end - create LIG


# begin - edit LIG
def edit_logical_interconnect_group(lig_obj):
    """ Edit logical interconnect group for C7000 and Tbird
    C7000
    Arguments:
      <lig>
          name*                     --  Name of logical interconnect group as a string.
          new_name                  --  (Optional) The name of new logical interconnect group
          fastmaccachefailover      --  (Optional) Whether to enable 'Fast MAC cache failover'. Possible value: true|false.
          macrefreshinterval        --  (Optional) MAC refresh interval as integer. This setting will not take effect if fastmaccachefailover is set to false
          igmpsnooping              --  (Optional) Whether to enable 'IGMP Snooping'. Possible value: true|false.
          igmpidletimeout           --  (Optional) IGMP idle timeout interval as integer. This setting will not take effect if igmpsnooping is set to false
          loopprotection            --  (Optional) Whether to enable 'Loop protection'. Possible value: true|false.
          pausefloodprotection      --  (Optional) Whether to enable 'Pause flood protection'. Possible value: true|false.
          qos_configuration_type    --  (Optional) Possible value: Passthrough/Custom (with FCoE lossless)|Custom (without FCoE lossless)
          internal_networks         --  (Optional) Configure internal networks, can be empty which indicate remove all existing internal networks settings
          <switch> (Optional) for specifying interconnect model. If this node present, it will restore all interconnect bays type 'None' at first before configuring bay type according to test data here.
            bay*                    --  Interconnect bay no as integer. e.g. 1
            type*                   --  Interconnect bay model as string. Need to grap from create lig page. e.g. HP VC FlexFabric-20/40 F8 Module|HP VC FlexFabric-20/40 F8 Module
          <remove_lus> (Optional) Remove uplink set
            name*                   --  Name of uplink set to be removed
          <add_lus> optional, for adding new uplink set
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
            <snmp> Optional, for configuring snmp related settings. if not present, use default snmp settings
              snmpenabled           --  (Optional) Whether to enable snmp settings, possible value: ENABLED|DISABLED
              syscontact            --  (Optional) SNMP System contact as string value.
              readcommunity         --  (Optional) SNMP Read community as string value.
              <remove_trapdestination> (Optional) Remove snmp trap destination config item
                trapdestination*    --  Which snmp trapdestination to be removed
              <add_trapdestination> (Optional) For adding snmp trapdestination
                trapdestination*    --  Trap destination. e.g. 192.168.1.2
                communitystring*    --  Community string as string value.
                trapformat*         --  Trap Format. Possible value: SNMPv1|SNMPv2
              <remove_snmpaccess> (Optional) Remove snmp access config item
                iporsubnet*         -- snmp 'ip or subnet'. e.g. 192.168.1.0/24
              <add_snmpaccess> (Optional) For configuring snmp access. Accpet multiple nodes.
                iporsubnet*         --  IP or subnet for SNMP Access. e.g. 192.168.1.0/24

    * Required Arguments
    - Note that this function always perform remove lus then add lus operation even though the sequence of <remove_lus> and <add_lus> in test data is reversal.

    Example:
        data/ligs -> @{TestData.editligs}
        <editligs>
            <lig name="LIG-wpst32"
                 new_name="LIG-wpst32-updated"
                 fastmaccachefailover="FALSE"
                 macrefreshinterval="5"
                 igmpsnooping="TRUE"
                 igmpidletimeout="280"
                 loopprotection="TRUE"
                 pausefloodprotection="TRUE"
                 qos_configuration_type="Passthrough"
                 internal_networks="dev101-management, dev103-ft-a">
                <!--if reconfigure interconnect bay type, all port will be removed from each uplink set-->
                <switch bay="1" type="HP VC FlexFabric-20/40 F8 Module" />
                <switch bay="2" type="HP VC FlexFabric-20/40 F8 Module" />
                <switch bay="3" type="HP VC FlexFabric-20/40 F8 Module" />
                <switch bay="4" type="HP VC FlexFabric-20/40 F8 Module" />
                <switch bay="5" type="None" />
                <switch bay="6" type="None" />
                <remove_lus name="FA-path3" />
                <remove_lus name="FA-path4" />
                <remove_lus name="FA-path1" />
                <remove_lus name="FA-path2" />
                <remove_lus name="DA-path1" />
                <remove_lus name="DA-path2" />
                <remove_lus name="Pub-net" />
                <remove_lus name="FO-net" />
                <remove_lus name="PXE-net" />
                <add_lus connectionMode="AUTO" lacptimer="" name="FA-path3-updated" native="" networkType="Fibre Channel" networks="FA3" ports="bay3|X3|Auto" preferredPort="" />
                <add_lus connectionMode="AUTO" lacptimer="Long (30s)" name="PXE-net-updated" native="dev300-pxeboot" networkType="Ethernet" networks="dev300-pxeboot" ports="bay2|Q2.1" preferredPort="" />
                <snmp snmpenabled="ENABLED" syscontact="Robert" readcommunity="private">
                    <remove_trapdestination trapdestination="10.0.0.12"/>
                    <remove_trapdestination trapdestination="172.2.1.3"/>
                    <add_trapdestination trapdestination="192.168.99.99" communitystring="public1" trapformat="SNMPv2"/>

                    <remove_snmpaccess iporsubnet="192.168.1.0/24" />
                    <add_snmpaccess iporsubnet="10.0.2.0/24"/>
                </snmp>
            </lig>
        </editligs>

    --------------------------------------------------------------------------------------
    Tbird
    Example:
        data/ligs -> @{TestData.editligs}

        <editligs>
            <lig name="LIG_POTASH_bak"
                 new_name="LIG_POTASH_test"
                 igmpsnooping="TRUE"
                 igmpidletimeout="280"
                 loopprotection="TRUE"
                 lldp_tagging="TRUE"
                 qos_configuration_type="Passthrough"
                 internal_networks="dev101-management, dev103-ft-a">
                <!--if reconfigure interconnect bay type, all port will be removed from each uplink set-->
                <switch enclosure="1" bay="3" type="Virtual Connect SE 40Gb F8 Module for Synergy" />
                <switch enclosure="1" bay="6" type="Synergy 20Gb Interconnect Link Module" />
                <switch enclosure="2" bay="3" type="Synergy 20Gb Interconnect Link Module" />
                <switch enclosure="2" bay="6" type="Virtual Connect SE 40Gb F8 Module for Synergy" />
                <switch enclosure="3" bay="6" type="Synergy 20Gb Interconnect Link Module" />
                <switch enclosure="3" bay="3" type="Synergy 20Gb Interconnect Link Module" />
                <remove_lus name="FA-path1" />
                <remove_lus name="Pub-net" />
                <add_lus connectionMode="AUTO" lacptimer="Long (30s)" name="lus_eth" native="dev300-pxeboot" networkType="Ethernet" networks="dev300-pxeboot" ports="bay3|Q1:1" preferredPort="" />
                <add_lus connectionMode="AUTO" lacptimer="" name="lus_fc" native="" networkType="Fibre Channel" networks="FA3" ports="bay3|Q2:1|Auto" preferredPort="" />
                <snmp syscontact="SHQA" readcommunity="public">
                    <remove_trapdestination trapdestination="192.168.99.2"/>
                    <remove_trapdestination trapdestination="192.168.99.1"/>
                    <add_trapdestination trapdestination="192.168.99.98" communitystring="public1" trapformat="SNMPv1"/>
                    <add_trapdestination trapdestination="192.168.99.99" communitystring="public2" trapformat="SNMPv2"/>
                    <add_trapdestination trapdestination="192.168.99.100" communitystring="public2" trapformat="SNMPv2"/>
                </snmp>
            </lig>
        </editligs>
    """
    navigate()

    not_exists = 0
    total_len = len(lig_obj)
    ov_model_type = FusionUIBase.APIMethods().get_oneview_model_type()
    logger.debug("Editing {0} Logical Interconnect Groups...".format(ov_model_type))
    for n, lig in enumerate(lig_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total_len, '-' * 14))
        logger.info("Editing a LIG with name '{0}'".format(lig.name))
        if not VerifyLogicalInterconnectGroups.verify_lig_exist(lig.name, fail_if_false=False):
            logger.warn("LIG '{0}' not exists".format(lig.name))
            not_exists += 1
            continue

        # select LIG
        if select_logical_interconnect_group(lig.name) is False:
            not_exists += 1
            continue

        EditLogicalInterconnectGroups.select_actions_edit()
        EditLogicalInterconnectGroups.wait_edit_lig_dialog_shown()
        EditLogicalInterconnectGroups.select_general_section()
        if hasattr(lig, "new_name"):
            logger.info("Edit new name to {0}".format(lig.new_name))
            EditLogicalInterconnectGroups.input_name(lig.new_name)

        # Will call related method according to OneView model type
        if hasattr(lig, 'switch'):
            for switch_bay in lig.switch:
                if ov_model_type == "C7000":
                    _edit_lig_config_interconnect_bay_type(switch_bay)
                elif ov_model_type == "Synergy":
                    _edit_lig_config_interconnect_bay_type_tbird(switch_bay)
                else:
                    ui_lib.fail_test("Identified a unknown OneView model type {0}".format(ov_model_type))

        # keep internal network no change if attribute 'internal_networks' does not present
        if hasattr(lig, "internal_networks") is True:
            internal_networks = getattr(lig, "internal_networks")
            if internal_networks != "":
                # configure internal networks
                _edit_lig_add_internal_networks(internal_networks)
            else:
                # remove all internal networks if 'internal_networks' is empty string
                _edit_lig_clean_internal_networks()
        # TODO: Hard code to deal with remove, add uplink set one by one since TestData module load ligs' child nodes in disorder, can't process them according to user defined order in test data file
        # TODO: not support edit uplink set. Workaround is remove exist uplink set then add new uplink set
        # remove uplink sets (node: remove_lus)
        if hasattr(lig, "remove_lus"):
            for i, uplink_set in enumerate(lig.remove_lus):
                logger.info("Remove uplink set {2} No: {0} --- Total: {1} {2}".format((i + 1), len(lig.remove_lus),
                                                                                      '-' * 14))
                _edit_lig_remove_uplink_set(uplink_set)
        # add uplink sets (node: add_lus)
        if hasattr(lig, "add_lus"):
            total_lus = len(lig.add_lus)
            for i, uplink_set in enumerate(lig.add_lus):
                logger.info("Add uplink set {2} No: {0} --- Total: {1} {2}".format((i + 1), total_lus, '-' * 14))
                if i < total_lus - 1:
                    _edit_lig_create_uplink_set(uplink_set, add_plus=True)
                else:
                    _edit_lig_create_uplink_set(uplink_set)

        if getattr(lig, 'InterconnectType', '').lower() != 'fabric extender':
            # Interconnect Settings
            _edit_lig_config_interconnect_settings(getattr(lig, 'fastmaccachefailover', None),
                                                   getattr(lig, 'macrefreshinterval', None),
                                                   getattr(lig, 'igmpsnooping', None),
                                                   getattr(lig, 'igmpidletimeout', None),
                                                   getattr(lig, 'loopprotection', None),
                                                   getattr(lig, 'pausefloodprotection', None),
                                                   getattr(lig, 'lldptagging', None),
                                                   getattr(lig, 'lldpenhancedtlv', None))
        # SNMP
        if hasattr(lig, 'snmp'):
            if ov_model_type == "C7000":
                _edit_lig_config_snmp(lig.snmp)
            elif ov_model_type == "Synergy":
                _edit_lig_config_snmp_tbird(lig.snmp)

        # Quality of Service (QoS)
        if hasattr(lig, "qos_configuration_type"):
            _edit_lig_config_qos(lig.qos_configuration_type)

        EditLogicalInterconnectGroups.click_ok_button()
        # wait operation done
        EditLogicalInterconnectGroups.wait_status_changing_shown()
        EditLogicalInterconnectGroups.wait_status_changing_disappear(timeout=60)
        if EditLogicalInterconnectGroups.wait_edit_lig_dialog_disappear(fail_if_false=False) is False:
            # may encounter errors, get message
            msg = FusionUIBase.get_warning_message_from_dialog()
            logger.warn("Failed to edit LIG '%s'. Got message:\n%s" % (lig.name, msg))
            ui_lib.fail_test(msg)

        # TODO: simple verification
        # verify if exist in table list
        if hasattr(lig, "new_name"):
            VerifyLogicalInterconnectGroups.verify_lig_exist(lig.new_name, timeout=15)
        # check LIG activity
        FusionUIBase.show_activity_sidebar()
        if hasattr(lig, "new_name"):
            CommonOperationLogicalInterconnectGroups.wait_activity_action_ok(lig.new_name, 'Update')
        else:
            CommonOperationLogicalInterconnectGroups.wait_activity_action_ok(lig.name, 'Update')
        FusionUIBase.show_activity_sidebar()
        logger.info("Edit LIG {0} successfully".format(lig.name))

    return True if not not_exists else False


def validate_warning_message_when_edit_logical_interconnect_group(lig_obj):
    '''
    Function to validate warning message when edit LIG.
    If target LIG is using by EG and LE, a warning message will be shown when edit LIG.
    No warning messge will return True

    Examples:
        data/ligs -> @{TestData.editligs}

        <editligs>
            <lig name="ICM1-4" />
        </editligs>

    ${InconsistencyWarningMsgSummary}       Warning: One or more logical interconnects are using this logical interconnect group.
    ${InconsistencyWarningMsgDetailsPart1}  \n[u'Modifying this logical interconnect group will cause logical interconnect
    ${InconsistencyWarningMsgDetailsPart2}  to become inconsistent.']
    ${expectedWarningMessage}=  catenate  SEPARATOR=  ${InconsistencyWarningMsgSummary}   ${InconsistencyWarningMsgDetailsPart1}
    ${expectedWarningMessage}=  catenate  ${expectedWarningMessage}    ${TestData.LOIGp0003.li}    ${InconsistencyWarningMsgDetailsPart2}
    Run Keyword and Expect Error  ${expectedWarningMessage}  Fusion Ui Validate Warning Message When Edit Logical Interconnect Group  @{TestData.editligs}

    '''
    navigate()

    total_len = len(lig_obj)
    logger.debug("Editing Logical Interconnect Groups for Tbird...")

    for n, lig in enumerate(lig_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total_len, '-' * 14))
        logger.info("Editing a LIG with name '{0}'".format(lig.name))

        TBirdVerifyLogicalInterconnectGroups.verify_lig_exist(lig.name)

        CommonOperationLogicalInterconnectGroups.click_lig(lig.name)
        CommonOperationLogicalInterconnectGroups.wait_lig_selected(lig.name)

        EditLogicalInterconnectGroups.select_actions_edit()
        EditLogicalInterconnectGroups.wait_edit_lig_dialog_shown()

        if TBirdVerifyLogicalInterconnectGroups.verify_warning_message_shown(fail_if_false=False):
            TBirdEditLogicalInterconnectGroups.click_warning_message_details()
            status, msg = FusionUIBase.get_info_message_from_dialog()
            if status is True:
                logger.warn("Got info message when edit LIG")
                ui_lib.fail_test(msg)

        EditLogicalInterconnectGroups.click_cancel_button()
        EditLogicalInterconnectGroups.wait_edit_lig_dialog_disappear()

    return True


# begin - edit Natasha LIG
def edit_natasha_logical_interconnect_group(lig_obj):
    """ Create Ethernet Network


    Arguments:
          <lig>
          name                     --  Name of Natasha logical interconnect group as a string.
          interconnecttype          --   Interconnect Type of the Lig
        <switch> required, for specifying interconnect model
            enclosure               --  Enclosure the Interconnect belongs to
            bay                    --  Interconnect bay no as integer. e.g. 1
            type                   --  Interconnect bay model as string. Need to grap from create lig page. e.g. Synergy 12Gb SAS Connection Module
    Example:
        data/natasha_ligs -> @{TestData.natasha_ligs}
        <natasha_ligs>
            <natasha_lig name="LIG_OVAEncICM" utilizationSampling='enable' intervalSamples='300', totalSamples='12'>
                 interconnecttype = "Synergy 12Gb SAS Connection Module"
                <switch enclosure="1" bay="1" type="Synergy 12Gb SAS Connection Module"/>
                <switch enclosure="1" bay="4" type="Synergy 12Gb SAS Connection Module" />
            </natasha_lig>
        </natasha_ligs>
    """
    navigate()

    logger.debug("Editing Natasha Logical Interconnect Groups...")

    count = 0
    total_len = len(lig_obj)
    for n, lig in enumerate(lig_obj):
        # check if LIG is existing
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total_len, '-' * 14))
        logger.info("Editing a Natasha LIG with name '{0}'".format(lig.name))
        if C7000VerifyLogicalInterconnectGroups.verify_lig_exist(lig.name, fail_if_false=False) is False:
            logger.warn("LIG '{0}' not exists".format(lig.name))
            continue

        # select LIG
        if select_logical_interconnect_group(lig.name) is False:
            continue

        TBirdEditLogicalInterconnectGroups.select_actions_edit_dfrm()
        C7000EditLogicalInterconnectGroups.wait_edit_lig_dialog_shown()
        C7000EditLogicalInterconnectGroups.select_general_section()
        if hasattr(lig, "new_name"):
            logger.info("Edit new name to %s" % lig.new_name)
            C7000EditLogicalInterconnectGroups.input_name(lig.new_name)

        # keep interconnect bays no change if no switch child node in lig node
        if hasattr(lig, 'switch'):
            for switch_bay in lig.switch:
                # configure interconnect bay type
                _edit_lig_config_interconnect_bay_type(switch_bay)

        # TODO: simple verification
        C7000EditLogicalInterconnectGroups.click_ok_button()
        # wait operation done
        C7000EditLogicalInterconnectGroups.wait_status_changing_shown()
        C7000EditLogicalInterconnectGroups.wait_status_changing_disappear()
        # verify if exist in table list
        if hasattr(lig, "new_name"):
            C7000VerifyLogicalInterconnectGroups.verify_lig_exist(lig.new_name, timeout=15)
        # check LIG activity
        FusionUIBase.show_activity_sidebar()
        if hasattr(lig, "new_name"):
            CommonOperationLogicalInterconnectGroups.wait_activity_action_ok(lig.new_name, 'Update')
        else:
            CommonOperationLogicalInterconnectGroups.wait_activity_action_ok(lig.name, 'Update')
        FusionUIBase.show_activity_sidebar()
        logger.info("Edit LIG {0} successfully".format(lig.name))
        count += 1

    if count == 0:
        logger.warn("No LIGs updated!")
        logger.warn("Return Value = False")
        return False

    if count != total_len:
        logger.warn("Not able to edit all LIGs!")
        logger.warn("Return Value = False")
        return False

    logger.debug("Return Value = True")
    return True


def _edit_lig_config_interconnect_bay_type(switch):
    logger.info("Configuring interconnect - bay: %s, type: %s " % (switch.bay, switch.type))
    C7000EditLogicalInterconnectGroups.select_bay_type(switch.bay, switch.type)
    logger.info("Configuring interconnect at switch bay: %s, type: %s " % (switch.bay, switch.type))


def _edit_lig_config_interconnect_bay_type_tbird(switch):
    logger.info("Configuring interconnect - bay: %s, type: %s " % (switch.bay, switch.type))
    # For Carbon, the element used to identify module in LIG is different than other modules, hence including the
    # check mechanism to identify Carbon and do accordigly
    if switch.type.lower() == FusionUIConst.CONST_CARBON.lower():
        TBirdEditLogicalInterconnectGroups.select_bay_type_fc(switch.bay, switch.type, encl_no=switch.enclosure)
    else:
        TBirdEditLogicalInterconnectGroups.select_bay_type(switch.bay, switch.type, encl_no=switch.enclosure)
    logger.info("Configuring interconnect at switch bay: %s, type: %s " % (switch.bay, switch.type))


def _edit_lig_clean_internal_networks():
    logger.info("Function call to remove all internal networks")
    EditLogicalInterconnectGroups.select_general_section()
    EditLogicalInterconnectGroups.click_edit_internal_networks_gear()
    EditLogicalInterconnectGroups.wait_edit_internal_networks_dialog_shown()
    EditLogicalInterconnectGroups.click_edit_internal_networks_remove_all()
    EditLogicalInterconnectGroups.click_edit_internal_networks_ok()
    EditLogicalInterconnectGroups.wait_edit_internal_networks_dialog_disappear()

    # TODO: verify if there is no networks in table list


def _edit_lig_add_internal_networks(networks):
    network_list = [item.strip() for item in networks.split(',')]

    if len(network_list) == 0:
        return

    logger.info("configure internal networks")
    EditLogicalInterconnectGroups.select_general_section()
    EditLogicalInterconnectGroups.click_edit_internal_networks_gear()
    EditLogicalInterconnectGroups.wait_edit_internal_networks_dialog_shown()
    if EditLogicalInterconnectGroups.wait_edit_internal_networks_table_header_shown("Name", fail_if_false=False):
        logger.info("remove all internal networks at first")
        EditLogicalInterconnectGroups.click_edit_internal_networks_remove_all()
    EditLogicalInterconnectGroups.click_edit_internal_networks_add_networks()
    EditLogicalInterconnectGroups.wait_edit_internal_networks_add_networks_dialog_shown()

    network_len = len(network_list)
    for i, network in enumerate(network_list):
        EditLogicalInterconnectGroups.input_edit_internal_networks_add_networks_search_network(network)
        EditLogicalInterconnectGroups.wait_edit_internal_networks_add_networks_table_row_shown(network)
        if i < network_len - 1:
            EditLogicalInterconnectGroups.click_edit_internal_networks_add_networks_add_plus()
        else:
            EditLogicalInterconnectGroups.click_edit_internal_networks_add_networks_add()
            EditLogicalInterconnectGroups.wait_edit_internal_networks_add_networks_dialog_disappear()

    # verify if present in table list
    for i, network in enumerate(network_list):
        EditLogicalInterconnectGroups.wait_edit_internal_networks_table_row_shown(network)

    EditLogicalInterconnectGroups.click_edit_internal_networks_ok()
    EditLogicalInterconnectGroups.wait_edit_internal_networks_dialog_disappear()


def _edit_lig_config_interconnect_settings(fast_mac_cache_failover,
                                           mac_refresh_interval,
                                           igmp_snooping,
                                           igmp_idle_timeout_interval,
                                           loop_protection,
                                           pause_flood_protection,
                                           lldp_tagging,
                                           lldp_enhancedtlv):
    logger.info("configure Interconnect Settings")

    EditLogicalInterconnectGroups.select_logical_interconnect_settings_section()

    if mac_refresh_interval is not None:
        if fast_mac_cache_failover.lower() == "true":
            EditLogicalInterconnectGroups.tick_interconnect_settings_fast_mac_cache_failover()
            EditLogicalInterconnectGroups.input_interconnect_settings_mac_refresh_interval(mac_refresh_interval)
        else:
            EditLogicalInterconnectGroups.untick_interconnect_settings_fast_mac_cache_failover()

    if igmp_snooping is not None:
        if igmp_snooping.lower() == "true":
            EditLogicalInterconnectGroups.tick_interconnect_settings_igmp_snooping()
            EditLogicalInterconnectGroups.input_interconnect_settings_igmp_idle_timeout_interval(igmp_idle_timeout_interval)
        else:
            EditLogicalInterconnectGroups.untick_interconnect_settings_igmp_snooping()

    if loop_protection is not None:
        if loop_protection.lower() == "true":
            EditLogicalInterconnectGroups.tick_interconnect_settings_loop_protection()
        else:
            EditLogicalInterconnectGroups.untick_interconnect_settings_loop_protection()

    if pause_flood_protection is not None:
        if pause_flood_protection.lower() == "true":
            EditLogicalInterconnectGroups.tick_interconnect_settings_pause_flood_protection()
        else:
            EditLogicalInterconnectGroups.untick_interconnect_settings_pause_flood_protection()

    if lldp_tagging is not None:
        if lldp_tagging.lower() == "true":
            EditLogicalInterconnectGroups.tick_interconnect_settings_lldp_tagging()

        else:
            EditLogicalInterconnectGroups.untick_interconnect_settings_lldp_tagging()

    if lldp_enhancedtlv is not None:
        if lldp_enhancedtlv.lower() == "true":
            EditLogicalInterconnectGroups.tick_interconnect_settings_lldp_enhancedtlv()
        else:
            EditLogicalInterconnectGroups.untick_interconnect_settings_lldp_enhancedtlv()


def _edit_lig_remove_uplink_set(uplink_set):
    uplink_set_name = uplink_set.name
    logger.info("Function to call to remove uplink set %s" % uplink_set_name)
    EditLogicalInterconnectGroups.select_general_section()
    EditLogicalInterconnectGroups.click_remove_uplink_set_icon(uplink_set_name)
    EditLogicalInterconnectGroups.wait_uplink_set_box_disappear(uplink_set_name)


def _edit_lig_create_uplink_set(uplink_set, add_plus=False):
    uplink_set_name = uplink_set.name
    uplink_set_type = uplink_set.networkType
    logger.info("Function to call to edit uplink set %s" % uplink_set_name)

    # choose connection mode, LACP timer for ethernet, tunnel, untagged
    if uplink_set_type == "Ethernet":
        __edit_lig_add_ethernet_uplink_set(uplink_set)
    elif uplink_set_type == "Tunnel":
        __edit_lig_add_tunnel_uplink_set(uplink_set)
    elif uplink_set_type == "Untagged":
        __edit_lig_add_untagged_uplink_set(uplink_set)
    elif uplink_set_type == "Fibre Channel":
        __edit_lig_add_fc_uplink_set(uplink_set)
    else:
        ui_lib.fail_test("Not support changing uplink set type '%s'" % uplink_set_type)

    # TODO: simple verify selected networks & uplink ports

    # hit add button
    if add_plus is False:  # add
        C7000CreateLogicalInterconnectGroups.click_create_uplink_set_add()
        C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_dialog_disappear()
    else:  # add plus
        C7000CreateLogicalInterconnectGroups.click_create_uplink_set_add_plus()


def __edit_lig_open_dialog_and_set_uplink_set_name_and_type(uplink_set):
    uplink_set_name = uplink_set.name
    uplink_set_type = uplink_set.networkType
    if C7000CreateLogicalInterconnectGroups.verify_add_uplink_set_dialog_shown(fail_if_false=False) is False:
        # sometimes user might be adding Uplink Set using Create+ button therefore the dialog won't be closed
        # when the next item adding action is calling this function, so add this verify to avoid the unnecessary click/wait
        C7000CreateLogicalInterconnectGroups.click_add_uplink_set()
        C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_dialog_shown()
    C7000CreateLogicalInterconnectGroups.input_create_uplink_set_name(uplink_set_name)
    C7000CreateLogicalInterconnectGroups.select_create_uplink_set_type(uplink_set_type)


def __edit_lig_set_connection_mode_and_lacp(uplink_set):
    # choose connection mode, LACP timer for ethernet, tunnel, untagged
    # - connection mode
    connection_mode = uplink_set.connectionMode.lower()
    if connection_mode == "auto":
        uplink_set_lacp_timer = uplink_set.lacptimer
        EditLogicalInterconnectGroups.tick_create_uplink_set_connection_mode_automatic()
        if uplink_set_lacp_timer != "":
            EditLogicalInterconnectGroups.select_create_uplink_set_lacp_timer(uplink_set_lacp_timer)
    elif connection_mode == "failover":
        EditLogicalInterconnectGroups.tick_create_uplink_set_connection_mode_failover()
    else:
        ui_lib.fail_test(
            "Unexpected ethernet connection mode '%s' of uplink set '%s'" % (connection_mode, uplink_set.name))


def __edit_lig_add_uplink_set_fc_network(uplink_set):
    port_list = [item.strip() for item in uplink_set.ports.split(',')]
    if port_list:
        C7000CreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports()
        C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_add_uplink_ports_to_dialog_shown()
        for i, port_tag in enumerate(port_list):
            bay_no, port_name, port_speed = port_tag.split('|')
            bay_no = bay_no.lower().replace('bay', '')
            C7000CreateLogicalInterconnectGroups.input_create_uplink_set_add_uplink_ports_to_search_port(port_name)
            C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_add_uplink_ports_to_table_row_shown(bay_no, port_name)
            C7000CreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_table_row(bay_no, port_name)
            if i == len(port_list) - 1:
                C7000CreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_add()
            else:
                C7000CreateLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_add_plus()
        C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_add_uplink_ports_to_dialog_disappear()
    else:
        ui_lib.fail_test("no [ ports ] attribute specified in data file when create uplink set > add uplink ports")

    # verify if present in table list
    for i, port_tag in enumerate(port_list):
        bay_no, port_name, port_speed = port_tag.split('|')
        bay_no = bay_no.lower().replace('bay', '')
        C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_port_table_row_shown(bay_no, port_name)


def __edit_lig_add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set):
    port_list = [item.strip() for item in uplink_set.ports.split(',')]
    if port_list:
        EditLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports()
        EditLogicalInterconnectGroups.wait_create_uplink_set_add_uplink_ports_to_dialog_shown()
        for i, port_tag in enumerate(port_list):
            bay_no, port_name = port_tag.split('|')
            bay_no = bay_no.lower().replace('bay', '')
            EditLogicalInterconnectGroups.input_create_uplink_set_add_uplink_ports_to_search_port(port_name)
            EditLogicalInterconnectGroups.wait_create_uplink_set_add_uplink_ports_to_table_row_shown(bay_no, port_name)
            EditLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_table_row(bay_no, port_name)
            if i == len(port_list) - 1:
                EditLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_add()
            else:
                EditLogicalInterconnectGroups.click_create_uplink_set_add_uplink_ports_to_add_plus()
        EditLogicalInterconnectGroups.wait_create_uplink_set_add_uplink_ports_to_dialog_disappear()
    else:
        ui_lib.fail_test("no [ ports ] attribute specified in data file when create uplink set > add uplink ports")

    # verify if present in table list
    for i, port_tag in enumerate(port_list):
        bay_no, port_name = port_tag.split('|')
        bay_no = bay_no.lower().replace('bay', '')
        EditLogicalInterconnectGroups.wait_create_uplink_set_port_table_row_shown(bay_no, port_name)


def __edit_lig_add_ethernet_uplink_set(uplink_set):
    __edit_lig_open_dialog_and_set_uplink_set_name_and_type(uplink_set)
    __edit_lig_set_connection_mode_and_lacp(uplink_set)

    # - networks
    network_list = [item.strip() for item in uplink_set.networks.split(',')]
    if network_list:
        EditLogicalInterconnectGroups.click_create_uplink_set_add_networks()
        EditLogicalInterconnectGroups.wait_create_uplink_set_add_networks_to_dialog_shown()
        for i, network_name in enumerate(network_list):
            EditLogicalInterconnectGroups.input_create_uplink_set_add_networks_to_search_network(network_name)
            EditLogicalInterconnectGroups.wait_create_uplink_set_add_networks_to_table_row_shown(network_name)
            if i == len(network_list) - 1:
                EditLogicalInterconnectGroups.click_create_uplink_set_add_networks_to_add()
            else:
                EditLogicalInterconnectGroups.click_create_uplink_set_add_networks_to_add_plus()
        EditLogicalInterconnectGroups.wait_create_uplink_set_add_networks_to_dialog_disappear()
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")
    # - choose native network
    native_network = getattr(uplink_set, "native", "")
    if native_network != "":
        EditLogicalInterconnectGroups.tick_create_uplink_set_native_network(native_network)

    # verify if present in table list
    for network in network_list:
        EditLogicalInterconnectGroups.wait_create_uplink_set_network_table_row_shown(network)

    # - ports
    __edit_lig_add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set)


def __edit_lig_add_tunnel_uplink_set(uplink_set):
    __edit_lig_open_dialog_and_set_uplink_set_name_and_type(uplink_set)
    __edit_lig_set_connection_mode_and_lacp(uplink_set)

    # - networks
    network = uplink_set.networks
    if network != "":
        EditLogicalInterconnectGroups.select_create_uplink_set_tunnel_network(network)
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")

    # - ports
    __edit_lig_add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set)


def __edit_lig_add_untagged_uplink_set(uplink_set):
    __edit_lig_open_dialog_and_set_uplink_set_name_and_type(uplink_set)
    __edit_lig_set_connection_mode_and_lacp(uplink_set)

    # - networks
    network = uplink_set.networks
    if network != "":
        EditLogicalInterconnectGroups.select_create_uplink_set_untagged_network(network)
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")

    # - ports
    __edit_lig_add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set)


def __edit_lig_add_fc_uplink_set(uplink_set):
    __edit_lig_open_dialog_and_set_uplink_set_name_and_type(uplink_set)

    # - networks
    network = uplink_set.networks
    if network != "":
        EditLogicalInterconnectGroups.select_create_uplink_set_fc_network(network)
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")
    # - ports
    port = uplink_set.ports
    if port == "":
        ui_lib.fail_test("no [ ports ] attribute specified in data file when create uplink set > add networks")

    __edit_lig_add_uplink_set_fc_network(uplink_set)
    # -- port & port speed
    port_list = [item.strip() for item in port.split(',')]
    for port_and_speed in port_list:
        bay_no, port_name, port_speed = port_and_speed.split('|')
        bay_no = bay_no.replace('bay', '')
        EditLogicalInterconnectGroups.select_create_uplink_set_fc_port_speed(bay_no, port_name, port_speed)


def __edit_lig_remove_trap_destination(remove_obj):
    logger.info("Remove trap destination with Destination '{0}'".format(remove_obj.trapdestination))
    C7000EditLogicalInterconnectGroups.click_remove_trap_destination_icon(remove_obj.trapdestination)
    EditLogicalInterconnectGroups.wait_remove_trap_destination_confirm_dialog_shown()
    EditLogicalInterconnectGroups.click_remove_trap_destination_yes_remove()
    EditLogicalInterconnectGroups.wait_remove_trap_destination_confirm_dialog_disappear()
    EditLogicalInterconnectGroups.wait_trap_destination_table_row_disappear(remove_obj.trapdestination)


def __edit_lig_remove_trap_destination_tbird(remove_obj):
    logger.info("Remove trap destination with Destination '{0}'".format(remove_obj.trapdestination))
    TBirdEditLogicalInterconnectGroups.click_remove_trap_destination_icon_tbird(remove_obj.trapdestination)
    EditLogicalInterconnectGroups.wait_remove_trap_destination_confirm_dialog_shown()
    EditLogicalInterconnectGroups.click_remove_trap_destination_yes_remove()
    EditLogicalInterconnectGroups.wait_remove_trap_destination_confirm_dialog_disappear()
    EditLogicalInterconnectGroups.wait_trap_destination_table_row_disappear(remove_obj.trapdestination)


def __edit_lig_add_trap_destination(snmp_obj):
    logger.info("- add Trap Destination settings")
    td_list = snmp_obj.add_trapdestination
    td_len = len(td_list)
    EditLogicalInterconnectGroups.click_add_trap_destination()
    EditLogicalInterconnectGroups.wait_add_trap_destination_dialog_shown()
    for i, td_obj in enumerate(td_list):
        EditLogicalInterconnectGroups.input_add_trap_destination_trap_destination(td_obj.trapdestination)
        EditLogicalInterconnectGroups.input_add_trap_destination_community_string(td_obj.communitystring)
        if td_obj.trapformat.lower() == "snmpv1":
            EditLogicalInterconnectGroups.tick_add_trap_destination_trap_format_snmpv1()
        elif td_obj.trapformat.lower() == "snmpv2":
            EditLogicalInterconnectGroups.tick_add_trap_destination_trap_format_snmpv2()
        else:
            ui_lib.fail_test("unexpected trapformation attribute '%s'" % td_obj.trapformat)
        # TODO: implement detail configuration for severity, VCM traps etc

        if i < td_len - 1:
            EditLogicalInterconnectGroups.click_add_trap_destination_add_plus()
        else:
            EditLogicalInterconnectGroups.click_add_trap_destination_add()
            EditLogicalInterconnectGroups.wait_add_trap_destination_dialog_disappear()
        time.sleep(2)


def __edit_lig_add_snmpaccess(snmp_obj):
    logger.info("- add SNMP access settings")
    sa_list = snmp_obj.add_snmpaccess
    sa_len = len(sa_list)
    EditLogicalInterconnectGroups.click_add_snmp_access()
    EditLogicalInterconnectGroups.wait_add_snmp_access_dialog_shown()
    for i, td_obj in enumerate(sa_list):
        EditLogicalInterconnectGroups.input_add_snmp_access_ip_or_subnet(td_obj.iporsubnet)

        if i < sa_len - 1:
            EditLogicalInterconnectGroups.click_add_snmp_access_add_plus()
        else:
            EditLogicalInterconnectGroups.click_add_snmp_access_add()
            EditLogicalInterconnectGroups.wait_add_snmp_access_dialog_disappear()
        time.sleep(2)


def __edit_lig_remove_snmpaccess(snmp_obj):
    for n, remove_obj in enumerate(snmp_obj.remove_snmpaccess):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(snmp_obj.remove_snmpaccess), '-' * 14))
        logger.info("Remove trap destination with 'ip or subnet' '{0}'".format(remove_obj.iporsubnet))
        EditLogicalInterconnectGroups.click_remove_snmp_access_icon(remove_obj.iporsubnet)
        EditLogicalInterconnectGroups.wait_remove_snmp_access_confirm_dialog_shown()
        EditLogicalInterconnectGroups.click_remove_snmp_access_yes_remove()
        EditLogicalInterconnectGroups.wait_remove_snmp_access_confirm_dialog_disappear()
        EditLogicalInterconnectGroups.wait_snmp_access_table_row_disappear(remove_obj.iporsubnet)


def _edit_lig_config_snmp(snmp_obj):
    snmp_obj = snmp_obj if isinstance(snmp_obj, DataObj) else snmp_obj[0]
    logger.info("updating LIG snmp settings")

    EditLogicalInterconnectGroups.select_logical_snmp_section()
    if hasattr(snmp_obj, 'snmpenabled'):
        if snmp_obj.snmpenabled.lower() == 'enabled':
            EditLogicalInterconnectGroups.toggle_snmp_enabled()
        elif snmp_obj.snmpenabled.lower() == 'disabled':
            EditLogicalInterconnectGroups.toggle_snmp_disabled()
        else:
            ui_lib.fail_test("unexpected snmpenabled attribute '%s'" % snmp_obj.snmpenabled)

    if hasattr(snmp_obj, 'snmpv3enabled'):
        if snmp_obj.snmpv3enabled.lower() == 'enabled':
            C7000CreateLogicalInterconnectGroups.toggle_snmpv3_enabled()
        elif snmp_obj.snmpv3enabled.lower() == 'disabled':
            C7000CreateLogicalInterconnectGroups.toggle_snmpv3_disabled()

    # - The below variants (remove_snmpuser,adduser and edit_snmp_user) are appliacble only for feature toggle for OVF292&OVF293
    # - removes snmpv3 user
    if getattr(snmp_obj, 'remove_snmpuser', None):
        for n, remove_obj in enumerate(snmp_obj.remove_snmpuser):
            logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(snmp_obj.remove_snmpuser), '-' * 14))
            __edit_lig_remove_snmp_user(remove_obj)

    # - adds snmpv3 user
    if getattr(snmp_obj, 'adduser', None):
        _add_snmp_v3_user(snmp_obj)

    # - edits snmpv3 user
    if getattr(snmp_obj, 'edit_snmpuser', None):
        for n, usr_obj in enumerate(snmp_obj.edit_snmpuser):
            logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(snmp_obj.edit_snmpuser), '-' * 14))
            __edit_lig_edit_snmp_user(usr_obj)

    if hasattr(snmp_obj, 'syscontact'):
        EditLogicalInterconnectGroups.input_snmp_system_contact(snmp_obj.syscontact)
    if hasattr(snmp_obj, 'readcommunity'):
        EditLogicalInterconnectGroups.input_snmp_read_community(snmp_obj.readcommunity)

    # - Remove trap destinations
    if getattr(snmp_obj, 'remove_trapdestination', None):
        for n, remove_obj in enumerate(snmp_obj.remove_trapdestination):
            logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(snmp_obj.remove_trapdestination), '-' * 14))
            __edit_lig_remove_trap_destination(remove_obj)
    # - Add trap destinations
    if getattr(snmp_obj, 'add_trapdestination', None):
        __edit_lig_add_trap_destination(snmp_obj)

    # - The below varaints(add_snmpv3_trapdestination,edit_snmpv3_trapdestination,remove_snmpv3_trapdestination) are
    #   applicable only for feature toggle in OVF292 & OVF293
    # - Add snmpv3 trap destinations
    if getattr(snmp_obj, 'add_snmpv3_trapdestination', None):
        __create_lig_add_snmpv3_trap_destination(snmp_obj)
    # - Edit snmpv3 trap destination
    if getattr(snmp_obj, 'edit_snmpv3_trapdestination', None):
        for n, edit_obj in enumerate(snmp_obj.edit_snmpv3_trapdestination):
            logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(snmp_obj.edit_snmpv3_trapdestination), '-' * 14))
            __edit_lig_edit_snmpv3_trap_destination(edit_obj)
    # - remove snmpv3 trap destination
    if getattr(snmp_obj, 'remove_snmpv3_trapdestination', None):
        for n, remove_obj in enumerate(snmp_obj.remove_snmpv3_trapdestination):
            logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(snmp_obj.remove_snmpv3_trapdestination), '-' * 14))
            __edit_lig_remove_snmpv3_trap_destination(remove_obj)

    # remove SNMP Access
    if getattr(snmp_obj, "remove_snmpaccess", None):
        __edit_lig_remove_snmpaccess(snmp_obj)
    # add SNMP Access
    if getattr(snmp_obj, "add_snmpaccess", None):
        __edit_lig_add_snmpaccess(snmp_obj)


def _edit_lig_config_snmp_tbird(snmp_obj):
    snmp_obj = snmp_obj if isinstance(snmp_obj, DataObj) else snmp_obj[0]
    logger.info("updating LIG snmp settings")

    EditLogicalInterconnectGroups.select_logical_snmp_section()

    if hasattr(snmp_obj, 'syscontact'):
        EditLogicalInterconnectGroups.input_snmp_system_contact(snmp_obj.syscontact)
    if hasattr(snmp_obj, 'readcommunity'):
        EditLogicalInterconnectGroups.input_snmp_read_community(snmp_obj.readcommunity)

    # - Remove trap destinations
    if getattr(snmp_obj, 'remove_trapdestination', None):
        for n, remove_obj in enumerate(snmp_obj.remove_trapdestination):
            logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(snmp_obj.remove_trapdestination), '-' * 14))
            __edit_lig_remove_trap_destination_tbird(remove_obj)
    # - Add trap destinations
    if getattr(snmp_obj, 'add_trapdestination', None):
        __edit_lig_add_trap_destination(snmp_obj)

    # - The below variants( adduser, edit_snmpuser, remove_snmpuser,remove_snmpv3_trapdestination,
    #   add_snmpv3_trapdestination,edit_snmpv3_trapdestination) are applicable only for feature toggle in OVF292
    if hasattr(snmp_obj, 'remove_snmpuser'):
        for n, remove_obj in enumerate(snmp_obj.remove_snmpuser):
            logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(snmp_obj.remove_snmpuser), '-' * 14))
            __edit_lig_remove_snmp_user(remove_obj)
    # - Adds new nmpv3 user
    if hasattr(snmp_obj, 'adduser'):
        _add_snmp_v3_user(snmp_obj)
    # - Edits existing snmpv3 users
    if hasattr(snmp_obj, 'edit_snmpuser'):
        for n, edit_obj in enumerate(snmp_obj.edit_snmpuser):
            logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(snmp_obj.edit_snmpuser), '-' * 14))
            __edit_lig_edit_snmp_user(edit_obj)

    # - Remove trap destinations
    if hasattr(snmp_obj, 'remove_snmpv3_trapdestination'):
        for n, remove_obj in enumerate(snmp_obj.remove_snmpv3_trapdestination):
            logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(snmp_obj.remove_snmpv3_trapdestination), '-' * 14))
            __edit_lig_remove_snmpv3_trap_destination(remove_obj)

    # - Add snmpv3 trap destinations
    if hasattr(snmp_obj, 'add_snmpv3_trapdestination'):
        __create_lig_add_snmpv3_trap_destination(snmp_obj)

        # - Edits snmpv3 trap destination
    if hasattr(snmp_obj, 'edit_snmpv3_trapdestination'):
        for n, edit_obj in enumerate(snmp_obj.edit_snmpv3_trapdestination):
            logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(snmp_obj.edit_snmpv3_trapdestination), '-' * 14))
            __edit_lig_edit_snmpv3_trap_destination(edit_obj)

    # add SNMP Access
    if getattr(snmp_obj, "add_snmpaccess", None):
        __edit_lig_add_snmpaccess(snmp_obj)


def _edit_lig_config_qos(qos_configuration_type):
    logger.info("configure Quality of Service (QoS)")
    EditLogicalInterconnectGroups.select_quality_of_service_section()
    EditLogicalInterconnectGroups.select_qos_configuration_type(qos_configuration_type)
    # TODO: implement qos detail configuration if choose "Custom (with FCoE lossless)", "Custom (without FCoE lossless)"
# end - edit LIG


# begin - delete LIG
def delete_logical_interconnect_group(lig_obj):
    """ Delete Logical Interconnect Group(s)
    Arguments:
      <lig>
          name*                     --  Name of logical interconnect group as a string.

    * Required Arguments

    Example:
        data/ligs -> @{TestData.ligs}
        <ligs>
            <lig  name="LIG-wpst32" />
        </ligs>

    * function accepts any lig node with name attribute, will ignore other attributes
    """
    navigate()
    logger.debug("Deleting LIGs...")
    error_string = ""
    err_msg = ""
    err_resolution = ""
    count = 0
    for n, lig in enumerate(lig_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(lig_obj), '-' * 14))
        logger.info("Removing LIG - %s" % lig.name)
        if not select_logical_interconnect_group(lig.name):
            continue
        if 'sas' in getattr(lig, 'interconnecttype', '').lower():
            DeleteLogicalInterconnectGroups.select_sas_actions_delete()
        else:
            DeleteLogicalInterconnectGroups.select_actions_delete()
        if DeleteLogicalInterconnectGroups.wait_delete_dialog_shown(fail_if_false=False) is False:
            if DeleteLogicalInterconnectGroups.wait_delete_error_dialog_shown(fail_if_false=False):
                ui_lib.get_s2l().capture_page_screenshot()
                error_msg = DeleteLogicalInterconnectGroups.get_delete_error_text()
                logger.warn("Got warning message '%s' on trying to remove LIG '%s'" % (error_msg, lig.name))
                error_string += error_msg + '\t'
                DeleteLogicalInterconnectGroups.click_close()
                DeleteLogicalInterconnectGroups.wait_delete_error_dialog_disappear(timeout=10)
            else:
                ui_lib.get_s2l().capture_page_screenshot()
                logger.warn("Failed to delete LIG with name %s" % lig.name)
                error_string += "Failed to delete LIG with name %s" % lig.name + '\t'
            continue
        DeleteLogicalInterconnectGroups.click_yes_delete_button()

        # check if any errors are seen on form on clicking delete
        if DeleteLogicalInterconnectGroups.wait_delete_error_displayed(fail_if_false=False):
            err_msg = DeleteLogicalInterconnectGroups.get_delete_error_message_on_confirm_dialog()
            err_resolution = DeleteLogicalInterconnectGroups.get_error_resolution_on_confirm_dialog()
            logger.warn("ERROR Message while deleting LIG %s : %s \n Resolution : %s" % (lig.name, err_msg, err_resolution))
            DeleteLogicalInterconnectGroups.click_error_popup_close(timeout=10)
            DeleteLogicalInterconnectGroups.wait_delete_dialog_disappear(timeout=10)
            error_string += "Error : %s.Resolution : %s\t" % (err_msg, err_resolution)
            continue
        DeleteLogicalInterconnectGroups.wait_delete_dialog_disappear(timeout=10)

        FusionUIBase.show_activity_sidebar()
        if not CommonOperationLogicalInterconnectGroups.wait_activity_action_ok(lig.name, "Delete", timeout=20, fail_if_false=False):
            error_string += "Activity Delete status is not as expected\t"
        FusionUIBase.show_activity_sidebar()

        if C7000VerifyLogicalInterconnectGroups.verify_lig_not_exist(lig.name, fail_if_false=False):
            logger.info("Remove LIG {0} successfully".format(lig.name))
        elif DeleteLogicalInterconnectGroups.wait_lig_show_not_found(lig.name, fail_if_false=False):
            logger.info("LIG status appear as 'not found', remove LIG {0} successfully.".format(lig.name))
        else:
            msg = "The LIG did not disappear!"
            logger.warn(msg)
            error_string += msg + '\t'
            continue
        count += 1

    if count == 0:
        error_string += "no target LIGs exists!\t"
    if count != len(lig_obj):
        error_string += "Not able to delete all logical interconnect groups!" + '\t'

    if error_string:
        raise AssertionError(error_string)
    logger.debug("Return Value = True")
    return True
# end - delete LIG


# begin - verify LIG
def verify_logical_interconnect_group(ligs_obj):
    """ Verify LIG

    Arguments:
      <lig>
          name*                     --  In General view. Name of LIG as a string.
          type                      --  In General view. LIG type. e.g. C7000
          used_by_eg                --  In General view. Enclosure group associated with this LIG e.g. encgrp32
          used_by_li                --  In General view. Logical interconnect associated with this LIG. e.g. wpst14-lig14
          quality_of_service        --  In Quality of Service view. e.g. Passthrough
          <internal_networks> optional, for verify internal networks configuration (only support 1 node)
              <item>
                name*               --  In Internal Networks view. Internal network name. e.g. dev101-management
                vlan                --  In Internal Networks view. Internal network vlan. e.g. 101. For tunnel network, you can set 'Tunnel' as vlan
          <uplink_set> optional, for verify uplink set configuration (only support 1 node)
              <item> (support multiple nodes)
                name*               --  In Uplink Sets view. Uplink set name. e.g. DA-path1
                type*               --  In Uplink Sets view. Uplink set type. e.g. fc, ethernet
                fc_type             --  In Uplink Sets view. Only take effect when type set to 'fc'. e.g. 'Direct attach', 'Fabric attach'
                <network> optional (support multiple nodes)
                  name*             --  In Uplink Sets view. Network name in uplink set. e.g. DA1
                  speed             --  In Uplink Sets view. Only take effect when type set to 'fc'. e.g. Auto, 4Gb/s
                  connection_mode   --  In Uplink Sets view. Only take effect when type set to 'ethernet'. e.g. Automatic, Failover
                  lacp_timer        --  In Uplink Sets view. Only take effect when type set to 'ethernet'. e.g. Short (1s)
                <uplink> optional
                  name*             --  In Uplink Sets view. Uplink port name. e.g. 'Enclosure 1, Bay 3, Port X2'
          <interconnect_settings> optional (only support 1 node)
              fast_mac_cache_failover       --  In Interconnect settings view. Possible value: Enabled/Disabled
              mac_refresh_interval          --  In Interconnect settings view. e.g. '10 seconds'
              igmp_snooping                 --  In Interconnect settings view. Possible value: Enabled/Disabled
              igmp_idle_timeout_interval    --  In Interconnect settings view. e.g. '260 seconds'
              loop_protection               --  In Interconnect settings view. Possible value: Enabled/Disabled
              pause_flood_protection        --  In Interconnect settings view. Possible value: Enabled/Disabled
          <utilization_sampling> optional (only support 1 node)
              interval_between_samples      --  In Utilization Sampling view. e.g. "300 seconds"
              total_number_of_samples       --  In Utilization Sampling view. e.g. "12"
              sample_collection_rate        --  In Utilization Sampling view. e.g. "12.0 samples per hour"
              total_sampling_history        --  In Utilization Sampling view. e.g. "01:00:00"
          <snmp> optional (only support 1 node)
              snmpv3_enabled                --  In SNMPv3 view. Possible value: Enabled/Disabled
              system_contact                --  In SNMP view. Possible value: None
              read_community                --  In SNMP view. Possible value: public
              <snmpuser> optional (support multiple nodes)
                  enabled                   --  In SNMP view. Possible value: Enabled/Disabled
              system_contact                --  In SNMP view. Possible value: None
              read_community                --  In SNMP view. Possible value: public
              <trapdestination> optional (support multiple nodes)
                 trapdestination*           --  In SNMP Trap Destinations view. e.g. '10.0.0.12'
                 communitystring            --  In SNMP Trap Destinations view. e.g. public1
                 trapformat                 --  In SNMP Trap Destinations view. e.g. SNMPv2<
              <snmpaccess> optional (support multiple nodes)
                 iporsubnet*                --  In SNMP SNMP Access e.g. '192.168.1.1/24'
        <snmpv3>** optional (only support 1 node)
                  username                  --  To verify snmp username
                  authentication_protocol   -- To verify configured authentication protocol set for the user
                  privacy_protocol          -- To verify configured privacy protocol set for the user
                  security_level            -- To verify security level set for the user.
              <snmpv3_trapdestination> optional (support multiple nodes)
                 trapdestination*           --  In SNMPv3 Trap Destinations view. e.g. '10.0.0.12'
                 communitystring            --  In SNMPv3 Trap Destinations view. e.g. public1
                 trapformat                 --  In SNMPv3 Trap Destinations view. e.g. SNMPv3
                 notificationtype           --  In SNMPv3 Trap Destinations view. e.g. Trap
                 username                   --  In SNMPv3 Trap Destinations view. e.g. user1
    * Required Arguments
    ** Applicable only for feature toggle in OVF292/0VF293
    Example:
        data/verifyligs -> @{TestData.verifyligs}
        <verifyligs>
            <lig name="LIG-wpst32"
                 type="C7000"
                 used_by_eg="no enclosure groups"
                 used_by_li="no logical interconnects"
                 quality_of_service="Passthrough" >
                <!--internal networks-->
                <internal_networks>
                    <item name="dev101-management" vlan="101"/>
                    <item name="dev103-ft-a" vlan="103"/>
                    <item name="tu-net1" vlan="Tunnel"/>
                </internal_networks>
                <!--uplink set-->
                <uplink_set>
                    <item name="DA-path1" type="fc" fc_type="Direct attach">
                        <network name="DA1" speed="Auto" />
                        <uplink name="Enclosure 1, Bay 3, Port X2" />
                    </item>
                    <item name="DA-path2" type="fc" fc_type="Direct attach">
                        <network name="DA2" speed="Auto" />
                        <uplink name="Enclosure 1, Bay 4, Port X2" />
                    </item>
                    <item name="FA-path1" type="fc" fc_type="Fabric attach">
                        <network name="FA1" speed="Auto" />
                        <uplink name="Enclosure 1, Bay 5, Port 1" />
                    </item>
                    <item name="FA-path2" type="fc" fc_type="Fabric attach">
                        <network name="FA2" speed="Auto" />
                        <uplink name="Enclosure 1, Bay 6, Port 1" />
                    </item>
                    <item name="FA-path3" type="fc" fc_type="Fabric attach">
                        <network name="FA3" speed="Auto" />
                        <uplink name="Enclosure 1, Bay 1, Port X1" />
                    </item>
                    <item name="FA-path4" type="fc" fc_type="Fabric attach">
                        <network name="FA4" speed="Auto" />
                        <uplink name="Enclosure 1, Bay 2, Port X1" />
                    </item>
                    <item name="FO-net" type="ethernet" connection_mode="Automatic" lacp_timer="Short (1s)">
                        <network name="dev102-vmmigration" vlan_id="102" type="Untagged" />
                        <uplink name="Enclosure 1, Bay 1, Port X2" />
                        <uplink name="Enclosure 1, Bay 3, Port X3" />
                    </item>
                    <item name="Pub-net" type="ethernet" connection_mode="Automatic" lacp_timer="Short (1s)">
                        <network name="dev100" vlan_id="100" type="Untagged" />
                        <uplink name="Enclosure 1, Bay 1, Port X3" />
                    </item>
                    <item name="PXE-net" type="ethernet" connection_mode="Automatic" lacp_timer="Short (1s)">
                        <network name="dev300-pxeboot" vlan_id="300" type="Untagged" />
                        <uplink name="Enclosure 1, Bay 2, Port X3" />
                    </item>
                </uplink_set>
                <!--interconnect settings-->
                <interconnect_settings fast_mac_cache_failover="Enabled"
                                       mac_refresh_interval="10 seconds"
                                       igmp_snooping="Disabled"
                                       igmp_idle_timeout_interval="260 seconds"
                                       loop_protection="Enabled"
                                       pause_flood_protection="Enabled"
                        />
                <!--Utilization Sampling-->
                <utilization_sampling interval_between_samples="300 seconds"
                                      total_number_of_samples="12"
                                      sample_collection_rate="12.0 samples per hour"
                                      total_sampling_history="01:00:00"
                        />
                <!--SNMP-->
                <snmp enabled="Enabled"
                      system_contact=""
                      read_community="public">
                    <trapdestination trapdestination="10.0.0.12" communitystring="public1" trapformat="SNMPv2" />
                    <trapdestination trapdestination="172.2.1.3" communitystring="public2" trapformat="SNMPv1" />
                    <snmpaccess iporsubnet="192.168.1.0/24" />
                    <snmpaccess iporsubnet="192.168.1.1/24" />
                </snmp>

            </lig>
        </verifyligs>

        <verifylig>
        <lig name="LIG1">
        <snmpv3 snmpv3_enabled="true" readcommunity="public">
        <snmpuser user="user1" security_level="none"></snmpuser>
        <snmpv3_trapdestination trapdestination="1.1.11.0" trapformat="SNMPV3" notificationtype="user1" username="user1"></snmpv3_trapdetination>
    </snmpv3>
    </lig>
    </verifylig>
    """
    navigate()

    count = 0
    ret = True
    for n, lig_obj in enumerate(ligs_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(ligs_obj), '-' * 14))
        logger.info("Verifying a LIG with name %s" % lig_obj.name)
        if not select_logical_interconnect_group(lig_obj.name):
            continue

        # overview
        FusionUIBase.select_view_by_name('General')
        logger.info("Verifying configuration in General view...")

        if hasattr(lig_obj, 'type'):
            C7000VerifyLogicalInterconnectGroups.verify_general_type(lig_obj.type)

        if hasattr(lig_obj, 'used_by_eg'):
            C7000VerifyLogicalInterconnectGroups.verify_general_used_by_eg(lig_obj.used_by_eg)

        if hasattr(lig_obj, 'used_by_li'):
            C7000VerifyLogicalInterconnectGroups.verify_general_used_by_li(lig_obj.used_by_li)

        # internal networks
        if hasattr(lig_obj, 'internal_networks'):
            logger.info("Verifying configuration in Internal Networks view...")

            FusionUIBase.select_view_by_name('Internal Networks')
            internal_networks = lig_obj.internal_networks

            # verify network number in view title like 'Internal Networks (3)'
            if len(internal_networks) > 0:
                C7000VerifyLogicalInterconnectGroups.verify_internal_network_count(len(internal_networks))

            for network in internal_networks:
                C7000VerifyLogicalInterconnectGroups.verify_internal_network_name_exist(network.name)
                if hasattr(network, 'vlan'):
                    C7000VerifyLogicalInterconnectGroups.verify_internal_network_vlan(network.name, network.vlan)

        # uplink sets
        if hasattr(lig_obj, 'uplink_set'):
            logger.info("Verifying configuration in Uplink Sets view...")

            FusionUIBase.select_view_by_name('Uplink Sets')

            uplink_sets = lig_obj.uplink_set

            for uplink_set in uplink_sets:
                C7000VerifyLogicalInterconnectGroups.verify_uplink_sets_item_exist(uplink_set.name)
                C7000VerifyLogicalInterconnectGroups.make_uplink_set_panel_into_viewpoint(uplink_set.name)
                # expand panel
                C7000VerifyLogicalInterconnectGroups.expand_uplink_set_in_uplink_sets_view(uplink_set.name)
                C7000VerifyLogicalInterconnectGroups.wait_uplink_sets_panel_shown(uplink_set.name)

                # fc network
                if uplink_set.type == 'fc':

                    if hasattr(uplink_set, 'network'):

                        if hasattr(uplink_set, 'type'):
                            C7000VerifyLogicalInterconnectGroups.verify_uplink_set_fc_network_type(uplink_set.name, uplink_set.fc_type)

                        for network in uplink_set.network:
                            if hasattr(network, 'name'):
                                C7000VerifyLogicalInterconnectGroups.verify_uplink_set_fc_network_name(uplink_set.name, network.name)

                            if hasattr(network, 'speed'):
                                C7000VerifyLogicalInterconnectGroups.verify_uplink_set_fc_network_speed(uplink_set.name, network.speed)

                    if hasattr(uplink_set, 'uplink'):
                        for uplink in uplink_set.uplink:
                            C7000VerifyLogicalInterconnectGroups.verify_uplink_set_fc_port(uplink_set.name, uplink.name)

                # ethernet network
                if uplink_set.type == 'ethernet':

                    if hasattr(uplink_set, 'connection_mode'):
                        C7000VerifyLogicalInterconnectGroups.verify_uplink_set_ethernet_network_connection_mode(uplink_set.name, uplink_set.connection_mode)

                    if hasattr(uplink_set, 'lacp_timer'):
                        C7000VerifyLogicalInterconnectGroups.verify_uplink_set_ethernet_network_lacp_timer(uplink_set.name, uplink_set.lacp_timer)

                    if hasattr(uplink_set, 'network'):
                        networks = uplink_set.network

                        for network in networks:
                            C7000VerifyLogicalInterconnectGroups.verify_uplink_set_ethernet_network_exist(uplink_set.name, network.name)
                            C7000VerifyLogicalInterconnectGroups.verify_uplink_set_ethernet_network_vlan(uplink_set.name, network.name, network.vlan_id)
                            C7000VerifyLogicalInterconnectGroups.verify_uplink_set_ethernet_network_type(uplink_set.name, network.name, network.type)

                    if hasattr(uplink_set, 'uplink'):
                        uplinks = uplink_set.uplink

                        for uplink in uplinks:
                            C7000VerifyLogicalInterconnectGroups.verify_uplink_set_ethernet_network_port_exist(uplink_set.name, uplink.name)
                            if hasattr(uplink, 'speed'):
                                C7000VerifyLogicalInterconnectGroups.verify_uplink_ethernet_network_speed(uplink_set.name, uplink.name, uplink.speed, 10)
                            if hasattr(uplink, 'auto_negotiation'):
                                C7000VerifyLogicalInterconnectGroups.verify_uplink_ethernet_network_auto_negotiation(uplink_set.name, uplink.name, uplink.auto_negotiation, 10)

                # folding panel
                C7000VerifyLogicalInterconnectGroups.fold_uplink_set_in_uplink_sets_view(uplink_set.name)

        # interconnect settings
        if hasattr(lig_obj, 'interconnect_settings'):
            logger.info("Verifying configuration in Interconnect settings view...")

            FusionUIBase.select_view_by_name('Interconnect settings')

            interconnect_settings = lig_obj.interconnect_settings
            interconnect_settings = interconnect_settings[0] if isinstance(interconnect_settings, list) else interconnect_settings
            if hasattr(interconnect_settings, 'fast_mac_cache_failover'):
                C7000VerifyLogicalInterconnectGroups.verify_interconnect_settings_fast_mac_cache_failover(interconnect_settings.fast_mac_cache_failover)

            if hasattr(interconnect_settings, 'mac_refresh_interval'):
                C7000VerifyLogicalInterconnectGroups.verify_interconnect_settings_mac_refresh_interval(interconnect_settings.mac_refresh_interval)

            if hasattr(interconnect_settings, 'igmp_snooping'):
                C7000VerifyLogicalInterconnectGroups.verify_interconnect_settings_igmp_snooping(interconnect_settings.igmp_snooping)

            if hasattr(interconnect_settings, 'igmp_idle_timeout_interval'):
                C7000VerifyLogicalInterconnectGroups.verify_interconnect_settings_igmp_idle_timeout_interval(interconnect_settings.igmp_idle_timeout_interval)

            if hasattr(interconnect_settings, 'loop_protection'):
                C7000VerifyLogicalInterconnectGroups.verify_interconnect_settings_loop_protection(interconnect_settings.loop_protection)

            if hasattr(interconnect_settings, 'pause_flood_protection'):
                C7000VerifyLogicalInterconnectGroups.verify_interconnect_settings_pause_flood_protection(interconnect_settings.pause_flood_protection)

        # utilization sampling
        if hasattr(lig_obj, 'utilization_sampling'):
            logger.info("Verifying configuration in Utilization Sampling view...")

            FusionUIBase.select_view_by_name('Utilization Sampling')

            utilization_sampling = lig_obj.utilization_sampling
            utilization_sampling = utilization_sampling[0] if isinstance(utilization_sampling, list) else utilization_sampling
            if hasattr(utilization_sampling, 'interval_between_samples'):
                C7000VerifyLogicalInterconnectGroups.verify_utilization_sampling_interval_between_samples(utilization_sampling.interval_between_samples)

            if hasattr(utilization_sampling, 'total_number_of_samples'):
                C7000VerifyLogicalInterconnectGroups.verify_utilization_sampling_total_number_of_samples(utilization_sampling.total_number_of_samples)

            if hasattr(utilization_sampling, 'sample_collection_rate'):
                C7000VerifyLogicalInterconnectGroups.verify_utilization_sampling_sample_collection_rate(utilization_sampling.sample_collection_rate)

            if hasattr(utilization_sampling, 'total_sampling_history'):
                C7000VerifyLogicalInterconnectGroups.verify_utilization_sampling_total_sampling_history(utilization_sampling.total_sampling_history)

        # snmp
        if hasattr(lig_obj, 'snmp'):
            logger.info("Verifying configuration in SNMP view...")

            FusionUIBase.select_view_by_name('SNMP')

            snmp = lig_obj.snmp
            snmp = snmp[0] if isinstance(snmp, list) else snmp

            if hasattr(snmp, 'enabled'):
                C7000VerifyLogicalInterconnectGroups.verify_snmp_enabled(snmp.enabled)
            # The below variants (snmpv1v2_enabled,snmpv3_enabled,snmpuser)are applicable only for feature toggle in OVF293
            if hasattr(snmp, 'snmpv1v2_enabled'):
                C7000VerifyLogicalInterconnectGroups.verify_snmpv1v2_enabled(snmp.snmpv1v2_enabled)

            if hasattr(snmp, 'snmpv3_enabled'):
                C7000VerifyLogicalInterconnectGroups.verify_snmpv3_enabled(snmp.snmpv3_enabled)
            # - snmp user
            if hasattr(snmp, 'snmpuser'):
                logger.info("Verifying SNMP users...")
                snmp_snmpuser = snmp.snmpuser
                for user in snmp_snmpuser:
                    if C7000VerifyLogicalInterconnectGroups.verify_snmp_users_user_exist(user.username):
                        logger.info("Successfully verified that snmp user %s exist" % user.username)
                    if hasattr(user, 'privacy_protocol'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_user_priv_protocol(user.username, user.privacy_protocol)
                    if hasattr(user, 'authentication_protocol'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_user_auth_protocol(user.username, user.authentication_protocol)
                    if hasattr(user, 'security_level'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_user_security_level(user.username, user.security_level)

            if hasattr(snmp, 'system_contact'):
                C7000VerifyLogicalInterconnectGroups.verify_snmp_system_contact(snmp.system_contact)

            if hasattr(snmp, 'read_community'):
                C7000VerifyLogicalInterconnectGroups.verify_snmp_read_community(snmp.read_community)

            # - trap destination
            if hasattr(snmp, 'trapdestination'):
                logger.info("Verifying SNMP trap destination settings...")

                snmp_trapdestination = snmp.trapdestination

                for trap_item in snmp_trapdestination:
                    C7000VerifyLogicalInterconnectGroups.verify_snmp_trap_destinations_destination_exist(trap_item.trapdestination)
                    if hasattr(snmp_trapdestination, 'communitystring'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmp_trap_destinations_community_string(trap_item.trapdestination, trap_item.communitystring)
                    if hasattr(snmp_trapdestination, 'trapformat'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmp_trap_destinations_format(trap_item.trapdestination, trap_item.trapformat)

            # The below variants snmpv3_trapdestination is applicable only for feature toggle in OVF293
            if hasattr(snmp, 'snmpv3_trapdestination'):
                logger.info("Verifying SNMPv3 trap destination settings...")
                snmp_trapdestination = snmp.snmpv3_trapdestination
                for trap_item in snmp_trapdestination:
                    CommonOperationLogicalInterconnectGroups.click_snmpv3_trap_destination_values(trap_item.trapdestination)
                    C7000VerifyLogicalInterconnectGroups.verify_snmp_trap_destinations_destination_exist(trap_item.trapdestination)
                    if hasattr(snmp_trapdestination, 'communitystring'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_trap_destinations_community_string()
                    if hasattr(snmp_trapdestination, 'trapformat'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_trap_destinations_format(trap_item.trapdestination, trap_item.trapformat)
                    if hasattr(trap_item, 'port'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_trap_destinations_port(trap_item.trapdestination, trap_item.port)
                    if hasattr(trap_item, 'notificationtype'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_trap_destinations_notification_type(trap_item.trapdestination, trap_item.notificationtype)
                    if hasattr(trap_item, 'engineid'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_trap_destinations_engineid(trap_item.trapdestination, trap_item.engineid)
                    if hasattr(trap_item, 'username'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_trap_destinations_username(trap_item.trapdestination, trap_item.username)
                    if hasattr(trap_item, 'severity'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_trap_destinations_severity(trap_item.trapdestination, trap_item.severity)
                    if hasattr(trap_item, 'vcm_traps'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_trap_destinations_vcm_traps(trap_item.trapdestination, trap_item.vcm_traps)
                    if hasattr(trap_item, 'enet_traps'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmv3_trap_destinations_enet_traps(trap_item.trapdestination, trap_item.enet_traps)
                    if hasattr(trap_item, 'fc_traps'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_trap_destinations_fc_traps(trap_item.trapdestination, trap_item.fc_traps)
                    CommonOperationLogicalInterconnectGroups.close_snmpv3_trap_destination_values(trap_item.trapdestination)

            # - access
            if hasattr(snmp, 'snmpaccess'):
                logger.info("Verifying SNMP access settings...")

                snmp_access = snmp.snmpaccess

                for access_item in snmp_access:
                    C7000VerifyLogicalInterconnectGroups.verify_snmp_access_ip_or_subnet_exist(access_item.iporsubnet)

        # quality of service
        if hasattr(lig_obj, 'quality_of_service'):
            logger.info("Verifying configuration in Quality of Service view...")

            FusionUIBase.select_view_by_name('Quality of Service')

            C7000VerifyLogicalInterconnectGroups.verify_quality_of_service_qos_configuration_type(lig_obj.quality_of_service)

        count += 1

    if count == 0:
        msg = "no target LIG exists!"
        logger.warn(msg)
        logger.warn("Return Value = False")
        return False

    if count != len(ligs_obj):
        logger.warn("Not able to verify all LIGs!")
        logger.warn("Return Value = False")
        return False

    logger.debug("Return Value = %s" % ret)
    return ret


# end - verify LIG

def verify_logical_interconnect_group_tbird(ligs_obj):
    """ Verify LIG

    Arguments:
      <lig>
          name*                     --  In General view. Name of LIG as a string.
          used_by_eg                --  In General view. Enclosure group associated with this LIG e.g. encgrp32
          used_by_li                --  In General view. Logical interconnect associated with this LIG. e.g. wpst14-lig14
          quality_of_service        --  In Quality of Service view. e.g. Passthrough
          <internal_networks> optional, for verify internal networks configuration (only support 1 node)
              <item>
                name*               --  In Internal Networks view. Internal network name. e.g. dev101-management
                vlan                --  In Internal Networks view. Internal network vlan. e.g. 101. For tunnel network, you can set 'Tunnel' as vlan
          <uplink_set> optional, for verify uplink set configuration (only support 1 node)
              <item> (support multiple nodes)
                name*               --  In Uplink Sets view. Uplink set name. e.g. DA-path1
                type*               --  In Uplink Sets view. Uplink set type. e.g. fc, ethernet
                fc_type             --  In Uplink Sets view. Only take effect when type set to 'fc'. e.g. 'Direct attach', 'Fabric attach'
                <network> optional (support multiple nodes)
                  name*             --  In Uplink Sets view. Network name in uplink set. e.g. DA1
                  speed             --  In Uplink Sets view. Only take effect when type set to 'fc'. e.g. Auto, 4Gb/s
                  connection_mode   --  In Uplink Sets view. Only take effect when type set to 'ethernet'. e.g. Automatic, Failover
                  lacp_timer        --  In Uplink Sets view. Only take effect when type set to 'ethernet'. e.g. Short (1s)
                <uplink> optional
                  name*             --  In Uplink Sets view. Uplink port name. e.g. 'Enclosure 1, Bay 3, Port Q1'
          <interconnect_settings> optional (only support 1 node)
              fast_mac_cache_failover       --  In Interconnect settings view. Possible value: Enabled/Disabled
              mac_refresh_interval          --  In Interconnect settings view. e.g. '10 seconds'
              igmp_snooping                 --  In Interconnect settings view. Possible value: Enabled/Disabled
              igmp_idle_timeout_interval    --  In Interconnect settings view. e.g. '260 seconds'
              loop_protection               --  In Interconnect settings view. Possible value: Enabled/Disabled
              pause_flood_protection        --  In Interconnect settings view. Possible value: Enabled/Disabled
          <utilization_sampling> optional (only support 1 node)
              interval_between_samples      --  In Utilization Sampling view. e.g. "300 seconds"
              total_number_of_samples       --  In Utilization Sampling view. e.g. "12"
              sample_collection_rate        --  In Utilization Sampling view. e.g. "12.0 samples per hour"
              total_sampling_history        --  In Utilization Sampling view. e.g. "01:00:00"
          <snmp> optional (only support 1 node)
              enabled                       --  In SNMP view. Possible value: Enabled/Disabled
              system_contact                --  In SNMP view. Possible value: None
              read_community                --  In SNMP view. Possible value: public
              <trapdestination> optional (support multiple nodes)
                 trapdestination*           --  In SNMP Trap Destinations view. e.g. '10.0.0.12'
                 communitystring            --  In SNMP Trap Destinations view. e.g. public1
                 trapformat                 --  In SNMP Trap Destinations view. e.g. SNMPv2
              <snmpaccess> optional (support multiple nodes)
                 iporsubnet*                --  In SNMP SNMP Access e.g. '192.168.1.1/24'

    * Required Arguments

    Example:
        data/verifyligs -> @{TestData.verifyligs}
        <verifyligs>
            <lig name="LIG-wpst32"
                 used_by_eg="no enclosure groups"
                 used_by_li="no logical interconnects"
                 quality_of_service="Passthrough" >
                <!--internal networks-->
                <internal_networks>
                    <item name="dev101-management" vlan="101"/>
                    <item name="dev103-ft-a" vlan="103"/>
                    <item name="tu-net1" vlan="Tunnel"/>
                </internal_networks>
                <!--uplink set-->
                <uplink_set>
                    <item name="DA-path1" type="fc" fc_type="Direct attach">
                        <network name="DA1" speed="Auto" />
                        <uplink name="Enclosure 1, Bay 3, Port Q1" />
                    </item>
                    <item name="DA-path2" type="fc" fc_type="Direct attach">
                        <network name="DA2" speed="Auto" />
                        <uplink name="Enclosure 1, Bay 6, Port Q1" />
                    </item>
                </uplink_set>
                <!--interconnect settings-->
                <interconnect_settings fast_mac_cache_failover="Enabled"
                                       mac_refresh_interval="10 seconds"
                                       igmp_snooping="Disabled"
                                       igmp_idle_timeout_interval="260 seconds"
                                       loop_protection="Enabled"
                                       pause_flood_protection="Enabled"
                        />
                <!--Utilization Sampling-->
                <utilization_sampling interval_between_samples="300 seconds"
                                      total_number_of_samples="12"
                                      sample_collection_rate="12.0 samples per hour"
                                      total_sampling_history="01:00:00"
                        />
                <!--SNMP-->
                <snmp enabled="Enabled"
                      system_contact=""
                      read_community="public">
                    <trapdestination trapdestination="10.0.0.12" communitystring="public1" trapformat="SNMPv2" />
                    <trapdestination trapdestination="172.2.1.3" communitystring="public2" trapformat="SNMPv1" />
                    <snmpaccess iporsubnet="192.168.1.0/24" />
                    <snmpaccess iporsubnet="192.168.1.1/24" />
                </snmp>

            </lig>
        </verifyligs>

    """

    logger.info("\n*** Verifying Logical Interconnect Group ***")

    navigate()
    count = 0
    for n, lig_obj in enumerate(ligs_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(ligs_obj), '-' * 14))
        logger.info("Verifying a LIG with name %s" % lig_obj.name)
        if not select_logical_interconnect_group(lig_obj.name):
            continue

        # overview
        FusionUIBase.select_view_by_name('General')
        logger.info("Verifying configuration in General view...")
        logger.info("checking the used by attribute values")
        # checking the used by attribute for none case scenario
        used_by_text = CommonOperationLogicalInterconnectGroups.get_text_used_by()
        if used_by_text == "none":
            logger.info("text value of used by attribute is %s" % used_by_text)
        else:
            logger.info("click the link used by eg or li")
            if hasattr(lig_obj, 'used_by_eg'):
                used_by = CommonOperationLogicalInterconnectGroups.get_text_used_by()
                logger.info("value of used_by %s" % used_by)
                enc_group = lig_obj.used_by_eg
                for used_by_eg in enc_group:
                    # click operation for used by eg link
                    TBirdCommonOperationLogicalInterconnectGroups.click_link_used_by_eg()
                    logger.info("verifying whether eg exists")
                    CommonOperationEnclosureGroups.verify_enclosure_group_exist(used_by_eg.egname)
                    # navigate to LIG page
                    navigate()
                    # verifying whether the lig is selected or not
                    if not select_logical_interconnect_group(lig_obj.name):
                        continue

            if hasattr(lig_obj, 'used_by_li'):
                used_by = CommonOperationLogicalInterconnectGroups.get_text_used_by()
                logger.info("value of used_by %s" % used_by)
                logical_inc = lig_obj.used_by_li
                for used_by_li in logical_inc:
                    # click operation for used by li link
                    TBirdCommonOperationLogicalInterconnectGroups.click_link_used_by_li()
                    logger.info("verifying whether li exists")
                    VerifyLogicalInterconnects.verify_logical_interconnect_exist(used_by_li.liname)
                    # navigate to LIG page
                    navigate()
                    # verifying whether the lig is selected or not
                    if not select_logical_interconnect_group(lig_obj.name):
                        continue

        # internal networks
        if hasattr(lig_obj, 'internal_networks'):
            logger.info("Verifying configuration in Internal Networks view...")

            FusionUIBase.select_view_by_name('Internal Networks')
            internal_networks = lig_obj.internal_networks

            # verify network number in view title like 'Internal Networks (3)'
            if len(internal_networks) > 0:
                TBirdVerifyLogicalInterconnectGroups.verify_internal_network_count(len(internal_networks))

            for network in internal_networks:
                TBirdVerifyLogicalInterconnectGroups.verify_internal_network_name_exist(network.name)
                if hasattr(network, 'vlan'):
                    TBirdVerifyLogicalInterconnectGroups.verify_internal_network_vlan(network.name, network.vlan)

        # interconnect settings
        if hasattr(lig_obj, 'interconnect_settings'):
            logger.info("Verifying configuration in Interconnect settings view...")

            FusionUIBase.select_view_by_name('Interconnect Settings')

            interconnect_settings = lig_obj.interconnect_settings
            interconnect_settings = interconnect_settings[0] if isinstance(interconnect_settings, list) else interconnect_settings

            if hasattr(interconnect_settings, 'fast_mac_cache_failover'):
                TBirdVerifyLogicalInterconnectGroups.verify_interconnect_settings_fast_mac_cache_failover(interconnect_settings.fast_mac_cache_failover)

            if hasattr(interconnect_settings, 'mac_refresh_interval'):
                TBirdVerifyLogicalInterconnectGroups.verify_interconnect_settings_mac_refresh_interval(interconnect_settings.mac_refresh_interval)

            if hasattr(interconnect_settings, 'igmp_snooping'):
                TBirdVerifyLogicalInterconnectGroups.verify_interconnect_settings_igmp_snooping(interconnect_settings.igmp_snooping)

            if hasattr(interconnect_settings, 'igmp_idle_timeout_interval'):
                TBirdVerifyLogicalInterconnectGroups.verify_interconnect_settings_igmp_idle_timeout_interval(interconnect_settings.igmp_idle_timeout_interval)

            if hasattr(interconnect_settings, 'loop_protection'):
                TBirdVerifyLogicalInterconnectGroups.verify_interconnect_settings_loop_protection(interconnect_settings.loop_protection)

            if hasattr(interconnect_settings, 'pause_flood_protection'):
                TBirdVerifyLogicalInterconnectGroups.verify_interconnect_settings_pause_flood_protection(interconnect_settings.pause_flood_protection)

        # utilization sampling
        if hasattr(lig_obj, 'utilization_sampling'):
            logger.info("Verifying configuration in Utilization Sampling view...")

            FusionUIBase.select_view_by_name('Utilization Sampling')

            utilization_sampling = lig_obj.utilization_sampling
            utilization_sampling = utilization_sampling[0] if isinstance(utilization_sampling, list) else utilization_sampling
            if hasattr(utilization_sampling, 'interval_between_samples'):
                TBirdVerifyLogicalInterconnectGroups.verify_utilization_sampling_interval_between_samples(utilization_sampling.interval_between_samples)

            if hasattr(utilization_sampling, 'total_number_of_samples'):
                TBirdVerifyLogicalInterconnectGroups.verify_utilization_sampling_total_number_of_samples(utilization_sampling.total_number_of_samples)

            if hasattr(utilization_sampling, 'sample_collection_rate'):
                TBirdVerifyLogicalInterconnectGroups.verify_utilization_sampling_sample_collection_rate(utilization_sampling.sample_collection_rate)

            if hasattr(utilization_sampling, 'total_sampling_history'):
                TBirdVerifyLogicalInterconnectGroups.verify_utilization_sampling_total_sampling_history(utilization_sampling.total_sampling_history)

        # snmp
        if hasattr(lig_obj, 'snmp'):
            logger.info("Verifying configuration in SNMP view...")

            FusionUIBase.select_view_by_name('SNMP')

            snmp = lig_obj.snmp
            snmp = snmp[0] if isinstance(snmp, list) else snmp

            if hasattr(snmp, 'enabled'):
                TBirdVerifyLogicalInterconnectGroups.verify_snmp_enabled(snmp.enabled)

            if hasattr(snmp, 'system_contact'):
                TBirdVerifyLogicalInterconnectGroups.verify_snmp_system_contact(snmp.system_contact)
            if hasattr(snmp, 'snmpv3_enabled'):
                C7000VerifyLogicalInterconnectGroups.verify_snmp_enabled(snmp.snmpv3_enabled)
            if hasattr(snmp, 'read_community'):
                TBirdVerifyLogicalInterconnectGroups.verify_snmp_read_community(snmp.read_community)

            # - trap destination
            if hasattr(snmp, 'trapdestination'):
                logger.info("Verifying SNMP trap destination settings...")

                snmp_trapdestination = snmp.trapdestination

                for trap_item in snmp_trapdestination:
                    TBirdVerifyLogicalInterconnectGroups.verify_snmp_trap_destinations_destination_exist(trap_item.trapdestination)
                    if hasattr(snmp_trapdestination, 'communitystring'):
                        TBirdVerifyLogicalInterconnectGroups.verify_snmp_trap_destinations_community_string(trap_item.trapdestination, trap_item.communitystring)
                    if hasattr(snmp_trapdestination, 'trapformat'):
                        TBirdVerifyLogicalInterconnectGroups.verify_snmp_trap_destinations_format(trap_item.trapdestination, trap_item.trapformat)
            # The below variants(snmpuser,snmpv3_trapdestination) is applicable only for feature toglle in OVF292
            if hasattr(snmp, 'snmpuser'):
                logger.info("Verifying SNMP users...")
                snmp_snmpuser = snmp.snmpuser
                for user in snmp_snmpuser:

                    if C7000VerifyLogicalInterconnectGroups.verify_snmp_users_user_exist(user.username):
                        logger.info("Successfully verified that snmp user %s exist" % user.username)
                    if hasattr(user, 'privacy_protocol'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_user_priv_protocol(user.username, user.privacy_protocol)
                    if hasattr(user, 'authentication_protocol'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_user_auth_protocol(user.username, user.authentication_protocol)
                    if hasattr(user, 'security_level'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_user_security_level(user.username, user.security_level)

            if hasattr(snmp, 'snmpv3_trapdestination'):
                logger.info("Verifying SNMPv3 trap destination settings...")

                snmp_trapdestination = snmp.snmpv3_trapdestination

                for trap_item in snmp_trapdestination:
                    C7000VerifyLogicalInterconnectGroups.get_snmpv3_trap_destination_values(trap_item.trapdestination)
                    C7000VerifyLogicalInterconnectGroups.verify_snmp_trap_destinations_destination_exist(trap_item.trapdestination)
                    if hasattr(snmp_trapdestination, 'communitystring'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_trap_destinations_community_string()
                    if hasattr(snmp_trapdestination, 'trapformat'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_trap_destinations_format(trap_item.trapdestination, trap_item.trapformat)
                    if hasattr(trap_item, 'port'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_trap_destinations_port(trap_item.trapdestination, trap_item.port)
                    if hasattr(trap_item, 'notificationtype'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_trap_destinations_notification_type(trap_item.trapdestination, trap_item.notificationtype)
                    if hasattr(trap_item, 'engineid'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_trap_destinations_EngineID(trap_item.trapdestination, trap_item.engineid)
                    if hasattr(trap_item, 'username'):
                        C7000VerifyLogicalInterconnectGroups.verify_snmpv3_trap_destinations_username(trap_item.trapdestination, trap_item.username)

            # - access
            if hasattr(snmp, 'snmpaccess'):
                logger.info("Verifying SNMP access settings...")

                snmp_access = snmp.snmpaccess

                for access_item in snmp_access:
                    TBirdVerifyLogicalInterconnectGroups.verify_snmp_access_ip_or_subnet_exist(access_item.iporsubnet)

        # quality of service
        if hasattr(lig_obj, 'quality_of_service'):
            logger.info("Verifying configuration in Quality of Service view...")

            FusionUIBase.select_view_by_name('Quality of Service')

            TBirdVerifyLogicalInterconnectGroups.verify_quality_of_service_qos_configuration_type(lig_obj.quality_of_service)
        # Logical Interconnect Group settings

        if hasattr(lig_obj, 'logical_interconnect_settings'):
            logger.info("Verifying configuration in Logical Interconnect settings view...")
            FusionUIBase.select_view_by_name('Logical Interconnect Group')
            logical_interconnect_settings = lig_obj.logical_interconnect_settings
            logical_interconnect_settings = logical_interconnect_settings[0] if isinstance(logical_interconnect_settings, list) else logical_interconnect_settings
            # check redundancy
            if hasattr(logical_interconnect_settings, 'redundancy'):
                TBirdVerifyLogicalInterconnectGroups.verify_interconnect_settings_redundancy(logical_interconnect_settings.redundancy)
            # uplink sets
        if hasattr(lig_obj, 'uplink_set'):
            logger.info("Verifying configuration in Uplink Sets view...")

            FusionUIBase.select_view_by_name('Uplink Sets')

            uplink_sets = lig_obj.uplink_set

            for uplink_set in uplink_sets:
                TBirdVerifyLogicalInterconnectGroups.verify_uplink_sets_item_exist(uplink_set.name)
                CommonOperationLogicalInterconnectGroups.make_uplink_set_panel_into_viewpoint(uplink_set.name)
                # expand panel
                TBirdVerifyLogicalInterconnectGroups.expand_uplink_set_in_uplink_sets_view(uplink_set.name)
                TBirdVerifyLogicalInterconnectGroups.wait_uplink_sets_panel_shown(uplink_set.name)

                # fc network
                if uplink_set.type == 'fc':

                    if hasattr(uplink_set, 'network'):

                        if hasattr(uplink_set, 'type'):
                            TBirdVerifyLogicalInterconnectGroups.verify_uplink_set_fc_network_type(uplink_set.name, uplink_set.fc_type)

                        for network in uplink_set.network:
                            if hasattr(network, 'name'):
                                TBirdVerifyLogicalInterconnectGroups.verify_uplink_set_fc_network_name(uplink_set.name, network.name)

                            if hasattr(network, 'speed'):
                                TBirdVerifyLogicalInterconnectGroups.verify_uplink_set_fc_network_speed(uplink_set.name, network.speed)

                    if hasattr(uplink_set, 'uplink'):
                        for uplink in uplink_set.uplink:
                            TBirdVerifyLogicalInterconnectGroups.verify_uplink_set_fc_port(uplink_set.name, uplink.name)

                # ethernet network
                if uplink_set.type == 'ethernet':

                    if hasattr(uplink_set, 'connection_mode'):
                        TBirdVerifyLogicalInterconnectGroups.verify_uplink_set_ethernet_network_connection_mode(uplink_set.name, uplink_set.connection_mode)

                    if hasattr(uplink_set, 'lacp_timer'):
                        TBirdVerifyLogicalInterconnectGroups.verify_uplink_set_ethernet_network_lacp_timer(uplink_set.name, uplink_set.lacp_timer)

                    if hasattr(uplink_set, 'network'):
                        networks = uplink_set.network

                        for network in networks:
                            TBirdVerifyLogicalInterconnectGroups.verify_uplink_set_ethernet_network_exist(uplink_set.name, network.name)
                            TBirdVerifyLogicalInterconnectGroups.verify_uplink_set_ethernet_network_vlan(uplink_set.name, network.name, network.vlan_id)

                    if hasattr(uplink_set, 'uplink'):
                        uplinks = uplink_set.uplink

                        for uplink in uplinks:
                            TBirdVerifyLogicalInterconnectGroups.verify_uplink_set_ethernet_network_port_exist(uplink_set.name, uplink.name)
                            if hasattr(uplink, 'speed'):
                                TBirdVerifyLogicalInterconnectGroups.verify_uplink_ethernet_network_speed(uplink_set.name, uplink.name, uplink.speed)
                            if hasattr(uplink, 'auto_negotiation'):
                                TBirdVerifyLogicalInterconnectGroups.verify_uplink_ethernet_network_auto_negotiation(uplink_set.name, uplink.name, uplink.auto_negotiation)

                # folding panel
                TBirdVerifyLogicalInterconnectGroups.fold_uplink_set_in_uplink_sets_view(uplink_set.name)

        count += 1

    if count == 0:
        logger.warn("no target LIG exists!")
        return False

    if count != len(ligs_obj):
        ui_lib.fail_test("Not able to verify all LIGs!")
    return True


def select_logical_interconnect_group(ligname):
    """ select_logical_interconnect_group

        Example:
        | `Select LST`      |     |
    """
    navigate()

    logger.info("Selecting a LIG with name '{0}'".format(ligname))
    if VerifyLogicalInterconnectGroups.verify_lig_exist(ligname, fail_if_false=False):
        CommonOperationLogicalInterconnectGroups.click_lig(ligname)
        CommonOperationLogicalInterconnectGroups.wait_lig_selected(ligname)
        return True
    else:
        logger.warn("LIG '{0}' does not exist".format(ligname))
        ui_lib.get_s2l().capture_page_screenshot()
        return False


def create_logical_interconnect_group_tbird(*lig_obj):
    '''
    Function to create LIG for TBIRD
    Returns True if creation is successful without any errors else returns error string
    '''

    logging._log_to_console_and_log_file("*** Create logical interconnect group for TBird***")
    selenium2lib = ui_lib.get_s2l()
    errors_on_form = None
    error_status = None
    error = 0
    error_string = ''

    ic_data = {}

    ''' Set the redundancy Mapping values '''
    # initialize dictionaries containing the redundancy options and IC types
    redundancy = FusionLogicalInterconnectGroupPage.LIG_REDUNDANCY
    if not selenium2lib._is_element_present(FusionLogicalInterconnectGroupPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element_visible(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()

    if isinstance(lig_obj, test_data.DataObj):
        lig_obj = [lig_obj]
    elif isinstance(lig_obj, tuple):
        lig_obj = list(lig_obj[0])

    for lig in lig_obj:
        # if the lig type is not Tbird skip creation
        if str(lig.type).lower() != "tbird":
            logging._warn("The LIG type specified is not 'tbird' and is '{}'.Skipping creation".format(lig.type))
            continue

        ic_data.clear()
        ibs = int(lig.ibs)
        ic_type_a = ""
        ic_type_b = ""

        ''' Find out the ic types in each enclosure '''
        # add the enclosure number and the IC types for the enclosure in the dictionary
        if hasattr(lig, "switch"):
            for ic in lig.switch:  # lig.ic:
                ic_data[ic.enc] = ic.type

        # Skip creation if name not specified
        if lig.name.strip() == "" or lig.name is None:
            logging._warn("LIG name not specified.Check input!!")
            continue

        # skip this LIG creation if already present
        if ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.XPATH_LIG_TABLE_ELEMENT % lig.name, PerfConstants.DEFAULT_SYNC_TIME):
            logging._warn("LIG '{0}' already present".format(lig.name))
            continue

        # privilege check - if user does not have privilege break out of the loop
        if not ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_LINK_CREATE_LOGICAL_INTERCONNECT_GROUPS, PerfConstants.DEFAULT_SYNC_TIME):
            logging._warn("Create Logical Interconnects Group button not seen in UI!! User may not have create privilege.")
            error += 1
            error_string += "Create Logical Interconnects Group button not seen in UI!! User may not have create privilege.\t"
            break

        # Click create link and  type LIG name
        logging._log_to_console_and_log_file("\nCreating LIG : {}".format(lig.name))

        selenium2lib.click_link(FusionLogicalInterconnectGroupPage.ID_LINK_CREATE_LOGICAL_INTERCONNECT_GROUPS)
        ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_ADD_LIG)
        ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectGroupPage.ID_INPUT_NAME_LST, lig.name)

        ''' Select the enclosure count '''
        if hasattr(lig, 'enccount'):
            logging._log_to_console_and_log_file("Setting Enclosure Count : {}".format(lig.enccount))
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_ENC_COUNT)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_ENC_COUNT_SELECT % lig.enccount)

        # select the interconnect bay set
        if hasattr(lig, 'ibs'):
            logging._log_to_console_and_log_file("Setting Interconnect Bay Set : {}".format(lig.ibs))
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_IBS)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_IBS_SELECT % lig.ibs)

        # set redundancy
        if hasattr(lig, 'redundancy'):
            redundancy_ov = redundancy[lig.redundancy.upper()]
            logging._log_to_console_and_log_file("Setting Redundancy : {}".format(redundancy_ov))
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_REDUNDANCY)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_REDUNDANCY_SELECT % redundancy_ov)

        # click select interconnect button
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_SELECT_INTERCONNECT, PerfConstants.DEFAULT_SYNC_TIME)
        if not ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_ADD_SWITCH, PerfConstants.DEFAULT_SYNC_TIME):
            logging._warn("Unable to Click  select Interconnects button!!")
            error += 1
            error_string += "Unable to Click Select Interconnects button!!\t"
            return False

        # type LIG name - fail safe
        ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectGroupPage.ID_INPUT_NAME_LST, lig.name)

        if ic_data:
            select_interconnect_status = _select_interconnect_tbird(int(lig.enccount), int(lig.ibs), ic_data)
            if select_interconnect_status:
                logging._warn("--Error while selecting interconnects--")
                error += 1
                error_string += select_interconnect_status
            else:
                logging._log_to_console_and_log_file("\n---Interconnects Selected Successfully--\n")

        # CODE TO ADD LOGICAL UPLINK SET TO EXISTING LOGICAL INTERCONNECT GROUP
        addlus = None
        if hasattr(lig, 'addlus'):
            addlus = lig.addlus
            if addlus is None:
                logging._warn("There are no Logical Uplink Sets to add in input")
            if isinstance(addlus, (list)):
                for lus in addlus:
                    ui_lib.scroll_into_view(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_LOGICAL_UPLINK_TEMPLATE)
                    if not _add_lus_to_lig(lus):
                        logging._warn("Error While adding Logical Uplink Set {}".format(lus.name))
                        error += 1
                        error_string += "Error While adding Logical Uplink Set {}\t".format(lus.name)
        else:
            logging._warn("No  Logical Uplink Sets specified in input")

        # add internal network
        add_internal_netowrks = None
        if hasattr(lig, 'internalnetwork'):
            add_internal_netowrks = lig.internalnetwork
            if add_internal_netowrks is None:
                logging._warn("No Internal Networks to add")
            if isinstance(add_internal_netowrks, (list)):
                logging._log_to_console_and_log_file("\n----Adding internal networks to LIG---")
                for internal_network in add_internal_netowrks:
                    if not _add_internal_network(internal_network):
                        logging._warn("Error While adding internal network {}".format(internal_network.name))
                        error += 1
                        error_string += "Error While adding internal network {}\t".format(internal_network.name)
                logging._log_to_console_and_log_file("\n----Adding internal networks to LIG Completed---\n")
        else:
            logging._warn("No Internal Networks to add")

        # Code to add interconnect settings
        if _add_interconnect_settings(lig):
            logging._log_to_console_and_log_file("--Interconnect Settings Set successfully---")
        else:
            logging._warn("Error While adding interconnect settings")
            error += 1
            error_string += "Error While adding interconnect settings\t"

        # set snmp system contact and read community
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LIG_ADD_PANEL_SELECTOR)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.LINK_LIG_SNMP, PerfConstants.DEFAULT_SYNC_TIME)

        if hasattr(lig, "syscontact"):
            if lig.syscontact.lower().strip() not in ("", None, "none"):
                ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectGroupPage.ID_LIG_SYSTEM_CONTACT, lig.syscontact)
        else:
            logging._warn("No system contact to be added")

        if hasattr(lig, "readcommunity"):
            if lig.readcommunity.lower().strip() not in ("", None, "none"):
                ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectGroupPage.ID_LIG_READ_COMMUNITY, lig.readcommunity)
        else:
            logging._warn("No read community to be added")

        # CODE TO ADD TRAP destinations
        addtraps = None
        if hasattr(lig, 'addtrapdest'):
            addtraps = lig.addtrapdest
            if addtraps is None:
                logging._warn("There are no Trap Destinations to be added")
            if isinstance(addtraps, (list)):
                for trap in addtraps:
                    trap_status = None
                    trap_status = _add_trap_to_lig_tbird(trap)
                    if trap_status:
                        logging._warn("Error While adding Trap destination {}".format(trap.ip))
                        error += 1
                        error_string += "Error While adding Trap destination {}\t".format(trap.ip) + trap_status + "\t"
                    else:
                        logging._log_to_console_and_log_file("Trap '{}' added successfully".format(trap.ip))
        else:
            logging._warn("There are no Trap Destinations to be added")

        # click create
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_CREATE_LST)
        ui_lib.wait_for_element_notvisible(FusionLogicalInterconnectGroupPage.ID_LIG_ADD_FORM, timeout=20)

        logging._log_to_console_and_log_file("Checking For errors on form...")
        # check for errors
        errors_on_form = base_page.get_errors_on_form(FusionLogicalInterconnectGroupPage.ID_LIG_ADD)
        # check if any status errors are seen
        error_status = ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.XPATH_EG_ADD_HP_STATUS_ERROR)
        if error_status or errors_on_form:
            error += 1
            if errors_on_form:
                error_string += errors_on_form + "\t"
            if error_status:
                logger._warn("Error Summary - {}".format(ui_lib.get_text(FusionLogicalInterconnectGroupPage.XPATH_EG_ADD_FORM_MESSAGE_SUMMARY)))
                logger._warn("Error Details - {}".format(ui_lib.get_text(FusionLogicalInterconnectGroupPage.XPATH_EG_ADD_FORM_MESSAGE_DETAILS)))
                error_string += ui_lib.get_text(FusionLogicalInterconnectGroupPage.XPATH_EG_ADD_FORM_MESSAGE_SUMMARY) + "." + ui_lib.get_text(FusionLogicalInterconnectGroupPage.XPATH_EG_ADD_FORM_MESSAGE_DETAILS) + "\t"
            # if add form is still seen click cancel
            if ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_LIG_ADD_FORM):
                logger._log_to_console_and_log_file("Clicking Cancel")
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_CANCEL_LST)
            continue
        else:
            logger._log_to_console_and_log_file("- No errors Seen")

        # wait for creation to complete
        timeout = 1
        while timeout <= FusionLogicalInterconnectGroupPage.TIMEOUT:
            logger._log_to_console_and_log_file("Creation in progress...")
            if ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.XPATH_UPDATE_COMPLETE, FusionLogicalInterconnectGroupPage.UPDATE_WAIT_TIME):
                logger._log_to_console_and_log_file("Creation Completed.\n")
                break
            elif ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.XPATH_UPDATE_STATUS_WARNING, FusionLogicalInterconnectGroupPage.UPDATE_WAIT_TIME):
                logger._warn("Creation Completed but with warning")
                break
            elif ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.XPATH_UPDATE_STATUS_ERROR, FusionLogicalInterconnectGroupPage.UPDATE_WAIT_TIME):
                logger._warn("--Error during creation")
                break
            timeout += (FusionLogicalInterconnectGroupPage.UPDATE_WAIT_TIME * 3) / 60.0

        if timeout > FusionLogicalInterconnectGroupPage.TIMEOUT:
            logger._warn("Either Creation of LIG '{}' has not completed or Create Alert is not seen , even after waiting for {} minutes!!".format(lig.name, timeout))
            # if add form is still seen click cancel
            if ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_LIG_ADD_FORM):
                logger._log_to_console_and_log_file("Clicking Cancel")
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_CANCEL_LST)

        if not ui_lib.table_contains(FusionLogicalInterconnectGroupPage.ID_LIG_TABLE, lig.name):
            logging._warn("LIG '{0}' is not seen in UI".format(lig.name))
            error += 1
            error_string += "LIG '{0}' is not seen in UI".format(lig.name)
        else:
            logging._log_to_console_and_log_file("LIG '{0}' is seen in UI".format(lig.name))

    # if add form is still visible
    if ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_LIG_ADD_FORM, 10):
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_CANCEL_LST)
        ui_lib.wait_for_element_notvisible(FusionLogicalInterconnectGroupPage.ID_BTN_CANCEL_LST, timeout=30)

    # if error - return error strings else return true
    if error > 0:
        return error_string
    else:
        return True


def _select_interconnect_tbird(enclosure_count, interconnect_bay_set, ic_data):
    '''
    Function to select interconnects for TBird LIG
    Returns NOne if no errors are seen , else returns error string
    '''
    error = 0
    error_string = ""
    ic_type_a = ""
    ic_type_b = ""
    interconnect_type = FusionLogicalInterconnectGroupPage.IC_TYPE

    enclosure_xpath = ""
    interconnect_bay_xpath = ""
    dropdown_options_xpath = ""
    interconnet_xpath = ""
    # initialize xpaths based on add/edit form visible
    if ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_LIG_ADD_FORM):
        enclosure_xpath = FusionLogicalInterconnectGroupPage.ID_ENCLOSURE_INDEX
        interconnect_bay_xpath = FusionLogicalInterconnectGroupPage.ID_INTERCONNECT_BAY
        dropdown_options_xpath = FusionLogicalInterconnectGroupPage.ID_DROP_DOWN_OPTIONS
        ic_second_bayset_member_xpath = FusionLogicalInterconnectGroupPage.XPATH_ADD_INTERCONNECT_SECOND_BAYSET_MEMBER
    elif ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_LIG_EDIT_FORM):
        enclosure_xpath = FusionLogicalInterconnectGroupPage.ID_LIG_EDIT_ENCLOSURE_INDEX
        interconnect_bay_xpath = FusionLogicalInterconnectGroupPage.ID_LIG_EDIT_INTERCONNECT_BAY
        dropdown_options_xpath = FusionLogicalInterconnectGroupPage.ID_LIG_EDIT_DROP_DOWN_OPTIONS
        ic_second_bayset_member_xpath = FusionLogicalInterconnectGroupPage.XPATH_EDIT_INTERCONNECT_SECOND_BAYSET_MEMBER
    else:
        logging._warn("Neither ADD nor EDIT LIG form is seen!!Cannot select interconnects")
        return "Neither ADD nor EDIT LIG form is seen!!Cannot select interconnects\t"

    # selecting interconnects for the enclosures
    for i in range(1, enclosure_count + 1):
        ic_type = []
        '''Select A side interconnects '''
        # scroll into view only if enclosure count is greater than 1
        if enclosure_count > 1:
            ui_lib.scroll_into_view(enclosure_xpath % i, align_with_top=True)

        if str(i) in ic_data:
            logging._log_to_console_and_log_file("\nSelecting Interconnects for Enclosure {}".format(i))
            ic_type = ic_data[str(i)].split("|")
            if ic_type[0] != "":
                if ui_lib.wait_for_element_visible(interconnect_bay_xpath % (str(i), str(interconnect_bay_set))):
                    ui_lib.wait_for_element_and_click(interconnect_bay_xpath % (str(i), str(interconnect_bay_set)), PerfConstants.DEFAULT_SYNC_TIME)  # cic-switch-template-add-device-%s-%s/cic-switch-template-edit-device-%s-%s
                    ic_type_a = interconnect_type[ic_type[0]]
                    ica = (dropdown_options_xpath % (str(i), str(interconnect_bay_set), ic_type_a))  # cic-switch-template-add-device-%s-%s/cic-switch-template-edit-device-%s-%s

                    # check if ic-a is seen in the dropdown
                    if ui_lib.wait_for_element_visible(ica, PerfConstants.DEFAULT_SYNC_TIME):
                        logging._log_to_console_and_log_file("Selecting interconnect : '%s' for Bay : '%d' " % (ic_type_a, interconnect_bay_set))
                        ui_lib.wait_for_element_and_click(ica, PerfConstants.DEFAULT_SYNC_TIME)
                    else:
                        logger._warn("The IC '{}' is not seen in the drop down for bay '{}'!!!".format(ic_type_a, interconnect_bay_set))
                        error += 1
                        error_string += "The IC '{}' is not seen in the drop down for bay '{}'!!!\t".format(ic_type_a, interconnect_bay_set)

            if ic_type[1] != "":
                if ui_lib.wait_for_element_visible(interconnect_bay_xpath % (str(i), str(interconnect_bay_set + FusionLogicalInterconnectGroupPage.BAY_SET_MEMBER_INCREMENT))):
                    # scroll the IC into view
                    ui_lib.scroll_into_view(ic_second_bayset_member_xpath % str(i), True)
                    ui_lib.wait_for_element_and_click(interconnect_bay_xpath % (str(i), str(interconnect_bay_set + FusionLogicalInterconnectGroupPage.BAY_SET_MEMBER_INCREMENT)), PerfConstants.DEFAULT_SYNC_TIME)  # cic-switch-template-add-device-%s-%s/cic-switch-template-edit-device-%s-%s
                    ic_type_b = interconnect_type[ic_type[1]]
                    icb = (dropdown_options_xpath % (str(i), str(interconnect_bay_set + FusionLogicalInterconnectGroupPage.BAY_SET_MEMBER_INCREMENT), ic_type_b))

                    # check if ic-b is seen in the dropdown
                    if ui_lib.wait_for_element_visible(icb, PerfConstants.DEFAULT_SYNC_TIME):
                        logging._log_to_console_and_log_file("Selecting Interconnect : '%s' for Bay : '%d' " % (ic_type_b, interconnect_bay_set + FusionLogicalInterconnectGroupPage.BAY_SET_MEMBER_INCREMENT))
                        ui_lib.wait_for_element_and_click(icb, PerfConstants.DEFAULT_SYNC_TIME)
                    else:
                        logger._warn("The IC '{}' is not seen in the drop down for bay '{}'!!!".format(ic_type_b, interconnect_bay_set + FusionLogicalInterconnectGroupPage.BAY_SET_MEMBER_INCREMENT))
                        error += 1
                        error_string += "The IC '{}' is not seen in the drop down for bay '{}'!!!\t".format(ic_type_b, interconnect_bay_set + FusionLogicalInterconnectGroupPage.BAY_SET_MEMBER_INCREMENT)
            # Fail safe sleep
            BuiltIn().sleep(5)

    if error > 0:
        return error_string
    return None


def _add_internal_network(internal_network):
    '''
    Function to add/remove internal networks to lig
    Returns True if no errors are seen else returns False
    '''
    logging._log_to_console_and_log_file(internal_network)

    # click edit
    if not ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.XPATH_LIG_INTERNAL_NETWORK_EDIT, PerfConstants.DEFAULT_SYNC_TIME):
        logging._warn("Edit internal Network Button Not Visible in UI!")
        return False
    ui_lib.scroll_into_view(FusionLogicalInterconnectGroupPage.XPATH_LIG_INTERNAL_NETWORK_EDIT)
    if not ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.XPATH_LIG_INTERNAL_NETWORK_EDIT, PerfConstants.DEFAULT_SYNC_TIME):
        logging._warn("Unable to click Edit internal Network Button!")
        return False
    # check if networks are present
    if ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.XPATH_LIG_NO_INTERNAL_NETWORKS, PerfConstants.DEFAULT_SYNC_TIME):
        logging._warn("No networks to add.Create some first!!")
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.XPATH_LIG_INTERNAL_NETWORKS_CANCEL)
        return False

    # check if the network is already added
    if not ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.XPATH_LIG_INTERNAL_NETWORK_ADDED % internal_network.name, PerfConstants.DEFAULT_SYNC_TIME):
        # click add networks
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LIG_INTERNAL_NETWORK_ADD)
        # check if the network is seen in the table
        if ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.XPATH_LIG_INTERNAL_NETWORK % internal_network.name, PerfConstants.DEFAULT_SYNC_TIME):
            # select network
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.XPATH_LIG_INTERNAL_NETWORK % internal_network.name)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.XPATH_LIG_INTERNAL_NETWORK_ADD)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LIG_INTERNALE_NETWORK_EDIT_OK)
            logging._log_to_console_and_log_file("Added internal network : '{}' to LIG".format(internal_network.name))
            return True
        else:
            # if not present click cancel
            logging._warn("The network {} is not present in the table.Make sure it exists".format(internal_network.name))
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.XPATH_LIG_INTERNAL_NETWORK_CANCEL)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.XPATH_LIG_INTERNALE_NETWORK_EDIT_CANCEL)
            return False
    else:
        if hasattr(internal_network, "action"):
            if str(internal_network.action).lower() == "remove":
                logging._log_to_console_and_log_file("Removing internal network : '{}'".format(internal_network.name))
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.XPATH_LIG_REMOVE_INTERNAL_NETWORK % internal_network.name)
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LIG_INTERNALE_NETWORK_EDIT_OK)
                return True

        logging._log_to_console_and_log_file("The network '{}' is already added".format(internal_network.name))
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LIG_INTERNALE_NETWORK_EDIT_OK)
        return True


def _add_lus_to_lig(lus):
    """ add_lus_to_edit_lig
       This function will add a new logical uplink set to existing logical interconnect group.

    """
    logging._log_to_console_and_log_file("----- function call to add uplink Set %s " % lus.name)
    # filling values in UI as supplied via xml data sheet
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_LOGICAL_UPLINK_TEMPLATE)
    # ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_LOGICAL_UPLINK_TEMPLATE)

    # function to add uplink set
    if(_add_logical_uplink_set(lus.name, lus.networkType, lus.connectionMode, lus.networks, lus.native, lus.ports, lus.preferredPort, lus.ports, lus.lacptimer)):
        if (lus.has_property("negative")):
            logging._log_to_console_and_log_file("-----Added Uplink Set with name %s.  Caller wanted it to fail." % lus.name)
            return False
        else:
            logging._log_to_console_and_log_file("-----Added Uplink Set with name %s" % lus.name)
            return True
    else:
        if (lus.has_property("negative")):
            logging._log_to_console_and_log_file("-----Failed to add Uplink Set with name %s as expected" % lus.name)
            return True
        else:
            logging._log_to_console_and_log_file("-----Failed to add Uplink Set with name %s" % lus.name)
            return False


def _add_interconnect_settings(lig_obj):
    """ add/edit Logical Interconnect settings

        Example:
        | `add Logical Interconnect settings`      |     |
    Returns True if no errors are seen else returns False
    """
    logging._log_to_console_and_log_file("\n*** Adding/Editing  Interconnect settings ***\n")
    # logging._log_to_console_and_log_file(lig_obj)
    s2l = ui_lib.get_s2l()
    return_value = True

    interconnect_settings_xpath = ""
    igmp_snooping_xpath = ""
    igmp_timeout_xpath = ""
    loop_protection_xpath = ""
    # initialize xpaths based on add/edit form visible
    if ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_LIG_ADD_FORM):
        interconnect_settings_xpath = FusionLogicalInterconnectGroupPage.ID_LIG_INTERCONNECT_SETTINGS
        igmp_snooping_xpath = FusionLogicalInterconnectGroupPage.ID_CHKBOX_IGMPSNOOPING
        igmp_timeout_xpath = FusionLogicalInterconnectGroupPage.ID_INPUT_IGMP_IDLETTIMEOUTINTERVAL
        loop_protection_xpath = FusionLogicalInterconnectGroupPage.XPATH_LOOPPROTECTION_CHECKBOX
    elif ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_LIG_EDIT_FORM):
        interconnect_settings_xpath = FusionLogicalInterconnectGroupPage.ID_EDIT_LIG_INTERCONNECT_SETTINGS
        igmp_snooping_xpath = FusionLogicalInterconnectGroupPage.ID_EDIT_LIG_CHKBOX_IGMPSNOOPING
        igmp_timeout_xpath = FusionLogicalInterconnectGroupPage.ID_EDIT_LIG_INPUT_IGMP_IDLETTIMEOUTINTERVAL
        loop_protection_xpath = FusionLogicalInterconnectGroupPage.XPATH_EDIT_LIG_LOOPPROTECTION_CHECKBOX
    else:
        logging._warn("Neither ADD nor EDIT LIG form is seen!!Cannot set interconnect settings")
        return False

    # get the interconnect settings in visible area
    ui_lib.scroll_into_view(interconnect_settings_xpath)

    # edit IGMP snooping
    if hasattr(lig_obj, "igmpsnooping"):
        if lig_obj.igmpsnooping.lower() == "true":
            ui_lib.wait_for_element_visible(igmp_snooping_xpath, PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_checkbox_and_select(igmp_snooping_xpath)
            logging._log_to_console_and_log_file("Enabling IGMP Snooping")
            # time.sleep(10)
            if hasattr(lig_obj, "igmpidletimeout"):
                if not (lig_obj.igmpidletimeout == ""):
                    ui_lib.wait_for_element_visible(igmp_timeout_xpath, 10)
                    if lig_obj.igmpidletimeout.lower() <= '3600':
                        logging._log_to_console_and_log_file("Setting IGMP idle timeout interval to : {}".format(lig_obj.igmpidletimeout))
                        ui_lib.wait_for_element_and_input_text(igmp_timeout_xpath, lig_obj.igmpidletimeout)
                    else:
                        logging._warn("Setting IGMP idle timeout interval to : 3600 since input {} is more than allowed value of 3600".format(lig_obj.igmpidletimeout))
                        ui_lib.wait_for_element_and_input_text(igmp_timeout_xpath, '3600')
                        return_value = False
            else:
                logging._warn("IGMP idle timeout interval not specified in input")
        elif lig_obj.igmpsnooping.lower() == "false":
            logging._log_to_console_and_log_file("Disabling IGMP Snooping")
            ui_lib.wait_for_checkbox_and_unselect(igmp_snooping_xpath)
        else:
            logging._warn("Invalid Input for IGMP snooping.Should be either 'True' or 'False'")
            return_value = False
    else:
        logging._warn("IGMP snooping not specified in input")
    # edit loop protection
    if (hasattr(lig_obj, "loopprotection")):
        ui_lib.wait_for_element_visible(loop_protection_xpath)
        if(lig_obj.loopprotection.lower() == "true"):
            logging._log_to_console_and_log_file("Enabling loop protection")
            ui_lib.wait_for_checkbox_and_select(loop_protection_xpath)
        elif(lig_obj.loopprotection.lower() == "false"):
            logging._log_to_console_and_log_file("Disabling loop protection")
            ui_lib.wait_for_checkbox_and_unselect(loop_protection_xpath)
        else:
            logging._warn("Invalid Input for Loop Protection.Should be either 'True' or 'False'")
            return_value = False
    else:
        logging._warn("Loop Protection not specified in input")

    # Added newly for Edit lldp Tagging
    if (hasattr(lig_obj, "lldptagging")):
        lldp_tagging = lig_obj.lldptagging
        logger.info("Tagging value is %s" % lldp_tagging)
        if lldp_tagging is not None:
            if lldp_tagging.lower() == "true":
                logger.info("lldp Interconnect Settings")
                EditLogicalInterconnectGroups.tick_interconnect_settings_lldp_tagging(lldp_tagging)
            else:
                EditLogicalInterconnectGroups.untick_interconnect_settings_lldp_tagging(lldp_tagging)
    else:
        logger.warn("LLDP not specified in input")
        return False
    return return_value


def _add_trap_to_lig_tbird(trap):
    """ This function is to add/edit/remove trap to LIG """
    """_add_trap_to_edit_lig

        Example:
        |_add_trap_to_edit_lig(trap)
    Returns None if no errors are seen else returns the error string
    """

    error = 0
    error_string = ''
    logging._log_to_console_and_log_file("\nAdding Trap Destination IP : %s " % trap.ip)
    selenium2lib = ui_lib.get_s2l()
    validateip = validate_trap_ip(trap.ip)
    # validate IP
    if (validateip):
        ui_lib.scroll_into_view(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_TRAPS)
        if not selenium2lib._is_element_present(FusionLogicalInterconnectGroupPage.ID_TRAP_PATH % trap.ip):
            ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_TRAPS, PerfConstants.TRAP_BUTTON)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_TRAPS)
            # provide input
            ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_TXT_INPUT_TRAP, PerfConstants.INPUT_TEXT_TRAP)
            ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectGroupPage.ID_TXT_INPUT_TRAP, trap.ip)
            ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectGroupPage.ID_COMMUNITY_STRING, trap.communitystring)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_TRAP_FORMAT % trap.trapformat)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_ADD_TRAP)
        else:
            logging._log_to_console_and_log_file("Trap '{}' already added to the appliance.....".format(trap.ip))
            # if action is to remove delete the trap else if it is to edit , edit the trap
            if hasattr(trap, "action"):
                if str(trap.action).lower() == "remove":
                    logging._log_to_console_and_log_file("Removing trap '{}'".format(trap.ip))
                    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.XPATH_LIG_REMOVE_TRAP % trap.ip)
                    # click ok
                    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.XPATH_LIG_REMOVE_TRAP_OK, PerfConstants.DEFAULT_SYNC_TIME)
                elif str(trap.action).lower() == "edit":
                    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.XPATH_LIG_EDIT_TRAP % trap.ip)
                    # provide values
                    ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_TXT_INPUT_TRAP, PerfConstants.INPUT_TEXT_TRAP)
                    ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectGroupPage.ID_TXT_INPUT_TRAP, trap.newip)
                    ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectGroupPage.ID_COMMUNITY_STRING, trap.communitystring)
                    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_TRAP_FORMAT % trap.trapformat)
                    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LIG_TRAP_EDIT_OK)

        # check if any status errors are seen after create/edit
        error_status = ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.XPATH_EG_TRAP_HP_STATUS_ERROR)
        if error_status:
            logger._warn("Error Seen .\nError Summary - {}".format(ui_lib.get_text(FusionLogicalInterconnectGroupPage.XPATH_EG_TRAP_ERROR_MESSAGE_SUMMARY)))
            logger._warn("Error Details - {}".format(ui_lib.get_text(FusionLogicalInterconnectGroupPage.XPATH_EG_TRAP_ERROR_MESSAGE_DETAILS)))
            error_string += ui_lib.get_text(FusionLogicalInterconnectGroupPage.XPATH_EG_TRAP_ERROR_MESSAGE_SUMMARY) + "." + ui_lib.get_text(FusionLogicalInterconnectGroupPage.XPATH_EG_TRAP_ERROR_MESSAGE_DETAILS) + "\t"
            error += 1
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.XPATH_LIG_TRAP_CANCEL)

    else:
        logging._warn("Invalid Trap IP {}".format(trap.ip))
        error += 1
        error_string += "Invalid Trap IP {}\t".format(trap.ip)

    if error > 0:
        return error_string
    return None


def validate_trap_ip(trap):
    """ This function will validate the trap IP address """
    """validate_trap_ip

        Example:
        | validate_trap_ip(trap)
    """
    ip = trap.split('.')
    flag = 0
    if(len(ip) == 4):
        try:
            for address in ip[0:len(ip)]:
                if 0 <= int(address) <= 255:
                    flag = flag + 1
            if flag == 4:
                logging._log_to_console_and_log_file("IP is in the valid class")
                return True
            else:
                logging._log_to_console_and_log_file("IP is not in the valid class")
                return False
        except:
            logging._log_to_console_and_log_file("Invalid IP")
    else:
        logging._log_to_console_and_log_file("Length of IP is invalid")
        return False


def delete_all_appliance_ligs():
    selenium2lib = ui_lib.get_s2l()
    """ Navigate to Logical Interconnects Page """
    if not selenium2lib._is_element_present(FusionLogicalInterconnectGroupPage.ID_PAGE_LABEL):
        navigate()

    ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_LIG_TABLE)
    ligs_list = CommonOperationLogicalInterconnectGroups.get_lig_list()
    for lig_name in ligs_list:
        logger._log_to_console_and_log_file("Deleting LIG: %s" % lig_name)
        lig_obj = test_data.DataObj()
        lig_obj.add_property('name', lig_name)
        lig_obj = (lig_obj,)
        lig_delete_status = delete_logical_interconnect_group(lig_obj)
        if lig_delete_status is False:
            logger._warn("Failed to delete LIG: {0}".format(lig_name))
            return False
        else:
            logger._log_to_console_and_log_file("'{0}' LIG is deleted Successfully".format(lig_name))
    return True


def _add_logical_uplink_set(lusname, ustype, mode, networks, nativenetwork, uplinkethports, preferredport, fcswitchandport, timer):
    """ This function will add the given logical uplink set of existing logical interconnect group. """
    """ _add_logical_uplink_set

        Example:
        | _add_logical_uplink_set(lusname, ustype, mode, networks, nativenetwork, uplinkethports, preferredport, fcswitchandport):
    """
    flag_bool = True

    logging._log_to_console_and_log_file("--adding inputs to Logical Uplink Set")
    selenium2lib = ui_lib.get_s2l()
    ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectGroupPage.ID_INPUT_UPLINK_NAME, lusname)

    # Specify if it's an ethernet or FC network
    # selenium2lib.click_element("xpath=//div[text()='Select type']")
    # ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.XPATH_LUS_SELECT_TYPE)
    # ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.XPATH_LUS_TYPE % ustype)
    # using select type from business_logic since this is working
    TBirdCreateLogicalInterconnectGroups.select_create_uplink_set_type(ustype)

    if ustype == "Ethernet":
        # selecting Connection Mode : AUTO or FAILOVER
        if mode == "AUTO":
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_RADIO_AUTO_CONNECTION_MODE)
        if mode == "FAILOVER":
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_RADIO_FAILOVER_CONNECTION_MODE)
        if timer is not "":
            if (timer.lower() == "short (1s)" or timer.lower() == "long (30s)"):
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.XPATH_LUS_LACP_TIMER_SELECT)
                if timer.lower() == "short (1s)":
                    ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_LACP_SHORT_TIMER, PerfConstants.DEFAULT_SYNC_TIME)
                    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LACP_SHORT_TIMER)
                elif timer.lower() == "long (30s)":
                    ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_LACP_LONG_TIMER, PerfConstants.DEFAULT_SYNC_TIME)
                    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LACP_LONG_TIMER)
            else:
                logging._warn("--Invalid LACP timer input : {}".format(timer))

        # Add Networks
        networkList = networks.split(',')
        if len(networkList) > 0:
            # Adding the networks
            for network in networkList:
                if(network != ""):
                    _Add_Netwok_To_Uplink(network, lusname)
            # Select native network
            if(nativenetwork != ""):
                _Select_Given_Network_As_Native_Uplink(nativenetwork, nativenetwork, lusname)
        else:
            logging._warn("No Networks specified in input to add")

        # Add uplink ports
        ethuplinkportList = uplinkethports.split(',')
        if len(ethuplinkportList) > 0:
            for port in ethuplinkportList:
                if (port == ''):
                    break
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_UPLINK_PORTS)
                bayportList = port.split('|')
                bayno = bayportList[0][-1:]
                ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectGroupPage.ID_SEARCH_INPUT_UPLINK_PORT, bayportList[1])

                # select based on bay number and enclosure number if tbird
                selenium2lib.wait_until_page_contains_element(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_UPLINK_PORT)
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_SELECT_TABLE_ADD_PORT % (bayno, bayportList[1]))
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_UPLINK_PORT)

        # Add Preferred port, if mode selected as 'FAILOVER'
        if mode == "FAILOVER":
            prefportList = preferredport.split('|')
            prefbayno = prefportList[0][-1:]
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_CHKBOX_FAILOVER_PREFERRED_PORT % (prefbayno, prefportList[1]))

    elif ustype == "Fibre Channel":
        logging._log_to_console_and_log_file("creating FC uplink set ")
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_UPLINK_LIST)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_FC_UPLINK)

        fcswitchportlist = fcswitchandport.split('|')
        ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_LIST_FC_UPLINK_NETWORKS, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LIST_FC_UPLINK_NETWORKS)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_FC_UPLINK_NETWORK % networks)
        ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_LIST_FC_UPLINK_PORTS, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LIST_FC_UPLINK_PORTS)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_FC_UPLINK_PORT % fcswitchportlist[0][-1:])

        # Add fc uplink ports
        fcswitchportlist = fcswitchandport.split(',')
        if len(fcswitchportlist) > 0:
            for port in fcswitchportlist:
                if (port == ''):
                    break
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_UPLINK_PORTS)
                bayportList = port.split('|')
                bayno = bayportList[0][-1:]
                ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectGroupPage.ID_SEARCH_INPUT_UPLINK_PORT, bayportList[1])
                selenium2lib.wait_until_page_contains_element(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_UPLINK_PORT)
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_SELECT_TABLE_ADD_PORT % (bayno, bayportList[1]))
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_UPLINK_PORT)

        # selecting the port
        fcswitchportlist.pop(0)  # to remove the interconnect switch info from the list.
        for fcport in fcswitchportlist:
            selenium2lib.wait_until_page_contains_element(FusionLogicalInterconnectGroupPage.ID_CHKBOX_BASE % fcport)
            selenium2lib.select_checkbox(FusionLogicalInterconnectGroupPage.ID_CHKBOX_BASE % fcport)

    # click on create
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_CREATE_LOGICAL_UPLINK_TEML)
    if (ui_lib.wait_for_element_visible("xpath=//div[@class='hp-status hp-status-error']")):
        selenium2lib.capture_page_screenshot()
        ui_lib.wait_for_element_and_click("xpath=//a[@class='hp-button hp-cancel']")
        flag_bool = False

    return flag_bool


def _Add_Netwok_To_Uplink(Network, Uplink):
    """ This function is used to add given network to the uplink set """
    """ _Add_Netwok_To_Networkset

        Example:
        | _Add_Netwok_To_Networkset(Network)
    """

    # Loading the library functions
    # selenium2lib = ui_lib.get_s2l()
    # adding networks to given network set
    logging._log_to_console_and_log_file("Adding network %s to Uplink" % Network)
    # Verifying network is already present or not
    if ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_ELEMENT_UPLINK_NETWORK_NAME % Network, PerfConstants.FUSION_PAGE_SYNC):
        logging._log_to_console_and_log_file("Network %s is already added to Uplink" % Network)
        return True
    else:
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_NETWORK_UPLINK_PAGE)
        if not ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_NETWORK_ADD, PerfConstants.FUSION_PAGE_SYNC):
            logging._warn("Add networks to uplink tab is not loaded properly")
            return False
        else:
            if ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_ELEMENT_UPLINK_NETWORK_NAME % Network, PerfConstants.FUSION_PAGE_SYNC):
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_ELEMENT_UPLINK_NETWORK_NAME % Network)
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_NETWORK_EDIT_UPLINK_ADD_NETWORK)
                # Verifying network is successfully added or not
                if ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_ELEMENT_UPLINK_NETWORK_NAME % Network, PerfConstants.FUSION_PAGE_SYNC):
                    logging._log_to_console_and_log_file("Given network %s is successfully added to uplink " % Network)
                    return True
            else:
                logging._warn("Given network %s is not present in the appliance" % Network)
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_NETWORK_CANCEL)
                return False


def _Select_Given_Network_As_Native_Uplink(currentNativeNetwork, newNativeNetwork, lusnewname):
    """ Selecting given network as native """
    """_Select_Given_Network_As_Native

        Example:
        | _Select_Given_Network_As_Native(currentNativeNetwork,newNativeNetwork)
    """
    flag_bool = True
    selenium2lib = ui_lib.get_s2l()
    if newNativeNetwork == "":
        # if no network is needed to select as native unselecting the already selected native naetwork
        if selenium2lib._is_element_present(FusionLogicalInterconnectGroupPage.ID_ELEMENT_UPLINK_NETWORK_NAME % currentNativeNetwork):
            logging._log_to_console_and_log_file("unselecting network %s from native as we provided input make none as native" % currentNativeNetwork)
            selenium2lib.unselect_checkbox(FusionLogicalInterconnectGroupPage.ID_CHECKBOX_NATIVE_NETWORK_UPLINK % currentNativeNetwork)
            logging._log_to_console_and_log_file("network %s unselected from native option" % currentNativeNetwork)
        else:
            logging._warn("given current native Network %s is not present in the uplink set" % currentNativeNetwork)
    else:
        # Verifying the given network is already present or not.If present we will make it as native
        if selenium2lib._is_element_present(FusionLogicalInterconnectGroupPage.ID_ELEMENT_UPLINK_NETWORK_NAME % newNativeNetwork):
            logging._log_to_console_and_log_file("Selecting network %s as native" % newNativeNetwork)
            if ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_CHECKBOX_NATIVE_NETWORK_UPLINK % newNativeNetwork, PerfConstants.FUSION_PAGE_SYNC):
                selenium2lib.select_checkbox(FusionLogicalInterconnectGroupPage.ID_CHECKBOX_NATIVE_NETWORK_UPLINK % newNativeNetwork)
                selenium2lib.select_checkbox(FusionLogicalInterconnectGroupPage.ID_CHECKBOX_NATIVE_NETWORK_UPLINK % newNativeNetwork)
                logging._log_to_console_and_log_file("Selected the network %s as native" % newNativeNetwork)
            else:
                logging._warn("Check box to check the native network is not visible")
        else:
            # Adding network if it is not added
            if (_Add_Netwok_To_Uplink(newNativeNetwork, lusnewname)):
                # Making the network as native if it is successfully added
                if ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_CHECKBOX_NATIVE_NETWORK_UPLINK % newNativeNetwork, PerfConstants.FUSION_PAGE_SYNC):
                    selenium2lib.select_checkbox(FusionLogicalInterconnectGroupPage.ID_CHECKBOX_NATIVE_NETWORK_UPLINK % newNativeNetwork)
                    selenium2lib.select_checkbox(FusionLogicalInterconnectGroupPage.ID_CHECKBOX_NATIVE_NETWORK_UPLINK % newNativeNetwork)
                    logging._log_to_console_and_log_file("Selected the network %s as native" % newNativeNetwork)
                else:
                    logging._warn("Check box to check the native network is not visible")
            else:
                flag_bool = False
    return flag_bool


def edit_logical_interconnect_group_tbird(*lig_obj):
    '''
    Function to edit the LIG from TBIRd
    returns True if edit is successful without any errors else returns error string

    Arguments:
      <lig>
          name*                     --  Name of logical interconnect group as a string.
          interconnecttype          --   Interconnect Type of the Lig
          enclosure_count*          --  Enclosure count as number.
          ibs*                      --  Interconnect bay set count as number.
          redundancy*               --  Possible value: Highly available/Non-redundant (A-side only)/Non-redundant (B-side only)/Redundant
          igmpsnooping*             --  Whether to enable 'IGMP Snooping'. Possible value: true|false.
          igmpidletimeout*          --  IGMP idle timeout interval as integer. This setting will not take effect if igmpsnooping is set to false
          loopprotection*           --  Whether to enable 'Loop protection'. Possible value: true|false.
          internal_networks*        --  Configure internal networks, can be empty which indicate no need to configure internal networks

            <snmp> Optional, for configuring snmp related settings. if not present, use default snmp settings
              syscontact*           --  SNMP System contact as string value.
              readcommunity*        --  SNMP Read community as string value.

            snmpv3enabled**         --  Whether to enable snmpv3 settings, possible value: ENABLED|DISABLED
            adduser                 -- Optional,adds snmpv3 users
            edit_snmpuser           -- Optional,edits existing snmpv3 user
            remove_snmpuser         -- Optional,removes snmpv3 user
              syscontact            --  Optional,SNMP System contact as string value.
              readcommunity         --  Optional,SNMP Read community as string value.
            <add_snmpv3_trapdestination> -- Optional, for adding snmpv3 trap destination. Accept multiple nodes.
            <edit_snmpv3_trapdestination> -- Optional, for editing snmpv3 trap destination. Accept multiple nodes.
            <remove_snmpv3_trapdestination> -- Optional, for removing snmpv3 trap destination. Accept multiple nodes.
                trapdestination**    --  Trap destination. e.g. 192.168.1.2
                trapformat           --  Trap Format. Possible value: SNMPv1|SNMPv2|SNMPv3
                notification_type**  -- Whether to enable notification type, Possible value : TRAP|INFORM.Applicable only for Trap Format snmpv3.
                snmp_user            -- Optional,to choose the snmpv3 user. If not, default user will be selected.Applicable only for Trap Format snmpv3.
                communitystring      --  Optional,Community string as string value. Applicable only for Trap Formats snmpv1 and snmpv2.

    * Required Arguments

    ** Required Arguments for OVF292
    Example:   Potash_payload
        data/ligs -> @{TestData.ligs}

    **<ligs_snmpv3>
    <lig>
   <snmp snmpv3enabled="enabled" syscontact="None" >
                    <adduser username= "user6"
                      security_level="authenticationandprivacy" auth_protocol="MD5"
                      authentication_password="Password1" confirm_auth_password="Password1"
                      priv_protocol="AES-192" privacy_password="Password2"
                      confirm_priv_password="Password2"></adduser>
                    <add_snmpv3_trapdestination trapdestination= "10.101.11.14"  trapformat="snmpv3" notification_type="trap"  snmp_user="user5" ></add_snmpv3_trapdestination>
                    </snmp>
                **<snmp snmpv1v2enabled="disabled" syscontact="None" readcommunity="public">
                  <adduser username= "user1"  security_level="none" ></adduser>
                  </snmp>
            </lig>
        </ligs_snmp>
    ** Applicable only for feature toggle in OVF292

    '''

    logging._log_to_console_and_log_file("\n*** Edit logical interconnect group for TBird***\n")
    selenium2lib = ui_lib.get_s2l()

    errors_on_form = None
    error_status = None
    error = 0
    error_string = ''

    ic_data = {}

    if not selenium2lib._is_element_present(FusionLogicalInterconnectGroupPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element_visible(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()

    if isinstance(lig_obj, test_data.DataObj):
        lig_obj = [lig_obj]
    elif isinstance(lig_obj, tuple):
        lig_obj = list(lig_obj[0])

    for lig in lig_obj:
        # if the lig type is not Tbird skip creation
        if str(lig.type).lower() != "tbird":
            logging._warn("The LIG type specified is not 'tbird' and is '{}'.Skipping creation".format(lig.type))
            continue

        ic_data.clear()
        ibs = int(lig.ibs)
        ic_type_a = ""
        ic_type_b = ""

        ''' Find out the ic types in each enclosure '''
        # add the enclosure number and the IC types for the enclosure in the dictionary
        if hasattr(lig, "switch"):
            for ic in lig.switch:  # lig.ic:
                ic_data[ic.enc] = ic.type

        # skip this LIG edit  if LIG is not present
        if not ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.XPATH_LIG_TABLE_ELEMENT % lig.name, PerfConstants.DEFAULT_SYNC_TIME):
            logging._warn("LIG '{0}' is not present".format(lig.name))
            continue

        # Click edit link and  type LIG name
        logging._log_to_console_and_log_file("\nEditing LIG : {}".format(lig.name))

        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.XPATH_LIG_NAME % lig.name)
        # privilege check - if user does not have privilege break out of the loop
        if ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_ACTION_MAIN_BTN, PerfConstants.DEFAULT_SYNC_TIME):
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_ACTION_MAIN_BTN)
            if not ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_MENU_ACTION_LST_EDIT):
                logging._warn("Edit link not seen in actions menu in UI!! User may not have edit privilege.")
                error += 1
                error_string += "Edit link not seen in actions menu in UI!! User may not have edit privilege.\t"
                break
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_MENU_ACTION_LST_EDIT)
            ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_LIG_EDIT_FORM, PerfConstants.DEFAULT_SYNC_TIME)
        else:
            logging._warn("Actions Button is not seen in UI!! USer may not have edit privileges")
            error += 1
            error_string += "Actions Button is not seen in UI!! USer may not have edit privileges\t"
            break

        # type new name if provided
        ligname = ""
        if hasattr(lig, "newname"):
            if str(lig.newname).strip() != "":
                ligname = lig.newname
            else:
                ligname = lig.name
        else:
            ligname = lig.name

        # provide name
        ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectGroupPage.ID_LIG_EDIT_NAME, ligname)

        # edit internal network
        logging._log_to_console_and_log_file("-\n---Editing internal networks in LIG ---\n")
        add_internal_netowrks = None
        if hasattr(lig, 'internalnetwork'):
            add_internal_netowrks = lig.internalnetwork
            if add_internal_netowrks is None:
                logging._warn("--No Internal Networks to edit")
            if isinstance(add_internal_netowrks, (list)):
                logging._log_to_console_and_log_file("-\n---Editing internal networks in LIG---")
                for internal_network in add_internal_netowrks:
                    if not _add_internal_network(internal_network):
                        logging._warn("Error While editing internal network {}".format(internal_network.name))
                        error += 1
                        error_string += "Error While editing internal network {}\t".format(internal_network.name)
                logging._log_to_console_and_log_file("-\n---Editing internal networks in LIG completed---\n")
        else:
            logging._warn("--No Internal Networks to edit")

        # remove logical uplink set - if any
        logging._log_to_console_and_log_file("\n--Removing Uplink Sets--\n")
        removelus = None
        if hasattr(lig, 'removelus'):
            removelus = lig.removelus
            if removelus is None:
                logging._warn("--There are no Logical Uplink Sets to remove in input")
            if isinstance(removelus, (list)):
                # ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_INPUT_NAME_LST)
                for lus in removelus:
                    ui_lib.scroll_into_view(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_LOGICAL_UPLINK_TEMPLATE)
                    if not _remove_lus_from_edit_lig(lus):
                        logging._warn("Error While removing Logical Uplink Set {}".format(lus.name))
                        error += 1
                        error_string += "Error While removing Logical Uplink Set {}\t".format(lus.name)
        else:
            logging._warn("--No Logical Uplink Sets to remove specified in input")

        # edit interconnects
        if ic_data:
            logging._log_to_console_and_log_file("\n--Selecting Interconnects--\n")
            select_interconnect_status = _select_interconnect_tbird(int(lig.enccount), int(lig.ibs), ic_data)
            if select_interconnect_status:
                logging._warn("--Error while selecting interconnects--\n")
                error += 1
                error_string += select_interconnect_status
            else:
                logging._log_to_console_and_log_file("\n--Interconnects Selected Successfully--\n")

        # edit logical uplink set - if any
        logging._log_to_console_and_log_file("\n--Editing Uplink Sets--\n")
        editlus = None
        if hasattr(lig, 'editlus'):
            editlus = lig.editlus
            if editlus is None:
                logging._warn("There are no Logical Uplink Sets to edit in input")
            if isinstance(editlus, (list)):
                # ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_INPUT_NAME_LST)
                for lus in editlus:
                    ui_lib.scroll_into_view(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_LOGICAL_UPLINK_TEMPLATE)
                    if not edit_lus_to_edit_lig(lus):
                        logging._warn("Error While editing Logical Uplink Set {}".format(lus.name))
                        error += 1
                        error_string += "Error While editing Logical Uplink Set {}\t".format(lus.name)
        else:
            logging._warn("No  Logical Uplink Sets to edit specified in input")

        # add logical uplink set - if any
        logging._log_to_console_and_log_file("\n--Adding Uplink Sets--\n")
        addlus = None
        if hasattr(lig, 'addlus'):
            addlus = lig.addlus
            if addlus is None:
                logging._warn("There are no Logical Uplink Sets to add in input")
            if isinstance(addlus, (list)):
                # ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_INPUT_NAME_LST)
                for lus in addlus:
                    ui_lib.scroll_into_view(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_LOGICAL_UPLINK_TEMPLATE)
                    if not _add_lus_to_lig(lus):
                        logging._warn("Error While adding Logical Uplink Set {}".format(lus.name))
                        error += 1
                        error_string += "Error While adding Logical Uplink Set {}\t".format(lus.name)
        else:
            logging._warn("No  Logical Uplink Sets to add specified in input")

        # Code to edit interconnect settings
        if _add_interconnect_settings(lig):
            logging._log_to_console_and_log_file("\n--Interconnect Settings Set successfully---\n")
        else:
            logging._warn("Error While editing interconnect settings\n")
            error += 1
            error_string += "Error While editing interconnect settings\t"

        # set snmp system contact and read community
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LIG_EDIT_PANEL_SELECTOR)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.LINK_LIG_SNMP, PerfConstants.DEFAULT_SYNC_TIME)

        if hasattr(lig, "syscontact"):
            if lig.syscontact.lower().strip() not in ("", None, "none"):
                ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectGroupPage.ID_LIG_SYSTEM_CONTACT, lig.syscontact)
        else:
            logging._warn("No system contact to be added")

        if hasattr(lig, "readcommunity"):
            if lig.readcommunity.lower().strip() not in ("", None, "none"):
                ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectGroupPage.ID_LIG_READ_COMMUNITY, lig.readcommunity)
        else:
            logging._warn("No read community to be added")

        # Code to edit snmp- This is applicable only for feature toggle in OVF292
        if hasattr(lig, 'snmp'):
            _edit_lig_config_snmp_tbird(lig.snmp)

        # CODE TO EDIT TRAP destinations
        addtraps = None
        if hasattr(lig, 'addtrapdest'):
            addtraps = lig.addtrapdest
            if addtraps is None:
                logging._warn("There are no Trap Destinations to be added/edited")
            if isinstance(addtraps, (list)):
                for trap in addtraps:
                    trap_status = None
                    trap_status = _add_trap_to_lig_tbird(trap)
                    if trap_status:
                        logging._warn("Error While editing Trap destination {}".format(trap.ip))
                        error += 1
                        error_string += "Error While editing Trap destination {}\t".format(trap.ip) + trap_status + "\t"
                    else:
                        logging._log_to_console_and_log_file("Trap '{}' added successfully".format(trap.ip))
        else:
            logging._warn("There are no Trap Destinations to be edited")

        # Click OK
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LIG_EDIT_FORM_OK)
        ui_lib.wait_for_element_notvisible(FusionLogicalInterconnectGroupPage.ID_LIG_EDIT_FORM, timeout=20)

        logging._log_to_console_and_log_file("\nChecking For errors on form...")
        # check for errors
        errors_on_form = base_page.get_errors_on_form(FusionLogicalInterconnectGroupPage.ID_LIG_EDIT)
        # check if any status errors are seen
        error_status = ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.XPATH_EG_EDIT_HP_STATUS_ERROR)
        if error_status or errors_on_form:
            error += 1
            if errors_on_form:
                error_string += errors_on_form + "\t"
            if error_status:
                logger._warn("Error Summary - {}".format(ui_lib.get_text(FusionLogicalInterconnectGroupPage.XPATH_EG_EDIT_FORM_MESSAGE_SUMMARY)))
                logger._warn("Error Details - {}".format(ui_lib.get_text(FusionLogicalInterconnectGroupPage.XPATH_EG_EDIT_FORM_MESSAGE_DETAILS)))
                error_string += ui_lib.get_text(FusionLogicalInterconnectGroupPage.XPATH_EG_EDIT_FORM_MESSAGE_SUMMARY) + "." + ui_lib.get_text(FusionLogicalInterconnectGroupPage.XPATH_EG_EDIT_FORM_MESSAGE_DETAILS) + "\t"
            # if add form is still seen click cancel
            if ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_LIG_EDIT_FORM):
                logger._log_to_console_and_log_file("Clicking Cancel")
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LIG_EDIT_CANCEL)
            continue
        else:
            logger._log_to_console_and_log_file("- No errors Seen")

        # wait for creation to complete
        timeout = 1
        while timeout <= FusionLogicalInterconnectGroupPage.TIMEOUT:
            logger._log_to_console_and_log_file("Edit operation in progress...")
            if ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.XPATH_UPDATE_COMPLETE, FusionLogicalInterconnectGroupPage.UPDATE_WAIT_TIME):
                logger._log_to_console_and_log_file("Edit Completed.\n")
                break
            elif ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.XPATH_UPDATE_STATUS_WARNING, FusionLogicalInterconnectGroupPage.UPDATE_WAIT_TIME):
                logger._warn("Edit Completed but with warning")
                break
            elif ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.XPATH_UPDATE_STATUS_ERROR, FusionLogicalInterconnectGroupPage.UPDATE_WAIT_TIME):
                logger._warn("--Error during Edit/Updation")
                error += 1
                error_string += "--Error during Edit/Updation\t"
                break
            timeout += (FusionLogicalInterconnectGroupPage.UPDATE_WAIT_TIME * 3) / 60.0

        if timeout > FusionLogicalInterconnectGroupPage.TIMEOUT:
            logger._warn("Either Edit of LIG '{}' has not completed or update Alert is not seen , even after waiting for {} minutes!!".format(ligname, timeout))
            error += 1
            error_string += "Either Edit  of LIG '{}'  has not completed or update Alert is not seen , even after waiting for {} minutes!!\t".format(ligname, timeout)
            # if edit form is still seen click cancel
            if ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_LIG_EDIT_FORM):
                logger._log_to_console_and_log_file("Clicking Cancel")
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LIG_EDIT_CANCEL)

        if not ui_lib.table_contains(FusionLogicalInterconnectGroupPage.ID_LIG_TABLE, ligname):
            logging._warn("LIG '{0}' is not seen in UI".format(ligname))
            error += 1
            error_string += "LIG '{0}' is not seen in UI".format(ligname)
        else:
            logging._log_to_console_and_log_file("LIG '{0}' is seen in UI".format(ligname))

    # if edit form is still visible
    if ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_LIG_EDIT_FORM):
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LIG_EDIT_CANCEL)
        ui_lib.wait_for_element_notvisible(FusionLogicalInterconnectGroupPage.ID_LIG_EDIT_FORM, timeout=30)

    # if error - return error strings else return true
    if error > 0:
        return error_string
    else:
        return True


def _remove_lus_from_edit_lig(lus):
    """ This function will remove the given uplink set from existing logical interconnect group. """
    """_remove_lus_from_edit_lig

        Example:
        |_remove_lus_from_edit_lig(lus)
    """
    flag_bool = True
    logging._log_to_console_and_log_file("function call to remove uplink set - %s " % lus.name)
    selenium2lib = ui_lib.get_s2l()
    if selenium2lib._is_element_present(FusionLogicalInterconnectGroupPage.ID_BTN_REMOVE_UPLINK_SET_NAME % lus.name):
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_REMOVE_UPLINK_SET_NAME % lus.name)
        if not selenium2lib._is_element_present(FusionLogicalInterconnectGroupPage.ID_BTN_REMOVE_UPLINK_SET_NAME % lus.name):
            logging._log_to_console_and_log_file("Given uplink set %s is deleted from the LIG successfully" % lus.name)
        else:
            flag_bool = False
            logging._log_to_console_and_log_file("Unable to delete the uplink set %s from the given LIG" % lus.name)

    elif selenium2lib._is_element_present(FusionLogicalInterconnectGroupPage.ID_BTN_REMOVE_UPLINK_SET_NAME_DIV % lus.name):
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_REMOVE_UPLINK_SET_NAME_DIV % lus.name)
        if not selenium2lib._is_element_present(FusionLogicalInterconnectGroupPage.ID_BTN_REMOVE_UPLINK_SET_NAME_DIV % lus.name):
            logging._log_to_console_and_log_file("Given uplink set %s is deleted from the LIG successfully" % lus.name)
        else:
            flag_bool = False
            logging._log_to_console_and_log_file("Unable to delete the uplink set %s from the given LIG" % lus.name)
    else:
        logging._log_to_console_and_log_file("Given uplink set %s is not present in the LIG" % lus.name)
    return flag_bool


def edit_lus_to_edit_lig(editLus):
    """ This function will edit the given logical uplink set of existing logical interconnect group. """
    """ edit_lus_to_edit_lig

        Example:
        | edit_lus_to_edit_lig(editLus)
    """
    flag_bool = True
    logging._log_to_console_and_log_file("----- function call to edit uplink Set %s " % editLus.name)
    # filling values in UI as supplied via xml data sheet
    selenium2lib = ui_lib.get_s2l()

    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LINK_LIG_EDIT)
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_SELECT_LIG_EDIT)

    # While editing the newly added LIG it will be identified as add only and While editing the existing LIG it will be identified as edit.
    # Editing the LIG newly added.
    if(ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_LUS_SELECT_TO_ADD_EDIT % editLus.name, PerfConstants.FUSION_PAGE_SYNC)):
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LUS_SELECT_TO_ADD_EDIT % editLus.name)
        # function to add uplink set
        if((editLus.networkType).upper() == "ETHERNET"):
            flag_bool = _edit_logical_uplink_set_Ethernet(editLus.name, editLus.newname, editLus.connectionMode, editLus.networkstoadd, editLus.networkstodelete, editLus.currentNative, editLus.newNnative, editLus.addports, editLus.removeports, editLus.preferredPort)
        elif(((editLus.networkType).upper() == "FIBRE_CHANNEL") or ((editLus.networkType).upper() == "FIBRECHANNEL") or ((editLus.networkType).upper() == "FIBRE CHANNEL")):
            if hasattr(editLus, 'PortSpeed'):
                flag_bool = _edit_logical_uplink_set_FC(editLus.name, editLus.newname, editLus.network, editLus.PortstoAdd, editLus.PortstoRemove, editLus.PortSpeed)
            else:
                flag_bool = _edit_logical_uplink_set_FC(editLus.name, editLus.newname, editLus.network, editLus.PortstoAdd, editLus.PortstoRemove)
        else:
            flag_bool = False
            logging._log_to_console_and_log_file("Provided invalid network type. provided value is %s " % editLus.networkType)

    # Editing the LIG added previously.
    elif(ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_LUS_SELECT_TO_EDIT_LABEL % editLus.name, PerfConstants.FUSION_PAGE_SYNC)):
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LUS_SELECT_TO_EDIT_LABEL % editLus.name)
        # function to add uplink set
        ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_LUS_TYPE, PerfConstants.FUSION_PAGE_SYNC)
        network_Type = selenium2lib.get_text(FusionLogicalInterconnectGroupPage.ID_LUS_TYPE)
        if "Ethernet" in str(network_Type):
            flag_bool = _edit_logical_uplink_set_Ethernet(editLus.name, editLus.newname, editLus.connectionMode, editLus.networkstoadd, editLus.networkstodelete, editLus.currentNative, editLus.newNnative, editLus.addports, editLus.removeports, editLus.preferredPort)
        elif "Fibre Channel" in str(network_Type):
            if hasattr(editLus, 'PortSpeed'):
                flag_bool = _edit_logical_uplink_set_FC(editLus.name, editLus.newname, editLus.network, editLus.PortstoAdd, editLus.PortstoRemove, editLus.PortSpeed)
            else:
                flag_bool = _edit_logical_uplink_set_FC(editLus.name, editLus.newname, editLus.network, editLus.PortstoAdd, editLus.PortstoRemove)
        else:
            flag_bool = False
            logging._log_to_console_and_log_file("Provided invalid network type. provided value is %s " % editLus.networkType)

    # To handle different Objects to identify edit.
    # Editting the LIG added previously.
    elif(ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_LUS_SELECT_TO_EDIT_DIV % editLus.name, PerfConstants.FUSION_PAGE_SYNC)):
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LUS_SELECT_TO_EDIT_DIV % editLus.name)
        # function to add uplink set
        ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_LUS_TYPE, PerfConstants.FUSION_PAGE_SYNC)
        network_Type = selenium2lib.get_text(FusionLogicalInterconnectGroupPage.ID_LUS_TYPE)
        if "Ethernet" in str(network_Type):
            flag_bool = _edit_logical_uplink_set_Ethernet(editLus.name, editLus.newname, editLus.connectionMode, editLus.networkstoadd, editLus.networkstodelete, editLus.currentNative, editLus.newNnative, editLus.addports, editLus.removeports, editLus.preferredPort)
        elif "Fibre Channel" in str(network_Type):
            flag_bool = _edit_logical_uplink_set_FC(editLus.name, editLus.newname, editLus.network, editLus.PortstoAdd, editLus.PortstoRemove)
        else:
            logging._log_to_console_and_log_file("Provided invalid network type. provided value is %s " % editLus.networkType)
    else:
        flag_bool = False
        logging._warn("uplink set %s is not present in the appliance" % editLus.name)

    s = "-----Edit Uplink Set name %s " % editLus.name
    if (editLus.has_property("negative")):
        if (flag_bool):
            logging._log_to_console_and_log_file(s + "did not fail.  Failure expected.")
            return False
        else:
            logging._log_to_console_and_log_file(s + "failed as expected.")
            return True
    else:
        if (flag_bool):
            logging._log_to_console_and_log_file(s + "succeeded.")
            return True
        else:
            logging._log_to_console_and_log_file(s + "failed ")
            return False


def _edit_logical_uplink_set_Ethernet(lusname, lusnewname, Mode, networkstoadd, networkstodelete, currentNative, newNative, addports, removeports, preferredPort, timer="short (1s)"):
    """ This function will edit the given ethernet logical uplink set of the existing logical interconnect group. """
    """_edit_logical_uplink_set_Ethernet

        Example:
        | _edit_logical_uplink_set_Ethernet(currentNativeNetwork,newNativeNetwork)
    """
    flag_bool = True
    logging._log_to_console_and_log_file("--adding inputs to Logical Uplink Set")
    selenium2lib = ui_lib.get_s2l()

    ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectGroupPage.ID_INPUT_UPLINK_NAME, lusnewname)
    logging._log_to_console_and_log_file("Given uplink is renamed to %s" % lusnewname)

    # selecting Connection Mode : AUTO or FAILOVER
    if Mode == "AUTO":
        selenium2lib.select_checkbox(FusionLogicalInterconnectGroupPage.ID_RADIO_AUTO_CONNECTION_MODE)
        logging._log_to_console_and_log_file("Uplink mode is changed to 'AUTO'")
    if Mode == "FAILOVER":
        selenium2lib.select_checkbox(FusionLogicalInterconnectGroupPage.ID_RADIO_FAILOVER_CONNECTION_MODE)
        logging._log_to_console_and_log_file("Uplink mode is changed to 'FAILOVER'")

    if (timer.lower() == "short (1s)" or timer.lower() == "long (30s)"):
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.XPATH_LUS_LACP_TIMER_SELECT)
        if timer.lower() == "short (1s)":
            ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_LACP_SHORT_TIMER, PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LACP_SHORT_TIMER)
        elif timer.lower() == "long (30s)":
            ui_lib.wait_for_element_visible(FusionLogicalInterconnectGroupPage.ID_LACP_LONG_TIMER, PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_LACP_LONG_TIMER)
    else:
        logging._warn("--Invalid LACP timer input : {}".format(timer))

    # Add Networks
    if(networkstoadd != ""):
        networkList = networkstoadd.split(',')
        for network in networkList:
            if(network != ""):
                if not(_Add_Netwok_To_Uplink(network, lusnewname)):
                    flag_bool = False
    else:
        logger._log_to_console_and_log_file("--No new Networks to ADD")

    # Delete Networks
    if(networkstodelete != ""):
        logging._log_to_console_and_log_file("Networks to delete : %s" % networkstodelete)
        networkList = networkstodelete.split(',')
        for network in networkList:
            if selenium2lib._is_element_present(FusionLogicalInterconnectGroupPage.ID_ELEMENT_UPLINK_NETWORK_NAME % network):
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_ELEMENT_DELETE_NETWORK_LOGICAL_UPLINK % network)
                if selenium2lib._is_element_present(FusionLogicalInterconnectGroupPage.ID_ELEMENT_UPLINK_NETWORK_NAME % network):
                    flag_bool = False
                    logging._warn("Deleting network %s is failed" % network)
                else:
                    logging._log_to_console_and_log_file("Network %s got deleted successfully" % network)
            else:
                logging._log_to_console_and_log_file("Network %s is not present in the given networkset" % network)
    else:
        logging._log_to_console_and_log_file("--No networks to delete")

    # Selecting native network
    _Select_Given_Network_As_Native_Uplink(currentNative, newNative, lusnewname)

    # Add uplink ports
    if(addports != ""):
        ethuplinkportList = addports.split(',')
        for port in ethuplinkportList:
            bayportList = port.split('|')
            bayno = bayportList[0][-1:]
            if (ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_ELEMENT_DELETE_PORT_UPLINK % (bayno, bayportList[1]), 5)):
                logging._warn("port %s is already present in the Uplink" % port)
            else:
                logging._log_to_console_and_log_file("Adding port %s to given Uplink" % port)
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_UPLINK_PORTS)
                if(ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_UPLINK_PORT, PerfConstants.FUSION_PAGE_SYNC)):
                    ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectGroupPage.ID_SEARCH_INPUT_UPLINK_PORT, bayportList[1])
                    if(ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_SELECT_TABLE_ADD_PORT % (bayno, bayportList[1]), PerfConstants.FUSION_PAGE_SYNC)):
                        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_SELECT_TABLE_ADD_PORT % (bayno, bayportList[1]))
                        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_ADD_UPLINK_PORT)
                        if ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_ELEMENT_DELETE_PORT_UPLINK % (bayno, bayportList[1]), PerfConstants.FUSION_PAGE_SYNC):
                            logging._log_to_console_and_log_file("port %s is added to Uplink successfully" % port)
                    else:
                        flag_bool = False
                        logging._warn("given port %s is not present in the appliance" % port)
                else:
                    flag_bool = False
                    ui_lib.fail_test("Add port page is not opened after clicking on 'add ports' button", False)

    # remove uplink ports
    if(removeports != ""):
        ethuplinkportList = removeports.split(',')
        for port in ethuplinkportList:
            logging._log_to_console_and_log_file("removing Uplink Port %s" % port)
            bayportList = port.split('|')
            bayno = bayportList[0][-1:]
            if(ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_ELEMENT_DELETE_PORT_UPLINK % (bayno, bayportList[1]), PerfConstants.FUSION_PAGE_SYNC)):
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_ELEMENT_DELETE_PORT_UPLINK % (bayno, bayportList[1]))
            else:
                logging._warn("Given port %s is not present in the uplink." % port)

    # Add Preferred port, if mode selected as 'FAILOVER'
    if Mode == "FAILOVER":
        if(preferredPort != ""):
            prefportList = preferredPort.split('|')
            prefbayno = prefportList[0][-1:]
            if(ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_CHKBOX_FAILOVER_PREFERRED_PORT % (prefbayno, prefportList[1]), PerfConstants.FUSION_PAGE_SYNC)):
                selenium2lib.select_checkbox(FusionLogicalInterconnectGroupPage.ID_CHKBOX_FAILOVER_PREFERRED_PORT % (prefbayno, prefportList[1]))
                logging._log_to_console_and_log_file("Selected %s port as preferred" % preferredPort)
            else:
                flag_bool = False
                logging._warn("Given port %s is not present in the uplink." % preferredPort)

    # click on create
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_CREATE_LOGICAL_UPLINK_TEML)
    if (ui_lib.wait_for_element_visible("xpath=//div[@class='hp-status hp-status-error']")):
        selenium2lib.capture_page_screenshot()
        ui_lib.wait_for_element_and_click("xpath=//a[@class='hp-button hp-cancel']")
        flag_bool = False
    return flag_bool


def _edit_logical_uplink_set_FC(lusname, lusnewname, network, PortstoAdd, PortstoRemove, PortSpeed=None):
    """ This function is used to edit the FC uplink set """
    """_edit_logical_uplink_set_FC

        Example:
        | _edit_logical_uplink_set_FC(lusname, lusnewname, network, PortstoAdd, PortstoRemove)
        prerequisite: edit uplink page should be already opened.
    """
    flag_bool = True
    logging._log_to_console_and_log_file("adding inputs to Logical Uplink Set")
    selenium2lib = ui_lib.get_s2l()
    ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectGroupPage.ID_INPUT_UPLINK_NAME, lusnewname)
    logging._log_to_console_and_log_file("Uplink set is renamed to %s" % lusnewname)

    if(ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_INPUT_FC_NETWORK, PerfConstants.FUSION_PAGE_SYNC)):
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_COMBO_DROPDOWN_UPLINK_SET)
        if selenium2lib._is_element_present("xpath=//div/a[text()='Search for another']"):
            ui_lib.wait_for_element_and_click("xpath=//div/a[text()='Search for another']")
        if (ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_ELEMENT_COMBO_DROPDOWN_UPLINK_SET % network, PerfConstants.FUSION_PAGE_SYNC)):
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_ELEMENT_COMBO_DROPDOWN_UPLINK_SET % network)

            if(PortstoAdd != ""):
                portdata = PortstoAdd.split(',')
                for port in portdata:
                    data = port.split(':')
                    ui_lib.wait_for_element_and_click("xpath=//*[@id='cic-switch-template-dialog-uplinks']/li[4]/div/div/div[2]")
                    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_ELEMENT_COMBO_FC_UPLINK_SET_PORT % data[0])
                    if ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_CHKBOX_BASE % data[1]):
                        selenium2lib.select_checkbox(FusionLogicalInterconnectGroupPage.ID_CHKBOX_BASE % data[1])
                    else:
                        flag_bool = False
                        logging._warn("Given port %s is already used or not present in the given interconnect" % network)

            if(PortstoRemove != ""):
                portdata = PortstoRemove.split(',')
                for port in portdata:
                    data = port.split(':')
                    ui_lib.wait_for_element_and_click("xpath=//*[@id='cic-switch-template-dialog-uplinks']/li[4]/div/div/div[2]")
                    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_ELEMENT_COMBO_FC_UPLINK_SET_PORT % data[0])
                    selenium2lib.wait_until_page_contains_element(FusionLogicalInterconnectGroupPage.ID_CHKBOX_BASE % data[1])
                    if ui_lib.wait_for_element(FusionLogicalInterconnectGroupPage.ID_CHKBOX_BASE % data[1]):
                        selenium2lib.unselect_checkbox(FusionLogicalInterconnectGroupPage.ID_CHKBOX_BASE % data[1])
                    else:
                        logging._log_to_console_and_log_file("Given port %s is already deleted or not present in the given interconnect" % network)

            if PortSpeed is not None:
                portdata = PortSpeed.split(',')
                for port in portdata:
                    data = port.split('|')
                    logger.info("data is %s" % data)
                    bay_no = data[0][-1]
                    port_name = data[1]
                    port_speed = data[2]
                    if not EditLogicalInterconnectGroups.select_create_uplink_set_fc_port_speed(bay_no, port_name, port_speed):
                        flag_bool = False
                    else:
                        logger.info("Successfully edited the port speed")
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_CREATE_LOGICAL_UPLINK_TEML)
        else:
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectGroupPage.ID_BTN_CANCEL_UPLINK_PORT)
            flag_bool = False
            logging._warn("Given network %s is not availabe in the appliance." % network, False)
        return flag_bool


def validate_qos_configuration(lig_obj):
    """ validate_qos_configuration

    Arguments:
      <lig>
          name*                     --  Name of logical interconnect group as a string.
          verifytype*               -- to verify the QoS type in LIG possible values:Passthrough/Custom (with FCoE lossless)|Custom (without FCoE lossless)
          verifyfcoe*               -- To verify if fcoelossless class is available in Custom (with FCoE lossless) type
          qos_configuration_type*   --  Possible value: Passthrough/Custom (with FCoE lossless)|Custom (without FCoE lossless)
          classname*                --  name of the class possible value:FCoE lossless
          qos_type                  --  Possible value: Passthrough/Custom (with FCoE lossless)|Custom (without FCoE lossless)
          verifyingpassthroughoptions* --  To verify the option for QoS type Passthrough possible value:none
                  sharevalue*               -- Possible values: Between 1 and 100
                  egresspriority*            -- Possible values: from 0 to 7
                  dot1pvalue*                -- Possible values: 0 to 5
                  dscpvalue*                -- Possible values:DSCP_10_AF11,DSCP_10_AF11, DSCP_0_CS0, DSCP_12_AF12, DSCP_14_AF13, DSCP_8_CS1
          dot1p_priority             --    Specifies the dot1p priority value to remark for the egressing packets. This provides flexibility to control priority treatment for packets at the next hops based on the remarked dot1p value
    * Required Arguments

    Example:
        data/ligs -> @{TestData.ligs}
        <ligs>
            <lig  name="LIG-wpst32"
                 verifytype = "Custom (with FCoE lossless)"
                 verifyfcoe ="None"
                  QoS = "passthrough"
                 qos_configuration_type = "Custom (with FCoE lossless)"
                 qos_type="Custom (with FCoE lossless)"
                 verifyingpassthroughoptions="None"
                                 sharevalue = "1,3,6,9,12,15"
                                 egresspriority = "0, 1, 3, 4, 6, 7"
                                 dot1pvalue = "0,1,2,3,4,5"
                                 dscpvalue = "DSCP_10_AF11,DSCP_10_AF11, DSCP_0_CS0, DSCP_12_AF12, DSCP_14_AF13, DSCP_8_CS1" dot1p_dscp_mappings="2,4,6,8,10,12,14,16"
            </lig>
        </ligs>
     Example for attribute "dot1p_priority":
       data/ligs -> @{TestData.ligs}
        <ligs>
            <lig  name="LIG-wpst32"
                qos_configuration_type = "Custom (with FCoE lossless)"
                classname="Class3"
                classEnable="Enabled/Disabled"
                dot1p_priority="1,2,4,5,6,7"
       </lig>
        </ligs>
    """
    navigate()
    logger.info("verifyimg QoS values on Logical Interconnect Groups...")

    count = 0

    total_len = len(lig_obj)
    for n, lig in enumerate(lig_obj):
        # check if LIG is existing
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total_len, '-' * 14))
        logger.info("Editing a LIG with name '{0}'".format(lig.name))
        if C7000VerifyLogicalInterconnectGroups.verify_lig_exist(lig.name, fail_if_false=False) is False:
            logger.warn("LIG '{0}' not exists".format(lig.name))
            ui_lib.fail_test("LIG not exists")
        # select LIG
        if select_logical_interconnect_group(lig.name) is False:
            ui_lib.fail_test("LIG not selected")
        C7000EditLogicalInterconnectGroups.select_actions_edit()
        C7000EditLogicalInterconnectGroups.wait_edit_lig_dialog_shown()
        FusionUIBase.select_view_by_name('Quality of Service')
        if hasattr(lig, 'verifytype'):
            EditLogicalInterconnectGroups.verify_quality_of_service_qos_configuration_type(lig.verifytype)
        if hasattr(lig, 'verifyfcoe'):
            logger.info("Verifying FCoE lossless")
            C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_configuration_type)
            if C7000EditLogicalInterconnectGroups.verify_fcoelosssless_class_exists(lig.classname):
                logger.info("FCoE lossless class is available in QoS customWithFCoE")
                if not C7000EditLogicalInterconnectGroups.verify_fcoe_lossless_class_no_edit_option(lig.classname):
                    ui_lib.fail_test("Unexpected behaviour EDIT option is  available")
                logger.info("As expected unable to edit FCoElossless class EDIT option is not available")
            else:
                C7000EditLogicalInterconnectGroups.click_cancel_button()
                ui_lib.fail_test("FCoE lossless class is not available in QoS customWithFCoE")
            C7000EditLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_type)
            if C7000EditLogicalInterconnectGroups.verify_fcoelosssless_class_exists(lig.classname, fail_if_false=False):
                C7000EditLogicalInterconnectGroups.click_cancel_button()
                ui_lib.fail_test("FCoE lossless class is available in QoS customWithoutFCoE")
            else:
                logger.info("FCoE lossless name is not available")
        if hasattr(lig, 'verifyingeditoption'):
            logger.info("Navigate to edit option")
            values_list = []
            C7000EditLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_type)
            share = C7000EditLogicalInterconnectGroups.get_fcoeshare()
            maxshare = C7000EditLogicalInterconnectGroups.get_fcoemaxshare()
            values_list.append(share)
            values_list.append(maxshare)
            logger.info("list value is % s" % values_list)
            C7000EditLogicalInterconnectGroups.click_cancel_button()
            return values_list
        if hasattr(lig, 'verifyingpassthroughoptions'):
            logger.info("Verifying Passthroughoptions in Quality of Service view...")
            if C7000VerifyLogicalInterconnectGroups.verify_passthrough_options():
                logger.info("verified passthrough options does not exist as expected")
            else:
                C7000EditLogicalInterconnectGroups.click_cancel_button()
                ui_lib.fail_test("verified passthrough options does exist")
        if hasattr(lig, 'mappings'):
            C7000EditLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_type)
            class_list = [item.strip() for item in lig.classname.split(',')]
            nomapping_list = [item.strip() for item in lig.clasnosmapping.split(',')]
            mapping_list = [item.strip() for item in lig.mappings.split(',')]
            for class1 in class_list:
                EditLogicalInterconnectGroups.select_editoption(class1)
                EditLogicalInterconnectGroups.click_qos_class(fail_if_false=False)
                EditLogicalInterconnectGroups.input_share_values(lig.sharevalue)
                EditLogicalInterconnectGroups.tick_dot1p_values(lig.dot1pvalues)
                EditLogicalInterconnectGroups.tick_dscp_values(lig.dscpvalues)
                EditLogicalInterconnectGroups.click_class_ok_button()
                EditLogicalInterconnectGroups.select_classname(class1)
                for value in mapping_list:
                    if value != "No mappings":
                        if C7000VerifyLogicalInterconnectGroups.verify_mappings_visibility(value):
                            logger.info(" Sucessfully verifying DOT1P and DSCP values for  %s" % class1)
                        else:
                            ui_lib.fail_test(" failed verifying DOT1P and DSCP values")
            for class1 in nomapping_list:
                EditLogicalInterconnectGroups.select_classname(class1)
                for value in mapping_list:
                    if value == "No mappings":
                        logger.info("value is %s" % value)
                        if not C7000VerifyLogicalInterconnectGroups.verify_mappings_visibility(value):
                            ui_lib.fail_test("failed verifying NO mappings values")
                        logger.info(" Sucessfully verified NO mappings values for  %s" % class1)
        if hasattr(lig, 'dot1p'):
            C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_type)
            EditLogicalInterconnectGroups.select_editoption(lig.classname)
            doip_list = [item.strip() for item in lig.dot1p.split(',')]
            EditLogicalInterconnectGroups.click_qos_class(fail_if_false=False)
            for qos in doip_list:
                if not C7000VerifyLogicalInterconnectGroups.verify_dot1poption(qos):
                    C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
                    C7000EditLogicalInterconnectGroups.click_cancel_button()
                    ui_lib.fail_test("DOI1P values %s is present for the selected QoS type ")
            C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
            # validating the negative Scenario.error message should be poped up if classname exceeds 225 chaeracters
        if hasattr(lig, 'uniqueclass'):
            logger.info("%s" % lig.uniqueclass)
            C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_configuration_type)
            if not EditLogicalInterconnectGroups.select_editoption(lig.Classname):
                ui_lib.fail_test("Failed to click edit button")

            if not C7000EditLogicalInterconnectGroups.input_classname(lig.uniqueclass):
                ui_lib.fail_test("Failed to input name")
            EditLogicalInterconnectGroups.click_class_ok_button()
            error = C7000EditLogicalInterconnectGroups.get_error_message()
            logger.info("%s" % error)
            if not error:
                ui_lib.fail_test("unexpected behaviour")
            logger.info("%s" % error)
            if (error == lig.error):
                logger.info("As expected error message is poped up if classname exceeds 225 characters")
            else:
                C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
                C7000EditLogicalInterconnectGroups.click_cancel_button()
                ui_lib.fail_test("error message is not poped up if classname exceeds 225 characters")
            C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
            # validating the negative Scenario.error message should be poped up if Best effort class share values is less than 1
        if hasattr(lig, 'verifysharevalues'):
            validate = False
            C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_type)
            class_list = [item.strip() for item in lig.classname.split(',')]
            initial_value = EditLogicalInterconnectGroups.get_share_value(lig.besteffort, lig.share)
            set_value = int(initial_value) / 2
            for class1 in class_list:
                EditLogicalInterconnectGroups.select_editoption(class1)
                EditLogicalInterconnectGroups.click_qos_class(fail_if_false=False)
                EditLogicalInterconnectGroups.input_share_values(set_value)
                EditLogicalInterconnectGroups.click_class_ok_button()
                class_value = EditLogicalInterconnectGroups.get_share_value(class1, lig.share)
                logger.info("share value for selected class is %s" % class_value)
                best_effort = EditLogicalInterconnectGroups.get_share_value(lig.besteffort, lig.share)
                actual_value = int(initial_value) - int(class_value)
                if int(best_effort) == int(actual_value) and int(best_effort) > 1:
                    logger.info("best effort share value is adjusted and it is less than 100 %s " % best_effort)
                    set_value = int(best_effort) + 1
                    initial_value = EditLogicalInterconnectGroups.get_share_value(lig.besteffort, lig.share)
                else:
                    logger.info("share value execeeds 100 ")
                    C7000EditLogicalInterconnectGroups.click_ok_button()
                    error = EditLogicalInterconnectGroups.get_qos_error_msg(timeout=30)
                    if (error == lig.error):
                        logger.info("Best efforts value is less than 1 %s " % error)
                    else:
                        C7000EditLogicalInterconnectGroups.click_cancel_button()
                        ui_lib.fail_test("error message is not poped up when besteffort value is lees than 1")
                        break
        if hasattr(lig, 'verifyqossettings'):
            logger.info("Verifying QOS Settings")
            C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_type)
        if hasattr(lig, 'verify_besteffort'):
            C7000EditLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_type)
            if not EditLogicalInterconnectGroups.select_editoption(lig.classname):
                C7000EditLogicalInterconnectGroups.click_cancel_button()
                ui_lib.fail_test("Failed to click edit option %s " % classname)
            if C7000EditLogicalInterconnectGroups.input_classname(lig.text, fail_if_false=False):
                C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
                C7000EditLogicalInterconnectGroups.click_cancel_button()
                ui_lib.fail_test("Best effort is editable")
            logger.info("Best effort is not editable")
            C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
            # validating the negative Scenario.error message should be poped up if classname is not unique
        if hasattr(lig, 'verify_uniquename'):
            C7000EditLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_type)
            unique = C7000EditLogicalInterconnectGroups.get_uniquename()
            logger.info("list value is %s" % unique)
            classes = [item.strip() for item in lig.classes.split(',')]
            logger.info("Classes value %s" % classes)
            EditLogicalInterconnectGroups.select_editoption(lig.classname)
            C7000EditLogicalInterconnectGroups.input_classname(lig.text)
            EditLogicalInterconnectGroups.click_class_ok_button()
            error = C7000EditLogicalInterconnectGroups.get_error_message()
            if (unique == classes) and (error == lig.error):
                logger.info("Successfully verified that all classnames are unique")
            else:
                C7000EditLogicalInterconnectGroups.click_cancel_button()
                C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
                ui_lib.fail_test("class names are not unique ")
            C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
        if hasattr(lig, 'verify_traffic'):
            traffic_list = [item.strip() for item in lig.verify_traffic.split(',')]
            total_traffic = len(traffic_list)
            C7000EditLogicalInterconnectGroups.select_qos_configuration_type(lig.custom_type)
            EditLogicalInterconnectGroups.select_editoption(lig.classname)
            for traffic in traffic_list:
                if not C7000VerifyLogicalInterconnectGroups.verify_traffic_option(traffic):
                    C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
                    C7000EditLogicalInterconnectGroups.click_cancel_button()
                    ui_lib.fail_test(" Failed to Verify traffic value")
            C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
        if hasattr(lig, 'qualityofservice'):
            C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(lig.qualityofservice)
            if not C7000EditLogicalInterconnectGroups.verify_fcoe_lossless_class_no_edit_option(lig.classname):
                ui_lib.fail_test("Unexpected behaviour!!FCoElossless class is editable ")
            logger.info("As expected unable to edit FCoElossless class EDIT option is not available")
        if hasattr(lig, 'priorities'):
            EditLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_configuration_type)
            EditLogicalInterconnectGroups.select_editoption(lig.Classname)
            TBirdEditLogicalInterconnectGroups.click_qos_class(fail_if_false=False)
            if C7000EditLogicalInterconnectGroups.select_egress_priority(lig.priority, fail_if_false=False):
                C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
                C7000EditLogicalInterconnectGroups.click_cancel_button()
                ui_lib.fail_test("failed  priority 3 is  available in the dropdown")
            C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
            logger.info("Successfully verified that priority 3 is not available in the dropdown")
            # validating the negative Scenario.error message should be poped up for invalid values such as -1, .10, abcd, @#$% etc
        if hasattr(lig, 'validateshareormax'):
            C7000EditLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_type)
            if not C7000EditLogicalInterconnectGroups.select_editoption(lig.classname):
                logger.info("Failed to click edit option %s " % classname)
                C7000EditLogicalInterconnectGroups.click_cancel_button()
                ui_lib.fail_test("Failed to click edit option %s " % classname)
            EditLogicalInterconnectGroups.click_qos_class(fail_if_false=False)
            logger.info("Field value %s" % lig.fieldvalues)
            if lig.validateshareormax == "max-share":
                if not C7000EditLogicalInterconnectGroups.input_shareormax(lig.validateshareormax, lig.fieldvalues):
                    C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
                    C7000EditLogicalInterconnectGroups.click_cancel_button()
                    ui_lib.fail_test("Failed to log text into the textbox")
                C7000EditLogicalInterconnectGroups.click_max_text()
                error = C7000EditLogicalInterconnectGroups.get_error_message()
                if (error == lig.error) or (error == lig.error2):
                    logger.info("invalid values such as -1, .10, abcd, @#$% etc are not allowed for maxshare values")
                else:
                    C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
                    C7000EditLogicalInterconnectGroups.click_cancel_button()
                    ui_lib.fail_test("invalid values such as -1, .10, abcd, @#$% etc are allowed")
                C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
            elif lig.validateshareormax == "share":
                if not C7000EditLogicalInterconnectGroups.input_shareormax(lig.validateshareormax, lig.fieldvalues):
                    C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
                    C7000EditLogicalInterconnectGroups.click_cancel_button()
                    ui_lib.fail_test("Failed to log text into the textbox")
                EditLogicalInterconnectGroups.click_class_ok_button()
                error = C7000EditLogicalInterconnectGroups.get_error_message()
                if (error == lig.error) or (error == lig.error2):
                    logger.info("invalid values such as -1, .10, abcd, @#$% etc are not allowed for maxshare values")
                else:
                    C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
                    C7000EditLogicalInterconnectGroups.click_cancel_button()
                    ui_lib.fail_test("invalid values such as -1, .10, abcd, @#$% etc are allowed")
                C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
            else:

                C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
                C7000EditLogicalInterconnectGroups.click_cancel_button()
                ui_lib.fail_test("INVALID VALUE")
        if hasattr(lig, 'dot1p_priority'):
            C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_configuration_type)
            besteffort_fcoe_priority = TBirdEditLogicalInterconnectGroups.get_besteffort_fcoe_priority()
            logger.info(besteffort_fcoe_priority)
            TBirdEditLogicalInterconnectGroups.select_editoption(lig.classname)
            classenable_list = [item.strip() for item in lig.classenable.split('/')]
            logger.info("classEnable_list value %s" % classenable_list)
            total_len = len(classenable_list)
            logger.info("length of classenable_list values are %d" % total_len)
            for classenable in classenable_list:
                logger.info("value in list is %s" % classenable)
                if classenable == ("Enabled"):
                    TBirdEditLogicalInterconnectGroups.click_qos_class(fail_if_false=False)
                    if C7000VerifyLogicalInterconnectGroups.verify_priority_availability(True):
                        logger.info("Egress DOT1P priorities are available")
                        dot1p_priority_list = [item.strip() for item in lig.dot1p_priority.split(',')]
                        logger.info("dot1p_priority_list value %s" % dot1p_priority_list)
                        C7000EditLogicalInterconnectGroups.click_dot1p_priority_dropdown()
                        logger.info("dropdown list displayed")
                        for i in dot1p_priority_list:
                            dot1p_priority_ui = C7000EditLogicalInterconnectGroups.select_dot1p_priority(i)
                            logger.info(dot1p_priority_ui)
                            logger.info(i)
                            if re.search(i, dot1p_priority_ui):
                                if dot1p_priority_ui != besteffort_fcoe_priority[0] and dot1p_priority_ui != besteffort_fcoe_priority[1]:
                                    logger.info("%s is not Best Effort and FCoE class priority" % dot1p_priority_ui)
                                else:
                                    logger.info("Best Effort and FCoE class priorities are available in Egress DOT1P priority dropdown list")
                                    ui_lib.fail_test("Unexpected Behaviour")
                            else:
                                ui_lib.fail_test("priority doesn't get matched")
                    else:
                        ui_lib.fail_test("Egress DOT1P priorities are available by defect")

                elif classenable == ("Disabled"):
                    TBirdEditLogicalInterconnectGroups.click_qos_class_disable()
                    if C7000VerifyLogicalInterconnectGroups.verify_priority_availability(False):
                        logger.info("Egress DOT1P priorities are not available")
                    else:
                        ui_lib.fail_test("Egress DOT1P priorities are not available by defect")
                else:
                    ui_lib.fail_test("Invalid values")
            C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
        if hasattr(lig, 'enableclass'):
            C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_type)
            classname_list = [item.strip() for item in lig.enableclass.split(',')]
            classes = [item.strip() for item in lig.classeslist.split(',')]
            for name in classname_list:
                count = 0
                EditLogicalInterconnectGroups.select_editoption(name)
                EditLogicalInterconnectGroups.click_qos_class(fail_if_false=False)
                EditLogicalInterconnectGroups.input_share_values(lig.Sharevalues)
                if not C7000EditLogicalInterconnectGroups.click_qos_real_class():
                    C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
                    ui_lib.fail_test("Failed to disable class")
                EditLogicalInterconnectGroups.click_class_ok_button()
                real_time_value = EditLogicalInterconnectGroups.get_real_time_value_of_class(name)
                logger.info("select value [ %s ]" % real_time_value)
                if(real_time_value == 'Yes'):
                    logger.info("The real time is enabled")
                else:
                    C7000EditLogicalInterconnectGroups.click_cancel_button()
                    return False
            for classname in classes:
                real_time_value = EditLogicalInterconnectGroups.get_real_time_coloumn_value(classname)
                logger.info("Real time value for the class is %s" % real_time_value)
                if (real_time_value == 'Yes'):
                    logger.info("The real time is enabled")
                    if (name == classname):
                        logger.info("The real time is enabled for the class %s" % classname)
                        count += 1
                else:
                    logger.info("The real time value is not enabled for remaining classes ")
            if count == 1:
                logger.info("Real Time is enabled only for one class")
            else:
                C7000EditLogicalInterconnectGroups.click_cancel_button()
                ui_lib.fail_test("Real Time is enabled only for more than one class")
        if hasattr(lig, 'mapping_availability'):
            C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_type)
            logger.info("clicking the edit button of the given class")
            EditLogicalInterconnectGroups.select_editoption(lig.classname)
            classenable_list = [item.strip() for item in lig.classenable.split('/')]
            logger.info("classEnable_list value %s" % classenable_list)
            total_len = len(classenable_list)
            logger.info("length of classenable_list values are %d" % total_len)
            for classenable in classenable_list:
                logger.info("value in list is %s" % classenable)
                if classenable == ("Enabled"):
                    TBirdEditLogicalInterconnectGroups.click_qos_class(fail_if_false=False)
                    if TBirdVerifyLogicalInterconnectGroups.verify_dot1p_and_dscp_availability(True):
                        logger.info("DOT1P and DSCP mappings are available")
                        dot1p_value_list = [item.strip() for item in lig.dot1pvalue.split(',')]
                        logger.info("dot1p_value_list value %s" % dot1p_value_list)
                        total_len = len(dot1p_value_list)
                        logger.info("length of dot1p_value_list values are %d" % total_len)

                        dot1p_current_list = [item.strip() for item in lig.dot1pcurrent.split(',')]
                        logger.info("dot1_current_list value %s" % dot1p_current_list)
                        total_len = len(dot1p_current_list)
                        logger.info("length of dot1p_current_list values are %d" % total_len)
                        total_len = total_len + 1
                        for i in range(1, total_len):
                            dot1p_value = EditLogicalInterconnectGroups.get_text_dot1p_value(i)
                            logger.info(dot1p_value)
                            dot1p_current = EditLogicalInterconnectGroups.get_text_dot1p_current(i)
                            logger.info(dot1p_current)
                            if dot1p_value == dot1p_value_list[i - 1] and dot1p_current == dot1p_current_list[i - 1]:
                                logger.info("%s Initial configuration verified successfully for DOT1P" % i)
                            else:
                                ui_lib.fail_test("Initial configuration not verified for DOT1P")

                        dscp_value_list = [item.strip() for item in lig.dscpvalue.split('/')]
                        logger.info("dscp_value_list value %s" % dscp_value_list)
                        total_len = len(dscp_value_list)
                        logger.info("length of dscp_value_list values are %d" % total_len)

                        dscp_current_list = [item.strip() for item in lig.dscpcurrent.split(',')]
                        logger.info("dscp_current_list value %s" % dscp_current_list)
                        total_len = len(dscp_current_list)
                        logger.info("length of dot1p_current_list values are %d" % total_len)
                        total_len = total_len + 1
                        for i in range(1, total_len):
                            dscp_value = EditLogicalInterconnectGroups.get_text_dscp_value(i)
                            logger.info(dscp_value)
                            dscp_current = EditLogicalInterconnectGroups.get_text_dscp_current(i)
                            logger.info(dscp_current)
                            if dscp_value == dscp_value_list[i - 1] and dscp_current == dscp_current_list[i - 1]:
                                logger.info(" %s Initial configuration verified successfully for DSCP" % i)
                            else:
                                ui_lib.fail_test("Initial configuration not verified for DSCP")
                    else:
                        ui_lib.fail_test("DOT1P and DSCP mappings are not available by defect")
                elif classenable == ("Disabled"):
                    TBirdEditLogicalInterconnectGroups.click_qos_class_disable()
                    if not TBirdVerifyLogicalInterconnectGroups.verify_dot1p_and_dscp_availability(False):
                        ui_lib.fail_test("DOT1P and DSCP mappings are available by defect")
                    else:
                        logger.info("DOT1P and DSCP mappings are removed")
                else:
                    ui_lib.fail_test("Invalid values")
            C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
        if hasattr(lig, 'qostype'):
            C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_configuration_type)
            values_list1 = []
            values_list2 = []
            values_list3 = []
            class_list = [item.strip() for item in lig.classname.split(',')]
            value_list = [item.strip() for item in lig.value.split(',')]
            for value in class_list:
                EditLogicalInterconnectGroups.select_editoption(value)
                EditLogicalInterconnectGroups.click_qos_class(fail_if_false=False)
                EditLogicalInterconnectGroups.input_share_values(lig.share)
                EditLogicalInterconnectGroups.input_maxshare_value(lig.maxshare)
                EditLogicalInterconnectGroups.click_class_ok_button()
            C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_type)
            C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_configuration_type)
            for value in class_list:
                val = EditLogicalInterconnectGroups.get_class_enabled(value)
                values_list1.append(val)
                logger.info("successfully got text for enabled %s" % values_list1)
                val = EditLogicalInterconnectGroups.get_share_value(value, lig.sharetext)
                values_list2.append(val)
                logger.info("successfully got text for share %s" % values_list2)
                val = EditLogicalInterconnectGroups.get_maxsharevalue(value)
                values_list3.append(val)
                logger.info("successfully got text for maxshare %s" % values_list3)
            C7000EditLogicalInterconnectGroups.click_cancel_button()
            return values_list1, values_list2, values_list3
        if hasattr(lig, 'verifybackuprestore'):
            C7000EditLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_configuration_type)
            class_list = [item.strip() for item in lig.classname1.split(',')]
            sharevalue_list = [item.strip() for item in lig.sharevalue.split(',')]
            egresspriority_list = [item.strip() for item in lig.egresspriority.split(',')]
            dot1pvalue_list = [item.strip() for item in lig.dot1pvalue.split(',')]
            dscpvalue_list = [item.strip() for item in lig.dscpvalue.split(',')]
            i = 0
            for value in class_list:
                if value != 'Best effort':
                    EditLogicalInterconnectGroups.select_editoption(value)
                    if not EditLogicalInterconnectGroups.click_qos_class(fail_if_false=False):
                        logger.info("Class is already enabled")
                        C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
                    else:
                        logger.info("Class is now enabled")
                        EditLogicalInterconnectGroups.input_share_values(sharevalue_list[i])
                        EditLogicalInterconnectGroups.select_egress_priority(egresspriority_list[i])
                        EditLogicalInterconnectGroups.tick_dot1p_values(dot1pvalue_list[i])
                        EditLogicalInterconnectGroups.tick_dscp_values(dscpvalue_list[i])
                        EditLogicalInterconnectGroups.click_class_ok_button()
                i += 1
                if value == 'Best effort':
                    EditLogicalInterconnectGroups.select_editoption(value)
                    if not EditLogicalInterconnectGroups.click_best_effort_class():
                        logger.info("Best effort is already enabled")
                        C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
                    else:
                        ui_lib.test_fail("unexpected behaviour")
            C7000EditLogicalInterconnectGroups.click_ok_button()
            return True
        if hasattr(lig, 'realclass'):
            C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_type)
            EditLogicalInterconnectGroups.select_editoption(lig.realclass)
            if not VerifyLogicalInterconnectGroups.verify_realclass_invisibility(fail_if_false=False):
                ui_lib.fail_test("Unexpected behaviour real class is visible when class is disabled")
            EditLogicalInterconnectGroups.click_qos_class(fail_if_false=False)
            EditLogicalInterconnectGroups.click_qos_real_class()
            check_list = [item.strip() for item in lig.share.split(',')]
            logger.info("Check_list value %s" % check_list)
            total_len = len(check_list)
            logger.info("No of values to be checked are %d" % total_len)
            for value in check_list:
                if (int(value) <= 50):
                    EditLogicalInterconnectGroups.input_share_values(value)
                    EditLogicalInterconnectGroups.click_class_ok_button()
                    sharevalue = EditLogicalInterconnectGroups.get_share_value(lig.realclass, lig.sharetext)
                    maxsharevalue = EditLogicalInterconnectGroups.get_maxsharevalue(lig.realclass)
                    if (sharevalue == maxsharevalue):
                        logger.info("Sucessfully verified share and maxshare has same values after enabling real class in the table")
                    else:
                        ui_lib.test_fail("share and maxshare has different values")
                else:
                    EditLogicalInterconnectGroups.select_editoption(lig.realclass)
                    EditLogicalInterconnectGroups.input_share_values(value)
                    EditLogicalInterconnectGroups.click_class_ok_button()
                    error = EditLogicalInterconnectGroups.get_error_message()
                    logger.info(error)
                    C7000EditLogicalInterconnectGroups.click_traffic_cancel_button()
                    C7000EditLogicalInterconnectGroups.click_cancel_button()
                    return error
        if hasattr(lig, 'Reset'):
            C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_configuration_type)
            i = 0
            values_list1 = []
            values_list2 = []
            values_list3 = []
            values_list4 = []
            class_list = [item.strip() for item in lig.classname.split(',')]
            value_list = [item.strip() for item in lig.value.split(',')]
            for value in class_list:
                EditLogicalInterconnectGroups.select_editoption(value)
                EditLogicalInterconnectGroups.click_qos_class(fail_if_false=False)
                EditLogicalInterconnectGroups.input_share_values(lig.share)
                EditLogicalInterconnectGroups.input_maxshare_value(lig.maxshare)
                EditLogicalInterconnectGroups.tick_dot1p_values(lig.dot1p1, timeout=15)
                EditLogicalInterconnectGroups.tick_dscp_values(lig.dscp1)
                EditLogicalInterconnectGroups.click_class_ok_button()
            C7000EditLogicalInterconnectGroups.click_reset_button()
            for value in class_list:
                val = EditLogicalInterconnectGroups.get_class_enabled(value)
                values_list1.append(val)
                logger.info("successfully got text for enabled %s" % values_list1)
                val = EditLogicalInterconnectGroups.get_share_value(value, lig.sharetext)
                values_list2.append(val)
                logger.info("successfully got text for share %s" % values_list2)
                val = EditLogicalInterconnectGroups.get_maxsharevalue(value)
                values_list3.append(val)
                logger.info("successfully got text for maxshare %s" % values_list3)
                EditLogicalInterconnectGroups.select_classname(value)
                val = EditLogicalInterconnectGroups.get_dot1p_dscp_mapping_values(value_list[i])
                logger.info("Retrieved value is %s" % val)
                values_list4.append(val)
                logger.info("successfully got text for DSCP DOt1p mappings %s" % values_list4)
                i += 1
            C7000EditLogicalInterconnectGroups.click_cancel_button()
            return values_list1, values_list2, values_list3, values_list4
        if hasattr(lig, 'validatedisableclass'):
            logger.info("Check value for the disabled class")
            C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_type)
            isclassenabled = C7000EditLogicalInterconnectGroups.get_class_enabled(lig.classno, fail_if_false=False)
            validatedisableclass = C7000EditLogicalInterconnectGroups.get_share_value(lig.classno, lig.share)
            if isclassenabled == "No" and int(validatedisableclass) == 0:
                logger.info("VALUE 0 IS ALLOWED FOR DISABLED CLASS")
            else:
                C7000EditLogicalInterconnectGroups.click_cancel_button()
                ui_lib.fail_test("VALUE 0 IS NOT ALLOWED FOR ENABLED CLASS")
        if hasattr(lig, 'verifypriorities'):
            dot1p_priority = [item.strip() for item in lig.priority1.split(',')]
            C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_type)
            EditLogicalInterconnectGroups.select_editoption(lig.besteffort)
            if not EditLogicalInterconnectGroups.select_egress_fields():
                ui_lib.fail_test("egress priority values is editable for Best Effort")
            logger.info("egress priority values is  not  editable for Best Effort ")
            EditLogicalInterconnectGroups.click_class_ok_button()
            priority_list = [item.strip() for item in lig.priority.split(',')]
            class_list = [item.strip() for item in lig.classname.split(',')]
            i = 0
            for class1 in class_list:
                EditLogicalInterconnectGroups.select_editoption(class1)
                EditLogicalInterconnectGroups.click_qos_class(fail_if_false=False)
                EditLogicalInterconnectGroups.input_share_values(lig.share)
                if not EditLogicalInterconnectGroups.select_egress_priority(priority_list[i]):
                    ui_lib.fail_test("failed to select egrees value from dropdown")
                i += 1
                EditLogicalInterconnectGroups.click_class_ok_button()
            dot1p = []
            validate1 = EditLogicalInterconnectGroups.get_egress_priority_values()
            logger.info("egress priority values  %s " % validate1)
            dot1p.append(validate1)
            dot1p.append(dot1p_priority)
            C7000EditLogicalInterconnectGroups.click_cancel_button()
            return dot1p
        if hasattr(lig, 'showqueue'):
            class_list = [item.strip() for item in lig.classname.split(',')]
            C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_type)
            EditLogicalInterconnectGroups.select_editoption(lig.besteffort)
            if not EditLogicalInterconnectGroups.select_egress_fields():
                ui_lib.fail_test("egress priority values is editable for Best Effort")
            logger.info("egress priority values is  not  editable for Best Effort ")
            EditLogicalInterconnectGroups.click_class_ok_button()
            priority_list = [item.strip() for item in lig.priority.split(',')]
            share_list = [item.strip() for item in lig.share.split(',')]
            i = 0
            for class1 in class_list:
                EditLogicalInterconnectGroups.select_editoption(class1)
                EditLogicalInterconnectGroups.click_qos_class(fail_if_false=False)
                EditLogicalInterconnectGroups.input_share_values(share_list[i])
                if not EditLogicalInterconnectGroups.select_egress_priority(priority_list[i]):
                    ui_lib.fail_test("failed to select egrees value from dropdown")
                i += 1
                EditLogicalInterconnectGroups.click_class_ok_button()
            C7000EditLogicalInterconnectGroups.click_ok_button()
        C7000EditLogicalInterconnectGroups.click_cancel_button()
        return True


def edit_scope_for_logical_interconnect_groups(ligs_list):
    """ edit scope for LIG
        This function is to edit scope for LIGs
        Example:
            edit_scope_for_logical_interconnect_groups(ligs_list)
    """
    logger.info("Function call to edit scope for Logical Interconnect Groups ")
    navigate()
    for lig in ligs_list:
        if not select_logical_interconnect_group(lig.name):
            FusionUIBase.fail_test_or_return_false("Failed to find the target LIG")
        FusionUIBase.select_view_by_name("Scopes")
        EditScopeForLogicalInterconnectGroups.click_edit_scope_button()
        EditScopeForLogicalInterconnectGroups.wait_edit_scope_dialog_open()
        if lig.has_property("scopes"):
            scope_list = lig.scopes.split(',')
            for scope in scope_list:
                if not VerifyLogicalInterconnectGroups.verify_scope_should_exist_in_edit_page(scope, 2, fail_if_false=False):
                    EditScopeForLogicalInterconnectGroups.click_assign_button()
                    EditScopeForLogicalInterconnectGroups.wait_assign_scope_dialog_open()
                    EditScopeForLogicalInterconnectGroups.input_scope_name(scope)
                    EditScopeForLogicalInterconnectGroups.click_scope_name(scope)
                    EditScopeForLogicalInterconnectGroups.click_add_button()
                    EditScopeForLogicalInterconnectGroups.wait_assign_scope_dialog_close()
        if lig.has_property("remove_scopes"):
            remove_scope_list = lig.remove_scopes.split(',')
            for scope in remove_scope_list:
                if VerifyLogicalInterconnectGroups.verify_scope_should_exist_in_edit_page(scope, timeout=5):
                    EditScopeForLogicalInterconnectGroups.click_remove_scope_icon(scope)
        EditScopeForLogicalInterconnectGroups.click_ok_button()
        EditScopeForLogicalInterconnectGroups.wait_edit_scope_dialog_close()
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(lig.name, 'Update', timeout=60, fail_if_false=True)
        FusionUIBase.show_activity_sidebar()
    return True


def validate_user_privileges(*lig_obj):
    """ validate_user_privileges

    Arguments:
      <lig>
          name*                     --  Name of logical interconnect group as a string.
          qos_configuration_type*   --  Possible value: Passthrough/Custom (with FCoE lossless)|Custom (without FCoE lossless)
    * Required Arguments

    Example:
        data/ligs -> @{TestData.ligs}
        <ligs>
            <lig  name="LIG-wpst32"
                 qos_configuration_type = "Custom (with FCoE lossless)"
            </lig>
        </ligs>

    """
    navigate()

    logger.info("verifying action button visibility")
    if isinstance(lig_obj, test_data.DataObj):
        lig_obj = [lig_obj]
    elif isinstance(lig_obj, tuple):
        lig_obj = list(lig_obj[0])

    total = len(lig_obj)
    for lig in lig_obj:
        navigate()
        editligname = lig.name
        # select LIG
        if not select_logical_interconnect_group(editligname):
            ui_lib.fail_test("LIG not selected")
        logger.info("successfully selected the LIG")
        if not C7000EditLogicalInterconnectGroups.click_actions_menu():
            ui_lib.fail_test("Failed to verify action button visibility under actions menu")
    return True


def get_qos_class_values(lig_obj):
    """ get_qos_class_values
    # To get all the QoS configuration values i.e egresspriority, sharevalue,dscpvalue,dot1p values in LIG page
    Arguments:
      <lig>
          name*                     --  Name of logical interconnect group as a string.
          qos_configuration_type*   --  Possible value: Passthrough/Custom (with FCoE lossless)|Custom (without FCoE lossless)
                  classname1*               --  name of the class possible value:FCoE lossless
                  qos_configuration_type_with_fcoe* --  Possible value: Passthrough/Custom (with FCoE lossless)|Custom (without FCoE lossless)
                  sharevalue*               -- Possible values: Between 1 and 100
                  egresspriority*            -- Possible values: from 0 to 7
                  dot1pvalue*                -- Possible values: 0 to 5
                  dscpvalue*                -- Possible values:DSCP_10_AF11,DSCP_10_AF11, DSCP_0_CS0, DSCP_12_AF12, DSCP_14_AF13, DSCP_8_CS1
                  dot1p_dscp_mappings       -- Possible values: 0 to 16
                  egress_priority_status    -- Possible values: 0 to 16
    * Required Arguments

    Example:
        data/ligs -> @{TestData.ligs}
        <ligs>
                        <lig name="LIG1"
                        verifybackuprestore = ""
                        qos_configuration_type = "Custom (without FCoE lossless)"
                        qos_configuration_type_with_fcoe = "Custom (with FCoE lossless)"
                        classname1 = "Best effort, Class1, Class2, Class3, Class4, Class5, Medium, Real time"
                        </lig>
        </ligs>

    """

    navigate()
    logger.info("verifying QoS values on Logical Interconnect Groups...")

    total_len = len(lig_obj)
    for n, lig in enumerate(lig_obj):
        # check if LIG is existing
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total_len, '-' * 14))
        logger.info("Editing a LIG with name '{0}'".format(lig.name))
        if C7000VerifyLogicalInterconnectGroups.verify_lig_exist(lig.name, fail_if_false=False) is False:
            logger.warn("LIG '{0}' not exists".format(lig.name))
            continue

        # select LIG

        if select_logical_interconnect_group(lig.name) is False:
            continue
        C7000EditLogicalInterconnectGroups.select_actions_edit()
        C7000EditLogicalInterconnectGroups.wait_edit_lig_dialog_shown()
    if hasattr(lig, 'verifybackuprestore'):
        C7000EditLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_configuration_type)
        i = 0
        values_list1 = []
        values_list2 = []
        values_list3 = []
        values_list4 = []
        class_list = [item.strip() for item in lig.classname1.split(',')]
        dtop_dscp_mappings_list = [item.strip() for item in lig.dot1p_dscp_mappings.split(',')]
        for value in class_list:
            val = EditLogicalInterconnectGroups.get_class_enabled(value)
            values_list1.append(val)
            logger.info("Successfully got value for class enabled %s" % values_list1)
            val = EditLogicalInterconnectGroups.get_share_value(value, lig.sharetext)
            values_list2.append(val)
            logger.info("Successfully got share value %s" % values_list2)
            EditLogicalInterconnectGroups.select_classname(value)
            val = EditLogicalInterconnectGroups.get_egress_priority_fields(value)
            values_list3.append(val)
            logger.info("Successfully got egress priority %s" % values_list3)
            val = EditLogicalInterconnectGroups.get_dot1p_dscp_mapping_values(dtop_dscp_mappings_list[i])
            logger.info("Retrieved value is %s" % val)
            values_list4.append(val)
            logger.info("Successfully got value for DSCP DOT1P mappings %s" % values_list4)
            i += 1
        C7000EditLogicalInterconnectGroups.click_cancel_button()
        return values_list1, values_list2, values_list4
    if hasattr(lig, 'showqueue'):
        class_list = [item.strip() for item in lig.realtime.split(',')]
        C7000CreateLogicalInterconnectGroups.select_qos_configuration_type(lig.qos_type)
        sharevalue_list = []
        sharevalues = []
        queuelist = []
        priorityvalues = []
        priorities_list = EditLogicalInterconnectGroups.get_egress_priority_values()
        logger.info("priority values  %s " % priorities_list)
        for val in class_list:
            real_time_value = EditLogicalInterconnectGroups.get_real_time_coloumn_value(val)
            logger.info("Real time value for the class is %s" % real_time_value)
            if (real_time_value == 'Yes'):
                logger.info("The real time is enabled")
                sharevalue = EditLogicalInterconnectGroups.get_realtime_sharevalue(val, lig.sharetext, fail_if_false=False)
                sharevalue = lig.defaultsharerealtime
                sharevalue_list.append(sharevalue)
            else:
                real_time_sharevalue = EditLogicalInterconnectGroups.get_realtime_sharevalue(val, lig.sharetext, fail_if_false=False)
                sharevalue_list.append(real_time_sharevalue)
        list_value = sharevalue_list.index('Share is based on the profile FC connection configuration')
        logger.info(" index  %s " % list_value)
        sharevalue_list[list_value] = lig.defaultsharefcoelossless
        logger.info(" share values  %s " % sharevalue_list)
        priorityvalues = [(int(x) + 1) for x in priorities_list]
        sharevalues = [int(i) / 2 for i in sharevalue_list]
        share_value = sharevalues.index(int(sharevalue) / 2)
        logger.info(" index  %s " % share_value)
        sharevalues[share_value] = lig.realenabled
        unicode_values = [unicode(i) for i in priorityvalues]
        logger.info("unicode_values is %s " % unicode_values)
        unicade_values1 = [unicode(i) for i in sharevalues]
        logger.info("unicade_values1 is %s " % unicade_values1)
        queuelist.append(unicode_values)
        queuelist.append(unicade_values1)
        C7000EditLogicalInterconnectGroups.click_cancel_button()
        return queuelist


def _add_snmp_v3_user(snmp_obj):
    ''' Adds snmpv3 users
    <adduser
    username*                   --  Snmpv3 user name
    security_level*             --  Security level to be chosen for user.values can be none, authentication or authenticationandprivacy
    auth_protocol               --  authentication protocol to be provided if user chooses
                                    authentication or authenticationandprivacy as security level.
   authentication_password      --  password for authentication protocol.Must be 8-31 alphanumeric characters
   confirm_auth_password        --  password set for authentication_password should be passed
   priv_protocol                --  privacy protocol to be provided if user chooses
                                    authenticationandprivacy as security level
    privacy_password            --  password for privacy protocol.Must be 8-31 alphanumeric characters
   confirm_priv_password        --  password set for privacy_password should be passed
   action*                      --  option to be given as add or add_plus  . adds user with the option "add"

     * Required Arguments

     Examples:
     <adduser username= "user1"  security_level="none" action="add"></adduser>

    <adduser username= "user3"  security_level="authentication" auth_protocol="MD5"
    authentication_password="Password1" confirm_auth_password="Password1" action="add"></adduser>

    <adduser username= "user6"
          security_level="authenticationandprivacy" auth_protocol="MD5"
          authentication_password="Password1" confirm_auth_password="Password1"
          priv_protocol="AES-192" privacy_password="Password2"
          confirm_priv_password="Password2" action="add"></adduser>
        '''

    logger.info("Adding user for SNMPv3")
    add_length = len(snmp_obj.adduser)
    logger.info("Number of users to be added is %s" % add_length)
    CreateLogicalInterconnectGroups.click_add_snmp_user()
    VerifyLogicalInterconnectGroups.verify_add_snmp_user_dialog_visible()
    for index, usr_obj in enumerate(snmp_obj.adduser):
        if index != add_length:
            logger.info("Adding user %s" % usr_obj.username)
            CreateLogicalInterconnectGroups.input_add_snmp_user_name(usr_obj.username)
            __add_user(usr_obj)
        else:
            if index == add_length or error_flag:
                if usr_obj.action == "edit":
                    VerifyLogicalInterconnectGroups.wait_edit_snmp_user_confirm_dialog_disappear()
                elif usr_obj.action == "add":
                    VerifyLogicalInterconnectGroups.wait_add_snmp_user_dialog_disappear()
    return True


def __add_user(usr_obj):
    error_flag = 0
    logger.info("configuring add user details")
    if usr_obj.security_level.lower() == "none":
        CreateLogicalInterconnectGroups.select_security_level_none()

    elif usr_obj.security_level.lower() == "authentication":
        CreateLogicalInterconnectGroups.select_security_level_authentication()
    elif usr_obj.security_level.lower() == "authenticationandprivacy":
        if VerifyLogicalInterconnectGroups.verify_security_level_authentication_and_privacy_visibility():
            CreateLogicalInterconnectGroups.select_security_level_authentication_and_privacy()
        else:
            logger.info("The security level is enabled as authentication and privacy in FIPS/CNSA mode ")
    else:
        ui_lib.fail_test("invalid option for user type")
    if usr_obj.security_level == "authentication" or usr_obj.security_level == "authenticationandprivacy":
        CreateLogicalInterconnectGroups.click_dropdown_authentication_protocol()
        list = CreateLogicalInterconnectGroups.get_authentication_protocols()
        logger.info("available authentication protocols are %s" % list)
        if usr_obj.auth_protocol in list:
            CreateLogicalInterconnectGroups.select_authentication_protocol(usr_obj.auth_protocol)
            if hasattr(usr_obj, "authentication_password"):
                CreateLogicalInterconnectGroups.input_authentication_password(usr_obj.authentication_password)
                CreateLogicalInterconnectGroups.input_confirm_authentication_password(usr_obj.confirm_auth_password)
        else:
            logger.warn("authentication protocol %s provided by the user is invalid. Hence the current snmpv3 user canot be added" % usr_obj.auth_protocol)
            CreateLogicalInterconnectGroups.click_add_snmp_user_cancel()
            return False

    if usr_obj.security_level == "authenticationandprivacy":
        CreateLogicalInterconnectGroups.click_dropdown_privacy_protocol()
        list = CreateLogicalInterconnectGroups.get_privacy_protocols()
        logger.info("available privacy protocols are %s" % list)
        if usr_obj.priv_protocol in list:
            CreateLogicalInterconnectGroups.select_authentication_and_privacy_protocol(usr_obj.priv_protocol)
            if hasattr(usr_obj, "privacy_password"):
                CreateLogicalInterconnectGroups.input_privacy_password(usr_obj.privacy_password)
                CreateLogicalInterconnectGroups.input_confirm_privacy_password(usr_obj.confirm_priv_password)
        else:
            logger.warn(" privacy protocol provided by the user is invalid.Hence SNMPv3 user cannot be added in the current LIG")
            CreateLogicalInterconnectGroups.click_add_snmp_user_cancel()
            return False
    if usr_obj.action == "add":
        CreateLogicalInterconnectGroups.click_add_snmp_user_add()
    elif usr_obj.action == "edit":
        EditLogicalInterconnectGroups.click_add_snmp_user_edit()
    elif usr_obj.action == "add_plus":
        CreateLogicalInterconnectGroups.click_add_snmp_user_add_plus()
    if hasattr(usr_obj, "max_user_error"):
        if VerifyLogicalInterconnectGroups.verify_add_max_snmp_user_error_message(usr_obj.max_user_error):
            CreateLogicalInterconnectGroups.click_add_snmp_user_cancel()
            error_flag += 1
            return error_flag

    elif hasattr(usr_obj, "auth_password_error"):
        if VerifyLogicalInterconnectGroups.verify_invalid_authentication_password_error_message(usr_obj.auth_password_error):
            CreateLogicalInterconnectGroups.click_add_snmp_user_cancel()

    elif hasattr(usr_obj, "privacy_password_error"):
        if VerifyLogicalInterconnectGroups.verify_invalid_privacy_password_error_message(usr_obj.privacy_password_error):
            CreateLogicalInterconnectGroups.click_add_snmp_user_cancel()

    elif hasattr(usr_obj, "invalid_username_error"):
        if VerifyLogicalInterconnectGroups.verify_invalid_username_error_message(usr_obj.invalid_username_error):
            CreateLogicalInterconnectGroups.click_add_snmp_user_cancel()

    elif hasattr(usr_obj, "duplicate_username_error"):
        if VerifyLogicalInterconnectGroups.verify_duplicate_username_error_message(usr_obj.duplicate_username_error):
            CreateLogicalInterconnectGroups.click_add_snmp_user_cancel()

    return True


def __create_lig_add_snmpv3_trap_destination(snmp_obj):
    '''
     Adds trap destination for snmpv3
    <trapdestination>
    trapdestination*    --  Trap Destination for snmpv3
    trapformat*         --  Trap Format. Possible value: SNMPv1|SNMPv2|SNMPv3
    notification_type*  --  Whether to enable notification type, Possible value : TRAP|INFORM.Applicable only for Trap Format snmpv3.
    action*             --  Action to be performed in the trap destination,Possible values are add or add_plus
    snmp_user           --  To choose the snmpv3 user. If not, default user will be selected.Applicable only for Trap Format snmpv3.
    port                --  Port configuration
    engineid
    communitystring     --  Optional,Community string as string value. Applicable only for Trap Formats snmpv1 and snmpv2.
    severity            --  Sets severity of the trap. possible values are:
                            Critical-> The SNMP manager cannot manage installed components.
                            Major->One or more of the component's subsystems is not operating properly, causing serious disruption to functions.
                            Minor->One or more of the component's subsystems is not operating properly, causing slight disruption to functions.
                            Warning-> The component has a potential problem.
                            Normal->The component is fully functional.
                            Info->Operational information on the fully functioning component.
                            Unknown->The SNMP manager has not yet established communication with the component.
   VCM_traps           --   Trap category for VCM (Virtual Connect Manager) possible values are:
                                Legacy ->When the software changes status, configuration status, or redundancy mode.
    Enet_traps         --  Ethernet Trap Categories. Possible values are:
                              Port Status ->When a link changes from being up or down.
                              Port Thresholds->Throughput utilization thresholds are exceeded.
                              Other->Authentication failures.
   FC_traps            --  Fiber Channel trap categories. Possible values are:
                            Port Status->When a link changes from being up or down.
                            Other->Authentication failures.
   </trapdestination>
     * Required Arguments

     Examples:
     <trapdestination trapdestination= "10.101.11.14" action="add" trapformat="snmpv3" notification_type="Trap"  snmp_user="user5" ></trapdestination>
     <trapdestination trapdestination= "10.101.11.15" action="add" trapformat="snmpv3" port="165" notification_type="Inform" engineid="0XFFFFfffffffff" snmp_user="user5" VCM_traps="legacy"
     Enet_traps="Port status, Other" FC_traps="Port status, Other"  ></trapdestination>

          <trapdestination trapdestination= "10.101.11.16" action="add" trapformat="snmpv2" communitystring="public"
          severity="Crtical, Major" VCM_traps="legacy" Enet_traps="Port status, Other" FC_traps="Port status, Other"  ></trapdestination>
         VCM_traps

    '''
    logger.info("- configure Trap Destination settings for snmpv3")
    td_list = snmp_obj.add_snmpv3_trapdestination
    td_len = len(td_list)
    CreateLogicalInterconnectGroups.click_add_trap_destination()
    CreateLogicalInterconnectGroups.wait_add_trap_destination_dialog_shown()

    for index, td_obj in enumerate(td_list):
        if index != td_len:
            CreateLogicalInterconnectGroups.input_add_trap_destination_trap_destination(td_obj.trapdestination)
            __add_trap_values(td_obj)
        else:
            if index == td_len or error_flag:
                if td_obj.action == "add":
                    CreateLogicalInterconnectGroups.wait_add_trap_destination_dialog_disappear()
                elif td_obj.action == "edit":
                    EditLogicalInterconnectGroups.wait_edit_trap_destination_dialog_disappear()
    return True


def __add_trap_values(td_obj):
    error_flag = 0
    if hasattr(td_obj, 'communitystring'):
        CreateLogicalInterconnectGroups.input_add_trap_destination_community_string(td_obj.communitystring)
    if hasattr(td_obj, 'trapformat'):
        if td_obj.trapformat.lower() == "snmpv1":
            CreateLogicalInterconnectGroups.tick_add_trap_destination_trap_format_snmpv1()
        elif td_obj.trapformat.lower() == "snmpv2":
            if VerifyLogicalInterconnectGroups.verify_trap_format_visibility():
                CreateLogicalInterconnectGroups.tick_add_trap_destination_trap_format_snmpv2()
                if not VerifyLogicalInterconnectGroups.verify_snmpv3_trap_destination_notification_visibility():
                    logger.info("Successfully verified that notification type is disabled for snmpv2")
                    if not VerifyLogicalInterconnectGroups.view_snmpv3_trap_destination_snmp_user_visibility():
                        logger.info("Successfully verified that users are disabled for snmpv2")
            else:
                logger.info("successfully verified that trap format is invisible in FIPS mode")
                CreateLogicalInterconnectGroups.click_add_trap_destination_cancel()
                return True

        elif td_obj.trapformat.lower() == "snmpv3":
            CreateLogicalInterconnectGroups.tick_add_trap_destination_trap_format_snmpv3()
    if hasattr(td_obj, 'notification_type'):
        if td_obj.notification_type == "trap":
            CreateLogicalInterconnectGroups.disable_snmpv3_trap_destination_notification()
        elif td_obj.notification_type == "inform":
            CreateLogicalInterconnectGroups.enable_snmpv3_trap_destination_notification()
    if hasattr(td_obj, 'engineid'):
        CreateLogicalInterconnectGroups.input_add_trap_destination_engine_id(td_obj.engineid)
    if hasattr(td_obj, 'snmp_user'):
        logger.info("user is %s" % td_obj.snmp_user)
        CreateLogicalInterconnectGroups.click_dropdown_snmpv3_user_in_trap_destination()
        list = CreateLogicalInterconnectGroups.get_snmpv3_user_in_trap_destination()
        logger.info("list is %s" % list)
        if td_obj.snmp_user in list:
            logger.info("successfully verified that user is displayed in the list")
        else:
            logger.warn("user is not added in the snmp. Please add a user and then use it in trap destination")
            CreateLogicalInterconnectGroups.click_add_trap_destination_cancel()
            return False
        CreateLogicalInterconnectGroups.select_snmpv3_user_in_trap_destination(td_obj.snmp_user)
    if hasattr(td_obj, 'port'):
        CreateLogicalInterconnectGroups.input_trap_destination_port(td_obj.port)

        # detail configuration for severity, VCM traps etc
    if hasattr(td_obj, 'severity'):
        severity = [item.strip() for item in td_obj.severity.split(',')]
        CreateLogicalInterconnectGroups.click_add_severity()
        for i, severe in enumerate(severity):
            CreateLogicalInterconnectGroups.select_trap_destination_severity(severe)

    if hasattr(td_obj, 'vcm_traps'):
        traps = [item.strip() for item in td_obj.vcm_traps.split(',')]
        CreateLogicalInterconnectGroups.click_add_vcm_traps()
        for i, trap in enumerate(traps):
            CreateLogicalInterconnectGroups.select_trap_destination_vcm_trap(trap)

    if hasattr(td_obj, 'enet_traps'):
        enet_traps = [item.strip() for item in td_obj.enet_traps.split(',')]
        CreateLogicalInterconnectGroups.click_add_vc_enet_traps()
        for i, trap in enumerate(enet_traps):
            CreateLogicalInterconnectGroups.select_trap_destination_vc_enet_traps(trap)

    if hasattr(td_obj, 'fc_traps'):
        fc_traps = [item.strip() for item in td_obj.fc_traps.split(',')]
        CreateLogicalInterconnectGroups.click_add_vc_fc_traps()
        for i, trap in enumerate(fc_traps):
            CreateLogicalInterconnectGroups.select_trap_destination_vc_fc_traps(trap)
    if td_obj.action == "add":
        CreateLogicalInterconnectGroups.click_add_trap_destination_add()
    elif td_obj.action == "edit":
        EditLogicalInterconnectGroups.click_edit_trap_destination_ok()
    elif td_obj.action == "add_plus":
        CreateLogicalInterconnectGroups.click_add_trap_destination_add_plus()

        logger.info("edited successfully")
    if hasattr(td_obj, 'trap_error'):
        max_trap_error = td_obj.trap_error + "\n" + td_obj.resolution
        if VerifyLogicalInterconnectGroups.verify_max_trap_error_message(max_trap_error):
            CreateLogicalInterconnectGroups.click_add_trap_destination_cancel()
            error_flag += 1
            return error_flag
    elif hasattr(td_obj, 'snmp_user_error'):
        if VerifyLogicalInterconnectGroups.verify_no_snmp_user_error_msg(td_obj.snmp_user_error):
            CreateLogicalInterconnectGroups.click_add_trap_destination_cancel()

    elif hasattr(td_obj, 'port_error'):
        if VerifyLogicalInterconnectGroups.verify_invalid_port_error(td_obj.port_error):
            CreateLogicalInterconnectGroups.click_add_trap_destination_cancel()

    elif hasattr(td_obj, 'engineid_error'):
        if VerifyLogicalInterconnectGroups.verify_invalid_engine_id_error(td_obj.engineid_error):
            CreateLogicalInterconnectGroups.click_add_trap_destination_cancel()

    return True


def __edit_lig_remove_snmp_user(remove_obj):
    ''' Removes existing snmp users
    <remove_snmpuser
    user*        -- snmpv3 username
    remove_error -- throws appropriate error in the UI page if the users attempts to remove a snmpv3user
                    that is currently used in any of the trap destination
    resolution   -- Resolution steps provided in the UI page to remove the snmpv3user  when user try remove a snmpv3
                     user currently held in any of the trap destination
    * Required Arguments

    Examples:


        <remove_snmpuser user="user2" remove_error="user2 cannot be removed while it is being used by one or more trap destinations."
            resolution="Remove the associated trap destinations first and try again. Alternatively, edit the trap destinations
            to specify a different user and try again.">
        </remove_snmpuser>

        <remove_snmpuser user="user1"></remove_snmpuser>
        <remove_snmpuser user="user1" traps_associated="192.168.147.12,192.168.147.15"></remove_snmpuser>

    '''

    logger.info("Remove snmp user with user '{0}'".format(remove_obj.user))
    EditLogicalInterconnectGroups.click_remove_snmp_user_icon(remove_obj.user)
    VerifyLogicalInterconnectGroups.wait_remove_snmp_user_confirm_dialog_shown()
    if hasattr(remove_obj, 'remove_error'):
        remove_error = remove_obj.remove_error + "\n" + "\n" + remove_obj.resolution
        if VerifyLogicalInterconnectGroups.verify_remove_snmpv3_user_error(remove_error):
            CreateLogicalInterconnectGroups.click_snmp_error_close_button()
    elif hasattr(remove_obj, 'traps_associated'):
        CreateLogicalInterconnectGroups.click_traps_associated()
        text = CreateLogicalInterconnectGroups.get_text_associated_trap_destination()
        logger.info("traps associated with the user are %s" % text)
        traps = [item.strip() for item in remove_obj.traps_associated.split(',')]
        for i, trap in enumerate(traps):
            logger.info("trap is %s" % trap)
            VerifyLogicalInterconnectGroups.verify_snmpv3_trap_associated_user(trap)
        CreateLogicalInterconnectGroups.click_snmp_error_close_button()

    else:
        EditLogicalInterconnectGroups.click_remove_snmp_user_confirm()
        VerifyLogicalInterconnectGroups.wait_remove_snmp_user_confirm_dialog_disappear()
        VerifyLogicalInterconnectGroups.wait_snmp_user_table_disappear(remove_obj.user)
        return True


def __edit_lig_edit_snmp_user(usr_obj):
    ''' Edits exisiting snmpv3 users
        <edit_snmpuser
        username*                   --  Snmpv3 user name
        security_level             --  Security level to be chosen for user.values can be none, authentication or authenticationandprivacy
        auth_protocol               --  authentication protocol to be provided if user chooses
                                        authentication or authenticationandprivacy as security level.
       authentication_password      --  password for authentication protocol.Must be 8-31 alphanumeric characters
       confirm_auth_password        --  password set for authentication_password should be passed
       priv_protocol                --  privacy protocol to be provided if user chooses
                                        authenticationandprivacy as security level
        privacy_password            --  password for privacy protocol.Must be 8-31 alphanumeric characters
       confirm_priv_password        --  password set for privacy_password should be passed
         * Required Arguments

         Examples:
         <edit_snmpuser username= "user1"  security_level="none"></edit_snmpuser>

        <edit_snmpuser username= "user3"  security_level="authentication" auth_protocol="MD5"
        authentication_password="Password1" confirm_auth_password="Password1"></edit_snmpuser>

        <edit_snmpuser username= "user6"
              security_level="authenticationandprivacy" auth_protocol="MD5"
              authentication_password="Password1" confirm_auth_password="Password1"
              priv_protocol="AES-128" privacy_password="Password2"
              confirm_priv_password="Password2"></edit_snmpuser>
    '''

    logger.info("Editing SNMP USer %s " % usr_obj.username)
    EditLogicalInterconnectGroups.click_edit_snmp_user(usr_obj.username)
    VerifyLogicalInterconnectGroups.wait_edit_snmp_user_confirm_dialog_shown()
    __add_user(usr_obj)
    return True


def __edit_lig_edit_snmpv3_trap_destination(td_obj):
    '''
     Edits trap destination for snmpv3
    <edit_trapdestination>
    trapdestination*   --  Trap Destination for snmpv3
    new_trapdestination -- New trap destination
    trapformat*        --  Trap Format. Possible value: SNMPv1|SNMPv2|SNMPv3
    notification_type --  Whether to enable notification type, Possible value : TRAP|INFORM.Applicable only for Trap Format snmpv3.

   snmp_user           --  To choose the snmpv3 user. If not, default user will be selected.Applicable only for Trap Format snmpv3.
   port                --  Port configuration
   engineid
   communitystring     --  Optional,Community string as string value. Applicable only for Trap Formats snmpv1 and snmpv2.
   severity            --  Sets severity of the trap. possible values are:
                            Critical-> The SNMP manager cannot manage installed components.
                            Major->One or more of the component's subsystems is not operating properly, causing serious disruption to functions.
                            Minor->One or more of the component's subsystems is not operating properly, causing slight disruption to functions.
                            Warning-> The component has a potential problem.
                            Normal->The component is fully functional.
                            Info->Operational information on the fully functioning component.
                            Unknown->The SNMP manager has not yet established communication with the component.
   vcm_traps           --   Trap category for VCM (Virtual Connect Manager) possible values are:
                                Legacy ->When the software changes status, configuration status, or redundancy mode.
    enet_traps         --  Ethernet Trap Categories. Possible values are:
                              Port Status ->When a link changes from being up or down.
                              Port Thresholds->Throughput utilization thresholds are exceeded.
                              Other->Authentication failures.
   fc_traps            --  Fiber Channel trap categories. Possible values are:
                            Port Status->When a link changes from being up or down.
                            Other->Authentication failures.
   </edit_trapdestination>
     * Required Arguments

     Examples:
     <edit_trapdestination trapdestination= "10.101.11.14" new_trapdestionation="10.1.1.1" trapformat="snmpv3" notification_type="Trap"  snmp_user="user5" ></edit_trapdestination>
     <edit_trapdestination trapdestination= "10.101.11.15"  trapformat="snmpv3" port="165" notification_type="Inform" engineid="0XFFFFfffffffff" snmp_user="user5" vcm_traps="legacy"
     enet_traps="Port status, Other" fc_traps="Port status, Other"  ></edit_trapdestination>

          <edit_trapdestination trapdestination= "10.101.11.16"  trapformat="snmpv2" communitystring="public"
          severity="Crtical, Major" vcm_traps="legacy" enet_traps="Port status, Other" fc_traps="Port status, Other"  ></edit_trapdestination>
         vcm_traps

    '''
    logger.info("- Edit Trap Destination settings")
    EditLogicalInterconnectGroups.click_edit_trap_destination_icon(td_obj.trapdestination)
    EditLogicalInterconnectGroups.wait_edit_trap_destination_dialog_shown()
    if hasattr(td_obj, 'new_trapdestination'):
        CreateLogicalInterconnectGroups.input_add_trap_destination_trap_destination(td_obj.new_trapdestination)
    __add_trap_values(td_obj)
    return True


def __edit_lig_remove_snmpv3_trap_destination(remove_obj):
    ''' Removes existing trap destination

    <remove_snmpv3_trapdestination
    trapdestination*        -- snmpv3 trapdestination

    * Required Arguments

    Example:

   <remove_snmpv3_trapdestination trapdestination="10.101.11.1" ></remove_snmpv3_trapdestination>

    '''

    logger.info("Remove snmpv3 trap destination with Destination '{0}'".format(remove_obj.trapdestination))
    C7000EditLogicalInterconnectGroups.click_remove_snmpv3_trap_destination_icon(remove_obj.trapdestination)
    VerifyLogicalInterconnectGroups.wait_remove_snmpv3_trap_destination_confirm_dialog_shown()
    EditLogicalInterconnectGroups.click_remove_trap_destination_yes_remove()
    VerifyLogicalInterconnectGroups.wait_remove_snmpv3_trap_destination_confirm_dialog_disappear()
    EditLogicalInterconnectGroups.wait_trap_destination_table_row_disappear(remove_obj.trapdestination)

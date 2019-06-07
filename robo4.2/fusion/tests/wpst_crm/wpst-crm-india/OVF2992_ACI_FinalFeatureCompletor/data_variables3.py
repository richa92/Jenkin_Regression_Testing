from robot.libraries.BuiltIn import BuiltIn
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

# FM Test Variables
fm_variables = {
    "FM_Name": "FVT-ACI",
    "FM_Tenant_name": "Auto_Tenant_TestSet2",
    "ApplicationProfile_Name": "Auto_Appl_Profile_TestSet_NEW",
    "EPG_Name": "Auto_EPG_TestSet_NEW",
    "VmmDomain_Name": "Automation_Wipro_VMM",
    "PC_Name": "",
    "vPC_Name": "Automation_VPC",
    "MicroSegmentedEPG_Name": "epg_microSeg",
    "IntraEPGIsolation_Name": "epg_isolstion6",
    # Compliance Test Variables
    # Uplink Sets Inconsistency related vlans
    "us_unexpected_nw_present": ["1700"],
    "us_expected_nw_absent": ["1600"],
    # Uplink Sets Inconsistency related vlans
    "ns_unexpected_nw_present": ["100", "101"],
    "ns_expected_nw_absent": ["1200", "15", "1600", "508", "510", "511", "520"],
}
# APIC related data

APIC_URL = "https://192.168.144.114"
APIC_USERNAME = "admin"
APIC_PASSWORD = "password"
tenantes = ["Tenant1", "Tenant2", "Tenant2"]

tenants_details = {"tenant_name": fm_variables['FM_Tenant_name'], "ApProfile_name": fm_variables['ApplicationProfile_Name'], "epg_name": fm_variables['EPG_Name'], "BD_name": "Test_bd", "VRF_name": "VRF_name"}

vmmDomain_data = {"vmmDomain_name": "Automation_Wipro_VMM"}

INTERFACE_Details = {'type': 'eth', 'pod': '1', 'node': '101', 'module': '1', 'port': '40'}

VLAN_Details = {'name': 'vlan506', 'encap_type': 'vlan', 'encap_id': '506'}
# OneView Related Data
PC_INTERFACE1_Details = {'type': 'eth', 'pod': '1', 'node': '101', 'module': '1', 'port': '29'}
PC_INTERFACE2_Details = {'type': 'eth', 'pod': '1', 'node': '101', 'module': '1', 'port': '29'}
PC_VLAN_Details = {'name': 'vlan512', 'encap_type': 'vlan', 'encap_id': '512', 'PC_name': 'PortChannelFMTest512'}

vPC_INTERFACE1_Details = {'type': 'eth', 'pod': '1', 'node': '101', 'module': '1', 'port': '29'}
vPC_INTERFACE2_Details = {'type': 'eth', 'pod': '1', 'node': '102', 'module': '1', 'port': '29'}
vPC_VLAN_Details = {'name': 'vlan513', 'encap_type': 'vlan', 'encap_id': '513', 'vPC_name': 'FMTestvPCTest'}

vPC_details_url = {"tenant_name": fm_variables['FM_Tenant_name'], "ApProfile_name": fm_variables['FM_Tenant_name'], "epg_name": fm_variables['FM_Tenant_name'], "vlan": "520", "policygrp": fm_variables['vPC_Name']}
PC_details_url = {"tenant_name": fm_variables['FM_Tenant_name'], "ApProfile_name": "Auto_Appl_Profile_TestSet2", "epg_name": "Auto_EPG_TestSet2", "vlan": "521", "policygrp": "RV_ACI_NS_PC_15_17", "node": "101"}

# OneView Setup data
ethernet_networks_present = [
    # Uplink Sets Inconsistency related networks
    {'name': 'us_unexpected_nw_present_1', 'vlanId': fm_variables['us_unexpected_nw_present'][0], 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
    # Network Sets Inconsistency related networks
    {'name': 'ns_unexpected_nw_present_1', 'vlanId': fm_variables['ns_unexpected_nw_present'][0], 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
    {'name': 'ns_unexpected_nw_present_2', 'vlanId': fm_variables['ns_unexpected_nw_present'][1], 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
]

ethernet_networks_absent = [
    {'name': 'us_expected_nw_absent_1', 'vlanId': fm_variables['us_expected_nw_absent'][0], 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
    {'name': 'ns_expected_nw_absent_1', 'vlanId': fm_variables['ns_expected_nw_absent'][0], 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
    {'name': 'ns_expected_nw_absent_2', 'vlanId': fm_variables['ns_expected_nw_absent'][1], 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
]
uplink_sets = {
    'US1': {'name': 'US-FM', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['us_unexpected_nw_present_1', 'us_unexpected_nw_present_2', 'ns_unexpected_nw_present_1', 'ns_unexpected_nw_present_2'], 'mode': 'Auto',
            'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1:1', 'speed': 'Auto'},
                                       ]
            },
    'US_Inconsistent_Ports': {'name': 'US-FM', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['us_unexpected_nw_present_1', 'us_unexpected_nw_present_2', 'ns_unexpected_nw_present_1', 'ns_unexpected_nw_present_2'], 'mode': 'Auto',
                              'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1:1', 'speed': 'Auto'},
                                                         {'enclosure': '1', 'bay': '3', 'port': 'Q1:3', 'speed': 'Auto'},
                                                         ]
                              },
}

ligs = {"name": "LIG-FM",
        "type": "logical-interconnect-groupV4",
        "enclosureType": "SY12000",
        "ethernetSettings": {'type': 'EthernetInterconnectSettingsV201', 'interconnectType': 'Ethernet', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5,
                             'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True},
        "description": None,
        "status": None,
        "state": None,
        "category": None,
        "created": None,
        "modified": None,
        "eTag": None,
        "uri": None,
        "uplinkSets": [uplink_sets['US1'].copy(),
                       ],
        'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                    ],
        "internalNetworkUris": [],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantASide',
        'enclosureIndexes': [1],
        "qosConfiguration": {"activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough", "downlinkClassificationType": None, "uplinkClassificationType": None, "qosTrafficClassifiers": None, "description": None, "status": None, "name": None, "state": None, "category": "qos-aggregated-configuration", "created": None, "modified": None, "eTag": None, "uri": None}, "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None, "type": "qos-aggregated-configuration", "name": None, "state": None, "status": None, "eTag": None, "modified": None, "created": None, "category": "qos-aggregated-configuration", "uri": None}}

encl_group = [{"name": "EG-FM",
               "interconnectBayMappings": [{"interconnectBay": 3,
                                            "logicalInterconnectGroupUri": "LIG:LIG-FM"}],
               "configurationScript": "",
               "powerMode": "RedundantPowerFeed",
               "ipAddressingMode": "DHCP",
               "ipRangeUris": [],
               "enclosureCount": 1}]

logical_encl = [{"name": "LE",
                 "enclosureUris": ["ENC:SGH734VBEB"],
                 "enclosureGroupUri": "EG:EG-FM",
                 "firmwareBaselineUri": None,
                 "forceInstallFirmware": False}]

network_sets_update_add = [{'name': 'netset1', 'add_networkUris': ['ns_unexpected_nw_present_1']}]

network_sets_update_delete = [{'name': 'netset1', 'delete_networkUris': ['ns_expected_nw_absent_1']}]

fabric_manager_create = {"name": fm_variables['FM_Name'],
                         "fabricManagerType": "Cisco ACI",
                         "userName": "admin",
                         "password": "password",
                         "fabricManagerClusterNodeInfo": [{"oobMgmtAddr": "192.168.144.114"}],
                         "type": "FabricManager"}

fabric_manager_add_tenant = {"name": fm_variables['FM_Name'],
                             "fabricManagerType": "Cisco ACI",
                             "userName": "admin",
                             "password": "",
                             "fabricManagerClusterNodeInfo": [{"oobMgmtAddr": "192.168.144.114"}],
                             "type": "FabricManager",
                             "tenants": [
    {"name": fm_variables['FM_Tenant_name'], "uri": "", "type": "Tenant", "monitored": "true"},
]
}
fabric_manager_remove_tenant = {"name": "FVT-ACI2",
                                "fabricManagerType": "Cisco ACI",
                                "userName": "admin",
                                "password": "password",
                                "fabricManagerClusterNodeInfo": [{"oobMgmtAddr": "192.168.144.114"}],
                                "type": "FabricManager",
                                "tenants": [
                                    {"name": fm_variables['FM_Tenant_name'], "uri": "", "type": "Tenant", "monitored": "true"},
                                ]
                                }

fabric_manager_alerts = {"Test": tenants_details.get('tenant_name'),
                         "EPG_Not_Associated": 'For tenant "' + tenants_details.get('tenant_name') + '", EPG ' + tenants_details.get('epg_name') + ' is not associated with any interface/domain.',
                         "Intra_EPG_Not_Supported": 'Intra EPG configuration for ' + tenants_details.get('tenant_name') + ': ' + tenants_details.get('epg_name') + ' is not supported.',
                         "Micro_Segmented_EPG_Not_Supported": 'Micro segmented EPG common: ' + tenants_details.get('epg_name') + ' is not supported',
                         "": 'For tenant "' + tenants_details.get('tenant_name') + '", VLAN rsdomAtt-[uni/vmmp-VMware/dom-FVT_DVS] of the EPG ' + tenants_details.get('epg_name') + 'should have Fabric interface(s)',
                         "Tenant_EPG_Not_Compliant": 'For tenant "' + tenants_details.get('tenant_name') + '", EPG ' + tenants_details.get('epg_name') + ' associated with interfaces [101:eth1/17, 101:eth1/27, 102:eth1/17] are not compliant with leaf profile.',
                         "Application_Profile_Missing": 'No Application Profile available for the tenant "' + tenants_details.get('tenant_name') + '".',
                         "LLDP_TAG_DISABLED": '',
                         "NS_Missing": '',
                         "NS_Remove_Vlan": '',
                         "NS_Missing_Vlan": '',
                         "US_NW_Missing": '',
                         "US_NW_Remove": '',
                         "Manual_Uplink_Set_Missing": '',
                         "LI_PORT_Inconsistent": "logical interconnects *LE-LIG-FM* is inconsistent with the fabric manager and requires remediation.",
                         "FM_Tenant_Auto_Delete": "Tenant '" + fm_variables['FM_Tenant_name'] + "' of fabric manager '" + fm_variables['FM_Name'] + "' has been deleted.",
                         "FM_Tenant_Missing_AP": 'No application profile available for the tenant ' + fm_variables['FM_Tenant_name'] + '.',
                         "FM_Tenant_AP_Missing_EPG": 'For tenant ' + fm_variables['FM_Tenant_name'] + ', no EPG is created with the application profile ' + fm_variables['ApplicationProfile_Name'] + '.',
                         "FM_Tenant_AP_EPG_Missing_Interfaces": 'For tenant ' + fm_variables['FM_Tenant_name'] + ', VLAN ' + fm_variables['VmmDomain_Name'] + ' of the EPG ' + fm_variables['EPG_Name'] + ' should have Fabric interface(s).',
                         "FM_CDP_Inconsistency": "For leaf profile group " + fm_variables['vPC_Name'] + ", CDP policy should be disabled.",
                         "FM_LLDP_Inconsistency": "For leaf profile group " + fm_variables['vPC_Name'] + ", LLDP bidirectional policy should be enabled.",
                         "FM_LACP_Inconsistency": "For leaf profile group " + fm_variables['vPC_Name'] + ", port channel policy should be set to LACP Active.",
                         "FM_MicroSegmenetedEPG_Inconsistency": "Micro segmented EPG " + fm_variables['FM_Tenant_name'] + ": " + fm_variables['MicroSegmentedEPG_Name'] + " is not supported.",
                         "FM_IntraEPGIsolation_Inconsistency": "Intra EPG configuration for " + fm_variables['FM_Tenant_name'] + ": " + fm_variables['IntraEPGIsolation_Name'] + " is not supported.",
                         "FM_VMMDomain_NoVLAN_Range": 'For tenant ' + fm_variables['FM_Tenant_name'] + ', domain Automation_No_VlanRange of the EPG ' + fm_variables['EPG_Name'] + ' should have fabric interface(s).',
                         "FM_VMMDomain_NoVLAN_Pool": 'For tenant ' + fm_variables['FM_Tenant_name'] + ', domain Automation_No_VlanPool of the EPG ' + fm_variables['EPG_Name'] + ' should have fabric interface(s).',

                         }

fm_inconsistencies = {"NS_Missing": "VLAN(s)  " + ', '.join(fm_variables['ns_expected_nw_absent']) + " missing.",
                      "LLDP_TAG_DISABLED": "LLDP tagging not enabled.",
                      "US_NW_Missing": "VLAN 2 not expected.",
                      "NS_Remove_Vlan": "VLAN(s)  " + fm_variables['ns_unexpected_nw_present'][0] + " not expected.",
                      "NS_Missing_Vlan": "VLAN(s)  " + fm_variables['ns_expected_nw_absent'][0] + " missing."
                      }
fm_inconsistencies2 = {"NS_Missing": {"inconsistency": "VLAN(s)  " + ', '.join(fm_variables['ns_expected_nw_absent']) + " missing.", "autoRemediate": "true"},
                       "LLDP_TAG_DISABLED": {"inconsistency": "LLDP tagging not enabled.", "autoRemediate": "True"},
                       "US_NW_Missing": {"inconsistency": "VLAN " + ', '.join(fm_variables['us_expected_nw_absent']) + " missing.", "autoRemediate": "True"},
                       "US_NW_Remove": {"inconsistency": "VLAN " + ', '.join(fm_variables['us_unexpected_nw_present']) + " not expected.", "autoRemediate": "True"},
                       "NS_Remove_Vlan": {"inconsistency": "VLAN(s)  " + fm_variables['ns_unexpected_nw_present'][0] + " not expected.", "autoRemediate": "true"},
                       "NS_Missing_Vlan": {"inconsistency": "VLAN(s)  " + fm_variables['ns_expected_nw_absent'][0] + " missing.", "autoRemediate": "true"},
                       "Manual_Uplink_Set_Missing": {"inconsistency": "An Uplink Set is missing.", "autoRemediate": "false", "policyGroup": "topology/pod-1/paths-101/pathep-[eth1/31]"},
                       "Manual_US_Missing_PortGroup": {"inconsistency": "An Uplink Set is missing.", "autoRemediate": "False", "resolution": "Create an uplink Set of type Tagged Ethernet in a Logical Interconnect.<br>Uplink Set should contain Network(s) with VLAN(s)  506 .<br>Uplink Set should contain Port(s) connected to <br>topology/pod-1/paths-101/pathep-[eth1/40]."},
                       "Manual_US_Missing_PortChannel": {"inconsistency": "An Uplink Set is missing.", "autoRemediate": "False", "resolution": "Create an uplink Set of type Tagged Ethernet in a Logical Interconnect.<br>Uplink Set should contain Network(s) with VLAN(s)  521 .<br>Uplink Set should contain Port(s) connected to <br>topology/pod-1/node-102/sys/phys-[eth1/15]."},
                       "Manual_US_Missing_VirtualPortChannel": {"inconsistency": "An Uplink Set is missing.", "autoRemediate": "False", "resolution": "Create an uplink Set of type Tagged Ethernet in a Logical Interconnect.<br>Uplink Set should contain Network(s) with VLAN(s)  520 .<br>Uplink Set should contain Port(s) connected to <br>topology/pod-1/node-102/sys/phys-[eth1/29],<br>topology/pod-1/node-101/sys/phys-[eth1/29]."},
                       "Manual_US_Unexpexted_Port": {"inconsistency": "Unexpected port.", "autoRemediate": "False", "uplinkPortName": "Q1:3"},
                       }
CERT_BODY = {'type': "CertificateInfoV2", 'certificateDetails': [{'base64Data': '', 'aliasName': '', 'type': "CertificateDetailV2"}]}

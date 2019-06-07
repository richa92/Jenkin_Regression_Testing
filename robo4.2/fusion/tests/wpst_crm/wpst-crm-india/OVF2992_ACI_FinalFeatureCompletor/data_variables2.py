from robot.libraries.BuiltIn import BuiltIn
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

# APIC related data

APIC_URL = "https://192.168.144.114"
APIC_USERNAME = "admin"
APIC_PASSWORD = "password"
tenantes = ["Tenant1", "Tenant2", "Tenant2"]

tenants_details = {"tenant_name": "Automation_Tenant_Wipro", "ApProfile_name": "Automation_Wipro_Appl_Profile", "epg_name": "Automation_Wipro_EPG", "BD_name": "Test_bd", "VRF_name": "VRF_name"}

vmmDomain_data = {"vmmDomain_name": "Automation_Wipro_VMM"}

INTERFACE_Details = {'type': 'eth', 'pod': '1', 'node': '101', 'module': '1', 'port': '40'}

VLAN_Details = {'name': 'vlan532', 'encap_type': 'vlan', 'encap_id': '532'}
# OneView Related Data
PC_INTERFACE1_Details = {'type': 'eth', 'pod': '1', 'node': '101', 'module': '1', 'port': '29'}
PC_INTERFACE2_Details = {'type': 'eth', 'pod': '1', 'node': '101', 'module': '1', 'port': '29'}
PC_VLAN_Details = {'name': 'vlan512', 'encap_type': 'vlan', 'encap_id': '512', 'PC_name': 'PortChannelFMTest512'}

vPC_INTERFACE1_Details = {'type': 'eth', 'pod': '1', 'node': '101', 'module': '1', 'port': '29'}
vPC_INTERFACE2_Details = {'type': 'eth', 'pod': '1', 'node': '102', 'module': '1', 'port': '29'}
vPC_VLAN_Details = {'name': 'vlan513', 'encap_type': 'vlan', 'encap_id': '513', 'vPC_name': 'FMTestvPCTest'}

vPC_details_url = {"tenant_name": "Automation_Tenant_Wipro", "ApProfile_name": "Automation_Wipro_Appl_Profile", "epg_name": "Automation_Wipro_EPG", "vlan": "520", "policygrp": "RV_VPC_Policy_Group"}
PC_details_url = {"tenant_name": "Automation_Tenant_Wipro", "ApProfile_name": "Automation_Wipro_Appl_Profile", "epg_name": "Automation_Wipro_EPG", "vlan": "521", "policygrp": "Pol_GRP1_PC_fvt_AP1_VMM111", "node": "101"}

fm_variables = {
    # Compliance Test Variables
    # Uplink Sets Inconsistency related vlans
    "us_unexpected_nw_present": ["1700"],
    "us_expected_nw_absent": ["1600"],
    # Uplink Sets Inconsistency related vlans
    "ns_unexpected_nw_present": ["100", "101"],
    "ns_expected_nw_absent": ["1200", "15", "1600", "508", "510", "511", "520"],
    "FM_Edit_Tenant_name": "Automation_Tenant_Wipro"
}
ethernet_networks_present = [
    # Uplink Sets Inconsistency related networks
    {'name': 'us_unexpected_nw_present_1', 'vlanId': fm_variables['us_unexpected_nw_present'][0], 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
    # Network Sets Inconsistency related networks
    {'name': 'ns_unexpected_nw_present_1', 'vlanId': fm_variables['ns_unexpected_nw_present'][0], 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
    {'name': 'ns_unexpected_nw_present_2', 'vlanId': fm_variables['ns_unexpected_nw_present'][1], 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
    {'name': 'Network_Tunnel', 'vlanId': 0, 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tunnel', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
]

ethernet_networks_absent = [
    {'name': 'us_expected_nw_absent_1', 'vlanId': fm_variables['us_expected_nw_absent'][0], 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},

    {'name': 'ns_expected_nw_absent_1', 'vlanId': fm_variables['ns_expected_nw_absent'][0], 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
    {'name': 'ns_expected_nw_absent_2', 'vlanId': fm_variables['ns_expected_nw_absent'][1], 'purpose': 'General', 'smartLink': 'false', 'privateNetwork': 'false', 'ethernetNetworkType': 'Tagged', 'type': 'ethernet-networkV4', 'connectionTemplateUri': None},
]

uplink_sets = {
    'US1': {'name': 'US-FM', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['us_unexpected_nw_present_1', 'us_unexpected_nw_present_2'], 'mode': 'Auto',
            'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1:1', 'speed': 'Auto'},
                                       {'enclosure': '1', 'bay': '6', 'port': 'Q1:1', 'speed': 'Auto'}
                                       ]
            },
    'US_Inconsistent_Ports': {'name': 'US-FM', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['us_unexpected_nw_present_1', 'us_unexpected_nw_present_2'], 'mode': 'Auto',
                              'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1:1', 'speed': 'Auto'},
                                                         {'enclosure': '1', 'bay': '6', 'port': 'Q1:1', 'speed': 'Auto'},
                                                         {'enclosure': '1', 'bay': '3', 'port': 'Q1:3', 'speed': 'Auto'},
                                                         ]
                              },
    'US_Tunnel': {'name': 'US-Tunnel', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tunnel', 'networkUris': ['Network_Tunnel'], 'mode': 'Auto',
                  'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1:1', 'speed': 'Auto'},
                                             {'enclosure': '1', 'bay': '6', 'port': 'Q1:1', 'speed': 'Auto'}
                                             ]
                  },
    'US_Tunnel_No_Network': {'name': 'US-Tunnel_No_Network', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tunnel', 'networkUris': [], 'mode': 'Auto',
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1:1', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '6', 'port': 'Q1:1', 'speed': 'Auto'}
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
        "uplinkSets": [uplink_sets['US1'].copy()],
        'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                    {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                    ],
        "internalNetworkUris": [],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'enclosureIndexes': [1],
        "qosConfiguration": {"activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough", "downlinkClassificationType": None, "uplinkClassificationType": None, "qosTrafficClassifiers": None, "description": None, "status": None, "name": None, "state": None, "category": "qos-aggregated-configuration", "created": None, "modified": None, "eTag": None, "uri": None}, "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None, "type": "qos-aggregated-configuration", "name": None, "state": None, "status": None, "eTag": None, "modified": None, "created": None, "category": "qos-aggregated-configuration", "uri": None}}

encl_group = [{"name": "EG-FM",
               "interconnectBayMappings": [{"interconnectBay": 3,
                                            "logicalInterconnectGroupUri": "LIG:LIG-FM"},
                                           {"interconnectBay": 6,
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

fabric_manager_create = {"name": "FVT-ACI",
                         "fabricManagerType": "Cisco ACI",
                         "userName": "admin",
                         "password": "password",
                         "fabricManagerClusterNodeInfo": [{"oobMgmtAddr": "192.168.144.114"}],
                         "type": "FabricManager"}

fabric_manager_edit = {"name": "FVT-ACI",
                       "fabricManagerType": "Cisco ACI",
                       "userName": "admin",
                       "password": "",
                       "fabricManagerClusterNodeInfo": [{"oobMgmtAddr": "192.168.144.114"}],
                       "type": "FabricManager",
                       "tenants": [
                                   {"name": fm_variables['FM_Edit_Tenant_name'], "uri": "", "type": "Tenant", "monitored": "true"},
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
                         "NS_Missing": "",
                         "NS_Remove_Vlan": "Network set *NS_DVS-dom-Automation_Wipro_VMM* is inconsistent with the fabric manager and requires remediation.",
                         "NS_Missing_Vlan": "Network set *NS_DVS-dom-Automation_Wipro_VMM* is inconsistent with the fabric manager and requires remediation.",
                         "US_NW_Missing": '',
                         "US_NW_Remove": '',
                         "Manual_Uplink_Set_Missing": '',
                         "LI_PORT_Inconsistent": "Logical interconnect *LE-LIG-FM* is inconsistent with the fabric manager and requires remediation.",
                         }

fabric_manager_compliance = {"tenants": [{"tenantUri": "/rest/fabric-managers/a2e966a6-fc5c-4d9c-b76c-f4e65592e038/tenants/ecbb5633-af77-46d7-980e-9856b034ddd5",
                                          "networkSets": ["813319d8-31d1-477e-8ebe-c39d8aa52155"],
                                          "logicalInterconnects": []}
                                         ],
                             "type": "RemediateFabricManager"
                             }

fm_inconsistencies = {"NS_Missing": "VLAN(s)  " + ', '.join(fm_variables['ns_expected_nw_absent']) + " missing.",
                      "LLDP_TAG_DISABLED": "LLDP tagging not enabled.",
                      "US_NW_Missing": "VLAN 2 not expected.",
                      "NS_Remove_Vlan": "VLAN(s)  " + fm_variables['ns_unexpected_nw_present'][0] + " not expected.",
                      "NS_Missing_Vlan": "VLAN(s)  " + fm_variables['ns_expected_nw_absent'][0] + " missing."
                      }
fm_inconsistencies2 = {"NS_Missing": {"inconsistency": "Network set missing", 'resolution': "Create network set containing VLAN(s)  " + ', '.join(fm_variables['ns_expected_nw_absent']) + ".", "remediationAction": "AUTO_ADD"},
                       "LLDP_TAG_DISABLED": {"inconsistency": "LLDP tagging not enabled<br>", "remediationAction": "AUTO_UPDATE"},
                       "US_NW_Missing": {"inconsistency": "VLAN " + ', '.join(fm_variables['us_expected_nw_absent']) + " missing<br>", "remediationAction": "AUTO_ADD"},
                       "US_NW_Remove": {"inconsistency": "VLAN " + ', '.join(fm_variables['us_unexpected_nw_present']) + " not expected<br>", "remediationAction": "AUTO_REMOVE"},
                       "NS_Remove_Vlan": {"inconsistency": "VLAN(s)  " + fm_variables['ns_unexpected_nw_present'][0] + " not expected<br>", "remediationAction": "AUTO_UPDATE"},
                       "NS_Missing_Vlan": {"inconsistency": "VLAN(s)  " + fm_variables['ns_expected_nw_absent'][0] + " missing<br>", "remediationAction": "AUTO_UPDATE"},
                       "Manual_Uplink_Set_Missing": {"inconsistency": "An uplink set is missing<br>", "complianceStatus": "RESOURCE_MISSING", "remediationAction": "MANUAL_UPDATE", "policyGroup": "topology/pod-1/paths-101/pathep-[eth1/3]"},
                       "Manual_US_Missing_PortGroup": {"inconsistency": "An uplink set is missing<br>", "remediationAction": "MANUAL_UPDATE", "policyGroup": "topology/pod-1/paths-101/pathep-[eth1/40]"},
                       #"Manual_US_Missing_PortChannel": {"inconsistency": "An uplink set is missing<br>", "remediationAction": "MANUAL_UPDATE", "policyGroup": "topology/pod-1/paths-101/pathep-[Pol_GRP1_PC_fvt_AP1_VMM111]"},
                       "Manual_US_Missing_PortChannel": {"inconsistency": "An uplink set is missing<br>", "remediationAction": "MANUAL_UPDATE", "policyGroup": "accbundle-VPC_Pol_Bheem_GRP1"},
                       "Manual_US_Missing_VirtualPortChannel": {"inconsistency": "An uplink set is missing<br>", "remediationAction": "MANUAL_UPDATE", "policyGroup": "accbundle-RV_VPC_Policy_Group"},
                       "Manual_US_Unexpexted_Port": {"inconsistency": "Unexpected port<br>", "remediationAction": "MANUAL_REMOVE", "uplinkPortName": "Q1:3"},
                       "Missing_Tunnel_NW": {"inconsistency": "Tunnel network missing in uplink set<br>", "remediationAction": "AUTO_UPDATE", "resolution": "Add tunnel network to uplink set.<br>"}

                       }

CERT_BODY = {'type': "CertificateInfoV2", 'certificateDetails': [{'base64Data': '', 'aliasName': '', 'type': "CertificateDetailV2"}]}

LI_Resource_Mapping = {'CONNECTION_MODE': 'AUTO',
                       'SGH734VBEB, interconnect 3:Q1:1': 'topology/pod-1/node-102/sys/phys-[eth1/31]',
                       'SGH734VBEB, interconnect 6:Q1:1': 'topology/pod-1/node-101/sys/phys-[eth1/31]',
                       'UPLINK_SET_TYPE': 'TAGGED_ETHERNET',
                       'compliantPortCount': 2}

NW_Resource_Mapping = {'ACI_network_1200': '1200',
                       'ACI_network_15': '15',
                       'ACI_network_1600': '1600',
                       'ACI_network_508': '508',
                       'ACI_network_510': '510',
                       'ACI_network_511': '511',
                       'ACI_network_520': '520'}

NW_Set_resource_Mapping = {'NS_DVS-dom-Automation_Wipro_VMM': [15, 508, 510, 511, 520, 1200, 1600]}

Tunnel_LI_No_NW_Resource_Mapping = {'CONNECTION_MODE': 'AUTO',
                                    'SGH734VBEB, interconnect 3:Q1:1': 'topology/pod-1/node-102/sys/phys-[eth1/31]',
                                    'SGH734VBEB, interconnect 6:Q1:1': 'topology/pod-1/node-101/sys/phys-[eth1/31]',
                                    'UPLINK_SET_TYPE': 'TUNNEL',
                                    'compliantPortCount': 2}

Tunnel_LI_Resource_Mapping = {'CONNECTION_MODE': 'AUTO',
                              'SGH734VBEB, interconnect 3:Q1:1': 'topology/pod-1/node-102/sys/phys-[eth1/31]',
                              'SGH734VBEB, interconnect 6:Q1:1': 'topology/pod-1/node-101/sys/phys-[eth1/31]',
                              'UPLINK_SET_TUNNEL_NETWORK': 'ETH:Network_Tunnel',
                              'UPLINK_SET_TYPE': 'TUNNEL',
                              'compliantPortCount': 2}

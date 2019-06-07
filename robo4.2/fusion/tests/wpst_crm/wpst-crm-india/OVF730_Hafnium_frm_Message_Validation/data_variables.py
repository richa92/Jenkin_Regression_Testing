
login_details = {'userName': 'Administrator', 'password': 'hpvse123'}
network_login_details = {'userName': 'network', 'password': 'hpvse123'}
server_login_details = {'userName': 'server', 'password': 'hpvse123'}
storage_login_details = {'userName': 'storage', 'password': 'hpvse123'}
software_login_details = {'userName': 'software', 'password': 'hpvse123'}

users = [{'userName': 'server', 'password': 'hpvse123', 'fullName': 'server', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'network', 'password': 'hpvse123', 'fullName': 'network', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'storage', 'password': 'hpvse123', 'fullName': 'storage', 'roles': ['Storage administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'software', 'password': 'hpvse123', 'fullName': 'software', 'roles': ['Software administrator'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]

ICM_NAME_1 = '0000A66101, interconnect 3'
ICM_NAME_2 = '0000A66101, interconnect 3'

Expected = 'Set Variable   Unable to verify whether firmware update can be performed non-disruptively. Resolution: To minimize disruption during firmware update, ensure NIC teaming/bonding has been configured for failover and link loss detection on the server operating system for all Ethernet connections. If NIC teaming/bonding is not configured, the server may experience network disruption.Also, ensure multipathing has been configured on the server profiles operating systems for the logical interconnect that include FC or FCoE connections. If multipathing has not been configured for an FC or FCoE connection, the firmware update will be disruptive to that connection.'
# REDUNDANTFAILUREMESSAGE= 'Ensure that the following points have been addressed. - Redundancy is available for all the logical interconnect uplinksets. - Multipathing has been configured on the server operating system for FC/FCOE networks. - NIC teaming/bonding has been has been configured for failover and link loss detection on the server operating system for all Ethernet connections. Retry the update after these have been setup correctly to ensure a non disruptive update. Alternatively, power off the server(s) that do not meet the listed criteria'
# REDUNDANTFAILUREMESSAGE= 'Ensure that the following points have been addressed. - Redundancy is available for all the logical interconnect uplinksets. - Multipathing has been configured on the server operating system for FC/FCOE networks. - NIC teaming/bonding has been configured for failover and link loss detection on the server operating system for all Ethernet connections. Retry the update after these have been setup correctly to ensure a non disruptive update. Alternatively, power off the server(s) that do not meet the listed criteria'
REDUNDANTFAILUREMESSAGE = 'Ensure that the following points have been addressed. - Redundancy is available for all the logical interconnect uplinksets. - Multipathing has been configured on the server operating system for FC/FCoE networks. - NIC teaming/bonding has been configured for failover and link loss detection on the server operating system for all Ethernet connections. Retry the update after these have been setup correctly to ensure a non disruptive update. Alternatively, power off the server(s) that do not meet the listed criteria'
FC_ENET = 'To minimize disruption during firmware update, ensure NIC teaming/bonding has been configured for failover and link loss detection on the server operating system for all Ethernet connections. If NIC teaming/bonding is not configured, the server may experience network disruption. Also, ensure multipathing has been configured on the server profiles operating systems for the logical interconnect that include FC or FCoE connections. If multipathing has not been configured for an FC or FCoE connection, the firmware update will be disruptive to that connection.'

upgrade_firmware_path = '/rest/firmware-drivers/cust-K120-36-EM2-Gen10'
# upgrade_firmware_path = '/rest/firmware-drivers/cust-K120-22-Dev-EM2-G10_BB'
# downgrade_firmware_path = '/rest/firmware-drivers/CAR-26-Snap6-bp-Hf115-C26-CLSyl-101-2016-03-09-01'

LIG_Version = 'logical-interconnect-groupV4'
eth_network_Version = 'ethernet-networkV4'
fcoe_network_version = 'fcoe-networkV4'
fc_network_version = 'fc-networkV4'
# FC_Redundant_server
# FC_Not_Redundant_server
# FCOE_Not_Redundant_server
# FCOE_Redundant_server
# ETH_Not_Redundant_server
# ETH_Redundant_server
#
# KC_LIG Guide lines = 'The potash port number while creating uplink set on LIG start from 62 (i.e. Q1.1) till end on Q8
# Example 61 is for Q1 and 62 is for Q1:1 and 63 is for Q1:2
# and for Q2 it is 66 and for Q2:1 is 67
# Q2 - 67
# Q3 - 71
# Q4 - 76
#
EG = [{'name': 'eg',
       'ipAddressingMode': "DHCP",
       'enclosureCount': 3,
       'configurationScript': None,
               'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                                           {'interconnectBay': 2, 'logicalInterconnectGroupUri': "LIG:lig-ibs2"},
                                           {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig-ibs3"},
                                           {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                           {'interconnectBay': 5, 'logicalInterconnectGroupUri': "LIG:lig-ibs2"},
                                           {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig-ibs3"}
                                           ]}]

ENC1 = '0000A66101'
ENC2 = '0000A66102'
ENC3 = '0000A66103'

icmap_ME = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'Synergy 20Gb Interconnect Link Module'},
            {'enclosure': 2, 'enclosureIndex': 2, 'bay': 3, 'type': 'Synergy 20Gb Interconnect Link Module'},
            {'enclosure': 2, 'enclosureIndex': 2, 'bay': 6, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
            {'enclosure': 3, 'enclosureIndex': 3, 'bay': 3, 'type': 'Synergy 20Gb Interconnect Link Module'},
            {'enclosure': 3, 'enclosureIndex': 3, 'bay': 6, 'type': 'Synergy 20Gb Interconnect Link Module'},
            ]

OVF730_lig_3frame_ibs3_ha = {"type": LIG_Version,
                             "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                             "description": None,
                             "name": "LIG_BAY_SET_3",
                             "interconnectMapTemplate": icmap_ME,
                             "enclosureType": "SY12000",
                             "enclosureIndexes": [1, 2, 3],
                             "interconnectBaySet": "3",
                             "redundancyType": "HighlyAvailable",
                             "internalNetworkUris": [],
                             "snmpConfiguration": None,
                             "qosConfiguration": None,
                             "uplinkSets": [
                                 {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["Ethernet100", "Ethernet101"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'},
                                                             {'bay': '6', 'enclosure': '2', 'port': 'Q1.1', 'speed': 'Auto'}]},
                                 {'name': 'us1_eth102', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["Ethernet102", "Ethernet103"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.2', 'speed': 'Auto'},
                                                             {'bay': '6', 'enclosure': '2', 'port': 'Q1.2', 'speed': 'Auto'}]},
                                 {'name': 'us1_eth120', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["Ethernet120", "Ethernet121"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.3', 'speed': 'Auto'}]},
                                 {'name': 'UPL_Untagged', 'ethernetNetworkType': 'Untagged', 'networkType': 'Ethernet', 'networkUris': ["Untagged_Net_1"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.4', 'speed': 'Auto'},
                                                             {'bay': '6', 'enclosure': '2', 'port': 'Q1.4', 'speed': 'Auto'}]},
                                 {'name': 'us2_eth109', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["Ethernet109"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '2', 'port': 'Q2.1', 'speed': 'Auto'}]},
                                 {'name': 'FC1', 'ethernetNetworkType': 'Tagged', 'networkType': 'FibreChannel', 'networkUris': ['FC1'], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q2.2', 'speed': 'Auto'}]},
                                 {'name': 'FC2', 'ethernetNetworkType': 'Tagged', 'networkType': 'FibreChannel', 'networkUris': ['FC2'], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '2', 'port': 'Q2.2', 'speed': 'Auto'}]},
                                 {'name': 'us_fcoe1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["FCOE1"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q2.3', 'speed': 'Auto'}]},
                                 {'name': 'us_fcoe2', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["FCOE2"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '2', 'port': 'Q2.3', 'speed': 'Auto'}]},
                                 {'name': 'UPL_Tunnel', 'ethernetNetworkType': 'Tunnel', 'networkType': 'Ethernet', 'networkUris': ["Tunnel_Net_1"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q2.4', 'speed': 'Auto'},
                                                             {'bay': '6', 'enclosure': '2', 'port': 'Q2.4', 'speed': 'Auto'}, ]},
                             ]}

OVF730_eg_3enc_BaySet2_3_ha = [{'name': 'EG_Temp',
                                'ipAddressingMode': "External",
                                'enclosureCount': 3,
                                'configurationScript': None,
                                'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                                                            {'interconnectBay': 2, 'logicalInterconnectGroupUri': "LIG:LIG_BAY_SET_2"},
                                                            {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:LIG_BAY_SET_3"},
                                                            {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                                            {'interconnectBay': 5, 'logicalInterconnectGroupUri': "LIG:LIG_BAY_SET_2"},
                                                            {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:LIG_BAY_SET_3"}
                                                            ]}]

OVF730_eg_3enc_BaySet3_ha = [{'name': 'EG',
                              'ipAddressingMode': "External",
                              'enclosureCount': 3,
                              'configurationScript': None,
                              'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                                                          {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                                          {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:LIG_BAY_SET_3"},
                                                          {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                                          {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                                          {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:LIG_BAY_SET_3"}
                                                          ]}]

le_2enc_BaySet3_ha = [{'name': 'LE_2frame_BaySet3_HA',
                       'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2],
                       'enclosureGroupUri': 'EG:EG_2frame_BaySet3_HA',
                       'firmwareBaselineUri': None,
                       'forceInstallFirmware': False
                       }]

OVF730_le = [{'name': 'LE',
              'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
              'enclosureGroupUri': 'EG:EG',
              'firmwareBaselineUri': None,
              'forceInstallFirmware': False
              }]


Eth_networks = [{"vlanId": "100", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "Ethernet100", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "101", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "Ethernet101", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "102", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "Ethernet102", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "103", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "Ethernet103", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "104", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "Ethernet104", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "105", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "Ethernet105", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "106", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "Ethernet106", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "107", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "Ethernet107", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "109", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "Ethernet109", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "110", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "Ethernet110", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "120", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "Ethernet120", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "121", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "Ethernet121", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "122", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "Ethernet122", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "123", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "Ethernet123", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "124", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "Ethernet124", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "1", "ethernetNetworkType": "Untagged", "subnetUri": None, "purpose": "General", "name": "Untagged_Net_1", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "1", "ethernetNetworkType": "Tunnel", "subnetUri": None, "purpose": "General", "name": "Tunnel_Net_1", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version}, ]

fc_networks = [{'name': 'FC1', 'type': fc_network_version, 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'FC2', 'type': fc_network_version, 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'FC3', 'type': fc_network_version, 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'FC4', 'type': fc_network_version, 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}
               ]

fcoe_networks = [{'name': 'FCOE1', 'type': fcoe_network_version, 'vlanId': 1001},
                 {'name': 'FCOE2', 'type': fcoe_network_version, 'vlanId': 1002},
                 {'name': 'FCOE3', 'type': fcoe_network_version, 'vlanId': 1003},
                 {'name': 'FCOE4', 'type': fcoe_network_version, 'vlanId': 1004}
                 ]

Eth_range = [{"vlanId": "100-110", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "KC-ETH", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version}]

network_sets = [{'name': 'LAG_Server_UPL_No_LAG', 'type': 'network-setV4', 'networkUris': ['Ethernet110', 'Ethernet105'], 'nativeNetworkUri': None},
                {'name': 'NO_LAG_Redundant_network_set_t', 'type': 'network-setV4', 'networkUris': ['Ethernet110'], 'nativeNetworkUri': None},
                {'name': 'Network_Set_1', 'type': 'network-setV4', 'networkUris': ['Ethernet100'], 'nativeNetworkUri': None},
                {'name': 'Network_Set_2', 'type': 'network-setV4', 'networkUris': ['Ethernet101'], 'nativeNetworkUri': None},
                {'name': 'Server_Networkset_LAG_1', 'type': 'network-setV4', 'networkUris': ['Ethernet100', 'Ethernet101'], 'nativeNetworkUri': None},
                {'name': 'Server_Networkset_LAG_2', 'type': 'network-setV4', 'networkUris': ['Ethernet102', 'Ethernet103'], 'nativeNetworkUri': None},
                {'name': 'Eth_120_121', 'type': 'network-setV4', 'networkUris': ['Ethernet120', 'Ethernet121'], 'nativeNetworkUri': None},
                {'name': 'Uplink-not-redundant_UPL', 'type': 'network-setV4', 'networkUris': ['Ethernet120', 'Ethernet121'], 'nativeNetworkUri': None},
                {'name': 'Uplink-not-redundant_UPL', 'type': 'network-setV4', 'networkUris': ['Ethernet105', 'Ethernet106'], 'nativeNetworkUri': None},
                {'name': 'NO_LAG_Redundant_network_set', 'type': 'network-setV4', 'networkUris': ['Ethernet110'], 'nativeNetworkUri': None}
                ]

t_network_sets = [{'name': 't_LAG_Server_UPL_No_LAG', 'type': 'network-setV4', 'networkUris': ['Ethernet110', 'Ethernet105'], 'nativeNetworkUri': None},
                  {'name': 't_NO_LAG_Redundant_network_set_t', 'type': 'network-setV4', 'networkUris': ['Ethernet110'], 'nativeNetworkUri': None},
                  {'name': 't_Network_Set_1', 'type': 'network-setV4', 'networkUris': ['Ethernet100'], 'nativeNetworkUri': None},
                  {'name': 't_Network_Set_2', 'type': 'network-setV4', 'networkUris': ['Ethernet101'], 'nativeNetworkUri': None},
                  {'name': 't_Server_Networkset_LAG_1', 'type': 'network-setV4', 'networkUris': ['Ethernet100', 'Ethernet101'], 'nativeNetworkUri': None},
                  {'name': 't_Server_Networkset_LAG_2', 'type': 'network-setV4', 'networkUris': ['Ethernet102', 'Ethernet103'], 'nativeNetworkUri': None},
                  {'name': 't_Eth_120_121', 'type': 'network-setV4', 'networkUris': ['Ethernet120', 'Ethernet121'], 'nativeNetworkUri': None},
                  {'name': 't_Uplink-not-redundant_UPL', 'type': 'network-setV4', 'networkUris': ['Ethernet120', 'Ethernet121'], 'nativeNetworkUri': None},
                  {'name': 't_Uplink-not-redundant_UPL', 'type': 'network-setV4', 'networkUris': ['Ethernet105', 'Ethernet106'], 'nativeNetworkUri': None},
                  {'name': 't_NO_LAG_Redundant_network_set', 'type': 'network-setV4', 'networkUris': ['Ethernet110'], 'nativeNetworkUri': None}
                  ]

# network_sets = [{'name': 'Server_Networkset_LAG_1_t', 'type': 'network-setV4', 'networkUris': ['Ethernet100,Ethernet101'], 'nativeNetworkUri': None}]

# network_sets = [{'name': 'netset-vlan100', 'type': 'network-setV4', 'networkUris': ['Ethernet100','Ethernet101'], 'nativeNetworkUri': None, 'connectionTemplateUri': None }]


# Server Profile Data

Redundant_Server_FC_Temp = [{'name': 'Redundant_Server_FC_Temp', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:0000A66102, bay 3', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical', 'description': 'Updated Profile', 'affinity': 'Bay',
                             'connections': [],
                             'boot': {'manageBoot': False},
                             'bootMode': {'manageMode': False},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                             'localStorage': None,
                             'sanStorage': None,
                             'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FC:FC1', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                    {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FC:FC2', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                    ]},
                             }]

Not_Redundant_Server_FC_Temp = [{'name': 'Not_Redundant_Server_FC_Temp', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:0000A66102, bay 4', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical', 'description': 'Updated Profile', 'affinity': 'Bay',
                                 'connections': [],
                                 'boot': {'manageBoot': False},
                                 'bootMode': {'manageMode': False},
                                 'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                 'bios': {'manageBios': False, 'overriddenSettings': []},
                                 'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                                 'localStorage': None,
                                 'sanStorage': None,
                                 'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FC:FC1', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                        ]},
                                 }]

Redundant_Server_FCOE_Temp = [{'name': 'Redundant_Server_FCOE_Temp', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:0000A66102, bay 5', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical', 'description': 'Updated Profile', 'affinity': 'Bay',
                               'connections': [],
                               'boot': {'manageBoot': False},
                               'bootMode': {'manageMode': False},
                               'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                               'bios': {'manageBios': False, 'overriddenSettings': []},
                               'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                               'localStorage': None,
                               'sanStorage': None,
                               'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FCOE:FCOE1', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                      {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FCOE:FCOE2', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                      ]},
                               }]

FCOE_Redundant_Server_Uplink_not_redundant_Temp = [{'name': 'FCOE_Redundant_Server_Uplink_not_redundant_Temp', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:0000A66102, bay 5', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical', 'description': 'Updated Profile', 'affinity': 'Bay',
                                                    'connections': [],
                                                    'boot': {'manageBoot': False},
                                                    'bootMode': {'manageMode': False},
                                                    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                                    'bios': {'manageBios': False, 'overriddenSettings': []},
                                                    'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                                                    'localStorage': None,
                                                    'sanStorage': None,
                                                    'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FCOE:FCOE1', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                                           {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FCOE:FCOE2', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                                           ]},
                                                    }]

Not_Redundant_Server_FCOE_Temp = [{'name': 'Not_Redundant_Server_FCOE_Temp', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:0000A66102, bay 6', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical', 'description': 'Updated Profile', 'affinity': 'Bay',
                                   'connections': [],
                                   'boot': {'manageBoot': False},
                                   'bootMode': {'manageMode': False},
                                   'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                   'bios': {'manageBios': False, 'overriddenSettings': []},
                                   'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                                   'localStorage': None,
                                   'sanStorage': None,
                                   'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FCOE:FCOE1', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                          ]},
                                   }]

Eth_Server_Redundant_Uplink_not_redundant_temp = [{'name': 'Eth_Server_Redundant_Uplink_not_redundant_temp', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:0000A66103, bay 3', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical', 'description': 'Updated Profile', 'affinity': 'Bay',
                                                   'connections': [],
                                                   'boot': {'manageBoot': False},
                                                   'bootMode': {'manageMode': False},
                                                   'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                                   'bios': {'manageBios': False, 'overriddenSettings': []},
                                                   'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                                                   'localStorage': None,
                                                   'sanStorage': None,
                                                   'connectionSettings': {'connections': [{'id': 1, 'name': 'Connection 1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                                                           'requestedMbps': '2500', 'networkUri': 'NS:Uplink-not-redundant_UPL',
                                                                                           'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                                          {'id': 1, 'name': 'Connection 2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                                                           'requestedMbps': '2500', 'networkUri': 'NS:Uplink-not-redundant_UPL',
                                                                                           'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                                          ]},
                                                   }]

LAG_Server_temp = [{'name': 'LAG_Server_temp', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:0000A66101, bay 4', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical', 'description': 'Updated Profile', 'affinity': 'Bay',
                    'connections': [],
                    'boot': {'manageBoot': False},
                    'bootMode': {'manageMode': False},
                    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                    'bios': {'manageBios': False, 'overriddenSettings': []},
                    'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                    'localStorage': None,
                    'sanStorage': None,
                    'connectionSettings': {'connections': [{'id': 1, 'name': 'Connection 1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                            'requestedMbps': '2500', 'networkUri': 'NS:Server_Networkset_LAG_1',
                                                            'mac': None, 'wwpn': '', 'wwnn': '', 'lagName': 'LAG1'},
                                                           {'id': 1, 'name': 'Connection 2', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                            'requestedMbps': '2500', 'networkUri': 'NS:Server_Networkset_LAG_1',
                                                            'mac': None, 'wwpn': '', 'wwnn': '', 'lagName': 'LAG1'},
                                                           ]},
                    }]

Untagged_LAG_Server_temp = [{'name': 'Untagged_LAG_Server_temp', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:0000A66101, bay 11', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical', 'description': 'Updated Profile', 'affinity': 'Bay',
                             'connections': [],
                             'boot': {'manageBoot': False},
                             'bootMode': {'manageMode': False},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                             'localStorage': None,
                             'sanStorage': None,
                             'connectionSettings': {'connections': [{'id': 1, 'name': 'Connection 1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                     'requestedMbps': '2500', 'networkUri': 'ETH:Untagged_Net_1',
                                                                     'mac': None, 'wwpn': '', 'wwnn': '', 'lagName': 'LAG1'},
                                                                    {'id': 1, 'name': 'Connection 2', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                     'requestedMbps': '2500', 'networkUri': 'ETH:Untagged_Net_1',
                                                                     'mac': None, 'wwpn': '', 'wwnn': '', 'lagName': 'LAG1'},
                                                                    ]},
                             }]

Tunnel_LAG_Server_temp = [{'name': 'Tunnel_LAG_Server_tem', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:0000A66101, bay 12', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical', 'description': 'Updated Profile', 'affinity': 'Bay',
                           'connections': [],
                           'boot': {'manageBoot': False},
                           'bootMode': {'manageMode': False},
                           'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                           'bios': {'manageBios': False, 'overriddenSettings': []},
                           'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                           'localStorage': None,
                           'sanStorage': None,
                           'connectionSettings': {'connections': [{'id': 1, 'name': 'Connection 1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                   'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel_Net_1',
                                                                   'mac': None, 'wwpn': '', 'wwnn': '', 'lagName': 'LAG1'},
                                                                  {'id': 1, 'name': 'Connection 2', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                   'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel_Net_1',
                                                                   'mac': None, 'wwpn': '', 'wwnn': '', 'lagName': 'LAG1'},
                                                                  ]},
                           }]

Eth_LAG_Server_UPL_NOLAG_Redundant_temp = [{'name': 'Eth_LAG_Server_UPL_NOLAG_Redundant_temp', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:0000A66102, bay 7', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical', 'description': 'Updated Profile', 'affinity': 'Bay',
                                            'connections': [],
                                            'boot': {'manageBoot': False},
                                            'bootMode': {'manageMode': False},
                                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                            'bios': {'manageBios': False, 'overriddenSettings': []},
                                            'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                                            'localStorage': None,
                                            'sanStorage': None,
                                            'connectionSettings': {'connections': [{'id': 1, 'name': 'Connection 1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                                    'requestedMbps': '2500', 'networkUri': 'NS:LAG_Server_UPL_No_LAG',
                                                                                    'mac': None, 'wwpn': '', 'wwnn': '', 'lagName': 'LAG1'},
                                                                                   {'id': 1, 'name': 'Connection 2', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                                    'requestedMbps': '2500', 'networkUri': 'NS:LAG_Server_UPL_No_LAG',
                                                                                    'mac': None, 'wwpn': '', 'wwnn': '', 'lagName': 'LAG1'},
                                                                                   ]},
                                            }]

temp_server = [{'name': 'Server_temp_server', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:0000A66101, bay 3', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical', 'description': 'Updated Profile', 'affinity': 'Bay',
                        'boot': {'manageBoot': False},
                        'bootMode': {'manageMode': False},
                        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                        'bios': {'manageBios': False, 'overriddenSettings': []},
                        'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                        'localStorage': None,
                        'sanStorage': None,
                        'connectionSettings': {'connections': [{'id': 1, 'name': 'Ethernet100', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                'requestedMbps': '2500', 'networkUri': 'NS:Server_Networkset_LAG_1',
                                                                'mac': None, 'wwpn': '', 'wwnn': ''}]},
                }]

NO_LAG_Server_temp = [{'name': 'NO_LAG_Server_temp', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:0000A66103, bay 8', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical', 'description': 'Updated Profile', 'affinity': 'Bay',
                       'connections': [],
                       'boot': {'manageBoot': False},
                       'bootMode': {'manageMode': False},
                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                       'bios': {'manageBios': False, 'overriddenSettings': []},
                       'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                       'localStorage': None,
                       'sanStorage': None,
                       'connectionSettings': {'connections': [{'id': 1, 'name': 'Connection 1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                               'requestedMbps': '2500', 'networkUri': 'NS:Server_Networkset_LAG_1',
                                                               'mac': None, 'wwpn': '', 'wwnn': ''},
                                                              {'id': 1, 'name': 'Connection 2', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                               'requestedMbps': '2500', 'networkUri': 'NS:Server_Networkset_LAG_1',
                                                               'mac': None, 'wwpn': '', 'wwnn': ''},
                                                              ]},
                       }]

Multi_LAG_Server_temp = [{'name': 'Multi_LAG_Server_temp', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:0000A66103, bay 6', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical', 'description': 'Updated Profile', 'affinity': 'Bay',
                          'connections': [],
                          'boot': {'manageBoot': False},
                          'bootMode': {'manageMode': False},
                          'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                          'bios': {'manageBios': False, 'overriddenSettings': []},
                          'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                          'localStorage': None,
                          'sanStorage': None,
                          'connectionSettings': {'connections': [{'id': 1, 'name': 'Connection 1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                  'requestedMbps': '2500', 'networkUri': 'NS:Server_Networkset_LAG_1',
                                                                  'mac': None, 'wwpn': '', 'wwnn': '', 'lagName': 'LAG1'},
                                                                 {'id': 1, 'name': 'Connection 2', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                  'requestedMbps': '2500', 'networkUri': 'NS:Server_Networkset_LAG_1',
                                                                  'mac': None, 'wwpn': '', 'wwnn': '', 'lagName': 'LAG1'},
                                                                 {'id': 1, 'name': 'Connection 3', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                  'requestedMbps': '2500', 'networkUri': 'NS:Server_Networkset_LAG_2',
                                                                  'mac': None, 'wwpn': '', 'wwnn': '', 'lagName': 'LAG2'},
                                                                 {'id': 1, 'name': 'Connection 4', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                  'requestedMbps': '2500', 'networkUri': 'NS:Server_Networkset_LAG_2',
                                                                  'mac': None, 'wwpn': '', 'wwnn': '', 'lagName': 'LAG2'},
                                                                 ]},
                          }]

Not_redundant_server_Eth_Temp = [{'name': 'Not_redundant_server_Eth_Temp', 'type': 'ServerProfileV8', 'serverHardwareUri': 'SH:0000A66103, bay 7', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical', 'description': 'Updated Profile', 'affinity': 'Bay',
                                  'connections': [],
                                  'boot': {'manageBoot': False},
                                  'bootMode': {'manageMode': False},
                                  'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                  'bios': {'manageBios': False, 'overriddenSettings': []},
                                  'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                                  'localStorage': None,
                                  'sanStorage': None,
                                  'connectionSettings': {'connections': [{'id': 1, 'name': 'Connection 1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                          'requestedMbps': '2500', 'networkUri': 'NS:Network_Set_1',
                                                                          'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                         {'id': 1, 'name': 'Connection 2', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                          'requestedMbps': '2500', 'networkUri': 'NS:Network_Set_2',
                                                                          'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                         ]},
                                  }]

server_profiles = [
    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 5',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': 'Profile5', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a',
                      'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
]

# Firmware Related Variables

LI_fw_update_Hafnium = {"path": "/firmware", 'command': 'UPDATE', 'ethernetActivationDelay': 0, 'ethernetActivationType': 'PairProtect', "fcActivationDelay": 0, "fcActivationType": "PairProtect", 'force': False, 'sppUri': upgrade_firmware_path, "validationType": "ValidateOnly"}


DownLinkPort = 'd2'
UpLinkPort = 'Q2:4'

Eth_DownLinkPort = 'd4'
Eth_UpLinkPort = 'Q1:2'

Eth_Untagged_DownLinkPort = 'd4'
Eth_Untagged_UpLinkPort = 'Q1:4'

Eth_Tunnel_DownLinkPort = 'd4'
Eth_Tunnel_UpLinkPort = 'Q2:4'

FC_UpLinkPort = 'Q2:2'
FC_DownLinkPort = 'd15'

FCOE_UpLinkPort = 'Q2:3'
FCOE_DownLinkPort = 'd17'


Eth_Disable_UpLinkPort = {
    "associatedUplinkSetUri": "FCOE1_IPL",
    "interconnectName": ICM_NAME_1,
    "portType": "Uplink",
    "portId": Eth_UpLinkPort,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": False,
    "portName": Eth_UpLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

Eth_Untagged_Disable_UpLinkPort = {
    "associatedUplinkSetUri": "FCOE1_IPL",
    "interconnectName": ICM_NAME_1,
    "portType": "Uplink",
    "portId": Eth_Untagged_UpLinkPort,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": False,
    "portName": Eth_UpLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

Eth_Tunnel_Disable_UpLinkPort = {
    "associatedUplinkSetUri": "FCOE1_IPL",
    "interconnectName": ICM_NAME_1,
    "portType": "Uplink",
    "portId": Eth_Tunnel_UpLinkPort,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": False,
    "portName": Eth_UpLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

Eth_Disable_downlink = {
    "associatedUplinkSetUri": "us-unTagged",
    "interconnectName": '0000A66101, interconnect 3',
    "portType": "Downlink",
    "portId": Eth_DownLinkPort,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": False,
    "portName": Eth_DownLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

Eth_Enable_UpLinkPort = {
    "associatedUplinkSetUri": "FCOE1_IPL",
    "interconnectName": ICM_NAME_1,
    "portType": "Uplink",
    "portId": Eth_UpLinkPort,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": True,
    "portName": Eth_UpLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

Eth_Untagged_Enable_UpLinkPort = {
    "associatedUplinkSetUri": "FCOE1_IPL",
    "interconnectName": ICM_NAME_1,
    "portType": "Uplink",
    "portId": Eth_Untagged_UpLinkPort,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": True,
    "portName": Eth_Untagged_UpLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

Eth_Tunnel_Enable_UpLinkPort = {
    "associatedUplinkSetUri": "FCOE1_IPL",
    "interconnectName": ICM_NAME_1,
    "portType": "Uplink",
    "portId": Eth_Tunnel_UpLinkPort,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": True,
    "portName": Eth_Tunnel_UpLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

Eth_Enable_downlink = {
    "associatedUplinkSetUri": "us-unTagged",
    "interconnectName": '0000A66101, interconnect 3',
    "portType": "Downlink",
    "portId": Eth_DownLinkPort,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": True,
    "portName": Eth_DownLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

FC_Disable_uplink = {
    "associatedUplinkSetUri": "FCOE1_IPL",
    "interconnectName": ICM_NAME_1,
    "portType": "Uplink",
    "portId": FC_UpLinkPort,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": False,
    "portName": FC_UpLinkPort,
    "portStatus": "Linked",
    "type": "port"
}
FC_Enable_uplink = {
    "associatedUplinkSetUri": "FCOE1_IPL",
    "interconnectName": ICM_NAME_1,
    "portType": "Uplink",
    "portId": FC_UpLinkPort,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": True,
    "portName": FC_UpLinkPort,
    "portStatus": "Linked",
    "type": "port"
}
FC_Disable_downlink = {
    "associatedUplinkSetUri": "us-unTagged",
    "interconnectName": '0000A66101, interconnect 3',
    "portType": "Downlink",
    "portId": FC_DownLinkPort,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": False,
    "portName": FCOE_DownLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

FC_Enable_downlink = {
    "associatedUplinkSetUri": "us-unTagged",
    "interconnectName": '0000A66101, interconnect 3',
    "portType": "Downlink",
    "portId": FC_DownLinkPort,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": True,
    "portName": FC_DownLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

FCOE_Disable_uplink = {
    "associatedUplinkSetUri": "FCOE1_IPL",
    "interconnectName": ICM_NAME_1,
    "portType": "Uplink",
    "portId": FCOE_UpLinkPort,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": False,
    "portName": FCOE_UpLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

FCOE_Disable_downlink = {
    "associatedUplinkSetUri": "us-unTagged",
    "interconnectName": '0000A66101, interconnect 3',
    "portType": "Downlink",
    "portId": FCOE_UpLinkPort,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": False,
    "portName": FCOE_UpLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

FCOE_Enable_uplink = {
    "associatedUplinkSetUri": "FCOE1_IPL",
    "interconnectName": ICM_NAME_1,
    "portType": "Uplink",
    "portId": FCOE_UpLinkPort,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": True,
    "portName": FCOE_UpLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

FCOE_Enable_downlink = {
    "associatedUplinkSetUri": "us-unTagged",
    "interconnectName": '0000A66101, interconnect 3',
    "portType": "Downlink",
    "portId": FCOE_DownLinkPort,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": True,
    "portName": FCOE_DownLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

enable_uplink = {
    "associatedUplinkSetUri": "FCOE1_IPL",
    "interconnectName": ICM_NAME_1,
    "portType": "Uplink",
    "portId": "Q2:4",
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": True,
    "portName": UpLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

disable_uplink = {
    "associatedUplinkSetUri": "FCOE1_IPL",
    "interconnectName": ICM_NAME_1,
    "portType": "Uplink",
    "portId": "Q2:4",
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": False,
    "portName": UpLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

enable_downlink = {
    "associatedUplinkSetUri": "us-unTagged",
    "interconnectName": '0000A66101, interconnect 3',
    "portType": "Downlink",
    "portId": "d5",
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": True,
    "portName": DownLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

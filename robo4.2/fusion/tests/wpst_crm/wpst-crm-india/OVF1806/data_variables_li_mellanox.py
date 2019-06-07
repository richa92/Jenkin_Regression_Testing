"""
    This module contains test specific data variables for Manganese
    sFlow LI test cases and python keywords/helpers.
"""

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

FileBeatLocation = 'http://192.168.146.236/ELK/'

upgrade_firmware_path = '/rest/firmware-drivers/Cust-K130-46-EM202-prod-G10'
downgrade_firmware_path = '/rest/firmware-drivers/Cust-K130-44-EM202-prod-G10'


LIG_Version = 'logical-interconnect-groupV7'
EG_Version = 'EnclosureGroupV8'
LIG_EthernetInterconnectSettings = 'EthernetInterconnectSettingsV6'
eth_network_Version = 'ethernet-networkV4'
fcoe_network_version = 'fcoe-networkV4'
fc_network_version = 'fc-networkV4'

LIG_NAME_POTASH = 'LIG-POTASH'
LIG_NAME_MELLANOX = 'LIG-MELLANOX'
EG_NAME = "EG"
LE_NAME = "LE"
LI_NAME_POTASH = LE_NAME + '-' + LIG_NAME_POTASH
LI_NAME_MELLANOX = LE_NAME + '-' + LIG_NAME_MELLANOX
ENC1 = 'SGH734VDHV'
ENC2 = ''

MELLANOX_ICM_BAY_SET = [1, 4]
POTASH_ICM_BAY_SET = [2, 5]

POTASH = 'Virtual Connect SE 40Gb F8 Module for Synergy'
NITRO = 'Virtual Connect SE 100Gb F32 Module for Synergy'
CL10 = 'Synergy 10Gb Interconnect Link Module'
CL20 = 'Synergy 20Gb Interconnect Link Module'
METHANE = 'Synergy 50Gb Interconnect Link Module'
CARBON16GB = 'Virtual Connect SE 16Gb FC Module for Synergy'
CARBON32GB = 'Virtual Connect SE 32Gb FC Module for Synergy'
CARBON32GB = 'Virtual Connect SE 32Gb FC Module for Synergy'
MELLANOX = 'Mellanox SH2200 TAA Switch Module for Synergy'
redundant = 'Redundant'
highlyAvailable = 'HighlyAvailable'
side_a_redundancyType = 'NonRedundantASide'
side_b_redundancyType = 'NonRedundantBSide'

ManganeseModule1 = 'SGH734VDHV, interconnect 1'
ManganeseModule2 = 'SGH734VDHV, interconnect 4'
PotashModule1 = 'SGH734VDHV, interconnect 2'
PotashModule2 = 'SGH734VDHV, interconnect 5'
NitroModule1 = 'SGH721WSR0, interconnect 2'
Mellanox_ICM_list = [ManganeseModule1, ManganeseModule2]

remove_staticmode_ethernet_name = 'eth-net100'
remove_ippoolmode_ethernet_name = 'eth-net1'

sFlow_collector_IP = '192.168.146.98'
sFlow_agent_IP = '192.168.151.228'

sflow_ports_lig = {
    "Q1_bay1": {"portName": "Q1", "collectorId": 1, "icmName": MELLANOX, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                "enclosureIndex": -1,
                "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                            {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "Q1_bay4": {"portName": "Q1", "collectorId": 1, "icmName": MELLANOX, "bayNumber": MELLANOX_ICM_BAY_SET[1],
                "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                  {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "Q2_bay1": {"portName": "Q2", "collectorId": 1, "icmName": MELLANOX, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                  {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "Q2_bay4": {"portName": "Q2", "collectorId": 1, "icmName": MELLANOX, "bayNumber": MELLANOX_ICM_BAY_SET[1],
                "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                  {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "Q3:1_bay1": {"portName": "Q3:1", "collectorId": 1, "icmName": MELLANOX, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                  "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                    {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "Q3:1_bay4": {"portName": "Q3:1", "collectorId": 1, "icmName": MELLANOX, "bayNumber": MELLANOX_ICM_BAY_SET[1],
                  "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                    {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "Q5:1_bay1": {"portName": "Q5:1", "collectorId": 1, "icmName": MELLANOX, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                  "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                    {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "Q5:1_bay4": {"portName": "Q5:1", "collectorId": 1, "icmName": MELLANOX, "bayNumber": MELLANOX_ICM_BAY_SET[1],
                  "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                    {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "d1_bay1": {"portName": "d1", "collectorId": 1, "icmName": MELLANOX, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                  {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "d2_bay1": {"portName": "d2", "collectorId": 1, "icmName": MELLANOX, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                  {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "d3_bay1": {"portName": "d3", "collectorId": 1, "icmName": MELLANOX, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                  {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
}

sflow_ports = {
    "Q1_bay1": {"portName": "Q1", "collectorId": 1, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                  {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "Q1_bay4": {"portName": "Q1", "collectorId": 1, "icmName": ManganeseModule2, "bayNumber": MELLANOX_ICM_BAY_SET[1],
                "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                  {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "Q2_bay1": {"portName": "Q2", "collectorId": 1, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                  {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "Q2_bay4": {"portName": "Q2", "collectorId": 1, "icmName": ManganeseModule2, "bayNumber": MELLANOX_ICM_BAY_SET[1],
                "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                  {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "Q3:1_bay1": {"portName": "Q3:1", "collectorId": 1, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                  "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                    {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "Q3:1_bay4": {"portName": "Q3:1", "collectorId": 1, "icmName": ManganeseModule2, "bayNumber": MELLANOX_ICM_BAY_SET[1],
                  "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                    {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "Q5:1_bay1": {"portName": "Q5:1", "collectorId": 1, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                  "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                    {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "Q5:1_bay4": {"portName": "Q5:1", "collectorId": 1, "icmName": ManganeseModule2, "bayNumber": MELLANOX_ICM_BAY_SET[1],
                  "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                    {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "d1_bay1": {"portName": "d1", "collectorId": 1, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                  {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "d2_bay1": {"portName": "d2", "collectorId": 1, "icmName": ManganeseModule2, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                  {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "d3_bay1": {"portName": "d3", "collectorId": 1, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                  {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "Q1_bay1_sampling_only": {"portName": "Q1", "collectorId": 1, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                              "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "Q1_bay1_sampling_only_invalid_samplingRate": {"portName": "Q1", "collectorId": 1, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                                                   "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16777217}]},
    "Q1_bay1_sampling_only_without_samplingRate": {"portName": "Q1", "collectorId": 1, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                                                   "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16777217}]},
    "Q1_bay1_polling_only": {"portName": "Q1", "collectorId": 1, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                             "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20}]},
    "Q1_bay1_polling_only_invalid_pollingRate": {"portName": "Q1", "collectorId": 1, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                                                 "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 11}]},
    "Q1_bay1_polling_only_no_interval": {"portName": "Q1", "collectorId": 1, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                                         "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling"}]},
    "Q2_bay1_sampling_only": {"portName": "Q2", "collectorId": 1, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                              "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "Q1_bay1_ingress_edit": {"portName": "Q1", "collectorId": 1, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                             "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                               {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 6000}]},
    "Q2_bay4_ingress_edit": {"portName": "Q2", "collectorId": 1, "icmName": ManganeseModule2, "bayNumber": MELLANOX_ICM_BAY_SET[1],
                             "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                               {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 6000}]},
    "Q3:1_bay1_ingress_edit": {"portName": "Q3:1", "collectorId": 1, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                               "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                                 {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 6000}]},
    "d1_bay1_ingress_edit": {"portName": "d1", "collectorId": 1, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                             "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                               {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 6000}]},
    "Q1_bay1_polling_interval_edit": {"portName": "Q1", "collectorId": 1, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                                      "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 100},
                                                                                        {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "Q9_bay1_invalid_port": {"portName": "Q9", "collectorId": 1, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                             "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                               {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]},
    "Q1_bay1_collectorid_2": {"portName": "Q1", "collectorId": 2, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0],
                              "enclosureIndex": -1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20},
                                                                                {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 16000}]}
}

subnet = [{'type': 'Subnet',
           'gateway': '192.168.144.1',
           'networkId': '192.168.144.0',
           'subnetmask': '255.255.248.0',
           'dnsServers': [],
           'domain': 'Subnet145.com'}]

subnet_range = [{'type': 'Range',
                 'startStopFragments': [{'startAddress': '192.168.144.5',
                                         'endAddress': '192.168.144.45',
                                         }],
                 'name': 'RangeForSubnet144',
                 'subnetUri': '192.168.144.0'}]

ethernet_networks = [
    {'name': 'eth-net20', 'type': eth_network_Version, 'vlanId': 20, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
    {'name': 'eth-net30', 'type': eth_network_Version, 'vlanId': 30, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
    {'name': 'eth-net40', 'type': eth_network_Version, 'vlanId': 40, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
    {'name': remove_staticmode_ethernet_name, 'type': eth_network_Version, 'vlanId': 100, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
    {'name': 'eth-net110', 'type': eth_network_Version, 'vlanId': 110, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
    {'name': 'eth-net120', 'type': eth_network_Version, 'vlanId': 120, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
    {'name': 'eth-net130', 'type': eth_network_Version, 'vlanId': 130, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
    {'name': 'eth-net140', 'type': eth_network_Version, 'vlanId': 140, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
    {'name': 'eth-net150', 'type': eth_network_Version, 'vlanId': 150, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
    {'name': 'eth-net160', 'type': eth_network_Version, 'vlanId': 160, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
    {'name': 'eth-net200', 'type': eth_network_Version, 'vlanId': 200, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
    {'name': 'eth-tunnel', 'type': eth_network_Version, 'vlanId': None, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tunnel'},
    {'name': 'eth-untagged', 'type': eth_network_Version, 'vlanId': None, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Untagged'},
]

eth_networks_subnet = [{"vlanId": "1", "ethernetNetworkType": "Tagged", "subnetUri": '192.168.144.0', "purpose": "General", "name": remove_ippoolmode_ethernet_name, "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version}]


icmap_ME = [{'enclosure': -1, 'bay': 1, 'type': MELLANOX, 'enclosureIndex': -1},
            {'enclosure': -1, 'bay': 4, 'type': MELLANOX, 'enclosureIndex': -1}
            ]

uplink_sets_redundant = {'us-Q1': {'name': 'us-Q1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'mode': 'Auto',
                                   'networkUris': [remove_ippoolmode_ethernet_name, 'eth-net20'],
                                   'nativeNetworkUri': remove_ippoolmode_ethernet_name,
                                   'consistencyChecking': 'MinimumMatch',
                                   'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': MELLANOX_ICM_BAY_SET[0], 'port': 'Q1', 'speed': 'Speed40G'},
                                                              {'enclosure': '-1', 'bay': MELLANOX_ICM_BAY_SET[1], 'port': 'Q1', 'speed': 'Speed40G'}
                                                              ]
                                   },
                         'us-Q2-100g': {'name': 'us-Q2-100g', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'mode': 'Auto',
                                        'networkUris': [remove_staticmode_ethernet_name],
                                        'consistencyChecking': 'MinimumMatch',
                                        'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': MELLANOX_ICM_BAY_SET[0], 'port': 'Q2', 'speed': 'Speed100G'},
                                                                   {'enclosure': '-1', 'bay': MELLANOX_ICM_BAY_SET[1], 'port': 'Q2', 'speed': 'Speed100G'}
                                                                   ]
                                        },
                         'us-Q3-1-25g': {'name': 'us-Q3-1-25g', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'mode': 'Auto',
                                         'networkUris': ['eth-net110'],
                                         'consistencyChecking': 'MinimumMatch',
                                         'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': MELLANOX_ICM_BAY_SET[0], 'port': 'Q3:1', 'speed': 'Speed25G'},
                                                                    {'enclosure': '-1', 'bay': MELLANOX_ICM_BAY_SET[1], 'port': 'Q3:1', 'speed': 'Speed25G'}
                                                                    ]
                                         },
                         'us-Q51-iscsi': {'name': 'us-Q51-iscsi', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'mode': 'Auto',
                                          'networkUris': ['eth-net200'],
                                          'consistencyChecking': 'MinimumMatch',
                                          'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': MELLANOX_ICM_BAY_SET[0], 'port': 'Q5:1', 'speed': 'Speed10G'},
                                                                     {'enclosure': '-1', 'bay': MELLANOX_ICM_BAY_SET[1], 'port': 'Q5:1', 'speed': 'Speed10G'}
                                                                     ]
                                          }
                         }

sflow_lig_static_redundant = {"type": LIG_Version,
                              "ethernetSettings": {"type": LIG_EthernetInterconnectSettings, "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                              "description": None,
                              "name": LIG_NAME_MELLANOX,
                              "interconnectMapTemplate": icmap_ME,
                              "enclosureType": "SY12000",
                              "enclosureIndexes": [-1],
                              "interconnectBaySet": "1",
                              "redundancyType": "Redundant",
                              "internalNetworkUris": [],
                              "snmpConfiguration": None,
                              "qosConfiguration": None,
                              "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                     "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 128, "port": 6343, "collectorId": 1}],
                                                     "sflowAgents": [{"ipMode": "Static"}],
                                                     "sflowPorts": [
                                  sflow_ports_lig['Q1_bay1'].copy(),
                                  # sflow_ports['Q1_bay4'].copy(),
                                  sflow_ports_lig['Q2_bay1'].copy(),
                                  # sflow_ports['Q2_bay4'].copy(),
                                  sflow_ports_lig['Q3:1_bay1'].copy(),
                                  # sflow_ports['Q3:1_bay4'].copy(),
                                  sflow_ports_lig['Q5:1_bay1'].copy(),
                                  # sflow_ports['Q5:1_bay4'].copy(),
                                  sflow_ports_lig['d1_bay1'].copy(),
                                  # sflow_ports['d2_bay1'].copy(),
                                  # sflow_ports['d3_bay1'].copy()
                              ]
                              },
                              "uplinkSets": [
                                  uplink_sets_redundant['us-Q1'].copy(),
                                  uplink_sets_redundant['us-Q2-100g'].copy(),
                                  uplink_sets_redundant['us-Q3-1-25g'].copy(),
                                  uplink_sets_redundant['us-Q51-iscsi'].copy(),
                              ]
                              }

sflow_lig_ippool_redundant = {"type": LIG_Version,
                              "ethernetSettings": {"type": LIG_EthernetInterconnectSettings, "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                              "description": None,
                              "name": LIG_NAME_MELLANOX,
                              "interconnectMapTemplate": icmap_ME,
                              "enclosureType": "SY12000",
                              "enclosureIndexes": [-1],
                              "interconnectBaySet": "1",
                              "redundancyType": "Redundant",
                              "internalNetworkUris": [],
                              "snmpConfiguration": None,
                              "qosConfiguration": None,
                              "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": remove_ippoolmode_ethernet_name},
                                                     "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 128, "port": 6343, "collectorId": 1}],
                                                     "sflowAgents": [{"ipMode": "ippool"}],
                                                     "sflowPorts": [
                                  sflow_ports_lig['Q1_bay1'].copy(),
                                  # sflow_ports['Q1_bay4'].copy(),
                                  sflow_ports_lig['Q2_bay1'].copy(),
                                  # sflow_ports['Q2_bay4'].copy(),
                                  sflow_ports_lig['Q3:1_bay1'].copy(),
                                  # sflow_ports['Q3:1_bay4'].copy(),
                                  sflow_ports_lig['Q5:1_bay1'].copy(),
                                  # sflow_ports['Q5:1_bay4'].copy(),
                                  sflow_ports_lig['d1_bay1'].copy(),
                                  # sflow_ports['d2_bay1'].copy(),
                                  # sflow_ports['d3_bay1'].copy()
                              ]
                              },
                              "uplinkSets": [
                                  uplink_sets_redundant['us-Q1'].copy(),
                                  uplink_sets_redundant['us-Q2-100g'].copy(),
                                  uplink_sets_redundant['us-Q3-1-25g'].copy(),
                                  uplink_sets_redundant['us-Q51-iscsi'].copy(),
                              ]
                              }

sflow_lig_dhcp_potash = {"type": LIG_Version,
                         "ethernetSettings": {"type": LIG_EthernetInterconnectSettings, "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                         "description": None,
                         "name": LIG_NAME_POTASH,
                         "interconnectMapTemplate": [{'enclosure': 1, 'bay': POTASH_ICM_BAY_SET[0], 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                                     {'enclosure': 1, 'bay': POTASH_ICM_BAY_SET[1], 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
                                                     ],
                         "enclosureType": "SY12000",
                         "enclosureIndexes": [1],
                         "interconnectBaySet": "2",
                         "redundancyType": "Redundant",
                         "internalNetworkUris": [],
                         "snmpConfiguration": None,
                         "qosConfiguration": None,
                         "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": remove_ippoolmode_ethernet_name},
                                                "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 128, "port": 6343, "collectorId": 1}],
                                                "sflowAgents": [{"ipMode": "DHCP"}],
                                                "sflowPorts": [{"portName": "Q1:1", "collectorId": 1, "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 2,
                                                                "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20, "pollingEnabled": True},
                                                                                                                 {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "4096", "samplingEnabled": True}]},
                                                               {"portName": "Q1:1", "collectorId": 1, "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 5,
                                                                   "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 20, "pollingEnabled": True},
                                                                                                                    {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "4096", "samplingEnabled": True}]},
                                                               ]
                                                },
                         "uplinkSets": [
                             {'name': 'us-Q1:1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': [remove_ippoolmode_ethernet_name, remove_staticmode_ethernet_name], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                 'logicalPortConfigInfos': [{'bay': POTASH_ICM_BAY_SET[0], 'enclosure': '1', 'port': 'Q1:1', 'speed': 'Auto'},
                                                            {'bay': POTASH_ICM_BAY_SET[1], 'enclosure': '1', 'port': 'Q1:1', 'speed': 'Auto'}]}
                         ]
                         }

sflow_eg_with_potash = [{'name': EG_NAME,
                         'ipAddressingMode': "External",
                         'enclosureCount': 1,
                         'configurationScript': None,
                         'interconnectBayMappings': [{'enclosureIndex': 1, "interconnectBay": 1,
                                                      "logicalInterconnectGroupUri": "LIG:" + LIG_NAME_MELLANOX},
                                                     {'enclosureIndex': 1, "interconnectBay": 2,
                                                      "logicalInterconnectGroupUri": "LIG:" + LIG_NAME_POTASH},
                                                     {'enclosureIndex': 1, "interconnectBay": 3,
                                                      "logicalInterconnectGroupUri": None},
                                                     {'enclosureIndex': 1, "interconnectBay": 4,
                                                      "logicalInterconnectGroupUri": "LIG:" + LIG_NAME_MELLANOX},
                                                     {'enclosureIndex': 1, "interconnectBay": 5,
                                                      "logicalInterconnectGroupUri": "LIG:" + LIG_NAME_POTASH},
                                                     ]
                         }]

sflow_eg_ippool = [{'name': 'EG2',
                    'ipAddressingMode': "IpPool",
                    "ipRangeUris": ['RangeForSubnet144'],
                    'enclosureCount': 1,
                    'configurationScript': None,
                    'interconnectBayMappings': [{'enclosureIndex': 1, "interconnectBay": 1,
                                                 "logicalInterconnectGroupUri": "LIG:" + LIG_NAME_MELLANOX},
                                                {'enclosureIndex': 1, "interconnectBay": 2,
                                                 "logicalInterconnectGroupUri": "LIG:" + LIG_NAME_POTASH},
                                                {'enclosureIndex': 1, "interconnectBay": 3,
                                                 "logicalInterconnectGroupUri": None},
                                                {'enclosureIndex': 1, "interconnectBay": 4,
                                                 "logicalInterconnectGroupUri": "LIG:" + LIG_NAME_MELLANOX},
                                                {'enclosureIndex': 1, "interconnectBay": 5,
                                                 "logicalInterconnectGroupUri": "LIG:" + LIG_NAME_POTASH},
                                                ]
                    }]

sflow_le = [{'name': LE_NAME,
             'enclosureUris': ['ENC:' + ENC1],
             'enclosureGroupUri': 'EG:' + EG_NAME,
             'firmwareBaselineUri': None,
             'forceInstallFirmware': False
             }]

sflow_le_ippol = {'name': 'LE2',
                  'enclosureUris': ['ENC:' + ENC1],
                  'enclosureGroupUri': 'EG:EG2',
                  'firmwareBaselineUri': None,
                  'forceInstallFirmware': False
                  }

edit_li_edit_collector_ip = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                    "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "192.168.146.99", "maxDatagramSize": 1400, "maxHeaderSize": 128, "port": 6343, "collectorId": 1}],
                                                    "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                    "sflowPorts": [
    sflow_ports['Q1_bay1'].copy(),
    # sflow_ports['Q1_bay4'].copy(),
    sflow_ports['Q2_bay1'].copy(),
    # sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    # sflow_ports['Q3:1_bay4'].copy(),
    sflow_ports['Q5:1_bay1'].copy(),
    # sflow_ports['Q5:1_bay4'].copy(),
    sflow_ports['d1_bay1'].copy(),
    # sflow_ports['d2_bay1'].copy(),
    # sflow_ports['d3_bay1'].copy()
]
}}

edit_li_for_inconsistency = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                    "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 6000, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                    "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                    "sflowPorts": [{"portName": "Q1", "collectorId": 1, "icmName": ManganeseModule1, "bayNumber": MELLANOX_ICM_BAY_SET[0], "enclosureIndex": -1,
                                                                    "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 100},
                                                                                                {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 4000}
                                                                                                ]},
                                                                   {"portName": "Q2", "collectorId": 1, "icmName": ManganeseModule2, "bayNumber": MELLANOX_ICM_BAY_SET[1], "enclosureIndex": -1,
                                                                    "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": 100},
                                                                                                {"configurationMode": "Sampling", "direction": "Ingress", "samplingRate": 4000}
                                                                                                ]}
                                                                   ]
                                                    }}

edit_li_add_more_uplinkports = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                       "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 128, "port": 6343, "collectorId": 1}],
                                                       "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                       "sflowPorts": [
    sflow_ports['d1_bay1'].copy(),
    sflow_ports['d2_bay1'].copy(),
    sflow_ports['d3_bay1'].copy(),
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q1_bay4'].copy(),
    sflow_ports['Q2_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['Q3:1_bay4'].copy(),
    sflow_ports['Q5:1_bay1'].copy(),
    sflow_ports['Q5:1_bay4'].copy()

]
}}

edit_li_disable_collector = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                    "sflowCollectors": [{"name": "C100", "collectorEnabled": False, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 128, "port": 6343, "collectorId": 1}],
                                                    "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                    "sflowPorts": [
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q1_bay4'].copy(),
    sflow_ports['Q2_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['Q3:1_bay4'].copy(),
    sflow_ports['Q5:1_bay1'].copy(),
    sflow_ports['Q5:1_bay4'].copy(),
    sflow_ports['d1_bay1'].copy(),
    sflow_ports['d2_bay1'].copy(),
    sflow_ports['d3_bay1'].copy()
]
}}

edit_li_enable_collector = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                   "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 128, "port": 6343, "collectorId": 1}],
                                                   "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                   "sflowPorts": [
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q1_bay4'].copy(),
    sflow_ports['Q2_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['Q3:1_bay4'].copy(),
    sflow_ports['Q5:1_bay1'].copy(),
    sflow_ports['Q5:1_bay4'].copy(),
    sflow_ports['d1_bay1'].copy(),
    sflow_ports['d2_bay1'].copy(),
    sflow_ports['d3_bay1'].copy()
]
}}

edit_li_max_datagramsize1 = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                    "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                    "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                    "sflowPorts": [
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q1_bay4'].copy(),
    sflow_ports['Q2_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['Q3:1_bay4'].copy(),
    sflow_ports['Q5:1_bay1'].copy(),
    sflow_ports['Q5:1_bay4'].copy(),
    sflow_ports['d1_bay1'].copy(),
    sflow_ports['d2_bay1'].copy(),
    sflow_ports['d3_bay1'].copy()
]
}}

edit_li_max_datagramsize2 = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                    "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 9000, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                    "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                    "sflowPorts": [
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q1_bay4'].copy(),
    sflow_ports['Q2_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['Q3:1_bay4'].copy(),
    sflow_ports['Q5:1_bay1'].copy(),
    sflow_ports['Q5:1_bay4'].copy(),
    sflow_ports['d1_bay1'].copy(),
    sflow_ports['d2_bay1'].copy(),
    sflow_ports['d3_bay1'].copy()
]
}}

edit_li_max_headersize1 = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                  "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 128, "port": 6343, "collectorId": 1}],
                                                  "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                  "sflowPorts": [
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q1_bay4'].copy(),
    sflow_ports['Q2_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['Q3:1_bay4'].copy(),
    sflow_ports['Q5:1_bay1'].copy(),
    sflow_ports['Q5:1_bay4'].copy(),
    sflow_ports['d1_bay1'].copy(),
    sflow_ports['d2_bay1'].copy(),
    sflow_ports['d3_bay1'].copy()
]
}}

edit_li_max_headersize2 = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                  "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                  "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                  "sflowPorts": [
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q1_bay4'].copy(),
    sflow_ports['Q2_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['Q3:1_bay4'].copy(),
    sflow_ports['Q5:1_bay1'].copy(),
    sflow_ports['Q5:1_bay4'].copy(),
    sflow_ports['d1_bay1'].copy(),
    sflow_ports['d2_bay1'].copy(),
    sflow_ports['d3_bay1'].copy()
]
}}

edit_li_polling_collector = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                    "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 9000, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                    "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                    "sflowPorts": [
    sflow_ports['Q1_bay1_polling_only'].copy(),
]
}}

edit_li_polling_changing_ip_of_collector = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                                   "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "192.168.146.99", "maxDatagramSize": 9000, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                                   "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                                   "sflowPorts": [
    sflow_ports['Q1_bay1_polling_only'].copy(),
]
}}

edit_li_sampling_collector = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                     "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 9000, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                     "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                     "sflowPorts": [
    sflow_ports['Q1_bay1_sampling_only'].copy(),
]
}}

edit_li_sampling_changing_ip_of_collector = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                                    "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "192.168.146.99", "maxDatagramSize": 9000, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                                    "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                                    "sflowPorts": [
    sflow_ports['Q1_bay1_sampling_only'].copy(),

]
}}

edit_li_sampling_changing_port_of_collector = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                                      "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "192.168.146.99", "maxDatagramSize": 9000, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                                      "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                                      "sflowPorts": [
    sflow_ports['Q2_bay1_sampling_only'].copy(),

]
}}

edit_li_removing_collector = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                     "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "192.168.146.99", "maxDatagramSize": 9000, "maxHeaderSize": 256, "port": 6343, "collectorId": 2}],
                                                     "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                     "sflowPorts": [
    sflow_ports['Q2_bay1'].copy(),

]
}}


edit_li_new_sflow_network = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": remove_staticmode_ethernet_name},
                                                    "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 9000, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                    "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                    "sflowPorts": [
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['d1_bay1'].copy()
]
}}

edit_li_invalid_datagram_size1 = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                         "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": "10000", "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                         "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                         "sflowPorts": [
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['d1_bay1'].copy()
]
}}

edit_li_invalid_datagram_size2 = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                         "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": "100", "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                         "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                         "sflowPorts": [
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['d1_bay1'].copy()
]
}}

edit_li_invalid_maxheader_size = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                         "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 9000, "maxHeaderSize": "512", "port": 6343, "collectorId": 1}],
                                                         "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                         "sflowPorts": [
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['d1_bay1'].copy()
]
}}

edit_li_modify_polling_interval = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                          "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 128, "port": 6343, "collectorId": 1}],
                                                          "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                          "sflowPorts": [
    sflow_ports['Q1_bay1_polling_interval_edit'].copy(),
    sflow_ports['Q1_bay4'].copy(),
    sflow_ports['Q2_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['Q3:1_bay4'].copy(),
    sflow_ports['Q5:1_bay1'].copy(),
    sflow_ports['Q5:1_bay4'].copy(),
    sflow_ports['d1_bay1'].copy(),
    sflow_ports['d2_bay1'].copy(),
    sflow_ports['d3_bay1'].copy()
]
}}

edit_li_invalid_port = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                               "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                               "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                               "sflowPorts": [
    sflow_ports['Q9_bay1_invalid_port'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['d1_bay1'].copy()
]
}}

edit_li_add_morethan_max_collector_ips = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                                 "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 256, "port": 6343, "collectorId": 1},
                                                                                     {"name": "C200", "collectorEnabled": True, "ipAddress": "192.168.146.99", "maxDatagramSize": 1400, "maxHeaderSize": 256, "port": 6343, "collectorId": 2}],
                                                                 "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                                 "sflowPorts": [
    sflow_ports['Q1_bay1_collectorid_2'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['d1_bay1'].copy()
]
}}

edit_li_add_invalid_collector_id = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                           "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                           "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                           "sflowPorts": [
    sflow_ports['Q1_bay1_collectorid_2'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['d1_bay1'].copy()
]
}}

edit_li_adding_fc_nw = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "fc-net1"},
                                               "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                               "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                               "sflowPorts": [
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['d1_bay1'].copy()
]
}}

edit_li_adding_tunnel_nw = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-tunnel"},
                                                   "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                   "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                   "sflowPorts": [
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['d1_bay1'].copy()
]
}}

edit_li_adding_untagged_nw = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-untagged"},
                                                     "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                     "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                     "sflowPorts": [
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['d1_bay1'].copy()
]
}}

edit_li_changing_mode_of_sflow = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": remove_ippoolmode_ethernet_name},
                                                         "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 128, "port": 6343, "collectorId": 1}],
                                                         "sflowAgents": [{"ipMode": "IpPool", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                         "sflowPorts": [
    sflow_ports['d1_bay1'].copy(),
    sflow_ports['d2_bay1'].copy(),
    sflow_ports['d3_bay1'].copy(),
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q1_bay4'].copy(),
    sflow_ports['Q2_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['Q3:1_bay4'].copy(),
    sflow_ports['Q5:1_bay1'].copy(),
    sflow_ports['Q5:1_bay4'].copy()

]
}}


edit_li_downlink_ports_only = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                      "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 128, "port": 6343, "collectorId": 1}],
                                                      "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                      "sflowPorts": [
    sflow_ports['d1_bay1'].copy(),
    sflow_ports['d2_bay1'].copy(),
    sflow_ports['d3_bay1'].copy(),
]
}}

edit_li_10gb_ports = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                             "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 128, "port": 6343, "collectorId": 1}],
                                             "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                             "sflowPorts": [
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['Q5:1_bay1'].copy()
]
}}

edit_li_40gb_ports = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                             "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 128, "port": 6343, "collectorId": 1}],
                                             "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                             "sflowPorts": [
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q2_bay1'].copy()
]
}}

edit_li_without_sampling_interval = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                            "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 9000, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                            "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                            "sflowPorts": [
    sflow_ports['Q1_bay1_sampling_only_without_samplingRate'].copy(),
]
}}

edit_li_without_polling_interval = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                           "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 9000, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                           "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                           "sflowPorts": [
    sflow_ports['Q1_bay1_polling_only_no_interval'].copy(),

]
}}

edit_li_invalid_static_ip = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                    "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 128, "port": 6343, "collectorId": 1}],
                                                    "sflowAgents": [{"ipMode": "Static", "ipAddr": "192.168.145.43.12", "subnetMask": "255.255.248.0"}],
                                                    "sflowPorts": [
    sflow_ports['d1_bay1'].copy(),
    sflow_ports['d2_bay1'].copy(),
    sflow_ports['d3_bay1'].copy(),
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q1_bay4'].copy(),
    sflow_ports['Q2_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['Q3:1_bay4'].copy(),
    sflow_ports['Q5:1_bay1'].copy(),
    sflow_ports['Q5:1_bay4'].copy()

]
}}

edit_li_invalid_collector_name = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                         "sflowCollectors": [{"name": "Invalid_Collector_Name_More_Than_64_Characters_In_Length_xxxxxxxxxxxxxxxxxx", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 128, "port": 6343, "collectorId": 1}],
                                                         "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                         "sflowPorts": [
    sflow_ports['d1_bay1'].copy(),
    sflow_ports['d2_bay1'].copy(),
    sflow_ports['d3_bay1'].copy(),
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q1_bay4'].copy(),
    sflow_ports['Q2_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['Q3:1_bay4'].copy(),
    sflow_ports['Q5:1_bay1'].copy(),
    sflow_ports['Q5:1_bay4'].copy()

]
}}

edit_li_invalid_collector_port = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                         "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 128, "port": "6000", "collectorId": 1}],
                                                         "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                         "sflowPorts": [
    sflow_ports['d1_bay1'].copy(),
    sflow_ports['d2_bay1'].copy(),
    sflow_ports['d3_bay1'].copy(),
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q1_bay4'].copy(),
    sflow_ports['Q2_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['Q3:1_bay4'].copy(),
    sflow_ports['Q5:1_bay1'].copy(),
    sflow_ports['Q5:1_bay4'].copy()

]
}}

edit_li_invalid_sampling_interval = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                            "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 9000, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                            "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                            "sflowPorts": [
    sflow_ports['Q1_bay1_sampling_only_invalid_samplingRate'].copy(),
]
}}

edit_li_invalid_polling_interval = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                           "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 9000, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                           "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                           "sflowPorts": [
    sflow_ports['Q1_bay1_polling_only_invalid_pollingRate'].copy()
]
}}

edit_li_only_ingress_packets = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                       "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 9000, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                       "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                       "sflowPorts": [
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['d1_bay1'].copy()
]
}}

edit_li_modify_ingress_rate = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "eth-net20"},
                                                      "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 9000, "maxHeaderSize": 256, "port": 6343, "collectorId": 1}],
                                                      "sflowAgents": [{"ipMode": "Static", "ipAddr": sFlow_agent_IP, "subnetMask": "255.255.248.0"}],
                                                      "sflowPorts": [
    sflow_ports['Q1_bay1_ingress_edit'].copy(),
    sflow_ports['Q2_bay4_ingress_edit'].copy(),
    sflow_ports['Q3:1_bay1_ingress_edit'].copy(),
    sflow_ports['d1_bay1_ingress_edit'].copy(),
]
}}

edit_li_valid_ip_pool = {'sflowconfiguration': {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": remove_ippoolmode_ethernet_name},
                                                "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": sFlow_collector_IP, "maxDatagramSize": 1400, "maxHeaderSize": 128, "port": 6343, "collectorId": 1}],
                                                "sflowAgents": [{"ipMode": "IpPool"}],
                                                "sflowPorts": [
    sflow_ports['d1_bay1'].copy(),
    sflow_ports['d2_bay1'].copy(),
    sflow_ports['d3_bay1'].copy(),
    sflow_ports['Q1_bay1'].copy(),
    sflow_ports['Q1_bay4'].copy(),
    sflow_ports['Q2_bay1'].copy(),
    sflow_ports['Q2_bay4'].copy(),
    sflow_ports['Q3:1_bay1'].copy(),
    sflow_ports['Q3:1_bay4'].copy(),
    sflow_ports['Q5:1_bay1'].copy(),
    sflow_ports['Q5:1_bay4'].copy()

]
}}

sflow_server1 = [{'name': 'SP_Bay1_Bronco', 'type': 'ServerProfileV11', 'serverHardwareUri': 'SH:SGH734VDHV, bay 1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical', 'description': 'Updated Profile', 'affinity': 'Bay',
                  'boot': {'manageBoot': False},
                  'bootMode': {'manageMode': False},
                  'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                  'bios': {'manageBios': False, 'overriddenSettings': []},
                  'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                  'localStorage': None,
                  'sanStorage': None,
                  'connectionSettings': {'connections': [
                      {'id': 1, 'name': 'Connection 1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1',
                       'requestedMbps': '10000', 'networkUri': 'ETH:eth-net20',
                       'mac': None, 'wwpn': '', 'wwnn': ''},
                      #                                                         {'id': 2, 'name': 'Connection 2', 'functionType': 'Ethernet', 'portId': 'Auto',
                      #                                                          'requestedMbps': '2500', 'networkUri': 'ETH:Ethernet_1000',
                      #                                                          'mac': None, 'wwpn': '', 'wwnn': ''},
                  ]},
                  }]

sflow_server2 = [{'name': 'SP_Bay3_Melrose', 'type': 'ServerProfileV11', 'serverHardwareUri': 'SH:SGH734VDHV, bay 3', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical', 'description': 'Updated Profile', 'affinity': 'Bay',
                  'boot': {'manageBoot': False},
                  'bootMode': {'manageMode': False},
                  'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                  'bios': {'manageBios': False, 'overriddenSettings': []},
                  'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                  'localStorage': None,
                  'sanStorage': None,
                  'connectionSettings': {'connections': [{'id': 1, 'name': 'Connection 1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1',
                                                          'requestedMbps': '25000', 'networkUri': 'ETH:eth-net20',
                                                          'mac': None, 'wwpn': '', 'wwnn': ''},
                                                         #                                                          {'id': 2, 'name': 'Connection 2', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                         #                                                           'requestedMbps': '2500', 'networkUri': 'ETH:Ethernet_1000',
                                                         #                                                           'mac': None, 'wwpn': '', 'wwnn': ''},
                                                         ]},
                  }]


def verify_sflow_data(sflow_data, sflow_li):
    """
    Gets sFlow configuration details from LI against LI sFlow data file
    details
    """
    keys = sflow_data.keys()
    status = True

    if 'enabled' in keys:
        print "\nComparing sflow_data['enabled'] ==  sflow_li['enabled']\n"
        if sflow_data['enabled'] != sflow_li['enabled']:
            status = False
            print "enabled: ", sflow_data['enabled'], "!=", sflow_li['enabled']
            print "\nSetting Verify status to False"
        else:
            print "enabled: ", sflow_data['enabled'], "==", sflow_li['enabled']
    else:
        print "\n'Enabled' key not in expected data\n"

    if 'sflowNetwork' in keys:
        print "\nComparing  sflow_data['sflowNetwork'] ==  sflow_li['sflowNetwork']\n"
        for key2 in sflow_data['sflowNetwork'].keys():
            if sflow_data['sflowNetwork'][key2] != sflow_li['sflowNetwork'][key2]:
                status = False
                print "%s: " % key2, sflow_data['sflowNetwork'][key2], "!=", sflow_li['sflowNetwork'][key2]
                print "\nSetting Verify status to False"
            else:
                print "%s: " % key2, sflow_data['sflowNetwork'][key2], "==", sflow_li['sflowNetwork'][key2]
    else:
        print "\'sflowNetwork' key not in expected data\n"

    if 'sflowAgents' in keys:
        print "\nComparing  sflow_data['sflowAgents'] ==  sflow_li['sflowAgents']\n"
        pairs = zip(sflow_data['sflowAgents'], sflow_li['sflowAgents'])
        if any(x != y for x, y in pairs):
            status = False
            print "\nSetting Verify status to False"
            print [(x, y) for x, y in pairs if x != y]
    else:
        print "\n'sflowAgents' key not in expected data\n"

    if 'sflowCollectors' in keys:
        print "\nComparing  sflow_data['sflowCollectors'] ==  sflow_li['sflowCollectors']\n"
        pairs = zip(sflow_data['sflowCollectors'], sflow_li['sflowCollectors'])
        if any(x != y for x, y in pairs):
            status = False
            print "\nSetting Verify status to False"
            print [(x, y) for x, y in pairs if x != y]
    else:
        print "\n'sflowCollectors' key not in expected data\n"

    if 'sflowPorts' in keys:
        print "\nComparing  sflow_data['sflowPorts'] ==  sflow_li['sflowPorts']\n"
        port_keys = ['portName', 'bayNumber', 'enclosureIndex', 'collectorId']
        for dport in sflow_data['sflowPorts']:
            dport_found = True
            print "\nLooking for %s in LI sflow body" % dport['portName']
            for lport in sflow_li['sflowPorts']:
                dport_found = True
                print "Checking if ", dport['portName'], "==", lport['portName']
                for key3 in port_keys:
                    if dport[key3] == lport[key3]:
                        print "%s: " % key3, dport[key3], "==", lport[key3]
                        continue
                    else:
                        dport_found = False
                        print "%s: " % key3, dport[key3], "!=", lport[key3]
                        break
                if dport_found:
                    print "\nFound port %s in LI SFlow body. Now comparing ConfigModes" % dport['portName']
                    dmodes = dport['sflowConfigurationModes']
                    lmodes = lport['sflowConfigurationModes']
                    mode_found = False
                    for dmode in dmodes:
                        for lmode in lmodes:
                            if dmode['configurationMode'] == lmode['configurationMode']:
                                mode_found = True
                                print "\nComparing %s configurationMode dictionaries" % dmode['configurationMode']
                                dmode_keys = dmode.keys()
                                lmode_keys = lmode.keys()
                                if len(dmode_keys) != len(lmode_keys):
                                    status = False
                                    print "\n%s Length of configurationMode dictionaries not same" % dmode['configurationMode']
                                    print "\nSetting Verify status to False"
                                else:
                                    for key in dmode_keys:
                                        if dmode[key] != lmode[key]:
                                            status = False
                                            print "%s: " % key, dmode[key], "!=", dmode[key]
                                            print "\nSetting Verify status to False"
                                        else:
                                            print "%s: " % key, dmode[key], "==", dmode[key]
                                continue
                        if not mode_found:
                            status = False
                            print "Config Mode %s not found in LI body for port %s" % (dmode['configurationMode'], dport['portName'])
                            print "\nSetting Verify status to False"
                if dport_found:
                    break
            if not dport_found:
                print "Port %s not found in LI sflow body" % dport['portName']
                status = False
                print "\nSetting Verify status to False"
        else:
            print "\n'sflowPorts' key not in expected data\n"
    return status

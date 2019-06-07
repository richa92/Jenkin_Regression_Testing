
login_details = {'userName': 'Administrator', 'password': 'hpvse123'}
LIG_Version = 'logical-interconnect-groupV4'
eth_network_Version = 'ethernet-networkV4'
fcoe_network_version = 'fcoe-networkV4'
fc_network_version = 'fc-networkV4'
ENC1 = '0000A66101'
ENC2 = '0000A66102'
ENC3 = '0000A66103'
subnet = {'type': 'Subnet',
          'gateway': '192.168.145.1',
          'networkId': '192.168.145.0',
          'subnetmask': '255.255.255.0',
          'dnsServers': [],
          'domain': 'Subnet222.com'}

range = {'type': 'Range',
         'startAddress': '192.168.145.5',
         'endAddress': '192.168.145.45',
         'name': 'RangeForSubnet222_1',
         'subnetUri': ' '}

icmap_ME = [{'enclosure': 1, 'bay': 3, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
            {'enclosure': 1, 'bay': 6, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
            ]


sflow_lig_dhcp = {"type": LIG_Version,
                  "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                  "description": None,
                  "name": "LIG_DHCP",
                  "interconnectMapTemplate": icmap_ME,
                  "enclosureType": "SY12000",
                  "enclosureIndexes": [1],
                  "interconnectBaySet": "3",
                  "redundancyType": "Redundant",
                  "internalNetworkUris": [],
                  "snmpConfiguration": None,
                  "qosConfiguration": None,
                  "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                         "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1}],
                                         "sflowAgents": [{"ipMode": "DHCP"}],
                                         "sflowPorts": [{"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                         "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                          {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]}
                                                        ]
                                         },
                  "uplinkSets": [
                      {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                  ]}

sflow_lig_static = {"type": LIG_Version,
                    "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                    "description": None,
                    "name": "LIG_STATIC",
                    "interconnectMapTemplate": icmap_ME,
                    "enclosureType": "SY12000",
                    "enclosureIndexes": [1],
                    "interconnectBaySet": "3",
                    "redundancyType": "Redundant",
                    "internalNetworkUris": [],
                    "snmpConfiguration": None,
                    "qosConfiguration": None,
                    "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_200"},
                                           "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "20.20.20.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1}],
                                           "sflowAgents": [{"ipMode": "Static"}],
                                           "sflowPorts": [{"portName": "Q2:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                           "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                            {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]}
                                                          ]
                                           },
                    "uplinkSets": [
                        {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_200"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q2.1', 'speed': 'Auto'}]}
                    ]}

sflow_lig_ippool = {"type": LIG_Version,
                    "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                    "description": None,
                    "name": "LIG_IP_POOL",
                    "interconnectMapTemplate": icmap_ME,
                    "enclosureType": "SY12000",
                    "enclosureIndexes": [1],
                    "interconnectBaySet": "3",
                    "redundancyType": "Redundant",
                    "internalNetworkUris": [],
                    "snmpConfiguration": None,
                    "qosConfiguration": None,
                    "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_300"},
                                           "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "30.30.30.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1}],
                                           "sflowAgents": [{"ipMode": "IpPool"}],
                                           "sflowPorts": [{"portName": "Q3:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                           "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                            {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]}
                                                          ]
                                           },
                    "uplinkSets": [
                        {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_300"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                    ]}

sflow_lig_dhcp_3collectors = {"type": LIG_Version,
                              "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                              "description": None,
                              "name": "LIG_DHCP_3COLLECTORS",
                              "interconnectMapTemplate": icmap_ME,
                              "enclosureType": "SY12000",
                              "enclosureIndexes": [1],
                              "interconnectBaySet": "3",
                              "redundancyType": "Redundant",
                              "internalNetworkUris": [],
                              "snmpConfiguration": None,
                              "qosConfiguration": None,
                              "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                     "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1},
                                                                         {"name": "C200", "collectorEnabled": False, "ipAddress": "20.20.20.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 2},
                                                                         {"name": "C300", "collectorEnabled": False, "ipAddress": "30.30.30.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 3}],
                                                     "sflowAgents": [{"ipMode": "DHCP"}],
                                                     "sflowPorts": [{"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                     "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                                      {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]}
                                                                    ]
                                                     },
                              "uplinkSets": [
                                  {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                   'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                              ]}

sflow_lig_dhcp_static = {"type": LIG_Version,
                         "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                         "description": None,
                         "name": "LIG_DHCP_STATIC",
                         "interconnectMapTemplate": icmap_ME,
                         "enclosureType": "SY12000",
                         "enclosureIndexes": [1],
                         "interconnectBaySet": "3",
                         "redundancyType": "Redundant",
                         "internalNetworkUris": [],
                         "snmpConfiguration": None,
                         "qosConfiguration": None,
                         "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1}
                                                                    ],
                                                "sflowAgents": [{"ipMode": "DHCP"},
                                                                {"ipMode": "Static"}],
                                                "sflowPorts": [{"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                                 {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]}
                                                               ]
                                                },
                         "uplinkSets": [
                                 {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                         ]}

sflow_lig_without_sflowagentipmode = {"type": LIG_Version,
                                      "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                      "description": None,
                                      "name": "LIG_DHCP_STATIC",
                                      "interconnectMapTemplate": icmap_ME,
                                      "enclosureType": "SY12000",
                                      "enclosureIndexes": [1],
                                      "interconnectBaySet": "3",
                                      "redundancyType": "Redundant",
                                      "internalNetworkUris": [],
                                      "snmpConfiguration": None,
                                      "qosConfiguration": None,
                                      "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                             "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1}
                                                                                 ],
                                                             "sflowAgents": [{"ipMode": ""}
                                                                             ],
                                                             "sflowPorts": [{"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                             "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                                              {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]}
                                                                            ]
                                                             },
                                      "uplinkSets": [
                                          {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                           'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                      ]}

sflow_lig_nonexistant_receiver = {"type": LIG_Version,
                                  "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                  "description": None,
                                  "name": "LIG_DHCP_1",
                                  "interconnectMapTemplate": icmap_ME,
                                  "enclosureType": "SY12000",
                                  "enclosureIndexes": [1],
                                  "interconnectBaySet": "3",
                                  "redundancyType": "Redundant",
                                  "internalNetworkUris": [],
                                  "snmpConfiguration": None,
                                  "qosConfiguration": None,
                                  "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                         "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1}],
                                                         "sflowAgents": [{"ipMode": "DHCP"}],
                                                         "sflowPorts": [{"portName": "Q1:1", "collectorId": "2", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                         "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                                          {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]}
                                                                        ]
                                                         },
                                  "uplinkSets": [
                                      {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                       'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                  ]}

LIG1 = 'LIG_DHCP'
sflow_editlig_more_uplinkports = {"type": LIG_Version,
                                  "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                  "description": None,
                                  "name": "LIG_DHCP",
                                  "interconnectMapTemplate": icmap_ME,
                                  "enclosureType": "SY12000",
                                  "enclosureIndexes": [1],
                                  "interconnectBaySet": "3",
                                  "redundancyType": "Redundant",
                                  "internalNetworkUris": [],
                                  "snmpConfiguration": None,
                                  "qosConfiguration": None,
                                  "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                         "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1}],
                                                         "sflowAgents": [{"ipMode": "DHCP"}],
                                                         "sflowPorts": [{"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                         "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                                          {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]},
                                                                        {"portName": "Q2:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                         "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                                          {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "16777216", "samplingEnabled": True}]},
                                                                        {"portName": "Q3:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                         "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "604800", "pollingEnabled": True},
                                                                                                                          {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "257", "samplingEnabled": True}]}
                                                                        ]
                                                         },
                                  "uplinkSets": [
                                      {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                       'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                  ]}

sflow_edit_lig_change_collectorid = {"type": LIG_Version,
                                     "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                     "description": None,
                                     "name": "LIG_DHCP",
                                     "interconnectMapTemplate": icmap_ME,
                                     "enclosureType": "SY12000",
                                     "enclosureIndexes": [1],
                                     "interconnectBaySet": "3",
                                     "redundancyType": "Redundant",
                                     "internalNetworkUris": [],
                                     "snmpConfiguration": None,
                                     "qosConfiguration": None,
                                     "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                            "sflowCollectors": [{"name": "C100", "collectorEnabled": False, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1},
                                                                                {"name": "C200", "collectorEnabled": True, "ipAddress": "50.50.50.1", "maxDatagramSize": "4000", "maxHeaderSize": "1024", "port": "6343", "collectorId": 2}],
                                                            "sflowAgents": [{"ipMode": "DHCP"}],
                                                            "sflowPorts": [{"portName": "Q1:1", "collectorId": 2, "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                            "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                                             {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]}
                                                                           ]
                                                            },
                                     "uplinkSets": [
                                         {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                          'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                     ]}

sflow_edit_lig_disable_collector = {"type": LIG_Version,
                                    "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                    "description": None,
                                    "name": "LIG_DHCP",
                                    "interconnectMapTemplate": icmap_ME,
                                    "enclosureType": "SY12000",
                                    "enclosureIndexes": [1],
                                    "interconnectBaySet": "3",
                                    "redundancyType": "Redundant",
                                    "internalNetworkUris": [],
                                    "snmpConfiguration": None,
                                    "qosConfiguration": None,
                                    "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                           "sflowCollectors": [{"name": "C100", "collectorEnabled": False, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1}],
                                                           "sflowAgents": [{"ipMode": "DHCP"}],
                                                           "sflowPorts": [{"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                           "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                                            {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]}
                                                                          ]
                                                           },
                                    "uplinkSets": [
                                        {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                         'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                    ]}

sflow_edit_lig_max_datagramsize = {"type": LIG_Version,
                                   "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                   "description": None,
                                   "name": "LIG_DHCP",
                                   "interconnectMapTemplate": icmap_ME,
                                   "enclosureType": "SY12000",
                                   "enclosureIndexes": [1],
                                   "interconnectBaySet": "3",
                                   "redundancyType": "Redundant",
                                   "internalNetworkUris": [],
                                   "snmpConfiguration": None,
                                   "qosConfiguration": None,
                                   "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                          "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "10.10.10.1", "maxDatagramSize": "9000", "maxHeaderSize": "128", "port": "6343", "collectorId": 1}],
                                                          "sflowAgents": [{"ipMode": "DHCP"}],
                                                          "sflowPorts": [{"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                          "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                                           {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]}
                                                                         ]
                                                          },
                                   "uplinkSets": [
                                       {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                        'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                   ]}

sflow_edit_lig_invalid_max_datagramsize = {"type": LIG_Version,
                                           "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                           "description": None,
                                           "name": "LIG_DHCP",
                                           "interconnectMapTemplate": icmap_ME,
                                           "enclosureType": "SY12000",
                                           "enclosureIndexes": [1],
                                           "interconnectBaySet": "3",
                                           "redundancyType": "Redundant",
                                           "internalNetworkUris": [],
                                           "snmpConfiguration": None,
                                           "qosConfiguration": None,
                                           "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                                  "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "10.10.10.1", "maxDatagramSize": "19000", "maxHeaderSize": "128", "port": "6343", "collectorId": 1}],
                                                                  "sflowAgents": [{"ipMode": "DHCP"}],
                                                                  "sflowPorts": [{"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                                  "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                                                   {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]}
                                                                                 ]
                                                                  },
                                           "uplinkSets": [
                                               {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                                'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                           ]}
sflow_edit_lig_max_headersize = {"type": LIG_Version,
                                 "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                 "description": None,
                                 "name": "LIG_DHCP",
                                 "interconnectMapTemplate": icmap_ME,
                                 "enclosureType": "SY12000",
                                 "enclosureIndexes": [1],
                                 "interconnectBaySet": "3",
                                 "redundancyType": "Redundant",
                                 "internalNetworkUris": [],
                                 "snmpConfiguration": None,
                                 "qosConfiguration": None,
                                 "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                        "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "1024", "port": "6343", "collectorId": 1}],
                                                        "sflowAgents": [{"ipMode": "DHCP"}],
                                                        "sflowPorts": [{"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                        "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                                         {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]}
                                                                       ]
                                                        },
                                 "uplinkSets": [
                                     {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                      'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                 ]}

sflow_edit_lig_invalid_max_headersize = {"type": LIG_Version,
                                         "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                         "description": None,
                                         "name": "LIG_DHCP",
                                         "interconnectMapTemplate": icmap_ME,
                                         "enclosureType": "SY12000",
                                         "enclosureIndexes": [1],
                                         "interconnectBaySet": "3",
                                         "redundancyType": "Redundant",
                                         "internalNetworkUris": [],
                                         "snmpConfiguration": None,
                                         "qosConfiguration": None,
                                         "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                                "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "1025", "port": "6343", "collectorId": 1}],
                                                                "sflowAgents": [{"ipMode": "DHCP"}],
                                                                "sflowPorts": [{"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                                "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                                                 {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]}
                                                                               ]
                                                                },
                                         "uplinkSets": [
                                             {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                              'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                         ]}

sflow_edit_lig_disabled_collectors = {"type": LIG_Version,
                                      "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                      "description": None,
                                      "name": "LIG_DHCP",
                                      "interconnectMapTemplate": icmap_ME,
                                      "enclosureType": "SY12000",
                                      "enclosureIndexes": [1],
                                      "interconnectBaySet": "3",
                                      "redundancyType": "Redundant",
                                      "internalNetworkUris": [],
                                      "snmpConfiguration": None,
                                      "qosConfiguration": None,
                                      "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                             "sflowCollectors": [{"name": "C100", "collectorEnabled": False, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1},
                                                                                 {"name": "C200", "collectorEnabled": False, "ipAddress": "50.50.50.1", "maxDatagramSize": "4000", "maxHeaderSize": "1024", "port": "6343", "collectorId": 2}],
                                                             "sflowAgents": [{"ipMode": "DHCP"}],
                                                             "sflowPorts": [{"portName": "Q1:1", "collectorId": "2", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                             "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                                              {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]}
                                                                            ]
                                                             },
                                      "uplinkSets": [
                                          {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                           'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                      ]}

sflow_edit_lig_enable_one_collector = {"type": LIG_Version,
                                       "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                       "description": None,
                                       "name": "LIG_DHCP",
                                       "interconnectMapTemplate": icmap_ME,
                                       "enclosureType": "SY12000",
                                       "enclosureIndexes": [1],
                                       "interconnectBaySet": "3",
                                       "redundancyType": "Redundant",
                                       "internalNetworkUris": [],
                                       "snmpConfiguration": None,
                                       "qosConfiguration": None,
                                       "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                              "sflowCollectors": [{"name": "C100", "collectorEnabled": False, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1},
                                                                                  {"name": "C200", "collectorEnabled": True, "ipAddress": "50.50.50.1", "maxDatagramSize": "4000", "maxHeaderSize": "1024", "port": "6343", "collectorId": 2}],
                                                              "sflowAgents": [{"ipMode": "DHCP"}],
                                                              "sflowPorts": [{"portName": "Q1:1", "collectorId": "2", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                              "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                                               {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]}
                                                                             ]
                                                              },
                                       "uplinkSets": [
                                           {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                            'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                       ]}

sflow_edit_lig_sampling_collector = {"type": LIG_Version,
                                     "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                     "description": None,
                                     "name": "LIG_DHCP",
                                     "interconnectMapTemplate": icmap_ME,
                                     "enclosureType": "SY12000",
                                     "enclosureIndexes": [1],
                                     "interconnectBaySet": "3",
                                     "redundancyType": "Redundant",
                                     "internalNetworkUris": [],
                                     "snmpConfiguration": None,
                                     "qosConfiguration": None,
                                     "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                            "sflowCollectors": [{"name": "C100", "collectorEnabled": False, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1},
                                                                                {"name": "C200", "collectorEnabled": True, "ipAddress": "50.50.50.1", "maxDatagramSize": "4000", "maxHeaderSize": "1024", "port": "6343", "collectorId": 2}],
                                                            "sflowAgents": [{"ipMode": "DHCP"}],
                                                            "sflowPorts": [{"portName": "Q1:1", "collectorId": "2", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                            "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}
                                                                                                                             ]}
                                                                           ]
                                                            },
                                     "uplinkSets": [
                                         {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                          'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                     ]}

sflow_edit_lig_polling_collector = {"type": LIG_Version,
                                    "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                    "description": None,
                                    "name": "LIG_DHCP",
                                    "interconnectMapTemplate": icmap_ME,
                                    "enclosureType": "SY12000",
                                    "enclosureIndexes": [1],
                                    "interconnectBaySet": "3",
                                    "redundancyType": "Redundant",
                                    "internalNetworkUris": [],
                                    "snmpConfiguration": None,
                                    "qosConfiguration": None,
                                    "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                           "sflowCollectors": [{"name": "C100", "collectorEnabled": False, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1},
                                                                               {"name": "C200", "collectorEnabled": True, "ipAddress": "50.50.50.1", "maxDatagramSize": "4000", "maxHeaderSize": "1024", "port": "6343", "collectorId": 2}],
                                                           "sflowAgents": [{"ipMode": "DHCP"}],
                                                           "sflowPorts": [{"portName": "Q1:1", "collectorId": "2", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                           "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True}
                                                                                                                            ]}
                                                                          ]
                                                           },
                                    "uplinkSets": [
                                        {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                         'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                    ]}

sflow_edit_lig_sampling_changing_ip_of_collector = {"type": LIG_Version,
                                                    "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                                    "description": None,
                                                    "name": "LIG_DHCP",
                                                    "interconnectMapTemplate": icmap_ME,
                                                    "enclosureType": "SY12000",
                                                    "enclosureIndexes": [1],
                                                    "interconnectBaySet": "3",
                                                    "redundancyType": "Redundant",
                                                    "internalNetworkUris": [],
                                                    "snmpConfiguration": None,
                                                    "qosConfiguration": None,
                                                    "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                                           "sflowCollectors": [{"name": "C100", "collectorEnabled": False, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1},
                                                                                               {"name": "C200", "collectorEnabled": True, "ipAddress": "90.90.90.1", "maxDatagramSize": "4000", "maxHeaderSize": "1024", "port": "6343", "collectorId": 2}],
                                                                           "sflowAgents": [{"ipMode": "DHCP"}],
                                                                           "sflowPorts": [{"portName": "Q1:1", "collectorId": "2", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                                           "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}
                                                                                                                                            ]}
                                                                                          ]
                                                                           },
                                                    "uplinkSets": [
                                                        {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                                         'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                                    ]}

sflow_edit_lig_polling_changing_ip_of_collector = {"type": LIG_Version,
                                                   "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                                   "description": None,
                                                   "name": "LIG_DHCP",
                                                   "interconnectMapTemplate": icmap_ME,
                                                   "enclosureType": "SY12000",
                                                   "enclosureIndexes": [1],
                                                   "interconnectBaySet": "3",
                                                   "redundancyType": "Redundant",
                                                   "internalNetworkUris": [],
                                                   "snmpConfiguration": None,
                                                   "qosConfiguration": None,
                                                   "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                                          "sflowCollectors": [{"name": "C100", "collectorEnabled": False, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1},
                                                                                              {"name": "C200", "collectorEnabled": True, "ipAddress": "70.70.70.1", "maxDatagramSize": "4000", "maxHeaderSize": "1024", "port": "6343", "collectorId": 2}],
                                                                          "sflowAgents": [{"ipMode": "DHCP"}],
                                                                          "sflowPorts": [{"portName": "Q1:1", "collectorId": "2", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                                          "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True}
                                                                                                                                           ]}
                                                                                         ]
                                                                          },
                                                   "uplinkSets": [
                                                       {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                                        'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                                   ]}

sflow_edit_lig_sampling_changing_port_of_collector = {"type": LIG_Version,
                                                      "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                                      "description": None,
                                                      "name": "LIG_DHCP",
                                                      "interconnectMapTemplate": icmap_ME,
                                                      "enclosureType": "SY12000",
                                                      "enclosureIndexes": [1],
                                                      "interconnectBaySet": "3",
                                                      "redundancyType": "Redundant",
                                                      "internalNetworkUris": [],
                                                      "snmpConfiguration": None,
                                                      "qosConfiguration": None,
                                                      "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                                             "sflowCollectors": [{"name": "C100", "collectorEnabled": False, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1},
                                                                                                 {"name": "C200", "collectorEnabled": True, "ipAddress": "90.90.90.1", "maxDatagramSize": "4000", "maxHeaderSize": "1024", "port": "65535", "collectorId": 2}],
                                                                             "sflowAgents": [{"ipMode": "DHCP"}],
                                                                             "sflowPorts": [{"portName": "Q1:1", "collectorId": "2", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                                             "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}
                                                                                                                                              ]}
                                                                                            ]
                                                                             },
                                                      "uplinkSets": [
                                                          {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                                           'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                                      ]}

sflow_edit_lig_sampling_changing_invalidport_of_collector = {"type": LIG_Version,
                                                             "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                                             "description": None,
                                                             "name": "LIG_DHCP",
                                                             "interconnectMapTemplate": icmap_ME,
                                                             "enclosureType": "SY12000",
                                                             "enclosureIndexes": [1],
                                                             "interconnectBaySet": "3",
                                                             "redundancyType": "Redundant",
                                                             "internalNetworkUris": [],
                                                             "snmpConfiguration": None,
                                                             "qosConfiguration": None,
                                                             "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                                                    "sflowCollectors": [{"name": "C100", "collectorEnabled": False, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1},
                                                                                                        {"name": "C200", "collectorEnabled": True, "ipAddress": "90.90.90.1", "maxDatagramSize": "4000", "maxHeaderSize": "1024", "port": "655345", "collectorId": 2}],
                                                                                    "sflowAgents": [{"ipMode": "DHCP"}],
                                                                                    "sflowPorts": [{"portName": "Q1:1", "collectorId": "2", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                                                    "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}
                                                                                                                                                     ]}
                                                                                                   ]
                                                                                    },
                                                             "uplinkSets": [
                                                                 {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                                                  'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                                             ]}

sflow_edit_lig_removing_collector = {"type": LIG_Version,
                                     "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                     "description": None,
                                     "name": "LIG_DHCP",
                                     "interconnectMapTemplate": icmap_ME,
                                     "enclosureType": "SY12000",
                                     "enclosureIndexes": [1],
                                     "interconnectBaySet": "3",
                                     "redundancyType": "Redundant",
                                     "internalNetworkUris": [],
                                     "snmpConfiguration": None,
                                     "qosConfiguration": None,
                                     "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                            "sflowCollectors": [{"name": "C100", "collectorEnabled": False, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1}
                                                                                ],
                                                            "sflowAgents": [{"ipMode": "DHCP"}],
                                                            "sflowPorts": [{"portName": "Q1:1", "collectorId": "2", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                            "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}
                                                                                                                             ]}
                                                                           ]
                                                            },
                                     "uplinkSets": [
                                         {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                          'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                     ]}

sflow_edit_lig_wrong_collectorid_for_port = {"type": LIG_Version,
                                             "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                             "description": None,
                                             "name": "LIG_DHCP",
                                             "interconnectMapTemplate": icmap_ME,
                                             "enclosureType": "SY12000",
                                             "enclosureIndexes": [1],
                                             "interconnectBaySet": "3",
                                             "redundancyType": "Redundant",
                                             "internalNetworkUris": [],
                                             "snmpConfiguration": None,
                                             "qosConfiguration": None,
                                             "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                                    "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1},
                                                                                        {"name": "C200", "collectorEnabled": True, "ipAddress": "50.50.50.1", "maxDatagramSize": "4000", "maxHeaderSize": "1024", "port": "6343", "collectorId": 2}],
                                                                    "sflowAgents": [{"ipMode": "DHCP"}],
                                                                    "sflowPorts": [{"portName": "Q1:1", "collectorId": "3", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                                    "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                                                     {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]}
                                                                                   ]
                                                                    },
                                             "uplinkSets": [
                                                 {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                                  'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                             ]}

sflow_edit_lig_wrong_collectorid = {"type": LIG_Version,
                                    "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                    "description": None,
                                    "name": "LIG_DHCP",
                                    "interconnectMapTemplate": icmap_ME,
                                    "enclosureType": "SY12000",
                                    "enclosureIndexes": [1],
                                    "interconnectBaySet": "3",
                                    "redundancyType": "Redundant",
                                    "internalNetworkUris": [],
                                    "snmpConfiguration": None,
                                    "qosConfiguration": None,
                                    "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                           "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1},
                                                                               {"name": "C200", "collectorEnabled": True, "ipAddress": "50.50.50.1", "maxDatagramSize": "4000", "maxHeaderSize": "1024", "port": "6343", "collectorId": 4}],
                                                           "sflowAgents": [{"ipMode": "DHCP"}],
                                                           "sflowPorts": [{"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                           "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                                            {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]}
                                                                          ]
                                                           },
                                    "uplinkSets": [
                                        {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                         'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                    ]}

sflow_edit_lig_duplicate_collectorname = {"type": LIG_Version,
                                          "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                          "description": None,
                                          "name": "LIG_DHCP",
                                          "interconnectMapTemplate": icmap_ME,
                                          "enclosureType": "SY12000",
                                          "enclosureIndexes": [1],
                                          "interconnectBaySet": "3",
                                          "redundancyType": "Redundant",
                                          "internalNetworkUris": [],
                                          "snmpConfiguration": None,
                                          "qosConfiguration": None,
                                          "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                                 "sflowCollectors": [{"name": "C100", "collectorEnabled": False, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1},
                                                                                     {"name": "C100", "collectorEnabled": True, "ipAddress": "90.90.90.1", "maxDatagramSize": "4000", "maxHeaderSize": "1024", "port": "65535", "collectorId": 2}],
                                                                 "sflowAgents": [{"ipMode": "DHCP"}],
                                                                 "sflowPorts": [{"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                                 "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}
                                                                                                                                  ]}
                                                                                ]
                                                                 },
                                          "uplinkSets": [
                                              {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                               'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                          ]}
sflow_edit_lig_without_sampling_interval = {"type": LIG_Version,
                                            "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                            "description": None,
                                            "name": "LIG_DHCP",
                                            "interconnectMapTemplate": icmap_ME,
                                            "enclosureType": "SY12000",
                                            "enclosureIndexes": [1],
                                            "interconnectBaySet": "3",
                                            "redundancyType": "Redundant",
                                            "internalNetworkUris": [],
                                            "snmpConfiguration": None,
                                            "qosConfiguration": None,
                                            "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                                   "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1},
                                                                                       {"name": "C200", "collectorEnabled": True, "ipAddress": "20.20.20.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 2},
                                                                                       {"name": "C300", "collectorEnabled": True, "ipAddress": "30.30.30.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 3}],
                                                                   "sflowAgents": [{"ipMode": "DHCP"}],
                                                                   "sflowPorts": [{"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                                   "enclosureIndex": 1, "sflowConfigurationModes": [
                                                                                       {"configurationMode": "Sampling", "direction": "BOTH", "samplingEnabled": True}]}
                                                                                  ]
                                                                   },
                                            "uplinkSets": [
                                                {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                                 'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                            ]}
sflow_edit_lig_without_polling_interval = {"type": LIG_Version,
                                           "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                           "description": None,
                                           "name": "LIG_DHCP",
                                           "interconnectMapTemplate": icmap_ME,
                                           "enclosureType": "SY12000",
                                           "enclosureIndexes": [1],
                                           "interconnectBaySet": "3",
                                           "redundancyType": "Redundant",
                                           "internalNetworkUris": [],
                                           "snmpConfiguration": None,
                                           "qosConfiguration": None,
                                           "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                                  "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1},
                                                                                      {"name": "C200", "collectorEnabled": True, "ipAddress": "20.20.20.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 2},
                                                                                      {"name": "C300", "collectorEnabled": True, "ipAddress": "30.30.30.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 3}],
                                                                  "sflowAgents": [{"ipMode": "DHCP"}],
                                                                  "sflowPorts": [{"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                                  "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingEnabled": True}
                                                                                                                                   ]}
                                                                                 ]
                                                                  },
                                           "uplinkSets": [
                                               {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                                'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                           ]}

sflow_edit_lig_invalid_sampling_rate = {"type": LIG_Version,
                                        "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                        "description": None,
                                        "name": "LIG_DHCP",
                                        "interconnectMapTemplate": icmap_ME,
                                        "enclosureType": "SY12000",
                                        "enclosureIndexes": [1],
                                        "interconnectBaySet": "3",
                                        "redundancyType": "Redundant",
                                        "internalNetworkUris": [],
                                        "snmpConfiguration": None,
                                        "qosConfiguration": None,
                                        "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                               "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1},
                                                                                   {"name": "C200", "collectorEnabled": False, "ipAddress": "20.20.20.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 2},
                                                                                   {"name": "C300", "collectorEnabled": False, "ipAddress": "30.30.30.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 3}],
                                                               "sflowAgents": [{"ipMode": "DHCP"}],
                                                               "sflowPorts": [{"portName": "Q1:1", "collectorId": 1, "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                               "enclosureIndex": 1, "sflowConfigurationModes": [
                                                                                   {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "255", "samplingEnabled": True}]}
                                                                              ]
                                                               },
                                        "uplinkSets": [
                                            {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                             'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                        ]}
sflow_edit_lig_invalid_polling_rate = {"type": LIG_Version,
                                       "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                                       "description": None,
                                       "name": "LIG_DHCP",
                                       "interconnectMapTemplate": icmap_ME,
                                       "enclosureType": "SY12000",
                                       "enclosureIndexes": [1],
                                       "interconnectBaySet": "3",
                                       "redundancyType": "Redundant",
                                       "internalNetworkUris": [],
                                       "snmpConfiguration": None,
                                       "qosConfiguration": None,
                                       "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_100"},
                                                              "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "10.10.10.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1},
                                                                                  {"name": "C200", "collectorEnabled": True, "ipAddress": "20.20.20.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 2},
                                                                                  {"name": "C300", "collectorEnabled": True, "ipAddress": "30.30.30.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 3}],
                                                              "sflowAgents": [{"ipMode": "DHCP"}],
                                                              "sflowPorts": [{"portName": "Q1:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                                              "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "604801", "pollingEnabled": True}
                                                                                                                               ]}
                                                                             ]
                                                              },
                                       "uplinkSets": [
                                           {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_100"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                                            'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}]}
                                       ]}

eth_networks = [{"vlanId": "100", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "net_100", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "101", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "net_200", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "300", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "net_301", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "1", "ethernetNetworkType": "Tunnel", "subnetUri": None, "purpose": "General", "name": "tunnel_nw", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version},
                {"vlanId": "100", "ethernetNetworkType": "Tagged", "subnetUri": None, "purpose": "General", "name": "us1_eth100", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version}]

eth_networks_subnet = {"vlanId": "102", "ethernetNetworkType": "Tagged", "subnetUri": '', "purpose": "General", "name": "net_300", "smartLink": 'true', "privateNetwork": 'false', "connectionTemplateUri": None, "type": eth_network_Version}

sflow_lig_for_le = {"type": LIG_Version,
                    "ethernetSettings": {"type": 'EthernetInterconnectSettingsV4', "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                    "description": None,
                    "name": "LIG",
                    "interconnectMapTemplate": icmap_ME,
                    "enclosureType": "SY12000",
                    "enclosureIndexes": [1],
                    "interconnectBaySet": "3",
                    "redundancyType": "Redundant",
                    "internalNetworkUris": [],
                    "snmpConfiguration": None,
                    "qosConfiguration": None,
                    "sflowConfiguration": {"type": "sflow-configuration", "enabled": True, "sflowNetwork": {"name": "net_200"},
                                           "sflowCollectors": [{"name": "C100", "collectorEnabled": True, "ipAddress": "20.20.20.1", "maxDatagramSize": "1400", "maxHeaderSize": "128", "port": "6343", "collectorId": 1}],
                                           "sflowAgents": [{"ipMode": "Static"}],
                                           "sflowPorts": [{"portName": "Q2:1", "collectorId": "1", "icmName": "Virtual Connect SE 40Gb F8 Module for Synergy", "bayNumber": 3,
                                                           "enclosureIndex": 1, "sflowConfigurationModes": [{"configurationMode": "Polling", "pollingInterval": "20", "pollingEnabled": True},
                                                                                                            {"configurationMode": "Sampling", "direction": "BOTH", "samplingRate": "256", "samplingEnabled": True}]}
                                                          ]
                                           },
                    "uplinkSets": [
                        {'name': 'us1_eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ["net_200"], 'primaryPort': None, 'nativeNetworkUri': None, 'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q2.1', 'speed': 'Auto'}]}
                    ]}

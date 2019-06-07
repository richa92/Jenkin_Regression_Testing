"""
    Data File for Nitro Lacp features
"""

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ethernet_networks = [
    {"vlanIdRange": "21-25",
     "namePrefix": "Eth_network",
     "privateNetwork": False,
     "smartLink": True,
     "purpose": "General",
     "type": "bulk-ethernet-networkV2",
     "bandwidth": {"maximumBandwidth": 20000, "typicalBandwidth": 2500},
     }
]

Nitro_LI_ibs2 = {'name': 'LE-LIG-LACP'}

ENC1 = 'SGH734VBEB'
ENC2 = 'SGH734VBE6'
POTASH = 'Virtual Connect SE 40Gb F8 Module for Synergy'
NITRO = 'Virtual Connect SE 100Gb F32 Module for Synergy'
METHANE = 'Synergy 50Gb Interconnect Link Module'
LIG_Version = 'logical-interconnect-groupV7'
LIG_ethernet_version = 'EthernetInterconnectSettingsV6'
eth_network_Version = 'ethernet-networkV4'
fcoe_network_version = 'fcoe-networkV4'
fc_network_version = 'fc-networkV4'
UPLINK_TYPE = 'uplink-setV6'
SERVER_PROFILE = 'ServerProfileV10'
LE_NAME = "LE"
LIG_NAME = "LIG-LACP2"
LI_NAME = LE_NAME + '-' + LIG_NAME
US_NAME = 'US1'
US_EDIT_NAME = 'US_Edit'
ICM_3 = ENC1 + ', interconnect 3'
ICM_6 = ENC1 + ', interconnect 6'
ICM_2_ENC1 = ENC1 + ', interconnect 2'
ICM_5_ENC1 = ENC1 + ', interconnect 5'
ICM_2_ENC2 = ENC2 + ', interconnect 2'
ICM_5_ENC2 = ENC2 + ', interconnect 5'
Source_Destination_Mac_Snmp = 'Source and Destination MAC Address'
Source_Destination_IP_Snmp = 'Source and Destination IP Address'
Source_Mac_Snmp = 'Source MAC Address'
Destination_Mac_Snmp = 'Destination MAC Address'
Source_IP_Snmp = 'Source IP Address'
Destination_IP_Snmp = 'Destination IP Address'
Load_Source_Destination_Mac = 'SourceAndDestinationMac'
Load_Source_Destination_Ip = 'SourceAndDestinationIp'
Load_Destination_Mac = 'DestinationMac'
Load_Destination_Ip = 'DestinationIp'
Load_Source_Mac = 'SourceMac'
Load_Source_Ip = 'SourceIp'


uplink_fibre = 'FibreChannel'

uplink_sets = {'US1': {
    'name': 'US1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
    'networkUris': ['Eth_network_21'],
    'mode': 'Auto',
    'loadBalancingMode': 'SourceAndDestinationIp',
    'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1:1', 'speed': 'Speed10G'},
                               {'enclosure': '1', 'bay': '2', 'port': 'Q1:2', 'speed': 'Speed10G'},
                               {'enclosure': '2', 'bay': '5', 'port': 'Q2:1', 'speed': 'Speed10G'},
                               {'enclosure': '2', 'bay': '5', 'port': 'Q2:2', 'speed': 'Speed10G'}],
}
}

uplink_set_tunnel = {'US1': {
    'name': 'US1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tunnel',
    'networkUris': ['Eth_network_21'],
    'mode': 'Auto',
    'loadBalancingMode': 'SourceAndDestinationIp',
    'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1:1', 'speed': 'Speed10G'},
                               {'enclosure': '1', 'bay': '2', 'port': 'Q1:2', 'speed': 'Speed10G'},
                               {'enclosure': '2', 'bay': '5', 'port': 'Q2:1', 'speed': 'Speed10G'},
                               {'enclosure': '2', 'bay': '5', 'port': 'Q2:2', 'speed': 'Speed10G'}],
}
}

US_Edit_LoadBalancing = {'name': 'US1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                         'networkUris': ['Eth_network_21'],
                         'mode': 'Auto',
                         'lacpTimer': "Short",
                         'loadBalancingMode': "SourceIp",
                         'fcMode': "NA",
                         'fcoeMlagMode': "None",
                         'fcoeNetworkMlagBays': [],
                         'nativeNetworkUri': None,
                         'primaryPort': None,
                         'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1:1', 'speed': 'Speed10G'},
                                                    {'enclosure': '1', 'bay': '2', 'port': 'Q1:2', 'speed': 'Speed10G'},
                                                    {'enclosure': '2', 'bay': '5', 'port': 'Q2:1', 'speed': 'Speed10G'},
                                                    {'enclosure': '2', 'bay': '5', 'port': 'Q2:2', 'speed': 'Speed10G'}],
                         'privateVlanDomains': []

                         }

US_Del_Port = [{'name': 'US1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                'networkUris': ['Eth_network_21'],
                'mode': 'Auto',
                'lacpTimer':"Short",
                'loadBalancingMode':"SourceIp",
                'fcMode': "NA",
                'fcoeMlagMode': "None",
                            'fcoeNetworkMlagBays': [],
                            'nativeNetworkUri': None,
                            'primaryPort': None,
                'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1:1', 'speed': 'Speed25G'},
                                           {'enclosure': '1', 'bay': '2', 'port': 'Q1:2', 'speed': 'Speed25G'},
                                           {'enclosure': '2', 'bay': '5', 'port': 'Q2:1', 'speed': 'Speed25G'}],
                'privateVlanDomains': []
                }]


US_Del_Port_2 = [
    {'consistencyChecking': 'ExactMatch',
     'ethernetNetworkType': 'Tagged',
     'fcMode': 'NA',
     'lacpTimer': 'Short',
     'loadBalancingMode': 'SourceMac',
     'logicalPortConfigInfos': [
         {'desiredFecMode': 'Auto', 'desiredSpeed': 'Speed10G', 'logicalLocation': {'locationEntries': [{'relativeValue': 2, 'type': 'Enclosure'}, {'relativeValue': 5, 'type': 'Bay'}, {'relativeValue': 67, 'type': 'Port'}]}},
         {'desiredFecMode': 'Auto', 'desiredSpeed': 'Speed10G', 'logicalLocation': {'locationEntries': [{'relativeValue': 2, 'type': 'Bay'}, {'relativeValue': 1, 'type': 'Enclosure'}, {'relativeValue': 62, 'type': 'Port'}]}},
         {'desiredFecMode': 'Auto', 'desiredSpeed': 'Speed10G', 'logicalLocation': {'locationEntries': [{'relativeValue': 2, 'type': 'Enclosure'}, {'relativeValue': 5, 'type': 'Bay'}, {'relativeValue': 68, 'type': 'Port'}]}}
     ],
     }
]

Del_port_uplink = [{"desiredFecMode": "Auto", "desiredSpeed": "Speed10G", "logicalLocation": {"locationEntries": [{"relativeValue": 2, "type": "Enclosure"}, {"relativeValue": 5, "type": "Bay"}, {"relativeValue": 67, "type": "Port"}]}},
                   {"desiredFecMode": "Auto", "desiredSpeed": "Speed10G", "logicalLocation": {"locationEntries": [{"relativeValue": 2, "type": "Bay"}, {"relativeValue": 1, "type": "Enclosure"}, {"relativeValue": 62, "type": "Port"}]}},
                   {"desiredFecMode": "Auto", "desiredSpeed": "Speed10G", "logicalLocation": {"locationEntries": [{"relativeValue": 2, "type": "Enclosure"}, {"relativeValue": 5, "type": "Bay"}, {"relativeValue": 68, "type": "Port"}]}}]

Add_port_uplink = [{"desiredFecMode": "Auto", "desiredSpeed": "Speed10G", "logicalLocation": {"locationEntries": [{"relativeValue": 2, "type": "Enclosure"}, {"relativeValue": 5, "type": "Bay"}, {"relativeValue": 67, "type": "Port"}]}},
                   {"desiredFecMode": "Auto", "desiredSpeed": "Speed10G", "logicalLocation": {"locationEntries": [{"relativeValue": 2, "type": "Bay"}, {"relativeValue": 1, "type": "Enclosure"}, {"relativeValue": 62, "type": "Port"}]}},
                   {"desiredFecMode": "Auto", "desiredSpeed": "Speed10G", "logicalLocation": {"locationEntries": [{"relativeValue": 2, "type": "Bay"}, {"relativeValue": 1, "type": "Enclosure"}, {"relativeValue": 63, "type": "Port"}]}},
                   {"desiredFecMode": "Auto", "desiredSpeed": "Speed10G", "logicalLocation": {"locationEntries": [{"relativeValue": 2, "type": "Enclosure"}, {"relativeValue": 5, "type": "Bay"}, {"relativeValue": 68, "type": "Port"}]}}]


US_Edit_LoadBalancing_old = {'name': 'US1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                             'networkUris': ['Eth_network_21'],
                             'mode': 'Auto',
                             'lacpTimer': "Short",
                             'loadBalancingMode': "SourceIp",
                             'fcMode': "NA",
                             'fcoeMlagMode': "None",
                             'fcoeNetworkMlagBays': [],
                             'nativeNetworkUri': None,
                             'primaryPort': None,
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1:1', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q2:1', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '6', 'port': 'Q1:1', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '6', 'port': 'Q2:1', 'speed': 'Auto'}],
                             'privateVlanDomains': []

                             }


ligs = {"name": "LIG-LACP2",
        "type": LIG_Version,
        "downlinkSpeedMode": "SPEED_10GB",
        "enclosureType": "SY12000",
        "ethernetSettings": {'type': LIG_ethernet_version, 'interconnectType': 'Ethernet', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5,
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
        'interconnectMapTemplate': [{'bay': 2, 'enclosure': 1, 'type': NITRO, 'enclosureIndex': 1},
                                    {'bay': 5, 'enclosure': 1, 'type': METHANE, 'enclosureIndex': 1},
                                    {'bay': 2, 'enclosure': 2, 'type': METHANE, 'enclosureIndex': 2},
                                    {'bay': 5, 'enclosure': 2, 'type': NITRO, 'enclosureIndex': 2}],
        "internalNetworkUris": [],
        'interconnectBaySet': 2,
        'redundancyType': 'HighlyAvailable',
        'enclosureIndexes': [1, 2],
        "qosConfiguration": {"activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough", "downlinkClassificationType": None, "uplinkClassificationType": None, "qosTrafficClassifiers": None, "description": None, "status": None, "name": None, "state": None, "category": "qos-aggregated-configuration", "created": None, "modified": None, "eTag": None, "uri": None}, "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None, "type": "qos-aggregated-configuration", "name": None, "state": None, "status": None, "eTag": None, "modified": None, "created": None, "category": "qos-aggregated-configuration", "uri": None}
        }


ligs_edit = [{"name": "LIG-LACP",
              "type": LIG_Version,
              "enclosureType": "SY12000",
              "ethernetSettings": {'type': LIG_ethernet_version, 'interconnectType': 'Ethernet', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5,
                                   'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True},
              "description": None,
              "status": None,
              "state": None,
              "category": None,
              "created": "logical-interconnect-groups",
              "modified": None,
              "eTag": None,
              "uri": None,
              "uplinkSets": [],
              'interconnectMapTemplate': [{'bay': 2, 'enclosure': 1, 'type': NITRO, 'enclosureIndex': 1},
                                          {'bay': 5, 'enclosure': 1, 'type': METHANE, 'enclosureIndex': 1},
                                          {'bay': 2, 'enclosure': 2, 'type': METHANE, 'enclosureIndex': 2},
                                          {'bay': 5, 'enclosure': 2, 'type': NITRO, 'enclosureIndex': 2}],
              "internalNetworkUris": [],
              'interconnectBaySet': 2,
              'redundancyType': 'HighlyAvailable',
              'enclosureIndexes': [1, 2],
              'telemetryConfiguration': None,
              'snmpConfiguration': None,
              "qosConfiguration": {"activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough", "downlinkClassificationType": None, "uplinkClassificationType": None, "qosTrafficClassifiers": None, "description": None, "status": None, "name": None, "state": None, "category": "qos-aggregated-configuration", "created": None, "modified": None, "eTag": None, "uri": None}, "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None, "type": "qos-aggregated-configuration", "name": None, "state": None, "status": None, "eTag": None, "modified": None, "created": None, "category": "qos-aggregated-configuration", "uri": None}
              }]


li_uplink_sets_LoadBalancing_potash = [{'name': 'US1',
                                        'ethernetNetworkType': 'Tagged',
                                                'networkType': 'Ethernet',
                                                'networkUris': ['Eth_network_21'],
                                                'fcNetworkUris': [],
                                        'fcoeNetworkUris': [],
                                        'lacpTimer': 'Short',
                                        'logicalInterconnectUri': LI_NAME,
                                        'primaryPortLocation': None,
                                        'manualLoginRedistributionState': 'NotSupported',
                                        'connectionMode': 'Auto',
                                        'nativeNetworkUri': None,
                                        'loadBalancingMode':'',
                                        "portConfigInfos":[{"desiredSpeed": "Auto",
                                                            "location": {"locationEntries": [{"value": "Q2:1", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                             {"value": "/rest/enclosures/000000%s" % ENC1, "type": "Enclosure"}
                                                                                             ]
                                                                         }
                                                            },
                                                           {"desiredSpeed": "Auto",
                                                            "location": {"locationEntries": [{"value": "Q1:1", "type": "Port"}, {"value": "3", "type": "Bay"},
                                                                                             {"value": "/rest/enclosures/000000%s" % ENC1, "type": "Enclosure"}
                                                                                             ]
                                                                         }
                                                            },
                                                           {"desiredSpeed": "Auto",
                                                            "location": {"locationEntries": [{"value": "Q2:1", "type": "Port"}, {"value": "6", "type": "Bay"},
                                                                                             {"value": "/rest/enclosures/000000%s" % ENC1, "type": "Enclosure"}
                                                                                             ]
                                                                         }
                                                            },
                                                           {"desiredSpeed": "Auto",
                                                            "location": {"locationEntries": [{"value": "Q1:1", "type": "Port"}, {"value": "6", "type": "Bay"},
                                                                                             {"value": "/rest/enclosures/000000%s" % ENC1, "type": "Enclosure"}
                                                                                             ]
                                                                         }
                                                            }
                                                           ],
                                        "type": UPLINK_TYPE,
                                        "category": "logical-interconnects",
                                        "uri": None,
                                        "privateVlanDomains": []
                                        }]


li_uplink_sets_LoadBalancing = [{'name': 'US1',
                                 'ethernetNetworkType': 'Tagged',
                                         'networkType': 'Ethernet',
                                         'networkUris': ['Eth_network_21'],
                                         'fcNetworkUris': [],
                                         'fcoeNetworkUris': [],
                                         'lacpTimer': 'Short',
                                         'logicalInterconnectUri': LI_NAME,
                                         'primaryPortLocation': None,
                                         'manualLoginRedistributionState': 'NotSupported',
                                         'connectionMode': 'Auto',
                                         'nativeNetworkUri': None,
                                         'loadBalancingMode':'',
                                         "portConfigInfos":[{"desiredSpeed": "Speed10G",
                                                             "location": {"locationEntries": [{"value": "Q1:1", "type": "Port"}, {"value": "2", "type": "Bay"},
                                                                                              {"value": "/rest/enclosures/000000%s" % ENC1, "type": "Enclosure"}
                                                                                              ]
                                                                          }
                                                             },
                                                            {"desiredSpeed": "Speed10G",
                                                             "location": {"locationEntries": [{"value": "Q1:2", "type": "Port"}, {"value": "2", "type": "Bay"},
                                                                                              {"value": "/rest/enclosures/000000%s" % ENC1, "type": "Enclosure"}
                                                                                              ]
                                                                          }
                                                             },
                                                            {"desiredSpeed": "Speed10G",
                                                             "location": {"locationEntries": [{"value": "Q2:1", "type": "Port"}, {"value": "5", "type": "Bay"},
                                                                                              {"value": "/rest/enclosures/797740%s" % ENC2, "type": "Enclosure"}
                                                                                              ]
                                                                          }
                                                             },
                                                            {"desiredSpeed": "Speed10G",
                                                             "location": {"locationEntries": [{"value": "Q2:2", "type": "Port"}, {"value": "5", "type": "Bay"},
                                                                                              {"value": "/rest/enclosures/797740%s" % ENC2, "type": "Enclosure"}
                                                                                              ]
                                                                          }
                                                             }
                                                            ],
                                 "type": UPLINK_TYPE,
                                 "category": "logical-interconnects",
                                 "uri": None,
                                 "privateVlanDomains": []
                                 }]


uplink_All = {'US_Dest_IP': {
    'name': 'US_Dest_IP', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
    'networkUris': ['Eth_network_22'],
    'mode': 'Auto',
    'loadBalancingMode': 'DestinationIp',
    'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1:1', 'speed': 'Auto'},
                               {'enclosure': '1', 'bay': '3', 'port': 'Q2:1', 'speed': 'Auto'},
                               {'enclosure': '1', 'bay': '6', 'port': 'Q1:1', 'speed': 'Auto'},
                               {'enclosure': '1', 'bay': '6', 'port': 'Q2:1', 'speed': 'Auto'}],
},
    'US_Dest_Mac': {
    'name': 'US_Dest_Mac', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                           'networkUris': ['Eth_network_23'],
                           'mode': 'Auto',
                           'loadBalancingMode': 'DestinationMac',
                           'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1:2', 'speed': 'Auto'},
                                                      {'enclosure': '1', 'bay': '3', 'port': 'Q2:2', 'speed': 'Auto'},
                                                      {'enclosure': '1', 'bay': '6', 'port': 'Q1:2', 'speed': 'Auto'},
                                                      {'enclosure': '1', 'bay': '6', 'port': 'Q2:2', 'speed': 'Auto'}],
},
    'US_Source_Mac': {
    'name': 'US_Source_Mac', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
    'networkUris': ['Eth_network_24'],
    'mode': 'Auto',
    'loadBalancingMode': 'SourceMac',
    'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1:3', 'speed': 'Auto'},
                               {'enclosure': '1', 'bay': '3', 'port': 'Q2:3', 'speed': 'Auto'},
                               {'enclosure': '1', 'bay': '6', 'port': 'Q1:3', 'speed': 'Auto'},
                               {'enclosure': '1', 'bay': '6', 'port': 'Q2:3', 'speed': 'Auto'}],
},
    'US_Source_IP': {
    'name': 'US_Source_IP', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
    'networkUris': ['Eth_network_25'],
    'mode': 'Auto',
    'loadBalancingMode': 'SourceIp',
    'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1:4', 'speed': 'Auto'},
                               {'enclosure': '1', 'bay': '3', 'port': 'Q2:4', 'speed': 'Auto'},
                               {'enclosure': '1', 'bay': '6', 'port': 'Q1:4', 'speed': 'Auto'},
                               {'enclosure': '1', 'bay': '6', 'port': 'Q2:4', 'speed': 'Auto'}],
},
    'US_Source_and_Dest_IP': {
    'name': 'US_Source_and_Dest_IP', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
    'networkUris': ['Eth_network_26'],
    'mode': 'Auto',
    'loadBalancingMode': 'SourceAndDestinationIp',
    'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q3:1', 'speed': 'Auto'},
                               {'enclosure': '1', 'bay': '3', 'port': 'Q4:1', 'speed': 'Auto'},
                               {'enclosure': '1', 'bay': '6', 'port': 'Q3:1', 'speed': 'Auto'},
                               {'enclosure': '1', 'bay': '6', 'port': 'Q4:1', 'speed': 'Auto'}],
},
    'US_Source_and_Dest_Mac': {
    'name': 'US_Source_and_Dest_Mac', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
    'networkUris': ['Eth_network_27'],
    'mode': 'Auto',
    'loadBalancingMode': 'SourceAndDestinationMac',
    'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q3:1', 'speed': 'Auto'},
                               {'enclosure': '1', 'bay': '3', 'port': 'Q4:1', 'speed': 'Auto'},
                               {'enclosure': '1', 'bay': '6', 'port': 'Q3:1', 'speed': 'Auto'},
                               {'enclosure': '1', 'bay': '6', 'port': 'Q4:1', 'speed': 'Auto'}],
}

}

ligs_edit_all = [{"name": "LIG-LACP",
                  "type": "logical-interconnect-groupV6",
                  "enclosureType": "SY12000",
                  "ethernetSettings": {'type': LIG_ethernet_version, 'interconnectType': 'Ethernet', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5,
                                       'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True},
                  "description": None,
                  "status": None,
                  "state": None,
                  "category": None,
                  "created": None,
                  "modified": None,
                  "eTag": None,
                  "uri": None,
                  "uplinkSets": [],
                  'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                              {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                              ],
                  "internalNetworkUris": [],
                  'interconnectBaySet': 3,
                  'redundancyType': 'Redundant',
                  'enclosureIndexes': [1],
                  'telemetryConfiguration': None,
                  'snmpConfiguration': None,
                  "qosConfiguration": {"activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough", "downlinkClassificationType": None, "uplinkClassificationType": None, "qosTrafficClassifiers": None, "description": None, "status": None, "name": None, "state": None, "category": "qos-aggregated-configuration", "created": None, "modified": None, "eTag": None, "uri": None}, "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None, "type": "qos-aggregated-configuration", "name": None, "state": None, "status": None, "eTag": None, "modified": None, "created": None, "category": "qos-aggregated-configuration", "uri": None}
                  }]

encl_group = [{"name": "EG-LACP",
               "interconnectBayMappings": [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                           {'interconnectBay': 2, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG-LACP2"},
                                           {'interconnectBay': 3, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                           {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                           {'interconnectBay': 5, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG-LACP2"},
                                           {'interconnectBay': 6, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                           {'interconnectBay': 2, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': "LIG:LIG-LACP2"},
                                           {'interconnectBay': 5, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': "LIG:LIG-LACP2"}
                                           ],
               "configurationScript": "",
               "powerMode": "RedundantPowerFeed",
               "ipAddressingMode": "DHCP",
               "ipRangeUris": [],
               "enclosureCount": 2}]

encl_group_bulk = [{"name": "EG-FM",
                    "interconnectBayMappings": [{"interconnectBay": 3,
                                                 "logicalInterconnectGroupUri": "LIG:LIG-FM-BULK"},
                                                {"interconnectBay": 6,
                                                 "logicalInterconnectGroupUri": "LIG:LIG-FM-BULK"}],
                    "configurationScript": "",
                    "powerMode": "RedundantPowerFeed",
                    "ipAddressingMode": "DHCP",
                    "ipRangeUris": [],
                    "enclosureCount": 1}]

logical_encl = [{"name": "LE",
                 "enclosureUris": ['ENC:SGH734VBEB', 'ENC:SGH734VBE6'],
                 "enclosureGroupUri": "EG:EG-LACP",
                 "firmwareBaselineUri": None,
                 "forceInstallFirmware": False}]

server_profiles = [{'type': 'ServerProfileV10', 'serverHardwareUri': 'SH:SGH734VBEB, bay 1',
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': '',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'sp_b1', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'boot': {'manageBoot': False},
                    "connectionSettings": {"reapplyState": "NotApplying",
                                           'connections': [{'id': 1, 'name': 'con1_b1', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_network_21', 'functionType': 'Ethernet'},
                                                           {'id': 2, 'name': 'con2_b1', 'portId': 'Mezz 2:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_network_21', 'functionType': 'Ethernet'},
                                                           ]},
                    },
                   {'type': 'ServerProfileV10', 'serverHardwareUri': 'SH:SGH734VBEB, bay 2',
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': '',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'sp_b2', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'boot': {'manageBoot': False},
                    "connectionSettings": {"reapplyState": "NotApplying",
                                           'connections': [{'id': 1, 'name': 'con1_b2', 'portId': 'Mezz 2:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_network_21', 'functionType': 'Ethernet'},
                                                           {'id': 2, 'name': 'con2_b2', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth_network_21', 'functionType': 'Ethernet'},
                                                           ]},
                    }
                   ]

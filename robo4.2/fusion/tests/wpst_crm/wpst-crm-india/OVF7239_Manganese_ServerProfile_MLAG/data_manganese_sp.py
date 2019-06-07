"""
    This module contains test specific data variables for Manganese
    Server Profile Demo test cases and python keywords/helpers.
"""

from RoboGalaxyLibrary.utilitylib import logging as logger
from dynamic_data import DynamicData
import re
import paramiko
import time
import csv
DD = DynamicData()

MAX_NETWORKS = 3966

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ethernet_networks_other = [{'name': 'untagged1', 'type': 'ethernet-networkV4', 'vlanId': None, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Untagged'},
                           {'name': 'untagged2', 'type': 'ethernet-networkV4', 'vlanId': None, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Untagged'},
                           {"name": "tunnel", "type": "ethernet-networkV4", "vlanId": None, "purpose": "General", "smartLink": True, "privateNetwork": False, "ethernetNetworkType": "Tunnel"}
                           ]

networksets = [{'name': 'netset1', 'nativeNetworkUri': None, 'type': 'network-setV4', 'networkUris': ['PVLANnetwork_121', 'PVLANnetwork_122', 'PVLANnetwork_123', 'PVLANnetwork_124']},
               {'name': 'pvlan_primary', 'nativeNetworkUri': None, 'type': 'network-setV4', 'networkUris': ['PVLANnetwork_101', 'PVLANnetwork_103', 'PVLANnetwork_105', 'PVLANnetwork_107']},
               {'name': 'pvlan_secondary', 'nativeNetworkUri': None, 'type': 'network-setV4', 'networkUris': ['PVLANnetwork_102', 'PVLANnetwork_104', 'PVLANnetwork_106', 'PVLANnetwork_108']}]

net_sets = [{'network_set': "Bulk1", 'network_count': 999, 'start_vlan': 2, 'namePrefix': 'Network'},
            {'network_set': "Bulk2", 'network_count': 1000, 'start_vlan': 1001, 'namePrefix': 'Network'},
            {'network_set': "Bulk3", 'network_count': 1000, 'start_vlan': 2001, 'namePrefix': 'Network'},
            {'network_set': "Bulk4", 'network_count': 966, 'start_vlan': 3001, 'namePrefix': 'Network'}]
bulk_networksets = DD.create_network_set_data(net_sets)

ethernet_networks_tagged = [{"vlanIdRange": "2-" + str(MAX_NETWORKS),
                             "namePrefix": "Network",
                             "privateNetwork": False,
                             "smartLink": True,
                             "purpose": "General",
                             "type": "bulk-ethernet-networkV2",
                             "bandwidth": {"maximumBandwidth": 20000, "typicalBandwidth": 2500},
                             }]

ENC1 = 'SGH822WFT4'
LE_NAME = "LE"
LIG_NAME_POTASH = "LIG-POTASH"
LIG_NAME_NITRO = "LIG-NITRO"
LIG_NAME_MELLANOX = "LIG-MELLANOX"
LI_NAME_POTASH = LE_NAME + '-' + LIG_NAME_POTASH
LI_NAME_NITRO = LE_NAME + '-' + LIG_NAME_NITRO
LI_NAME_MELLANOX = LE_NAME + '-' + LIG_NAME_MELLANOX

uplink_sets = {'US1': {'name': 'US1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'mode': 'Auto',
                       'networkUris': [],
                       'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '3', 'port': 'Q1', 'speed': 'Speed100G'},
                                                  {'enclosure': '-1', 'bay': '6', 'port': 'Q1', 'speed': 'Speed100G'}
                                                  ]
                       },
               'US2_UNTAGGED_REDUNDANT': {'name': 'US2_UNTAGGED', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Untagged', 'mode': 'Auto',
                                          'networkUris': ['untagged1'],
                                          'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '3', 'port': 'Q2', 'speed': 'Speed100G'},
                                                                     {'enclosure': '-1', 'bay': '6', 'port': 'Q2', 'speed': 'Speed100G'}]
                                          },
               'US2_UNTAGGED_ASIDE': {'name': 'US2_UNTAGGED', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Untagged', 'mode': 'Auto',
                                      'networkUris': ['untagged1'],
                                      'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '3', 'port': 'Q2', 'speed': 'Speed100G'}
                                                                 ]
                                      }

               }

uplink_sets_data = [{'name': 'US1_BULK_REDUNDANT', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                     'networkUrisvlanIdStart': 2, 'networkUrisvlanIdEnd': MAX_NETWORKS, "namePrefix": "Network",
                     'mode': 'Auto',
                     'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '3', 'port': 'Q1', 'speed': 'Speed100G'},
                                                {'enclosure': '-1', 'bay': '6', 'port': 'Q1', 'speed': 'Speed100G'},
                                                ],
                     },
                    {'name': 'US2_BULK_ASIDE', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                     'networkUrisvlanIdStart': 2, 'networkUrisvlanIdEnd': MAX_NETWORKS, "namePrefix": "Network",
                     'mode': 'Auto',
                     'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '3', 'port': 'Q1', 'speed': 'Speed100G'}],
                     },
                    {'name': 'US1_POTASH', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                     'networkUrisvlanIdStart': 2, 'networkUrisvlanIdEnd': MAX_NETWORKS, "namePrefix": "Network",
                     'mode': 'Auto',
                     'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q1', 'speed': 'Auto'},
                                                {'enclosure': '1', 'bay': '4', 'port': 'Q1', 'speed': 'Auto'}],
                     },
                    {'name': 'US1_NITRO_ASIDE', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                     'networkUrisvlanIdStart': 2, 'networkUrisvlanIdEnd': MAX_NETWORKS, "namePrefix": "Network",
                     'mode': 'Auto',
                     'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1', 'speed': 'Auto'}],
                     },
                    ]

uplink_sets_bulk_nw = DD.create_uplink_data(uplink_sets_data)

lig_potash = {"name": "LIG-POTASH",
              "type": "logical-interconnect-groupV6",
              "enclosureType": "SY12000",
              "ethernetSettings": {'type': 'EthernetInterconnectSettingsV6', 'interconnectType': 'Ethernet', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5,
                                   'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True},
              "description": None,
              "status": None,
              "state": None,
              "category": None,
              "created": None,
              "modified": None,
              "eTag": None,
              "uri": None,
              "uplinkSets": [
                  uplink_sets_bulk_nw['US1_POTASH'].copy(),
              ],
              'interconnectMapTemplate': [
                  {
                      "enclosureIndex": 1,
                      "bay": 1,
                      "enclosure": 1,
                      "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
                  },

                  {
                      "enclosureIndex": 1,
                      "bay": 4,
                      "enclosure": 1,
                      "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
                  }
              ],
              "internalNetworkUris": [],
              'interconnectBaySet': 1,
              'redundancyType': 'Redundant',
              'enclosureIndexes': [1],
              "qosConfiguration": {"activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough", "downlinkClassificationType": None, "uplinkClassificationType": None, "qosTrafficClassifiers": None, "description": None, "status": None, "name": None, "state": None, "category": "qos-aggregated-configuration", "created": None, "modified": None, "eTag": None, "uri": None}, "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None, "type": "qos-aggregated-configuration", "name": None, "state": None, "status": None, "eTag": None, "modified": None, "created": None, "category": "qos-aggregated-configuration", "uri": None}
              }

lig_nitro = {"name": "LIG-NITRO",
             "type": "logical-interconnect-groupV6",
             "enclosureType": "SY12000",
             "ethernetSettings": {'type': 'EthernetInterconnectSettingsV6', 'interconnectType': 'Ethernet', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5,
                                  'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True},
             "description": None,
             "status": None,
             "state": None,
             "category": None,
             "created": None,
             "modified": None,
             "eTag": None,
             "uri": None,
             "uplinkSets": [
                 uplink_sets_bulk_nw['US1_NITRO_ASIDE'].copy(),
             ],
             'interconnectMapTemplate': [
                 {
                     "enclosureIndex": 1,
                     "bay": 2,
                     "enclosure": 1,
                     "type": "Virtual Connect SE 100Gb F32 Module for Synergy"
                 }
             ],
             "internalNetworkUris": [],
             'interconnectBaySet': 2,
             'redundancyType': 'NonRedundantASide',
             'enclosureIndexes': [1],
             "qosConfiguration": {"activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough", "downlinkClassificationType": None, "uplinkClassificationType": None, "qosTrafficClassifiers": None, "description": None, "status": None, "name": None, "state": None, "category": "qos-aggregated-configuration", "created": None, "modified": None, "eTag": None, "uri": None}, "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None, "type": "qos-aggregated-configuration", "name": None, "state": None, "status": None, "eTag": None, "modified": None, "created": None, "category": "qos-aggregated-configuration", "uri": None}
             }

lig_mellanox_redundant = {"name": LIG_NAME_MELLANOX,
                          "type": "logical-interconnect-groupV6",
                          "enclosureType": "SY12000",
                          "ethernetSettings": {'type': 'EthernetInterconnectSettingsV6', 'interconnectType': 'Ethernet', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5,
                                               'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True},
                          "description": None,
                          "status": None,
                          "state": None,
                          "category": None,
                          "created": None,
                          "modified": None,
                          "eTag": None,
                          "uri": None,
                          "uplinkSets": [uplink_sets_bulk_nw['US1_BULK_REDUNDANT'].copy(),
                                         uplink_sets['US2_UNTAGGED_REDUNDANT'].copy(),
                                         ],
                          'interconnectMapTemplate': [
                              {
                                  "enclosureIndex": -1,
                                  "bay": 6,
                                  "enclosure": -1,
                                  "type": "Mellanox SH2200 TAA Switch Module for Synergy"
                              },
                              {
                                  "enclosureIndex": -1,
                                  "bay": 3,
                                  "enclosure": -1,
                                  "type": "Mellanox SH2200 TAA Switch Module for Synergy"
                              }
                          ],
                          "internalNetworkUris": [],
                          'interconnectBaySet': 3,
                          'redundancyType': 'Redundant',
                          'enclosureIndexes': [-1],
                          "qosConfiguration": {"activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough", "downlinkClassificationType": None, "uplinkClassificationType": None, "qosTrafficClassifiers": None, "description": None, "status": None, "name": None, "state": None, "category": "qos-aggregated-configuration", "created": None, "modified": None, "eTag": None, "uri": None}, "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None, "type": "qos-aggregated-configuration", "name": None, "state": None, "status": None, "eTag": None, "modified": None, "created": None, "category": "qos-aggregated-configuration", "uri": None}
                          }

lig_mellanox_redundant_untagged = {"name": LIG_NAME_MELLANOX,
                                   "type": "logical-interconnect-groupV6",
                                   "enclosureType": "SY12000",
                                   "ethernetSettings": {'type': 'EthernetInterconnectSettingsV5', 'interconnectType': 'Ethernet', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5,
                                                        'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True},
                                   "description": None,
                                   "status": None,
                                   "state": None,
                                   "category": None,
                                   "created": None,
                                   "modified": None,
                                   "eTag": None,
                                   "uri": None,
                                   "uplinkSets": [uplink_sets_bulk_nw['US1_BULK_REDUNDANT'].copy(),
                                                  uplink_sets['US2_UNTAGGED_REDUNDANT'].copy(),
                                                  ],
                                   'interconnectMapTemplate': [
                                       {
                                           "enclosureIndex": 1,
                                           "bay": 6,
                                           "enclosure": 1,
                                           "type": "Mellanox SH2200 TAA Switch Module for Synergy"
                                       },
                                       {
                                           "enclosureIndex": 1,
                                           "bay": 3,
                                           "enclosure": 1,
                                           "type": "Mellanox SH2200 TAA Switch Module for Synergy"
                                       }
                                   ],
                                   "internalNetworkUris": [],
                                   'interconnectBaySet': 3,
                                   'redundancyType': 'Redundant',
                                   'enclosureIndexes': [1],
                                   "qosConfiguration": {"activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough", "downlinkClassificationType": None, "uplinkClassificationType": None, "qosTrafficClassifiers": None, "description": None, "status": None, "name": None, "state": None, "category": "qos-aggregated-configuration", "created": None, "modified": None, "eTag": None, "uri": None}, "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None, "type": "qos-aggregated-configuration", "name": None, "state": None, "status": None, "eTag": None, "modified": None, "created": None, "category": "qos-aggregated-configuration", "uri": None}
                                   }

lig_mellanox_sideA = {"name": LIG_NAME_MELLANOX,
                      "type": "logical-interconnect-groupV6",
                      "enclosureType": "SY12000",
                      "ethernetSettings": {'type': 'EthernetInterconnectSettingsV6',
                                           'interconnectType': 'Ethernet',
                                           'enableIgmpSnooping': False,
                                           'igmpIdleTimeoutInterval': 260,
                                           'enableFastMacCacheFailover': True,
                                           'macRefreshInterval': 5,
                                           'enableNetworkLoopProtection': True,
                                           'enablePauseFloodProtection': True
                                           },
                      "description": None,
                      "status": None,
                      "state": None,
                      "category": None,
                      "created": None,
                      "modified": None,
                      "eTag": None,
                      "uri": None,
                      "uplinkSets": [uplink_sets_bulk_nw['US2_BULK_ASIDE'].copy(),
                                       uplink_sets['US2_UNTAGGED_ASIDE'].copy(),
                                     ],
                      'interconnectMapTemplate': [{
                          "enclosureIndex": -1,
                          "bay": 3,
                          "enclosure": -1,
                          "type": "Mellanox SH2200 TAA Switch Module for Synergy"
                      }],
                      "internalNetworkUris": [],
                      'interconnectBaySet': 3,
                      'redundancyType': 'NonRedundantASide',
                      'enclosureIndexes': [-1],
                      "qosConfiguration": {"activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough", "downlinkClassificationType": None, "uplinkClassificationType": None, "qosTrafficClassifiers": None, "description": None, "status": None, "name": None, "state": None, "category": "qos-aggregated-configuration", "created": None, "modified": None, "eTag": None, "uri": None}, "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None, "type": "qos-aggregated-configuration", "name": None, "state": None, "status": None, "eTag": None, "modified": None, "created": None, "category": "qos-aggregated-configuration", "uri": None}
                      }

lig_mellanox_sideA_untagged = {"name": LIG_NAME_MELLANOX,
                               "type": "logical-interconnect-groupV6",
                               "enclosureType": "SY12000",
                               "ethernetSettings": {'type': 'EthernetInterconnectSettingsV6',
                                                    'interconnectType': 'Ethernet',
                                                    'enableIgmpSnooping': False,
                                                    'igmpIdleTimeoutInterval': 260,
                                                    'enableFastMacCacheFailover': True,
                                                    'macRefreshInterval': 5,
                                                    'enableNetworkLoopProtection': True,
                                                    'enablePauseFloodProtection': True
                                                    },
                               "description": None,
                               "status": None,
                               "state": None,
                               "category": None,
                               "created": None,
                               "modified": None,
                               "eTag": None,
                               "uri": None,
                               "uplinkSets": [uplink_sets_bulk_nw['US2_BULK_ASIDE'].copy(),
                                                uplink_sets['US2_UNTAGGED_ASIDE'].copy(),
                                              ],
                               'interconnectMapTemplate': [{
                                   "enclosureIndex": -1,
                                   "bay": 3,
                                   "enclosure": -1,
                                   "type": "Mellanox SH2200 TAA Switch Module for Synergy"
                               }],
                               "internalNetworkUris": [],
                               'interconnectBaySet': 3,
                               'redundancyType': 'NonRedundantASide',
                               'enclosureIndexes': [-1],
                               "qosConfiguration": {"activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough", "downlinkClassificationType": None, "uplinkClassificationType": None, "qosTrafficClassifiers": None, "description": None, "status": None, "name": None, "state": None, "category": "qos-aggregated-configuration", "created": None, "modified": None, "eTag": None, "uri": None}, "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None, "type": "qos-aggregated-configuration", "name": None, "state": None, "status": None, "eTag": None, "modified": None, "created": None, "category": "qos-aggregated-configuration", "uri": None}
                               }

encl_group_sideA = [{"name": "EG",
                     "interconnectBayMappings": [
                         {'enclosureIndex': 1, "interconnectBay": 3,
                          "logicalInterconnectGroupUri": "LIG:LIG-MELLANOX"},

                     ],
                     "configurationScript": "",
                     "powerMode": "RedundantPowerFeed",
                     "ipAddressingMode": "DHCP",
                     "ipRangeUris": [],
                     "enclosureCount": 1}]

encl_group = [{"name": "EG",
               "interconnectBayMappings": [
                   {'enclosureIndex': 1, "interconnectBay": 3,
                    "logicalInterconnectGroupUri": "LIG:LIG-MELLANOX"},
                   {'enclosureIndex': 1, "interconnectBay": 6,
                    "logicalInterconnectGroupUri": "LIG:LIG-MELLANOX"}
               ],
               "configurationScript": "",
               "powerMode": "RedundantPowerFeed",
               "ipAddressingMode": "DHCP",
               "ipRangeUris": [],
               "enclosureCount": 1}]

encl_group_full = [{"name": "EG2",
                    "interconnectBayMappings": [{'enclosureIndex': 1, "interconnectBay": 2,
                                                 "logicalInterconnectGroupUri": "LIG:LIG-NITRO"},
                                                {'enclosureIndex': 1, "interconnectBay": 3,
                                                 "logicalInterconnectGroupUri": "LIG:LIG-MELLANOX"},
                                                {'enclosureIndex': 1, "interconnectBay": 6,
                                                 "logicalInterconnectGroupUri": "LIG:LIG-MELLANOX"},
                                                {'enclosureIndex': 1, "interconnectBay": 1,
                                                 "logicalInterconnectGroupUri": "LIG:LIG-POTASH"},
                                                {'enclosureIndex': 1, "interconnectBay": 4,
                                                 "logicalInterconnectGroupUri": "LIG:LIG-POTASH"},
                                                ],
                    "configurationScript": "",
                    "powerMode": "RedundantPowerFeed",
                    "ipAddressingMode": "DHCP",
                    "ipRangeUris": [],
                    "enclosureCount": 1}]

logical_encl = [{"name": LE_NAME,
                 "enclosureUris": ["ENC:SGH822WFT4"],
                 "enclosureGroupUri": "EG:EG",
                 "firmwareBaselineUri": None,
                 "forceInstallFirmware": False}]

logical_encl_full = [{"name": LE_NAME,
                      "enclosureUris": ["ENC:SGH822WFT4"],
                      "enclosureGroupUri": "EG:EG2",
                      "firmwareBaselineUri": None,
                      "forceInstallFirmware": False}]

server_profile_data = [
    {'type': 'ServerProfileV11', 'serverHardwareUri': 'SH:SGH822WFT4, bay 10',
     'serverHardwareTypeUri': '', 'enclosureGroupUri': '',
     'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
     'name': 'SP_Linux', 'description': '', 'affinity': 'Bay',
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'boot': {'manageBoot': False},
     "connectionSettings": {"reapplyState": "NotApplying",
                            'connections': [{'id': 1, 'name': 'Mezz 3:1', 'portId': 'Mezz 3:1', 'requestedMbps': '25000', 'networkUri': 'NS:Network_Set_Bulk2', 'lagName': 'LAG1', 'functionType': 'Ethernet'},
                                            {'id': 2, 'name': 'Mezz 3:2', 'portId': 'Mezz 3:2', 'requestedMbps': '25000', 'networkUri': 'NS:Network_Set_Bulk2', 'lagName': 'LAG1', 'functionType': 'Ethernet'},
                                            {'id': 3, 'name': 'Mezz 1:1-a', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:Network_Set_Bulk2', 'functionType': 'Ethernet'},
                                            {'id': 4, 'name': 'Mezz 1:2-a', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:Network_Set_Bulk2', 'functionType': 'Ethernet'},
                                            ]
                            },
     },
    {'type': 'ServerProfileV11', 'serverHardwareUri': 'SH:SGH822WFT4, bay 11',
     'serverHardwareTypeUri': '', 'enclosureGroupUri': '',
     'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
     'name': 'SP_Windows', 'description': '', 'affinity': 'Bay',
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'boot': {'manageBoot': False},
     "connectionSettings": {"reapplyState": "NotApplying",
                                            'connections': [{'id': 1, 'name': 'Mezz 3:1', 'portId': 'Mezz 3:1', 'requestedMbps': '25000', 'networkUri': 'NS:Network_Set_Bulk2', 'lagName': 'LAG1', 'functionType': 'Ethernet'},
                                                            {'id': 2, 'name': 'Mezz 3:2', 'portId': 'Mezz 3:2', 'requestedMbps': '25000', 'networkUri': 'NS:Network_Set_Bulk2', 'lagName': 'LAG1', 'functionType': 'Ethernet'},
                                                            {'id': 3, 'name': 'Mezz 1:1-a', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:Network_Set_Bulk2', 'functionType': 'Ethernet'},
                                                            {'id': 4, 'name': 'Mezz 1:2-a', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:Network_Set_Bulk2', 'functionType': 'Ethernet'},
                                                            {'id': 5, 'name': 'Mezz 2:1-a', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:Network_Set_Bulk2', 'functionType': 'Ethernet'},
                                                            ]
                            },
     }
]

server_profile_schannel = [{'type': 'ServerProfileV11', 'serverHardwareUri': 'SH:SGH822WFT4, bay 5',
                            'serverHardwareTypeUri': '', 'enclosureGroupUri': '',
                            'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                            'name': 'SP2', 'description': '', 'affinity': 'Bay',
                            'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                            'boot': {'manageBoot': False},
                            "connectionSettings": {"reapplyState": "NotApplying",
                                                   'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '25000', 'networkUri': 'ETH:Network_2', 'functionType': 'Ethernet'},
                                                                   {'id': 2, 'name': 'Mezz 3:2-a', 'portId': 'Mezz 3:2-a', 'requestedMbps': '25000', 'networkUri': 'ETH:Network_2', 'functionType': 'Ethernet'}
                                                                   ]
                                                   },
                            }]

server_profile_unsupported_connection_speed = [{'type': 'ServerProfileV11', 'serverHardwareUri': 'SH:SGH822WFT4, bay 5',
                                                'serverHardwareTypeUri': '', 'enclosureGroupUri': '',
                                                'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                                                'name': 'SP2', 'description': '', 'affinity': 'Bay',
                                                'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                                'boot': {'manageBoot': False},
                                                "connectionSettings": {"reapplyState": "NotApplying",
                                                                       'connections': [{'id': 1, 'name': 'Mezz 3:1', 'portId': 'Mezz 3:1', 'requestedMbps': '7500', 'networkUri': 'ETH:Network_2', 'functionType': 'Ethernet'},
                                                                                       {'id': 2, 'name': 'Mezz 3:2', 'portId': 'Mezz 3:2', 'requestedMbps': '3500', 'networkUri': 'ETH:Network_2', 'functionType': 'Ethernet'}
                                                                                       ]
                                                                       },
                                                }]


def get_vlan_details_from_manganese(hostname, username, password):
    """
    Gets vlan details from manganese ICM
    """
    port = 22
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, port=port, username=username, password=password, look_for_keys=False, allow_agent=False)
    channel = ssh.invoke_shell(term='vt100', width=200, height=1000000, width_pixels=0, height_pixels=0)

    # Wait for Recv Ready after logging in.
    results = ''
    while channel.recv_ready() is False:
        time.sleep(10)
        logger._log('\nChannel receive ready status: \n %s' % (channel.recv_ready()), level='DEBUG')
    results += channel.recv(50000)
    logger._log("\nResults After Login: \n", level='DEBUG')

    # Send Show VLAN Command
    results = ''
    logger._log("\nSending 'show vlan' command.\n", level='DEBUG')
    channel.send('show vlan\n')
    while channel.recv_ready() is False:
        time.sleep(10)
        logger._log('\nChannel receive ready status: \n %s' % (channel.recv_ready()), level='DEBUG')
    results += channel.recv(500000)
    logger._log("Results after 'show vlan' command: \n %s" % (results), level='DEBUG')
    # Close SSH shell
    ssh.close()
    # Strip the header and footer from the output table and get only table rows
    results = "\n".join(results.split("\n")[:-2])
    table = ''.join(re.split(r'\r\nVLAN.*Ports\r\n----------------------------------------------------------------------', results)[1:])
    table = table.strip()
    table = table.split('\r\n')
    x = ""
    for line in table:
        line = ",".join(re.split(r'\s{2,}', line))
        x = x + "\n" + line
    # Convert row/line into Dictionary
    fnames = ["VLAN", "Ports"]
    results = csv.DictReader(x.splitlines(), fieldnames=fnames)
    dict_list = []
    for line in results:
        dict_list.append(line)
    return dict_list

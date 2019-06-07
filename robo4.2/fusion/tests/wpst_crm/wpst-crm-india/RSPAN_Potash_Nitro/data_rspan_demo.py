from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
import csv
import pprint
import re
import paramiko
import time

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}


ethernet_networks = [{"name": "net10", "type": "ethernet-networkV4", "vlanId": 10, "purpose": "General", "smartLink": True, "privateNetwork": False, "ethernetNetworkType": "Tagged"},
                     {"name": "net20", "type": "ethernet-networkV4", "vlanId": 20, "purpose": "General", "smartLink": True, "privateNetwork": False, "ethernetNetworkType": "Tagged"},
                     {"name": "net50", "type": "ethernet-networkV4", "vlanId": 50, "purpose": "General", "smartLink": True, "privateNetwork": False, "ethernetNetworkType": "Tagged"},
                     {"name": "net80", "type": "ethernet-networkV4", "vlanId": 80, "purpose": "General", "smartLink": True, "privateNetwork": False, "ethernetNetworkType": "Tagged"},
                     {"name": "net100", "type": "ethernet-networkV4", "vlanId": 100, "purpose": "General", "smartLink": True, "privateNetwork": False, "ethernetNetworkType": "Tagged"},
                     {"name": "net1601", "type": "ethernet-networkV4", "vlanId": 1601, "purpose": "General", "smartLink": True, "privateNetwork": False, "ethernetNetworkType": "Tagged"},
                     ]

networksets = [{'name': 'NS1', 'nativeNetworkUri': None, 'type': 'network-setV5', 'networkUris': ['net20']},
               {'name': 'NS2', 'nativeNetworkUri': None, 'type': 'network-setV5', 'networkUris': ['net50']},
               ]

ENC2 = 'SGH751SLBK'
ENC1 = 'SGH751SLBL'
LE_NAME = "LE"
LIG_NAME_POTASH = "LIG-POTASH"
LIG_NAME_NITRO = "LIG-NITRO"
LI_NAME_POTASH = LE_NAME + '-' + LIG_NAME_POTASH
LI_NAME_NITRO = LE_NAME + '-' + LIG_NAME_NITRO
US_NAME_POTASH = "US1-POTASH"
US_NAME_NITRO = "US1-NITRO"


uplink_sets = {'US1': {'name': "US1", 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['net20'], 'mode': 'Auto',
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q3', 'speed': 'Auto'}]
                       },
               'US2': {'name': "US2", 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['net100'], 'mode': 'Auto',
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q2:1', 'speed': 'Auto'}]
                       },
               'US3': {'name': "US3", 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['net10'], 'mode': 'Auto',
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1:1', 'speed': 'Auto'}]
                       },
               'US4': {'name': "US4", 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['net50'], 'mode': 'Auto',
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q5:1', 'speed': 'Auto'}]
                       },
               'US5': {'name': "US5", 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['net80'], 'mode': 'Auto',
                       'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '5', 'port': 'Q2:1', 'speed': 'Auto'}]
                       },
               'US1_NITRO': {'name': "US1", 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['net100'], 'mode': 'Auto',
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'}]
                             },
               'US2_NITRO': {'name': "US2", 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['net20'], 'mode': 'Auto',
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'}]
                             },
               'US3_NITRO': {'name': "US3", 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['net10'], 'mode': 'Auto',
                             'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q3:1', 'speed': 'Auto'}]
                             }
               }

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
              "uplinkSets": [uplink_sets['US1'].copy(),
                               uplink_sets['US2'].copy(),
                               uplink_sets['US3'].copy(),
                               uplink_sets['US4'].copy(),
                               uplink_sets['US5'].copy(),
                             ],
              'interconnectMapTemplate': [{
                  "enclosureIndex": 2,
                  "enclosure": 2,
                  "bay": 2,
                  "type": "Synergy 20Gb Interconnect Link Module"
              },
                  {
                  "enclosureIndex": 2,
                  "bay": 5,
                  "enclosure": 2,
                  "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
              },
                  {
                  "enclosureIndex": 1,
                  "bay": 5,
                  "enclosure": 1,
                  "type": "Synergy 20Gb Interconnect Link Module"
              },
                  {
                  "enclosureIndex": 1,
                  "bay": 2,
                  "enclosure": 1,
                  "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
              }
              ],
              "internalNetworkUris": [],
              'interconnectBaySet': 2,
              'redundancyType': 'HighlyAvailable',
              'enclosureIndexes': [1, 2],
              "qosConfiguration": {"activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough", "downlinkClassificationType": None, "uplinkClassificationType": None, "qosTrafficClassifiers": None, "description": None, "status": None, "name": None, "state": None, "category": "qos-aggregated-configuration", "created": None, "modified": None, "eTag": None, "uri": None}, "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None, "type": "qos-aggregated-configuration", "name": None, "state": None, "status": None, "eTag": None, "modified": None, "created": None, "category": "qos-aggregated-configuration", "uri": None}
              }

lig_nitro = {"name": "LIG-NITRO",
             "type": "logical-interconnect-groupV6",
             "enclosureType": "SY12000",
             "ethernetSettings": {'type': 'EthernetInterconnectSettingsV', 'interconnectType': 'Ethernet', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5,
                                  'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True},
             "description": None,
             "status": None,
             "state": None,
             "category": None,
             "created": None,
             "modified": None,
             "eTag": None,
             "uri": None,
             "uplinkSets": [uplink_sets['US1_NITRO'].copy(),
                            uplink_sets['US2_NITRO'].copy(),
                            uplink_sets['US3_NITRO'].copy(),
                            ],
             'interconnectMapTemplate': [{
                 "enclosureIndex": 2,
                 "enclosure": 2,
                 "bay": 3,
                 "type": "Synergy 50Gb Interconnect Link Module"
             },
                 {
                 "enclosureIndex": 2,
                 "bay": 6,
                 "enclosure": 2,
                 "type": "Virtual Connect SE 100Gb F32 Module for Synergy"
             },
                 {
                 "enclosureIndex": 1,
                 "bay": 6,
                 "enclosure": 1,
                 "type": "Synergy 50Gb Interconnect Link Module"
             },
                 {
                 "enclosureIndex": 1,
                 "bay": 3,
                 "enclosure": 1,
                 "type": "Virtual Connect SE 100Gb F32 Module for Synergy"
             }
             ],
             "internalNetworkUris": [],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'enclosureIndexes': [1, 2],
             "qosConfiguration": {"activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough", "downlinkClassificationType": None, "uplinkClassificationType": None, "qosTrafficClassifiers": None, "description": None, "status": None, "name": None, "state": None, "category": "qos-aggregated-configuration", "created": None, "modified": None, "eTag": None, "uri": None}, "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None, "type": "qos-aggregated-configuration", "name": None, "state": None, "status": None, "eTag": None, "modified": None, "created": None, "category": "qos-aggregated-configuration", "uri": None}
             }


encl_group_potash = [{"name": "EG",
                      "interconnectBayMappings": [
                          {'enclosureIndex': 1, "interconnectBay": 2,
                           "logicalInterconnectGroupUri": "LIG:LIG-POTASH"},
                          {'enclosureIndex': 1, "interconnectBay": 5,
                           "logicalInterconnectGroupUri": "LIG:LIG-POTASH"},
                          {'enclosureIndex': 2, "interconnectBay": 2,
                           "logicalInterconnectGroupUri": "LIG:LIG-POTASH"},
                          {'enclosureIndex': 2, "interconnectBay": 5,
                           "logicalInterconnectGroupUri": "LIG:LIG-POTASH"},
                      ],
                      "configurationScript": "",
                      "powerMode": "RedundantPowerFeed",
                      "ipAddressingMode": "DHCP",
                      "ipRangeUris": [],
                      "enclosureCount": 2}]

encl_group_nitro = [{"name": "EG",
                     "interconnectBayMappings": [
                         {'enclosureIndex': 1, "interconnectBay": 3,
                          "logicalInterconnectGroupUri": "LIG:LIG-NITRO"},
                         {'enclosureIndex': 1, "interconnectBay": 6,
                          "logicalInterconnectGroupUri": "LIG:LIG-NITRO"},
                         {'enclosureIndex': 2, "interconnectBay": 3,
                          "logicalInterconnectGroupUri": "LIG:LIG-NITRO"},
                         {'enclosureIndex': 2, "interconnectBay": 6,
                          "logicalInterconnectGroupUri": "LIG:LIG-NITRO"}
                     ],
                     "configurationScript": "",
                     "powerMode": "RedundantPowerFeed",
                     "ipAddressingMode": "DHCP",
                     "ipRangeUris": [],
                     "enclosureCount": 2}]

logical_encl = [{"name": LE_NAME,
                 "enclosureUris": ["ENC:SGH751SLBL", "ENC:SGH751SLBK"],
                 "enclosureGroupUri": "EG:EG",
                 "firmwareBaselineUri": None,
                 "forceInstallFirmware": False}]


server_profiles = [{'type': 'ServerProfileV11', 'serverHardwareUri': 'SH:SGH751SLBK, bay 9',
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': '',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'SP_Bay9', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'boot': {'manageBoot': False},
                    "connectionSettings": {"reapplyState": "NotApplying",
                                           'connections': [{'id': 1, 'name': 'Connection1', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NS1', 'functionType': 'Ethernet'},
                                                           ]
                                           },
                    },
                   {'type': 'ServerProfileV11', 'serverHardwareUri': 'SH:SGH751SLBK, bay 11',
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': '',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'SP_Bay11', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'boot': {'manageBoot': False},
                    "connectionSettings": {"reapplyState": "NotApplying",
                                           'connections': [{'id': 1, 'name': 'Connection1', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NS1', 'functionType': 'Ethernet'},
                                                           ]
                                           },
                    },
                   {'type': 'ServerProfileV11', 'serverHardwareUri': 'SH:SGH751SLBL, bay 12',
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': '',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'SP_Bay12', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'boot': {'manageBoot': False},
                    "connectionSettings": {"reapplyState": "NotApplying",
                                           'connections': [{'id': 1, 'name': 'Connection1', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NS1', 'functionType': 'Ethernet'},
                                                           {'id': 2, 'name': 'Connection2', 'portId': 'Mezz 2:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:NS2', 'functionType': 'Ethernet'},
                                                           ]},
                    }
                   ]

server_profiles_nitro = [
    {'type': 'ServerProfileV11', 'serverHardwareUri': 'SH:SGH751SLBK, bay 9',
     'serverHardwareTypeUri': '', 'enclosureGroupUri': '',
     'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
     'name': 'SP_Bay9', 'description': '', 'affinity': 'Bay',
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'boot': {'manageBoot': False},
     "connectionSettings": {"reapplyState": "NotApplying",
                            'connections': [{'id': 1, 'name': 'Connection1', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NS1', 'functionType': 'Ethernet'},
                                            ]
                            },
     },
    {'type': 'ServerProfileV11', 'serverHardwareUri': 'SH:SGH751SLBK, bay 11',
     'serverHardwareTypeUri': '', 'enclosureGroupUri': '',
     'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                         'name': 'SP_Bay11', 'description': '', 'affinity': 'Bay',
                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                         'boot': {'manageBoot': False},
                         "connectionSettings": {"reapplyState": "NotApplying",
                                                'connections': [{'id': 1, 'name': 'Connection1', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NS1', 'functionType': 'Ethernet'},
                                                                ]
                                                },
     },
    {'type': 'ServerProfileV11', 'serverHardwareUri': 'SH:SGH751SLBL, bay 12',
     'serverHardwareTypeUri': '', 'enclosureGroupUri': '',
     'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                         'name': 'SP_Bay12', 'description': '', 'affinity': 'Bay',
                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                         'boot': {'manageBoot': False},
                         "connectionSettings": {"reapplyState": "NotApplying",
                                                'connections': [{'id': 1, 'name': 'Connection1', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:NS1', 'functionType': 'Ethernet'},
                                                                ]},
     }
]

server_profile_error = [{'type': 'ServerProfileV11', 'serverHardwareUri': 'SH:SGH751SLBL, bay 8',
                         'serverHardwareTypeUri': '', 'enclosureGroupUri': '',
                         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                         'name': 'SP_Bay8', 'description': '', 'affinity': 'Bay',
                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                         'boot': {'manageBoot': False},
                         "connectionSettings": {"reapplyState": "NotApplying",
                                                'connections': [{'id': 1, 'name': 'Connection1', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net100', 'functionType': 'Ethernet'},
                                                                ]
                                                },
                         }]

server_profile_error_nitro = [{'type': 'ServerProfileV11', 'serverHardwareUri': 'SH:SGH751SLBL, bay 8',
                               'serverHardwareTypeUri': '', 'enclosureGroupUri': '',
                               'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                               'name': 'SP_Bay8', 'description': '', 'affinity': 'Bay',
                               'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                               'boot': {'manageBoot': False},
                               "connectionSettings": {"reapplyState": "NotApplying",
                                                      'connections': [{'id': 1, 'name': 'Connection1', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net100', 'functionType': 'Ethernet'},
                                                                      ]
                                                      },
                               }]

rspan_session = {
    "type": "port-monitorV1",
    "enablePortMonitor": True,
    "portMonitorType": "Remote",
    "remotePortMonitor": [
        {"networkUri": 'net80',
         "monitoredPorts": [
             {"portMonitorConfigInfo": "MonitoredBoth",
              "portUri": "d12"
              },
         ],
         "mirrorToPort": {
             "portMonitorConfigInfo": "AnalyzerPort",
             "portUri": "Q2:1"  # Enc2 Bay5
         }}]
}

rspan_session_nitro = {
    "type": "port-monitorV1",
    "enablePortMonitor": True,
    "portMonitorType": "Remote",
    "remotePortMonitor": [
        {"networkUri": 'net100',
         "monitoredPorts": [
             {"portMonitorConfigInfo": "MonitoredBoth",
              "portUri": "d12"
              },
         ],
         "mirrorToPort": {
             "portMonitorConfigInfo": "AnalyzerPort",
             "portUri": "Q1"  # Enc2 Bay5
         }}]
}

rspan_session2 = {
    "type": "port-monitorV1",
    "enablePortMonitor": True,
    "portMonitorType": "Remote",
    "remotePortMonitor": [
        {"networkUri": 'net100',
         "monitoredPorts": [
             {"portMonitorConfigInfo": "MonitoredBoth",
              "portUri": "d12"
              },
         ],
         "mirrorToPort": {
             "portMonitorConfigInfo": "AnalyzerPort",
             "portUri": "Q2:1"  # Enc1 Bay2
         }
         },
    ]
}

rspan_session2_nitro = {
    "type": "port-monitorV1",
    "enablePortMonitor": True,
    "portMonitorType": "Remote",
    "remotePortMonitor": [
        {"networkUri": 'net10',
         "monitoredPorts": [
             {"portMonitorConfigInfo": "MonitoredBoth",
              "portUri": "d12"
              },
         ],
         "mirrorToPort": {
             "portMonitorConfigInfo": "AnalyzerPort",
             "portUri": "Q3:1"  # Enc1 Bay2
         }
         },
    ]
}

rspan_session3 = {
    "type": "port-monitorV1",
    "enablePortMonitor": True,
    "portMonitorType": "Remote",
    "remotePortMonitor": [
        {"networkUri": 'net10',
         "monitoredPorts": [
             {"portMonitorConfigInfo": "MonitoredBoth",
              "portUri": "d12"
              },
         ],
         "mirrorToPort": {
             "portMonitorConfigInfo": "AnalyzerPort",
             "portUri": "Q1:1"  # Enc1 Bay2
         }
         },

    ]
}

rspan_session4 = {
    "type": "port-monitorV1",
    "enablePortMonitor": True,
    "portMonitorType": "Remote",
    "remotePortMonitor": [
        {"networkUri": 'net10',
         "monitoredPorts": [
             {"portMonitorConfigInfo": "MonitoredBoth",
              "portUri": "d12"
              },
         ],
         "mirrorToPort": {
             "portMonitorConfigInfo": "AnalyzerPort",
             "portUri": "Q5:1"   # Enc1 Bay2
         }
         },

    ]
}

rspan_session5_error = {
    "type": "port-monitorV1",
    "enablePortMonitor": True,
    "portMonitorType": "Remote",
    "remotePortMonitor": [
        {
            "networkUri": 'net10',
            "monitoredPorts": [
                {"portMonitorConfigInfo": "MonitoredBoth",
                 "portUri": "l1"
                 },
            ],
            "mirrorToPort": {
                "portMonitorConfigInfo": "AnalyzerPort",
                "portUri": "Q5:1"   # Enc1 Bay2
            }
        },

    ]
}

rspan_session5_error_nitro = {
    "type": "port-monitorV1",
    "enablePortMonitor": True,
    "portMonitorType": "Remote",
    "remotePortMonitor": [
        {
            "networkUri": 'net10',
            "monitoredPorts": [
                {"portMonitorConfigInfo": "MonitoredBoth",
                 "portUri": "l1"
                 },
            ],
            "mirrorToPort": {
                "portMonitorConfigInfo": "AnalyzerPort",
                "portUri": "Q3:1"   # Enc1 Bay2
            }
        },

    ]
}

rspan_session_dus = {
    "type": "port-monitorV1",
    "enablePortMonitor": True,
    "portMonitorType": "Remote",
    "remotePortMonitor": [{"networkUri": 'net80',
                           "monitoredPorts": [
                               {"portMonitorConfigInfo": "MonitoredBoth",
                                "portUri": "d12"
                                },
                           ],
                           "mirrorToPort": {
                               "portMonitorConfigInfo": "AnalyzerPort",
                               "portUri": "Q2:1"   # Enc2 Bay5
                           }}]
}

rspan_session_dus_nitro = {"type": "port-monitorV1",
                           "enablePortMonitor": True,
                           "portMonitorType": "Remote",
                           "remotePortMonitor": [{"networkUri": 'net10',
                                                  "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredToServer",
                                                                      "portUri": "SGH751SLBL, interconnect 3, d12"
                                                                      }],
                                                  "mirrorToPort": {"portMonitorConfigInfo": "AnalyzerPort",
                                                                   "portUri": "SGH751SLBK, interconnect 6, Q3:1"
                                                                   }
                                                  },
                                                 ]
                           }


rspan_session_same_nw_error = {
    "type": "port-monitorV1",
    "enablePortMonitor": True,
    "portMonitorType": "Remote",
    "remotePortMonitor": [{"networkUri": 'net80',
                           "monitoredPorts": [
                               {"portMonitorConfigInfo": "MonitoredBoth",
                                "portUri": "d12"
                                },
                           ],
                           "mirrorToPort": {
                               "portMonitorConfigInfo": "AnalyzerPort",
                               "portUri": "Q2:1"   # Enc2 Bay5
                           }},
                          {"networkUri": 'net80',
                           "monitoredPorts": [
                               {"portMonitorConfigInfo": "MonitoredBoth",
                                "portUri": "d13"
                                },
                           ],
                           "mirrorToPort": {
                               "portMonitorConfigInfo": "AnalyzerPort",
                               "portUri": "Q2:1"  # Enc2 Bay5
                           }}
                          ]
}

rspan_session_multi_ports = {
    "type": "port-monitorV1",
    "enablePortMonitor": True,
    "portMonitorType": "Remote",
    "remotePortMonitor": [
        {
            "networkUri": 'net100',
            "monitoredPorts": [
                {
                    "portMonitorConfigInfo": "MonitoredBoth",
                    "portUri": "d12"
                },
                {
                    "portMonitorConfigInfo": "MonitoredBoth",
                    "portUri": "d23"
                },
                {
                    "portMonitorConfigInfo": "MonitoredBoth",
                    "portUri": "d21"
                },
                {
                    "portMonitorConfigInfo": "MonitoredBoth",
                    "portUri": "d4"
                }
            ],
            "mirrorToPort": {
                "portMonitorConfigInfo": "AnalyzerPort",
                "portUri": "Q2:1"  # Enc1 Bay2
            }
        }
    ]
}

rspan_session_multi_ports_nitro = {
    "type": "port-monitorV1",
    "enablePortMonitor": True,
    "portMonitorType": "Remote",
    "remotePortMonitor": [
        {
            "networkUri": 'net100',
            "monitoredPorts": [
                                  {
                                      "portMonitorConfigInfo": "MonitoredBoth",
                                      "portUri": "d12"
                                  },
                {
                                      "portMonitorConfigInfo": "MonitoredBoth",
                                      "portUri": "d23"
                                  },
                {
                                      "portMonitorConfigInfo": "MonitoredBoth",
                                      "portUri": "d21"
                                  },
                {
                                      "portMonitorConfigInfo": "MonitoredBoth",
                                      "portUri": "d4"
                                  }
            ],
            "mirrorToPort": {
                "portMonitorConfigInfo": "AnalyzerPort",
                "portUri": "Q1"  # Enc1 Bay3
            }
        }
    ]
}

rspan_multi_sessions = {"type": "port-monitorV1",
                        "enablePortMonitor": True,
                        "portMonitorType": "Remote",
                        "remotePortMonitor": [{"networkUri": 'net100',
                                               "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredBoth",
                                                                   "portUri": "SGH751SLBL, interconnect 2, d12"
                                                                   }],
                                               "mirrorToPort": {"portMonitorConfigInfo": "AnalyzerPort",
                                                                "portUri": "SGH751SLBL, interconnect 2, Q2:1"
                                                                }
                                               },
                                              {"networkUri": 'net10',
                                               "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredBoth",
                                                                   "portUri": "SGH751SLBL, interconnect 2, d21"
                                                                   }],
                                               "mirrorToPort": {"portMonitorConfigInfo": "AnalyzerPort",
                                                                "portUri": "SGH751SLBL, interconnect 2, Q1:1"
                                                                }
                                               }
                                              ]
                        }

rspan_multi_sessions2 = {"type": "port-monitorV1",
                         "enablePortMonitor": True,
                         "portMonitorType": "Remote",
                         "remotePortMonitor": [{"networkUri": 'net100',
                                                "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredToServer",
                                                                    "portUri": "SGH751SLBL, interconnect 2, d12"
                                                                    }],
                                                "mirrorToPort": {"portMonitorConfigInfo": "AnalyzerPort",
                                                                 "portUri": "SGH751SLBL, interconnect 2, Q2:1"
                                                                 }
                                                },
                                               #                                                     { "networkUri": 'net10',
                                               #                                                       "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredToServer",
                                               #                                                                           "portUri": "SGH751SLBL, interconnect 2, d21"
                                               #                                                                           }],
                                               #                                                       "mirrorToPort": {"portMonitorConfigInfo": "AnalyzerPort",
                                               #                                                                        "portUri": "SGH751SLBL, interconnect 2, Q1:1"
                                               #                                                                        }
                                               #                                                      },
                                               {"networkUri": 'net80',
                                                "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredToServer",
                                                                    "portUri": "SGH751SLBL, interconnect 2, d23"
                                                                    }],
                                                "mirrorToPort": {"portMonitorConfigInfo": "AnalyzerPort",
                                                                 "portUri": "SGH751SLBK, interconnect 5, Q2:1"
                                                                 }
                                                },
                                               #                                                     {
                                               #                                                      "networkUri": 'net100',
                                               #                                                       "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredToServer",
                                               #                                                                           "portUri": "SGH751SLBL, interconnect 2, d12"
                                               #                                                                           }],
                                               #                                                       "mirrorToPort": {"portMonitorConfigInfo": "AnalyzerPort",
                                               #                                                                        "portUri": "SGH751SLBL, interconnect 2, Q5:1"
                                               #                                                                        }
                                               #                                                      }
                                               ]
                         }


rspan_multi_sessions_nitro = {"type": "port-monitorV1",
                              "enablePortMonitor": True,
                              "portMonitorType": "Remote",
                              "remotePortMonitor": [{"networkUri": 'net100',
                                                     "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredToServer",
                                                                         "portUri": "SGH751SLBL, interconnect 3, d12"
                                                                         }],
                                                     "mirrorToPort": {"portMonitorConfigInfo": "AnalyzerPort",
                                                                      "portUri": "SGH751SLBL, interconnect 3, Q1"
                                                                      }
                                                     },
                                                    {"networkUri": 'net10',
                                                     "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredToServer",
                                                                         "portUri": "SGH751SLBL, interconnect 3, d21"
                                                                         }],
                                                     "mirrorToPort": {"portMonitorConfigInfo": "AnalyzerPort",
                                                                      "portUri": "SGH751SLBK, interconnect 6, Q3:1"
                                                                      }
                                                     }]
                              }


icm_ports_mapping = {'d1': 'd1',
                     'd2': 'd2',
                     'd3': 'd3',
                     'd4': 'd4',
                     'd5': 'd5',
                     'd6': 'd6',
                     'd7': 'd7',
                     'd8': 'd8',
                     'd9': 'd9',
                     'd10': 'd10',
                     'd11': 'd11',
                     'd12': 'd12',
                     'd13': 'd1',
                     'd14': 'd2',
                     'd15': 'd3',
                     'd16': 'd4',
                     'd17': 'd5',
                     'd18': 'd6',
                     'd19': 'd7',
                     'd20': 'd8',
                     'd21': 'd9',
                     'd22': 'd10',
                     'd23': 'd11',
                     'd24': 'd12'
                     }


def get_rspan_details_from_ICM(hostname, username, password):
    port = 22
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)
    channel = ssh.invoke_shell(term='vt100', width=200, height=1000000, width_pixels=0, height_pixels=0)

    results = ''
    # Wait for shell to receive command
    while channel.recv_ready() is False:
        time.sleep(2)
        logger._log('\nChannel receive ready status: \n %s' % (channel.recv_ready()), level='DEBUG')
    results += channel.recv(50000)
    logger._log("\nResults After Login: \n", level='DEBUG')

    results = ''
    logger._log("\nSending 'no pagination' command.\n", level='DEBUG')
    channel.send('no pagination\n')
    while channel.recv_ready() is False:
        time.sleep(2)
        logger._log('\nChannel receive ready status: \n %s' % (channel.recv_ready()), level='DEBUG')
    results += channel.recv(50000)
    logger._log("\nResults after 'no pagination' command: \n", level='DEBUG')

    logger._log("Sending 'sh monitor all' command.\n", level='DEBUG')
    channel.send('sh monitor all\n')
    results = ''
    while channel.recv_ready() is False:
        time.sleep(2)
        logger._log('\nChannel receive ready status: \n %s' % (channel.recv_ready()), level='DEBUG')
    results += channel.recv(50000)
    logger._log("Results after 'sh monitor all' command: \n %s" % (results), level='DEBUG')

    # Close SSH shell
    ssh.close()

    # Get the table rows only from 'sh monitor all' command output
    table = "\n".join(results.split("\n")[5:-1])
    table = table.strip()
    table = table.split('\n')

    # Convert lines in table to dictionary
    dict = {k.strip(): v.strip() for k, v in (x.split(' : ') for x in table)}

    # Get required RSPAN session details from the dictionary
    nw_vlan_id = dict['Rspan Vlan Id']
    destination_port = 'Q' + dict['Destination Ports'].split('/')[-1]
    monitored_port = 'd' + dict['Both'].split('/')[-1]
    # Pack RSPAN session details into new dictionary and return the same
    dict2 = {'nw_vlan_id': nw_vlan_id, 'destination_port': destination_port, 'monitored_port': monitored_port}
    return dict2


def get_multi_rspan_details_from_ICM(hostname, username, password):
    port = 22
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)
    channel = ssh.invoke_shell(term='vt100', width=200, height=1000000, width_pixels=0, height_pixels=0)

    results = ''
    # Wait for shell to receive command
    while channel.recv_ready() is False:
        time.sleep(2)
        logger._log('\nChannel receive ready status: \n %s' % (channel.recv_ready()), level='DEBUG')
    results += channel.recv(50000)
    logger._log("\nResults After Login: \n", level='DEBUG')

    results = ''
    logger._log("\nSending 'no pagination' command.\n", level='DEBUG')
    channel.send('no pagination\n')
    while channel.recv_ready() is False:
        time.sleep(2)
        logger._log('\nChannel receive ready status: \n %s' % (channel.recv_ready()), level='DEBUG')
    results += channel.recv(50000)
    logger._log("\nResults after 'no pagination' command: \n", level='DEBUG')

    logger._log("Sending 'sh monitor all' command.\n", level='DEBUG')
    channel.send('sh monitor all\n')
    results = ''
    while channel.recv_ready() is False:
        time.sleep(2)
        logger._log('\nChannel receive ready status: \n %s' % (channel.recv_ready()), level='DEBUG')
    results += channel.recv(50000)
    logger._log("Results after 'sh monitor all' command: \n %s" % (results), level='DEBUG')

    # Close SSH shell
    ssh.close()
    # Get the table rows only from 'sh monitor all' command output
    results = "\n".join(results.split("\n")[:-1])
    # Convert multiple Sessions info into list of tables
    tables = re.split(r' Session     : \d{1}\r\n -------\r\n Source Ports', results)[1:]
    # Process List of tables and get required RSPAN Session Info
    session_list = []
    for session in tables:
        print "Table before Splitting\n", session
        session = session.strip()
        session = session.split('\r\n')
        print "Table After Splitting\n", session
        dict = {k.strip(): v.strip() for k, v in (x.split(' : ') for x in session)}
        nw_vlan_id = dict['Rspan Vlan Id']
        destination_ports_list = []
        if dict['Destination Ports'] != 'None':
            destination_ports = dict['Destination Ports'].split(',')
            for dp in destination_ports:
                dp = 'Q' + dp.split('/')[-1]
                destination_ports_list.append(dp)
        source_ports_dict = {}
        Rx_ports_list = []
        if dict['Rx'] != 'None':
            Rx_ports = dict['Rx'].split(',')
            for rp in Rx_ports:
                rp = 'd' + rp.split('/')[-1]
                Rx_ports_list.append(rp)
        Tx_ports_list = []
        if dict['Tx'] != 'None':
            Tx_ports = dict['Tx'].split(',')
            for tp in Tx_ports:
                tp = 'd' + tp.split('/')[-1]
                Tx_ports_list.append(tp)
        Monitored_both_port_list = []
        if dict['Both'] != 'None':
            Monitored_both_ports = dict['Both'].split(',')
            for mbp in Monitored_both_ports:
                mbp = 'd' + mbp.split('/')[-1]
                Monitored_both_port_list.append(mbp)
        monitored_ports = {'Tx_ports': Tx_ports_list.sort(), 'Rx_ports': Rx_ports_list.sort(), 'Monitored_both_ports': Monitored_both_port_list.sort()}
        session_dict = {'nw_vlan_id': nw_vlan_id, 'destination_ports': destination_ports_list, 'monitored_ports': monitored_ports}
        session_list.append(session_dict)
    return session_list


def get_rspan_details_from_data(dto):
    session_list = []
    sessions_dto = dto['remotePortMonitor']
    for session_dto in sessions_dto:
        nw_vlan_id = session_dto['networkUri']
        destination_ports_list = [(session_dto['mirrorToPort']['portUri'].split(',')[-1]).strip()]
        Tx_ports = []
        Rx_ports = []
        Monitored_both_ports = []
        for mtp_dto in session_dto['monitoredPorts']:
            if mtp_dto['portMonitorConfigInfo'] == 'MonitoredBoth':
                port_name = (mtp_dto['portUri'].split(',')[-1]).strip()
                port_name = icm_ports_mapping[port_name]
                Monitored_both_ports.append(port_name)
            elif mtp_dto['portMonitorConfigInfo'] == 'MonitoredFromServer':
                port_name = (mtp_dto['portUri'].split(',')[-1]).strip()
                port_name = icm_ports_mapping[port_name]
                Rx_ports.append(port_name)
            elif mtp_dto['portMonitorConfigInfo'] == 'MonitoredToServer':
                port_name = (mtp_dto['portUri'].split(',')[-1]).strip()
                port_name = icm_ports_mapping[port_name]
                Tx_ports.append(port_name)
        mtp_dict = {'Tx_ports': Tx_ports.sort(), 'Rx_ports': Rx_ports.sort(), 'Monitored_both_ports': Monitored_both_ports.sort()}
        session_dict = {'nw_vlan_id': nw_vlan_id, 'destination_ports': destination_ports_list, 'monitored_ports': mtp_dict}
        session_list.append(session_dict)
    return session_list

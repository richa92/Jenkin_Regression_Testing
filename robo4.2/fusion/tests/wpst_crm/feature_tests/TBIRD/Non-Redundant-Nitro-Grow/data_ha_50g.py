from data_common import *
CONFIG = 'HA'
SC = 4

update_downlink_speed = \
    [
        {
            "op": "replace",
            "path": "/downlinkSpeedMode",
            "value": "SPEED_25GB"
        }
    ]

uplink_set_1 = {
    'name': 'US1',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'lacpTimer': 'Short',
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '2', 'port': 'Q1', 'speed': 'Auto'},
    ]
}

uplink_set_2 = {
    'name': 'US2',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'lacpTimer': 'Short',
    'mode': 'Auto',
    'networkUris': ['net_420', 'net_421', 'net_422'],
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '2', 'bay': '5', 'port': 'Q1', 'speed': 'Auto'}
    ]
}

add_uplinkset = {
    'name': 'add_uplinkset',
    'type': 'uplink-setV5',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['net_425', 'net_426'],
    'manualLoginRedistributionState': 'NotSupported',
    'connectionMode': 'Auto',
    'portConfigInfos': [
                {	'desiredSpeed': 'Auto',
                  'location': {
                      'locationEntries': [
                          {
                              'value': 'Q6',
                              'type': 'Port'
                          },
                          {
                              'value': '2',
                              'type': 'Bay'
                          },
                          {
                              'value': ENC_1,
                              'type': 'Enclosure'
                          }
                      ]
                  }
                  }
    ],
}

edit_uplinkset = {
    'name': 'US1',
    'type': 'uplink-setV5',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'manualLoginRedistributionState': 'NotSupported',
    'lacpTimer': 'Long',
    'connectionMode': 'Auto',
    'portConfigInfos': [
        {
            'desiredSpeed': 'Auto',
            'location': {
                'locationEntries': [
                            {
                                'value': 'Q1',
                                'type': 'Port'
                            },
                    {
                                'value': '2',
                                'type': 'Bay'
                            },
                    {
                                'value': ENC_1,
                                'type': 'Enclosure'
                            }
                ]
            }
        }
    ],
}

###
# Interconnect bays configurations
# 2 Enclosures, Fabric 2
###

Enc2AMap = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2}
    ]

Enc2BMap = \
    [
        {'bay': 5, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]

###

###
# Interconnect bays configurations
# 3 Enclosures, Fabric 2
###

Enc3AMap = Enc2AMap + \
    [
        {'bay': 2, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

Enc3BMap = Enc2BMap + \
    [
        {'bay': 5, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]
###
# Interconnect bays configurations
# 4 Enclosures, Fabric 3
###

Enc4AMap = Enc3AMap + \
    [
        {'bay': 2, 'enclosure': 4, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 4}
    ]

Enc4BMap = Enc3BMap + \
    [
        {'bay': 5, 'enclosure': 4, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 4}
    ]

###
# Interconnect bays configurations
# 5 Enclosures, Fabric 3
###

Enc5AMap = Enc4AMap + \
    [
        {'bay': 2, 'enclosure': 5, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 5}
    ]

Enc5BMap = Enc4BMap + \
    [
        {'bay': 5, 'enclosure': 5, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 5}
    ]

###
# Logical Interconnect Groups
###
ligs = {
    'Enc2A-LIG': {
        'name': 'Enc2A-LIG',
                'interconnectMapTemplate': Enc2AMap,
                'enclosureIndexes': [1, 2],
                'interconnectBaySet': 2,
                'redundancyType': 'NonRedundantASide',
                'downlinkSpeedMode': 'SPEED_50GB',
                'uplinkSets': [uplink_set_1],
    },
    'Enc2B-LIG': {
        'name': 'Enc2B-LIG',
                'interconnectMapTemplate': Enc2BMap,
                'enclosureIndexes': [1, 2],
                'interconnectBaySet': 2,
                'redundancyType': 'NonRedundantBSide',
                'downlinkSpeedMode': 'SPEED_50GB',
                'uplinkSets': [uplink_set_2],
    },
    'Enc3A-LIG': {
        'name': 'Enc3A-LIG',
                'interconnectMapTemplate': Enc3AMap,
                'enclosureIndexes': [1, 2, 3],
                'interconnectBaySet': 2,
                'redundancyType': 'NonRedundantASide',
                'downlinkSpeedMode': 'SPEED_50GB',
                'uplinkSets': [uplink_set_1],
    },
    'Enc3B-LIG': {
        'name': 'Enc3B-LIG',
                'interconnectMapTemplate': Enc3BMap,
                'enclosureIndexes': [1, 2, 3],
                'interconnectBaySet': 2,
                'redundancyType': 'NonRedundantBSide',
                'downlinkSpeedMode': 'SPEED_50GB',
                'uplinkSets': [uplink_set_2],
    },
    'Enc4A-LIG': {
        'name': 'Enc4A-LIG',
                'interconnectMapTemplate': Enc4AMap,
                'enclosureIndexes': [1, 2, 3, 4],
                'interconnectBaySet': 2,
                'redundancyType': 'NonRedundantASide',
                'downlinkSpeedMode': 'SPEED_25GB',
                'uplinkSets': [uplink_set_1],
    },
    'Enc4B-LIG': {
        'name': 'Enc4B-LIG',
                'interconnectMapTemplate': Enc4BMap,
                'enclosureIndexes': [1, 2, 3, 4],
                'interconnectBaySet': 2,
                'redundancyType': 'NonRedundantBSide',
                'downlinkSpeedMode': 'SPEED_25GB',
                'uplinkSets': [uplink_set_2],
    },
    'Enc5A-LIG': {
        'name': 'Enc5A-LIG',
                'interconnectMapTemplate': Enc5AMap,
                'enclosureIndexes': [1, 2, 3, 4, 5],
                'interconnectBaySet': 2,
                'redundancyType': 'NonRedundantASide',
                'downlinkSpeedMode': 'SPEED_25GB',
                'uplinkSets': [uplink_set_1],
    },
    'Enc5B-LIG': {
        'name': 'Enc5B-LIG',
                'interconnectMapTemplate': Enc5BMap,
                'enclosureIndexes': [1, 2, 3, 4, 5],
                'interconnectBaySet': 2,
                'redundancyType': 'NonRedundantBSide',
                'downlinkSpeedMode': 'SPEED_25GB',
                'uplinkSets': [uplink_set_2],
    },
}

###
# Enclosure Groups
###
enc_group = {
    'Enc2-EG':
    {'name': 'Enc2-EG',
     'enclosureCount': 2,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc2A-LIG'},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc2B-LIG'},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
     },
    'Enc3-EG':
    {'name': 'Enc3-EG',
     'enclosureCount': 3,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc3A-LIG'},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc3B-LIG'},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
     },
    'Enc4-EG':
    {'name': 'Enc4-EG',
     'enclosureCount': 4,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc4A-LIG'},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc4B-LIG'},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
     },
    'Enc5-EG':
    {'name': 'Enc5-EG',
     'enclosureCount': 5,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc5A-LIG'},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc5B-LIG'},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
     }
}

###
# Server profiles
###
profiles = {
    'Profile1': {
        'payload': {
            'name': 'Profile1',
            'serverHardwareUri': ENC_1 + ', bay 2',
            'enclosureUri': ENC_1,
            'connectionSettings': {
                'connections': [
                    {	'name': 'conn',
                      'functionType': 'Ethernet',
                      'portId': 'Auto',
                      'networkUri': 'RNS',
                      },
                ]
            }
        },
        'IP': '10.11.0.255',
    },
    'Profile2': {
        'payload': {
            'name': 'Profile2',
            'serverHardwareUri': ENC_2 + ', bay 2',
            'enclosureUri': ENC_2,
            'connectionSettings': {
                'connections': [
                    {	'name': 'conn',
                      'functionType': 'Ethernet',
                      'portId': 'Auto',
                      'networkUri': 'RNS',
                      }
                ]
            }
        },
        'IP': '10.12.0.255',
    },
    'Profile3': {
        'payload': {
            'name': 'Profile3',
            'serverHardwareUri': ENC_3 + ', bay 2',
            'enclosureUri': ENC_3,
            'connectionSettings': {
                'connections': [
                    {	'name': 'conn',
                      'functionType': 'Ethernet',
                      'portId': 'Auto',
                      'networkUri': 'RNS',
                      }
                ]
            }
        },
        'IP': '10.13.0.255',
    },
    'Profile4': {
        'payload': {
            'name': 'Profile4',
            'serverHardwareUri': ENC_4 + ', bay 2',
            'enclosureUri': ENC_4,
            'connectionSettings': {
                'connections': [
                    {	'name': 'conn',
                      'functionType': 'Ethernet',
                      'portId': 'Auto',
                      'networkUri': 'net_404',
                      }
                ]
            }
        },
        'IP': '10.14.0.255',
    },
    'Profile5': {
        'payload': {
            'name': 'Profile5',
            'serverHardwareUri': ENC_5 + ', bay 2',
            'enclosureUri': ENC_5,
            'connectionSettings': {
                'connections': [
                    {	'name': 'conn',
                      'functionType': 'Ethernet',
                      'portId': 'Auto',
                      'networkUri': 'net_405',
                      }
                ]
            }
        },
        'IP': '10.15.0.255',
    }
}

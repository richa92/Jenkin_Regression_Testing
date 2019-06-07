from data_common import *
CONFIG = 'Redundant'
CXP = 'Mixed'

uplink_set = {
    'name': 'US1',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['wpstnetwork1', 'wpstnetwork2', 'wpstnetwork3', 'wpstnetwork4', 'wpstnetwork5'],
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '2', 'port': 'Q6', 'speed': 'Auto'}
    ]
}
uplink_set_2 = {
    'name': 'US2',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['wpstnetwork9', 'wpstnetwork10'],
    'lacpTimer': 'Short',
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'}
    ]
}
add_uplinkset = {
    'name': 'add_uplinkset',
    'type': 'uplink-setV300',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['wpstnetwork6', 'wpstnetwork7', 'wpstnetwork8'],
    'manualLoginRedistributionState': 'NotSupported',
    'connectionMode': 'Auto',
    'portConfigInfos': [
            {'desiredSpeed': 'Auto',
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
             },
    ],
    'logicalInterconnectUri': 'Grow-LE-Enc1A-LIG'
}
edit_uplinkset = {
    'name': 'US1',
    'type': 'uplink-setV300',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['wpstnetwork1', 'wpstnetwork2', 'wpstnetwork3'],
    'manualLoginRedistributionState': 'NotSupported',
    'lacpTimer': 'Long',
    'connectionMode': 'Auto',
    'portConfigInfos': [
            {'desiredSpeed': 'Auto',
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
             },
            {'desiredSpeed': 'Auto',
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
    'logicalInterconnectUri': 'Grow-LE-Enc1A-LIG'
}
###
# Interconnect bays configurations
# 1 Enclosures, Fabric 2
###

Enc1AMap = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    ]
Enc1BMap = \
    [
        {'bay': 5, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
    ]

###
# Interconnect bays configurations
# 2 Enclosures, Fabric 2
###
Enc2AMap = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
    ]

Enc2BMap = \
    [
        {'bay': 5, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2}
    ]

###
# Interconnect bays configurations
# 3 Enclosures, Fabric 2
###
Enc3AMap = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 2, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

Enc3BMap = \
    [
        {'bay': 5, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

###
# Interconnect bays configurations
# 4 Enclosures, Fabric 2
###
Enc4AMap = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 2, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 2, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

Enc4BMap = \
    [
        {'bay': 5, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 5, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4}
    ]
###
# LIGs for all 1, 2, 3 enclosure setups
###
ligs = {
    'Enc2A-LIG':
    {	'name': 'Enc2A-LIG',
      'interconnectMapTemplate': Enc2AMap,
      'enclosureIndexes': [1, 2],
      'interconnectBaySet': 2,
      'redundancyType': 'NonRedundantASide',
      'uplinkSets': [uplink_set],
      },
    'Enc2B-LIG':
    {	'name': 'Enc2B-LIG',
      'interconnectMapTemplate': Enc2BMap,
      'enclosureIndexes': [1, 2],
      'interconnectBaySet': 2,
      'redundancyType': 'NonRedundantBSide',
      'uplinkSets': [uplink_set_2],
      },
    'Enc3A-LIG':
    {	'name': 'Enc3A-LIG',
      'interconnectMapTemplate': Enc3AMap,
      'enclosureIndexes': [1, 2, 3],
      'interconnectBaySet': 2,
      'redundancyType': 'NonRedundantASide',
      'uplinkSets': [uplink_set],
      },
        'Enc3B-LIG':
    {	'name': 'Enc3B-LIG',
      'interconnectMapTemplate': Enc3BMap,
      'enclosureIndexes': [1, 2, 3],
      'interconnectBaySet': 2,
      'redundancyType': 'NonRedundantBSide',
      'uplinkSets': [uplink_set_2],
      },
    'Enc4A-LIG':
    {	'name': 'Enc4A-LIG',
      'interconnectMapTemplate': Enc4AMap,
      'enclosureIndexes': [1, 2, 3, 4],
      'interconnectBaySet': 2,
      'redundancyType': 'NonRedundantASide',
      'uplinkSets': [uplink_set],
      },
        'Enc4B-LIG':
    {	'name': 'Enc4B-LIG',
      'interconnectMapTemplate': Enc4BMap,
      'enclosureIndexes': [1, 2, 3, 4],
      'interconnectBaySet': 2,
      'redundancyType': 'NonRedundantBSide',
      'uplinkSets': [uplink_set_2],
      }
}

enc_group = {
    'Enc1-EG':
    {'name': 'Enc1-EG',
     'enclosureCount': 1,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc1A-LIG'},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc1B-LIG'},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
     },
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
     'powerMode': "RedundantPowerFeed"
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
     'powerMode': "RedundantPowerFeed"
     },
}

###
# Server profiles
###
profiles = {
    'Profile1': {
        'payload': {
            'name': 'Profile1',
            'serverHardwareUri': ENC_1 + ', bay 1',
            'enclosureUri': ENC_1,
            'connections': [
                {	'name': 'conn',
                  'functionType': 'Ethernet',
                  'portId': 'Auto',
                  'networkUri': 'wpstnetwork1',
                  }
            ]
        },
        'IP': '10.11.0.254',
        'handle': None
    },
    'Profile2': {
        'payload': {
            'name': 'Profile2',
            'serverHardwareUri': ENC_2 + ', bay 1',
            'enclosureUri': ENC_2,
            'connections': [
                {	'name': 'conn',
                  'functionType': 'Ethernet',
                  'portId': 'Auto',
                  'networkUri': 'wpstnetwork2',
                  }
            ]
        },
        'IP': '10.12.0.254',
        'handle': None
    },
    'Profile3': {
        'payload': {
            'name': 'Profile3',
            'serverHardwareUri': ENC_3 + ', bay 1',
            'enclosureUri': ENC_3,
            'connections': [
                {	'name': 'conn',
                  'functionType': 'Ethernet',
                  'portId': 'Auto',
                  'networkUri': 'wpstnetwork3',
                  }
            ]
        },
        'IP': '10.13.0.254',
        'handle': None
    },
    'Profile4': {
        'payload': {
            'name': 'Profile4',
            'serverHardwareUri': ENC_4 + ', bay 1',
            'enclosureUri': ENC_4,
            'connections': [
                {	'name': 'conn',
                  'functionType': 'Ethernet',
                  'portId': 'Auto',
                  'networkUri': 'wpstnetwork4',
                  }
            ]
        },
        'IP': '10.14.0.254',
        'handle': None
    }
}

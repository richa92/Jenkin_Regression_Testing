from data_common import *
CONFIG = 'Redundant'
CXP = 'CL20'

uplink_set = {
    'name': 'US1',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['wpstnetwork1', 'wpstnetwork2', 'wpstnetwork3', 'wpstnetwork4', 'wpstnetwork5'],
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '2', 'port': 'Q6', 'speed': 'Auto'},
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
            {'desiredSpeed': 'Auto',
             'location': {
                             'locationEntries': [
                                 {
                                     'value': 'Q1',
                                     'type': 'Port'
                                 },
                                 {
                                     'value': '5',
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
             },
            {'desiredSpeed': 'Auto',
             'location': {
                             'locationEntries': [
                                 {
                                     'value': 'Q1',
                                     'type': 'Port'
                                 },
                                 {
                                     'value': '5',
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
# 1 Enclosures, Fabric 2
###

Enc1Map = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
    ]

###
# Interconnect bays configurations
# 2 Enclosures, Fabric 2
###

Enc2Map = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2}
    ]

###
# Interconnect bays configurations
# 3 Enclosures, Fabric 2
###

Enc3Map = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 2, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 5, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

###
# LIGs for all 1, 2, 3 enclosure setups
###
ligs = {
    'Enc1-LIG':
    {'name': 'Enc1-LIG',
             'interconnectMapTemplate': Enc1Map,
             'enclosureIndexes': [1],
             'interconnectBaySet': 2,
             'redundancyType': 'Redundant',
             'uplinkSets': [uplink_set, uplink_set_2],
     },
        'Enc2-LIG':
            {'name': 'Enc2-LIG',
             'interconnectMapTemplate': Enc2Map,
             'enclosureIndexes': [1, 2],
             'interconnectBaySet': 2,
             'redundancyType': 'Redundant',
             'uplinkSets': [uplink_set, uplink_set_2],
             },
        'Enc3-LIG':
            {'name': 'Enc3-LIG',
             'interconnectMapTemplate': Enc3Map,
             'enclosureIndexes': [1, 2, 3],
             'interconnectBaySet': 2,
             'redundancyType': 'Redundant',
             'uplinkSets': [uplink_set, uplink_set_2],
             },
}

enc_group = {
    'Enc1-EG':
    {'name': 'Enc1-EG',
     'enclosureCount': 1,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc1-LIG'},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc1-LIG'},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
     },
    'Enc2-EG':
    {'name': 'Enc2-EG',
     'enclosureCount': 2,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
     },
    'Enc3-EG':
    {'name': 'Enc3-EG',
     'enclosureCount': 3,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG'},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG'},
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
    }
}

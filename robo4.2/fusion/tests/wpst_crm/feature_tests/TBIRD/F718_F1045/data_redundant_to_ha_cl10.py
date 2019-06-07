from data_common import *
CONFIG = 'Redundant_To_HA'
CXP = 'CL10'

uplink_set = {
    'name': 'US1',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['wpstnetwork1', 'wpstnetwork2', 'wpstnetwork3', 'wpstnetwork4', 'wpstnetwork5'],
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'}
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
                                     'value': '3',
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
    'logicalInterconnectUri': 'Grow-LE-Enc1-LIG'
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
                                     'value': '3',
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
    'logicalInterconnectUri': 'Grow-LE-Enc1-LIG'
}

###
# Interconnect bays configurations
# 1 Enclosures, Fabric 3
###

Enc1Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
    ]

###
# Interconnect bays configurations
# 2 Enclosures, Fabric 3
###

Enc2Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
    ]

###
# LIGs for 1 and 2 enclosure setup
###
ligs = {
    'Enc1-LIG':
    {'name': 'Enc1-LIG',
             'interconnectMapTemplate': Enc1Map,
             'enclosureIndexes': [1],
             'interconnectBaySet': 3,
             'redundancyType': 'Redundant',
             'uplinkSets': [uplink_set],
     },
        'Enc2-LIG':
            {'name': 'Enc2-LIG',
             'type': 'logical-interconnect-groupV3',
             'interconnectMapTemplate': Enc2Map,
             'enclosureIndexes': [1, 2],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [uplink_set],
             }
}

enc_group = {
    'Enc1-EG':
    {'name': 'Enc1-EG',
     'enclosureCount': 1,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc1-LIG'},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc1-LIG'}],
     },
    'Enc2-EG':
    {'name': 'Enc2-EG',
     'enclosureCount': 2,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'}],
     }
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
        'IP': '10.11.0.255',
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
        'IP': '10.12.0.255',
        'handle': None
    }
}

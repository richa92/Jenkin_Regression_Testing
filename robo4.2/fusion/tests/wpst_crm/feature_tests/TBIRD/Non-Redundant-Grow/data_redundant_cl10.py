from data_common import *
CONFIG = 'Redundant'
CXP = 'CL10'

uplink_set = {
    'name': 'US1',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['wpstnetwork1', 'wpstnetwork2', 'wpstnetwork3', 'wpstnetwork4', 'wpstnetwork5'],
    'lacpTimer': 'Short',
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'},
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
        {'enclosure': '1', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'}
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
                {
                    'desiredSpeed': 'Auto',
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
                }
    ],
    'logicalInterconnectUri': 'Grow-LE-Enc1A-LIG'
}
edit_uplinkset = {
    'name': 'US1',
    'type': 'uplink-setV300',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['wpstnetwork1', 'wpstnetwork2', 'wpstnetwork3', 'wpstnetwork4', 'wpstnetwork5', 'wpstnetwork6'],
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
    'logicalInterconnectUri': 'Grow-LE-Enc1A-LIG'
}

###
# Interconnect bays configurations
# 1 Enclosures, Fabric 3
###
Enc1AMap = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    ]

Enc1BMap = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
    ]
###
###
# Interconnect bays configurations
# 2 Enclosures, Fabric 3
###
Enc2AMap = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
    ]

Enc2BMap = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2}
    ]

###
###
# Interconnect bays configurations
# 3 Enclosures, Fabric 3
###
Enc3AMap = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

Enc3BMap = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

###
# Interconnect bays configurations
# 4 Enclosures, Fabric 3
###
Enc4AMap = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 3, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4}
    ]

Enc4BMap = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4}
    ]

###
# Interconnect bays configurations
# 5 Enclosures, Fabric 3
###
Enc5AMap = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 3, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 3, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5}
    ]

Enc5BMap = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 6, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5}
    ]

###
# Logical Interconnect Groups
###
ligs = {
    'Enc1A-LIG':
        {	'name': 'Enc1A-LIG',
          'interconnectMapTemplate': Enc1AMap,
          'enclosureIndexes': [1],
          'interconnectBaySet': 3,
          'redundancyType': 'NonRedundantASide',
          'uplinkSets': [uplink_set],
          },
    'Enc1B-LIG':
        {	'name': 'Enc1-LIG',
          'interconnectMapTemplate': Enc1BMap,
          'enclosureIndexes': [1],
          'interconnectBaySet': 3,
          'redundancyType': 'NonRedundantBSide',
          'uplinkSets': [uplink_set_2],
          },
    'Enc2A-LIG':
    {	'name': 'Enc2A-LIG',
            'interconnectMapTemplate': Enc2AMap,
            'enclosureIndexes': [1, 2],
            'interconnectBaySet': 3,
            'redundancyType': 'NonRedundantASide',
            'uplinkSets': [uplink_set],
      },
    'Enc2B-LIG':
    {	'name': 'Enc2B-LIG',
        'interconnectMapTemplate': Enc2BMap,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantBSide',
        'uplinkSets': [uplink_set_2],
      },
    'Enc3A-LIG':
        {	'name': 'Enc3A-LIG',
          'interconnectMapTemplate': Enc3AMap,
          'enclosureIndexes': [1, 2, 3],
          'interconnectBaySet': 3,
          'redundancyType': 'NonRedundantASide',
          'uplinkSets': [uplink_set],
          },
        'Enc3B-LIG':
        {	'name': 'Enc3B-LIG',
          'interconnectMapTemplate': Enc3BMap,
          'enclosureIndexes': [1, 2, 3],
          'interconnectBaySet': 3,
          'redundancyType': 'NonRedundantBSide',
          'uplinkSets': [uplink_set_2],
          },
        'Enc4A-LIG':
        {	'name': 'Enc4A-LIG',
          'interconnectMapTemplate': Enc4AMap,
          'enclosureIndexes': [1, 2, 3, 4],
          'interconnectBaySet': 3,
          'redundancyType': 'NonRedundantASide',
          'uplinkSets': [uplink_set],
          },
        'Enc4B-LIG':
        {	'name': 'Enc4B-LIG',
          'interconnectMapTemplate': Enc4BMap,
          'enclosureIndexes': [1, 2, 3, 4],
          'interconnectBaySet': 3,
          'redundancyType': 'NonRedundantBSide',
          'uplinkSets': [uplink_set_2],
          },
        'Enc5A-LIG':
        {	'name': 'Enc5A-LIG',
          'interconnectMapTemplate': Enc5AMap,
          'enclosureIndexes': [1, 2, 3, 4, 5],
          'interconnectBaySet': 3,
          'redundancyType': 'NonRedundantASide',
          'uplinkSets': [uplink_set],
          },
        'Enc5B-LIG':
        {	'name': 'Enc5B-LIG',
          'interconnectMapTemplate': Enc5BMap,
          'enclosureIndexes': [1, 2, 3, 4, 5],
          'interconnectBaySet': 3,
          'redundancyType': 'NonRedundantBSide',
          'uplinkSets': [uplink_set_2],
          },
}

###
# Enclosure Groups
###
enc_group = {
    'Enc1-EG':
    {'name': 'Enc1-EG',
     'enclosureCount': 1,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc1A-LIG'},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc1B-LIG'}],
     },
    'Enc2-EG':
    {'name': 'Enc2-EG',
     'enclosureCount': 2,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2A-LIG'},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2B-LIG'}],
     },
    'Enc3-EG':
    {'name': 'Enc3-EG',
     'enclosureCount': 3,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc3A-LIG'},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc3B-LIG'}],
     },
    'Enc4-EG':
    {'name': 'Enc4-EG',
     'enclosureCount': 4,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc4A-LIG'},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc4B-LIG'}],
     },
    'Enc5-EG':
    {'name': 'Enc5-EG',
     'enclosureCount': 5,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc5A-LIG'},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc5B-LIG'}],
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
        'IP': '10.13.0.255',
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
        'IP': '10.14.0.255',
        'handle': None
    },
    'Profile5': {
        'payload': {
            'name': 'Profile5',
            'serverHardwareUri': ENC_5 + ', bay 1',
            'enclosureUri': ENC_5,
            'connections': [
                {	'name': 'conn',
                  'functionType': 'Ethernet',
                  'portId': 'Auto',
                  'networkUri': 'wpstnetwork5',
                  }
            ]
        },
        'IP': '10.15.0.255',
        'handle': None
    }
}

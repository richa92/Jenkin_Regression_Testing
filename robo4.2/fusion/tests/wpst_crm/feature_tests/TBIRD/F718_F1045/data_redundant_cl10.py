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
        {'enclosure': '1', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}
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
                },
        {
                    'desiredSpeed': 'Auto',
                    'location': {
                        'locationEntries': [
                            {
                                'value': 'Q1',
                                'type': 'Port'
                            },
                            {
                                'value': '6',
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
    'logicalInterconnectUri': 'Grow-LE-Enc2-LIG'
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
        {
            'desiredSpeed': 'Auto',
            'location': {
                'locationEntries': [
                            {
                                'value': 'Q1',
                                'type': 'Port'
                            },
                    {
                                'value': '6',
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
    'logicalInterconnectUri': 'Grow-LE-Enc2-LIG'
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
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
    ]

###
# Interconnect bays configurations
# 3 Enclosures, Fabric 3
###

Enc3Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]


###
# Interconnect bays configurations
# 4 Enclosures, Fabric 3
###

Enc4Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 3, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 6, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4}
    ]

###
# Interconnect bays configurations
# 5 Enclosures, Fabric 3
###

Enc5Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 3, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 6, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 3, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5},
        {'bay': 6, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5}
    ]

###
# Logical Interconnect Groups
###
ligs = {
    'Enc1-LIG': {
        'name': 'Enc1-LIG',
                'interconnectMapTemplate': Enc1Map,
                'enclosureIndexes': [1],
                'interconnectBaySet': 3,
                'redundancyType': 'Redundant',
        'uplinkSets': [uplink_set],
    },
    'Enc2-LIG': {
        'name': 'Enc2-LIG',
        'interconnectMapTemplate': Enc2Map,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'uplinkSets': [uplink_set],
    },
    'Enc3-LIG': {
        'name': 'Enc3-LIG',
        'interconnectMapTemplate': Enc3Map,
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'uplinkSets': [uplink_set],
    },
    'Enc4-LIG': {
        'name': 'Enc4-LIG',
        'interconnectMapTemplate': Enc4Map,
        'enclosureIndexes': [1, 2, 3, 4],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'uplinkSets': [uplink_set],
    },
    'Enc5-LIG': {
        'name': 'Enc5-LIG',
        'interconnectMapTemplate': Enc5Map,
        'enclosureIndexes': [1, 2, 3, 4, 5],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'uplinkSets': [uplink_set],
    }
}

###
# Enclosure Groups
###
enc_group = {
    'Enc1-EG':
    {'name': 'Enc1-EG',
     'type': 'EnclosureGroupV400',
     'enclosureCount': 1,
     'enclosureTypeUri': '/rest/enclosure-types/SY12000',
     'stackingMode': 'Enclosure',
     'interconnectBayMappingCount': 6,
     'configurationScript': None,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc1-LIG'},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc1-LIG'}],
     'ipAddressingMode': "External",
     'ipRangeUris': [],
     'powerMode': "RedundantPowerFeed"
     },
    'Enc2-EG':
    {'name': 'Enc2-EG',
     'type': 'EnclosureGroupV400',
     'enclosureCount': 2,
     'enclosureTypeUri': '/rest/enclosure-types/SY12000',
     'stackingMode': 'Enclosure',
     'interconnectBayMappingCount': 6,
     'configurationScript': None,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'}],
     'ipAddressingMode': "External",
     'ipRangeUris': [],
     'powerMode': "RedundantPowerFeed"
     },
    'Enc3-EG':
    {'name': 'Enc3-EG',
     'type': 'EnclosureGroupV400',
     'enclosureCount': 3,
     'enclosureTypeUri': '/rest/enclosure-types/SY12000',
     'stackingMode': 'Enclosure',
     'interconnectBayMappingCount': 6,
     'configurationScript': None,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG'},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG'}],
     'ipAddressingMode': "External",
     'ipRangeUris': [],
     'powerMode': "RedundantPowerFeed"
     },
    'Enc4-EG':
    {'name': 'Enc4-EG',
     'type': 'EnclosureGroupV400',
     'enclosureCount': 4,
     'enclosureTypeUri': '/rest/enclosure-types/SY12000',
     'stackingMode': 'Enclosure',
     'interconnectBayMappingCount': 6,
     'configurationScript': None,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc4-LIG'},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc4-LIG'}],
     'ipAddressingMode': "External",
     'ipRangeUris': [],
     'powerMode': "RedundantPowerFeed"
     },
    'Enc5-EG':
    {'name': 'Enc5-EG',
     'type': 'EnclosureGroupV400',
     'enclosureCount': 5,
     'enclosureTypeUri': '/rest/enclosure-types/SY12000',
     'stackingMode': 'Enclosure',
     'interconnectBayMappingCount': 6,
     'configurationScript': None,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc5-LIG'},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc5-LIG'}],
     'ipAddressingMode': "External",
     'ipRangeUris': [],
     'powerMode': "RedundantPowerFeed"
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

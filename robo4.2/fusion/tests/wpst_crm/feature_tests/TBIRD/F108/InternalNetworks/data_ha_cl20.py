ENC_1 = 'CN754404R1'
ENC_2 = 'CN754406W2'
ENC_3 = 'CN754404R5'
CONFIG = 'HA'

ns1 = {
    'name': 'NS1',
    'type': 'network-setV4',
    'networkUris': ['wpstnetwork4', 'wpstnetwork5'],
    'nativeNetworkUri': 'wpstnetwork4'
}

ns1_add_network = {
    'name': 'NS1',
    'type': 'network-setV4',
    'networkUris': ['wpstnetwork4', 'wpstnetwork5', 'wpstnetwork6'],
    'nativeNetworkUri': 'wpstnetwork4'
}

ns2 = {
    'name': 'NS2',
    'type': 'network-setV4',
    'networkUris': ['wpstnetwork7', 'wpstnetwork8']
}

ns2_add_network = {
    'name': 'NS2',
    'type': 'network-setV4',
    'networkUris': ['wpstnetwork7', 'wpstnetwork8', 'wpstnetwork9']
}

uplink_set = {
    'name': 'US',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['wpstnetwork1', 'wpstnetwork2'],
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '2', 'port': 'Q6', 'speed': 'Auto'}
    ]
}

uplink_set_network_deleted = {
    'name': 'US',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['wpstnetwork2'],
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '2', 'port': 'Q6', 'speed': 'Auto'},
    ]
}

us_add_network = {
    'name': 'US',
    'type': 'uplink-setV4',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['wpstnetwork1', 'wpstnetwork2', 'wpstnetwork10'],
    'manualLoginRedistributionState': 'NotSupported',
    'connectionMode': 'Auto',
    'portConfigInfos': [
        {
            'desiredSpeed': 'Auto',
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
    'logicalInterconnectUri': 'Enc2-LE-Enc2-LIG'
}

us_delete_network = {
    'name': 'US',
    'type': 'uplink-setV4',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['wpstnetwork2'],
    'manualLoginRedistributionState': 'NotSupported',
    'connectionMode': 'Auto',
    'portConfigInfos': [
        {
            'desiredSpeed': 'Auto',
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
    'logicalInterconnectUri': 'Enc2-LE-Enc2-LIG'
}

lig_delete_network = {
    'type': 'logical-interconnect-groupV4',
    'enclosureType': 'SY12000',
    'interconnectBaySet': 2,
    'redundancyType': 'HighlyAvailable',
    'internalNetworkUris': ['wpstnetwork10'],
    'uplinkSets': [uplink_set_network_deleted]
}

###
# Interconnect bays configurations
# 2 Enclosures, Fabric 3
###

Enc2Map = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
    ]

###
# Interconnect bays configurations
# 3 Enclosures, Fabric 3
###

Enc3Map = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 2, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 5, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

###
# LIGs for all 1, 2, 3, 4 and 5 enclosure setups in one or two fabric mode using CL10 and CL20
###
ligs = {
    'Enc2-LIG': {
        'name': 'Enc2-LIG',
        'interconnectMapTemplate': Enc2Map,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 2,
        'redundancyType': 'HighlyAvailable',
        'uplinkSets': [uplink_set],
        'internalNetworkUris': ['wpstDefaultnetwork', 'wpstnetwork10']
    },
    'Enc3-LIG': {
        'name': 'Enc3-LIG',
        'interconnectMapTemplate': Enc3Map,
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 2,
        'redundancyType': 'HighlyAvailable',
        'uplinkSets': [uplink_set],
        'internalNetworkUris': ['wpstDefaultnetwork', 'wpstnetwork10']
    }
}

enc_group = {
    'Enc2-EG':
        {'name': 'Enc2-EG',
         'enclosureCount': 2,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}
              ],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
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
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}
              ],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         }
}

###
# All logical enclosures
###
les = {
    'Enc2-LE':
        {'name': 'Enc2-LE',
         'enclosureUris': [ENC_1, ENC_2],
         'enclosureGroupUri': 'Enc2-EG',
         'firmwareBaselineUri': None,
         'forceInstallFirmware': False
         },
    'Enc3-LE':
        {'name': 'Enc3-LE',
         'enclosureUris': [ENC_1, ENC_2, ENC_3],
         'enclosureGroupUri': 'Enc3-EG',
         'firmwareBaselineUri': None,
         'forceInstallFirmware': False
         }
}

###
# Server profiles
###
profiles = {
    'Profile1': {
        'name': 'Profile1',
        'type': 'ServerProfileV8',
        'serverHardwareUri': ENC_1 + ', bay 1',
        'enclosureUri': ENC_1,
        'connectionSettings': {
            'connections': [
                {'name': 'conn',
                 'functionType': 'Ethernet',
                 'portId': 'Auto',
                 'networkUri': 'wpstnetwork10',
                 }
            ]
        },
    },
    'Profile2': {
        'name': 'Profile2',
        'type': 'ServerProfileV8',
        'serverHardwareUri': ENC_1 + ', bay 1',
        'enclosureUri': ENC_1,
        'connectionSettings': {
            'connections': [
                {'name': 'conn',
                 'functionType': 'Ethernet',
                 'portId': 'Auto',
                 'networkUri': 'wpstnetwork1',
                 }
            ]
        },
    },
    'Profile3': {
        'name': 'Profile3',
        'type': 'ServerProfileV8',
        'serverHardwareUri': ENC_1 + ', bay 1',
        'enclosureUri': ENC_1,
        'connectionSettings': {
            'connections': [
                {'name': 'conn',
                 'functionType': 'Ethernet',
                 'portId': 'Auto',
                 'networkUri': 'NS2',
                 }
            ]
        },
    }
}

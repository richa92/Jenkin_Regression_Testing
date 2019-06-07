ENC_1 = 'CN754406W7'
ENC_2 = 'CN7544044C'
ENC_3 = 'CN754406WT'
ENC_4 = 'CN754404QX'
ENC_5 = 'CN7544044D'
CONFIG = 'HA'

lig_uplink_set = {
    'name': 'US1',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['wpstnetwork1', 'wpstnetwork2', 'wpstnetwork3', 'wpstnetwork4', 'wpstnetwork5'],
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'},
        {'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}
    ]
}

lig_add_uplinkset = {
    'name': 'add_uplinkset',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['wpstnetwork6', 'wpstnetwork7', 'wpstnetwork8'],
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'},
        {'enclosure': '2', 'bay': '6', 'port': 'Q1', 'speed': 'Auto'}
    ]
}

lig_edit_uplinkset = {
    'name': 'US1',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['wpstnetwork1', 'wpstnetwork2', 'wpstnetwork3'],
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'},
        {'enclosure': '2', 'bay': '6', 'port': 'Q1', 'speed': 'Auto'}
    ]
}

li_add_uplinkset = {
    'name': 'add_uplinkset',
    'type': 'uplink-setV4',
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
        {'desiredSpeed': 'Auto',
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
                     'value': ENC_2,
                     'type': 'Enclosure'
                 }
             ]
         }
         }
    ],
    'logicalInterconnectUri': 'Enc2-LE-Enc2-LIG'
}

li_edit_uplinkset = {
    'name': 'US1',
    'type': 'uplink-setV4',
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
        {'desiredSpeed': 'Auto',
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
                     'value': ENC_2,
                     'type': 'Enclosure'
                 }
             ]
         }
         }
    ],
    'logicalInterconnectUri': 'Enc2-LE-Enc2-LIG'
}

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
# Interconnect bays configurations
# 3 Enclosures, Fabric 3
###

Enc3Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
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
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
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
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 3, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 6, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 3, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5},
        {'bay': 6, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5}
    ]

###
# LIGs for all 1, 2, 3, 4 and 5 enclosure setups in one or two fabric mode using CL10 and CL20
###
ligs = {
    'Enc2-LIG':
        {'name': 'Enc2-LIG',
         'interconnectMapTemplate': Enc2Map,
         'enclosureIndexes': [1, 2],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'uplinkSets': [lig_uplink_set],
         },
    'Enc3-LIG':
        {'name': 'Enc3-LIG',
         'interconnectMapTemplate': Enc3Map,
         'enclosureIndexes': [1, 2, 3],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'uplinkSets': [lig_uplink_set],
         },
    'Enc4-LIG':
        {'name': 'Enc4-LIG',
         'interconnectMapTemplate': Enc4Map,
         'enclosureIndexes': [1, 2, 3, 4],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'uplinkSets': [lig_uplink_set],
         },
    'Enc5-LIG':
        {'name': 'Enc5-LIG',
         'interconnectMapTemplate': Enc5Map,
         'enclosureIndexes': [1, 2, 3, 4, 5],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'uplinkSets': [lig_uplink_set],
         },

}

telemetry = {
    'type': 'telemetry-configuration',
    'enableTelemetry': False,
    'sampleInterval': 200,
    'sampleCount': 20
}

ethernet_setting = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': False,
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 130,
    'macRefreshInterval': 10
}

edit_telemetry = {
    'type': 'logical-interconnect-groupV4',
    'enclosureType': 'SY12000',
    'interconnectBaySet': 3,
    'redundancyType': 'HighlyAvailable',
    'uplinkSets': [lig_uplink_set],
    'telemetryConfiguration': telemetry
}

edit_ethernetSettings = {
    'type': 'logical-interconnect-groupV4',
    'enclosureType': 'SY12000',
    'interconnectBaySet': 3,
    'redundancyType': 'HighlyAvailable',
    'uplinkSets': [lig_uplink_set],
    'ethernetSettings': ethernet_setting
}

edit_add_uplinkset = {
    'type': 'logical-interconnect-groupV4',
    'enclosureType': 'SY12000',
    'interconnectBaySet': 3,
    'redundancyType': 'HighlyAvailable',
    'uplinkSets': [lig_uplink_set, lig_add_uplinkset]
}

edit_delete_uplinkset = {
    'type': 'logical-interconnect-groupV4',
    'enclosureType': 'SY12000',
    'interconnectBaySet': 3,
    'redundancyType': 'HighlyAvailable',
    'uplinkSets': [lig_uplink_set]
}

edit_edit_uplinkset = {
    'type': 'logical-interconnect-groupV4',
    'enclosureType': 'SY12000',
    'interconnectBaySet': 3,
    'redundancyType': 'HighlyAvailable',
    'uplinkSets': [lig_edit_uplinkset]
}

enc_group = {
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
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },
    'Enc3-EG':
        {'name': 'Enc3-EG',
         'enclosureCount': 3,
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
         'enclosureCount': 4,
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
         'enclosureCount': 5,
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
         },
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
         },
    'Enc4-LE':
        {'name': 'Enc4-LE',
         'enclosureUris': [ENC_1, ENC_2, ENC_3, ENC_4],
         'enclosureGroupUri': 'Enc4-EG',
         'firmwareBaselineUri': None,
         'forceInstallFirmware': False
         },
    'Enc5-LE':
        {'name': 'Enc5-LE',
         'enclosureUris': [ENC_1, ENC_2, ENC_3, ENC_4, ENC_5],
         'enclosureGroupUri': 'Enc5-EG',
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
                 'networkUri': 'wpstnetwork1',
                 }
            ]
        },
    },
    'Profile2': {
        'name': 'Profile2',
        'type': 'ServerProfileV8',
        'serverHardwareUri': ENC_2 + ', bay 1',
        'enclosureUri': ENC_2,
        'connectionSettings': {
            'connections': [
                {'name': 'conn',
                 'functionType': 'Ethernet',
                 'portId': 'Auto',
                 'networkUri': 'wpstnetwork3',
                 }
            ]
        },
    },
    'Profile3': {
        'name': 'Profile3',
        'type': 'ServerProfileV8',
        'serverHardwareUri': ENC_3 + ', bay 1',
        'enclosureUri': ENC_3,
        'connectionSettings': {
            'connections': [
                {'name': 'conn',
                 'functionType': 'Ethernet',
                 'portId': 'Auto',
                 'networkUri': 'wpstnetwork2',
                 }
            ]
        },
    },
    'Profile4': {
        'name': 'Profile4',
        'type': 'ServerProfileV8',
        'serverHardwareUri': ENC_4 + ', bay 1',
        'enclosureUri': ENC_4,
        'connectionSettings': {
            'connections': [
                {'name': 'conn',
                 'functionType': 'Ethernet',
                 'portId': 'Auto',
                 'networkUri': 'wpstnetwork4',
                 }
            ]
        },
    },
    'Profile5': {
        'name': 'Profile5',
        'type': 'ServerProfileV8',
        'serverHardwareUri': ENC_5 + ', bay 1',
        'enclosureUri': ENC_5,
        'connectionSettings': {
            'connections': [
                {'name': 'conn',
                 'functionType': 'Ethernet',
                 'portId': 'Auto',
                 'networkUri': 'wpstnetwork5',
                 }
            ]
        },
    }
}

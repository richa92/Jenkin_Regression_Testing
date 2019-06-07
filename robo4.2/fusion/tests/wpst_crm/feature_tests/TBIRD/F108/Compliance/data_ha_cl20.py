ENC_1 = 'CN754404R1'
ENC_2 = 'CN754406W2'
ENC_3 = 'CN754404R5'
CONFIG = 'HA'

lig_uplink_set = {
    'name': 'US1',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['wpstnetwork1', 'wpstnetwork2', 'wpstnetwork3', 'wpstnetwork4', 'wpstnetwork5'],
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '2', 'port': 'Q6', 'speed': 'Auto'},
        {'enclosure': '2', 'bay': '5', 'port': 'Q6', 'speed': 'Auto'}
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
        {'enclosure': '1', 'bay': '2', 'port': 'Q1', 'speed': 'Auto'},
        {'enclosure': '2', 'bay': '5', 'port': 'Q1', 'speed': 'Auto'}
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
        {'enclosure': '1', 'bay': '2', 'port': 'Q1', 'speed': 'Auto'},
        {'enclosure': '2', 'bay': '5', 'port': 'Q1', 'speed': 'Auto'}
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
                        'value': '5',
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
                        'value': '5',
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
# LIGs for all 1, 2, 3 enclosure setups
###
ligs = {
    'Enc2-LIG': {
        'name': 'Enc2-LIG',
        'interconnectMapTemplate': Enc2Map,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 2,
        'redundancyType': 'HighlyAvailable',
        'uplinkSets': [lig_uplink_set],
    },
    'Enc3-LIG': {
        'name': 'Enc3-LIG',
        'interconnectMapTemplate': Enc3Map,
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 2,
        'redundancyType': 'HighlyAvailable',
        'uplinkSets': [lig_uplink_set],
    }
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
    'interconnectBaySet': 2,
    'redundancyType': 'HighlyAvailable',
    'uplinkSets': [lig_uplink_set],
    'telemetryConfiguration': telemetry
}

edit_ethernetSettings = {
    'type': 'logical-interconnect-groupV4',
    'enclosureType': 'SY12000',
    'interconnectBaySet': 2,
    'redundancyType': 'HighlyAvailable',
    'uplinkSets': [lig_uplink_set],
    'ethernetSettings': ethernet_setting
}

edit_add_uplinkset = {
    'type': 'logical-interconnect-groupV4',
    'enclosureType': 'SY12000',
    'interconnectBaySet': 2,
    'redundancyType': 'HighlyAvailable',
    'uplinkSets': [lig_uplink_set, lig_add_uplinkset]
}

edit_delete_uplinkset = {
    'type': 'logical-interconnect-groupV4',
    'enclosureType': 'SY12000',
    'interconnectBaySet': 2,
    'redundancyType': 'HighlyAvailable',
    'uplinkSets': [lig_uplink_set]
}

edit_edit_uplinkset = {
    'type': 'logical-interconnect-groupV4',
    'enclosureType': 'SY12000',
    'interconnectBaySet': 2,
    'redundancyType': 'HighlyAvailable',
    'uplinkSets': [lig_edit_uplinkset]
}

enc_group = {
    'Enc2-EG': {
        'name': 'Enc2-EG',
        'enclosureCount': 2,
        'interconnectBayMappings':
            [
                {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
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
    'Enc3-EG': {
        'name': 'Enc3-EG',
        'enclosureCount': 3,
        'interconnectBayMappings':
            [
                {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
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
    'Enc2-LE': {
        'name': 'Enc2-LE',
        'enclosureUris': [ENC_1, ENC_2],
        'enclosureGroupUri': 'Enc2-EG',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
    },
    'Enc3-LE': {
        'name': 'Enc3-LE',
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
    }
}

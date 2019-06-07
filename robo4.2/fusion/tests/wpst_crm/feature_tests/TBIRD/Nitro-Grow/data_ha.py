from data_common import *
CONFIG = 'HA'

update_downlink_speed = \
    [
        {
            "op": "replace",
            "path": "/downlinkSpeedMode",
            "value": ["SPEED_25GB"]
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
        {'enclosure': '1', 'bay': '2', 'port': 'Q6', 'speed': 'Auto'},
        {'enclosure': '2', 'bay': '5', 'port': 'Q6', 'speed': 'Auto'}
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
        {'enclosure': '1', 'bay': '2', 'port': 'Q1', 'speed': 'Auto'}
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
        {
            'desiredSpeed': 'Auto',
            'location': {
                'locationEntries': [
                            {
                                'value': 'Q6',
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
}

###
# Interconnect bays configurations
# 2 Enclosures, Fabric 2
###

Enc2Map = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
    ]

###
# Interconnect bays configurations
# 3 Enclosures, Fabric 2
###

Enc3Map = Enc2Map + \
    [
        {'bay': 2, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 5, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]


###
# Interconnect bays configurations
# 4 Enclosures, Fabric 2
###

Enc4Map = Enc3Map + \
    [
        {'bay': 2, 'enclosure': 4, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 5, 'enclosure': 4, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 4}
    ]

###
# Interconnect bays configurations
# 5 Enclosures, Fabric 2
###

Enc5Map = Enc4Map + \
    [

        {'bay': 2, 'enclosure': 5, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 5},
        {'bay': 5, 'enclosure': 5, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 5}
    ]

###
# Logical Interconnect Groups
###
ligs = {
    'Enc2-LIG': {
        'name': 'Enc2-LIG',
        'interconnectMapTemplate': Enc2Map,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 2,
        'redundancyType': 'HighlyAvailable',
        'uplinkSets': [uplink_set_1, uplink_set_2],
    },
    'Enc3-LIG': {
        'name': 'Enc3-LIG',
        'interconnectMapTemplate': Enc3Map,
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 2,
        'redundancyType': 'HighlyAvailable',
        'uplinkSets': [uplink_set_1, uplink_set_2],
    },
    'Enc4-LIG': {
        'name': 'Enc4-LIG',
        'interconnectMapTemplate': Enc4Map,
        'enclosureIndexes': [1, 2, 3, 4],
        'interconnectBaySet': 2,
        'redundancyType': 'HighlyAvailable',
        'uplinkSets': [uplink_set_1, uplink_set_2],
    },
    'Enc5-LIG': {
        'name': 'Enc5-LIG',
        'interconnectMapTemplate': Enc5Map,
        'enclosureIndexes': [1, 2, 3, 4, 5],
        'interconnectBaySet': 2,
        'redundancyType': 'HighlyAvailable',
        'uplinkSets': [uplink_set_1, uplink_set_2],
    }
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
     },
    'Enc4-EG':
    {'name': 'Enc4-EG',
            'enclosureCount': 4,
            'interconnectBayMappings':
            [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
             {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc4-LIG'},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc4-LIG'},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
     },
    'Enc5-EG':
    {'name': 'Enc5-EG',
            'enclosureCount': 5,
            'interconnectBayMappings':
            [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
             {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc5-LIG'},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc5-LIG'},
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
            'serverHardwareUri': ENC_1 + ', bay 3',
            'enclosureUri': ENC_1,
            'connectionSettings': {
                'connections': [
                    {	'name': 'conn1',
                      'functionType': 'Ethernet',
                      'portId': 'Mezz 2:1-a',
                      'networkUri': 'RNS',
                      'lagName': 'LAG1'
                      },
                    {	'name': 'conn2',
                      'functionType': 'Ethernet',
                      'portId': 'Mezz 2:2-a',
                      'networkUri': 'RNS',
                      'lagName': 'LAG1'
                      }
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

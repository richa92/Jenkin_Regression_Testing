from data_common import *

RNS_1000 = 1000
RNS_1001 = 1001
RNS_500 = 500
RNS_501 = 501
RNS_333 = 333
RNS_334 = 334
RNS_250 = 250
RNS_251 = 251
RNS_200 = 200
RNS_201 = 201

invalid_rns = [RNS_1001, RNS_501, RNS_334, RNS_251, RNS_201]
valid_rns = [RNS_1000, RNS_500, RNS_333, RNS_250, RNS_200]

networks = {
    'namePrefix': 'net',
    'privateNetwork': False,
    'smartLink': True,
    'purpose': 'General',
    'type': 'bulk-ethernet-networkV1'
}

ns_dto = {
    'type': 'network-setV4',
    'networkUris': None
}

uplink_set_1 = {
    'name': 'US1',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'lacpTimer': 'Short',
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '2', 'port': 'Q6', 'speed': 'Auto'},
        {'enclosure': '1', 'bay': '5', 'port': 'Q6', 'speed': 'Auto'}
    ]
}

###
# Interconnect bays configurations
# 1 Enclosures, Fabric 2
###

Enc1Map = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

###
# Interconnect bays configurations
# 2 Enclosures, Fabric 2
###

Enc2Map = Enc1Map + \
    [
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
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
    'Enc1-LIG': {
        'name': 'Enc1-LIG',
        'interconnectMapTemplate': Enc1Map,
        'enclosureIndexes': [1],
        'interconnectBaySet': 2,
        'redundancyType': 'Redundant',
        'uplinkSets': [uplink_set_1],
    },
    'Enc2-LIG': {
        'name': 'Enc2-LIG',
        'interconnectMapTemplate': Enc2Map,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 2,
        'redundancyType': 'Redundant',
        'uplinkSets': [uplink_set_1],
    },
    'Enc3-LIG': {
        'name': 'Enc3-LIG',
        'interconnectMapTemplate': Enc3Map,
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 2,
        'redundancyType': 'Redundant',
        'uplinkSets': [uplink_set_1],
    },
    'Enc4-LIG': {
        'name': 'Enc4-LIG',
        'interconnectMapTemplate': Enc4Map,
        'enclosureIndexes': [1, 2, 3, 4],
        'interconnectBaySet': 2,
        'redundancyType': 'Redundant',
        'uplinkSets': [uplink_set_1],
    },
    'Enc5-LIG': {
        'name': 'Enc5-LIG',
        'interconnectMapTemplate': Enc5Map,
        'enclosureIndexes': [1, 2, 3, 4, 5],
        'interconnectBaySet': 2,
        'redundancyType': 'Redundant',
        'uplinkSets': [uplink_set_1],
    }
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

Profile_Negative = {
    'name': 'Profile_Negative',
    'serverHardwareUri': ENC_1 + ', bay 4',
    'enclosureUri': ENC_1,
    'connectionSettings': {
            'connections': [
                {	'name': 'conn',
                  'functionType': 'Ethernet',
                  'portId': 'Auto',
                  }
            ]
    }
}

profiles = {
    'Profile0': {
        'payload': {
            'name': 'Profile0',
            'serverHardwareUri': ENC_1 + ', bay 2',
            'enclosureUri': ENC_1,
            'connectionSettings': {
                'connections': [
                    {	'name': 'conn1',
                      'functionType': 'Ethernet',
                      'portId': 'Mezz 2:1-a',
                      'networkUri': 'RNS_1000',
                      },
                    {	'name': 'conn2',
                      'functionType': 'Ethernet',
                      'portId': 'Mezz 2:1-b',
                      'networkUri': 'LNS2',
                      }
                ]
            }
        },
        'ILO': '15.245.132.174',
    },
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
                      'networkUri': 'LNS',
                      'lagName': 'LAG1'
                      },
                    {	'name': 'conn2',
                      'functionType': 'Ethernet',
                      'portId': 'Mezz 2:2-a',
                      'networkUri': 'LNS',
                      'lagName': 'LAG1'
                      }
                ]
            }
        },
        'ILO': '15.245.132.177',
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
                      'networkUri': 'RNS_200',
                      }
                ]
            }
        },
        'ILO': '15.245.132.234',
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
                      'networkUri': 'LNS',
                      }
                ]
            }
        },
        'ILO': '15.245.132.233',
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
                      'networkUri': 'LNS',
                      }
                ]
            }
        },
        'ILO': '15.245.132.210',
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
                      'networkUri': 'RNS_200',
                      }
                ]
            }
        },
        'ILO': '15.245.132.63',
    }
}

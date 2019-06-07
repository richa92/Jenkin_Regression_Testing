from data_common import *
CONFIG = 'HA'
CXP = 'Mixed'

uplink_set_1 = {
    'name': 'US1',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'lacpTimer': 'Short',
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'}
    ]
}

uplink_set_2 = {
    'name': 'US2',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['net_420', 'net_421', 'net_422'],
    'lacpTimer': 'Short',
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '2', 'bay': '6', 'port': 'Q1', 'speed': 'Auto'}
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
            {'desiredSpeed': 'Auto',
             'location': {
                             'locationEntries': [
                                 {
                                     'value': 'Q6',
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
    ]
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
             }
    ]
}

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
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
    ]
###
# Interconnect bays configurations
# 3 Enclosures, Fabric 3
###
Enc3AMap = Enc2AMap + \
    [
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

Enc3BMap = Enc2BMap + \
    [
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

###
# Interconnect bays configurations
# 4 Enclosures, Fabric 3
###
Enc4AMap = Enc3AMap + \
    [
        {'bay': 3, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4}
    ]

Enc4BMap = Enc3BMap + \
    [
        {'bay': 6, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4}
    ]


###
# Logical Interconnect Groups
###
ligs = {
    'Enc2A-LIG':
    {	'name': 'Enc2A-LIG',
      'interconnectMapTemplate': Enc2AMap,
      'enclosureIndexes': [1, 2],
      'interconnectBaySet': 3,
      'redundancyType': 'NonRedundantASide',
      'uplinkSets': [uplink_set_1],
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
          'uplinkSets': [uplink_set_1],
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
          'uplinkSets': [uplink_set_1],
          },
        'Enc4B-LIG':
        {	'name': 'Enc4B-LIG',
          'interconnectMapTemplate': Enc4BMap,
          'enclosureIndexes': [1, 2, 3, 4],
          'interconnectBaySet': 3,
          'redundancyType': 'NonRedundantBSide',
          'uplinkSets': [uplink_set_2],
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
                      'portId': 'Mezz 3:1-a',
                      'networkUri': 'RNS'
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
    }
}

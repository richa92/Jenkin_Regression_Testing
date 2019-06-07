admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
ethernet_networks1 = [{'name': 'vnet10',
                       'vlanId': 10,
                       'purpose': 'General',
                       'smartLink': True,
                       'privateNetwork': False,
                       'connectionTemplateUri': None,
                       'ethernetNetworkType': 'Tagged'},
                      {'name': 'vnet101',
                       'type': 'ethernet-networkV300',
                       'vlanId': 101,
                       'purpose': 'General',
                       'smartLink': True,
                       'privateNetwork': False,
                       'connectionTemplateUri': None,
                       'ethernetNetworkType': 'Tagged'},
                      ]

uplink_sets = {'uset1':
               {'name': 'uset1',
                'ethernetNetworkType': 'Tagged',
                'networkType': 'Ethernet',
                'networkUris': ['vnet100'],
                'primaryPort': None,
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'},
                                           {'enclosure': '1', 'bay': '3', 'port': 'Q2', 'speed': 'Auto'},
                                           ]},
               'uset2':
               {'name': 'uset2',
                'ethernetNetworkType': 'Tagged',
                'networkType': 'Ethernet',
                'networkUris': ['vnet101'],
                'primaryPort': None,
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q5', 'speed': 'Auto'},
                                           {'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'},
                                           ]},
               }

icmap = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'Synergy 10Gb Interconnect Link Module'},
         {'enclosure': 2, 'enclosureIndex': 2, 'bay': 3, 'type': 'Synergy 10Gb Interconnect Link Module'},
         {'enclosure': 2, 'enclosureIndex': 2, 'bay': 6, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
         {'enclosure': 3, 'enclosureIndex': 3, 'bay': 3, 'type': 'Synergy 10Gb Interconnect Link Module'},
         {'enclosure': 3, 'enclosureIndex': 3, 'bay': 6, 'type': 'Synergy 10Gb Interconnect Link Module'}
         ]

ligx = {'lig1':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'SY12000',
         'enclosureIndexes': [1, 2, 3],
         'interconnectMapTemplate': icmap,
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'uplinkSets': [uplink_sets['uset1'].copy(), uplink_sets['uset2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
        'lig2':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'SY12000',
         'enclosureIndexes': [1, 2, 3],
         'interconnectMapTemplate': icmap,
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'uplinkSets': [uplink_sets['uset1'].copy(), uplink_sets['uset2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
        'lig3':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'SY12000',
         'enclosureIndexes': [1, 2, 3],
         'interconnectMapTemplate': icmap,
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'uplinkSets': [uplink_sets['uset1'].copy(), uplink_sets['uset2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         }
        }

enc_group = {'name': 'encgrp1',
             'type': 'EnclosureGroupV300',
             'enclosureTypeUri': '/rest/enclosure-types/SY12000',
             'stackingMode': 'Enclosure',
             'ipAddressingMode': 'DHCP',
             'interconnectBayMappingCount': 2,
             'enclosureCount': 3,
             'configurationScript': None,
             'interconnectBayMappings':
             [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG1'}
              ]}


enc = {'name': 'logenc1',
       'enclosureUris': ['/rest/enclosures/0000000000A66101', '/rest/enclosures/0000000000A66102', '/rest/enclosures/0000000000A66103'],
       'enclosureGroupUri': 'EG:encgrp1'
       }

profile = {'type': 'ServerProfileV6', 'serverHardwareUri': '/rest/server-hardware/30303437-3034-4D32-3230-313131384752',
           'serverHardwareTypeUri': '/rest/server-hardware-types/5C789023-52E9-4998-A7AE-10C079CCC5EA', 'enclosureUri': '/rest/enclosures/0000000000A66101', 'enclosureGroupUri': 'EG:encgrp1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
           'name': 'profile3', 'description': '', 'affinity': 'Bay',
           'boot': {'manageBoot': False},
           'connections': [{'id': 1, 'name': 'conn1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:vnet100', 'mac': None, 'wwpn': '', 'wwnn': ''},
                           {'id': 2, 'name': 'conn2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:vnet101', 'mac': None, 'wwpn': '', 'wwnn': ''},
                           ]}

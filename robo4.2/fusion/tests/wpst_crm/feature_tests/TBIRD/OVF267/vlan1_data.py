import enclosure_map
import data_variables
import ast


ENC_1 = 'CN7544044G'

ENC_2 = 'CN7545084V'

ENC_3 = ''
ENC_4 = ''
ENC_5 = ''

encl_list = ['ENC:' + ENC_1, 'ENC:' + ENC_2, 'ENC:' + ENC_3, 'ENC:' + ENC_4, 'ENC:' + ENC_5]

CONFIG = 'HA'
CXP = 'CL20'


frame = 2


def rlist(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

taggedNetworks = [{'name': n,
                   'type': 'ethernet-networkV4',
                   'vlanId': int(n[6:]),
                   'purpose': 'General',
                   'smartLink': True,
                   'privateNetwork': False,
                   'ethernetNetworkType': 'Tagged'} for n in rlist(1, 10, 'ether_')]

fcoe_networks = [{'name': 'fcoe-1', 'type': 'fcoe-networkV4', 'vlanId': 1}]

bulk_networks = [{"vlanIdRange": "1-10",
                  "purpose": "General",
                  "namePrefix": "bulk",
                  "smartLink": False,
                  "privateNetwork": False,
                  "bandwidth": {
                      "maximumBandwidth": 10000,
                      "typicalBandwidth": 2000
                  },
                  "type": "bulk-ethernet-networkV1"},
                 ]
bulk_networkList = [x for x in rlist(1, 10, 'bulk_')]

network_sets = [{"name": "ns1",
                 "nativeNetworkUri": 'ether_1',
                 "networkUris": [x for x in rlist(1, 10, 'ether_')],
                 "connectionTemplateUri": None,
                 "type": "network-setV4"
                 },
                {"name": "ns1",
                 "nativeNetworkUri": None,
                 "networkUris": [x for x in rlist(1, 10, 'ether_')],
                 "connectionTemplateUri": None,
                 "type": "network-setV4"
                 },
                {"name": "ns1",
                 "nativeNetworkUri": 'ether_9',
                 "networkUris": [x for x in rlist(2, 10, 'ether_')],
                 "connectionTemplateUri": None,
                 "type": "network-setV4"
                 }
                ]

uplinkSets = [{'name': 'us',
               'ethernetNetworkType': 'Tagged',
               'networkType': 'Ethernet',
               'networkUris': ['ether_1', 'ether_2', 'ether_3', 'ether_4', 'ether_5', 'ether_6', 'ether_7', 'ether_8', 'ether_9', 'ether_10'],
               'lacpTimer': 'Short',
               'mode': 'Auto',
               'nativeNetworkUri': 'ether_1',
               'logicalPortConfigInfos': [
                   {'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'}]
               },
              {'name': 'us',
               'ethernetNetworkType': 'Tagged',
               'networkType': 'Ethernet',
               'networkUris': ['ether_1', 'ether_2', 'ether_3', 'ether_4', 'ether_5', 'ether_6', 'ether_7', 'ether_8', 'ether_9', 'ether_10'],
               'lacpTimer': 'Short',
               'mode': 'Auto',
               'nativeNetworkUri': None,
               'logicalPortConfigInfos': [
                   {'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'}]
               },
              {'name': 'us',
               'ethernetNetworkType': 'Tagged',
               'networkType': 'Ethernet',
               'networkUris': ['ether_2', 'ether_3', 'ether_4', 'ether_5', 'ether_6', 'ether_7', 'ether_8', 'ether_9', 'ether_10'],
               'lacpTimer': 'Short',
               'mode': 'Auto',
               'nativeNetworkUri': None,
               'logicalPortConfigInfos': [
                   {'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'}]
               }]

lig1 = {'name': 'LIG',
        'type': 'logical-interconnect-groupV400',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': 'Enc' + str(frame) + 'Map',
        'enclosureIndexes': [x for x in xrange(1, frame + 1)],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'uplinkSets': [uplinkSets[0]],
        }
lig2 = {'name': 'LIG',
        'type': 'logical-interconnect-groupV400',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': 'Enc' + str(frame) + 'Map',
        'enclosureIndexes': [x for x in xrange(1, frame + 1)],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'uplinkSets': [uplinkSets[1]],
        }
lig3 = {'name': 'LIG',
        'type': 'logical-interconnect-groupV400',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': 'Enc' + str(frame) + 'Map',
        'enclosureIndexes': [x for x in xrange(1, frame + 1)],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'uplinkSets': [uplinkSets[2]],
        }


eg1 = {'name': 'Enc-EG',
       'enclosureCount': frame,
       'configurationScript': None,
       'interconnectBayMappings':
       [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
        {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
           {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG'},
           {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
           {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
           {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG'}],
       'ipAddressingMode': "External",
       'ipRangeUris': [],
       'powerMode': "RedundantPowerSupply"
       }

eg2 = {'name': 'Enc-EG',
       'enclosureCount': frame,
       'configurationScript': None,
       'interconnectBayMappings':
           [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG'},
            {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG'}],
       'ipAddressingMode': "External",
       'ipRangeUris': [],
       'powerMode': "RedundantPowerSupply"
       }

eg3 = {'name': 'Enc-EG',
       'enclosureCount': frame,
       'configurationScript': None,
       'interconnectBayMappings':
           [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG'},
            {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG'}],
       'ipAddressingMode': "External",
       'ipRangeUris': [],
       'powerMode': "RedundantPowerSupply"
       }

eg4 = {'name': 'Enc-EG',
       'enclosureCount': frame,
       'configurationScript': None,
       'interconnectBayMappings':
           [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG'},
            {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG'}],
       'ipAddressingMode': "External",
       'ipRangeUris': [],
       'powerMode': "RedundantPowerSupply"
       }

eg5 = {'name': 'Enc-EG',
       'enclosureCount': frame,
       'configurationScript': None,
       'interconnectBayMappings':
           [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG'},
            {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG'}],
       'ipAddressingMode': "External",
       'ipRangeUris': [],
       'powerMode': "RedundantPowerSupply"
       }

les = [{
    'name': 'LE',
    'enclosureUris': encl_list[0:frame],
    'enclosureGroupUri': 'ENC:Enc-EG',
    'firmwareBaselineUri': None,
    'forceInstallFirmware': False
},
    {
        'name': 'LE',
        'enclosureUris': encl_list[0:frame],
        'enclosureGroupUri': 'ENC:Enc-EG',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
},
    {
        'name': 'LE',
        'enclosureUris': encl_list[0:frame],
        'enclosureGroupUri': 'ENC:Enc-EG',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
},
    {
        'name': 'LE',
        'enclosureUris': encl_list[0:frame],
        'enclosureGroupUri': 'ENC:Enc-EG',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
},
    {
        'name': 'LE',
        'enclosureUris': encl_list[0:frame],
        'enclosureGroupUri': 'ENC:Enc-EG',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
}]

profile = {'type': 'ServerProfileV8',
           'serverHardwareUri': ENC_2 + ', bay 1',
           'serverHardwareTypeUri': None,
           'enclosureUri': ENC_2,
           'enclosureGroupUri': 'Enc-EG',
           'serialNumberType': 'Virtual',
           'macType': 'Virtual',
           'wwnType': 'Virtual',
           'name': 'profile1',
           'description': 'Profile',
           'affinity': 'Bay',
           'connections': [{'id': 1,
                            'name': 'conn1',
                            'functionType': 'Ethernet',
                            'portId': 'Auto',
                            'requestedMbps': '2500',
                            'networkUri': 'ns1',
                            'mac': None,
                            'wwpn': None,
                            'wwnn': None
                            },
                           ]
           }

network_list = ['ether_1']

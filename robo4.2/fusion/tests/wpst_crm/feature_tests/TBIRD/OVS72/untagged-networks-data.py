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


def get_port_name(counter):
    print counter
    port = (counter / 4 + 1)
    subport = ((counter % 4) + 1)
    return "Q" + str(port) + "." + str(subport)


def getPortConfig(vlan, icmList):
    portConfigList = []
    vlan = vlan - 100
    if vlan < 24:
        portconfig = "{ " + \
            "'enclosure': '" + str('1') + "', " + \
            "'bay': '" + icmList[0] + "', " + \
            "'port': '" + get_port_name(vlan % 24) + "', " + \
            "'speed': 'Auto' }"
        return ast.literal_eval(portconfig)
    elif vlan < 48:
        portconfig = "{ " + \
            "'enclosure': '" + '2' + "', " + \
            "'bay': '" + icmList[1] + "', " + \
            "'port': '" + get_port_name(vlan % 24) + "', " + \
            "'speed': 'Auto' }"
        return ast.literal_eval(portconfig)
    else:
        return None


def createUplinkSets(prefix, vlan):
    body = {}
    body['name'] = prefix + str(vlan)
    body['ethernetNetworkType'] = 'Untagged'
    body['networkType'] = 'Ethernet'
    body['lacpTimer'] = 'Short'
    body['mode'] = 'Auto'
    body['nativeNetworkUri'] = None
    body['networkUris'] = ['unta_' + str(vlan)]
    port = getPortConfig(vlan, ['3', '6'])
    if (port):
        body['logicalPortConfigInfos'] = [getPortConfig(vlan, ['3', '6'])]

    return body

taggedNetworks = [{'name': n,
                   'type': 'ethernet-networkV4',
                   'vlanId': int(n[6:]),
                   'purpose': 'General',
                   'smartLink': True,
                   'privateNetwork': False,
                   'ethernetNetworkType': 'Tagged'} for n in rlist(1000, 1010, 'ether_')]

fcnetworks = [{'name': 'fc_net',
               'type': 'fc-networkV4',
               'linkStabilityTime': '30',
               'autoLoginRedistribution': True,
               'fabricType': 'FabricAttach'
               }]

networks = [{'name': n,
             'type': 'ethernet-networkV4',
             'vlanId': int(n[5:]),
             'purpose': 'General',
             'smartLink': True,
             'privateNetwork': False,
             'ethernetNetworkType': 'Untagged'} for n in rlist(100, 233, 'unta_')]

network_129 = [{'name': 'unta_229',
                'type': 'ethernet-networkV4',
                'vlanId': 229,
                'purpose': 'General',
                'smartLink': True,
                'privateNetwork': False,
                'ethernetNetworkType': 'Untagged'}]

uss = [createUplinkSets('us', vlan) for vlan in xrange(100, 200)]

fc_uss = {"networkUris": ["fc_net"],
          "mode": "Auto",
                  "lacpTimer": "Short",
                  "primaryPort": None,
                  "logicalPortConfigInfos": [],
                  "networkType": "FibreChannel",
                  "ethernetNetworkType": None,
                  "name": "usfc"}

li_add_us = {'name': 'us201',
             'ethernetNetworkType': 'Untagged',
             'networkType': 'Ethernet',
             'networkUris': ['unta_231'],
             'fcNetworkUris': [],
             'fcoeNetworkUris': [],
             'lacpTimer': 'Short',
             'logicalInterconnectUri': None,
             'primaryPortLocation': None,
             'manualLoginRedistributionState': 'NotSupported',
             'connectionMode': 'Auto',
             'nativeNetworkUri': None,
             'portConfigInfos': []
             }


lig1_red = {
    'LIG1': {'name': 'LIG1',
             'type': 'logical-interconnect-groupV400',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': 'Enc' + str(frame) + 'Map',
             'enclosureIndexes': [x for x in xrange(1, frame + 1)],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': uss,
             }}
Enc3MapRedundant = [
    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
    {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
    {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}
]

Enc3MapBay2 = [
    {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 5, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
    {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
    {'bay': 2, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
    {'bay': 2, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
    {'bay': 5, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}
]
Enc2MapAside = [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}, {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2}]

Enc2MapBside = [{'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1}, {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}]

lig1_nored = {
    'LIG1': {'name': 'LIG1',
             'type': 'logical-interconnect-groupV400',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}, {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2}],
             'enclosureIndexes': [x for x in xrange(1, frame + 1)],
             'interconnectBaySet': 3,
             'redundancyType': 'NonRedundantASide',
             'uplinkSets': [uss[0], uss[1]],
             }}

lig2_nored = {
    'LIG2': {'name': 'LIG2',
             'type': 'logical-interconnect-groupV400',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': [{'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1}, {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}],
             'enclosureIndexes': [x for x in xrange(1, frame + 1)],
             'interconnectBaySet': 3,
             'redundancyType': 'NonRedundantBSide',
             'uplinkSets': [uss[x - 100] for x in xrange(130, 142)],
             }}

lig1_fc = {
    'LIG1': {'name': 'LIG1',
             'type': 'logical-interconnect-groupV400',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': 'Enc' + str(frame) + 'Map',
             'enclosureIndexes': [x for x in xrange(1, frame + 1)],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [fc_uss, uss[0], uss[1]],
             }}

eg_red = [
    {'name': 'Enc-EG',
     'ambientTemperatureMode': 'Standard',
     'enclosureCount': frame,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG1'}],
     'ipAddressingMode': "External",
     'ipRangeUris': [],
     'powerMode': "RedundantPowerSupply"
     },
    {'name': 'Enc-EG',
     'ambientTemperatureMode': 'Standard',
     'enclosureCount': frame,
     'interconnectBayMappings':
         [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
          {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
          {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
          {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
          {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
          {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG1'}],
     'ipAddressingMode': "External",
     'ipRangeUris': [],
     'powerMode': "RedundantPowerSupply"
     },
    {'name': 'Enc-EG',
     'ambientTemperatureMode': 'Standard',
     'enclosureCount': frame,
     'interconnectBayMappings':
         [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
          {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
          {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
          {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
          {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
          {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG1'}],
     'ipAddressingMode': "External",
     'ipRangeUris': [],
     'powerMode': "RedundantPowerSupply"
     }
]


eg_nored = [
    {'name': 'Enc-EG',
     'ambientTemperatureMode': 'Standard',
     'enclosureCount': frame,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG2'}],
     'ipAddressingMode': "External",
     'ipRangeUris': [],
     'powerMode': "RedundantPowerSupply"
     }]

les = [{
    'name': 'LE',
    'enclosureUris': encl_list[0:frame],
    'enclosureGroupUri': 'ENC:Enc-EG',
    'firmwareBaselineUri': None,
    'forceInstallFirmware': False,
},
    {
        'name': 'LE',
        'enclosureUris': encl_list[0:frame],
        'enclosureGroupUri': 'ENC:Enc-EG',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False,
},
    {
        'name': 'LE',
        'enclosureUris': encl_list[0:frame],
        'enclosureGroupUri': 'ENC:Enc-EG',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False,
},
    {
        'name': 'LE',
        'enclosureUris': encl_list[0:frame],
        'enclosureGroupUri': 'ENC:Enc-EG',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False,
}]

updated_internal_network_list = ['unta_229']
vlan_reserved_pools = [{
    'start': 1,
    'length': 129,
    'type': 'vlan-pool'
},
    {
    'start': 1,
    'length': 59,
    'type': 'vlan-pool'
},
    {
    'start': 1,
    'length': 60,
    'type': 'vlan-pool'
},
    {
    'start': 3967,
    'length': 100,
    'type': 'vlan-pool'
},
    {
    'start': 3967,
    'length': 98,
    'type': 'vlan-pool'
}]

import copy


def rlist(start, end, prefix='net_', suffix='', step=1):
    L = []
    for x in xrange(start, end + 1, step):
        L.append('%s%s%s' % (prefix, str(x), suffix))
    return L


def deep_copy(obj):
    return copy.deepcopy(obj)


admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

icmap = [{'bay': 3, 'enclosure': 1, 'type': 'Mellanox SH2200 TAA Switch Module for Synergy',
          'enclosureIndex': 1},
         {'bay': 6, 'enclosure': 1, 'type': 'Mellanox SH2200 TAA Switch Module for Synergy',
          'enclosureIndex': 1},
         ]

lig = {'name': 'CarbonLIG',
       'type': 'logical-interconnect-groupV300',
       'enclosureType': 'SY12000',
       'interconnectMapTemplate': [
           {'enclosure': -1, 'enclosureIndex': -1, 'bay': 1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy'},
           {'enclosure': -1, 'enclosureIndex': -1, 'bay': 4, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy'}],
       'enclosureIndexes': [-1],
       'interconnectBaySet': 1,
       'redundancyType': 'Redundant',
       'fcoeSettings': {'fcoeMode': 'FcfNpv'},
       'uplinkSets': [{'name': 'us1',
                       'ethernetNetworkType': 'NotApplicable',
                       'networkType': 'FibreChannel',
                       # 'networkUris': ['fcoe-1001'],
                       'networkUris': ['SAN-A'],
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'lacpTimer': 'Long',
                       'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '1', 'port': 'Q1.1', 'speed': 'Auto'},
                                                  ]}, ],
       'stackingMode': 'Enclosure',
       'ethernetSettings': None,
       'state': 'Active',
       'telemetryConfiguration': None,
       'snmpConfiguration': None}

ligs = [{'name': 'mellanox-lig',
         'type': 'logical-interconnect-groupV6',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'Redundant',
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'uplinkSets': [{'name': 'us1',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['net_100'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'lacpTimer': 'Long',
                         'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Speed100G'},
                                                    ]}, ],
         }]

"""
lig = {'name': 'LIG1',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap,
         'enclosureIndexes': [1, 2],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'fcoeSettings': {'fcoeMode': 'FcfNpv'},
         'uplinkSets': [],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None}
"""

"""
class Data(object):
    class API500(object):

        x = {'userName': 'Administrator', 'password': '500'}

    class API600(object):
        x = {'userName': 'Administrator', 'password': '600'}

class API500(object):
    x = {'userName': 'Administrator', 'password': '500'}


class API600(object):
    x = {'userName': 'Administrator', 'password': '600'}
"""

xtype = {'500': {'/rest/ethernet_networks': {'type': 'ethernet-networkV300',
                                             'purpose': 'General',
                                             'thing': 1},
                 '/rest/fc_networks': {'type': 'fcoe-networkV300'}
                 },
         '600': {'/rest/ethernet_networks': {'type': 'ethernet-networkV4'},
                 '/rest/fc_networks': {'type': 'fcoe-networkV400'}
                 }
         }

fcoe_networks = [{'name': n,
                  'type': 'fcoe-networkV300',
                  'vlanId': int(n[5:])} for n in rlist(1001, 1256, 'fcoe_')]

fcoe_networks600 = [{'name': n,
                     'type': 'fcoe-networkV600',
                     'vlanId': int(n[5:])} for n in rlist(1001, 1256, 'fcoe_')]

fc_networks = [{'type': 'fc-networkV300',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': '%s' % n,
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'} for n in rlist(1, 6, 'fc_fa_')]


def fix(resource, dto, api):
    if isinstance(dto, dict):
        for k, v in xtype[api][resource].items():
            dto[k] = v
    return dto


b = {'name': 'untaggednetwork2',
     'type': 'ethernet-networkV222',
     'vlanId': None,
     'purpose': 'NOT-General'}

x = fix('/rest/ethernet_networks', b, '500')
pass


class API500(object):
    x = {'userName': 'Administrator', 'password': '500'}


class API600(object):
    x = {'userName': 'Administrator', 'password': '600'}

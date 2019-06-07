from copy import deepcopy


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


def rlist(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

eth_network = [{'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'name': 'eth_401', 'privateNetwork': False, 'purpose': 'General', 'smartLink': True, 'vlanId': 401},
               {'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'name': 'network-a', 'privateNetwork': False, 'purpose': 'General', 'smartLink': True, 'vlanId': 201},
               {'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'name': 'network-b', 'privateNetwork': False, 'purpose': 'General', 'smartLink': True, 'vlanId': 202},
               {'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'name': 'network-c', 'privateNetwork': False, 'purpose': 'General', 'smartLink': True, 'vlanId': 203}
               ]

ethernet_networks = [{'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'name': 'eth-100', 'privateNetwork': False, 'purpose': 'General', 'smartLink': True, 'vlanId': 100},
                     {'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'name': 'eth-101', 'privateNetwork': False, 'purpose': 'General', 'smartLink': True, 'vlanId': 101},
                     {'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'name': 'eth-102', 'privateNetwork': False, 'purpose': 'General', 'smartLink': True, 'vlanId': 102},
                     {'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'name': 'network-a', 'privateNetwork': False, 'purpose': 'General', 'smartLink': True, 'vlanId': 200},
                     {'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'name': 'network-b', 'privateNetwork': False, 'purpose': 'General', 'smartLink': True, 'vlanId': 201},
                     {'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'name': 'network-d', 'privateNetwork': False, 'purpose': 'General', 'smartLink': True, 'vlanId': 203},
                     {'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'name': 'eth_401', 'privateNetwork': False, 'purpose': 'General', 'smartLink': True, 'vlanId': 401}]

fc_network = [{'type': 'fc-networkV4', 'name': 'FC_1', 'fabricType': 'FabricAttach', 'linkStabilityTime': 30, 'autoLoginRedistribution': True}]

fcoe_1 = [{'name': 'fcoe-1', 'type': 'fcoe-networkV4', 'vlanId': 1}]
fcoe_100 = [{'name': 'fcoe-100', 'type': 'fcoe-networkV4', 'vlanId': 100}]
fcoe_100b = [{'name': 'fcoe-100b', 'type': 'fcoe-networkV4', 'vlanId': 100}]
no_vlanId = [{'name': 'no-vlanId', 'type': 'fcoe-networkV4'}]
fcoe_enet = [{'name': 'eth_401', 'type': 'fcoe-networkV4', 'vlanId': 209}]
fcoe_fc = [{'name': 'FC_1', 'type': 'fcoe-networkV4', 'vlanId': 210}]
fcoe_4095 = [{'name': 'fcoe-4095', 'type': 'fcoe-networkV4', 'vlanId': 4095}]
fcoe_BFS = [[{'name': 'fcoe-1002', 'type': 'fcoe-networkV4', 'vlanId': 1002}],
            [{'name': 'fcoe-1003', 'type': 'fcoe-networkV4', 'vlanId': 1003}]]

fcoe_networks = {'fcoe-1': {'name': 'fcoe-1', 'type': 'fcoe-networkV4', 'vlanId': 1},
                 'fcoe-100': {'name': 'fcoe-100', 'type': 'fcoe-networkV4', 'vlanId': 100},
                 'fcoe-2000': {'name': 'fcoe-2000', 'type': 'fcoe-networkV4', 'vlanId': 2000},
                 'fcoe-100b': {'name': 'fcoe-100b', 'type': 'fcoe-networkV4', 'vlanId': 100},
                 'fcnetwork-a': {'name': 'fcnetwork-a', 'type': 'fcoe-networkV4', 'vlanId': 209},
                 'network-a': {'name': 'network-a', 'type': 'fcoe-networkV4', 'vlanId': 210},
                 'network-b': {'name': 'network-b', 'type': 'fcoe-networkV4', 'vlanId': 211},
                 'no-vlanId': {'name': 'no-vlanId', 'type': 'fcoe-networkV4'},
                 'fcoe-4095': {'name': 'fcoe-4095', 'type': 'fcoe-networkV4', 'vlanId': 4095}}


fcoe_ranges = {'fcoe-range32a': {'prefix': 'fcoe-', 'suffix': 'a', 'start': 1001, 'end': 1032},
               'fcoe-range32b': {'prefix': 'fcoe-', 'suffix': 'b', 'start': 1001, 'end': 1032},
               'fcoe-range32c': {'prefix': 'fcoe-', 'suffix': 'c', 'start': 1001, 'end': 1032},
               'fcoe-range32d': {'prefix': 'fcoe-', 'suffix': 'd', 'start': 1001, 'end': 1032},
               'fcoe-range33': {'prefix': 'fcoe-', 'suffix': '', 'start': 1001, 'end': 1033},
               'fcoe-range30a': {'prefix': 'fcoe-', 'suffix': 'a', 'start': 1001, 'end': 1030},
               'fcoe-range128': {'prefix': 'fcoe-', 'suffix': '', 'start': 1001, 'end': 1128},
               'fcoe-range-delete-20': {'prefix': 'fcoe-', 'suffix': '', 'start': 1109, 'end': 1128}
               }
network_sets = [{'name': 'netset1', 'type': 'network-setV4', 'networkUris': ['network-a'], 'nativeNetworkUri': None},
                {'name': 'VlanTrunk1', 'type': 'network-setV4', 'networkUris': rlist(2, 163), 'nativeNetworkUri': None},
                ]


################################################################################################
#                                Variables for Nitro Hardware
# ##############################################################################################

LIG_Aside = 'LIG_Aside'
LIG_Bside = 'LIG_Bside'
LIG_HAside = 'LIG_HAside'
LIGAside = 'LIG_Aside'
LIGBside = 'LIG_Bside'

frame = 2
IBS = 3
LIG_FcoE_UPLINKS = ['Q2']

ENC_1 = 'CN75016BG8'
ENC_2 = 'CN750202SK'
ENC_3 = 'CN754406WT'
ENC_4 = ''
ENC_5 = ''

ENC_List = ['ENC:' + ENC_1, 'ENC:' + ENC_2, 'ENC:' + ENC_3, 'ENC:' + ENC_4, 'ENC:' + ENC_5]
ENC1ICBAY3 = 'CN75016BG8, interconnect 3'
ENCs = [ENC_1, ENC_2]


###
# Interconnect bays configurations
# 1 Enclosures, Fabric 3
###

Enc1Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

Enc1MapASide =\
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

Enc1MapBSide = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

###
# Interconnect bays configurations
# 2 Enclosures, Fabric 3
###

Enc2Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]

Enc2MapASide = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
    ]

Enc2MapBSide = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]


###
# Interconnect bays configurations
# 3 Enclosures, Fabric 3
###

Enc3bay3ICMMap = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]


Enc3MapASide = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}

    ]

Enc3MapBSide = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

###
# Interconnect bays configurations
# 4 Enclosures, Fabric 3
###

Enc4Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
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
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 3, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 6, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 3, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5},
        {'bay': 6, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5}
    ]

uplink_sets = {
    'US1': {
        'name': 'US1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe-1002', 'eth-101'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'}
                                   ]
    },
    'US2': {
        'name': 'US2',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe-1003', 'eth-102'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}
                                   ]
    },
    'US4': {
        'name': 'US4',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe-100', 'fcoe-1003', 'eth-102'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}
                                   ]
    },

    'US33_max': {
        'name': 'us-33-exceeds-32max',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(1004, 1037, 'fcoe-'),
        'primaryPort': None,
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'},
                                   {'enclosure': '1', 'bay': '3', 'port': 'Q2', 'speed': 'Auto'},
                                   {'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
                                   {'enclosure': '1', 'bay': '3', 'port': 'Q4', 'speed': 'Auto'}
                                   ]
    },
    'US_fcoe': {
        'name': 'us3',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe-1002'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'}]
    },
    'US_fcoe1': {
        'name': 'us4',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe-1003'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}]
    },
    'us-32fcoe-a': {
        'name': 'us-32fcoe-a',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(1040, 1071, 'fcoe-', ''),
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q5', 'speed': 'Auto'},
                                   {'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'}
                                   ]
    },
    'us-32fcoe-b': {
        'name': 'us-32fcoe-b',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(1072, 1103, 'fcoe-', ''),
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q5', 'speed': 'Auto'},
                                   {'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}
                                   ]
    },
    'us1-fcoe': {
        'name': 'us1-fcoe',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe-1032c'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
                                   {'enclosure': '1', 'bay': '3', 'port': 'Q4', 'speed': 'Auto'}
                                   ]
    },
    'duplicate-vlan': {
        'name': 'duplicate-vlan',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe-1032', 'fcoe-1032a'],
        'primaryPort': None,
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}
                                   ]
    },
    'duplicate-vlan-eth': {
        'name': 'duplicate-vlan',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth-100', 'fcoe-100'],
        'primaryPort': None,
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}
                                   ]
    },
    'us33a': {
        'name': 'us-33-exceeds-32max',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(1039, 1071, 'fcoe-'),
        'primaryPort': None,
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'}
                                   ]
    },
    'us-eth': {
        'name': 'us-eth',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['network-b'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q4', 'speed': 'Auto'},
                                   ]
    },
    'us_fcoe_multiple_ic': {
        'name': 'us-spans-multiple-ICMs',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(1037, 1038, 'fcoe-'),
        'primaryPort': None,
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'},
                                   {'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}
                                   ]
    },
    'US1_no_ports': {
        'name': 'US1_no_ports',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth-101', 'fcoe-1002'],
        'primaryPort': None,
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'logicalPortConfigInfos': []
    },
    'US2_no_ports': {
        'name': 'US2_no_ports',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth-102', 'fcoe-1003'],
        'primaryPort': None,
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'logicalPortConfigInfos': []
    },
    'US1_no_fcoe_nw': {
        'name': 'US1_no_fcoe_nw',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth-101'],
        'primaryPort': None,
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'}]
    },
    'US2_no_fcoe_nw': {
        'name': 'US2_no_fcoe_nw',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth-102'],
        'primaryPort': None,
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}]
    },
    'us_fcoe_Enet1': {
        'name': 'us3',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(1040, 1071, 'fcoe-', '') + ['network-a'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'}]
    },
    'us_fcoe_Enet2': {
        'name': 'us',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe-1003', 'eth-102'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}]
    }

}

if frame == 1:
    REDUNDANCY = 'Redundant'
elif frame == 2:
    REDUNDANCY = 'HighlyAvailable'

LIG = 'LIG' + '_' + REDUNDANCY
EG = 'EG'
LE = 'LE'

EG_AB = 'EG-1'

LE_HA = 'LE_HA'
LI_Aside = [{'name': LE + '-' + LIGAside}, {'name': LE + '-' + LIGBside}]
LI = {'name': LE + '-' + LIG}


ligs = {
    'LIG':
    {'name': LIG,
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': Enc2Map,
     'enclosureIndexes': [x for x in xrange(1, frame + 1)],
     'interconnectBaySet': IBS,
     'redundancyType': REDUNDANCY,
     'uplinkSets': [deepcopy(uplink_sets['US1']), deepcopy(uplink_sets['US2'])],
     'downlinkSpeedMode': 'SPEED_10GB'
     },
        'LIG1':
            {'name': LIG,
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc2Map,
             'enclosureIndexes': [x for x in xrange(1, frame + 1)],
             'interconnectBaySet': IBS,
             'redundancyType': REDUNDANCY,
             'uplinkSets': [deepcopy(uplink_sets['US1']), deepcopy(uplink_sets['US4'])],
             'downlinkSpeedMode': 'SPEED_10GB'
             },
        'LIGAside':
            {'name': LIGAside,
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc2MapASide,
             'enclosureIndexes': [x for x in xrange(1, frame + 1)],
             'interconnectBaySet': 3,
             'redundancyType': 'NonRedundantASide',
             'uplinkSets': [deepcopy(uplink_sets['US1'])],
             'downlinkSpeedMode': 'SPEED_10GB'
             },
        'LIGBside':
            {'name': LIGBside,
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc2MapBSide,
             'enclosureIndexes': [x for x in xrange(1, frame + 1)],
             'interconnectBaySet': 3,
             'redundancyType': 'NonRedundantBSide',
             'uplinkSets': [deepcopy(uplink_sets['US2'])],
             'downlinkSpeedMode': 'SPEED_10GB'
             },
        'LIG_with_us_fcoe_enet':
            {'name': LIG,
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc2Map,
             'enclosureIndexes': [x for x in xrange(1, frame + 1)],
             'interconnectBaySet': 3,
             'redundancyType': REDUNDANCY,
             'uplinkSets': [deepcopy(uplink_sets['us_fcoe_Enet1'])],
             'downlinkSpeedMode': 'SPEED_10GB'
             },
        'LIG_with_us_only_enet':
            {'name': LIG,
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc2Map,
             'enclosureIndexes': [x for x in xrange(1, frame + 1)],
             'interconnectBaySet': 3,
             'redundancyType': REDUNDANCY,
             'uplinkSets': [deepcopy(uplink_sets['us_fcoe_Enet1']), deepcopy(uplink_sets['us-eth'])],
             'downlinkSpeedMode': 'SPEED_10GB'

             }
}


ligs_remove_add_uplinkport = [[{'name': LIG,
                                'enclosureType': 'SY12000',
                                'interconnectMapTemplate': Enc2Map,
                                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                                'interconnectBaySet': 3,
                                'redundancyType': REDUNDANCY,
                                'uplinkSets': [deepcopy(uplink_sets['US1_no_ports']), deepcopy(uplink_sets['US2'])],
                                'downlinkSpeedMode': 'SPEED_10GB'
                                }],
                              [{'name': LIG,
                                'enclosureType': 'SY12000',
                                'interconnectMapTemplate': Enc2Map,
                                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                                'interconnectBaySet': 3,
                                'redundancyType': REDUNDANCY,
                                'uplinkSets': [deepcopy(uplink_sets['US1']), deepcopy(uplink_sets['US2_no_ports'])],
                                  'downlinkSpeedMode': 'SPEED_10GB'
                                }]
                              ]

ligs_remove_add_network_in_US = [[
    {'name': LIG,
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': Enc2Map,
     'enclosureIndexes': [x for x in xrange(1, frame + 1)],
     'interconnectBaySet': 3,
     'redundancyType': REDUNDANCY,
     'uplinkSets': [deepcopy(uplink_sets['US1_no_fcoe_nw']), deepcopy(uplink_sets['US2'])],
     'downlinkSpeedMode': 'SPEED_10GB'
     }],
    [{'name': LIG,
      'enclosureType': 'SY12000',
      'interconnectMapTemplate': Enc2Map,
      'enclosureIndexes': [x for x in xrange(1, frame + 1)],
      'interconnectBaySet': 3,
      'redundancyType': REDUNDANCY,
      'uplinkSets': [deepcopy(uplink_sets['US1']), deepcopy(uplink_sets['US2_no_fcoe_nw'])],
      'downlinkSpeedMode': 'SPEED_10GB'
      }]
]

ligs_neg = {'LIG_max_us33': {'name': LIG,
                             'enclosureType': 'SY12000',
                             'interconnectMapTemplate': Enc2Map,
                             'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                             'interconnectBaySet': IBS,
                             'redundancyType': REDUNDANCY,
                             'uplinkSets': [deepcopy(uplink_sets['US33_max'])],
                             'downlinkSpeedMode': 'SPEED_10GB'
                             },
            'LIG-with-more-than-64-fcoe': {'name': 'LIG-with-more-than-64-fcoe',
                                           'enclosureType': 'SY12000',
                                           'interconnectMapTemplate': Enc2Map,
                                           'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                                           'interconnectBaySet': IBS,
                                           'redundancyType': REDUNDANCY,
                                           'uplinkSets': [deepcopy(uplink_sets['us-32fcoe-a']), deepcopy(uplink_sets['us-32fcoe-b']),
                                                          deepcopy(uplink_sets['us1-fcoe'])],
                                           'downlinkSpeedMode': 'SPEED_10GB'
                                           },
            'duplicate-vlans': {'name': 'duplicate-vlans',
                                'enclosureType': 'SY12000',
                                'interconnectMapTemplate': Enc2Map,
                                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                                'interconnectBaySet': IBS,
                                'redundancyType': REDUNDANCY,
                                'uplinkSets': [deepcopy(uplink_sets['duplicate-vlan'])],
                                'downlinkSpeedMode': 'SPEED_10GB'
                                },
            'Invalid-LIG': {'name': 'Invalid-LIG',
                            'enclosureType': 'SY12000',
                            'interconnectMapTemplate': Enc2Map,
                            'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                            'interconnectBaySet': IBS,
                            'redundancyType': REDUNDANCY,
                            'uplinkSets': [deepcopy(uplink_sets['duplicate-vlan-eth'])],
                            'downlinkSpeedMode': 'SPEED_10GB'
                            },
            'LIG_with_us_only_32_fcoe': {'name': LIG,
                                         'enclosureType': 'SY12000',
                                         'interconnectMapTemplate': Enc2Map,
                                         'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                                         'interconnectBaySet': IBS,
                                         'redundancyType': REDUNDANCY,
                                         'uplinkSets': [deepcopy(uplink_sets['us-32fcoe-a'])],
                                         'downlinkSpeedMode': 'SPEED_10GB'
                                         },
            'LIG-with-US-with-more-than-32-fcoe': {'name': LIG,
                                                   'enclosureType': 'SY12000',
                                                   'interconnectMapTemplate': Enc2Map,
                                                   'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                                                   'interconnectBaySet': IBS,
                                                   'redundancyType': REDUNDANCY,
                                                   'uplinkSets': [deepcopy(uplink_sets['us33a'])],
                                                   'downlinkSpeedMode': 'SPEED_10GB'
                                                   },
            'LIG_with_fcoe_us_multiplie_ic': {'name': 'LIG_with_fcoe_us_multiplie_ic',
                                              'enclosureType': 'SY12000',
                                              'interconnectMapTemplate': Enc2Map,
                                              'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                                              'interconnectBaySet': IBS,
                                              'redundancyType': REDUNDANCY,
                                              'uplinkSets': [deepcopy(uplink_sets['us_fcoe_multiple_ic'])],
                                              'downlinkSpeedMode': 'SPEED_10GB'
                                              }
            }


li_uplink_sets = {'US1': {'name': 'US1',
                          'ethernetNetworkType': 'Tagged',
                          'networkType': 'Ethernet',
                          'networkUris': ['eth-101'],
                          'fcNetworkUris': [],
                          'fcoeNetworkUris': ['fcoe-1002'],
                          'lacpTimer': 'Short',
                          'logicalInterconnectUri': None,
                          'primaryPortLocation': None,
                          'manualLoginRedistributionState': 'NotSupported',
                          'connectionMode': 'Auto',
                          'nativeNetworkUri': None,
                          'portConfigInfos': [{'bay': '3', 'port': 'Q6', 'desiredSpeed': 'Auto', 'enclosure': ENC_1}]},
                  'US2': {'name': 'US2',
                          'ethernetNetworkType': 'Tagged',
                          'networkType': 'Ethernet',
                          'networkUris': ['eth-102'],
                          'fcNetworkUris': [],
                          'fcoeNetworkUris': ['fcoe-1003'],
                          'lacpTimer': 'Short',
                          'logicalInterconnectUri': None,
                          'primaryPortLocation': None,
                          'manualLoginRedistributionState': 'NotSupported',
                          'connectionMode': 'Auto',
                          'nativeNetworkUri': None,
                          'portConfigInfos': [{'bay': '3', 'port': 'Q6', 'desiredSpeed': 'Auto', 'enclosure': ENC_1}]},
                  'us1_32fcoe': {'name': 'us1_32fcoe',
                                 'ethernetNetworkType': 'Tagged',
                                 'networkType': 'Ethernet',
                                 'networkUris': [],
                                 'fcNetworkUris': [],
                                 'fcoeNetworkUris': make_range_list(1033, 1064, 'fcoe-'),
                                 'lacpTimer': 'Short',
                                 'logicalInterconnectUri': None,
                                 'primaryPortLocation': None,
                                 'manualLoginRedistributionState': 'NotSupported',
                                 'connectionMode': 'Auto',
                                 'nativeNetworkUri': None,
                                 'portConfigInfos': [{'bay': '3', 'port': 'Q6', 'desiredSpeed': 'Auto', 'enclosure': ENC_1}]},
                  'us_1_fcoe': {'name': 'us-1-fcoe',
                                'ethernetNetworkType': 'Tagged',
                                'networkType': 'Ethernet',
                                'networkUris': [],
                                'fcNetworkUris': [],
                                'fcoeNetworkUris': ['fcoe-100'],
                                'lacpTimer': 'Short',
                                'logicalInterconnectUri': None,
                                'primaryPortLocation': None,
                                'manualLoginRedistributionState': 'NotSupported',
                                'connectionMode': 'Auto',
                                'nativeNetworkUri': None,
                                'portConfigInfos': [{'bay': '3', 'port': 'Q5', 'desiredSpeed': 'Auto', 'enclosure': ENC_1}]},
                  'us1_33fcoe': {'name': 'us1_33fcoe',
                                 'ethernetNetworkType': 'Tagged',
                                 'networkType': 'Ethernet',
                                 'networkUris': [],
                                 'fcNetworkUris': [],
                                 'fcoeNetworkUris': make_range_list(1033, 1064, 'fcoe-') + ['fcoe-100'],
                                 'lacpTimer': 'Short',
                                 'logicalInterconnectUri': None,
                                 'primaryPortLocation': None,
                                 'manualLoginRedistributionState': 'NotSupported',
                                 'connectionMode': 'Auto',
                                 'nativeNetworkUri': None,
                                 'portConfigInfos': [{'bay': '3', 'port': 'Q4', 'desiredSpeed': 'Auto', 'enclosure': ENC_1}]},
                  'us1_remove_uplink_port': {'name': 'us1_32fcoe',
                                             'ethernetNetworkType': 'Tagged',
                                             'networkType': 'Ethernet',
                                             'networkUris': [],
                                             'fcNetworkUris': [],
                                             'fcoeNetworkUris': make_range_list(1033, 1064, 'fcoe-'),
                                             'lacpTimer': 'Short',
                                             'logicalInterconnectUri': None,
                                             'primaryPortLocation': None,
                                             'manualLoginRedistributionState': 'NotSupported',
                                             'connectionMode': 'Auto',
                                             'nativeNetworkUri': None,
                                             'portConfigInfos': []},
                  'us_spans_2_ics': {'name': 'us-spans-2-ics',
                                     'ethernetNetworkType': 'Tagged',
                                     'networkType': 'Ethernet',
                                     'networkUris': [],
                                     'fcNetworkUris': [],
                                     'fcoeNetworkUris': ['fcoe-1108'],
                                     'lacpTimer': 'Short',
                                     'logicalInterconnectUri': None,
                                     'primaryPortLocation': None,
                                     'manualLoginRedistributionState': 'NotSupported',
                                     'connectionMode': 'Auto',
                                     'nativeNetworkUri': None,
                                     'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': 'Q5', 'desiredSpeed': 'Auto'},
                                                         {'enclosure': ENC_2, 'bay': '6', 'port': 'Q1', 'desiredSpeed': 'Auto'}]},
                  'us_dup_vlanId': {'name': 'us-dup-vlanId',
                                    'ethernetNetworkType': 'Tagged',
                                    'networkType': 'Ethernet',
                                    'networkUris': ['eth-100'],
                                    'fcNetworkUris': [],
                                    'fcoeNetworkUris': ['fcoe-100'],
                                    'lacpTimer': 'Short',
                                    'logicalInterconnectUri': None,
                                    'primaryPortLocation': None,
                                    'manualLoginRedistributionState': 'NotSupported',
                                    'connectionMode': 'Auto',
                                    'nativeNetworkUri': None,
                                    'portConfigInfos': [
                                        {'enclosure': ENC_2, 'bay': '6', 'port': 'Q1', 'desiredSpeed': 'Auto'}]},
                  'us-eth': {'name': 'us-eth',
                             'ethernetNetworkType': 'Tagged',
                             'networkType': 'Ethernet',
                             'networkUris': ['network-d'],
                             'fcNetworkUris': [],
                             'fcoeNetworkUris': [],
                             'lacpTimer': 'Short',
                             'logicalInterconnectUri': None,
                             'primaryPortLocation': None,
                             'manualLoginRedistributionState': 'NotSupported',
                             'connectionMode': 'Auto',
                             'nativeNetworkUri': None,
                             'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': 'Q1', 'desiredSpeed': 'Auto'},
                                                 {'enclosure': ENC_2, 'bay': '6', 'port': 'Q1', 'desiredSpeed': 'Auto'}]},
                  'US_FcoE_enet1': {'name': 'US_FcoE_enet1',
                                    'ethernetNetworkType': 'Tagged',
                                    'networkType': 'Ethernet',
                                    'networkUris': ['eth-101', 'network-a'],
                                    'fcNetworkUris': [],
                                    'fcoeNetworkUris': ['fcoe-1002'],
                                    'lacpTimer': 'Short',
                                    'logicalInterconnectUri': None,
                                    'primaryPortLocation': None,
                                    'manualLoginRedistributionState': 'NotSupported',
                                    'connectionMode': 'Auto',
                                    'nativeNetworkUri': None,
                                    'portConfigInfos': [
                                        {'enclosure': ENC_1, 'bay': '3', 'port': 'Q6', 'desiredSpeed': 'Auto'}]},
                  'US_FcoE_enet2': {'name': 'US_FcoE_enet2',
                                    'ethernetNetworkType': 'Tagged',
                                    'networkType': 'Ethernet',
                                    'networkUris': ['eth-102', 'network-b'],
                                    'fcNetworkUris': [],
                                    'fcoeNetworkUris': ['fcoe-1003'],
                                    'lacpTimer': 'Short',
                                    'logicalInterconnectUri': None,
                                    'primaryPortLocation': None,
                                    'manualLoginRedistributionState': 'NotSupported',
                                    'connectionMode': 'Auto',
                                    'nativeNetworkUri': None,
                                    'portConfigInfos': [
                                        {'enclosure': ENC_2, 'bay': '6', 'port': 'Q6', 'desiredSpeed': 'Auto'}]},
                  'us-33-fcoe': {'name': 'us-33-fcoe',
                                 'ethernetNetworkType': 'Tagged',
                                 'networkType': 'Ethernet',
                                 'networkUris': [],
                                 'fcNetworkUris': [],
                                 'fcoeNetworkUris': make_range_list(1031, 1063, 'fcoe-'),
                                 'lacpTimer': 'Short',
                                 'logicalInterconnectUri': None,
                                 'primaryPortLocation': None,
                                 'manualLoginRedistributionState': 'NotSupported',
                                 'connectionMode': 'Auto',
                                 'nativeNetworkUri': None,
                                 'portConfigInfos': [
                                     {'enclosure': ENC_2, 'bay': '6', 'port': 'Q4', 'desiredSpeed': 'Auto'}]},
                  'BFS': {'name': 'Bside-Q6-40gb',
                          'ethernetNetworkType': 'Tagged',
                          'networkType': 'Ethernet',
                          'networkUris': ['eth-401'],
                          'fcNetworkUris': [],
                          'fcoeNetworkUris': ['fcoe-1003'],
                          'lacpTimer': 'Short',
                          'logicalInterconnectUri': None,
                          'primaryPortLocation': None,
                          'manualLoginRedistributionState': 'NotSupported',
                          'connectionMode': 'Auto',
                          'nativeNetworkUri': None,
                          'portConfigInfos': [{'enclosure': ENC_2, 'bay': '6', 'port': 'Q6', 'desiredSpeed': 'Auto'}]}
                  }

enc_group = {
    'EG_HA':
        {'name': EG,
         'enclosureCount': frame,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG_HAside},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG_HAside}],
         'ipAddressingMode': 'DHCP'
         },
    'EG':
        {'name': EG,
         'enclosureCount': frame,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG}],
         'ipAddressingMode': 'DHCP'
         },
    'EG_AB':
        {'name': EG,
         'enclosureCount': frame,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIGAside},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIGBside}],
         'ipAddressingMode': 'DHCP'
         }
}

les = {
    'LE_HA':
        {'name': LE_HA,
         'enclosureUris': ENC_List[0:frame],
         'enclosureGroupUri': 'EG:' + EG,
         'firmwareBaselineUri': None,
         'forceInstallFirmware': False
         },
    'LE':
        {'name': LE,
         'enclosureUris': ENC_List[0:frame],
         'enclosureGroupUri': 'EG:' + EG,
         'firmwareBaselineUri': None,
         'forceInstallFirmware': False
         }
}
Interconnect_name = [ENC_1 + ', ' + 'interconnect 3', ENC_2 + ', ' + 'interconnect 6']
Interconnect_dto = [{"name": Interconnect_name[0]}, {"name": Interconnect_name[1]}]
port_name = ['Q6', 'Q6']


uplink_body = {'associatedUplinkSetUri': 'us-unTagged',
               'interconnectName': ENC1ICBAY3,
               'portType': 'Uplink',
               'portId': 'ENC1ICBAY3:Q1:1',
               'portHealthStatus': 'Normal',
               'capability': ['EnetFcoe', 'Ethernet', 'FibreChannel'],
               'configPortTypes': ['EnetFcoe', 'Ethernet'],
               'enabled': False,
               'portName': 'UpLinkPort',
               'portStatus': 'Linked',
               'type': 'port'}

server_profiles = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC_1 + ', bay 6',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC_1, 'enclosureGroupUri': 'EG:%s' % EG,
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': ENC_1 + '_Bay6_Gen10_Quack', 'description': 'Gen10 Win', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                         'requestedMbps': '2500', 'networkUri': 'ETH:eth-101',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                         'requestedMbps': '2500', 'networkUri': 'ETH:eth-102',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                         'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe-1002',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                                         'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe-1003',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        ]}},
                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC_1 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC_1, 'enclosureGroupUri': 'EG:%s' % EG,
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': ENC_1 + '_Bay1_Win_BFS', 'description': 'Win2012,R2_BFS', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                         'requestedMbps': '2500', 'networkUri': 'ETH:eth-101',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                         'requestedMbps': '2500', 'networkUri': 'ETH:eth-102',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                         'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe-1002',
                                         'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined',
                                                  'targets': [{'arrayWwpn': '20110002AC003655', 'lun': '0'}]},
                                         'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                                         'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe-1003',
                                         'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined',
                                                  'targets': [{'arrayWwpn': '21110002AC003655', 'lun': '0'}]},
                                         'mac': None, 'wwpn': '', 'wwnn': ''},
                                        ]}},
                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC_2 + ', bay 6',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC_2, 'enclosureGroupUri': 'EG:%s' % EG,
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': ENC_2 + '_Bay6_ESXi_BFS', 'description': 'Firebird! - esxi 6', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                         'requestedMbps': '2500', 'networkUri': 'ETH:eth-101',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                         'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe-1002',
                                         'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined',
                                                  'targets': [{'arrayWwpn': '21110002AC003655', 'lun': '0'}]},
                                         'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                                         'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe-1003',
                                         'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined',
                                                  'targets': [{'arrayWwpn': '21110002AC003655', 'lun': '0'}]},
                                         'mac': None, 'wwpn': '', 'wwnn': ''},
                                        ]}}

                   ]

server_profiles1 = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC_1 + ', bay 6',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC_1, 'enclosureGroupUri': 'EG:%s' % EG,
                     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': ENC_1 + '_Bay6', 'description': 'Blackbird! rhel6.7', 'affinity': 'Bay',
                     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                     'boot': {'manageBoot': True, 'order': ['HardDisk']},
                     'connectionSettings': {
                         'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                          'requestedMbps': '2500', 'networkUri': 'ETH:eth-101',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                          'requestedMbps': '2500', 'networkUri': 'ETH:eth-102',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                         {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                          'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe-1002',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                         {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                                          'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe-1003',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                         ]}},
                    {'type': 'ServerProfileV9', 'serverHardwareUri': ENC_2 + ', bay 6',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC_2, 'enclosureGroupUri': 'EG:%s' % EG,
                     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': ENC_2 + '_Bay6-BFS', 'description': 'Firebird! - esxi 6', 'affinity': 'Bay',
                     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                     'boot': {'manageBoot': True, 'order': ['HardDisk']},
                     'connectionSettings': {
                         'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                          'requestedMbps': '2500', 'networkUri': 'ETH:eth-101',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                          'requestedMbps': '2500', 'networkUri': 'ETH:eth-102',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                         {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                          'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe-1002',
                                          'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined',
                                                   'targets': [{'arrayWwpn': '21110002AC003655', 'lun': '0'}]},
                                          'mac': None, 'wwpn': '', 'wwnn': ''},
                                         {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                                          'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe-1003',
                                          'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined',
                                                   'targets': [{'arrayWwpn': '21110002AC003655', 'lun': '0'}]},
                                          'mac': None, 'wwpn': '', 'wwnn': ''},
                                         ]}}
                    ]
ilo_details = [{'ilo_ip': '15.245.132.204', 'username': 'Administrator', 'password': 'hpvse123'}, {'ilo_ip': '15.245.132.94', 'username': 'Administrator', 'password': 'hpvse123'}]
ilo_details1 = {'ilo_ip': '15.245.132.94', 'username': 'Administrator', 'password': 'hpvse123'}
# serverIp_Normal = '192.168.1.132'
server_credentials = [{'userName': 'Administrator', 'password': 'hpvse@123'}, {'userName': 'Administrator', 'password': 'hpvse1'}]
serverIp_BFS = '192.169.0.216'
server_credentials_BFS = {'userName': 'root', 'password': 'hpvse123'}
diskspd_cmd = ['cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b10K -h -L D:\sample.dat >C:\sample1.dat"', 'cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b10K -h -L D:\sample.dat >C:\sample1.dat"']

lun_count_total = ['1', '4', '2']
# diskpart_cmd = 'cmd /c "powershell.exe Get-disk -FriendlyName *3PARdata* >C:\\WINDOWSLUN.txt"'
diskpart_cmd = 'powershell.exe;Get-disk -FriendlyName *3PARdata*'
# diskpart_cmd = '^powershell.exe^ & ^Get-disk | Select-Object -Property Number,FriendlyName^>WINDOWSLUN.txt'

listdisk_cmd_esxi = 'esxcli storage core path list>lunBFS.txt'
server_BFS = {'ip': '192.169.0.216', 'username': 'root', 'password': 'hpvse123'}
cmd = 'esxcli storage core path list'

cmd1 = 'cd /vmfs/volumes;ls'
lun_BFS = '6'
alertstate_ICM = 'Active'
alertType_ICM = 'crm.connectionStateChange'
interconnect_alert = 'Connection on downlink port'
alertstate_profiles = 'Locked'
alertType_profiles = 'profilemgr.Connections.CONNECTION_SCMB_ERROR'
profile_alert = 'An error has occurred on connection'
bay_numbers = ['3', '6']

FUSION_PROMPT = '#'
FUSION_IP = '15.245.131.206'
FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
FUSION_TIMEOUT = 180              # Timeout.  Move this out???

IC_stacking_domain_role = [['Subordinate', 'Master'], ['Master', 'Subordinate']]

serverIp_Win_BFS = ['192.168.1.132']
server_credentials_Win_BFS = {'userName': 'Administrator', 'password': 'hpvse1'}

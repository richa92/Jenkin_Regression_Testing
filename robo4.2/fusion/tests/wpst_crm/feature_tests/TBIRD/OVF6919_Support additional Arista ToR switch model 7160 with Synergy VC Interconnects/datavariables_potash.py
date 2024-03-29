
def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


def Remove_Whitespace(instring):
    return instring.strip()


def convert_unicode_to_string(String):
    res = String.encode('utf-8')
    return res


# Appliance credentials to be changed for different hardware
APPLIANCE_IP = '15.245.131.12'
appliance_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

# IP Series should be changed according to valid ip you get in servers
IP_series = '10\\.\\d+\\.\\d+\\.\\d+'

FUSION_PROMPT = '#'
FUSION_IP = '15.245.131.12'
FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
FUSION_TIMEOUT = 180              # Timeout.  Move this out???

# Name of LI
LI = 'LE' + '-' + 'LIG'

# Name of EG
EG = 'EG'

# frame count to be changed for no of enclosures used
frame = 2

# IBS configuration used is 2
IBS = 2

# Enclosure Names
ENC1 = 'CN754406W7'
ENC2 = 'CN7544044C'
ENC3 = 'XXXXXXXXXX'
ENC4 = 'XXXXXXXXXX'
ENC_List = ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3, 'ENC:' + ENC4]

# Data to be checked before running in different setup
# Ethernet uplink ports of potash IC2
ETH_UPLINKS = ['Q2']

# Ethernet uplink ports of potash IC5
ETH2_UPLINKS = ['Q1:1']

# Name of LSG
LSG = 'LSG'

# Name of LS
LS = 'Arista-LS'

# Uplink set Name
US_name = 'US_Unsplitter'
US_names = ['US_Unsplitter', 'US_Splitter']

# ARISTA 1 & ARISTA 2 IP
SWITCH1 = '15.245.128.217'


# Switch Credentials
Switch1_cred = {'username': 'admin', 'password': 'hpvse123'}

SWITCH_IP = [SWITCH1]

switch1_info = {'IP': '15.245.128.217', 'userName': 'admin', 'password': 'hpvse123', 'switch_command': ['speed forced 40gfull', 'speed forced 10gfull'], 'interface': ['interface Ethernet 50/1', 'interface Ethernet 51/1'], 'interface_num': ['Et50/1', 'Et51/1']}

# Number of LI'S created for A+B Side
No_of_LI = '2'

# It will be checking stacking member id of LS
role_name = 'StackingMemberId'

# Domain ID of switch
Domain_ID = 'mlag1'

Bay_Number = ['2', '5']

# Below I have mentioned the Uplink port & switch port configuration

# The uplink & switch ports used for test case 1 - Uplink ports are on a single Potash connected to a Arista-1 ToR switch (Single-homed from the Potash)

UP_Ports_TC1 = ['Q2']  # uplink ports of Potash IC5 connected to Arista1
Switch_ports_TC1 = ['50.1']  # Arista1 ports connected to IC5 potash
# port 50.1 -> Q2(IC2) -> ARISTA1

# The uplink & switch ports used for test case - Uplink ports span both potash and all ports are connected to a single Arista ToR switch in a 2 switch configuration (Single-homed from each potash)

Uplink_bay2 = ['Q2']  # uplink ports of Potash IC2 connected to Arista 1
Uplink_bay5 = ['Q1:1']  # uplink ports of potash IC5 connected to Arista 1
UP_Ports_TC3 = ['Q2', 'Q1:1']  # uplink ports used from two potash connecting to Arista 1
Switch_ports_TC3 = ['50.1', '51.1']  # Arista1 ports connecting to two potash

# Test case 5 - Disabling Arista1 port 1:1 and Enabling the same port

Switch_ports_TC5 = ['50.1', '51.1']  # Arista1 port which is disabled
port_no = ['50.1', '51.1']  # This is the switch port to disable

# Arista 1 port 50 -> Q2(IC2)
# Arista 1 port 51 -> Q1(IC5)

Interconnect_name = [ENC1 + ', ' + 'interconnect 2', ENC2 + ', ' + 'interconnect 5']
Interconnect_dto = [{'name': Interconnect_name[0]}, {'name': Interconnect_name[1]}]


# Interconnect map template configurations
# No of Enclosure - 1 , IBS - 2 configuration

ENC1map = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
    ]

ENC1Aside = [
    {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
]

ENC1Bside = [
    {'bay': 5, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
]

# No of Enclosure - 2 , IBS - 2 configuration
ENC2map = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
    ]

ENC2Aside = [
    {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2}
]

ENC2Bside = [
    {'bay': 5, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
    {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
]

# No of Enclosures - 3 , IBS - 2 configuration
ENC3map = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 5, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

ENC3Aside = [
    {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
    {'bay': 2, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
]

ENC3Bside = [
    {'bay': 5, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 5, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
    {'bay': 5, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
]

# To determine redundancy type of Interconnect
if frame == 1:
    REDUNDANCY = 'Redundant'
elif frame == 2:
    REDUNDANCY = 'HighlyAvailable'
elif frame == 3:
    REDUNDANCY = 'HighlyAvailable'

# Network creation body
ethernet_networks = [{
    'type': 'ethernet-networkV4',
    'ethernetNetworkType': 'Tagged',
    'name': 'Eth_401',
    'privateNetwork': False,
    'purpose': 'General',
    'smartLink': True,
    'vlanId': 401
},
    {
    'type': 'ethernet-networkV4',
    'ethernetNetworkType': 'Tagged',
    'name': 'Eth_402',
    'privateNetwork': False,
    'purpose': 'General',
    'smartLink': True,
    'vlanId': 402
}]

# LIG creation, uplink set body
uplink_sets_in_lig = [{
    'name': 'US_Unsplitter',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['Eth_401'],
    'lacpTimer': 'Short',
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '2', 'port': ETH_UPLINKS[0], 'speed': 'Speed40G'},
    ]
}]

lig = {'name': 'LIG',
       'interconnectMapTemplate': ENC2map,
       'enclosureIndexes': [x for x in xrange(1, frame + 1)],
       'interconnectBaySet': IBS,
       'redundancyType': REDUNDANCY,
       'telemetryConfiguration': {'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': 12, 'sampleInterval': 60},
       'uplinkSets': list(uplink_sets_in_lig)
       }

uplink_sets_in_ligA = [{
    'name': 'US_Unsplitter',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['Eth_401', 'Eth_402'],
    'lacpTimer': 'Short',
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '2', 'port': ETH_UPLINKS[0], 'speed': 'Speed40G'}]

}]

uplink_sets_in_ligB = [{
    'name': 'US_Splitter',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['Eth_401', 'Eth_402'],
    'lacpTimer': 'Short',
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '5', 'port': ETH2_UPLINKS[0], 'speed': 'Auto'},
    ]
}]

ligA = {'name': 'LIG_A',
        'interconnectMapTemplate': ENC2Aside,
        'enclosureIndexes': [x for x in xrange(1, frame + 1)],
        'interconnectBaySet': IBS,
        'redundancyType': 'NonRedundantASide',
        'telemetryConfiguration': {'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': 12, 'sampleInterval': 60},
        'uplinkSets': list(uplink_sets_in_ligA)
        }

ligB = {'name': 'LIG_B',
        'interconnectMapTemplate': ENC2Bside,
        'enclosureIndexes': [x for x in xrange(1, frame + 1)],
        'interconnectBaySet': IBS,
        'redundancyType': 'NonRedundantBSide',
        'telemetryConfiguration': {'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': 12, 'sampleInterval': 60},
        'uplinkSets': list(uplink_sets_in_ligB)
        }
# EG creation body
enc_group = {
    'EG':
        {'name': 'EG',
         'enclosureCount': frame,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG'},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG'},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
         'ipAddressingMode': 'DHCP'
         }
}


enc_grp_AB = {
    'EG_AB':
        {'name': 'EG_AB',
         'enclosureCount': frame,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG_A'},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG_B'},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
         'ipAddressingMode': 'DHCP'
         }
}

# LE creation body
LE = {
    'LE':
        {'name': 'LE',
         'enclosureUris': ENC_List[0:frame],
         'enclosureGroupUri': 'EG:' + 'EG',
         'firmwareBaselineUri': None,
         'forceInstallFirmware': False
         }
}

LE_AB = {
    'LE_AB':
        {'name': 'LE_AB',
         'enclosureUris': ENC_List[0:frame],
         'enclosureGroupUri': 'EG:' + 'EG_AB',
         'firmwareBaselineUri': None,
         'forceInstallFirmware': False
         }
}

uplinkset_unsplitter_li = {
    'type': 'uplink-setV6',
    'name': 'US_Splitter',
    'portConfigInfos': [{'desiredSpeed': 'Auto', 'location': {'locationEntries':
                                                              [{'value': ETH2_UPLINKS[0], 'type': 'Port'},
                                                               {'value': '5', 'type': 'Bay'},
                                                               {'value': ENC_List[1], 'type': 'Enclosure'
                                                                }]}
                         }],
    'networkType': 'Ethernet',
    'manualLoginRedistributionState': 'NotSupported',
    'logicalInterconnectUri': 'EG:%s' % LI,
    'connectionMode': 'Auto',
    'networkUris': ['Eth:Eth_402'],
    'fcNetworkUris': [],
    'fcoeNetworkUris': []
}


# server profile names
ENC1_SP_1_NAME = 'SP-enc1-bay1'
ENC2_SP_1_NAME = 'SP-enc2-bay1'

# Server profile creation body
server_profiles = [{'type': 'ServerProfileV11',
                    'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '',
                    'enclosureUri': 'ENC:' + ENC1,
                    'enclosureGroupUri': 'EG:%s' % EG,
                    'serialNumberType': 'Physical',
                    'macType': 'Physical',
                    'wwnType': 'Physical',
                    'name': ENC1_SP_1_NAME,
                    'description': 'Blackbird Windows - Aside',
                    'affinity': 'Bay',
                    'connectionSettings': {'connections': [{'id': 1,
                                                            'name': 'conn-net1',
                                                            'functionType': 'Ethernet',
                                                            'portId': 'Mezz 2:1-a',
                                                            'requestedMbps': 2500,
                                                            'networkUri': 'ETH:Eth_401',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 2,
                                                            'name': 'conn-net2',
                                                            'functionType': 'Ethernet',
                                                            'portId': 'Mezz 2:2-a',
                                                            'requestedMbps': 2500,
                                                            'networkUri': 'ETH:Eth_401',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None}]}},
                   {'type': 'ServerProfileV11',
                    'serverHardwareUri': ENC2 + ', bay 1',
                    'serverHardwareTypeUri': '',
                    'enclosureUri': 'ENC:' + ENC2,
                    'enclosureGroupUri': 'EG:%s' % 'EG',
                    'serialNumberType': 'Physical',
                    'macType': 'Physical',
                    'wwnType': 'Physical',
                    'name': ENC2_SP_1_NAME,
                    'description': 'Blackbird Windows - Aside',
                    'affinity': 'Bay',
                    'connectionSettings': {'connections': [{'id': 1,
                                                            'name': 'conn-net1',
                                                            'functionType': 'Ethernet',
                                                            'portId': 'Mezz 2:1-a',
                                                            'requestedMbps': 2500,
                                                            'networkUri': 'ETH:Eth_401',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 2,
                                                            'name': 'conn-net2',
                                                            'functionType': 'Ethernet',
                                                            'portId': 'Mezz 2:2-a',
                                                            'requestedMbps': 2500,
                                                            'networkUri': 'ETH:Eth_401',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None}]}}
                   ]

Edit_server_profiles1 = [{'type': 'ServerProfileV11',
                          'serverHardwareUri': ENC1 + ', bay 1',
                          'serverHardwareTypeUri': '',
                          'enclosureUri': 'ENC:' + ENC1,
                          'enclosureGroupUri': 'EG:%s' % EG,
                          'serialNumberType': 'Physical',
                          'macType': 'Physical',
                          'wwnType': 'Physical',
                          'name': ENC1_SP_1_NAME,
                          'description': 'Blackbird Windows - Aside',
                          'affinity': 'Bay',
                          'connectionSettings': {'connections': [{'id': 1,
                                                                  'name': 'conn-net1',
                                                                  'functionType': 'Ethernet',
                                                                  'portId': 'Mezz 2:1-a',
                                                                  'requestedMbps': 2500,
                                                                  'networkUri': 'ETH:Eth_401',
                                                                  'mac': None,
                                                                  'wwpn': None,
                                                                  'wwnn': None},
                                                                 {'id': 2,
                                                                  'name': 'conn-net2',
                                                                  'functionType': 'Ethernet',
                                                                  'portId': 'Mezz 2:2-a',
                                                                  'requestedMbps': 2500,
                                                                  'networkUri': 'ETH:Eth_401',
                                                                  'mac': None,
                                                                  'wwpn': None,
                                                                  'wwnn': None},
                                                                 {'id': 3,
                                                                  'name': 'conn-net3',
                                                                  'functionType': 'Ethernet',
                                                                  'portId': 'Mezz 2:1-d',
                                                                  'requestedMbps': 2500,
                                                                  'networkUri': 'ETH:Eth_402',
                                                                  'mac': None,
                                                                  'wwpn': None,
                                                                  'wwnn': None},
                                                                 {'id': 4,
                                                                  'name': 'conn-net4',
                                                                  'functionType': 'Ethernet',
                                                                  'portId': 'Mezz 2:2-d',
                                                                  'requestedMbps': 2500,
                                                                  'networkUri': 'ETH:Eth_402',
                                                                  'mac': None,
                                                                  'wwpn': None,
                                                                  'wwnn': None}]}},
                         {'type': 'ServerProfileV11',
                          'serverHardwareUri': ENC2 + ', bay 1',
                          'serverHardwareTypeUri': '',
                          'enclosureUri': 'ENC:' + ENC2,
                          'enclosureGroupUri': 'EG:%s' % 'EG',
                          'serialNumberType': 'Physical',
                          'macType': 'Physical',
                          'wwnType': 'Physical',
                          'name': ENC2_SP_1_NAME,
                          'description': 'Blackbird Windows - Aside',
                          'affinity': 'Bay',
                          'connectionSettings': {'connections': [{'id': 1,
                                                                  'name': 'conn-net1',
                                                                  'functionType': 'Ethernet',
                                                                  'portId': 'Mezz 2:1-a',
                                                                  'requestedMbps': 2500,
                                                                  'networkUri': 'ETH:Eth_401',
                                                                  'mac': None,
                                                                  'wwpn': None,
                                                                  'wwnn': None},
                                                                 {'id': 2,
                                                                  'name': 'conn-net2',
                                                                  'functionType': 'Ethernet',
                                                                  'portId': 'Mezz 2:2-a',
                                                                  'requestedMbps': 2500,
                                                                  'networkUri': 'ETH:Eth_401',
                                                                  'mac': None,
                                                                  'wwpn': None,
                                                                  'wwnn': None},
                                                                 {'id': 3,
                                                                  'name': 'conn-net3',
                                                                  'functionType': 'Ethernet',
                                                                  'portId': 'Mezz 2:1-d',
                                                                  'requestedMbps': 2500,
                                                                  'networkUri': 'ETH:Eth_402',
                                                                  'mac': None,
                                                                  'wwpn': None,
                                                                  'wwnn': None},
                                                                 {'id': 4,
                                                                  'name': 'conn-net4',
                                                                  'functionType': 'Ethernet',
                                                                  'portId': 'Mezz 2:2-d',
                                                                  'requestedMbps': 2500,
                                                                  'networkUri': 'ETH:Eth_402',
                                                                  'mac': None,
                                                                  'wwpn': None,
                                                                  'wwnn': None}]}}
                         ]

server_profiles_AB = [{'type': 'ServerProfileV11',
                       'serverHardwareUri': ENC1 + ', bay 1',
                       'serverHardwareTypeUri': '',
                       'enclosureUri': 'ENC:' + ENC1,
                       'enclosureGroupUri': 'EG:%s' % 'EG_AB',
                       'serialNumberType': 'Physical',
                       'macType': 'Physical',
                       'wwnType': 'Physical',
                       'name': ENC1_SP_1_NAME,
                       'description': 'Blackbird Windows - Aside',
                       'affinity': 'Bay',
                       'connectionSettings': {'connections': [{'id': 1,
                                                               'name': 'conn-net1',
                                                               'functionType': 'Ethernet',
                                                               'portId': 'Mezz 2:1-a',
                                                               'requestedMbps': 2500,
                                                               'networkUri': 'ETH:Eth_401',
                                                               'mac': None,
                                                               'wwpn': None,
                                                               'wwnn': None},
                                                              {'id': 2,
                                                               'name': 'conn-net2',
                                                               'functionType': 'Ethernet',
                                                               'portId': 'Mezz 2:2-a',
                                                               'requestedMbps': 2500,
                                                               'networkUri': 'ETH:Eth_401',
                                                               'mac': None,
                                                               'wwpn': None,
                                                               'wwnn': None},
                                                              {'id': 3,
                                                               'name': 'conn-net3',
                                                               'functionType': 'Ethernet',
                                                               'portId': 'Mezz 2:1-d',
                                                               'requestedMbps': 2500,
                                                               'networkUri': 'ETH:Eth_402',
                                                               'mac': None,
                                                               'wwpn': None,
                                                               'wwnn': None},
                                                              {'id': 4,
                                                               'name': 'conn-net4',
                                                               'functionType': 'Ethernet',
                                                               'portId': 'Mezz 2:2-d',
                                                               'requestedMbps': 2500,
                                                               'networkUri': 'ETH:Eth_402',
                                                               'mac': None,
                                                               'wwpn': None,
                                                               'wwnn': None}]}},
                      {'type': 'ServerProfileV11',
                       'serverHardwareUri': ENC2 + ', bay 1',
                       'serverHardwareTypeUri': '',
                       'enclosureUri': 'ENC:' + ENC2,
                       'enclosureGroupUri': 'EG:%s' % 'EG_AB',
                       'serialNumberType': 'Physical',
                       'macType': 'Physical',
                       'wwnType': 'Physical',
                       'name': ENC2_SP_1_NAME,
                       'description': 'Blackbird Windows - Aside',
                       'affinity': 'Bay',
                       'connectionSettings': {'connections': [{'id': 1,
                                                               'name': 'conn-net1',
                                                               'functionType': 'Ethernet',
                                                               'portId': 'Mezz 2:1-a',
                                                               'requestedMbps': 2500,
                                                               'networkUri': 'ETH:Eth_401',
                                                               'mac': None,
                                                               'wwpn': None,
                                                               'wwnn': None},
                                                              {'id': 2,
                                                               'name': 'conn-net2',
                                                               'functionType': 'Ethernet',
                                                               'portId': 'Mezz 2:2-a',
                                                               'requestedMbps': 2500,
                                                               'networkUri': 'ETH:Eth_401',
                                                               'mac': None,
                                                               'wwpn': None,
                                                               'wwnn': None},
                                                              {'id': 3,
                                                               'name': 'conn-net3',
                                                               'functionType': 'Ethernet',
                                                               'portId': 'Mezz 2:1-d',
                                                               'requestedMbps': 2500,
                                                               'networkUri': 'ETH:Eth_402',
                                                               'mac': None,
                                                               'wwpn': None,
                                                               'wwnn': None},
                                                              {'id': 4,
                                                               'name': 'conn-net4',
                                                               'functionType': 'Ethernet',
                                                               'portId': 'Mezz 2:2-d',
                                                               'requestedMbps': 2500,
                                                               'networkUri': 'ETH:Eth_402',
                                                               'mac': None,
                                                               'wwpn': None,
                                                               'wwnn': None}]}}
                      ]
# LSG BODY
LSG1 = {'name': LSG,
        'type': 'logical-switch-groupV4',
        'switchMapTemplate': {'switchMapEntryTemplates': [
            {'logicalLocation': {'locationEntries': [{'relativeValue': 1, 'type': 'StackingMemberId'}]},
             'permittedSwitchTypeUri': 'SWT:Arista 7160X'}
        ]}}

# Creating LS in Monitored mode
LS1 = {
    'logicalSwitch': {
        'name': 'LS_7160X',
        'managementLevel': 'MONITORED',
        'logicalSwitchGroupUri': 'LSG:' + LSG,
        'switchCredentialConfiguration': [
            {'logicalSwitchManagementHost': SWITCH1
             }

        ],
        'type': 'logical-switchV5',
    },
    'logicalSwitchCredentials': [
        {'connectionProperties': [
            {
                'propertyName': 'SshBasicAuthCredentialUser',
                'value': Switch1_cred['username'],
            },
            {
                'propertyName': 'SshBasicAuthCredentialPassword',
                'value': Switch1_cred['password'],
            }
        ]
        }
    ]
}

# Editing LS to Managed Mode
LS1_edit = {
    'logicalSwitch': {
        'name': 'LS_7160X',
        'managementLevel': 'BASIC_MANAGED',
        'logicalSwitchGroupUri': '',
        'uri': ' ',
        'switchCredentialConfiguration': [
            {'logicalSwitchManagementHost': SWITCH1,
                'switchUri': ''
             }
        ],
        'switchUris': [],
        'type': 'logical-switchV5',
    },
    'logicalSwitchCredentials': [
        {'connectionProperties': [
            {
                'propertyName': 'SshBasicAuthCredentialUser',
                'value': Switch1_cred['username'],
            },
            {
                'propertyName': 'SshBasicAuthCredentialPassword',
                'value': Switch1_cred['password'],
            }
        ]
        }
    ]
}

# Editing LS to Monitored Mode
LS2_edit = {
    'logicalSwitch': {
        'name': 'LS_7160X',
        'managementLevel': 'MONITORED',
        'logicalSwitchGroupUri': '',
        'uri': ' ',
        'switchCredentialConfiguration': [
            {'logicalSwitchManagementHost': SWITCH1,
                'switchUri': ''
             }
        ],
        'switchUris': [],
        'type': 'logical-switchV5',
    },
    'logicalSwitchCredentials': [
        {'connectionProperties': [
            {
                'propertyName': 'SshBasicAuthCredentialUser',
                'value': Switch1_cred['username'],
            },
            {
                'propertyName': 'SshBasicAuthCredentialPassword',
                'value': Switch1_cred['password'],
            }
        ]
        },
    ]
}

# Creating LS in Managed Mode
LS2 = {
    'logicalSwitch': {
        'name': 'LS_7160X',
        'managementLevel': 'BASIC_MANAGED',
        'logicalSwitchGroupUri': 'LSG:' + LSG,
        'switchCredentialConfiguration': [
            {'logicalSwitchManagementHost': SWITCH1
             }
        ],
        'type': 'logical-switchV5',
    },
    'logicalSwitchCredentials': [
        {'connectionProperties': [
            {
                'propertyName': 'SshBasicAuthCredentialUser',
                'value': Switch1_cred['username'],
            },
            {
                'propertyName': 'SshBasicAuthCredentialPassword',
                'value': Switch1_cred['password'],
            }
        ]
        },
    ]
}

LS3 = {
    'logicalSwitch': {
        'name': 'Arista_LS_7050X',
        'managementLevel': 'BASIC_MANAGED',
        'logicalSwitchGroupUri': 'LSG:' + LSG,
        'switchCredentialConfiguration': [
            {'logicalSwitchManagementHost': SWITCH1
             },
        ],
        'type': 'logical-switchV5',
    },
    'logicalSwitchCredentials': [
        {'connectionProperties': [
            {
                'propertyName': 'SshBasicAuthCredentialUser',
                'value': Switch1_cred['username'],
            },
            {
                'propertyName': 'SshBasicAuthCredentialPassword',
                'value': Switch1_cred['password'],
            }
        ]
        }
    ]
}

# ping command for server to server
ping_cmd_server1 = 'ping server_ip > sample.txt'

ping_cmd_server2 = 'ping server_ip > sample3.txt'

# ping command for server to gateway ping
ping_gateway_server1 = 'ping server_ip > sample1.txt'

ping_gateway_server2 = 'ping server_ip > sample2.txt'

# File names
file1 = 'sample.txt'  # server to server ping for server1
file2 = 'sample1.txt'  # server to gateway ping for server1
file3 = 'sample2.txt'  # server to gateway ping for server2
file4 = 'sample3.txt'  # server to server ping for server2

file_names = [file1, file2, file3, file4]

# continuous ping command for server to server
# based on ip's i have redirected to each file used for test case1
ping_cont_server1 = ['ping server_ip -t > test1.txt', 'ping server_ip -t > test2.txt']

ping_cont_server2 = ['ping server_ip -t > test3.txt', 'ping server_ip -t > test4.txt']

# Ping gateway continuously
ping_gateway_cont_server1 = ['ping server_ip -t > gate1.txt', 'ping server_ip -t > gate2.txt']

ping_gateway_cont_server2 = ['ping server_ip -t > gate3.txt', 'ping server_ip -t > gate4.txt']

# File Names for conti ping
text1 = 'test1.txt'
text2 = 'test2.txt'
text3 = 'test3.txt'
text4 = 'test4.txt'
text5 = 'gate1.txt'
text6 = 'gate2.txt'
text7 = 'gate3.txt'
text8 = 'gate4.txt'

text_names = [text1, text2, text3, text4, text5, text6, text7, text8]


# Command to kill traffic
kill_cmd = 'TASKKILL /F /IM PING.EXE'

# Server details
server1_details = {'username': 'Administrator', 'password': 'hpvse1'}
server2_details = {'username': 'Administrator', 'password': 'hpvse1'}
ilo_details_enc1_bay1 = {'ilo_ip': '15.245.132.119', 'username': 'Administrator', 'password': 'hpvse123'}
ilo_details_enc2_bay1 = {'ilo_ip': '15.245.132.129', 'username': 'Administrator', 'password': 'hpvse123'}


# Edit Switch Body to enable/disable switch port
switch_body = [{'portType': 'Uplink',
                'portId': ' ',
                'portHealthStatus': 'Normal',
                'enabled': ' ',
                'portName': Switch_ports_TC5[0],
                'portStatus':'Linked',
                'type':'portV6'},
               {'portType': 'Uplink',
                'portId': ' ',
                'portHealthStatus': 'Normal',
                'enabled': ' ',
                'portName': Switch_ports_TC5[1],
                'portStatus':'Linked',
                'type':'portV6'}
               ]

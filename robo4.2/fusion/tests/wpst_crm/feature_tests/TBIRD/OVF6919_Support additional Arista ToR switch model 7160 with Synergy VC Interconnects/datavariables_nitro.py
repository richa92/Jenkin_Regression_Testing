
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
IBS = 3

# Enclosure Names
ENC1 = 'CN754406W7'
ENC2 = 'CN7544044C'
ENC3 = 'XXXXXXXXXX'
ENC4 = 'XXXXXXXXXX'
ENC_List = ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3, 'ENC:' + ENC4]

# Data to be checked before running in different setup
# Ethernet uplink ports of Nitro IC3
ETH_UPLINKS = ['Q2:1']

# Ethernet uplink ports of Nitro IC6
ETH2_UPLINKS = ['Q1']

# Name of LSG
LSG = 'LSG_7160x'

# Name of LS
LS = 'LS_7160X'

# Uplink set Name
US_name = 'US_Splitter'
US_names = ['US_Splitter', 'US_Unsplitter']

# ARISTA 1 & ARISTA 2 IP
SWITCH1 = '15.245.128.217'

# Switch Credentials
Switch1_cred = {'username': 'admin', 'password': 'hpvse123'}

SWITCH_IP = [SWITCH1]
switch1_info = {'IP': '15.245.128.217', 'userName': 'admin', 'password': 'hpvse123', 'switch_command': ['speed forced 10gfull', 'speed forced 40gfull'], 'interface': ['interface Ethernet 25', 'interface Ethernet 49/1'], 'interface_num': ['Et25', 'Et49/1']}


# Number of LI'S created for A+B Side
No_of_LI = '2'

# Switch IP,Role,Memberid should be in same order
# SWITCH1 is primary switch with member id of 1 ,SWITCH2 is secondary switch with member id of 2
mem_id = ['1', '2']

roles = ['primary', 'secondary']

# It will be checking stacking member id of LS
role_name = 'StackingMemberId'

# Domain ID of switch
Domain_ID = 'mlag1'

# Below I have mentioned the Uplink port & switch port configuration

# The uplink & switch ports used for test case 1 - Uplink ports are on a single Potash connected to a Arista-1 ToR switch (Single-homed from the Nitro)

UP_Ports_TC1 = ['Q2:1']  # uplink ports of Nitro IC3 connected to Arista1
Switch_ports_TC1 = ['25']  # Arista1 ports connected to IC3 Nitro
# port 25 -> Q2.1(IC3)  -> ARISTA1


# The uplink & switch ports used for test case 3 - Uplink ports span both Nitro and all ports are connected to a single Arista ToR switch in a 2 switch configuration (Single-homed from each Nitro)

Uplink_bay2 = ['Q2:1']  # uplink ports of Nitro IC3 connected to Arista 1
Uplink_bay5 = ['Q1']  # uplink ports of Nitro IC6 connected to Arista 1
UP_Ports_TC3 = ['Q2:1', 'Q1']  # uplink ports used from two Nitro connecting to Arista 1
Switch_ports_TC3 = ['25', '49.1']  # Arista1 ports connecting to two Nitro

# port 25 -> Q2.1(IC3), port 49 -> Q1(IC6)  ->  ARISTA1


# Test case 5 - Disabling Arista1 port 1:1 and Enabling the same port
UP_Ports_TC5 = ['Q2:1']  # uplink ports from Nitro IC3 connecting to Arista1 51
Switch_ports_TC5 = ['25', '49.1']  # Arista1 port which is disabled
port_no = ['25', '49.1']  # This is the switch port.

# Arista 1 port 25 -> Q2.1 (IC3)

UP_Ports_TC4_SW1 = ['Q2:1', 'Q1']  # uplink ports of Nitro IC3, IC6 connected to Arista1
Switch1_ports_TC4 = ['25', '49.1']  # Arista1 ports connecting to two Nitro

Interconnect_name = [ENC1 + ', ' + 'interconnect 3', ENC2 + ', ' + 'interconnect 6']
Interconnect_dto = [{'name': Interconnect_name[0]}, {'name': Interconnect_name[1]}]

Bay_Number = ['3', '6']

# Interconnect map template configurations
# No of Enclosure - 1 , IBS - 3 configuration

ENC1map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

ENC1Aside = [
    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
]

ENC1Bside = [
    {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
]

# No of Enclosure - 2 , IBS - 3 configuration
ENC2map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]

ENC2Aside = [
    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2}
]

ENC2Bside = [
    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
]

# No of Enclosures - 3 , IBS - 3 configuration
ENC3map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

ENC3Aside = [
    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
    {'bay': 3, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
]

ENC3Bside = [
    {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
    {'bay': 6, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
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
    'name': 'US_Splitter',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['Eth_401'],
    'lacpTimer': 'Short',
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': ETH_UPLINKS[0], 'speed': 'Auto'},
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
    'name': 'US_Splitter',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['Eth_401'],
    'lacpTimer': 'Short',
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': ETH_UPLINKS[0], 'speed': 'Auto'}]
}
]

uplink_sets_in_ligB = [
    {
        'name': 'US_Unsplitter',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['Eth_402'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': ETH2_UPLINKS[0], 'speed': 'Speed40G'}]
    }
]

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
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG'}],
         'ipAddressingMode': 'DHCP'
         }
}


enc_grp_AB = {
    'EG_AB':
        {'name': 'EG_AB',
         'enclosureCount': frame,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG_A'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG_B'}],
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

# server profile names
ENC1_SP_1_NAME = 'SP-enc1-bay1'
ENC2_SP_1_NAME = 'SP-enc2-bay1'

# Server profile creation body
server_profiles = [{'type': 'ServerProfileV11',
                    'serverHardwareUri': ENC1 + ', bay 3',
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
                                                            'name': 'con_1',
                                                            'functionType': 'Ethernet',
                                                            'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': 2500,
                                                            'networkUri': 'ETH:Eth_401',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 1,
                                                            'name': 'con_2',
                                                            'functionType': 'Ethernet',
                                                            'portId': 'Mezz 3:2-a',
                                                            'requestedMbps': 2500,
                                                            'networkUri': 'ETH:Eth_401',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None}
                                                           ]}},
                   {'type': 'ServerProfileV11',
                    'serverHardwareUri': ENC2 + ', bay 2',
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
                                                            'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': 2500,
                                                            'networkUri': 'ETH:Eth_401',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 1,
                                                            'name': 'conn-net2',
                                                            'functionType': 'Ethernet',
                                                            'portId': 'Mezz 3:2-a',
                                                            'requestedMbps': 2500,
                                                            'networkUri': 'ETH:Eth_401',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None}
                                                           ]}}
                   ]

Edit_server_profiles1 = [{'type': 'ServerProfileV11',
                          'serverHardwareUri': ENC1 + ', bay 3',
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
                                                                  'name': 'con_1',
                                                                  'functionType': 'Ethernet',
                                                                  'portId': 'Mezz 3:1-a',
                                                                  'requestedMbps': 2500,
                                                                  'networkUri': 'ETH:Eth_401',
                                                                  'mac': None,
                                                                  'wwpn': None,
                                                                  'wwnn': None},
                                                                 {'id': 2,
                                                                  'name': 'con_2',
                                                                  'functionType': 'Ethernet',
                                                                  'portId': 'Mezz 3:2-a',
                                                                  'requestedMbps': 2500,
                                                                  'networkUri': 'ETH:Eth_401',
                                                                  'mac': None,
                                                                  'wwpn': None,
                                                                  'wwnn': None},
                                                                 {'id': 3,
                                                                  'name': 'con_3',
                                                                  'functionType': 'Ethernet',
                                                                  'portId': 'Mezz 3:1-d',
                                                                  'requestedMbps': 2500,
                                                                  'networkUri': 'ETH:Eth_402',
                                                                  'mac': None,
                                                                  'wwpn': None,
                                                                  'wwnn': None},
                                                                 {'id': 4,
                                                                  'name': 'con_4',
                                                                  'functionType': 'Ethernet',
                                                                  'portId': 'Mezz 3:2-d',
                                                                  'requestedMbps': 2500,
                                                                  'networkUri': 'ETH:Eth_402',
                                                                  'mac': None,
                                                                  'wwpn': None,
                                                                  'wwnn': None}]}},
                         {'type': 'ServerProfileV11',
                          'serverHardwareUri': ENC2 + ', bay 2',
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
                                                                  'portId': 'Mezz 3:1-a',
                                                                  'requestedMbps': 2500,
                                                                  'networkUri': 'ETH:Eth_401',
                                                                  'mac': None,
                                                                  'wwpn': None,
                                                                  'wwnn': None},
                                                                 {'id': 2,
                                                                  'name': 'conn-net2',
                                                                  'functionType': 'Ethernet',
                                                                  'portId': 'Mezz 3:2-a',
                                                                  'requestedMbps': 2500,
                                                                  'networkUri': 'ETH:Eth_401',
                                                                  'mac': None,
                                                                  'wwpn': None,
                                                                  'wwnn': None},
                                                                 {'id': 3,
                                                                  'name': 'con_3',
                                                                  'functionType': 'Ethernet',
                                                                  'portId': 'Mezz 3:1-d',
                                                                  'requestedMbps': 2500,
                                                                  'networkUri': 'ETH:Eth_402',
                                                                  'mac': None,
                                                                  'wwpn': None,
                                                                  'wwnn': None},
                                                                 {'id': 4,
                                                                  'name': 'con_4',
                                                                  'functionType': 'Ethernet',
                                                                  'portId': 'Mezz 3:2-d',
                                                                  'requestedMbps': 2500,
                                                                  'networkUri': 'ETH:Eth_402',
                                                                  'mac': None,
                                                                  'wwpn': None,
                                                                  'wwnn': None}]}}
                         ]

server_profiles_AB = [{'type': 'ServerProfileV11',
                       'serverHardwareUri': ENC1 + ', bay 3',
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
                                                               'name': 'con_1',
                                                               'functionType': 'Ethernet',
                                                               'portId': 'Mezz 3:1-a',
                                                               'requestedMbps': 2500,
                                                               'networkUri': 'ETH:Eth_401',
                                                               'mac': None,
                                                               'wwpn': None,
                                                               'wwnn': None},
                                                              ]}},
                      {'type': 'ServerProfileV11',
                       'serverHardwareUri': ENC2 + ', bay 2',
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
                                                               'name': 'con_1',
                                                               'functionType': 'Ethernet',
                                                               'portId': 'Mezz 3:2-a',
                                                               'requestedMbps': 2500,
                                                               'networkUri': 'ETH:Eth_402',
                                                               'mac': None,
                                                               'wwpn': None,
                                                               'wwnn': None},
                                                              ]}}
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

uplinkset_unsplitter_li = {
    'type': 'uplink-setV6',
    'name': 'US_Unsplitter',
    'portConfigInfos': [{'desiredSpeed': 'Speed40G', 'location': {'locationEntries':
                                                                  [{'value': ETH2_UPLINKS[0], 'type': 'Port'},
                                                                   {'value': '6', 'type': 'Bay'},
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

# ping command for server to server
ping_cmd_server1 = 'ping server_ip > sample.txt'

ping_cmd_server2 = 'ping server_ip > sample3.txt'

# ping command for server to gateway ping
ping_gateway_server1 = 'ping server_ip > sample1.txt'

ping_gateway_server2 = 'ping server_ip > sample2.txt'

# continuous ping command for server to server
# based on ip's i have redirected to each file used for test case1
ping_cont_server1 = ['ping server_ip -t > test1.txt']

ping_cont_server2 = ['ping server_ip -t > test2.txt']

# Ping gateway continuously
ping_gateway_cont_server1 = ['ping server_ip -t > gate1.txt']

ping_gateway_cont_server2 = ['ping server_ip -t > gate2.txt']

# File Names for conti ping
text1 = 'test1.txt'
text2 = 'test2.txt'
text3 = 'gate1.txt'
text4 = 'gate2.txt'

text_names = [text1, text2, text3, text4]

# Command to kill traffic
kill_cmd = 'TASKKILL /F /IM PING.EXE'

# File names
file1 = 'sample.txt'  # server to server ping for server1
file2 = 'sample1.txt'  # server to gateway ping for server1
file3 = 'sample2.txt'  # server to gateway ping for server2
file4 = 'sample3.txt'  # server to server ping for server2

file_names = [file1, file2, file3, file4]

# Server details
server1_details = {'username': 'Administrator', 'password': 'hpvse@1'}
server2_details = {'username': 'Administrator', 'password': 'hpvse@1'}
ilo_details_enc1_bay1 = {'ilo_ip': '15.245.134.32', 'username': 'Administrator', 'password': 'hpvse123'}
ilo_details_enc2_bay1 = {'ilo_ip': '15.245.133.31', 'username': 'Administrator', 'password': 'hpvse123'}


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
                'type':'portV6'}]

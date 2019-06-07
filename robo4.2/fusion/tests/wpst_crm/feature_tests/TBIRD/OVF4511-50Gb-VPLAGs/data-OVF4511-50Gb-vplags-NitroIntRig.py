from copy import deepcopy

# OneView REST API types
networkset_type = 'network-setV4'
lig_type = 'logical-interconnect-groupV6'
ServerProfile_type = 'ServerProfileV10'

FUSION_USERNAME = 'Administrator'  # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'  # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'  # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'  # Fusion SSH Password
FUSION_PROMPT = '#'  # Fusion Appliance Prompt
FUSION_TIMEOUT = 180  # Timeout.  Move this out???
FUSION_NIC = 'bond0'  # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

ENC_COUNT = 3

ENC_1 = 'MXQ81804ZF'
ENC_2 = 'MXQ81804ZH'
ENC_3 = 'MXQ81804ZG'

# Rack AV51 Servers for this test suite
# ENC_1 = 'MXQ81804ZF' servers used for testing
# Instead of 1st bay using 3rd bay as M2 is Bronco in 3rd bay server
QUAGMIREBAY1 = '1'
QUACKBAY1 = '2'

# ENC_2 = 'MXQ81804ZH'
QUAGMIRE2BAY1 = '3'

# Tunnel MLAG
ENC1_ICM_3_TUNNEL_PORT = 'Q1'
ENC2_ICM_6_TUNNEL_PORT = 'Q1'
# Tagged MLAG
ENC1_ICM_3_MLAG_PORT = 'Q3'
ENC2_ICM_6_MLAG_PORT = 'Q3'
# FCoE
ENC1_ICM_3_FCoE_PORT = 'Q5'
# Untagged MLAG
ENC1_ICM_3_UNTAGGED_PORT = 'Q6'
ENC2_ICM_6_UNTAGGED_PORT = 'Q6'

FCoE_VLAN = 1004

# For traffic verification:
#  pattern matching for ping statistics and allowed loss
NT_ZERO_PERCENT_LOSS = 'Lost = * (0% loss)'
LINUX_ZERO_PERCENT_LOSS = '0% packet loss'

# For S-Channel LAG connection, most of the time is 0 or 1 packet loss, rarely 2, set to 2
ALLOWED_PACKET_LOSS_SCHANNEL_LAG = 10

# RoboGalaxy Linux test head access info
linux_details = {"hostip": "15.245.132.112", "username": "root", "password": "hpvse123",
                 "dir_location": "/root/pexpect/pexpect-4.6.0/",
                 "python_cmd": "python2.7"}

# Blade server iLO access info
ilo_details = {'ilo_ip': '',
               "username": 'Administrator', "password": 'hpvse123'}

# Blade server with Windows OS access info
windows_server_cred = ["Administrator", 'hpvse@1']

server_bays = [3]

Server_network_ips = {server_bays[0]: ""}
bay2_DownLinkPort = 'd2'
Q6_UpLinkPort = 'Q6'


def make_range_list(start, end, prefix='net_', suffix=''):
    tlist = []
    for x in xrange(start, end + 1):
        tlist.append(prefix + str(x) + suffix)
    return tlist


def rlist(start, end, prefix='net_', suffix=''):
    tlist = []
    for x in xrange(start, end + 1):
        tlist.append(prefix + str(x) + suffix)
    return tlist


admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ethernet_networks = [
    {'name': 'net_400',
     'type': 'ethernet-networkV4',
     'vlanId': 400,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged',
     'bandwidth': {'maximumBandwidth': 50000, 'typicalBandwidth': 2500},
     },
    {'name': 'net_401',
     'type': 'ethernet-networkV4',
     'vlanId': 401,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged',
     'bandwidth': {'maximumBandwidth': 50000, 'typicalBandwidth': 2500},
     },
    {'name': 'net_402',
     'type': 'ethernet-networkV4',
     'vlanId': 402,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged',
     'bandwidth': {'maximumBandwidth': 50000, 'typicalBandwidth': 2500},
     },
    {'name': 'net_403',
     'type': 'ethernet-networkV4',
     'vlanId': 403,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged',
     'bandwidth': {'maximumBandwidth': 50000, 'typicalBandwidth': 2500},
     },
    {'name': 'net_404',
     'type': 'ethernet-networkV4',
     'vlanId': 404,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged',
     'bandwidth': {'maximumBandwidth': 50000, 'typicalBandwidth': 2500},
     },
    {'name': 'net_405',
     'type': 'ethernet-networkV4',
     'vlanId': 405,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged',
     'bandwidth': {'maximumBandwidth': 50000, 'typicalBandwidth': 2500},
     },
    {'name': 'net_406',
     'type': 'ethernet-networkV4',
     'vlanId': 406,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged',
     'bandwidth': {'maximumBandwidth': 50000, 'typicalBandwidth': 2500},
     },
    {'name': 'net_407',
     'type': 'ethernet-networkV4',
     'vlanId': 407,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged',
     'bandwidth': {'maximumBandwidth': 50000, 'typicalBandwidth': 2500},
     },
    {'name': 'net_408',
     'type': 'ethernet-networkV4',
     'vlanId': 408,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged',
     'bandwidth': {'maximumBandwidth': 50000, 'typicalBandwidth': 2500},
     },
    {'name': 'net_409',
     'type': 'ethernet-networkV4',
     'vlanId': 409,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged',
     'bandwidth': {'maximumBandwidth': 50000, 'typicalBandwidth': 2500},
     },
    {'name': 'net_410',
     'type': 'ethernet-networkV4',
     'vlanId': 410,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged',
     'bandwidth': {'maximumBandwidth': 50000, 'typicalBandwidth': 2500},
     },
    {'name': 'tunnelnetwork1',
     'type': 'ethernet-networkV4',
     'vlanId': None,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tunnel'},
    {'name': 'tunnelnetwork2',
     'type': 'ethernet-networkV4',
     'vlanId': None,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tunnel'},
    {'name': 'untaggednetwork1',
     'type': 'ethernet-networkV4',
     'vlanId': None,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Untagged'},
    {'name': 'untaggednetwork2',
     'type': 'ethernet-networkV4',
     'vlanId': None,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Untagged'},
]

# conn template sample for editing network sets bandwidth
conn_template = {
    'type': 'connection-template',
    'bandwidth': {
        'maximumBandwidth': None,
        'typicalBandwidth': None
    },
    'name': None
}

network_sets = [
    {'name': 'netset50G', 'type': networkset_type, 'networkUris': rlist(401, 403, prefix='net_'),
     'nativeNetworkUri': 'net_401'},
]

network_sets_bw = [
    {'name': 'netset50G', 'type': networkset_type, 'networkUris': rlist(401, 403, prefix='net_'),
     'bandwidth': {'maximumBandwidth': 50000, 'typicalBandwidth': 25000},
     'nativeNetworkUri': 'net_401'},
]

###
# Nitro Integration rig is IBS3 HA mode
# Interconnect bays configurations
# 3 Enclosures, Fabric 3
###

Enc3Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

# uplink sets data
uplink_set = {
    'us-tunnel': {
        'name': 'us-tunnel',
        'ethernetNetworkType': 'Tunnel',
        'networkType': 'Ethernet',
        'networkUris': ['tunnelnetwork1'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': ENC1_ICM_3_TUNNEL_PORT, 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': ENC2_ICM_6_TUNNEL_PORT, 'speed': 'Auto'}
        ]
    },
    'us-untagged': {
        'name': 'us-untagged',
        'ethernetNetworkType': 'Untagged',
        'networkType': 'Ethernet',
        'networkUris': ['untaggednetwork1'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': ENC1_ICM_3_UNTAGGED_PORT, 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': ENC2_ICM_6_UNTAGGED_PORT, 'speed': 'Auto'}
        ]
    },
    'us-tagged': {
        'name': 'us-tagged',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(401, 410, 'net_'),
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': ENC1_ICM_3_MLAG_PORT, 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': ENC2_ICM_6_MLAG_PORT, 'speed': 'Auto'},
        ]
    },
}

# LIGs for end to end tests
ligs_50G = {
    'Enc3-50G-LIG': {
        'name': 'Enc3-50G-LIG',
        'interconnectMapTemplate': Enc3Map,
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'downlinkSpeedMode': 'SPEED_50GB',
        'uplinkSets': [
            deepcopy(uplink_set['us-tunnel']),
            deepcopy(uplink_set['us-untagged']),
            deepcopy(uplink_set['us-tagged'])
        ],
    },
}

enc_group = {
    'Enc3-50G-EG':
        {'name': 'Enc3-50G-EG',
         'enclosureCount': 3,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc3-50G-LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc3-50G-LIG'}],
         'ipAddressingMode': "DHCP",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },
}

les = {
    'name': 'SPEED-LE',
    'enclosureUris': None,
    'enclosureGroupUri': None,
    'firmwareBaselineUri': None,
    'forceInstallFirmware': False
}


# Profile data with VPLAGs when LI speed mode is 50Gb
# Refer to Nitro Integration rig Windows server bays for servers to use

profilesVPLAG = {
    'Enc1-Profile1': {
        'payload': {
            'name': 'Enc1-Profile1',
            'type': ServerProfile_type,
            'serverHardwareUri': '{}, bay {}'.format(ENC_1, QUAGMIREBAY1),
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:EncN-XX-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 11, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '5000', 'networkUri': 'NS:netset50G', 'lagName': 'LAG1'},
                    {'id': 12, 'name': 'conn-tunnel-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                     'requestedMbps': '5000', 'networkUri': 'ETH:tunnelnetwork1', },
                    {'id': 13, 'name': 'conn-net1_405', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_405', 'lagName': 'LAG3'},
                    {'id': 14, 'name': 'conn-net1_406', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_406', 'lagName': 'LAG4'},
                    {'id': 15, 'name': 'conn-net1_407', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-e',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_407', 'lagName': 'LAG5'},
                    {'id': 16, 'name': 'conn-net1_408', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-f',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_408', 'lagName': 'LAG6'},
                    {'id': 17, 'name': 'conn-net1_409', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-g',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_409', 'lagName': 'LAG7'},
                    {'id': 18, 'name': 'conn-untagged-1h', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-h',
                     'requestedMbps': '5000', 'networkUri': 'ETH:untaggednetwork1', 'lagName': 'LAG8'},
                    {'id': 21, 'name': 'conn-netset-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                     'requestedMbps': '5000', 'networkUri': 'NS:netset50G', 'lagName': 'LAG1'},
                    {'id': 22, 'name': 'conn-tunnel-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                     'requestedMbps': '5000', 'networkUri': 'ETH:tunnelnetwork1', },
                    {'id': 23, 'name': 'conn-net2_405', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_405', 'lagName': 'LAG3'},
                    {'id': 24, 'name': 'conn-net2_406', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_406', 'lagName': 'LAG4'},
                    {'id': 25, 'name': 'conn-net2_407', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-e',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_407', 'lagName': 'LAG5'},
                    {'id': 26, 'name': 'conn-net2_408', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-f',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_408', 'lagName': 'LAG6'},
                    {'id': 27, 'name': 'conn-net2_409', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-g',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_409', 'lagName': 'LAG7'},
                    {'id': 28, 'name': 'conn-untagged-2h', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-h',
                     'requestedMbps': '5000', 'networkUri': 'ETH:untaggednetwork1', 'lagName': 'LAG8'},
                ],
            },
        },
        # Dummy IP info. Server IP addresses are read from iLO
        'IP': '172.16.5.31',
        'Server_network_ips': None,
        'handle': None
    },

    'Enc3-Profile3': {
        'payload': {
            'name': 'Enc3-Profile3',
            'type': ServerProfile_type,
            'serverHardwareUri': '{}, bay {}'.format(ENC_3, QUAGMIRE2BAY1),
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_3,
            'enclosureGroupUri': 'EG:EncN-XX-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 11, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '5000', 'networkUri': 'NS:netset50G', 'lagName': 'LAG1'},
                    {'id': 12, 'name': 'conn-tunnel-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                     'requestedMbps': '5000', 'networkUri': 'ETH:tunnelnetwork1', },
                    {'id': 13, 'name': 'conn-net1_405', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_405', 'lagName': 'LAG3'},
                    {'id': 14, 'name': 'conn-net1_406', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_406', 'lagName': 'LAG4'},
                    {'id': 15, 'name': 'conn-net1_407', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-e',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_407', 'lagName': 'LAG5'},
                    {'id': 16, 'name': 'conn-net1_408', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-f',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_408', 'lagName': 'LAG6'},
                    {'id': 17, 'name': 'conn-net1_409', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-g',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_409', 'lagName': 'LAG7'},
                    {'id': 18, 'name': 'conn-untagged-1h', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-h',
                     'requestedMbps': '5000', 'networkUri': 'ETH:untaggednetwork1', 'lagName': 'LAG8'},
                    {'id': 21, 'name': 'conn-netset-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                     'requestedMbps': '5000', 'networkUri': 'NS:netset50G', 'lagName': 'LAG1'},
                    {'id': 22, 'name': 'conn-tunnel-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                     'requestedMbps': '5000', 'networkUri': 'ETH:tunnelnetwork1', },
                    {'id': 23, 'name': 'conn-net2_405', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_405', 'lagName': 'LAG3'},
                    {'id': 24, 'name': 'conn-net2_406', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_406', 'lagName': 'LAG4'},
                    {'id': 25, 'name': 'conn-net2_407', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-e',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_407', 'lagName': 'LAG5'},
                    {'id': 26, 'name': 'conn-net2_408', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-f',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_408', 'lagName': 'LAG6'},
                    {'id': 27, 'name': 'conn-net2_409', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-g',
                     'requestedMbps': '5000', 'networkUri': 'ETH:net_409', 'lagName': 'LAG7'},
                    {'id': 28, 'name': 'conn-untagged-2h', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-h',
                     'requestedMbps': '5000', 'networkUri': 'ETH:untaggednetwork1', 'lagName': 'LAG8'},
                ],
            },
        },
        # Dummy IP info. Server IP addresses are read from iLO
        'IP': '172.16.5.32',
        'handle': None
    }
}

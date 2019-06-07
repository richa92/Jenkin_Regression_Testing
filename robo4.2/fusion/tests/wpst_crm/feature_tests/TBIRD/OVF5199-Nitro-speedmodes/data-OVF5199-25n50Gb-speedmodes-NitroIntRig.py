from copy import deepcopy

# OneView v4.20 REST API types
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
CONFIG = 'Redundant'
CXP = 'CL20'

ENC_1 = 'MXQ81804ZF'
ENC_2 = 'MXQ81804ZH'
ENC_3 = 'MXQ81804ZG'

# Rack AV51 Servers for this test suite
# ENC_1 = 'MXQ81804ZF' servers used for testing
# Instead of 1st bay using 3rd bay as M2 is Bronco in 3rd bay server
# ENC_2 = 'MXQ81804ZH'
# ENC_3 = 'MXQ81804ZG'
QUAGMIREBAY = '1'
QUACKBAY = '2'
QUAGMIRE2BAY = '3'

# Tunnel MLAG
ENC1_ICM_3_TUNNEL_PORT = 'Q1'
ENC2_ICM_6_TUNNEL_PORT = 'Q1'
# Tagged MLAG
ENC1_ICM_3_MLAG_PORT = 'Q3'
ENC2_ICM_6_MLAG_PORT = 'Q3'
# Tagged A + B
ENC1_ICM_3_ASIDE_PORT = 'Q3'
ENC2_ICM_6_BSIDE_PORT = 'Q3'

# FCoE
ENC1_ICM_3_FCoE_PORT = 'Q5'
# Untagged MLAG
ENC1_ICM_3_UNTAGGED_PORT = 'Q6'
ENC2_ICM_6_UNTAGGED_PORT = 'Q6'

FCoE_VLAN = 1004

# For traffic verification: pattern matching for ping statistics and allowed loss
NT_ZERO_PERCENT_LOSS = 'Lost = * (0% loss)'
LINUX_ZERO_PERCENT_LOSS = '0% packet loss'

# For S-Channel LAG connection, most of the time is 0 or 1 packet loss, rarely 2, set to 2
ALLOWED_PACKET_LOSS_SCHANNEL_LAG = 1000

# RoboGalaxy Linux test head access info
linux_details = {"hostip": "15.245.132.165", "username": "root", "password": "hpvse123",
                 "dir_location": "/root/pexpect/pexpect-4.6.0/",
                 "python_cmd": "python2.7"}

# Blade server iLO access info
ilo_details = {'ilo_ip': '',
               "username": 'Administrator', "password": 'hpvse123'}

# Blade server with Windows OS access info
windows_server_cred = ["Administrator", 'Hpvse1']


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

# Ethernet Tagged, Tunnel and Untagged Networks
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

# Network sets data
# Bandwidth is modified later in edit network set requests
#     'bandwidth': {'maximumBandwidth': <BW value>, 'typicalBandwidth': 2500},
network_sets = [
    # for 'maximumBandwidth': 10000
    {'name': 'netset10G', 'type': networkset_type, 'networkUris': rlist(401, 403, prefix='net_'),
     'nativeNetworkUri': 'net_401'},
    # for 'maximumBandwidth': 20000
    {'name': 'netset20G', 'type': networkset_type, 'networkUris': rlist(401, 403, prefix='net_'),
     'nativeNetworkUri': 'net_401'},
    # for 'maximumBandwidth': 25000
    {'name': 'netset25G', 'type': networkset_type, 'networkUris': rlist(401, 403, prefix='net_'),
     'nativeNetworkUri': 'net_401'},
    # for 'maximumBandwidth': 50000
    {'name': 'netset50G', 'type': networkset_type, 'networkUris': rlist(401, 403, prefix='net_'),
     'nativeNetworkUri': 'net_401'},
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

# Data for setting Max bandwidth of  network sets
network_sets_bw = [
    {'name': 'netset10G', 'type': networkset_type, 'networkUris': rlist(401, 403, prefix='net_'),
     'bandwidth': {'maximumBandwidth': 10000, 'typicalBandwidth': 2500},
     'nativeNetworkUri': 'net_401'},
    {'name': 'netset20G', 'type': networkset_type, 'networkUris': rlist(401, 403, prefix='net_'),
     'bandwidth': {'maximumBandwidth': 20000, 'typicalBandwidth': 2500},
     'nativeNetworkUri': 'net_401'},
    {'name': 'netset25G', 'type': networkset_type, 'networkUris': rlist(401, 403, prefix='net_'),
     'bandwidth': {'maximumBandwidth': 25000, 'typicalBandwidth': 10000},
     'nativeNetworkUri': 'net_401'},
    {'name': 'netset50G', 'type': networkset_type, 'networkUris': rlist(401, 403, prefix='net_'),
     'bandwidth': {'maximumBandwidth': 50000, 'typicalBandwidth': 25000},
     'nativeNetworkUri': 'net_401'},
]

# FCoE network for Qos Test case
fcoe_networks = [{'name': 'fcoenetwork', 'type': 'fcoe-networkV4', 'vlanId': FCoE_VLAN}]

###
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

# Uplink sets data
uplink_set = {
    # FCoE uplink set
    'us-bay3-fcoe': {
        'name': 'us-bay3-fcoe',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoenetwork'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': ENC1_ICM_3_FCoE_PORT, 'speed': 'Auto'}
        ]
    },
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
    'us-enet-Aside': {
        'name': 'us-enet-Aside',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(401, 405, 'net_'),
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': ENC1_ICM_3_ASIDE_PORT, 'speed': 'Auto'},
        ]
    },
    'us-enet-Bside': {
        'name': 'us-enet-Bside',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(409, 410, 'net_'),
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': ENC2_ICM_6_BSIDE_PORT, 'speed': 'Auto'},
        ]
    },
}

# LIGs for end to end tests
# SPEED_50GB
# SPEED_25GB

# workaround for OVD30521. Build LIG with qosConfiguration data
# 	Set To Dictionary	${body}	qosConfiguration	${LIGqosConfiguration}
LIGqosConfiguration = {
    'type': 'qos-aggregated-configuration',
    'uri': None,
    'category': 'qos-aggregated-configuration',
    'eTag': None,
    'created': None,
    'modified': None,
    'activeQosConfig': {
        'type': 'QosConfiguration',
        'uri': None,
        'category': 'qos-aggregated-configuration',
        'eTag': None,
        'created': None,
        'modified': None,
        'configType': 'Passthrough',
        'uplinkClassificationType': None,
        'downlinkClassificationType': None,
        'qosTrafficClassifiers': [],
        'description': None,
        'state': None,
        'status': None,
        'name': None
    }
}

# LIGs with default/downlink speed mode 25Gb
ligs_25G = {
    'Enc2-25G-LIG': {
        'name': 'Enc2-25G-LIG',
        'interconnectMapTemplate': [
            {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
            {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
             'enclosureIndex': 1},
            {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
            {'bay': 6, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        ],
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'downlinkSpeedMode': 'SPEED_25GB',
        'uplinkSets': [
            deepcopy(uplink_set['us-bay3-fcoe']),
            deepcopy(uplink_set['us-tunnel']),
            deepcopy(uplink_set['us-untagged']),
            deepcopy(uplink_set['us-tagged'])
        ],
    },
    'Enc2-25G-Aside-LIG': {
        'name': 'Enc2-25G-Aside-LIG',
        'interconnectMapTemplate': [
            {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
            {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        ],
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantASide',
        'downlinkSpeedMode': 'SPEED_25GB',
        'uplinkSets': [
            deepcopy(uplink_set['us-enet-Aside']),
            deepcopy(uplink_set['us-tunnel']),
        ],
    },
    'Enc2-25G-Bside-LIG': {
        'name': 'Enc2-25G-Bside-LIG',
        'interconnectMapTemplate': [
            {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
            {'bay': 6, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        ],
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantBSide',
        'downlinkSpeedMode': 'SPEED_25GB',
        'uplinkSets': [
            deepcopy(uplink_set['us-enet-Bside']),
            deepcopy(uplink_set['us-untagged']),
        ],
    },
    'Enc2-25G-EDIT-LIG': {
        'name': 'Enc2-25G-EDIT-LIG',
        'interconnectMapTemplate': [
            {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
            {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
             'enclosureIndex': 1},
            {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
            {'bay': 6, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        ],
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'downlinkSpeedMode': 'SPEED_25GB',
        'uplinkSets': [
        ],
    },
    'Enc3-25G-LIG': {
        'name': 'Enc3-25G-LIG',
        'interconnectMapTemplate': Enc3Map,
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'downlinkSpeedMode': 'SPEED_25GB',
        'uplinkSets': [
            deepcopy(uplink_set['us-bay3-fcoe']),
            deepcopy(uplink_set['us-tunnel']),
            deepcopy(uplink_set['us-untagged']),
            deepcopy(uplink_set['us-tagged'])
        ],
    },
    'Enc3-25G-Aside-LIG': {
        'name': 'Enc3-25G-Aside-LIG',
        'interconnectMapTemplate': [
            {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
            {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
            {'bay': 3, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
        ],
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantASide',
        'downlinkSpeedMode': 'SPEED_25GB',
        'uplinkSets': [
            deepcopy(uplink_set['us-enet-Aside']),
        ],
    },
    'Enc3-25G-Bside-LIG': {
        'name': 'Enc3-25G-Bside-LIG',
        'interconnectMapTemplate': [
            {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
            {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
            {'bay': 6, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
        ],
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantBSide',
        'downlinkSpeedMode': 'SPEED_25GB',
        'uplinkSets': [
            deepcopy(uplink_set['us-enet-Bside']),
        ],
    },
    'Enc3-25G-EDIT-LIG': {
        'name': 'Enc3-25G-EDIT-LIG',
        'interconnectMapTemplate': Enc3Map,
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'downlinkSpeedMode': 'SPEED_25GB',
        'uplinkSets': [
        ],
    },

}

# LIGs with downlink speed mode 50Gb
ligs_50G = {
    'Enc2-50G-LIG': {
        'name': 'Enc2-50G-LIG',
        'interconnectMapTemplate': [
            {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
            {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
             'enclosureIndex': 1},
            {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
            {'bay': 6, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        ],
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'downlinkSpeedMode': 'SPEED_50GB',
        'uplinkSets': [
            deepcopy(uplink_set['us-bay3-fcoe']),
            deepcopy(uplink_set['us-tunnel']),
            deepcopy(uplink_set['us-untagged']),
            deepcopy(uplink_set['us-tagged'])
        ],
    },
    'Enc2-50G-Aside-LIG': {
        'name': 'Enc2-50G-Aside-LIG',
        'interconnectMapTemplate': [
            {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
            {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        ],
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantASide',
        'downlinkSpeedMode': 'SPEED_50GB',
        'uplinkSets': [
            deepcopy(uplink_set['us-enet-Aside']),
            deepcopy(uplink_set['us-tunnel']),
        ],
    },
    'Enc2-50G-Bside-LIG': {
        'name': 'Enc2-50G-Bside-LIG',
        'interconnectMapTemplate': [
            {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
            {'bay': 6, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        ],
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantBSide',
        'downlinkSpeedMode': 'SPEED_50GB',
        'uplinkSets': [
            deepcopy(uplink_set['us-enet-Bside']),
            deepcopy(uplink_set['us-untagged']),
        ],
    },
    'Enc2-50G-EDIT-LIG': {
        'name': 'Enc2-50G-EDIT-LIG',
        'interconnectMapTemplate': [
            {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
            {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
             'enclosureIndex': 1},
            {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
            {'bay': 6, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        ],
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'downlinkSpeedMode': 'SPEED_50GB',
        'uplinkSets': [
        ],
    },
    'Enc3-50G-LIG': {
        'name': 'Enc3-50G-LIG',
        'interconnectMapTemplate': Enc3Map,
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'downlinkSpeedMode': 'SPEED_50GB',
        'uplinkSets': [
            deepcopy(uplink_set['us-bay3-fcoe']),
            deepcopy(uplink_set['us-tunnel']),
            deepcopy(uplink_set['us-untagged']),
            deepcopy(uplink_set['us-tagged'])
        ],
    },
    'Enc3-50G-Aside-LIG': {
        'name': 'Enc3-50G-Aside-LIG',
        'interconnectMapTemplate': [
            {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
            {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
            {'bay': 3, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
        ],
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantASide',
        'downlinkSpeedMode': 'SPEED_50GB',
        'uplinkSets': [
            deepcopy(uplink_set['us-enet-Aside']),
        ],
    },
    'Enc3-50G-Bside-LIG': {
        'name': 'Enc3-50G-Bside-LIG',
        'interconnectMapTemplate': [
            {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
            {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
            {'bay': 6, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
        ],
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantBSide',
        'downlinkSpeedMode': 'SPEED_50GB',
        'uplinkSets': [
            deepcopy(uplink_set['us-enet-Bside']),
        ],
    },
    'Enc3-50G-EDIT-LIG': {
        'name': 'Enc3-50G-EDIT-LIG',
        'interconnectMapTemplate': Enc3Map,
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'downlinkSpeedMode': 'SPEED_50GB',
        'uplinkSets': [
        ],
    },
}

# LIGs for Create LIG Negative test cases. Error returned as 400
EncX_ligs_400errs = \
    [

        # This generates LIG request with UNSUPPORTED downlinkSpeedMode
        {
            'ligBody': {
                'name': 'err-tbird-lig-UNSUPPORTED-speedmode',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': [
                    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 2},
                    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2},
                ],
                'enclosureIndexes': [1, 2],
                'interconnectBaySet': 3,
                'redundancyType': 'HighlyAvailable',
                'downlinkSpeedMode': 'UNSUPPORTED',
                'uplinkSets': [
                ]
            },
            'status_code': '400',
            'errorCode': 'CRM_INVALID_DOWNLINKSPEEDMODE',
        },

        # This generates LIG request with UNKNOWN downlinkSpeedMode
        {
            'ligBody': {
                'name': 'err-tbird-lig-UNKNOWN-speedmode',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': [
                    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 2},
                    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2},
                ],
                'enclosureIndexes': [1, 2],
                'interconnectBaySet': 3,
                'redundancyType': 'HighlyAvailable',
                'downlinkSpeedMode': 'UNKNOWN',
                'uplinkSets': [
                ]
            },
            'status_code': '400',
            'errorCode': 'CRM_INVALID_DOWNLINKSPEEDMODE',
        },

        # This generates LIG request with NOT_APPLICABLE downlinkSpeedMode
        {
            'ligBody': {
                'name': 'err-tbird-lig-NOT_APPLICABLE-speedmode',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': [
                    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 2},
                    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2},
                ],
                'enclosureIndexes': [1, 2],
                'interconnectBaySet': 3,
                'redundancyType': 'HighlyAvailable',
                'downlinkSpeedMode': 'NOT_APPLICABLE',
                'uplinkSets': [
                ]
            },
            'status_code': '400',
            'errorCode': 'CRM_INVALID_DOWNLINKSPEEDMODE',
        },

        # This generates LIG request with Invalid downlinkSpeedMode type
        {
            'ligBody': {
                'name': 'err-tbird-lig-Invalid-speedmode',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': [
                    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 2},
                    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2},
                ],
                'enclosureIndexes': [1, 2],
                'interconnectBaySet': 3,
                'redundancyType': 'HighlyAvailable',
                #                'downlinkSpeedMode': ["*SPEED_10GB?"],
                'downlinkSpeedMode': "SPEED_10GB_Err",
                'uplinkSets': [
                ]
            },
            'status_code': '400',
            'errorCode': 'INVALID_JSON_DATA_TYPE'
        },

        # This generates LIG request with Invalid downlinkSpeedMode
        {
            'ligBody': {
                'name': 'err-tbird-lig-Invalid-speedmodeType',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': [
                    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 2},
                    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2},
                ],
                'enclosureIndexes': [1, 2],
                'interconnectBaySet': 3,
                'redundancyType': 'HighlyAvailable',
                'downlinkSpeedMode': 'SPEED_10gb',
                'uplinkSets': [
                ]
            },
            'status_code': '400',
            'errorCode': 'INVALID_JSON_DATA_TYPE',
        },

        # This generates LIG request with Invalid downlinkSpeedMode
        {
            'ligBody': {
                'name': 'err-tbird-lig-Invalid-speedmodeType',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': [
                    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 2},
                    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2},
                ],
                'enclosureIndexes': [1, 2],
                'interconnectBaySet': 3,
                'redundancyType': 'HighlyAvailable',
                'downlinkSpeedMode': [],
                'uplinkSets': [
                ]
            },
            'status_code': '400',
            'errorCode': 'INVALID_JSON_MAPPING',
        },

        # This generates 4 frame LIG request with 50G downlinkSpeedMode
        {
            'ligBody': {
                'name': 'err-tbird-lig-4ME-50G-speedmode',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': [
                    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 2},
                    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2},
                    {'bay': 3, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 3},
                    {'bay': 6, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 3},
                    {'bay': 6, 'enclosure': 4, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 4},
                    {'bay': 3, 'enclosure': 4, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 4},
                ],
                'enclosureIndexes': [1, 2, 3, 4],
                'interconnectBaySet': 3,
                'redundancyType': 'HighlyAvailable',
                'downlinkSpeedMode': 'SPEED_50GB',
                'uplinkSets': [
                ]
            },
            #            'status_code': '400',
            'status_code': '412',
            'errorCode': 'CRM_INVALID_DOWNLINKSPEEDMODE50G_4OR5FRAME_ME',
        },

    ]

# LIGs for Create LIG Negative test cases. Error returned in Task
EncX_ligs_taskerrs = \
    [

        # This generates LIG request with Blank downlinkSpeedMode
        {
            'ligBody': {
                'name': 'err-tbird-lig-Blank-speedmode',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': [
                    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 2},
                    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2},
                ],
                'enclosureIndexes': [1, 2],
                'interconnectBaySet': 3,
                'redundancyType': 'HighlyAvailable',
                'downlinkSpeedMode': [],
                'uplinkSets': [
                ]
            },
            'status_code': '202',
            'errorCode': 'CRM_INVALID_DOWNLINKSPEEDMODE',
            #            'errorMessage': 'LIG_usportmix_error'
        },

    ]

# LIGs for Edit LIG use cases
ligs = {
    'Enc2-EDIT-LIG': {'name': 'Enc2-EDIT-LIG',
                      'type': lig_type,
                      'enclosureType': 'SY12000',
                      'interconnectMapTemplate': [
                          {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                           'enclosureIndex': 1},
                          {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                           'enclosureIndex': 1},
                          {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                           'enclosureIndex': 2},
                          {'bay': 6, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                           'enclosureIndex': 2}
                      ],
                      'enclosureIndexes': [1, 2],
                      'interconnectBaySet': 3,
                      'redundancyType': 'Redundant',
                      'uplinkSets': [

                      ]
                      },
    'Enc3-EDIT-LIG': {'name': 'Enc3-EDIT-LIG',
                      'type': lig_type,
                      'enclosureType': 'SY12000',
                      'interconnectMapTemplate': Enc3Map,
                      'enclosureIndexes': [1, 2, 3],
                      'interconnectBaySet': 3,
                      'redundancyType': 'HighlyAvailable',
                      'uplinkSets': [
                      ]
                      },

}

# LIG edit test case to downgrade and upgrade speed
edit_ligs = {

    # Speed mode 50G to 25G
    'Enc2-50G-EDIT-LIG': {
        'ligBody': {
            'name': 'Enc2-EDIT-LIG',
            'interconnectMapTemplate': [
                {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                 'enclosureIndex': 1},
                {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                 'enclosureIndex': 1},
                {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
                {'bay': 6, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
            ],
            'enclosureIndexes': [1, 2],
            'interconnectBaySet': 3,
            'redundancyType': 'Redundant',
            'downlinkSpeedMode': 'SPEED_25GB',
            'uplinkSets': [
                deepcopy(uplink_set['us-tagged']),
            ],
        },
    },

    'Enc3-50G-EDIT-LIG': {
        'ligBody': {
            'name': 'Enc3-EDIT-LIG',
            'interconnectMapTemplate': Enc3Map,
            'enclosureIndexes': [1, 2, 3],
            'interconnectBaySet': 3,
            'redundancyType': 'HighlyAvailable',
            'downlinkSpeedMode': 'SPEED_25GB',
            'uplinkSets': [
                deepcopy(uplink_set['us-tagged']),
            ],
        },
    },

    # Speed mode 25G to 50G
    'Enc2-25G-EDIT-LIG': {
        'ligBody': {
            'name': 'Enc2-EDIT-LIG',
            'interconnectMapTemplate': [
                {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                 'enclosureIndex': 1},
                {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                 'enclosureIndex': 1},
                {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
                {'bay': 6, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
            ],
            'enclosureIndexes': [1, 2],
            'interconnectBaySet': 3,
            'redundancyType': 'Redundant',
            'downlinkSpeedMode': 'SPEED_50GB',
            'uplinkSets': [
            ],
        },
    },

    'Enc3-25G-EDIT-LIG': {
        'ligBody': {
            'name': 'Enc3-EDIT-LIG',
            'interconnectMapTemplate': Enc3Map,
            'enclosureIndexes': [1, 2, 3],
            'interconnectBaySet': 3,
            'redundancyType': 'HighlyAvailable',
            'downlinkSpeedMode': 'SPEED_50GB',
            'uplinkSets': [
                deepcopy(uplink_set['us-tagged']),
            ],
        },
    },

    # 25G LIG for 50G upgrade with QoS use case
    'Enc2-25G-LIG': {
        'ligBody': {
            'name': 'Enc2-25G-LIG',
            'interconnectMapTemplate': [
                {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                 'enclosureIndex': 1},
                {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                 'enclosureIndex': 1},
                {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
                {'bay': 6, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
            ],
            'enclosureIndexes': [1, 2],
            'interconnectBaySet': 3,
            'redundancyType': 'Redundant',
            'downlinkSpeedMode': 'SPEED_50GB',
            'uplinkSets': [
                deepcopy(uplink_set['us-bay3-fcoe']),
                deepcopy(uplink_set['us-tunnel']),
                deepcopy(uplink_set['us-untagged']),
                deepcopy(uplink_set['us-tagged'])
            ],
        },
    },
    'Enc3-25G-LIG': {
        'ligBody': {
            'name': 'Enc3-25G-LIG',
            'interconnectMapTemplate': Enc3Map,
            'enclosureIndexes': [1, 2, 3],
            'interconnectBaySet': 3,
            'redundancyType': 'HighlyAvailable',
            'downlinkSpeedMode': 'SPEED_50GB',
            'uplinkSets': [
                deepcopy(uplink_set['us-bay3-fcoe']),
                deepcopy(uplink_set['us-tunnel']),
                deepcopy(uplink_set['us-untagged']),
                deepcopy(uplink_set['us-tagged'])
            ],
        },
    },

    # 50G LIG for 50G to 25G downgrade with QoS use case
    'Enc2-50G-LIG': {
        'ligBody': {
            'name': 'Enc2-50G-LIG',
            'interconnectMapTemplate': [
                {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                 'enclosureIndex': 1},
                {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                 'enclosureIndex': 1},
                {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
                {'bay': 6, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
            ],
            'enclosureIndexes': [1, 2],
            'interconnectBaySet': 3,
            'redundancyType': 'Redundant',
            'downlinkSpeedMode': 'SPEED_25GB',
            'uplinkSets': [
                deepcopy(uplink_set['us-bay3-fcoe']),
                deepcopy(uplink_set['us-tunnel']),
                deepcopy(uplink_set['us-untagged']),
                deepcopy(uplink_set['us-tagged'])
            ],
        },
    },

    'Enc3-50G-LIG': {
        'ligBody': {
            'name': 'Enc3-50G-LIG',
            'interconnectMapTemplate': Enc3Map,
            'enclosureIndexes': [1, 2, 3],
            'interconnectBaySet': 3,
            'redundancyType': 'HighlyAvailable',
            'downlinkSpeedMode': 'SPEED_25GB',
            'uplinkSets': [
                deepcopy(uplink_set['us-bay3-fcoe']),
                deepcopy(uplink_set['us-tunnel']),
                deepcopy(uplink_set['us-untagged']),
                deepcopy(uplink_set['us-tagged'])
            ],
        },
    },

}

# LIGs for Edit LIG Negative test cases. Error returned as 400
EncX_edit_ligs_400errs = \
    [

        # This generates Edit LIG request with UNSUPPORTED downlinkSpeedMode type
        {
            'ligBody': {
                #                'name': 'err-tbird-lig-Invalid-speedmode',
                'name': 'Enc2-EDIT-LIG',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': [
                    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2},
                    {'bay': 6, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2}
                ],
                'enclosureIndexes': [1, 2],
                'interconnectBaySet': 3,
                'redundancyType': 'Redundant',
                #                'downlinkSpeedMode': ["*SPEED_10GB?"],
                'downlinkSpeedMode': 'UNSUPPORTED',
                'uplinkSets': [
                ]
            },
            'status_code': '400',
            'errorCode': 'CRM_INVALID_DOWNLINKSPEEDMODE'
        },

        # This generates LIG request with UNKNOWN downlinkSpeedMode
        {
            'ligBody': {
                'name': 'Enc2-EDIT-LIG',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': [
                    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2},
                    {'bay': 6, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2}
                ],
                'enclosureIndexes': [1, 2],
                'interconnectBaySet': 3,
                'redundancyType': 'Redundant',
                'downlinkSpeedMode': 'UNKNOWN',
                'uplinkSets': [
                ]
            },
            'status_code': '400',
            #            'errorCode': 'null',
            'errorCode': 'CRM_INVALID_DOWNLINKSPEEDMODE',
            'errorMessage': 'The specified downlinkSpeedMode of UNKNOWN is invalid.'
        },

        # This generates LIG request with NOT_APPLICABLE downlinkSpeedMode
        {
            'ligBody': {
                'name': 'Enc2-EDIT-LIG',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': [
                    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2},
                    {'bay': 6, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2}
                ],
                'enclosureIndexes': [1, 2],
                'interconnectBaySet': 3,
                'redundancyType': 'Redundant',
                'downlinkSpeedMode': 'NOT_APPLICABLE',
                'uplinkSets': [
                ]
            },
            'status_code': '400',
            'errorCode': 'CRM_INVALID_DOWNLINKSPEEDMODE',
            'errorMessage': 'The specified downlinkSpeedMode of NOT_APPLICABLE is invalid.'
        },

        # This generates LIG request with Invalid downlinkSpeedMode type
        {
            'ligBody': {
                #                'name': 'err-tbird-lig-Invalid-speedmode',
                'name': 'Enc2-EDIT-LIG',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': [
                    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2},
                    {'bay': 6, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2}
                ],
                'enclosureIndexes': [1, 2],
                'interconnectBaySet': 3,
                'redundancyType': 'Redundant',
                'downlinkSpeedMode': 'SPEED_10GB_Err',
                'uplinkSets': [
                ]
            },
            'status_code': '400',
            'errorCode': 'INVALID_JSON_DATA_TYPE'
        },

        # This generates LIG request with Invalid downlinkSpeedMode
        {
            'ligBody': {
                #                'name': 'err-tbird-lig-Invalid-speedmodeType',
                'name': 'Enc2-EDIT-LIG',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': [
                    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2},
                    {'bay': 6, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2}
                ],
                'enclosureIndexes': [1, 2],
                'interconnectBaySet': 3,
                'redundancyType': 'Redundant',
                'downlinkSpeedMode': 'SPEED_10gb',
                'uplinkSets': [
                ]
            },
            'status_code': '400',
            'errorCode': 'INVALID_JSON_DATA_TYPE',
        },

        # This generates LIG request with Invalid downlinkSpeedMode
        {
            'ligBody': {
                'name': 'Enc2-EDIT-LIG',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': [
                    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                     'enclosureIndex': 1},
                    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2},
                    {'bay': 6, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module',
                     'enclosureIndex': 2}
                ],
                'enclosureIndexes': [1, 2],
                'interconnectBaySet': 3,
                'redundancyType': 'Redundant',
                'downlinkSpeedMode': [],
                'uplinkSets': [
                ]
            },
            'status_code': '400',
            'errorCode': 'INVALID_JSON_MAPPING',
            'errorMessage': 'The specified downlinkSpeedMode of NOT_APPLICABLE is invalid.'
        },

    ]

# LIGs for Edit LIG Negative test cases. Error returned in Task
EncX_edit_ligs_taskerrs = \
    [
        #     No Edit LIG task error use cases for this feature
    ]

serveradmin_user = {"type": "UserAndPermissions", "userName": "serveradmin", "fullName": "serveradmin",
                    "password": "serveradmin", "emailAddress": "", "officePhone": "", "mobilePhone": "",
                    "enabled": True, "roles": ["Server administrator"]}

enc_group = {
    'Enc2-25G-EG':
        {'name': 'Enc2-25G-EG',
         'enclosureCount': 2,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-25G-LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-25G-LIG'}],
         'ipAddressingMode': "DHCP",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },

    'Enc2-AB-25G-EG':
        {'name': 'Enc2-AB-25G-EG',
         'enclosureCount': 2,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-25G-Aside-LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-25G-Bside-LIG'}],
         'ipAddressingMode': "DHCP",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },

    'Enc2-50G-EG':
        {'name': 'Enc2-50G-EG',
         'enclosureCount': 2,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-50G-LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-50G-LIG'}],
         'ipAddressingMode': "DHCP",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },

    'Enc2-AB-50G-EG':
        {'name': 'Enc2-AB-50G-EG',
         'enclosureCount': 2,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-50G-Aside-LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-50G-Bside-LIG'}],
         'ipAddressingMode': "DHCP",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },

    'Enc3-25G-EG':
        {'name': 'Enc3-25G-EG',
         'enclosureCount': ENC_COUNT,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc3-25G-LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc3-25G-LIG'}],
         'ipAddressingMode': "DHCP",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },

    'Enc3-AB-25G-EG':
        {'name': 'Enc3-AB-25G-EG',
         'enclosureCount': ENC_COUNT,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc3-25G-Aside-LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc3-25G-Bside-LIG'}],
         'ipAddressingMode': "DHCP",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },

    'Enc3-50G-EG':
        {'name': 'Enc3-50G-EG',
         'enclosureCount': ENC_COUNT,
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

    'Enc3-AB-50G-EG':
        {'name': 'Enc3-AB-50G-EG',
         'enclosureCount': ENC_COUNT,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc3-50G-Aside-LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc3-50G-Bside-LIG'}],
         'ipAddressingMode': "DHCP",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },

}

LE = 'LE'

les = {
    'name': 'SPEED-LE',
    'enclosureUris': None,
    'enclosureGroupUri': None,
    'firmwareBaselineUri': None,
    'forceInstallFirmware': False
}

# Bay 1 - Mezzanine 3 Synergy 6810C 25/50Gb Ethernet Adptr (Quagmire I)
# Bay 2 - Mezzanine 3 Synergy 4820 10/25Gb CNA (Quack)
# Bay 3 - Mezzanine 3 Synergy 6820C 25/50Gb CNA (Quagmire II)

# Profile data for A + B LIs
profilesAB25 = {
    'Enc1-Profile2': {
        'payload': {
            'name': 'Enc1-Profile2',
            'type': ServerProfile_type,
            'serverHardwareUri': '{}, bay {}'.format(ENC_1, QUACKBAY),
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:EncN-XX-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                     'portId': 'Mezz 3:1-a',
                     'requestedMbps': '7500', 'networkUri': 'NS:netset10G'},
                    {'id': 3, 'name': 'conn-enet-2a', 'functionType': 'Ethernet',
                     'portId': 'Mezz 3:2-a',
                     'requestedMbps': '10000', 'networkUri': 'ETH:net_409'},
                ],
            },
        },
        'IP': '172.16.x.x',
    },
    'Enc1-Profile1': {
        'payload': {
            'name': 'Enc1-Profile1',
            'type': ServerProfile_type,
            'serverHardwareUri': '{}, bay {}'.format(ENC_1, QUAGMIREBAY),
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:EncN-XX-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                     'portId': 'Mezz 3:1-a',
                     'requestedMbps': '7500', 'networkUri': 'NS:netset10G'},
                    {'id': 3, 'name': 'conn-enet-2a', 'functionType': 'Ethernet',
                     'portId': 'Mezz 3:2-a',
                     'requestedMbps': '10000', 'networkUri': 'ETH:net_409'},
                ],
            },
        },
        'IP': '172.16.x.x',
    },
    'Enc3-Profile3': {
        'payload': {
            'name': 'Enc3-Profile3',
            'type': ServerProfile_type,
            'serverHardwareUri': '{}, bay {}'.format(ENC_3, QUAGMIRE2BAY),
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_3,
            'enclosureGroupUri': 'EG:EncN-XX-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                     'portId': 'Mezz 3:1-a',
                     'requestedMbps': '7500', 'networkUri': 'NS:netset10G'},
                    {'id': 3, 'name': 'conn-enet-2a', 'functionType': 'Ethernet',
                     'portId': 'Mezz 3:2-a',
                     'requestedMbps': '10000', 'networkUri': 'ETH:net_409'},
                ],
            },
        },
        'IP': '172.16.x.x',
    }
}

# Profile data when LI speed mode is 25Gb
profiles25 = {
    'Enc1-Profile1': {
        'payload': {
            'name': 'Enc1-Profile1',
            'type': ServerProfile_type,
            'serverHardwareUri': '{}, bay {}'.format(ENC_1, QUAGMIREBAY),
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:EncN-XX-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 11, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '25000', 'networkUri': 'NS:netset25G', 'lagName': 'LAG1'},
                    {'id': 21, 'name': 'conn-netset-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                     'requestedMbps': '25000', 'networkUri': 'NS:netset25G', 'lagName': 'LAG1'},
                ],
            },
        },
        'IP': '172.16.x.x',
        'handle': None
    },
    'Enc1-Profile2': {
        'payload': {
            'name': 'Enc1-Profile2',
            'type': ServerProfile_type,
            'serverHardwareUri': '{}, bay {}'.format(ENC_1, QUACKBAY),
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:EncN-XX-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 11, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                     'portId': 'Mezz 3:1-a',
                     'requestedMbps': '10000', 'maximumMbps': '25000', 'networkUri': 'NS:netset10G', 'lagName': 'LAG1'},
                    {'id': 21, 'name': 'conn-netset-2a', 'functionType': 'Ethernet',
                     'portId': 'Mezz 3:2-a',
                     'requestedMbps': '10000', 'maximumMbps': '25000', 'networkUri': 'NS:netset10G',
                     'lagName': 'LAG1'},
                ],

            },
        },
        'IP': '172.16.1.2',
        'handle': None
    },
    'Enc3-Profile3': {
        'payload': {
            'name': 'Enc3-Profile3',
            'type': ServerProfile_type,
            'serverHardwareUri': '{}, bay {}'.format(ENC_3, QUAGMIRE2BAY),
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_3,
            'enclosureGroupUri': 'EG:EncN-XX-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 11, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '25000', 'networkUri': 'NS:netset25G', 'lagName': 'LAG1'},
                    {'id': 21, 'name': 'conn-netset-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                     'requestedMbps': '25000', 'networkUri': 'NS:netset25G', 'lagName': 'LAG1'},
                ],
            },
        },
        'IP': '172.16.x.x',
        'handle': None
    }
}

profiles50to25 = {

    # no changes required for following profiles during 50G to 25G speedchange
    # just verify Ping continuity
    # Quack profile (Enc1 Bay 2; Enc1-Profile2)
    # as connection BW is less than 25G

    'Enc1-Profile2': {
        'payload': {
            'name': 'Enc1-Profile2',
            'type': ServerProfile_type,
            'serverHardwareUri': '{}, bay {}'.format(ENC_1, QUACKBAY),
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:EncN-XX-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 11, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                     'portId': 'Mezz 3:1-a',
                     'requestedMbps': '10000', 'maximumMbps': '25000', 'networkUri': 'NS:netset10G', 'lagName': 'LAG1'},
                    {'id': 12, 'name': 'conn-fcoe-1b', 'functionType': 'FibreChannel',
                     'portId': 'Mezz 3:1-b',
                     'requestedMbps': '10000', 'networkUri': 'FCOE:fcoenetwork'},
                    {'id': 21, 'name': 'conn-netset-2a', 'functionType': 'Ethernet',
                     'portId': 'Mezz 3:2-a',
                     'requestedMbps': '10000', 'maximumMbps': '25000', 'networkUri': 'NS:netset10G',
                     'lagName': 'LAG1'},
                ],
            },
        },
        'IP': '172.16.x.x',
        'handle': None
    },
    'Enc3-Profile3': {
        'payload': {
            'name': 'Enc3-Profile3',
            'type': ServerProfile_type,
            'serverHardwareUri': '{}, bay {}'.format(ENC_3, QUAGMIRE2BAY),
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_3,
            'enclosureGroupUri': 'EG:EncN-XX-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '10000', 'networkUri': 'NS:netset50G', 'lagName': 'LAG1'},
                    {'id': 2, 'name': 'conn-netset-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                     'requestedMbps': '10000', 'networkUri': 'NS:netset50G', 'lagName': 'LAG1'},
                    {'id': 22, 'name': 'conn-untagged', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                     'requestedMbps': '5000', 'networkUri': 'ETH:untaggednetwork1', },
                ],
            },
        },
        'IP': '172.16.x.x',
        'handle': None
    }

}

profiles50 = {
    'Enc1-Profile1': {
        'payload': {
            'name': 'Enc1-Profile1',
            'type': ServerProfile_type,
            'serverHardwareUri': '{}, bay {}'.format(ENC_1, QUAGMIREBAY),
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:EncN-XX-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 11, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '45000', 'networkUri': 'NS:netset50G', 'lagName': 'LAG1'},
                    {'id': 21, 'name': 'conn-netset-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                     'requestedMbps': '45000', 'networkUri': 'NS:netset50G', 'lagName': 'LAG1'},
                    {'id': 22, 'name': 'conn-untagged', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                     'requestedMbps': '5000', 'networkUri': 'ETH:untaggednetwork1', },
                ],
            },
        },
        'IP': '172.16.x.x',
        'handle': None
    },
}

# edit profile data with FCoE connections
edit_profiles_50Gto25G = {

    # no changes required for Quack profile (Enc1 Bay 2; Enc1-Profile2)
    # as connection BW is less than 25G

    # Edit remaining profiles with connection BW less than 25Gb

    'Enc1-Profile1': {
        'payload': {
            'name': 'Enc1-Profile1',
            'type': ServerProfile_type,
            'serverHardwareUri': '{}, bay {}'.format(ENC_1, QUAGMIREBAY),
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            #            'enclosureGroupUri': 'EG:Enc2-25G-EG',
            'enclosureGroupUri': 'EG:EncN-XX-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 11, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '20000', 'networkUri': 'NS:netset50G', 'lagName': 'LAG1'},
                    {'id': 21, 'name': 'conn-netset-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                     'requestedMbps': '20000', 'networkUri': 'NS:netset50G', 'lagName': 'LAG1'},
                    {'id': 22, 'name': 'conn-untagged', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                     'requestedMbps': '5000', 'networkUri': 'ETH:untaggednetwork1', },
                ],
            },
        },
        'IP': '172.16.x.x',
        'handle': None
    },
}

# LI patch call data
li_downlinkSpeedMode = [
    {
        'op': 'replace',
        'path': '/downlinkSpeedMode',
        'value': 'UNSUPPORTED'
    }
]

# QoS configuration used for speed mode test cases
QoS_Fcoe = {
    'qosConfiguration': {
        'activeQosConfig': {
            'type': 'QosConfiguration',
            'configType': 'CustomWithFCoE',
            'qosTrafficClassifiers': [
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '50',
                        'egressDot1pValue': 0,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'Best effort',
                        'enabled': True
                    },
                    'qosClassificationMapping': {
                        'dot1pClassMapping': [
                            1,
                            0
                        ],
                        'dscpClassMapping': [
                            'DSCP 10, AF11',
                            'DSCP 12, AF12',
                            'DSCP 14, AF13',
                            'DSCP 8, CS1',
                            'DSCP 0, CS0'
                        ]
                    }
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '10',
                        'egressDot1pValue': 1,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'Class1',
                        'enabled': True
                    },
                    'qosClassificationMapping': None
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '5',
                        'egressDot1pValue': 4,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'Class2',
                        'enabled': False
                    },
                    'qosClassificationMapping': None
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '9',
                        'egressDot1pValue': 6,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'Class3',
                        'enabled': False
                    },
                    'qosClassificationMapping': None
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '12',
                        'egressDot1pValue': 7,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'Class4',
                        'enabled': False
                    },
                    'qosClassificationMapping': None
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': 'fcoe',
                        'egressDot1pValue': 3,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'FCoE lossless',
                        'enabled': True
                    },
                    'qosClassificationMapping': {
                        'dot1pClassMapping': [
                            3
                        ],
                        'dscpClassMapping': []
                    }
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '30',
                        'egressDot1pValue': 2,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'Medium',
                        'enabled': True
                    },
                    'qosClassificationMapping': {
                        'dot1pClassMapping': [
                            4,
                            3,
                            2
                        ],
                        'dscpClassMapping': [
                            'DSCP 18, AF21',
                            'DSCP 20, AF22',
                            'DSCP 22, AF23',
                            'DSCP 26, AF31',
                            'DSCP 28, AF32',
                            'DSCP 30, AF33',
                            'DSCP 34, AF41',
                            'DSCP 36, AF42',
                            'DSCP 38, AF43',
                            'DSCP 16, CS2',
                            'DSCP 24, CS3',
                            'DSCP 32, CS4'
                        ]
                    }
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '10',
                        'egressDot1pValue': 5,
                        'maxBandwidth': 10,
                        'realTime': True,
                        'className': 'Real time',
                        'enabled': True
                    },
                    'qosClassificationMapping': {
                        'dot1pClassMapping': [
                            5,
                            6,
                            7
                        ],
                        'dscpClassMapping': [
                            'DSCP 46, EF',
                            'DSCP 40, CS5',
                            'DSCP 48, CS6',
                            'DSCP 56, CS7'
                        ]
                    }
                }
            ],
            'uplinkClassificationType': 'DOT1P',
            'downlinkClassificationType': 'DOT1P_AND_DSCP',
            'name': None,
            'state': None,
            'description': None,
            'status': None,
            'eTag': None,
            'created': None,
            'modified': None,
            'category': 'qos-aggregated-configuration',
            'uri': None
        },
        'inactiveFCoEQosConfig': None,
        'inactiveNonFCoEQosConfig': None,
        'type': 'qos-aggregated-configuration',
        'name': None,
        'state': None,
        'status': None,
        'eTag': None,
        'modified': None,
        'created': None,
        'category': 'qos-aggregated-configuration',
        'uri': None
    }
}

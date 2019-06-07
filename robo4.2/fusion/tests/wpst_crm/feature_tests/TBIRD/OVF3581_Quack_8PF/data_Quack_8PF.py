from copy import deepcopy
import data_common
# from data_common import *

appliance_ip = '15.245.131.132'
RACK = 'AZ51'

ENC_1 = 'CN7545061V'
ENC_2 = 'CN7545085D'
ENCLOSURE_URIS = ['ENC:' + ENC_1, 'ENC:' + ENC_2]

frame = 2

# Interconnect Bay Set
IBS = 3

# Chloride type for the IBS
ENC_CLTYPE = data_common.CHLORIDE20

REDUNDANCY = 'HA'
LE = 'LE' + '-' + REDUNDANCY
LIG = 'LIG'
EG = 'EG' + '-' + REDUNDANCY
LI = LE + '-' + LIG

# This is to make test program working for A+B (2 LI) and HA (1 LI); mainly for uplinkset verification
LIs = [LI, LI]

POTASH3 = ENC_1 + ', ' + 'interconnect 3'
POTASH6 = ENC_2 + ', ' + 'interconnect 6'

# for EM RIS Efuse
FUSION_IP = appliance_ip
interface = 'bond0'
FUSION_USERNAME = 'Administrator'  # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'  # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'  # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'  # Fusion SSH Password
FUSION_PROMPT = '#'  # Fusion Appliance Prompt
FUSION_TIMEOUT = 180  # Timeout.  Move this out???
FUSION_NIC = 'bond0'  # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

N2N_TEST_CONN = 4
MAX_PF_PER_PORT = 8

TAG_NET_PREFIX = 'net_'
UNTAG_PREFIX = 'untag_'
TUNNEL_PREFIX = 'tunnel_'

NATIVE_VID = 403


def rlist(start, end, prefix=TAG_NET_PREFIX, suffix='', step=1):
    l = []
    for c in xrange(start, end + 1, step):
        l.append('%s%s%s' % (prefix, str(c), suffix))
    return l


# return smartlink 'True' for odd number count, for tagged network, the input is vlanId
def get_smartlink(count):
    smartlink = True
    if count % 2 == 0:
        smartlink = False
    return smartlink


########################################
# networks and network sets
########################################

# tagged networks with vlanId 401-409, smartLink is 'False' for networks with even number of vlanId
# used by S-Channel LAG test cases
tagged_nets = [{'name': n,
                'type': 'ethernet-networkV4',
                'purpose': 'General',
                'smartLink': get_smartlink(int(n[len(TAG_NET_PREFIX):])),
                'privateNetwork': False,
                'connectionTemplateUri': None,
                'ethernetNetworkType': 'Tagged',
                'vlanId': int(n[len(TAG_NET_PREFIX):])} for n in rlist(401, 409)]

tunnel_nets = [{'name': n,
                'type': 'ethernet-networkV4',
                'purpose': 'General',
                'smartLink': get_smartlink(int(n[len(TUNNEL_PREFIX):])),
                'privateNetwork': False,
                'connectionTemplateUri': None,
                'ethernetNetworkType': 'Tunnel',
                'vlanId': None} for n in rlist(1, 2, 'tunnel_')]

untagged_nets = [{'name': n,
                  'type': 'ethernet-networkV4',
                  'purpose': 'General',
                  'smartLink': get_smartlink(int(n[len(UNTAG_PREFIX):])),
                  'privateNetwork': False,
                  'connectionTemplateUri': None,
                  'ethernetNetworkType': 'Untagged',
                  'vlanId': None} for n in rlist(1, 2, 'untag_')]

ethernet_networks = tagged_nets + tunnel_nets + untagged_nets

network_sets = [{'name': 'netset_1', 'type': 'network-setV4', 'networkUris': rlist(403, 404),
                 'nativeNetworkUri': rlist(NATIVE_VID, NATIVE_VID)[0]},
                {'name': 'netset_2', 'type': 'network-setV4', 'networkUris': rlist(405, 406),
                 'nativeNetworkUri': None},
                {'name': 'netset_3', 'type': 'network-setV4', 'networkUris': rlist(404, 405),
                 'nativeNetworkUri': None}
                ]

########################################
# OV Uplinkset uplinks info
########################################
US_TAG_UPLINK = 'Q6'
US_TUNNEL_UPLINK = 'Q1:1'
US_UNTAG_UPLINK = 'Q1:2'

US_TAG_UPLINK_SET = 'US-tag'
US_TUNNEL_UPLINK_SET = 'US-tunnel'
US_UNTAG_UPLINK_SET = 'US-untag'

ALL_UPLINK_SETS = [US_TAG_UPLINK_SET, US_TUNNEL_UPLINK_SET, US_UNTAG_UPLINK_SET]

ASIDE_UPLINKS = [US_TAG_UPLINK, US_TUNNEL_UPLINK, US_UNTAG_UPLINK]
BSIDE_UPLINKS = ASIDE_UPLINKS

# different uplinkset uplink port representation in LIG
LIG_US_TAG_UPLINK = US_TAG_UPLINK
LIG_US_TUNNEL_UPLINK = 'Q1.1'
LIG_US_UNTAG_UPLINK = 'Q1.2'

# server downlink on Enc1 and Enc2
ENC1_SERVER_1_ENC1_DL = 'd3'
ENC1_SERVER_1_ENC2_DL = 'd15'

# servers downlinks mapped to Aside and Bside Potash
ASIDE_SERVER_DOWNLINKS = [ENC1_SERVER_1_ENC1_DL]
BSIDE_SERVER_DOWNLINKS = [ENC1_SERVER_1_ENC2_DL]

# Server Hardware Type used by Server Profile Template
SHT_GEN10 = 'SHT:SY 480 Gen10 1'
SHT_GEN9 = 'SHT:SY 480 Gen9 1'

# Note: There is no guarantee the SHT name will remain the same since test environment adapter
#       may change and each API run start with import where SHT is created brand new again.
#       Test will need to get the SHT from SH
TEST_SHT = SHT_GEN10

# server profile names
ENC1_SP_1_NAME = 'SP-%s-enc1-bay3' % RACK

# servers name for server with Quack
ENC1_SERVER_1 = '%s, bay 3' % ENC_1

# servers ethernet connections with networkset, tagged, tunnel and untag network
ENC1_SERVER_IP_NS_NATIVE = '10.13.0.11'
ENC1_SERVER_IP_NS_TAG = '10.14.0.11'
ENC1_SERVER_IP_TAG = '10.17.0.11'
ENC1_SERVER_IP_TUNNEL_UNTAG = '10.22.0.11'
ENC1_SERVER_IP_TUNNEL_TAG = '10.20.0.11'
ENC1_SERVER_IP_UNTAG = '10.25.0.11'

# servers ethernet connections IPs
PING_LIST = \
    [ENC1_SERVER_IP_NS_NATIVE, ENC1_SERVER_IP_NS_TAG, ENC1_SERVER_IP_TAG, ENC1_SERVER_IP_TUNNEL_UNTAG,
     ENC1_SERVER_IP_TUNNEL_TAG, ENC1_SERVER_IP_UNTAG]

servers = [ENC1_SERVER_1]
server_profile_names = [ENC1_SP_1_NAME]

# For disable downlink test cases for servers with local OS
ENC1_SERVERS = [
    {'sp_name': ENC1_SP_1_NAME,
     'sh_name': ENC1_SERVER_1,
     'enc1_downlink': ENC1_SERVER_1_ENC1_DL,
     'enc2_downlink': ENC1_SERVER_1_ENC2_DL,
     'ip': PING_LIST}
]

# information for ping processes and output files for profile connections network
# Used for traffic verification
CONN_TRAFFIC_INFOS = {
    'NS_NATIVE': {
        'IP': ENC1_SERVER_IP_NS_NATIVE,
        'filePrefix': 'ping_NS_NATIVE',
        'handle': None
    },
    'NS_TAG': {
        'IP': ENC1_SERVER_IP_NS_TAG,
        'filePrefix': 'ping_NS_TAG',
        'handle': None
    },
    'TAG': {
        'IP': ENC1_SERVER_IP_TAG,
        'filePrefix': 'ping_TAG',
        'handle': None
    },
    'TUNNEL_UNTAG': {
        'IP': ENC1_SERVER_IP_TUNNEL_UNTAG,
        'filePrefix': 'ping_TUNNEL_UNTAG',
        'handle': None
    },
    'TUNNEL_TAG': {
        'IP': ENC1_SERVER_IP_TUNNEL_TAG,
        'filePrefix': 'ping_TUNNEL_TAG',
        'handle': None
    },
    'UNTAG': {
        'IP': ENC1_SERVER_IP_UNTAG,
        'filePrefix': 'ping_UNTAG',
        'handle': None
    }
}

unused_subport1 = {"portNumber": 1, "portStatus": data_common.UNLINKED, "portStatusReason": data_common.SUBPORT_OK}


# Create expected downlink port subports info. Note that there will be no subport entry for the subport not
# in use for connection, except for subport 1, which has subport entry with Unlink/Ok
def make_subports_template(number_of_conn, max_subports_per_port, status, reason):
    # connection is defined on the last n subports based on the desired number of connection
    start_subport = max_subports_per_port - number_of_conn + 1
    subports = [{"portNumber": sn, "portStatus": status, "portStatusReason": reason} for sn in
                xrange(start_subport, max_subports_per_port + 1)]
    if start_subport != 1:
        subports.insert(0, unused_subport1)
    return deepcopy(subports)


if MAX_PF_PER_PORT == 4:
    SUBPORT_OFFSET = 0
else:
    SUBPORT_OFFSET = 1


# When all S-Channel LAGed connections are OK, this is the expected downlink subports entries
# "portNumber": n, "portStatus": "Linked", "portStatusReason": "Active"
# Note: for downlink not S-Channel LAGed the portStatusReason is "Ok"
dl_subports_all_up_active_template = \
    make_subports_template(N2N_TEST_CONN, MAX_PF_PER_PORT, data_common.LINKED, data_common.ACTIVE)

# subport Unlinked due to SmartLink
# {"portNumber": n, "portStatus": "Unlinked", "portStatusReason": "SmartLink"}
dl_subports_all_down_smart_template = \
    make_subports_template(N2N_TEST_CONN, MAX_PF_PER_PORT, data_common.UNLINKED, data_common.SMARTLINK)

# subport Unlinked due to Downlink is Disabled
# Note that the subport 1 will contain the same value
# {"portNumber": n, "portStatus": "Unlinked", "portStatusReason": "AdminDisabled"}
dl_subports_all_down_disabled_template = \
    make_subports_template(N2N_TEST_CONN, MAX_PF_PER_PORT, data_common.UNLINKED, data_common.DISABLED)
dl_subports_all_down_disabled_template[0] = {"portNumber": 1, "portStatus": data_common.UNLINKED,
                                             "portStatusReason": data_common.DISABLED}

##################################
# uplinksets definitions in LIG
##################################

uplink_sets_in_lig = [
    {
        'name': 'US-tag',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': rlist(401, 409),
        'lacpTimer': 'Long',
        'mode': 'Auto',
        'nativeNetworkUri': rlist(NATIVE_VID, NATIVE_VID)[0],
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': LIG_US_TAG_UPLINK, 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': LIG_US_TAG_UPLINK, 'speed': 'Auto'}
        ]
    },
    {
        'name': 'US-tunnel',
        'ethernetNetworkType': 'Tunnel',
        'networkType': 'Ethernet',
        'networkUris': rlist(2, 2, 'tunnel_'),
        'lacpTimer': 'Long',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': LIG_US_TUNNEL_UPLINK, 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': LIG_US_TUNNEL_UPLINK, 'speed': 'Auto'}
        ]
    },
    {
        'name': 'US-untag',
        'ethernetNetworkType': 'Untagged',
        'networkType': 'Ethernet',
        'networkUris': rlist(2, 2, 'untag_'),
        'lacpTimer': 'Long',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': LIG_US_UNTAG_UPLINK, 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': LIG_US_UNTAG_UPLINK, 'speed': 'Auto'}
        ]
    }
]

##################################
# Interconnect bays configurations
# 2 or 3 Frames, IBS3, CL-20
##################################

InterconnectMapTemplate = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
    ]

ligs = [
    {'name': LIG,
     'interconnectMapTemplate': InterconnectMapTemplate,
     'enclosureIndexes': [x for x in xrange(1, frame + 1)],
     'interconnectBaySet': IBS,
     'redundancyType': 'HighlyAvailable',
     'uplinkSets': list(uplink_sets_in_lig)
     }
]

enc_group = {
    EG:
        {'name': EG,
         'enclosureCount': frame,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG}],
         'ipAddressingMode': "External"
         }
}

###
# All logical enclosures
###
les = {
    LE:
        {'name': LE,
         'enclosureUris': ENCLOSURE_URIS,
         'enclosureGroupUri': 'EG:' + EG,
         'firmwareBaselineUri': None,
         'forceInstallFirmware': False
         }
}

#################
# Server Profiles
#################

conn_filler_pf1to4 = [
    {'name': 'conn-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
     'networkUri': 'ETH:' + rlist(401, 401)[0], 'lagName': 'LAG1'},
    {'name': 'conn-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
     'networkUri': 'ETH:' + rlist(402, 402)[0], 'lagName': 'LAG2'},
    {'name': 'conn-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
     'networkUri': 'ETH:' + rlist(408, 408)[0], 'lagName': 'LAG3'},
    {'name': 'conn-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d',
     'networkUri': 'ETH:' + rlist(409, 409)[0], 'lagName': 'LAG4'},
    {'name': 'conn-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
     'networkUri': 'ETH:' + rlist(401, 401)[0], 'lagName': 'LAG1'},
    {'name': 'conn-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
     'networkUri': 'ETH:' + rlist(402, 402)[0], 'lagName': 'LAG2'},
    {'name': 'conn-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c',
     'networkUri': 'ETH:' + rlist(408, 408)[0], 'lagName': 'LAG3'},
    {'name': 'conn-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d',
     'networkUri': 'ETH:' + rlist(409, 409)[0], 'lagName': 'LAG4'}
]

conn_bronco_sclag_data = [
    {'name': 'conn-netset1-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
     'requestedMbps': data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT),
     'networkUri': 'NS:netset_1', 'lagName': 'LAG1'},
    {'name': 'conn-tag-1b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
     'requestedMbps': data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT),
     'networkUri': 'ETH:' + rlist(407, 407)[0], 'lagName': 'LAG2'},
    {'name': 'conn-tunnel-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
     'requestedMbps': data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT),
     'networkUri': 'ETH:tunnel_2', 'lagName': 'LAG3'},
    {'name': 'conn-untag-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d',
     'requestedMbps': data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT),
     'networkUri': 'ETH:untag_2', 'lagName': 'LAG4'},
    {'name': 'conn-netset1-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
     'requestedMbps': data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT),
     'networkUri': 'NS:netset_1', 'lagName': 'LAG1'},
    {'name': 'conn-tag-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
     'requestedMbps': data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT),
     'networkUri': 'ETH:' + rlist(407, 407)[0], 'lagName': 'LAG2'},
    {'name': 'conn-tunnel-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c',
     'requestedMbps': data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT),
     'networkUri': 'ETH:tunnel_2', 'lagName': 'LAG3'},
    {'name': 'conn-untag-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d',
     'requestedMbps': data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT),
     'networkUri': 'ETH:untag_2', 'lagName': 'LAG4'}
]

# connections on PF 5-8 for end to end traffic testing
conn_quack_sclag_pf5to8_data = [
    {'name': 'conn-netset1-1e', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-e',
     'requestedMbps': data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT),
     'networkUri': 'NS:netset_1', 'lagName': 'LAG5'},
    {'name': 'conn-tag-1f', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-f',
     'requestedMbps': data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT),
     'networkUri': 'ETH:' + rlist(407, 407)[0], 'lagName': 'LAG6'},
    {'name': 'conn-tunnel-1g', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-g',
     'requestedMbps': data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT),
     'networkUri': 'ETH:tunnel_2', 'lagName': 'LAG7'},
    {'name': 'conn-untag-1h', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-h',
     'requestedMbps': data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT),
     'networkUri': 'ETH:untag_2', 'lagName': 'LAG8'},
    {'name': 'conn-netset1-2e', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-e',
     'requestedMbps': data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT),
     'networkUri': 'NS:netset_1', 'lagName': 'LAG5'},
    {'name': 'conn-tag-2f', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-f',
     'requestedMbps': data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT),
     'networkUri': 'ETH:' + rlist(407, 407)[0], 'lagName': 'LAG6'},
    {'name': 'conn-tunnel-2g', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-g',
     'requestedMbps': data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT),
     'networkUri': 'ETH:tunnel_2', 'lagName': 'LAG7'},
    {'name': 'conn-untag-2h', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-h',
     'requestedMbps': data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT),
     'networkUri': 'ETH:untag_2', 'lagName': 'LAG8'}
]


def make_max_conn_data():
    if MAX_PF_PER_PORT == 4:
        return deepcopy(conn_bronco_sclag_data)
    else:
        c1 = deepcopy(conn_filler_pf1to4)
        c2 = deepcopy(conn_quack_sclag_pf5to8_data)
        c1.extend(c2)
        return deepcopy(c1)


def make_n2n_conn_data():
    if MAX_PF_PER_PORT == 4:
        return deepcopy(conn_bronco_sclag_data)
    else:
        return deepcopy(conn_quack_sclag_pf5to8_data)


# set up max connections data with S-Channel LAG
conn_max_sclag_data = make_max_conn_data()

# set up max connections data without S-Channel LAG, also make one connection in PF 6 without rbw
conn_max_nolag_data = deepcopy(conn_max_sclag_data)
for conn in conn_max_nolag_data:
    del conn['lagName']
    # prep for test with rbw from network preferred bandwidth
    if conn['name'] == 'conn-tag-1f':
        del conn['requestedMbps']


# Traffic test server profile; Also used for S-Channel LAG connection negative testing
server_profiles = [
    {'type': data_common.SP_TYPE,
     'serverHardwareUri': ENC1_SERVER_1,
     'enclosureUri': 'ENC:' + ENC_1,
     'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical',
     'macType': 'Physical',
     'wwnType': 'Physical',
     'name': ENC1_SP_1_NAME,
     'description': 'Gen10 WS2016 - Aside',
     'affinity': 'Bay',
     'connectionSettings': {
         'connections': make_n2n_conn_data()}
     }
]


# SP with connection  S-Channel LAG - used for negative testing
sp_lag_body_data = deepcopy(server_profiles[0])
sp_lag_body_data['connectionSettings']['connections'] = list(conn_max_sclag_data)

# SP with connection without S-Channel LAG - used for negative testing
sp_nolag_body_data = deepcopy(server_profiles[0])
sp_nolag_body_data['connectionSettings']['connections'] = list(conn_max_nolag_data)

#############################
# Server Profile Templates
#############################

spt_no_lag = {
    'type': data_common.SPT_TYPE,
    'serverHardwareTypeUri': TEST_SHT, 'enclosureGroupUri': 'EG:%s' % EG,
    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
    'name': 'spt_no_lag', 'description': 'Gen10 1 MZ card', 'affinity': 'Bay',
    'connectionSettings': {
        "manageConnections": True,
        'connections': list(conn_max_nolag_data)}
}

spt_lag = {
    'type': data_common.SPT_TYPE,
    'serverHardwareTypeUri': TEST_SHT, 'enclosureGroupUri': 'EG:%s' % EG,
    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
    'name': 'spt_lag', 'description': 'Gen10 1 MZ card', 'affinity': 'Bay',
    'connectionSettings': {
        "manageConnections": True,
        'connections': list(conn_max_sclag_data)}
}

# Used for Server Profile Creation from Server Profile Template
sp_with_spt_no_lag = {
    'type': data_common.SP_TYPE,
    'serverHardwareUri': ENC1_SERVER_1,
    'serverProfileTemplateUri': 'SPT:spt_no_lag',
    'name': 'sp_with_spt_no_lag',
    'description': 'Gen10 WS2016 - Aside',
    'affinity': 'Bay'
}

sp_with_spt_lag = {
    'type': data_common.SP_TYPE,
    'serverHardwareUri': ENC1_SERVER_1,
    'serverProfileTemplateUri': 'SPT:spt_lag',
    'name': 'sp_with_spt_lag',
    'description': 'Gen10 WS2016 - Aside',
    'affinity': 'Bay'
}

# --- Negative SPT testing ---

if MAX_PF_PER_PORT == 4:
    offset = 0
else:
    offset = 8

# max bandwidth and no duplicate network for connections per port
err_spt_exceed_max_bw = deepcopy(spt_no_lag)
err_spt_exceed_max_bw['connectionSettings']['connections'][0 + offset]['requestedMbps'] = \
    data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT) + 500

err_spt_exceed_max_bw_b = deepcopy(spt_no_lag)
err_spt_exceed_max_bw_b['connectionSettings']['connections'][0 + 4 + offset]['requestedMbps'] = \
    data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT) + 500

err_spt_dup_net_connections = deepcopy(spt_no_lag)
err_spt_dup_net_connections['connectionSettings']['connections'][1 + offset]['networkUri'] = 'ETH:' + rlist(403, 403)[0]

err_spt_dup_net_connections_b = deepcopy(spt_no_lag)
err_spt_dup_net_connections_b['connectionSettings']['connections'][1 + 4 + offset]['networkUri'] = 'ETH:' + \
                                                                                                   rlist(403, 403)[0]

err_spt_dup_net_connections_ns = deepcopy(spt_no_lag)
err_spt_dup_net_connections_ns['connectionSettings']['connections'][1 + offset]['networkUri'] = 'NS:netset_3'

# S-Channel LAGed connections
err_spt_different_net_same_lag_conn = deepcopy(spt_lag)
err_spt_different_net_same_lag_conn['connectionSettings']['connections'][1 + offset]['networkUri'] = 'ETH:' + \
                                                                                                     rlist(405, 405)[0]

err_spt_different_ns_same_lag_conn = deepcopy(spt_lag)
err_spt_different_ns_same_lag_conn['connectionSettings']['connections'][0 + offset]['networkUri'] = 'NS:netset_3'

err_spt_different_bw_same_lag_conn = deepcopy(spt_lag)
err_spt_different_bw_same_lag_conn['connectionSettings']['connections'][1 + offset]['requestedMbps'] = \
    data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT) - 1000

err_spt_list = \
    [
        {'errorCode': 'BW_TOTAL_LINKRATE_OVERFLOW_ERROR',
         'sptBody': err_spt_exceed_max_bw},
        {'errorCode': 'BW_TOTAL_LINKRATE_OVERFLOW_ERROR',
         'sptBody': err_spt_exceed_max_bw_b},
        {'errorCode': 'DuplicateNetworksPerPortError',
         'sptBody': err_spt_dup_net_connections},
        {'errorCode': 'DuplicateNetworksPerPortError',
         'sptBody': err_spt_dup_net_connections_b},
        {'errorCode': 'DuplicateNetworksPerPortError',
         'sptBody': err_spt_dup_net_connections_ns}
    ]

err_spt_scmlag_list = \
    [
        {'errorCode': 'MISMATCH_NETWORK_LAG_VIOLATION_ERROR',
         'sptBody': err_spt_different_net_same_lag_conn},
        {'errorCode': 'MISMATCH_NETWORK_LAG_VIOLATION_ERROR',
         'sptBody': err_spt_different_ns_same_lag_conn},
        {'errorCode': 'MISMATCH_BANDWIDTH_LAG_VIOLATION_ERROR',
         'sptBody': err_spt_different_bw_same_lag_conn}
    ]

##########################
# NEGATIVE Profile cases
##########################

# exceed max bandwidth connections on a physical port; BW_TOTAL_LINKRATE_OVERFLOW_ERROR
err_sp_exceed_max_bw = deepcopy(sp_nolag_body_data)
err_sp_exceed_max_bw['name'] = 'err_sp_exceed_max_bw'
err_sp_exceed_max_bw['connectionSettings']['connections'][0 + offset]['requestedMbps'] = \
    data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT) + 500

err_sp_exceed_max_bw_b = deepcopy(sp_nolag_body_data)
err_sp_exceed_max_bw_b['name'] = 'err_sp_exceed_max_bw_b'
err_sp_exceed_max_bw_b['connectionSettings']['connections'][0 + 4 + offset]['requestedMbps'] = \
    data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT) + 500

# duplicate network used in connections defined on a physical port; DuplicateNetworksPerPortError
# This case first connection with net_403 and net_404 in networkset netset_01, the second connection has net_403
err_sp_dup_net_connections = deepcopy(sp_nolag_body_data)
err_sp_dup_net_connections['name'] = 'err_sp_dup_net_connections'
err_sp_dup_net_connections['connectionSettings']['connections'][1 + offset]['networkUri'] = 'ETH:' + rlist(403, 403)[0]

err_sp_dup_net_connections_b = deepcopy(sp_nolag_body_data)
err_sp_dup_net_connections_b['name'] = 'err_sp_dup_net_connections_b'
err_sp_dup_net_connections_b['connectionSettings']['connections'][1 + 4 + offset]['networkUri'] = 'ETH:' + \
                                                                                                  rlist(403, 403)[0]

# duplicate network used in connections defined on a physical port; DuplicateNetworksPerPortError
# This case first connection with net_403 and net_404 in network set netset_1,
# the second connection has net_404 and net_405 in network set netset_3
err_sp_dup_net_connections_ns = deepcopy(sp_nolag_body_data)
err_sp_dup_net_connections_ns['name'] = 'err_sp_dup_net_connections_ns'
err_sp_dup_net_connections_ns['connectionSettings']['connections'][1 + offset]['networkUri'] = 'NS:netset_3'

# connection with network that is not provisioned
err_sp_conn_non_provisioned_net = deepcopy(sp_nolag_body_data)
err_sp_conn_non_provisioned_net['name'] = 'err_sp_conn_non_provisioned_net'
err_sp_conn_non_provisioned_net['connectionSettings']['connections'][1 + offset]['networkUri'] = 'ETH:tunnel_1'

# --- S-Channel LAG connection error case ---
# S-Channel LAGed connections should have the same network; MISMATCH_NETWORK_LAG_VIOLATION_ERROR
err_sp_different_net_same_lag_conn = deepcopy(sp_lag_body_data)
err_sp_different_net_same_lag_conn['name'] = 'err_sp_different_net_same_lag_conn'
err_sp_different_net_same_lag_conn['connectionSettings']['connections'][1 + offset]['networkUri'] = 'ETH:' + \
                                                                                                    rlist(405, 405)[0]

# S-Channel LAGed connections should have the same network set, LAG1 conn1 with netset_3, the other netset_1
# MISMATCH_NETWORK_LAG_VIOLATION_ERROR
err_sp_different_ns_same_lag_conn = deepcopy(sp_lag_body_data)
err_sp_different_ns_same_lag_conn['name'] = 'err_sp_different_ns_same_lag_conn'
err_sp_different_ns_same_lag_conn['connectionSettings']['connections'][0 + offset]['networkUri'] = 'NS:netset_3'

# S-Channel LAGed connections should have the same bandwidth; MISMATCH_BANDWIDTH_LAG_VIOLATION_ERROR
err_sp_different_bw_same_lag_conn = deepcopy(sp_lag_body_data)
err_sp_different_bw_same_lag_conn['name'] = 'err_sp_different_bw_same_lag_conn'
err_sp_different_bw_same_lag_conn['connectionSettings']['connections'][1 + offset]['requestedMbps'] = \
    data_common.get_enet_rbw(ENC_CLTYPE, MAX_PF_PER_PORT) - 1000

err_sp_list = \
    [
        {'errorCode': 'BW_TOTAL_LINKRATE_OVERFLOW_ERROR',
         'spBody': err_sp_exceed_max_bw},
        {'errorCode': 'BW_TOTAL_LINKRATE_OVERFLOW_ERROR',
         'spBody': err_sp_exceed_max_bw_b},
        {'errorCode': 'DuplicateNetworksPerPortError',
         'spBody': err_sp_dup_net_connections},
        {'errorCode': 'DuplicateNetworksPerPortError',
         'spBody': err_sp_dup_net_connections_b},
        {'errorCode': 'DuplicateNetworksPerPortError',
         'spBody': err_sp_dup_net_connections_ns},
        {'errorCode': 'UnavailableEthernetFCError',
         'spBody': err_sp_conn_non_provisioned_net}
    ]

err_sp_scmlag_list = \
    [
        {'errorCode': 'MISMATCH_NETWORK_LAG_VIOLATION_ERROR',
         'spBody': err_sp_different_net_same_lag_conn},
        {'errorCode': 'MISMATCH_NETWORK_LAG_VIOLATION_ERROR',
         'spBody': err_sp_different_ns_same_lag_conn},
        {'errorCode': 'MISMATCH_BANDWIDTH_LAG_VIOLATION_ERROR',
         'spBody': err_sp_different_bw_same_lag_conn}
    ]

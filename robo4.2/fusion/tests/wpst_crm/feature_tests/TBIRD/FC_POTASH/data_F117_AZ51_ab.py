"""
data file for testing FC DirectAttach with LE A+B redundancy for enclosure AZ51
"""

from copy import deepcopy
import data_common

appliance_ip = '15.245.131.132'
RACK = 'AZ51'

ENC_1 = 'CN7545061V'
ENC_2 = 'CN7545085D'
ENCLOSURE_URIS = ['ENC:' + ENC_1, 'ENC:' + ENC_2]
SP_TYPE = 'ServerProfileV11'

frame = 2

# Interconnect Bay Set
IBS = 3

MZ = 'Mezz ' + str(IBS)

# Chloride type for the IBS
ENC_CLTYPE = data_common.CHLORIDE20

REDUNDANCY = 'AB'
LE = 'LE' + '-' + REDUNDANCY
LIG_A = 'LIG-A'
LIG_B = 'LIG-B'
EG = 'EG' + '-' + REDUNDANCY
LI_A = LE + '-' + LIG_A
LI_B = LE + '-' + LIG_B
LIs = [LI_A, LI_B]

POTASH3 = ENC_1 + ', ' + 'interconnect 3'
POTASH6 = ENC_2 + ', ' + 'interconnect 6'

# for EM RIS Efuse
FUSION_IP = appliance_ip
interface = 'bond0'
FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'         # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'       # Fusion SSH Password
FUSION_PROMPT = '#'                  # Fusion Appliance Prompt
FUSION_TIMEOUT = 180                 # Timeout.  Move this out???
FUSION_NIC = 'bond0'                 # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

########################################
# OV Uplinkset uplinks info
########################################
US_DA1_UPLINKS = ['Q4:3', 'Q5:1']
US_DA3_UPLINKS = ['Q4:3', 'Q4:4']

IC3_DA_UPLINKS = US_DA1_UPLINKS
IC6_DA_UPLINKS = US_DA3_UPLINKS

US_FA1_UPLINKS = ['Q2:2']
US_FA3_UPLINKS = ['Q3:1']

IC3_FA_UPLINKS = US_FA1_UPLINKS
IC6_FA_UPLINKS = US_FA3_UPLINKS

ASIDE_UPLINK_SETS = ['US-DA1']
BSIDE_UPLINK_SETS = ['US-DA3']

ALL_UPLINK_SETS = ASIDE_UPLINK_SETS + BSIDE_UPLINK_SETS

# different uplinkset uplink port representation in LIG
LIG_ENET_UPLINK = 'Q2.1'
LIG_DA1_UPLINKS = ['Q4.3', 'Q5.1']
LIG_DA3_UPLINKS = ['Q4.3', 'Q4.4']
LIG_FA1_UPLINKS = ['Q2.2']
LIG_FA3_UPLINKS = ['Q3.1']

########################################
# DA uplink connected 3Par port portWwn
########################################
# connected to Tbird 3Par-B ports 0:2:1, 1:2:1 and 0:2:2, 1:2:2
IC3_DA_WWN_1 = '20:21:00:02:ac:01:2b:0b'
IC3_DA_WWN_2 = '21:21:00:02:ac:01:2b:0b'
IC6_DA_WWN_1 = '20:22:00:02:ac:01:2b:0b'
IC6_DA_WWN_2 = '21:22:00:02:ac:01:2b:0b'

ASIDE_HAPPY_CONNECTION_MAP = [IC3_DA_WWN_1, IC3_DA_WWN_2]
BSIDE_HAPPY_CONNECTION_MAP = [IC6_DA_WWN_1, IC6_DA_WWN_2]

########################################
# DA uplinks - 3par ports Dictionary
########################################
# For nameServer uplink DA port verification
IC3_UPLINKS_DA = [
    {'uplink': US_DA1_UPLINKS[0],
     'da_portwwn': IC3_DA_WWN_1},
    {'uplink': US_DA1_UPLINKS[1],
     'da_portwwn': IC3_DA_WWN_2}
]

IC6_UPLINKS_DA = [
    {'uplink': US_DA3_UPLINKS[0],
     'da_portwwn': IC6_DA_WWN_1},
    {'uplink': US_DA3_UPLINKS[1],
     'da_portwwn': IC6_DA_WWN_2}
]

# Enclosure 1 servers downlink on Enc1 and Enc2; 2 servers on each enclosure
ENC1_SERVER_1_ENC1_DL = 'd1'
ENC1_SERVER_1_ENC2_DL = 'd13'
ENC1_SERVER_2_ENC1_DL = 'd10'
ENC1_SERVER_2_ENC2_DL = 'd22'

# Enclosure 2 servers downlink on Enc1 and Enc2; 2 servers on each enclosure
ENC2_SERVER_1_ENC2_DL = 'd4'
ENC2_SERVER_1_ENC1_DL = 'd16'
ENC2_SERVER_2_ENC2_DL = 'd7'
ENC2_SERVER_2_ENC1_DL = 'd19'

# servers downlinks mapped to Aside and Bside Potash
ASIDE_SERVER_DOWNLINKS = [ENC1_SERVER_1_ENC1_DL, ENC1_SERVER_2_ENC1_DL,
                          ENC2_SERVER_1_ENC1_DL, ENC2_SERVER_2_ENC1_DL]
BSIDE_SERVER_DOWNLINKS = [ENC1_SERVER_1_ENC2_DL, ENC1_SERVER_2_ENC2_DL,
                          ENC2_SERVER_1_ENC2_DL, ENC2_SERVER_2_ENC2_DL]

# server profile names
ENC1_SP_1_NAME = 'SP-%s-enc1-bay1' % RACK
ENC1_SP_2_NAME = 'SP-%s-enc1-bay10' % RACK
ENC2_SP_1_NAME = 'SP-%s-enc2-bay4' % RACK
ENC2_SP_2_NAME = 'SP-%s-enc2-bay7' % RACK
ENC1_SP_1_BFS_NAME = 'SP-%s-BFS-enc1-bay10' % RACK
ENC2_SP_1_BFS_NAME = 'SP-%s-BFS-enc2-bay4' % RACK

# servers name
ENC1_SERVER_1 = '%s, bay 1' % ENC_1
ENC1_SERVER_2 = '%s, bay 10' % ENC_1
ENC2_SERVER_1 = '%s, bay 4' % ENC_2
ENC2_SERVER_2 = '%s, bay 7' % ENC_2

# servers static private IP
ENC1_SERVER_1_IP_A = '10.11.0.11'
ENC1_SERVER_2_IP_A = '10.11.0.12'      # Windows local and BFS static IP
ENC2_SERVER_1_IP_A = '10.11.0.14'      # Esx BFS server and Local RH6.7 static IP
ENC2_SERVER_2_IP_A = '10.11.0.13'

GW_IP_A = '10.11.0.1'
GW_IP_B = '10.12.0.1'

# ping list with server with local OS, Linux in first entry
PING_LIST_A = [ENC1_SERVER_1_IP_A, ENC1_SERVER_2_IP_A, ENC2_SERVER_1_IP_A, ENC2_SERVER_2_IP_A]

servers = [ENC1_SERVER_1, ENC1_SERVER_2, ENC2_SERVER_1, ENC2_SERVER_2]
server_profile_names = [ENC1_SP_1_NAME, ENC1_SP_2_NAME, ENC2_SP_1_NAME, ENC2_SP_2_NAME]

LINUX_BFS_USER = 'root'
LINUX_BFS_PWD = 'hpvse123'
LINUX_BFS_PROMPT = 'ESXi'

# For disable downlink test cases for servers with local OS
ENC1_SERVERS = [
    {'sp_name': ENC1_SP_1_NAME,
     'sh_name': ENC1_SERVER_1,
     'enc1_downlink': ENC1_SERVER_1_ENC1_DL,
     'enc2_downlink': ENC1_SERVER_1_ENC2_DL,
     'ip': ENC1_SERVER_1_IP_A},
    {'sp_name': ENC1_SP_2_NAME,
     'sh_name': ENC1_SERVER_2,
     'enc1_downlink': ENC1_SERVER_2_ENC1_DL,
     'enc2_downlink': ENC1_SERVER_2_ENC2_DL,
     'ip': ENC1_SERVER_2_IP_A}
]

ENC2_SERVERS = [
    {'sp_name': ENC2_SP_1_NAME,
     'sh_name': ENC2_SERVER_1,
     'enc1_downlink': ENC2_SERVER_1_ENC1_DL,
     'enc2_downlink': ENC2_SERVER_1_ENC2_DL,
     'ip': ENC2_SERVER_1_IP_A},
    {'sp_name': ENC2_SP_2_NAME,
     'sh_name': ENC2_SERVER_2,
     'enc1_downlink': ENC2_SERVER_2_ENC1_DL,
     'enc2_downlink': ENC2_SERVER_2_ENC2_DL,
     'ip': ENC2_SERVER_2_IP_A}
]

# BFS server: some enclosure has dual boot server with local OS and BFS,
# some has server with only BFS
BFS_ENC1_SERVERS = [
    {'sp_name': ENC1_SP_2_NAME,
     'sh_name': ENC1_SERVER_2,
     'os': 'Windows',
     'ip': ENC1_SERVER_2_IP_A}
]

BFS_ENC2_SERVERS = [
    {'sp_name': ENC2_SP_1_NAME,
     'sh_name': ENC2_SERVER_1,
     'os': 'Linux',
     'ip': ENC2_SERVER_1_IP_A}
]

# BFS servers ping list, need to put Linux BFS server in first entry since ssh will be used
BFS_PING_LIST = [BFS_ENC2_SERVERS[x]['ip'] for x in xrange(len(BFS_ENC2_SERVERS))]
BFS_PING_LIST.extend([BFS_ENC1_SERVERS[x]['ip'] for x in xrange(len(BFS_ENC1_SERVERS))])


##################################
# uplinksets definitions in LIG
##################################

uplink_sets_in_lig_A = [
    {
        'name': 'US-NET1',
        'consistencyChecking': 'ExactMatch',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['wpstnetwork1'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': LIG_ENET_UPLINK, 'speed': 'Auto'}
        ]
    },
    {
        'name': 'US-DA1',
        'consistencyChecking': 'ExactMatch',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['DA1'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': LIG_DA1_UPLINKS[0], 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': LIG_DA1_UPLINKS[1], 'speed': 'Auto'}
        ]
    },
    {
        'name': 'US-FA1',
        'consistencyChecking': 'ExactMatch',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['FA1'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': LIG_FA1_UPLINKS[0], 'speed': 'Auto'}
        ]
    }
]

uplink_sets_in_lig_B = [
    {
        'name': 'US-DA3',
        'consistencyChecking': 'ExactMatch',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['DA3'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': LIG_DA3_UPLINKS[0], 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': LIG_DA3_UPLINKS[1], 'speed': 'Auto'}
        ]
    },
    {
        'name': 'US-FA3',
        'consistencyChecking': 'ExactMatch',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['FA3'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': LIG_FA3_UPLINKS[0], 'speed': 'Auto'}
        ]
    }
]

##################################
# Interconnect bays configurations
# 2 or 3 Frames, IBS3, CL-20
##################################

InterconnectMapTemplate_A = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
         'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module',
         'enclosureIndex': 2}
    ]

InterconnectMapTemplate_B = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module',
         'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
         'enclosureIndex': 2}
    ]

ligs = [
    {'name': LIG_A,
     'interconnectMapTemplate': InterconnectMapTemplate_A,
     'enclosureIndexes': [x for x in xrange(1, frame + 1)],
     'interconnectBaySet': IBS,
     'redundancyType': 'NonRedundantASide',
     'uplinkSets': list(uplink_sets_in_lig_A)
     },
    {'name': LIG_B,
     'interconnectMapTemplate': InterconnectMapTemplate_B,
     'enclosureIndexes': [x for x in xrange(1, frame + 1)],
     'interconnectBaySet': IBS,
     'redundancyType': 'NonRedundantBSide',
     'uplinkSets': list(uplink_sets_in_lig_B)
     }
]

enc_group = {
    EG:
        {'name': EG,
         'enclosureCount': frame,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG_A},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG_B}],
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

###############
# LI Uplinksets
###############

# used for LI uplinkset updated

li_uplinksets = {
    'US_DA1_4Gb':
        {'name': 'US-DA1',
         'ethernetNetworkType': 'NotApplicable',
         'networkType': 'FibreChannel',
         'networkUris': [],
         'fcNetworkUris': ['DA1'],
         'fcoeNetworkUris': [],
         'manualLoginRedistributionState': 'Supported',
         'connectionMode': 'Auto',
         'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': US_DA1_UPLINKS[0],
                              'desiredSpeed': 'Speed4G'},
                             {'enclosure': ENC_1, 'bay': '3', 'port': US_DA1_UPLINKS[1],
                              'desiredSpeed': 'Speed4G'}],
         'logicalInterconnectUri': None},
    'US_DA1_8Gb':
        {'name': 'US-DA1',
         'ethernetNetworkType': 'NotApplicable',
         'networkType': 'FibreChannel',
         'networkUris': [],
         'fcNetworkUris': ['DA1'],
         'fcoeNetworkUris': [],
         'manualLoginRedistributionState': 'Supported',
         'connectionMode': 'Auto',
         'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': US_DA1_UPLINKS[0],
                              'desiredSpeed': 'Speed8G'},
                             {'enclosure': ENC_1, 'bay': '3', 'port': US_DA1_UPLINKS[1],
                              'desiredSpeed': 'Speed8G'}],
         'logicalInterconnectUri': None}
}

#################
# Server Profiles
#################
conn_data = [
    {'name': 'conn-net', 'functionType': 'Ethernet', 'portId': MZ + ':1-a',
     'requestedMbps': data_common.getEnetRBW(ENC_CLTYPE),
     'networkUri': 'ETH:wpstnetwork1'},
    {'name': 'conn-fc', 'functionType': 'FibreChannel', 'portId': MZ + ':1-b',
     'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
     'networkUri': 'FC:DA1'},
    {'name': 'conn-fc2', 'functionType': 'FibreChannel', 'portId': 'Auto',
     'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
     'networkUri': 'FC:DA3'}
]


def make_conn_data(data):
    """ copy and return connections for a server profile """
    return deepcopy(data)


server_profiles = [
    {'type': 'ServerProfileV11',
     'serverHardwareUri': ENC1_SERVER_1,
     'serverHardwareTypeUri': None,
     'enclosureUri': 'ENC:' + ENC_1,
     'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical',
     'macType': 'Physical',
     'wwnType': 'Physical',
     'name': ENC1_SP_1_NAME,
     'description': 'Blackbird rhel6.7 - Aside',
     'affinity': 'Bay',
     'connectionSettings': {
         'connections': make_conn_data(conn_data)}
     },
    {'type': SP_TYPE,
     'serverHardwareUri': ENC1_SERVER_2,
     'serverHardwareTypeUri': None,
     'enclosureUri': 'ENC:' + ENC_1,
     'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical',
     'macType': 'Physical',
     'wwnType': 'Physical',
     'name': ENC1_SP_2_NAME,
     'description': 'Blackbird Windows - Aside',
     'affinity': 'Bay',
     'connectionSettings': {
         'connections': make_conn_data(conn_data)}
     },
    {'type': SP_TYPE,
     'serverHardwareUri': ENC2_SERVER_1,
     'serverHardwareTypeUri': None,
     'enclosureUri': 'ENC:' + ENC_2,
     'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical',
     'macType': 'Physical',
     'wwnType': 'Physical',
     'name': ENC2_SP_1_NAME,
     'description': 'Blackbird Linux - Bside',
     'affinity': 'Bay',
     'connectionSettings': {
         'connections': make_conn_data(conn_data)}
     },
    {'type': SP_TYPE,
     'serverHardwareUri': ENC2_SERVER_2,
     'serverHardwareTypeUri': None,
     'enclosureUri': 'ENC:' + ENC_2,
     'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical',
     'macType': 'Physical',
     'wwnType': 'Physical',
     'name': ENC2_SP_2_NAME,
     'description': 'Blackbird Windows - Bside',
     'affinity': 'Bay',
     'connectionSettings': {
         'connections': make_conn_data(conn_data)}
     }
]

######################
# BFS server profiles
#######################
bfs_conn_data_a = [
    {'name': 'conn-net', 'functionType': 'Ethernet', 'portId': MZ + ':1-a',
     'requestedMbps': data_common.getEnetRBW(ENC_CLTYPE),
     'networkUri': 'ETH:wpstnetwork1'},
    {'name': 'conn-fc', 'functionType': 'FibreChannel', 'portId': 'Auto',
     'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
     'networkUri': 'FC:DA1',
     'boot': {'priority': 'Primary',
              'bootVolumeSource': 'UserDefined',
              'targets': [{'arrayWwpn': '20210002AC012B0B', 'lun': '1'}]}
     },
    {'name': 'conn-fc2', 'functionType': 'FibreChannel', 'portId': 'Auto',
     'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
     'networkUri': 'FC:DA3',
     'boot': {'priority': 'Secondary',
              'bootVolumeSource': 'UserDefined',
              'targets': [{'arrayWwpn': '20220002AC012B0B', 'lun': '1'}]}
     }
]

bfs_conn_data_b = make_conn_data(bfs_conn_data_a)
bfs_conn_data_b[1]['boot']['priority'] = 'Secondary'
bfs_conn_data_b[2]['boot']['priority'] = 'Primary'

bfs_server_profiles = [
    {'type': SP_TYPE,
     'serverHardwareUri': BFS_ENC1_SERVERS[0]['sh_name'],
     'serverHardwareTypeUri': None,
     'enclosureUri': 'ENC:' + ENC_1,
     'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical',
     'macType': 'Physical',
     'wwnType': 'Physical',
     'name': BFS_ENC1_SERVERS[0]['sp_name'],
     'description': 'Blackbird - Windows 2016 BFS Aside',
     'affinity': 'Bay',
     'bootMode': {'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto'},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'connectionSettings': {
         'connections': make_conn_data(bfs_conn_data_a)}
     },
    {'type': SP_TYPE,
     'serverHardwareUri': BFS_ENC2_SERVERS[0]['sh_name'],
     'serverHardwareTypeUri': None,
     'enclosureUri': 'ENC:' + ENC_2,
     'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical',
     'macType': 'Physical',
     'wwnType': 'Physical',
     'name': BFS_ENC2_SERVERS[0]['sp_name'],
     'description': 'Blackbird - ESXi BFS server Bside',
     'affinity': 'Bay',
     'bootMode': {'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto'},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'connectionSettings': {
         'connections': make_conn_data(bfs_conn_data_a)}
     }
]

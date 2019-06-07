import data_common

appliance_ip = '15.245.131.72'
RACK = 'BA51'

ENC_1 = 'CN7544044G'
ENC_2 = 'CN7545084V'
ENCLOSURE_URIS = ['ENC:' + ENC_1, 'ENC:' + ENC_2]

frame = 2

# Interconnect Bay Set
IBS = 3

# Chloride type for the IBS
ENC_CLTYPE = data_common.CHLORIDE10

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
US_FA1_UPLINKS = ['Q3:1', 'Q4:2']
US_FA2_UPLINKS = ['Q3:1', 'Q5:1']

IC3_FA_UPLINKS = US_FA1_UPLINKS
IC6_FA_UPLINKS = US_FA2_UPLINKS

ASIDE_UPLINK_SETS = ['US-FA1']
BSIDE_UPLINK_SETS = ['US-FA2']

ALL_UPLINK_SETS = ASIDE_UPLINK_SETS + BSIDE_UPLINK_SETS

# different uplinkset uplink port representation in LIG
IC3_LIG_ENET_UPLINK = 'Q4.1'
LIG_FA1_UPLINKS = ['Q3.1', 'Q4.2']
LIG_FA2_UPLINKS = ['Q3.1', 'Q5.1']

########################################
# FA uplinks connected to portwwn
# This is principal SAN switch switchwwn
########################################
CONNECTED_TO_WWN = '10:00:50:eb:1a:ed:00:b0'

# Enclosure 1 servers downlink on Enc1 and Enc2; 2 servers on each enclosure
ENC1_SERVER_1_ENC1_DL = 'd2'
ENC1_SERVER_1_ENC2_DL = 'd14'
ENC1_SERVER_2_ENC1_DL = 'd10'
ENC1_SERVER_2_ENC2_DL = 'd22'

# Enclosure 2 servers downlink on Enc1 and Enc2; 2 servers on each enclosure
ENC2_SERVER_1_ENC2_DL = 'd4'
ENC2_SERVER_1_ENC1_DL = 'd16'
ENC2_SERVER_2_ENC2_DL = 'd2'
ENC2_SERVER_2_ENC1_DL = 'd14'

# servers downlinks mapped to Aside and Bside Potash
ASIDE_SERVER_DOWNLINKS = [ENC1_SERVER_1_ENC1_DL, ENC1_SERVER_2_ENC1_DL, ENC2_SERVER_1_ENC1_DL, ENC2_SERVER_2_ENC1_DL]
BSIDE_SERVER_DOWNLINKS = [ENC1_SERVER_1_ENC2_DL, ENC1_SERVER_2_ENC2_DL, ENC2_SERVER_1_ENC2_DL, ENC2_SERVER_2_ENC2_DL]

# server profile names
ENC1_SP_1_NAME = 'SP-%s-enc1-bay2' % RACK
ENC1_SP_2_NAME = 'SP-%s-enc1-bay10' % RACK
ENC2_SP_1_NAME = 'SP-%s-enc2-bay4' % RACK
ENC2_SP_2_NAME = 'SP-%s-enc2-bay2' % RACK

# used for BFS testing
ENC1_SP_3_NAME = 'SP-%s-enc1-bay2' % RACK
ENC2_SP_3_NAME = 'SP-%s-enc2-bay1' % RACK
ENC2_SP_4_NAME = 'SP-%s-enc2-bay2' % RACK

# servers name
ENC1_SERVER_1 = '%s, bay 2' % ENC_1
ENC1_SERVER_2 = '%s, bay 10' % ENC_1
ENC2_SERVER_1 = '%s, bay 4' % ENC_2
ENC2_SERVER_2 = '%s, bay 2' % ENC_2

# used for BFS
ENC1_SERVER_3 = '%s, bay 2' % ENC_1
ENC2_SERVER_3 = '%s, bay 1' % ENC_2
ENC2_SERVER_4 = '%s, bay 2' % ENC_2

# servers private IP; currently DHCP; subject to change per standardization decision
ENC1_SERVER_1_IP_A = '10.11.1.1'
ENC1_SERVER_2_IP_A = '10.11.1.43'
ENC2_SERVER_1_IP_A = '10.11.1.44'
ENC2_SERVER_2_IP_A = '10.11.1.45'

ENC1_SERVER_3_IP_A = '10.11.1.77'
ENC2_SERVER_3_IP_A = '10.11.1.78'
ENC2_SERVER_4_IP_A = '10.11.1.79'

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

# BFS server: some enclosure has dual boot server with local OS and BFS, some has server with only BFS
BFS_ENC1_SERVERS = [
    {'sp_name': ENC1_SP_3_NAME,
     'sh_name': ENC1_SERVER_3,
     'os': 'Linux',
     'ip': ENC1_SERVER_3_IP_A}
]

BFS_ENC2_SERVERS = [
    {'sp_name': ENC2_SP_3_NAME,
     'sh_name': ENC2_SERVER_3,
     'os': 'Linux',
     'ip': ENC2_SERVER_3_IP_A},
    {'sp_name': ENC2_SP_4_NAME,
     'sh_name': ENC2_SERVER_4,
     'os': 'Linux',
     'ip': ENC2_SERVER_4_IP_A}
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
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['wpstnetwork1'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': IC3_LIG_ENET_UPLINK, 'speed': 'Auto'}
        ]
    },
    {
        'name': 'US-FA1',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['FA1'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': LIG_FA1_UPLINKS[0], 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': LIG_FA1_UPLINKS[1], 'speed': 'Auto'}
        ]
    }
]

uplink_sets_in_lig_B = [
    {
        'name': 'US-FA2',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['FA2'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': LIG_FA2_UPLINKS[0], 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': LIG_FA2_UPLINKS[1], 'speed': 'Auto'}
        ]
    }
]

##################################
# Interconnect bays configurations
# 2 Frames, IBS3
##################################

InterconnectMapTemplate_A = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2}
    ]

InterconnectMapTemplate_B = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
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
     'uplinkSets': list(uplink_sets_in_lig_B),
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

# used for LI uplinkset update
IC6_ADDED_UPLINK_PORT = 'Q4:2'
IC6_SPEED_CHANGE_PORT = US_FA2_UPLINKS[1]

li_uplinksets = {
    'US_FA1_4Gb':
        {'name': 'US-FA1',
         'ethernetNetworkType': 'NotApplicable',
         'networkType': 'FibreChannel',
         'networkUris': [],
         'fcNetworkUris': ['FA1'],
         'fcoeNetworkUris': [],
         'manualLoginRedistributionState': 'Supported',
         'connectionMode': 'Auto',
         'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': US_FA1_UPLINKS[0], 'desiredSpeed': 'Speed4G'},
                             {'enclosure': ENC_1, 'bay': '3', 'port': US_FA1_UPLINKS[1], 'desiredSpeed': 'Speed4G'}],
         'logicalInterconnectUri': None},
    'US_FA1_8Gb':
        {'name': 'US-FA1',
         'ethernetNetworkType': 'NotApplicable',
         'networkType': 'FibreChannel',
         'networkUris': [],
         'fcNetworkUris': ['FA1'],
         'fcoeNetworkUris': [],
         'manualLoginRedistributionState': 'Supported',
         'connectionMode': 'Auto',
         'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': US_FA1_UPLINKS[0], 'desiredSpeed': 'Speed8G'},
                             {'enclosure': ENC_1, 'bay': '3', 'port': US_FA1_UPLINKS[1], 'desiredSpeed': 'Speed8G'}],
         'logicalInterconnectUri': None},
    'US_FA1_Remove_Port':
        {'name': 'US-FA1',
         'ethernetNetworkType': 'NotApplicable',
         'networkType': 'FibreChannel',
         'networkUris': [],
         'fcNetworkUris': ['FA1'],
         'fcoeNetworkUris': [],
         'manualLoginRedistributionState': 'Supported',
         'connectionMode': 'Auto',
         'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': US_FA1_UPLINKS[1], 'desiredSpeed': 'Auto'}],
         'logicalInterconnectUri': None},
    'US_FA2_Add_Port_Speed_Change':
        {'name': 'US-FA2',
         'ethernetNetworkType': 'NotApplicable',
         'networkType': 'FibreChannel',
         'networkUris': [],
         'fcNetworkUris': ['FA2'],
         'fcoeNetworkUris': [],
         'manualLoginRedistributionState': 'Supported',
         'connectionMode': 'Auto',
         'portConfigInfos': [{'enclosure': ENC_2, 'bay': '6', 'port': IC6_ADDED_UPLINK_PORT, 'desiredSpeed': 'Speed4G'},
                             {'enclosure': ENC_2, 'bay': '6', 'port': IC6_SPEED_CHANGE_PORT, 'desiredSpeed': 'Speed4G'},
                             {'enclosure': ENC_2, 'bay': '6', 'port': US_FA2_UPLINKS[0], 'desiredSpeed': 'Auto'}],
         'logicalInterconnectUri': None},
}

#################
# Server Profiles
#################

server_profiles = [{'type': 'ServerProfileV9',
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
                    'connectionSettings': {'connections': [{'id': 1,
                                                            'name': 'conn-net',
                                                            'functionType': 'Ethernet',
                                                            'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': data_common.getEnetRBW(ENC_CLTYPE),
                                                            'networkUri': 'ETH:wpstnetwork1',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 2,
                                                            'name': 'conn-fc',
                                                            'functionType': 'FibreChannel',
                                                            'portId': 'Mezz 3:1-b',
                                                            'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
                                                            'networkUri': 'FC:FA1',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 3,
                                                            'name': 'conn-fc2',
                                                            'functionType': 'FibreChannel',
                                                            'portId': 'Auto',
                                                            'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
                                                            'networkUri': 'FC:FA2',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None}
                                                           ]}},

                   {'type': 'ServerProfileV9',
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
                    'connectionSettings': {'connections': [{'id': 1,
                                                            'name': 'conn-net',
                                                            'functionType': 'Ethernet',
                                                            'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': data_common.getEnetRBW(ENC_CLTYPE),
                                                            'networkUri': 'ETH:wpstnetwork1',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 2,
                                                            'name': 'conn-fc1',
                                                            'functionType': 'FibreChannel',
                                                            'portId': 'Auto',
                                                            'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
                                                            'networkUri': 'FC:FA1',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 3,
                                                            'name': 'conn-fc2',
                                                            'functionType': 'FibreChannel',
                                                            'portId': 'Auto',
                                                            'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
                                                            'networkUri': 'FC:FA2',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None}
                                                           ]}},

                   {'type': 'ServerProfileV9',
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
                    'connectionSettings': {'connections': [{'id': 1,
                                                            'name': 'conn-net1',
                                                            'functionType': 'Ethernet',
                                                            'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': data_common.getEnetRBW(ENC_CLTYPE),
                                                            'networkUri': 'ETH:wpstnetwork1',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 2,
                                                            'name': 'conn-fc1',
                                                            'functionType': 'FibreChannel',
                                                            'portId': 'Auto',
                                                            'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
                                                            'networkUri': 'FC:FA1',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 3,
                                                            'name': 'conn-fc2',
                                                            'functionType': 'FibreChannel',
                                                            'portId': 'Auto',
                                                            'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
                                                            'networkUri': 'FC:FA2',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None}
                                                           ]}},

                   {'type': 'ServerProfileV9',
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
                    'connectionSettings': {'connections': [{'id': 1,
                                                            'name': 'conn-net1',
                                                            'functionType': 'Ethernet',
                                                            'portId': 'Auto',
                                                            'requestedMbps': data_common.getEnetRBW(ENC_CLTYPE),
                                                            'networkUri': 'ETH:wpstnetwork1',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 2,
                                                            'name': 'conn-fc1',
                                                            'functionType': 'FibreChannel',
                                                            'portId': 'Auto',
                                                            'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
                                                            'networkUri': 'FC:FA1',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 3,
                                                            'name': 'conn-fc2',
                                                            'functionType': 'FibreChannel',
                                                            'portId': 'Auto',
                                                            'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
                                                            'networkUri': 'FC:FA2',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None}
                                                           ]}},

                   ]

#######################
# BFS server profiles
#######################
bfs_server_profiles = [
    {'type': 'ServerProfileV9',
     'serverHardwareUri': BFS_ENC1_SERVERS[0]['sh_name'],
     'serverHardwareTypeUri': None,
     'enclosureUri': 'ENC:' + ENC_1,
     'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical',
     'macType': 'Physical',
     'wwnType': 'Physical',
     'name': BFS_ENC1_SERVERS[0]['sp_name'],
     'description': 'Blackbird - ESXi BFS server Aside',
     'affinity': 'Bay',
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'connections': [{'id': 1,
                      'name': 'conn-net',
                      'functionType': 'Ethernet',
                      'portId': 'Mezz 3:1-a',
                      'requestedMbps': data_common.getEnetRBW(ENC_CLTYPE),
                      'networkUri': 'ETH:wpstnetwork1',
                      'mac': None,
                      'wwpn': None,
                      'wwnn': None},
                     {'id': 2,
                      'name': 'conn-fc1',
                      'functionType': 'FibreChannel',
                      'portId': 'Auto',
                      'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
                      'networkUri': 'FC:FA1',
                      'boot': {'priority': 'Primary',
                               'bootVolumeSource': 'UserDefined',
                               'targets': [{'arrayWwpn': '20110002AC012B0C', 'lun': '0'}]},
                      'mac': None,
                      'wwpn': None,
                      'wwnn': None},
                     {'id': 3,
                      'name': 'conn-fc2',
                      'functionType': 'FibreChannel',
                      'portId': 'Auto',
                      'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
                      'networkUri': 'FC:FA2',
                      'boot': {'priority': 'Secondary',
                               'bootVolumeSource': 'UserDefined',
                               'targets': [{'arrayWwpn': '20110002AC012B0C', 'lun': '0'}]},
                      'mac': None,
                      'wwpn': None,
                      'wwnn': None}
                     ]
     },
    {'type': 'ServerProfileV9',
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
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'connections': [{'id': 1,
                      'name': 'conn-net1',
                      'functionType': 'Ethernet',
                      'portId': 'Mezz 3:1-a',
                      'requestedMbps': data_common.getEnetRBW(ENC_CLTYPE),
                      'networkUri': 'ETH:wpstnetwork1',
                      'mac': None,
                      'wwpn': None,
                      'wwnn': None},
                     {'id': 2,
                      'name': 'conn-fc1',
                      'functionType': 'FibreChannel',
                      'portId': 'Auto',
                      'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
                      'networkUri': 'FC:FA1',
                      'boot': {'priority': 'Secondary',
                               'bootVolumeSource': 'UserDefined',
                               'targets': [{'arrayWwpn': '20110002AC012B0C', 'lun': '0'}]},
                      'mac': None,
                      'wwpn': None,
                      'wwnn': None},
                     {'id': 3,
                      'name': 'conn-fc2',
                      'functionType': 'FibreChannel',
                      'portId': 'Auto',
                      'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
                      'networkUri': 'FC:FA2',
                      'boot': {'priority': 'Primary',
                               'bootVolumeSource': 'UserDefined',
                               'targets': [{'arrayWwpn': '20110002AC012B0C', 'lun': '0'}]},
                      'mac': None,
                      'wwpn': None,
                      'wwnn': None}
                     ]
     },
    {'type': 'ServerProfileV9',
     'serverHardwareUri': BFS_ENC2_SERVERS[1]['sh_name'],
     'serverHardwareTypeUri': None,
     'enclosureUri': 'ENC:' + ENC_2,
     'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical',
     'macType': 'Physical',
     'wwnType': 'Physical',
     'name': BFS_ENC2_SERVERS[1]['sp_name'],
     'description': 'Blackbird - ESXi BFS server Bside',
     'affinity': 'Bay',
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'connections': [{'id': 1,
                      'name': 'conn-net1',
                      'functionType': 'Ethernet',
                      'portId': 'Mezz 3:1-a',
                      'requestedMbps': data_common.getEnetRBW(ENC_CLTYPE),
                      'networkUri': 'ETH:wpstnetwork1',
                      'mac': None,
                      'wwpn': None,
                      'wwnn': None},
                     {'id': 2,
                      'name': 'conn-fc1',
                      'functionType': 'FibreChannel',
                      'portId': 'Auto',
                      'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
                      'networkUri': 'FC:FA1',
                      'boot': {'priority': 'Secondary',
                               'bootVolumeSource': 'UserDefined',
                               'targets': [{'arrayWwpn': '20110002AC012B0C', 'lun': '0'}]},
                      'mac': None,
                      'wwpn': None,
                      'wwnn': None},
                     {'id': 3,
                      'name': 'conn-fc2',
                      'functionType': 'FibreChannel',
                      'portId': 'Auto',
                      'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
                      'networkUri': 'FC:FA2',
                      'boot': {'priority': 'Primary',
                               'bootVolumeSource': 'UserDefined',
                               'targets': [{'arrayWwpn': '20110002AC012B0C', 'lun': '0'}]},
                      'mac': None,
                      'wwpn': None,
                      'wwnn': None}
                     ]
     }
]

import data_common

appliance_ip = '15.245.131.12'
RACK = 'AR51'

ENC_1 = 'CN754406W7'
ENC_2 = 'CN7544044C'
ENC_3 = 'CN754406WT'
ENCLOSURE_URIS = ['ENC:' + ENC_1, 'ENC:' + ENC_2, 'ENC:' + ENC_3]

frame = 3

# Interconnect Bay Set
IBS = 3

ENC_CLTYPE = data_common.CHLORIDE10

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
US_DA1_UPLINKS = ['Q4:3', 'Q4:4']
US_DA3_UPLINKS = ['Q4:3', 'Q4:4']

IC3_DA_UPLINKS = US_DA1_UPLINKS
IC6_DA_UPLINKS = US_DA3_UPLINKS

US_FA1_UPLINKS = []
US_FA3_UPLINKS = []

# US_FA1_UPLINKS = ['Q4:2']
# US_FA3_UPLINKS = ['Q4:2']

IC3_FA_UPLINKS = US_FA1_UPLINKS
IC6_FA_UPLINKS = US_FA3_UPLINKS

ASIDE_UPLINK_SETS = ['US-DA1']
BSIDE_UPLINK_SETS = ['US-DA3']

ALL_UPLINK_SETS = ASIDE_UPLINK_SETS + BSIDE_UPLINK_SETS

# different uplinkset uplink port representation in LIG
LIG_ENET_UPLINK = 'Q6'
LIG_DA1_UPLINKS = ['Q4.3', 'Q4.4']
LIG_DA3_UPLINKS = ['Q4.3', 'Q4.4']
# LIG_FA1_UPLINKS = ['Q4.2']
# LIG_FA3_UPLINKS = ['Q4.2']

########################################
# DA uplink connected 3Par port portWwn
########################################
# connected to Tbird 3Par-A ports 0:2:1, 1:2:1 and 0:2:2, 1:2:2
IC3_DA_WWN_1 = '20:21:00:02:ac:01:2b:0c'
IC3_DA_WWN_2 = '21:21:00:02:ac:01:2b:0c'
IC6_DA_WWN_1 = '20:22:00:02:ac:01:2b:0c'
IC6_DA_WWN_2 = '21:22:00:02:ac:01:2b:0c'

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
ENC1_SERVER_2_ENC1_DL = 'd4'
ENC1_SERVER_2_ENC2_DL = 'd16'

# Enclosure 2 servers downlink on Enc1 and Enc2; 2 servers on each enclosure
ENC2_SERVER_1_ENC2_DL = 'd1'
ENC2_SERVER_1_ENC1_DL = 'd13'
ENC2_SERVER_2_ENC2_DL = 'd4'
ENC2_SERVER_2_ENC1_DL = 'd16'

# servers downlinks mapped to Aside and Bside Potash
ASIDE_SERVER_DOWNLINKS = [ENC1_SERVER_1_ENC1_DL, ENC1_SERVER_2_ENC1_DL, ENC2_SERVER_1_ENC1_DL, ENC2_SERVER_2_ENC1_DL]
BSIDE_SERVER_DOWNLINKS = [ENC1_SERVER_1_ENC2_DL, ENC1_SERVER_2_ENC2_DL, ENC2_SERVER_1_ENC2_DL, ENC2_SERVER_2_ENC2_DL]

# server profile names
ENC1_SP_1_NAME = 'SP-%s-enc1-bay1' % RACK
ENC1_SP_2_NAME = 'SP-%s-enc1-bay4' % RACK
ENC2_SP_1_NAME = 'SP-%s-enc2-bay1' % RACK
ENC2_SP_2_NAME = 'SP-%s-enc2-bay4' % RACK
ENC1_SP_1_BFS_NAME = 'SP-%s-BFS-enc1-bay1' % RACK
ENC2_SP_1_BFS_NAME = 'SP-%s-BFS-enc2-bay4' % RACK

# servers name and private IP through dhcp
ENC1_SERVER_1 = '%s, bay 1' % ENC_1
ENC1_SERVER_2 = '%s, bay 4' % ENC_1
ENC2_SERVER_1 = '%s, bay 1' % ENC_2
ENC2_SERVER_2 = '%s, bay 4' % ENC_2

# REVISIT - to be changed
ENC1_SERVER_1_IP_A = '10.11.1.5'
ENC1_SERVER_2_IP_A_OLD = '10.11.1.23'  # no mac on server
ENC1_SERVER_2_IP_A = '10.11.1.4'
ENC2_SERVER_1_IP_A = '10.11.1.3'
ENC2_SERVER_2_IP_A = '10.11.1.28'

GW_IP = '10.11.0.1'

PING_LIST = [ENC1_SERVER_1_IP_A, ENC1_SERVER_2_IP_A, ENC2_SERVER_1_IP_A, ENC2_SERVER_2_IP_A]

servers = [ENC1_SERVER_1, ENC1_SERVER_2, ENC2_SERVER_1, ENC2_SERVER_2]
server_profile_names = [ENC1_SP_1_NAME, ENC1_SP_2_NAME, ENC2_SP_1_NAME, ENC2_SP_2_NAME]

LINUX_BFS_USER = 'root'
LINUX_BFS_PWD = 'hpvse123'
LINUX_BFS_PROMPT = 'ESXi'

# For disable downlink test cases
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


##################################
# uplinksets definitions in LIG
##################################

uplink_sets_in_lig = [
    {
        'name': 'US-NET1',
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
        'name': 'US-DA3',
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
    }
    # {
    #     'name': 'US-FA1',
    #     'ethernetNetworkType': 'NotApplicable',
    #     'networkType': 'FibreChannel',
    #     'networkUris': ['FA1'],
    #     'lacpTimer': 'Short',
    #     'mode': 'Auto',
    #     'nativeNetworkUri': None,
    #     'logicalPortConfigInfos': [
    #         {'enclosure': '1', 'bay': '3', 'port': LIG_FA1_UPLINKS[0], 'speed': 'Auto'}
    #     ]
    # },
    # {
    #     'name': 'US-FA3',
    #     'ethernetNetworkType': 'NotApplicable',
    #     'networkType': 'FibreChannel',
    #     'networkUris': ['FA3'],
    #     'lacpTimer': 'Short',
    #     'mode': 'Auto',
    #     'nativeNetworkUri': None,
    #     'logicalPortConfigInfos': [
    #         {'enclosure': '2', 'bay': '6', 'port': LIG_FA3_UPLINKS[0], 'speed': 'Auto'}
    #     ]
    # }
]

##################################
# Interconnect bays configurations
# 2 or 3 Frames, IBS3, CL-20
##################################

InterconnectMapTemplate = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}
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
         'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': US_DA1_UPLINKS[0], 'desiredSpeed': 'Speed4G'},
                             {'enclosure': ENC_1, 'bay': '3', 'port': US_DA1_UPLINKS[1], 'desiredSpeed': 'Speed4G'}],
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
         'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': US_DA1_UPLINKS[0], 'desiredSpeed': 'Speed8G'},
                             {'enclosure': ENC_1, 'bay': '3', 'port': US_DA1_UPLINKS[1], 'desiredSpeed': 'Speed8G'}],
         'logicalInterconnectUri': None},
}

#################
# Server Profiles
#################

server_profiles = [{'type': 'ServerProfileV8',
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
                                     'name': 'conn-fc',
                                     'functionType': 'FibreChannel',
                                     'portId': 'Mezz 3:1-b',
                                     'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
                                     'networkUri': 'FC:DA1',
                                     'mac': None,
                                     'wwpn': None,
                                     'wwnn': None},
                                    {'id': 3,
                                     'name': 'conn-fc2',
                                     'functionType': 'FibreChannel',
                                     'portId': 'Auto',
                                     'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
                                     'networkUri': 'FC:DA3',
                                     'mac': None,
                                     'wwpn': None,
                                     'wwnn': None}
                                    ]},

                   {'type': 'ServerProfileV8',
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
                                     'networkUri': 'FC:DA1',
                                     'mac': None,
                                     'wwpn': None,
                                     'wwnn': None},
                                    {'id': 3,
                                     'name': 'conn-fc2',
                                     'functionType': 'FibreChannel',
                                     'portId': 'Auto',
                                     'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
                                     'networkUri': 'FC:DA3',
                                     'mac': None,
                                     'wwpn': None,
                                     'wwnn': None}
                                    ]},

                   {'type': 'ServerProfileV8',
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
                                     'networkUri': 'FC:DA1',
                                     'mac': None,
                                     'wwpn': None,
                                     'wwnn': None},
                                    {'id': 3,
                                     'name': 'conn-fc2',
                                     'functionType': 'FibreChannel',
                                     'portId': 'Auto',
                                     'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
                                     'networkUri': 'FC:DA3',
                                     'mac': None,
                                     'wwpn': None,
                                     'wwnn': None}
                                    ]},

                   {'type': 'ServerProfileV8',
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
                                     'networkUri': 'FC:DA1',
                                     'mac': None,
                                     'wwpn': None,
                                     'wwnn': None},
                                    {'id': 3,
                                     'name': 'conn-fc2',
                                     'functionType': 'FibreChannel',
                                     'portId': 'Auto',
                                     'requestedMbps': data_common.getFcRBW(ENC_CLTYPE),
                                     'networkUri': 'FC:DA3',
                                     'mac': None,
                                     'wwpn': None,
                                     'wwnn': None}
                                    ]},

                   ]


#########################
# NEGATIVE LIG UPLINKSETS
#########################
NEG_UPLINK_PORT = 'Q1:1'

# negative case return task with errorCode in taskError
err_ligs =\
    [
        {
            'errorCode': 'CRM_INVALID_UPLINK_SET_PORT',
            'ligBody': {
                'name': 'Err-lig-uplinkset-q7-q8-split',
                'type': 'logical-interconnect-groupV4',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': InterconnectMapTemplate,
                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                'interconnectBaySet': IBS,
                'redundancyType': 'HighlyAvailable',
                'uplinkSets': [
                    {'name': 'SAN-irf-split-port',
                     'ethernetNetworkType': 'NotApplicable',
                     'networkType': 'FibreChannel',
                     'networkUris': ['DA4'],
                     'lacpTimer': 'Short',
                     'mode': 'Auto',
                     'nativeNetworkUri': None,
                     'logicalPortConfigInfos': [
                         {'enclosure': '1', 'bay': '3', 'port': 'Q7.1', 'speed': 'Auto'}]
                     }
                ]
            }
        },

        {
            'errorCode': 'CRM_INVALID_UPLINK_SET_PORT',
            'ligBody': {
                'name': 'Err-lig-uplinkset-q7-q8',
                'type': 'logical-interconnect-groupV4',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': InterconnectMapTemplate,
                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                'interconnectBaySet': IBS,
                'redundancyType': 'HighlyAvailable',
                'uplinkSets': [
                    {'name': 'SAN-irf-port',
                     'ethernetNetworkType': 'NotApplicable',
                     'networkType': 'FibreChannel',
                     'networkUris': ['DA4'],
                     'lacpTimer': 'Short',
                     'mode': 'Auto',
                     'nativeNetworkUri': None,
                     'logicalPortConfigInfos': [
                         {'enclosure': '1', 'bay': '3', 'port': 'Q8', 'speed': 'Auto'}]
                     }
                ]
            }
        },

        {
            'errorCode': 'CRM_LOGICAL_UPLINK_TEMPLATE_FIBRE_CHANNEL_PORTS_DO_NOT_ALL_BELONG_TO_SAME_SWITCH',
            'ligBody': {
                'name': 'Err-lig-uplinkset-uplinks-on-different-ICM',
                'type': 'logical-interconnect-groupV4',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': InterconnectMapTemplate,
                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                'interconnectBaySet': IBS,
                'redundancyType': 'HighlyAvailable',
                'uplinkSets': [
                    {'name': 'SAN-uplinks-different-icm',
                     'ethernetNetworkType': 'NotApplicable',
                     'networkType': 'FibreChannel',
                     'networkUris': ['DA4'],
                     'lacpTimer': 'Short',
                     'mode': 'Auto',
                     'nativeNetworkUri': None,
                     'logicalPortConfigInfos': [
                         {'enclosure': '1', 'bay': '3', 'port': NEG_UPLINK_PORT, 'speed': 'Auto'},
                         {'enclosure': '2', 'bay': '6', 'port': NEG_UPLINK_PORT, 'speed': 'Auto'}]
                     }
                ]
            }
        },

        {
            'errorCode': 'CRM_LOGICAL_UPLINK_CAN_ONLY_CONTAIN_MAX_ONE_FC_NETWORK',
            'ligBody': {
                'name': 'Err-lig-uplinkset-multiple-fcnets',
                'type': 'logical-interconnect-groupV4',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': InterconnectMapTemplate,
                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                'interconnectBaySet': IBS,
                'redundancyType': 'HighlyAvailable',
                'uplinkSets': [
                    {'name': 'SAN-multiple-fcnets',
                     'ethernetNetworkType': 'NotApplicable',
                     'networkType': 'FibreChannel',
                     'networkUris': ['DA4', 'DA5'],
                     'lacpTimer': 'Short',
                     'mode': 'Auto',
                     'nativeNetworkUri': None,
                     'logicalPortConfigInfos': [
                         {'enclosure': '1', 'bay': '3', 'port': NEG_UPLINK_PORT, 'speed': 'Auto'}]
                     }
                ]
            }
        },

        {
            'errorCode': 'CRM_INVALID_UPLINK_SET_PORT_FC',
            'ligBody': {
                'name': 'Err-lig-uplinkset-unsplit-port',
                'type': 'logical-interconnect-groupV4',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': InterconnectMapTemplate,
                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                'interconnectBaySet': IBS,
                'redundancyType': 'HighlyAvailable',
                'uplinkSets': [
                    {'name': 'SAN-unsplit-port',
                     'ethernetNetworkType': 'NotApplicable',
                     'networkType': 'FibreChannel',
                     'networkUris': ['DA4'],
                     'lacpTimer': 'Short',
                     'mode': 'Auto',
                     'nativeNetworkUri': None,
                     'logicalPortConfigInfos': [
                         {'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'}]
                     }
                ]
            }
        }

    ]

##########################
# NEGATIVE LI Uplinksets
##########################
ALREADY_ASSIGNED_PORT = 'Q4:3'

err_li_us_list = \
    [
        {
            'errorCode': 'CRM_PORT_CONFIG_INFO_LOCATION_IS_NOT_FC_UPLINK_CAPABLE',
            'usBody': {
                'name': 'Err-SAN-unsplit-port',
                'ethernetNetworkType': 'NotApplicable',
                'networkType': 'FibreChannel',
                'networkUris': [],
                'fcNetworkUris': ['DA4'],
                'fcoeNetworkUris': [],
                'manualLoginRedistributionState': 'Supported',
                'connectionMode': 'Auto',
                'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': 'Q1', 'desiredSpeed': 'Auto'}],
                'logicalInterconnectUri': None
            }
        },
        {
            'errorCode': 'CRM_PORT_CONFIG_INFO_LOCATION_IS_NOT_FC_UPLINK_CAPABLE',
            'usBody': {
                'name': 'Err-SAN-irf-split-port',
                'ethernetNetworkType': 'NotApplicable',
                'networkType': 'FibreChannel',
                'networkUris': [],
                'fcNetworkUris': ['DA4'],
                'fcoeNetworkUris': [],
                'manualLoginRedistributionState': 'Supported',
                'connectionMode': 'Auto',
                'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': 'Q8:1', 'desiredSpeed': 'Auto'}],
                'logicalInterconnectUri': None
            }
        },
        {
            'errorCode': 'CRM_PORT_CONFIG_INFO_LOCATION_IS_NOT_FC_UPLINK_CAPABLE',
            'usBody': {
                'name': 'Err-SAN-irf-unsplit-port',
                'ethernetNetworkType': 'NotApplicable',
                'networkType': 'FibreChannel',
                'networkUris': [],
                'fcNetworkUris': ['DA4'],
                'fcoeNetworkUris': [],
                'manualLoginRedistributionState': 'Supported',
                'connectionMode': 'Auto',
                'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': 'Q7', 'desiredSpeed': 'Auto'}],
                'logicalInterconnectUri': None
            }
        },
        {
            'errorCode': 'CRM_PORTS_IN_DIFFERENT_SWITCH',
            'usBody': {
                'name': 'Err-SAN-uplinks-different-icm',
                'ethernetNetworkType': 'NotApplicable',
                'networkType': 'FibreChannel',
                'networkUris': [],
                'fcNetworkUris': ['DA4'],
                'fcoeNetworkUris': [],
                'manualLoginRedistributionState': 'Supported',
                'connectionMode': 'Auto',
                'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': NEG_UPLINK_PORT, 'desiredSpeed': 'Auto'},
                                    {'enclosure': ENC_2, 'bay': '6', 'port': NEG_UPLINK_PORT, 'desiredSpeed': 'Auto'}],
                'logicalInterconnectUri': None
            }
        },
        {
            'errorCode': 'CRM_LOGICAL_UPLINK_CAN_ONLY_CONTAIN_MAX_ONE_FC_NETWORK',
            'usBody': {
                'name': 'Err-SAN-multiple-fcnets',
                'ethernetNetworkType': 'NotApplicable',
                'networkType': 'FibreChannel',
                'networkUris': [],
                'fcNetworkUris': ['DA4', 'DA5'],
                'fcoeNetworkUris': [],
                'manualLoginRedistributionState': 'Supported',
                'connectionMode': 'Auto',
                'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': NEG_UPLINK_PORT, 'desiredSpeed': 'Auto'}],
                'logicalInterconnectUri': None
            }
        },
        {
            'errorCode': 'CRM_PORT_ALREADY_ASSIGNED',
            'usBody': {
                'name': 'Err-SAN-assigned-port',
                'ethernetNetworkType': 'NotApplicable',
                'networkType': 'FibreChannel',
                'networkUris': [],
                'fcNetworkUris': ['DA4'],
                'fcoeNetworkUris': [],
                'manualLoginRedistributionState': 'Supported',
                'connectionMode': 'Auto',
                'portConfigInfos': [
                    {'enclosure': ENC_1, 'bay': '3', 'port': ALREADY_ASSIGNED_PORT, 'desiredSpeed': 'Auto'}],
                'logicalInterconnectUri': None
            }
        },
        {
            'errorCode': 'CRM_PORT_NUMBER_UNKNOWN_FORMAT',
            'usBody': {
                'name': 'Err-SAN-invalid-uplinkport',
                'ethernetNetworkType': 'NotApplicable',
                'networkType': 'FibreChannel',
                'networkUris': [],
                'fcNetworkUris': ['DA4'],
                'fcoeNetworkUris': [],
                'manualLoginRedistributionState': 'Supported',
                'connectionMode': 'Auto',
                'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': 'Q10:1', 'desiredSpeed': 'Auto'}],
                'logicalInterconnectUri': None
            }
        }
    ]

import data_common

appliance_ip = '15.245.131.132'

ENC_1 = 'CN7545061V'
ENC_2 = 'CN7545085D'
frame = 2

REDUNDANCY = 'HA'
LE = 'LE' + '-' + REDUNDANCY
LIG = 'tbird-2enc-ha-ibs3-lig'
EG = 'tbird-2enc-ha-ibs3-eg'
LI = LE + '-' + LIG

RACK = 'AZ51'

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
US_DA2_UPLINKS = ['Q4:4']

IC3_DA_UPLINKS = ['Q4:3', 'Q5:1', 'Q4:4']
IC6_DA_UPLINKS = ['Q4:4']

IC3_FA_UPLINKS = ['Q2:2', 'Q3:1']
IC6_FA_UPLINKS = ['Q3:1']

ASIDE_UPLINK_SETS = ['US-DA1', 'US-DA2']
BSIDE_UPLINK_SETS = ['US-DA3']

ALL_UPLINK_SETS = ASIDE_UPLINK_SETS + BSIDE_UPLINK_SETS

########################################
# DA uplink connected 3Par port portWwn
########################################
IC3_Q43_DA_WWN = '20:12:00:02:ac:01:2b:0c'
IC3_Q51_DA_WWN = '21:12:00:02:ac:01:2b:0c'
IC3_Q44_DA_WWN = '20:12:00:02:ac:01:2b:0b'
IC6_Q44_DA_WWN = '21:12:00:02:ac:01:2b:0b'

########################################
# DA uplinks - 3par ports Dictionary
########################################
# For nameServer uplink DA port verification
IC3_UPLINKS_DA = [
    {'uplink': 'Q4:3',
     'da_portwwn': IC3_Q43_DA_WWN},
    {'uplink': 'Q5:1',
     'da_portwwn': IC3_Q51_DA_WWN},
    {'uplink': 'Q4:4',
     'da_portwwn': IC3_Q44_DA_WWN}
]

IC6_UPLINKS_DA = [
    {'uplink': 'Q4:4',
     'da_portwwn': IC6_Q44_DA_WWN}
]

SERVER1_ENC1_DL = 'd1'
SERVER1_ENC2_DL = 'd13'
SERVER10_ENC1_DL = 'd10'
SERVER10_ENC2_DL = 'd22'
SERVER4_ENC2_DL = 'd4'
SERVER4_ENC1_DL = 'd16'
SERVER7_ENC2_DL = 'd7'
SERVER7_ENC1_DL = 'd19'

ASIDE_SERVER_DOWNLINKS = [SERVER1_ENC1_DL, SERVER7_ENC1_DL, SERVER4_ENC1_DL, SERVER10_ENC1_DL]
BSIDE_SERVER_DOWNLINKS = [SERVER1_ENC2_DL, SERVER7_ENC2_DL, SERVER4_ENC2_DL, SERVER10_ENC2_DL]

# server profile names
ENC1_SP1_NAME = 'SP-%s-enc1-bay1' % RACK
ENC1_SP10_NAME = 'SP-%s-enc1-bay10' % RACK
ENC2_SP4_NAME = 'SP-%s-enc2-bay4' % RACK
ENC2_SP7_NAME = 'SP-%s-enc2-bay7' % RACK
ENC1_SP10_BFS_NAME = 'SP-BFS-%s-enc1-bay10' % RACK

# servers name and private IP through dhcp
ENC1_SERVER1 = '%s, bay 1' % ENC_1
ENC1_SERVER10 = '%s, bay 10' % ENC_1
ENC2_SERVER4 = '%s, bay 4' % ENC_2
ENC2_SERVER7 = '%s, bay 7' % ENC_2

ENC1_SERVER1_IP_A = '10.11.1.5'
ENC1_SERVER10_IP_A_OLD = '10.11.1.23'  # no mac on server
ENC1_SERVER10_IP_A = '10.11.1.4'
ENC2_SERVER4_IP_A = '10.11.1.3'
ENC2_SERVER7_IP_A = '10.11.1.21'

GW_IP = '10.11.0.1'

PING_LIST = [ENC1_SERVER10_IP_A, ENC1_SERVER1_IP_A, ENC2_SERVER4_IP_A, ENC2_SERVER7_IP_A]

servers = [ENC1_SERVER1, ENC1_SERVER10, ENC2_SERVER4, ENC2_SERVER7]
server_profile_names = [ENC1_SP1_NAME, ENC1_SP10_NAME, ENC2_SP4_NAME, ENC2_SP7_NAME]

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
            {'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'}
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
            {'enclosure': '1', 'bay': '3', 'port': 'Q4.3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q5.1', 'speed': 'Auto'}
        ]
    },
    {
        'name': 'US-DA2',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['DA2'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q4.4', 'speed': 'Auto'}
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
            {'enclosure': '2', 'bay': '6', 'port': 'Q4.4', 'speed': 'Auto'}
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
            {'enclosure': '1', 'bay': '3', 'port': 'Q2.2', 'speed': 'Auto'}
        ]
    },
    {
        'name': 'US-FA2',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['FA2'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q3.1', 'speed': 'Auto'}
        ]
    },
    {
        'name': 'US-FA3',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['FA3'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': 'Q3.1', 'speed': 'Auto'}
        ]
    }
]

##################################
# Interconnect bays configurations
# 2 Frames, IBS3
##################################

Enc2IBS3Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
    ]

ligs = {
    LIG:
        {'name': LIG,
         'interconnectMapTemplate': Enc2IBS3Map,
         'enclosureIndexes': [1, 2],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'uplinkSets': list(uplink_sets_in_lig),
         }
}

enc_group = {
    EG:
        {'name': EG,
         'type': 'EnclosureGroupV400',
         'enclosureCount': 2,
         'enclosureTypeUri': '/rest/enclosure-types/SY12000',
         'stackingMode': 'Enclosure',
         'interconnectBayMappingCount': 6,
         'configurationScript': None,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         }
}

###
# All logical enclosures
###
les = {
    LE:
        {'name': LE,
         'enclosureUris': ['ENC:' + ENC_1, 'ENC:' + ENC_2],
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
         'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': 'Q4:3', 'desiredSpeed': 'Speed4G'},
                             {'enclosure': ENC_1, 'bay': '3', 'port': 'Q5:1', 'desiredSpeed': 'Speed4G'}],
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
         'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': 'Q4:3', 'desiredSpeed': 'Speed8G'},
                             {'enclosure': ENC_1, 'bay': '3', 'port': 'Q5:1', 'desiredSpeed': 'Speed8G'}],
         'logicalInterconnectUri': None},
}

#################
# Server Profiles
#################

server_profiles = [{'type': 'ServerProfileV7',
                    'serverHardwareUri': ENC1_SERVER1,
                    'serverHardwareTypeUri': None,
                    'enclosureUri': 'ENC:' + ENC_1,
                    'enclosureGroupUri': 'EG:%s' % EG,
                    'serialNumberType': 'Physical',
                    'macType': 'Physical',
                    'wwnType': 'Physical',
                    'name': 'SP-%s-enc1-bay1' % RACK,
                    'description': 'Blackbird rhel6.7 - Aside',
                    'affinity': 'Bay',
                    'connections': [{'id': 1,
                                     'name': 'conn-net',
                                     'functionType': 'Ethernet',
                                     'portId': 'Mezz 3:1-a',
                                     'requestedMbps': '2500',
                                     'networkUri': 'ETH:wpstnetwork1',
                                     'mac': None,
                                     'wwpn': None,
                                     'wwnn': None},
                                    {'id': 2,
                                     'name': 'conn-fc',
                                     'functionType': 'FibreChannel',
                                     'portId': 'Mezz 3:1-b',
                                     'requestedMbps': '8000',
                                     'networkUri': 'FC:DA1',
                                     'mac': None,
                                     'wwpn': None,
                                     'wwnn': None},
                                    {'id': 3,
                                     'name': 'conn-fc2',
                                     'functionType': 'FibreChannel',
                                     'portId': 'Auto',
                                     'requestedMbps': '8000',
                                     'networkUri': 'FC:DA3',
                                     'mac': None,
                                     'wwpn': None,
                                     'wwnn': None}
                                    ]},

                   {'type': 'ServerProfileV7',
                    'serverHardwareUri': ENC1_SERVER10,
                    'serverHardwareTypeUri': None,
                    'enclosureUri': 'ENC:' + ENC_1,
                    'enclosureGroupUri': 'EG:%s' % EG,
                    'serialNumberType': 'Physical',
                    'macType': 'Physical',
                    'wwnType': 'Physical',
                    'name': 'SP-%s-enc1-bay10' % RACK,
                    'description': 'Blackbird Windows - Aside',
                    'affinity': 'Bay',
                    'connections': [{'id': 1,
                                     'name': 'conn-net',
                                     'functionType': 'Ethernet',
                                     'portId': 'Mezz 3:1-a',
                                     'requestedMbps': '2500',
                                     'networkUri': 'ETH:wpstnetwork1',
                                     'mac': None,
                                     'wwpn': None,
                                     'wwnn': None},
                                    {'id': 2,
                                     'name': 'conn-fc1',
                                     'functionType': 'FibreChannel',
                                     'portId': 'Auto',
                                     'requestedMbps': '8000',
                                     'networkUri': 'FC:DA2',
                                     'mac': None,
                                     'wwpn': None,
                                     'wwnn': None},
                                    {'id': 3,
                                     'name': 'conn-fc2',
                                     'functionType': 'FibreChannel',
                                     'portId': 'Auto',
                                     'requestedMbps': '8000',
                                     'networkUri': 'FC:DA3',
                                     'mac': None,
                                     'wwpn': None,
                                     'wwnn': None}
                                    ]},

                   {'type': 'ServerProfileV7',
                    'serverHardwareUri': ENC2_SERVER4,
                    'serverHardwareTypeUri': None,
                    'enclosureUri': 'ENC:' + ENC_2,
                    'enclosureGroupUri': 'EG:%s' % EG,
                    'serialNumberType': 'Physical',
                    'macType': 'Physical',
                    'wwnType': 'Physical',
                    'name': 'SP-%s-enc2-bay4' % RACK,
                    'description': 'Blackbird Linux - Bside',
                    'affinity': 'Bay',
                    'connections': [{'id': 1,
                                     'name': 'conn-net1',
                                     'functionType': 'Ethernet',
                                     'portId': 'Mezz 3:1-a',
                                     'requestedMbps': '2500',
                                     'networkUri': 'ETH:wpstnetwork1',
                                     'mac': None,
                                     'wwpn': None,
                                     'wwnn': None},
                                    {'id': 2,
                                     'name': 'conn-fc1',
                                     'functionType': 'FibreChannel',
                                     'portId': 'Auto',
                                     'requestedMbps': '8000',
                                     'networkUri': 'FC:DA2',
                                     'mac': None,
                                     'wwpn': None,
                                     'wwnn': None},
                                    {'id': 3,
                                     'name': 'conn-fc2',
                                     'functionType': 'FibreChannel',
                                     'portId': 'Auto',
                                     'requestedMbps': '8000',
                                     'networkUri': 'FC:DA3',
                                     'mac': None,
                                     'wwpn': None,
                                     'wwnn': None}
                                    ]},

                   {'type': 'ServerProfileV7',
                    'serverHardwareUri': ENC2_SERVER7,
                    'serverHardwareTypeUri': None,
                    'enclosureUri': 'ENC:' + ENC_2,
                    'enclosureGroupUri': 'EG:%s' % EG,
                    'serialNumberType': 'Physical',
                    'macType': 'Physical',
                    'wwnType': 'Physical',
                    'name': 'SP-%s-enc2-bay7' % RACK,
                    'description': 'Blackbird Windows - Bside',
                    'affinity': 'Bay',
                    'connections': [{'id': 1,
                                     'name': 'conn-net1',
                                     'functionType': 'Ethernet',
                                     'portId': 'Mezz 3:1-a',
                                     'requestedMbps': '2500',
                                     'networkUri': 'ETH:wpstnetwork1',
                                     'mac': None,
                                     'wwpn': None,
                                     'wwnn': None},
                                    {'id': 2,
                                     'name': 'conn-fc1',
                                     'functionType': 'FibreChannel',
                                     'portId': 'Auto',
                                     'requestedMbps': '8000',
                                     'networkUri': 'FC:DA1',
                                     'mac': None,
                                     'wwpn': None,
                                     'wwnn': None},
                                    {'id': 3,
                                     'name': 'conn-fc2',
                                     'functionType': 'FibreChannel',
                                     'portId': 'Auto',
                                     'requestedMbps': '8000',
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
                'type': 'logical-interconnect-groupV300',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': Enc2IBS3Map,
                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                'interconnectBaySet': 3,
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
                'type': 'logical-interconnect-groupV300',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': Enc2IBS3Map,
                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                'interconnectBaySet': 3,
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
                'type': 'logical-interconnect-groupV300',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': Enc2IBS3Map,
                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                'interconnectBaySet': 3,
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
                'type': 'logical-interconnect-groupV300',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': Enc2IBS3Map,
                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                'interconnectBaySet': 3,
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
                'type': 'logical-interconnect-groupV300',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': Enc2IBS3Map,
                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                'interconnectBaySet': 3,
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

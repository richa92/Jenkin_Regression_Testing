from copy import deepcopy
import data_common

three_par_name = 'fvt-3par-bb56-8200a'
three_par_info = \
    {'ip': '15.245.128.186',
     'name': three_par_name,
     'user': '3paradm',
     'pwd': '3pardata',
     'prompt': three_par_name + ' cli%'}

appliance_ip = '15.245.131.142'
RACK = 'BB56'

ENC_1 = 'MXQ71902DM'
ENC_2 = 'MXQ71906M8'

enclosures = [ENC_1, ENC_2]

frame = 2
ENCLOSURE_URIS = ['ENC:' + enclosures[x] for x in xrange(0, frame)]

if frame == 1:
    bside_frame = 1
else:
    bside_frame = 2


# Interconnect Bay Set
IBS = 3
ICMA = 3
ICMB = 6

MZ = 'Mezz ' + str(IBS)

NITROA = ENC_1 + ', ' + 'interconnect ' + str(ICMA)
NITROB = ENC_2 + ', ' + 'interconnect ' + str(ICMB)

REDUNDANCY_TYPE = 'HighlyAvailable'

REDUNDANCY = 'HA'
LE = 'LE' + '-' + REDUNDANCY
LIG = 'LIG'
EG = 'EG' + '-' + REDUNDANCY
LI = LE + '-' + LIG

# This is to make test program working for A+B (2 LI) and HA (1 LI); mainly for uplinkset verification
LIs = [LI, LI]

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


def rlist(start, end, prefix='', suffix='', step=1):
    lst = []
    for c in xrange(start, end + 1, step):
        lst.append('%s%s%s' % (prefix, str(c), suffix))
    return lst


# return autoLoginRedistribution value 'True' for odd number count, 'False' for even number count
def get_autolrd(count):
    autolrd = True
    if count % 2 == 0:
        autolrd = False
    return autolrd


########################################
# FC and Ethernet networks info
########################################
da_networks =\
    [{'name': n,
      'type': 'fc-networkV4',
      'linkStabilityTime': 0,
      'autoLoginRedistribution': False,
      'connectionTemplateUri': None,
      'managedSanUri': None,
      'fabricType': 'DirectAttach'} for n in rlist(1, 20, 'DA')]

fa_networks =\
    [{'name': n,
      'type': 'fc-networkV4',
      'linkStabilityTime': 30,
      'autoLoginRedistribution': get_autolrd(int(n[2:])),
      'connectionTemplateUri': None,
      'managedSanUri': None,
      'fabricType': 'FabricAttach'} for n in rlist(1, 20, 'FA')]

ENET_PREFIX = 'net_'
ethernet_networks = [{'name': n,
                      'type': 'ethernet-networkV4',
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged',
                      'vlanId': int(n[len(ENET_PREFIX):])} for n in rlist(401, 402, ENET_PREFIX)]


########################################
# OV Uplinkset uplinks info
########################################
US_DA1_UPLINKS = ['Q2', 'Q5']
# REVISIT: Use this when 4x32 QSFP is available
# US_DA2_UPLINKS = ['Q4:3', 'Q4:4']
US_DA2_UPLINKS = ['Q2:1', 'Q4:1']

ORIG_UPLINK_SPEED = data_common.OPSPEED16

IC3_DA_UPLINKS = US_DA1_UPLINKS
IC6_DA_UPLINKS = US_DA2_UPLINKS

US_FA1_UPLINKS = ['Q3:1', 'Q4:1']
US_FA2_UPLINKS = ['Q3', 'Q5']

IC3_FA_UPLINKS = US_FA1_UPLINKS
IC6_FA_UPLINKS = US_FA2_UPLINKS

ASIDE_UPLINK_SETS = ['US-DA1']
BSIDE_UPLINK_SETS = ['US-DA2']

ALL_UPLINK_SETS = ASIDE_UPLINK_SETS + BSIDE_UPLINK_SETS

# different uplinkset uplink port representation in LIG
IC3_LIG_ENET_UPLINK = 'Q1'
LIG_DA1_UPLINKS = ['Q2', 'Q5']
# DF REVISIT: use this when 4x32Gb QSFP is available
# LIG_DA2_UPLINKS = ['Q4.3' 'Q4.4']
LIG_DA2_UPLINKS = ['Q2.1', 'Q4.1']
LIG_FA1_UPLINKS = ['Q3.1', 'Q4.1']
LIG_FA2_UPLINKS = ['Q3', 'Q5']

########################################
# DA uplink connected 3Par port portWwn
########################################
# connected to Tbird 3par fvt_3par_bb56_8200a system ports 0:2:1, 1:2:1 and 0:2:2, 1:2:2
IC3_DA_WWN_1 = '20:21:00:02:ac:01:d4:db'
IC3_DA_WWN_2 = '21:21:00:02:ac:01:d4:db'
IC6_DA_WWN_1 = '20:22:00:02:ac:01:d4:db'
IC6_DA_WWN_2 = '21:22:00:02:ac:01:d4:db'

ASIDE_HAPPY_CONNECTION_MAP = [IC3_DA_WWN_1, IC3_DA_WWN_2]
BSIDE_HAPPY_CONNECTION_MAP = [IC6_DA_WWN_1, IC6_DA_WWN_2]

########################################
# Used by 3par showportdev ns <port> cmd
########################################

da_3par_port_Aside_1 = '0:2:1'
da_3par_port_Aside_2 = '1:2:1'
da_3par_port_Bside_1 = '0:2:2'
da_3par_port_Bside_2 = '1:2:2'

da_3par_ports_Aside = [da_3par_port_Aside_1, da_3par_port_Aside_2]
da_3par_ports_Bside = [da_3par_port_Bside_1, da_3par_port_Bside_2]

da_3par_wwpn_Aside_1 = IC3_DA_WWN_1.replace(":", "").upper()
da_3par_wwpn_Aside_2 = IC3_DA_WWN_2.replace(":", "").upper()
da_3par_wwpn_Bside_1 = IC6_DA_WWN_1.replace(":", "").upper()
da_3par_wwpn_Bside_2 = IC6_DA_WWN_2.replace(":", "").upper()

da_3par_wwpn_Aside = [da_3par_wwpn_Aside_1, da_3par_wwpn_Aside_2]
da_3par_wwpn_Bside = [da_3par_wwpn_Bside_1, da_3par_wwpn_Bside_2]

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
    {'uplink': US_DA2_UPLINKS[0],
     'da_portwwn': IC6_DA_WWN_1},
    {'uplink': US_DA2_UPLINKS[1],
     'da_portwwn': IC6_DA_WWN_2}
]


GW_IP_A = '10.11.0.1'
GW_IP_B = '10.12.0.1'

LINUX_BFS_USER = 'root'
LINUX_BFS_PWD = 'hpvse123'
LINUX_BFS_PROMPT = 'ESXi'


##################################
# uplinksets definitions in LIG
##################################

uplink_sets_in_lig = [
    {
        'name': 'US-NET1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': [rlist(401, 401, ENET_PREFIX)[0]],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': ICMA, 'port': IC3_LIG_ENET_UPLINK, 'speed': 'Auto'}
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
            {'enclosure': '1', 'bay': ICMA, 'port': LIG_DA1_UPLINKS[0], 'speed': ORIG_UPLINK_SPEED},
            {'enclosure': '1', 'bay': ICMA, 'port': LIG_DA1_UPLINKS[1], 'speed': ORIG_UPLINK_SPEED}
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
            {'enclosure': bside_frame, 'bay': ICMB, 'port': LIG_DA2_UPLINKS[0], 'speed': ORIG_UPLINK_SPEED},
            {'enclosure': bside_frame, 'bay': ICMB, 'port': LIG_DA2_UPLINKS[1], 'speed': ORIG_UPLINK_SPEED}
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
            {'enclosure': '1', 'bay': ICMA, 'port': LIG_FA1_UPLINKS[0], 'speed': data_common.OPSPEED16},
            {'enclosure': '1', 'bay': ICMA, 'port': LIG_FA1_UPLINKS[1], 'speed': data_common.OPSPEED32}
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
            {'enclosure': bside_frame, 'bay': ICMB, 'port': LIG_FA2_UPLINKS[0], 'speed': data_common.OPSPEED16},
            {'enclosure': bside_frame, 'bay': ICMB, 'port': LIG_FA2_UPLINKS[1], 'speed': data_common.OPSPEED32}
        ]
    }
]

##################################
# Interconnect bays configurations
# 2 or 3 Frames, IBS3, CL-20
##################################

InterconnectMapTemplate = \
    [
        {'bay': ICMA, 'enclosure': 1, 'type': data_common.NITRO_MODEL, 'enclosureIndex': 1},
        {'bay': ICMB, 'enclosure': 1, 'type': data_common.CL50_MODEL, 'enclosureIndex': 1},
        {'bay': ICMA, 'enclosure': bside_frame, 'type': data_common.CL50_MODEL,
         'enclosureIndex': bside_frame},
        {'bay': ICMB, 'enclosure': bside_frame, 'type': data_common.NITRO_MODEL,
         'enclosureIndex': bside_frame}
    ]

ligs = [
    {'name': LIG,
     'interconnectMapTemplate': InterconnectMapTemplate,
     'enclosureIndexes': [x for x in xrange(1, frame + 1)],
     'interconnectBaySet': IBS,
     'redundancyType': REDUNDANCY_TYPE,
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


def li_fc_us(**kwargs):
    return deepcopy({'name': kwargs.get('name', None),
                     'ethernetNetworkType': kwargs.get('ethernetNetworkType', 'NotApplicable'),
                     'networkType': kwargs.get('networkType', 'FibreChannel'),
                     'networkUris': kwargs.get('networkUris', []),
                     'fcNetworkUris': kwargs.get('fcNetworkUris', []),
                     'fcoeNetworkUris': kwargs.get('fcoeNetworkUris', []),
                     'logicalInterconnectUri': kwargs.get('logicalInterconnectUri', None),
                     'manualLoginRedistributionState': kwargs.get('manualLoginRedistributionState', 'Supported'),
                     'connectionMode': kwargs.get('connectionMode', 'Auto'),
                     'portConfigInfos': kwargs.get('portConfigInfos', None)})


# used for LI uplinkset updated
li_uplinksets = {
    'US_DA1_8Gb':
        li_fc_us(name='US-DA1',
                 fcNetworkUris=['DA1'],
                 portConfigInfos=[{'enclosure': ENC_1, 'bay': ICMA, 'port': US_DA1_UPLINKS[0],
                                   'desiredSpeed': data_common.OPSPEED8},
                                  {'enclosure': ENC_1, 'bay': ICMA, 'port': US_DA1_UPLINKS[1],
                                   'desiredSpeed': data_common.OPSPEED8}
                                  ]),
    'US_DA1_16Gb':
        li_fc_us(name='US-DA1',
                 fcNetworkUris=['DA1'],
                 portConfigInfos=[{'enclosure': ENC_1, 'bay': ICMA, 'port': US_DA1_UPLINKS[0],
                                   'desiredSpeed': data_common.OPSPEED16},
                                  {'enclosure': ENC_1, 'bay': ICMA, 'port': US_DA1_UPLINKS[1],
                                   'desiredSpeed': data_common.OPSPEED16}
                                  ])
}

#################
# Server Profiles
#################

# Let network decide the request and max bandwidth
conn_data = [
    # {'name': 'conn-net', 'functionType': 'Ethernet', 'portId': MZ + ':1-a',
    #  'networkUri': 'ETH:' + rlist(401, 401, ENET_PREFIX)[0]},
    {'name': 'conn-fc', 'functionType': 'FibreChannel', 'portId': MZ + ':1-b',
     'networkUri': 'FC:DA1'},
    {'name': 'conn-fc2', 'functionType': 'FibreChannel', 'portId': 'Auto',
     'networkUri': 'FC:DA2'}
]

bfs_conn_data_a = [
    # {'name': 'conn-net', 'functionType': 'Ethernet', 'portId': MZ + ':1-a',
    #  'networkUri': 'ETH:' + rlist(401, 401, ENET_PREFIX)[0]},
    {'name': 'conn-fc', 'functionType': 'FibreChannel', 'portId': MZ + ':1-b',
     'networkUri': 'FC:DA1',
     'boot': {'priority': 'Primary',
              'bootVolumeSource': 'UserDefined',
              'targets': [
                  {'arrayWwpn': da_3par_wwpn_Aside_1, 'lun': '1'},
                  {'arrayWwpn': da_3par_wwpn_Aside_2, 'lun': '1'}
              ]},
     },
    {'name': 'conn-fc2', 'functionType': 'FibreChannel', 'portId': 'Auto',
     'networkUri': 'FC:DA2',
     'boot': {'priority': 'Secondary',
              'bootVolumeSource': 'UserDefined',
              'targets': [
                  {'arrayWwpn': da_3par_wwpn_Bside_1, 'lun': '1'},
                  {'arrayWwpn': da_3par_wwpn_Bside_2, 'lun': '1'}
              ]},
     }
]


def make_conn_data(data):
    return deepcopy(data)


bfs_conn_data_b = make_conn_data(bfs_conn_data_a)
bfs_conn_data_b[0]['boot']['priority'] = 'Secondary'
bfs_conn_data_b[1]['boot']['priority'] = 'Primary'


enc1_server_1 = {
    'sp_name': 'SP-%s-enc1-bay1' % RACK,
    'sh_name': '%s, bay 1' % ENC_1,
    'enc1_downlink': 'd1',
    'enc2_downlink': 'd13',
    'conn_data': conn_data,
    # 'ip_a': '10.11.1.87'
}

enc1_server_2 = {
    'sp_name': 'SP-%s-enc1-bay12-BFS' % RACK,
    'sh_name': '%s, bay 12' % ENC_1,
    'enc1_downlink': 'd12',
    'enc2_downlink': 'd24',
    'conn_data': bfs_conn_data_a,
    # 'ip_a': '10.11.1.9'
}

enc2_server_1 = {
    'sp_name': 'SP-%s-enc2-bay3-BFS' % RACK,
    'sh_name': '%s, bay 3' % ENC_2,
    'enc1_downlink': 'd15',
    'enc2_downlink': 'd3',
    'conn_data': bfs_conn_data_b,
    # 'ip_a': '10.11.1.55'
}

enc2_server_2 = {
    'sp_name': 'SP-%s-enc2-bay12' % RACK,
    'sh_name': '%s, bay 12' % ENC_2,
    'enc1_downlink': 'd24',
    'enc2_downlink': 'd12',
    'conn_data': conn_data,
    # 'ip_a': '10.11.4.170'
}


servers_info = [enc1_server_1, enc1_server_2, enc2_server_1, enc2_server_2]

ASIDE_SERVER_DOWNLINKS =\
    [svr['enc1_downlink'] for svr in servers_info]

BSIDE_SERVER_DOWNLINKS =\
    [svr['enc2_downlink'] for svr in servers_info]

# expected attached devices to the 3par DA port; plus 1 since it includes its own wwpn
STORAGE_ATTACH_DEVICES = len(ASIDE_SERVER_DOWNLINKS) + 1

# PING_LIST_A =\
#     [svr['ip_a'] for svr in servers_info]

#################
# Server Profiles
#################

server_profiles = [
    {'type': data_common.SP_TYPE,
     'serverHardwareUri': enc1_server_1['sh_name'],
     'enclosureUri': 'ENC:' + ENC_1,
     'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical',
     'macType': 'Physical',
     'wwnType': 'Physical',
     'name': enc1_server_1['sp_name'],
     'description': 'Gen10 - Aside',
     'affinity': 'Bay',
     'connectionSettings': {
         'connections': make_conn_data(enc1_server_1['conn_data'])}
     },
    {'type': data_common.SP_TYPE,
     'serverHardwareUri': enc1_server_2['sh_name'],
     'enclosureUri': 'ENC:' + ENC_1,
     'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical',
     'macType': 'Physical',
     'wwnType': 'Physical',
     'name': enc1_server_2['sp_name'],
     'description': 'Gen10 Windows - Aside',
     'affinity': 'Bay',
     'bootMode': {'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto'},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'connectionSettings': {
         'connections': make_conn_data(enc1_server_2['conn_data'])}
     },
    {'type': data_common.SP_TYPE,
     'serverHardwareUri': enc2_server_1['sh_name'],
     'enclosureUri': 'ENC:' + ENC_2,
     'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical',
     'macType': 'Physical',
     'wwnType': 'Physical',
     'name': enc2_server_1['sp_name'],
     'description': 'Gen10 Linux - Bside',
     'affinity': 'Bay',
     'bootMode': {'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto'},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'connectionSettings': {
         'connections': make_conn_data(enc2_server_1['conn_data'])}
     },
    {'type': data_common.SP_TYPE,
     'serverHardwareUri': enc2_server_2['sh_name'],
     'enclosureUri': 'ENC:' + ENC_2,
     'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical',
     'macType': 'Physical',
     'wwnType': 'Physical',
     'name': enc2_server_2['sp_name'],
     'description': 'Gen10 Windows - Bside',
     'affinity': 'Bay',
     'connectionSettings': {
         'connections': make_conn_data(enc2_server_2['conn_data'])}
     }
]

server_profile_names =\
    [sp['name'] for sp in server_profiles]

server_hws =\
    [sp['serverHardwareUri'] for sp in server_profiles]


###############################
# SP connection rbw update info
###############################

QUACK_SERVERS = [enc1_server_1, enc2_server_1]

QUAG2_SERVERS = [enc1_server_2, enc2_server_2]

# This is for server with MZ card that support 50Gb, updated when in DLS 50Gb mode
# NOTE: BFS server could not change rbw while power on. Need non-BFS server
sp_upgrade_conn_rbw_info = [
    # {'sp_name': QUAG2_SERVERS[0]['sp_name'],
    #  'connections': [
    #      {'conn_name': 'conn-fc', 'requestedMbps': '32000'},
    #      {'conn_name': 'conn-fc2', 'requestedMbps': '32000'}]
    #  },
    {'sp_name': QUAG2_SERVERS[1]['sp_name'],
     'connections': [
         {'conn_name': 'conn-fc', 'requestedMbps': '32000'},
         {'conn_name': 'conn-fc2', 'requestedMbps': '32000'}]
     }
]

sp_downgrade_conn_rbw_info = [
    # {'sp_name': QUAG2_SERVERS[0]['sp_name'],
    #  'connections': [
    #      {'conn_name': 'conn-fc', 'requestedMbps': '16000'},
    #      {'conn_name': 'conn-fc2', 'requestedMbps': '16000'}]
    #  },
    {'sp_name': QUAG2_SERVERS[1]['sp_name'],
     'connections': [
         {'conn_name': 'conn-fc', 'requestedMbps': '16000'},
         {'conn_name': 'conn-fc2', 'requestedMbps': '16000'}]
     }
]


#########################
# NEGATIVE LIG UPLINKSETS
#########################
NEG_UPLINK_PORT = 'Q6:1'
NEG_UNSPLIT_UPLINK_PORT = 'Q6'

# negative case return task with errorCode in taskError
err_ligs =\
    [
        {
            'errorCode': 'CRM_INVALID_UPLINK_SET_PORT',
            'ligBody': {
                'name': 'Err-lig-uplinkset-q7-q8-split',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': InterconnectMapTemplate,
                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                'interconnectBaySet': IBS,
                'redundancyType': REDUNDANCY_TYPE,
                'uplinkSets': [
                    {'name': 'SAN-irf-split-port',
                     'ethernetNetworkType': 'NotApplicable',
                     'networkType': 'FibreChannel',
                     'networkUris': ['DA11'],
                     'lacpTimer': 'Short',
                     'mode': 'Auto',
                     'nativeNetworkUri': None,
                     'logicalPortConfigInfos': [
                         {'enclosure': '1', 'bay': ICMA, 'port': 'Q7.1', 'speed': data_common.OPSPEED8}]
                     }
                ]
            }
        },

        {
            'errorCode': 'CRM_INVALID_UPLINK_SET_PORT',
            'ligBody': {
                'name': 'Err-lig-uplinkset-q7-q8',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': InterconnectMapTemplate,
                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                'interconnectBaySet': IBS,
                'redundancyType': REDUNDANCY_TYPE,
                'uplinkSets': [
                    {'name': 'SAN-irf-port',
                     'ethernetNetworkType': 'NotApplicable',
                     'networkType': 'FibreChannel',
                     'networkUris': ['DA11'],
                     'lacpTimer': 'Short',
                     'mode': 'Auto',
                     'nativeNetworkUri': None,
                     'logicalPortConfigInfos': [
                         {'enclosure': '1', 'bay': ICMA, 'port': 'Q8', 'speed': data_common.OPSPEED8}]
                     }
                ]
            }
        },

        {
            'errorCode': 'CRM_LOGICAL_UPLINK_TEMPLATE_FIBRE_CHANNEL_PORTS_DO_NOT_ALL_BELONG_TO_SAME_SWITCH',
            'ligBody': {
                'name': 'Err-lig-uplinkset-uplinks-on-different-ICM',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': InterconnectMapTemplate,
                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                'interconnectBaySet': IBS,
                'redundancyType': REDUNDANCY_TYPE,
                'uplinkSets': [
                    {'name': 'SAN-uplinks-different-icm',
                     'ethernetNetworkType': 'NotApplicable',
                     'networkType': 'FibreChannel',
                     'networkUris': ['DA11'],
                     'lacpTimer': 'Short',
                     'mode': 'Auto',
                     'nativeNetworkUri': None,
                     'logicalPortConfigInfos': [
                         {'enclosure': '1', 'bay': ICMA, 'port': NEG_UPLINK_PORT, 'speed': data_common.OPSPEED8},
                         {'enclosure': bside_frame, 'bay': ICMB, 'port': NEG_UPLINK_PORT,
                          'speed': data_common.OPSPEED8}]
                     }
                ]
            }
        },

        {
            'errorCode': 'CRM_LOGICAL_UPLINK_CAN_ONLY_CONTAIN_MAX_ONE_FC_NETWORK',
            'ligBody': {
                'name': 'Err-lig-uplinkset-multiple-fcnets',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': InterconnectMapTemplate,
                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                'interconnectBaySet': IBS,
                'redundancyType': REDUNDANCY_TYPE,
                'uplinkSets': [
                    {'name': 'SAN-multiple-fcnets',
                     'ethernetNetworkType': 'NotApplicable',
                     'networkType': 'FibreChannel',
                     'networkUris': ['DA11', 'DA12'],
                     'lacpTimer': 'Short',
                     'mode': 'Auto',
                     'nativeNetworkUri': None,
                     'logicalPortConfigInfos': [
                         {'enclosure': '1', 'bay': ICMA, 'port': NEG_UPLINK_PORT, 'speed': data_common.OPSPEED8}]
                     }
                ]
            }
        },

        {
            'errorCode': 'CRM_BOTH_SPLIT_AND_UNSPLIT_PORTS_USED_IN_UPLINK_SETS',
            'ligBody': {
                'name': 'Err-lig-uplinkset-mixed_split_unsplit-port',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': InterconnectMapTemplate,
                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                'interconnectBaySet': IBS,
                'redundancyType': REDUNDANCY_TYPE,
                'uplinkSets': [
                    {'name': 'SAN-unsplit-port',
                     'ethernetNetworkType': 'NotApplicable',
                     'networkType': 'FibreChannel',
                     'networkUris': ['DA11'],
                     'lacpTimer': 'Short',
                     'mode': 'Auto',
                     'nativeNetworkUri': None,
                     'logicalPortConfigInfos': [
                         {'enclosure': '1', 'bay': ICMA, 'port': NEG_UNSPLIT_UPLINK_PORT,
                          'speed': data_common.OPSPEED8},
                         {'enclosure': '1', 'bay': ICMA, 'port': 'Q2:2', 'speed': data_common.OPSPEED8}
                     ]
                     }
                ]
            }
        },

        {
            'errorCode': 'CRM_INVALID_DESIRED_PORT_SPEED_FOR_NITRO_FC_PORT',
            'ligBody': {
                'name': 'Err-lig-uplinkset-speed-2g',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': InterconnectMapTemplate,
                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                'interconnectBaySet': IBS,
                'redundancyType': REDUNDANCY_TYPE,
                'uplinkSets': [
                    {'name': 'SAN-uplink-speed-2g',
                     'ethernetNetworkType': 'NotApplicable',
                     'networkType': 'FibreChannel',
                     'networkUris': ['DA11'],
                     'lacpTimer': 'Short',
                     'mode': 'Auto',
                     'nativeNetworkUri': None,
                     'logicalPortConfigInfos': [
                         {'enclosure': '1', 'bay': ICMA, 'port': NEG_UPLINK_PORT, 'speed': data_common.OPSPEED2}
                     ]
                     }
                ]
            }
        },

        {
            'errorCode': 'CRM_INVALID_DESIRED_PORT_SPEED_FOR_NITRO_FC_PORT',
            'ligBody': {
                'name': 'Err-lig-uplinkset-speed-4g',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': InterconnectMapTemplate,
                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                'interconnectBaySet': IBS,
                'redundancyType': REDUNDANCY_TYPE,
                'uplinkSets': [
                    {'name': 'SAN-uplink-speed-4g',
                     'ethernetNetworkType': 'NotApplicable',
                     'networkType': 'FibreChannel',
                     'networkUris': ['DA11'],
                     'lacpTimer': 'Short',
                     'mode': 'Auto',
                     'nativeNetworkUri': None,
                     'logicalPortConfigInfos': [
                         {'enclosure': '1', 'bay': ICMA, 'port': NEG_UPLINK_PORT, 'speed': data_common.OPSPEED4}
                     ]
                     }
                ]
            }
        },

        {
            'errorCode': 'CRM_INVALID_DESIRED_PORT_SPEED_FOR_NITRO_FC_PORT',
            'ligBody': {
                'name': 'Err-lig-uplinkset-speed-auto',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': InterconnectMapTemplate,
                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                'interconnectBaySet': IBS,
                'redundancyType': REDUNDANCY_TYPE,
                'uplinkSets': [
                    {'name': 'SAN-uplink-speed-auto',
                     'ethernetNetworkType': 'NotApplicable',
                     'networkType': 'FibreChannel',
                     'networkUris': ['DA11'],
                     'lacpTimer': 'Short',
                     'mode': 'Auto',
                     'nativeNetworkUri': None,
                     'logicalPortConfigInfos': [
                         {'enclosure': '1', 'bay': ICMA, 'port': NEG_UPLINK_PORT, 'speed': 'Auto'}
                     ]
                     }
                ]
            }
        },

        {
            'errorCode': 'CRM_INVALID_DESIRED_PORT_SPEED_FOR_NITRO_FC_PORT',
            'ligBody': {
                'name': 'Err-lig-uplinkset-no-speed',
                'enclosureType': 'SY12000',
                'interconnectMapTemplate': InterconnectMapTemplate,
                'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                'interconnectBaySet': IBS,
                'redundancyType': REDUNDANCY_TYPE,
                'uplinkSets': [
                    {'name': 'SAN-uplink-no-speed',
                     'ethernetNetworkType': 'NotApplicable',
                     'networkType': 'FibreChannel',
                     'networkUris': ['DA11'],
                     'lacpTimer': 'Short',
                     'mode': 'Auto',
                     'nativeNetworkUri': None,
                     'logicalPortConfigInfos': [
                         {'enclosure': '1', 'bay': ICMA, 'port': NEG_UPLINK_PORT}
                     ]
                     }
                ]
            }
        }

    ]

###############################################
# LI Uplinksets uplink portStatusReason cases
###############################################
# uplinkset with split uplink format on unsplit SFP: Unknown? Unavailable?
TEST_UNAVAILABLE_PORT_UNSPLIT_SFP = 'Q2:2'
# DA uplinkset with uplink connected SAN switch
TEST_PORT_DA_ON_FA = 'Q3'
# **********
# DF REVISIT: remove when 3par change to 32Gb HBA
# uplinkset with 32Gb speed uplink on 16Gb SFP: FcSpeedMismatch
TEST_PORT_32G_SPEED_ON_16GB_SFP = 'Q2:1'

# uplinkset with uplink connected to Enet Switch: ModuleIncompatible
TEST_PORT_DA_ON_ENET = 'Q1'

# DF TEMP: UNPOPULATED, both Q6 and Q6:1 has reason 'None'
TEST_PORT_UNPOPULATED = 'Q6'

# DF REVISIT UNCOMMENT when 4x32 QSFP is available
# uplinkset with unsplit uplink format on split QSFP (4x): Unknown?
TEST_UNSPLIT_PORT_SPLIT_SFP = 'Q4'


li_us_port_unlink_list = \
    [
        {
            'uplink': TEST_PORT_DA_ON_FA,
            'icm': NITROA,
            'expected_reason': 'FabricTypeMismatch',
            'usBody':
                li_fc_us(name='US_fabric_mismatch',
                         fcNetworkUris=['DA12'],
                         portConfigInfos=[{'enclosure': ENC_1, 'bay': ICMA, 'port': TEST_PORT_DA_ON_FA,
                                           'desiredSpeed': data_common.OPSPEED16}])
        },
        {
            'uplink': TEST_PORT_UNPOPULATED,
            'icm': NITROB,
            'expected_reason': 'Unpopulated',
            'usBody':
                li_fc_us(name='US_unpopulated',
                         fcNetworkUris=['DA13'],
                         portConfigInfos=[{'enclosure': ENC_2, 'bay': ICMB, 'port': TEST_PORT_UNPOPULATED,
                                           'desiredSpeed': data_common.OPSPEED16}])
        },
        {
            'uplink': TEST_PORT_32G_SPEED_ON_16GB_SFP,
            'icm': NITROB,
            'expected_reason': 'FcSpeedMismatch',
            'usBody':
                li_fc_us(name='US_speed_mismatch',
                         fcNetworkUris=['DA14'],
                         portConfigInfos=[{'enclosure': ENC_2, 'bay': ICMB, 'port': TEST_PORT_32G_SPEED_ON_16GB_SFP,
                                           'desiredSpeed': data_common.OPSPEED32}])
        },
        {
            'uplink': TEST_PORT_DA_ON_ENET,
            'icm': NITROA,
            'expected_reason': 'ModuleIncompatible',
            'usBody':
                li_fc_us(name='US_module_incompatible',
                         fcNetworkUris=['DA15'],
                         portConfigInfos=[{'enclosure': ENC_1, 'bay': ICMA, 'port': TEST_PORT_DA_ON_ENET,
                                           'desiredSpeed': data_common.OPSPEED16}])
        },
        {
            'uplink': TEST_UNAVAILABLE_PORT_UNSPLIT_SFP,
            'icm': NITROA,
            'expected_reason': 'None',
            'usBody':
                li_fc_us(name='US_unavailable_on_nonsplit_SFP',
                         fcNetworkUris=['DA11'],
                         portConfigInfos=[{'enclosure': ENC_1, 'bay': ICMA, 'port': TEST_UNAVAILABLE_PORT_UNSPLIT_SFP,
                                           'desiredSpeed': data_common.OPSPEED16}])

        },
        # {
        #     'uplink': TEST_UNSPLIT_PORT_SPLIT_SFP,
        #     'icm': NITROB,
        #     'expected_reason': 'Unknown',
        #     'usBody':
        #         li_fc_us(name='US_unsplit_port_on_split_qsfp',
        #                  fcNetworkUris=['DA16'],
        #                  portConfigInfos=[{'enclosure': ENC_2, 'bay': ICMB, 'port': TEST_UNSPLIT_PORT_SPLIT_SFP,
        #                                    'desiredSpeed': data_common.OPSPEED16}])
        # }
    ]


##########################
# NEGATIVE LI Uplinksets
##########################
ALREADY_ASSIGNED_PORT = US_DA1_UPLINKS[0]

err_li_us_list = \
    [
        {
            'errorCode': 'CRM_BOTH_SPLIT_AND_UNSPLIT_PORTS_USED_IN_UPLINK_SETS',
            'usBody':
                li_fc_us(name='Err-SAN-mix-split-unsplit',
                         fcNetworkUris=['DA11'],
                         portConfigInfos=[{'enclosure': ENC_2, 'bay': ICMB, 'port': NEG_UPLINK_PORT,
                                           'desiredSpeed': data_common.OPSPEED8},
                                          {'enclosure': ENC_2, 'bay': ICMB, 'port': 'Q1',
                                           'desiredSpeed': data_common.OPSPEED8}
                                          ])
        },
        {
            'errorCode': 'CRM_PORT_CONFIG_INFO_LOCATION_IS_NOT_FC_UPLINK_CAPABLE',
            'usBody':
                li_fc_us(name='Err-SAN-irf-split-port',
                         fcNetworkUris=['DA11'],
                         portConfigInfos=[{'enclosure': ENC_1, 'bay': ICMA, 'port': 'Q8:1',
                                           'desiredSpeed': data_common.OPSPEED8}
                                          ])
        },
        {
            'errorCode': 'CRM_PORT_CONFIG_INFO_LOCATION_IS_NOT_FC_UPLINK_CAPABLE',
            'usBody':
                li_fc_us(name='Err-SAN-irf-unsplit-port',
                         fcNetworkUris=['DA11'],
                         portConfigInfos=[{'enclosure': ENC_1, 'bay': ICMA, 'port': 'Q7',
                                           'desiredSpeed': data_common.OPSPEED8}
                                          ])
        },
        {
            'errorCode': 'CRM_PORTS_IN_DIFFERENT_SWITCH',
            'usBody':
                li_fc_us(name='Err-SAN-uplinks-different-icm',
                         fcNetworkUris=['DA11'],
                         portConfigInfos=[{'enclosure': ENC_1, 'bay': ICMA, 'port': NEG_UPLINK_PORT,
                                           'desiredSpeed': data_common.OPSPEED8},
                                          {'enclosure': ENC_2, 'bay': ICMB, 'port': NEG_UPLINK_PORT,
                                           'desiredSpeed': data_common.OPSPEED8}
                                          ])
        },
        {
            'errorCode': 'CRM_LOGICAL_UPLINK_CAN_ONLY_CONTAIN_MAX_ONE_FC_NETWORK',
            'usBody':
                li_fc_us(name='Err-SAN-multiple-fcnets',
                         fcNetworkUris=['DA11', 'DA12'],
                         portConfigInfos=[{'enclosure': ENC_1, 'bay': ICMA, 'port': NEG_UPLINK_PORT,
                                           'desiredSpeed': data_common.OPSPEED8}
                                          ])
        },
        {
            'errorCode': 'CRM_PORT_ALREADY_ASSIGNED',
            'usBody':
                li_fc_us(name='Err-SAN-assigned-port',
                         fcNetworkUris=['DA11'],
                         portConfigInfos=[{'enclosure': ENC_1, 'bay': ICMA, 'port': ALREADY_ASSIGNED_PORT,
                                           'desiredSpeed': data_common.OPSPEED8}
                                          ])
        },
        {
            'errorCode': 'CRM_PORT_NUMBER_UNKNOWN_FORMAT',
            'usBody':
                li_fc_us(name='rr-SAN-invalid-uplinkport',
                         fcNetworkUris=['DA11'],
                         portConfigInfos=[{'enclosure': ENC_1, 'bay': ICMA, 'port': 'Q10:1',
                                           'desiredSpeed': data_common.OPSPEED8}
                                          ])
        },
        {
            'errorCode': 'CRM_INVALID_DESIRED_PORT_SPEED_FOR_NITRO_FC_PORT',
            'usBody':
                li_fc_us(name='Err-SAN-speed-4g',
                         fcNetworkUris=['DA11'],
                         portConfigInfos=[{'enclosure': ENC_1, 'bay': ICMA, 'port': NEG_UPLINK_PORT,
                                           'desiredSpeed': data_common.OPSPEED4}])
        },
        {
            'errorCode': 'CRM_INVALID_DESIRED_PORT_SPEED_FOR_NITRO_FC_PORT',
            'usBody':
                li_fc_us(name='Err-SAN-speed-2g',
                         fcNetworkUris=['DA11'],
                         portConfigInfos=[{'enclosure': ENC_1, 'bay': ICMA, 'port': NEG_UPLINK_PORT,
                                           'desiredSpeed': data_common.OPSPEED2}])
        },
        {
            'errorCode': 'CRM_INVALID_DESIRED_PORT_SPEED_FOR_NITRO_FC_PORT',
            'usBody':
                li_fc_us(name='Err-SAN-speed-Auto',
                         fcNetworkUris=['DA11'],
                         portConfigInfos=[{'enclosure': ENC_1, 'bay': ICMA, 'port': NEG_UPLINK_PORT,
                                           'desiredSpeed': 'Auto'}])
        },
        {
            'errorCode': 'CRM_INVALID_DESIRED_PORT_SPEED_FOR_NITRO_FC_PORT',
            'usBody':
                li_fc_us(name='Err-SAN-no_desired_speed',
                         fcNetworkUris=['DA11'],
                         portConfigInfos=[{'enclosure': ENC_1, 'bay': ICMA,
                                           'port': NEG_UPLINK_PORT}])
        }
    ]

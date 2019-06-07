from copy import deepcopy
import data_common

three_par_name = 'fvt-3par-bb56-8200a'
three_par_info = \
    {'ip': '15.245.128.186',
     'name': three_par_name,
     'user': '3paradm',
     'pwd': '3pardata',
     'prompt': three_par_name + ' cli%'}

nimble_name = 'Nimble'
nimble_info = \
    {'ip': '15.186.4.180',
     'name': nimble_name,
     'user': 'admin',
     'pwd': 'admin',
     'prompt': nimble_name + ' OS $'}

appliance_ip = '15.186.9.159'
RACK = 'eagle159'

ENC_1 = 'MXQ8190018'
ENC_2 = 'MXQ82705W8'

enclosures = [ENC_1, ENC_2]

frame = 2
ENCLOSURE_URIS = ['ENC:' + enclosures[x] for x in xrange(0, frame)]
# ENCLOSURE_URIS = ['ENC:' + ENC_1, 'ENC:' + ENC_2]

if frame == 1:
    bside_frame = 1
else:
    bside_frame = 2


# Interconnect Bay Set
IBS1 = 1
IBS3 = 3

IBS1ICMA = 1
IBS1ICMB = 4
IBS3ICMA = 3
IBS3ICMB = 6

IBS1MZ = 'Mezz ' + str(IBS1)
IBS3MZ = 'Mezz ' + str(IBS3)

REDUNDANCY_TYPE = 'HighlyAvailable'

REDUNDANCY = 'HA'
LE = 'LE' + '-' + REDUNDANCY
LIG_P = 'LIG-POTASH'
LIG_N = 'LIG-NITRO'
EG = 'EG' + '-' + REDUNDANCY
LI_P = LE + '-' + LIG_P
LI_N = LE + '-' + LIG_N

# This is to make test program working for A+B (2 LI) and HA (1 LI); mainly for uplinkset verification
LIs = [LI_P, LI_N]

POTASHA = ENC_1 + ', ' + 'interconnect 1'
POTASHB = ENC_2 + ', ' + 'interconnect 4'
NITROA = ENC_1 + ', ' + 'interconnect 3'
NITROB = ENC_2 + ', ' + 'interconnect 6'

NITRO_ICMS = [NITROA, NITROB]
POTASH_ICMS = [POTASHA, POTASHB]

ICMS = NITRO_ICMS + POTASH_ICMS

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
# FC networks info
########################################
da_networks_p =\
    [{'name': n,
      'type': 'fc-networkV4',
      'linkStabilityTime': 0,
      'autoLoginRedistribution': False,
      'connectionTemplateUri': None,
      'managedSanUri': None,
      'fabricType': 'DirectAttach'} for n in rlist(1, 2, 'DA-POTASH-')]

da_networks_n =\
    [{'name': n,
      'type': 'fc-networkV4',
      'linkStabilityTime': 0,
      'autoLoginRedistribution': False,
      'connectionTemplateUri': None,
      'managedSanUri': None,
      'fabricType': 'DirectAttach'} for n in rlist(1, 2, 'DA-NITRO-')]

da_networks = da_networks_p + da_networks_n

fa_networks =\
    [{'name': n,
      'type': 'fc-networkV4',
      'linkStabilityTime': 30,
      'autoLoginRedistribution': get_autolrd(int(n[2:])),
      'connectionTemplateUri': None,
      'managedSanUri': None,
      'fabricType': 'FabricAttach'} for n in rlist(1, 2, 'FA')]

########################################
# OV Uplinkset uplinks info
########################################
US_POTASH_UPLINKS = ['Q1:1', 'Q2:1']
US_POTASH_ASIDE_UPLINKS = US_POTASH_UPLINKS
US_POTASH_BSIDE_UPLINKS = US_POTASH_UPLINKS

US_NITRO_ASIDE_UPLINKS = ['Q1', 'Q2']
US_NITRO_BSIDE_UPLINKS = US_POTASH_UPLINKS

POTASH_ORIG_UPLINK_SPEED = data_common.OPSPEED8
NITRO_ORIG_UPLINK_SPEED = data_common.OPSPEED16

POTASH_ASIDE_UPLINK_SET = 'US-' + da_networks_p[0]['name']
POTASH_BSIDE_UPLINK_SET = 'US-' + da_networks_p[1]['name']

NITRO_ASIDE_UPLINK_SET = 'US-' + da_networks_n[0]['name']
NITRO_BSIDE_UPLINK_SET = 'US-' + da_networks_n[1]['name']

ALL_NITRO_UPLINK_SETS = [NITRO_ASIDE_UPLINK_SET, NITRO_BSIDE_UPLINK_SET]
ALL_POTASH_UPLINK_SETS = [POTASH_ASIDE_UPLINK_SET, POTASH_BSIDE_UPLINK_SET]

ALL_UPLINK_SETS = ALL_NITRO_UPLINK_SETS + ALL_POTASH_UPLINK_SETS

LIG_POTASH_UPLINKS = ['Q1.1', 'Q2.1']
LIG_NITRO_ASIDE_UPLINKS = US_NITRO_ASIDE_UPLINKS
LIG_NITRO_BSIDE_UPLINKS = LIG_POTASH_UPLINKS


#################################################
# Used by Nimble fc info cli for connected device
#################################################
# Both uplinks in the same DA uplinkset are Nimble active/standby port with same port name
da_potashA_Nimble_port = "fc1c.1"
da_potashB_Nimble_port = "fc2c.1"

da_nitroA_Nimble_port = "fc1a.1"
da_nitroB_Nimble_port = "fc2a.1"

# active and standby ports, same port name
da_potashA_Nimble_ports = [da_potashA_Nimble_port]
da_potashB_Nimble_ports = [da_potashB_Nimble_port]

da_nitroA_Nimble_ports = [da_nitroA_Nimble_port]
da_nitroB_Nimble_ports = [da_nitroB_Nimble_port]

nimble_wwpn_prefix = "56:c9:ce:90:8f:75:25:"

da_potashA_nimble_wwpn_1 = nimble_wwpn_prefix + "03"
da_potashA_nimble_wwpn_2 = nimble_wwpn_prefix + "0f"
da_potashB_nimble_wwpn_1 = nimble_wwpn_prefix + "07"
da_potashB_nimble_wwpn_2 = nimble_wwpn_prefix + "13"

da_nitroA_nimble_wwpn_1 = nimble_wwpn_prefix + "01"
da_nitroA_nimble_wwpn_2 = nimble_wwpn_prefix + "0d"
da_nitroB_nimble_wwpn_1 = nimble_wwpn_prefix + "05"
da_nitroB_nimble_wwpn_2 = nimble_wwpn_prefix + "11"

# expected connected initiator alias pattern for Nitro/Potash Aside/Bside DA uplinks
potashA_initiator_alias_pattern = RACK + '-enc*-bay*-mz1-1b'
potashB_initiator_alias_pattern = RACK + '-enc*-bay*-mz1-2b'

nitroA_initiator_alias_pattern = RACK + '-enc*-bay*-mz3-1b'
nitroB_initiator_alias_pattern = RACK + '-enc*-bay*-mz3-2b'

##########################
# BFS target array wwpn
##########################
potash_bfs_a_target1_wwn = da_potashA_nimble_wwpn_1.replace(":", "").upper()
potash_bfs_a_target2_wwn = da_potashA_nimble_wwpn_2.replace(":", "").upper()
potash_bfs_b_target1_wwn = da_potashB_nimble_wwpn_1.replace(":", "").upper()
potash_bfs_b_target2_wwn = da_potashB_nimble_wwpn_2.replace(":", "").upper()

nitro_bfs_a_target1_wwn = da_nitroA_nimble_wwpn_1.replace(":", "").upper()
nitro_bfs_a_target2_wwn = da_nitroA_nimble_wwpn_2.replace(":", "").upper()
nitro_bfs_b_target1_wwn = da_nitroB_nimble_wwpn_1.replace(":", "").upper()
nitro_bfs_b_target2_wwn = da_nitroB_nimble_wwpn_2.replace(":", "").upper()

########################################
# DA uplinks - Nimble ports Dictionary
########################################
# For server DA connection verification through nameServers downlink connectionMap

NITRO_ASIDE_HAPPY_CONNECTION_MAP = [da_nitroA_nimble_wwpn_1, da_nitroA_nimble_wwpn_2]
NITRO_BSIDE_HAPPY_CONNECTION_MAP = [da_nitroB_nimble_wwpn_1, da_nitroB_nimble_wwpn_2]

POTASH_ASIDE_HAPPY_CONNECTION_MAP = [da_potashA_nimble_wwpn_1, da_potashA_nimble_wwpn_2]
POTASH_BSIDE_HAPPY_CONNECTION_MAP = [da_potashB_nimble_wwpn_1, da_potashB_nimble_wwpn_2]


#############################################
# For nameServer uplink DA port verification
#############################################
POTASH_A_UPLINKS_DA = [
    {'uplink': US_POTASH_ASIDE_UPLINKS[0],
     'da_portwwn': da_potashA_nimble_wwpn_1},
    {'uplink': US_POTASH_ASIDE_UPLINKS[1],
     'da_portwwn': da_potashA_nimble_wwpn_2}
]

POTASH_B_UPLINKS_DA = [
    {'uplink': US_POTASH_BSIDE_UPLINKS[0],
     'da_portwwn': da_potashB_nimble_wwpn_1},
    {'uplink': US_POTASH_BSIDE_UPLINKS[1],
     'da_portwwn': da_potashB_nimble_wwpn_2}
]

NITRO_A_UPLINKS_DA = [
    {'uplink': US_NITRO_ASIDE_UPLINKS[0],
     'da_portwwn': da_nitroA_nimble_wwpn_1},
    {'uplink': US_NITRO_ASIDE_UPLINKS[1],
     'da_portwwn': da_nitroA_nimble_wwpn_2}
]

NITRO_B_UPLINKS_DA = [
    {'uplink': US_NITRO_BSIDE_UPLINKS[0],
     'da_portwwn': da_nitroB_nimble_wwpn_1},
    {'uplink': US_NITRO_BSIDE_UPLINKS[1],
     'da_portwwn': da_nitroB_nimble_wwpn_2}
]


##################################
# uplinksets definitions in LIG
##################################
uplink_sets_in_lig_p = [
    {
        'name': POTASH_ASIDE_UPLINK_SET,
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': [da_networks_p[0]['name']],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': IBS1ICMA, 'port': LIG_POTASH_UPLINKS[0],
             'speed': POTASH_ORIG_UPLINK_SPEED},
            {'enclosure': '1', 'bay': IBS1ICMA, 'port': LIG_POTASH_UPLINKS[1],
             'speed': POTASH_ORIG_UPLINK_SPEED}
        ]
    },
    {
        'name': POTASH_BSIDE_UPLINK_SET,
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': [da_networks_p[1]['name']],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': bside_frame, 'bay': IBS1ICMB, 'port': LIG_POTASH_UPLINKS[0],
             'speed': POTASH_ORIG_UPLINK_SPEED},
            {'enclosure': bside_frame, 'bay': IBS1ICMB, 'port': LIG_POTASH_UPLINKS[1],
             'speed': POTASH_ORIG_UPLINK_SPEED}
        ]
    }
]

uplink_sets_in_lig_n = [
    {
        'name': NITRO_ASIDE_UPLINK_SET,
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': [da_networks_n[0]['name']],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': IBS3ICMA, 'port': LIG_NITRO_ASIDE_UPLINKS[0],
             'speed': NITRO_ORIG_UPLINK_SPEED},
            {'enclosure': '1', 'bay': IBS3ICMA, 'port': LIG_NITRO_ASIDE_UPLINKS[1],
             'speed': NITRO_ORIG_UPLINK_SPEED}
        ]
    },
    {
        'name': NITRO_BSIDE_UPLINK_SET,
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': [da_networks_n[1]['name']],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': bside_frame, 'bay': IBS3ICMB, 'port': LIG_NITRO_BSIDE_UPLINKS[0],
             'speed': NITRO_ORIG_UPLINK_SPEED},
            {'enclosure': bside_frame, 'bay': IBS3ICMB, 'port': LIG_NITRO_BSIDE_UPLINKS[1],
             'speed': NITRO_ORIG_UPLINK_SPEED}
        ]
    }
]

##################################
# Interconnect bays configurations
# 2 or 3 Frames, IBS3, CL-20
##################################

InterconnectMapTemplate_P = \
    [
        {'bay': IBS1ICMA, 'enclosure': 1, 'type': data_common.POTASH_MODEL, 'enclosureIndex': 1},
        {'bay': IBS1ICMB, 'enclosure': 1, 'type': data_common.CL20_MODEL, 'enclosureIndex': 1},
        {'bay': IBS1ICMA, 'enclosure': bside_frame, 'type': data_common.CL20_MODEL,
         'enclosureIndex': bside_frame},
        {'bay': IBS1ICMB, 'enclosure': bside_frame, 'type': data_common.POTASH_MODEL,
         'enclosureIndex': bside_frame}
    ]

InterconnectMapTemplate_N = \
    [
        {'bay': IBS3ICMA, 'enclosure': 1, 'type': data_common.NITRO_MODEL, 'enclosureIndex': 1},
        {'bay': IBS3ICMB, 'enclosure': 1, 'type': data_common.CL50_MODEL, 'enclosureIndex': 1},
        {'bay': IBS3ICMA, 'enclosure': bside_frame, 'type': data_common.CL50_MODEL,
         'enclosureIndex': bside_frame},
        {'bay': IBS3ICMB, 'enclosure': bside_frame, 'type': data_common.NITRO_MODEL,
         'enclosureIndex': bside_frame}
    ]

ligs = [
    {'name': LIG_P,
     'interconnectMapTemplate': InterconnectMapTemplate_P,
     'enclosureIndexes': [x for x in xrange(1, frame + 1)],
     'interconnectBaySet': IBS1,
     'redundancyType': REDUNDANCY_TYPE,
     'uplinkSets': list(uplink_sets_in_lig_p)
     },
    {'name': LIG_N,
     'interconnectMapTemplate': InterconnectMapTemplate_N,
     'enclosureIndexes': [x for x in xrange(1, frame + 1)],
     'interconnectBaySet': IBS3,
     'redundancyType': REDUNDANCY_TYPE,
     'uplinkSets': list(uplink_sets_in_lig_n)
     }
]

enc_group = {
    EG:
        {'name': EG,
         'enclosureCount': frame,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG_P},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG_N},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:' + LIG_P},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG_N}],
         'ipAddressingMode': "External"
         }
}

########################
# All logical enclosures
########################
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


# used for LI uplinkset update uplinks speed
nitro_li_uplinksets_a = {
    'US_8Gb':
        li_fc_us(name=NITRO_ASIDE_UPLINK_SET,
                 fcNetworkUris=[da_networks_n[0]['name']],
                 logicalInterconnectUri=LIs[1],
                 portConfigInfos=[{'enclosure': ENC_1, 'bay': IBS3ICMA, 'port': US_NITRO_ASIDE_UPLINKS[0],
                                   'desiredSpeed': data_common.OPSPEED8},
                                  {'enclosure': ENC_1, 'bay': IBS3ICMA, 'port': US_NITRO_ASIDE_UPLINKS[1],
                                   'desiredSpeed': data_common.OPSPEED8}
                                  ])
}

potash_li_uplinksets_b = {
    'US_4Gb':
        li_fc_us(name=POTASH_BSIDE_UPLINK_SET,
                 fcNetworkUris=[da_networks_p[1]['name']],
                 logicalInterconnectUri=LIs[0],
                 portConfigInfos=[{'enclosure': ENC_2, 'bay': IBS1ICMB, 'port': US_POTASH_BSIDE_UPLINKS[0],
                                   'desiredSpeed': data_common.OPSPEED4},
                                  {'enclosure': ENC_2, 'bay': IBS1ICMB, 'port': US_POTASH_BSIDE_UPLINKS[1],
                                   'desiredSpeed': data_common.OPSPEED4}
                                  ])
}

#################
# Server Profiles
#################


def make_conn_data(data):
    return deepcopy(data)


def make_n2n_conn_data(data):
    return make_conn_data(data)


def make_bfs_conn_data(data):
    return make_conn_data(data)


# Let network decide the request and max bandwidth
potash_conn_data = [
    {'name': 'conn-fc', 'functionType': 'FibreChannel', 'portId': IBS1MZ + ':1-b',
     'networkUri': 'FC:' + da_networks_p[0]['name']},
    {'name': 'conn-fc2', 'functionType': 'FibreChannel', 'portId': 'Auto',
     'networkUri': 'FC:' + da_networks_p[1]['name']}
]

nitro_conn_data = [
    {'name': 'conn-fc', 'functionType': 'FibreChannel', 'portId': IBS3MZ + ':1-b',
     'networkUri': 'FC:' + da_networks_n[0]['name']},
    {'name': 'conn-fc2', 'functionType': 'FibreChannel', 'portId': 'Auto',
     'networkUri': 'FC:' + da_networks_n[1]['name']}
]

potash_bfs_conn_data_b = [
    {'name': 'conn-fc', 'functionType': 'FibreChannel', 'portId': IBS1MZ + ':1-b',
     'networkUri': 'FC:' + da_networks_p[0]['name'],
     'boot': {'priority': 'Secondary',
              'bootVolumeSource': 'UserDefined',
              'targets': [
                  {'arrayWwpn': potash_bfs_a_target1_wwn, 'lun': '0'},
                  {'arrayWwpn': potash_bfs_a_target2_wwn, 'lun': '0'}]
              }
     },
    {'name': 'conn-fc2', 'functionType': 'FibreChannel', 'portId': 'Auto',
     'networkUri': 'FC:' + da_networks_p[1]['name'],
     'boot': {'priority': 'Primary',
              'bootVolumeSource': 'UserDefined',
              'targets': [
                  {'arrayWwpn': potash_bfs_b_target1_wwn, 'lun': '0'},
                  {'arrayWwpn': potash_bfs_b_target2_wwn, 'lun': '0'}]
              }
     }
]

nitro_bfs_conn_data_a = [
    {'name': 'conn-fc', 'functionType': 'FibreChannel', 'portId': IBS3MZ + ':1-b',
     'networkUri': 'FC:' + da_networks_n[0]['name'],
     'boot': {'priority': 'Primary',
              'bootVolumeSource': 'UserDefined',
              'targets': [
                  {'arrayWwpn': nitro_bfs_a_target1_wwn, 'lun': '0'},
                  {'arrayWwpn': nitro_bfs_a_target2_wwn, 'lun': '0'}]
              }
     },
    {'name': 'conn-fc2', 'functionType': 'FibreChannel', 'portId': 'Auto',
     'networkUri': 'FC:' + da_networks_n[1]['name'],
     'boot': {'priority': 'Secondary',
              'bootVolumeSource': 'UserDefined',
              'targets': [
                  {'arrayWwpn': nitro_bfs_b_target1_wwn, 'lun': '0'},
                  {'arrayWwpn': nitro_bfs_b_target2_wwn, 'lun': '0'}]
              }
     }
]

# nitro_bfs_conn_data_b has target lun '0'; make conn-fc2 Primary boot since enc2 server
nitro_bfs_conn_data_b = make_n2n_conn_data(nitro_bfs_conn_data_a)
nitro_bfs_conn_data_b[0]['boot']['priority'] = 'Secondary'
nitro_bfs_conn_data_b[1]['boot']['priority'] = 'Primary'


################################################################################
# Servers information: SP name, SH name, Aside and Bside downlink number
################################################################################
# For disable enable server downlink testing. data file driven, no hard-code in test script

potash_enc1_server_1 = {
    'sp_name': 'SP-ENC1-POTASH-BAY1',
    'sh_name': '%s, bay 1' % ENC_1,
    'enc1_downlink': 'd1',
    'enc2_downlink': 'd13',
    'conn_data': potash_conn_data,
    'icm': POTASHA
}

potash_enc2_server_1 = {
    'sp_name': 'SP-ENC2-POTASH-BAY3',
    'sh_name': '%s, bay 3' % ENC_2,
    'enc1_downlink': 'd15',
    'enc2_downlink': 'd3',
    'conn_data': potash_conn_data,
    'icm': POTASHB
}

# BFS
potash_enc2_server_2 = {
    'sp_name': 'SP-ENC2-POTASH-BAY1',
    'sh_name': '%s, bay 1' % ENC_2,
    'enc1_downlink': 'd13',
    'enc2_downlink': 'd1',
    'conn_data': potash_bfs_conn_data_b,
    'icm': POTASHB
}

nitro_enc1_server_1 = {
    'sp_name': 'SP-ENC1-NITRO-BAY2',
    'sh_name': '%s, bay 2' % ENC_1,
    'enc1_downlink': 'd2',
    'enc2_downlink': 'd14',
    'conn_data': nitro_conn_data,
    'icm': NITROA
}

# BFS
nitro_enc1_server_2 = {
    'sp_name': 'SP-ENC1-NITRO-BAY3',
    'sh_name': '%s, bay 3' % ENC_1,
    'enc1_downlink': 'd3',
    'enc2_downlink': 'd15',
    'conn_data': nitro_bfs_conn_data_a,
    'icm': NITROA
}

# BFS
nitro_enc2_server_1 = {
    'sp_name': 'SP-ENC2-NITRO-BAY2',
    'sh_name': '%s, bay 2' % ENC_2,
    'enc1_downlink': 'd14',
    'enc2_downlink': 'd2',
    'conn_data': nitro_bfs_conn_data_b,
    'icm': NITROB
}


POTASH_ASIDE_SERVER_DOWNLINKS = [
    potash_enc1_server_1['enc1_downlink'],
    potash_enc2_server_1['enc1_downlink'],
    potash_enc2_server_2['enc1_downlink']
]

POTASH_BSIDE_SERVER_DOWNLINKS = [
    potash_enc1_server_1['enc2_downlink'],
    potash_enc2_server_1['enc2_downlink'],
    potash_enc2_server_2['enc2_downlink']
]

NITRO_ASIDE_SERVER_DOWNLINKS = [
    nitro_enc1_server_1['enc1_downlink'],
    nitro_enc1_server_2['enc1_downlink'],
    nitro_enc2_server_1['enc1_downlink']
]

NITRO_BSIDE_SERVER_DOWNLINKS = [
    nitro_enc1_server_1['enc2_downlink'],
    nitro_enc1_server_2['enc2_downlink'],
    nitro_enc2_server_1['enc2_downlink']
]

ASIDE_SERVER_DOWNLINKS = POTASH_ASIDE_SERVER_DOWNLINKS + NITRO_ASIDE_SERVER_DOWNLINKS
BSIDE_SERVER_DOWNLINKS = POTASH_BSIDE_SERVER_DOWNLINKS + NITRO_BSIDE_SERVER_DOWNLINKS


#################
# Server Profiles
#################

potash_server_profiles = [
    {'type': data_common.SP_TYPE,
     'serverHardwareUri': potash_enc1_server_1['sh_name'],
     'enclosureUri': 'ENC:' + ENC_1,
     'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical',
     'macType': 'Physical',
     'wwnType': 'Physical',
     'name': potash_enc1_server_1['sp_name'],
     'description': 'WS2016 - Aside',
     'affinity': 'Bay',
     'connectionSettings': {
         'connections': make_n2n_conn_data(potash_enc1_server_1['conn_data'])}
     },
    {'type': data_common.SP_TYPE,
     'serverHardwareUri': potash_enc2_server_1['sh_name'],
     'enclosureUri': 'ENC:' + ENC_2,
     'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical',
     'macType': 'Physical',
     'wwnType': 'Physical',
     'name': potash_enc2_server_1['sp_name'],
     'description': 'WS2016 - Bside',
     'affinity': 'Bay',
     'connectionSettings': {
         'connections': make_n2n_conn_data(potash_enc2_server_1['conn_data'])}
     },
    {'type': data_common.SP_TYPE,
     'serverHardwareUri': potash_enc2_server_2['sh_name'],
     'enclosureUri': 'ENC:' + ENC_2,
     'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical',
     'macType': 'Physical',
     'wwnType': 'Physical',
     'name': potash_enc2_server_2['sp_name'],
     'description': 'Gen10 WS2016 - Bside BFS',
     'bootMode': {'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto'},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'affinity': 'Bay',
     'connectionSettings': {
         'connections': make_n2n_conn_data(potash_enc2_server_2['conn_data'])}
     }
]

nitro_server_profiles = [
    {'type': data_common.SP_TYPE,
     'serverHardwareUri': nitro_enc1_server_1['sh_name'],
     'enclosureUri': 'ENC:' + ENC_1,
     'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical',
     'macType': 'Physical',
     'wwnType': 'Physical',
     'name': nitro_enc1_server_1['sp_name'],
     'description': 'Gen10 WS2016 - Aside',
     'affinity': 'Bay',
     'connectionSettings': {
         'connections': make_n2n_conn_data(nitro_enc1_server_1['conn_data'])}
     },
    {'type': data_common.SP_TYPE,
     'serverHardwareUri': nitro_enc1_server_2['sh_name'],
     'enclosureUri': 'ENC:' + ENC_1,
     'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical',
     'macType': 'Physical',
     'wwnType': 'Physical',
     'name': nitro_enc1_server_2['sp_name'],
     'description': 'Gen10 WS2016 - Aside BFS',
     'affinity': 'Bay',
     'bootMode': {'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto'},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'connectionSettings': {
         'connections': make_n2n_conn_data(nitro_enc1_server_2['conn_data'])}
     },
    {'type': data_common.SP_TYPE,
     'serverHardwareUri': nitro_enc2_server_1['sh_name'],
     'enclosureUri': 'ENC:' + ENC_2,
     'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical',
     'macType': 'Physical',
     'wwnType': 'Physical',
     'name': nitro_enc2_server_1['sp_name'],
     'description': 'Gen10 WS2016 - Bside BFS',
     'affinity': 'Bay',
     'bootMode': {'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto'},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'connectionSettings': {
         'connections': make_n2n_conn_data(nitro_enc2_server_1['conn_data'])}
     }
]

server_profiles = potash_server_profiles + nitro_server_profiles

potash_server_profile_names =\
    [ps['name'] for ps in potash_server_profiles]

nitro_server_profile_names =\
    [ns['name'] for ns in nitro_server_profiles]

server_profile_names = potash_server_profile_names + nitro_server_profile_names

server_hws =\
    [sp['serverHardwareUri'] for sp in server_profiles]

###############################################
# LI Uplinksets uplink portStatusReason cases
###############################################

TEST_PORT_FA_ON_DA = 'Q1'
TEST_PORT_FA_ON_DA_P = 'Q1:1'

li_us_port_unlink_list = \
    [
        {
            'uplink': TEST_PORT_FA_ON_DA,
            'icm': NITROA,
            'expected_reason': 'FabricTypeMismatch',
            'logicalInterconnectUri': LIs[1],
            'usBody':
                li_fc_us(name='US_Nitro_fabric_mismatch',
                         fcNetworkUris=['FA1'],
                         portConfigInfos=[{'enclosure': ENC_1, 'bay': IBS3ICMA, 'port': TEST_PORT_FA_ON_DA,
                                           'desiredSpeed': data_common.OPSPEED16}])
        },
        {
            'uplink': TEST_PORT_FA_ON_DA_P,
            'icm': POTASHB,
            'expected_reason': 'FabricTypeMismatch',
            'logicalInterconnectUri': LIs[0],
            'usBody':
                li_fc_us(name='US_Potash_fabric_mismatch_p',
                         fcNetworkUris=['FA2'],
                         portConfigInfos=[{'enclosure': ENC_2, 'bay': IBS1ICMB, 'port': TEST_PORT_FA_ON_DA_P,
                                           'desiredSpeed': data_common.OPSPEED8}])
        }
    ]

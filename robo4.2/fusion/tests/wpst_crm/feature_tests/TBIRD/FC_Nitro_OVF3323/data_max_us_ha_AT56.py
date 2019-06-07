import copy
import ast
import data_common

appliance_ip = '15.245.131.251'
RACK = 'AT56'

ENC_1 = 'MXQ81804ZF'
ENC_2 = 'MXQ81804ZH'
ENC_3 = 'MXQ81804ZG'

enclosures = [ENC_1, ENC_2, ENC_3]

frame = 3
ENCLOSURE_URIS = ['ENC:' + enclosures[x] for x in xrange(0, frame)]

if frame == 1:
    bside_frame = 1
else:
    bside_frame = 2

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

# Interconnect Bay Set
IBS = 2
ICMA = 2
ICMB = 5

NITROA = ENC_1 + ', ' + 'interconnect ' + str(ICMA)
NITROB = ENC_2 + ', ' + 'interconnect ' + str(ICMB)

REDUNDANCY_TYPE = 'HighlyAvailable'

REDUNDANCY = 'HA'
LE = 'LE' + '-' + REDUNDANCY + '-MAX-US'
LIG = 'LIG'
EG = 'EG' + '-' + REDUNDANCY + '-MAX-US'
LI = LE + '-' + LIG


# return list of FC network names
def name_list(start, end, prefix='FA'):
    names = []
    for x1 in xrange(start, end):
        names.append(prefix + str(1) + '_' + str(x1))
        names.append(prefix + str(2) + '_' + str(x1))
    return names


# 16 DA and FA networks  [DA|FA]<enc#>_[0-15]
danetworks = \
    [{'name': n,
      'type': 'fc-networkV4',
      'linkStabilityTime': 0,
      'autoLoginRedistribution': False,
      'connectionTemplateUri': None,
      'managedSanUri': None,
      'fabricType': 'DirectAttach'} for n in name_list(0, 20, 'DA')]

fanetworks = \
    [{'name': n,
      'type': 'fc-networkV4',
      'linkStabilityTime': 30,
      'autoLoginRedistribution': True,
      'connectionTemplateUri': None,
      'managedSanUri': None,
      'fabricType': 'FabricAttach'} for n in name_list(0, 20, 'FA')]


def get_port_name(counter):
    print counter
    port = (counter / 4 + 1)
    subport = (counter % 4 + 1)
    return "Q" + str(port) + "." + str(subport)


# construct portConfigInfo example as {'enclosure': '1', 'bay': '3', 'port': 'Q1.4', 'speed': 'Auto'}
def getPortConfig(counter, bay_num):
    if bay_num == ICMA:
        enc_num = 1
    elif bay_num == ICMB:
        enc_num = bside_frame
    else:
        return None

    portconfig = "{ " + \
                 "'enclosure': '" + str(enc_num) + "', " + \
                 "'bay': '" + str(bay_num) + "', " + \
                 "'port': '" + get_port_name(counter % 24) + "', " + \
                 "'speed': 'Speed16G' }"
    return ast.literal_eval(portconfig)


# create uplinkset with format required in lig with name US_<fabric_type><enc_num>_counter
# using network <fabric_type><enc_num>_counter; port defined on specified enclosure number
def createUplinkSets(fabric_type, bay_num, count):
    if bay_num == ICMA:
        enc_num = 1
    elif bay_num == ICMB:
        enc_num = bside_frame
    else:
        return None

    network_name = fabric_type + str(enc_num) + '_' + str(count)
    body = {}
    body['name'] = 'US_' + network_name
    body['ethernetNetworkType'] = 'NotApplicable'
    body['networkType'] = 'FibreChannel'
    body['lacpTimer'] = 'Short'
    body['mode'] = 'Auto'
    body['nativeNetworkUri'] = None
    body['networkUris'] = [network_name]
    port = getPortConfig(count, bay_num)
    if (port):
        body['logicalPortConfigInfos'] = [port]
    else:
        body['logicalPortConfigInfos'] = []

    return body


# 8 DA US and 7 FA US in each Nitro - max allowed FC uplinksets per ICM
us_fa_enc1 = [createUplinkSets('FA', ICMA, counter) for counter in xrange(0, 7)]
us_da_enc1 = [createUplinkSets('DA', ICMA, counter) for counter in xrange(8, 16)]
us_fa_enc2 = [createUplinkSets('FA', ICMB, counter) for counter in xrange(0, 7)]
us_da_enc2 = [createUplinkSets('DA', ICMB, counter) for counter in xrange(8, 16)]

us_da2_enc1 = [createUplinkSets('DA', ICMA, counter) for counter in xrange(16, 17)]
us_da2_enc2 = [createUplinkSets('DA', ICMB, counter) for counter in xrange(16, 17)]

# combine uplinkset list; note that it is shallow copy, since used to read for create LE, it's ok
# used to import LE with uplinksets, then add 1 more for LI uplinkset limit error chewck
us_max = us_da_enc1 + us_fa_enc1 + us_da_enc2 + us_fa_enc2

us_aside_max = us_da_enc1 + us_fa_enc1

# used to test lig max us limit error
us_max_err_1 = copy.deepcopy(us_aside_max) + copy.deepcopy(us_da2_enc1)
us_max_err_2 = copy.deepcopy(us_max) + copy.deepcopy(us_da2_enc2)

InterconnectMapTemplate = \
    [
        {'bay': ICMA, 'enclosure': 1, 'type': data_common.NITRO_MODEL, 'enclosureIndex': 1},
        {'bay': ICMB, 'enclosure': 1, 'type': data_common.CL50_MODEL, 'enclosureIndex': 1},
        {'bay': ICMA, 'enclosure': bside_frame, 'type': data_common.CL50_MODEL,
         'enclosureIndex': bside_frame},
        {'bay': ICMB, 'enclosure': bside_frame, 'type': data_common.NITRO_MODEL,
         'enclosureIndex': bside_frame},
        {'bay': ICMA, 'enclosure': frame, 'type': data_common.CL50_MODEL, 'enclosureIndex': frame},
        {'bay': ICMB, 'enclosure': frame, 'type': data_common.CL50_MODEL, 'enclosureIndex': frame}
    ]

ligs = {
    LIG: {'name': LIG,
          'interconnectMapTemplate': InterconnectMapTemplate,
          'enclosureIndexes': [x for x in xrange(1, frame + 1)],
          'interconnectBaySet': IBS,
          'redundancyType': REDUNDANCY_TYPE,
          'uplinkSets': us_max,
          },
    'LIG-MAX-US-ERR1': {'name': 'LIG-MAX-US-ERR1',
                        'interconnectMapTemplate': InterconnectMapTemplate,
                        'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                        'interconnectBaySet': IBS,
                        'redundancyType': REDUNDANCY_TYPE,
                        'uplinkSets': us_max_err_1,
                        },
    'LIG-MAX-US-ERR2': {'name': 'LIG-MAX-US-ERR2',
                        'interconnectMapTemplate': InterconnectMapTemplate,
                        'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                        'interconnectBaySet': IBS,
                        'redundancyType': REDUNDANCY_TYPE,
                        'uplinkSets': us_max_err_2,
                        },
}

enc_group = {
    EG:
        {'name': EG,
         'enclosureCount': frame,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + LIG},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + LIG},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
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

# to be add to exceed Max per bay on Aside Nitro
li_add_uplinkset1 = {
    'name': 'li_add_uplinkset1',
    'ethernetNetworkType': 'NotApplicable',
    'networkType': 'FibreChannel',
    'networkUris': [],
    'fcNetworkUris': ['DA1_15'],
    'fcoeNetworkUris': [],
    'manualLoginRedistributionState': 'Supported',
    'connectionMode': 'Auto',
    'portConfigInfos': [{'enclosure': ENC_1, 'bay': ICMA, 'port': 'Q5:1', 'desiredSpeed': data_common.OPSPEED16}],
    'logicalInterconnectUri': None
}

li_add_uplinkset2 = {
    'name': 'li_add_uplinkset2',
    'ethernetNetworkType': 'NotApplicable',
    'networkType': 'FibreChannel',
    'networkUris': [],
    'fcNetworkUris': ['DA2_15'],
    'fcoeNetworkUris': [],
    'manualLoginRedistributionState': 'Supported',
    'connectionMode': 'Auto',
    'portConfigInfos': [{'enclosure': ENC_2, 'bay': ICMB, 'port': 'Q5:4', 'desiredSpeed': data_common.OPSPEED16}],
    'logicalInterconnectUri': None
}

###############
# Error Message
###############

MSG_CRM_MAX_FC_NETWORKS_EXCEEDED = \
    'The number of FC networks has exceeded the maximum limit of 30.'

MSG_CRM_EXCEEDS_MAX_ALLOWED_FC_NETWORKS_PER_BAY = \
    'The interconnect in bay \d+ has exceeded the maximum number of allowed FC networks.'

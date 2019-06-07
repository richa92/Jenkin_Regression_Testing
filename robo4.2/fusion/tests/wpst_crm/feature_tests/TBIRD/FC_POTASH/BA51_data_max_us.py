import copy
import ast

appliance_ip = '15.245.131.72'
RACK = 'BA51'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ENC_1 = 'CN7544044G'
ENC_2 = 'CN7545084V'
ENCLOSURE_URIS = ['ENC:' + ENC_1, 'ENC:' + ENC_2]

frame = 2

# Interconnect Bay Set
IBS = 3

POTASH3 = ENC_1 + ', ' + 'interconnect 3'
POTASH6 = ENC_2 + ', ' + 'interconnect 6'

EG = 'eg-2enc-ha-ibs3-max-us'
LIG = 'LIG-MAX-US'
LE = 'LE-HA'
LI = LE + '-' + LIG


# return list of FC network names
def nameList(start, end, prefix='FA'):
    names = []
    for x in xrange(start, end):
        names.append(prefix + str(1) + '_' + str(x))
        names.append(prefix + str(2) + '_' + str(x))
    return names


# 16 DA and FA networks  [DA|FA]<enc#>_[0-15]
danetworks = \
    [{'name': n,
      'type': 'fc-networkV4',
      'linkStabilityTime': 0,
      'autoLoginRedistribution': False,
      'connectionTemplateUri': None,
      'managedSanUri': None,
      'fabricType': 'DirectAttach'} for n in nameList(0, 20, 'DA')]

fanetworks = \
    [{'name': n,
      'type': 'fc-networkV4',
      'linkStabilityTime': 30,
      'autoLoginRedistribution': True,
      'connectionTemplateUri': None,
      'managedSanUri': None,
      'fabricType': 'FabricAttach'} for n in nameList(0, 20, 'FA')]


def get_port_name(counter):
    print counter
    port = (counter / 4 + 1)
    print ("port is %s" % port)
    subport = (counter % 4 + 1)
    print ("subport is %s" % subport)
    return "Q" + str(port) + "." + str(subport)


# construct portConfigInfo example as {'enclosure': '1', 'bay': '3', 'port': 'Q1.4', 'speed': 'Auto'}
def getPortConfig(counter, enc_num):
    if enc_num == 1:
        bay_num = 3
    elif enc_num == 2:
        bay_num = 6
    else:
        return None

    portconfig = "{ " + \
                 "'enclosure': '" + str(enc_num) + "', " + \
                 "'bay': '" + str(bay_num) + "', " + \
                 "'port': '" + get_port_name(counter % 24) + "', " + \
                 "'speed': 'Auto' }"
    return ast.literal_eval(portconfig)


# create uplinkset with format required in lig with name US_<fabric_type><enc_num>_counter
# using network <fabric_type><enc_num>_counter; port defined on specified enclosure number
def createUplinkSets(fabric_type, enc_num, count):
    networkName = fabric_type + str(enc_num) + '_' + str(count)
    body = {}
    body['name'] = 'US_' + networkName
    body['ethernetNetworkType'] = 'NotApplicable'
    body['networkType'] = 'FibreChannel'
    body['lacpTimer'] = 'Short'
    body['mode'] = 'Auto'
    body['nativeNetworkUri'] = None
    body['networkUris'] = [networkName]
    port = getPortConfig(count, enc_num)
    if (port):
        body['logicalPortConfigInfos'] = [port]
    else:
        body['logicalPortConfigInfos'] = []

    return body


# 8 DA US and 7 FA US in each Potash - max allowed FC uplinksets per ICM
us_fa_enc1 = [createUplinkSets('FA', 1, counter) for counter in xrange(0, 7)]
us_da_enc1 = [createUplinkSets('DA', 1, counter) for counter in xrange(8, 16)]
us_fa_enc2 = [createUplinkSets('FA', 2, counter) for counter in xrange(0, 7)]
us_da_enc2 = [createUplinkSets('DA', 2, counter) for counter in xrange(8, 16)]

us_da2_enc1 = [createUplinkSets('DA', 1, counter) for counter in xrange(16, 17)]
us_da2_enc2 = [createUplinkSets('DA', 2, counter) for counter in xrange(16, 17)]

# combine uplinkset list; note that it is shallow copy, since used to read for create LE, it's ok
# used to import LE with uplinksets, then add 1 more for LI uplinkset limit error chewck
us_max = us_da_enc1 + us_fa_enc1 + us_da_enc2 + us_fa_enc2
us_aside_max = us_da_enc1 + us_fa_enc1

# used to test lig max us limit error
us_max_err_1 = copy.deepcopy(us_aside_max) + copy.deepcopy(us_da2_enc1)
us_max_err_2 = copy.deepcopy(us_max) + copy.deepcopy(us_da2_enc2)

Enc2IBS3Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
    ]

ligs = {
    LIG: {'name': LIG,
          'type': 'logical-interconnect-groupV4',
          'enclosureType': 'SY12000',
          'interconnectMapTemplate': Enc2IBS3Map,
          'enclosureIndexes': [x for x in xrange(1, frame + 1)],
          'interconnectBaySet': IBS,
          'redundancyType': 'HighlyAvailable',
          'uplinkSets': us_max,
          },
    'LIG-MAX-US-ERR1': {'name': 'LIG-MAX-US-ERR1',
                        'type': 'logical-interconnect-groupV4',
                        'enclosureType': 'SY12000',
                        'interconnectMapTemplate': Enc2IBS3Map,
                        'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                        'interconnectBaySet': IBS,
                        'redundancyType': 'HighlyAvailable',
                        'uplinkSets': us_max_err_1,
                        },
    'LIG-MAX-US-ERR2': {'name': 'LIG-MAX-US-ERR2',
                        'type': 'logical-interconnect-groupV4',
                        'enclosureType': 'SY12000',
                        'interconnectMapTemplate': Enc2IBS3Map,
                        'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                        'interconnectBaySet': IBS,
                        'redundancyType': 'HighlyAvailable',
                        'uplinkSets': us_max_err_2,
                        },
}

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

# to be add to exceed Max per bay on Potash3
li_add_uplinkset1 = {
    'name': 'li_add_uplinkset1',
    'ethernetNetworkType': 'NotApplicable',
    'networkType': 'FibreChannel',
    'networkUris': [],
    'fcNetworkUris': ['DA1_15'],
    'fcoeNetworkUris': [],
    'manualLoginRedistributionState': 'Supported',
    'connectionMode': 'Auto',
    'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': 'Q5:1', 'desiredSpeed': 'Auto'}],
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
    'portConfigInfos': [{'enclosure': ENC_2, 'bay': '6', 'port': 'Q5:4', 'desiredSpeed': 'Auto'}],
    'logicalInterconnectUri': None
}

###############
# Error Message
###############

MSG_MAX_FC_NETWORKS_EXCEEDED = \
    'The number of FC networks has exceeded the maximum limit of 30.'

MSG_EXCEED_MAX_ALLED_FC_NETWORK_PER_BAY = \
    'The interconnect in bay \d+ has exceeded the maximum number of allowed FC networks.'

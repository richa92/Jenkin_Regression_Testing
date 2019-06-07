import os
import sys


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


APPLIANCE_IP = '15.245.131.251'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
REDUNDANCY = ''
frame = 3
IBS = 3
IBS_2 = 2
IBS2 = True
IBS3 = True
ENC1 = 'MXQ81804ZF'
ENC2 = 'MXQ81804ZH'
ENC3 = 'MXQ81804ZG'
ENC4 = 'XXXXXXXXXX'
ENC_List = ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3, 'ENC:' + ENC4]

#############################################
# Data that need to be checked before running test case
#  ############################################

Interconnect_name_ibs3 = [ENC1 + ', ' + 'interconnect 3', ENC2 + ', ' + 'interconnect 6']
Interconnect_name_ibs2 = [ENC1 + ', ' + 'interconnect 2', ENC2 + ', ' + 'interconnect 5']
Interconnect_dto_ibs3 = [{"name": Interconnect_name_ibs3[0]}, {"name": Interconnect_name_ibs3[1]}]
Interconnect_dto_ibs2 = [{"name": Interconnect_name_ibs2[0]}, {"name": Interconnect_name_ibs2[1]}]

# Supported SFP
Supported_port_data = {'port_name': 'Q4.1', 'type': 'Ethernet', 'enclosure': '2', 'bay': '6', 'status': 'Linked', 'speed': 'Auto',
                       'ic_name': Interconnect_name_ibs3[1], 'ic_dto': Interconnect_dto_ibs3[1]}

# Unsupported QSFP - unsplit port
unsupported_QSFP_data = {'port_name': 'Q3', 'type': 'Ethernet', 'enclosure': '2', 'bay': '6', 'status': 'Linked', 'speed': 'Auto',
                         'ic_name': Interconnect_name_ibs3[1], 'ic_dto': Interconnect_dto_ibs3[1]}

# No_SFP
No_SFP_data = {'port_name': 'Q1', 'type': 'Ethernet', 'enclosure': '1', 'bay': '2', 'status': 'Unlinked', 'speed': 'Auto',
               'ic_name': Interconnect_name_ibs2[0], 'ic_dto': Interconnect_dto_ibs2[0]}

# QSFP - split port
split_QSFP_data = {'port_name': '', 'type': 'Ethernet', 'enclosure': '1', 'bay': '3', 'speed': 'Auto',
                   'ic_name': Interconnect_name_ibs3[0], 'ic_dto': Interconnect_dto_ibs3[0]}

# QSFP - unsplit port
unsplit_QSFP_data = {'port_name': 'Q4', 'type': 'Ethernet', 'enclosure': '1', 'bay': '3', 'speed': 'Auto',
                     'ic_name': Interconnect_name_ibs3[0], 'ic_dto': Interconnect_dto_ibs3[0]}

Split_QSFP = [{"portName": "Q3.1"}, {"portName": "Q3.2"}, {"portName": "Q3.3"}, {"portName": "Q3.4"}]

# Additional ports to this list to be added if need to be tested
ports = [Supported_port_data, unsupported_QSFP_data, No_SFP_data, unsplit_QSFP_data]

uplinkset_ports_ibs2 = [No_SFP_data]
ibs3_ports = [Supported_port_data, unsupported_QSFP_data, unsplit_QSFP_data]

Linked_port = 'Q1'

# Add this list according to length of ports
logicalPortConfigInfos_ibs3 = [{'enclosure': ' ', 'bay': ' ', 'port': ' ', 'speed': 'Auto'},
                               {'enclosure': ' ', 'bay': ' ', 'port': ' ', 'speed': 'Auto'},
                               {'enclosure': ' ', 'bay': ' ', 'port': ' ', 'speed': 'Auto'},
                               {'enclosure': ' ', 'bay': ' ', 'port': ' ', 'speed': 'Auto'}
                               ]

logicalPortConfigInfos_ibs2 = [{'enclosure': ' ', 'bay': ' ', 'port': ' ', 'speed': 'Auto'},
                               {'enclosure': ' ', 'bay': ' ', 'port': ' ', 'speed': 'Auto'},
                               {'enclosure': ' ', 'bay': ' ', 'port': ' ', 'speed': 'Auto'},
                               {'enclosure': ' ', 'bay': ' ', 'port': ' ', 'speed': 'Auto'}
                               ]
# Value changes based on part number
DDMI_values_SFP_SR = {'txPowerdBm': 'numeric', 'txPowermW': 'numeric', 'rxPowerdBm': 'numeric',
                      'rxPowermW': 'numeric', 'current': 'numeric'}

DDMI_values_Unsplit_QSFP = {'txPowerdBm': 'unsupported', 'txPowermW': 'unsupported', 'rxPowerdBm': 'numeric',
                            'rxPowermW': 'numeric', 'current': 'numeric'}

DDMI_values_split_QSFP = {'txPowerdBm': 'unsupported', 'txPowermW': 'unsupported', 'rxPowerdBm': 'numeric',
                          'rxPowermW': 'numeric', 'current': 'invalid'}

#######################################################################################################################
# Transceiver Informations
########################################################################################################################
Supported_transreceiver_SFP = {"portName": ports[0]['port_name'],
                               "speed": "null",
                               "vendorName": "HPE",
                               "vendorPartNumber": "455883-B21",
                               "vendorRevision": "A",
                               "vendorOui": "00:90:65",
                               "extIdentifier": "null",
                               "digitalDiagnostics":
                               {
                                   "temperature": " 28",
                                   "voltage": "3.3125",
                                   "laneInformation":
                                        [
                                            {
                                                "laneId": "1",
                                                "rxPowermW": "unsupported",
                                                "txPowermW": "0.0477",
                                                "rxPowerdBm": "unsupported",
                                                "txPowerdBm": "-13.1605",
                                                "current": "unsupported"
                                            }
                                        ]
},
    "serialNumber": "ARR2PKS",
    "identifier": "SFP",
    "connector": "UNKNOWN_OR_UNSPECIFIED"
}

unsupported_sfp = {"portName": ports[1]['port_name'],
                   "identifier": "QSFP_PLUS", "extIdentifier": "null", "connector": "UNKNOWN_OR_UNSPECIFIED", "vendorName": "HPE",
                   "vendorOui": "fc:7c:e7", "vendorPartNumber": "845406-B21", "vendorRevision": "1",
                   "speed": "null", "serialNumber": "9CV7060027",
                   "digitalDiagnostics": {"temperature": "25", "voltage": "3.2956",
                                          "laneInformation": [{"laneId": "1", "txPowermW": "unsupported", "txPowerdBm": "unsupported",
                                                                "rxPowermW": "invalid", "rxPowerdBm": "invalid", "current": "invalid"},
                                                              {"laneId": "2", "txPowermW": "unsupported", "txPowerdBm": "unsupported",
                                                               "rxPowermW": "invalid", "rxPowerdBm": "invalid", "current": "invalid"},
                                                              {"laneId": "3", "txPowermW": "unsupported", "txPowerdBm": "unsupported",
                                                               "rxPowermW": "invalid", "rxPowerdBm": "invalid", "current": "invalid"},
                                                              {"laneId": "4", "txPowermW": "unsupported", "txPowerdBm": "unsupported",
                                                               "rxPowermW": "invalid", "rxPowerdBm": "invalid", "current": "invalid"}]}}

No_SFP = {"portName": ports[2]['port_name'],
          "speed": "null",
          "vendorName": "",
          "vendorPartNumber": "",
          "vendorRevision": "",
          "vendorOui": "00",
          "extIdentifier": "null",
          "digitalDiagnostics":
          {
    "temperature": "null",
    "voltage": "null",
    "laneInformation":
    [
    ]
},
    "serialNumber": "null",
    "identifier": "UNSET",
    "connector": "UNKNOWN_OR_UNSPECIFIED"
}

Unsplit_QSFP = {"portName": ports[3]['port_name'],
                "identifier": "QSFP_PLUS", "extIdentifier": "null",
                "connector": "UNKNOWN_OR_UNSPECIFIED", "vendorName": "HPE", "vendorOui": "00:90:65",
                "vendorPartNumber": "845410-B21", "vendorRevision": "A", "speed": "null", "serialNumber": "8C1747000T",
                "digitalDiagnostics": {"temperature": "46", "voltage": "3.2752",
                                       "laneInformation": [{"laneId": "1", "txPowermW": "unsupported", "txPowerdBm": "unsupported",
                                                            "rxPowermW": "invalid", "rxPowerdBm": "invalid", "current": "invalid"},
                                                           {"laneId": "2", "txPowermW": "unsupported", "txPowerdBm": "unsupported",
                                                            "rxPowermW": "invalid", "rxPowerdBm": "invalid", "current": "invalid"},
                                                           {"laneId": "3", "txPowermW": "unsupported", "txPowerdBm": "unsupported",
                                                            "rxPowermW": "invalid", "rxPowerdBm": "invalid", "current": "invalid"},
                                                           {"laneId": "4", "txPowermW": "unsupported", "txPowerdBm": "unsupported",
                                                            "rxPowermW": "invalid", "rxPowerdBm": "invalid", "current": "invalid"}]}}


#######################################################################################################################
# Data for Setup Creation
#######################################################################################################################

ethernet_networks = [{'name': 'Net_401',
                      'type': 'ethernet-networkV4',
                      'vlanId': '401',
                      'purpose': 'Management',
                      'smartLink': True,
                      'privateNetwork': False,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'Net_402',
                      'type': 'ethernet-networkV4',
                      'vlanId': '402',
                      'purpose': 'Management',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'}
                     ]

fc_netowrks = [{'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'FC1',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'}]

uplink_sets_in_lig_ibs3 = [
    {
        'name': 'US_Enet',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['Net_401'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': []
    },
    {
        'name': 'US-FC',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['FC1'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': []
    }
]

uplink_sets_in_lig_ibs2 = [
    {
        'name': 'US_Enet',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['Net_401'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': []
    },
    {
        'name': 'US-FC',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['FC1'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': []
    }
]

length = len(ibs3_ports)
for x in range(0, length):
    print ibs3_ports[x]
    logicalPortConfigInfos_ibs3[x]['port'] = ibs3_ports[x]['port_name']
    logicalPortConfigInfos_ibs3[x]['enclosure'] = ibs3_ports[x]['enclosure']
    logicalPortConfigInfos_ibs3[x]['bay'] = ibs3_ports[x]['bay']
    logicalPortConfigInfos_ibs3[x]['speed'] = ibs3_ports[x]['speed']
    if ibs3_ports[x]['type'] == 'Ethernet':
        uplink_sets_in_lig_ibs3[0]['logicalPortConfigInfos'].append(logicalPortConfigInfos_ibs3[x])
    elif ibs3_ports[x]['type'] == 'FC':
        uplink_sets_in_lig_ibs3[1]['logicalPortConfigInfos'].append(logicalPortConfigInfos_ibs3[x])

length2 = len(uplinkset_ports_ibs2)
for x in range(0, length2):
    logicalPortConfigInfos_ibs2[x]['port'] = uplinkset_ports_ibs2[x]['port_name']
    logicalPortConfigInfos_ibs2[x]['enclosure'] = uplinkset_ports_ibs2[x]['enclosure']
    logicalPortConfigInfos_ibs2[x]['bay'] = uplinkset_ports_ibs2[x]['bay']
    logicalPortConfigInfos_ibs2[x]['speed'] = uplinkset_ports_ibs2[x]['speed']
    if uplinkset_ports_ibs2[x]['type'] == 'Ethernet':
        uplink_sets_in_lig_ibs2[0]['logicalPortConfigInfos'].append(logicalPortConfigInfos_ibs2[x])
    elif uplinkset_ports_ibs2[x]['type'] == 'FC':
        uplink_sets_in_lig_ibs2[1]['logicalPortConfigInfos'].append(logicalPortConfigInfos_ibs2[x])


icmap_1 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

icmap_2 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]

icmap_3 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

icmap_1_ibs2 = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

icmap_2_ibs2 = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]

icmap_3_ibs2 = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 2, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 5, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

if frame == 1:
    REDUNDANCY = 'Redundant'
    InterconnectMapTemplate = icmap_1
    icmap_ibs2 = icmap_1_ibs2
elif frame == 2:
    REDUNDANCY = 'HighlyAvailable'
    InterconnectMapTemplate = icmap_2
    icmap_ibs2 = icmap_2_ibs2
elif frame == 3:
    REDUNDANCY = 'HighlyAvailable'
    InterconnectMapTemplate = icmap_3
    icmap_ibs2 = icmap_3_ibs2

LIG = 'LIG' + '_' + REDUNDANCY + '_IBS3'
LIG_IBS2 = 'LIG' + '_' + REDUNDANCY + '_IBS2'
EG = 'EG' + '_' + REDUNDANCY
LE = 'LE' + '_' + REDUNDANCY


ligs = [{'name': LIG,
         'interconnectMapTemplate': InterconnectMapTemplate,
         'enclosureIndexes': [x for x in xrange(1, frame + 1)],
         'interconnectBaySet': IBS,
         'redundancyType': REDUNDANCY,
         'uplinkSets': list(uplink_sets_in_lig_ibs3),
         'downlinkSpeedMode': 'SPEED_25GB'
         },
        {'name': LIG_IBS2,
         'interconnectMapTemplate': icmap_ibs2,
         'enclosureIndexes': [x for x in xrange(1, frame + 1)],
         'interconnectBaySet': IBS_2,
         'redundancyType': REDUNDANCY,
         'uplinkSets': list(uplink_sets_in_lig_ibs2),
         'downlinkSpeedMode': 'SPEED_25GB'
         }]

enc_group = {'name': EG,
             'enclosureCount': frame,
             'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + LIG_IBS2},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + LIG_IBS2},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG}],
             'ipAddressingMode': "DHCP"
             }

LE = {'name': LE,
      'enclosureUris': ENC_List[0:frame],
      'enclosureGroupUri': 'EG:' + EG,
      'firmwareBaselineUri': None,
      'forceInstallFirmware': False
      }


SUBPORT_STATUS_WAIT = '60s'
FUSION_PROMPT = '#'
FUSION_IP = '15.245.131.251'
FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
vlanids = ['401', '402']

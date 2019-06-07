import os
import sys


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


APPLIANCE_IP = '15.245.131.108'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
REDUNDANCY = ''
frame = 1
IBS = 3
IBS2 = False
IBS3 = True
ENC1 = 'CN754406WY'
ENC2 = 'XXXXXXXXXX'
ENC3 = 'XXXXXXXXXX'
ENC4 = 'XXXXXXXXXX'
ENC_List = ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3, 'ENC:' + ENC4]

#############################################
# Data that need to be checked before running test case
#  ############################################

Interconnect_name_ibs3 = [ENC1 + ', ' + 'interconnect 3', ENC1 + ', ' + 'interconnect 6']
Interconnect_name_ibs2 = [ENC1 + ', ' + 'interconnect 2', ENC1 + ', ' + 'interconnect 5']
Interconnect_dto_ibs3 = [{"name": Interconnect_name_ibs3[0]}, {"name": Interconnect_name_ibs3[1]}]
Interconnect_dto_ibs2 = [{"name": Interconnect_name_ibs2[0]}, {"name": Interconnect_name_ibs2[1]}]

# Supported SFP
Supported_port_data = {'port_name': 'Q3', 'type': 'Ethernet', 'enclosure': '1', 'bay': '3', 'status': 'Linked', 'speed': 'Auto',
                       'ic_name': Interconnect_name_ibs3[0], 'ic_dto': Interconnect_dto_ibs3[0]}

# Unsupported QSFP - unsplit port
unsupported_QSFP_data = {'port_name': 'Q5', 'type': 'Ethernet', 'enclosure': '1', 'bay': '3', 'status': 'Linked', 'speed': 'Auto',
                         'ic_name': Interconnect_name_ibs3[0], 'ic_dto': Interconnect_dto_ibs3[0]}

# No_SFP
No_SFP_data = {'port_name': 'Q2', 'type': 'Ethernet', 'enclosure': '1', 'bay': '3', 'status': 'Unlinked', 'speed': 'Auto',
               'ic_name': Interconnect_name_ibs3[0], 'ic_dto': Interconnect_dto_ibs3[0]}

# QSFP - split port
split_QSFP_data = {'port_name': '', 'type': 'Ethernet', 'enclosure': '1', 'bay': '3', 'speed': 'Auto',
                   'ic_name': Interconnect_name_ibs3[0], 'ic_dto': Interconnect_dto_ibs3[0]}

# QSFP - unsplit port
unsplit_QSFP_data = {'port_name': 'Q4', 'type': 'Ethernet', 'enclosure': '1', 'bay': '3', 'speed': 'Auto',
                     'ic_name': Interconnect_name_ibs3[0], 'ic_dto': Interconnect_dto_ibs3[0]}

Split_QSFP = [{"portName": "Q3.1"}, {"portName": "Q3.2"}, {"portName": "Q3.3"}, {"portName": "Q3.4"}]

# Additional ports to this list to be added if need to be tested

uplinkset_ports_ibs3 = [Supported_port_data, unsupported_QSFP_data, No_SFP_data, unsplit_QSFP_data]
uplinkset_ports_ibs2 = []

ports = [Supported_port_data, unsupported_QSFP_data, No_SFP_data, unsplit_QSFP_data]

Linked_port = 'Q1'

# Add this list according to length of ports
logicalPortConfigInfos = [{'enclosure': ' ', 'bay': ' ', 'port': ' ', 'speed': 'Auto'},
                          {'enclosure': ' ', 'bay': ' ', 'port': ' ', 'speed': 'Auto'},
                          {'enclosure': ' ', 'bay': ' ', 'port': ' ', 'speed': 'Auto'},
                          {'enclosure': ' ', 'bay': ' ', 'port': ' ', 'speed': 'Auto'}
                          ]
# Value changes based on part number
DDMI_values_SFP_SR = {'txPowerdBm': 'numeric', 'txPowermW': 'numeric', 'rxPowerdBm': 'unsupported',
                      'rxPowermW': 'unsupported', 'current': 'unsupported'}

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
    "serialNumber": "AMJ0QJC",
    "identifier": "SFP",
    "connector": "UNKNOWN_OR_UNSPECIFIED"
}

unsupported_sfp = {"portName": ports[1]['port_name'],
                   "identifier": "QSFP_PLUS", "extIdentifier": "null", "connector": "UNKNOWN_OR_UNSPECIFIED", "vendorName": "HPE",
                   "vendorOui": "00:90:65", "vendorPartNumber": "720211-B21", "vendorRevision": "A ",
                   "speed": "null", "serialNumber": "WY30PT8         ",
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
                "digitalDiagnostics": {"temperature": "25", "voltage": "3.2956",
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

uplink_sets_in_lig = [
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
length = len(ports)
for x in range(0, length):
    logicalPortConfigInfos[x]['port'] = ports[x]['port_name']
    logicalPortConfigInfos[x]['enclosure'] = ports[x]['enclosure']
    logicalPortConfigInfos[x]['bay'] = ports[x]['bay']
    logicalPortConfigInfos[x]['speed'] = ports[x]['speed']
    if ports[x]['type'] == 'Ethernet':
        uplink_sets_in_lig[0]['logicalPortConfigInfos'].append(logicalPortConfigInfos[x])
    elif ports[x]['type'] == 'FC':
        uplink_sets_in_lig[1]['logicalPortConfigInfos'].append(logicalPortConfigInfos[x])


icmap_1 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

icmap_2 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]

icmap_3 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

if frame == 1:
    REDUNDANCY = 'Redundant'
elif frame == 2:
    REDUNDANCY = 'HighlyAvailable'

LIG = 'LIG' + '_' + REDUNDANCY
EG = 'EG' + '_' + REDUNDANCY
LE = 'LE' + '_' + REDUNDANCY

ligs = [{'name': LIG,
         'interconnectMapTemplate': icmap_1,
         'enclosureIndexes': [x for x in xrange(1, frame + 1)],
         'interconnectBaySet': IBS,
         'redundancyType': REDUNDANCY,
         'uplinkSets': list(uplink_sets_in_lig),
         'downlinkSpeedMode':'SPEED_10GB'
         }]

enc_group = {'name': EG,
             'enclosureCount': frame,
             'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG}],
             'ipAddressingMode': "DHCP"
             }

LE = {'name': LE,
      'enclosureUris': ENC_List[0:frame],
      'enclosureGroupUri': 'EG:' + EG,
      'firmwareBaselineUri': None,
      'forceInstallFirmware': False
      }

Interconnect_name = [ENC1 + ', ' + 'interconnect 3', ENC1 + ', ' + 'interconnect 6']
Interconnect_dto = [{"name": Interconnect_name[0]}, {"name": Interconnect_name[1]}]

SUBPORT_STATUS_WAIT = '60s'
FUSION_PROMPT = '#'
FUSION_IP = '15.245.131.108'
FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
FUSION_TIMEOUT = 180              # Timeout.  Move this out???

vlanids = ['401', '402']

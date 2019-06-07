import os
import sys

from copy import deepcopy


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


appliance_ip = '15.186.9.136'

ip_pattern            'Ip=(192\\.\\d+\\.\\d+\\.\\d+)'
gatewayip_pattern    'Gateway=(0\\.\\d+\\.\\d+\\.\\d+)'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ethernet_networks = [{'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'name': 'eth_10', 'privateNetwork': False, 'purpose': 'General', 'smartLink': True, 'vlanId': 10},
                     {'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'name': 'eth_20', 'privateNetwork': False, 'purpose': 'General', 'smartLink': True, 'vlanId': 20},
                     {'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'name': 'eth_30', 'privateNetwork': False, 'purpose': 'General', 'smartLink': True, 'vlanId': 30}
                     ]

fcoe_networks = [
    {
        "name": "fcoe-1050",
        "vlanId": "1050",
        "type": "fcoe-networkV4"
    },
    {
        "name": "fcoe-1051",
        "vlanId": "1051",
        "type": "fcoe-networkV4"
    }
]

fc_networks = [{'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'FC1',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'FC2',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'FC1_nitro',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'FC2_nitro',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               ]
frame = 2
IBS = 3
IBS1 = 1
ENC_1 = 'MXQ80503HJ'
ENC_2 = 'MXQ734024N'
ENC_3 = ''
ENC_4 = ''
ENC_5 = ''
IC_bay_set = 1
IC_bay_set_pair = IC_bay_set + 3

port_name = ['Q1', 'Q2', 'Q3']
port_name1 = ['Q1', 'Q2', 'Q3']
ENC_List = ['ENC:' + ENC_1, 'ENC:' + ENC_2, 'ENC:' + ENC_3, 'ENC:' + ENC_4, 'ENC:' + ENC_5]

ENC1ICBAY3 = 'MXQ80503HJ, interconnect 3'
bay_numbers = ['3', '6']

uplink_sets_lig_A = {
    'US1': {
        'name': 'EthernetUS1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth_10'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'}]},
    'US2': {
        'name': 'FCOE1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe-1050'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q2', 'speed': 'Auto'}]},
    'US3': {
        'name': 'FC1',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['FC1_nitro'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Speed16G'}]}
}

uplink_sets_lig_B = {
    'US1': {
        'name': 'EthernetUS1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth_10'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q1', 'speed': 'Auto'}]},
    'US2': {
        'name': 'FCOE2',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe-1051'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q2', 'speed': 'Auto'}]},
    'US3': {
        'name': 'FC2',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['FC2_nitro'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q3', 'speed': 'Speed16G'}]}
}

Edit_sets = {
    'US1': {
        'name': 'EthernetUS1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth_10'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'}]},
    'US2': {
        'name': 'FCOE1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe-1050'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q2', 'speed': 'Auto'}]},
    'US3': {
        'name': 'FC1',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['FC1_nitro'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Speed16G'}]},
    'US4': {
        'name': 'uplink4',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth_20'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q4', 'speed': 'Auto'}]}
}

Edit_sets1 = {
    'US1': {
        'name': 'EthernetUS1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth_10'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q2', 'speed': 'Auto'}]},
    'US2': {
        'name': 'FCOE2',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe-1051'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q1', 'speed': 'Auto'}]},
    'US3': {
        'name': 'FC2',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['FC2'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q3', 'speed': 'Speed16G'}]}
}

uplink_sets1 = {'US1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                        'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'}]},
                'US2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                        'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'}
                                                   ]}}

InterconnectMapTemplate_A = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2}
    ]

InterconnectMapTemplate_B = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]

REDUNDANCY = 'AB'

LIG_A = 'LIG-A'
LIG_B = 'LIG-B'
LIG1 = 'LIG-carbon-Redundant'
EG = 'EG' + '-' + REDUNDANCY
LE = 'LE' + '_' + REDUNDANCY
LI_A = LE + '-' + LIG_A
LI_B = LE + '-' + LIG_B
LI = [LI_A, LI_B]

icmap_1 = \
    [
        {'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1},
        {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1}
    ]

ligs = [
    {'name': LIG_A,
     'enclosureIndexes': [x for x in xrange(1, frame + 1)],
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': InterconnectMapTemplate_A,
     'interconnectBaySet': IBS,
     'redundancyType': 'NonRedundantASide',
     'uplinkSets': [deepcopy(uplink_sets_lig_A['US1']), deepcopy(uplink_sets_lig_A['US2']), deepcopy(uplink_sets_lig_A['US3'])]
     },
    {'name': LIG_B,
     'enclosureIndexes': [x for x in xrange(1, frame + 1)],
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': InterconnectMapTemplate_B,
     'interconnectBaySet': IBS,
     'redundancyType': 'NonRedundantBSide',
     'uplinkSets': [deepcopy(uplink_sets_lig_B['US1']), deepcopy(uplink_sets_lig_B['US2']), deepcopy(uplink_sets_lig_B['US3'])]
     },

    {'name': LIG1,
     'type': 'logical-interconnect-groupV5',
             'enclosureIndexes': [-1],
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': icmap_1,
             'interconnectBaySet': IBS1,
             'redundancyType': 'Redundant',
     'uplinkSets': [deepcopy(uplink_sets1['US1']), deepcopy(uplink_sets1['US2'])]
     }
]

ligs1 = [
    {'name': LIG_A,
     'enclosureIndexes': [x for x in xrange(1, frame + 1)],
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': InterconnectMapTemplate_A,
     'interconnectBaySet': IBS,
     'redundancyType': 'NonRedundantASide',
     'uplinkSets': [deepcopy(uplink_sets_lig_A['US1']), deepcopy(uplink_sets_lig_A['US2']), deepcopy(uplink_sets_lig_A['US3'])]
     },
    {'name': LIG_B,
     'enclosureIndexes': [x for x in xrange(1, frame + 1)],
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': InterconnectMapTemplate_B,
     'interconnectBaySet': IBS,
     'redundancyType': 'NonRedundantBSide',
     'uplinkSets': [deepcopy(uplink_sets_lig_B['US1']), deepcopy(uplink_sets_lig_B['US2']), deepcopy(uplink_sets_lig_B['US3'])]
     },
]

editlig = [
    {'name': LIG_A,
     'interconnectMapTemplate': InterconnectMapTemplate_A,
     'enclosureIndexes': [x for x in xrange(1, frame + 1)],
     'interconnectBaySet': IBS,
     'redundancyType': 'NonRedundantASide',
     'uplinkSets': [deepcopy(Edit_sets['US1']), deepcopy(Edit_sets['US2']), deepcopy(Edit_sets['US3']), deepcopy(Edit_sets['US4']), ]
     }

]

enc_group = {'name': EG,
             'enclosureCount': frame,
             'interconnectBayMappings':
             [{"interconnectBay": IC_bay_set, "enclosureIndex": 1, "logicalInterconnectGroupUri": 'LIG:' + LIG1},
              {"interconnectBay": IC_bay_set_pair, "enclosureIndex": 1, "logicalInterconnectGroupUri": 'LIG:' + LIG1},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG_A},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG_B}],
             'ipAddressingMode': "DHCP"
             }

LEbody = {'name': LE,
          'enclosureUris': ENC_List[0:frame],
          'enclosureGroupUri': 'EG:' + EG,
          'firmwareBaselineUri': None,
          'forceInstallFirmware': False
          }

Interconnect_name = [ENC_1 + ', ' + 'interconnect 3', ENC_2 + ', ' + 'interconnect 6', ENC_1 + ', ' + 'interconnect 6']
Interconnect_dto = [{"name": Interconnect_name[0]}, {"name": Interconnect_name[1]}]
Module = 'Nitro'
Module1 = 'AB'
ICM_dto = [{'name': 'MXQ80503HJ, interconnect 3'}, {'name': 'MXQ734024N, interconnect 6'}]
ICM1_dto = [{'name': 'MXQ80503HJ, interconnect 3'}, {'name': 'MXQ80503HJ, interconnect 3'}]
SUP_dto = [{'name': 'MXQ80503HJ, interconnect 6'}]
LI_Name = [LI_A, LI_B]
LI_dto = [{'name': 'LE_AB-LIG-A'}, {'name': 'LE_AB-LIG-B'}]

test = [{'type': 'ServerProfileV10',
         'serverHardwareUri': ENC_1 + ', bay 7',
         'serverHardwareTypeUri': '',
         'enclosureUri': 'ENC:' + ENC_1,
         'enclosureGroupUri': 'EG:' + EG,
         'serialNumberType': 'Virtual',
         'macType': 'Virtual',
         'wwnType': 'Virtual',
         'name': 'Profile2',
         'description': '',
         'affinity': 'Bay',
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         'connectionSettings':{'connections': [{'id': 1,
                                                'name': '1',
                                                'functionType': 'Ethernet',
                                                'portId': 'Mezz 3:1-a',
                                                'requestedMbps': '2500',
                                                'networkUri': 'ETH:eth_10',
                                                'mac': None,
                                                'wwpn': '',
                                                'wwnn': ''},
                                               {'id': 2,
                                                'name': '2',
                                                'functionType': 'Ethernet',
                                                'portId': 'Mezz 3:2-a',
                                                'requestedMbps': '2500',
                                                'networkUri': 'ETH:eth_10',
                                                'mac': None,
                                                'wwpn': '',
                                                'wwnn': ''},
                                               {'id': 3,
                                                'name': '3',
                                                'functionType': 'FibreChannel',
                                                'portId': 'Mezz 3:1-b',
                                                'requestedMbps': '2500',
                                                'networkUri': 'FC:FC1_nitro',
                                                'mac': None,
                                                'wwpn': '10:00:70:20:6F:76:B5:92',
                                                'wwnn': '20:00:70:20:6F:76:B5:92'},
                                               {'id': 4,
                                                'name': '4',
                                                'functionType': 'FibreChannel',
                                                'portId': 'Mezz 3:2-b',
                                                'requestedMbps': '2500',
                                                'networkUri': 'FC:FC2_nitro',
                                                'mac': None,
                                                'wwpn': '10:00:70:20:6F:76:B5:93',
                                                'wwnn': '20:00:70:20:6F:76:B5:93'},
                                               {'id': 5,
                                                'name': '5',
                                                'functionType': 'FibreChannel',
                                                'portId': 'Mezz 1:1',
                                                'requestedMbps': 'Auto',
                                                'networkUri': 'FC:FC1',
                                                'mac': None,
                                                'boot': {"priority": 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{"arrayWwpn": "20020002AC01CDEC", 'lun': "0"}], 'iscsi': {}},
                                                'wwpn': '10:00:00:00:c9:71:7b:30',
                                                'wwnn': '20:00:00:00:c9:71:7b:30'},
                                               {'id': 6,
                                                'name': '6',
                                                'functionType': 'FibreChannel',
                                                'portId': 'Mezz 1:2',
                                                'requestedMbps': 'Auto',
                                                'networkUri': 'FC:FC2',
                                                'mac': None,
                                                'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21020002AC01CDEC', 'lun': '0'}], 'iscsi': {}},
                                                'wwpn': '10:00:00:00:c9:71:7b:31',
                                                'wwnn': '20:00:00:00:c9:71:7b:31'},
                                               ]}}]
server_profiles = [{'type': 'ServerProfileV10',
                    'serverHardwareUri': ENC_1 + ', bay 1',
                    'serverHardwareTypeUri': '',
                    'enclosureUri': 'ENC:' + ENC_1,
                    'enclosureGroupUri': 'EG:' + EG,
                    'serialNumberType': 'Physical',
                    'macType': 'Physical',
                    'wwnType': 'Physical',
                    'name': 'Profile1',
                    'description': '',
                    'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': False},
                    'connectionSettings': {'connections': [{'id': 1,
                                                            'name': '1',
                                                            'functionType': 'Ethernet',
                                                            'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': '2500',
                                                            'networkUri': 'ETH:eth_10',
                                                            'mac': None,
                                                            'wwpn': '',
                                                            'wwnn': ''},
                                                           {'id': 2,
                                                            'name': '2',
                                                            'functionType': 'Ethernet',
                                                            'portId': 'Mezz 3:2-a',
                                                            'requestedMbps': '2500',
                                                            'networkUri': 'ETH:eth_10',
                                                            'mac': None,
                                                            'wwpn': '',
                                                            'wwnn': ''},
                                                           {'id': 3,
                                                            'name': '3',
                                                            'functionType': 'FibreChannel',
                                                            'portId': 'Mezz 3:1-b',
                                                            'requestedMbps': '2500',
                                                            'networkUri': 'FCOE:fcoe-1050',
                                                            'mac': None,
                                                            'wwpn': '10:00:70:20:6F:76:B5:80',
                                                            'wwnn': '20:00:70:20:6F:76:B5:80'},
                                                           {'id': 4,
                                                            'name': '4',
                                                            'functionType': 'FibreChannel',
                                                            'portId': 'Mezz 3:2-b',
                                                            'requestedMbps': '2500',
                                                            'networkUri': 'FCOE:fcoe-1051',
                                                            'mac': None,
                                                            'wwpn': '10:00:70:20:6F:76:B5:81',
                                                            'wwnn': '20:00:70:20:6F:76:B5:81'}]}},
                   {'type': 'ServerProfileV10',
                    'serverHardwareUri': ENC_1 + ', bay 7',
                    'serverHardwareTypeUri': '',
                    'enclosureUri': 'ENC:' + ENC_1,
                    'enclosureGroupUri': 'EG:' + EG,
                    'serialNumberType': 'Virtual',
                    'macType': 'Virtual',
                    'wwnType': 'Virtual',
                    'name': 'Profile2',
                    'description': '',
                    'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings':{'connections': [{'id': 1,
                                                           'name': '1',
                                                           'functionType': 'Ethernet',
                                                           'portId': 'Mezz 3:1-a',
                                                           'requestedMbps': '2500',
                                                           'networkUri': 'ETH:eth_10',
                                                           'mac': None,
                                                           'wwpn': '',
                                                           'wwnn': ''},
                                                          {'id': 2,
                                                           'name': '2',
                                                           'functionType': 'Ethernet',
                                                           'portId': 'Mezz 3:2-a',
                                                           'requestedMbps': '2500',
                                                           'networkUri': 'ETH:eth_10',
                                                           'mac': None,
                                                           'wwpn': '',
                                                           'wwnn': ''},
                                                          {'id': 3,
                                                           'name': '3',
                                                           'functionType': 'FibreChannel',
                                                           'portId': 'Mezz 3:1-b',
                                                           'requestedMbps': '2500',
                                                           'networkUri': 'FC:FC1_nitro',
                                                           'mac': None,
                                                           'wwpn': '10:00:70:20:6F:76:B5:92',
                                                           'wwnn': '20:00:70:20:6F:76:B5:92'},
                                                          {'id': 4,
                                                           'name': '4',
                                                           'functionType': 'FibreChannel',
                                                           'portId': 'Mezz 3:2-b',
                                                           'requestedMbps': '2500',
                                                           'networkUri': 'FC:FC2_nitro',
                                                           'mac': None,
                                                           'wwpn': '10:00:70:20:6F:76:B5:93',
                                                           'wwnn': '20:00:70:20:6F:76:B5:93'},
                                                          {'id': 5,
                                                           'name': '5',
                                                           'functionType': 'FibreChannel',
                                                           'portId': 'Mezz 1:1',
                                                           'requestedMbps': 'Auto',
                                                           'networkUri': 'FC:FC1',
                                                           'mac': None,
                                                           'boot': {"priority": 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{"arrayWwpn": "20020002AC01CDEC", 'lun': "0"}], 'iscsi': {}},
                                                           'wwpn': '10:00:00:00:c9:71:7b:30',
                                                           'wwnn': '20:00:00:00:c9:71:7b:30'},
                                                          {'id': 6,
                                                           'name': '6',
                                                           'functionType': 'FibreChannel',
                                                           'portId': 'Mezz 1:2',
                                                           'requestedMbps': 'Auto',
                                                           'networkUri': 'FC:FC2',
                                                           'mac': None,
                                                           'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21020002AC01CDEC', 'lun': '0'}], 'iscsi': {}},
                                                           'wwpn': '10:00:00:00:c9:71:7b:31',
                                                           'wwnn': '20:00:00:00:c9:71:7b:31'},
                                                          ]}}
                   ]
FUSION_PROMPT = '#'
FUSION_IP = '15.186.9.136'
FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
FUSION_TIMEOUT = 180              # Timeout.  Move this out???

kill_diskspd = "TASKKILL /F /IM diskspd.exe"

kill_paexec = "TASKKILL /F /IM diskspd.exe"

diskspd_cmd = ["C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b10K -h -L F:\\sample.dat >C:\\Server1.dat",
               "C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b10K -h -L F:\\sample.dat >C:\\Server2.dat"]

ping_cmd1 = ["cmd /c ping -n 10 -l 1024 gateway_ip>sample.txt"]

server_credentials = {'userName': 'Administrator', 'password': 'password@123'}
pingfile = 'sample.txt'
Ping_Lost = 'Lost'
number = 5
flag = 'Windows'

ENC1_SERVER_FcoE_ILO = {'ilo_ip': '15.186.22.183', 'username': 'Administrator', 'password': 'hpvse123', 'OS': 'windows'}
ENC1_SERVER_Fc_ILO = {'ilo_ip': '15.186.18.15', 'username': 'Administrator', 'password': 'hpvse123', 'OS': 'windows'}

ILO_List = [ENC1_SERVER_FcoE_ILO, ENC1_SERVER_Fc_ILO]

ENC1_SERVER_FcoE_cred = {'username': 'Administrator', 'password': 'password@123', 'ip': ''}
ENC1_SERVER_Fc_ILO_cred = {'username': 'Administrator', 'password': 'password@123', 'ip': ''}

server_details = [ENC1_SERVER_FcoE_cred, ENC1_SERVER_Fc_ILO_cred]

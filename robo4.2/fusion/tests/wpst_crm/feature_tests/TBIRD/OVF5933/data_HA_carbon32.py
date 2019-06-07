import os
import sys

from copy import deepcopy


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


appliance_ip = '15.186.9.136'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ethernet_networks = [{'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'name': 'eth_10', 'privateNetwork': False, 'purpose': 'General', 'smartLink': True, 'vlanId': 10},
                     {'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'name': 'eth_20', 'privateNetwork': False, 'purpose': 'General', 'smartLink': True, 'vlanId': 20}
                     ]

fcoe_networks = [
    {
        "name": "fcoe-1002",
        "vlanId": "1002",
        "type": "fcoe-networkV4"
    },
    {
        "name": "fcoe-1004",
        "vlanId": "1004",
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
                'fabricType': 'FabricAttach'}]

frame = 2
IBS = 1
IBS1 = 3
ENC_2 = 'MXQ80503HJ'
ENC_1 = 'MXQ734024N'
enclosureCount = 2
IC_bay_set = 1
IC_bay_set_pair = IC_bay_set + 3
REDUNDANCY = 'Redundant'
REDUNDANCY1 = 'HighlyAvailable'
LIG1 = 'LIG1' + '_' + REDUNDANCY
LIG2 = 'LIG1' + '_' + REDUNDANCY1
EG1 = 'EG1' + '_' + REDUNDANCY
LE = 'LE' + '_' + REDUNDANCY
LI = LE + '-' + LIG1 + '-1'
LI1 = LE + '-' + LIG2

port_name = ['1']
port_name1 = ['1']
ENC_List = ['ENC:' + ENC_1, 'ENC:' + ENC_2]

bay_numbers = ['1', '4']

uplink_sets = {'US1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'}]},
               'US2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'}]}

               }

uplink_sets1 = {
    'US1': {
        'name': 'EthernetUS1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth_10'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q2', 'speed': 'Auto'},
                                   {'enclosure': '2', 'bay': '6', 'port': 'Q4', 'speed': 'Auto'}]
    }}

Edit_sets = {'US': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                    'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'}]}
             }

icmap_1 = \
    [
        {'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
        {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
    ]

icmap_2 = \
    [
        {'bay': 1, 'enclosure': 1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': 1},
        {'bay': 4, 'enclosure': 1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': 1},
        {'bay': 1, 'enclosure': 2, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': 2},
        {'bay': 4, 'enclosure': 2, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': 2}
    ]

icmap_3 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]

ligs = [
    {'name': LIG1,
     'type': 'logical-interconnect-groupV5',
     'enclosureIndexes': [-1],
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': icmap_1,
     'interconnectBaySet': IBS,
     'redundancyType': REDUNDANCY,
     'uplinkSets': [deepcopy(uplink_sets['US1']), deepcopy(uplink_sets['US2'])]
     },
    {'name': LIG2,
     'enclosureIndexes': [x for x in xrange(1, frame + 1)],
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': icmap_3,
     'interconnectBaySet': IBS1,
     'redundancyType': REDUNDANCY1,
     'telemetryConfiguration':{'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': 12, 'sampleInterval': 300},
     'uplinkSets': [deepcopy(uplink_sets1['US1'])]

     }]

editlig = [
    {'name': LIG1,
     'type': 'logical-interconnect-groupV5',
             'interconnectMapTemplate': icmap_1,
             'enclosureIndexes': [-1],
             'interconnectBaySet': IBS,
             'redundancyType': REDUNDANCY,
             'uplinkSets': [deepcopy(Edit_sets['US'])]
     }]

enc_group = {'name': EG1,
             'enclosureCount': enclosureCount,
             'interconnectBayMappings':
             [{"interconnectBay": IC_bay_set, "enclosureIndex": 1, "logicalInterconnectGroupUri": 'LIG:' + LIG1},
              {"interconnectBay": IC_bay_set_pair, "enclosureIndex": 1, "logicalInterconnectGroupUri": 'LIG:' + LIG1},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG2},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG2}],
             'ipAddressingMode': "DHCP"
             }

LEbody = {'name': LE,
          'enclosureUris': ENC_List[0:frame],
          'enclosureGroupUri': 'EG:' + EG1,
          'firmwareBaselineUri': None,
          'forceInstallFirmware': False
          }

Interconnect_name = [ENC_1 + ', ' + 'interconnect 1', ENC_1 + ', ' + 'interconnect 4', ]
Interconnect_dto = [{"name": Interconnect_name[0]}, {"name": Interconnect_name[1]}]
Module = 'Carbon'
Module1 = 'HA'
ICM_dto = [{'name': 'CN754406W5, interconnect 1'}, {'name': 'CN754406W5, interconnect 4'}]
ICM1_dto = [{'name': 'CN754406W5, interconnect 1'}, {'name': 'CN754406W5, interconnect 4'}]
LI_dto = [{'name': LI}, {'name': LI1}]
SUP_dto = [{'name': 'CN754406W5, interconnect 6'}]
LI_Name = [LI, LI1]
server_profiles = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC_1 + ', bay 7',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC_1, 'enclosureGroupUri': 'EG:' + EG1,
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Profile1', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                         'requestedMbps': '2500', 'networkUri': 'ETH:eth_10',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1',
                                         'requestedMbps': '2500', 'networkUri': 'FC:FC1',
                                         'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined',
                                                  'targets': [{'arrayWwpn': '20020002AC01CDEC', 'lun': '0'}]},
                                         'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:30', 'wwnn': '20:00:00:00:c9:71:7b:30'},
                                        {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2',
                                         'requestedMbps': '2500', 'networkUri': 'FC:FC1',
                                         'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined',
                                                  'targets': [{'arrayWwpn': '21020002AC01CDEC', 'lun': '0'}]},
                                         'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:31', 'wwnn': '20:00:00:00:c9:71:7b:31'},
                                        ]}}
                   ]
FUSION_PROMPT = '#'
FUSION_IP = '15.245.131.62'
FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
FUSION_TIMEOUT = 180              # Timeout.  Move this out???

server_credentials = {'userName': 'Administrator', 'password': 'hpvse@1'}
pingfile = 'sample.txt'
Ping_Lost = 'Lost'
number = 5
flag = 'Windows'

diskspd_cmd = ["C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b10K -h -L D:\\sample.dat >C:\\Server1.dat"]

ping_cmd1 = ["cmd /c ping -n 10 -l 1024 gateway_ip>sample.txt"]

ENC1_SERVER_Fc_ILO = {'ilo_ip': '15.186.18.15', 'username': 'Administrator', 'password': 'hpvse123', 'OS': 'windows'}

ILO_List = [ENC1_SERVER_Fc_ILO]

ENC1_SERVER_FcoE_cred = {'username': 'Administrator', 'password': 'password@123', 'ip': '', 'gateway_ip': ''}

server_details = [ENC1_SERVER_FcoE_cred]

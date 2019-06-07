from copy import deepcopy


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


def Remove_Whitespace(instring):
    return instring.strip()


appliance_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

SUBPORT_STATUS_WAIT = '60s'
FUSION_PROMPT = '#'
FUSION_IP = '15.245.131.142'
FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
FUSION_TIMEOUT = 180              # Timeout.  Move this out???


REDUNDANCY = 'HA'
LIG = 'LIG'
frame = 2
IBS = 3
LIG = 'LIG'
EG = 'EG' + '-' + REDUNDANCY
LIG_ETH1_UPLINKS = ['Q1', 'Q1']
LIG_FC_FA_UPLINKS = ['Q4:1', 'Q5']
LIG_FC_DA_UPLINKS = ['Q2', 'Q2:1']
ENC1 = 'MXQ71902DM'
ENC2 = 'MXQ71906M8'
ENC3 = 'XXXXXXXXXX'
ENC4 = 'XXXXXXXXXX'
LI = 'LE' + '-' + 'LIG'
LI_dto = {'name': LI}
ENCs = [ENC1, ENC2]
ENC_List = ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3, 'ENC:' + ENC4]
bay_numbers = ['3', '6']
traffic_time = ['200sec']
IC1_ports = ['Q4:1', 'Q2']  # FA PORTS ,DA PORTS OF IC3
IC2_ports = ['Q5', 'Q2:1']  # FA PORTS ,DA PORTS OF IC6
FA_PORTS = ['Q4:1', 'Q5']
DA_PORTS = ['Q2', 'Q2:1']
ICM3_FA_port = [IC1_ports[0]]
ICM3_DA_port = [IC1_ports[1]]

kill_diskspd = "TASKKILL /F /IM diskspd.exe"

ethernet_networks = [{
    'type': 'ethernet-networkV4',
    'ethernetNetworkType': 'Tagged',
    'name': 'eth_401',
    'privateNetwork': False,
    'purpose': 'General',
    'smartLink': True,
    'vlanId': 401
}]

fc_netowrks = [{'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'FA1',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'FA2',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 0,
                'autoLoginRedistribution': False,
                'name': 'DA1',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'DirectAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 0,
                'autoLoginRedistribution': False,
                'name': 'DA2',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'DirectAttach'}]
uplink_sets_in_lig = [{
    'name': 'US-eth1',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['eth_401'],
    'lacpTimer': 'Short',
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': LIG_ETH1_UPLINKS[0], 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': LIG_ETH1_UPLINKS[0], 'speed': 'Auto'}
    ]
},
    {
        'name': 'US-FA1',
        'networkType': 'FibreChannel',
        'ethernetNetworkType': None,
        'networkUris': ['FA1'],
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'primaryPort': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': LIG_FC_FA_UPLINKS[0], 'speed': 'Speed32G'},

        ]
},
    {
        'name': 'US-FA2',
        'networkType': 'FibreChannel',
        'ethernetNetworkType': None,
        'networkUris': ['FA2'],
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'primaryPort': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': LIG_FC_FA_UPLINKS[1], 'speed': 'Speed32G'},

        ]
},
    {
        'name': 'US-DA1',
        'networkType': 'FibreChannel',
        'ethernetNetworkType': None,
        'networkUris': ['DA1'],
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'primaryPort': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': LIG_FC_DA_UPLINKS[0], 'speed': 'Speed16G'},

        ]
},
    {
        'name': 'US-DA2',
        'networkType': 'FibreChannel',
        'ethernetNetworkType': None,
        'networkUris': ['DA2'],
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'primaryPort': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': LIG_FC_DA_UPLINKS[1], 'speed': 'Speed16G'},

        ]
}
]

InterconnectMapTemplate = [
    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
]

ligs = {'LIG':
        {'name': LIG,
         'interconnectMapTemplate': InterconnectMapTemplate,
         'enclosureIndexes': [x for x in xrange(1, frame + 1)],
         'interconnectBaySet': IBS,
         'redundancyType': 'HighlyAvailable',
         'telemetryConfiguration': {'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': 12, 'sampleInterval': 60},
         'uplinkSets': list(uplink_sets_in_lig)
         }
        }

enc_group = {
    'EG':
        {'name': EG,
         'enclosureCount': frame,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG}],
         'ipAddressingMode': 'DHCP'
         }
}

LE_Nitro = {
    'LE':
        {'name': 'LE',
         'enclosureUris': ENC_List[0:frame],
         'enclosureGroupUri': 'EG:' + EG,
         'firmwareBaselineUri': None,
         'forceInstallFirmware': False
         }
}

# server profile names
ENC1_SP_1_NAME = 'SP-enc1-bay1'
ENC2_SP_1_NAME = 'SP-enc2-bay12'

server_profiles = [{'type': 'ServerProfileV10',
                    'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '',
                    'enclosureUri': 'ENC:' + ENC1,
                    'enclosureGroupUri': 'EG:%s' % EG,
                    'serialNumberType': 'Physical',
                    'macType': 'Physical',
                    'wwnType': 'Physical',
                    'name': ENC1_SP_1_NAME,
                    'description': 'Blackbird Windows - Aside',
                    'affinity': 'Bay',
                    'connectionSettings': {'connections': [{'id': 1,
                                                            'name': 'conn-net1',
                                                            'functionType': 'Ethernet',
                                                            'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': 2500,
                                                            'networkUri': 'ETH:eth_401',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 2,
                                                            'name': 'conn-net2',
                                                            'functionType': 'Ethernet',
                                                            'portId': 'Mezz 3:2-a',
                                                            'requestedMbps': 2500,
                                                            'networkUri': 'ETH:eth_401',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 3,
                                                            'name': 'conn-fc1',
                                                            'functionType': 'FibreChannel',
                                                            'portId': 'Mezz 3:1-b',
                                                            'requestedMbps': 8000,
                                                            'networkUri': 'FC:FA1',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 4,
                                                            'name': 'conn-fc2',
                                                            'functionType': 'FibreChannel',
                                                            'portId': 'Mezz 3:2-b',
                                                            'requestedMbps': 8000,
                                                            'networkUri': 'FC:FA2',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None}
                                                           ]}},

                   {'type': 'ServerProfileV10',
                    'serverHardwareUri': ENC2 + ', bay 12',
                    'serverHardwareTypeUri': '',
                    'enclosureUri': 'ENC:' + ENC2,
                    'enclosureGroupUri': 'EG:%s' % EG,
                    'serialNumberType': 'Physical',
                    'macType': 'Physical',
                    'wwnType': 'Physical',
                    'name': ENC2_SP_1_NAME,
                    'description': 'Blackbird Windows - Aside',
                    'affinity': 'Bay',
                    'connectionSettings': {'connections': [{'id': 1,
                                                            'name': 'conn-net1',
                                                            'functionType': 'Ethernet',
                                                            'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': 2500,
                                                            'networkUri': 'ETH:eth_401',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 2,
                                                            'name': 'conn-net2',
                                                            'functionType': 'Ethernet',
                                                            'portId': 'Mezz 3:2-a',
                                                            'requestedMbps': 2500,
                                                            'networkUri': 'ETH:eth_401',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 3,
                                                            'name': 'conn-fc1',
                                                            'functionType': 'FibreChannel',
                                                            'portId': 'Mezz 3:1-b',
                                                            'requestedMbps': 8000,
                                                            'networkUri': 'FC:DA1',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 4,
                                                            'name': 'conn-fc2',
                                                            'functionType': 'FibreChannel',
                                                            'portId': 'Mezz 3:2-b',
                                                            'requestedMbps': 8000,
                                                            'networkUri': 'FC:DA2',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None}
                                                           ]}}]

server_details = {'username': 'Administrator', 'password': 'hpvse@1'}

ilo_details = [{'ilo_ip': '15.245.132.203', 'username': 'Administrator', 'password': 'hpvse123'}, {'ilo_ip': '15.245.132.232', 'username': 'Administrator', 'password': 'hpvse123'}]

Interconnect_name = [ENC1 + ', ' + 'interconnect 3', ENC2 + ', ' + 'interconnect 6']
Interconnect_dto = [{"name": Interconnect_name[0]}, {"name": Interconnect_name[1]}]

counters = ['fcInvalidCRC', 'fcRxBbCredit0', 'fcRxLipCount', 'fcClass2RxFrames', 'fcRxLossSig', 'fcRxInvalidSet', 'fcClass2TxFrames', 'fcTxBbCredit0', 'fcDelimiterErrors', 'fcRxEncodeDisparity', 'fcClass3RxFrames', 'fcClass3TxFrames', 'fcRxGoodFrames', 'fcRxLinkFail', 'fcRxPrimSeqErr', 'fcRxFrameTooLong', 'fcRxByt', 'fcClass3Discards', 'fcTxByt', 'fcRxRuntFrames']

FC_counters = ['fcClass3RxFrames', 'fcClass3TxFrames', 'fcTxByt', 'fcRxByt']

diskspd_cmd = ["C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d1300 -r -w70 -t9 -o9 -b10K -h -L G:\\sample.dat >C:\\sample1.dat",
               "C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d1300 -r -w70 -t9 -o9 -b10K -h -L E:\\sample.dat >C:\\sample2.dat"]

diskspd_cmd_1hr = ["C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d36000 -r -w70 -t9 -o9 -b10K -h -L G:\\sample.dat >C:\\sample1.dat",
                   "C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d36000 -r -w70 -t9 -o9 -b10K -h -L E:\\sample.dat >C:\\sample2.dat"]

diskspd_cmd1 = ["C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d1000 -r -w70 -t9 -o9 -b10K -h -L G:\\sample.dat >C:\\OVF5608_file1.dat",
                "C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d1000 -r -w70 -t9 -o9 -b20K -h -L G:\\sample.dat >C:\\OVF5608_file1.dat",
                "C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d1000 -r -w70 -t9 -o9 -b30K -h -L G:\\sample.dat >C:\\OVF5608_file1.dat"]

diskspd_cmd2 = ["C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d1000 -r -w70 -t9 -o9 -b10K -h -L E:\\sample.dat >C:\\OVF5608_file2.dat",
                "C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d1000 -r -w70 -t9 -o9 -b20K -h -L E:\\sample.dat >C:\\OVF5608_file2.dat",
                "C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d1000 -r -w70 -t9 -o9 -b30K -h -L E:\\sample.dat >C:\\OVF5608_file2.dat"]

Uplink_speed_16G = ['US_FA1_16Gb', 'US_FA2_16Gb']
Uplink_speed_8G_FA = ['US_FA1_8Gb', 'US_FA2_8Gb']
Uplink_speed_8G_DA = ['US_DA1_8Gb', 'US_DA2_8Gb']
US_name_FA = ['US-FA1', 'US-FA2']
US_name_DA = ['US-DA1', 'US-DA2']
li_uplinksets = {
    'US_DA1_8Gb':
        {'name': 'US-DA1',
         'ethernetNetworkType': 'NotApplicable',
         'networkType': 'FibreChannel',
         'networkUris': [],
         'fcNetworkUris': ['DA1'],
         'fcoeNetworkUris': [],
         'manualLoginRedistributionState': 'Supported',
         'connectionMode': 'Auto',
         'portConfigInfos': [{'enclosure': ENC1, 'bay': '3', 'port': LIG_FC_DA_UPLINKS[0], 'desiredSpeed': 'Speed8G'}],
         'logicalInterconnectUri': None},
    'US_DA2_8Gb':
        {'name': 'US-DA2',
         'ethernetNetworkType': 'NotApplicable',
         'networkType': 'FibreChannel',
         'networkUris': [],
         'fcNetworkUris': ['DA2'],
         'fcoeNetworkUris': [],
         'manualLoginRedistributionState': 'Supported',
         'connectionMode': 'Auto',
         'portConfigInfos': [{'enclosure': ENC2, 'bay': '6', 'port': LIG_FC_DA_UPLINKS[1], 'desiredSpeed': 'Speed8G'}],
         'logicalInterconnectUri': None},
    'US_FA1_16Gb':
        {'name': 'US-FA1',
         'ethernetNetworkType': 'NotApplicable',
         'networkType': 'FibreChannel',
         'networkUris': [],
         'fcNetworkUris': ['FA1'],
         'fcoeNetworkUris': [],
         'manualLoginRedistributionState': 'Supported',
         'connectionMode': 'Auto',
         'portConfigInfos': [{'enclosure': ENC1, 'bay': '3', 'port': LIG_FC_FA_UPLINKS[0], 'desiredSpeed': 'Speed16G'}],
         'logicalInterconnectUri': None},
    'US_FA2_16Gb':
        {'name': 'US-FA2',
         'ethernetNetworkType': 'NotApplicable',
         'networkType': 'FibreChannel',
         'networkUris': [],
         'fcNetworkUris': ['FA2'],
         'fcoeNetworkUris': [],
         'manualLoginRedistributionState': 'Supported',
         'connectionMode': 'Auto',
         'portConfigInfos': [{'enclosure': ENC2, 'bay': '6', 'port': LIG_FC_FA_UPLINKS[1], 'desiredSpeed': 'Speed16G'}],
         'logicalInterconnectUri': None},
    'US_FA1_8Gb':
        {'name': 'US-FA1',
         'ethernetNetworkType': 'NotApplicable',
         'networkType': 'FibreChannel',
         'networkUris': [],
         'fcNetworkUris': ['FA1'],
         'fcoeNetworkUris': [],
         'manualLoginRedistributionState': 'Supported',
         'connectionMode': 'Auto',
         'portConfigInfos': [{'enclosure': ENC1, 'bay': '3', 'port': LIG_FC_FA_UPLINKS[0], 'desiredSpeed': 'Speed8G'}],
         'logicalInterconnectUri': None},
    'US_FA2_8Gb':
        {'name': 'US-FA2',
         'ethernetNetworkType': 'NotApplicable',
         'networkType': 'FibreChannel',
         'networkUris': [],
         'fcNetworkUris': ['FA2'],
         'fcoeNetworkUris': [],
         'manualLoginRedistributionState': 'Supported',
         'connectionMode': 'Auto',
         'portConfigInfos': [{'enclosure': ENC2, 'bay': '6', 'port': LIG_FC_FA_UPLINKS[1], 'desiredSpeed': 'Speed8G'}],
         'logicalInterconnectUri': None},
}

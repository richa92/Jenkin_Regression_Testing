def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


def Remove_Whitespace(instring):
    return instring.strip()

############################
# Values that need to be changed before running the test cases
#############################

APPLIANCE_IP = '15.245.131.132'
appliance_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

RACK = 'AZ51'
frame = 2
IBS = 3

ENC1 = 'CN7545061V'
ENC2 = 'CN7545085D'
ENC3 = 'XXXXXXXXXX'
ENC4 = 'XXXXXXXXXX'

icmap_1 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2}
    ]

icmap_2 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
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
    icmap = icmap_1
elif frame == 2:
    REDUNDANCY = 'HighlyAvailable'
    icmap = icmap_2
elif frame == 3:
    REDUNDANCY = 'HighlyAvailable'
    icmap = icmap_3

ENC_List = ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3, 'ENC:' + ENC4]

# server profile names

ENC1_SP_1_NAME = 'Enc1_Bay10'
ENC2_SP_1_NAME = 'Enc2_Bay7'
server_profile_names = [ENC1_SP_1_NAME, ENC2_SP_1_NAME]

# servers name

ENC1_SERVER_1 = '%s, bay 10' % ENC1
ENC2_SERVER_1 = '%s, bay 7' % ENC2
servers = [ENC1_SERVER_1, ENC2_SERVER_1]

ICM3_ETH_UPLINK = 'Q6'
ICM6_ETH_UPLINK = 'Q6'
LIG_DA_UPLINKS_ICM3 = 'Q4:3'
LIG_DA_UPLINKS_ICM6 = 'Q4:3'
LIG_FA_UPLINKS_ICM3 = 'Q3:1'
LIG_FA_UPLINKS_ICM6 = 'Q3:1'

ilo_details = [{'ilo_ip': '15.245.133.180', 'username': 'Administrator', 'password': 'hpvse123'},
               {'ilo_ip': '15.245.132.72', 'username': 'Administrator', 'password': 'hpvse123'}]

server_details = [{'username': 'Administrator', 'password': 'hpvse@1'}, {'username': 'Administrator', 'password': 'hpvse@1'}]

###############################################################################################################

LIG = 'LIG'
EG = 'EG'
LI = 'LE' + '-' + LIG
LI_dto = {'name': LI}
LE = 'LE'

Packet_Interval = '200sec'
wait_for_clear_counter = '300sec'
Wait_for_Traffic = '100sec'

IC1_ports = [LIG_FA_UPLINKS_ICM3, LIG_DA_UPLINKS_ICM3]

IC2_ports = [LIG_FA_UPLINKS_ICM6, LIG_DA_UPLINKS_ICM6]

uplink_ports_ICM3 = [LIG_FA_UPLINKS_ICM3, LIG_DA_UPLINKS_ICM3, ICM3_ETH_UPLINK]
uplink_ports_ICM6 = [LIG_FA_UPLINKS_ICM6, LIG_DA_UPLINKS_ICM6, ICM6_ETH_UPLINK]

Delete_Network = ['FA1', 'DA1']

kill_diskspd = "TASKKILL /F /IM diskspd.exe"

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


uplink_sets_in_lig = [
    {
        'name': 'US-NET401',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['Net_401'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': ICM3_ETH_UPLINK, 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': ICM6_ETH_UPLINK, 'speed': 'Auto'}
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
            {'enclosure': '1', 'bay': '3', 'port': LIG_DA_UPLINKS_ICM3, 'speed': 'Auto'}
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
            {'enclosure': '2', 'bay': '6', 'port': LIG_DA_UPLINKS_ICM6, 'speed': 'Auto'}
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
            {'enclosure': '1', 'bay': '3', 'port': LIG_FA_UPLINKS_ICM3, 'speed': 'Auto'}
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
            {'enclosure': '2', 'bay': '6', 'port': LIG_FA_UPLINKS_ICM3, 'speed': 'Auto'}
        ]
    }
]


ligs = [{'name': LIG,
         'interconnectMapTemplate': icmap,
         'enclosureIndexes': [x for x in xrange(1, frame + 1)],
         'interconnectBaySet': IBS,
         'redundancyType': REDUNDANCY,
         'uplinkSets': list(uplink_sets_in_lig),
         'telemetryConfiguration':{'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': 12, 'sampleInterval': 90}
         }]


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

LE = {'name': LE,
      'enclosureUris': ENC_List[0:frame],
      'enclosureGroupUri': 'EG:' + EG,
      'firmwareBaselineUri': None,
      'forceInstallFirmware': False
      }

server_profiles = [{'type': 'ServerProfileV10',
                    'serverHardwareUri': ENC1 + ', bay 10',
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
                                                            'networkUri': 'ETH:Net_401',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 2,
                                                            'name': 'conn-net2',
                                                            'functionType': 'Ethernet',
                                                            'portId': 'Mezz 3:2-a',
                                                            'requestedMbps': 2500,
                                                            'networkUri': 'ETH:Net_401',
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
                    'serverHardwareUri': ENC2 + ', bay 7',
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
                                                            'networkUri': 'ETH:Net_401',
                                                            'mac': None,
                                                            'wwpn': None,
                                                            'wwnn': None},
                                                           {'id': 2,
                                                            'name': 'conn-net2',
                                                            'functionType': 'Ethernet',
                                                            'portId': 'Mezz 3:2-a',
                                                            'requestedMbps': 2500,
                                                            'networkUri': 'ETH:Net_401',
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
                                                           ]}}
                   ]

diskspd_cmd = ["C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d1200 -r -w70 -t9 -o9 -b10K -h -L D:\\sample.dat >C:\\OVF5609_file1.dat",
               "C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d1200 -r -w70 -t9 -o9 -b10K -h -L D:\\sample.dat >C:\\OVF5609_file2.dat"]

diskspd_cmd1 = ["C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d500 -r -w70 -t9 -o9 -b10K -h -L D:\\sample.dat >C:\\OVF5609_file1.dat",
                "C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d300 -r -w70 -t9 -o9 -b20K -h -L D:\\sample.dat >C:\\OVF5609_file1.dat",
                "C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d300 -r -w70 -t9 -o9 -b30K -h -L D:\\sample.dat >C:\\OVF5609_file1.dat"]

diskspd_cmd2 = ["C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d500 -r -w70 -t9 -o9 -b10K -h -L D:\\sample.dat >C:\\OVF5609_file2.dat",
                "C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d300 -r -w70 -t9 -o9 -b20K -h -L D:\\sample.dat >C:\\OVF5609_file2.dat",
                "C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d300 -r -w70 -t9 -o9 -b30K -h -L D:\\sample.dat >C:\\OVF5609_file2.dat"]

diskspd_cmd_3600 = ["C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d3600 -r -w70 -t9 -o9 -b10K -h -L D:\\sample.dat >C:\\OVF5609_file1.dat",
                    "C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d3600 -r -w70 -t9 -o9 -b10K -h -L D:\\sample.dat >C:\\OVF5609_file2.dat"]


Interconnect_name = [ENC1 + ', ' + 'interconnect 3', ENC2 + ', ' + 'interconnect 6']
Interconnect_dto = [{"name": Interconnect_name[0]}, {"name": Interconnect_name[1]}]


counters = ['fcRxUcastPkts', 'fcRxBcastPkts', 'fcTxBcastPkts', 'fcInvalidCRC', 'fcRxFrameTooLong', 'fcRxLipCount', 'fcRxInvalidSet', 'fcRxTruncFrames', 'fcRxDropFrames', 'fcRxByt', 'fcRxNosCount', 'fcTxGoodFrames', 'fcDelimiterErrors', 'fcRxRuntFrames', 'fcRxLossSig', 'fcRxEncodeDisparity', 'fcRxOtherErr', 'fcTxFifoUnderRun', 'fcTxByt', 'fcTxUcastPkts', 'fcRxGoodFrames', 'fcRxBbCredit0', 'fcRxLinkFail', 'fcRxPrimSeqErr', 'fcTxBbCredit0', 'fcRxErrFrames', 'fcTxDropFrames']

FC_counters = ['fcRxUcastPkts', 'fcTxUcastPkts', 'fcClass3RxFrames', 'fcClass3TxFrames', 'fcRxByt', 'fcTxByt']
Uplink_speed_4G = ['US_FA1_4Gb', 'US_FA2_4Gb', 'US_DA1_4Gb', 'US_DA2_4Gb']
Uplink_speed_8G = ['US_FA1_8Gb', 'US_FA2_8Gb', 'US_DA1_8Gb', 'US_DA2_8Gb']
Uplink_speed_2G = ['US_FA1_2Gb', 'US_FA2_2Gb']
US_name = ['US-FA1', 'US-FA2', 'US-DA1', 'US-DA2']

li_uplinksets = {
    'US_FA1_2Gb':
        {'name': 'US-FA1',
         'ethernetNetworkType': 'NotApplicable',
         'networkType': 'FibreChannel',
         'networkUris': [],
         'fcNetworkUris': ['FA1'],
         'fcoeNetworkUris': [],
         'manualLoginRedistributionState': 'Supported',
         'connectionMode': 'Auto',
         'portConfigInfos': [{'enclosure': ENC1, 'bay': '3', 'port': LIG_FA_UPLINKS_ICM3, 'desiredSpeed': 'Speed2G'}],
         'logicalInterconnectUri': None},
    'US_FA2_2Gb':
        {'name': 'US-FA2',
         'ethernetNetworkType': 'NotApplicable',
         'networkType': 'FibreChannel',
         'networkUris': [],
         'fcNetworkUris': ['FA2'],
         'fcoeNetworkUris': [],
         'manualLoginRedistributionState': 'Supported',
         'connectionMode': 'Auto',
         'portConfigInfos': [{'enclosure': ENC2, 'bay': '6', 'port': LIG_FA_UPLINKS_ICM6, 'desiredSpeed': 'Speed2G'}],
         'logicalInterconnectUri': None},
    'US_DA1_4Gb':
        {'name': 'US-DA1',
         'ethernetNetworkType': 'NotApplicable',
         'networkType': 'FibreChannel',
         'networkUris': [],
         'fcNetworkUris': ['DA1'],
         'fcoeNetworkUris': [],
         'manualLoginRedistributionState': 'Supported',
         'connectionMode': 'Auto',
         'portConfigInfos': [{'enclosure': ENC1, 'bay': '3', 'port': LIG_DA_UPLINKS_ICM3, 'desiredSpeed': 'Speed4G'}],
         'logicalInterconnectUri': None},
    'US_DA2_4Gb':
        {'name': 'US-DA2',
         'ethernetNetworkType': 'NotApplicable',
         'networkType': 'FibreChannel',
         'networkUris': [],
         'fcNetworkUris': ['DA2'],
         'fcoeNetworkUris': [],
         'manualLoginRedistributionState': 'Supported',
         'connectionMode': 'Auto',
         'portConfigInfos': [{'enclosure': ENC2, 'bay': '6', 'port': LIG_DA_UPLINKS_ICM6, 'desiredSpeed': 'Speed4G'}],
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
         'portConfigInfos': [{'enclosure': ENC1, 'bay': '3', 'port': LIG_DA_UPLINKS_ICM3, 'desiredSpeed': 'Speed8G'}],
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
         'portConfigInfos': [{'enclosure': ENC2, 'bay': '6', 'port': LIG_DA_UPLINKS_ICM6, 'desiredSpeed': 'Speed8G'}],
         'logicalInterconnectUri': None},
    'US_FA1_4Gb':
    {'name': 'US-FA1',
            'ethernetNetworkType': 'NotApplicable',
            'networkType': 'FibreChannel',
            'networkUris': [],
            'fcNetworkUris': ['FA1'],
            'fcoeNetworkUris': [],
            'manualLoginRedistributionState': 'Supported',
            'connectionMode': 'Auto',
            'portConfigInfos': [{'enclosure': ENC1, 'bay': '3', 'port': LIG_FA_UPLINKS_ICM3, 'desiredSpeed': 'Speed4G'}],
            'logicalInterconnectUri': None},
    'US_FA2_4Gb':
        {'name': 'US-FA2',
         'ethernetNetworkType': 'NotApplicable',
         'networkType': 'FibreChannel',
         'networkUris': [],
         'fcNetworkUris': ['FA2'],
         'fcoeNetworkUris': [],
         'manualLoginRedistributionState': 'Supported',
         'connectionMode': 'Auto',
         'portConfigInfos': [{'enclosure': ENC2, 'bay': '6', 'port': LIG_FA_UPLINKS_ICM6, 'desiredSpeed': 'Speed4G'}],
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
         'portConfigInfos': [{'enclosure': ENC1, 'bay': '3', 'port': LIG_FA_UPLINKS_ICM3, 'desiredSpeed': 'Speed8G'}],
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
         'portConfigInfos': [{'enclosure': ENC2, 'bay': '6', 'port': LIG_FA_UPLINKS_ICM6, 'desiredSpeed': 'Speed8G'}],
         'logicalInterconnectUri': None},
}

SUBPORT_STATUS_WAIT = '60s'
FUSION_PROMPT = '#'
FUSION_IP = '15.245.131.132'
FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
FUSION_TIMEOUT = 180              # Timeout.  Move this out???

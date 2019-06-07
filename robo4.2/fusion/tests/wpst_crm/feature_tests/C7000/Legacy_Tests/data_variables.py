import os

cwd = os.getcwd()
download_to_path = cwd


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist
APPLIANCE_IP = '15.245.133.155'
ENCLOSURE_IP = '15.245.129.1'
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
enclosure_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

SWITCH_USERNAME = 'Administrator'
SWITCH_PASSWORD = 'wpsthpvse1'
SWITCH_PROMPT = '>'
SWITCH_TIMEOUT = 300

appliance_cred = ['root', 'hpvse1']

modes = {'Active', 'StandBy'}

debug = ['terminal debugging', 'terminal monitor']
undodebug = 'undo debugging all'
undo = 'undo shutdown'

network_user = {'enabled': True, 'password': 'wpsthpvse1', 'roles': ['Network administrator'], 'type': 'UserAndRoles', 'userName': 'NetworkUser'}

users = [{'enabled': True, 'password': 'wpsthpvse1', 'roles': ['Backup administrator'], 'type': 'UserAndRoles', 'userName': 'BackupUser'},
         {'enabled': True, 'password': 'wpsthpvse1', 'roles': ['Server administrator'], 'type': 'UserAndRoles', 'userName': 'ServerUser'},
         {'enabled': True, 'password': 'wpsthpvse1', 'roles': ['Read only'], 'type': 'UserAndRoles', 'userName': 'ReadOnlyUser'},
         {'enabled': True, 'password': 'wpsthpvse1', 'roles': ['Storage administrator'], 'type': 'UserAndRoles', 'userName': 'Storageuser'}]

ethernet_101 = [{'name': 'net_101-E', 'type': 'ethernet-networkV4', 'vlanId': 101, 'purpose': 'General', 'smartLink': True,
                 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                {'name': 'net_101-F', 'type': 'ethernet-networkV4', 'vlanId': 101, 'purpose': 'General', 'smartLink': True,
                 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                {'name': 'net_101-G', 'type': 'ethernet-networkV4', 'vlanId': 101, 'purpose': 'General', 'smartLink': True,
                 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'}]

ethernet_networks = [{'name': 'net_101-A', 'type': 'ethernet-networkV4', 'vlanId': 101, 'purpose': 'General', 'smartLink': True,
                      'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_101-B', 'type': 'ethernet-networkV4', 'vlanId': 101, 'purpose': 'General', 'smartLink': True,
                      'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_101-C', 'type': 'ethernet-networkV4', 'vlanId': 101, 'purpose': 'General', 'smartLink': True,
                      'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_101-D', 'type': 'ethernet-networkV4', 'vlanId': 101, 'purpose': 'General', 'smartLink': True,
                      'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_102-A', 'type': 'ethernet-networkV4', 'vlanId': 102, 'purpose': 'General', 'smartLink': True,
                      'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_102-B', 'type': 'ethernet-networkV4', 'vlanId': 102, 'purpose': 'General', 'smartLink': True,
                      'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_103-A', 'type': 'ethernet-networkV4', 'vlanId': 103, 'purpose': 'General', 'smartLink': True,
                      'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_103-B', 'type': 'ethernet-networkV4', 'vlanId': 103, 'purpose': 'General', 'smartLink': True,
                      'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_104-A', 'type': 'ethernet-networkV4', 'vlanId': 104, 'purpose': 'General', 'smartLink': True,
                      'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_104-B', 'type': 'ethernet-networkV4', 'vlanId': 104, 'purpose': 'General', 'smartLink': True,
                      'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_105', 'type': 'ethernet-networkV4', 'vlanId': 105, 'purpose': 'General', 'smartLink': True,
                      'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'}]

ethernet_lacp = [{'name': 'net_101', 'type': 'ethernet-networkV4', 'vlanId': 101, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                 {'name': 'net_102', 'type': 'ethernet-networkV4', 'vlanId': 102, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                 {'name': 'net_103', 'type': 'ethernet-networkV4', 'vlanId': 103, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                 {'name': 'net_104', 'type': 'ethernet-networkV4', 'vlanId': 104, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                 {'name': 'net_105', 'type': 'ethernet-networkV4', 'vlanId': 105, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                 {'name': 'net_401', 'type': 'ethernet-networkV4', 'vlanId': 401, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'}]

Bulk_enet = [{'vlanIdRange': '101-104',
              'namePrefix': 'prod',
              'privateNetwork': False,
              'smartLink': True,
              'purpose': 'General',
              'type': 'bulk-ethernet-network',
              'bandwidth': {'maximumBandwidth': 20000,
                            'typicalBandwidth': 2500
                            }},
             {'vlanIdRange': '105-108',
              'namePrefix': 'dev',
              'privateNetwork': False,
              'smartLink': True,
              'purpose': 'General',
              'type': 'bulk-ethernet-network',
              'bandwidth': {'maximumBandwidth': 20000,
                            'typicalBandwidth': 2500
                            }},
             {'vlanIdRange': '109-112',
              'namePrefix': 'test',
              'privateNetwork': False,
              'smartLink': True,
              'purpose': 'General',
              'type': 'bulk-ethernet-network',
              'bandwidth': {'maximumBandwidth': 20000,
                            'typicalBandwidth': 2500
                            }}
             ]

fcnets = [{"type": "fc-networkV4",
           "name": "SAN_A1",
           "fabricType": "FabricAttach",
           "linkStabilityTime": 30,
           "autoLoginRedistribution": True
           },
          {"type": "fc-networkV4",
           "name": "SAN_A2",
           "fabricType": "FabricAttach",
           "linkStabilityTime": 30,
           "autoLoginRedistribution": True
           },
          {"type": "fc-networkV4",
           "name": "SAN_B1",
           "fabricType": "FabricAttach",
           "linkStabilityTime": 30,
           "autoLoginRedistribution": True
           },
          {"type": "fc-networkV4",
           "name": "SAN_B2",
           "fabricType": "FabricAttach",
           "linkStabilityTime": 30,
           "autoLoginRedistribution": True
           }]

network_sets = [{'name': 'NWset-A', 'type': 'network-setV4', 'networkUris': ['net_105'], 'nativeNetworkUri': None},
                {'name': 'NWset-1', 'type': 'network-setV4', 'networkUris': ['net_101-A', 'net_101-B'], 'nativeNetworkUri': None}]

network_2 = [{'name': 'NWset-E', 'type': 'network-setV4', 'networkUris': ['net_101-F'], 'nativeNetworkUri': None},
             {'name': 'NWset-F', 'type': 'network-setV4', 'networkUris': ['net_101-G'], 'nativeNetworkUri': None},
             {'name': 'nn', 'type': 'network-setV4', 'networkUris': ['net_101-C', 'net_101-D', 'net_101-G'], 'nativeNetworkUri': None}]

ENC1 = 'AR56-EN11'
LIG1 = 'LIG-1'
EG1 = 'EG-1'
US1 = 'US-1A'
INTERCONNECTS = ['AR56-EN11, interconnect 1', 'AR56-EN11, interconnect 2']
LE1 = 'AR56-EN11'
LIG2 = 'LIG-LACP'

US1 = 'US-1A'
test_nets = ['test_109', 'test_110', 'test_111', 'test_112']
enets = ['net_101-A', 'net_101-B']
IC_port = 'X5'
dev_prod = ['dev_105', 'dev_106', 'dev_107', 'dev_108', 'prod_101', 'prod_102', 'prod_103', 'prod_104']
san = ['SAN_A1', 'SAN_B1', 'SAN_A2']

uplink_sets = {'UplinkSet_1': {'name': 'US-1A', 'mode': 'Auto', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['net_101-B'], 'nativeNetworkUri': None, 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'port': 'X5', 'speed': 'Auto'},
                                                          {'bay': '2', 'port': 'X5', 'speed': 'Auto'}]},
               'UplinkSet_2': {'name': 'US-Agg1', 'mode': 'Auto', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['net_401'], 'nativeNetworkUri': None, 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '3', 'port': 'X3', 'speed': 'Auto'},
                                                          {'bay': '3', 'port': 'X5', 'speed': 'Auto'},
                                                          {'bay': '3', 'port': 'X6', 'speed': 'Auto'}]},
               'UplinkSet_3': {'name': 'dev', 'mode': 'Auto', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['dev_105', 'dev_106', 'dev_107', 'dev_108'], 'nativeNetworkUri': None, 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'port': 'X5', 'speed': 'Auto'}]},
               'UplinkSet_4': {'name': 'prod', 'mode': 'Auto', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['prod_101', 'prod_102', 'prod_103', 'prod_104'], 'nativeNetworkUri': None, 'primaryPort': {'bay': '3', 'port': 'X7'},
                               'logicalPortConfigInfos': [{'bay': '1', 'port': 'X4', 'speed': 'Auto'},
                                                          {'bay': '2', 'port': 'X5', 'speed': 'Auto'}]},
               'UplinkSet_5': {'name': 'SAN_A1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['SAN_A1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'port': 'X7', 'speed': 'Auto'}]},
               'UplinkSet_6': {'name': 'SAN_B1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['SAN_B1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'},
                                                          {'bay': '2', 'port': 'X2', 'speed': 'Auto'}]},
               'UplinkSet_7': {'name': 'SAN_A2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['SAN_A2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': []},
               'UplinkSet_8': {'name': 'dev', 'mode': 'Auto', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['dev_105', 'dev_106', 'dev_107', 'dev_108'], 'nativeNetworkUri': None, 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'port': 'X5', 'speed': 'Auto'},
                                                          {'bay': '2', 'port': 'X8', 'speed': 'Auto'}]},
               'UplinkSet_9': {'name': 'prod', 'mode': 'Auto', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['prod_101', 'prod_102', 'prod_103', 'prod_104'], 'nativeNetworkUri': None, 'primaryPort': {'bay': '3', 'port': 'X7'},
                               'logicalPortConfigInfos': [{'bay': '1', 'port': 'X4', 'speed': 'Auto'}]},
               'UplinkSet_10': {'name': 'test', 'mode': 'Auto', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['test_109', 'test_110', 'test_111', 'test_112'], 'nativeNetworkUri': None, 'primaryPort': {'bay': '3', 'port': 'X7'},
                                'logicalPortConfigInfos': [{'bay': '2', 'port': 'X4', 'speed': 'Auto'}]}
               }

li_uplink_sets = {'US-1A': {'name': 'US-1A', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['net_101-A', 'net_101-B'], 'fcNetworkUris': [], 'fcoeNetworkUris': [], 'lacpTimer': 'Short',
                            'logicalInterconnectUri': None, 'primaryPortLocation': None, 'manualLoginRedistributionState': 'NotSupported', 'connectionMode': 'Auto', 'nativeNetworkUri': None,
                            'portConfigInfos': [{'bay': '1', 'port': 'X5', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                                {'bay': '2', 'port': 'X5', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  'US-2': {'name': 'US-2', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['net_101-A'], 'fcNetworkUris': [], 'fcoeNetworkUris': [], 'lacpTimer': 'Short',
                           'logicalInterconnectUri': None, 'primaryPortLocation': None, 'manualLoginRedistributionState': 'NotSupported', 'connectionMode': 'Auto', 'nativeNetworkUri': None,
                           'portConfigInfos': []},
                  'US-3': {'name': 'US-2', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['net_101-C', 'net_101-D'], 'fcNetworkUris': [], 'fcoeNetworkUris': [], 'lacpTimer': 'Short',
                           'logicalInterconnectUri': None, 'primaryPortLocation': None, 'manualLoginRedistributionState': 'NotSupported', 'connectionMode': 'Auto', 'nativeNetworkUri': None,
                           'portConfigInfos': []}}

ligs = {'lig1':
        {'name': 'LIG-1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC Flex-10/10D Module'},

                                     ],
         'uplinkSets': [{'networkType': 'Ethernet',
                         'ethernetNetworkType': 'Tagged',
                         'networkUris': ['net_101-A'],
                         'nativeNetworkUri': None,
                         'lacpTimer': 'Short',
                         'primaryPort': None,
                         'logicalPortConfigInfos':[{'bay': '1', 'port': 'X5', 'speed': 'Auto'},
                                                   {'bay': '2', 'port': 'X5', 'speed': 'Auto'}],
                         'mode': 'Auto',
                         'name': 'US-1A'}],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
        'lig102':
        {'name': 'LIG-2',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC Flex-10/10D Module'},
                                     ],
         'uplinkSets': [{'networkType': 'Ethernet',
                         'ethernetNetworkType': 'Tagged',
                         'networkUris': ['net_101-A', 'net_101-B'],
                         'nativeNetworkUri': None,
                         'lacpTimer': 'Short',
                         'primaryPort': None,
                         'logicalPortConfigInfos':[{'bay': '1', 'port': 'X5', 'speed': 'Auto'},
                                                   {'bay': '2', 'port': 'X5', 'speed': 'Auto'}],
                         'mode': 'Auto',
                         'name': 'US-2A'}],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
        'lig103':
        {'name': 'LIG-1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC Flex-10/10D Module'},
                                     ],
         'uplinkSets': [{'networkType': 'Ethernet',
                         'ethernetNetworkType': 'Tagged',
                         'networkUris': ['net_101-A', 'net_101-B', 'net_101-C', 'net_101-D'],
                         'nativeNetworkUri': None,
                         'lacpTimer': 'Short',
                         'primaryPort': None,
                         'logicalPortConfigInfos':[{'bay': '1', 'port': 'X5', 'speed': 'Auto'},
                                                   {'bay': '2', 'port': 'X5', 'speed': 'Auto'}],
                         'mode': 'Auto',
                         'name': 'US-1A'}],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
        'lige':
        {'name': 'LIG-2',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC Flex-10/10D Module'},
                                     ],
         'uplinkSets': [{'networkType': 'Ethernet',
                         'ethernetNetworkType': 'Tagged',
                         'networkUris': ['net_101-E'],
                         'nativeNetworkUri': None,
                         'lacpTimer': 'Short',
                         'primaryPort': None,
                         'logicalPortConfigInfos':[{'bay': '1', 'port': 'X8', 'speed': 'Auto'}],
                         'mode': 'Auto',
                         'name': 'US-A'}],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
        'lig105':
        {'name': 'LIG-1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC Flex-10/10D Module'},
                                     ],
         'uplinkSets': [{'networkType': 'Ethernet',
                         'ethernetNetworkType': 'Tagged',
                         'networkUris': ['net_101-A'],
                         'nativeNetworkUri': None,
                         'lacpTimer': 'Short',
                         'primaryPort': None,
                         'logicalPortConfigInfos':[{'bay': '1', 'port': 'X5', 'speed': 'Auto'}],
                         'mode': 'Auto',
                         'name': 'US-1A'},
                        {'networkType': 'Ethernet',
                         'ethernetNetworkType': 'Tagged',
                         'networkUris': ['net_101-B'],
                         'nativeNetworkUri': None,
                         'lacpTimer': 'Short',
                         'primaryPort': None,
                         'logicalPortConfigInfos':[{'bay': '2', 'port': 'X5', 'speed': 'Auto'}],
                         'mode': 'Auto',
                         'name': 'US-1B'}],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
        'lig_lacp':
        {'name': 'LIG-1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC Flex-10/10D Module'},
                                     ],
         'uplinkSets': [{'name': 'US-Agg-Lng', 'mode': 'Auto', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['net_101'], 'nativeNetworkUri': None, 'lacpTimer': 'Long', 'primaryPort': None,
                         'logicalPortConfigInfos':[{'bay': '1', 'port': 'X5', 'speed': 'Auto'}]},
                        {'name': 'US-Agg-Shrt', 'mode': 'Auto', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['net_102'], 'nativeNetworkUri': None, 'lacpTimer': 'Short', 'primaryPort': None,
                         'logicalPortConfigInfos':[{'bay': '2', 'port': 'X5', 'speed': 'Auto'}]},
                        {'name': 'US-Failover-1', 'mode': 'Failover', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['net_103'], 'nativeNetworkUri': None, 'primaryPort': {'bay': '3', 'port': 'X7'},
                         'logicalPortConfigInfos': [{'bay': '3', 'port': 'X7', 'speed': 'Auto'}]}],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
        'lig_edit':
        {'name': 'LIG-1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC Flex-10/10D Module'},
                                     ],
         'uplinkSets': [{'networkType': 'Ethernet',
                         'ethernetNetworkType': 'Tagged',
                         'networkUris': ['net_101'],
                         'nativeNetworkUri': None,
                         'lacpTimer': 'Long',
                         'primaryPort': None,
                         'logicalPortConfigInfos':[{'bay': '1', 'port': 'X5', 'speed': 'Auto'}],
                         'mode': 'Auto',
                         'name': 'US-Agg-Lng'},
                        {'networkType': 'Ethernet',
                         'ethernetNetworkType': 'Tagged',
                         'networkUris': ['net_102'],
                         'nativeNetworkUri': None,
                         'lacpTimer': 'Short',
                         'primaryPort': None,
                         'logicalPortConfigInfos':[{'bay': '2', 'port': 'X5', 'speed': 'Auto'}],
                         'mode': 'Auto',
                         'name': 'US-Agg-Shrt'},
                        {'networkType': 'Ethernet',
                         'ethernetNetworkType': 'Tagged',
                         'networkUris': ['net_103'],
                         'nativeNetworkUri': None,
                         'primaryPort': {'bay': '3', 'port': 'X7'},
                         'logicalPortConfigInfos': [{'bay': '3', 'port': 'X7', 'speed': 'Auto'}],
                         'mode': 'Failover',
                         'name': 'US-Failover-1'},
                        {'networkType': 'Ethernet',
                         'ethernetNetworkType': 'Tagged',
                         'networkUris': ['net_401'],
                         'nativeNetworkUri': None,
                         'lacpTimer': 'Short',
                         'primaryPort': None,
                         'logicalPortConfigInfos': [{'bay': '3', 'port': 'X3', 'speed': 'Auto'},
                                                    {'bay': '3', 'port': 'X5', 'speed': 'Auto'},
                                                    {'bay': '3', 'port': 'X6', 'speed': 'Auto'}],
                         'mode': 'Auto',
                         'name': 'US-Agg1'}],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
        'lig_lacp1':
        {'name': 'LIG-LACP',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'},
                                     ],
         'uplinkSets': [{'networkType': 'Ethernet',
                         'ethernetNetworkType': 'Tagged',
                         'networkUris': ['net_104'],
                         'nativeNetworkUri': None,
                         'primaryPort': None,
                         'logicalPortConfigInfos':[{'bay': '1', 'port': 'X5', 'speed': 'Auto'}],
                         'mode': 'Auto',
                         'name': 'US-Agg-Lng2'},
                        {'networkType': 'Ethernet',
                         'ethernetNetworkType': 'Tagged',
                         'networkUris': ['net_105'],
                         'nativeNetworkUri': None,
                         'primaryPort': {'bay': '3', 'port': 'X7'},
                         'logicalPortConfigInfos': [{'bay': '3', 'port': 'X7', 'speed': 'Auto'}],
                         'mode': 'Failover',
                         'name': 'US-Failover-2'}],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
        'lig_topo':
        {'name': 'LIG-1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     ],
         'uplinkSets': [uplink_sets['UplinkSet_3'].copy(), uplink_sets['UplinkSet_4'].copy(), uplink_sets['UplinkSet_5'].copy(), uplink_sets['UplinkSet_6'].copy(), uplink_sets['UplinkSet_7'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'internalNetworkUris': ['test_109', 'test_110', 'test_111', 'test_112'],
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
        'lig_topo1':
        {'name': 'LIG-1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     ],
         'uplinkSets': [uplink_sets['UplinkSet_5'].copy(), uplink_sets['UplinkSet_6'].copy(), uplink_sets['UplinkSet_7'].copy(), uplink_sets['UplinkSet_8'].copy(), uplink_sets['UplinkSet_9'].copy(), uplink_sets['UplinkSet_10'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'internalNetworkUris': [],
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         }
        }


eg_body1 = {'EG_1':
            {'name': 'EG-1',
             "ipRangeUris": [],
             "enclosureCount": 1,
             "osDeploymentSettings": None,
             "configurationScript": None,
             "powerMode": None,
             "ambientTemperatureMode": "Standard",
             'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-1'},
                                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG-1'},
                                         {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-1'},
                                         {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG-1'},
                                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG-1'},
                                         {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG-1'},
                                         {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                                         {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]},
            'EG_2':
            {'name': 'EG-1',
             "ipRangeUris": [],
             "enclosureCount": 1,
             "osDeploymentSettings": None,
             "configurationScript": None,
             "powerMode": None,
             "ambientTemperatureMode": "Standard",
             'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-1'},
                                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG-1'},
                                         {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-1'},
                                         {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG-1'},
                                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG-1'},
                                         {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG-1'},
                                         {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                                         {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}
            }


enc_body1 = {'hostname': ENCLOSURE_IP, 'username': enclosure_credentials['userName'], 'password': enclosure_credentials['password'], 'enclosureGroupUri': '', 'force': False, 'licensingIntent': 'OneViewNoiLO'}

valDict_1 = {'errorCode': 'CRM_DUPLICATE_NETWORK_NAME'}

valDict_2 = {'errorCode': 'CRM_DUPLICATE_VLAN_IDS_UPLINK_SET_GROUP',
             'message': 'Duplicate VLAN IDs are not allowed in the same uplink set.'}

valDict_3 = {'status_code': 400,
             'errorCode': 'CRM_DUPLICATE_VLAN_IDS_UPLINK_SET',
             'message': 'Duplicate VLAN IDs are not allowed in the same uplink set.'}

valDict_4 = {'status_code': 400,
             'errorCode': 'CRM_NETWORK_ALREADY_ASSIGNED',
             'message': 'Another uplink set is using one of the networks.'}

valDict_5 = {'status_code': 400,
             'errorCode': 'CRM_DUPLICATE_VLAN_IDS_NETWORK_SET',
             'message': 'Duplicate VLAN IDs are not allowed in the same network set.'}

valDict_user = {'status_code': 403,
                'errorCode': 'ACTION_FORBIDDEN_BY_ROLE',
                'message': 'The requested action is not authorized.'}

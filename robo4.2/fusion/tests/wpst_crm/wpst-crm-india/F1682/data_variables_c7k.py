def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
network_admin = {'userName': 'network', 'password': 'networkadmin'}
storage_admin = {'userName': 'storage', 'password': 'storageadmin'}
backup_admin = {'userName': 'backup', 'password': 'backupadmin'}
server_admin = {'userName': 'server', 'password': 'serveradmin'}
read_only = {'userName': 'readonly', 'password': 'readonly'}

# setup details 1:
tor_switch_ip = "192.168.144.118"
server_ip = "25.25.26.2"


users = [{'userName': 'server', 'password': 'serveradmin', 'fullName': 'Sarah', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'network', 'password': 'networkadmin', 'fullName': 'Nat', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'backup', 'password': 'backupadmin', 'fullName': 'Backup', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'readonly', 'password': 'readonly', 'fullName': 'Rheid', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'storage', 'password': 'storageadmin', 'fullName': 'Rheid', 'roles': ['Storage administrator'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]

ethernet_networks = [{'name': 'eth-10', 'type': 'ethernet-networkV300', 'vlanId': 10, 'purpose': 'General', 'smartLink': True,
                      'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'eth-11', 'type': 'ethernet-networkV300', 'vlanId': 11, 'purpose': 'General',
                      'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'eth-12', 'type': 'ethernet-networkV300', 'vlanId': 12, 'purpose': 'General', 'smartLink': True,
                      'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Untagged'},
                     {'name': 'eth-13', 'type': 'ethernet-networkV300', 'vlanId': 13, 'purpose': 'General',
                      'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tunnel'}]

fcoe_networks = [{'name': 'FCOE-100', 'type': 'fcoe-networkV300', 'vlanId': 100},
                 {'name': 'FCOE-101', 'type': 'fcoe-networkV300', 'vlanId': 101}]

fc_networks = [{'type': 'fc-networkV300', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'name': 'SAN-1-A', 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'type': 'fc-networkV300', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'name': 'SAN-2-A', 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}]


lig_c7k_f1682 = [{'name': 'LIG1',
                  'type': 'logical-interconnect-groupV300',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [
                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC FlexFabric-20/40 F8 Module'}
                  ],
                  'uplinkSets': [{'name': 'uplink1',
                                  'ethernetNetworkType': 'Tagged',
                                  'networkType': 'Ethernet',
                                  'networkUris': ['eth-10'],
                                  'nativeNetworkUri': None,
                                  'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'},
                                                             {'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'},
                                                             ]}
                                 ],
                  'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': None,
                  'snmpConfiguration': None}
                 ]

lig_c7k_f1682_1 = [{'name': 'LIG2',
                    'type': 'logical-interconnect-groupV300',
                    'enclosureType': 'C7000',
                    'interconnectMapTemplate': [
                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC FlexFabric-20/40 F8 Module'}
                    ],
                    'uplinkSets': [{'name': 'uplink1',
                                    'ethernetNetworkType': 'Tagged',
                                    'networkType': 'Ethernet',
                                    'networkUris': ['eth-10'],
                                    'nativeNetworkUri': None,
                                    'mode': 'Auto',
                                    'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'},
                                                               {'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'},
                                                               ]}
                                   ],
                    'stackingMode': 'Enclosure',
                    'ethernetSettings': None,
                    'state': 'Active',
                    'telemetryConfiguration': None,
                    'snmpConfiguration': None}
                   ]

uplinkSets_4912 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                    'nativeNetworkUri': None, 'mode': 'Auto',
                    'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q1.1', 'speed': 'Speed40G'}
                                               ]},
                   {'name': 'uplink2', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-11'],
                    'nativeNetworkUri': None, 'mode': 'Auto',
                    'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q1.2', 'speed': 'Auto'}
                                               ]}]


uplink_TC_68 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                         'nativeNetworkUri': 'eth-10', 'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q1.1', 'speed': 'Speed40G'}]}]

uplink_TC_69 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                         'nativeNetworkUri': 'eth-10', 'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'},
                                                    {'bay': '5', 'port': 'Q2.2', 'speed': 'Auto'},
                                                    {'bay': '5', 'port': 'Q2.3', 'speed': 'Auto'},
                                                    {'bay': '5', 'port': 'Q2.4', 'speed': 'Auto'}]}]

uplink_TC_69_2 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                   'nativeNetworkUri': 'eth-10', 'mode': 'Auto',
                   'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q4.1', 'speed': 'Auto'},
                                              {'bay': '5', 'port': 'Q4.2', 'speed': 'Auto'},
                                              {'bay': '5', 'port': 'Q4.3', 'speed': 'Auto'},
                                              {'bay': '5', 'port': 'Q4.4', 'speed': 'Auto'}]}]

uplink_TC_95 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                         'nativeNetworkUri': 'eth-10', 'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'},
                                                    {'bay': '5', 'port': 'X1', 'speed': 'Auto'}, ]}]


LIF_pingQ1 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
               'nativeNetworkUri': 'eth-10', 'mode': 'Auto',
               'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'}]}]


LIF_pingQ1_1 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                         'nativeNetworkUri': 'eth-10', 'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q1.1', 'speed': 'Speed40G'}]}]

LIF_pingQ2 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
               'nativeNetworkUri': 'eth-10', 'mode': 'Auto',
               'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'}]}]


LIF_pingQ2_1 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                         'nativeNetworkUri': 'eth-10', 'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q2.1', 'speed': 'Speed40G'}]}]


LIF_pingQ3 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
               'nativeNetworkUri': 'eth-10', 'mode': 'Auto',
               'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q3.1', 'speed': 'Auto'}]}]


LIF_pingQ3_1 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                         'nativeNetworkUri': 'eth-10', 'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q3.1', 'speed': 'Speed40G'}]}]


LIF_pingQ4 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
               'nativeNetworkUri': 'eth-10', 'mode': 'Auto',
               'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q4.1', 'speed': 'Auto'}]}]

LIF_pingQ4_1 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                         'nativeNetworkUri': 'eth-10', 'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q4.1', 'speed': 'Speed40G'}]}]

LIF_pingQ61 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                'nativeNetworkUri': 'eth-10', 'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'}]}]

LIF_pingQ61_1 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                  'nativeNetworkUri': 'eth-10', 'mode': 'Auto',
                  'logicalPortConfigInfos': [{'bay': '6', 'port': 'Q1.1', 'speed': 'Speed40G'}]}]


uplinkSets_6_compliance = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                            'nativeNetworkUri': None, 'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q1.1', 'speed': 'Speed40G'},
                                                       {'bay': '5', 'port': 'Q2.1', 'speed': 'Speed40G'},

                                                       ]}]

uplinkSets_6_precompliance = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                               'nativeNetworkUri': None, 'mode': 'Auto',
                               'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'},
                                                          {'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'},

                                                          ]}]
interconn_1 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                'nativeNetworkUri': 'eth-10', 'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'},
                                           {'bay': '5', 'port': 'Q1.2', 'speed': 'Auto'},
                                           {'bay': '5', 'port': 'Q4.1', 'speed': 'Auto'},
                                           ]},
               {'name': 'uplink2', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-11'],
                'nativeNetworkUri': 'eth-11', 'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q2.1', 'speed': 'Speed40G'},
                                           {'bay': '5', 'port': 'Q3.1', 'speed': 'Speed40G'},
                                           ]}]

uplinkSets_48 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                  'nativeNetworkUri': 'eth-10', 'mode': 'Auto',
                  'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q1.1', 'speed': 'Speed40G'},
                                             {'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'},
                                             {'bay': '5', 'port': 'Q2.2', 'speed': 'Auto'}]}]


uplinkSets_481 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                   'nativeNetworkUri': 'eth-10', 'mode': 'Auto',
                   'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q1.1', 'speed': '10G'},
                                              {'bay': '5', 'port': 'Q2.1', 'speed': '2G'},
                                              {'bay': '5', 'port': 'Q2.2', 'speed': '8G'}]}]


uplinkSets_FUnc1 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                     'nativeNetworkUri': 'eth-10', 'mode': 'Auto',
                     'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'},
                                                {'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'},
                                                {'bay': '5', 'port': 'Q3.1', 'speed': 'Auto'},
                                                {'bay': '5', 'port': 'Q4.1', 'speed': 'Auto'},
                                                ]}]

uplinkSets_FUnc2 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                     'nativeNetworkUri': 'eth-10', 'mode': 'Auto',
                     'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q1.1', 'speed': 'Speed40G'},
                                                {'bay': '5', 'port': 'Q2.1', 'speed': 'Speed40G'},
                                                {'bay': '5', 'port': 'Q3.1', 'speed': 'Speed40G'},
                                                {'bay': '5', 'port': 'Q4.1', 'speed': 'Speed40G'},
                                                ]}]


Uplinkset42_1 = [{"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tagged",
                  "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                  "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                  "modified": None, "name": "uplink2", "nativeNetworkUri": "eth-11",
                  "networkType": "Ethernet", "networkUris": ["eth-11"],
                  "portConfigInfos": [{"desiredSpeed": "Auto", "location": {
                      "locationEntries": [{"type": "Port", "value": "Q1.2"}, {"type": "Bay", "value": 5},
                                          {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
                  "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None}]

Uplinkset44 = [{"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tagged",
                "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                "modified": None, "name": "uplink1", "nativeNetworkUri": "eth-10",
                "networkType": "Ethernet", "networkUris": ["eth-10"],
                "portConfigInfos": [{"desiredSpeed": "Speed40G", "location": {
                    "locationEntries": [{"type": "Port", "value": "Q1.1"}, {"type": "Bay", "value": 5},
                                        {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
                "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None}
               ]

Uplinkset44_p2 = [
    {"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tagged",
     "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
     "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
     "modified": None, "name": "uplink2", "nativeNetworkUri": "eth-11",
     "networkType": "Ethernet", "networkUris": ["eth-11"],
     "portConfigInfos": [{"desiredSpeed": "Speed40G", "location": {
         "locationEntries": [{"type": "Port", "value": "Q2.1"}, {"type": "Bay", "value": 5},
                             {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
     "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None}
]


Uplinkset_LI_compliance = [{"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tagged",
                            "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                            "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                            "modified": None, "name": "uplink1", "nativeNetworkUri": "eth-10",
                            "networkType": "Ethernet", "networkUris": ["eth-10"],
                            "portConfigInfos": [{"desiredSpeed": "Speed40G", "location": {
                                "locationEntries": [{"type": "Port", "value": "Q1.1"}, {"type": "Bay", "value": 5},
                                                    {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}},
                                                {"desiredSpeed": "Auto", "location": {
                                                    "locationEntries": [{"type": "Port", "value": "Q2.1"}, {"type": "Bay", "value": 5},
                                                                        {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}},

                                                ],
                            "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None}]


uplinkSets_781 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                   'nativeNetworkUri': None, 'mode': 'Auto',
                   'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'},
                                              {'bay': '5', 'port': 'Q2.2', 'speed': 'Auto'},
                                              {'bay': '5', 'port': 'Q2.3', 'speed': 'Auto'},
                                              {'bay': '5', 'port': 'Q2.4', 'speed': 'Auto'},
                                              {'bay': '5', 'port': 'Q1.1', 'speed': 'Speed40G'}]}]


uplinkSets_691 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                   'nativeNetworkUri': None, 'mode': 'Auto',
                   'logicalPortConfigInfos': [{'bay': '5', 'port': 'X1', 'speed': 'Auto'}]}]

uplinkSets_692 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                   'nativeNetworkUri': None, 'mode': 'Auto',
                   'logicalPortConfigInfos': [
    {'bay': '5', 'port': 'X1', 'speed': 'Auto'},
    {'bay': '5', 'port': 'Q1.1', 'speed': 'Speed40G'}]}]


uplinkSets_39 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                  'nativeNetworkUri': None, 'mode': 'Auto',
                  'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q1.1', 'speed': 'Speed40G'},
                                             {'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'}]}]


Uplinkset40 = [{"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tagged",
                "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                "modified": None, "name": "uplink1", "nativeNetworkUri": None,
                "networkType": "Ethernet", "networkUris": ["eth-10"],
                "portConfigInfos": [{"desiredSpeed": "Auto", "location": {
                    "locationEntries": [{"type": "Port", "value": "Q1.1"}, {"type": "Bay", "value": 5},
                                        {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
                "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None}]

Uplinkset41 = [{"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tagged",
                "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                "modified": None, "name": "uplink2", "nativeNetworkUri": None,
                "networkType": "Ethernet", "networkUris": ["eth-10"],
                "portConfigInfos": [{"desiredSpeed": "Speed40G", "location": {
                    "locationEntries": [{"type": "Port", "value": "Q1.1"}, {"type": "Bay", "value": 5},
                                        {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}},
                                    {"desiredSpeed": "Auto", "location": {
                                        "locationEntries": [{"type": "Port", "value": "Q2.1"}, {"type": "Bay", "value": 5},
                                                            {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}},
                                    {"desiredSpeed": "Speed40G", "location": {
                                        "locationEntries": [{"type": "Port", "value": "Q2.2"}, {"type": "Bay", "value": 5},
                                                            {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}
                                    ],
                "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None}]

Uplinkset41_1 = [{"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tagged",
                  "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                  "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                  "modified": None, "name": "uplink2", "nativeNetworkUri": None,
                  "networkType": "Ethernet", "networkUris": ["eth-10"],
                  "portConfigInfos": [{"desiredSpeed": "Speed40G", "location": {
                      "locationEntries": [{"type": "Port", "value": "Q1.1"}, {"type": "Bay", "value": 5},
                                          {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}},
                                      {"desiredSpeed": "Speed40G", "location": {
                                          "locationEntries": [{"type": "Port", "value": "Q2.1"}, {"type": "Bay", "value": 5},
                                                              {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}},
                                      {"desiredSpeed": "Auto", "location": {
                                          "locationEntries": [{"type": "Port", "value": "Q2.2"}, {"type": "Bay", "value": 5},
                                                              {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}
                                      ],
                  "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None}]

Uplinkset42 = [{"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tagged",
                "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                "modified": None, "name": "uplink1", "nativeNetworkUri": None,
                "networkType": "Ethernet", "networkUris": ["eth-10"],
                "portConfigInfos": [{"desiredSpeed": "Speed40G", "location": {
                    "locationEntries": [{"type": "Port", "value": "Q1.1"}, {"type": "Bay", "value": 5},
                                        {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
                "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None},

               {"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tagged",
                "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                "modified": None, "name": "uplink2", "nativeNetworkUri": None,
                "networkType": "Ethernet", "networkUris": ["eth-11"],
                "portConfigInfos": [{"desiredSpeed": "Speed40G", "location": {
                    "locationEntries": [{"type": "Port", "value": "Q2.1"}, {"type": "Bay", "value": 5},
                                        {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
                "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None},

               {"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Untagged",
                "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                "modified": None, "name": "uplink3", "nativeNetworkUri": None,
                "networkType": "Ethernet", "networkUris": ["eth-12"],
                "portConfigInfos": [{"desiredSpeed": "Speed40G", "location": {
                    "locationEntries": [{"type": "Port", "value": "Q3.1"}, {"type": "Bay", "value": 5},
                                        {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
                "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None},

               {"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tunnel",
                "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                "modified": None, "name": "uplink4", "nativeNetworkUri": None,
                "networkType": "Ethernet", "networkUris": ["eth-13"],
                "portConfigInfos": [{"desiredSpeed": "Speed40G", "location": {
                    "locationEntries": [{"type": "Port", "value": "Q4.1"}, {"type": "Bay", "value": 5},
                                        {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
                "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None}]


Uplinkset_func = [{"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tagged",
                   "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                   "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                   "modified": None, "name": "uplink1", "nativeNetworkUri": None,
                   "networkType": "Ethernet", "networkUris": ["eth-10"],
                   "portConfigInfos": [{"desiredSpeed": "Auto", "location": {
                       "locationEntries": [{"type": "Port", "value": "Q1.1"}, {"type": "Bay", "value": 5},
                                           {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
                   "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None},

                  {"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tagged",
                   "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                   "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                   "modified": None, "name": "uplink2", "nativeNetworkUri": None,
                   "networkType": "Ethernet", "networkUris": ["eth-11"],
                   "portConfigInfos": [{"desiredSpeed": "Speed40G", "location": {
                       "locationEntries": [{"type": "Port", "value": "Q2.1"}, {"type": "Bay", "value": 5},
                                           {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
                   "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None},

                  {"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Untagged",
                   "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                   "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                   "modified": None, "name": "uplink3", "nativeNetworkUri": None,
                   "networkType": "Ethernet", "networkUris": ["eth-12"],
                   "portConfigInfos": [{"desiredSpeed": "Speed40G", "location": {
                       "locationEntries": [{"type": "Port", "value": "Q3.1"}, {"type": "Bay", "value": 5},
                                           {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
                   "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None},

                  {"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tunnel",
                   "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                   "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                   "modified": None, "name": "uplink4", "nativeNetworkUri": None,
                   "networkType": "Ethernet", "networkUris": ["eth-13"],
                   "portConfigInfos": [{"desiredSpeed": "Speed40G", "location": {
                       "locationEntries": [{"type": "Port", "value": "Q4.1"}, {"type": "Bay", "value": 5},
                                           {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
                   "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None}]


uplink_null = []

Uplinkset42_2 = [{"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tagged",
                  "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                  "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                  "modified": None, "name": "uplink1", "nativeNetworkUri": None,
                  "networkType": "Ethernet", "networkUris": ["eth-10"],
                  "portConfigInfos": [{"desiredSpeed": "Auto", "location": {
                      "locationEntries": [{"type": "Port", "value": "Q1.1"}, {"type": "Bay", "value": 5},
                                          {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
                  "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None},

                 {"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tunnel",
                  "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                  "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                  "modified": None, "name": "uplink4", "nativeNetworkUri": None,
                  "networkType": "Ethernet", "networkUris": ["eth-13"],
                  "portConfigInfos": [{"desiredSpeed": "Auto", "location": {
                      "locationEntries": [{"type": "Port", "value": "Q4.1"}, {"type": "Bay", "value": 5},
                                          {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
                  "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None}]

Uplinkset43 = [{"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tagged",
                "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                "modified": None, "name": "uplink1", "nativeNetworkUri": None,
                "networkType": "Ethernet", "networkUris": ["eth-10"],
                "portConfigInfos": [{"desiredSpeed": "Auto", "location": {
                    "locationEntries": [{"type": "Port", "value": "Q1.1"}, {"type": "Bay", "value": 5},
                                        {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}, {"desiredSpeed": "Auto", "location": {
                                            "locationEntries": [{"type": "Port", "value": "Q1.4"}, {"type": "Bay", "value": 5},
                                                                {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}, {"desiredSpeed": "Auto", "location": {
                                                                    "locationEntries": [{"type": "Port", "value": "Q2.1"}, {"type": "Bay", "value": 5},
                                                                                        {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}, {"desiredSpeed": "Auto", "location": {
                                                                                            "locationEntries": [{"type": "Port", "value": "Q2.4"}, {"type": "Bay", "value": 5},
                                                                                                                {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}},
                                    {"desiredSpeed": "Auto", "location": {
                                        "locationEntries": [{"type": "Port", "value": "Q3.1"}, {"type": "Bay", "value": 5},
                                                            {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}, {"desiredSpeed": "Auto", "location": {
                                                                "locationEntries": [{"type": "Port", "value": "Q3.2"}, {"type": "Bay", "value": 5},
                                                                                    {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}},
                                    {"desiredSpeed": "Auto", "location": {
                                        "locationEntries": [{"type": "Port", "value": "X1"}, {"type": "Bay", "value": 5},
                                                            {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
                "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None},

               {"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tunnel",
                "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                "modified": None, "name": "uplink4", "nativeNetworkUri": None,
                "networkType": "Ethernet", "networkUris": ["eth-13"],
                "portConfigInfos": [{"desiredSpeed": "Auto", "location": {
                    "locationEntries": [{"type": "Port", "value": "Q4.1"}, {"type": "Bay", "value": 5},
                                        {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}},
                                    {"desiredSpeed": "Auto", "location": {
                                        "locationEntries": [{"type": "Port", "value": "Q4.4"}, {"type": "Bay", "value": 5},
                                                            {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}, {"desiredSpeed": "Auto", "location": {
                                                                "locationEntries": [{"type": "Port", "value": "Q3.4"}, {"type": "Bay", "value": 5},
                                                                                    {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}},
                                    {"desiredSpeed": "Auto", "location": {
                                        "locationEntries": [{"type": "Port", "value": "X3"}, {"type": "Bay", "value": 5},
                                                            {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}},
                                    {"desiredSpeed": "Auto", "location": {
                                        "locationEntries": [{"type": "Port", "value": "X2"}, {"type": "Bay", "value": 5},
                                                            {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}

                                    ],
                "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None}]


li_FW_46 = {"sppUri": "/rest/firmware-drivers/cust-upgrade-rpm-4-6-c7k-22-11-2016latest", "command": "UPDATE", "force": True, "ethernetActivationType": "Parallel", "ethernetActivationDelay": "0", "fcActivationType": "Parallel", "fcActivationDelay": "0", "validationType": "None"}


li_fW_44 = {"sppUri": "/rest/firmware-drivers/bp-C7K-VC440-2015-11-05-01", "command": "UPDATE", "force": True, "ethernetActivationType": "Parallel",
            "ethernetActivationDelay": "0", "fcActivationType": "Parallel", "fcActivationDelay": "0", "validationType": "None"}


uplinkSets_49 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                  'nativeNetworkUri': None, 'mode': 'Auto',
                  'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'},
                                             {'bay': '5', 'port': 'Q2.1', 'speed': 'Speed40G'},
                                             {'bay': '5', 'port': 'Q2.2', 'speed': 'Auto'}
                                             ]}]

uplinkSets_50 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                  'nativeNetworkUri': None, 'mode': 'Auto',
                  'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q1.1', 'speed': 'Speed40G'},
                                             {'bay': '5', 'port': 'Q2.1', 'speed': 'Speed40G'},
                                             {'bay': '5', 'port': 'Q4.1', 'speed': 'Speed40G'}
                                             ]}]

uplinkSets_50_1 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                    'nativeNetworkUri': None, 'mode': 'Auto',
                    'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q1.1', 'speed': 'Speed40G'},
                                               {'bay': '5', 'port': 'Q2.2', 'speed': 'Speed40G'},
                                               {'bay': '5', 'port': 'Q4.1', 'speed': 'Speed40G'}
                                               ]}]

uplinkSets_51 = [{'name': 'uplink1', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth-10'],
                  'nativeNetworkUri': None, 'mode': 'Auto',
                  'logicalPortConfigInfos': [{'bay': '5', 'port': 'Q1.1', 'speed': 'Speed40G'},
                                             {'bay': '5', 'port': 'Q2.2', 'speed': 'Speed41G'},
                                             {'bay': '5', 'port': 'Q4.1', 'speed': 'Speed40G'}
                                             ]}]

Uplinkset16 = [{"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tagged",
                "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                "modified": None, "name": "uplink1", "nativeNetworkUri": None,
                "networkType": "Ethernet", "networkUris": ["eth-10"],
                "portConfigInfos": [{"desiredSpeed": "Auto", "location": {
                    "locationEntries": [{"type": "Port", "value": "Q1.1"}, {"type": "Bay", "value": 5},
                                        {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
                "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None},

               {"category": None, "connectionMode": "Speed40G", "description": None, "ethernetNetworkType": "Tagged",
                "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                "modified": None, "name": "uplink2", "nativeNetworkUri": None,
                "networkType": "Ethernet", "networkUris": ["eth-11"],
                "portConfigInfos": [{"desiredSpeed": "Speed40G", "location": {
                    "locationEntries": [{"type": "Port", "value": "Q2.1"}, {"type": "Bay", "value": 5},
                                        {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
                "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None}]

Uplinkset16_1 = [{"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tagged",
                  "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
                  "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
                  "modified": None, "name": "uplink1", "nativeNetworkUri": None,
                  "networkType": "Ethernet", "networkUris": ["eth-10"],
                  "portConfigInfos": [{"desiredSpeed": "Speed40G", "location": {
                      "locationEntries": [{"type": "Port", "value": "Q1.1"}, {"type": "Bay", "value": 5},
                                          {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}, {"desiredSpeed": "Speed40G", "location": {
                                              "locationEntries": [{"type": "Port", "value": "Q3.1"}, {"type": "Bay", "value": 5},
                                                                  {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
                  "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None}]

Uplinkset16_2 = [


    {"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Untagged",
     "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
     "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
     "modified": None, "name": "uplink3", "nativeNetworkUri": None,
     "networkType": "Ethernet", "networkUris": ["eth-12"],
     "portConfigInfos": [{"desiredSpeed": "Auto", "location": {
         "locationEntries": [{"type": "Port", "value": "Q4.1"}, {"type": "Bay", "value": 5},
                             {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
     "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None},

    {"category": None, "connectionMode": "Auto", "description": None, "ethernetNetworkType": "Tunnel",
     "fcNetworkUris": [], "fcoeNetworkUris": [], "lacpTimer": "Short",
     "logicalInterconnectUri": "SGH439WJKT-LIG1", "manualLoginRedistributionState": "NotSupported",
     "modified": None, "name": "uplink4", "nativeNetworkUri": None,
     "networkType": "Ethernet", "networkUris": ["eth-13"],
     "portConfigInfos": [{"desiredSpeed": "Auto", "location": {
         "locationEntries": [{"type": "Port", "value": "Q4.2"}, {"type": "Bay", "value": 5},
                             {"type": "Enclosure", "value": "/rest/enclosures/09SGH439WJKT"}]}}],
     "primaryPortLocation": None, "reachability": None, "type": "uplink-setV300", "uri": None}]


# this is the data for the c7k UI scenarios

li_intents_20_val = [["SGH439WJKT, interconnect 5, Q1.1", "Auto", "10 Gb/s", "Enabled", "Linked"], ["SGH439WJKT, interconnect 5, Q2.2", "Auto", "0 Gb/s", "Unlinked", "n/a"],
                     ["SGH439WJKT, interconnect 5, Q4.1", "Auto", "40 Gb/s", "Disabled"], ["SGH439WJKT, interconnect 5, Q4.2", "Auto", "0 Gb/s", "n/a"]]

li_intents_21_val = [["SGH439WJKT, interconnect 5, Q1.1", "40 Gb/s", "10 Gb/s", "Disabled", "Linked"], ["SGH439WJKT, interconnect 5, Q2.2", "Auto", "0 Gb/s", "n/a", "Unlinked"],
                     ["SGH439WJKT, interconnect 5, Q2.1", "Auto", "0 Gb/s", "Enabled", "Unlinked"], ["SGH439WJKT, interconnect 5, Q3.1", "Auto", "40 Gb/s", "Enabled", "Linked"]]


#####


li_1enc = {'name': 'LE_1Enc-LIG-bay3-1enc'}

enc_groups = [{'name': 'EG1',
               'type': 'EnclosureGroupV400',
               'enclosureTypeUri': '/rest/enclosure-types/c7000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 8,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}]

enc_groups_ui = [{'name': 'EG1',
                  'type': 'EnclosureGroupV400',
                  'enclosureTypeUri': '/rest/enclosure-types/c7000',
                  'stackingMode': 'Enclosure',
                  'interconnectBayMappingCount': 8,
                  'configurationScript': None,
                  'interconnectBayMappings':
                  [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                   {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                   {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                   {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                   {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG_UI_f1682'},
                   {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG_UI_f1682'},
                   {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                   {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}]

server_profiles = [
    {'type': 'ServerProfileV7', 'serverHardwareUri': 'SGH439WJKT, bay 1',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:SGH439WJKT', 'enclosureGroupUri': 'EG:EG1',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': 'Profile5', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'connections': [{'id': 1, 'name': 'conn1', 'functionType': 'Ethernet', 'portId': 'Auto',
                      'requestedMbps': '2500', 'networkUri': 'ETH:eth-10',
                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]}]

ENC1 = 'SGH439WJKT'

encs = [{'hostname': '192.168.144.135', 'username': 'Administrator', 'password': 'Admin', 'enclosureGroupUri': 'EG:EG1', 'force': True, 'licensingIntent': 'OneViewNoiLO'}]


ICM_powercycle = [{'op': 'replace', 'path': '/deviceResetState', 'value': 'Reset'}]


split_unsplit_msg = 'An uplink set may not contain both split and un-split uplink ports.'
LI = 'SGH439WJKT-LIG1'
split_recomaction = 'Specify only split or only un-split ports in an uplink set.'
message1 = 'The uplink set cannot contain both 40 Gb/s ports and ports that require the use of a splitter cable.'
recomact1 = 'Remove port(s) Q2.2, or change the speed for port(s) Q2.1 to Auto.'
msg2 = 'For uplink set uplink1 : Speed configuration 40 Gb/s for the port SGH439WJKT, interconnect 5 :Q1.1 conflicts with the plugged-in transceiver in splitter mode.'
resol2 = 'Change the speed configuration to match the existing transceiver. Alternatively, if this is the intended configuration, replace the transceiver to match the intended configuration.'
msg3 = 'For uplink set uplink1 : Speed configuration 40 Gb/s for the port SGH439WJKT, interconnect 5 :Q1.1 conflicts with the plugged-in transceiver in splitter mode.'
ic = 'SGH439WJKT, interconnect 5'
msg69 = 'For uplink set uplink1, uplink ports SGH439WJKT, interconnect 5 :Q2.2, Q2.4, Q2.3, Q2.1 are non operational.'
msg69AOC = 'For uplink set Uplink1, uplink ports SGH439WJKT, interconnect 5 :Q4.3, Q4.4, Q4.2 are non operational.'
msg95 = 'Q2.1 are non operational'
msg50_1 = 'Port speed of 40 Gb/s is invalid for uplink port Q2.2'
recom50_1 = 'Select Auto speed for this uplink port and retry the operation.'

icm5 = 'SGH439WJKT, interconnect 5'
icm6 = 'SGH439WJKT, interconnect 6'
msg_7811 = 'For uplink set uplink1 : Speed configuration 40 Gb/s for the port SGH439WJKT, interconnect 5 :Q1.1 conflicts with the plugged-in transceiver in splitter mode.'
msg_7812 = 'For uplink set uplink1, uplink ports SGH439WJKT, interconnect 5 :Q2.1 are non operational.'
ICM_powercycle = [{'op': 'replace', 'path': '/deviceResetState', 'value': 'Reset'}]


ui5_msg = "The uplink set cannot contain both 40 Gb/s ports and ports that require the use of a splitter cable."
ui8_msg = "Port(s) Q1.2 are used by other uplink sets as Auto ports and conflict with port selections in uplink set Uplink1."
ui8_resol = "Resolution Remove port(s) Q1.1, set the speed to Auto or change the configuration of the ports causing the conflict."
ui8_1msg = "Port(s) Q1.1 are used by other uplink sets as 40 Gb/s ports and conflict with port selections in uplink set Uplink2."
ui8_2msg = "Resolution Remove port(s) Q1.2 from the Uplink2 uplink set to proceed."
ui10_msg = "Port(s) Q3.1 are used by other uplink sets as 40 Gb/s ports and conflict with port selections in uplink set Uplink1."
ui10_resol = "Remove port(s) Q3.2 from the Uplink1 uplink set to proceed."
li_name = "LE_1Enc_HA-LIG-bay3-1enc"
li_name_A = "LE_1Enc_HA-LIG-bay3-1enc_A"
li_name_B = "LE_1Enc_HA-LIG-bay3-1enc_B"

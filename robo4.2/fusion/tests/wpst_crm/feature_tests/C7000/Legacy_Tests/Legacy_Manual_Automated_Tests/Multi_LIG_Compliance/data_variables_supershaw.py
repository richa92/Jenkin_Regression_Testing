def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


def convert_unicode_to_string(String):
    res = String.encode("utf-8")
    return res


APPLIANCE_IP = '15.186.14.17'

ENCLOSURE_IP = '15.186.2.227'

ENCLOSURE_NAME = 'aus-c7000-188'

servers = ['5']
lig_length = '2'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

oa_details = {"oa_ip": ENCLOSURE_IP, "username": "Administrator", "password": "Compaq123"}
Preview_uri = '/rest/enclosure-preview'

Preview_body = {"hostname": ENCLOSURE_IP, "username": oa_details['username'], "password": oa_details['password'], "ligPrefix": "LIG1", "force": True, "logicalInterconnectGroupNeeded": True}

users = [{'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True, 'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}]},
         {'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True, 'permissions': [{'roleName': 'Server administrator', 'scopeUri': None}]}
         ]

serveradmin_credentials = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

networkadmin_credentials = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

# uplink_len=2
edit_up_data = ['ss-comp-ug2']
edit_up2_data = ['ss-comp-ug1']
add_up_data = ['ss-comp-ug2', 'ss-comp-add']

alert1 = 'The logical interconnect is inconsistent with the logical interconnect group LIG-COMP-SS1.'
alert2 = 'The logical interconnect is inconsistent with the logical interconnect group LIG-COMP-SS2.'
interconnects = ['1', '2', '3', '4']
bays = ['1', '2', '3', '4']
ethernet_networks = [
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "wpstnetwork1",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 10
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "wpstnetwork2",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 20
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "wpstnetwork2",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 20
    }, {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "wpstnetwork3",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 30
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "wpstnetwork4",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 40
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "wpstnetwork5",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 50
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "wpstnetwork6",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 60
    }
]
Fc_body = {"name": "", "connectionTemplateUri": None, "linkStabilityTime": "30", "autoLoginRedistribution": True, "fabricType": "", "type": "fc-networkV4"}

LIG = [{'name': 'LIG-COMP-SS1',
        'type': 'logical-interconnect-groupV6',
        'enclosureType': 'C7000',
        'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'}

                                    ],
        'uplinkSets': [{'name': 'ss-comp-ug1',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['wpstnetwork1'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'lacpTimer': 'Short',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X2', 'speed': 'Auto'},

                                                    ]

                        }],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None},
       {'name': 'LIG-COMP-SS2',
        'type': 'logical-interconnect-groupV6',
        'enclosureType': 'C7000',
        'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'},
                                    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'}

                                    ],
        'uplinkSets': [{'name': 'ss-comp-ug2',
                        'ethernetNetworkType': 'Tagged',
                        'networkType': 'Ethernet',
                        'networkUris': ['wpstnetwork2'],
                        'nativeNetworkUri': None,
                        'mode': 'Auto',
                        'lacpTimer': 'Short',
                        'logicalPortConfigInfos': [{'bay': '3', 'port': 'X1', 'speed': 'Auto'}
                                                   ]

                        }],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None}]

telemetryConfiguration_edit = {'type': 'telemetry-configuration', 'sampleCount': 15, 'sampleInterval': 300, 'enableTelemetry': True}
ethernetSettings_edit = {'type': 'EthernetInterconnectSettingsV5', 'Fast MAC cache failover': False, 'MAC refresh interval': 20, 'IGMP snooping': True, 'IGMP idle timeout interval': 300, 'Loop protection': False}
lig_adduplink = {'name': 'LIG-COMP-SS2',
                 'type': 'logical-interconnect-groupV6',
                 'enclosureType': 'C7000',
                 'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'}

                                             ],
                 'uplinkSets': [{'name': 'ss-comp-ug2',
                                 'ethernetNetworkType': 'Tagged',
                                 'networkType': 'Ethernet',
                                 'networkUris': ['wpstnetwork2'],
                                 'nativeNetworkUri': None,
                                 'mode': 'Auto',
                                 'lacpTimer': 'Short',
                                 'logicalPortConfigInfos': [{'bay': '3', 'port': 'X1', 'speed': 'Auto'}
                                                            ]

                                 },
                                {'name': 'ss-comp-add',
                                 'ethernetNetworkType': 'Tagged',
                                 'networkType': 'Ethernet',
                                 'networkUris': ['wpstnetwork4'],
                                 'nativeNetworkUri': None,
                                 'mode': 'Auto',
                                 'lacpTimer': 'Short',
                                 'logicalPortConfigInfos': [{'bay': '4', 'port': 'X1', 'speed': 'Auto'}
                                                            ]

                                 }],
                 'stackingMode': 'Enclosure',
                 'ethernetSettings': None,
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': None}
lig_deleteuplink = {'name': 'LIG-COMP-SS1',
                    'type': 'logical-interconnect-groupV6',
                    'enclosureType': 'C7000',
                    'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'}

                                                ],
                    'uplinkSets': [],
                    'stackingMode': 'Enclosure',
                    'ethernetSettings': None,
                    'state': 'Active',
                    'telemetryConfiguration': None,
                    'snmpConfiguration': None}

lig_edit_interconnect = [{'name': 'LIG-COMP-SS1',
                          'type': 'logical-interconnect-groupV6',
                          'enclosureType': 'C7000',
                          'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
                                                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'}

                                                      ],
                          'uplinkSets': [{'name': 'ss-comp-ug1',
                                          'ethernetNetworkType': 'Tagged',
                                          'networkType': 'Ethernet',
                                          'networkUris': ['wpstnetwork1'],
                                          'nativeNetworkUri': None,
                                          'mode': 'Auto',
                                          'lacpTimer': 'Short',
                                          'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},

                                                                     ]

                                          }],
                          'stackingMode': 'Enclosure',
                          'ethernetSettings': None,
                          'state': 'Active',
                          'telemetryConfiguration': None,
                          'snmpConfiguration': None},
                         {'name': 'LIG-COMP-SS2',
                          'type': 'logical-interconnect-groupV6',
                          'enclosureType': 'C7000',
                          'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC FlexFabric-20/40 F8 Module'}

                                                      ],
                          'uplinkSets': [{'name': 'ss-comp-ug2',
                                          'ethernetNetworkType': 'Tagged',
                                          'networkType': 'Ethernet',
                                          'networkUris': ['wpstnetwork2'],
                                          'nativeNetworkUri': None,
                                          'mode': 'Auto',
                                          'lacpTimer': 'Short',
                                          'logicalPortConfigInfos': [{'bay': '3', 'port': 'X2', 'speed': 'Auto'}
                                                                     ]

                                          }],
                          'stackingMode': 'Enclosure',
                          'ethernetSettings': None,
                          'state': 'Active',
                          'telemetryConfiguration': None,
                          'snmpConfiguration': None}]

lig_remove_interconnect = [{'name': 'LIG-COMP-SS1',
                            'type': 'logical-interconnect-groupV6',
                            'enclosureType': 'C7000',
                            'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'}
                                                        # {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'}

                                                        ],
                            'uplinkSets': [{'name': 'ss-comp-ug1',
                                            'ethernetNetworkType': 'Tagged',
                                            'networkType': 'Ethernet',
                                            'networkUris': ['wpstnetwork1'],
                                            'nativeNetworkUri': None,
                                            'mode': 'Auto',
                                            'lacpTimer': 'Short',
                                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},

                                                                       ]

                                            }],
                            'stackingMode': 'Enclosure',
                            'ethernetSettings': None,
                            'state': 'Active',
                            'telemetryConfiguration': None,
                            'snmpConfiguration': None},
                           {'name': 'LIG-COMP-SS2',
                            'type': 'logical-interconnect-groupV5',
                            'enclosureType': 'C7000',
                            'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                                        # {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'}

                                                        ],
                            'uplinkSets': [{'name': 'ss-comp-ug2',
                                            'ethernetNetworkType': 'Tagged',
                                            'networkType': 'Ethernet',
                                            'networkUris': ['wpstnetwork2'],
                                            'nativeNetworkUri': None,
                                            'mode': 'Auto',
                                            'lacpTimer': 'Short',
                                            'logicalPortConfigInfos': [{'bay': '3', 'port': 'X2', 'speed': 'Auto'}
                                                                       ]

                                            }],
                            'stackingMode': 'Enclosure',
                            'ethernetSettings': None,
                            'state': 'Active',
                            'telemetryConfiguration': None,
                            'snmpConfiguration': None}]

eg_body = {'name': 'config4-group',
           'ipRangeUris': [],
           'enclosureCount': 1,
           'osDeploymentSettings': None,
           'configurationScript': '',
           'powerMode': None,
           'ambientTemperatureMode': 'Standard',
           'interconnectBayMappings':
           [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS1'},
            {'interconnectBay': 2, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS1'},
            {'interconnectBay': 3, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS2'},
            {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS2'},
            {'interconnectBay': 5, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 6, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 7, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 8, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None}
            ]}
encs = [{'hostname': '15.186.2.227', 'username': 'Administrator', 'password': 'Compaq123', 'enclosureGroupUri': 'EG:config4-group', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]

SP_body1 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENCLOSURE_NAME + ', bay 5',
             'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENCLOSURE_NAME, 'enclosureGroupUri': 'EG:config4-group', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
             'name': 'PROFILE1', 'description': '', 'affinity': 'Bay',
             'boot': {'manageBoot': False},
             'bootMode': None,
             'connectionSettings': {'connections': [{'id': 1, 'name': 'Connection_1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:wpstnetwork1'}
                                                    ]}}]

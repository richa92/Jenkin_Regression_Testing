def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


def convert_unicode_to_string(String):
    res = String.encode("utf-8")
    return res


APPLIANCE_IP = '15.186.30.57'

ENCLOSURE_IP = '15.186.17.26'

ENCLOSURE_NAME = 'USE0515652'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

oa_details = {"oa_ip": ENCLOSURE_IP, "username": "Administrator", "password": "compaq"}
Preview_uri = '/rest/enclosure-preview'

Preview_body = {"hostname": ENCLOSURE_IP, "username": oa_details['username'], "password": oa_details['password'], "ligPrefix": "LIG1", "force": True, "logicalInterconnectGroupNeeded": True}

users = [{'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True, 'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}]},
         {'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True, 'permissions': [{'roleName': 'Server administrator', 'scopeUri': None}]}
         ]

serveradmin_credentials = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

networkadmin_credentials = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

servers = ['2']

add_up_data = ['fc-comp-add', 'fc-comp-ug2']
edit_up_data = ['fc-comp-ug2']
edit_up2_data = ['fc-comp-ug1']
alert1 = 'The logical interconnect is inconsistent with the logical interconnect group LIG-COMP-OU-1.'
alert2 = 'The logical interconnect is inconsistent with the logical interconnect group LIG-COMP-OU-2.'
interconnects = ['1', '2', '3', '4', '5', '6', '7', '8']
bays = ['3', '4', '5', '6']


add_up_data = ['fc-comp-add', 'fc-comp-ug2']
edit_up_data = ['fc-comp-ug2']
edit_up2_data = ['fc-comp-ug1']

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


LIG = [{'name': 'LIG-COMP-OU-1',
        'type': 'logical-interconnect-groupV6',
        'enclosureType': 'C7000',
        'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 8Gb 24-Port FC Module'}],
        'uplinkSets': [{'name': 'fc-comp-ug1',
                         'ethernetNetworkType': None,
                         'networkType': 'FibreChannel',
                         'networkUris': ['FC_1'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'lacpTimer': 'Short',
                         'logicalPortConfigInfos': [{'bay': '3', 'port': '1', 'speed': 'Auto'}
                                                    ]

                        }],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None},

       {'name': 'LIG-COMP-OU-2',
        'type': 'logical-interconnect-groupV6',
        'enclosureType': 'C7000',
        'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 20-Port FC Module'},
                                    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 20-Port FC Module'},
                                    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC Flex-10 Enet Module'},
                                    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC Flex-10 Enet Module'}],
        'uplinkSets': [{'name': 'fc-comp-ug2',
                        'ethernetNetworkType': None,
                        'networkType': 'FibreChannel',
                        'networkUris': ['FC_2'],
                        'nativeNetworkUri': None,
                        'mode': 'Auto',
                        'lacpTimer': 'Short',
                        'logicalPortConfigInfos': [{'bay': '5', 'port': '2', 'speed': 'Auto'}
                                                   ]

                        }],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None}]

telemetryConfiguration_edit = {'type': 'telemetry-configuration', 'sampleCount': 15, 'sampleInterval': 300, 'enableTelemetry': True}
ethernetSettings_edit = {'type': 'EthernetInterconnectSettingsV5', 'Fast MAC cache failover': False, 'MAC refresh interval': 20, 'IGMP snooping': True, 'IGMP idle timeout interval': 300, 'Loop protection': False}

lig_adduplink = {'name': 'LIG-COMP-OU-2',
                 'type': 'logical-interconnect-groupV6',
                 'enclosureType': 'C7000',
                 'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 20-Port FC Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 20-Port FC Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC Flex-10 Enet Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC Flex-10 Enet Module'}
                                             ],
                 'uplinkSets': [{'name': 'fc-comp-ug2',
                                 'ethernetNetworkType': None,
                                 'networkType': 'FibreChannel',
                                 'networkUris': ['FC_2'],
                                 'nativeNetworkUri': None,
                                 'mode': 'Auto',
                                 'lacpTimer': 'Short',
                                 'logicalPortConfigInfos': [{'bay': '5', 'port': '2', 'speed': 'Auto'}
                                                            # {'bay': '4', 'port': 'X2', 'speed': 'Auto'}
                                                            ]

                                 },
                                {'name': 'fc-comp-add',
                                 'ethernetNetworkType': None,
                                 'networkType': 'FibreChannel',
                                 'networkUris': ['FC_3'],
                                 'nativeNetworkUri': None,
                                 'mode': 'Auto',
                                 'lacpTimer': 'Short',
                                 'logicalPortConfigInfos': [  # {'bay': '3', 'port': '1', 'speed': 'Auto'}
                                     {'bay': '6', 'port': '1', 'speed': 'Auto'}
                                 ]

                                 }],
                 'stackingMode': 'Enclosure',
                 'ethernetSettings': None,
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': None}

lig_deleteuplink = {'name': 'LIG-COMP-OU-1',
                    'type': 'logical-interconnect-groupV6',
                    'enclosureType': 'C7000',
                    'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 8Gb 24-Port FC Module'},

                                                ],
                    'uplinkSets': [],
                    'stackingMode': 'Enclosure',
                    'ethernetSettings': None,
                    'state': 'Active',
                    'telemetryConfiguration': None,
                    'snmpConfiguration': None}

lig_edit_interconnect = [{'name': 'LIG-COMP-OU-1',
                          'type': 'logical-interconnect-groupV6',
                          'enclosureType': 'C7000',
                          'interconnectMapTemplate': [
                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 8Gb 20-Port FC Module'},
                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 8Gb 20-Port FC Module'},

                          ],
                          'uplinkSets': [],
                          'stackingMode': 'Enclosure',
                          'ethernetSettings': None,
                          'state': 'Active',
                          'telemetryConfiguration': None,
                          'snmpConfiguration': None},

                         {'name': 'LIG-COMP-OU-2',
                          'type': 'logical-interconnect-groupV6',
                          'enclosureType': 'C7000',
                          'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'}
                                                      ],
                          'uplinkSets': [],
                          'stackingMode': 'Enclosure',
                          'ethernetSettings': None,
                          'state': 'Active',
                          'telemetryConfiguration': None,
                          'snmpConfiguration': None}]

lig_remove_interconnect = [{'name': 'LIG-COMP-OU-1',
                            'type': 'logical-interconnect-groupV6',
                            'enclosureType': 'C7000',
                            'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 8Gb 24-Port FC Module'}
                                                        # {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 8Gb 24-Port FC Module'},

                                                        ],
                            'uplinkSets': [{'name': 'fc-comp-ug1',
                                            'ethernetNetworkType': None,
                                            'networkType': 'FibreChannel',
                                            'networkUris': ['FC_1'],
                                            'nativeNetworkUri': None,
                                            'mode': 'Auto',
                                            'lacpTimer': 'Short',
                                            'logicalPortConfigInfos': [{'bay': '3', 'port': '1', 'speed': 'Auto'}
                                                                       ]

                                            }],
                            'stackingMode': 'Enclosure',
                            'ethernetSettings': None,
                            'state': 'Active',
                            'telemetryConfiguration': None,
                            'snmpConfiguration': None},

                           {'name': 'LIG-COMP-OU-2',
                            'type': 'logical-interconnect-groupV6',
                            'enclosureType': 'C7000',
                            'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 20-Port FC Module'},
                                                        # {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 20-Port FC Module'},
                                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC Flex-10 Enet Module'},
                                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC Flex-10 Enet Module'}],
                            'uplinkSets': [{'name': 'fc-comp-ug2',
                                            'ethernetNetworkType': None,
                                            'networkType': 'FibreChannel',
                                            'networkUris': ['FC_2'],
                                            'nativeNetworkUri': None,
                                            'mode': 'Auto',
                                            'lacpTimer': 'Short',
                                            'logicalPortConfigInfos': [{'bay': '5', 'port': '2', 'speed': 'Auto'}
                                                                       ]

                                            }],
                            'stackingMode': 'Enclosure',
                            'ethernetSettings': None,
                            'state': 'Active',
                            'telemetryConfiguration': None,
                            'snmpConfiguration': None}]
eg_body = {'name': 'config1-group',
           'ipRangeUris': [],
           'enclosureCount': 1,
           'osDeploymentSettings': None,
           'configurationScript': '',
           'powerMode': None,
           'ambientTemperatureMode': 'Standard',
           'interconnectBayMappings':
           [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU-1'},
            {'interconnectBay': 2, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU-1'},
            {'interconnectBay': 3, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU-1'},
            {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU-1'},
            {'interconnectBay': 5, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU-2'},
            {'interconnectBay': 6, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU-2'},
            {'interconnectBay': 7, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU-2'},
            {'interconnectBay': 8, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-OU-2'}
            ]}

encs = [{'hostname': '15.186.17.26', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:config1-group', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]

SP_body1 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENCLOSURE_NAME + ', bay 2',
             'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENCLOSURE_NAME, 'enclosureGroupUri': 'EG:config1-group', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
             'name': 'PROFILE1', 'description': '', 'affinity': 'Bay',
             'boot': {'manageBoot': False},
             'bootMode': None,
             'connectionSettings': {'connections': [{'id': 1, 'name': 'Connection_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1'}
                                                    ]}}]

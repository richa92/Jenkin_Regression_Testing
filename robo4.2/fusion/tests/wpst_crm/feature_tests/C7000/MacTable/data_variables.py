def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


SSH_PASS = 'hpvse1'

OA_HOST = '192.173.0.20'
OA_USER = 'Administrator'
OA_PASS = 'wpsthpvse1'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

vcenter = {'server': '15.199.230.130', 'user': 'rbriggs', 'password': 'hpvse1'}

appliance = {'type': 'ApplianceNetworkConfigurationV2',
             'applianceNetworks':
                 [{'device': 'eth0',
                   'macAddress': None,
                   'interfaceName': 'VLAN106',
                   'activeNode': '1',
                   'unconfigure': False,
                   'ipv4Type': 'DHCP',
                   'ipv6Type': 'UNCONFIGURE',
                   'hostname': 'mactable.usa.hp.com',
                   'confOneNode': True,
                   'domainName': 'usa.hp.com',
                   'aliasDisabled': True}]}

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['192.173.0.23'],
                 'locale': 'en_US.UTF-8'}

users = [
    {'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin',
     'permissions': [{'roleName': 'Server administrator'}],
     'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'},
    {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin',
     'permissions': [{'roleName': 'Network administrator'}], 'emailAddress': 'nat@hp.com',
     'officePhone': '970-555-0003',
     'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
    {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin',
     'permissions': [{'roleName': 'Backup administrator'}],
     'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'},
    {'userName': 'Noprivledge', 'password': 'Noprivledge', 'fullName': 'Noprivledge',
     'permissions': [{'roleName': 'Read only'}],
     'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'}
]

POSITIVE_USERS = ['Administrator', 'Networkadmin']
NEGATIVE_USERS = ['Serveradmin', 'Backupadmin', 'Noprivledge']

ethernet_ranges = [
    {'prefix': 'net_', 'suffix': '', 'start': 101, 'end': 110, 'name': None, 'type': 'ethernet-networkV4',
     'vlanId': None, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'}
]

fc_networks = [{'name': 'SAN-A', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'SAN-B', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}]

fcoe_networks = [{'name': 'fcoe_103', 'type': 'fcoe-networkV4', 'vlanId': 103},
                 {'name': 'fcoe_104', 'type': 'fcoe-networkV4', 'vlanId': 104}]

enc_groups = [{'name': 'EG',
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': 'LIG:LIG1'}]},
              {'name': 'EG-FC-ONLY',
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG2'},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG2'},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}
              ]

encs = [
    {'hostname': '192.173.0.20', 'username': 'Administrator', 'password': 'wpsthpvse1', 'enclosureGroupUri': 'EG:EG',
     'force': False, 'licensingIntent': 'OneViewNoiLO'}]

negencs = [{'hostname': '192.173.0.20', 'username': 'Administrator', 'password': 'wpsthpvse1',
            'enclosureGroupUri': 'EG:EG-FC-ONLY', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]

ENC1 = 'WPST-PAAW63-EN1'
EG1 = 'EG'
EG2 = 'EG-FC-ONLY'
LIG1 = 'LIG1'
LIG2 = 'LIG2'
LI1 = ENC1 + '-' + LIG1
LI2 = ENC1 + '-' + LIG2

ligs = [{'name': 'LIG1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'},
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'},
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 20-Port FC Module'},
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 20-Port FC Module'},
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
         ],
         'uplinkSets': [{'name': 'US1',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['net_101', 'net_102'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X2', 'speed': 'Auto'},
                                                    {'bay': '2', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '2', 'port': 'X2', 'speed': 'Auto'},
                                                    {'bay': '3', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '3', 'port': 'X2', 'speed': 'Auto'},
                                                    {'bay': '4', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '4', 'port': 'X2', 'speed': 'Auto'},
                                                    {'bay': '7', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '7', 'port': 'X2', 'speed': 'Auto'},
                                                    {'bay': '8', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '8', 'port': 'X2', 'speed': 'Auto'}]},
                        {'name': 'SAN-A',
                         'ethernetNetworkType': 'NotApplicable',
                         'networkType': 'FibreChannel',
                         'networkUris': ['SAN-A'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X4', 'speed': 'Auto'},
                                                    ]},
                        {'name': 'SAN-B',
                         'ethernetNetworkType': 'NotApplicable',
                         'networkType': 'FibreChannel',
                         'networkUris': ['SAN-B'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '2', 'port': 'X4', 'speed': 'Auto'},
                                                    ]}
                        ],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        {'name': 'LIG2',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 20-Port FC Module'},
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 20-Port FC Module'},
         ],
         'uplinkSets': [{'name': 'SAN-A',
                         'ethernetNetworkType': 'NotApplicable',
                         'networkType': 'FibreChannel',
                         'networkUris': ['SAN-A'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '5', 'port': '1', 'speed': 'Auto'}]},
                        {'name': 'SAN-B',
                         'ethernetNetworkType': 'NotApplicable',
                         'networkType': 'FibreChannel',
                         'networkUris': ['SAN-B'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '6', 'port': '1', 'speed': 'Auto'}]}
                        ],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None}
        ]

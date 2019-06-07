def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


SSH_PASS = 'hpvse1'

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
                   'hostname': 'biggs.usa.hp.com',
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
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}]

encs = [
    {'hostname': '192.173.0.20', 'username': 'Administrator', 'password': 'wpsthpvse1', 'enclosureGroupUri': 'EG:EG',
     'force': False, 'licensingIntent': 'OneViewNoiLO'}]

ENC1 = 'WPST-PAAW63-EN1'
LIG1 = 'LIG1'
BAY5_IP = '192.169.0.205'
BAY5 = ENC1 + ', bay 5'
BAY6_IP = '192.169.0.206'
BAY6 = ENC1 + ', bay 6'
SERVERS = [BAY5, BAY6]
GW_IP = '192.169.0.1'

ligs = [{'name': 'LIG1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'},
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'},
         ],
         'uplinkSets': [{'name': 'ETH-FCOE',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['net_101', 'net_102', 'fcoe_103'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '3', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '3', 'port': 'X2', 'speed': 'Auto'},
                                                    {'bay': '3', 'port': 'X3', 'speed': 'Auto'},
                                                    {'bay': '3', 'port': 'X4', 'speed': 'Auto'},
                                                    {'bay': '3', 'port': 'X5', 'speed': 'Auto'},
                                                    # {'bay': '3', 'port': 'X6', 'speed': 'Auto'},  STACKING!
                                                    {'bay': '3', 'port': 'X7', 'speed': 'Auto'},
                                                    {'bay': '3', 'port': 'X8', 'speed': 'Auto'},
                                                    {'bay': '3', 'port': 'X9', 'speed': 'Auto'},
                                                    {'bay': '3', 'port': 'X10', 'speed': 'Auto'}]}
                        ],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None}
        ]

negligs = {'1': {'name': 'invalid-uses-FC',
                 'type': 'logical-interconnect-groupV4',
                 'enclosureType': 'C7000',
                 'interconnectMapTemplate': [
                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'},
                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'},
                 ],
                 'uplinkSets': [{'name': 'FC-not-allowed',
                                 'ethernetNetworkType': 'NotApplicable',
                                 'networkType': 'FibreChannel',
                                 'networkUris': ['SAN-A'],
                                 'nativeNetworkUri': None,
                                 'mode': 'Auto',
                                 'logicalPortConfigInfos': [{'bay': '3', 'port': 'X1', 'speed': 'Auto'},
                                                            {'bay': '3', 'port': 'X2', 'speed': 'Auto'},
                                                            {'bay': '3', 'port': 'X3', 'speed': 'Auto'},
                                                            {'bay': '3', 'port': 'X4', 'speed': 'Auto'},
                                                            {'bay': '3', 'port': 'X5', 'speed': 'Auto'},
                                                            {'bay': '3', 'port': 'X6', 'speed': 'Auto'},
                                                            {'bay': '3', 'port': 'X7', 'speed': 'Auto'},
                                                            {'bay': '3', 'port': 'X8', 'speed': 'Auto'},
                                                            {'bay': '3', 'port': 'X9', 'speed': 'Auto'},
                                                            {'bay': '3', 'port': 'X10', 'speed': 'Auto'}]}
                                ],
                 'stackingMode': 'Enclosure',
                 'ethernetSettings': None,
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': None},
           '2': {'name': 'invalid-uses-X11-X14',
                 'type': 'logical-interconnect-groupV4',
                 'enclosureType': 'C7000',
                 'interconnectMapTemplate': [
                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'},
                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'},
                 ],
                 'uplinkSets': [{'name': 'ETH-FCOE',
                                 'ethernetNetworkType': 'Tagged',
                                 'networkType': 'Ethernet',
                                 'networkUris': ['net_103', 'net_104', 'fcoe_103'],
                                 'nativeNetworkUri': None,
                                 'mode': 'Auto',
                                 'logicalPortConfigInfos': [{'bay': '3', 'port': 'X11', 'speed': 'Auto'},
                                                            {'bay': '3', 'port': 'X12', 'speed': 'Auto'},
                                                            {'bay': '3', 'port': 'X13', 'speed': 'Auto'},
                                                            {'bay': '3', 'port': 'X14', 'speed': 'Auto'}]}
                                ],
                 'stackingMode': 'Enclosure',
                 'ethernetSettings': None,
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': None},

           }

li_uplink_sets = {'us1': {'name': 'Invalid-Uses-FC',
                          'ethernetNetworkType': 'NotApplicable',
                          'networkType': 'FibreChannel',
                          'networkUris': [],
                          'fcNetworkUris': ['SAN-A'],
                          'fcoeNetworkUris': [],
                          'lacpTimer': 'Short',
                          'logicalInterconnectUri': None,
                          'primaryPortLocation': None,
                          'manualLoginRedistributionState': 'NotSupported',
                          'connectionMode': 'Auto',
                          'nativeNetworkUri': None,
                          'portConfigInfos': [{'bay': '4', 'port': 'X10', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  'us2': {'name': 'ETH-FCOE2',
                          'ethernetNetworkType': 'Tagged',
                          'networkType': 'Ethernet',
                          'networkUris': ['net_104'],
                          'fcNetworkUris': [],
                          'fcoeNetworkUris': ['fcoe_1004'],
                          'lacpTimer': 'Short',
                          'logicalInterconnectUri': None,
                          'primaryPortLocation': None,
                          'manualLoginRedistributionState': 'NotSupported',
                          'connectionMode': 'Auto',
                          'nativeNetworkUri': None,
                          'portConfigInfos': [{'bay': '4', 'port': 'X1', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                              {'bay': '4', 'port': 'X2', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                              {'bay': '4', 'port': 'X3', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                              {'bay': '4', 'port': 'X4', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                              {'bay': '4', 'port': 'X5', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                              {'bay': '4', 'port': 'X6', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                              {'bay': '4', 'port': 'X7', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                              {'bay': '4', 'port': 'X8', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                              {'bay': '4', 'port': 'X9', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                              {'bay': '4', 'port': 'X10', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  'us3': {'name': 'Invalid-Uses-X11-X14',
                          'ethernetNetworkType': 'Tagged',
                          'networkType': 'Ethernet',
                          'networkUris': ['net_104'],
                          'fcNetworkUris': [],
                          'fcoeNetworkUris': ['fcoe_1004'],
                          'lacpTimer': 'Short',
                          'logicalInterconnectUri': None,
                          'primaryPortLocation': None,
                          'manualLoginRedistributionState': 'NotSupported',
                          'connectionMode': 'Auto',
                          'nativeNetworkUri': None,
                          'portConfigInfos': [{'bay': '4', 'port': 'X11', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                              {'bay': '4', 'port': 'X12', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                              {'bay': '4', 'port': 'X13', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                              {'bay': '4', 'port': 'X14', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  }

server_profiles = [
    {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 5',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': 'Profile5', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a',
                                             'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                             'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                            {'id': 2, 'name': '2', 'functionType': 'FibreChannel',
                                             'portId': 'Mezz 1:1-b',
                                             'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe_103',
                                             'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                            {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a',
                                             'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                             'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '',
                                             'wwnn': ''}]}},
    {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 6',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': 'Profile6', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a',
                                             'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                             'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                            {'id': 2, 'name': '2', 'functionType': 'FibreChannel',
                                             'portId': 'Mezz 1:1-b',
                                             'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe_103',
                                             'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                            {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a',
                                             'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                             'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '',
                                             'wwnn': ''}]}},
]

"""
{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 3',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Profile3', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Lom 1:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Lom 1:1-b',
                                     'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe_103',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Lom 1:1-c',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                   {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 4',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Profile4', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Lom 1:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Lom 1:1-b',
                                     'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe_103',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Lom 1:1-c',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
"""

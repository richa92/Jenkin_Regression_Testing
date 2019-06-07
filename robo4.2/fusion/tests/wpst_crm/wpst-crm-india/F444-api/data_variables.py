def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

SSH_PASS = 'hpvse1'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

vcenter = {'server': '15.199.230.130', 'user': 'rbriggs', 'password': 'hpvse1'}

appliance = {'type': 'ApplianceNetworkConfiguration',
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

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['192.173.0.23'], 'locale': 'en_US.UTF-8'}

li_spp_downgrade = {'command':'UPDATE','sppUri':'rest/firmware-drivers/SPP2015090_2015_0825_54','force': True}

li_spp_upgrade = {'command':'UPDATE','sppUri':'/rest/firmware-drivers/SPP4_5','force': False}

users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Noprivledge', 'password': 'Noprivledge', 'fullName': 'Noprivledge', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]

POSITIVE_USERS = ['Administrator', 'Networkadmin']
NEGATIVE_USERS = ['Serveradmin', 'Backupadmin', 'Noprivledge']

ethernet_ranges = [{'prefix': 'net_', 'suffix': '', 'start': 101, 'end': 110, 'name': None, 'type': 'ethernet-networkV3',
                    'vlanId': None, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False,
                    'connectionTemplateUri': None,
                    'ethernetNetworkType': 'Tagged'}
                   ]

fc_networks = [{'name': 'SAN-A', 'type': 'fc-networkV300', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'SAN-B', 'type': 'fc-networkV300', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}]


fcoe_networks = [{'name': 'fcoe_103', 'type': 'fcoe-networkV300', 'vlanId': 103},
                 {'name': 'fcoe_104', 'type': 'fcoe-networkV300', 'vlanId': 104}]

enc_groups = [{'name': 'EG',
               'type': 'EnclosureGroupV300',
               'enclosureTypeUri': '/rest/enclosure-types/c7000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 8,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}]

encs = [{'hostname':'10.10.0.2', 'username': 'Administrator', 'password': 'Admin', 'enclosureGroupUri': 'EG:EG', 'force': True, 'licensingIntent': 'OneView'}]
encs1 = [{'hostname':'10.10.0.2', 'username': 'Administrator', 'password': 'Admin', 'enclosureGroupUri': 'EG:EG', 'force': True, 'licensingIntent': 'OneView'}]

ENC1 = 'SGH420HHY8'
LIG1 = 'LIG1'
BAY5_IP = '192.169.0.205'
BAY5 = ENC1 + ', bay 5'
BAY6_IP = '192.169.0.206'
BAY6 = ENC1 + ', bay 6'
SERVERS = [BAY5, BAY6]
GW_IP = '192.169.0.1'

ligs = [{'name': 'LIG1',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC FlexFabric-20/40 F8 Module'}
               
                                     ],
         'uplinkSets': [{'name': 'us1',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['net_101', 'net_102', 'net_103', 'net_104', 'net_105', 'net_106','net_107', 'net_108'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos':[{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                   {'bay': '3', 'port': 'X3', 'speed': 'Auto'}]}
                        ],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'qosConfiguration':None}
        ]

negligs = {'1': {'name': 'invalid-uses-FC',
                 'type': 'logical-interconnect-groupV300',
                 'enclosureType': 'C7000',
                 'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'VC Flex-10/10D Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'VC Flex-10/10D Module'},
                                             ],
                 'uplinkSets': [{'name': 'FC-not-allowed',
                                 'ethernetNetworkType': 'NotApplicable',
                                 'networkType': 'Ethernet',
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
                                                            {'bay': '3', 'port': 'X8', 'speed': 'Auto'}
                                                            #{'bay': '3', 'port': 'X9', 'speed': 'Auto'},
                                                            #{'bay': '3', 'port': 'X10', 'speed': 'Auto'}
                                                            ]}
                                ],
                 'stackingMode': 'Enclosure',
                 'ethernetSettings': None,
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': None},
           '2': {'name': 'invalid-uses-X11-X14',
                 'type': 'logical-interconnect-groupV300',
                 'enclosureType': 'C7000',
                 'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'VC Flex-10/10D Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'VC Flex-10/10D Module'},
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
                   {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 11',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'Profile5', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'mezz 1:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'mezz 1:1-b',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'mezz 1:1-c',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_103',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'mezz 1:1-d',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_104',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    
                                    ]}                 
                  ]

newports_profiles = [
                   {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 11',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'Profile5', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '5', 'functionType': 'Ethernet', 'portId': 'mezz 1:1-e',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_105',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                       
                                    ]}                 
                  ]

newports_profiles1 = [
                   {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 11',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'Profile5', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '5', 'functionType': 'Ethernet', 'portId': 'mezz 1:1-e',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_105',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '6', 'functionType': 'Ethernet', 'portId': 'mezz 1:1-f',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_106',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '7', 'functionType': 'Ethernet', 'portId': 'mezz 1:1-g',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_107',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
   
                                    ]}                 
                  ]

allconn_server_profiles = {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 11',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'Profile5', 'description': '', 'affinity': 'BayAndServer',
                    'eTag': '',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-b',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_103',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-d',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_104',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 5, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-e',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_105',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-f',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_106',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 7, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-g',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_107',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                     {'id': 8, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-h',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_108',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                    
                                    ]} 

mezz_profiles = [
                   {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'Profile5', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'mezz 1:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'mezz 1:1-b',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'mezz 1:1-c',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_103',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'mezz 1:1-d',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_104',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}                                  
                                    ]}               
                  ]

mezz_profiles2 = [
                   {'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'Profile5', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'mezz 1:1-e',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_105',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}                                                                    
                                    ]} 
                  ]  
errormessage = 'Move this connection and other affected connections to different FlexNICs, or upgrade the interconnect firmware to a version that supports the additional FlexNICs. The minimum firmware version required to support additional FlexNICs is 4.50.'                
errormessage1 = 'Select a different port and try again.'

"""
errormessage = 'Select a different port and try again.'


errormessage = 'Move this connection and other affected connections to different FlexNICs, or upgrade the interconnect firmware to a version that supports the additional FlexNICs. The minimum firmware version required to support additional FlexNICs is 4.50.'                
'Select a different port and try again.'



{'type': 'ServerProfileV5', 'serverHardwareUri': ENC1 + ', bay 3',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Profile31', 'description': '', 'affinity': 'Bay',
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
                   {'type': 'ServerProfileV5', 'serverHardwareUri': ENC1 + ', bay 4',
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
li_downlink = [{'enclosureTypeUri': '/rest/logical-downlinks','module1':'HP VC FlexFabric-20/40 F8 Module)',
               'Ports':{"1":"a","2":"b","3":"c","4":"d","5":"e","6":"f","7":"g","8":"h"}},
               {'enclosureTypeUri': '/rest/logical-downlinks','module1':'HP VC Flex-10/10D Module)',
                'Ports':{"1":"a","2":"b","3":"c","4":"d"}},
               {'enclosureTypeUri': '/rest/logical-downlinks','module1':'HP VC FlexFabric-20/40 F8 Module)',
                'Ports':{"1":"a","2":"b","3":"c","4":"d"}}]
               
mezz_downlink = ['mezz 1:1-a','mezz 1:1-b','mezz 1:1-c','mezz 1:1-d']

icmap = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'}]

icmap2 = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC FlexFabric-20/40 F8 Module'}]



uplink_sets = {'us1': {'name': 'us1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['net_101', 'net_102', 'net_103', 'net_104', 'net_105', 'net_106','net_107', 'net_108'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                  {'bay': '1', 'port': 'X2', 'speed': 'Auto'}
                                                  ]},
               'us2': {'name': 'us1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['net_101', 'net_102', 'net_103', 'net_104', 'net_105', 'net_106','net_107', 'net_108'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                  {'bay': '1', 'port': 'X2', 'speed': 'Auto'}
                                                  ]}}

ligs1 = {'lig1':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us1'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        
         'lig2':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap2,
         'uplinkSets': [uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        }
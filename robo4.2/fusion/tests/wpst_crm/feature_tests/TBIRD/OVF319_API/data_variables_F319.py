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

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['192.173.0.23'], 'locale': 'en_US.UTF-8'}

users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Noprivledge', 'password': 'Noprivledge', 'fullName': 'Noprivledge', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]

POSITIVE_USERS = ['Administrator', 'Networkadmin']
NEGATIVE_USERS = ['Serveradmin', 'Backupadmin', 'Noprivledge']

ethernet_ranges = [{'prefix': 'net_', 'suffix': '', 'start': 101, 'end': 110, 'name': None, 'type': 'ethernet-networkV300',
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
               'type': 'EnclosureGroupV400',
               'enclosureTypeUri': '/rest/enclosure-types/c7000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 8,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}]

encs = [{'hostname': '192.173.0.20', 'username': 'Administrator', 'password': 'wpsthpvse1', 'enclosureGroupUri': 'EG:EG', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]

ENC1 = 'Luna'
LIG1 = 'LIG_SGH525WPHT_1'
BAY5_IP = '192.169.0.205'
BAY5 = ENC1 + ', bay 5'
BAY6_IP = '192.169.0.206'
BAY6 = ENC1 + ', bay 6'
SERVERS = [BAY5, BAY6]
GW_IP = '192.169.0.1'
US_edit = 'set1'
stat = 'ports'
port = 'Q1.1'
IC1 = 'Luna, interconnect 2'
INTERCONNECTS = ['Luna, interconnect 1']
Linked_Uplink_port = ['Q2.1']
lig_edit = {'1': {'name': LIG1,
                  'type': 'logical-interconnect-groupV500',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                              ],
                  'uplinkSets': [{'name': 'set1',
                                  'ethernetNetworkType': 'Tagged',
                                  'networkType': 'Ethernet',
                                  'networkUris': ['net1'],
                                  'nativeNetworkUri': None,
                                  'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '1', 'port': 'Q2.1', 'speed': 'Speed40G'}]}
                                 ],
                  'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': {'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': '300', 'sampleInterval': '300'},
                  'snmpConfiguration': None},
            '2': {'name': LIG1,
                  'type': 'logical-interconnect-groupV500',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                              ],
                  'uplinkSets': [{'name': 'set1',
                                  'ethernetNetworkType': 'Tagged',
                                  'networkType': 'Ethernet',
                                  'networkUris': ['net1'],
                                  'nativeNetworkUri': None,
                                  'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '1', 'port': 'Q2.1', 'speed': 'Auto'}]}
                                 ],
                  'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': {'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': '300', 'sampleInterval': '300'},
                  'snmpConfiguration': None},
            '3': {'name': LIG1,
                  'type': 'logical-interconnect-groupV500',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                              ],
                  'uplinkSets': [{'name': 'set1',
                                  'ethernetNetworkType': 'Tagged',
                                  'networkType': 'Ethernet',
                                  'networkUris': ['net1'],
                                  'nativeNetworkUri': None,
                                  'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '1', 'port': 'Q2.2', 'speed': 'Speed40G'}]}
                                 ],
                  'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': {'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': '300', 'sampleInterval': '300'},
                  'snmpConfiguration': None
                  }
            }


ligs = {'1': {'name': LIG1,
              'type': 'logical-interconnect-groupV500',
              'enclosureType': 'C7000',
              'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                          ],
              'uplinkSets': [{'name': 'set1',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                              'networkUris': ['net1'],
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '2', 'port': 'Q1.1', 'speed': 'Speed40G'}]}
                             ],
              'stackingMode': 'Enclosure',
              'ethernetSettings': None,
              'state': 'Active',
              'telemetryConfiguration': {'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': '300', 'sampleInterval': '300'},
              'snmpConfiguration': None},
        '2': {'name': LIG1,
              'type': 'logical-interconnect-groupV500',
              'enclosureType': 'C7000',
              'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                          ],
              'uplinkSets': [{'name': 'set1',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                              'networkUris': ['net1'],
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'}]}
                             ],
              'stackingMode': 'Enclosure',
              'ethernetSettings': None,
              'state': 'Active',
              'telemetryConfiguration': {'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': '300', 'sampleInterval': '300'},
              'snmpConfiguration': None},
        '3': {'name': LIG1,
              'type': 'logical-interconnect-groupV500',
              'enclosureType': 'C7000',
              'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                          ],
              'uplinkSets': [{'name': 'set1',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                              'networkUris': ['net1'],
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '2', 'port': 'Q1.2', 'speed': 'Speed40G'}]}
                             ],
              'stackingMode': 'Enclosure',
              'ethernetSettings': None,
              'state': 'Active',
              'telemetryConfiguration': {'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': '300', 'sampleInterval': '300'},
              'snmpConfiguration': None
              }

        }

li_uplink_sets = {'us1': {'name': 'set1',
                          'ethernetNetworkType': 'Tagged',
                          'networkType': 'Ethernet',
                          'networkUris': ['net1'],
                          'fcNetworkUris': [],
                          'fcoeNetworkUris': [],
                          'lacpTimer': 'Short',
                          'logicalInterconnectUri': None,
                          'primaryPortLocation': None,
                          'manualLoginRedistributionState': 'NotSupported',
                          'connectionMode': 'Auto',
                          'nativeNetworkUri': None,
                          'portConfigInfos': [{'bay': '1', 'port': 'Q2.1', 'desiredSpeed': 'Speed40G', 'enclosure': ENC1}]},
                  'us2': {'name': 'set1',
                          'ethernetNetworkType': 'Tagged',
                          'networkType': 'Ethernet',
                          'networkUris': ['net1'],
                          'fcNetworkUris': [],
                          'fcoeNetworkUris': [],
                          'lacpTimer': 'Short',
                          'logicalInterconnectUri': None,
                          'primaryPortLocation': None,
                          'manualLoginRedistributionState': 'NotSupported',
                          'connectionMode': 'Auto',
                          'nativeNetworkUri': None,
                          'portConfigInfos': [{'bay': '1', 'port': 'Q2.1', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  'us3': {'name': 'set1',
                          'ethernetNetworkType': 'Tagged',
                          'networkType': 'Ethernet',
                          'networkUris': ['net1'],
                          'fcNetworkUris': [],
                          'fcoeNetworkUris': [],
                          'lacpTimer': 'Short',
                          'logicalInterconnectUri': None,
                          'primaryPortLocation': None,
                          'manualLoginRedistributionState': 'NotSupported',
                          'connectionMode': 'Auto',
                          'nativeNetworkUri': None,
                          'portConfigInfos': [{'bay': '1', 'port': 'Q2.2', 'desiredSpeed': 'Speed40G', 'enclosure': ENC1}]},
                  }

server_profiles = [
    {'type': 'ServerProfileV7', 'serverHardwareUri': ENC1 + ', bay 5',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': 'Profile5', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a',
                      'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                     {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1-b',
                      'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe_103',
                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                     {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a',
                      'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
    {'type': 'ServerProfileV7', 'serverHardwareUri': ENC1 + ', bay 6',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': 'Profile6', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a',
                      'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                     {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1-b',
                      'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe_103',
                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                     {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a',
                      'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
]

"""
{'type': 'ServerProfileV7', 'serverHardwareUri': ENC1 + ', bay 3',
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
                   {'type': 'ServerProfileV7', 'serverHardwareUri': ENC1 + ', bay 4',
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

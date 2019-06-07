# from robot.libraries.BuiltIn import BuiltIn

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}
cliq_credentials = {'mgmt_ip': '16.71.149.173', 'username': 'admin', 'password': 'admin'}
oa_credentials = {'username': 'dcs', 'password': 'dcs'}

# Resource types for X-API-Version=1000
APPLIANCE_NETWORK_CONFIGURATION_TYPE = 'ApplianceNetworkConfigurationV2'
TIME_AND_LOCALE_TYPE = 'TimeAndLocale'
USER_AND_PERMISSION_TYPE = 'UserAndPermissions'
ETHERNET_NETWORK_TYPE = 'ethernet-networkV4'
FCOE_NETWORK_TYPE = 'fcoe-networkV4'
FC_NETWORK_TYPE = 'fc-networkV4'
NETWORK_SET_TYPE = 'network-setV5'
LOGICAL_INTERCONNECT_GROUP_TYPE = 'logical-interconnect-groupV5'
SAS_LOGICAL_INTERCONNECT_GROUP_TYPE = 'sas-logical-interconnect-groupV2'
ENCLOSURE_GROUP_TYPE = 'EnclosureGroupV7'
INTERCONNECT_TYPE = 'InterconnectV4'
ENCLOSURE_TYPE = 'EnclosureV7'
STORAGE_SYSTEM_TYPE = 'StorageSystemV4'
SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV6'
SERVER_PROFILE_TYPE = 'ServerProfileV11'
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'

# FTS, users, and licenses

timeandlocale = {
    'type': TIME_AND_LOCALE_TYPE,
    'dateTime': None,
    'timezone': 'UTC',
    'ntpServers': ['ntp.hpecorp.net'],
    'locale': 'en_US.UTF-8'}

users = [
    {"type": USER_AND_PERMISSION_TYPE,
     "userName": "Serveradmin",
     "fullName": "Serveradmin",
     "password": "Serveradmin",
     "emailAddress": "sarah@hp.com",
     "officePhone": "970-555-0003",
     "mobilePhone": "970-500-0003",
     "enabled": True,
     "permissions": [{"roleName": "Server administrator",
                      "scopeUri": None}
                     ]
     },
    {'userName': 'Networkadmin',
     'password': 'Networkadmin',
     'fullName': 'Networkadmin',
     "permissions": [{"roleName": "Network administrator",
                      "scopeUri": None}
                     ],
     'emailAddress': 'nat@hp.com',
     'officePhone': '970-555-0003',
     'mobilePhone': '970-500-0003',
     'type': USER_AND_PERMISSION_TYPE},
    {'userName': 'Backupadmin',
     'password': 'Backupadmin',
     'fullName': 'Backupadmin',
     "permissions": [{"roleName": "Backup administrator",
                      "scopeUri": None}
                     ],
     'emailAddress': 'backup@hp.com',
     'officePhone': '970-555-0003',
     'mobilePhone': '970-500-0003',
     'type': USER_AND_PERMISSION_TYPE},
    {'userName': 'Noprivledge',
     'password': 'Noprivledge',
     'fullName': 'Noprivledge',
     "permissions": [{"roleName": "Read only",
                      "scopeUri": None}
                     ],
     'emailAddress': 'rheid@hp.com',
     'officePhone': '970-555-0003',
     'mobilePhone': '970-500-0003',
     'type': USER_AND_PERMISSION_TYPE}
]

# Enclosures
ENC1 = 'Encl1'
ENC1_OA1 = "172.18.1.11"
ENC2 = 'Encl2'
ENC2_OA1 = "172.18.1.13"
ENC3 = 'Encl3'
ENC3_OA1 = "172.18.1.15"
ENC4 = 'Encl4'
ENC4_OA1 = "172.18.1.17"

# Interconnects
ENC1ICBAY1 = '%s, interconnect 1' % ENC1
ENC1ICBAY2 = '%s, interconnect 2' % ENC1
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY4 = '%s, interconnect 4' % ENC1
ENC1ICBAY5 = '%s, interconnect 5' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
ENC2ICBAY1 = '%s, interconnect 1' % ENC2
ENC2ICBAY2 = '%s, interconnect 2' % ENC2
ENC2ICBAY3 = '%s, interconnect 3' % ENC2
ENC2ICBAY4 = '%s, interconnect 4' % ENC2
ENC2ICBAY5 = '%s, interconnect 5' % ENC2
ENC2ICBAY6 = '%s, interconnect 6' % ENC2
ENC3ICBAY1 = '%s, interconnect 1' % ENC3
ENC3ICBAY2 = '%s, interconnect 2' % ENC3
ENC3ICBAY3 = '%s, interconnect 3' % ENC3
ENC3ICBAY4 = '%s, interconnect 4' % ENC3
ENC3ICBAY5 = '%s, interconnect 5' % ENC3
ENC3ICBAY6 = '%s, interconnect 6' % ENC3
ENC4ICBAY1 = '%s, interconnect 1' % ENC4
ENC4ICBAY2 = '%s, interconnect 2' % ENC4
ENC4ICBAY3 = '%s, interconnect 3' % ENC4
ENC4ICBAY4 = '%s, interconnect 4' % ENC4
ENC4ICBAY5 = '%s, interconnect 5' % ENC4
ENC4ICBAY6 = '%s, interconnect 6' % ENC4

# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1    # BL460c Gen10
ENC1SHBAY2 = '%s, bay 2' % ENC1    # BL660c Gen8
ENC1SHBAY3 = '%s, bay 3' % ENC1    # BL460c Gen10
ENC1SHBAY4 = '%s, bay 4' % ENC1    # BL460c Gen8
ENC1SHBAY5 = '%s, bay 5' % ENC1    # BL460c Gen9
ENC1SHBAY6 = '%s, bay 6' % ENC1    #
ENC1SHBAY7 = '%s, bay 7' % ENC1    # BL660c Gen9
ENC1SHBAY8 = '%s, bay 8' % ENC1    #
ENC1SHBAY9 = '%s, bay 9' % ENC1    #
ENC1SHBAY10 = '%s, bay 10' % ENC1    #

ENC2SHBAY1 = '%s, bay 1' % ENC2    # BL460c Gen8
ENC2SHBAY2 = '%s, bay 2' % ENC2    # BL460c Gen10
ENC2SHBAY3 = '%s, bay 3' % ENC2    # BL460c G7
ENC2SHBAY4 = '%s, bay 4' % ENC2    # BL460c G7
ENC2SHBAY5 = '%s, bay 5' % ENC2    #
ENC2SHBAY6 = '%s, bay 6' % ENC2    #
ENC2SHBAY7 = '%s, bay 7' % ENC2    #
ENC2SHBAY8 = '%s, bay 8' % ENC2  #
ENC2SHBAY9 = '%s, bay 9' % ENC2  #
ENC2SHBAY10 = '%s, bay 10' % ENC2  #

ENC3SHBAY1 = '%s, bay 1' % ENC3    # BL460c G7
ENC3SHBAY2 = '%s, bay 2' % ENC3    # BL460c Gen8
ENC3SHBAY3 = '%s, bay 3' % ENC3    # BL660c Gen8
ENC3SHBAY4 = '%s, bay 4' % ENC3    #
ENC3SHBAY5 = '%s, bay 5' % ENC3    #
ENC3SHBAY6 = '%s, bay 6' % ENC3    #
ENC3SHBAY7 = '%s, bay 7' % ENC3    #
ENC3SHBAY8 = '%s, bay 8' % ENC3    #
ENC3SHBAY9 = '%s, bay 9' % ENC3    # BL460c G7
ENC3SHBAY10 = '%s, bay 10' % ENC3  # BL460c Gen8

ENC4SHBAY1 = '%s, bay 1' % ENC4    # BL460c G7
ENC4SHBAY2 = '%s, bay 2' % ENC4    # BL460c Gen8
ENC4SHBAY3 = '%s, bay 3' % ENC4    # BL460c Gen8
ENC4SHBAY4 = '%s, bay 4' % ENC4    #
ENC4SHBAY5 = '%s, bay 5' % ENC4    #
ENC4SHBAY6 = '%s, bay 6' % ENC4    #
ENC4SHBAY7 = '%s, bay 7' % ENC4    #
ENC4SHBAY8 = '%s, bay 8' % ENC4    #
ENC4SHBAY9 = '%s, bay 9' % ENC4    # BL460c G7
ENC4SHBAY10 = '%s, bay 10' % ENC4  # BL460c Gen8

# DL
DL380_name = 'WIN-6H9DOGLP0AB'
DL380_IP = '172.18.31.4'

Gen10_DLs = [{'name': DL380_name,
              'hostname': DL380_IP,
              'licensingIntent': 'OneViewNoiLO',
              'username': 'Administrator',
              'password': 'hpvse123',
              'force': True,
              'configurationState': 'Managed'}, ]

enc4_bl460 = {"server": ENC4SHBAY5,
              "username": "Administrator",
              "password": "hpvse123",
              "path": "/dcs/rest/passThrough/", }

ris_node_bl460 = {"server": ENC4SHBAY5,
                  "username": "Administrator",
                  "password": "hpvse123",
                  "path": "/redfish/v1/Systems/1/Memory/", }

ris_nodes = [enc4_bl460]

ris_nodes_in_profiles = [enc4_bl460]

# LIGs and EGs
LIG1_NAME = 'LIG1'
EG1_NAME = 'EG1'
LIG2_NAME = 'LIG2'
EG2_NAME = 'EG2'
LIG3_NAME = 'LIG3'
EG3_NAME = 'EG3'
LIG4_NAME = 'LIG4'
EG4_NAME = 'EG4'

ethernet_networks = [
    {'name': 'network-tunnel',
     'type': ETHERNET_NETWORK_TYPE,
     'vlanId': 1,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tunnel'},
    {'name': 'network-untagged',
     'type': ETHERNET_NETWORK_TYPE,
     'vlanId': 1,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Untagged'},
    {'name': 'net100',
     'type': ETHERNET_NETWORK_TYPE,
     'vlanId': 100,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'net300',
     'type': ETHERNET_NETWORK_TYPE,
     'vlanId': 300,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
]

fc_networks = [{'name': 'fa-a', 'autoLoginRedistribution': True, 'type': FC_NETWORK_TYPE, 'linkStabilityTime': '30', 'fabricType': 'FabricAttach', 'connectionTemplateUri': None, 'managedSanUri': None},
               {'name': 'fa-b',
                'autoLoginRedistribution': True,
                'type': FC_NETWORK_TYPE,
                'linkStabilityTime': '30',
                'fabricType': 'FabricAttach',
                'connectionTemplateUri': None,
                'managedSanUri': None},
               {'name': 'FA3',
                'type': FC_NETWORK_TYPE,
                'fabricType': 'FabricAttach',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'managedSanUri': None},
               {'name': 'FA4',
                'type': FC_NETWORK_TYPE,
                'fabricType': 'FabricAttach',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True},
               {'name': 'DA1',
                'type': FC_NETWORK_TYPE,
                'fabricType': 'DirectAttach',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'managedSanUri': None},
               {'name': 'DA2',
                'type': FC_NETWORK_TYPE,
                'fabricType': 'DirectAttach',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True}
               ]

fcoe_networks = [{'name': 'fcoe_103', 'type': FCOE_NETWORK_TYPE, 'vlanId': 103},
                 {'name': 'FCoE1',
                  'type': FCOE_NETWORK_TYPE,
                  'vlanId': 750,
                  'managedSanUri': 'FCSan:VSAN750'},
                 {'name': 'FCoE2',
                  'type': FCOE_NETWORK_TYPE,
                  'vlanId': 850,
                  'managedSanUri': 'FCSan:VSAN850'},
                 ]

network_sets = [{'name': 'NS1',
                 'type': NETWORK_SET_TYPE,
                 'networkUris': ['net100', 'net300'],
                 'nativeNetworkUri': 'net100'},
                {'name': 'Net-Set1',
                 'type': NETWORK_SET_TYPE,
                 'networkUris': ['dev100',
                                 'dev300-pxeboot'],
                 'nativeNetworkUri': None},
                {'name': 'Net-Set2',
                 'type': NETWORK_SET_TYPE,
                 'networkUris': ['dev101-management',
                                 'dev103-ft-a'],
                 'nativeNetworkUri': None},
                ]


ligs = [{'name': LIG1_NAME,
         'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1,
                                      'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2,
                                      'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     ],
         'uplinkSets': [{'name': 'us-untagged',
                         'ethernetNetworkType': 'Untagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['network-untagged'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'}]},
                        {'name': 'us-tunnel',
                         'ethernetNetworkType': 'Tunnel',
                         'networkType': 'Ethernet',
                         'networkUris': ['network-tunnel'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '2', 'port': 'X3', 'speed': 'Auto'}]},
                        ],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        {'name': LIG2_NAME,
         'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10 Enet Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10 Enet Module'},
                                     ],
         'uplinkSets': [{'name': 'us-untagged',
                         'ethernetNetworkType': 'Untagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['network-untagged'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'}]},
                        {'name': 'us-tunnel',
                         'ethernetNetworkType': 'Tunnel',
                         'networkType': 'Ethernet',
                         'networkUris': ['network-tunnel'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'}]},
                        {'name': 'us-tagged',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['net100', 'net300'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '3', 'port': 'X3', 'speed': 'Auto'}, {'bay': '4', 'port': 'X3', 'speed': 'Auto'}]},
                        ],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        {'name': LIG3_NAME,
         'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                     ],
         'uplinkSets': [{'name': 'us-untagged',
                         'ethernetNetworkType': 'Untagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['network-untagged'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'}]},
                        {'name': 'us-tunnel',
                         'ethernetNetworkType': 'Tunnel',
                         'networkType': 'Ethernet',
                         'networkUris': ['network-tunnel'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '2', 'port': 'X3', 'speed': 'Auto'}]},
                        {'name': 'us-fa-a',
                         'ethernetNetworkType': 'NotApplicable',
                         'networkType': 'FibreChannel',
                         'networkUris': ['fa-a'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '5', 'port': '1', 'speed': 'Auto'}]},
                        {'name': 'us-fa-b',
                         'ethernetNetworkType': 'NotApplicable',
                         'networkType': 'FibreChannel',
                         'networkUris': ['fa-b'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '6', 'port': '1', 'speed': 'Auto'}]},
                        ],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        {'name': LIG4_NAME,
         'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 20-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 20-Port FC Module'},
                                     ],
         'uplinkSets': [{'name': 'us-untagged',
                         'ethernetNetworkType': 'Untagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['network-untagged'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'}]},
                        {'name': 'us-tunnel',
                         'ethernetNetworkType': 'Tunnel',
                         'networkType': 'Ethernet',
                         'networkUris': ['network-tunnel'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '2', 'port': 'X3', 'speed': 'Auto'}]},
                        {'name': 'us-fa-a',
                         'ethernetNetworkType': 'NotApplicable',
                         'networkType': 'FibreChannel',
                         'networkUris': ['fa-a'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '5', 'port': '1', 'speed': 'Auto'}]},
                        {'name': 'us-fa-b',
                         'ethernetNetworkType': 'NotApplicable',
                         'networkType': 'FibreChannel',
                         'networkUris': ['fa-b'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '6', 'port': '1', 'speed': 'Auto'}]},
                        ],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        ]

enc_groups = [{'name': EG1_NAME,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]
               },
              {'name': EG2_NAME,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]
               },
              {'name': EG3_NAME,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]
               },
              {'name': EG4_NAME,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG4_NAME},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + LIG4_NAME},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + LIG4_NAME},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG4_NAME},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]
               }
              ]

enclosures = [
    {'hostname': ENC1_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'], 'enclosureGroupUri': 'EG:' + EG1_NAME,
     'force': True, 'licensingIntent': 'OneView', "firmwareBaselineUri": None, },
    {'hostname': ENC2_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'], 'enclosureGroupUri': 'EG:' + EG2_NAME,
     'force': True, 'licensingIntent': 'OneView', "firmwareBaselineUri": None, },
    {'hostname': ENC3_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'], 'enclosureGroupUri': 'EG:' + EG3_NAME,
     'force': True, 'licensingIntent': 'OneView', "firmwareBaselineUri": None, },
    {'hostname': ENC4_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'], 'enclosureGroupUri': 'EG:' + EG4_NAME,
     'force': True, 'licensingIntent': 'OneView', "firmwareBaselineUri": None, }
]

enclosures_expected = [
    {"type": ENCLOSURE_TYPE, "name": ENC1, "state": "Configured", },
    {"type": ENCLOSURE_TYPE, "name": ENC2, "state": "Configured", },
    {"type": ENCLOSURE_TYPE, "name": ENC3, "state": "Configured", },
    {"type": ENCLOSURE_TYPE, "name": ENC4, "state": "Configured", },
]

interconnects_expected = [
    {"type": INTERCONNECT_TYPE,
     "name": ENC1ICBAY1,
     "productName": "HP VC FlexFabric 10Gb/24-Port Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC1ICBAY2,
     "productName": "HP VC FlexFabric 10Gb/24-Port Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC2ICBAY1,
     "productName": "HP VC FlexFabric 10Gb/24-Port Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC2ICBAY2,
     "productName": "HP VC FlexFabric 10Gb/24-Port Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC2ICBAY3,
     "productName": "HP VC Flex-10 Enet Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC2ICBAY4,
     "productName": " HP VC Flex-10 Enet Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC3ICBAY1,
     "productName": " HP VC FlexFabric-20/40 F8 Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC3ICBAY2,
     "productName": "HP VC FlexFabric-20/40 F8 Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC3ICBAY5,
     "productName": "HP VC 8Gb 24-Port FC Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC3ICBAY6,
     "productName": "HP VC 8Gb 24-Port FC Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC4ICBAY1,
     "productName": "HP VC FlexFabric 10Gb/24-Port Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC4ICBAY2,
     "productName": "HP VC FlexFabric 10Gb/24-Port Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC4ICBAY5,
     "productName": "HP VC 8Gb 20-Port FC Module",
     },
    {"type": INTERCONNECT_TYPE,
     "name": ENC4ICBAY6,
     "productName": "HP VC 8Gb 20-Port FC Module",
     },
]


# SAN Manager and Managed SANs
SAN_Managers = [
    {"connectionInfo": [
        {'name': 'Type', 'value': 'Brocade Network Advisor'},
        {"name": "Host",
         "displayName": "Host",
         "required": True,
         "value": "16.125.65.9",
         "valueFormat": "IPAddressOrHostname",
         "valueType": "String"},
        {"name": "Port",
         "displayName": "Port",
         "required": True,
         "value": 5989,
         "valueFormat": "None",
         "valueType": "Integer"},
        {"name": "Username",
         "displayName": "Username",
         "required": True,
         "value": "Administrator",
         "valueFormat": "None",
         "valueType": "String"},
        {"name": "Password",
         "displayName": "Password",
         "required": True,
         "value": "password",
         "valueFormat": "SecuritySensitive",
         "valueType": "String"},
        {"name": "UseSsl", "displayName": "UseSsl", "required": True, "value": True, "valueFormat": "None", "valueType": "Boolean"}, ],
     },
    {"connectionInfo": [
        {'name': 'Type', 'value': 'HPE'},
        {"name": "Host", "value": "16.125.25.45"},
        {"name": "SnmpPort", "value": 161},
        {"name": "SnmpUserName", "value": "UNoAuthNoPriv"},
        {"name": "SnmpAuthLevel", "value": "NOAUTHNOPRIV"}]
     }
]
FA_SAN_A = 'wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55'
FA_SAN_B = 'wpstsan14.vse.rdlabs.hpecorp.net-FID101-10:00:00:27:f8:fe:0c:56'

licenses = {'licenseType': 'HPE OneView Advanced',
            'license': [{'key': 'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'}]}

gen10_server_profiles = [
    {
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": "SH:" + ENC4SHBAY5,
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA:1:HPE Smart Array P416ie-m SR G10",
        "enclosureGroupUri": "EG:" + EG4_NAME,
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": ENC4 + ", bay 8-gen10-Harrier with LS and JBODs",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [{
                "id": 1,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:net100",
                "requestedVFs": "0",
                "ipv4": {},
            }, {
                "id": 2,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:net300",
                "requestedVFs": "0",
                "ipv4": {},
            }]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", "HardDisk", "PXE"]
        },
        "bootMode": {
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None,
            "firmwareScheduleDateTime": "",
            "firmwareActivationType": "Immediate"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{
                "id": "CustomPostMessage",
                "value": "Harrier"
            }]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [{
                "id": 1,
                "deviceSlot": "Mezz 1",
                "name": "ljb1",
                "numPhysicalDrives": 1,
                "driveMinSizeGB": 50,
                "driveMaxSizeGB": 500,
                "driveTechnology": "SasHdd",
                "sasLogicalJBODUri": None
            }],
            "controllers": [{
                "logicalDrives": [{
                    "name": "rd0",
                    "raidLevel": "RAID0",
                    "bootable": False,
                    "numPhysicalDrives": 1,
                    "driveTechnology": "SasHdd",
                    "sasLogicalJBODId": None,
                    "driveNumber": None
                }],
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False
            }]
        },
        "sanStorage": None
    }, ]

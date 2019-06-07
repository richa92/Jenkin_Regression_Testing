from robot.libraries.BuiltIn import BuiltIn

# Resource types for X-API-Version=800
APPLIANCE_NETWORK_CONFIGURATION_TYPE = 'ApplianceNetworkConfigurationV2'
TIME_AND_LOCALE_TYPE = 'TimeAndLocale'
USER_AND_PERMISSION_TYPE = 'UserAndPermissions'
ETHERNET_NETWORK_TYPE = 'ethernet-networkV4'
NETWORK_SET_TYPE = 'network-setV4'
FCOE_NETWORK_TYPE = 'fcoe-networkV4'
FC_NETWORK_TYPE = 'fc-networkV4'
LOGICAL_INTERCONNECT_GROUP_TYPE = 'logical-interconnect-groupV4'
INTERCONNECT_TYPE = 'InterconnectV4'
ENCLOSURE_TYPE = 'EnclosureV7'
ENCLOSURE_GROUP_TYPE = 'EnclosureGroupV7'
SERVER_HARDWARE_TYPE = 'server-hardware-8'
STORAGE_SYSTEM_TYPE = 'StorageSystemV4'
STORAGE_POOL_TYPE = 'StoragePoolV4'
STORAGE_VOLUME_TEMPLATE_TYPE = 'StorageTemplateV4'
STORAGE_VOLUME_TYPE = 'StorageVolumeV4'
SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV6'
SERVER_PROFILE_TYPE = 'ServerProfileV10'
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'

admin_credentials = {'userName': 'Administrator',
                     'password': 'wpsthpvse1'
                     }

oa_credentials = {'username': 'Administrator',
                  'password': 'hpvse14'
                  }

ilo_credentials = {'username': 'Administrator',
                   'password': 'hpvse1-ilo'
                   }

cliq_credentials = {'mgmt_ip': '16.71.148.116',
                    'username': 'admin',
                    'password': 'admin'
                    }

user_specified_cliq_credentials = {'mgmt_ip': '16.71.149.173',
                                   'username': 'admin',
                                   'password': 'admin'
                                   }

dhcp_managed_cluster = {'ip': '16.71.148.116',
                        'username': 'admin',
                        'password': 'admin',
                        'network': 'network-untagged',
                        'clusterName': 'VSA_Cluster_116'
                        }

# LIGs and EGs
LIG1_NAME = 'LIG22'
EG1_NAME = 'EG22'
LIG2_NAME = 'LIG23'
EG2_NAME = 'EG23'
LIG3_NAME = 'LIG26'
EG3_NAME = 'EG26'

# Enclosures
ENC1 = 'wpst22'
ENC1_OA1 = "16.125.77.71"
ENC2 = 'wpst23'
ENC2_OA1 = "16.125.77.80"
ENC3 = 'wpst26'
ENC3_OA1 = "16.125.79.45"

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

interconnects_expected = [
    {"type": INTERCONNECT_TYPE, "name": ENC1ICBAY1, "productName": "HP VC FlexFabric 10Gb/24-Port Module", },
    {"type": INTERCONNECT_TYPE, "name": ENC1ICBAY2, "productName": "HP VC FlexFabric 10Gb/24-Port Module", },
    {"type": INTERCONNECT_TYPE, "name": ENC1ICBAY3, "productName": "HP VC FlexFabric 10Gb/24-Port Module", },
    {"type": INTERCONNECT_TYPE, "name": ENC1ICBAY4, "productName": "HP VC FlexFabric 10Gb/24-Port Module", },
    {"type": INTERCONNECT_TYPE, "name": ENC1ICBAY5, "productName": "HP VC 8Gb 20-Port FC Module", },
    {"type": INTERCONNECT_TYPE, "name": ENC1ICBAY6, "productName": "HP VC 8Gb 20-Port FC Module", },
    {"type": INTERCONNECT_TYPE, "name": ENC2ICBAY1, "productName": "HP VC FlexFabric-20/40 F8 Module", },
    {"type": INTERCONNECT_TYPE, "name": ENC2ICBAY2, "productName": "HP VC FlexFabric-20/40 F8 Module", },
    {"type": INTERCONNECT_TYPE, "name": ENC2ICBAY3, "productName": "HP VC FlexFabric 10Gb/24-Port Module", },
    {"type": INTERCONNECT_TYPE, "name": ENC2ICBAY4, "productName": "HP VC FlexFabric 10Gb/24-Port Module", },
    {"type": INTERCONNECT_TYPE, "name": ENC2ICBAY5, "productName": "HP VC 8Gb 20-Port FC Module", },
    {"type": INTERCONNECT_TYPE, "name": ENC2ICBAY6, "productName": "HP VC 8Gb 20-Port FC Module", },
    {"type": INTERCONNECT_TYPE, "name": ENC3ICBAY1, "productName": "HP VC FlexFabric 10Gb/24-Port Module", },
    {"type": INTERCONNECT_TYPE, "name": ENC3ICBAY2, "productName": "HP VC FlexFabric 10Gb/24-Port Module", },
    {"type": INTERCONNECT_TYPE, "name": ENC3ICBAY3, "productName": "HP VC FlexFabric 10Gb/24-Port Module", },
    {"type": INTERCONNECT_TYPE, "name": ENC3ICBAY4, "productName": "HP VC FlexFabric 10Gb/24-Port Module", },
    {"type": INTERCONNECT_TYPE, "name": ENC3ICBAY5, "productName": "HP VC 8Gb 24-Port FC Module", },
    {"type": INTERCONNECT_TYPE, "name": ENC3ICBAY6, "productName": "HP VC 8Gb 24-Port FC Module", },
]
# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1
ENC1SHBAY2 = '%s, bay 2' % ENC1
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY4 = '%s, bay 4' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC1SHBAY14 = '%s, bay 14' % ENC1
ENC1SHBAY16 = '%s, bay 16' % ENC1
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC2SHBAY2 = '%s, bay 2' % ENC2
ENC2SHBAY3 = '%s, bay 3' % ENC2
ENC2SHBAY4 = '%s, bay 4' % ENC2
ENC2SHBAY5 = '%s, bay 5' % ENC2
ENC2SHBAY6 = '%s, bay 6' % ENC2
ENC2SHBAY7 = '%s, bay 7' % ENC2
ENC3SHBAY1 = '%s, bay 1' % ENC3
ENC3SHBAY2 = '%s, bay 2' % ENC3
ENC3SHBAY3 = '%s, bay 3' % ENC3
ENC3SHBAY4 = '%s, bay 4' % ENC3
ENC3SHBAY5 = '%s, bay 5' % ENC3
ENC3SHBAY6 = '%s, bay 6' % ENC3
ENC3SHBAY7 = '%s, bay 7' % ENC3
ENC3SHBAY8 = '%s, bay 8' % ENC3
ENC3SHBAY9 = '%s, bay 9' % ENC3
ENC3SHBAY10 = '%s, bay 10' % ENC3

APP1_IPV4_ADDRESS = BuiltIn().get_variable_value("${APPLIANCE_IP}")
HOSTNAME = "FVT-C7000-Regression"

appliance = {'type': APPLIANCE_NETWORK_CONFIGURATION_TYPE,
             'applianceNetworks':
                 [{'device': 'eth0',
                   'macAddress': None,
                   'interfaceName': 'Appliance',
                   'activeNode': '1',
                   'unconfigure': False,
                   'ipv4Type': 'STATIC',
                   'app1Ipv4Addr': APP1_IPV4_ADDRESS,
                   'ipv6Type': 'UNCONFIGURE',
                   'ipv4Subnet': '255.255.240.0',
                   'ipv4Gateway': '16.114.208.1',
                   'hostname': HOSTNAME,
                   'confOneNode': True,
                   'domainName': 'vse.rdlabs.hpecorp.net',
                   'ipv4NameServers': ['16.125.25.81', '16.125.25.82', '16.125.24.20'],
                   'aliasDisabled': True}]}

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

licenses = [
    {'key':
        '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZY2-LDVV4-92DQT-L6TTW'},
    {'key':
        'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
]


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

network_sets = [{'name': 'NS1', 'type': NETWORK_SET_TYPE, 'networkUris': ['net100', 'net300'], 'nativeNetworkUri': 'net100'}, ]

ligs = [{'name': LIG1_NAME,
         'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
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
        {'name': LIG2_NAME,
         'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 20-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 20-Port FC Module'},
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
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
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
        ]

enc_groups = [{'name': EG1_NAME,
               'type': ENCLOSURE_GROUP_TYPE,
               'enclosureTypeUri': '/rest/enclosure-types/c7000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 8,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]
               },
              {'name': EG2_NAME,
               'type': ENCLOSURE_GROUP_TYPE,
               'enclosureTypeUri': '/rest/enclosure-types/c7000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 8,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]
               },
              {'name': EG3_NAME,
               'type': ENCLOSURE_GROUP_TYPE,
               'enclosureTypeUri': '/rest/enclosure-types/c7000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 8,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]
               }
              ]

enclosures = [
    {'hostname': ENC1_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'], 'enclosureGroupUri': 'EG:' + EG1_NAME,
     'force': True, 'licensingIntent': 'OneViewNoiLO'},
    {'hostname': ENC2_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'], 'enclosureGroupUri': 'EG:' + EG2_NAME,
     'force': True, 'licensingIntent': 'OneViewNoiLO'},
    {'hostname': ENC3_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'], 'enclosureGroupUri': 'EG:' + EG3_NAME,
     'force': True, 'licensingIntent': 'OneViewNoiLO'},
]

enclosures_expected = [
    {"type": ENCLOSURE_TYPE, "name": "wpst22", "state": "Configured", },
    {"type": ENCLOSURE_TYPE, "name": "wpst23", "state": "Configured", },
    {"type": ENCLOSURE_TYPE, "name": "wpst23", "state": "Configured", },
]

TEMPLATE_SHT = 'BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class'
Gen10_TEMPLATE_SHT = 'BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter'

# MANAGED VOLUMES
ENC1BAY1_VOLUME_NAME = 'wpst22-bay1-dhcp-managed-volume'
ENC1BAY5_VOLUME_NAME = 'wpst22-bay5-dhcp-managed-volume'
ENC3BAY7_VOLUME_NAME = 'wpst26-bay7-dhcp-managed-volume'
ENC3BAY8_VOLUME_NAME = 'wpst26-bay8-dhcp-managed-volume'
ENC2BAY1_VOLUME_NAME = 'wpst23-bay1-dhcp-managed-volume'

# iSCSI
INITIATOR_GATEWAY = "192.168.0.1"
INITIATOR_SUBNET_MASK = "255.255.192.0"
DHCP_BOOT_TARGET_IP = "192.168.21.59"
USER_SPECIFIED_BOOT_TARGET_IP = "192.168.21.71"
CHAP_SECRET = "wpsthpvse123"
MCHAP_SECRET = "hpvse123wpst"

# ENC1BAY1_PROFILE1: profile on ENC1 bay1, BL465c Gen8 DHCP Initiator
ENC1BAY1_PROFILE1_NAME = "wpst22-bay1"
ENC1BAY1_PROFILE1_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-116:766:wpst22-bay1-dhcp'
ENC1BAY1_PROFILE1_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst22-bay1-dhcp"

# ENC1BAY1_PROFILE2: profile on ENC1 bay1, BL465c Gen8 User Specified Initiator with MCHAP
ENC1BAY1_PROFILE2_NAME = "wpst22-bay1"
ENC1BAY1_PROFILE2_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1300:wpst22-bay1-bootvol'
ENC1BAY1_PROFILE2_INITIATOR_IP_1 = "192.168.22.140"
ENC1BAY1_PROFILE2_INITIATOR_IP_2 = "192.168.22.141"
ENC1BAY1_PROFILE2_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst22-bay1"
ENC1BAY1_PROFILE2_CHAP_NAME = 'wpst22-bay1'
ENC1BAY1_PROFILE2_MCHAP_NAME = 'wpst22-bay1'

# ENC1BAY1_PROFILE3: profile on ENC1 bay1, BL465c Gen8 DHCP managed volume
ENC1BAY1_PROFILE3_NAME = "wpst22-bay1"
ENC1BAY1_PROFILE3_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst22-bay1-dhcp-managed-volume"


# ENC1BAY5_PROFILE1: profile on ENC1 bay5, BL460c Gen9 DHCP Initiator with CHAP
ENC1BAY5_PROFILE1_NAME = "wpst22-bay5"
ENC1BAY5_PROFILE1_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-116:769:wpst22-bay5-dhcp'
ENC1BAY5_PROFILE1_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst22-bay5-dhcp"
ENC1BAY5_PROFILE1_CHAP_NAME = 'wpst22-bay5'

# ENC1BAY5_PROFILE2: profile on ENC1 bay5, BL460c Gen9 User Specified Initiator
ENC1BAY5_PROFILE2_NAME = "wpst22-bay5"
ENC1BAY5_PROFILE2_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1303:wpst22-bay5-bootvol'
ENC1BAY5_PROFILE2_INITIATOR_IP_1 = "192.168.22.142"
ENC1BAY5_PROFILE2_INITIATOR_IP_2 = "192.168.22.143"
ENC1BAY5_PROFILE2_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst22-bay5"
ENC1BAY5_PROFILE2_CHAP_NAME = 'wpst22-bay5'

# ENC1BAY5_PROFILE3: profile on ENC1 bay5, BL460c Gen9 DHCP managed volume
ENC1BAY5_PROFILE3_NAME = "wpst22-bay5"
ENC1BAY5_PROFILE3_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst22-bay5-dhcp-managed-volume"


# ENC3BAY7_PROFILE1: profile on ENC3 bay7, BL660c Gen9 DHCP Initiator
ENC3BAY7_PROFILE1_NAME = "wpst26-bay7"
ENC3BAY7_PROFILE1_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-116:784:wpst26-bay7-dhcp'
ENC3BAY7_PROFILE1_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst26-bay7-dhcp"

# ENC3BAY7_PROFILE2: profile on ENC3 bay7, BL660c Gen9 User Specified Initiator with CHAP
ENC3BAY7_PROFILE2_NAME = "wpst26-bay7"
ENC3BAY7_PROFILE2_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1309:wpst26-bay7-bootvol'
ENC3BAY7_PROFILE2_INITIATOR_IP_1 = "192.168.22.144"
ENC3BAY7_PROFILE2_INITIATOR_IP_2 = "192.168.22.145"
ENC3BAY7_PROFILE2_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst26-bay7"
ENC3BAY7_PROFILE2_CHAP_NAME = 'wpst26-bay7'
ENC3BAY7_PROFILE2_MCHAP_NAME = 'wpst26-bay7'

# ENC3BAY7_PROFILE3: profile on ENC3 bay7, BL660c Gen9 DHCP managed volume
ENC3BAY7_PROFILE3_NAME = "wpst26-bay7"
ENC3BAY7_PROFILE3_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst26-bay7-dhcp-managed-volume"


# ENC3BAY8_PROFILE1: profile on ENC3 bay8, BL660c Gen8 DHCP Initiator with CHAP
ENC3BAY8_PROFILE1_NAME = "wpst26-bay8"
ENC3BAY8_PROFILE1_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-116:787:wpst26-bay8-dhcp'
ENC3BAY8_PROFILE1_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst26-bay8-dhcp"
ENC3BAY8_PROFILE1_CHAP_NAME = 'wpst26-bay8'
ENC3BAY8_PROFILE1_MCHAP_NAME = 'wpst26-bay8'

# ENC3BAY8_PROFILE2: profile on ENC3 bay8, BL660c Gen8 User Specified Initiator
ENC3BAY8_PROFILE2_NAME = "wpst26-bay8"
ENC3BAY8_PROFILE2_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1312:wpst26-bay8-bootvol'
ENC3BAY8_PROFILE2_INITIATOR_IP_1 = "192.168.22.146"
ENC3BAY8_PROFILE2_INITIATOR_IP_2 = "192.168.22.147"
ENC3BAY8_PROFILE2_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst26-bay8"
ENC3BAY8_PROFILE2_CHAP_NAME = 'wpst26-bay8'

# ENC3BAY8_PROFILE3: profile on ENC3 bay8, BL660c Gen8 DHCP managed volume
ENC3BAY8_PROFILE3_NAME = "wpst26-bay8"
ENC3BAY8_PROFILE3_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst26-bay8-dhcp-managed-volume"


# ENC2BAY1_PROFILE1: profile on ENC2 bay1 DHCP Initiator with CHAP
ENC2BAY1_PROFILE1_NAME = "wpst23-bay1"
ENC2BAY1_PROFILE1_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-116:772:wpst23-bay1-dhcp'
ENC2BAY1_PROFILE1_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst23-bay1-dhcp"
ENC2BAY1_PROFILE1_CHAP_NAME = 'wpst23-bay1'

# ENC2BAY1_PROFILE2: profile on ENC2 bay1 User Specified Initiator
ENC2BAY1_PROFILE2_NAME = "wpst23-bay1"
ENC2BAY1_PROFILE2_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1315:wpst23-bay1-bootvol'
ENC2BAY1_PROFILE2_INITIATOR_IP_1 = "192.168.22.148"
ENC2BAY1_PROFILE2_INITIATOR_IP_2 = "192.168.22.149"
ENC2BAY1_PROFILE2_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst23-bay1"

# ENC2BAY1_PROFILE3: profile on ENC2 bay1 DHCP managed volume
ENC2BAY1_PROFILE3_NAME = "wpst23-bay1"
ENC2BAY1_PROFILE3_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst23-bay1-dhcp-managed-volume"

# ENC1BAY14_PROFILE1: profile on ENC1 bay14, BL460c Gen10 DHCP Initiator
ENC1BAY14_PROFILE1_NAME = "wpst22-bay14-profile1-two-connections"
ENC1BAY14_PROFILE1_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst22-bay14-dhcp"
ENC1BAY14_EDIT_PROFILE1_NAME = "wpst22-bay14-profile1-one-connection"

# ENC1BAY16_PROFILE1: profile on ENC1 bay16, BL460c Gen10 DHCP Initiator
ENC1BAY16_PROFILE1_NAME = "wpst22-bay16-profile1-one-connection-untagged"
ENC1BAY16_PROFILE1_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst22-bay16-dhcp"


STORAGE_POOL = 'VSA_Cluster_116'

existing_volumes = [
    {
        "storageSystemUri": STORAGE_POOL,
        "name": ENC1BAY1_VOLUME_NAME,
        "deviceVolumeName": ENC1BAY1_VOLUME_NAME,
        "isShareable": False,
    },
    {
        "storageSystemUri": STORAGE_POOL,
        "name": ENC1BAY5_VOLUME_NAME,
        "deviceVolumeName": ENC1BAY5_VOLUME_NAME,
        "isShareable": False,
    },
    {
        "storageSystemUri": STORAGE_POOL,
        "name": ENC3BAY7_VOLUME_NAME,
        "deviceVolumeName": ENC3BAY7_VOLUME_NAME,
        "isShareable": False,
    },
    {
        "storageSystemUri": STORAGE_POOL,
        "name": ENC3BAY8_VOLUME_NAME,
        "deviceVolumeName": ENC3BAY8_VOLUME_NAME,
        "isShareable": False,
    },
    {
        "storageSystemUri": STORAGE_POOL,
        "name": ENC2BAY1_VOLUME_NAME,
        "deviceVolumeName": ENC2BAY1_VOLUME_NAME,
        "isShareable": False,
    },
]


# Profile1 Two Connections: ENC1 bay 1, BL465c Gen8
# DHCP Initiator
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
enc1bay1_profile1_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY1, 'enclosureUri': 'ENC:' + ENC1,
                                     "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                     "macType": "Physical", "wwnType": "Physical", "name": ENC1BAY1_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                     "connectionSettings": {
                                         "connections": [
                                             {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                              "boot": {
                                                  "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                      "firstBootTargetPort": "3260",
                                                      "bootTargetName": ENC1BAY1_PROFILE1_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "chapLevel": "None",
                                                      "chapName": "",
                                                      "chapSecret": None,
                                                      "mutualChapName": "",
                                                      "mutualChapSecret": None
                                                  }}},
                                             {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                                 "boot": {
                                                  "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                      "firstBootTargetPort": "3260",
                                                      "bootTargetName": ENC1BAY1_PROFILE1_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "chapLevel": "None",
                                                      "chapName": "",
                                                      "chapSecret": None,
                                                      "mutualChapName": "",
                                                      "mutualChapSecret": None
                                                  }}}
                                         ]
                                     },
                                     "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                     "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                     "iscsiInitiatorName": ENC1BAY1_PROFILE1_INITIATOR_NAME,
                                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                     }


# Profile1 One Connection Tunnel: ENC1 bay 1, BL465c Gen8
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to tunnel network
enc1bay1_profile1_one_connection_tunnel = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY1, 'enclosureUri': 'ENC:' + ENC1,
                                           "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                           "macType": "Physical", "wwnType": "Physical", "name": ENC1BAY1_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                           "connectionSettings": {
                                               "connections": [
                                                   {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                    "networkUri": 'ETH:network-tunnel',
                                                    "ipv4": {
                                                        "ipAddressSource": "DHCP",
                                                        "subnetMask": "",
                                                        "gateway": "",
                                                    },
                                                       "boot": {
                                                        "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                        "iscsi": {
                                                            "initiatorNameSource": "UserDefined",
                                                            "initiatorName": ENC1BAY1_PROFILE1_INITIATOR_NAME,
                                                            "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                            "firstBootTargetPort": "3260",
                                                            "bootTargetName": ENC1BAY1_PROFILE1_BOOT_TARGET_NAME,
                                                            "bootTargetLun": "0",
                                                            "chapLevel": "None",
                                                            "chapName": "",
                                                            "chapSecret": None,
                                                            "mutualChapName": "",
                                                            "mutualChapSecret": None
                                                        }}}
                                               ]
                                           },
                                           "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                           "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                           "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                           "iscsiInitiatorName": ENC1BAY1_PROFILE1_INITIATOR_NAME,
                                           "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                           }


# Profile1 One Connection Untagged: ENC1 bay 1, BL465c Gen8
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to Untagged network
enc1bay1_profile1_one_connection_untagged = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY1, 'enclosureUri': 'ENC:' + ENC1,
                                             "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                             "macType": "Physical", "wwnType": "Physical", "name": ENC1BAY1_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                             "connectionSettings": {
                                                 "connections": [
                                                     {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                      "networkUri": 'ETH:network-untagged',
                                                      "ipv4": {
                                                          "ipAddressSource": "DHCP",
                                                          "subnetMask": "",
                                                          "gateway": "",
                                                      },
                                                         "boot": {
                                                          "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                          "iscsi": {
                                                              "initiatorNameSource": "UserDefined",
                                                              "initiatorName": ENC1BAY1_PROFILE1_INITIATOR_NAME,
                                                              "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                              "firstBootTargetPort": "3260",
                                                              "bootTargetName": ENC1BAY1_PROFILE1_BOOT_TARGET_NAME,
                                                              "bootTargetLun": "0",
                                                              "chapLevel": "None",
                                                              "chapName": "",
                                                              "chapSecret": None,
                                                              "mutualChapName": "",
                                                              "mutualChapSecret": None
                                                          }}}
                                                 ]
                                             },
                                             "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                             "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                             "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                             "iscsiInitiatorName": ENC1BAY1_PROFILE1_INITIATOR_NAME,
                                             "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                             }

# Profile2 Two Connections: ENC1 bay 1, BL465c Gen8
# User Specified Initiator and Target
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
enc1bay1_profile2_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY1, 'enclosureUri': 'ENC:' + ENC1,
                                     "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                     "macType": "Physical", "wwnType": "Physical", "name": ENC1BAY1_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                     "connectionSettings": {
                                         "connections": [
                                             {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "UserDefined",
                                                  "ipAddress": ENC1BAY1_PROFILE2_INITIATOR_IP_1,
                                                  "subnetMask": INITIATOR_SUBNET_MASK,
                                                  "gateway": ""
                                              },
                                              "boot": {
                                                  "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "bootTargetName": ENC1BAY1_PROFILE2_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                      "firstBootTargetPort": "3260",
                                                      "chapLevel": "MutualChap",
                                                      "chapName": ENC1BAY1_PROFILE2_CHAP_NAME,
                                                      "chapSecret": CHAP_SECRET,
                                                      "mutualChapName": ENC1BAY1_PROFILE2_MCHAP_NAME,
                                                      "mutualChapSecret": MCHAP_SECRET
                                                  }}},
                                             {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                              "ipv4": {
                                                  "ipAddressSource": "UserDefined",
                                                  "ipAddress": ENC1BAY1_PROFILE2_INITIATOR_IP_2,
                                                  "subnetMask": INITIATOR_SUBNET_MASK,
                                                  "gateway": ""
                                              },
                                                 "boot": {
                                                  "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "bootTargetName": ENC1BAY1_PROFILE2_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                      "firstBootTargetPort": "3260",
                                                      "chapLevel": "MutualChap",
                                                      "chapName": ENC1BAY1_PROFILE2_CHAP_NAME,
                                                      "chapSecret": CHAP_SECRET,
                                                      "mutualChapName": ENC1BAY1_PROFILE2_MCHAP_NAME,
                                                      "mutualChapSecret": MCHAP_SECRET
                                                  }}}
                                         ]
                                     },
                                     "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                     "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                     "iscsiInitiatorName": ENC1BAY1_PROFILE2_INITIATOR_NAME,
                                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                     }

# Profile2 One Connection Tunnel: ENC1 bay 1, BL465c Gen8
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to tunnel network
enc1bay1_profile2_one_connection_tunnel = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY1, 'enclosureUri': 'ENC:' + ENC1,
                                           "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                           "macType": "Physical", "wwnType": "Physical", "name": ENC1BAY1_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                           "connectionSettings": {
                                               "connections": [
                                                   {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                    "networkUri": 'ETH:network-tunnel',
                                                    "ipv4": {
                                                        "ipAddressSource": "UserDefined",
                                                        "ipAddress": ENC1BAY1_PROFILE2_INITIATOR_IP_1,
                                                        "subnetMask": INITIATOR_SUBNET_MASK,
                                                        "gateway": ""
                                                    },
                                                       "boot": {
                                                        "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                        "iscsi": {
                                                            "initiatorNameSource": "ProfileInitiatorName",
                                                            "bootTargetName": ENC1BAY1_PROFILE2_BOOT_TARGET_NAME,
                                                            "bootTargetLun": "0",
                                                            "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                            "firstBootTargetPort": "3260",
                                                            "chapLevel": "MutualChap",
                                                            "chapName": ENC1BAY1_PROFILE2_CHAP_NAME,
                                                            "chapSecret": CHAP_SECRET,
                                                            "mutualChapName": ENC1BAY1_PROFILE2_MCHAP_NAME,
                                                            "mutualChapSecret": MCHAP_SECRET
                                                        }}}
                                               ]
                                           },
                                           "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                           "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                           "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                           "iscsiInitiatorName": ENC1BAY1_PROFILE2_INITIATOR_NAME,
                                           "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                           }

# Profile2 One Connection Untagged: ENC1 bay 1, BL465c Gen8
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to Untagged network
enc1bay1_profile2_one_connection_untagged = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY1, 'enclosureUri': 'ENC:' + ENC1,
                                             "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                             "macType": "Physical", "wwnType": "Physical", "name": ENC1BAY1_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                             "connectionSettings": {
                                                 "connections": [
                                                     {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                      "networkUri": 'ETH:network-untagged',
                                                      "ipv4": {
                                                          "ipAddressSource": "UserDefined",
                                                          "ipAddress": ENC1BAY1_PROFILE2_INITIATOR_IP_1,
                                                          "subnetMask": INITIATOR_SUBNET_MASK,
                                                          "gateway": ""
                                                      },
                                                         "boot": {
                                                          "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                          "iscsi": {
                                                              "initiatorNameSource": "ProfileInitiatorName",
                                                              "bootTargetName": ENC1BAY1_PROFILE2_BOOT_TARGET_NAME,
                                                              "bootTargetLun": "0",
                                                              "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                              "firstBootTargetPort": "3260",
                                                              "chapLevel": "MutualChap",
                                                              "chapName": ENC1BAY1_PROFILE2_CHAP_NAME,
                                                              "chapSecret": CHAP_SECRET,
                                                              "mutualChapName": ENC1BAY1_PROFILE2_MCHAP_NAME,
                                                              "mutualChapSecret": MCHAP_SECRET
                                                          }}}
                                                 ]
                                             },
                                             "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                             "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                             "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                             "iscsiInitiatorName": ENC1BAY1_PROFILE2_INITIATOR_NAME,
                                             "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                             }

# Profile3 Two Connections: ENC1 bay 1, BL465c Gen8
# DHCP Initiator
# Managed Volume
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to untagged network
enc1bay1_profile3_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY1, 'enclosureUri': 'ENC:' + ENC1,
                                     "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                     "macType": "Physical", "wwnType": "Physical", "name": ENC1BAY1_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                     "connectionSettings": {
                                         "connections": [
                                             {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                              "boot": {
                                                  "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                                              }},
                                             {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                                 "boot": {
                                                  "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
                                              }}
                                         ]
                                     },
                                     "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                     "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                     "iscsiInitiatorName": ENC1BAY1_PROFILE3_INITIATOR_NAME,
                                     "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                     "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                    "volumeAttachments": [
                                                        {
                                                            "id": 1,
                                                            "isBootVolume": True,
                                                            "lun": None,
                                                            "lunType": "Auto",
                                                            "storagePaths": [{
                                                                "isEnabled": True,
                                                                "connectionId": "1",
                                                                "targetSelector": "Auto",
                                                                "targets": []
                                                            }],
                                                            "volume": None,
                                                            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                                                            "volumeUri": 'v:' + ENC1BAY1_VOLUME_NAME,
                                                        }
                                                    ]
                                                    }
                                     }


# Profile3 One Connection Untagged: ENC1 bay 1, BL465c Gen8
# DHCP Initiator
# Managed volume
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexibleLOM1:1b to Untagged network
enc1bay1_profile3_one_connection_untagged = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY1, 'enclosureUri': 'ENC:' + ENC1,
                                             "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                             "macType": "Physical", "wwnType": "Physical", "name": ENC1BAY1_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                             "connectionSettings": {
                                                 "connections": [
                                                     {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                                      "ipv4": {
                                                          "ipAddressSource": "DHCP",
                                                          "subnetMask": "",
                                                          "gateway": "",
                                                      },
                                                      "boot": {
                                                          "priority": "Primary", "bootVolumeSource": "ManagedVolume"
                                                      }},
                                                 ]
                                             },
                                             "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                             "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                             "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                             "iscsiInitiatorName": ENC1BAY1_PROFILE3_INITIATOR_NAME,
                                             "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                             "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                            "volumeAttachments": [
                                                                {
                                                                    "id": 1,
                                                                    "isBootVolume": True,
                                                                    "lun": None,
                                                                    "lunType": "Auto",
                                                                    "storagePaths": [{
                                                                        "isEnabled": True,
                                                                        "connectionId": "1",
                                                                        "targetSelector": "Auto",
                                                                        "targets": []
                                                                    }],
                                                                    "volume": None,
                                                                    "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                                                                    "volumeUri": 'v:' + ENC1BAY1_VOLUME_NAME,
                                                                }
                                                            ]
                                                            }
                                             }


# Profile1 Two Connections: ENC1 bay5, BL460c Gen9
# DHCP Initiator
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
enc1bay5_profile1_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY5, 'enclosureUri': 'ENC:' + ENC1,
                                     "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                     "macType": "Physical", "wwnType": "Physical", "name": ENC1BAY5_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                     "connectionSettings": {
                                         "connections": [
                                             {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "ipAddress": "",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                              "boot": {
                                                  "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "bootTargetName": ENC1BAY5_PROFILE1_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                      "chapLevel": "Chap",
                                                      "chapName": ENC1BAY5_PROFILE1_CHAP_NAME,
                                                      "chapSecret": CHAP_SECRET,
                                                      "mutualChapName": "",
                                                      "mutualChapSecret": None
                                                  }}},
                                             {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "ipAddress": "",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                                 "boot": {
                                                  "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "bootTargetName": ENC1BAY5_PROFILE1_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                      "chapLevel": "Chap",
                                                      "chapName": ENC1BAY5_PROFILE1_CHAP_NAME,
                                                      "chapSecret": CHAP_SECRET,
                                                      "mutualChapName": "",
                                                      "mutualChapSecret": None
                                                  }}}
                                         ]
                                     },
                                     "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                     "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                     "iscsiInitiatorName": ENC1BAY5_PROFILE1_INITIATOR_NAME,
                                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                     }


# Profile1 One Connection Tunnel: ENC1 bay5, BL460c Gen9
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to tunnel network
enc1bay5_profile1_one_connection_tunnel = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY5, 'enclosureUri': 'ENC:' + ENC1,
                                           "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                           "macType": "Physical", "wwnType": "Physical", "name": ENC1BAY5_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                           "connectionSettings": {
                                               "connections": [
                                                   {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                                                    "networkUri": 'ETH:network-tunnel',
                                                    "ipv4": {
                                                        "ipAddressSource": "DHCP",
                                                        "subnetMask": "",
                                                        "gateway": "",
                                                    },
                                                       "boot": {
                                                        "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                        "iscsi": {
                                                            "initiatorNameSource": "UserDefined",
                                                            "initiatorName": ENC1BAY5_PROFILE1_INITIATOR_NAME,
                                                            "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                            "firstBootTargetPort": "3260",
                                                            "bootTargetName": ENC1BAY5_PROFILE1_BOOT_TARGET_NAME,
                                                            "bootTargetLun": "0",
                                                            "chapLevel": "Chap",
                                                            "chapName": ENC1BAY5_PROFILE1_CHAP_NAME,
                                                            "chapSecret": CHAP_SECRET,
                                                            "mutualChapName": "",
                                                            "mutualChapSecret": None
                                                        }}}
                                               ]
                                           },
                                           "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                           "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                           "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                           "iscsiInitiatorName": ENC1BAY5_PROFILE1_INITIATOR_NAME,
                                           "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                           }


# Profile1 One Connection Untagged: ENC1 bay5, BL460c Gen9
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to Untagged network
enc1bay5_profile1_one_connection_untagged = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY5, 'enclosureUri': 'ENC:' + ENC1,
                                             "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                             "macType": "Physical", "wwnType": "Physical", "name": ENC1BAY5_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                             "connectionSettings": {
                                                 "connections": [
                                                     {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                      "networkUri": 'ETH:network-untagged',
                                                      "ipv4": {
                                                          "ipAddressSource": "DHCP",
                                                          "subnetMask": "",
                                                          "gateway": "",
                                                      },
                                                         "boot": {
                                                          "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                          "iscsi": {
                                                              "initiatorNameSource": "UserDefined",
                                                              "initiatorName": ENC1BAY5_PROFILE1_INITIATOR_NAME,
                                                              "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                              "firstBootTargetPort": "3260",
                                                              "bootTargetName": ENC1BAY5_PROFILE1_BOOT_TARGET_NAME,
                                                              "bootTargetLun": "0",
                                                              "chapLevel": "Chap",
                                                              "chapName": ENC1BAY5_PROFILE1_CHAP_NAME,
                                                              "chapSecret": CHAP_SECRET,
                                                              "mutualChapName": "",
                                                              "mutualChapSecret": None
                                                          }}}
                                                 ]
                                             },
                                             "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                             "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                             "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                             "iscsiInitiatorName": ENC1BAY5_PROFILE1_INITIATOR_NAME,
                                             "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                             }

# Profile2 Two Connections: ENC1 bay5, BL460c Gen9
# User Specified Initiator and Target
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
enc1bay5_profile2_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY5, 'enclosureUri': 'ENC:' + ENC1,
                                     "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                     "macType": "Physical", "wwnType": "Physical", "name": ENC1BAY5_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                     "connectionSettings": {
                                         "connections": [
                                             {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "UserDefined",
                                                  "ipAddress": ENC1BAY5_PROFILE2_INITIATOR_IP_1,
                                                  "subnetMask": INITIATOR_SUBNET_MASK,
                                                  "gateway": ""
                                              },
                                              "boot": {
                                                  "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "bootTargetName": ENC1BAY5_PROFILE2_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                      "firstBootTargetPort": "3260",
                                                      "chapLevel": "Chap",
                                                      "chapName": ENC1BAY5_PROFILE2_CHAP_NAME,
                                                      "chapSecret": CHAP_SECRET,
                                                      "mutualChapName": "",
                                                      "mutualChapSecret": None
                                                  }}},
                                             {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                              "ipv4": {
                                                  "ipAddressSource": "UserDefined",
                                                  "ipAddress": ENC1BAY5_PROFILE2_INITIATOR_IP_2,
                                                  "subnetMask": INITIATOR_SUBNET_MASK,
                                                  "gateway": ""
                                              },
                                                 "boot": {
                                                  "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "bootTargetName": ENC1BAY5_PROFILE2_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                      "firstBootTargetPort": "3260",
                                                      "chapLevel": "Chap",
                                                      "chapName": ENC1BAY5_PROFILE2_CHAP_NAME,
                                                      "chapSecret": CHAP_SECRET,
                                                      "mutualChapName": "",
                                                      "mutualChapSecret": None
                                                  }}}
                                         ]
                                     },
                                     "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                     "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                     "iscsiInitiatorName": ENC1BAY5_PROFILE2_INITIATOR_NAME,
                                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                     }

# Profile2 One Connection Tunnel: ENC1 bay5, BL460c Gen9
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to tunnel network
enc1bay5_profile2_one_connection_tunnel = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY5, 'enclosureUri': 'ENC:' + ENC1,
                                           "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                           "macType": "Physical", "wwnType": "Physical", "name": ENC1BAY5_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                           "connectionSettings": {
                                               "connections": [
                                                   {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                                                    "networkUri": 'ETH:network-tunnel',
                                                    "ipv4": {
                                                        "ipAddressSource": "UserDefined",
                                                        "ipAddress": ENC1BAY5_PROFILE2_INITIATOR_IP_1,
                                                        "subnetMask": INITIATOR_SUBNET_MASK,
                                                        "gateway": ""
                                                    },
                                                       "boot": {
                                                        "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                        "iscsi": {
                                                            "initiatorNameSource": "ProfileInitiatorName",
                                                            "bootTargetName": ENC1BAY5_PROFILE2_BOOT_TARGET_NAME,
                                                            "bootTargetLun": "0",
                                                            "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                            "firstBootTargetPort": "3260",
                                                            "chapLevel": "Chap",
                                                            "chapName": ENC1BAY5_PROFILE2_CHAP_NAME,
                                                            "chapSecret": CHAP_SECRET,
                                                            "mutualChapName": "",
                                                            "mutualChapSecret": None
                                                        }}}
                                               ]
                                           },
                                           "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                           "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                           "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                           "iscsiInitiatorName": ENC1BAY5_PROFILE2_INITIATOR_NAME,
                                           "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                           }

# Profile2 One Connection Untagged: ENC1 bay5, BL460c Gen9
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to Untagged network
enc1bay5_profile2_one_connection_untagged = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY5, 'enclosureUri': 'ENC:' + ENC1,
                                             "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                             "macType": "Physical", "wwnType": "Physical", "name": ENC1BAY5_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                             "connectionSettings": {
                                                 "connections": [
                                                     {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                      "networkUri": 'ETH:network-untagged',
                                                      "ipv4": {
                                                          "ipAddressSource": "UserDefined",
                                                          "ipAddress": ENC1BAY5_PROFILE2_INITIATOR_IP_1,
                                                          "subnetMask": INITIATOR_SUBNET_MASK,
                                                          "gateway": ""
                                                      },
                                                         "boot": {
                                                          "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                          "iscsi": {
                                                              "initiatorNameSource": "ProfileInitiatorName",
                                                              "bootTargetName": ENC1BAY5_PROFILE2_BOOT_TARGET_NAME,
                                                              "bootTargetLun": "0",
                                                              "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                              "firstBootTargetPort": "3260",
                                                              "chapLevel": "Chap",
                                                              "chapName": ENC1BAY5_PROFILE2_CHAP_NAME,
                                                              "chapSecret": CHAP_SECRET,
                                                              "mutualChapName": "",
                                                              "mutualChapSecret": None
                                                          }}}
                                                 ]
                                             },
                                             "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                             "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                             "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                             "iscsiInitiatorName": ENC1BAY5_PROFILE2_INITIATOR_NAME,
                                             "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                             }

# Profile3 Two Connections: ENC1 bay5, BL460c Gen9
# DHCP Initiator
# Managed Volume
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to untagged network
enc1bay5_profile3_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY5, 'enclosureUri': 'ENC:' + ENC1,
                                     "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                     "macType": "Physical", "wwnType": "Physical", "name": ENC1BAY5_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                     "connectionSettings": {
                                         "connections": [
                                             {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                              "boot": {
                                                  "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                                              }},
                                             {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                                 "boot": {
                                                  "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
                                              }}
                                         ]
                                     },
                                     "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                     "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                     "iscsiInitiatorName": ENC1BAY5_PROFILE3_INITIATOR_NAME,
                                     "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                     "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                    "volumeAttachments": [
                                                        {
                                                            "id": 1,
                                                            "isBootVolume": True,
                                                            "lun": None,
                                                            "lunType": "Auto",
                                                            "storagePaths": [
                                                                {
                                                                    "isEnabled": True,
                                                                    "connectionId": "1",
                                                                    "targetSelector": "Auto",
                                                                    "targets": []
                                                                },
                                                                {
                                                                    "isEnabled": True,
                                                                    "connectionId": "2",
                                                                    "targetSelector": "Auto",
                                                                    "targets": []
                                                                },
                                                            ],
                                                            "volume": None,
                                                            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                                                            "volumeUri": 'v:' + ENC1BAY5_VOLUME_NAME,
                                                        }
                                                    ]
                                                    }}


# Profile3 One Connection Untagged: ENC1 bay5, BL460c Gen9
# DHCP Initiator
# Managed volume
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexibleLOM1:1b to Untagged network
enc1bay5_profile3_one_connection_untagged = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY5, 'enclosureUri': 'ENC:' + ENC1,
                                             "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                             "macType": "Physical", "wwnType": "Physical", "name": ENC1BAY5_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                             "connectionSettings": {
                                                 "connections": [
                                                     {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                                      "ipv4": {
                                                          "ipAddressSource": "DHCP",
                                                          "subnetMask": "",
                                                          "gateway": "",
                                                      },
                                                      "boot": {
                                                          "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                                                      }},
                                                 ]
                                             },
                                             "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                             "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                             "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                             "iscsiInitiatorName": ENC1BAY5_PROFILE3_INITIATOR_NAME,
                                             "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                             "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                            "volumeAttachments": [
                                                                {
                                                                    "id": 1,
                                                                    "isBootVolume": True,
                                                                    "lun": None,
                                                                    "lunType": "Auto",
                                                                    "storagePaths": [{
                                                                        "isEnabled": True,
                                                                        "connectionId": "1",
                                                                        "targetSelector": "Auto",
                                                                        "targets": []
                                                                    }],
                                                                    "volume": None,
                                                                    "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                                                                    "volumeUri": 'v:' + ENC1BAY5_VOLUME_NAME,
                                                                }
                                                            ]
                                                            }
                                             }

# Profile1 Two Connections: ENC3 bay7, BL660c Gen9
# DHCP Initiator
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
enc3bay7_profile1_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC3SHBAY7, 'enclosureUri': 'ENC:' + ENC3,
                                     "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                     "macType": "Physical", "wwnType": "Physical", "name": ENC3BAY7_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                     "connectionSettings": {
                                         "connections": [
                                             {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                              "boot": {
                                                  "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                      "firstBootTargetPort": "3260",
                                                      "bootTargetName": ENC3BAY7_PROFILE1_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "chapLevel": None,
                                                      "chapName": "",
                                                      "chapSecret": None,
                                                      "mutualChapName": "",
                                                      "mutualChapSecret": None
                                                  }}},
                                             {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                                 "boot": {
                                                  "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "bootTargetName": ENC3BAY7_PROFILE1_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "chapLevel": None,
                                                      "chapName": "",
                                                      "chapSecret": None,
                                                      "mutualChapName": "",
                                                      "mutualChapSecret": None
                                                  }}}
                                         ]
                                     },
                                     "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                     "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                     "iscsiInitiatorName": ENC3BAY7_PROFILE1_INITIATOR_NAME,
                                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                     }


# Profile1 One Connection Tunnel: ENC3 bay7, BL660c Gen9
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Flb1:1b to tunnel network
enc3bay7_profile1_one_connection_tunnel = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC3SHBAY7, 'enclosureUri': 'ENC:' + ENC3,
                                           "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                           "macType": "Physical", "wwnType": "Physical", "name": ENC3BAY7_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                           "connectionSettings": {
                                               "connections": [
                                                   {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                    "networkUri": 'ETH:network-tunnel',
                                                    "ipv4": {
                                                        "ipAddressSource": "DHCP",
                                                        "subnetMask": "",
                                                        "gateway": "",
                                                    },
                                                       "boot": {
                                                        "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                        "iscsi": {
                                                            "initiatorNameSource": "UserDefined",
                                                            "initiatorName": ENC3BAY7_PROFILE1_INITIATOR_NAME,
                                                            "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                            "firstBootTargetPort": "3260",
                                                            "bootTargetName": ENC3BAY7_PROFILE1_BOOT_TARGET_NAME,
                                                            "bootTargetLun": "0",
                                                            "chapLevel": None,
                                                            "chapName": "",
                                                            "chapSecret": None,
                                                            "mutualChapName": "",
                                                            "mutualChapSecret": None
                                                        }}}
                                               ]
                                           },
                                           "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                           "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                           "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                           "iscsiInitiatorName": ENC3BAY7_PROFILE1_INITIATOR_NAME,
                                           "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                           }


# Profile1 One Connection Untagged: ENC3 bay7, BL660c Gen9
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Flb1:1b to Untagged network
enc3bay7_profile1_one_connection_untagged = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC3SHBAY7, 'enclosureUri': 'ENC:' + ENC3,
                                             "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                             "macType": "Physical", "wwnType": "Physical", "name": ENC3BAY7_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                             "connectionSettings": {
                                                 "connections": [
                                                     {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                      "networkUri": 'ETH:network-untagged',
                                                      "ipv4": {
                                                          "ipAddressSource": "DHCP",
                                                          "subnetMask": "",
                                                          "gateway": "",
                                                      },
                                                         "boot": {
                                                          "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                          "iscsi": {
                                                              "initiatorNameSource": "UserDefined",
                                                              "initiatorName": ENC3BAY7_PROFILE1_INITIATOR_NAME,
                                                              "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                              "firstBootTargetPort": "3260",
                                                              "bootTargetName": ENC3BAY7_PROFILE1_BOOT_TARGET_NAME,
                                                              "bootTargetLun": "0",
                                                              "chapLevel": None,
                                                              "chapName": "",
                                                              "chapSecret": None,
                                                              "mutualChapName": "",
                                                              "mutualChapSecret": None
                                                          }}}
                                                 ]
                                             },
                                             "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                             "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                             "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                             "iscsiInitiatorName": ENC3BAY7_PROFILE1_INITIATOR_NAME,
                                             "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                             }

# Profile2 Two Connections: ENC3 bay7, BL660c Gen9
# User Specified Initiator and Target
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
enc3bay7_profile2_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC3SHBAY7, 'enclosureUri': 'ENC:' + ENC3,
                                     "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                     "macType": "Physical", "wwnType": "Physical", "name": ENC3BAY7_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                     "connectionSettings": {
                                         "connections": [
                                             {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "UserDefined",
                                                  "ipAddress": ENC3BAY7_PROFILE2_INITIATOR_IP_1,
                                                  "subnetMask": INITIATOR_SUBNET_MASK,
                                                  "gateway": ""
                                              },
                                              "boot": {
                                                  "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "bootTargetName": ENC3BAY7_PROFILE2_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                      "firstBootTargetPort": "3260",
                                                      "chapLevel": "MutualChap",
                                                      "chapName": ENC3BAY7_PROFILE2_CHAP_NAME,
                                                      "chapSecret": CHAP_SECRET,
                                                      "mutualChapName": ENC3BAY7_PROFILE2_MCHAP_NAME,
                                                      "mutualChapSecret": MCHAP_SECRET
                                                  }}},
                                             {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                              "ipv4": {
                                                  "ipAddressSource": "UserDefined",
                                                  "ipAddress": ENC3BAY7_PROFILE2_INITIATOR_IP_2,
                                                  "subnetMask": INITIATOR_SUBNET_MASK,
                                                  "gateway": ""
                                              },
                                                 "boot": {
                                                  "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "bootTargetName": ENC3BAY7_PROFILE2_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                      "firstBootTargetPort": "3260",
                                                      "chapLevel": "MutualChap",
                                                      "chapName": ENC3BAY7_PROFILE2_CHAP_NAME,
                                                      "chapSecret": CHAP_SECRET,
                                                      "mutualChapName": ENC3BAY7_PROFILE2_MCHAP_NAME,
                                                      "mutualChapSecret": MCHAP_SECRET
                                                  }}}
                                         ]
                                     },
                                     "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                     "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                     "iscsiInitiatorName": ENC3BAY7_PROFILE2_INITIATOR_NAME,
                                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                     }

# Profile2 One Connection Tunnel: ENC3 bay7, BL660c Gen9
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Flb1:1b to tunnel network
enc3bay7_profile2_one_connection_tunnel = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC3SHBAY7, 'enclosureUri': 'ENC:' + ENC3,
                                           "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                           "macType": "Physical", "wwnType": "Physical", "name": ENC3BAY7_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                           "connectionSettings": {
                                               "connections": [
                                                   {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                    "networkUri": 'ETH:network-tunnel',
                                                    "ipv4": {
                                                        "ipAddressSource": "UserDefined",
                                                        "ipAddress": ENC3BAY7_PROFILE2_INITIATOR_IP_1,
                                                        "subnetMask": INITIATOR_SUBNET_MASK,
                                                        "gateway": ""
                                                    },
                                                       "boot": {
                                                        "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                        "iscsi": {
                                                            "initiatorNameSource": "ProfileInitiatorName",
                                                            "bootTargetName": ENC3BAY7_PROFILE2_BOOT_TARGET_NAME,
                                                            "bootTargetLun": "0",
                                                            "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                            "firstBootTargetPort": "3260",
                                                            "chapLevel": "MutualChap",
                                                            "chapName": ENC3BAY7_PROFILE2_CHAP_NAME,
                                                            "chapSecret": CHAP_SECRET,
                                                            "mutualChapName": ENC3BAY7_PROFILE2_MCHAP_NAME,
                                                            "mutualChapSecret": MCHAP_SECRET
                                                        }}}
                                               ]
                                           },
                                           "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                           "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                           "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                           "iscsiInitiatorName": ENC3BAY7_PROFILE2_INITIATOR_NAME,
                                           "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                           }

# Profile2 One Connection Untagged: ENC3 bay7, BL660c Gen9
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Flb1:1b to Untagged network
enc3bay7_profile2_one_connection_untagged = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC3SHBAY7, 'enclosureUri': 'ENC:' + ENC3,
                                             "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                             "macType": "Physical", "wwnType": "Physical", "name": ENC3BAY7_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                             "connectionSettings": {
                                                 "connections": [
                                                     {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                      "networkUri": 'ETH:network-untagged',
                                                      "ipv4": {
                                                          "ipAddressSource": "UserDefined",
                                                          "ipAddress": ENC3BAY7_PROFILE2_INITIATOR_IP_1,
                                                          "subnetMask": INITIATOR_SUBNET_MASK,
                                                          "gateway": ""
                                                      },
                                                         "boot": {
                                                          "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                          "iscsi": {
                                                              "initiatorNameSource": "ProfileInitiatorName",
                                                              "bootTargetName": ENC3BAY7_PROFILE2_BOOT_TARGET_NAME,
                                                              "bootTargetLun": "0",
                                                              "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                              "firstBootTargetPort": "3260",
                                                              "chapLevel": "MutualChap",
                                                              "chapName": ENC3BAY7_PROFILE2_CHAP_NAME,
                                                              "chapSecret": CHAP_SECRET,
                                                              "mutualChapName": ENC3BAY7_PROFILE2_MCHAP_NAME,
                                                              "mutualChapSecret": MCHAP_SECRET
                                                          }}}
                                                 ]
                                             },
                                             "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                             "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                             "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                             "iscsiInitiatorName": ENC3BAY7_PROFILE2_INITIATOR_NAME,
                                             "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                             }

# Profile3 Two Connections: ENC3 bay7, BL660c Gen9
# DHCP Initiator
# Managed Volume
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to untagged network
enc3bay7_profile3_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC3SHBAY7, 'enclosureUri': 'ENC:' + ENC3,
                                     "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                     "macType": "Physical", "wwnType": "Physical", "name": ENC3BAY7_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                     "connectionSettings": {
                                         "connections": [
                                             {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                              "boot": {
                                                  "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                                              }},
                                             {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                                 "boot": {
                                                  "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
                                              }}
                                         ]
                                     },
                                     "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                     "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                     "iscsiInitiatorName": ENC3BAY7_PROFILE3_INITIATOR_NAME,
                                     "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                     "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                    "volumeAttachments": [
                                                        {
                                                            "id": 1,
                                                            "isBootVolume": True,
                                                            "lunType": "Auto",
                                                            "storagePaths": [{
                                                                "isEnabled": True,
                                                                "connectionId": 1,
                                                                "targetSelector": "Auto",
                                                                "targets": []
                                                            }, {
                                                                "isEnabled": True,
                                                                "connectionId": 2,
                                                                "targetSelector": "Auto",
                                                                "targets": []
                                                            }],
                                                            "volume": None,
                                                            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                                                            "volumeUri": 'v:' + ENC3BAY7_VOLUME_NAME,
                                                        }
                                                    ]
                                                    }
                                     }


# Profile3 One Connection Untagged: ENC3 bay7, BL660c Gen9
# DHCP Initiator
# Managed volume
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexibleLOM1:1b to Untagged network
enc3bay7_profile3_one_connection_untagged = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC3SHBAY7, 'enclosureUri': 'ENC:' + ENC3,
                                             "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                             "macType": "Physical", "wwnType": "Physical", "name": ENC3BAY7_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                             "connectionSettings": {
                                                 "connections": [
                                                     {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                                      "ipv4": {
                                                          "ipAddressSource": "DHCP",
                                                          "subnetMask": "",
                                                          "gateway": "",
                                                      },
                                                      "boot": {
                                                          "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                                                      }},
                                                 ]
                                             },
                                             "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                             "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                             "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                             "iscsiInitiatorName": ENC3BAY7_PROFILE3_INITIATOR_NAME,
                                             "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                             "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                            "volumeAttachments": [
                                                                {
                                                                    "id": 1,
                                                                    "isBootVolume": True,
                                                                    "lunType": "Auto",
                                                                    "storagePaths": [{
                                                                        "isEnabled": True,
                                                                        "connectionId": 1,
                                                                        "targetSelector": "Auto",
                                                                    }],
                                                                    "volume": None,
                                                                    "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                                                                    "volumeUri": "v:" + ENC3BAY7_VOLUME_NAME,
                                                                }
                                                            ]
                                                            }
                                             }


# Profile1 Two Connections: ENC3 bay8, BL660c Gen8
# DHCP Initiator
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
enc3bay8_profile1_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC3SHBAY8, 'enclosureUri': 'ENC:' + ENC3,
                                     "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                     "macType": "Physical", "wwnType": "Physical", "name": ENC3BAY8_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                     "connectionSettings": {
                                         "connections": [
                                             {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                              "boot": {
                                                  "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                      "firstBootTargetPort": "3260",
                                                      "bootTargetName": ENC3BAY8_PROFILE1_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "chapLevel": "Chap",
                                                      "chapName": ENC3BAY8_PROFILE1_CHAP_NAME,
                                                      "chapSecret": CHAP_SECRET,
                                                      "mutualChapName": ENC3BAY8_PROFILE1_MCHAP_NAME,
                                                      "mutualChapSecret": MCHAP_SECRET
                                                  }}},
                                             {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Mezz 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                                 "boot": {
                                                  "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                      "bootTargetName": ENC3BAY8_PROFILE1_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "chapLevel": "MutualChap",
                                                      "chapName": ENC3BAY8_PROFILE1_CHAP_NAME,
                                                      "chapSecret": CHAP_SECRET,
                                                      "mutualChapName": ENC3BAY8_PROFILE1_MCHAP_NAME,
                                                      "mutualChapSecret": MCHAP_SECRET
                                                  }}}
                                         ]
                                     },
                                     "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                     "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                     "iscsiInitiatorName": ENC3BAY8_PROFILE1_INITIATOR_NAME,
                                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                     }


# Profile1 One Connection Tunnel: ENC3 bay8, BL660c Gen8
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to tunnel network
enc3bay8_profile1_one_connection_tunnel = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC3SHBAY8, 'enclosureUri': 'ENC:' + ENC3,
                                           "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                           "macType": "Physical", "wwnType": "Physical", "name": ENC3BAY8_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                           "connectionSettings": {
                                               "connections": [
                                                   {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                    "networkUri": 'ETH:network-tunnel',
                                                    "ipv4": {
                                                        "ipAddressSource": "DHCP",
                                                        "subnetMask": "",
                                                        "gateway": "",
                                                    },
                                                       "boot": {
                                                        "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                        "iscsi": {
                                                            "initiatorNameSource": "UserDefined",
                                                            "initiatorName": ENC3BAY8_PROFILE1_INITIATOR_NAME,
                                                            "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                            "firstBootTargetPort": "3260",
                                                            "bootTargetName": ENC3BAY8_PROFILE1_BOOT_TARGET_NAME,
                                                            "bootTargetLun": "0",
                                                            "chapLevel": "MutualChap",
                                                            "chapName": ENC3BAY8_PROFILE1_CHAP_NAME,
                                                            "chapSecret": CHAP_SECRET,
                                                            "mutualChapName": ENC3BAY8_PROFILE1_MCHAP_NAME,
                                                            "mutualChapSecret": MCHAP_SECRET
                                                        }}}
                                               ]
                                           },
                                           "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                           "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                           "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                           "iscsiInitiatorName": ENC3BAY8_PROFILE1_INITIATOR_NAME,
                                           "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                           }


# Profile1 One Connection Untagged: ENC3 bay8, BL660c Gen8
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to Untagged network
enc3bay8_profile1_one_connection_untagged = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC3SHBAY8, 'enclosureUri': 'ENC:' + ENC3,
                                             "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                             "macType": "Physical", "wwnType": "Physical", "name": ENC3BAY8_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                             "connectionSettings": {
                                                 "connections": [
                                                     {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                      "networkUri": 'ETH:network-untagged',
                                                      "ipv4": {
                                                          "ipAddressSource": "DHCP",
                                                          "subnetMask": "",
                                                          "gateway": "",
                                                      },
                                                         "boot": {
                                                          "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                          "iscsi": {
                                                              "initiatorNameSource": "UserDefined",
                                                              "initiatorName": ENC3BAY8_PROFILE1_INITIATOR_NAME,
                                                              "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                              "firstBootTargetPort": "3260",
                                                              "bootTargetName": ENC3BAY8_PROFILE1_BOOT_TARGET_NAME,
                                                              "bootTargetLun": "0",
                                                              "chapLevel": "MutualChap",
                                                              "chapName": ENC3BAY8_PROFILE1_CHAP_NAME,
                                                              "chapSecret": CHAP_SECRET,
                                                              "mutualChapName": ENC3BAY8_PROFILE1_MCHAP_NAME,
                                                              "mutualChapSecret": MCHAP_SECRET
                                                          }}}
                                                 ]
                                             },
                                             "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                             "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                             "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                             "iscsiInitiatorName": ENC3BAY8_PROFILE1_INITIATOR_NAME,
                                             "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                             }

# Profile2 Two Connections: ENC3 bay8, BL660c Gen8
# User Specified Initiator and Target
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
enc3bay8_profile2_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC3SHBAY8, 'enclosureUri': 'ENC:' + ENC3,
                                     "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                     "macType": "Physical", "wwnType": "Physical", "name": ENC3BAY8_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                     "connectionSettings": {
                                         "connections": [
                                             {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "UserDefined",
                                                  "ipAddress": ENC3BAY8_PROFILE2_INITIATOR_IP_1,
                                                  "subnetMask": INITIATOR_SUBNET_MASK,
                                                  "gateway": ""
                                              },
                                              "boot": {
                                                  "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "bootTargetName": ENC3BAY8_PROFILE2_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                      "firstBootTargetPort": "3260",
                                                      "chapLevel": "Chap",
                                                      "chapName": ENC3BAY8_PROFILE2_CHAP_NAME,
                                                      "chapSecret": CHAP_SECRET,
                                                      "mutualChapName": "",
                                                      "mutualChapSecret": None
                                                  }}},
                                             {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Mezz 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                              "ipv4": {
                                                  "ipAddressSource": "UserDefined",
                                                  "ipAddress": ENC3BAY8_PROFILE2_INITIATOR_IP_2,
                                                  "subnetMask": INITIATOR_SUBNET_MASK,
                                                  "gateway": ""
                                              },
                                                 "boot": {
                                                  "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "bootTargetName": ENC3BAY8_PROFILE2_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                      "firstBootTargetPort": "3260",
                                                      "chapLevel": "Chap",
                                                      "chapName": ENC3BAY8_PROFILE2_CHAP_NAME,
                                                      "chapSecret": CHAP_SECRET,
                                                      "mutualChapName": "",
                                                      "mutualChapSecret": None
                                                  }}}
                                         ]
                                     },
                                     "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                     "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                     "iscsiInitiatorName": ENC3BAY8_PROFILE2_INITIATOR_NAME,
                                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                     }

# Profile2 One Connection Tunnel: ENC3 bay8, BL660c Gen8
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to tunnel network
enc3bay8_profile2_one_connection_tunnel = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC3SHBAY8, 'enclosureUri': 'ENC:' + ENC3,
                                           "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                           "macType": "Physical", "wwnType": "Physical", "name": ENC3BAY8_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                           "connectionSettings": {
                                               "connections": [
                                                   {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                    "networkUri": 'ETH:network-tunnel',
                                                    "ipv4": {
                                                        "ipAddressSource": "UserDefined",
                                                        "ipAddress": ENC3BAY8_PROFILE2_INITIATOR_IP_1,
                                                        "subnetMask": INITIATOR_SUBNET_MASK,
                                                        "gateway": ""
                                                    },
                                                       "boot": {
                                                        "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                        "iscsi": {
                                                            "initiatorNameSource": "ProfileInitiatorName",
                                                            "bootTargetName": ENC3BAY8_PROFILE2_BOOT_TARGET_NAME,
                                                            "bootTargetLun": "0",
                                                            "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                            "firstBootTargetPort": "3260",
                                                            "chapLevel": "Chap",
                                                            "chapName": ENC3BAY8_PROFILE2_CHAP_NAME,
                                                            "chapSecret": CHAP_SECRET,
                                                            "mutualChapName": "",
                                                            "mutualChapSecret": None
                                                        }}}
                                               ]
                                           },
                                           "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                           "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                           "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                           "iscsiInitiatorName": ENC3BAY8_PROFILE2_INITIATOR_NAME,
                                           "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                           }

# Profile2 One Connection Untagged: ENC3 bay8, BL660c Gen8
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to Untagged network
enc3bay8_profile2_one_connection_untagged = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC3SHBAY8, 'enclosureUri': 'ENC:' + ENC3,
                                             "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                             "macType": "Physical", "wwnType": "Physical", "name": ENC3BAY8_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                             "connectionSettings": {
                                                 "connections": [
                                                     {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                      "networkUri": 'ETH:network-untagged',
                                                      "ipv4": {
                                                          "ipAddressSource": "UserDefined",
                                                          "ipAddress": ENC3BAY8_PROFILE2_INITIATOR_IP_1,
                                                          "subnetMask": INITIATOR_SUBNET_MASK,
                                                          "gateway": ""
                                                      },
                                                         "boot": {
                                                          "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                          "iscsi": {
                                                              "initiatorNameSource": "ProfileInitiatorName",
                                                              "bootTargetName": ENC3BAY8_PROFILE2_BOOT_TARGET_NAME,
                                                              "bootTargetLun": "0",
                                                              "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                              "firstBootTargetPort": "3260",
                                                              "chapLevel": "Chap",
                                                              "chapName": ENC3BAY8_PROFILE2_CHAP_NAME,
                                                              "chapSecret": CHAP_SECRET,
                                                              "mutualChapName": "",
                                                              "mutualChapSecret": None
                                                          }}}
                                                 ]
                                             },
                                             "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                             "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                             "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                             "iscsiInitiatorName": ENC3BAY8_PROFILE2_INITIATOR_NAME,
                                             "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                             }

# Profile3 Two Connections: ENC3 bay8, BL660c Gen8
# DHCP Initiator
# Managed Volume
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to untagged network
enc3bay8_profile3_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC3SHBAY8, 'enclosureUri': 'ENC:' + ENC3,
                                     "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                     "macType": "Physical", "wwnType": "Physical", "name": ENC3BAY8_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                     "connectionSettings": {
                                         "connections": [
                                             {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                              "boot": {
                                                  "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                                              }},
                                             {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Mezz 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                                 "boot": {
                                                  "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
                                              }}
                                         ]
                                     },
                                     "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                     "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                     "iscsiInitiatorName": ENC3BAY8_PROFILE3_INITIATOR_NAME,
                                     "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                     "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                    "volumeAttachments": [
                                                        {
                                                            "id": 1,
                                                            "isBootVolume": True,
                                                            "lunType": "Auto",
                                                            "storagePaths": [{
                                                                "isEnabled": True,
                                                                "connectionId": 1,
                                                                "targetSelector": "Auto",
                                                                "targets": []
                                                            }, {
                                                                "isEnabled": True,
                                                                "connectionId": 2,
                                                                "targetSelector": "Auto",
                                                                "targets": []
                                                            }],
                                                            "volume": None,
                                                            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                                                            "volumeUri": 'v:' + ENC3BAY8_VOLUME_NAME,
                                                        }
                                                    ]
                                                    }
                                     }


# Profile3 One Connection Untagged: ENC3 bay8, BL660c Gen8
# DHCP Initiator
# Managed volume
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexibleLOM1:1b to Untagged network
enc3bay8_profile3_one_connection_untagged = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC3SHBAY8, 'enclosureUri': 'ENC:' + ENC3,
                                             "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                             "macType": "Physical", "wwnType": "Physical", "name": ENC3BAY8_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                             "connectionSettings": {
                                                 "connections": [
                                                     {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                                      "ipv4": {
                                                          "ipAddressSource": "DHCP",
                                                          "subnetMask": "",
                                                          "gateway": "",
                                                      },
                                                      "boot": {
                                                          "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                                                      }},
                                                 ]
                                             },
                                             "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                             "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                             "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                             "iscsiInitiatorName": ENC3BAY8_PROFILE3_INITIATOR_NAME,
                                             "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                             "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                            "volumeAttachments": [
                                                                {
                                                                    "id": 1,
                                                                    "isBootVolume": True,
                                                                    "lunType": "Auto",
                                                                    "storagePaths": [{
                                                                        "isEnabled": True,
                                                                        "connectionId": 1,
                                                                        "targetSelector": "Auto",
                                                                        "targets": []
                                                                    }],
                                                                    "volume": None,
                                                                    "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                                                                    "volumeUri": 'v:' + ENC3BAY8_VOLUME_NAME,
                                                                }
                                                            ]
                                                            }
                                             }


# Profile1 Two Connections: ENC2 bay1
# DHCP Initiator
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
enc2bay1_profile1_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC2SHBAY1, 'enclosureUri': 'ENC:' + ENC2,
                                     "enclosureGroupUri": "EG:" + EG2_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                     "macType": "Physical", "wwnType": "Physical", "name": ENC2BAY1_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                     "connectionSettings": {
                                         "connections": [
                                             {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                              "boot": {
                                                  "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                      "firstBootTargetPort": "3260",
                                                      "bootTargetName": ENC2BAY1_PROFILE1_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "chapLevel": "Chap",
                                                      "chapName": ENC2BAY1_PROFILE1_CHAP_NAME,
                                                      "chapSecret": CHAP_SECRET,
                                                      "mutualChapName": "",
                                                      "mutualChapSecret": None
                                                  }}},
                                             {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                                 "boot": {
                                                  "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                      "firstBootTargetPort": "3260",
                                                      "bootTargetName": ENC2BAY1_PROFILE1_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "chapLevel": "Chap",
                                                      "chapName": ENC2BAY1_PROFILE1_CHAP_NAME,
                                                      "chapSecret": CHAP_SECRET,
                                                      "mutualChapName": "",
                                                      "mutualChapSecret": None
                                                  }}}
                                         ]
                                     },
                                     "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                     "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                     "iscsiInitiatorName": ENC2BAY1_PROFILE1_INITIATOR_NAME,
                                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                     }


# Profile1 One Connection Tunnel: ENC2 bay1
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Flb1:1b to tunnel network
enc2bay1_profile1_one_connection_tunnel = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC2SHBAY1, 'enclosureUri': 'ENC:' + ENC2,
                                           "enclosureGroupUri": "EG:" + EG2_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                           "macType": "Physical", "wwnType": "Physical", "name": ENC2BAY1_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                           "connectionSettings": {
                                               "connections": [
                                                   {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                    "networkUri": 'ETH:network-tunnel',
                                                    "ipv4": {
                                                        "ipAddressSource": "DHCP",
                                                        "subnetMask": "",
                                                        "gateway": "",
                                                    },
                                                       "boot": {
                                                        "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                        "iscsi": {
                                                            "initiatorNameSource": "UserDefined",
                                                            "initiatorName": ENC2BAY1_PROFILE1_INITIATOR_NAME,
                                                            "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                            "firstBootTargetPort": "3260",
                                                            "bootTargetName": ENC2BAY1_PROFILE1_BOOT_TARGET_NAME,
                                                            "bootTargetLun": "0",
                                                            "chapLevel": "Chap",
                                                            "chapName": ENC2BAY1_PROFILE1_CHAP_NAME,
                                                            "chapSecret": CHAP_SECRET,
                                                            "mutualChapName": "",
                                                            "mutualChapSecret": None
                                                        }}}
                                               ]
                                           },
                                           "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                           "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                           "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                           "iscsiInitiatorName": ENC2BAY1_PROFILE1_INITIATOR_NAME,
                                           "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                           }


# Profile1 One Connection Untagged: ENC2 bay1
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Flb1:1b to Untagged network
enc2bay1_profile1_one_connection_untagged = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC2SHBAY1, 'enclosureUri': 'ENC:' + ENC2,
                                             "enclosureGroupUri": "EG:" + EG2_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                             "macType": "Physical", "wwnType": "Physical", "name": ENC2BAY1_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                             "connectionSettings": {
                                                 "connections": [
                                                     {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                      "networkUri": 'ETH:network-untagged',
                                                      "ipv4": {
                                                          "ipAddressSource": "DHCP",
                                                          "subnetMask": "",
                                                          "gateway": "",
                                                      },
                                                         "boot": {
                                                          "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                          "iscsi": {
                                                              "initiatorNameSource": "UserDefined",
                                                              "initiatorName": ENC2BAY1_PROFILE1_INITIATOR_NAME,
                                                              "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                              "firstBootTargetPort": "3260",
                                                              "bootTargetName": ENC2BAY1_PROFILE1_BOOT_TARGET_NAME,
                                                              "bootTargetLun": "0",
                                                              "chapLevel": "Chap",
                                                              "chapName": ENC2BAY1_PROFILE1_CHAP_NAME,
                                                              "chapSecret": CHAP_SECRET,
                                                              "mutualChapName": "",
                                                              "mutualChapSecret": None
                                                          }}}
                                                 ]
                                             },
                                             "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                             "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                             "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                             "iscsiInitiatorName": ENC2BAY1_PROFILE1_INITIATOR_NAME,
                                             "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                             }

# Profile2 Two Connections: ENC2 bay1
# User Specified Initiator and Target
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
enc2bay1_profile2_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC2SHBAY1, 'enclosureUri': 'ENC:' + ENC2,
                                     "enclosureGroupUri": "EG:" + EG2_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                     "macType": "Physical", "wwnType": "Physical", "name": ENC2BAY1_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                     "connectionSettings": {
                                         "connections": [
                                             {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "UserDefined",
                                                  "ipAddress": ENC2BAY1_PROFILE2_INITIATOR_IP_1,
                                                  "subnetMask": INITIATOR_SUBNET_MASK,
                                                  "gateway": ""
                                              },
                                              "boot": {
                                                  "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "bootTargetName": ENC2BAY1_PROFILE2_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                      "firstBootTargetPort": "3260",
                                                      "chapLevel": None,
                                                      "chapName": "",
                                                      "chapSecret": None,
                                                      "mutualChapName": "",
                                                      "mutualChapSecret": None
                                                  }}},
                                             {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                              "ipv4": {
                                                  "ipAddressSource": "UserDefined",
                                                  "ipAddress": ENC2BAY1_PROFILE2_INITIATOR_IP_2,
                                                  "subnetMask": INITIATOR_SUBNET_MASK,
                                                  "gateway": ""
                                              },
                                                 "boot": {
                                                  "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "bootTargetName": ENC2BAY1_PROFILE2_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                      "firstBootTargetPort": "3260",
                                                      "chapLevel": None,
                                                      "chapName": "",
                                                      "chapSecret": None,
                                                      "mutualChapName": "",
                                                      "mutualChapSecret": None
                                                  }}}
                                         ]
                                     },
                                     "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                     "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                     "iscsiInitiatorName": ENC2BAY1_PROFILE2_INITIATOR_NAME,
                                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                     }

# Profile2 One Connection Tunnel: ENC2 bay1
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Flb1:1b to tunnel network
enc2bay1_profile2_one_connection_tunnel = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC2SHBAY1, 'enclosureUri': 'ENC:' + ENC2,
                                           "enclosureGroupUri": "EG:" + EG2_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                           "macType": "Physical", "wwnType": "Physical", "name": ENC2BAY1_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                           "connectionSettings": {
                                               "connections": [
                                                   {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                    "networkUri": 'ETH:network-tunnel',
                                                    "ipv4": {
                                                        "ipAddressSource": "UserDefined",
                                                        "ipAddress": ENC2BAY1_PROFILE2_INITIATOR_IP_1,
                                                        "subnetMask": INITIATOR_SUBNET_MASK,
                                                        "gateway": ""
                                                    },
                                                       "boot": {
                                                        "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                        "iscsi": {
                                                            "initiatorNameSource": "ProfileInitiatorName",
                                                            "bootTargetName": ENC2BAY1_PROFILE2_BOOT_TARGET_NAME,
                                                            "bootTargetLun": "0",
                                                            "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                            "firstBootTargetPort": "3260",
                                                            "chapLevel": None,
                                                            "chapName": "",
                                                            "chapSecret": None,
                                                            "mutualChapName": "",
                                                            "mutualChapSecret": None
                                                        }}}
                                               ]
                                           },
                                           "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                           "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                           "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                           "iscsiInitiatorName": ENC2BAY1_PROFILE2_INITIATOR_NAME,
                                           "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                           }

# Profile2 One Connection Untagged: ENC2 bay1
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Flb1:1b to Untagged network
enc2bay1_profile2_one_connection_untagged = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC2SHBAY1, 'enclosureUri': 'ENC:' + ENC2,
                                             "enclosureGroupUri": "EG:" + EG2_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                             "macType": "Physical", "wwnType": "Physical", "name": ENC2BAY1_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                             "connectionSettings": {
                                                 "connections": [
                                                     {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                      "networkUri": 'ETH:network-untagged',
                                                      "ipv4": {
                                                          "ipAddressSource": "UserDefined",
                                                          "ipAddress": ENC2BAY1_PROFILE2_INITIATOR_IP_1,
                                                          "subnetMask": INITIATOR_SUBNET_MASK,
                                                          "gateway": ""
                                                      },
                                                         "boot": {
                                                          "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                          "iscsi": {
                                                              "initiatorNameSource": "ProfileInitiatorName",
                                                              "bootTargetName": ENC2BAY1_PROFILE2_BOOT_TARGET_NAME,
                                                              "bootTargetLun": "0",
                                                              "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                              "firstBootTargetPort": "3260",
                                                              "chapLevel": None,
                                                              "chapName": "",
                                                              "chapSecret": None,
                                                              "mutualChapName": "",
                                                              "mutualChapSecret": None
                                                          }}}
                                                 ]
                                             },
                                             "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                             "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                             "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                             "iscsiInitiatorName": ENC2BAY1_PROFILE2_INITIATOR_NAME,
                                             "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                             }

# Profile3 Two Connections: ENC2 bay1
# DHCP Initiator
# Managed Volume
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to untagged network
enc2bay1_profile3_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC2SHBAY1, 'enclosureUri': 'ENC:' + ENC2,
                                     "enclosureGroupUri": "EG:" + EG2_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                     "macType": "Physical", "wwnType": "Physical", "name": ENC2BAY1_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                     "connectionSettings": {
                                         "connections": [
                                             {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                              "boot": {
                                                  "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                                              }},
                                             {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                                 "boot": {
                                                  "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
                                              }}
                                         ]
                                     },
                                     "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                     "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                     "iscsiInitiatorName": ENC2BAY1_PROFILE3_INITIATOR_NAME,
                                     "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                     "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                    "volumeAttachments": [
                                                        {
                                                            "id": 1,
                                                            "isBootVolume": True,
                                                            "lunType": "Auto",
                                                            "storagePaths": [{
                                                                "isEnabled": True,
                                                                "connectionId": 1,
                                                                "targetSelector": "Auto",
                                                                "targets": []
                                                            }, {
                                                                "isEnabled": True,
                                                                "connectionId": 2,
                                                                "targetSelector": "Auto",
                                                                "targets": []
                                                            }],
                                                            "volume": None,
                                                            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                                                            "volumeUri": 'v:' + ENC2BAY1_VOLUME_NAME,
                                                        }
                                                    ]
                                                    }
                                     }


# Profile3 One Connection Untagged: ENC2 bay1
# DHCP Initiator
# Managed volume
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexibleLOM1:1b to Untagged network
enc2bay1_profile3_one_connection_untagged = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC2SHBAY1, 'enclosureUri': 'ENC:' + ENC2,
                                             "enclosureGroupUri": "EG:" + EG2_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                             "macType": "Physical", "wwnType": "Physical", "name": ENC2BAY1_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                             "connectionSettings": {
                                                 "connections": [
                                                     {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                                      "ipv4": {
                                                          "ipAddressSource": "DHCP",
                                                          "subnetMask": "",
                                                          "gateway": "",
                                                      },
                                                      "boot": {
                                                          "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                                                      }},
                                                 ]
                                             },
                                             "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                             "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                             "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                             "iscsiInitiatorName": ENC2BAY1_PROFILE3_INITIATOR_NAME,
                                             "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                             "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                            "volumeAttachments": [
                                                                {
                                                                    "id": 1,
                                                                    "isBootVolume": True,
                                                                    "lunType": "Auto",
                                                                    "storagePaths": [{
                                                                        "isEnabled": True,
                                                                        "connectionId": 1,
                                                                        "targetSelector": "Auto",
                                                                        "targets": []
                                                                    }],
                                                                    "volume": None,
                                                                    "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                                                                    "volumeUri": 'v:' + ENC2BAY1_VOLUME_NAME,
                                                                }
                                                            ]
                                                            }
                                             }

# Gen10 Profile1 Two Connections: ENC1 bay14, BL460c Gen10
# DHCP Initiator
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
enc1bay14_profile1_two_connections = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY14, 'enclosureUri': 'ENC:' + ENC1,
                                      "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                      "macType": "Physical", "wwnType": "Physical", "name": ENC1BAY14_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                      "connectionSettings": {
                                          "connections": [
                                              {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                               "ipv4": {
                                                   "ipAddressSource": "DHCP",
                                                   "subnetMask": "",
                                                   "gateway": "",
                                               },
                                                  "boot": {
                                                   "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                      "firstBootTargetPort": "3260",
                                                      "bootTargetName": ENC3BAY7_PROFILE1_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "chapLevel": None,
                                                      "chapName": "",
                                                      "chapSecret": None,
                                                      "mutualChapName": "",
                                                      "mutualChapSecret": None
                                                  }}},
                                              {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                               "ipv4": {
                                                   "ipAddressSource": "DHCP",
                                                   "subnetMask": "",
                                                   "gateway": "",
                                               },
                                                  "boot": {
                                                   "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                                   "iscsi": {
                                                       "initiatorNameSource": "ProfileInitiatorName",
                                                       "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                       "firstBootTargetPort": "3260",
                                                       "bootTargetName": ENC3BAY7_PROFILE1_BOOT_TARGET_NAME,
                                                       "bootTargetLun": "0",
                                                       "chapLevel": None,
                                                       "chapName": "",
                                                       "chapSecret": None,
                                                       "mutualChapName": "",
                                                       "mutualChapSecret": None
                                                   }}}
                                          ]
                                      },
                                      "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                      "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                      "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                      "iscsiInitiatorName": ENC1BAY14_PROFILE1_INITIATOR_NAME,
                                      "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                      }

# Gen10 Profile2 One Connection Tunnel: ENC3 bay7, BL660c Gen9
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Flb1:1b to tunnel network
enc1bay16_profile1_one_connection_untagged = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY16, 'enclosureUri': 'ENC:' + ENC1,
                                              "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                              "macType": "Physical", "wwnType": "Physical", "name": ENC1BAY16_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                              "connectionSettings": {
                                                  "connections": [
                                                      {"id": 1, "name": "iSCSI", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                       "networkUri": 'ETH:network-untagged',
                                                       "ipv4": {},
                                                       }
                                                  ]
                                              },
                                              "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                              "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                              "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                              "iscsiInitiatorName": ENC1BAY16_PROFILE1_INITIATOR_NAME,
                                              "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                              "sanStorage": {'manageSanStorage': True, "hostOSType": "Windows 2012 / WS2012 R2",
                                                             "volumeAttachments": [{
                                                                 "id": 1,
                                                                 "bootVolumePriority": "NotBootable",
                                                                 "lunType": "Auto",
                                                                 "storagePaths": [{
                                                                     "isEnabled": True,
                                                                     "connectionId": 1,
                                                                     "targetSelector": "Auto",
                                                                     "targets": []}],
                                                                 "volume": None,
                                                                 "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                                                                 "volumeUri": 'v:' + ENC1BAY1_VOLUME_NAME,
                                                             }
                                                             ]
                                                             }
                                              }

# Gen10 Profile1 Two Connections: ENC1 bay14, BL460c Gen10
# DHCP Initiator
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
enc1bay14_profile1_one_connection = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY14, 'enclosureUri': 'ENC:' + ENC1,
                                     "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                     "macType": "Physical", "wwnType": "Physical", "name": ENC1BAY14_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                     "connectionSettings": {
                                         "connections": [
                                             {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                              "ipv4": {
                                                  "ipAddressSource": "DHCP",
                                                  "subnetMask": "",
                                                  "gateway": "",
                                              },
                                              "boot": {
                                                  "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                      "firstBootTargetPort": "3260",
                                                      "bootTargetName": ENC3BAY7_PROFILE1_BOOT_TARGET_NAME,
                                                      "bootTargetLun": "0",
                                                      "chapLevel": None,
                                                      "chapName": "",
                                                      "chapSecret": None,
                                                      "mutualChapName": "",
                                                      "mutualChapSecret": None
                                                  }}},
                                         ]
                                     },
                                     "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                     "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                     "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                     "iscsiInitiatorName": ENC1BAY14_PROFILE1_INITIATOR_NAME,
                                     "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                     }

# Negative Profiles


# DHCP with IP address
negative_sp_dhcp_with_ip = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC3SHBAY8, 'enclosureUri': 'ENC:' + ENC3,
                            "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                            "macType": "Physical", "wwnType": "Physical", "name": "DHCP with IP", "description": "", "affinity": "Bay",
                            "connectionSettings": {
                                "connections": [
                                    {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                     "networkUri": 'ETH:network-tunnel',
                                     "ipv4": {
                                         "ipAddressSource": "DHCP",
                                         "ipAddress": ENC3BAY8_PROFILE2_INITIATOR_IP_1,
                                         "subnetMask": "",
                                         "gateway": "",
                                     },
                                        "boot": {
                                         "priority": "Primary", "bootVolumeSource": "UserDefined",
                                         "iscsi": {
                                             "initiatorNameSource": "UserDefined",
                                             "initiatorName": ENC3BAY8_PROFILE1_INITIATOR_NAME,
                                             "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                             "firstBootTargetPort": "3260",
                                             "bootTargetName": ENC3BAY8_PROFILE1_BOOT_TARGET_NAME,
                                             "bootTargetLun": "0",
                                             "chapLevel": "Chap",
                                             "chapName": ENC3BAY8_PROFILE1_CHAP_NAME,
                                             "chapSecret": CHAP_SECRET,
                                             "mutualChapName": "",
                                             "mutualChapSecret": None
                                         }}}
                                ]
                            },
                            "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                            "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                            "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                            "iscsiInitiatorName": ENC3BAY8_PROFILE1_INITIATOR_NAME,
                            "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                            }


# DHCP with Subnetmask
negative_sp_dhcp_with_subnetmask = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC3SHBAY8, 'enclosureUri': 'ENC:' + ENC3,
                                    "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                    "macType": "Physical", "wwnType": "Physical", "name": "DHCP with Subnetmask", "description": "", "affinity": "Bay",
                                    "connectionSettings": {
                                        "connections": [
                                            {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                             "networkUri": 'ETH:network-tunnel',
                                             "ipv4": {
                                                 "ipAddressSource": "DHCP",
                                                 "ipAddress": "",
                                                 "subnetMask": INITIATOR_SUBNET_MASK,
                                                 "gateway": "",
                                             },
                                                "boot": {
                                                 "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                 "iscsi": {
                                                     "initiatorNameSource": "UserDefined",
                                                     "initiatorName": ENC3BAY8_PROFILE1_INITIATOR_NAME,
                                                     "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                     "firstBootTargetPort": "3260",
                                                     "bootTargetName": ENC3BAY8_PROFILE1_BOOT_TARGET_NAME,
                                                     "bootTargetLun": "0",
                                                     "chapLevel": "Chap",
                                                     "chapName": ENC3BAY8_PROFILE1_CHAP_NAME,
                                                     "chapSecret": CHAP_SECRET,
                                                     "mutualChapName": "",
                                                     "mutualChapSecret": None
                                                 }}}
                                        ]
                                    },
                                    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                    "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                    "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                    "iscsiInitiatorName": ENC3BAY8_PROFILE1_INITIATOR_NAME,
                                    "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                    }

# DHCP with Gateway
negative_sp_dhcp_with_gateway = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC3SHBAY8, 'enclosureUri': 'ENC:' + ENC3,
                                 "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                 "macType": "Physical", "wwnType": "Physical", "name": "DHCP with Gateway", "description": "", "affinity": "Bay",
                                 "connectionSettings": {
                                     "connections": [
                                         {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                          "networkUri": 'ETH:network-tunnel',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "ipAddress": "",
                                              "subnetMask": "",
                                              "gateway": INITIATOR_GATEWAY,
                                          },
                                             "boot": {
                                              "priority": "Primary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "UserDefined",
                                                  "initiatorName": ENC3BAY8_PROFILE1_INITIATOR_NAME,
                                                  "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "bootTargetName": ENC3BAY8_PROFILE1_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "chapLevel": "Chap",
                                                  "chapName": ENC3BAY8_PROFILE1_CHAP_NAME,
                                                  "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None
                                              }}}
                                     ]
                                 },
                                 "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                 "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                 "iscsiInitiatorName": ENC3BAY8_PROFILE1_INITIATOR_NAME,
                                 "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                 }


# Move Test
# Profile1 Two Connections: ENC2 bay 1 to ENC1 bay1
# DHCP Initiator
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
move_enc2bay1_profile1_two_connections_to_enc1bay1 = {"type": SERVER_PROFILE_TYPE, "serverHardwareUri": 'SH:' + ENC1SHBAY1, 'enclosureUri': 'ENC:' + ENC1,
                                                      "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                                      "macType": "Physical", "wwnType": "Physical", "name": ENC2BAY1_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                                      "connectionSettings": {
                                                          "connections": [
                                                              {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                                               "ipv4": {
                                                                   "ipAddressSource": "DHCP",
                                                                   "subnetMask": "",
                                                                   "gateway": "",
                                                               },
                                                               "boot": {
                                                                   "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                                   "iscsi": {
                                                                       "initiatorNameSource": "ProfileInitiatorName",
                                                                       "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                                       "firstBootTargetPort": "3260",
                                                                       "bootTargetName": ENC2BAY1_PROFILE1_BOOT_TARGET_NAME,
                                                                       "bootTargetLun": "0",
                                                                       "chapLevel": "Chap",
                                                                       "chapName": ENC2BAY1_PROFILE1_CHAP_NAME,
                                                                       "chapSecret": CHAP_SECRET,
                                                                       "mutualChapName": "",
                                                                       "mutualChapSecret": None
                                                                   }}},
                                                              {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                                               "ipv4": {
                                                                   "ipAddressSource": "DHCP",
                                                                   "subnetMask": "",
                                                                   "gateway": "",
                                                               },
                                                                  "boot": {
                                                                   "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                                                   "iscsi": {
                                                                       "initiatorNameSource": "ProfileInitiatorName",
                                                                       "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                                       "firstBootTargetPort": "3260",
                                                                       "bootTargetName": ENC2BAY1_PROFILE1_BOOT_TARGET_NAME,
                                                                       "bootTargetLun": "0",
                                                                       "chapLevel": "Chap",
                                                                       "chapName": ENC2BAY1_PROFILE1_CHAP_NAME,
                                                                       "chapSecret": CHAP_SECRET,
                                                                       "mutualChapName": "",
                                                                       "mutualChapSecret": None
                                                                   }}}
                                                          ]
                                                      },
                                                      "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                                      "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                                      "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                                      "iscsiInitiatorName": ENC2BAY1_PROFILE1_INITIATOR_NAME,
                                                      "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                                      }


# Create with API v300
create_v300_profile = {"type": "ServerProfileV6", "serverHardwareUri": 'SH:' + ENC1SHBAY5, 'enclosureUri': 'ENC:' + ENC1,
                       "enclosureGroupUri": "EG:" + EG1_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                       "macType": "Physical", "wwnType": "Physical", "name": "API v300 Profile", "description": "", "affinity": "Bay",
                       "connections": [
                           {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                            "networkUri": 'ETH:network-untagged',
                            "ipv4": {
                                "ipAddressSource": "DHCP",
                                "subnetMask": "",
                                "gateway": "",
                            },
                               "boot": {
                                "priority": "Primary", "bootVolumeSource": "UserDefined",
                                "iscsi": {
                                    "initiatorNameSource": "UserDefined",
                                    "initiatorName": ENC1BAY5_PROFILE1_INITIATOR_NAME,
                                    "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                    "firstBootTargetPort": "3260",
                                    "bootTargetName": ENC1BAY5_PROFILE1_BOOT_TARGET_NAME,
                                    "bootTargetLun": "0",
                                    "chapLevel": "Chap",
                                    "chapName": ENC1BAY5_PROFILE1_CHAP_NAME,
                                    "chapSecret": CHAP_SECRET,
                                    "mutualChapName": "",
                                    "mutualChapSecret": None
                                }}}
                       ],
                       "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                       "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                       "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                       "iscsiInitiatorName": ENC1BAY5_PROFILE1_INITIATOR_NAME,
                       "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                       }

# API v300 GET
get_300_profile = {"type": "ServerProfileV6", "serverHardwareUri": 'SH:' + ENC3SHBAY8, 'enclosureUri': 'ENC:' + ENC1,
                   "enclosureGroupUri": "EG:" + EG3_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                   "macType": "Physical", "wwnType": "Physical", "name": ENC3BAY8_PROFILE1_NAME, "description": "", "affinity": "Bay",
                   "connections": [],
                   "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                   "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                   "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                   "iscsiInitiatorName": ENC3BAY8_PROFILE1_INITIATOR_NAME,
                   "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                   }


# Blade CLPs

# Enc 1 Bay 1 no profile
clp_enc1bay1_no_profile = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"
"""
}


# Enc 1 Bay 5 no profile
clp_enc1bay5_no_profile = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "5",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=3413"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=3413"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"
"""
}


# Enc 3 Bay 7 no profile
clp_enc3bay7_no_profile = {
    "oa": ENC3_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "7",
    "validate":
    """

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"
"""
}

# Enc 3 Bay 8 no profile
clp_enc3bay8_no_profile = {
    "oa": ENC3_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "8",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"

Blade 8 mezz 2: NOT FOUND

Blade 8 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"
"""
}

# Enc 2 Bay 1 no profile
clp_enc2bay1_no_profile = {
    "oa": ENC2_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"
"""
}


# Enc 1 Bay 1 profile 1 two connections
clp_enc1bay1_profile1_two_connections = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"

--------------------------------------

HP LPe1205A 8Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1416"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1412"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;AC162DAB6148;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;AC162DAB6149;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay2-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:158:wpst10-bay2-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=None"

     PID44: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID45: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=060Fh)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;AC162DAB614C;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;AC162DAB614D;1001;2500;10000;enabled;enabled""

     PID36: "set netport2 OEMHP_IPVersion=IPv4"

     PID37: "set netport2 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport2 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay2-dhcp"

     PID39: "set netport2 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:158:wpst10-bay2-dhcp"

     PID40: "set netport2 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport2 OEMHP_targetPort=3260"

     PID42: "set netport2 OEMHP_LUN=0"

     PID43: "set netport2 OEMHP_authenticationMethod=None"

     PID44: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID45: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"
"""
}

# Enc 1 Bay 5 profile 1 two connections
clp_enc1bay5_profile1_two_connections = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "5",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=3413"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=3413"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;6CC21737C500;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;6CC21737C501;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst22-bay5-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:769:wpst22-bay5-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst22-bay5""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0670h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;6CC21737C508;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;6CC21737C509;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst22-bay5-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:769:wpst22-bay5-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst22-bay5""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"
"""
}

# Enc 3 Bay 8 profile 1 two connections
clp_enc3bay8_profile1_two_connections = {
    "oa": ENC3_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "8",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;5CB901D71160;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;5CB901D71161;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:161:wpst10-bay7-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay7""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0670h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;5CB901D71164;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;5CB901D71165;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:161:wpst10-bay7-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay7""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1412"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1415"

     PID05: "exit"

Blade 7 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

Blade 7 mezz A: NOT FOUND
"""
}

# Enc 2 Bay 1 profile 1 two connections
clp_enc2bay1_profile1_two_connections = {
    "oa": ENC2_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;D89D6773C010;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;D89D6773C011;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst23-bay1-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:772:wpst23-bay1-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst23-bay1""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0670h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;D89D6773C014;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;D89D6773C015;1001;2500;10000;enabled;enabled""

     PID36: "set netport2 OEMHP_IPVersion=IPv4"

     PID37: "set netport2 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport2 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst23-bay1-dhcp"

     PID39: "set netport2 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:772:wpst23-bay1-dhcp"

     PID40: "set netport2 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport2 OEMHP_targetPort=3260"

     PID42: "set netport2 OEMHP_LUN=0"

     PID43: "set netport2 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport2 OEMHP_username="wpst23-bay1""

     PID45: "set netport2 OEMHP_secret=777073746870767365313233"

     PID46: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"
"""
}


# Enc 1 Bay 1profile 1 one connection untagged
clp_enc1bay1_profile1_one_connection_untagged = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;A0B3CC1C80C8;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;A0B3CC1C80C9;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay2-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:158:wpst10-bay2-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=None"

     PID44: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID45: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=060Fh)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;A0B3CC1C80CC;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;A0B3CC1C80CD;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP LPe1205A 8Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1416"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1412"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"
"""
}

# Enc 1 Bay 5 profile 1 one connection untagged
clp_enc1bay5_profile1_one_connection_untagged = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "5",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"

--------------------------------------

HP LPe1205A 8Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1416"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1411"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;C4346BC8E468;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;C4346BC8E469;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay3-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:150:wpst10-bay3-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay3""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0670h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;C4346BC8E46C;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;C4346BC8E46D;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"
"""
}

clp_enc3bay7_profile1_one_connection_untagged = {
    "oa": ENC3_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "7",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;6CC217372290;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;6CC217372291;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst26-bay7-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:784:wpst26-bay7-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=None"

     PID44: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID45: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=060Fh)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;6CC217372298;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;6CC217372299;1001;0;0;disabled;disabled""

     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"
"""
}

# Enc 3 Bay 8 profile 1 one connection untagged
clp_enc3bay8_profile1_one_connection_untagged = {
    "oa": ENC3_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "8",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1412"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1415"

     PID05: "exit"

Blade 7 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;ECB1D7A95B70;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;ECB1D7A95B71;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:161:wpst10-bay7-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay7""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0670h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;ECB1D7A95B78;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;ECB1D7A95B79;1001;0;0;disabled;disabled""

     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

Blade 7 mezz A: NOT FOUND
"""
}

# Enc 2 Bay 1 profile 1 one connection untagged
clp_enc2bay1_profile1_one_connection_untagged = {
    "oa": ENC2_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3CA82AFEFF40;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3CA82AFEFF41;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:164:wpst10-bay8-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay8""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0670h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;3CA82AFEFF44;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;3CA82AFEFF45;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

Blade 8 mezz 2: NOT FOUND

Blade 8 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"
"""
}


# Enc 1 Bay 1 profile 1 one connection tunnel
clp_enc1bay1_profile1_one_connection_tunnel = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;A0B3CC1C80C8;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;A0B3CC1C80C9;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay2-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:158:wpst10-bay2-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=None"

     PID44: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID45: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=060Fh)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;A0B3CC1C80CC;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;A0B3CC1C80CD;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP LPe1205A 8Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1416"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1412"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"
"""
}

# Enc 1 Bay 5 profile 1 one connection tunnel
clp_enc1bay5_profile1_one_connection_tunnel = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "5",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;10604B010400;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;10604B010401;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay3-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:150:wpst10-bay3-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay3""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0670h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;10604B010404;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;10604B010405;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP LPe1205A 8Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1416"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1411"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"
"""
}

# Enc 3 Bay 8 profile 1 one connection tunnel
clp_enc3bay8_profile1_one_connection_tunnel = {
    "oa": ENC3_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "8",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"

Blade 8 mezz 2: NOT FOUND

Blade 8 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;B4B52F5AAA20;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;B4B52F5AAA21;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst26-bay8-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:787:wpst26-bay8-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=MutualCHAP"

     PID44: "set netport1 OEMHP_username="wpst26-bay8""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_MutualUsername="wpst26-bay8""

     PID47: "set netport1 OEMHP_mutualSecret=687076736531323377707374"

     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=06E3h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;B4B52F5AAA24;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;B4B52F5AAA25;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"
"""
}

# Enc 2 Bay 1 profile 1 one connection tunnel
clp_enc2bay1_profile1_one_connection_tunnel = {
    "oa": ENC2_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3CA82AFEFF40;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3CA82AFEFF41;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:164:wpst10-bay8-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay8""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0670h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;3CA82AFEFF44;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;3CA82AFEFF45;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

Blade 8 mezz 2: NOT FOUND

Blade 8 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

"""
}


# Enc 1 Bay 5 profile 2 two connections
clp_enc1bay5_profile2_two_connections = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "5",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;10604B010400;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;10604B010401;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.128"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay3"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:829:wpst10-bay3-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=None"

     PID45: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0644h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;10604B010404;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;10604B010405;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP LPe1205A 8Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1416"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1411"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;C4346BC8E468;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;C4346BC8E469;1001;0;0;disabled;disabled""

     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=046Bh)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;C4346BC8E46C;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;C4346BC8E46D;1001;2500;10000;enabled;enabled""

     PID36: "set netport2 OEMHP_IPVersion=IPv4"

     PID37: "set netport2 OEMHP_InitiatorIP=192.168.22.129"

     PID38: "set netport2 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport2 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay3"

     PID40: "set netport2 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:829:wpst10-bay3-bootvol"

     PID41: "set netport2 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport2 OEMHP_targetPort=3260"

     PID43: "set netport2 OEMHP_LUN=0"

     PID44: "set netport2 OEMHP_authenticationMethod=None"

     PID45: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"
"""
}

# Enc 3 Bay 8 profile 2 two connections
clp_enc3bay8_profile2_two_connections = {
    "oa": ENC3_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "8",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;5CB901D71160;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;5CB901D71161;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.126"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:821:wpst10-bay7-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=None"

     PID45: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0644h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;5CB901D71164;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;5CB901D71165;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.127"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:821:wpst10-bay7-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=None"

     PID45: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1412"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1415"

     PID05: "exit"

Blade 7 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

Blade 7 mezz A: NOT FOUND
"""
}

# Enc 2 Bay 1 profile 2 two connections
clp_enc2bay1_profile2_two_connections = {
    "oa": ENC2_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"

Blade 8 mezz 2: NOT FOUND

Blade 8 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3863BB4176F8;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3863BB4176F9;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.130"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:879:wpst10-bay8-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=None"

     PID45: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0644h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3863BB4176FC;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3863BB4176FD;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.131"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:879:wpst10-bay8-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=None"

     PID45: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"
"""
}


# Enc 3 Bay 8 profile 2 one connection tunnel
clp_enc3bay8_profile2_one_connection_tunnel = {
    "oa": ENC3_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "8",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1412"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1415"

     PID05: "exit"

Blade 7 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;ECB1D7A95B70;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;ECB1D7A95B71;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.126"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:821:wpst10-bay7-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=None"

     PID45: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0644h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;ECB1D7A95B78;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;ECB1D7A95B79;1001;0;0;disabled;disabled""

     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

Blade 7 mezz A: NOT FOUND
"""
}

# Enc 2 Bay 1 profile 2 one connection tunnel
clp_enc2bay1_profile2_one_connection_tunnel = {
    "oa": ENC2_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;D89D6773C010;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;D89D6773C011;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.148"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst23-bay1"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1315:wpst23-bay1-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=None"

     PID45: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0645h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;D89D6773C014;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;D89D6773C015;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"
"""
}


clp_enc3bay7_profile2_one_connection_tunnel = {
    "oa": ENC3_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "7",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;6CC217372290;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;6CC217372291;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.144"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst26-bay7"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1309:wpst26-bay7-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=MutualCHAP"

     PID45: "set netport1 OEMHP_username="wpst26-bay7""

     PID46: "set netport1 OEMHP_secret=777073746870767365313233"

     PID47: "set netport1 OEMHP_MutualUsername="wpst26-bay7""

     PID48: "set netport1 OEMHP_mutualSecret=687076736531323377707374"

     PID49: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID50: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0719h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;6CC217372298;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;6CC217372299;1001;0;0;disabled;disabled""

     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"
"""
}


# Enc 1 Bay 5 profile 2 one connection untagged
clp_enc1bay5_profile2_one_connection_untagged = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "5",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=3413"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=3413"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;6CC21737C500;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;6CC21737C501;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.142"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst22-bay5"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1303:wpst22-bay5-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID45: "set netport1 OEMHP_username="wpst22-bay5""

     PID46: "set netport1 OEMHP_secret=777073746870767365313233"

     PID47: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID48: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=06A6h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;6CC21737C508;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;6CC21737C509;1001;0;0;disabled;disabled""

     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"
"""
}

# Enc 3 Bay 8 profile 2 one connection untagged
clp_enc3bay8_profile2_one_connection_untagged = {
    "oa": ENC3_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "8",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"

Blade 8 mezz 2: NOT FOUND

Blade 8 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;B4B52F5AAA20;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;B4B52F5AAA21;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.146"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst26-bay8"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1312:wpst26-bay8-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID45: "set netport1 OEMHP_username="wpst26-bay8""

     PID46: "set netport1 OEMHP_secret=777073746870767365313233"

     PID47: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID48: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=06A6h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;B4B52F5AAA24;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;B4B52F5AAA25;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"
"""
}

# Enc 2 Bay 1 profile 2 one connection untagged
clp_enc2bay1_profile2_one_connection_untagged = {
    "oa": ENC2_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3CA82AFEFF40;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3CA82AFEFF41;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.130"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:879:wpst10-bay8-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=None"

     PID45: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0644h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;3CA82AFEFF44;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;3CA82AFEFF45;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

Blade 8 mezz 2: NOT FOUND

Blade 8 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"
"""
}


# Enc 3 Bay 7 profile 3 two connections
clp_enc3bay7_profile3_two_connections = {
    "oa": ENC3_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "7",
    "validate":
    """
Blade 4 mezz F: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

        --> status: 00000500h

     PID02: "exit"

        --> status: 00000500h

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1414"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1412"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

        --> status: 00000500h

     PID32: "set netport1 OEMHP_CVNI=2001"

        --> status: 00000500h

     PID33: "set netport1 OEMHP_FlowControl=function"

        --> status: 00000500h

     PID34: "set netport1 OEMHP_LF0="E;1;6CC2173C0080;1000;0;0;disabled;disabled""

        --> status: 00000500h

     PID35: "set netport1 OEMHP_LF1="I;1;6CC2173C0081;1001;2500;10000;enabled;enabled""

        --> status: 00000500h

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

        --> status: 00000500h

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

        --> status: 00000500h

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay4-dhcp-managed-volume"

        --> status: 00000500h

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:539:wpst10-bay4-dhcp-managed-volume"

        --> status: 00000500h

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

        --> status: 00000500h

     PID41: "set netport1 OEMHP_targetPort=3260"

1475707274:Wed Oct  5 22:41:14 2016:1245:nettray.c:2766:GetIOIPv6Info::SWM5: Read 1 addr from SWM IPV6_INFO
        --> status: 00000500h

     PID42: "set netport1 OEMHP_LUN=0"

        --> status: 00000500h

     PID43: "set netport1 OEMHP_authenticationMethod=MutualCHAP"

        --> status: 00000500h

     PID44: "set netport1 OEMHP_username="iqn.2015-02.com.hpe:oneview-wpst10-bay4-dhcp-managed-volume""

        --> status: 00000500h

     PID45: "set netport1 OEMHP_secret=304f55724c61736b744f725724734a71"

        --> status: 00000500h

     PID46: "set netport1 OEMHP_MutualUsername="iqn.2015-02.com.hpe:oneview-wpst10-bay4-dhcp-managed-volume""

        --> status: 00000500h

     PID47: "set netport1 OEMHP_mutualSecret=725444644e3173763074646d496c6661"

1475707275:Wed Oct  5 22:41:15 2016:1245:nettray.c:2980:GetIOIPv6ProtoData::SWM5 doesn't form URL for the IPv6 address [1 of 1].
        --> status: 0000FF02h

     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

        --> status: 00000500h

     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

        --> status: 00000500h

     PID02: "exit"

        --> status: 00000500h

  FIP: 1 (off=0771h)

     PID01: "set netport1 default"

        --> status: 00000500h

     PID32: "set netport1 OEMHP_CVNI=2001"

        --> status: 00000500h

     PID33: "set netport1 OEMHP_FlowControl=function"

        --> status: 00000500h

     PID34: "set netport1 OEMHP_LF0="E;1;6CC2173C0088;1000;0;0;disabled;disabled""

        --> status: 00000500h

     PID35: "set netport1 OEMHP_LF1="I;1;6CC2173C0089;1001;2500;10000;enabled;enabled""

        --> status: 00000500h

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

        --> status: 00000500h

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

        --> status: 00000500h

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay4-dhcp-managed-volume"

        --> status: 00000500h

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:539:wpst10-bay4-dhcp-managed-volume"

        --> status: 00000500h

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

        --> status: 00000500h

     PID41: "set netport1 OEMHP_targetPort=3260"

        --> status: 00000500h

     PID42: "set netport1 OEMHP_LUN=0"

        --> status: 00000500h

     PID43: "set netport1 OEMHP_authenticationMethod=MutualCHAP"

        --> status: 00000500h

     PID44: "set netport1 OEMHP_username="iqn.2015-02.com.hpe:oneview-wpst10-bay4-dhcp-managed-volume""

        --> status: 00000500h

     PID45: "set netport1 OEMHP_secret=304f55724c61736b744f725724734a71"

        --> status: 00000500h

     PID46: "set netport1 OEMHP_MutualUsername="iqn.2015-02.com.hpe:oneview-wpst10-bay4-dhcp-managed-volume""

        --> status: 00000500h

     PID47: "set netport1 OEMHP_mutualSecret=725444644e3173763074646d496c6661"

        --> status: 0000FF02h

     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

        --> status: 00000500h

     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

        --> status: 00000500h

     PID02: "exit"

        --> status: 00000500h
"""
}

# Bay 7 profile 3 two connections
clp_bay7_profile3_two_connections = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "7",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;5CB901D71160;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;5CB901D71161;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp-managed-volume"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:334:wpst10-bay7-dhcp-managed-volume"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=MutualCHAP"

     PID44: "set netport1 OEMHP_username="iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp-managed-volume""

     PID45: "set netport1 OEMHP_secret=4d5839717546584a6143394e21476b38"

     PID46: "set netport1 OEMHP_MutualUsername="iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp-managed-volume""

     PID47: "set netport1 OEMHP_mutualSecret=77364f48592d5a292321674145434274"

     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0771h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;5CB901D71164;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;5CB901D71165;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp-managed-volume"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:334:wpst10-bay7-dhcp-managed-volume"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=MutualCHAP"

     PID44: "set netport1 OEMHP_username="iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp-managed-volume""

     PID45: "set netport1 OEMHP_secret=4d5839717546584a6143394e21476b38"

     PID46: "set netport1 OEMHP_MutualUsername="iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp-managed-volume""

     PID47: "set netport1 OEMHP_mutualSecret=77364f48592d5a292321674145434274"

     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1412"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1415"

     PID05: "exit"

Blade 7 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

Blade 7 mezz A: NOT FOUND
"""
}

# Enc 2 Bay 1 profile 3 two connections
clp_enc2bay1_profile3_two_connections = {
    "oa": ENC2_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"

Blade 8 mezz 2: NOT FOUND

Blade 8 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3863BB4176F8;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3863BB4176F9;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp-managed-volume"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:337:wpst10-bay8-dhcp-managed-volume"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=MutualCHAP"

     PID44: "set netport1 OEMHP_username="iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp-managed-volume""

     PID45: "set netport1 OEMHP_secret=765e5276494278585462797736595a79"

     PID46: "set netport1 OEMHP_MutualUsername="iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp-managed-volume""

     PID47: "set netport1 OEMHP_mutualSecret=566e384941335733275f386b5e415072"

     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0771h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3863BB4176FC;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3863BB4176FD;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp-managed-volume"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:337:wpst10-bay8-dhcp-managed-volume"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=MutualCHAP"

     PID44: "set netport1 OEMHP_username="iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp-managed-volume""

     PID45: "set netport1 OEMHP_secret=765e5276494278585462797736595a79"

     PID46: "set netport1 OEMHP_MutualUsername="iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp-managed-volume""

     PID47: "set netport1 OEMHP_mutualSecret=566e384941335733275f386b5e415072"

     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"
"""
}


# Bay 7 profile 3 one connection untagged
clp_bay7_profile3_one_connection_untagged = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "7",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;5CB901D71160;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;5CB901D71161;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp-managed-volume"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:334:wpst10-bay7-dhcp-managed-volume"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=MutualCHAP"

     PID44: "set netport1 OEMHP_username="iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp-managed-volume""

     PID45: "set netport1 OEMHP_secret=55594e4f67402b3348384d614e54454c"

     PID46: "set netport1 OEMHP_MutualUsername="iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp-managed-volume""

     PID47: "set netport1 OEMHP_mutualSecret=496326306575616a4b62476e64555666"

     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0771h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;5CB901D71164;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;5CB901D71165;1001;0;0;disabled;disabled""

     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1412"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1415"

     PID05: "exit"

Blade 7 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

Blade 7 mezz A: NOT FOUND
"""
}

# Enc 2 Bay 1 profile 3 one connection untagged
clp_enc2bay1_profile3_one_connection_untagged = {
    "oa": ENC2_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"

Blade 8 mezz 2: NOT FOUND

Blade 8 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3863BB4176F8;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3863BB4176F9;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp-managed-volume"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:337:wpst10-bay8-dhcp-managed-volume"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=MutualCHAP"

     PID44: "set netport1 OEMHP_username="iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp-managed-volume""

     PID45: "set netport1 OEMHP_secret=337172285f79742425314b2669257021"

     PID46: "set netport1 OEMHP_MutualUsername="iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp-managed-volume""

     PID47: "set netport1 OEMHP_mutualSecret=676d47726d274b6431246a6c21502379"

     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0771h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3863BB4176FC;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3863BB4176FD;1001;0;0;disabled;disabled""

     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"
"""
}

# Enc 1 Bay 1 no profile
clp_enc1bay1_move = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;FC15B425C3C8;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;FC15B425C3C9;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst23-bay1-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:772:wpst23-bay1-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst23-bay1""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0670h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;FC15B425C3CC;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;FC15B425C3CD;1001;2500;10000;enabled;enabled""

     PID36: "set netport2 OEMHP_IPVersion=IPv4"

     PID37: "set netport2 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport2 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst23-bay1-dhcp"

     PID39: "set netport2 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:772:wpst23-bay1-dhcp"

     PID40: "set netport2 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport2 OEMHP_targetPort=3260"

     PID42: "set netport2 OEMHP_LUN=0"

     PID43: "set netport2 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport2 OEMHP_username="wpst23-bay1""

     PID45: "set netport2 OEMHP_secret=777073746870767365313233"

     PID46: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"
"""
}
# Server Profile Templates

# DHCP iSCSI primary only, Legacy Bios, untagged network
dhcp_primary_only_legacy_bios_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_primary_only_legacy_bios_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# edit from DHCP to User Specified iSCSI primary only, Legacy Bios, untagged network
edit_dhcp_primary_only_legacy_bios_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_primary_only_legacy_bios_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# DHCP iSCSI primary only, Legacy Bios, untagged network
dhcp_managed_volume_primary_only_legacy_bios_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_managed_volume_primary_only_legacy_bios_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "template_dhcp_primary_only_legacy_bios",
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            }
        ]
    }
}

# DHCP iSCSI primary only, Legacy Bios, untagged network
dhcp_managed_volume_primary_only_legacy_bios_untagged_template_edit2 = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_managed_volume_primary_only_legacy_bios_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "template_dhcp_primary_only_legacy_bios",
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            }
        ]
    }
}

# edit DHCP to User Specified iSCSI primary only, Legacy Bios, untagged network
edit_dhcp_managed_volume_primary_only_legacy_bios_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_managed_volume_primary_only_legacy_bios_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "edit_template_dhcp_primary_only_legacy_bios",
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            }
        ]
    }
}

# DHCP iSCSI primary only, Legacy Bios, tunnel network
dhcp_primary_only_legacy_bios_tunnel_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_primary_only_legacy_bios_tunnel_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# edit DHCP to User Specified iSCSI primary only, Legacy Bios, tunnel network
edit_dhcp_primary_only_legacy_bios_tunnel_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_primary_only_legacy_bios_tunnel_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# DHCP iSCSI primary & secondary, Legacy Bios, untagged network
dhcp_legacy_bios_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_legacy_bios_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# edit DHCP to User Specified iSCSI primary & secondary, Legacy Bios, untagged network
edit_dhcp_legacy_bios_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_legacy_bios_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# DHCP iSCSI with managed volume primary & secondary, Legacy Bios, untagged network
dhcp_managed_volume_legacy_bios_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_managed_volume_legacy_bios_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "template_dhcp_legacy_bios",
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            }
        ]
    }
}

# DHCP iSCSI with managed volume primary & secondary, Legacy Bios, untagged network
dhcp_managed_volume_legacy_bios_untagged_template_edit2 = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_managed_volume_legacy_bios_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "template_dhcp_legacy_bios",
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            }
        ]
    }
}

# edit DHCP to User Specified iSCSI with managed volume primary & secondary, Legacy Bios, untagged network
edit_dhcp_managed_volume_legacy_bios_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_managed_volume_legacy_bios_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "edit_template_dhcp_legacy_bios",
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            }
        ]
    }
}

# DHCP iSCSI primary & secondary, Legacy BIOs, tunnel network
dhcp_legacy_bios_tunnel_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_legacy_bios_tunnel_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# edit DHCP to User Specified iSCSI primary & secondary, Legacy BIOs, tunnel network
edit_dhcp_legacy_bios_tunnel_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_legacy_bios_tunnel_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# DHCP iSCSI primary only, UEFI, untagged network
dhcp_primary_only_UEFI_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_primary_only_UEFI_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# edit DHCP to User Specified iSCSI primary only, UEFI, untagged network
edit_dhcp_primary_only_UEFI_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_primary_only_UEFI_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# DHCP iSCSI primary only, UEFI, untagged network
dhcp_managed_volume_primary_only_UEFI_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_managed_volume_primary_only_UEFI_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "template_dhcp_primary_only_uefi",
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            }
        ]
    }
}

# gen10 DHCP iSCSI primary only, UEFI, untagged network
gen10_dhcp_managed_volume_primary_only_UEFI_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'gen10_dhcp_managed_volume_primary_only_UEFI_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + Gen10_TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {
                "id": 1,
                "lunType": "Auto",
                "lun": None,
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],
                "bootVolumePriority": "Primary",
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "template_dhcp_primary_only_uefi",
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "templateVersion": "1.1",
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                        "isAdaptiveOptimizationEnabled": True
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            }
        ]
    }
}

# DHCP iSCSI primary only, UEFI, untagged network
dhcp_managed_volume_primary_only_UEFI_untagged_template_edit2 = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_managed_volume_primary_only_UEFI_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "template_dhcp_primary_only_uefi",
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            }
        ]
    }
}

# edit DHCP to User Specified iSCSI primary only, UEFI, untagged network
edit_dhcp_managed_volume_primary_only_UEFI_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_managed_volume_primary_only_UEFI_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "edit_template_dhcp_primary_only_uefi",
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            }
        ]
    }
}

# DHCP iSCSI primary only, UEFI, tunnel network
dhcp_primary_only_UEFI_tunnel_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_primary_only_UEFI_tunnel_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# edit DHCP to User Specified iSCSI primary only, UEFI, tunnel network
edit_dhcp_primary_only_UEFI_tunnel_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_primary_only_UEFI_tunnel_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# DHCP iSCSI primary & secondary, UEFI, untagged network
dhcp_UEFI_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_UEFI_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# edit DHCP to User Specified iSCSI primary & secondary, UEFI, untagged network
edit_dhcp_UEFI_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_UEFI_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }}},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# DHCP iSCSI with managed volume primary & secondary, UEFI, untagged network
dhcp_managed_volume_UEFI_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_managed_volume_UEFI_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "template_dhcp_uefi",
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            }
        ]
    }
}

# DHCP iSCSI with managed volume primary & secondary, UEFI, untagged network
dhcp_managed_volume_UEFI_untagged_template_edit2 = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_managed_volume_UEFI_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "template_dhcp_uefi",
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            }
        ]
    }
}

# edit DHCP to User Specified iSCSI with managed volume primary & secondary, UEFI, untagged network
edit_dhcp_managed_volume_UEFI_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_managed_volume_UEFI_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "edit_template_dhcp_uefi",
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            }
        ]
    }
}

# DHCP iSCSI primary & secondary, UEFI, tunnel network
dhcp_UEFI_tunnel_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_UEFI_tunnel_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }}},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# edit DHCP to User Specified iSCSI primary & secondary, UEFI, tunnel network
edit_dhcp_UEFI_tunnel_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_UEFI_tunnel_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }}},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# DHCP iSCSI primary only, UEFI Optimized, untagged network
dhcp_primary_only_UEFI_optimized_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_primary_only_UEFI_optimized_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# edit DHCP to User Specified iSCSI primary only, UEFI Optimized, untagged network
edit_dhcp_primary_only_UEFI_optimized_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_primary_only_UEFI_optimized_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# DHCP iSCSI primary only, UEFI Optimized, untagged network
dhcp_managed_volume_primary_only_UEFI_optimized_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_managed_volume_primary_only_UEFI_optimized_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "template_dhcp_primary_only_uefi_optimized",
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            }
        ]
    }
}

# DHCP iSCSI primary only, UEFI Optimized, untagged network
dhcp_managed_volume_primary_only_UEFI_optimized_untagged_template_edit2 = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_managed_volume_primary_only_UEFI_optimized_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "template_dhcp_primary_only_uefi_optimized",
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            }
        ]
    }
}

# edit DHCP to User Specified iSCSI primary only, UEFI Optimized, untagged network
edit_dhcp_managed_volume_primary_only_UEFI_optimized_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_managed_volume_primary_only_UEFI_optimized_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "edit_template_dhcp_primary_only_uefi_optimized",
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            }
        ]
    }
}

# DHCP iSCSI primary only, UEFI optimized, tunnel network
dhcp_primary_only_UEFI_optimized_tunnel_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_primary_only_UEFI_optimized_tunnel_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# edit DHCP to User Specified iSCSI primary only, UEFI optimized, tunnel network
edit_dhcp_primary_only_UEFI_optimized_tunnel_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_primary_only_UEFI_optimized_tunnel_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# DHCP iSCSI primary & secondary, UEFI optimized, untagged network
dhcp_UEFI_optimized_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_UEFI_optimized_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }}},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# edit DHCP to User Specified iSCSI primary & secondary, UEFI optimized, untagged network
edit_dhcp_UEFI_optimized_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_UEFI_optimized_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }}},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# DHCP iSCSI with managed volume primary & secondary, UEFI Optimized, untagged network
dhcp_managed_volume_UEFI_optimized_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_managed_volume_UEFI_optimized_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],

                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "template_dhcp_uefi_optimized",
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            }
        ]
    }
}

# DHCP iSCSI with managed volume primary & secondary, UEFI Optimized, untagged network
dhcp_managed_volume_UEFI_optimized_untagged_template_edit2 = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_managed_volume_UEFI_optimized_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],

                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "template_dhcp_uefi_optimized",
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            }
        ]
    }
}

# edit DHCP to User Specified iSCSI with managed volume primary & secondary, UEFI Optimized, untagged network
edit_dhcp_managed_volume_UEFI_optimized_untagged_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_managed_volume_UEFI_optimized_untagged_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "edit_template_dhcp_uefi_optimized",
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            }
        ]
    }
}

# DHCP iSCSI primary & secondary, UEFI optimized, tunnel network
dhcp_UEFI_optimized_tunnel_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_UEFI_optimized_tunnel_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }}},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# edit DHCP to User Specified iSCSI primary & secondary, UEFI optimized, tunnel network
edit_dhcp_UEFI_optimized_tunnel_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_UEFI_optimized_tunnel_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }}},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# Negative Server Profile Templates

# DHCP with IP address
negative_spt_dhcp_with_ip = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_with_ip_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "ipAddress": ENC3BAY7_PROFILE2_INITIATOR_IP_1,
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# DHCP with Subnetmask
negative_spt_dhcp_with_subnetmask = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_with_subnetmask_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "ipAddress": "",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# DHCP with gateway
negative_spt_dhcp_with_gateway = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'dhcp_with_gateway_template',
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "ipAddress": "",
                "subnetMask": "",
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}


all_profiles = [move_enc2bay1_profile1_two_connections_to_enc1bay1.copy(),
                enc2bay1_profile1_two_connections.copy(),
                # enc3bay8_profile3_one_connection_untagged.copy(),
                enc3bay8_profile2_one_connection_untagged.copy(),
                enc1bay5_profile3_two_connections.copy(),
                enc3bay7_profile1_one_connection_untagged.copy(),
                enc1bay14_profile1_two_connections.copy(),
                enc1bay16_profile1_one_connection_untagged.copy(),
                enc1bay14_profile1_one_connection.copy(),
                ]

create_profiles = [
    enc2bay1_profile3_two_connections.copy(),
    # enc2bay1_profile2_one_connection_tunnel.copy(),
    enc3bay8_profile1_one_connection_tunnel.copy(),
    enc1bay5_profile1_two_connections.copy(),
    enc3bay7_profile3_one_connection_untagged.copy(),
]

edit_profiles = [
    enc2bay1_profile2_one_connection_tunnel.copy(),
    enc3bay8_profile2_one_connection_untagged.copy(),
    enc1bay5_profile2_one_connection_untagged.copy(),
    enc3bay7_profile2_one_connection_tunnel.copy(),
]

edit_profiles2 = [enc2bay1_profile1_two_connections.copy(),
                  enc3bay8_profile3_one_connection_untagged.copy(),
                  enc1bay5_profile3_two_connections.copy(),
                  enc3bay7_profile1_one_connection_untagged.copy(),
                  ]

move_profiles = [move_enc2bay1_profile1_two_connections_to_enc1bay1.copy(),
                 ]

create_gen10_profiles = [
    enc1bay14_profile1_two_connections.copy(),
    enc1bay16_profile1_one_connection_untagged.copy(), ]

edit_gen10_profile = [enc1bay14_profile1_one_connection.copy(), ]

delete_profiles = [
    enc3bay8_profile3_one_connection_untagged.copy(),
    # enc3bay8_profile2_one_connection_untagged.copy(),
    enc1bay5_profile3_two_connections.copy(),
    enc3bay7_profile1_one_connection_untagged.copy(),
    move_enc2bay1_profile1_two_connections_to_enc1bay1.copy(),
]

clp_after_create = [
    # clp_enc2bay1_profile2_one_connection_tunnel.copy(),
    clp_enc3bay8_profile1_one_connection_tunnel.copy(),
    clp_enc1bay5_profile1_two_connections.copy(),
]

clp_after_edit = [
    clp_enc2bay1_profile2_one_connection_tunnel.copy(),
    clp_enc3bay8_profile2_one_connection_untagged.copy(),
    clp_enc1bay5_profile2_one_connection_untagged.copy(),
    clp_enc3bay7_profile2_one_connection_tunnel.copy(),
]

clp_after_edit2 = [clp_enc2bay1_profile1_two_connections.copy(),
                   clp_enc3bay7_profile1_one_connection_untagged.copy(),
                   ]

clp_after_move = [clp_enc1bay1_move.copy(),
                  clp_enc2bay1_no_profile.copy(),
                  ]

clp_after_delete = [clp_enc3bay8_no_profile.copy(),
                    clp_enc2bay1_no_profile.copy(),
                    clp_enc1bay1_no_profile.copy(),
                    clp_enc1bay5_no_profile.copy(),
                    clp_enc3bay7_no_profile.copy(),
                    ]

negative_profile_tasks = [
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_dhcp_with_ip.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_dhcp_server_profile_with_ip_address'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_dhcp_with_subnetmask.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_dhcp_server_profile_with_ip_address'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_dhcp_with_gateway.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_dhcp_server_profile_with_ip_address'},
]

create_profile_templates = [dhcp_primary_only_legacy_bios_untagged_template.copy(),
                            dhcp_primary_only_legacy_bios_tunnel_template.copy(),
                            dhcp_legacy_bios_untagged_template.copy(),
                            dhcp_legacy_bios_tunnel_template.copy(),
                            dhcp_primary_only_UEFI_untagged_template.copy(),
                            dhcp_primary_only_UEFI_tunnel_template.copy(),
                            dhcp_UEFI_untagged_template.copy(),
                            dhcp_UEFI_tunnel_template.copy(),
                            dhcp_primary_only_UEFI_optimized_untagged_template.copy(),
                            dhcp_primary_only_UEFI_optimized_tunnel_template.copy(),
                            dhcp_UEFI_optimized_untagged_template.copy(),
                            dhcp_UEFI_optimized_tunnel_template.copy(),
                            dhcp_managed_volume_primary_only_legacy_bios_untagged_template.copy(),
                            dhcp_managed_volume_legacy_bios_untagged_template.copy(),
                            dhcp_managed_volume_primary_only_UEFI_untagged_template.copy(),
                            dhcp_managed_volume_UEFI_untagged_template.copy(),
                            dhcp_managed_volume_primary_only_UEFI_optimized_untagged_template.copy(),
                            dhcp_managed_volume_UEFI_optimized_untagged_template.copy(),
                            ]
create_gen10_profile_template = [gen10_dhcp_managed_volume_primary_only_UEFI_untagged_template.copy(), ]

edit_profile_templates = [edit_dhcp_primary_only_legacy_bios_untagged_template.copy(),
                          edit_dhcp_primary_only_legacy_bios_tunnel_template.copy(),
                          edit_dhcp_legacy_bios_untagged_template.copy(),
                          edit_dhcp_legacy_bios_tunnel_template.copy(),
                          edit_dhcp_primary_only_UEFI_untagged_template.copy(),
                          edit_dhcp_primary_only_UEFI_tunnel_template.copy(),
                          edit_dhcp_UEFI_untagged_template.copy(),
                          edit_dhcp_UEFI_tunnel_template.copy(),
                          edit_dhcp_primary_only_UEFI_optimized_untagged_template.copy(),
                          edit_dhcp_primary_only_UEFI_optimized_tunnel_template.copy(),
                          edit_dhcp_UEFI_optimized_untagged_template.copy(),
                          edit_dhcp_UEFI_optimized_tunnel_template.copy(),
                          edit_dhcp_managed_volume_primary_only_legacy_bios_untagged_template.copy(),
                          edit_dhcp_managed_volume_legacy_bios_untagged_template.copy(),
                          edit_dhcp_managed_volume_primary_only_UEFI_untagged_template.copy(),
                          edit_dhcp_managed_volume_UEFI_untagged_template.copy(),
                          edit_dhcp_managed_volume_primary_only_UEFI_optimized_untagged_template.copy(),
                          edit_dhcp_managed_volume_UEFI_optimized_untagged_template.copy(),
                          ]

edit_profile_templates2 = [dhcp_primary_only_legacy_bios_untagged_template.copy(),
                           dhcp_primary_only_legacy_bios_tunnel_template.copy(),
                           dhcp_legacy_bios_untagged_template.copy(),
                           dhcp_legacy_bios_tunnel_template.copy(),
                           dhcp_primary_only_UEFI_untagged_template.copy(),
                           dhcp_primary_only_UEFI_tunnel_template.copy(),
                           dhcp_UEFI_untagged_template.copy(),
                           dhcp_UEFI_tunnel_template.copy(),
                           dhcp_primary_only_UEFI_optimized_untagged_template.copy(),
                           dhcp_primary_only_UEFI_optimized_tunnel_template.copy(),
                           dhcp_UEFI_optimized_untagged_template.copy(),
                           dhcp_UEFI_optimized_tunnel_template.copy(),
                           dhcp_managed_volume_primary_only_legacy_bios_untagged_template_edit2.copy(),
                           dhcp_managed_volume_legacy_bios_untagged_template_edit2.copy(),
                           dhcp_managed_volume_primary_only_UEFI_untagged_template_edit2.copy(),
                           dhcp_managed_volume_UEFI_untagged_template_edit2.copy(),
                           dhcp_managed_volume_primary_only_UEFI_optimized_untagged_template_edit2.copy(),
                           dhcp_managed_volume_UEFI_optimized_untagged_template_edit2.copy(),
                           ]

negative_profile_template_tasks = [
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_dhcp_with_subnetmask.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_dhcp_server_profile_template_with_subnetmask_or_gateway'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_dhcp_with_gateway.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_dhcp_server_profile_template_with_subnetmask_or_gateway'},
]

delete_profile_templates = ['dhcp_primary_only_legacy_bios_untagged_template',
                            'dhcp_primary_only_legacy_bios_tunnel_template',
                            'dhcp_legacy_bios_untagged_template',
                            'dhcp_legacy_bios_tunnel_template',
                            'dhcp_primary_only_UEFI_untagged_template',
                            'dhcp_primary_only_UEFI_tunnel_template',
                            'dhcp_UEFI_untagged_template',
                            'dhcp_UEFI_tunnel_template',
                            'dhcp_primary_only_UEFI_optimized_untagged_template',
                            'dhcp_primary_only_UEFI_optimized_tunnel_template',
                            'dhcp_UEFI_optimized_untagged_template',
                            'dhcp_UEFI_optimized_tunnel_template',
                            'dhcp_managed_volume_primary_only_legacy_bios_untagged_template',
                            'dhcp_managed_volume_legacy_bios_untagged_template',
                            'dhcp_managed_volume_primary_only_UEFI_untagged_template',
                            'dhcp_managed_volume_UEFI_untagged_template',
                            'dhcp_managed_volume_primary_only_UEFI_optimized_untagged_template',
                            'dhcp_managed_volume_UEFI_optimized_untagged_template',
                            'gen10_dhcp_managed_volume_primary_only_UEFI_untagged_template',
                            ]

negative_create_profile_with_v300 = [create_v300_profile.copy(), ]

create_profile_for_v300_verify = [enc3bay8_profile1_one_connection_untagged.copy(), ]

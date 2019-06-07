from robot.libraries.BuiltIn import BuiltIn

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

oa_credentials = {'username': 'Administrator', 'password': 'hpvse14'}

ilo_credentials = {'username': 'Administrator', 'password': 'hpvse1-ilo'}

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
SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV5'
SERVER_PROFILE_TYPE = 'ServerProfileV9'
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'
SAS_LOGICAL_INTERCONNECT_GROUP_TYPE = 'sas-logical-interconnect-groupV2'

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

# FTS, users, and licenses
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
                   'aliasDisabled': False}]}

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

network_sets = [{'name': 'NS1',
                 'type': NETWORK_SET_TYPE,
                 'networkUris': ['net100', 'net300'],
                 'nativeNetworkUri': 'net100'}
                ]

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
    {'hostname': ENC1_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'],
     'enclosureGroupUri': 'EG:' + EG1_NAME, 'force': True, 'licensingIntent': 'OneViewNoiLO'},
    {'hostname': ENC2_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'],
     'enclosureGroupUri': 'EG:' + EG2_NAME, 'force': True, 'licensingIntent': 'OneViewNoiLO'},
    {'hostname': ENC3_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'],
     'enclosureGroupUri': 'EG:' + EG3_NAME, 'force': True, 'licensingIntent': 'OneViewNoiLO'},
]

enclosures_expected = [
    {"type": ENCLOSURE_TYPE, "name": "wpst22", "state": "Configured", },
    {"type": ENCLOSURE_TYPE, "name": "wpst23", "state": "Configured", },
    {"type": ENCLOSURE_TYPE, "name": "wpst23", "state": "Configured", },
]

# ports
DownLinkPort = 'd1'
UpLinkPort = 'X3'

flex_IC_on = [{"name": ENC1ICBAY1, "uri": "IC:" + ENC1ICBAY1, "powerState": "On"}]
flex_IC_off = [{"name": ENC1ICBAY1, "uri": "IC:" + ENC1ICBAY1, "powerState": "Off"}]

disable_uplink = {
    "associatedUplinkSetUri": "us-untagged",
    "interconnectName": ENC1ICBAY1,
    "portType": "Uplink",
    "portId": "X3",
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": False,
    "portName": UpLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

enable_uplink = {
    "associatedUplinkSetUri": "us-untagged",
    "interconnectName": ENC1ICBAY1,
    "portType": "Uplink",
    "portId": "X3",
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": True,
    "portName": UpLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

disable_downlink = {
    "associatedUplinkSetUri": "us-tagged",
    "interconnectName": ENC1ICBAY1,
    "portType": "Downlink",
    "portId": "d1",
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": False,
    "portName": "d1",
    "portStatus": "Unlinked",
    "type": "port"
}

enable_downlink = {
    "associatedUplinkSetUri": "us-tagged",
    "interconnectName": ENC1ICBAY1,
    "portType": "Downlink",
    "portId": "d1",
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": True,
    "portName": "d1",
    "portStatus": "Linked",
    "type": "port"
}

profile_with_DownlinkPort_down = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": "BAY1_PROFILE1_NAME",
    "description": "",
    "affinity": "Bay",
    'connectionSettings': {
            'connections': [{"id": 1, "name": "1", "functionType": "Ethernet", "portId": "Auto",
                             "requestedMbps": "2500", "networkUri": 'ETH:net100', "ipv4": {}}]},
    "boot": {"manageBoot": False}, "bootMode": None,
    "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False,
                 "firmwareInstallType": None, "firmwareScheduleDateTime": ""},
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": None
}

bay4_profile = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": 'SH:' + ENC1SHBAY4,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": "BAY4_PROFILE1_NAME",
    "description": "",
    "affinity": "Bay",
    'connectionSettings': {
            'connections': [{"id": 1, "name": "1", "functionType": "Ethernet", "portId": "Auto",
                             "requestedMbps": "2500", "networkUri": 'ETH:network-untagged', "ipv4": {}}]},
    "boot": {"manageBoot": False}, "bootMode": None,
    "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False,
                 "firmwareInstallType": None, "firmwareScheduleDateTime": ""},
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": None
}

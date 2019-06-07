admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}

cliq_credentials = {'mgmt_ip': '16.71.149.173', 'username': 'admin', 'password': 'admin'}

LIG_NAME = 'LIG1'
RM_LIG_NAME = 'RM_LIG'
EG_NAME = 'EG_standard'
LE_NAME = 'LE1'
EG_NAME_A3 = 'EG_A3'
EG_NAME_A4 = 'EG_A4'
EG_NAME_Telco = 'EG_Telco'
RM_LE_NAME = 'RM_LE'
RM_EG_NAME = 'Remote_EG'
# Enclosures
REMOTE_ENC = 'CN744502CL'

RMENC1ICBAY3 = '%s, interconnect 3' % REMOTE_ENC
RMENC1ICBAY6 = '%s, interconnect 6' % REMOTE_ENC
# Server Hardware
RMENC1SHBAY1 = '%s, bay 1' % REMOTE_ENC
RMENC1SHBAY2 = '%s, bay 2' % REMOTE_ENC
RMENC1SHBAY3 = '%s, bay 3' % REMOTE_ENC
RMENC1SHBAY5 = '%s, bay 5' % REMOTE_ENC
RMENC1SHBAY6 = '%s, bay 6' % REMOTE_ENC

REMOTE_EG = [{'name': RM_EG_NAME,
              'type': 'EnclosureGroupV400',
              'enclosureCount': 1,
              'enclosureTypeUri': '/rest/enclosure-types/SY12000',
              'stackingMode': 'Enclosure',
              "ambientTemperatureMode": "Standard",
              'interconnectBayMappingCount': 2,
              'interconnectBayMappings':
              [
                  {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:" + RM_LIG_NAME},
                  {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:" + RM_LIG_NAME}
              ],
              'ipAddressingMode': "External",
              'ipRangeUris': [],
              'powerMode': "RedundantPowerFeed"
              }]

REMOTE_LE = [{'name': RM_LE_NAME,
              'enclosureUris': ['ENC:' + REMOTE_ENC],
              'enclosureGroupUri': "EG:" + RM_EG_NAME,
              'firmwareBaselineUri': None,
              'forceInstallFirmware': False,
              }]

# EM defaults
EM_NI = 'eth0'             # Default primary NIC.
EM_LOGIN = 'root'             # EM SSH Username
# Fusion defaults

FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
# FUSION_SSH_PASSWORD = 'hponeview'        # Fusion SSH Password

FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC
# Enclosures
ENC1 = 'CN754406XL'
ENC2 = 'CN754404R6'
ENC3 = 'CN754406WB'

# Sas Interconnects
ENC1SASICBAY1 = '%s, interconnect 1' % ENC1
ENC1SASICBAY4 = '%s, interconnect 4' % ENC1

# Potash and Chloride
ENC1ICBAY3 = '%s, interconnect 3' % ENC1  # Potash
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
ENC2ICBAY3 = '%s, interconnect 3' % ENC2  # Potash
ENC2ICBAY6 = '%s, interconnect 6' % ENC2
ENC3ICBAY3 = '%s, interconnect 3' % ENC3
ENC3ICBAY6 = '%s, interconnect 6' % ENC3

# Drive Enclosures (Bigbird)
ENC1DEBAY1 = '%s, bay 1' % ENC1

# Server Hardware
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC2SHBAY5 = '%s, bay 5' % ENC2
ENC3SHBAY1 = '%s, bay 1' % ENC3
ENC3SHBAY5 = '%s, bay 5' % ENC3

enclosures = [
    {"type": "EnclosureV400", "name": ENC1},
    {"type": "EnclosureV400", "name": ENC2},
    {"type": "EnclosureV400", "name": ENC3}
]


appliance = {
    "type": "ApplianceNetworkConfiguration",
    "applianceNetworks": [
        {"activeNode": 1, "unconfigure": False, "app1Ipv4Addr": "16.114.210.217", "app1Ipv6Addr": "",
         "app2Ipv4Addr": "16.114.210.218", "app2Ipv6Addr": "",
                         "virtIpv4Addr": "16.114.211.88", "virtIpv6Addr": None, "app1Ipv4Alias": None, "app1Ipv6Alias": None,
                         "app2Ipv4Alias": None, "app2Ipv6Alias": None, "hostname": "wpst-tbird-9-oneview.vse.rdlabs.hpecorp.net",
                         "confOneNode": True, "interfaceName": "", "macAddress": None,
                         "ipv4Type": "STATIC", "ipv6Type": "UNCONFIGURE", "overrideIpv4DhcpDnsServers": False, "ipv4Subnet": "255.255.240.0", "ipv4Gateway": "16.114.208.1", "ipv6Subnet": None, "ipv6Gateway": None,
                         "domainName": "vse.rdlabs.hpecorp.net", "searchDomains": [], "ipv4NameServers":["16.125.25.81", "16.125.25.82"],
                         "ipv6NameServers":["16.125.25.81", "16.125.25.82"], "bondedTo":None, "aliasDisabled":True,
                         "configureRabbitMqSslListener":False, "configurePostgresSslListener":False, "webServerCertificate":None,
                         "webServerCertificateChain":None, "webServerCertificateKey":None}
    ],
    "serverCertificate": {"rabbitMQCertificate": None, "rabbitMQRootCACertificate": None,
                          "rabbitMQCertificateKey": None, "postgresCertificate": None,
                          "postgresRootCACertificate": None, "postgresCertificateKey": None}
}

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'], 'locale': 'en_US.UTF-8'}

users = [{'userName': 'Serveradmin', 'password': 'wpsthpvse1', 'fullName': 'Serveradmin', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Networkadmin', 'password': 'wpsthpvse1', 'fullName': 'Networkadmin', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Backupadmin', 'password': 'wpsthpvse1', 'fullName': 'Backupadmin', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Noprivledge', 'password': 'wpsthpvse1', 'fullName': 'Noprivledge', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'}
         ]

licenses = [{'key': '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZY2-LDVV4-92DQT-L6TTW'},
            {'key': 'AA9C AQAA H9PY CHVY V7B5 HWWB Y9JL KMPL 3JKH 5FVM DXAU 2CSM GHTG L762 MTK7 FYB9 KJVT D5KM EFVW DT5J 4BEM M2SC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZXJ-RDCJQ-55T3M-BP3H2'},
            {'key': 'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
            {'key': 'AAAE BQAA H9P9 CHW2 V7B5 HWWB Y9JL KMPL SRWE 8HJU DXAU 2CSM GHTG L762 LAB2 VRJA KJVT D5KM EFVW DT5J TF9K 54C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3G7SK-QDGSY-LRT8D-PWPVP-QWRKW'},
            {'key': '9AQA BQAA H9PA GHWZ V7B5 HWWB Y9JL KMPL SR2G 7AZU DXAU 2CSM GHTG L762 69VZ USJA KJVT D5KM EFVW DT5J VFQM 85S8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3G8YL-HHGX3-6M6KH-DZ99V-BDXMM'},
            {'key': 'YAAE DQAA H9P9 GHV3 U7B5 HWW5 Y9JL KMPL CRKE 6AJU DXAU 2CSM GHTG L762 H9Z2 WUZY KJVT D5KM EFVW DT5J FFAK N5C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
            ]

ics = [
    {"name": ENC1ICBAY3, },
    {"name": ENC1ICBAY6, },
]

FA_SAN_A = 'wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55'
FA_SAN_B = 'wpstsan14.vse.rdlabs.hpecorp.net-FID101-10:00:00:27:f8:fe:0c:56'

fc_networks = [
    {'name': 'fa-a', 'autoLoginRedistribution': True, 'type': 'fc-networkV300', 'linkStabilityTime': '30', 'fabricType': 'FabricAttach', 'connectionTemplateUri': None, 'managedSanUri': 'FCSan:' + FA_SAN_A},
    {'name': 'fa-b', 'autoLoginRedistribution': True, 'type': 'fc-networkV300', 'linkStabilityTime': '30', 'fabricType': 'FabricAttach', 'connectionTemplateUri': None, 'managedSanUri': 'FCSan:' + FA_SAN_B},
]

ethernet_networks = [
    {'name': 'network-tunnel',
     'type': 'ethernet-networkV300',
     'vlanId': 0,
     'subnetUri': None,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tunnel'},
    {'name': 'network-untagged',
     'type': 'ethernet-networkV300',
     'vlanId': 0,
     'subnetUri': None,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Untagged'},
    {'name': 'net100',
     'type': 'ethernet-networkV300',
     'vlanId': 100,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'net300',
     'type': 'ethernet-networkV300',
     'vlanId': 300,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
]

network_sets = [{'name': 'NS1', 'type': 'network-setV300', 'networkUris': ['net100', 'net300'], 'nativeNetworkUri': 'net100'}, ]

RM_icmap = [
    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
]

icmap = [
    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
    {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
    {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
]

RM_uplink_sets = {'us_network-untagged': {'name': 'us-network-untagged',
                                          'ethernetNetworkType': 'Untagged',
                                          'networkType': 'Ethernet',
                                          'networkUris': ['network-untagged'],
                                          'nativeNetworkUri': None,
                                          'mode': 'Auto',
                                          'lacpTimer': 'Long',
                                          'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'},
                                                                     {'enclosure': '1', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'},
                                                                     ]
                                          },
                  'us_network-tunnel': {'name': 'us-network-tunnel',
                                        'ethernetNetworkType': 'Tunnel',
                                        'networkType': 'Ethernet',
                                        'networkUris': ['network-tunnel'],
                                        'nativeNetworkUri': None,
                                        'mode': 'Auto',
                                        'lacpTimer': 'Long',
                                        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'},
                                                                   ]
                                        },
                  'us_tagged': {'name': 'us-tagged',
                                'ethernetNetworkType': 'Tagged',
                                'networkType': 'Ethernet',
                                'networkUris': ['net300', 'net100'],
                                'nativeNetworkUri': None,
                                'mode': 'Auto',
                                'lacpTimer': 'Long',
                                'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '6', 'port': 'Q2.1', 'speed': 'Auto'},
                                                           ]
                                },
                  'fa-a': {'name': 'fa-a',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkType': 'FibreChannel',
                           'networkUris': ['fa-a'],
                           'lacpTimer': 'Long',
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q4.1', 'speed': 'Auto'},
                                                      ]
                           },
                  'fa-b': {'name': 'fa-b',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkType': 'FibreChannel',
                           'networkUris': ['fa-b'],
                           'lacpTimer': 'Long',
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '6', 'port': 'Q4.1', 'speed': 'Auto'},
                                                      ]
                           }
                  }

uplink_sets = {'us_untagged': {'name': 'us-untagged',
                               'ethernetNetworkType': 'Untagged',
                               'networkType': 'Ethernet',
                               'networkUris': ['network-untagged'],
                               'nativeNetworkUri': None,
                               'mode': 'Auto',
                               'lacpTimer': 'Long',
                               'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'},
                                                          {'enclosure': '2', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'},
                                                          ]
                               },
               'us_tagged': {'name': 'us-tagged',
                             'ethernetNetworkType': 'Tagged',
                             'networkType': 'Ethernet',
                             'networkUris': ['net100', 'net300'],
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'lacpTimer': 'Long',
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q2.1', 'speed': 'Auto'},
                                                        ]
                             },
               'us_tunnel': {'name': 'us-tunnel',
                             'ethernetNetworkType': 'Tunnel',
                             'networkType': 'Ethernet',
                             'networkUris': ['network-tunnel'],
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'lacpTimer': 'Long',
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q3.1', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q3.1', 'speed': 'Auto'},
                                                        ]
                             },
               }

ligs = [
    {'name': RM_LIG_NAME,
     'type': 'logical-interconnect-groupV300',
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': RM_icmap,
     'enclosureIndexes': [1],
     'interconnectBaySet': 3,
     'redundancyType': 'Redundant',
     'ethernetSettings': None,
     'fcoeSettings': {'fcoeMode': 'FcfNpv'},
     'stackingMode': 'Enclosure',
     'state': 'Active',
     'telemetryConfiguration': None,
     'snmpConfiguration': None,
     'uplinkSets': [RM_uplink_sets['us_network-untagged'].copy(), RM_uplink_sets['us_network-tunnel'].copy(), RM_uplink_sets['us_tagged'].copy(), RM_uplink_sets['fa-a'].copy(), RM_uplink_sets['fa-b'].copy()]
     },
    {'name': LIG_NAME,
     'type': 'logical-interconnect-groupV300',
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': icmap,
     'enclosureIndexes': [1, 2, 3],
     'interconnectBaySet': 3,
     'redundancyType': 'HighlyAvailable',
     'fcoeSettings': {'fcoeMode': 'FcfNpv'},
     'stackingMode': 'Enclosure',
     'ethernetSettings': None,
     'state': 'Linked',
     'telemetryConfiguration': None,
     'snmpConfiguration': None,
     'uplinkSets': [uplink_sets['us_untagged'].copy(), uplink_sets['us_tagged'].copy(), uplink_sets['us_tunnel'].copy(), ],
     }
]


les = [{'name': LE_NAME,
        'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
        'enclosureGroupUri': "EG:" + EG_NAME,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False}
       ]

egs = [{'name': EG_NAME,
        'type': 'EnclosureGroupV400',
        'enclosureCount': 3,
        'enclosureTypeUri': '/rest/enclosure-types/SY12000',
        'stackingMode': 'Enclosure',
        "ambientTemperatureMode": "Standard",
        'interconnectBayMappingCount': 2,
        'interconnectBayMappings':
        [
                {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
                {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME}
        ],
        'ipAddressingMode': "External",
        'ipRangeUris': [],
        'powerMode': "RedundantPowerFeed"
        }]
Telco_EGs = [{'name': EG_NAME,
              'type': 'EnclosureGroupV400',
              'enclosureCount': 3,
              'enclosureTypeUri': '/rest/enclosure-types/SY12000',
              'stackingMode': 'Enclosure',
              "ambientTemperatureMode": "Standard",
              'interconnectBayMappingCount': 2,
              'interconnectBayMappings':
              [
                  {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
                  {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME}
              ],
              'ipAddressingMode': "External",
              'ipRangeUris': [],
              'powerMode': "RedundantPowerFeed"
              },
             {'name': EG_NAME_A3,
              'type': 'EnclosureGroupV400',
              'enclosureCount': 3,
              'enclosureTypeUri': '/rest/enclosure-types/SY12000',
              'stackingMode': 'Enclosure',
              "ambientTemperatureMode": "ASHRAE_A3",
              'interconnectBayMappingCount': 2,
              'interconnectBayMappings':
              [
                  {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
                  {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME}
              ],
              'ipAddressingMode': "External",
              'ipRangeUris': [],
              'powerMode': "RedundantPowerFeed"
              },
             {'name': EG_NAME_A4,
              'type': 'EnclosureGroupV400',
              'enclosureCount': 3,
              'enclosureTypeUri': '/rest/enclosure-types/SY12000',
              'stackingMode': 'Enclosure',
              "ambientTemperatureMode": "ASHRAE_A4",
              'interconnectBayMappingCount': 2,
              'interconnectBayMappings':
              [
                  {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
                  {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME}
              ],
              'ipAddressingMode': "External",
              'ipRangeUris': [],
              'powerMode': "RedundantPowerFeed"
              },
             {'name': EG_NAME_Telco,
              'type': 'EnclosureGroupV400',
              'enclosureCount': 3,
              'enclosureTypeUri': '/rest/enclosure-types/SY12000',
              'stackingMode': 'Enclosure',
              "ambientTemperatureMode": "Telco",
              'interconnectBayMappingCount': 2,
              'interconnectBayMappings':
              [
                  {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
                  {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME}
              ],
              'ipAddressingMode': "External",
              'ipRangeUris': [],
              'powerMode': "RedundantPowerFeed"
              }

             ]

ambient_temp_mode = ['Standard', 'Telco', 'ASHRAE_A4', 'ASHRAE_A3']

les_ASHRAE_A3 = [{'name': LE_NAME,
                  'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
                  'enclosureGroupUri': "EG:" + EG_NAME_A3,
                  'firmwareBaselineUri': None,
                  'forceInstallFirmware': False,
                  }]

verify_les_ASHRAE_A3 = [{'name': LE_NAME,
                         'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
                         'enclosureGroupUri': "EG:" + EG_NAME_A3,
                         'ambientTemperatureMode': 'ASHRAE_A3',
                         'type': 'LogicalEnclosureV400',
                         }]

EDIT_LE_EG_A4 = {'name': LE_NAME,
                 'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
                 'enclosureGroupUri': "EG:" + EG_NAME_A3,
                 'firmwareBaselineUri': None,
                 'forceInstallFirmware': False,
                 'ambientTemperatureMode': 'ASHRAE_A4',
                 'type': 'LogicalEnclosureV400',
                 }

VERIFY_EDIT_LE_EG_A4 = [{'name': LE_NAME,
                         'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
                         'enclosureGroupUri': "EG:" + EG_NAME_A3,
                         'ambientTemperatureMode': 'ASHRAE_A4',
                         'type': 'LogicalEnclosureV400',
                         }]

EDIT_LE_TELCO = {'name': LE_NAME,
                 'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
                 'enclosureGroupUri': "EG:" + EG_NAME_A3,
                 'ambientTemperatureMode': 'Telco',
                 'type': 'LogicalEnclosureV400',
                 }

EDIT_LE_A3 = {'name': LE_NAME,
              'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
              'enclosureGroupUri': "EG:" + EG_NAME_A3,
              'ambientTemperatureMode': 'ASHRAE_A3',
              'type': 'LogicalEnclosureV400',
              }

VERIFY_EDIT_LE_TELCO = [{'name': LE_NAME,
                         'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
                         'enclosureGroupUri': "EG:" + EG_NAME_A3,
                         'ambientTemperatureMode': 'Telco',
                         'type': 'LogicalEnclosureV400',
                         }]

EDIT_LE_TELCO_INCONSISTENT = {'name': LE_NAME,
                              'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
                              'enclosureGroupUri': "EG:" + EG_NAME_A3,
                              'ambientTemperatureMode': 'Telco',
                              'type': 'LogicalEnclosureV400',
                              }

EDIT_EG_ASHRAE_A4 = {'name': EG_NAME_A3,
                     'type': 'EnclosureGroupV400',
                     'enclosureCount': 3,
                     'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                     'stackingMode': 'Enclosure',
                     "ambientTemperatureMode": "ASHRAE_A4",
                     'interconnectBayMappingCount': 2,
                     'interconnectBayMappings':
                     [
                         {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
                         {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME}
                     ],
                     'ipAddressingMode': "External",
                     'ipRangeUris': [],
                     'powerMode': "RedundantPowerFeed"
                     }

EDIT_EG_Telco = {'name': EG_NAME_A3,
                 'type': 'EnclosureGroupV400',
                 'enclosureCount': 3,
                 'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                 'stackingMode': 'Enclosure',
                 "ambientTemperatureMode": "Telco",
                 'interconnectBayMappingCount': 2,
                 'interconnectBayMappings':
                 [
                     {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
                     {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME}
                 ],
                 'ipAddressingMode': "External",
                 'ipRangeUris': [],
                 'powerMode': "RedundantPowerFeed"
                 }

ris_node_enc1bay3 = [{
    "server": ENC1SHBAY3,
    "username": ilo_credentials['username'],
    "password":ilo_credentials['password'],
    "path":"/rest/v1/Systems/1/bios/settings",
    "validate":{
        "Description": "This is the Platform/BIOS Configuration (RBSU) Pending Settings",
        'ExtendedAmbientTemp': 'ASHRAE3'}
}]

ris_node_enc2bay1_A3 = [{
    "server": ENC2SHBAY1,
    "username": ilo_credentials['username'],
    "password":ilo_credentials['password'],
    "path":"/rest/v1/Systems/1/bios/settings",
    "validate":{
        "Description": "This is the Platform/BIOS Configuration (RBSU) Pending Settings",
        'ExtendedAmbientTemp': 'ASHRAE3'}
}]

ris_node_enc2bay1_A4 = [{
    "server": ENC2SHBAY1,
    "username": ilo_credentials['username'],
    "password":ilo_credentials['password'],
    "path":"/rest/v1/Systems/1/bios/settings",
    "validate":{
        "Description": "This is the Platform/BIOS Configuration (RBSU) Pending Settings",
        'ExtendedAmbientTemp': 'ASHRAE4'}
}]

ris_node_enc1bay5_Telco = [{
    "server": ENC1SHBAY5,
    "username": ilo_credentials['username'],
    "password":ilo_credentials['password'],
    "path":"/rest/v1/Systems/1/bios/settings",
    "validate":{
        "Description": "This is the Platform/BIOS Configuration (RBSU) Pending Settings",
        'ExtendedAmbientTemp': 'Disabled'}
}]

ris_node_enc3bay1 = [{
    "server": ENC3SHBAY1,
    "username": ilo_credentials['username'],
    "password":ilo_credentials['password'],
    "path":"/rest/v1/Systems/1/bios/settings",
    "validate":{
        "Description": "This is the Platform/BIOS Configuration (RBSU) Pending Settings",
        'ExtendedAmbientTemp': 'ASHRAE4'}
}]

ris_node_enc3bay5 = {
    "server": ENC3SHBAY5,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/rest/v1/Systems/1/bios/settings",
    "validate": {
        "Description": "This is the Platform/BIOS Configuration (RBSU) Pending Settings",
        'ExtendedAmbientTemp': 'ASHRAE4'}
}

# ts1_ris_nodes_after_create = [ ris_node_enc1bay1.copy(),
#                               ris_node_enc1bay2.copy(),
#                               ris_node_enc1bay3.copy(),
#                               ris_node_enc1bay6.copy(),
#                               ]

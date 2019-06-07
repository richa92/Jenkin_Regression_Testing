admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

appliance = {
    "type": "ApplianceNetworkConfiguration",
    "applianceNetworks": [
        {"activeNode": 1, "unconfigure": False, "app1Ipv4Addr": "16.114.213.32", "app1Ipv6Addr": "",
         "app2Ipv4Addr": "16.114.213.33", "app2Ipv6Addr": "",
                         "virtIpv4Addr": "16.114.213.31", "virtIpv6Addr": None, "app1Ipv4Alias": None, "app1Ipv6Alias": None,
                         "app2Ipv4Alias": None, "app2Ipv6Alias": None, "hostname": "wpst-31.vse.rdlabs.hpecorp.net",
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
            {'key': '9CTC C9MA H9PY CHUY V7B5 HWWB Y9JL KMPL VACE 8GRE DXAU 2CSM GHTG L762 7RGY XHBE KJVT D5KM EFVW DT5J VX79 5T22 AK2P 3EW2 9JA6 XUNV TZZH MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEC 3F9V JQY5 "423542193 HPOV-NFR1 HP_OneView_16_Seat_NFR 9UH2JJECJ4AA"_3JNDQ-Z35J3-D6T6M-5XKZL-WC2W2'},
            {'key': 'YBLG B99A H9PQ 8HVZ U7B5 HWW5 Y9JL KMPL VAWA 8CBE DXAU 2CSM GHTG L762 5NW5 HDV4 KJVT D5KM EFVW DT5J VXP8 4XK2 GNSL 9F82 7JKT QVXB XZKH ABB4 NV2C LHXU KN7U 5NA6 BKRK 35QB D8UW R42A X3BN LQ6M 5V9A PM6Q 4MN9 9GGS EZU7 GEMX VUJW CDB5 JVRX 8HEN 2J98 ACPB "TKOPREN HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR JJADJJEDATCA"'},
            ]

# Enclosures
ENC1 = '0000A66101'
ENC2 = '0000A66102'
ENC3 = '0000A66103'
# Interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
ENC2ICBAY3 = '%s, interconnect 3' % ENC2
ENC2ICBAY6 = '%s, interconnect 6' % ENC2
ENC3ICBAY3 = '%s, interconnect 3' % ENC3
ENC3ICBAY6 = '%s, interconnect 6' % ENC3
# Sas Interconnects
ENC1SASICBAY1 = '%s, interconnect 1' % ENC1
ENC1SASICBAY4 = '%s, interconnect 4' % ENC1
ENC2SASICBAY1 = '%s, interconnect 1' % ENC2
ENC2SASICBAY4 = '%s, interconnect 4' % ENC2
ENC3SASICBAY1 = '%s, interconnect 1' % ENC3
ENC3SASICBAY4 = '%s, interconnect 4' % ENC3
# Drive Enclosures (Bigbird)
ENC1DEBAY1 = '%s, bay 1' % ENC1
ENC1DEBAY7 = '%s, bay 7' % ENC1
ENC2DEBAY1 = '%s, bay 1' % ENC2
ENC2DEBAY7 = '%s, bay 7' % ENC2
ENC3DEBAY1 = '%s, bay 1' % ENC3
ENC3DEBAY7 = '%s, bay 7' % ENC3
# Server Hardware
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY4 = '%s, bay 4' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1
ENC1SHBAY9 = '%s, bay 9' % ENC1
ENC1SHBAY10 = '%s, bay 10' % ENC1
ENC1SHBAY11 = '%s, bay 11' % ENC1
ENC1SHBAY12 = '%s, bay 12' % ENC1
ENC2SHBAY3 = '%s, bay 3' % ENC2
ENC2SHBAY4 = '%s, bay 4' % ENC2
ENC2SHBAY5 = '%s, bay 5' % ENC2
ENC2SHBAY6 = '%s, bay 6' % ENC2
ENC2SHBAY9 = '%s, bay 9' % ENC2
ENC2SHBAY10 = '%s, bay 10' % ENC2
ENC2SHBAY11 = '%s, bay 11' % ENC2
ENC2SHBAY12 = '%s, bay 12' % ENC2
ENC3SHBAY3 = '%s, bay 3' % ENC3
ENC3SHBAY4 = '%s, bay 4' % ENC3
ENC3SHBAY5 = '%s, bay 5' % ENC3
ENC3SHBAY6 = '%s, bay 6' % ENC3
ENC3SHBAY9 = '%s, bay 9' % ENC3
ENC3SHBAY10 = '%s, bay 10' % ENC3
ENC3SHBAY11 = '%s, bay 11' % ENC3
ENC3SHBAY12 = '%s, bay 12' % ENC3

enclosures = [
    {"type": "EnclosureV300", "name": ENC1, },
    {"type": "EnclosureV300", "name": ENC2, },
    {"type": "EnclosureV300", "name": ENC3, },
]

sasics = [
    {"name": ENC1SASICBAY1, },
    {"name": ENC2SASICBAY1, },
    {"name": ENC3SASICBAY1, },
    {"name": ENC1SASICBAY4, },
    {"name": ENC2SASICBAY4, },
    {"name": ENC3SASICBAY4, },
]

sasics_bay1 = [
    {"name": ENC1SASICBAY1, },
    {"name": ENC2SASICBAY1, },
    {"name": ENC3SASICBAY1, },
]

sasics_bay4 = [
    {"name": ENC1SASICBAY4, },
    {"name": ENC2SASICBAY4, },
    {"name": ENC3SASICBAY4, },

]

ics = [
    {"name": ENC1ICBAY3, },
    {"name": ENC1ICBAY6, },
    {"name": ENC2ICBAY3, },
    {"name": ENC2ICBAY6, },
    {"name": ENC3ICBAY3, },
    {"name": ENC3ICBAY6, },
]

ethernet_networks = [{'name': 'net100',
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

icmap = [
    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
    {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
    {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
]

uplink_sets = {'us_ethernet': {'name': 'us_ethernet',
                               'ethernetNetworkType': 'Tagged',
                               'networkType': 'Ethernet',
                               'networkUris': ['net100', 'net300'],
                               'nativeNetworkUri': None,
                               'mode': 'Auto',
                               'lacpTimer': 'Long',
                               'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'},
                                                          ]
                               },
               }

ligs = [
    {'name': 'LIG1',
     'type': 'logical-interconnect-groupV300',
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': icmap,
     'enclosureIndexes': [1, 2, 3],
     'interconnectBaySet': 3,
     'redundancyType': 'HighlyAvailable',
     'ethernetSettings': None,
     'fcoeSettings': {'fcoeMode': 'FcfNpv'},
     'stackingMode': 'Enclosure',
     'ethernetSettings': None,
     'state': 'Active',
     'telemetryConfiguration': None,
     'snmpConfiguration': None,
     'uplinkSets': [uplink_sets['us_ethernet'].copy()],
     }
]

sasligs = [
    {'name': 'SASLIG1',  # Single SAS switch
             "type": "sas-logical-interconnect-group",
             "enclosureType": "SY12000",
             "enclosureIndexes": [1],
             "interconnectBaySet": "1",
             'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'Synergy 12Gb SAS Connection Module'},
                                         ],
     }
]

edit_sasligs = [
    {'name': 'SASLIG1',  # Dual SAS switch
             "type": "sas-logical-interconnect-group",
     "enclosureType": "SY12000",
     "enclosureIndexes": [1],
     "interconnectBaySet": "1",
     'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'Synergy 12Gb SAS Connection Module'},
                                 {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'Synergy 12Gb SAS Connection Module'},
                                 ],
     }
]

egs = [{'name': 'EG1',
        'type': 'EnclosureGroupV300',
        'enclosureCount': 3,
        'enclosureTypeUri': '/rest/enclosure-types/SY12000',
        'stackingMode': 'Enclosure',
        'interconnectBayMappingCount': 2,
        'configurationScript': None,
        'interconnectBayMappings':
        [
                {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:LIG1"},
                {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:LIG1"}
        ],
        'ipAddressingMode': "External",
        'ipRangeUris': [],
        'powerMode': "RedundantPowerFeed"
        }
       ]

edit_egs = [{'name': 'EG1',
             'type': 'EnclosureGroupV300',
             'enclosureCount': 3,
             'enclosureTypeUri': '/rest/enclosure-types/SY12000',
             'stackingMode': 'Enclosure',
             'interconnectBayMappingCount': 3,
             'configurationScript': None,
             'interconnectBayMappings':
             [{"interconnectBay": 1, "logicalInterconnectGroupUri": "SASLIG:SASLIG1"},
              {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:LIG1"},
              {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:LIG1"}
              ],
             'ipAddressingMode': "External",
             'ipRangeUris': [],
             'powerMode': "RedundantPowerFeed"
             }
            ]

les = [{'name': 'LE1',
        'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
        'enclosureGroupUri': 'EG:EG1',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }]

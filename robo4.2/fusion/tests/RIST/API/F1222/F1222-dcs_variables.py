admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
server_credentials = {'userName': 'Serveradmin', 'password': 'wpsthpvse1'}
network_credentials = {'userName': 'Networkadmin', 'password': 'wpsthpvse1'}
storage_credentials = {'userName': 'storageadmin', 'password': 'wpsthpvse1'}

appliance = {"type": "ApplianceNetworkConfiguration",
             "applianceNetworks": [{"activeNode": 1, "unconfigure": False, "app1Ipv4Addr": "16.114.213.95", "app1Ipv6Addr": "",
                                    "app2Ipv4Addr": "16.114.213.96", "app2Ipv6Addr": "",
                                    "virtIpv4Addr": "16.114.213.94", "virtIpv6Addr": None, "app1Ipv4Alias": None, "app1Ipv6Alias": None,
                                    "app2Ipv4Alias": None, "app2Ipv6Alias": None, "hostname": "hung-dcs.vse.rdlabs.hpecorp.net",
                                    "confOneNode": True, "interfaceName": "", "macAddress": None,
                                    "ipv4Type": "STATIC", "ipv6Type": "UNCONFIGURE", "overrideIpv4DhcpDnsServers": False,
                                    "ipv4Subnet": "255.255.240.0", "ipv4Gateway": "16.114.208.1", "ipv6Subnet": None, "ipv6Gateway": None,
                                    "domainName": "vse.rdlabs.hpecorp.net", "searchDomains": [], "ipv4NameServers":["16.125.25.81", "16.125.25.82"],
                                    "ipv6NameServers":["16.125.25.81", "16.125.25.82"], "bondedTo":None, "aliasDisabled":True,
                                    "configureRabbitMqSslListener":False, "configurePostgresSslListener":False, "webServerCertificate":None,
                                    "webServerCertificateChain":None, "webServerCertificateKey":None}
                                   ],
             "serverCertificate": {"rabbitMQCertificate": None, "rabbitMQRootCACertificate": None,
                                   "rabbitMQCertificateKey": None, "postgresCertificate": None,
                                   "postgresRootCACertificate": None, "postgresCertificateKey": None}
             }

users = [{'userName': 'Serveradmin', 'password': 'wpsthpvse1', 'fullName': 'Serveradmin', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Networkadmin', 'password': 'wpsthpvse1', 'fullName': 'Networkadmin', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Backupadmin', 'password': 'wpsthpvse1', 'fullName': 'Backupadmin', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Noprivledge', 'password': 'wpsthpvse1', 'fullName': 'Noprivledge', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'}
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

icmap = [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
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

ligs = [{'name': 'LIG1',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap,
         'enclosureIndexes': [1, 2, 3],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'ethernetSettings': None,
         'fcoeSettings': {'fcoeMode': 'FcfNpv'},
         'stackingMode': 'Enclosure',
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'uplinkSets': [uplink_sets['us_ethernet'].copy()],
         }
        ]

sasligs = [{'name': 'SASLIG1',  # Single SAS switch
            "type": "sas-logical-interconnect-group",
            "enclosureType": "SY12000",
            "enclosureIndexes": [1],
            "interconnectBaySet": "1",
            'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'Synergy 12Gb SAS Connection Module'},
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


profile_templates = [{'type': 'ServerProfileTemplateV2',
                      'serverProfileDescription': 'change SHT-rack server',
                      'serverHardwareTypeUri': 'SHT:DL360p Gen8 1',
                      'serialNumberType': 'Physical',
                      'macType': 'Physical',
                      'wwnType': 'Physical',
                      'name': 'change_sht-DL',
                      'description': 'change SHT-rack server',
                      'connections': [],
                      "boot": {
                          "manageBoot": True,
                          "order": [
                              "Floppy",
                              "PXE",
                              "USB",
                              "HardDisk",
                              "CD"
                          ]
                      },
                      "bios": {
                          "manageBios": True,
                          "overriddenSettings": [
                              {
                                  "id": "64",
                                  "value": "1"
                              }
                          ]
                      },
                      "localStorage": {
                          "sasLogicalJBODs": [],
                          "controllers": []
                      },
                      "sanStorage": {
                          "manageSanStorage": False,
                          "volumeAttachments": []
                      }},
                     {
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-blade server',
    'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                     'enclosureGroupUri': 'EG:mixed-eg1',
                     'serialNumberType': 'Virtual',
                     'macType': 'Virtual',
                     'wwnType': 'Virtual',
                     'name': 'change-sht-blade server',
                     'description': 'change-sht-blade server',
                     'affinity': 'Bay',
                     'connections': [{
                                     'id': 1,
                                     'name': '',
                                     'functionType': 'Ethernet',
                                     'portId': 'Flb 1:1-a',
                                     'requestedMbps': '2500',
                                     'networkUri': 'ETH:deployment',
                                     'requestedVFs': 'Auto'
                                     }
                                     ],
                     "boot": {
                         "manageBoot": True,
                         "order": [
                             "Floppy",
                             "HardDisk",
                             "USB",
                             "CD",
                             "PXE"
                         ]
                     },

                     "bios": {
                         "manageBios": True,
                         "overriddenSettings": [
                             {
                                 "id": "64",
                                 "value": "1"
                             }
                         ]
                     },
                     "localStorage": {
                         "sasLogicalJBODs": [],
                         "controllers": []
                     },
                     "sanStorage": {
                         "manageSanStorage": False,
                         "volumeAttachments": []
                     }},
                     {
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-blade server to dl server - Virtual Addresses',
    'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                     'enclosureGroupUri': 'EG:mixed-eg1',
                     'serialNumberType': 'Virtual',
                     'macType': 'Virtual',
                     'wwnType': 'Virtual',
                     'name': 'change-sht-blade server to dl server-Virtual',
                     'description': 'change-sht-blade server to dl server',
                     'affinity': 'Bay',
                     'connections': [{
                                     'id': 1,
                                     'name': '',
                                     'functionType': 'Ethernet',
                                     'portId': 'Flb 1:1-a',
                                     'requestedMbps': '2500',
                                     'networkUri': 'ETH:deployment',
                                     'requestedVFs': 'Auto'
                                     }
                                     ],
                     "boot": {
                         "manageBoot": True,
                         "order": [
                             "Floppy",
                             "PXE",
                             "USB",
                             "HardDisk",
                             "CD"
                         ]
                     },

                     "bios": {
                         "manageBios": True,
                         "overriddenSettings": [
                             {
                                 "id": "67",
                                 "value": "1"
                             }
                         ]
                     },
                     "localStorage": {
                         "sasLogicalJBODs": [],
                         "controllers": []
                     },
                     "sanStorage": {
                         "manageSanStorage": False,
                         "volumeAttachments": []
                     }},
                     {
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-blade server to dl server-Physical Addresses',
    'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                     'enclosureGroupUri': 'EG:mixed-eg1',
                     'serialNumberType': 'Physical',
                     'macType': 'Physical',
                     'wwnType': 'Physical',
                     'name': 'change-sht-blade server to dl server-Physical',
                     'description': 'change-sht-blade server to dl server',
                     'affinity': 'Bay',
                     'connections': [{
                                     'id': 1,
                                     'name': '',
                                     'functionType': 'Ethernet',
                                     'portId': 'Flb 1:1-a',
                                     'requestedMbps': '2500',
                                     'networkUri': 'ETH:deployment',
                                     'requestedVFs': 'Auto'
                                     }
                                     ],
                     "boot": {
                         "manageBoot": True,
                         "order": [
                             "Floppy",
                             "PXE",
                             "USB",
                             "HardDisk",
                             "CD"
                         ]
                     },

                     "bios": {
                         "manageBios": True,
                         "overriddenSettings": [
                             {
                                 "id": "67",
                                 "value": "1"
                             }
                         ]
                     },
                     "localStorage": {
                         "sasLogicalJBODs": [],
                         "controllers": []
                     },
                     "sanStorage": {
                         "manageSanStorage": False,
                         "volumeAttachments": []
                     }},
                     {
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-blade server to dl server-Physical Addresses',
    'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                     'enclosureGroupUri': 'EG:mixed-eg1',
                     'serialNumberType': 'Physical',
                     'macType': 'Physical',
                     'wwnType': 'Physical',
                     'name': 'change-sht-blade server to dl server-Physical2',
                     'description': 'change-sht-blade server to dl server',
                     'affinity': 'Bay',
                     'connections': [{
                                     'id': 1,
                                     'name': '',
                                     'functionType': 'Ethernet',
                                     'portId': 'Flb 1:1-a',
                                     'requestedMbps': '2500',
                                     'networkUri': 'ETH:deployment',
                                     'requestedVFs': 'Auto'
                                     }
                                     ],
                     "boot": {
                         "manageBoot": True,
                         "order": [
                             "Floppy",
                             "PXE",
                             "USB",
                             "HardDisk",
                             "CD"
                         ]
                     },

                     "bios": {
                         "manageBios": True,
                         "overriddenSettings": [
                             {
                                 "id": "67",
                                 "value": "1"
                             }
                         ]
                     },
                     "localStorage": {
                         "sasLogicalJBODs": [],
                         "controllers": []
                     },
                     "sanStorage": {
                         "manageSanStorage": False,
                         "volumeAttachments": []
                     }},
                     {
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-dl server to bl server',
    'serverHardwareTypeUri': 'SHT:DL360p Gen8 1',
                     'serialNumberType': 'Physical',
                     'macType': 'Physical',
                     'wwnType': 'Physical',
                     'name': 'change-sht-dl server to bl server',
                     'description': 'change-sht-dl server to bl server',
                     'connections': [],
                     "boot": {
                         "manageBoot": True,
                         "order": [
                             "Floppy",
                             "PXE",
                             "USB",
                             "HardDisk",
                             "CD"
                         ]
                     },

                     "bios": {
                         "manageBios": True,
                         "overriddenSettings": [
                             {
                                 "id": "64",
                                 "value": "1"
                             }
                         ]
                     },
                     "localStorage": {
                         "sasLogicalJBODs": [],
                         "controllers": []
                     },
                     "sanStorage": {
                         "manageSanStorage": False,
                         "volumeAttachments": []
                     }},

                     {
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-and eg',
    'serverHardwareTypeUri': 'SHT:BL660c Gen8 1',
                     'enclosureGroupUri': "EG:mixed-eg2",
                     'serialNumberType': 'Physical',
                     'macType': 'Physical',
                     'wwnType': 'Physical',
                     'name': 'change-sht-and eg',
                     'description': 'change-sht-and eg',
                     'affinity': 'Bay',
                     'connections': [],
                     "boot": {
                         "manageBoot": True,
                         "order": [
                             "Floppy",
                             "PXE",
                             "USB",
                             "HardDisk",
                             "CD"
                         ]
                     },

                     "bios": {
                         "manageBios": True,
                         "overriddenSettings": [
                             {
                                 "id": "64",
                                 "value": "1"
                             }
                         ]
                     },
                     "localStorage": {
                         "sasLogicalJBODs": [],
                         "controllers": []
                     },
                     "sanStorage": {
                         "manageSanStorage": False,
                         "volumeAttachments": []
                     }},
                     {
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change eg',
    'serverHardwareTypeUri': 'SHT:BL660c Gen8 1',
                     'enclosureGroupUri': "EG:mixed-eg2",
                     'serialNumberType': 'Physical',
                     'macType': 'Physical',
                     'wwnType': 'Physical',
                     'name': 'change eg',
                     'description': 'change eg',
                     'affinity': 'Bay',
                     'connections': [],
                     "boot": {
                         "manageBoot": True,
                         "order": [
                             "Floppy",
                             "PXE",
                             "USB",
                             "HardDisk",
                             "CD"
                         ]
                     },

                     "bios": {
                         "manageBios": True,
                         "overriddenSettings": [
                             {
                                 "id": "64",
                                 "value": "1"
                             }
                         ]
                     },
                     "localStorage": {
                         "sasLogicalJBODs": [],
                         "controllers": []
                     },
                     "sanStorage": {
                         "manageSanStorage": False,
                         "volumeAttachments": []
                     }},
                     ]


edit_sht_templates = [{'type': 'ServerProfileTemplateV2',
                       'serverProfileDescription': 'change SHT-rack server',
                       'serverHardwareTypeUri': 'SHT:DL380p Gen8 1',
                       'serialNumberType': 'Physical',
                       'macType': 'Physical',
                       'wwnType': 'Physical',
                       'name': 'change_sht-DL',
                       'description': 'change SHT-rack server',
                       'connections': [],
                       "boot": {
                           "manageBoot": True,
                           "order": [
                                  "Floppy",
                                  "PXE",
                                  "USB",
                               "HardDisk",
                               "CD"
                           ]},
                       "localStorage": {
                           "sasLogicalJBODs": [],
                           "controllers": []
                       },
                       "sanStorage": {
                           "manageSanStorage": False,
                           "volumeAttachments": []
                       }},
                      {
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-blade server',
    'serverHardwareTypeUri': 'SHT:BL465c Gen8 1',
    'enclosureGroupUri': 'EG:mixed-eg1',
    'serialNumberType': 'Virtual',
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'name': 'change-sht-blade server',
    'description': 'change-sht-blade server',
    'affinity': 'Bay',
    'connections': [{
        'id': 1,
        'name': '',
        'functionType': 'Ethernet',
        'portId': 'Flb 1:1-a',
        'requestedMbps': '2500',
        'networkUri': 'ETH:deployment',
        'requestedVFs': 'Auto'
    }
    ],
    "boot": {
        "manageBoot": True,
        "order": [
            "Floppy",
            "PXE",
            "USB",
            "HardDisk",
            "CD"
        ]}}]

edit_sht_rack_and_blade_templates = [
    {
        'type': 'ServerProfileTemplateV2',
        'serverProfileDescription': 'change-sht-blade server to dl server',
        'serverHardwareTypeUri': 'SHT:DL360p Gen8 1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'change-sht-blade server to dl server-Physical2',
        'description': 'hange-sht-dl server to bl server',
        'connections': [],
        "boot": {
            "manageBoot": True,
            "order": [
                "Floppy",
                "PXE",
                "USB",
                "HardDisk",
                "CD"
            ]
        },

        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "67",
                    "value": "1"
                }
            ]
        }},
    {
        'type': 'ServerProfileTemplateV2',
        'serverProfileDescription': 'change-sht-dl server to bl server',
        'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
        'enclosureGroupUri': 'EG:mixed-eg1',
        'affinity': 'Bay',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'change-sht-blade server to dl server-Physical',
        'description': 'change-sht-dl server to bl server',
        'connections': [],
        "boot": {
            "manageBoot": True,
            "order": [
                "Floppy",
                "PXE",
                "USB",
                "HardDisk",
                "CD"
            ]
        },

        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "64",
                    "value": "1"
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
        }}]

edit_eg_templates = [
    {
        'type': 'ServerProfileTemplateV2',
        'serverProfileDescription': 'change eg',
        'serverHardwareTypeUri': 'SHT:BL660c Gen8 1',
        'enclosureGroupUri': "EG:mixed-eg1",
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'change eg',
        'description': 'change eg',
        'affinity': 'Bay',
        'connections': [],
        "boot": {
            "manageBoot": True,
            "order": [
                "Floppy",
                "PXE",
                "USB",
                "HardDisk",
                "CD"
            ]
        },

        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "64",
                    "value": "1"
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
        }},

    {
        'type': 'ServerProfileTemplateV2',
        'serverProfileDescription': 'change-sht-and eg',
        'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
        'enclosureGroupUri': "EG:mixed-eg1",
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'change-sht-and eg',
        'description': 'change-sht-and eg',
        'affinity': 'Bay',
        'connections': [],
        "boot": {
            "manageBoot": True,
            "order": [
                "Floppy",
                "PXE",
                "USB",
                "HardDisk",
                "CD"
            ]
        },

        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "64",
                    "value": "1"
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
        }}
]

auth_test_edit_eg_templates = {
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-and eg',
    'serverHardwareTypeUri': 'SHT:BL465c Gen8 1',
    'enclosureGroupUri': "EG:mixed-eg2",
    'serialNumberType': 'Physical',
    'macType': 'Physical',
    'wwnType': 'Physical',
    'name': 'change-sht-and eg',
    'description': 'change-sht-and eg',
    'affinity': 'Bay',
    'connections': [],
    "boot": {
        "manageBoot": True,
        "order": [
            "Floppy",
            "PXE",
            "USB",
            "HardDisk",
            "CD"
        ]
    },

    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "64",
                "value": "5"
            }
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    }}

transformation_edit_eg_templates = [{
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-and eg',
    'serverHardwareTypeUri': 'SHT:BL460c G7 1',
    'enclosureGroupUri': "EG:mixed-eg2",
    'serialNumberType': 'Physical',
    'macType': 'Physical',
    'wwnType': 'Physical',
    'name': 'change-sht-and eg',
    'description': 'change-sht-and eg',
    'affinity': 'Bay',
    'connections': [],
    "boot": {
        "manageBoot": True,
        "order": [
            "Floppy",
            "PXE",
            "USB",
            "HardDisk",
            "CD"
        ]
    },

    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    }}]

invalid_eg_edit_template = {
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-and eg',
    'serverHardwareTypeUri': 'SHT:BL465c Gen8 1',
    'enclosureGroupUri': "/rest/enclosure-groups/5f275fb2-f74c-4992-a761-54ee58391111",
    'serialNumberType': 'Physical',
    'macType': 'Physical',
    'wwnType': 'Physical',
    'name': 'change-sht-and eg',
    'description': 'change-sht-and eg',
    'affinity': 'Bay',
    'connections': [],
    "boot": {
        "manageBoot": True,
        "order": [
            "Floppy",
            "PXE",
            "USB",
            "HardDisk",
            "CD"
        ]
    },

    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "64",
                "value": "5"
            }
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    }}

invalid_sht_edit_template = {
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-and eg',
    'serverHardwareTypeUri': "/rest/server-hardware-types/5f275fb2-f74c-4992-a761-54ee58391111",
    'enclosureGroupUri': "EG:mixed-eg2",
    'serialNumberType': 'Physical',
    'macType': 'Physical',
    'wwnType': 'Physical',
    'name': 'change-sht-and eg',
    'description': 'change-sht-and eg',
    'affinity': 'Bay',
    'connections': [],
    "boot": {
        "manageBoot": True,
        "order": [
            "Floppy",
            "PXE",
            "USB",
            "HardDisk",
            "CD"
        ]
    },

    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "64",
                "value": "5"
            }
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    }}

invalid_addresses_change_edit_template = {
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-and eg',
    'serverHardwareTypeUri': 'SHT:BL465c Gen8 1',
    'enclosureGroupUri': "EG:mixed-eg2",
    'serialNumberType': 'Virtual',
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'name': 'change-sht-and eg',
    'description': 'change-sht-and eg',
    'affinity': 'Bay',
    'connections': [],
    "boot": {
        "manageBoot": True,
        "order": [
            "Floppy",
            "PXE",
            "USB",
            "HardDisk",
            "CD"
        ]
    },

    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "64",
                "value": "5"
            }
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    }}

negative_unauth_edit_template = [
    {'keyword': 'Edit Server Profile Template',
     'argument': auth_test_edit_eg_templates.copy(),
     'taskState': 'Error',
     'timeout': '120',
     'errorMessage': 'AUTHORIZATION'}]

negative_tests_eg_sht_addresses = [

    {'keyword': 'Edit Server Profile Template',
     'argument': invalid_eg_edit_template.copy(),
     'taskState': 'Error',
     'timeout': '120',
     'errorMessage': 'INVALID_ENCLOSURE_GROUP'},

    {'keyword': 'Edit Server Profile Template',
     'argument': invalid_sht_edit_template.copy(),
     'taskState': 'Error',
     'timeout': '120',
     'errorMessage': 'UNKNOWN_SERVER_TYPE'},
    {'keyword': 'Edit Server Profile Template',
     'argument': invalid_addresses_change_edit_template.copy(),
     'taskState': 'Error',
     'timeout': '120',
     'errorMessage': 'FINAL_ATTRIBUTE_CHANGED'}

]

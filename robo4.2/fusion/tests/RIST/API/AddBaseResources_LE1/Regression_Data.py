# Credentials
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}
cliq_credentials = {
    'mgmt_ip': '16.71.149.173',
    'username': 'admin',
    'password': 'admin'}

# Resource types for X-API-Version=800
APPLIANCE_NETWORK_CONFIGURATION_TYPE = 'ApplianceNetworkConfigurationV2'
TIME_AND_LOCALE_TYPE = 'TimeAndLocale'
USER_AND_PERMISSION_TYPE = 'UserAndPermissions'
ETHERNET_NETWORK_TYPE = 'ethernet-networkV4'
FCOE_NETWORK_TYPE = 'fcoe-networkV4'
FC_NETWORK_TYPE = 'fc-networkV4'
NETWORK_SET_TYPE = 'network-setV4'
LOGICAL_INTERCONNECT_GROUP_TYPE = 'logical-interconnect-groupV6'
SAS_LOGICAL_INTERCONNECT_GROUP_TYPE = 'sas-logical-interconnect-group'
ENCLOSURE_GROUP_TYPE = 'EnclosureGroupV7'
INTERCONNECT_TYPE = 'InterconnectV4'
ENCLOSURE_TYPE = 'EnclosureV7'
STORAGE_SYSTEM_TYPE = 'StorageSystemV4'
SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV6'
SERVER_PROFILE_TYPE = 'ServerProfileV10'
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'

# LIG, SASLIG, AND LE
LIG_NAME = 'LIG1'
SASLIG_NAME = 'SASLIG1'
EG_NAME = 'EG1'
LE_NAME = 'LE1'

# Enclosures
ENC1 = 'CN754406XL'
ENC2 = 'CN754404R6'
ENC3 = 'CN754406WB'

# Potash interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC2ICBAY6 = '%s, interconnect 6' % ENC2

# Natasha SAS interconnects
ENC1SASICBAY1 = '%s, interconnect 1' % ENC1
ENC1SASICBAY4 = '%s, interconnect 4' % ENC1

# Drive Enclosures (Bigbird)
ENC1DEBAY1 = '%s, bay 1' % ENC1

# Server Hardware
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC3SHBAY1 = '%s, bay 1' % ENC3

# StRM
# StoreServ
STORESERV1_NAME = 'wpst3par-7200-7-srv'
STORESERV1_HOSTNAME = 'wpst3par-7200-7-srv.vse.rdlabs.hpecorp.net'
STORESERV1_POOL1 = 'FVT_Tbird_reg1_r1'
STORESERV1_POOL2 = 'FVT_Tbird_reg1_r5'
STORESERV1_POOL3 = 'FVT_Tbird_reg1_r6'
# StoreVirtual
STOREVIRTUAL_SLPT_STATIC_NAME = 'VSA_Cluster_173-2'
STOREVIRTUAL_SLPT_STATIC_HOSTNAME = '16.71.149.173'
STOREVIRTUAL_SLPT_STATIC_VIP = '192.168.21.71'
STOREVIRTUAL_SLPT_STATIC_POOL = 'VSA_Cluster_173-2'
STOREVIRTUAL_SLPT_DHCP_NAME = 'VSA_Cluster_116'
STOREVIRTUAL_SLPT_DHCP_HOSTNAME = '16.71.148.116'
STOREVIRTUAL_SLPT_DHCP_VIP = '192.168.21.59'
STOREVIRTUAL_SLPT_DHCP_POOL = 'VSA_Cluster_116'
STOREVIRTUAL_MLPT_NAME = 'VSA84_Storage_Pool'
STOREVIRTUAL_MLPT_HOSTNAME = '16.71.151.84'
STOREVIRTUAL_MLPT_VIP = '16.71.151.84'
STOREVIRTUAL_MLPT_POOL = 'VSA84_Storage_Pool'

appliance = {
    "type": APPLIANCE_NETWORK_CONFIGURATION_TYPE,
    "applianceNetworks": [
        {"activeNode": 1, "unconfigure": False, "app1Ipv4Addr": "16.114.210.227", "app1Ipv6Addr": "",
         "app2Ipv4Addr": "16.114.210.228", "app2Ipv6Addr": "",
         "virtIpv4Addr": "16.114.209.223", "virtIpv6Addr": None, "app1Ipv4Alias": None, "app1Ipv6Alias": None,
         "app2Ipv4Alias": None, "app2Ipv6Alias": None, "hostname": "wpst-tbird-15-oneview.vse.rdlabs.hpecorp.net",
         "confOneNode": True, "interfaceName": "", "macAddress": None,
         "ipv4Type": "STATIC", "ipv6Type": "UNCONFIGURE", "overrideIpv4DhcpDnsServers": False,
         "ipv4Subnet": "255.255.240.0", "ipv4Gateway": "16.114.208.1", "ipv6Subnet": None, "ipv6Gateway": None,
         "domainName": "vse.rdlabs.hpecorp.net", "searchDomains": [],
         "ipv4NameServers": ["16.125.25.81", "16.125.25.82"],
         "ipv6NameServers": ["16.125.25.81", "16.125.25.82"], "bondedTo": None, "aliasDisabled": True,
         "configureRabbitMqSslListener": False, "configurePostgresSslListener": False, "webServerCertificate": None,
         "webServerCertificateChain": None, "webServerCertificateKey": None}
    ],
    "serverCertificate": {
        "rabbitMQCertificate": None, "rabbitMQRootCACertificate": None,
        "rabbitMQCertificateKey": None, "postgresCertificate": None,
        "postgresRootCACertificate": None, "postgresCertificateKey": None}
}

Time_and_Locale = {'type': TIME_AND_LOCALE_TYPE,
                   'locale': 'en_US.UTF-8',
                   'timezone': 'UTC',
                   'ntpServers': [
                       '16.110.135.123'
                   ]
                   }

timeandlocale = {'type': TIME_AND_LOCALE_TYPE, 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'],
                 'locale': 'en_US.UTF-8'}

users = [
    {'userName': 'Serveradmin', 'password': 'wpsthpvse1', 'fullName': 'Serveradmin', 'roles': ['Server administrator'],
     'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': USER_AND_PERMISSION_TYPE},
    {'userName': 'Networkadmin', 'password': 'wpsthpvse1', 'fullName': 'Networkadmin',
     'roles': ['Network administrator'],
     'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': USER_AND_PERMISSION_TYPE},
    {'userName': 'Backupadmin', 'password': 'wpsthpvse1', 'fullName': 'Backupadmin', 'roles': ['Backup administrator'],
     'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': USER_AND_PERMISSION_TYPE},
    {'userName': 'Noprivledge', 'password': 'wpsthpvse1', 'fullName': 'Noprivledge', 'roles': ['Read only'],
     'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': USER_AND_PERMISSION_TYPE}
]

licenses = [
    {
        'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    },
    {
        'key': 'YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    },
]

# Reserved location of SPP bundles for FVT Regression testing
spp_path = r'Z:\firmware\SPP\FVT-Regression'

enclosures = [
    {"type": ENCLOSURE_TYPE, "name": ENC1, },
    {"type": ENCLOSURE_TYPE, "name": ENC2, },
    {"type": ENCLOSURE_TYPE, "name": ENC3, },
]

sasics = [
    {"name": ENC1SASICBAY1, },
    {"name": ENC1SASICBAY4, }
]

sasics_bay1 = [
    {"name": ENC1SASICBAY1}
]

sasics_bay4 = [
    {"name": ENC1SASICBAY4}
]

ics = [
    {"name": ENC1ICBAY3},
    {"name": ENC2ICBAY6}
]

interconnects_linked_ports_expected = [
    {
        "name": ENC1 + ", interconnect 3",
        "linked_ports": ['d3', 'd5', 'd6', 'd7', 'd8', 'd13', 'd17', 'd19', 'd20', 'd25', 'd29', 'Q1:1', 'Q2:1', 'Q3:1', 'Q4:1', 'Q7', 'Q8', 'l1', 'l2', 'l3', 'l4']

    },
    {
        "name": ENC1 + ", interconnect 6",
        "linked_ports": ['d3', 'd5', 'd6', 'd7', 'd8', 'l1', 'l2']
    },
    {
        "name": ENC2 + ", interconnect 3",
        "linked_ports": ['d1', 'd5', 'd7', 'd8', 'l1', 'l2']
    },
    {
        "name": ENC2 + ", interconnect 6",
        "linked_ports": ['d1', 'd5', 'd7', 'd8', 'd15', 'd17', 'd18', 'd19', 'd20', 'd25', 'd29', 'Q1:1', 'Q2:1', 'Q3:1', 'Q4:1', 'Q7', 'Q8', 'l1', 'l2', 'l3', 'l4']
    },
    {
        "name": ENC3 + ", interconnect 3",
        "linked_ports": ['d1', 'd5', 'l1', 'l2']
    },
    {
        "name": ENC3 + ", interconnect 6",
        "linked_ports": ['d1', 'd5', 'l1', 'l2']
    },
]

ethernet_networks = [
    {'name': 'network-tunnel',
     'type': ETHERNET_NETWORK_TYPE,
     'vlanId': 0,
     'subnetUri': None,
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

fc_networks = [
    {'name': 'FA1',
     'type': FC_NETWORK_TYPE,
     'fabricType': 'FabricAttach',
     'linkStabilityTime': 30,
     'autoLoginRedistribution': True,
     'managedSanUri': 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55'},
    {'name': 'FA2',
     'type': FC_NETWORK_TYPE,
     'fabricType': 'FabricAttach',
     'linkStabilityTime': 30,
     'autoLoginRedistribution': True,
     'managedSanUri': 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID101-10:00:00:27:f8:fe:0c:56'},
]

fcoe_networks = [
    {'name': 'FCoE_350', 'type': FCOE_NETWORK_TYPE, 'vlanId': 350, 'managedSanUri': 'FCSan:VSAN350'},
    {'name': 'FCoE_450', 'type': FCOE_NETWORK_TYPE, 'vlanId': 450, 'managedSanUri': 'FCSan:VSAN450'}
]

san_managers = [
    {"connectionInfo": [
        {'name': 'Type',
         'value': 'Brocade Network Advisor'},
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
        {"name": "UseSsl",
            "displayName": "UseSsl",
            "required": True,
            "value": True,
            "valueFormat": "None",
            "valueType": "Boolean"},
    ], },
    {"connectionInfo": [
        {'name': 'Type', 'value': 'HPE'},
        {"name": "Host", "value": "16.125.25.45"},
        {"name": "SnmpPort", "value": 161},
        {"name": "SnmpUserName", "value": "UNoAuthNoPriv"},
        {"name": "SnmpAuthLevel", "value": "NOAUTHNOPRIV"},
        {"name": "SnmpAuthProtocol", "value": ""},
        {"name": "SnmpAuthString", "value": ""},
        {"name": "SnmpPrivProtocol", "value": ""},
        {"name": "SnmpPrivString", "value": ""}
    ], },
]

network_sets = [{'name': 'NS1',
                 'type': NETWORK_SET_TYPE,
                 'networkUris': ['net100'],
                 'nativeNetworkUri': 'net100'},
                ]

icmap = [
    {'bay': 3,
     'enclosure': 1,
     'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
     'enclosureIndex': 1},
    {'bay': 6,
     'enclosure': 2,
     'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
     'enclosureIndex': 2},
    {'bay': 6,
     'enclosure': 1,
     'type': 'Synergy 20Gb Interconnect Link Module',
     'enclosureIndex': 1},
    {'bay': 3,
     'enclosure': 2,
     'type': 'Synergy 20Gb Interconnect Link Module',
     'enclosureIndex': 2},
    {'bay': 3,
     'enclosure': 3,
     'type': 'Synergy 20Gb Interconnect Link Module',
     'enclosureIndex': 3},
    {'bay': 6,
     'enclosure': 3,
     'type': 'Synergy 20Gb Interconnect Link Module',
     'enclosureIndex': 3},
]

uplink_sets = {'us_untagged': {'name': 'us-untagged',
                               'ethernetNetworkType': 'Untagged',
                               'networkType': 'Ethernet',
                               'networkUris': ['network-untagged'],
                               'nativeNetworkUri': None,
                               'mode': 'Auto',
                               'lacpTimer': 'Long',
                               'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'},
                                                          {'enclosure': '2',
                                                           'bay': '6',
                                                           'port': 'Q1.1',
                                                           'speed': 'Auto'},
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
                                                        {'enclosure': '2',
                                                         'bay': '6',
                                                         'port': 'Q2.1',
                                                         'speed': 'Auto'},
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
                                                        {'enclosure': '2',
                                                         'bay': '6',
                                                         'port': 'Q3.1',
                                                         'speed': 'Auto'},
                                                        ]
                             },
               'FA-path1': {'name': 'FA-path1',
                            'ethernetNetworkType': None,
                            'networkType': 'FibreChannel',
                            'networkUris': ['FA1'],
                            'primaryPort': None,
                            'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q4:1', 'speed': 'Auto'}
                                                       ]
                            },
               'FA-path2': {'name': 'FA-path2',
                            'ethernetNetworkType': None,
                            'networkType': 'FibreChannel',
                            'networkUris': ['FA2'],
                            'primaryPort': None,
                            'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q4:1', 'speed': 'Auto'}
                                                       ]
                            },
               }

ligs = [{'name': LIG_NAME,
         'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap,
         'enclosureIndexes': [1, 2, 3],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'fcoeSettings': {'fcoeMode': 'FcfNpv'},
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'uplinkSets': [
             uplink_sets['us_untagged'].copy(),
             uplink_sets['us_tagged'].copy(),
             uplink_sets['us_tunnel'].copy(),
             uplink_sets['FA-path1'].copy(),
             uplink_sets['FA-path2'].copy(),
         ],
         }
        ]

sasligs = [{'name': SASLIG_NAME,  # Single SAS switch
            "type": SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
            "enclosureType": "SY12000",
            "enclosureIndexes": [1],
            "interconnectBaySet": "1",
            'interconnectMapTemplate': [
                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'Synergy 12Gb SAS Connection Module'}]}
           ]

edit_sasligs = [{"name": SASLIG_NAME,  # Dual SAS switch
                 "type": SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
                 "enclosureType": "SY12000",
                 "enclosureIndexes": [1],
                 "interconnectBaySet": "1",
                 'interconnectMapTemplate': [
                     {'enclosure': 1,
                      'enclosureIndex': 1,
                      'bay': 1,
                      'type': 'Synergy 12Gb SAS Connection Module'},
                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'Synergy 12Gb SAS Connection Module'}]}
                ]

egs = [{'name': EG_NAME,
        'enclosureCount': 3,
        'configurationScript': None,
        'interconnectBayMappings':
        [
            {"interconnectBay": 3,
             "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
            {"interconnectBay": 6,
             "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
        ],
        'ipAddressingMode': "External",
        'ipRangeUris': [],
        'powerMode': "RedundantPowerFeed"
        }
       ]

edit_egs = [{'name': EG_NAME,
             'type': ENCLOSURE_GROUP_TYPE,
             'enclosureCount': 3,
             'enclosureTypeUri': '/rest/enclosure-types/SY12000',
             'stackingMode': 'Enclosure',
             'interconnectBayMappingCount': 3,
             'configurationScript': None,
             'interconnectBayMappings':
             [{"enclosureIndex": 1, "interconnectBay": 1, "logicalInterconnectGroupUri": "SASLIG:" + SASLIG_NAME},
              {"enclosureIndex": 2,
               "interconnectBay": 1,
               "logicalInterconnectGroupUri": "SASLIG:" + SASLIG_NAME},
              {"interconnectBay": 3,
               "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
              {"interconnectBay": 6,
               "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
              ],
             'ipAddressingMode': "External",
             'ipRangeUris': [],
             'powerMode': "RedundantPowerFeed"
             }
            ]

les = [{'name': LE_NAME,
        'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
        'enclosureGroupUri': "EG:" + EG_NAME,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False}
       ]

storage_systems = [
    {'type': STORAGE_SYSTEM_TYPE,
     'name': STORESERV1_NAME,
     'family': 'StoreServ',
     "hostname": STORESERV1_HOSTNAME,
     'credentials': {'username': 'fusionadm', 'password': 'hpvse1'},
     "deviceSpecificAttributes":
         {
             "discoveredDomains": [
                 "NO DOMAIN",
             ],
             "managedDomain": "Tbird_Regression_Domain",
     },
     },
    {'type': STORAGE_SYSTEM_TYPE,
     'name': STOREVIRTUAL_SLPT_STATIC_NAME,
     "family": "StoreVirtual",
     "hostname": STOREVIRTUAL_SLPT_STATIC_HOSTNAME,
     "credentials": {"username": "admin", "password": 'admin'},
     "ports": [
         {
             "name": STOREVIRTUAL_SLPT_STATIC_VIP,
             "expectedNetworkUri": "ETH:network-untagged",
             "expectedNetworkName": "network-untagged",
             "mode": "Managed",
         },
     ],
     },
    {'type': STORAGE_SYSTEM_TYPE,
     'name': STOREVIRTUAL_SLPT_DHCP_NAME,
     "family": "StoreVirtual",
     "hostname": STOREVIRTUAL_SLPT_DHCP_HOSTNAME,
     "credentials": {"username": "admin", "password": 'admin'},
     "ports": [
         {
             "name": STOREVIRTUAL_SLPT_DHCP_VIP,
             "expectedNetworkUri": "ETH:network-untagged",
             "expectedNetworkName": "network-untagged",
             "mode": "Managed",
         },
     ],
     },
    {'type': STORAGE_SYSTEM_TYPE,
     'name': STOREVIRTUAL_MLPT_NAME,
     "family": "StoreVirtual",
     "hostname": STOREVIRTUAL_MLPT_HOSTNAME,
     "credentials": {"username": "admin", "password": 'admin'},
     "ports": [
         {
             "name": STOREVIRTUAL_MLPT_VIP,
             "expectedNetworkUri": "ETH:network-tunnel",
             "expectedNetworkName": "network-tunnel",
             "mode": "Managed",
         },
     ],
     },
]

storage_pools = [
    {"storageSystemUri": STORESERV1_NAME,
     "name": STORESERV1_POOL1,
     "isManaged": True,
     },
    {"storageSystemUri": STORESERV1_NAME,
     "name": STORESERV1_POOL2,
     "isManaged": True,
     },
    {"storageSystemUri": STORESERV1_NAME,
     "name": STORESERV1_POOL3,
     "isManaged": True,
     },
]

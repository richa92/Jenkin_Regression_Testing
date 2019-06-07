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

licenses = [{'key': 'YCDC D9MA H9PQ KHX2 V7B5 HWWB Y9JL KMPL TA2E PDRA DXAU 2CSM GHTG L762 HUK7 GB5M KJVT D5KM EFRW DS5R TXXK 6Q22 AK2P 3EW2 AJQ4 HU5V TZZH AB6X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEC 3F9V JQY5 "423542007 HPOV-NFR1 HP_OneView_16_Seat_NFR 75YYJJECU46C"_3DWNY-6B2KD-D8Z6S-6YR4B-K8GDW'},
            {'key': '9CTC B9MA H9PA GHWY V7B5 HWWB Y9JL KMPL 3ASE NGRE DXAU 2CSM GHTG L762 FN83 EARE KJVT D5KM EFRW DS5R 3XPK 4T22 AK2P 3EW2 AJA6 XUNV TZZX MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEC 3F9V JQY5 "423542185 HPOV-NFR1 HP_OneView_16_Seat_NFR JJT5JJEC9DC5"_3JNBT-28349-3DJ6L-TBRPP-PDLNR'},
            {'key': '9B3C A99A H9P9 GHUZ U7B5 HWW5 Y9JL KMPL 5AWA 8CBE DXAU 2CSM GHTG L762 7NGZ GDV4 KJVT D5KM EFRW DS5R 5XP8 4XK2 GNSL 9F82 7JKT QVXB XZKH ABB4 NV2C LHXU KN7U 5NA6 BKRK 35QB D8UW R42A X3BN LQ6M 5V9A PM6Q 4MN9 9GGS EZU7 GEMX VUJW CDB5 JVRX 8HEN 2J98 ACPB "TKOPREN HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR ATJUJJEDAT2Y"'},
            {'key': 'QCTG B9MA H9P9 8HW3 V7B5 HWWB Y9JL KMPL 5AKE 8DBA DXAU 2CSM GHTG L762 VYW6 GCN9 KJVT D5KM EFVW DT5J 5XHK 5QK2 AK2P 3EW2 QJQ4 HU5V TZZ7 9B5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEC 3F9V JQY5 "423542022 HPOV-NFR1 HP_OneView_16_Seat_NFR AACUJJECUT2J"_3DWNY-DZZW8-24Y5Y-NZB2K-YH5R2'},
            {'key': '9CTC C9MA H9PY CHUY V7B5 HWWB Y9JL KMPL VACE 8GRE DXAU 2CSM GHTG L762 7RGY XHBE KJVT D5KM EFVW DT5J VX79 5T22 AK2P 3EW2 9JA6 XUNV TZZH MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEC 3F9V JQY5 "423542193 HPOV-NFR1 HP_OneView_16_Seat_NFR 9UH2JJECJ4AA"_3JNDQ-Z35J3-D6T6M-5XKZL-WC2W2'},
            {'key': 'YBLG B99A H9PQ 8HVZ U7B5 HWW5 Y9JL KMPL VAWA 8CBE DXAU 2CSM GHTG L762 5NW5 HDV4 KJVT D5KM EFVW DT5J VXP8 4XK2 GNSL 9F82 7JKT QVXB XZKH ABB4 NV2C LHXU KN7U 5NA6 BKRK 35QB D8UW R42A X3BN LQ6M 5V9A PM6Q 4MN9 9GGS EZU7 GEMX VUJW CDB5 JVRX 8HEN 2J98 ACPB "TKOPREN HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR JJADJJEDATCA"'},
            ]

EG_NAME = 'EG1'

# Enclosures
ENC1 = 'wpst11'
ENC2 = ''
ENC3 = ''
# Interconnects
ENC1ICBAY3 = '%s, interconnect 1' % ENC1
ENC1ICBAY6 = '%s, interconnect 2' % ENC1
ENC2ICBAY3 = '%s, interconnect 3' % ENC2
ENC2ICBAY6 = '%s, interconnect 4' % ENC2
ENC3ICBAY3 = '%s, interconnect 5' % ENC3
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

STORAGE_POOL = 'Cluster-1'
VOLUME_TEMPLATE = 'volume-template'

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

vol_sp = [{
    "properties": {
        "storagePool": STORAGE_POOL,
        "size": 6000000,
        "dataProtectionLevel": "NetworkRaid5SingleParity",
        "name": "vol_sp_1"
    },
    "templateUri": VOLUME_TEMPLATE,
    "isPermanent": True,
},
    {
    "properties": {
        "storagePool": STORAGE_POOL,
        "size": 6000000,
        "dataProtectionLevel": "NetworkRaid5SingleParity",
        "name": "vol_sp_2"
    },
    "templateUri": VOLUME_TEMPLATE,
    "isPermanent": True,
},
    {
    "properties": {
        "storagePool": STORAGE_POOL,
        "size": 6000000,
        "dataProtectionLevel": "NetworkRaid5SingleParity",
        "name": "vol_sp_3"
    },
    "templateUri": VOLUME_TEMPLATE,
    "isPermanent": True,
},
    {
    "properties": {
        "storagePool": STORAGE_POOL,
        "size": 6000000,
        "dataProtectionLevel": "NetworkRaid5SingleParity",
        "name": "vol_sp_4"
    },
    "templateUri": VOLUME_TEMPLATE,
    "isPermanent": True,
},
    {
    "properties": {
        "storagePool": STORAGE_POOL,
        "size": 6000000,
        "dataProtectionLevel": "NetworkRaid5SingleParity",
        "name": "vol_sp_5"
    },
    "templateUri": VOLUME_TEMPLATE,
    "isPermanent": True,
},
]

# volume_template = {
#           "name":"storeserv1-pool1-private-thin",
#            "rootTemplateUri":"QUERY"
#            "description":"Private thin volume template for storeserv1 pool1",
#            "properties":{
#                  "name":{"title":"Volume name","description":"A volume name between 1 and 100 characters",
#                          "type":"string","minLength":1,"maxLength":100,"required":True,
#                           "meta":{"locked":False}},
#                   "description":{"title":"Description","description":"A description for the volume",
#                                  "type":"string","minLength":0,"maxLength":2000,"default":"",
#                                 "meta":{"locked":False}},
#                   "storagePool":{"title":"Storage Pool","description":"A common provisioning group URI reference",
#                                  "type":"string","required":True,"format":"x-uri-reference",
#                                  "meta":{"locked":False,"createOnly":True,"semanticType":"device-storage-pool"},
#                                  "default":STORESERV1_POOL1
#                   },
#                   "size":{"title":"Capacity","description":"The capacity of the volume in bytes",
#                           "type":"integer","required":True,"minimum":1073741824,"maximum":17592186044416,
#                           "meta":{"locked":False,"semanticType":"capacity"},
#                           "default":1073741824,},
#                   "isShareable":{"title":"Is Shareable","description":"The shareability of the volume",
#                                  "type":"boolean","meta":{"locked":False},
#                                  "default":False,},
#                   "provisioningType":{"title":"Provisioning Type","description":"The provisioning type for the volume",
#                                       "type":"string","enum":["Thin","Full"],"meta":{"locked":True,"createOnly":True},
#                                       "default":"Thin"},
#                   "snapshotPool":{"title":"FC_wpst16_r1","description":"A URI referenceto the common provisioning group used to create snapshots",
#                                   "type":"string","format":"x-uri-reference","meta":{"locked":True,"semanticType":"device-snapshot-storage-pool"},
#                                   "default":STORESERV1_POOL1,}
#                   },
#          { "name":"vsa1-raid5-private",
#            "rootTemplateUri":"Volume root template for StoreVirtual 1.2",
#            "description":"",
#            "properties":
#                 {"name":{"title":"Volume name","description":"A volume name between 1 and 100 characters",
#                          "type":"string","minLength":1,"maxLength":100,"required":True,"meta":{"locked":False}},
#                  "description":{"title":"Description","description":"A description for the volume",
#                                 "type":"string","minLength":0,"maxLength":2000,
#                                 "default":"",
#                                 "meta":{"locked":False}},
#                  "storagePool":{"title":"Storage Pool","description":"StoragePoolURI the volume should be added to",
#                                 "type":"string","format":"x-uri-reference","required":True,
#                                 "meta":{"locked":False,"createOnly":True,"semanticType":"device-storage-pool"},
#                                 "default":STOREVIRTUAL1_POOL},
#                  "size":{"title":"Capacity","description":"Capacity of the volume in bytes",
#                          "type":"integer","minimum":4194304,"required":True,
#                          "default":1073741824,
#                          "meta":{"locked":False,"semanticType":"capacity"}},
#                  "dataProtectionLevel":{"title":"Data Protection Level","description":"Indicates the number and configuration of data copies in the Storage Pool",
#                                         "type":"string","enum":["NetworkRaid0None","NetworkRaid5SingleParity","NetworkRaid10Mirror2Way","NetworkRaid10Mirror3Way","NetworkRaid10Mirror4Way","NetworkRaid6DualParity"],
#                                         "default":"NetworkRaid5SingleParity",
#                                         "required":True,"meta":{"locked":True,"semanticType":"device-dataProtectionLevel"}},
#                  "provisioningType":{"title":"Provisioning Type","description":"The provisioning type for the volume",
#                                      "type":"string","enum":["Thin","Full"],
#                                      "default":"Thin",
#                                      "meta":{"locked":True,"createOnly":"True","semanticType":"device-provisioningType"}},
#                  "isAdaptiveOptimizationEnabled":{"title":"Adaptive Optimization","description":"",
#                                       "type":"boolean","default":True,"meta":{"locked":True}},
#                 "isShareable":{"title":"Is Shareable","description":"The shareability of the volume",
#                                 "type":"boolean","default":False,"meta":{"locked":False}}
#                  },
#             },

sp_sw_edit_add_secondary_volume = {
    "type": "ServerProfileV400",
    'serverHardwareUri': 'SH:' + ENC1SHBAY10,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "sp-ethernet-bay10",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "HardDisk"
        ],
        "manageBoot": True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
                "iscsi": {
                    "initiatorNameSource": "ProfileInitiatorName",
                },
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.2",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": "ETH:net100",
        },
        {
            "boot": {
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
                "iscsi": {
                    "initiatorNameSource": "ProfileInitiatorName",
                },
                "priority": "Secondary"
            },
            "functionType": "Ethernet",
            "id": 2,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.2",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 2",
            "networkUri": "ETH:net100",
        }
    ],
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 2,
                "lunType": "Auto",
                "isBootVolume": False,
                "volumeUri": "SVOL:vol_sp_3",
                "storagePaths": [{
                      "connectionId": 1,
                      "isEnabled": True
                },
                ]
            },
            {
                "id": 1,
                "lunType": "Auto",
                "isBootVolume": True,
                "volumeUri": "SVOL:vol_sp_4",
                "storagePaths": [{
                    "connectionId": 2,
                    "isEnabled": True
                },
                ]
            },
        ]
    }
}

sp_hw_edit_add_secondary_volume = {
    "type": "ServerProfileV400",
    'serverHardwareUri': 'SH:' + ENC1SHBAY11,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "sp-iscsi-bay11",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "HardDisk"
        ],
        "manageBoot": True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "bootVolumeSource": "ManagedVolume",
                "iscsi": {
                    "initiatorNameSource": "ProfileInitiatorName",
                },
                "priority": "Primary"
            },
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.2",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": "ETH:net100",
        }
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": "SVOL:vol_sp_2",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            }]
        }]
    }
},

sp_edit_boot_volume = {
    "type": "ServerProfileV400",
    'serverHardwareUri': 'SH:' + ENC1SHBAY10,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "sp-ethernet-bay10",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "HardDisk"
        ],
        "manageBoot": True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
                "iscsi": {
                    "initiatorNameSource": "ProfileInitiatorName",
                },
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.2",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": "ETH:net100",
        }
    ],
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 4,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": "SVOL:vol_sp_3",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            },
            ]
        }]
    }
}

sp_edit_boot_volume_verify = {
    "type": "ServerProfileV400",
    'serverHardwareUri': 'SH:' + ENC1SHBAY10,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "sp-ethernet-bay10",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "HardDisk"
        ],
        "manageBoot": True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
                "iscsi": {
                    "initiatorNameSource": "ProfileInitiatorName",
                },
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.2",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": "ETH:net100",
        }
    ],
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 4,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": "SVOL:vol_sp_3",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            },
            ]
        }]
    }
}


sp_1 = [
    {
        "type": "ServerProfileV400",
        'serverHardwareUri': 'SH:' + ENC1SHBAY10,
        "enclosureGroupUri": "EG:" + EG_NAME,
        "name": "sp-ethernet-bay10",
        "affinity": "Bay",
        "bios": {
            "manageBios": False
        },
        "boot": {
            "order": [
                "HardDisk"
            ],
            "manageBoot": True
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
            'pxeBootPolicy': 'Auto'
        },
        "category": "server-profiles",
        "connections": [
            {
                "boot": {
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                    },
                    "priority": "Primary"
                },
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "gateway": "16.125.64.1",
                    "ipAddress": "16.125.64.2",
                    "subnetMask": "255.255.255.0"
                },
                "name": "Connection 1",
                "networkUri": "ETH:net100",
            }
        ],
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [{
                "id": 1,
                "lunType": "Auto",
                "isBootVolume": True,
                "volumeUri": "SVOL:vol_sp_1",
                "storagePaths": [{
                    "connectionId": 1,
                    "isEnabled": True
                }]
            }]
        }
    },
    {
        "type": "ServerProfileV400",
        'serverHardwareUri': 'SH:' + ENC1SHBAY11,
        "enclosureGroupUri": "EG:" + EG_NAME,
        "name": "sp-iscsi-bay11",
        "affinity": "Bay",
        "bios": {
            "manageBios": False
        },
        "boot": {
            "order": [
                "HardDisk"
            ],
            "manageBoot": True
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
            'pxeBootPolicy': 'Auto'
        },
        "category": "server-profiles",
        "connections": [
            {
                "boot": {
                    "bootVolumeSource": "ManagedVolume",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                    },
                    "priority": "Primary"
                },
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "gateway": "16.125.64.1",
                    "ipAddress": "16.125.64.2",
                    "subnetMask": "255.255.255.0"
                },
                "name": "Connection 1",
                "networkUri": "ETH:net100",
            }
        ],
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [{
                "id": 1,
                "lunType": "Auto",
                "isBootVolume": True,
                "volumeUri": "SVOL:vol_sp_2",
                "storagePaths": [{
                    "connectionId": 1,
                    "isEnabled": True
                }]
            }]
        }
    },
    {
        "type": "ServerProfileV400",
        'serverHardwareUri': 'SH:' + ENC1SHBAY11,
        "enclosureGroupUri": "EG:" + EG_NAME,
        "name": "sp-ethernet-11",
        "affinity": "Bay",
        "bios": {
            "manageBios": False
        },
        "boot": {
            "order": [
                "HardDisk"
            ],
            "manageBoot": True
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
            'pxeBootPolicy': 'Auto'
        },
        "category": "server-profiles",
        "connections": [
            {
                "boot": {
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                    },
                    "priority": "Primary"
                },
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "gateway": "16.125.64.1",
                    "ipAddress": "16.125.64.2",
                    "subnetMask": "255.255.255.0"
                },
                "name": "Connection 1",
                "networkUri": "ETH:net100",
            }
        ],
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [{
                "id": 1,
                "lunType": "Auto",
                "isBootVolume": True,
                "volumeUri": "SVOL:vol_sp_1",
                "storagePaths": [{
                    "connectionId": 1,
                    "isEnabled": True
                }]
            }]
        }
    },
]

sp_sw_1_verify = {
    "type": "ServerProfileV400",
    'serverHardwareUri': 'SH:' + ENC1SHBAY10,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "sp-ethernet-bay10",

    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "HardDisk"
        ],
        "manageBoot": True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
                "iscsi": {
                    "initiatorNameSource": "ProfileInitiatorName",
                },
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.2",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": "ETH:net100",
        }
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": "SVOL:vol_sp_1",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            }]
        }]
    }
}

sp_hw_1_verify = {
    "type": "ServerProfileV400",
    'serverHardwareUri': 'SH:' + ENC1SHBAY11,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "sp-iscsi-bay11",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "HardDisk"
        ],
        "manageBoot": True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "bootVolumeSource": "ManagedVolume",
                "iscsi": {
                    "initiatorNameSource": "ProfileInitiatorName",
                },
                "priority": "Primary"
            },
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.2",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": "ETH:net100",
        }
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": "SVOL:vol_sp_2",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            }]
        }]
    }
}

negative_sp_1 = {
    "type": "ServerProfileV400",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "negative_profile_1",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "HardDisk"
        ],
        "manageBoot": True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
                "iscsi": {
                    "chapLevel": "None",
                    "initiatorNameSource": "ProfileInitiatorName",
                },
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.2",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": "ETH:net100",
        },
        {
            "boot": {
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
                "iscsi": {
                    "chapLevel": "None",
                    "initiatorNameSource": "ProfileInitiatorName",
                },
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 2,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.2",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 2",
            "networkUri": "ETH:net100",
        }
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": None,
            "volumeName": "vol-sp-1",
            "volumeProvisionType": "Thin",
            "dataProtectionLevel": "NetworkRaid0None",
            "volumeProvisionedCapacityBytes": "2684354560",
            "permanent": False,
            "volumeShareable": False,
            "volumeStoragePoolUri": "SPOOL:Cluster-1",
            "volumeStorageSystemUri": "SSYS:Cluster-1",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            }]
        }]
    }
}

negative_sp_2 = {
    "type": "ServerProfileV400",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "negative_profile_2",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "HardDisk"
        ],
        "manageBoot": True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
                "iscsi": {
                    "chapLevel": "None",
                    "initiatorNameSource": "ProfileInitiatorName",
                },
                "priority": "Secondary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.2",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": "ETH:net100",
        },
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": None,
            "volumeName": "vol-sp-1",
            "volumeProvisionType": "Thin",
            "dataProtectionLevel": "NetworkRaid0None",
            "volumeProvisionedCapacityBytes": "2684354560",
            "permanent": False,
            "volumeShareable": False,
            "volumeStoragePoolUri": "SPOOL:Cluster-1",
            "volumeStorageSystemUri": "SSYS:Cluster-1",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            }]
        }]
    }
}

negative_sp_3 = {
    "type": "ServerProfileV400",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "negative_profile_3",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "HardDisk"
        ],
        "manageBoot": True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
                "iscsi": {
                    "chapLevel": "None",
                    "initiatorNameSource": "ProfileInitiatorName",
                },
                "priority": "Secondary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.2",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": "ETH:net100",
        },
        {
            "boot": {
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
                "iscsi": {
                    "chapLevel": "None",
                    "initiatorNameSource": "ProfileInitiatorName",
                },
                "priority": "Secondary"
            },
            "functionType": "Ethernet",
            "id": 2,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.2",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 2",
            "networkUri": "ETH:net100",
        },
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": None,
            "volumeName": "vol-sp-1",
            "volumeProvisionType": "Thin",
            "dataProtectionLevel": "NetworkRaid0None",
            "volumeProvisionedCapacityBytes": "2684354560",
            "permanent": False,
            "volumeShareable": False,
            "volumeStoragePoolUri": "SPOOL:Cluster-1",
            "volumeStorageSystemUri": "SSYS:Cluster-1",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            }]
        }]
    }
}

negative_sp_4 = {
    "type": "ServerProfileV400",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "negative_profile_4",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "HardDisk"
        ],
        "manageBoot": True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'BIOS',
    },
    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
                "iscsi": {
                    "chapLevel": "None",
                    "initiatorNameSource": "ProfileInitiatorName",
                },
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.2",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": "ETH:net100",
        },
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": None,
            "volumeName": "vol-sp-1",
            "volumeProvisionType": "Thin",
            "dataProtectionLevel": "NetworkRaid0None",
            "volumeProvisionedCapacityBytes": "2684354560",
            "permanent": False,
            "volumeShareable": False,
            "volumeStoragePoolUri": "SPOOL:Cluster-1",
            "volumeStorageSystemUri": "SSYS:Cluster-1",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            }]
        }]
    }
}

negative_sp_5 = {
    "type": "ServerProfileV400",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "negative_profile_5",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "HardDisk"
        ],
        "manageBoot": True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
                "iscsi": {
                    "chapLevel": "None",
                    "initiatorNameSource": "ProfileInitiatorName",
                },
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.2",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": "ETH:net100",
        }
    ],
}

negative_sp_6 = {
    "type": "ServerProfileV400",

    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "negative_profile_6",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "HardDisk"
        ],
        "manageBoot": True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
                "iscsi": {
                    "chapLevel": "None",
                    "initiatorNameSource": "ProfileInitiatorName",
                },
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.2",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": "ETH:net100",
        },
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": None,
            "volumeName": "vol-sp-1",
            "volumeProvisionType": "Thin",
            "dataProtectionLevel": "NetworkRaid0None",
            "volumeProvisionedCapacityBytes": "2684354560",
            "permanent": False,
            "volumeShareable": False,
            "volumeStoragePoolUri": "SPOOL:Cluster-1",
            "volumeStorageSystemUri": "SSYS:Cluster-1",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            }],
        },
            {
            "id": 2,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": None,
            "volumeName": "vol-sp-2",
            "volumeProvisionType": "Thin",
            "dataProtectionLevel": "NetworkRaid0None",
            "volumeProvisionedCapacityBytes": "2684354560",
            "permanent": False,
            "volumeShareable": False,
            "volumeStoragePoolUri": "SPOOL:Cluster-1",
            "volumeStorageSystemUri": "SSYS:Cluster-1",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            }],
        }]
    }
}

negative_sp_7 = {
    "type": "ServerProfileV400",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "negative_profile_7",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "HardDisk"
        ],
        "manageBoot": True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
                "iscsi": {
                    "chapLevel": "None",
                    "initiatorNameSource": "ProfileInitiatorName",
                },
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.2",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": "ETH:net100",
        }
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": None,
            "volumeName": "vol-sp-1",
            "volumeProvisionType": "Thin",
            "dataProtectionLevel": "NetworkRaid0None",
            "volumeProvisionedCapacityBytes": "2684354560",
            "permanent": False,
            "volumeShareable": True,
            "volumeStoragePoolUri": "SPOOL:Cluster-1",
            "volumeStorageSystemUri": "SSYS:Cluster-1",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            }]
        }]
    }
}

negative_sp_8 = {
    "type": "ServerProfileV400",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "ethernet_profile_1",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "HardDisk"
        ],
        "manageBoot": True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
                "iscsi": {
                    "chapLevel": "None",
                    "initiatorNameSource": "ProfileInitiatorName",
                },
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.2",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": "ETH:net100",
        }
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": None,
            "volumeName": "vol-sp-1",
            "volumeProvisionType": "Thin",
            "dataProtectionLevel": "NetworkRaid0None",
            "volumeProvisionedCapacityBytes": "2684354560",
            "permanent": False,
            "volumeShareable": False,
            "volumeStoragePoolUri": "SPOOL:Cluster-1",
            "volumeStorageSystemUri": "SSYS:Cluster-1",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": False,
            }]
        }]
    }
}

negative_sp_8 = {
    "type": "ServerProfileV400",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "ethernet_profile_1",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "HardDisk"
        ],
        "manageBoot": True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
                "iscsi": {
                    "chapLevel": "None",
                    "initiatorNameSource": "ProfileInitiatorName",
                },
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.2",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": "ETH:net100",
        }
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": None,
            "volumeName": "vol-sp-1",
            "volumeProvisionType": "Thin",
            "dataProtectionLevel": "NetworkRaid0None",
            "volumeProvisionedCapacityBytes": "2684354560",
            "permanent": False,
            "volumeShareable": False,
            "volumeStoragePoolUri": "SPOOL:Cluster-1",
            "volumeStorageSystemUri": "SSYS:Cluster-1",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": False,
            }]
        }]
    }
}


negative_sp_tasks = [
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_1.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_primary_boot'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_2.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_secondary_boot_connection'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_3.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_secondary_boot'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_4.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_iSCSI_and_BIOS_boot_mode'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_5.copy(),
        'taskState': 'Error',
        'errorMessage': 'Bootable_connection_nonbootable_volume'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_6.copy(),
        'taskState': 'Error',
        'errorMessage': 'More_than_one_boot_volume'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_7.copy(),
        'taskState': 'Error',
        'errorMessage': 'Only_private_boot_volume'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_8.copy(),
        'taskState': 'Error',
        'errorMessage': 'Storage_path_disabled_not_exist'},
]

negative_sp_tasks_8 = [
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_8.copy(),
        'taskState': 'Error',
        'errorMessage': 'error'},
]

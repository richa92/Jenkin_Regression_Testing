admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

ilo_credentials = {'username': 'Administrator',
                   'password': 'hpvse123'
                   }

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
            {'key': '9AQA BQAA H9PA GHWZ V7B5 HWWB Y9JL KMPL SR2G 7AZU DXAU 2CSM GHTG L762 69VZ USJA KJVT D5KM EFVW DT5J VFQM 85S8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3G8YL-HHGX3-6M6KH-DZ99V-BDXMM'},
            {'key': 'YAAE DQAA H9P9 GHV3 U7B5 HWW5 Y9JL KMPL CRKE 6AJU DXAU 2CSM GHTG L762 H9Z2 WUZY KJVT D5KM EFVW DT5J FFAK N5C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
            ]

EG_NAME = 'EG1'

# Enclosures
ENC1 = 'wpst20'
# Interconnects
ENC1ICBAY1 = '%s, interconnect 1' % ENC1
ENC1ICBAY2 = '%s, interconnect 2' % ENC1
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY4 = '%s, interconnect 4' % ENC1
ENC1ICBAY5 = '%s, interconnect 5' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
ENC1ICBAY7 = '%s, interconnect 7' % ENC1
ENC1ICBAY8 = '%s, interconnect 8' % ENC1
# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1
ENC1SHBAY2 = '%s, bay 2' % ENC1
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY4 = '%s, bay 4' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC1SHBAY8 = '%s, bay 8' % ENC1
ENC1SHBAY9 = '%s, bay 9' % ENC1
ENC1SHBAY11 = '%s, bay 11' % ENC1
ENC1SHBAY12 = '%s, bay 12' % ENC1


# PROFILE1 SETTINGS
PROFILE1_NAME = 'Bay12_PXE_Boot'
PROFILE1_SHT = 'BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter'

# PROFILE2 SETTINGS
PROFILE2_NAME = 'Bay11_PXE_Boot'
PROFILE2_SHT = 'BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter'


# 2 Connections IPv4 Only
two_connections_ipv4 = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY12,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             }
        ]
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# one connection IPv6 Only
one_connection_ipv6 = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY11,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "IPv6"
    },
    "connections": [
        {"id": 1,
         "name": "PXE-boot-primary",
         "functionType": "Ethernet",
         "requestedMbps": "2500",
         "networkUri": 'ETH:net300',
         "boot": {
             "priority": "Primary",
             "ethernetBootType": "PXE",
         },
         },
    ],
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# one connection IPv6 Only edit to two connections auto
one_connection_ipv6_edit1 = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY11,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             }
        ]
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# 2 Connections IPv4 Only edit to one connection IPv6
two_connections_ipv4_edit1 = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY12,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "IPv6"
    },
    "connectionSettings": {
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
        ]
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# edit to one connection IPv4
one_connection_ipv6_edit2 = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY11,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
        ]
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# edit to two connections Auto
two_connections_ipv4_edit2 = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY12,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             }
        ]
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}


# Templates
ipv4_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

ipv6_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "IPv6"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             },
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

auto_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "PXE_Boot_Auto_Template",
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             },
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

ipv4_template_edit1 = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             },
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

ipv6_template_edit1 = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

auto_template_edit1 = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "PXE_Boot_Auto_Template",
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "IPv6"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             },
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}


ipv4_template_edit2 = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "IPv6"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             },
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

ipv6_template_edit2 = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

auto_template_edit2 = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "PXE_Boot_Auto_Template",
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             },
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}


# Create profiles from Templates
profile1_from_spt = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY12,
    'serverProfileTemplateUri': 'SPT:' + PROFILE1_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "IPv6"
    },
    "connectionSettings": {
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             },
        ]
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

profile2_from_spt = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY11,
    'serverProfileTemplateUri': 'SPT:' + PROFILE2_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
        ]
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}


# Compliance Test
non_compliant_profile1_from_spt_profile_edit = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY12,
    'serverProfileTemplateUri': 'SPT:' + PROFILE1_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
        ]
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

non_compliant_profile2_from_spt_profile_edit = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY11,
    'serverProfileTemplateUri': 'SPT:' + PROFILE2_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "IPv6"
    },
    "connectionSettings": {
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             },
        ]
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

non_compliant_profile1_from_spt_template_edit = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

non_compliant_profile2_from_spt_template_edit = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}


# RIS Data
ris_pxe_profile1_ipv4 = {
    "server": ENC1SHBAY12,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "PrebootNetworkEnvPolicy": "IPv4",
        }
    }
}

ris_pxe_profile1_ipv6 = {
    "server": ENC1SHBAY12,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "PrebootNetworkEnvPolicy": "IPv6",
        }
    }
}

ris_pxe_profile1_auto = {
    "server": ENC1SHBAY12,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "PrebootNetworkEnvPolicy": "Auto",
        }
    }
}

ris_pxe_profile2_ipv4 = {
    "server": ENC1SHBAY11,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "PrebootNetworkEnvPolicy": "IPv4",
        }
    }
}

ris_pxe_profile2_ipv6 = {
    "server": ENC1SHBAY11,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "PrebootNetworkEnvPolicy": "IPv6",
        }
    }
}

ris_pxe_profile2_auto = {
    "server": ENC1SHBAY11,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "PrebootNetworkEnvPolicy": "Auto",
        }
    }
}


# Compliance data

sp_compliant_profile1 = {
    "name": PROFILE1_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": []
    }
}

sp_compliant_profile2 = {
    "name": PROFILE2_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": []
    }
}

sp_non_compliant1_profile1 = {
    "name": PROFILE1_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [
            'Change PXE boot policy to IPv6.',
            'REGEX:Create a connection to network {\"name\":\"net300\", \"uri\":\".*\"} with id \d on FlexibleLOM \(Flb\) \d:\d-\w.',
        ],
        "manualUpdates": []
    }
}

sp_non_compliant1_profile2 = {
    "name": PROFILE2_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [
            'Change PXE boot policy to IPv6.',
            'REGEX:Delete the connection with id \d on FlexibleLOM \(Flb\) \d:\d-\w\.',
        ],
        "manualUpdates": []
    }
}

sp_non_compliant2_profile1 = {
    "name": PROFILE1_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [
            'Change PXE boot policy to Auto.',
            'REGEX:Delete the connection with id \d on FlexibleLOM \(Flb\) \d:\d-\w\.',
        ],
        "manualUpdates": []
    }
}

sp_non_compliant2_profile2 = {
    "name": PROFILE2_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [
            "Change PXE boot policy to IPv4."
        ],
        "manualUpdates": []
    }
}


# Negative Profile Data
create_profile_for_neg_edit_tests = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Edit Profile Test",
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             }
        ]
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

neg_ipv4thenipv6_profile = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Profile Test - Gen10 with PXE policy: IPv4 Then TPv6",
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "IPv4ThenIPv6"
    },
    "connectionSettings": {
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             }
        ]
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

neg_ipv6thenipv4_profile = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Profile Test - Gen10 with PXE policy: IPv6 Then TPv4",
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "IPv6ThenIPv4"
    },
    "connectionSettings": {
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             }
        ]
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

neg_multiple_primary_profile = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Profile Test - Multiple PXE Primary Connections",
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary1",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-primary2",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             }
        ]
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

neg_multiple_secondary_profile = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Profile Test - Multiple PXE Secondary Connections",
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "connections": [
            {"id": 1,
             "name": "PXE-boot-secondary1",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary2",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             }
        ]
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

neg_only_secondary_profile = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Profile Test - Only PXE Secondary Connection",
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "connections": [
            {"id": 1,
             "name": "PXE-boot-secondary1",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             },
        ]
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

neg_ipv4thenipv6_edit_profile = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Edit Profile Test",
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "IPv4ThenIPv6"
    },
    "connectionSettings": {
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             }
        ]
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

neg_ipv6thenipv4_edit_profile = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Edit Profile Test",
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "IPv6ThenIPv4"
    },
    "connectionSettings": {
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             }
        ]
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}


# Negative Template Data
create_template_for_neg_edit_tests = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Edit Template Test",
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             }
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

neg_ipv4thenipv6_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Template Test - Gen10 with PXE policy: IPv4 Then TPv6",
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "IPv4ThenIPv6"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             }
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

neg_ipv6thenipv4_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Template Test - Gen10 with PXE policy: IPv6 Then TPv4",
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "IPv6ThenIPv4"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             }
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

neg_multiple_primary_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Template Test - Multiple PXE Primary Connections",
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary1",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-primary2",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             }
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

neg_multiple_secondary_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Template Test - Multiple PXE Secondary Connections",
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1,
             "name": "PXE-boot-secondary1",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary2",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             }
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

neg_only_secondary_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Template Test - Only PXE Secondary Connection",
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "IPv4"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1,
             "name": "PXE-boot-secondary1",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             },
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

neg_ipv4thenipv6_edit_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Edit Template Test",
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "IPv4ThenIPv6"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             }
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

neg_ipv6thenipv4_edit_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative Edit Template Test",
    "affinity": "Bay",
    "bios": {
        "manageBios": False,
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "IPv6ThenIPv4"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1,
             "name": "PXE-boot-primary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "PXE",
             },
             },
            {"id": 2,
             "name": "iSCSI-boot-secondary",
             "functionType": "Ethernet",
             "requestedMbps": "2500",
             "networkUri": 'ETH:net300',
             "boot": {
                 "priority": "Secondary",
                 "ethernetBootType": "PXE",
             },
             }
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}


ts0_create_profiles = [
    create_profile_for_neg_edit_tests.copy(),
]

negative_profile_tasks = [
    {
        'keyword': 'Add Server Profile',
        'argument': neg_ipv4thenipv6_profile.copy(),
        'taskState': 'Error',
        'errorMessage': 'PXE_BOOT_POLICY_ERROR_IPV4_THEN_IPV6'},
    {
        'keyword': 'Add Server Profile',
        'argument': neg_ipv6thenipv4_profile.copy(),
        'taskState': 'Error',
        'errorMessage': 'PXE_BOOT_POLICY_ERROR_IPV6_THEN_IPV4'},
    {
        'keyword': 'Add Server Profile',
        'argument': neg_multiple_primary_profile.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_primary_boot'},
    {
        'keyword': 'Add Server Profile',
        'argument': neg_multiple_secondary_profile.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_secondary_boot'},
    {
        'keyword': 'Add Server Profile',
        'argument': neg_only_secondary_profile.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_secondary_boot_connection'},
    {
        'keyword': 'Edit Server Profile',
        'argument': neg_ipv4thenipv6_edit_profile.copy(),
        'taskState': 'Error',
        'errorMessage': 'PXE_BOOT_POLICY_ERROR_IPV4_THEN_IPV6'},
    {
        'keyword': 'Edit Server Profile',
        'argument': neg_ipv6thenipv4_edit_profile.copy(),
        'taskState': 'Error',
        'errorMessage': 'PXE_BOOT_POLICY_ERROR_IPV6_THEN_IPV4'},
]

ts1_create_profiles = [
    two_connections_ipv4.copy(),
    # one_connection_ipv6.copy()
]

ts1_edit_profiles1 = [
    two_connections_ipv4_edit1.copy(),
    # one_connection_ipv6_edit1.copy()
]

ts1_edit_profiles2 = [
    two_connections_ipv4_edit2.copy(),
    # one_connection_ipv6_edit2.copy()
]

ts1_ris_after_create = [
    ris_pxe_profile1_ipv4.copy(),
    # ris_pxe_profile2_ipv6.copy(),
]

ts1_ris_after_edit1 = [
    ris_pxe_profile1_ipv6.copy(),
    # ris_pxe_profile2_auto.copy(),
]

ts1_ris_after_edit2 = [
    ris_pxe_profile1_auto.copy(),
    # ris_pxe_profile2_ipv4.copy(),
]

ts2_create_profiles_template = [
    auto_template.copy(),
    ipv4_template.copy(),
    ipv6_template.copy(),
]

ts2_edit_profiles1_template = [
    auto_template_edit1.copy(),
    ipv4_template_edit1.copy(),
    ipv6_template_edit1.copy(),
]

ts2_edit_profiles2_template = [
    auto_template_edit2.copy(),
    ipv4_template_edit2.copy(),
    ipv6_template_edit2.copy(),
]

ts3_create_profile_templates = [
    create_template_for_neg_edit_tests.copy(),
]

negative_template_tasks = [
    {
        'keyword': 'Add Server Profile Template',
        'argument': neg_ipv4thenipv6_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'PXE_BOOT_POLICY_ERROR_IPV4_THEN_IPV6'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': neg_ipv6thenipv4_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'PXE_BOOT_POLICY_ERROR_IPV6_THEN_IPV4'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': neg_multiple_primary_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_primary_boot'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': neg_multiple_secondary_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_secondary_boot'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': neg_only_secondary_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_secondary_boot_connection'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': neg_ipv4thenipv6_edit_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'PXE_BOOT_POLICY_ERROR_IPV4_THEN_IPV6'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': neg_ipv6thenipv4_edit_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'PXE_BOOT_POLICY_ERROR_IPV6_THEN_IPV4'},
]

ts4_create_sp_from_spt = [
    profile1_from_spt.copy(),
    # profile2_from_spt.copy(),
]

ts4_ris_after_create_from_spt = [
    ris_pxe_profile1_ipv6.copy(),
    # ris_pxe_profile2_auto.copy(),
]

ts5_edit_sp_non_compliant = [
    non_compliant_profile1_from_spt_profile_edit.copy(),
    # non_compliant_profile2_from_spt_profile_edit.copy(),
]

ts5_edit_spt_non_compliant = [
    non_compliant_profile1_from_spt_template_edit.copy(),
    # non_compliant_profile2_from_spt_template_edit.copy(),
]

ts4_sp_compliance = [
    sp_compliant_profile1.copy(),
    # sp_compliant_profile2.copy(),
]

ts5_sp_non_compliant1 = [
    sp_non_compliant1_profile1.copy(),
    # sp_non_compliant1_profile2.copy(),
]

ts5_sp_non_compliant2 = [
    sp_non_compliant2_profile1.copy(),
    # sp_non_compliant2_profile2.copy(),
]

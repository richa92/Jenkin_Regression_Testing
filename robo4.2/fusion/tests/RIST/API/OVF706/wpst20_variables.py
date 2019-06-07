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

BOOT_URL1 = "http://wpstwork4.vse.rdlabs.hpecorp.net/software_distributions/miniLinux/Core-current.iso"
BOOT_URL2 = "https://wpstwork4.vse.rdlabs.hpecorp.net/software_distributions/miniLinux/nanolinux64-1.3.iso"
BOOT_URL3 = "http://wpstwork4.vse.rdlabs.hpecorp.net/software_distributions/miniLinux/Porteus-v3.1-x86_64.iso"
BOOT_URL4 = "http://wpstwork4.vse.rdlabs.hpecorp.net/software_distributions/miniLinux/TinyCore-current.iso"
BOOT_URL5 = "https://[2002:107d:4024::107d:4024]/software_distributions/miniLinux/CorePlus-current.iso"
BOOT_URL6 = "http://[2002:107d:4024::107d:4024]/software_distributions/miniLinux/nanolinux64-1.3.iso"
BOOT_URL7 = "https://[2002:107d:4024::107d:4024]/software_distributions/miniLinux/Porteus-v3.1-x86_64.iso"
BOOT_URL8 = "http://[2002:107d:4024::107d:4024]/software_distributions/miniLinux/Core-current.iso"

BAD_URL1 = "http://192.168/software_distributions/miniLinux/Core-current.iso"
BAD_URL2 = "http://wpstwork4.vse.rdlabs.hpecorp.net/software_distributions/miniLinux/"
BAD_URL3 = "http://wpstwork4.vse.rdlabs.hpecorp.net/software_distributions/miniLinux/Core-current.exe"
BAD_URL4 = "https://[2002::107d:4024::O000:107d:4024]/software_distributions/miniLinux/Porteus-v3.1-x86_64.iso"

# PROFILE1 SETTINGS
PROFILE1_NAME = 'Gen10_multiple_boot_url_test'
PROFILE1_SHT = 'BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter'


# 4 Bootable URLs
four_bootable_urls = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY12,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL1
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL2
            },
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL3
            },
            {
                "id": "UrlBootFile4",
                "value": BOOT_URL4
            },
        ]
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
    "connections": [],
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# 4 Bootable URLs (edit to different URLs)
four_bootable_urls_edit = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY12,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL5
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL6
            },
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL7
            },
            {
                "id": "UrlBootFile4",
                "value": BOOT_URL8
            },
        ]
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
    "connections": [],
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# 3 Bootable URLs
three_bootable_urls = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY12,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL1
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL2
            },
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL3
            },
        ]
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
    "connections": [],
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# 2 Bootable URLs
two_bootable_urls = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY12,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL1
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL2
            },
        ]
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
    "connections": [],
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# 1 Bootable URL
only_first_bootable_url = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY12,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL1
            },
        ]
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
    "connections": [],
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Only 2nd Bootable URL
only_second_bootable_url = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY12,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL2
            },
        ]
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
    "connections": [],
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Only 3rd Bootable URL
only_third_bootable_url = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY12,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL3
            },
        ]
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
    "connections": [],
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Only 4th Bootable URL
only_fourth_bootable_url = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY12,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile4",
                "value": BOOT_URL4
            },
        ]
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
    "connections": [],
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Bad URL1
bad_url1 = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY12,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "bad_url_test_1",
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BAD_URL1
            },
        ]
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
    "connections": [],
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Bad URL2
bad_url2 = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY12,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "bad_url_test_2",
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile2",
                "value": BAD_URL2
            },
        ]
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
    "connections": [],
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Bad URL3
bad_url3 = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY12,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "bad_url_test_3",
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile3",
                "value": BAD_URL3
            },
        ]
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
    "connections": [],
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Bad URL4
bad_url4 = {
    "type": "ServerProfileV9",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + ENC1SHBAY12,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "bad_url_test_4",
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile4",
                "value": BAD_URL4
            },
        ]
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
    "connections": [],
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

# RIS validation for Four Bootable URLs
ris_four_bootable_urls = {
    "server": ENC1SHBAY12,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "UrlBootFile": BOOT_URL1,
            "UrlBootFile2": BOOT_URL2,
            "UrlBootFile3": BOOT_URL3,
            "UrlBootFile4": BOOT_URL4,
        }
    }
}

# RIS validation for Four Bootable URLs after edit
ris_four_bootable_urls_edit = {
    "server": ENC1SHBAY12,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "UrlBootFile": BOOT_URL5,
            "UrlBootFile2": BOOT_URL6,
            "UrlBootFile3": BOOT_URL7,
            "UrlBootFile4": BOOT_URL8,
        }
    }
}

# RIS validation for three Bootable URLs
ris_three_bootable_urls = {
    "server": ENC1SHBAY12,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "UrlBootFile": BOOT_URL1,
            "UrlBootFile2": BOOT_URL2,
            "UrlBootFile3": BOOT_URL3,
            "UrlBootFile4": "",
        },
    }
}

# RIS validation for two Bootable URLs
ris_two_bootable_urls = {
    "server": ENC1SHBAY12,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "UrlBootFile": BOOT_URL1,
            "UrlBootFile2": BOOT_URL2,
            "UrlBootFile3": "",
            "UrlBootFile4": "",
        },
    }
}

# RIS validation for one Bootable URL
ris_only_first_bootable_url = {
    "server": ENC1SHBAY12,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "UrlBootFile": BOOT_URL1,
            "UrlBootFile2": "",
            "UrlBootFile3": "",
            "UrlBootFile4": "",
        },
    }
}

# RIS validation for only second Bootable URL
ris_only_second_bootable_url = {
    "server": ENC1SHBAY12,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "UrlBootFile": "",
            "UrlBootFile2": BOOT_URL2,
            "UrlBootFile3": "",
            "UrlBootFile4": "",
        },
    }
}

# RIS validation for only third Bootable URL
ris_only_thrid_bootable_url = {
    "server": ENC1SHBAY12,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "UrlBootFile": "",
            "UrlBootFile2": "",
            "UrlBootFile3": BOOT_URL3,
            "UrlBootFile4": "",
        },
    }
}

# RIS validation for only fourth Bootable URL
ris_only_fourth_bootable_url = {
    "server": ENC1SHBAY12,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "UrlBootFile": "",
            "UrlBootFile2": "",
            "UrlBootFile3": "",
            "UrlBootFile4": BOOT_URL4,
        },
    }
}

# 4 Bootable URLs template
four_bootable_urls_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL1
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL2
            },
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL3
            },
            {
                "id": "UrlBootFile4",
                "value": BOOT_URL4
            },
        ]
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
        "manageConnections": False,
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

# 4 Bootable URLs from Template
four_bootable_urls_from_spt = {
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
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL1
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL2
            },
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL3
            },
            {
                "id": "UrlBootFile4",
                "value": BOOT_URL4
            },
        ]
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
    "connections": [],
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# 4 Bootable URLs (edit to different URLs) template
four_bootable_urls_edit_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL5
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL6
            },
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL7
            },
            {
                "id": "UrlBootFile4",
                "value": BOOT_URL8
            },
        ]
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
        "manageConnections": False,
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

# 4 Bootable URLs from Template
four_bootable_urls_from_spt_edit = {
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
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL4
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL3
            },
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL2
            },
            {
                "id": "UrlBootFile4",
                "value": BOOT_URL1
            },
        ]
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
    "connections": [],
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# 3 Bootable URLs template
three_bootable_urls_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL1
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL2
            },
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL3
            },
        ]
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
        "manageConnections": False,
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

# 2 Bootable URLs template
two_bootable_urls_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL1
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL2
            },
        ]
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
        "manageConnections": False,
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

# 1 Bootable URL template
only_first_bootable_url_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL6
            },
        ]
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
        "manageConnections": False,
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

# Only 2nd Bootable URL template
only_second_bootable_url_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL2
            },
        ]
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
        "manageConnections": False,
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

# Only 3rd Bootable URL template
only_third_bootable_url_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL3
            },
        ]
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
        "manageConnections": False,
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

# Only 4th Bootable URL template
only_fourth_bootable_url_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile4",
                "value": BOOT_URL4
            },
        ]
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
        "manageConnections": False,
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

# Bad URL1 template
bad_url1_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "bad_url_test_1",
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BAD_URL1
            },
        ]
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
        "manageConnections": False,
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

# Bad URL2 template
bad_url2_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "bad_url_test_2",
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile2",
                "value": BAD_URL2
            },
        ]
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
        "manageConnections": False,
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

# Bad URL3 template
bad_url3_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "bad_url_test_3",
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile3",
                "value": BAD_URL3
            },
        ]
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
        "manageConnections": False,
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

# Bad URL4 template
bad_url4_template = {
    "type": "ServerProfileTemplateV5",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "bad_url_test_4",
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile4",
                "value": BAD_URL4
            },
        ]
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
        "manageConnections": False,
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

sp_compliant_profile1 = {
    "name": PROFILE1_NAME,
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
            'REGEX:Change BIOS setting \"Boot from URL 1\" to \"' + BOOT_URL1 + '\".',
            'REGEX:Change BIOS setting \"Boot from URL 2\" to \"' + BOOT_URL2 + '\".',
            'REGEX:Change BIOS setting \"Boot from URL 3\" to \"' + BOOT_URL3 + '\".',
            'REGEX:Change BIOS setting \"Boot from URL 4\" to \"' + BOOT_URL4 + '\".',
        ],
        "manualUpdates": []
    }
}

sp_non_compliant2_profile1 = {
    "name": PROFILE1_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [
            'REGEX:Change BIOS setting \"Boot from URL 1\" to the default value \"\".',
            'REGEX:Change BIOS setting \"Boot from URL 2\" to the default value \"\".',
            'REGEX:Change BIOS setting \"Boot from URL 4\" to the default value \"\".',
        ],
        "manualUpdates": []
    }
}

ts1_create_profiles = [
    four_bootable_urls.copy(),
]

ts1_edit_profiles1 = [
    four_bootable_urls_edit.copy(),
]

ts1_edit_profiles2 = [
    three_bootable_urls.copy(),
]

ts1_edit_profiles3 = [
    two_bootable_urls.copy(),
]

ts1_ris_after_create = [
    ris_four_bootable_urls.copy(),
]

ts1_ris_after_edit1 = [
    ris_four_bootable_urls_edit.copy(),
]

ts1_ris_after_edit2 = [
    ris_three_bootable_urls.copy(),
]

ts1_ris_after_edit3 = [
    ris_two_bootable_urls.copy(),
]

ts2_create_profiles = [
    only_fourth_bootable_url.copy(),
]

ts2_edit_profiles1 = [
    only_third_bootable_url.copy(),
]

ts2_edit_profiles2 = [
    only_second_bootable_url.copy(),
]

ts2_edit_profiles3 = [
    only_first_bootable_url.copy(),
]

ts2_ris_after_create = [
    ris_only_fourth_bootable_url.copy(),
]

ts2_ris_after_edit1 = [
    ris_only_thrid_bootable_url.copy(),
]

ts2_ris_after_edit2 = [
    ris_only_second_bootable_url.copy(),
]

ts2_ris_after_edit3 = [
    ris_only_first_bootable_url.copy(),
]

negative_tasks = [
    {
        'keyword': 'Add Server Profile',
        'argument': bad_url1.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_PROFILE_BOOT_URL'},
    {
        'keyword': 'Add Server Profile',
        'argument': bad_url2.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_PROFILE_BOOT_URL'},
    {
        'keyword': 'Add Server Profile',
        'argument': bad_url2.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_PROFILE_BOOT_URL'},
    {
        'keyword': 'Add Server Profile',
        'argument': bad_url2.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_PROFILE_BOOT_URL'},
]


ts3_create_profiles_template = [
    four_bootable_urls_template.copy(),
]

ts3_edit_profiles1_template = [
    four_bootable_urls_edit_template.copy(),
]

ts3_edit_profiles2_template = [
    three_bootable_urls_template.copy(),
]

ts3_edit_profiles3_template = [
    two_bootable_urls_template.copy(),
]

ts4_create_profiles_template = [
    only_fourth_bootable_url_template.copy(),
]

ts4_edit_profiles1_template = [
    only_third_bootable_url_template.copy(),
]

ts4_edit_profiles2_template = [
    only_second_bootable_url_template.copy(),
]

ts4_edit_profiles3_template = [
    only_first_bootable_url_template.copy(),
]

create_sp_from_spt = [
    four_bootable_urls_from_spt.copy(),
]

edit_sp_non_compliant = [
    four_bootable_urls_from_spt_edit.copy(),
]

edit_spt_non_compliant = [
    only_third_bootable_url_template.copy(),
]

sp_compliance = [
    sp_compliant_profile1.copy(),
]

sp_non_compliant1 = [
    sp_non_compliant1_profile1.copy(),
]

sp_non_compliant2 = [
    sp_non_compliant2_profile1.copy(),
]

negative_spt_tasks = [
    {
        'keyword': 'Add Server Profile Template',
        'argument': bad_url1_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_TEMPLATE_BOOT_URL'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': bad_url2_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_TEMPLATE_BOOT_URL'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': bad_url2_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_TEMPLATE_BOOT_URL'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': bad_url2_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_TEMPLATE_BOOT_URL'},
]

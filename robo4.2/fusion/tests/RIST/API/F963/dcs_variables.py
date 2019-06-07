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
ENC1SHBAY2 = '%s, bay 2' % ENC1
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
STORAGE_POOL_NETWORK = 'ETH:Untagged'
VOLUME_TEMPLATE = 'volume-template'
ETHERNET_BLADE = ENC1SHBAY2
ISCSI_BLADE = ENC1SHBAY3
NEG_ISCSI_BLADE = ENC1SHBAY4
NEG_ETHERNET_BLADE = ENC1SHBAY5
ETHERNET_BLADE_VOL = 'tbird8-bay1-F963'
ETHERNET_BLADE_VOL_2 = 'tbird8-bay1-F963-2'
ISCSI_BLADE_VOL = 'tbird8-bay2-F963'
ISCSI_BLADE_VOL_2 = 'tbird8-bay2-F963-2'
ISCSI_BLADE_VOL_SHARED = 'tbird8-bay2-F963-shared'

vol_sp = [
    {
        "properties": {
            "storagePool": STORAGE_POOL,
            "size": 6000000,
            "dataProtectionLevel": "NetworkRaid5SingleParity",
            "name": ETHERNET_BLADE_VOL,
        },
        "templateUri": VOLUME_TEMPLATE,
        "isPermanent": True,
    },
    {
        "properties": {
            "storagePool": STORAGE_POOL,
            "size": 6000000,
            "dataProtectionLevel": "NetworkRaid5SingleParity",
            "name": ISCSI_BLADE_VOL
        },
        "templateUri": VOLUME_TEMPLATE,
        "isPermanent": True,
    },
    {
        "properties": {
            "storagePool": STORAGE_POOL,
            "size": 6000000,
            "dataProtectionLevel": "NetworkRaid5SingleParity",
            "name": ETHERNET_BLADE_VOL_2
        },
        "templateUri": VOLUME_TEMPLATE,
        "isPermanent": True,
    },
    {
        "properties": {
            "storagePool": STORAGE_POOL,
            "size": 6000000,
            "dataProtectionLevel": "NetworkRaid5SingleParity",
            "name": ISCSI_BLADE_VOL_2
        },
        "templateUri": VOLUME_TEMPLATE,
        "isPermanent": True,
    },
    {
        "properties": {
            "storagePool": STORAGE_POOL,
            "size": 6000000,
            "dataProtectionLevel": "NetworkRaid5SingleParity",
            "name": ISCSI_BLADE_VOL_SHARED,
            "isShareable": True,
        },
        "templateUri": VOLUME_TEMPLATE,
        "isPermanent": True,

    },
]


sp_sw_edit_add_secondary_connection = {
    "type": "ServerProfileV400",
    "name": "sp-ethernet",
    "iscsiInitiatorNameType": "AutoGenerated",
    'serverHardwareUri': 'SH:' + ETHERNET_BLADE,
    "category": "server-profiles",
    "connections": [{
        "id": 1,
        "name": "Connection 1",
        "functionType": "Ethernet",
        "networkUri": STORAGE_POOL_NETWORK,
        "ipv4": {
            "ipAddressSource": "UserDefined",
            "subnetMask": "255.255.255.0",
            "gateway": "16.125.64.1",
            "ipAddress": "16.125.64.11"
        },
        "boot": {
            "priority": "Primary",
            "ethernetBootType": "iSCSI",
            "bootVolumeSource": "ManagedVolume",
        }
    }, {
        "id": 2,
        "name": "connection 2",
        "functionType": "Ethernet",
        "networkUri": STORAGE_POOL_NETWORK,
        "ipv4": {
            "ipAddressSource": "UserDefined",
            "subnetMask": "255.255.255.0",
            "gateway": "",
            "ipAddress": "192.168.22.58"
        },
        "boot": {
            "priority": "Secondary",
            "ethernetBootType": "iSCSI",
            "bootVolumeSource": "ManagedVolume",
        }
    }],
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": []
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [{
            "id": 1,
            "volumeUri": "SVOL:" + ETHERNET_BLADE_VOL,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, {
                "isEnabled": True,
                "connectionId": 2,
                "targetSelector": "Auto",
                "targets": []
            }]
        }]
    },
}

sp_sw_edit_boot_volume = {
    "type": "ServerProfileV400",
    "name": "sp-ethernet",
    "iscsiInitiatorNameType": "AutoGenerated",
    'serverHardwareUri': 'SH:' + ETHERNET_BLADE,
    "category": "server-profiles",
    "connections": [{
        "id": 1,
        "name": "Connection 1",
        "functionType": "Ethernet",
        "networkUri": STORAGE_POOL_NETWORK,
        "ipv4": {
            "ipAddressSource": "UserDefined",
            "subnetMask": "255.255.255.0",
            "gateway": "16.125.64.1",
            "ipAddress": "16.125.64.11"
        },
        "boot": {
            "priority": "Primary",
            "ethernetBootType": "iSCSI",
            "bootVolumeSource": "ManagedVolume",
        }
    }, {
        "id": 2,
        "name": "connection 2",
        "functionType": "Ethernet",
        "networkUri": STORAGE_POOL_NETWORK,
        "ipv4": {
            "ipAddressSource": "UserDefined",
            "subnetMask": "255.255.255.0",
            "gateway": "",
            "ipAddress": "192.168.22.58"
        },
        "boot": {
            "priority": "Secondary",
            "ethernetBootType": "iSCSI",
            "bootVolumeSource": "ManagedVolume",
        }
    }],
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": []
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [{
            "id": 1,
            "volumeUri": "SVOL:" + ETHERNET_BLADE_VOL,
            "isBootVolume": False,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": False,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, {
                "isEnabled": False,
                "connectionId": 2,
                "targetSelector": "Auto",
                "targets": []
            }]
        },
            {
            "id": 2,
            "volumeUri": "SVOL:" + ETHERNET_BLADE_VOL_2,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, {
                "isEnabled": True,
                "connectionId": 2,
                "targetSelector": "Auto",
                "targets": []
            }]
        }
        ]
    },
}

sp_hw_edit_add_secondary_connection = {
    "type": "ServerProfileV400",
    "name": "sp-iscsi",
    "iscsiInitiatorNameType": "AutoGenerated",
    'serverHardwareUri': 'SH:' + ISCSI_BLADE,
    "category": "server-profiles",
    "connections": [{
        "id": 1,
        "name": "Connection 1",
        "functionType": "iSCSI",
        "networkUri": STORAGE_POOL_NETWORK,
        "ipv4": {
            "ipAddressSource": "UserDefined",
            "subnetMask": "255.255.255.0",
            "gateway": "16.125.64.1",
            "ipAddress": "16.125.64.60"
        },
        "boot": {
            "priority": "Primary",
            "bootVolumeSource": "ManagedVolume",
        }
    }, {
        "id": 2,
        "name": "connection 2",
        "functionType": "iSCSI",
        "networkUri": STORAGE_POOL_NETWORK,
        "ipv4": {
            "ipAddressSource": "UserDefined",
            "subnetMask": "255.255.255.0",
            "gateway": "",
            "ipAddress": "192.168.22.59"
        },
        "boot": {
            "priority": "Secondary",
            "bootVolumeSource": "ManagedVolume",
        }
    }],
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": []
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [{
            "id": 1,
            "volumeUri": "SVOL:" + ISCSI_BLADE_VOL,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, {
                "isEnabled": True,
                "connectionId": 2,
                "targetSelector": "Auto",
                "targets": []
            }]
        }]
    },
}

sp_hw_edit_boot_volume = {
    "type": "ServerProfileV400",
    "name": "sp-iscsi",
    "iscsiInitiatorNameType": "AutoGenerated",
    'serverHardwareUri': 'SH:' + ISCSI_BLADE,
    "category": "server-profiles",
    "connections": [{
        "id": 1,
        "name": "Connection 1",
        "functionType": "iSCSI",
        "networkUri": STORAGE_POOL_NETWORK,
        "ipv4": {
            "ipAddressSource": "UserDefined",
            "subnetMask": "255.255.255.0",
            "gateway": "16.125.64.1",
            "ipAddress": "16.125.64.60"
        },
        "boot": {
            "priority": "Primary",
            "bootVolumeSource": "ManagedVolume",
        }
    }, {
        "id": 2,
        "name": "connection 2",
        "functionType": "iSCSI",
        "networkUri": STORAGE_POOL_NETWORK,
        "ipv4": {
            "ipAddressSource": "UserDefined",
            "subnetMask": "255.255.255.0",
            "gateway": "",
            "ipAddress": "192.168.22.59"
        },
        "boot": {
            "priority": "Secondary",
            "bootVolumeSource": "ManagedVolume",
        }
    }],
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": []
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [{
            "id": 1,
            "volumeUri": "SVOL:" + ISCSI_BLADE_VOL,
            "isBootVolume": False,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": False,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, {
                "isEnabled": False,
                "connectionId": 2,
                "targetSelector": "Auto",
                "targets": []
            }]
        },
            {
            "id": 2,
            "volumeUri": "SVOL:" + ISCSI_BLADE_VOL_2,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, {
                "isEnabled": True,
                "connectionId": 2,
                "targetSelector": "Auto",
                "targets": []
            }]
        }
        ]
    },
}

sp_power = [
    {
        'serverHardwareUri': 'SH:' + ETHERNET_BLADE,
    },
    {
        'serverHardwareUri': 'SH:' + ISCSI_BLADE,
    },
    {
        'serverHardwareUri': 'SH:' + NEG_ISCSI_BLADE,
    },
    {
        'serverHardwareUri': 'SH:' + NEG_ETHERNET_BLADE,
    },
]

sp_1 = [
    {
        "type": "ServerProfileV400",
        'serverHardwareUri': 'SH:' + ETHERNET_BLADE,
        "enclosureGroupUri": "EG:" + EG_NAME,
        "name": "sp-ethernet",
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
                    "priority": "Primary"
                },
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "gateway": "16.125.64.1",
                    "ipAddress": "16.125.64.11",
                    "subnetMask": "255.255.255.0"
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [{
                "id": 1,
                "lunType": "Auto",
                "isBootVolume": True,
                "volumeUri": "SVOL:" + ETHERNET_BLADE_VOL,
                "storagePaths": [{
                    "connectionId": 1,
                    "isEnabled": True
                }]
            }]
        }
    },
    {
        "type": "ServerProfileV400",
        'serverHardwareUri': 'SH:' + ISCSI_BLADE,
        "enclosureGroupUri": "EG:" + EG_NAME,
        "name": "sp-iscsi",
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
                    "priority": "Primary"
                },
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "gateway": "16.125.64.1",
                    "ipAddress": "16.125.64.22",
                    "subnetMask": "255.255.255.0"
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [{
                "id": 1,
                "lunType": "Auto",
                "isBootVolume": True,
                "volumeUri": "SVOL:" + ISCSI_BLADE_VOL,
                "storagePaths": [{
                    "connectionId": 1,
                    "isEnabled": True
                }]
            }]
        }
    },
]

negative_sp_1 = {
    "type": "ServerProfileV400",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serverHardwareUri": "SH:" + NEG_ISCSI_BLADE,
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
                "iscsi": None,
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.31",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        },
        {
            "boot": {
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
                "iscsi": None,
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 2,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.32",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 2",
            "networkUri": STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": "SVOL:" + ISCSI_BLADE_VOL,
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
    "serverHardwareUri": "SH:" + NEG_ISCSI_BLADE,
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
                "iscsi": None,
                "priority": "Secondary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.31",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        },
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": "SVOL:" + ISCSI_BLADE_VOL,
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
    "serverHardwareUri": "SH:" + NEG_ISCSI_BLADE,
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
                "iscsi": None,
                "priority": "Secondary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.31",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        },
        {
            "boot": {
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
                "iscsi": None,
                "priority": "Secondary"
            },
            "functionType": "Ethernet",
            "id": 2,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.32",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 2",
            "networkUri": STORAGE_POOL_NETWORK,
        },
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": "SVOL:" + ISCSI_BLADE_VOL,
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
    "serverHardwareUri": "SH:" + NEG_ISCSI_BLADE,
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
                "iscsi": None,
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.31",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        },
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": "SVOL:" + ISCSI_BLADE_VOL,
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
    "serverHardwareUri": "SH:" + NEG_ISCSI_BLADE,
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
                "iscsi": None,
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.31",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "isBootVolume": False,
            "volumeUri": "SVOL:" + ISCSI_BLADE_VOL,
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            }]
        }]
    }
}

negative_sp_6 = {
    "type": "ServerProfileV400",
    "serverHardwareUri": "SH:" + NEG_ISCSI_BLADE,
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
                "iscsi": None,
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.31",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        },
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": "SVOL:" + ISCSI_BLADE_VOL,
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            }],
        },
            {
            "id": 2,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": "SVOL:" + ISCSI_BLADE_VOL_2,
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
    "serverHardwareUri": "SH:" + NEG_ISCSI_BLADE,
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
                "iscsi": None,
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.31",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": "SVOL:" + ISCSI_BLADE_VOL_SHARED,
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
    "serverHardwareUri": "SH:" + NEG_ISCSI_BLADE,
    "name": "sp-ethernet-12",
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
                "iscsi": None,
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.31",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": "SVOL:" + ETHERNET_BLADE_VOL,
            "storagePaths": [
                  {
                      "connectionId": 1,
                      "isEnabled": False
                  }, ]
        }, ]
    }
}

negative_sp_9 = {
    "type": "ServerProfileV400",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serverHardwareUri": "SH:" + NEG_ISCSI_BLADE,
    "name": "negative_sp_9",
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
                "iscsi": None,
                "priority": "Primary"
            },
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "gateway": "16.125.64.1",
                "ipAddress": "16.125.64.31",
                "subnetMask": "255.255.255.0"
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "isBootVolume": True,
            "volumeUri": "SVOL:" + ISCSI_BLADE_VOL,
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True,
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
        'errorMessage': 'SP_Bootable_connection_nonbootable_volume'},
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

negative_sp_tasks_9 = [
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_9.copy(),
        'taskState': 'Error',
        'errorMessage': 'Already_attached_to_different_host'},
]

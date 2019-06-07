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
            {'key': '9AQA BQAA H9PA GHWZ V7B5 HWWB Y9JL KMPL SR2G 7AZU DXAU 2CSM GHTG L762 69VZ USJA KJVT D5KM EFVW DT5J VFQM 85S8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3G8YL-HHGX3-6M6KH-DZ99V-BDXMM'},
            {'key': 'YAAE DQAA H9P9 GHV3 U7B5 HWW5 Y9JL KMPL CRKE 6AJU DXAU 2CSM GHTG L762 H9Z2 WUZY KJVT D5KM EFVW DT5J FFAK N5C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
            ]

EG_NAME = 'EG1'

# Enclosures
ENC1 = 'wpst10'
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

INITIATOR_GATEWAY = "192.168.0.1"
INITIATOR_SUBNET_MASK = "255.255.192.0"
STORAGE_POOL = 'VSA_Cluster_173-2'
STORAGE_POOL_NETWORK = 'ETH:Untagged'
VOLUME_TEMPLATE = 'volume-template'
ETHERNET_BLADE = ENC1SHBAY1
ETHERNET_BLADE_INITIATOR_IP = '192.168.22.49'
ETHERNET_BLADE_INITIATOR_IP_2 = '192.168.22.50'
ISCSI_BLADE = ENC1SHBAY3
ISCSI_BLADE_INITIATOR_IP = '192.168.22.58'
ISCSI_BLADE_INITIATOR_IP_2 = '192.168.22.59'
NEG_ISCSI_BLADE = ENC1SHBAY1
NEG_ETHERNET_BLADE = ENC1SHBAY8
ETHERNET_BLADE_VOL = 'wpst10-bay1-F963'
ETHERNET_BLADE_VOL_2 = 'wpst10-bay1-F963-2'
ISCSI_BLADE_VOL = 'wpst10-bay2-F963'
ISCSI_BLADE_VOL_2 = 'wpst10-bay2-F963-2'
ISCSI_BLADE_VOL_SHARED = 'wpst10-bay2-F963-shared'


vol_sp = [
    {
        "properties": {
            "storagePool": STORAGE_POOL,
            "size": 10000000000,
            "dataProtectionLevel": "NetworkRaid5SingleParity",
            "name": ETHERNET_BLADE_VOL,
        },
        "templateUri": VOLUME_TEMPLATE,
        "isPermanent": True,
    },
    {
        "properties": {
            "storagePool": STORAGE_POOL,
            "size": 10000000000,
            "dataProtectionLevel": "NetworkRaid5SingleParity",
            "name": ISCSI_BLADE_VOL
        },
        "templateUri": VOLUME_TEMPLATE,
        "isPermanent": True,
    },
    {
        "properties": {
            "storagePool": STORAGE_POOL,
            "size": 10000000000,
            "dataProtectionLevel": "NetworkRaid5SingleParity",
            "name": ETHERNET_BLADE_VOL_2
        },
        "templateUri": VOLUME_TEMPLATE,
        "isPermanent": True,
    },
    {
        "properties": {
            "storagePool": STORAGE_POOL,
            "size": 10000000000,
            "dataProtectionLevel": "NetworkRaid5SingleParity",
            "name": ISCSI_BLADE_VOL_2
        },
        "templateUri": VOLUME_TEMPLATE,
        "isPermanent": True,
    },
    {
        "properties": {
            "storagePool": STORAGE_POOL,
            "size": 10000000000,
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
            "subnetMask": INITIATOR_SUBNET_MASK,
            "gateway": INITIATOR_GATEWAY,
            "ipAddress": ETHERNET_BLADE_INITIATOR_IP,
        },
        "boot": {
            "priority": "Primary",
            "bootVolumeSource": "ManagedVolume",
        }
    }, {
        "id": 2,
        "name": "connection 2",
        "functionType": "Ethernet",
        "networkUri": STORAGE_POOL_NETWORK,
        "ipv4": {
            "ipAddressSource": "UserDefined",
            "subnetMask": INITIATOR_SUBNET_MASK,
            "gateway": INITIATOR_GATEWAY,
            "ipAddress": ETHERNET_BLADE_INITIATOR_IP_2
        },
        "boot": {
            "priority": "Secondary",
            "bootVolumeSource": "ManagedVolume",
        }
    }],
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
            "subnetMask": INITIATOR_SUBNET_MASK,
            "gateway": INITIATOR_GATEWAY,
            "ipAddress": ETHERNET_BLADE_INITIATOR_IP,
        },
        "boot": {
            "priority": "Primary",
            "bootVolumeSource": "ManagedVolume",
        }
    }, {
        "id": 2,
        "name": "connection 2",
        "functionType": "Ethernet",
        "networkUri": STORAGE_POOL_NETWORK,
        "ipv4": {
            "ipAddressSource": "UserDefined",
            "subnetMask": INITIATOR_SUBNET_MASK,
            "gateway": INITIATOR_GATEWAY,
            "ipAddress": ETHERNET_BLADE_INITIATOR_IP_2
        },
        "boot": {
            "priority": "Secondary",
            "bootVolumeSource": "ManagedVolume",
        }
    }],
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
            "subnetMask": INITIATOR_SUBNET_MASK,
            "gateway": INITIATOR_GATEWAY,
            "ipAddress": ISCSI_BLADE_INITIATOR_IP
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
            "subnetMask": INITIATOR_SUBNET_MASK,
            "gateway": INITIATOR_GATEWAY,
            "ipAddress": ISCSI_BLADE_INITIATOR_IP_2
        },
        "boot": {
            "priority": "Secondary",
            "bootVolumeSource": "ManagedVolume",
        }
    }],
    "boot": {
        "order": ['HardDisk', 'CD', 'Floppy', 'USB', 'PXE'],
        "manageBoot": True
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
            "subnetMask": INITIATOR_SUBNET_MASK,
            "gateway": INITIATOR_GATEWAY,
            "ipAddress": ISCSI_BLADE_INITIATOR_IP
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
            "subnetMask": INITIATOR_SUBNET_MASK,
            "gateway": INITIATOR_GATEWAY,
            "ipAddress": ISCSI_BLADE_INITIATOR_IP_2
        },
        "boot": {
            "priority": "Secondary",
            "bootVolumeSource": "ManagedVolume",
        }
    }],
    "boot": {
        "order": ['HardDisk', 'CD', 'Floppy', 'USB', 'PXE'],
        "manageBoot": True
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
        'serverHardwareUri': 'SH:' + ISCSI_BLADE,
        "enclosureGroupUri": "EG:" + EG_NAME,
        "name": "sp-iscsi",
        "affinity": "Bay",
        "bios": {
            "manageBios": False
        },
        "boot": {
            "order": ['HardDisk', 'CD', 'Floppy', 'USB', 'PXE'],
            "manageBoot": True
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
                    "ipAddress": ISCSI_BLADE_INITIATOR_IP,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
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
    'serverHardwareUri': 'SH:' + NEG_ISCSI_BLADE,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "neg-sp-1",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk', 'CD', 'Floppy', 'USB', 'PXE'],
        "manageBoot": True
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
                "ipAddress": ISCSI_BLADE_INITIATOR_IP,
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY,
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        },
        {
            "boot": {
                "bootVolumeSource": "ManagedVolume",
                "priority": "Primary"
            },
            "functionType": "iSCSI",
            "id": 2,
            "ipv4": {
                "ipAddress": ISCSI_BLADE_INITIATOR_IP,
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY,
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
    'serverHardwareUri': 'SH:' + NEG_ISCSI_BLADE,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "neg-sp-2",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk', 'CD', 'Floppy', 'USB', 'PXE'],
        "manageBoot": True
    },
    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "bootVolumeSource": "ManagedVolume",
                "priority": "Secondary"
            },
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddress": ISCSI_BLADE_INITIATOR_IP,
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY,
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
        "order": ['HardDisk', 'CD', 'Floppy', 'USB', 'PXE'],
        "manageBoot": True
    },

    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "bootVolumeSource": "ManagedVolume",
                "iscsi": None,
                "priority": "Secondary"
            },
            "functionType": "iSCSI",
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
                "bootVolumeSource": "ManagedVolume",
                "iscsi": None,
                "priority": "Secondary"
            },
            "functionType": "iSCSI",
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
        "order": ['HardDisk', 'CD', 'Floppy', 'USB', 'PXE'],
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
                "bootVolumeSource": "ManagedVolume",
                "iscsi": None,
                "priority": "Primary"
            },
            "functionType": "iSCSI",
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
        "order": ['HardDisk', 'CD', 'Floppy', 'USB', 'PXE'],
        "manageBoot": True
    },

    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "bootVolumeSource": "ManagedVolume",
                "iscsi": None,
                "priority": "Primary"
            },
            "functionType": "iSCSI",
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
        "order": ['HardDisk', 'CD', 'Floppy', 'USB', 'PXE'],
        "manageBoot": True
    },

    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "bootVolumeSource": "ManagedVolume",
                "iscsi": None,
                "priority": "Primary"
            },
            "functionType": "iSCSI",
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
        "order": ['HardDisk', 'CD', 'Floppy', 'USB', 'PXE'],
        "manageBoot": True
    },

    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "bootVolumeSource": "ManagedVolume",
                "iscsi": None,
                "priority": "Primary"
            },
            "functionType": "iSCSI",
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
        "order": ['HardDisk', 'CD', 'Floppy', 'USB', 'PXE'],
        "manageBoot": True
    },
    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "bootVolumeSource": "ManagedVolume",
                "iscsi": None,
                "priority": "Primary"
            },
            "functionType": "iSCSI",
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
        "order": ['HardDisk', 'CD', 'Floppy', 'USB', 'PXE'],
        "manageBoot": True
    },
    "category": "server-profiles",
    "connections": [
        {
            "boot": {
                "bootVolumeSource": "ManagedVolume",
                "iscsi": None,
                "priority": "Primary"
            },
            "functionType": "iSCSI",
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

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

ilo_credentials = {'username': 'Administrator',
                   'password': 'hpvse123'
                   }

cliq_credentials = {'mgmt_ip': '16.71.148.116',
                    'username': 'admin',
                    'password': 'admin'
                    }

timeandlocale = {
    'type': 'TimeAndLocale',
    'dateTime': None,
    'timezone': 'UTC',
    'ntpServers': ['ntp.hpecorp.net'],
    'locale': 'en_US.UTF-8'}

users = [{'userName': 'Serveradmin', 'password': 'wpsthpvse1', 'fullName': 'Serveradmin', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Networkadmin',
          'password': 'wpsthpvse1',
          'fullName': 'Networkadmin',
          'roles': ['Network administrator'],
          'emailAddress': 'nat@hp.com',
          'officePhone': '970-555-0003',
          'mobilePhone': '970-500-0003',
          'type': 'UserAndPermissions'},
         {'userName': 'Backupadmin',
          'password': 'wpsthpvse1',
          'fullName': 'Backupadmin',
          'roles': ['Backup administrator'],
          'emailAddress': 'backup@hp.com',
          'officePhone': '970-555-0003',
          'mobilePhone': '970-500-0003',
          'type': 'UserAndPermissions'},
         {'userName': 'Noprivledge',
          'password': 'wpsthpvse1',
          'fullName': 'Noprivledge',
          'roles': ['Read only'],
          'emailAddress': 'rheid@hp.com',
          'officePhone': '970-555-0003',
          'mobilePhone': '970-500-0003',
          'type': 'UserAndPermissions'}
         ]

licenses = [{'key': '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZY2-LDVV4-92DQT-L6TTW'},
            {'key': 'AA9C AQAA H9PY CHVY V7B5 HWWB Y9JL KMPL 3JKH 5FVM DXAU 2CSM GHTG L762 MTK7 FYB9 KJVT D5KM EFVW DT5J 4BEM M2SC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZXJ-RDCJQ-55T3M-BP3H2'},
            {'key': 'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
            {'key': 'AAAE BQAA H9P9 CHW2 V7B5 HWWB Y9JL KMPL SRWE 8HJU DXAU 2CSM GHTG L762 LAB2 VRJA KJVT D5KM EFVW DT5J TF9K 54C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3G7SK-QDGSY-LRT8D-PWPVP-QWRKW'},
            {'key': '9AQA BQAA H9PA GHWZ V7B5 HWWB Y9JL KMPL SR2G 7AZU DXAU 2CSM GHTG L762 69VZ USJA KJVT D5KM EFVW DT5J VFQM 85S8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3G8YL-HHGX3-6M6KH-DZ99V-BDXMM'},
            {'key': 'YAAE DQAA H9P9 GHV3 U7B5 HWW5 Y9JL KMPL CRKE 6AJU DXAU 2CSM GHTG L762 H9Z2 WUZY KJVT D5KM EFVW DT5J FFAK N5C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
            ]

# LIG, SASLIG, AND LE
LIG_NAME = 'LIG1'
SASLIG_NAME = 'SASLIG1'
EG_NAME = 'EG1'
LE_NAME = 'LE1'

# Enclosures
ENC1 = 'CN75120D7B'
ENC2 = 'CN75120D77'
ENC3 = 'CN750163KD'

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
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC2SHBAY5 = '%s, bay 5' % ENC2
ENC3SHBAY1 = '%s, bay 1' % ENC3
ENC3SHBAY5 = '%s, bay 5' % ENC3

STORAGE_POOL = 'VSA_Cluster_116'
DHCP_BOOT_TARGET_IP = "192.168.21.59"
CHAP_SECRET = "wpsthpvse123"
MCHAP_SECRET = "hpvse123wpst"

# VOLUME_TEMPLATE = 'Volume root template for StoreVirtual 1.2'

EXISTING_SHARED_VOLUME1 = "ovs3803-dhcp-shared-volume1"
NEW_PRIVATE_VOLUME1 = 'ovs3803-dhcp-private-volume1-tbird'
NEW_PRIVATE_VOLUME2 = 'ovs3803-dhcp-private-volume2-tbird'
NEW_PRIVATE_VOLUME3 = 'ovs3803-dhcp-private-volume3-tbird'
NEW_PRIVATE_VOLUME4 = 'ovs3803-dhcp-private-volume4-tbird'


INITIATOR_GATEWAY = "192.168.0.1"
INITIATOR_SUBNET_MASK = "255.255.192.0"
STORAGE_POOL_NETWORK = 'ETH:network-untagged'
NETWORK_SET = "NS1"

# PROFILE1 SETTINGS
PROFILE1_TEMPLATE_NAME = 'tbird15-bay7-DHCP-legacy-bios-hw-iSCSI-simplified-boot'
PROFILE1_EXISTING_VOLUME = 'tbird15-bay7-rhel-dhcp-managed-volume'
PROFILE1_SHT_NAME = 'SY 480 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA'
PROFILE1_INITIATOR_NAME = 'iqn.2015-02.com.hpe:oneview-tbird15-bay7-dhcp-managed-volume'

# PROFILE2 SETTINGS
PROFILE2_TEMPLATE_NAME = 'tbird16-bay5-DHCP-uefi-hw-iSCSI-simplified-boot'
PROFILE2_EXISTING_VOLUME = 'tbird16-bay5-rhel-dhcp-managed-volume'
PROFILE2_SHT_NAME = 'SY 660 Gen9:1:Synergy 3830C 16G FC HBA:3:HP Synergy 3820C 10/20Gb CNA'
PROFILE2_INITIATOR_NAME = 'iqn.2015-02.com.hpe:oneview-tbird16-bay5-dhcp-managed-volume'
PROFILE2_BOOT_TARGET_NAME = "iqn.2003-10.com.lefthandnetworks:vsa-mg-116:854:tbird9-bay6-dhcp"
PROFILE2_CHAP_NAME = 'tbird16-bay5'
PROFILE2_MCHAP_NAME = 'tbird16-bay5'

# PROFILE3 SETTINGS
PROFILE3_TEMPLATE_NAME = 'tbird16-bay1-DHCP-uefi-optimized-hw-iSCSI-simplified-boot'
PROFILE3_EXISTING_VOLUME = 'tbird16-bay1-rhel-dhcp-managed-volume'
PROFILE3_SHT_NAME = 'SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:HP Synergy 3820C 10/20Gb CNA'
PROFILE3_INITIATOR_IP1 = '192.168.22.189'
PROFILE3_INITIATOR_IP2 = '192.168.22.190'
PROFILE3_INITIATOR_NAME = 'iqn.2015-02.com.hpe:oneview-tbird16-bay1-managed-volume'


existing_volumes = [
    {
        "storageSystemUri": STORAGE_POOL,
        "name": PROFILE1_EXISTING_VOLUME,
        "deviceVolumeName": PROFILE1_EXISTING_VOLUME,
        "isShareable": False,
    },
    {
        "storageSystemUri": STORAGE_POOL,
        "name": PROFILE2_EXISTING_VOLUME,
        "deviceVolumeName": PROFILE2_EXISTING_VOLUME,
        "isShareable": False,
    },
    {
        "storageSystemUri": STORAGE_POOL,
        "name": PROFILE3_EXISTING_VOLUME,
        "deviceVolumeName": PROFILE3_EXISTING_VOLUME,
        "isShareable": False,
    },
    {
        "storageSystemUri": STORAGE_POOL,
        "name": EXISTING_SHARED_VOLUME1,
        "deviceVolumeName": EXISTING_SHARED_VOLUME1,
        "isShareable": True,
    },
]

# UEFI
spt_hw_iscsi_managed_volume_uefi = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
            "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "bootVolumePriority": "Primary",
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME1,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 21474836480,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }]
    }
}

# UEFI optimized
spt_hw_iscsi_managed_volume_uefi_optimized = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE3_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
            "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }, ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "bootVolumePriority": "Primary",
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME2,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 21474836480,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }]
    }
}

# Legacy BIOS
spt_hw_iscsi_managed_volume_legacy_bios = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
            "manageBios": False
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "CD",
            "USB",
            "PXE",
            "HardDisk"
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        },
            {
            "functionType": "iSCSI",
            "id": 2,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 2",
                    "networkUri": STORAGE_POOL_NETWORK,
        }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            },
                {
                "isEnabled": True,
                "connectionId": 2,
                "targetSelector": "Auto",
            }
            ],
            "bootVolumePriority": "Primary",
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME3,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 21474836480,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }]
    }
}


# edit UEFI template to Change to a different boot volume
edit_spt_hw_iscsi_managed_volume_uefi = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
            "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "associatedTemplateAttachmentId": 'SPTVAID:1',
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "bootVolumePriority": "Primary",
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME4,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 21474836480,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }], "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }]
    }
}

# edit UEFI optimized to add a secondary boot volume
edit_spt_hw_iscsi_managed_volume_uefi_optimized = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE3_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
            "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        },
            {
            "functionType": "iSCSI",
            "id": 2,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 2",
                    "networkUri": STORAGE_POOL_NETWORK,
        }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "associatedTemplateAttachmentId": 'SPTVAID:1',
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            },
                {
                "isEnabled": True,
                "connectionId": 2,
                "targetSelector": "Auto",
            },
            ],
            "bootVolumePriority": "Primary",
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME2,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 21474836480,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }], "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }]
    }
}

# edit Legacy BIOS to disable simplified boot
edit_spt_hw_iscsi_managed_volume_legacy_bios = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
            "manageBios": False
    },
    "boot": {
        "order": [],
        "manageBoot": False
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    }
}


# UEFI edit 2 back to original
edit2_spt_hw_iscsi_managed_volume_uefi = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_TEMPLATE_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
            "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "associatedTemplateAttachmentId": 'SPTVAID:1',
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "bootVolumePriority": "Primary",
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME1,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 21474836480,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }], "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }]
    }
}

# UEFI optimized back to original
edit2_spt_hw_iscsi_managed_volume_uefi_optimized = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE3_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_TEMPLATE_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
            "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }, ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "associatedTemplateAttachmentId": 'SPTVAID:1',
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "bootVolumePriority": "Primary",
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME2,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 21474836480,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }], "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }]
    }
}

# Legacy BIOS back to original
edit2_spt_hw_iscsi_managed_volume_legacy_bios = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_TEMPLATE_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
            "manageBios": False
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "CD",
            "USB",
            "PXE",
            "HardDisk"
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        },
            {
            "functionType": "iSCSI",
            "id": 2,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 2",
                    "networkUri": STORAGE_POOL_NETWORK,
        }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            },
                {
                "isEnabled": True,
                "connectionId": 2,
                "targetSelector": "Auto",
            }
            ],
            "bootVolumePriority": "Primary",
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME3,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 21474836480,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }], "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }]
    }
}


# Create template with HW iSCSI boot from StoreVirtual managed volume
# using defined volume and UEFI
sp_from_spt_hw_uefi_defined_volume = {
    "type": "ServerProfileV10",
    'serverHardwareUri': 'SH:' + ENC2SHBAY5,
    "serverProfileTemplateUri": 'SPT:' + PROFILE2_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "associatedTemplateAttachmentId": 'SPTVAID:1',
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "bootVolumePriority": "Primary",
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME1,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 21474836480,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }], "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }]
    }
}

# verify DTO fro Create template with HW iSCSI boot from StoreVirtual
# managed volume using defined volume and UEFI
verify_sp_from_spt_hw_uefi_defined_volume = {
    "type": "ServerProfileV10",
    'serverHardwareUri': 'SH:' + ENC2SHBAY5,
    "serverProfileTemplateUri": 'SPT:' + PROFILE2_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "associatedTemplateAttachmentId": 'SPTVAID:1',
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "bootVolumePriority": "Primary",
            "volume": None,
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": "V:" + NEW_PRIVATE_VOLUME1,
        }], "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }]
    }
}

# Create template with HW iSCSI boot from StoreVirtual managed volume
# using defined volume and UEFI optimized
sp_from_spt_hw_iscsi_uefi_optimized_defined_volume = {
    "type": "ServerProfileV10",
    'serverHardwareUri': 'SH:' + ENC2SHBAY1,
    "serverProfileTemplateUri": 'SPT:' + PROFILE3_TEMPLATE_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE3_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
            "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }, ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "associatedTemplateAttachmentId": 'SPTVAID:1',
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "bootVolumePriority": "Primary",
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME2,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 21474836480,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }], "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }]
    }
}

# Verify DTO for Create template with HW iSCSI boot from StoreVirtual
# managed volume using defined volume and UEFI optimized
verify_sp_from_spt_hw_iscsi_uefi_optimized_defined_volume = {
    "type": "ServerProfileV10",
    'serverHardwareUri': 'SH:' + ENC2SHBAY1,
    "serverProfileTemplateUri": 'SPT:' + PROFILE3_TEMPLATE_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE3_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
            "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }, ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "associatedTemplateAttachmentId": 'SPTVAID:1',
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "volume": None,
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": "V:" + NEW_PRIVATE_VOLUME2,
        }], "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }]
    }
}

# Create template with HW iSCSI boot from StoreVirtual managed volume
# using defined volume and Legacy BIOS
sp_from_spt_hw_legacy_bios_defined_volume = {
    "type": "ServerProfileV10",
    'serverHardwareUri': 'SH:' + ENC1SHBAY7,
    "serverProfileTemplateUri": 'SPT:' + PROFILE1_TEMPLATE_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
            "manageBios": False
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "CD",
            "USB",
            "PXE",
            "HardDisk"
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "connectionSettings": {
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        },
            {
            "functionType": "iSCSI",
            "id": 2,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 2",
                    "networkUri": STORAGE_POOL_NETWORK,
        }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "associatedTemplateAttachmentId": 'SPTVAID:1',
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, {
                "isEnabled": True,
                "connectionId": 2,
                "targetSelector": "Auto",
            }],
            "bootVolumePriority": "Primary",
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME3,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 21474836480,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }], "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }]
    }
}

# Verify DTO for Create template with HW iSCSI boot from StoreVirtual
# managed volume using defined volume and Legacy BIOS
verify_sp_from_spt_hw_legacy_bios_defined_volume = {
    "type": "ServerProfileV10",
    'serverHardwareUri': 'SH:' + ENC1SHBAY7,
    "serverProfileTemplateUri": 'SPT:' + PROFILE1_TEMPLATE_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
            "manageBios": False
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "CD",
            "USB",
            "PXE",
            "HardDisk"
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "connectionSettings": {
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        },
            {
            "functionType": "iSCSI",
            "id": 2,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 2",
                "networkUri": STORAGE_POOL_NETWORK,
        }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "associatedTemplateAttachmentId": 'SPTVAID:1',
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            },
                {
                "isEnabled": True,
                    "connectionId": 2,
                    "targetSelector": "Auto",
            }
            ],
            "volume": None,
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": "V:" + NEW_PRIVATE_VOLUME3,
        }], "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }]
    }
}


# Create template with HW iSCSI boot from StoreVirtual managed volume
# using existing volume and UEFI
sp_from_spt_hw_uefi_existing_volume = {
    "type": "ServerProfileV10",
    'serverHardwareUri': 'SH:' + ENC2SHBAY5,
    "serverProfileTemplateUri": 'SPT:' + PROFILE2_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "associatedTemplateAttachmentId": 'SPTVAID:1',
            "id": 2,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "bootVolumePriority": "Primary",
            "volume": None,
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": "V:" + PROFILE2_EXISTING_VOLUME,
        }], "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }]}
}

# Create template with HW iSCSI boot from StoreVirtual managed volume
# using existing volume and UEFI optimized
sp_from_spt_hw_iscsi_uefi_optimized_existing_volume = {
    "type": "ServerProfileV10",
    'serverHardwareUri': 'SH:' + ENC2SHBAY1,
    "serverProfileTemplateUri": 'SPT:' + PROFILE3_TEMPLATE_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE3_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
            "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }, ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "associatedTemplateAttachmentId": 'SPTVAID:1',
            "id": 2,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "bootVolumePriority": "Primary",
            "volume": None,
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": "V:" + PROFILE3_EXISTING_VOLUME,
        }], "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }]
    }
}

# Create template with HW iSCSI boot from StoreVirtual managed volume
# using existing volume and Legacy BIOS
sp_from_spt_hw_legacy_bios_existing_volume = {
    "type": "ServerProfileV10",
    'serverHardwareUri': 'SH:' + ENC1SHBAY7,
    "serverProfileTemplateUri": 'SPT:' + PROFILE1_TEMPLATE_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
            "manageBios": False
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "CD",
            "USB",
            "PXE",
            "HardDisk"
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "connectionSettings": {
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        },
            {
            "functionType": "iSCSI",
            "id": 2,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 2",
                "networkUri": STORAGE_POOL_NETWORK,
        }
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "associatedTemplateAttachmentId": 'SPTVAID:1',
            "id": 2,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            },
                {
                "isEnabled": True,
                    "connectionId": 2,
                    "targetSelector": "Auto",
            }
            ],
            "bootVolumePriority": "Primary",
            "volume": None,
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": "V:" + PROFILE1_EXISTING_VOLUME,
        }], "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }]
    }
}


sp_from_spt_hw_iscsi_uefi_compliant = {
    "name": PROFILE2_TEMPLATE_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": []}
}

sp_from_spt_hw_iscsi_uefi_optimized_compliant = {
    "name": PROFILE3_TEMPLATE_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": []}
}

sp_from_spt_hw_iscsi_legacy_bios_compliant = {
    "name": PROFILE1_TEMPLATE_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": []}
}

sp_from_spt_hw_iscsi_uefi_non_compliant = {
    "name": PROFILE2_TEMPLATE_NAME,
    "compliance-preview": {
        "automaticUpdates": [
            "REGEX:Configure SAN storage to managed by profile\.",
            "REGEX:Change host OS type to RHE Linux \(5.x, 6.x, 7.x\)\.",
            "REGEX:Create an attachment to a new volume \"" + NEW_PRIVATE_VOLUME1 + "\"\.",
            "REGEX:Add a storage path using connection \"1\" to attachment for volume \"" + NEW_PRIVATE_VOLUME1 + "\"\.",
        ],
        "manualUpdates": [
            "REGEX:Change boot source of connection \d on port Mezzanine \(Mezz\) \d:\d-b to Managed volume\.",
            "REGEX:Change boot setting of volume attachment for volume \"" + NEW_PRIVATE_VOLUME1 + "\" to primary."
        ],
        "type": "ServerProfileCompliancePreviewV1"
    }
}

sp_from_spt_hw_iscsi_legacy_bios_non_compliant = {
    "name": PROFILE1_TEMPLATE_NAME,
    "compliance-preview": {
        "automaticUpdates": [
            "REGEX:Change storage path using connection \"\d\" in volume attachment id \"\d\" for volume {\"name\":\".*\", \"uri\":\".*\"} to enabled\.",
            "REGEX:Change storage path using connection \"\d\" in volume attachment id \"\d\" for volume {\"name\":\".*\", \"uri\":\".*\"} to enabled\.",
            "REGEX:Change boot setting for volume {\"name\":\".*\", \"uri\":\".*\"} attachment id \"\d\" to match the associated template setting\.",
        ],
        "manualUpdates": [],
        "type": "ServerProfileCompliancePreviewV1"

    }
}

sp_from_spt_hw_iscsi_legacy_bios_non_compliant2 = {
    "name": PROFILE1_TEMPLATE_NAME,
    "compliance-preview": {
        "automaticUpdates": [
            "REGEX:Create an attachment to a new volume \"" +
            NEW_PRIVATE_VOLUME4 + "\"\.",
            "REGEX:Change storage path using connection \"\d\" in volume attachment id \"\d\" for volume {\"name\":\".*\", \"uri\":\".*\"} to disabled\.",
            "REGEX:Change storage path using connection \"\d\" in volume attachment id \"\d\" for volume {\"name\":\".*\", \"uri\":\".*\"} to disabled\.",
        ],
        "manualUpdates": [
            "REGEX:The boot setting for attachment id \"\d\" for volume {\"name\":\".*\", \"uri\":\".*\"} does not match the associated template setting\.  Change either the profile or the template setting accordingly\."
        ],
        "type": "ServerProfileCompliancePreviewV1"

    }
}

sp_from_spt_hw_iscsi_uefi_optimized_non_compliant = {
    "name": PROFILE3_TEMPLATE_NAME,
    "compliance-preview": {
        "automaticUpdates": [],
        "manualUpdates": [
            "REGEX:Change server hardware type to {\"name\":\".*\", \"uri\":\".*\"}."

        ],
        "type": "ServerProfileCompliancePreviewV1"

    }
}


# Edit legacy bios SP to boot from a non-associated ATAI
compliance_legacy_bios_non_associated_atai = {
    "type": "ServerProfileV10",
    'serverHardwareUri': 'SH:' + ENC1SHBAY7,
    "serverProfileTemplateUri": 'SPT:' + PROFILE1_TEMPLATE_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
            "manageBios": False
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "CD",
            "USB",
            "PXE",
            "HardDisk"
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "connectionSettings": {
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        },
            {
            "functionType": "iSCSI",
            "id": 2,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 2",
                "networkUri": STORAGE_POOL_NETWORK,
        }
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "associatedTemplateAttachmentId": 'SPTVAID:1',
            "id": 2,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": False,
                "connectionId": 1,
                "targetSelector": "Auto",
            },
                {
                "isEnabled": False,
                    "connectionId": 2,
                    "targetSelector": "Auto",
            }
            ],
            "bootVolumePriority": "Primary",
            "volume": None,
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": "V:" + PROFILE1_EXISTING_VOLUME,
        }, {
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            },
                {
                "isEnabled": True,
                "connectionId": 2,
                "targetSelector": "Auto",
            }
            ],
            "volume": None,
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": "V:" + NEW_PRIVATE_VOLUME3,
        }], "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }]
    }
}

# Removing the bootable volume
comliance_uefi_no_bootable_volume = {
    "type": "ServerProfileV10",
    'serverHardwareUri': 'SH:' + ENC2SHBAY5,
    "serverProfileTemplateUri": 'SPT:' + PROFILE2_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
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
        "connections": [{
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "UserDefined",
                "iscsi": {
                    "initiatorNameSource": "ProfileInitiatorName",
                    "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                    "bootTargetLun": "0",
                    "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                    "firstBootTargetPort": "3260",
                    "chapLevel": "MutualChap",
                    "chapName": PROFILE2_CHAP_NAME,
                    "chapSecret": CHAP_SECRET,
                    "mutualChapName": PROFILE2_MCHAP_NAME,
                    "mutualChapSecret": MCHAP_SECRET
                }
            },
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }]
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


# Edit legacy bios SPT to boot from a non-associated ATAI
compliance_legacy_bios_non_associated_atai_template = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": 'SHT:' + PROFILE1_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_TEMPLATE_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
            "manageBios": False
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "CD",
            "USB",
            "PXE",
            "HardDisk"
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        },
            {
            "functionType": "iSCSI",
            "id": 2,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 2",
                    "networkUri": STORAGE_POOL_NETWORK,
        }
        ],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "associatedTemplateAttachmentId": 'SPTVAID:1',
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": False,
                "connectionId": 1,
                "targetSelector": "Auto",
            },
                {
                "isEnabled": False,
                "connectionId": 2,
                "targetSelector": "Auto",
            }
            ],
            "bootVolumePriority": "Primary",
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME3,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 21474836480,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }, {
            "id": 2,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            },
                {
                "isEnabled": True,
                "connectionId": 2,
                "targetSelector": "Auto",
            }
            ],
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME4,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 21474836480,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }], "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }]
    }
}

# Removing the bootable volume
comliance_uefi_no_bootable_volume_template = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_TEMPLATE_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
            "manageBios": False
    },
    "boot": {
        "order": [],
        "manageBoot": False
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    }
}


# edit UEFI optimized template to different SHT
comliance_uefi_optimized_different_sht_template = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_TEMPLATE_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
            "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }, ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "associatedTemplateAttachmentId": 'SPTVAID:1',
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "bootVolumePriority": "Primary",
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME2,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 21474836480,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }], "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }]
    }
}

# Legacy BIOS back to original
edit_compliance_legacy_bios_return_to_compliant_template = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_TEMPLATE_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
            "manageBios": False
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "CD",
            "USB",
            "PXE",
            "HardDisk"
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        },
            {
            "functionType": "iSCSI",
            "id": 2,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 2",
                    "networkUri": STORAGE_POOL_NETWORK,
        }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "associatedTemplateAttachmentId": 'SPTVAID:1',
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            },
                {
                "isEnabled": True,
                "connectionId": 2,
                "targetSelector": "Auto",
            }
            ],
            "bootVolumePriority": "Primary",
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME3,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 21474836480,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }], "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }]
    }
}

# UEFI edit 2 back to original
edit_compliance_uefi_return_to_compliant_template = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_TEMPLATE_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
            "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "bootVolumePriority": "Primary",
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME1,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 21474836480,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }], "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }]
    }
}


# Multiple primary boot connections
negative_spt_1 = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "wpst10-negative-1",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        },
            {
            "functionType": "iSCSI",
            "id": 2,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 2",
            "networkUri": STORAGE_POOL_NETWORK,
        }],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME1,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }]
    }
}

# Only secondary boot connection
negative_spt_2 = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "wpst10-negative-2",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }, ],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME1,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }]
    }
}

# Multiple secondary boot connection
negative_spt_3 = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "wpst10-negative-3",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        },
            {
            "functionType": "iSCSI",
            "id": 2,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Secondary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 2",
            "networkUri": STORAGE_POOL_NETWORK,
        }, ],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME1,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }]
    }
}

# iSCSI boot without managed storage
negative_spt_5 = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "negative-spt-5",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }],
    },
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
}

# iSCSI boot with non-bootable volume
negative_spt_6 = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "negative_spt_6",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME1,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }]
    }
}

# Multiple boot volumes selected
negative_spt_7 = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "negative_spt_7",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "bootVolumePriority": "Primary",
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME1,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }, {
            "id": 2,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "bootVolumePriority": "Primary",
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": "volume 2",
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }]
    }
}

# Existing shared volume
negative_spt_8 = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "negative_spt_8",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True,
                "targetSelector": "Auto",
            }],
            "bootVolumePriority": "Primary",
            "volume": None,
            "volumeUri": "v:" + EXISTING_SHARED_VOLUME1,
        }]
    }
}

# Existing private volume
negative_spt_9 = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "negative_spt_9",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True,
                "targetSelector": "Auto",
            }],
            "volume": None,
            "volumeUri": "v:" + PROFILE1_EXISTING_VOLUME,
        }]
    }
}

# New shared volume
negative_spt_10 = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "negative_spt_10",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": "negative-volume",
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": True,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }]
    }
}

# Disabled storage path
negative_spt_11 = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "negative_spt_11",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": False,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "bootVolumePriority": "Primary",
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": "negative_spt_11",
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }]
    }
}

# Using network set
negative_spt_12 = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "negative_spt_12",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": "NS:" + NETWORK_SET,
        }],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": "negative_spt_12",
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }]
    }
}

# managed boot while specifying iscsi section
negative_spt_13 = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "negative_spt_13",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "bootVolumeSource": "ManagedVolume",
                "priority": "Primary",
                "iscsi": {
                    "chapLevel": "None",
                    "initiatorName": "iqn.2015-02.com.hpe:oneview-vcgs03t010",
                    "initiatorNameSource": "UserDefined"
                }
            },
            "name": "Connection 131",
            "networkUri": STORAGE_POOL_NETWORK,
        }],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "bootVolumePriority": "Primary",
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": "negative_spt_13",
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }]
    }
}

# edit to disable Boot Volume for managed volume
negative_spt_14 = {
    "type": "ServerProfileTemplateV6",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
            "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "associatedTemplateAttachmentId": 'SPTVAID:1',
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "bootVolumePriority": "NotBootable",
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME1,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 21474836480,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }], "sanSystemCredentials": [{
            "storageSystemUri": "SSYS:VSA_Cluster_116",
            "chapLevel": "MutualChap"
        }]
    }
}


# Create profile from template with simplified iSCSI boot without initiator IP
negative_sp_from_spt_1 = {
    "type": "ServerProfileV10",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "serverProfileTemplateUri": "SPT:" + PROFILE2_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "negative_sp_from_spt_1",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }]},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME1,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }]
    }
}

# Create profile from template with different SHT
negative_sp_from_spt_2 = {
    "type": "ServerProfileV10",
    'serverHardwareTypeUri': 'SHT:BL660c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    "serverProfileTemplateUri": "SPT:" + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "negative_sp_from_spt_2",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
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
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }]
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME1,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }]
    }
}


# sp_power = [
#   {
#         'serverHardwareUri': 'SH:'+ETHERNET_BLADE,
#   },
#   {
#         'serverHardwareUri': 'SH:'+ISCSI_BLADE,
#   },
#   {
#         'serverHardwareUri': 'SH:'+NEG_ISCSI_BLADE,
#   },
#   {
#         'serverHardwareUri': 'SH:'+NEG_ETHERNET_BLADE,
#   },
# ]

create_templates = [
    spt_hw_iscsi_managed_volume_legacy_bios.copy(),
    spt_hw_iscsi_managed_volume_uefi.copy(),
    spt_hw_iscsi_managed_volume_uefi_optimized.copy(),
]

edit_templates1 = [
    edit_spt_hw_iscsi_managed_volume_uefi.copy(),
    edit_spt_hw_iscsi_managed_volume_uefi_optimized.copy(),
    edit_spt_hw_iscsi_managed_volume_legacy_bios.copy(),
]

edit_templates2 = [
    edit2_spt_hw_iscsi_managed_volume_legacy_bios.copy(),
    edit2_spt_hw_iscsi_managed_volume_uefi.copy(),
    edit2_spt_hw_iscsi_managed_volume_uefi_optimized.copy(),
]

negative_spt_tasks = [
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_1.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_primary_boot'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_2.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_secondary_boot_connection'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_3.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_secondary_boot'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_5.copy(),
        'taskState': 'Error',
        'errorMessage': 'SPT_Bootable_connection_nonbootable_volume'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_6.copy(),
        'taskState': 'Error',
        'errorMessage': 'SPT_Bootable_connection_nonbootable_volume'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_7.copy(),
        'taskState': 'Error',
        'errorMessage': 'DuplicateBootVolumePriority'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_8.copy(),
        'taskState': 'Error',
        'errorMessage': 'Only_private_boot_volume'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_9.copy(),
        'taskState': 'Error',
        'errorMessage': 'SPT_attach_exist_private_volume'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_10.copy(),
        'taskState': 'Error',
        'errorMessage': 'ShareablePendingVolumeAttachmentNotSupported'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_11.copy(),
        'taskState': 'Error',
        'errorMessage': 'Managed_Volume_No_Bootable_Connections'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_12.copy(),
        'taskState': 'Error',
        'errorMessage': 'Profile_network_set_iscsi'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_13.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_iSCSI_target_data_managed_volume'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_spt_14.copy(),
        'taskState': 'Error',
        'errorMessage': 'SPT_Bootable_connection_nonbootable_volume'},
]

negative_sp_tasks = [
    # {
    #     'keyword': 'Add Server Profile',
    #     'argument': negative_sp_from_spt_1.copy(),
    #     'taskState': 'Error',
    #     'errorMessage': 'iSCSI_initiator_IP_required'},
    # {
    #     'keyword': 'Add Server Profile',
    #     'argument': negative_sp_from_spt_2.copy(),
    #     'taskState': 'Error',
    #     'errorMessage': 'iSCSI_initiator_IP_required'},
]

create_sp_from_spt = [
    sp_from_spt_hw_uefi_defined_volume.copy(),
    sp_from_spt_hw_iscsi_uefi_optimized_defined_volume.copy(),
    sp_from_spt_hw_legacy_bios_defined_volume.copy(),
]

verify_create_sp_from_spt = [
    verify_sp_from_spt_hw_uefi_defined_volume.copy(),
    verify_sp_from_spt_hw_iscsi_uefi_optimized_defined_volume.copy(),
    verify_sp_from_spt_hw_legacy_bios_defined_volume.copy(),
]

edit_sp_from_spt = [
    sp_from_spt_hw_uefi_existing_volume.copy(),
    sp_from_spt_hw_iscsi_uefi_optimized_existing_volume.copy(),
    sp_from_spt_hw_legacy_bios_existing_volume.copy(),
]

edit_compliance1_sp_from_spt = [
    # 4.20 6/15 RS, this edit now fails at the task.  Never gets to compliance check.  Create Negative tests?
    # RS compliance_legacy_bios_non_associated_atai.copy(),
    comliance_uefi_no_bootable_volume.copy(),
]

edit_compliance2_template = [
    # 4.20 6/15 RS, this edit now fails at the task.  Never gets to compliance check.  Create Negative tests?
    # RS compliance_legacy_bios_non_associated_atai_template.copy(),
    comliance_uefi_no_bootable_volume_template.copy(),
    comliance_uefi_optimized_different_sht_template.copy(),
]

edit_compliance3_template = [
    edit_compliance_legacy_bios_return_to_compliant_template.copy(),
    edit_compliance_uefi_return_to_compliant_template.copy(),
    edit2_spt_hw_iscsi_managed_volume_uefi_optimized.copy(),
]

sp_compliance = [
    sp_from_spt_hw_iscsi_uefi_compliant.copy(),
    sp_from_spt_hw_iscsi_uefi_optimized_compliant.copy(),
    sp_from_spt_hw_iscsi_legacy_bios_compliant.copy(),
]

verify_non_compliance_sp_from_spt = [
    sp_from_spt_hw_iscsi_uefi_non_compliant.copy(),
    # 4.20 6/15 RS, this edit now fails at the task.  Never gets to compliance check.  Create Negative tests?
    # RS sp_from_spt_hw_iscsi_legacy_bios_non_compliant.copy(),
]

verify_non_compliance_sp_from_spt2 = [
    # sp_from_spt_hw_iscsi_uefi_non_compliant.copy(),
    # 4.20 6/15 RS, this edit now fails at the task.  Never gets to compliance check.  Create Negative tests?
    # RS sp_from_spt_hw_iscsi_legacy_bios_non_compliant2.copy(),
    sp_from_spt_hw_iscsi_uefi_optimized_non_compliant.copy(),
]

delete_profile_templates = [
    PROFILE1_TEMPLATE_NAME,
    PROFILE2_TEMPLATE_NAME,
    PROFILE3_TEMPLATE_NAME,
]

new_permanent_volumes = [
    {"properties": {"name": NEW_PRIVATE_VOLUME1}},
    {"properties": {"name": NEW_PRIVATE_VOLUME2}},
    {"properties": {"name": NEW_PRIVATE_VOLUME3}},
    {"properties": {"name": NEW_PRIVATE_VOLUME4}},
]

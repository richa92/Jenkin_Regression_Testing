admin_credentials = {
    'userName': 'Administrator',
    'password': 'wpsthpvse1'
}

ilo_credentials = {
    'username': 'Administrator',
    'password': 'hpvse123'
}

hpmctp_credentials = {
    'ip': '16.114.216.129',
    'username': 'root',
    'password': 'hpvse1'
}

cliq_credentials = {
    'mgmt_ip': '16.71.149.173',
    'username': 'admin',
    'password': 'admin'
}

# EG
EG_NAME = 'EG1'

# Enclosures
ENC1 = 'CN754406XL'
ENC2 = 'CN754404R6'
ENC3 = 'CN754406WB'

# Server Hardware
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC2SHBAY2 = '%s, bay 2' % ENC2
ENC2SHBAY3 = '%s, bay 3' % ENC2
ENC2SHBAY5 = '%s, bay 5' % ENC2
ENC2SHBAY7 = '%s, bay 7' % ENC2
ENC2SHBAY8 = '%s, bay 8' % ENC2
ENC3SHBAY1 = '%s, bay 1' % ENC3
ENC3SHBAY5 = '%s, bay 5' % ENC3

# iSCSI
STORAGE_POOL = 'VSA_Cluster_173-2'
INITIATOR_GATEWAY = "192.168.0.1"
INITIATOR_SUBNET_MASK = "255.255.192.0"
FIRST_BOOT_TARGET_IP = "192.168.21.71"
CHAP_SECRET = "wpsthpvse123"
MCHAP_SECRET = "hpvse123wpst"
STORAGE_POOL_NETWORK = "ETH:network-untagged"

EXISTING_SHARED_VOLUME1 = "ovs3803-shared-volume1"
EXISTING_PRIVATE_VOLUME5 = "tbird17-bay1-rhel-managed-volume"
EXISTING_PRIVATE_VOLUME6 = "tbird17-bay7-managed-volume"

# PROFILE1: profile on ENC1 bay7, Blackbird
PROFILE1_NAME = "tbird14-bay7-SW-iSCSI-managed-volume"
PROFILE1_SH = 'SH:' + ENC1SHBAY7
PROFILE1_INITIATOR_IP_1 = "192.168.22.158"
PROFILE1_INITIATOR_IP_2 = "192.168.22.159"
PROFILE1_EXISTING_VOLUME = 'tbird14-bay7-rhel-managed-volume'

# PROFILE2: profile on ENC2 bay5, Redbird
PROFILE2_NAME = "tbird17-bay5-HW-iSCSI-managed-volume"
PROFILE2_SH = 'SH:' + ENC2SHBAY5
PROFILE2_INITIATOR_IP_1 = "192.168.22.167"
PROFILE2_INITIATOR_IP_2 = "192.168.22.168"
PROFILE2_EXISTING_VOLUME = 'tbird17-bay5-rhel-managed-volume'

# PROFILE3: profile on ENC1 bay6, Condor
PROFILE3_NAME = "tbird17-bay7-SW-iSCSI-managed-volume-Gen10"
PROFILE3_SHT = 'SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA'
PROFILE3_SH = 'SH:' + ENC2SHBAY7
PROFILE3_INITIATOR_IP_1 = "192.168.21.161"
PROFILE3_INITIATOR_IP_2 = "192.168.21.162"
PROFILE3_EXISTING_VOLUME = 'tbird17-bay7-managed-volume'

# PROFILE4: profile on ENC2 bay7, Harrier
PROFILE4_NAME = "tbird17-bay8-HW-iSCSI-managed-volume-Gen10"
PROFILE4_SHT = 'SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA'
PROFILE4_SH = 'SH:' + ENC2SHBAY8
PROFILE4_INITIATOR_IP_1 = "192.168.21.166"
PROFILE4_INITIATOR_IP_2 = "192.168.21.169"
PROFILE4_EXISTING_VOLUME = 'tbird17-bay8-managed-volume'


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
    # {
    #     "storageSystemUri": STORAGE_POOL,
    #     "name": PROFILE3_EXISTING_VOLUME,
    #     "deviceVolumeName": PROFILE3_EXISTING_VOLUME,
    #     "isShareable": False,
    # },
    # {
    #     "storageSystemUri": STORAGE_POOL,
    #     "name": PROFILE4_EXISTING_VOLUME,
    #     "deviceVolumeName": PROFILE4_EXISTING_VOLUME,
    #     "isShareable": False,
    # },
    {
        "storageSystemUri": STORAGE_POOL,
        "name": EXISTING_PRIVATE_VOLUME5,
        "deviceVolumeName": EXISTING_PRIVATE_VOLUME5,
        "isShareable": False,
    },
    {
        "storageSystemUri": STORAGE_POOL,
        "name": EXISTING_PRIVATE_VOLUME6,
        "deviceVolumeName": EXISTING_PRIVATE_VOLUME6,
        "isShareable": False,
    },
    {
        "storageSystemUri": STORAGE_POOL,
        "name": EXISTING_SHARED_VOLUME1,
        "deviceVolumeName": EXISTING_SHARED_VOLUME1,
        "isShareable": True,
    },
]


# Negative Server Profile Validation Tasks

# Multiple_primary_boot
negative_sp_1 = {
    "type": "ServerProfileV10",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serverHardwareTypeUri": "SHT:" + PROFILE3_SHT,
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
    "connectionSettings": {
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
        ]
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            }],
            "volume": None,
            "volumeUri": "V:" + PROFILE1_EXISTING_VOLUME,
        }]
    }
}

# Invalid_secondary_boot_connection
negative_sp_2 = {
    "type": "ServerProfileV10",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serverHardwareTypeUri": "SHT:" + PROFILE3_SHT,
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
    "connectionSettings": {
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
        ]
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            }],
            "volume": None,
            "volumeUri": "V:" + PROFILE1_EXISTING_VOLUME,
        }]
    }
}

# Multiple_secondary_boot
negative_sp_3 = {
    "type": "ServerProfileV10",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serverHardwareTypeUri": "SHT:" + PROFILE3_SHT,
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
    "connectionSettings": {
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
        ]
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            }],
            "volume": None,
            "volumeUri": "V:" + PROFILE1_EXISTING_VOLUME,
        }]
    }
}

# Invalid_iSCSI_and_BIOS_boot_mode
negative_sp_4 = {
    "type": "ServerProfileV10",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serverHardwareTypeUri": "SHT:" + PROFILE3_SHT,
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
    "connectionSettings": {
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
        ]
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            }],
            "volume": None,
            "volumeUri": "V:" + PROFILE1_EXISTING_VOLUME,
        }]
    }
}

# SP_Bootable_connection_nonbootable_volume
negative_sp_5 = {
    "type": "ServerProfileV10",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serverHardwareTypeUri": "SHT:" + PROFILE3_SHT,
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
    "connectionSettings": {
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
        ]
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "isBootVolume": False,
            "lunType": "Auto",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            }],
            "volume": None,
            "volumeUri": "V:" + PROFILE1_EXISTING_VOLUME,
        }]
    }
}

# More_than_one_boot_volume
negative_sp_6 = {
    "type": "ServerProfileV10",
    "serverHardwareTypeUri": "SHT:" + PROFILE3_SHT,
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
    "connectionSettings": {
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
        ]
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [{
                    "connectionId": 1,
                    "isEnabled": True
                }],
                "volume": None,
                "volumeUri": "V:" + PROFILE1_EXISTING_VOLUME,
            },
            {
                "id": 2,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [{
                    "connectionId": 1,
                    "isEnabled": True
                }],
                "volume": None,
                "volumeUri": "V:" + PROFILE2_EXISTING_VOLUME,
            }
        ]
    }
}

# Only_private_boot_volume
negative_sp_7 = {
    "type": "ServerProfileV10",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serverHardwareTypeUri": "SHT:" + PROFILE3_SHT,
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
    "connectionSettings": {
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
        ]
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            }],
            "volume": None,
            "volumeUri": "V:" + EXISTING_SHARED_VOLUME1,
        }]
    }
}

# Storage_path_disabled_not_exist
negative_sp_8 = {
    "type": "ServerProfileV10",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serverHardwareTypeUri": "SHT:" + PROFILE3_SHT,
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
    "connectionSettings": {
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
        ]
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [{
                      "connectionId": 1,
                      "isEnabled": False
            }],
            "volume": None,
            "volumeUri": "V:" + PROFILE1_EXISTING_VOLUME,
        }]
    }
}


# CREATE PROFILES

# SW iSCSI with managed volume and only primary connection - Gen9
create_profile1_sw_iscsi = {
    "type": "ServerProfileV10",
    'serverHardwareUri': PROFILE1_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
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
    "connectionSettings": {
        "connections": [
            {
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
                "functionType": "Ethernet",
                "id": 1,
                "boot": {
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                    "priority": "Primary"
                },
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                },
            }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True,
            }],
            "volume": None,
            "volumeUri": "V:" + PROFILE1_EXISTING_VOLUME,
        }]
    }
}

# HW iSCSI with managed volume and only primary connection - Gen9
create_profile2_hw_iscsi = {
    "type": "ServerProfileV10",
    'serverHardwareUri': PROFILE2_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
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
    "connectionSettings": {
        "connections": [
            {
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
                "functionType": "iSCSI",
                "id": 1,
                "boot": {
                    "bootVolumeSource": "ManagedVolume",
                    "priority": "Primary"
                },
                "ipv4": {
                    "ipAddress": PROFILE2_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                },
            }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True
            }],
            "volume": None,
            "volumeUri": "V:" + PROFILE2_EXISTING_VOLUME,
        }]
    }
}

# SW iSCSI with managed volume and only primary connection - Gen10
create_profile3_sw_iscsi = {
    "type": "ServerProfileV10",
    'serverHardwareUri': PROFILE3_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_NAME,
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
    "connectionSettings": {
        "connections": [
            {
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
                "functionType": "Ethernet",
                "id": 1,
                "boot": {
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                    "priority": "Primary"
                },
                "ipv4": {
                    "ipAddress": PROFILE3_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                },
            }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [{
                "connectionId": 1,
                "isEnabled": True,
            }],
            "volume": None,
            "volumeUri": "V:" + PROFILE3_EXISTING_VOLUME,
        }]
    }
}

# HW iSCSI with managed volume and only primary connection - Gen10
create_profile4_hw_iscsi = {
    "type": "ServerProfileV10",
    'serverHardwareUri': PROFILE4_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE4_NAME,
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
    "connectionSettings": {
        "connections": [
            {
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
                "functionType": "iSCSI",
                "id": 1,
                "boot": {
                    "bootVolumeSource": "ManagedVolume",
                    "priority": "Primary"
                },
                "ipv4": {
                    "ipAddress": PROFILE4_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                },
            }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [
                {
                    "connectionId": 1,
                    "isEnabled": True
                }
            ],
            "volume": None,
            "volumeUri": "V:" + PROFILE4_EXISTING_VOLUME,
        }]
    }
}


# hpMCTP Data after Profile Create

hpMCTP_profile2 = {
    "hpmctpIp": hpmctp_credentials['ip'],
    "hpmctpUsername": hpmctp_credentials['username'],
    "hpmctpPassword": hpmctp_credentials['password'],
    "serverName": PROFILE2_SH,
    "iloUsername": ilo_credentials['username'],
    "iloPassword": ilo_credentials['password'],
    "mezzSlot": 'Mezzanine Slot 3',
}

hpMCTP_profile4 = {
    "hpmctpIp": hpmctp_credentials['ip'],
    "hpmctpUsername": hpmctp_credentials['username'],
    "hpmctpPassword": hpmctp_credentials['password'],
    "serverName": PROFILE4_SH,
    "iloUsername": ilo_credentials['username'],
    "iloPassword": ilo_credentials['password'],
    "mezzSlot": 'Mezzanine Slot 3',
}


# Edit the profiles the first time

# Edit SW iSCSI profile and add a secondary connection to managed volume - Gen9
profile1_sw_iscsi_edit1 = {
    "type": "ServerProfileV10",
    "name": PROFILE1_NAME,
    "iscsiInitiatorNameType": "AutoGenerated",
    'serverHardwareUri': PROFILE1_SH,
    "category": "server-profiles",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "Connection 1",
                "functionType": "Ethernet",
                "networkUri": STORAGE_POOL_NETWORK,
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                }
            },
            {
                "id": 2,
                "name": "Connection 2",
                "functionType": "Ethernet",
                "networkUri": STORAGE_POOL_NETWORK,
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                    "ipAddress": PROFILE1_INITIATOR_IP_2
                },
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                }
            }
        ]
    },
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
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "volumeAttachments": [{
            "id": 1,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [
                {
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
            "volumeUri": "V:" + PROFILE1_EXISTING_VOLUME,
        }]
    }
}

# Edit HW iSCSI profile and add a secondary connection to managed volume - Gen9
profile2_hw_iscsi_edit1 = {
    "type": "ServerProfileV10",
    "name": PROFILE2_NAME,
    "iscsiInitiatorNameType": "AutoGenerated",
    'serverHardwareUri': 'SH:' + PROFILE2_SH,
    "category": "server-profiles",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "Connection 1",
                "functionType": "iSCSI",
                "networkUri": STORAGE_POOL_NETWORK,
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                    "ipAddress": PROFILE2_INITIATOR_IP_1
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                }
            },
            {
                "id": 2,
                "name": "connection 2",
                "functionType": "iSCSI",
                "networkUri": STORAGE_POOL_NETWORK,
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                    "ipAddress": PROFILE2_INITIATOR_IP_2
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                }
            }
        ]
    },
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
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "volumeAttachments": [{
            "id": 1,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [
                {
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
            "volumeUri": "V:" + PROFILE2_EXISTING_VOLUME,
        }]
    }
}


# Edit SW iSCSI profile and add a secondary connection to managed volume - Gen10
profile3_sw_iscsi_edit1 = {
    "type": "ServerProfileV10",
    "name": PROFILE3_NAME,
    "iscsiInitiatorNameType": "AutoGenerated",
    'serverHardwareUri': PROFILE3_SH,
    "category": "server-profiles",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "Connection 1",
                "functionType": "Ethernet",
                "networkUri": STORAGE_POOL_NETWORK,
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                    "ipAddress": PROFILE3_INITIATOR_IP_1,
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                }
            },
            {
                "id": 2,
                "name": "Connection 2",
                "functionType": "Ethernet",
                "networkUri": STORAGE_POOL_NETWORK,
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                    "ipAddress": PROFILE3_INITIATOR_IP_2
                },
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                }
            }
        ]
    },
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
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "volumeAttachments": [{
            "id": 1,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [
                {
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
            "volumeUri": "V:" + PROFILE3_EXISTING_VOLUME,
        }]
    }
}

# Edit HW iSCSI profile and add a secondary connection to managed volume - Gen10
profile4_hw_iscsi_edit1 = {
    "type": "ServerProfileV10",
    "name": PROFILE4_NAME,
    "iscsiInitiatorNameType": "AutoGenerated",
    'serverHardwareUri': 'SH:' + PROFILE4_SH,
    "category": "server-profiles",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "Connection 1",
                "functionType": "iSCSI",
                "networkUri": STORAGE_POOL_NETWORK,
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                    "ipAddress": PROFILE4_INITIATOR_IP_1
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                }
            },
            {
                "id": 2,
                "name": "connection 2",
                "functionType": "iSCSI",
                "networkUri": STORAGE_POOL_NETWORK,
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                    "ipAddress": PROFILE4_INITIATOR_IP_2
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                }
            }
        ]
    },
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
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "volumeAttachments": [{
            "id": 1,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [
                {
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
            "volumeUri": "V:" + PROFILE4_EXISTING_VOLUME,
        }]
    }
}


# Edit Profiles a second time

# Edit SW iSCSI profile and change to a different managed volume - Gen9
profile1_sw_iscsi_edit2 = {
    "type": "ServerProfileV10",
    "name": PROFILE1_NAME,
    "iscsiInitiatorNameType": "AutoGenerated",
    'serverHardwareUri': PROFILE1_SH,
    "category": "server-profiles",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "Connection 1",
                "functionType": "Ethernet",
                "networkUri": STORAGE_POOL_NETWORK,
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                }
            },
            {
                "id": 2,
                "name": "connection 2",
                "functionType": "Ethernet",
                "networkUri": STORAGE_POOL_NETWORK,
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                    "ipAddress": PROFILE1_INITIATOR_IP_2,
                },
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                }
            }
        ]
    },
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
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "volumeAttachments": [{
            "id": 2,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [
                {
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
            "volumeUri": "V:" + EXISTING_PRIVATE_VOLUME5,
        }]
    }
}

# Edit HW iSCSI profile and change to a different managed volume - Gen9
profile2_hw_iscsi_edit2 = {
    "type": "ServerProfileV10",
    "name": PROFILE2_NAME,
    "iscsiInitiatorNameType": "AutoGenerated",
    'serverHardwareUri': PROFILE2_SH,
    "category": "server-profiles",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "Connection 1",
                "functionType": "iSCSI",
                "networkUri": STORAGE_POOL_NETWORK,
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                    "ipAddress": PROFILE2_INITIATOR_IP_1,
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                }
            },
            {
                "id": 2,
                "name": "connection 2",
                "functionType": "iSCSI",
                "networkUri": STORAGE_POOL_NETWORK,
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                    "ipAddress": PROFILE2_INITIATOR_IP_2,
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                }
            }
        ]
    },
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
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "volumeAttachments": [{
            "id": 2,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [
                {
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
            "volume": None,
            "volumeUri": "V:" + EXISTING_PRIVATE_VOLUME6,
        }]
    }
}

# Edit SW iSCSI profile and change to a different managed volume - Gen10
profile3_sw_iscsi_edit2 = {
    "type": "ServerProfileV10",
    "name": PROFILE3_NAME,
    "iscsiInitiatorNameType": "AutoGenerated",
    'serverHardwareUri': PROFILE3_SH,
    "category": "server-profiles",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "Connection 1",
                "functionType": "Ethernet",
                "networkUri": STORAGE_POOL_NETWORK,
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                    "ipAddress": PROFILE3_INITIATOR_IP_1,
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                }
            },
            {
                "id": 2,
                "name": "connection 2",
                "functionType": "Ethernet",
                "networkUri": STORAGE_POOL_NETWORK,
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                    "ipAddress": PROFILE3_INITIATOR_IP_2,
                },
                "boot": {
                    "priority": "Secondary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                }
            }
        ]
    },
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
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "volumeAttachments": [{
            "id": 2,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [
                {
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
            "volumeUri": "V:" + EXISTING_PRIVATE_VOLUME6,
        }]
    }
}

# Edit HW iSCSI profile and change to a different managed volume - Gen10
profile4_hw_iscsi_edit2 = {
    "type": "ServerProfileV10",
    "name": PROFILE4_NAME,
    "iscsiInitiatorNameType": "AutoGenerated",
    'serverHardwareUri': PROFILE4_SH,
    "category": "server-profiles",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "Connection 1",
                "functionType": "iSCSI",
                "networkUri": STORAGE_POOL_NETWORK,
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                    "ipAddress": PROFILE4_INITIATOR_IP_1,
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                }
            },
            {
                "id": 2,
                "name": "connection 2",
                "functionType": "iSCSI",
                "networkUri": STORAGE_POOL_NETWORK,
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY,
                    "ipAddress": PROFILE4_INITIATOR_IP_2,
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                }
            }
        ]
    },
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
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "volumeAttachments": [{
            "id": 2,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [
                {
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
            "volume": None,
            "volumeUri": "V:" + PROFILE3_EXISTING_VOLUME,
        }]
    }
}


negative_sp_tasks = [
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_1.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_primary_boot'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_2.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_secondary_boot_connection'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_3.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_secondary_boot'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_4.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_iSCSI_and_BIOS_boot_mode'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_5.copy(),
        'taskState': 'Error',
        'errorMessage': 'SP_Bootable_connection_nonbootable_volume'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_6.copy(),
        'taskState': 'Error',
        'errorMessage': 'More_than_one_boot_volume'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_7.copy(),
        'taskState': 'Error',
        'errorMessage': 'Only_private_boot_volume'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_8.copy(),
        'taskState': 'Error',
        'errorMessage': 'Storage_path_disabled_not_exist'
    },
]

create_profiles = [
    create_profile1_sw_iscsi.copy(),
    create_profile2_hw_iscsi.copy(),
    # create_profile3_sw_iscsi.copy(),
    # create_profile4_hw_iscsi.copy(),
]

ris_nodes_iscsi_settings_create = [
    {
        "server": PROFILE1_SH,
        "username": ilo_credentials['username'],
        "password":ilo_credentials['password'],
        "path":"/rest/v1/Systems/1/bios/iSCSI/settings"
    },
    #     {
    #         "server": PROFILE3_SH,
    #         "username": ilo_credentials['username'],
    #         "password":ilo_credentials['password'],
    #         "path":"/redfish/v1/Systems/1/bios/iSCSI/settings"
    #     },
]

get_hpMCTP = [
    hpMCTP_profile2.copy(),
    # hpMCTP_profile4.copy(),
]

sp_edit_add_secondary_connection = [
    profile1_sw_iscsi_edit1.copy(),
    profile2_hw_iscsi_edit1.copy(),
    # profile3_sw_iscsi_edit1.copy(),
    # profile4_hw_iscsi_edit1.copy(),
]

sp_iscsi_edit_boot_volume = [
    profile1_sw_iscsi_edit2.copy(),
    # profile3_sw_iscsi_edit2.copy(),
    profile2_hw_iscsi_edit2.copy(),
    # profile4_hw_iscsi_edit2.copy(),
]

sp_edit2 = [
    profile1_sw_iscsi_edit2.copy(),
    # profile3_sw_iscsi_edit2.copy(),
    profile2_hw_iscsi_edit2.copy(),
    # profile4_hw_iscsi_edit2.copy(),
]

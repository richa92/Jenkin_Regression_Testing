admin_credentials = {
    'userName': 'Administrator',
    'password': 'wpsthpvse1'
}

ilo_credentials = {
    'username': 'Administrator',
    'password': 'hpvse123'
}

# PCI Vendor and device IDs for known Synergy FC mezz cards
HP_PCI_VENDOR_ID = 0x103c
HP_PCI_DEVICE_ID_3530C = 0x8001  # Electron 16Gb FC
HP_PCI_DEVICE_ID_3830C = 0x8002  # Quartz 16Gb FC
VALID_FC_PCI_DEVICE_IDS = [HP_PCI_DEVICE_ID_3530C, HP_PCI_DEVICE_ID_3830C]

# The server's mezz slot with the FCoE mezz card used as first boot device
FC_DEVICE_MEZZ_SLOT = 1

EG_NAME = 'EG1'

# Enclosures
ENC2 = 'CN754404R6'

# Gen9 server hardware
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC2SHBAY8 = '%s, bay 8' % ENC2

server_hardware_urisGen10 = [
    {
        'serverHardwareUri': 'SH:' + ENC2SHBAY8,
    },
]

server_hardware_urisGen9 = [
    {
        'serverHardwareUri': 'SH:' + ENC2SHBAY1,
    },
]

# PROFILE1 SETTINGS
PROFILE1_NAME_PREFIX = 'OVF387_Gen10_FC_Boot'
PROFILE1_UEFI_NAME = PROFILE1_NAME_PREFIX + " (UEFI)"
PROFILE1_BIOS_NAME = PROFILE1_NAME_PREFIX + " (BIOS)"
PROFILE1_SH = "SH:" + ENC2SHBAY8

PROFILE2_NAME_PREFIX = 'OVF388_Gen9_FC_Boot'
PROFILE2_UEFI_NAME = PROFILE2_NAME_PREFIX + " (UEFI)"
PROFILE2_BIOS_NAME = PROFILE2_NAME_PREFIX + " (BIOS)"
PROFILE2_SH = "SH:" + ENC2SHBAY1

STORESERV_NAME = 'wpst3par-7200-7-srv'
STORESERV_POOL = 'FVT_Tbird_reg1_r1'
STORESERV_VOLUME_NAME = 'OVF388_Gen9_vol1'

FC_NETWORK_A = 'FA1'
FC_NETWORK_B = 'FA2'
FC_NETWORK_A_VSAN = 'wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55'
FC_NETWORK_B_VSAN = 'wpstsan14.vse.rdlabs.hpecorp.net-FID101-10:00:00:27:f8:fe:0c:56'

ris_nodeGen10 = {
    "server": ENC2SHBAY8,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/redfish/v1/Systems/1/bios/boot/settings",
}

ris_nodeGen9 = {
    "server": ENC2SHBAY1,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/redfish/v1/Systems/1/bios/boot/settings",
}

# Start of Data

OVF388_simplified_UEFI_FC_2x_boot_from_managed_SAN_storage_volume = {
    "type": "ServerProfileV10",
    "name": PROFILE2_UEFI_NAME,
    "description": "OVF388 Server Profile",
    "iscsiInitiatorNameType": "AutoGenerated",
    "templateCompliance": "Unknown",
    "serverHardwareUri": PROFILE2_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "enclosureUri": 'ENC:' + ENC2,
    "affinity": "Bay",
    "associatedServer": None,
    "hideUnusedFlexNics": True,
    "macType": "Physical",
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "category": "server-profiles",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "FCConnA",
                "functionType": "FibreChannel",
                "networkUri": "FC:" + FC_NETWORK_A,
                "portId": "Auto",
                "requestedVFs": None,
                "allocatedVFs": None,
                "macType": "Physical",
                "wwpnType": "Virtual",
                "requestedMbps": 3000,
                "maximumMbps": 3000,
                "ipv4": None,
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                    "targets": []
                },
                "state": "Deployed",
                "status": "OK",
                "managed": True,
                "networkName": None,
                "lagName": None
            },
            {
                "id": 2,
                "name": "FCConnB",
                "functionType": "FibreChannel",
                "networkUri": "FC:" + FC_NETWORK_B,
                "portId": "Auto",
                "macType": "Physical",
                "wwpnType": "Virtual",
                "requestedMbps": 3000,
                "maximumMbps": 3000,
                "ipv4": None,
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                    "targets": []
                },
                "state": "Deployed",
                "status": "OK",
                "managed": True,
                "networkName": None,
                "lagName": None
            }
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto",
        "secureBoot": "Unmanaged"
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"
        ]
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "lunType": "Auto",
                "volumeUri": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                "bootVolumePriority": "Primary",
                "volume": {
                    "properties": {
                        "name": STORESERV_VOLUME_NAME,
                        "storagePool": "SPOOL:" + STORESERV_POOL,
                        "provisioningType": "Thin",
                        "size": 2147483648,
                        "isShareable": False,
                    },
                    "isPermanent": False,
                    "templateUri": "ROOT:" + STORESERV_POOL,
                },
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "isEnabled": True
                    },
                    {
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "isEnabled": True
                    }
                ],
                "isBootVolume": True,
            }
        ],
    },
    "osDeploymentSettings": None,
}

OVF388_simplified_BIOS_FC_2x_boot_from_managed_SAN_storage_volume = {
    "type": "ServerProfileV10",
    "name": PROFILE2_BIOS_NAME,
    "description": "OVF393 Server Profile",
    "iscsiInitiatorNameType": "AutoGenerated",
    "templateCompliance": "Unknown",
    "serverHardwareUri": PROFILE2_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "enclosureUri": 'ENC:' + ENC2,
    "affinity": "Bay",
    "associatedServer": None,
    "hideUnusedFlexNics": True,
    "macType": "Physical",
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "category": "server-profiles",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "FCConnA",
                "functionType": "FibreChannel",
                "networkUri": "FC:" + FC_NETWORK_A,
                "portId": "Auto",
                "requestedVFs": None,
                "allocatedVFs": None,
                "macType": "Physical",
                "wwpnType": "Virtual",
                "requestedMbps": 3000,
                "maximumMbps": 3000,
                "ipv4": None,
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                    "targets": []
                },
                "state": "Deployed",
                "status": "OK",
                "managed": True,
                "networkName": None,
                "lagName": None
            },
            {
                "id": 2,
                "name": "FCConnB",
                "functionType": "FibreChannel",
                "networkUri": "FC:" + FC_NETWORK_B,
                "portId": "Auto",
                "macType": "Physical",
                "wwpnType": "Virtual",
                "requestedMbps": 3000,
                "maximumMbps": 3000,
                "ipv4": None,
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                    "targets": []
                },
                "state": "Deployed",
                "status": "OK",
                "managed": True,
                "networkName": None,
                "lagName": None
            }
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk", "CD", "USB", "PXE"
        ]
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "lunType": "Auto",
                "volumeUri": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                "bootVolumePriority": "Primary",
                "volume": {
                    "properties": {
                        "name": STORESERV_VOLUME_NAME,
                        "storagePool": "SPOOL:" + STORESERV_POOL,
                        "provisioningType": "Thin",
                        "size": 2147483648,
                        "isShareable": False,
                    },
                    "isPermanent": False,
                    "templateUri": "ROOT:" + STORESERV_POOL,
                },
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "isEnabled": True
                    },
                    {
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "isEnabled": True
                    }
                ],
                "isBootVolume": True,
            }
        ],
    },
    "osDeploymentSettings": None,
}

OVF388_create_UEFI_profiles = [
    OVF388_simplified_UEFI_FC_2x_boot_from_managed_SAN_storage_volume.copy()
]

OVF388_create_BIOS_profiles = [
    OVF388_simplified_BIOS_FC_2x_boot_from_managed_SAN_storage_volume.copy()
]

OVF388_simplified_UEFI_FC_1x_boot_from_managed_SAN_storage_volume = {
    "type": "ServerProfileV10",
    "name": PROFILE2_UEFI_NAME,
    "description": "OVF393 Server Profile",
    "iscsiInitiatorNameType": "AutoGenerated",
    "templateCompliance": "Unknown",
    "serverHardwareUri": PROFILE2_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "enclosureUri": 'ENC:' + ENC2,
    "affinity": "Bay",
    "associatedServer": None,
    "hideUnusedFlexNics": True,
    "macType": "Physical",
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "category": "server-profiles",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "FCConnA",
                "functionType": "FibreChannel",
                "networkUri": "FC:" + FC_NETWORK_A,
                "portId": "Auto",
                "requestedVFs": None,
                "allocatedVFs": None,
                "macType": "Physical",
                "wwpnType": "Virtual",
                "requestedMbps": 3000,
                "maximumMbps": 3000,
                "ipv4": None,
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                    "targets": []
                },
                "state": "Deployed",
                "status": "OK",
                "managed": True,
                "networkName": None,
                "lagName": None
            }
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto",
        "secureBoot": "Unmanaged"
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"
        ]
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "lunType": "Auto",
                "volumeUri": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                "bootVolumePriority": "Primary",
                "volume": {
                    "properties": {
                        "name": STORESERV_VOLUME_NAME,
                        "storagePool": "SPOOL:" + STORESERV_POOL,
                        "provisioningType": "Thin",
                        "size": 2147483648,
                        "isShareable": False,
                    },
                    "isPermanent": False,
                    "templateUri": "ROOT:" + STORESERV_POOL,
                },
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "isEnabled": True
                    }
                ],
                "isBootVolume": True,
            }
        ],
    },
    "osDeploymentSettings": None,
}

OVF388_create_1x_UEFI_profiles = [
    OVF388_simplified_UEFI_FC_1x_boot_from_managed_SAN_storage_volume.copy()
]


# OVF387
OVF387_simplified_UEFI_FC_2x_boot_from_managed_SAN_storage_volume = {
    "type": "ServerProfileV10",
    "name": PROFILE1_UEFI_NAME,
    "description": "OVF387 Server Profile",
    "iscsiInitiatorNameType": "AutoGenerated",
    "templateCompliance": "Unknown",
    "serverHardwareUri": PROFILE1_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "enclosureUri": 'ENC:' + ENC2,
    "affinity": "Bay",
    "associatedServer": None,
    "hideUnusedFlexNics": True,
    "macType": "Physical",
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "category": "server-profiles",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "FCConnA",
                "functionType": "FibreChannel",
                "networkUri": "FC:" + FC_NETWORK_A,
                "portId": "Auto",
                "requestedVFs": None,
                "allocatedVFs": None,
                "macType": "Physical",
                "wwpnType": "Virtual",
                "requestedMbps": 3000,
                "maximumMbps": 3000,
                "ipv4": None,
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                    "targets": []
                },
                "state": "Deployed",
                "status": "OK",
                "managed": True,
                "networkName": None,
                "lagName": None
            },
            {
                "id": 2,
                "name": "FCConnB",
                "functionType": "FibreChannel",
                "networkUri": "FC:" + FC_NETWORK_B,
                "portId": "Auto",
                "macType": "Physical",
                "wwpnType": "Virtual",
                "requestedMbps": 3000,
                "maximumMbps": 3000,
                "ipv4": None,
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                    "targets": []
                },
                "state": "Deployed",
                "status": "OK",
                "managed": True,
                "networkName": None,
                "lagName": None
            }
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto",
        "secureBoot": "Unmanaged"
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"
        ]
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "lunType": "Auto",
                "volumeUri": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                "bootVolumePriority": "Primary",
                "volume": {
                    "properties": {
                        "name": STORESERV_VOLUME_NAME,
                        "storagePool": "SPOOL:" + STORESERV_POOL,
                        "provisioningType": "Thin",
                        "size": 2147483648,
                        "isShareable": False,
                    },
                    "isPermanent": False,
                    "templateUri": "ROOT:" + STORESERV_POOL,
                },
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "isEnabled": True
                    },
                    {
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "isEnabled": True
                    }
                ],
                "isBootVolume": True,
            }
        ],
    },
    "osDeploymentSettings": None,
}

OVF387_simplified_BIOS_FC_2x_boot_from_managed_SAN_storage_volume = {
    "type": "ServerProfileV10",
    "name": PROFILE1_BIOS_NAME,
    "description": "OVF387 Server Profile",
    "iscsiInitiatorNameType": "AutoGenerated",
    "templateCompliance": "Unknown",
    "serverHardwareUri": PROFILE1_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "enclosureUri": 'ENC:' + ENC2,
    "affinity": "Bay",
    "associatedServer": None,
    "hideUnusedFlexNics": True,
    "macType": "Physical",
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "category": "server-profiles",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "FCConnA",
                "functionType": "FibreChannel",
                "networkUri": "FC:" + FC_NETWORK_A,
                "portId": "Auto",
                "requestedVFs": None,
                "allocatedVFs": None,
                "macType": "Physical",
                "wwpnType": "Virtual",
                "requestedMbps": 3000,
                "maximumMbps": 3000,
                "ipv4": None,
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                    "targets": []
                },
                "state": "Deployed",
                "status": "OK",
                "managed": True,
                "networkName": None,
                "lagName": None
            },
            {
                "id": 2,
                "name": "FCConnB",
                "functionType": "FibreChannel",
                "networkUri": "FC:" + FC_NETWORK_B,
                "portId": "Auto",
                "macType": "Physical",
                "wwpnType": "Virtual",
                "requestedMbps": 3000,
                "maximumMbps": 3000,
                "ipv4": None,
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                    "targets": []
                },
                "state": "Deployed",
                "status": "OK",
                "managed": True,
                "networkName": None,
                "lagName": None
            }
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk", "CD", "USB", "PXE"
        ]
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "lunType": "Auto",
                "volumeUri": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                "bootVolumePriority": "Primary",
                "volume": {
                    "properties": {
                        "name": STORESERV_VOLUME_NAME,
                        "storagePool": "SPOOL:" + STORESERV_POOL,
                        "provisioningType": "Thin",
                        "size": 2147483648,
                        "isShareable": False,
                    },
                    "isPermanent": False,
                    "templateUri": "ROOT:" + STORESERV_POOL,
                },
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "isEnabled": True
                    },
                    {
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "isEnabled": True
                    }
                ],
                "isBootVolume": True,
            }
        ],
    },
    "osDeploymentSettings": None,
}

OVF387_create_UEFI_profiles = [
    OVF387_simplified_UEFI_FC_2x_boot_from_managed_SAN_storage_volume.copy()
]

OVF387_create_BIOS_profiles = [
    OVF387_simplified_BIOS_FC_2x_boot_from_managed_SAN_storage_volume.copy()
]

admin_credentials = {
    'userName': 'Administrator',
    'password': 'hpvse123'
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

EG_NAME = 'EG'

# Enclosures
ENC1 = 'MXQ72605PX'

# Gen9 server hardware
ENC1SHBAY2 = '%s, bay 2' % ENC1

server_hardware_uris = [
    {
        'serverHardwareUri': 'SH:' + ENC1SHBAY2,
    },
]

# PROFILE1 SETTINGS
PROFILE1_NAME_PREFIX = 'OVF388_Gen9_FC_Boot'
PROFILE1_UEFI_NAME = PROFILE1_NAME_PREFIX + " (UEFI)"
PROFILE1_BIOS_NAME = PROFILE1_NAME_PREFIX + " (BIOS)"
PROFILE1_SH = "SH:" + ENC1SHBAY2

STORESERV_NAME = 'tb3par1'
STORESERV_POOL = 'FC_r1'
STORESERV_VOLUME_NAME = 'OVF388_Gen9_vol1'

FC_NETWORK_A = 'FC-A'
FC_NETWORK_A_VSAN = 'VSAN20'
FC_NETWORK_B = 'FC-B'
FC_NETWORK_B_VSAN = 'VSAN30'

ris_node = {"server": ENC1SHBAY2,
            "username": "Administrator",
            "password": "hpvse123",
            "path": "/redfish/v1/Systems/1/bios/boot/settings",
            }

# Start of Data

simplified_UEFI_FC_2x_boot_from_managed_SAN_storage_volume = {
    "type": "ServerProfileV9",
    "name": PROFILE1_UEFI_NAME,
    "description": "OVF393 Server Profile",
    "iscsiInitiatorNameType": "AutoGenerated",
    "templateCompliance": "Unknown",
    "serverHardwareUri": PROFILE1_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "enclosureUri": 'ENC:' + ENC1,
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
                "requestedMbps": "Auto",
                "allocatedMbps": 16000,
                "maximumMbps": 16000,
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
                "requestedMbps": "Auto",
                "allocatedMbps": 16000,
                "maximumMbps": 16000,
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

simplified_BIOS_FC_2x_boot_from_managed_SAN_storage_volume = {
    "type": "ServerProfileV9",
    "name": PROFILE1_BIOS_NAME,
    "description": "OVF393 Server Profile",
    "iscsiInitiatorNameType": "AutoGenerated",
    "templateCompliance": "Unknown",
    "serverHardwareUri": PROFILE1_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "enclosureUri": 'ENC:' + ENC1,
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
                "requestedMbps": "Auto",
                "allocatedMbps": 16000,
                "maximumMbps": 16000,
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
                "requestedMbps": "Auto",
                "allocatedMbps": 16000,
                "maximumMbps": 16000,
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

ts1_create_UEFI_profiles = [
    simplified_UEFI_FC_2x_boot_from_managed_SAN_storage_volume.copy()
]

ts1_create_BIOS_profiles = [
    simplified_BIOS_FC_2x_boot_from_managed_SAN_storage_volume.copy()
]

simplified_UEFI_FC_1x_boot_from_managed_SAN_storage_volume = {
    "type": "ServerProfileV9",
    "name": PROFILE1_UEFI_NAME,
    "description": "OVF393 Server Profile",
    "iscsiInitiatorNameType": "AutoGenerated",
    "templateCompliance": "Unknown",
    "serverHardwareUri": PROFILE1_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "enclosureUri": 'ENC:' + ENC1,
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
                "requestedMbps": "Auto",
                "allocatedMbps": 16000,
                "maximumMbps": 16000,
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

ts1_create_1x_UEFI_profiles = [
    simplified_UEFI_FC_1x_boot_from_managed_SAN_storage_volume.copy()
]
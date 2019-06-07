# DTO Versioning
PORT_DTO_TYPE = "portV5"
SERVER_PROFILE_DTO_TYPE = "ServerProfileV10"

# Credentials
appliance_credentials = {
    'userName': 'Administrator',
    'password': 'hpvse123'
}

ilo_credentials = {
    'username': 'Administrator',
    'password': 'hpvse123'
}

EG_NAME = 'FattireEG'

# Enclosures
ENC1 = 'MXQ72605PX'

# Server bays
SERVER_GEN9_BAY = 2
SERVER_GEN10_BAY = 1

# Server name
SERVER_GEN9 = '%s, bay %d' % (ENC1, SERVER_GEN9_BAY)
SERVER_GEN10 = '%s, bay %d' % (ENC1, SERVER_GEN10_BAY)

# Server hardware URIs
SH_GEN9 = "SH:" + SERVER_GEN9
SH_GEN10 = "SH:" + SERVER_GEN10

server_hardware_uris_gen9 = [
    {
        'serverHardwareUri': SH_GEN9,
    }
]
server_hardware_uris_gen10 = [
    {
        'serverHardwareUri': SH_GEN10,
    }
]
server_hardware_uris = server_hardware_uris_gen9 + server_hardware_uris_gen10

# PROFILE1 SETTINGS
PROFILE1_NAME_PREFIX = 'OVF5290_FC_2BootVol'
PROFILE1_GEN9_NAME = PROFILE1_NAME_PREFIX + " (Gen9)"
PROFILE1_GEN10_NAME = PROFILE1_NAME_PREFIX + " (Gen10)"

PROFILE_TEMPLATE1_NAME_PREFIX = 'OVF5290_FC_2BootVol_SPT'
PROFILE_TEMPLATE1_GEN9_NAME = PROFILE_TEMPLATE1_NAME_PREFIX + " (Gen9)"
PROFILE_TEMPLATE1_GEN10_NAME = PROFILE_TEMPLATE1_NAME_PREFIX + " (Gen10)"

# There should really be 2 StorServs for these tests. Tests will work with 1 if that's all you have available
STORESERV1_NAME = 'tb3par1'
STORESERV2_NAME = 'tb3par1'
STORESERV1_POOL = 'FC_r1'
STORESERV2_POOL = 'FC_r1'
STORESERV_VOLUME_PREFIX = 'OVF5290_vol'
STORESERV_VOLUME1_NAME_GEN9 = STORESERV_VOLUME_PREFIX + '1 (Gen9)'
STORESERV_VOLUME2_NAME_GEN9 = STORESERV_VOLUME_PREFIX + '2 (Gen9)'
STORESERV_VOLUME1_NAME_GEN10 = STORESERV_VOLUME_PREFIX + '1 (Gen10)'
STORESERV_VOLUME2_NAME_GEN10 = STORESERV_VOLUME_PREFIX + '2 (Gen10)'

FC_NETWORK_A = 'FC_Net20'
FC_NETWORK_B = 'FC_Net30'

FC_UPLINK_ICM = {"A": "%s, interconnect 1" % ENC1, "B": "%s, interconnect 4" % ENC1}
FC_UPLINK_SET = {"A": "FC1UL", "B": "FC2UL"}

DOWNLINK_PORT_GEN9 = "d%d" % SERVER_GEN9_BAY
DOWNLINK_PORT_GEN10 = "d%d" % SERVER_GEN10_BAY

downlink_DTO = {
    "gen9": {
        "A": {
            "type": PORT_DTO_TYPE,
            "associatedUplinkSetUri": FC_UPLINK_SET["A"],
            "interconnectName": FC_UPLINK_ICM["A"],
            "enabled": False,
            "portName": DOWNLINK_PORT_GEN9
        },
        "B": {
            "type": PORT_DTO_TYPE,
            "associatedUplinkSetUri": FC_UPLINK_SET["B"],
            "interconnectName": FC_UPLINK_ICM["B"],
            "enabled": False,
            "portName": DOWNLINK_PORT_GEN9
        }
    },
    "gen10": {
        "A": {
            "type": PORT_DTO_TYPE,
            "associatedUplinkSetUri": FC_UPLINK_SET["A"],
            "interconnectName": FC_UPLINK_ICM["A"],
            "enabled": False,
            "portName": DOWNLINK_PORT_GEN10
        },
        "B": {
            "type": PORT_DTO_TYPE,
            "associatedUplinkSetUri": FC_UPLINK_SET["B"],
            "interconnectName": FC_UPLINK_ICM["B"],
            "enabled": False,
            "portName": DOWNLINK_PORT_GEN10
        }
    },
}

ts1_gen9_2_target_2_boot_volume_sp = {
    "type": SERVER_PROFILE_DTO_TYPE,
    "name": PROFILE1_GEN9_NAME,
    "description": "",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareUri": SH_GEN9,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "FCConnA",
                "functionType": "FibreChannel",
                "networkUri": "FC:" + FC_NETWORK_A,
                "portId": "Auto",
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "managed": True,
            },
            {
                "id": 2,
                "name": "FCConnB",
                "functionType": "FibreChannel",
                "networkUri": "FC:" + FC_NETWORK_B,
                "portId": "Auto",
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "managed": True,
            }
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
    "boot": {"manageBoot": True, "order": ["HardDisk"]},
    "bios": {"manageBios": False},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "lunType": "Auto",
                "volumeUri": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volume": {
                    "properties": {
                        "name": STORESERV_VOLUME1_NAME_GEN9,
                        "storagePool": "SPOOL:" + STORESERV1_POOL,
                        "provisioningType": "Thin",
                        "size": 2147483648,
                        "isShareable": False,
                    },
                    "isPermanent": False,
                    "templateUri": "ROOT:" + STORESERV1_POOL,
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
                "bootVolumePriority": "Primary",
            },
            {
                "id": 2,
                "lunType": "Auto",
                "volumeUri": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV2_NAME,
                "volume": {
                    "properties": {
                        "name": STORESERV_VOLUME2_NAME_GEN9,
                        "storagePool": "SPOOL:" + STORESERV2_POOL,
                        "provisioningType": "Thin",
                        "size": 2147483648,
                        "isShareable": False,
                    },
                    "isPermanent": False,
                    "templateUri": "ROOT:" + STORESERV2_POOL,
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
                "bootVolumePriority": "Secondary",
            }
        ],
        "sanSystemCredentials": [],
    },
}

ts1_gen10_2_target_2_boot_volume_sp = {
    "type": SERVER_PROFILE_DTO_TYPE,
    "name": PROFILE1_GEN10_NAME,
    "description": "",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareUri": SH_GEN10,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "FCConnA",
                "functionType": "FibreChannel",
                "networkUri": "FC:" + FC_NETWORK_A,
                "portId": "Auto",
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "managed": True,
            },
            {
                "id": 2,
                "name": "FCConnB",
                "functionType": "FibreChannel",
                "networkUri": "FC:" + FC_NETWORK_B,
                "portId": "Auto",
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "managed": True,
            }
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
    "boot": {"manageBoot": True, "order": ["HardDisk"]},
    "bios": {"manageBios": False},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "lunType": "Auto",
                "volumeUri": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volume": {
                    "properties": {
                        "name": STORESERV_VOLUME1_NAME_GEN10,
                        "storagePool": "SPOOL:" + STORESERV1_POOL,
                        "provisioningType": "Thin",
                        "size": 2147483648,
                        "isShareable": False,
                    },
                    "isPermanent": False,
                    "templateUri": "ROOT:" + STORESERV1_POOL,
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
                "bootVolumePriority": "Primary",
            },
            {
                "id": 2,
                "lunType": "Auto",
                "volumeUri": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV2_NAME,
                "volume": {
                    "properties": {
                        "name": STORESERV_VOLUME2_NAME_GEN10,
                        "storagePool": "SPOOL:" + STORESERV2_POOL,
                        "provisioningType": "Thin",
                        "size": 2147483648,
                        "isShareable": False,
                    },
                    "isPermanent": False,
                    "templateUri": "ROOT:" + STORESERV2_POOL,
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
                "bootVolumePriority": "Secondary",
            }
        ],
        "sanSystemCredentials": [],
    },
}

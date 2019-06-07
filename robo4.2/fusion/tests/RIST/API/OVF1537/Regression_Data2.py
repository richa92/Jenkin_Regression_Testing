admin_credentials = {'userName': 'Administrator',
                     'password': 'wpsthpvse1'
                     }

EG_NAME = 'EG1'

# Enclosures
ENC1 = 'CN75120D7B'
ENC2 = 'CN75120D77'
ENC3 = 'CN750163KD'

# Server Hardware
ENC1SHBAY7 = '%s, bay 7' % ENC1

# StoreVirtuals
STOREVIRTUAL_STORAGE_POOL_NETWORK = 'ETH:network-untagged'

STOREVIRTUAL_SLPT_STATIC_STORAGE_SYSTEM = 'VSA_Cluster_173-2'
STOREVIRTUAL_SLPT_STATIC_STORAGE_POOL = 'VSA_Cluster_173-2'

STOREVIRTUAL_SLPT_DHCP_STORAGE_SYSTEM = 'VSA_Cluster_116'
STOREVIRTUAL_SLPT_DHCP_STORAGE_POOL = 'VSA_Cluster_116'

STOREVIRTUAL_VOLUME1_NAME = 'volume1'
STOREVIRTUAL_VOLUME2_NAME = 'volume2'

# PROFILE1: profile on ENC1 bay7, Blackbird
PROFILE1_NAME = "tbird14-bay7-profile"

# Body for PATCH request to server profile to regenerate CHAP secrets
regenerate_chap_secrets = {
    "op": "replace",
    "path": "/sanstorage/regenerateChapSecrets"
}

# Create profile with a single StoreVirtual managed volume
profile1 = {
    "type": "ServerProfileV10", "name": PROFILE1_NAME, "description": "",
    "serverHardwareUri": 'SH:' + ENC1SHBAY7, "enclosureGroupUri": 'EG:' + EG_NAME, "enclosureUri": 'ENC:' + ENC1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True, "osDeploymentSettings": None,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "iSCSI1", "functionType": "iSCSI", "portId": "Mezz 3:1-b",
             "wwpnType": "Virtual",
             "requestedMbps": "2500",
             "networkUri": "ETH:network-untagged",
             "macType": "Virtual"},

            {"id": 2, "name": "iSCSI2",
             "functionType": "iSCSI",
             "portId": "Mezz 3:2-b",
             "wwpnType": "Virtual",
             "requestedMbps": "2500",
             "networkUri": "ETH:network-untagged",
             "macType": "Virtual"
             },

        ]
    },
    "bios": {
        "overriddenSettings": [],
        "manageBios": False
    },
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
    },
    "boot": {
        "manageBoot": False,
        "order": []
    },
    "hideUnusedFlexNics": True,
    "bootMode": {
        "manageMode": True,
        "pxeBootPolicy": "Auto",
        "mode": "UEFI"
    },
    "affinity": "Bay",
    "localStorage": {
        "controllers": [],
        "sasLogicalJBODs": []
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME1_NAME,
                        "storagePool": "StoragePoolV2:" + STOREVIRTUAL_SLPT_STATIC_STORAGE_POOL,
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STOREVIRTUAL_SLPT_STATIC_STORAGE_POOL,
                },
                "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL_SLPT_STATIC_STORAGE_SYSTEM,
                "volumeUri": None,
            },
        ],
    }
}


# edit profile to add a second managed volume on a second StoreVirtual
edit_profile1 = {
    "type": "ServerProfileV10", "name": PROFILE1_NAME, "description": "",
    "serverHardwareUri": 'SH:' + ENC1SHBAY7, "enclosureGroupUri": 'EG:' + EG_NAME, "enclosureUri": 'ENC:' + ENC1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True, "osDeploymentSettings": None,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "iSCSI1", "functionType": "iSCSI", "portId": "Mezz 3:1-b",
             "wwpnType": "Virtual",
             "requestedMbps": "2500",
             "networkUri": "ETH:network-untagged",
             "macType": "Virtual"},

            {"id": 2, "name": "iSCSI2",
             "functionType": "iSCSI",
             "portId": "Mezz 3:2-b",
             "wwpnType": "Virtual",
             "requestedMbps": "2500",
             "networkUri": "ETH:network-untagged",
             "macType": "Virtual"
             },

        ]
    },
    "bios": {
        "overriddenSettings": [],
        "manageBios": False
    },
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
    },
    "boot": {
        "manageBoot": False,
        "order": []
    },
    "hideUnusedFlexNics": True,
    "bootMode": {
        "manageMode": True,
        "pxeBootPolicy": "Auto",
        "mode": "UEFI"
    },
    "affinity": "Bay",
    "localStorage": {
        "controllers": [],
        "sasLogicalJBODs": []
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + STOREVIRTUAL_VOLUME1_NAME,
            },
            {
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME2_NAME,
                        "storagePool": "StoragePoolV2:" + STOREVIRTUAL_SLPT_DHCP_STORAGE_POOL,
                        "size": 2147483648,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STOREVIRTUAL_SLPT_DHCP_STORAGE_POOL,
                },
                "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL_SLPT_DHCP_STORAGE_SYSTEM,
                "volumeUri": None,
            },
        ]
    }
}

admin_credentials = {
    'userName': 'Administrator',
    'password': 'hpvse123'
}

ilo_credentials = {
    'username': 'Administrator',
    'password': 'hpvse123'
}

cliq_credentials_sv1 = {
    'mgmt_ip': '15.242.131.120',
    'port': 16022,
    'username': 'admin',
    'password': 'mccmgmt'
}

cliq_credentials_sv2 = {
    'mgmt_ip': '15.242.131.118',
    'port': 16022,
    'username': 'admin',
    'password': 'mccmgmt'
}


CHAP_LEVELS = ['None', 'Chap', 'MutualChap']

ETH_NETWORK = 'UntaggedNetwork'
# Networks for StoreVirtual #1 and #2
ISCSI_NETWORK_1 = 'UntaggediSCSINetwork'
ISCSI_NETWORK_2 = 'VLAN10iSCSINetwork'

EG_NAME = 'EG'

# Enclosures
ENC1 = 'MXQ73406DD'

# Gen9 server hardware
SERVER_GEN9_1 = '%s, bay 1' % ENC1
SERVER_GEN9_2 = '%s, bay 2' % ENC1

SHT_SERVER_GEN9_1 = "SH:" + SERVER_GEN9_1
SHT_SERVER_GEN9_2 = "SH:" + SERVER_GEN9_2

server_hardware_uris = [
    {
        'serverHardwareUri': 'SH:' + SERVER_GEN9_1,
    },
    {
        'serverHardwareUri': 'SH:' + SERVER_GEN9_2,
    },
]

STOREVIRTUAL_1_SYSTEM_NAME = 'dl802Cluster'
STOREVIRTUAL_1_POOL_NAME = 'dl802Cluster'
STOREVIRTUAL_2_SYSTEM_NAME = 'dl801Cluster'
STOREVIRTUAL_2_POOL_NAME = 'dl801Cluster'

SPT1_NAME = "OVF1396_SPT1"
SPT2_NAME = "OVF1396_SPT2"
SPT1_1SV_NAME = "OVF1396_SPT1_1SV"

SP1_NAME = "OVF1396_SP_1"
SP2_NAME = "OVF1396_SP_2"

VOLUME_SV1_1_NAME = "OVF1396Vol1.1"
VOLUME_SV1_2_NAME = "OVF1396Vol1.2"
VOLUME_SV2_1_NAME = "OVF1396Vol2.1"
VOLUME_SV2_2_NAME = "OVF1396Vol2.2"

SP1_FROM_SPT1 = {
    "serverProfileTemplateUri": "SPT:" + SPT1_NAME,
    "name": SP1_NAME,
    "serverHardwareUri": SERVER_GEN9_1,
    # "serverHardwareTypeUri": SHT_GEN9,
}

SP2_FROM_SPT1 = {
    "serverProfileTemplateUri": "SPT:" + SPT1_NAME,
    "name": SP2_NAME,
    "serverHardwareUri": SERVER_GEN9_2,
    # "serverHardwareTypeUri": SHT_GEN9,
}

SP1_FROM_SPT1_1SV = {
    "serverProfileTemplateUri": "SPT:" + SPT1_1SV_NAME,
    "name": SP1_NAME,
    "serverHardwareUri": SERVER_GEN9_1,
    # "serverHardwareTypeUri": SHT_GEN9,
}

ts1_spt_0_storevirtual = {
    "type": "ServerProfileTemplateV6",
    "name": SPT1_NAME,
    "serverHardwareTypeUri": "SHT:" + SHT_SERVER_GEN9_1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "bootMode": {"manageMode": True, "mode": "UEFI"},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": True,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                    }
                ],
                "volumeUri": None,
                "volume": {
                    "templateUri": "ROOT:" + STOREVIRTUAL_1_POOL_NAME,
                    "properties": {
                        "name": VOLUME_SV1_1_NAME,
                        "storagePool": "SP:" + STOREVIRTUAL_1_SYSTEM_NAME,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "isAdaptiveOptimizationEnabled": False
                    },
                    "isPermanent": False
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME
            },
        ],
        "sanSystemCredentials": []
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "EthConn",
                "functionType": "Ethernet",
                "networkUri": "ETH:" + ETH_NETWORK,
                "boot": {
                    "priority": "NotBootable",
                    "bootVlanId": None
                },
                "managed": True
            },
            {
                "id": 2,
                "name": "iSCSIConn",
                "functionType": "iSCSI",
                "networkUri": "ETH:" + ISCSI_NETWORK_1,
                "ipv4": {
                    "ipAddressSource": "DHCP"
                },
                "boot": {
                    "bootVolumeSource": "ManagedVolume",
                    "priority": "Primary",
                    "bootVlanId": None
                },
                "managed": True
            },
        ]
    },
}


ts1_spt_1_storevirtual = {
    "type": "ServerProfileTemplateV6",
    "name": SPT1_NAME,
    "serverHardwareTypeUri": "SHT:" + SHT_SERVER_GEN9_1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "bootMode": {"manageMode": True, "mode": "UEFI"},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": True,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                    }
                ],
                "volumeUri": None,
                "volume": {
                    "templateUri": "ROOT:" + STOREVIRTUAL_1_POOL_NAME,
                    "properties": {
                        "name": VOLUME_SV1_1_NAME,
                        "storagePool": "SP:" + STOREVIRTUAL_1_SYSTEM_NAME,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "isAdaptiveOptimizationEnabled": False
                    },
                    "isPermanent": False
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME
            },
        ],
        "sanSystemCredentials": [
            {
                "storageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME,
                "chapLevel": "None"
            },
        ]
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "EthConn",
                "functionType": "Ethernet",
                "networkUri": "ETH:" + ETH_NETWORK,
                "boot": {
                    "priority": "NotBootable",
                    "bootVlanId": None
                },
                "managed": True
            },
            {
                "id": 2,
                "name": "iSCSIConn",
                "functionType": "iSCSI",
                "networkUri": "ETH:" + ISCSI_NETWORK_1,
                "ipv4": {
                    "ipAddressSource": "DHCP"
                },
                "boot": {
                    "bootVolumeSource": "ManagedVolume",
                    "priority": "Primary",
                    "bootVlanId": None
                },
                "managed": True
            },
        ]
    },
}


ts1_spt_2_storevirtual = {
    "type": "ServerProfileTemplateV6",
    "name": SPT1_NAME,
    "serverHardwareTypeUri": "SHT:" + SHT_SERVER_GEN9_1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "bootMode": {"manageMode": True, "mode": "UEFI"},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": True,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                    }
                ],
                "volumeUri": None,
                "volume": {
                    "templateUri": "ROOT:" + STOREVIRTUAL_1_POOL_NAME,
                    "properties": {
                        "name": VOLUME_SV1_1_NAME,
                        "storagePool": "SP:" + STOREVIRTUAL_1_SYSTEM_NAME,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "isAdaptiveOptimizationEnabled": False
                    },
                    "isPermanent": False
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME
            },
            {
                "id": 2,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                    }
                ],
                "volumeUri": None,
                "volume": {
                    "templateUri": "ROOT:" + STOREVIRTUAL_1_POOL_NAME,
                    "properties": {
                        "name": VOLUME_SV1_2_NAME,
                        "storagePool": "SP:" + STOREVIRTUAL_1_SYSTEM_NAME,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "isAdaptiveOptimizationEnabled": False
                    },
                    "isPermanent": False
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME
            },
            {
                "id": 3,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 3,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                    }
                ],
                "volumeUri": None,
                "volume": {
                    "templateUri": "ROOT:" + STOREVIRTUAL_2_POOL_NAME,
                    "properties": {
                        "name": VOLUME_SV2_1_NAME,
                        "storagePool": "SP:" + STOREVIRTUAL_2_SYSTEM_NAME,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "isAdaptiveOptimizationEnabled": False
                    },
                    "isPermanent": False
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_2_SYSTEM_NAME
            }
        ],
        "sanSystemCredentials": [
            {
                "storageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME,
                "chapLevel": "None"
            },
            {
                "storageSystemUri": "SSYS:" + STOREVIRTUAL_2_SYSTEM_NAME,
                "chapLevel": "None"
            }
        ]
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "EthConn",
                "functionType": "Ethernet",
                "networkUri": "ETH:" + ETH_NETWORK,
                "boot": {
                    "priority": "NotBootable",
                    "bootVlanId": None
                },
                "managed": True
            },
            {
                "id": 2,
                "name": "iSCSIConn",
                "functionType": "iSCSI",
                "networkUri": "ETH:" + ISCSI_NETWORK_1,
                "ipv4": {
                    "ipAddressSource": "DHCP"
                },
                "boot": {
                    "bootVolumeSource": "ManagedVolume",
                    "priority": "Primary",
                    "bootVlanId": None
                },
                "managed": True
            },
            {
                "id": 3,
                "name": "iSCSIVLAN10Conn",
                "functionType": "iSCSI",
                "networkUri": "ETH:" + ISCSI_NETWORK_2,
                "boot": {
                    "priority": "NotBootable",
                    "bootVlanId": None
                },
                "managed": True
            }
        ]
    },
}

ts2_sp_0_storevirtual = {
    "type": "ServerProfileV10",
    "name": SP1_NAME,
    "serverHardwareUri": "SH:" + SERVER_GEN9_1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "bootMode": {"manageMode": True, "mode": "UEFI"},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": True,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                    }
                ],
                "volumeUri": None,
                "volume": {
                    "templateUri": "ROOT:" + STOREVIRTUAL_1_POOL_NAME,
                    "properties": {
                        "name": VOLUME_SV1_1_NAME,
                        "storagePool": "SP:" + STOREVIRTUAL_1_SYSTEM_NAME,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "isAdaptiveOptimizationEnabled": False
                    },
                    "isPermanent": False
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME
            },
            {
                "id": 2,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                    }
                ],
                "volumeUri": None,
                "volume": {
                    "templateUri": "ROOT:" + STOREVIRTUAL_1_POOL_NAME,
                    "properties": {
                        "name": VOLUME_SV1_2_NAME,
                        "storagePool": "SP:" + STOREVIRTUAL_1_SYSTEM_NAME,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "isAdaptiveOptimizationEnabled": False
                    },
                    "isPermanent": False
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME
            },
        ],
        "sanSystemCredentials": []
    },
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "EthConn",
                "functionType": "Ethernet",
                "networkUri": "ETH:" + ETH_NETWORK,
                "boot": {
                    "priority": "NotBootable",
                    "bootVlanId": None
                },
                "managed": True
            },
            {
                "id": 2,
                "name": "iSCSIConn",
                "functionType": "iSCSI",
                "networkUri": "ETH:" + ISCSI_NETWORK_1,
                "ipv4": {
                    "ipAddressSource": "DHCP"
                },
                "boot": {
                    "bootVolumeSource": "ManagedVolume",
                    "priority": "Primary",
                    "bootVlanId": None
                },
                "managed": True
            },
        ]
    },
}


ts2_sp_1_storevirtual = {
    "type": "ServerProfileV10",
    "name": SP1_NAME,
    "serverHardwareUri": "SH:" + SERVER_GEN9_1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "bootMode": {"manageMode": True, "mode": "UEFI"},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": True,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                    }
                ],
                "volumeUri": None,
                "volume": {
                    "templateUri": "ROOT:" + STOREVIRTUAL_1_POOL_NAME,
                    "properties": {
                        "name": VOLUME_SV1_1_NAME,
                        "storagePool": "SP:" + STOREVIRTUAL_1_SYSTEM_NAME,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "isAdaptiveOptimizationEnabled": False
                    },
                    "isPermanent": False
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME
            },
            {
                "id": 2,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                    }
                ],
                "volumeUri": None,
                "volume": {
                    "templateUri": "ROOT:" + STOREVIRTUAL_1_POOL_NAME,
                    "properties": {
                        "name": VOLUME_SV1_2_NAME,
                        "storagePool": "SP:" + STOREVIRTUAL_1_SYSTEM_NAME,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "isAdaptiveOptimizationEnabled": False
                    },
                    "isPermanent": False
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME
            },
        ],
        "sanSystemCredentials": [
            {
                "storageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME,
                "chapLevel": "None"
            },
        ]
    },
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "EthConn",
                "functionType": "Ethernet",
                "networkUri": "ETH:" + ETH_NETWORK,
                "boot": {
                    "priority": "NotBootable",
                    "bootVlanId": None
                },
                "managed": True
            },
            {
                "id": 2,
                "name": "iSCSIConn",
                "functionType": "iSCSI",
                "networkUri": "ETH:" + ISCSI_NETWORK_1,
                "ipv4": {
                    "ipAddressSource": "DHCP"
                },
                "boot": {
                    "bootVolumeSource": "ManagedVolume",
                    "priority": "Primary",
                    "bootVlanId": None
                },
                "managed": True
            },
        ]
    },
}


ts2_sp_2_storevirtual = {
    "type": "ServerProfileV10",
    "name": SP1_NAME,
    "serverHardwareUri": "SH:" + SERVER_GEN9_1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "bootMode": {"manageMode": True, "mode": "UEFI"},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": True,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                    }
                ],
                "volumeUri": None,
                "volume": {
                    "templateUri": "ROOT:" + STOREVIRTUAL_1_POOL_NAME,
                    "properties": {
                        "name": VOLUME_SV1_1_NAME,
                        "storagePool": "SP:" + STOREVIRTUAL_1_SYSTEM_NAME,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "isAdaptiveOptimizationEnabled": False
                    },
                    "isPermanent": False
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME
            },
            {
                "id": 2,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                    }
                ],
                "volumeUri": None,
                "volume": {
                    "templateUri": "ROOT:" + STOREVIRTUAL_1_POOL_NAME,
                    "properties": {
                        "name": VOLUME_SV1_2_NAME,
                        "storagePool": "SP:" + STOREVIRTUAL_1_SYSTEM_NAME,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "isAdaptiveOptimizationEnabled": False
                    },
                    "isPermanent": False
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME
            },
            {
                "id": 3,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 3,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                    }
                ],
                "volumeUri": None,
                "volume": {
                    "templateUri": "ROOT:" + STOREVIRTUAL_2_POOL_NAME,
                    "properties": {
                        "name": VOLUME_SV2_1_NAME,
                        "storagePool": "SP:" + STOREVIRTUAL_2_SYSTEM_NAME,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "isAdaptiveOptimizationEnabled": False
                    },
                    "isPermanent": False
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_2_SYSTEM_NAME
            }
        ],
        "sanSystemCredentials": [
            {
                "storageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME,
                "chapLevel": "None"
            },
            {
                "storageSystemUri": "SSYS:" + STOREVIRTUAL_2_SYSTEM_NAME,
                "chapLevel": "None"
            }
        ]
    },
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "EthConn",
                "functionType": "Ethernet",
                "networkUri": "ETH:" + ETH_NETWORK,
                "boot": {
                    "priority": "NotBootable",
                    "bootVlanId": None
                },
                "managed": True
            },
            {
                "id": 2,
                "name": "iSCSIConn",
                "functionType": "iSCSI",
                "networkUri": "ETH:" + ISCSI_NETWORK_1,
                "ipv4": {
                    "ipAddressSource": "DHCP"
                },
                "boot": {
                    "bootVolumeSource": "ManagedVolume",
                    "priority": "Primary",
                    "bootVlanId": None
                },
                "managed": True
            },
            {
                "id": 3,
                "name": "iSCSIVLAN10Conn",
                "functionType": "iSCSI",
                "networkUri": "ETH:" + ISCSI_NETWORK_2,
                "boot": {
                    "priority": "NotBootable",
                    "bootVlanId": None
                },
                "managed": True
            }
        ]
    },
}

ts6_spt_create = {
    "type": "ServerProfileTemplateV6",
    "name": SPT1_NAME,
    "serverHardwareTypeUri": "SHT:" + SHT_SERVER_GEN9_1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "bootMode": {"manageMode": True, "mode": "UEFI"},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": True,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                    }
                ],
                "volumeUri": None,
                "volume": {
                    "templateUri": "ROOT:" + STOREVIRTUAL_1_POOL_NAME,
                    "properties": {
                        "name": VOLUME_SV1_1_NAME,
                        "storagePool": "SP:" + STOREVIRTUAL_1_SYSTEM_NAME,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "isAdaptiveOptimizationEnabled": False
                    },
                    "isPermanent": False
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME
            },
            {
                "id": 2,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                    }
                ],
                "volumeUri": None,
                "volume": {
                    "templateUri": "ROOT:" + STOREVIRTUAL_1_POOL_NAME,
                    "properties": {
                        "name": VOLUME_SV1_2_NAME,
                        "storagePool": "SP:" + STOREVIRTUAL_1_SYSTEM_NAME,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "isAdaptiveOptimizationEnabled": False
                    },
                    "isPermanent": False
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME
            },
        ],
        "sanSystemCredentials": [
            {
                "storageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME,
                "chapLevel": "MutualChap"
            },
        ]
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "EthConn",
                "functionType": "Ethernet",
                "networkUri": "ETH:" + ETH_NETWORK,

                "boot": {
                    "priority": "NotBootable",
                    "bootVlanId": None
                },
                "managed": True
            },
            {
                "id": 2,
                "name": "iSCSIConn",
                "functionType": "iSCSI",
                "networkUri": "ETH:" + ISCSI_NETWORK_1,
                "ipv4": {
                    "ipAddressSource": "DHCP"
                },
                "boot": {
                    "bootVolumeSource": "ManagedVolume",
                    "priority": "Primary",
                    "bootVlanId": None
                },
                "managed": True
            },
            {
                "id": 3,
                "name": "iSCSIVLAN10Conn",
                "functionType": "iSCSI",
                "networkUri": "ETH:" + ISCSI_NETWORK_2,
                "boot": {
                    "priority": "NotBootable",
                    "bootVlanId": None
                },
                "managed": True
            }
        ]
    },
}

ts6_spt_edit = {
    "type": "ServerProfileTemplateV6",
    "name": SPT1_NAME,
    "serverHardwareTypeUri": "SHT:" + SHT_SERVER_GEN9_1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "bootMode": {"manageMode": True, "mode": "UEFI"},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "isBootVolume": True,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                    }
                ],
                "volumeUri": None,
                "volume": {
                    "templateUri": "ROOT:" + STOREVIRTUAL_1_POOL_NAME,
                    "properties": {
                        "name": VOLUME_SV1_1_NAME,
                        "storagePool": "SP:" + STOREVIRTUAL_1_SYSTEM_NAME,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "isAdaptiveOptimizationEnabled": False
                    },
                    "isPermanent": False
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 2,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                    }
                ],
                "volumeUri": None,
                "volume": {
                    "templateUri": "ROOT:" + STOREVIRTUAL_1_POOL_NAME,
                    "properties": {
                        "name": VOLUME_SV1_2_NAME,
                        "storagePool": "SP:" + STOREVIRTUAL_1_SYSTEM_NAME,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "isAdaptiveOptimizationEnabled": False
                    },
                    "isPermanent": False
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME
            },
            {
                "id": 3,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 3,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                    }
                ],
                "volumeUri": None,
                "volume": {
                    "templateUri": "ROOT:" + STOREVIRTUAL_2_POOL_NAME,
                    "properties": {
                        "name": VOLUME_SV2_1_NAME,
                        "storagePool": "SP:" + STOREVIRTUAL_2_SYSTEM_NAME,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "isAdaptiveOptimizationEnabled": False
                    },
                    "isPermanent": False
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_2_SYSTEM_NAME
            }
        ],
        "sanSystemCredentials": [
            {
                "storageSystemUri": "SSYS:" + STOREVIRTUAL_1_SYSTEM_NAME,
                "chapLevel": "MutualChap"
            },
            {
                "storageSystemUri": "SSYS:" + STOREVIRTUAL_2_SYSTEM_NAME,
                "chapLevel": "Chap"
            }
        ]
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "id": 1,
                "name": "EthConn",
                "functionType": "Ethernet",
                "networkUri": "ETH:" + ETH_NETWORK,

                "boot": {
                    "priority": "NotBootable",
                    "bootVlanId": None
                },
                "managed": True
            },
            {
                "id": 2,
                "name": "iSCSIConn",
                "functionType": "iSCSI",
                "networkUri": "ETH:" + ISCSI_NETWORK_1,
                "ipv4": {
                    "ipAddressSource": "DHCP"
                },
                "boot": {
                    "bootVolumeSource": "ManagedVolume",
                    "priority": "Primary",
                    "bootVlanId": None
                },
                "managed": True
            },
            {
                "id": 3,
                "name": "iSCSIVLAN10Conn",
                "functionType": "iSCSI",
                "networkUri": "ETH:" + ISCSI_NETWORK_2,
                "boot": {
                    "priority": "NotBootable",
                    "bootVlanId": None
                },
                "managed": True
            }
        ]
    },
}

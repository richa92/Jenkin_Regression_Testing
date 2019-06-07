admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

# EG
EG_NAME = 'EG1'

# Enclosures
ENC1 = 'CN754406XL'
ENC2 = 'CN754404R6'
ENC3 = 'CN754406WB'

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

# Server Hardware Types
SERVER_HARDWARE_TYPE1 = 'SHT:SY 660 Gen9:3:HP Synergy 3820C 10/20Gb CNA'

STOREVIRTUAL_SLPT_STORAGE_SYSTEM = 'VSA_Cluster_116'
STOREVIRTUAL_MLPT_STORAGE_SYSTEM = 'VSA84_Storage_Pool'
STORESERV_STORAGE_SYSTEM = 'wpst3par-7200-7-srv'
STORESERV_STORAGE_POOL = 'FVT_Tbird_reg1_r5'

STOREVIRTUAL_VOLUME_TEMPLATE_NAME1 = 'OVF961-StoreVirtual-RAID-0-Full-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME2 = 'OVF961-StoreVirtual-RAID-5-Full-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME3 = 'OVF961-StoreVirtual-RAID-6-Full-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME4 = 'OVF961-StoreVirtual-RAID-10-Full-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME5 = 'OVF961-StoreVirtual-RAID-10_1-Full-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME6 = 'OVF961-StoreVirtual-RAID-10_2-Full-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME7 = 'OVF961-StoreVirtual-RAID-0-Full-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME8 = 'OVF961-StoreVirtual-RAID-5-Full-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME9 = 'OVF961-StoreVirtual-RAID-6-Full-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME10 = 'OVF961-StoreVirtual-RAID-10-Full-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME11 = 'OVF961-StoreVirtual-RAID-10_1-Full-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME12 = 'OVF961-StoreVirtual-RAID-10_2-Full-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME13 = 'OVF961-StoreVirtual-RAID-0-Thin-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME14 = 'OVF961-StoreVirtual-RAID-5-Thin-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME15 = 'OVF961-StoreVirtual-RAID-6-Thin-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME16 = 'OVF961-StoreVirtual-RAID-10-Thin-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME17 = 'OVF961-StoreVirtual-RAID-10_1-Thin-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME18 = 'OVF961-StoreVirtual-RAID-10_2-Thin-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME19 = 'OVF961-StoreVirtual-RAID-0-Thin-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME20 = 'OVF961-StoreVirtual-RAID-5-Thin-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME21 = 'OVF961-StoreVirtual-RAID-6-Thin-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME22 = 'OVF961-StoreVirtual-RAID-10-Thin-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME23 = 'OVF961-StoreVirtual-RAID-10_1-Thin-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME24 = 'OVF961-StoreVirtual-RAID-10_2-Thin-Shared'
STORESERV_VOLUME_TEMPLATE_NAME1 = 'OVF961-StoreServ-Thin-Private'
STORESERV_VOLUME_TEMPLATE_NAME2 = 'OVF961-StoreServ-Full-Private'
STORESERV_VOLUME_TEMPLATE_NAME3 = 'OVF961-StoreServ-Thin-Shared'
STORESERV_VOLUME_TEMPLATE_NAME4 = 'OVF961-StoreServ-Full-Shared'

STOREVIRTUAL_EXISTING_SHARED_VOLUME1 = "dhcp-shared-volume1"
STOREVIRTUAL_EXISTING_PRIVATE_VOLUME1 = "tbird14-bay7-rhel-dhcp-managed-volume"
STOREVIRTUAL_EXISTING_PRIVATE_VOLUME2 = "tbird17-bay1-rhel-dhcp-managed-volume"


DHCP_BOOT_TARGET_IP = "192.168.21.59"
INITIATOR_GATEWAY = "192.168.0.1"
INITIATOR_SUBNET_MASK = "255.255.192.0"

STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK = 'ETH:network-untagged'
STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK = 'ETH:network-tunnel'
STORESERV_STORAGE_POOL_NETWORK = 'FC:FA1'

# Profiles
PROFILE1_NAME = 'OVF961-CGW-Profile1'
PROFILE2_NAME = 'OVF961-CGW-Profile2'
PROFILE2_VOLUME1_NAME = 'Existing Volume from ROOT Template'
PROFILE2_VOLUME1_DEVICE_VOLUME_NAME = 'ExistingVolumefromROOTTemplate'
PROFILE3_NAME = 'OVF961-CGW-Profile3'
PROFILE3_VOLUME1_NAME = 'OVF961-CGW-Profile3-Private-Thin-RAID-5'
PROFILE4_NAME = 'OVF961-CGW-Profile4'
PROFILE4_VOLUME1_NAME = 'OVF961-CGW-Profile4-StoreVirtual-MLPT-Private-Thin-RAID-10-3way'
PROFILE4_VOLUME2_NAME = 'OVF961-CGW-Profile4-StoreVirtual-MLPT-Shared-Full-RAID-0'
PROFILE5_NAME = 'OVF961-CGW-Profile5'
PROFILE5_VOLUME1_NAME = 'OVF961-StoreServ-Full-Private'

existing_volumes = [
    {
        "storageSystemUri": STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
        "name": STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
        "deviceVolumeName": STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
        "isShareable": True,
    },
]

# VOLUME TEMPLATES

# Full-RAID-0-Private
storevirtual_template1 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Full",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid0None",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
    "description": ""
}

storevirtual_template1_copy = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Full",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid0None",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        },
        "templateVersion": {
            "default": "1.1",
            "description": "Version of the template",
            "meta": {
                "locked": True
            },
            "required": True,
            "title": "Template version",
            "type": "string"
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
    "description": ""
}

# Full-RAID-5-Private
storevirtual_template2 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Full",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid5SingleParity",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME2,
    "description": ""
}

# Full-RAID-6-Private
storevirtual_template3 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Full",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid6DualParity",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME3,
    "description": ""
}

# Full-RAID-10-Private
storevirtual_template4 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Full",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid10Mirror2Way",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME4,
    "description": ""
}

# Full-RAID-10+1-Private
storevirtual_template5 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Full",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid10Mirror3Way",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME5,
    "description": ""
}

# Full-RAID-10+2-Private
storevirtual_template6 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Full",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid10Mirror4Way",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME6,
    "description": ""
}

# Full-RAID-0-Shared
storevirtual_template7 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": True,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Full",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid0None",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME7,
    "description": ""
}

# Full-RAID-5-Shared
storevirtual_template8 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": True,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Full",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid5SingleParity",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME8,
    "description": ""
}

# Full-RAID-6-Shared
storevirtual_template9 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": True,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Full",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid6DualParity",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME9,
    "description": ""
}

# Full-RAID-10-Shared
storevirtual_template10 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": True,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Full",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid10Mirror2Way",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME10,
    "description": ""
}

# Full-RAID-10+1-Shared
storevirtual_template11 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": True,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Full",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid10Mirror3Way",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME11,
    "description": ""
}

# Full-RAID-10+2-Shared
storevirtual_template12 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": True,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Full",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid10Mirror4Way",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME12,
    "description": ""
}

# Thin-RAID-0-Private
storevirtual_template13 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Thin",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid0None",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME13,
    "description": ""
}

# Thin-RAID-5-Private
storevirtual_template14 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Thin",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid5SingleParity",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME14,
    "description": ""
}

# Thin-RAID-6-Private
storevirtual_template15 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Thin",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid6DualParity",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
    "description": ""
}

storevirtual_template15_copy = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Thin",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid6DualParity",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        },
        "templateVersion": {
            "default": "1.1",
            "description": "Version of the template",
            "meta": {
                "locked": True
            },
            "required": True,
            "title": "Template version",
            "type": "string"
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
    "description": ""
}

# Thin-RAID-10-Private
storevirtual_template16 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Thin",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid10Mirror2Way",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME16,
    "description": ""
}

# Thin-RAID-10+1-Private
storevirtual_template17 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Thin",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid10Mirror3Way",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME17,
    "description": ""
}

# Thin-RAID-10+2-Private
storevirtual_template18 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Thin",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid10Mirror4Way",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME18,
    "description": ""
}

# Thin-RAID-0-Shared
storevirtual_template19 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": True,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Thin",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid0None",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME19,
    "description": ""
}

# Thin-RAID-5-Shared
storevirtual_template20 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": True,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Thin",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid5SingleParity",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME20,
    "description": ""
}

# Thin-RAID-6-Shared
storevirtual_template21 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": True,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Thin",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid6DualParity",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME21,
    "description": ""
}

# Thin-RAID-10-Shared
storevirtual_template22 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": True,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Thin",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid10Mirror2Way",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME22,
    "description": ""
}

# Thin-RAID-10+1-Shared
storevirtual_template23 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": True,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Thin",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid10Mirror3Way",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME23,
    "description": ""
}

# Thin-RAID-10+2-Shared
storevirtual_template24 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": True,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Thin",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid10Mirror4Way",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME24,
    "description": ""
}

# StoreServ-Thin-Private
storeserv_template1 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "maximum": 17592186044416,
            "minimum": 2684354560,
            "required": True,
            "description": "The capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "A common provisioning group URI reference",
            "default": STORESERV_STORAGE_POOL
        },
        "snapshotPool": {
            "meta": {
                "locked": True,
                "semanticType": "device-snapshot-storage-pool"
            },
            "type": "string",
            "title": "Snapshot Pool",
            "format": "x-uri-reference",
            "default": STORESERV_STORAGE_POOL,
            "description": "A URI reference to the common provisioning group used to create snapshots"
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full",
                "Thin Deduplication"
            ],
            "meta": {
                "locked": True,
                "createOnly": True
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Thin",
            "description": "The provisioning type for the volume"
        }
    },
    "name": STORESERV_VOLUME_TEMPLATE_NAME1,
    "description": ""
}

storeserv_template1_copy = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "maximum": 17592186044416,
            "minimum": 2684354560,
            "required": True,
            "description": "The capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "A common provisioning group URI reference",
            "default": STORESERV_STORAGE_POOL
        },
        "snapshotPool": {
            "meta": {
                "locked": True,
                "semanticType": "device-snapshot-storage-pool"
            },
            "type": "string",
            "title": "Snapshot Pool",
            "format": "x-uri-reference",
            "default": STORESERV_STORAGE_POOL,
            "description": "A URI reference to the common provisioning group used to create snapshots"
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full",
            ],
            "meta": {
                "locked": True,
                "createOnly": True
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Thin",
            "description": "The provisioning type for the volume"
        },
        "templateVersion": {
            "default": "1.1",
            "description": "Version of the template",
            "meta": {
                "locked": True
            },
            "required": True,
            "title": "Template version",
            "type": "string"
        },
        "isDeduplicated": {
            "default": False,
            "description": "Enables or disables deduplication of the volume",
            "meta": {
                "locked": True
            },
            "title": "Is Deduplicated",
            "type": "boolean"
        },
    },
    "name": STORESERV_VOLUME_TEMPLATE_NAME1,
    "description": ""
}

# StoreServ-Full-Private
storeserv_template2 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "maximum": 17592186044416,
            "minimum": 2684354560,
            "required": True,
            "description": "The capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "A common provisioning group URI reference",
            "default": STORESERV_STORAGE_POOL
        },
        "snapshotPool": {
            "meta": {
                "locked": True,
                "semanticType": "device-snapshot-storage-pool"
            },
            "type": "string",
            "title": "Snapshot Pool",
            "format": "x-uri-reference",
            "default": STORESERV_STORAGE_POOL,
            "description": "A URI reference to the common provisioning group used to create snapshots"
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full",
                "Thin Deduplication"
            ],
            "meta": {
                "locked": True,
                "createOnly": True
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Full",
            "description": "The provisioning type for the volume"
        }
    },
    "name": STORESERV_VOLUME_TEMPLATE_NAME2,
    "description": ""
}

# StoreServ-Thin-Shared
storeserv_template3 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "maximum": 17592186044416,
            "minimum": 2684354560,
            "required": True,
            "description": "The capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": True,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "A common provisioning group URI reference",
            "default": STORESERV_STORAGE_POOL
        },
        "snapshotPool": {
            "meta": {
                "locked": True,
                "semanticType": "device-snapshot-storage-pool"
            },
            "type": "string",
            "title": "Snapshot Pool",
            "format": "x-uri-reference",
            "default": STORESERV_STORAGE_POOL,
            "description": "A URI reference to the common provisioning group used to create snapshots"
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full",
                "Thin Deduplication"
            ],
            "meta": {
                "locked": True,
                "createOnly": True
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Thin",
            "description": "The provisioning type for the volume"
        }
    },
    "name": STORESERV_VOLUME_TEMPLATE_NAME3,
    "description": ""
}

# StoreServ-Full-Shared
storeserv_template4 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "maximum": 17592186044416,
            "minimum": 2684354560,
            "required": True,
            "description": "The capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True,
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": True,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "A common provisioning group URI reference",
            "default": STORESERV_STORAGE_POOL
        },
        "snapshotPool": {
            "meta": {
                "locked": True,
                "semanticType": "device-snapshot-storage-pool"
            },
            "type": "string",
            "title": "Snapshot Pool",
            "format": "x-uri-reference",
            "default": STORESERV_STORAGE_POOL,
            "description": "A URI reference to the common provisioning group used to create snapshots"
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full",
                "Thin Deduplication"
            ],
            "meta": {
                "locked": True,
                "createOnly": True
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Full",
            "description": "The provisioning type for the volume"
        }
    },
    "name": STORESERV_VOLUME_TEMPLATE_NAME4,
    "description": ""
}


# TS0 CREATE SERVER PROFILE TEMPLATES WITH V600 API

# one volume using templateUri:STOREVIRTUAL_VOLUME_TEMPLATE_NAME1
ts0_create_server_profile_template1 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# Existing StoreVirtual private volume
ts0_create_server_profile_template2 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE2_VOLUME1_NAME,
                        "description": "Existing private volume used as framework",
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# StoreVirtual private volume from Root template
ts0_create_server_profile_template3 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE3_VOLUME1_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid5SingleParity",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# StoreVirtual MLPT private volume from Root template
ts0_create_server_profile_template4 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE4_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE4_VOLUME1_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror3Way",
                        "storagePool": "SP:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Manual",
                "lun": 1,
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# StoreServprivate volume from Root template
ts0_create_server_profile_template5 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE5_NAME,
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
        "connections": [
            {
                "functionType": "FibreChannel",
                "id": 1,
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE5_VOLUME1_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STORESERV_STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}


# TS0 EDIT SERVER PROFILE TEMPLATES WITH V600 API

# Add a shared StoreServ volume
ts0_edit_server_profile_template1 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "FibreChannel",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            },

        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STORESERV_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL
                    },
                    "isPermanent": True,
                    "templateUri": 'SVT:' + STORESERV_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ],
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        }]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Add an existing shared StoreVirtual volume
ts0_edit_server_profile_template2 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE2_VOLUME1_NAME,
                        "description": "Existing private volume used as framework",
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ],
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        }]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# remove volume 1 and add a bootable StoreVirtual private volume from template
ts0_edit_server_profile_template3 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 2,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid6DualParity",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ],
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        }]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# add a StoreVirtual MLPT private volume from Root template and disable volume1 from being bootable
ts0_edit_server_profile_template4 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE4_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE4_VOLUME1_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror3Way",
                        "storagePool": "SP:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Manual",
                "lun": 1,
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE4_VOLUME2_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Manual",
                "lun": 2,
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ],
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM
        }]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# remove the bootable volume and the connection
ts0_edit_server_profile_template5 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE5_NAME,
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
        "manageConnections": False,
        "connections": [],
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}


# VERIFY CREATE SERVER PROFILE TEMPLATES WITH V600 API

# one volume using templateUri:STOREVIRTUAL_VOLUME_TEMPLATE_NAME1
ts1_verify_create_server_profile_template1_v600 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# Existing StoreVirtual Private volume
ts0_verify_create_server_profile_template2 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE2_VOLUME1_NAME,
                        "description": "Existing private volume used as framework",
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# StoreVirtual private volume from Root template
ts0_verify_create_server_profile_template3 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE3_VOLUME1_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid5SingleParity",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# StoreVirtual MLPT private volume from Root template
ts0_verify_create_server_profile_template4 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE4_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE4_VOLUME1_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror3Way",
                        "storagePool": "SP:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Manual",
                "lun": 1,
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# StoreServ private volume from Root template
ts0_verify_create_server_profile_template5 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE5_NAME,
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
        "connections": [
            {
                "functionType": "FibreChannel",
                "id": 1,
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE5_VOLUME1_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STORESERV_STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}


# TS0 VERIFY EDIT SERVER PROFILE TEMPLATES WITH V600 API

ts1_verify_edit_server_profile_template1_v600 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "FibreChannel",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            },

        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STORESERV_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STORESERV_STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

ts1_verify_edit_server_profile_template3_v600 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 2,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid6DualParity",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# TS1 CREATE SERVER PROFILE TEMPLATES WITH V500 API

# one volume using templateUri:STOREVIRTUAL_VOLUME_TEMPLATE_NAME1
ts1_create_server_profile_template1 = {
    "type": "ServerProfileTemplateV3",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volumeName": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                "volumeDescription": "useful description",
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
                "volumeProvisionType": "Full",
                "volumeProvisionedCapacityBytes": "10737418240",
                "volumeShareable": False,
                "lunType": "Auto",
                "dataProtectionLevel": "NetworkRaid0None",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "permanent": False,
            },
        ]
    }
}

# Existing StoreVirtual private volume
ts1_create_server_profile_template2 = {
    "type": "ServerProfileTemplateV3",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volumeName": PROFILE2_VOLUME1_NAME,
                "volumeDescription": "Existing private volume used as framework",
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "volumeProvisionedCapacityBytes": "21474836480",
                "volumeProvisionType": "Thin",
                "volumeShareable": False,
                "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                "permanent": True,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# StoreVirtual private volume from Root template
ts1_create_server_profile_template3 = {
    "type": "ServerProfileTemplateV3",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volumeName": PROFILE3_VOLUME1_NAME,
                "volumeDescription": "Private volume from ROOT template",
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "volumeProvisionedCapacityBytes": "10737418240",
                "volumeProvisionType": "Thin",
                "volumeShareable": False,
                "dataProtectionLevel": "NetworkRaid5SingleParity",
                "permanent": True,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# StoreVirtual MLPT private volume from Root template
ts1_create_server_profile_template4 = {
    "type": "ServerProfileTemplateV3",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE4_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volumeName": PROFILE4_VOLUME1_NAME,
                "volumeDescription": "Private volume from ROOT template",
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "volumeProvisionedCapacityBytes": "10737418240",
                "volumeProvisionType": "Thin",
                "volumeShareable": False,
                "dataProtectionLevel": "NetworkRaid10Mirror3Way",
                "permanent": False,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
                "lunType": "Manual",
                "lun": 1,
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# StoreServprivate volume from Root template
ts1_create_server_profile_template5 = {
    "type": "ServerProfileTemplateV3",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE5_NAME,
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
        "connections": [
            {
                "functionType": "FibreChannel",
                "id": 1,
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volumeName": PROFILE5_VOLUME1_NAME,
                "volumeDescription": "Private volume from ROOT template",
                "volumeStoragePoolUri": "SPOOL:" + STORESERV_STORAGE_POOL,
                "volumeProvisionedCapacityBytes": "10737418240",
                "volumeProvisionType": "Full",
                "volumeShareable": False,
                "permanent": False,
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}


# TS1 EDIT SERVER PROFILE TEMPLATES WITH V500 API

# Add a shared StoreServ volume
ts1_edit_server_profile_template1 = {
    "type": "ServerProfileTemplateV3",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "FibreChannel",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            },
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volumeName": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                "volumeDescription": "useful description",
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
                "volumeProvisionType": "Full",
                "volumeProvisionedCapacityBytes": "10737418240",
                "volumeShareable": False,
                "lunType": "Auto",
                "dataProtectionLevel": "NetworkRaid0None",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "permanent": False,
            },
            {
                "id": 2,
                "volumeUri": None,
                "volumeName": STORESERV_VOLUME_TEMPLATE_NAME1,
                "volumeDescription": "useful description",
                "volumeProvisionedCapacityBytes": "10737418240",
                "volumeProvisionType": "Thin",
                "volumeShareable": False,
                "volumeStoragePoolUri": "SPOOL:" + STORESERV_STORAGE_POOL,
                "permanent": True,
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Add an existing shared StoreVirtual volume
ts1_edit_server_profile_template2 = {
    "type": "ServerProfileTemplateV3",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volumeName": PROFILE2_VOLUME1_NAME,
                "volumeDescription": "Existing private volume used as framework",
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "volumeProvisionedCapacityBytes": "21474836480",
                "volumeProvisionType": "Thin",
                "volumeShareable": False,
                "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                "permanent": True,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# remove volume 1 and add a bootable StoreVirtual private volume from template
ts1_edit_server_profile_template3 = {
    "type": "ServerProfileTemplateV3",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 2,
                "volumeUri": None,
                "volumeName": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                "dataProtectionLevel": "NetworkRaid6DualParity",
                "volumeProvisionedCapacityBytes": "10737418240",
                "volumeProvisionType": "Thin",
                "volumeShareable": False,
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "permanent": False,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# add a StoreVirtual MLPT private volume from Root template and disable volume1 from being bootable
ts1_edit_server_profile_template4 = {
    "type": "ServerProfileTemplateV3",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE4_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volumeName": PROFILE4_VOLUME1_NAME,
                "volumeDescription": "Private volume from ROOT template",
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "volumeProvisionedCapacityBytes": "10737418240",
                "volumeProvisionType": "Thin",
                "volumeShareable": False,
                "dataProtectionLevel": "NetworkRaid10Mirror3Way",
                "permanent": False,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "isBootVolume": False,
                "lunType": "Manual",
                "lun": 1,
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "volumeUri": None,
                "volumeName": PROFILE4_VOLUME2_NAME,
                "volumeDescription": "Private volume from ROOT template",
                "dataProtectionLevel": "NetworkRaid0None",
                "volumeProvisionedCapacityBytes": "10737418240",
                "volumeProvisionType": "Thin",
                "volumeShareable": False,
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "permanent": False,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
                "lunType": "Manual",
                "lun": 2,
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# remove the bootable volume and the connection
ts1_edit_server_profile_template5 = {
    "type": "ServerProfileTemplateV3",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE5_NAME,
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
        "manageConnections": False,
        "connections": [],
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# TS2 DATA

ts2_verify_edit_server_profile_template1 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "FibreChannel",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            },

        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STORESERV_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STORESERV_STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# NEGATIVE CREATE SERVER PROFILE TASKS

# null volume name
negative_spt1 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Null_Volume_Name",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": None,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# invalid volume name with volume template
negative_spt2 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Invalid_Volume_Name",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": 3,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# Invalid description
negative_spt3 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Invalid_Description",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": 3,
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# Invalid size
negative_spt4 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Invalid_Size",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": "A",
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# null size
negative_spt5 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Null_Size",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": None,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# size too large for storage system
negative_spt6 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Size_Too_Large",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 999999999999999999,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# invalid data protection level with template
negative_spt7 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Set_Data_Protection_Level_Different_From_Volume_Template",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid11None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# invalid data protection level
negative_spt8 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Invalid_Data_Protection_Level",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid11None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# null data protection level
negative_spt9 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Null_Data_Protection_Level",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": None,
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# null isShareable
negative_spt10 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Null_isShareable",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": None,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# Invalid isShareable
negative_spt11 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Invalid_isShareable",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": 3,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# isShareable==True and Non-Permanent
negative_spt12 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_isShareable=True_and_Non-Permanent",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": True,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# isShareable==True and is bootable
negative_spt13 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_isShareable=True_and_Bootable",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME7,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": True,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME7,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}


# Data Provisioning Type Different from Template
negative_spt14 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Provisioning_Type_Different_From_Template",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# Invalid Data Provisioning Type
negative_spt15 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Invalid_Provisioning_Type",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Medium",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# Null Data Provisioning Type
negative_spt16 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Invalid_Provisioning_Type",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": None,
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# Null Storage Pool
negative_spt17 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Null_Storage_Pool",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": None,
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# Invalid isPermanent
negative_spt18 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Invalid_isPermanent",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                    },
                    "isPermanent": "A",
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# Null Template Uri
negative_spt19 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Null_TemplateUri",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                    },
                    "isPermanent": False,
                    "templateUri": None,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# Template Uri From Wrong Storage System/pool
negative_spt20 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_TemplateUri_from_Different_Pool",
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
        "connections": [
            {
                "functionType": "FibreChannel",
                "id": 1,
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL,
                    },
                    "isPermanent": False,
                    "templateUri": "SVT:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# Bootable volume but no bootable connections
negative_spt21 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Bootable_Volume_No_Bootable_Connections",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                    },
                    "isPermanent": False,
                    "templateUri": "SVT:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [],
            },
        ]
    }
}

# multiple Bootable volumes
negative_spt22 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Multiple_Boot_Volumes",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                    },
                    "isPermanent": False,
                    "templateUri": "SVT:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE2_VOLUME1_NAME,
                        "description": "Existing private volume used as framework",
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# POST with v600 API and v500 Request Body
negative_spt23 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_v600_API_with_v500_Request_Body",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volumeName": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                "volumeDescription": "",
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "volumeProvisionedCapacityBytes": "10737418240",
                "volumeProvisionType": "Thin",
                "volumeShareable": False,
                "dataProtectionLevel": "NetworkRaid10Mirror3Way",
                "permanent": False,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}


# NEGATIVE EDIT SERVER PROFILE TASKS

# create profile for negative edit validation tests
create_negative_edit_profile_template = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "manageConnections": False,
        "connections": [],
    }
}

# null volume name
negative_edit_spt1 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": None,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# invalid volume name with volume template
negative_edit_spt2 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": 3,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Invalid description
negative_edit_spt3 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": 3,
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Invalid size
negative_edit_spt4 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": "A",
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# null size
negative_edit_spt5 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": None,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# size too large for storaage system
negative_edit_spt6 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 999999999999999999,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# invalid data protection level with template
negative_edit_spt7 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid11None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# invalid data protection level
negative_edit_spt8 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid11None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# null data protection level
negative_edit_spt9 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": None,
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# null isShareable
negative_edit_spt10 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": None,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Invalid isShareable
negative_edit_spt11 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": 3,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# isShareable==True and Non-Permanent
negative_edit_spt12 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": True,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# isShareable==True and is bootable
negative_edit_spt13 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME7,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": True,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME7,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}


# Data Provisioning Type Different from Template
negative_edit_spt14 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Invalid Data Provisioning Type
negative_edit_spt15 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Medium",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Null Data Provisioning Type
negative_edit_spt16 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": None,
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Null Storage Pool
negative_edit_spt17 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": None,
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Invalid isPermanent
negative_edit_spt18 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                    },
                    "isPermanent": "A",
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Null Template Uri
negative_edit_spt19 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                    },
                    "isPermanent": False,
                    "templateUri": None,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Template Uri From Wrong Storage System/pool
negative_edit_spt20 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "FibreChannel",
                "id": 1,
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL,
                    },
                    "isPermanent": False,
                    "templateUri": "SVT:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Bootable volume but no bootable connections
negative_edit_spt21 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                    },
                    "isPermanent": False,
                    "templateUri": "SVT:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# multiple Bootable volumes
negative_edit_spt22 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                    },
                    "isPermanent": False,
                    "templateUri": "SVT:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE2_VOLUME1_NAME,
                        "description": "Existing private volume used as framework",
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# PUT with v600 API and v500 Request Body
negative_edit_spt23 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Edit_Profile_Validation_Test",
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volumeName": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                "volumeDescription": "",
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "volumeProvisionedCapacityBytes": "10737418240",
                "volumeProvisionType": "Thin",
                "volumeShareable": False,
                "dataProtectionLevel": "NetworkRaid10Mirror3Way",
                "permanent": False,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# CREATE SERVER PROFILE FROM SERVER PROFILE TEMPLATE DATA

# V600 API

ts6_create_spt_profile1 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "FibreChannel",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            },

        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STORESERV_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL
                    },
                    "isPermanent": True,
                    "templateUri": 'SVT:' + STORESERV_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
}

ts6_create_spt_profile2 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE2_VOLUME1_NAME,
                        "description": "Existing private volume used as framework",
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts6_create_spt_profile3 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 2,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid6DualParity",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts6_create_spt_profile4 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE4_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA84_Storage_Pool"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE4_VOLUME1_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror3Way",
                        "storagePool": "SP:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Manual",
                "lun": 1,
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE4_VOLUME2_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Manual",
                "lun": 2,
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts6_create_spt_profile5 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE5_NAME,
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
        "connections": [
            {
                "functionType": "FibreChannel",
                "id": 1,
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE5_VOLUME1_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STORESERV_STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts6_create_sp_from_spt_profile1 = {
    "type": "ServerProfileV10",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE1_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "FibreChannel",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            },

        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STORESERV_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL
                    },
                    "isPermanent": True,
                    "templateUri": 'SVT:' + STORESERV_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts6_verify_create_sp_from_spt_profile1 = {
    "type": "ServerProfileV10",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE1_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "FibreChannel",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            },

        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": 'v:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": 'v:' + STORESERV_VOLUME_TEMPLATE_NAME1,
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts6_create_sp_from_spt_profile2 = {
    "type": "ServerProfileV10",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE2_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE2_VOLUME1_NAME,
                        "description": "Existing private volume used as framework",
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts6_verify_create_sp_from_spt_profile2 = {
    "type": "ServerProfileV10",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE2_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": 'v:' + PROFILE2_VOLUME1_NAME,
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts6_create_sp_from_spt_profile3 = {
    "type": "ServerProfileV10",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE3_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid6DualParity",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts6_verify_create_sp_from_spt_profile3 = {
    "type": "ServerProfileV10",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE3_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": 'v:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts6_create_sp_from_spt_profile4 = {
    "type": "ServerProfileV10",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE4_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE4_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA84_Storage_Pool"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE4_VOLUME1_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror3Way",
                        "storagePool": "SP:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Manual",
                "lun": 1,
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE4_VOLUME2_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Manual",
                "lun": 2,
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts6_verify_create_sp_from_spt_profile4 = {
    "type": "ServerProfileV10",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE4_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE4_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA84_Storage_Pool"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": 'v:' + PROFILE4_VOLUME1_NAME,
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Manual",
                "lun": 1,
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": 'v:' + PROFILE4_VOLUME2_NAME,
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Manual",
                "lun": 2,
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts6_create_sp_from_spt_profile5 = {
    "type": "ServerProfileV10",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE5_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE5_NAME,
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
        "connections": [
            {
                "functionType": "FibreChannel",
                "id": 1,
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE5_VOLUME1_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STORESERV_STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts6_verify_create_sp_from_spt_profile5 = {
    "type": "ServerProfileV10",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE5_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE5_NAME,
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
        "connections": [
            {
                "functionType": "FibreChannel",
                "id": 1,
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": 'v:' + PROFILE5_VOLUME1_NAME,
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts7_create_spt_profile1 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "FibreChannel",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            },

        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STORESERV_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STORESERV_STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
}

ts7_create_spt_profile2 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE2_VOLUME1_NAME,
                        "description": "Existing private volume used as framework",
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts7_create_spt_profile3 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 2,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid6DualParity",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts7_create_spt_profile4 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE4_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA84_Storage_Pool"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE4_VOLUME1_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror3Way",
                        "storagePool": "SP:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Manual",
                "lun": 1,
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE4_VOLUME2_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Manual",
                "lun": 2,
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts7_create_spt_profile5 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE5_NAME,
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
        "connections": [
            {
                "functionType": "FibreChannel",
                "id": 1,
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE5_VOLUME1_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STORESERV_STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts7_create_sp_from_spt_profile1 = {
    "type": "ServerProfileV7",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE1_NAME,
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
    "connections": [
        {
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
        },
        {
            "functionType": "FibreChannel",
            "id": 2,
            "name": "Connection 2",
            "networkUri": STORESERV_STORAGE_POOL_NETWORK,
        },

    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volumeName": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                "volumeDescription": "useful description",
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
                "volumeProvisionType": "Full",
                "volumeProvisionedCapacityBytes": "10737418240",
                "volumeShareable": False,
                "lunType": "Auto",
                "dataProtectionLevel": "NetworkRaid0None",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "permanent": False,
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": None,
                "volumeName": STORESERV_VOLUME_TEMPLATE_NAME1,
                "volumeDescription": "useful description",
                "volumeProvisionedCapacityBytes": "10737418240",
                "volumeProvisionType": "Thin",
                "volumeShareable": False,
                "volumeStoragePoolUri": "SPOOL:" + STORESERV_STORAGE_POOL,
                "permanent": True,
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts7_create_sp_from_spt_profile2 = {
    "type": "ServerProfileV7",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE2_NAME,
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
    "connections": [
        {
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
        },
        {
            "functionType": "Ethernet",
            "id": 2,
            "name": "Connection 2",
            "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volumeName": PROFILE2_VOLUME1_NAME,
                "volumeDescription": "Existing private volume used as framework",
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "volumeProvisionedCapacityBytes": "21474836480",
                "volumeProvisionType": "Thin",
                "volumeShareable": False,
                "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                "permanent": True,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts7_create_sp_from_spt_profile3 = {
    "type": "ServerProfileV7",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE3_NAME,
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
    "connections": [
        {
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
        },
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": None,
                "volumeName": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                "dataProtectionLevel": "NetworkRaid6DualParity",
                "volumeProvisionedCapacityBytes": "10737418240",
                "volumeProvisionType": "Thin",
                "volumeShareable": False,
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "permanent": False,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts7_create_sp_from_spt_profile4 = {
    "type": "ServerProfileV7",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE4_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE4_NAME,
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
    "connections": [
        {
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
        },
        {
            "functionType": "Ethernet",
            "id": 2,
            "name": "Connection 2",
            "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA84_Storage_Pool"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volumeName": PROFILE4_VOLUME1_NAME,
                "volumeDescription": "Private volume from ROOT template",
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "volumeProvisionedCapacityBytes": "10737418240",
                "volumeProvisionType": "Thin",
                "volumeShareable": False,
                "dataProtectionLevel": "NetworkRaid10Mirror3Way",
                "permanent": False,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "isBootVolume": False,
                "lunType": "Manual",
                "lun": 1,
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": None,
                "volumeName": PROFILE4_VOLUME2_NAME,
                "volumeDescription": "Private volume from ROOT template",
                "dataProtectionLevel": "NetworkRaid0None",
                "volumeProvisionedCapacityBytes": "10737418240",
                "volumeProvisionType": "Thin",
                "volumeShareable": False,
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "permanent": False,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
                "lunType": "Manual",
                "lun": 2,
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts7_create_sp_from_spt_profile5 = {
    "type": "ServerProfileV7",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE5_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE5_NAME,
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
    "connections": [
        {
            "functionType": "FibreChannel",
            "id": 1,
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORESERV_STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volumeName": PROFILE5_VOLUME1_NAME,
                "volumeDescription": "Private volume from ROOT template",
                "volumeStoragePoolUri": "SPOOL:" + STORESERV_STORAGE_POOL,
                "volumeProvisionedCapacityBytes": "10737418240",
                "volumeProvisionType": "Full",
                "volumeShareable": False,
                "permanent": False,
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts7_verify_create_sp_from_spt_profile1 = {
    "type": "ServerProfileV7",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE1_NAME,
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
    "connections": [
        {
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
        },
        {
            "functionType": "FibreChannel",
            "id": 2,
            "name": "Connection 2",
            "networkUri": STORESERV_STORAGE_POOL_NETWORK,
        },

    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": 'v:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": 'v:' + STORESERV_VOLUME_TEMPLATE_NAME1,
                "volumeStoragePoolUri": "SPOOL:" + STORESERV_STORAGE_POOL,
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts7_verify_create_sp_from_spt_profile2 = {
    "type": "ServerProfileV7",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE2_NAME,
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
    "connections": [
        {
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
        },
        {
            "functionType": "Ethernet",
            "id": 2,
            "name": "Connection 2",
            "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": 'v:' + PROFILE2_VOLUME1_NAME,
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts7_verify_create_sp_from_spt_profile3 = {
    "type": "ServerProfileV7",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE3_NAME,
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
    "connections": [
        {
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
        },
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": 'v:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts7_verify_create_sp_from_spt_profile4 = {
    "type": "ServerProfileV7",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE4_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE4_NAME,
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
    "connections": [
        {
            "functionType": "Ethernet",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
        },
        {
            "functionType": "Ethernet",
            "id": 2,
            "name": "Connection 2",
            "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA84_Storage_Pool"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": 'v:' + PROFILE4_VOLUME1_NAME,
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "isBootVolume": False,
                "lunType": "Manual",
                "lun": 1,
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": 'v:' + PROFILE4_VOLUME2_NAME,
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
                "lunType": "Manual",
                "lun": 2,
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts7_verify_create_sp_from_spt_profile5 = {
    "type": "ServerProfileV7",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE5_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE5_NAME,
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
    "connections": [
        {
            "functionType": "FibreChannel",
            "id": 1,
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORESERV_STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": 'v:' + PROFILE5_VOLUME1_NAME,
                "volumeStoragePoolUri": "SPOOL:" + STORESERV_STORAGE_POOL,
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

# VERIFY VOLUMES AFTER CREATE SERVER PROFILES FROM TEMPLATES

ts6_verify_volume1_profile1 = {
    "category": "storage-volumes",
    "description": "useful description",
    "deviceSpecificAttributes": {
        "dataProtectionLevel": "NetworkRaid0None",
        "isAdaptiveOptimizationEnabled": True,
    },
    "deviceVolumeName": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
    "isPermanent": False,
    "isShareable": False,
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
    "provisionedCapacity": "10737418240",
    "provisioningType": "Full",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV7",
    "uri": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
    "volumeTemplateUri": "SVT:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
}

ts6_verify_volume2_profile1 = {
    "category": "storage-volumes",
    "description": "useful description",
    "deviceVolumeName": STORESERV_VOLUME_TEMPLATE_NAME1,
    "isPermanent": True,
    "isShareable": False,
    "name": STORESERV_VOLUME_TEMPLATE_NAME1,
    "provisionedCapacity": "10737418240",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STORESERV_STORAGE_POOL,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV7",
    "uri": STORESERV_VOLUME_TEMPLATE_NAME1,
    "volumeTemplateUri": "SVT:" + STORESERV_VOLUME_TEMPLATE_NAME1,
}

ts6_verify_volume1_profile2 = {
    "category": "storage-volumes",
    "description": "Existing private volume used as framework",
    "deviceSpecificAttributes": {
        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
        "isAdaptiveOptimizationEnabled": True,
    },
    "deviceVolumeName": PROFILE2_VOLUME1_DEVICE_VOLUME_NAME,
    "isPermanent": True,
    "isShareable": False,
    "name": PROFILE2_VOLUME1_NAME,
    "provisionedCapacity": "21474836480",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV7",
    "uri": PROFILE2_VOLUME1_NAME,
    "volumeTemplateUri": None,
}

ts6_verify_volume2_profile2 = {
    "category": "storage-volumes",
    "description": "",
    "deviceSpecificAttributes": {
        "dataProtectionLevel": "NetworkRaid5SingleParity",
        "isAdaptiveOptimizationEnabled": True,
    },
    "deviceVolumeName": STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
    "isPermanent": True,
    "isShareable": True,
    "name": STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
    "provisionedCapacity": "1073741824",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV7",
    "uri": STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
    "volumeTemplateUri": None,
}

ts6_verify_volume2_profile3 = {
    "category": "storage-volumes",
    "description": "",
    "deviceSpecificAttributes": {
        "dataProtectionLevel": "NetworkRaid6DualParity",
        "isAdaptiveOptimizationEnabled": True,
    },
    "deviceVolumeName": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
    "isPermanent": False,
    "isShareable": False,
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
    "provisionedCapacity": "10737418240",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV7",
    "uri": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
    "volumeTemplateUri": "SVT:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
}

ts6_verify_volume1_profile4 = {
    "category": "storage-volumes",
    "description": "Private volume from ROOT template",
    "deviceSpecificAttributes": {
        "dataProtectionLevel": "NetworkRaid10Mirror3Way",
        "isAdaptiveOptimizationEnabled": True,
    },
    "deviceVolumeName": PROFILE4_VOLUME1_NAME,
    "isPermanent": False,
    "isShareable": False,
    "name": PROFILE4_VOLUME1_NAME,
    "provisionedCapacity": "10737418240",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV7",
    "uri": PROFILE4_VOLUME1_NAME,
    "volumeTemplateUri": None,
}

ts6_verify_volume2_profile4 = {
    "category": "storage-volumes",
    "description": "Private volume from ROOT template",
    "deviceSpecificAttributes": {
        "dataProtectionLevel": "NetworkRaid0None",
        "isAdaptiveOptimizationEnabled": True,
    },
    "deviceVolumeName": PROFILE4_VOLUME2_NAME,
    "isPermanent": False,
    "isShareable": False,
    "name": PROFILE4_VOLUME2_NAME,
    "provisionedCapacity": "10737418240",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV7",
    "uri": PROFILE4_VOLUME2_NAME,
    "volumeTemplateUri": None,
}

ts6_verify_volume1_profile5 = {
    "category": "storage-volumes",
    "description": "Private volume from ROOT template",
    "deviceVolumeName": PROFILE5_VOLUME1_NAME,
    "isPermanent": False,
    "isShareable": False,
    "name": PROFILE5_VOLUME1_NAME,
    "provisionedCapacity": "10737418240",
    "provisioningType": "Full",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STORESERV_STORAGE_POOL,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV7",
    "uri": PROFILE5_VOLUME1_NAME,
    "volumeTemplateUri": None,
}

ts7_verify_volume1_profile1 = {
    "category": "storage-volumes",
    "description": "useful description",
    "deviceSpecificAttributes": {
        "dataProtectionLevel": "NetworkRaid0None",
        "isAdaptiveOptimizationEnabled": True,
    },
    "deviceVolumeName": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
    "isPermanent": False,
    "isShareable": False,
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
    "provisionedCapacity": "10737418240",
    "provisioningType": "Full",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV7",
    "uri": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
    "volumeTemplateUri": None,
}

ts7_verify_volume2_profile1 = {
    "category": "storage-volumes",
    "description": "useful description",
    "deviceVolumeName": STORESERV_VOLUME_TEMPLATE_NAME1,
    "isPermanent": True,
    "isShareable": False,
    "name": STORESERV_VOLUME_TEMPLATE_NAME1,
    "provisionedCapacity": "10737418240",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STORESERV_STORAGE_POOL,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV7",
    "uri": STORESERV_VOLUME_TEMPLATE_NAME1,
    "volumeTemplateUri": None,
}

ts7_verify_volume1_profile2 = {
    "category": "storage-volumes",
    "description": "Existing private volume used as framework",
    "deviceSpecificAttributes": {
        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
        "isAdaptiveOptimizationEnabled": True,
    },
    "deviceVolumeName": PROFILE2_VOLUME1_DEVICE_VOLUME_NAME,
    "isPermanent": True,
    "isShareable": False,
    "name": PROFILE2_VOLUME1_NAME,
    "provisionedCapacity": "21474836480",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV7",
    "uri": PROFILE2_VOLUME1_NAME,
    "volumeTemplateUri": None,
}

ts7_verify_volume2_profile2 = {
    "category": "storage-volumes",
    "description": "",
    "deviceSpecificAttributes": {
        "dataProtectionLevel": "NetworkRaid5SingleParity",
        "isAdaptiveOptimizationEnabled": True,
    },
    "deviceVolumeName": STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
    "isPermanent": True,
    "isShareable": True,
    "name": STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
    "provisionedCapacity": "1073741824",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV7",
    "uri": STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
    "volumeTemplateUri": None,
}

ts7_verify_volume2_profile3 = {
    "category": "storage-volumes",
    "description": "",
    "deviceSpecificAttributes": {
        "dataProtectionLevel": "NetworkRaid6DualParity",
        "isAdaptiveOptimizationEnabled": True,
    },
    "deviceVolumeName": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
    "isPermanent": False,
    "isShareable": False,
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
    "provisionedCapacity": "10737418240",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV7",
    "uri": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
    "volumeTemplateUri": None,
}

ts7_verify_volume1_profile4 = {
    "category": "storage-volumes",
    "description": "Private volume from ROOT template",
    "deviceSpecificAttributes": {
        "dataProtectionLevel": "NetworkRaid10Mirror3Way",
        "isAdaptiveOptimizationEnabled": True,
    },
    "deviceVolumeName": PROFILE4_VOLUME1_NAME,
    "isPermanent": False,
    "isShareable": False,
    "name": PROFILE4_VOLUME1_NAME,
    "provisionedCapacity": "10737418240",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV7",
    "uri": PROFILE4_VOLUME1_NAME,
    "volumeTemplateUri": None,
}

ts7_verify_volume2_profile4 = {
    "category": "storage-volumes",
    "description": "Private volume from ROOT template",
    "deviceSpecificAttributes": {
        "dataProtectionLevel": "NetworkRaid0None",
        "isAdaptiveOptimizationEnabled": True,
    },
    "deviceVolumeName": PROFILE4_VOLUME2_NAME,
    "isPermanent": False,
    "isShareable": False,
    "name": PROFILE4_VOLUME2_NAME,
    "provisionedCapacity": "10737418240",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV7",
    "uri": PROFILE4_VOLUME2_NAME,
    "volumeTemplateUri": None,
}

ts7_verify_volume1_profile5 = {
    "category": "storage-volumes",
    "description": "Private volume from ROOT template",
    "deviceVolumeName": PROFILE5_VOLUME1_NAME,
    "isPermanent": False,
    "isShareable": False,
    "name": PROFILE5_VOLUME1_NAME,
    "provisionedCapacity": "10737418240",
    "provisioningType": "Full",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STORESERV_STORAGE_POOL,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV7",
    "uri": PROFILE5_VOLUME1_NAME,
    "volumeTemplateUri": None,
}

# SERVER PROFILE COMPLIANCE

profile1_compliance = {
    "name": PROFILE1_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": []}
}

profile2_compliance = {
    "name": PROFILE2_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": []}
}

profile3_compliance = {
    "name": PROFILE3_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": []}
}

profile4_compliance = {
    "name": PROFILE4_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": []}
}

profile5_compliance = {
    "name": PROFILE5_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": []}
}

# NON-COMPLIANCE DATA

profile1_sp_non_compliant = {
    "name": PROFILE1_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": [
            "REGEX:Attachment id \d for volume {\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the permanent setting in the template\.",
            "REGEX:Attachment id \d for volume {\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the permanent setting in the template\.",
        ],
    }
}

profile2_sp_non_compliant = {
    "name": PROFILE2_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": [
            "REGEX:Attachment id \d for volume {\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the provisioning setting in the template\.",
            "REGEX:Attachment id \d for volume {\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the permanent setting in the template\.",
            "REGEX:Attachment id \d for volume {\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"} must be at least the capacity of the volume as defined in the server profile template\. The capacity of the volume can be corrected on the volumes page.  Alternatively, the volume\'s defined capacity can be corrected on the server profile template and volume template \(if present\) instead of changing the volume\'s capacity\.",
            "REGEX:Attachment id \d for volume {\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the data protection level setting in the template\."
        ],
    }
}

profile3_sp_non_compliant = {
    "name": PROFILE3_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": [
            "REGEX:Attachment id \d for volume {\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the permanent setting in the template\.",
        ],
    }
}

profile4_sp_non_compliant = {
    "name": PROFILE4_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": [
            "REGEX:Attachment id \d for volume {\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the provisioning setting in the template\.",
            "REGEX:Attachment id \d for volume {\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the permanent setting in the template\.",
            "REGEX:Attachment id \d for volume {\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"} must be at least the capacity of the volume as defined in the server profile template\. The capacity of the volume can be corrected on the volumes page.  Alternatively, the volume\'s defined capacity can be corrected on the server profile template and volume template \(if present\) instead of changing the volume\'s capacity\.",
            "REGEX:Attachment id \d for volume {\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the data protection level setting in the template\.",
            "REGEX:Attachment id \d for volume {\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the provisioning setting in the template\.",
            "REGEX:Attachment id \d for volume {\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the permanent setting in the template\.",
            "REGEX:Attachment id \d for volume {\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"} must be at least the capacity of the volume as defined in the server profile template\. The capacity of the volume can be corrected on the volumes page.  Alternatively, the volume\'s defined capacity can be corrected on the server profile template and volume template \(if present\) instead of changing the volume\'s capacity\.",
            "REGEX:Attachment id \d for volume {\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the data protection level setting in the template\."
        ],
    }
}

profile5_sp_non_compliant = {
    "name": PROFILE5_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": [
            "REGEX:Attachment id \d for volume {\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the provisioning setting in the template\.",
            "REGEX:Attachment id \d for volume {\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the permanent setting in the template\.",
            "REGEX:Attachment id \d for volume {\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"} must be at least the capacity of the volume as defined in the server profile template\. The capacity of the volume can be corrected on the volumes page.  Alternatively, the volume\'s defined capacity can be corrected on the server profile template and volume template \(if present\) instead of changing the volume\'s capacity\.",
        ],
    }
}

profile1_spt_non_compliant = {
    "name": PROFILE1_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": [
            "REGEX:Attachment id 1 for volume {\"name\":\"" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1 + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the provisioning setting in the template\.",
            "REGEX:Attachment id 1 for volume {\"name\":\"" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1 + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the permanent setting in the template\.",
            "REGEX:Attachment id 1 for volume {\"name\":\"" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1 + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} must be at least the capacity of the volume as defined in the server profile template\. The capacity of the volume can be corrected on the volumes page.  Alternatively, the volume\'s defined capacity can be corrected on the server profile template and volume template \(if present\) instead of changing the volume\'s capacity\.",
            "REGEX:Attachment id 1 for volume {\"name\":\"" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1 + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the data protection level setting in the template\.",
            "REGEX:Attachment id 1 for volume {\"name\":\"" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1 + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the volume template specified in the profile template\.",
            "REGEX:Attachment id 2 for volume {\"name\":\"" + STORESERV_VOLUME_TEMPLATE_NAME1 + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the provisioning setting in the template\.",
            "REGEX:Attachment id 2 for volume {\"name\":\"" + STORESERV_VOLUME_TEMPLATE_NAME1 + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the permanent setting in the template\.",
            "REGEX:Attachment id 2 for volume {\"name\":\"" + STORESERV_VOLUME_TEMPLATE_NAME1 + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} must be at least the capacity of the volume as defined in the server profile template\. The capacity of the volume can be corrected on the volumes page.  Alternatively, the volume\'s defined capacity can be corrected on the server profile template and volume template \(if present\) instead of changing the volume\'s capacity\.",
            "REGEX:Attachment id 2 for volume {\"name\":\"" + STORESERV_VOLUME_TEMPLATE_NAME1 + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the volume template specified in the profile template\.",
        ],
    }
}

profile2_spt_non_compliant = {
    "name": PROFILE2_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": [
            "REGEX:Attachment id 1 for volume {\"name\":\"" + PROFILE2_VOLUME1_NAME + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the provisioning setting in the template\.",
            "REGEX:Attachment id 1 for volume {\"name\":\"" + PROFILE2_VOLUME1_NAME + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the permanent setting in the template\.",
            "REGEX:Attachment id 1 for volume {\"name\":\"" + PROFILE2_VOLUME1_NAME + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the data protection level setting in the template\."
        ],
    }
}

profile3_spt_non_compliant = {
    "name": PROFILE3_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": [
            "REGEX:Change boot for connection 1 on port Mezzanine \(Mezz\) \d:\d-a to not bootable\.",
            "REGEX:Remove IPv4 configuration from connection 1 on port Mezzanine \(Mezz\) \d:\d-a\.",
            "REGEX:Change boot setting of volume attachment id 2 for volume {\"name\":\"" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15 + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} to not bootable\.",
            "REGEX:Attachment id 2 for volume {\"name\":\"" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15 + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the volume template specified in the profile template\."
        ],
    }
}

profile4_spt_non_compliant = {
    "name": PROFILE4_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [
            "REGEX:Configure the volume attachment\(s\) of storage system {\"name\":\"VSA_Cluster_116\", \"uri\":\"\/rest\/storage-systems\/.*\"} to use CHAP level MutualChap\."
        ],
        "manualUpdates": [
            "REGEX:Change network of connection 1 on port Mezzanine \(Mezz\) \d:\d-a to {\"name\":\"network-untagged\", \"uri\":\"\/rest\/ethernet-networks\/.*\"}\.",
            "REGEX:Attachment id 1 for volume {\"name\":\"" + PROFILE4_VOLUME1_NAME + "\", \"uri\":\"/rest/storage-volumes/.*\"} does not match the provisioning setting in the template\.",
            "REGEX:Attachment id 1 for volume {\"name\":\"" + PROFILE4_VOLUME1_NAME + "\", \"uri\":\"/rest/storage-volumes/.*\"} does not match the permanent setting in the template\.",
            "REGEX:Attachment id 1 for volume {\"name\":\"" + PROFILE4_VOLUME1_NAME + "\", \"uri\":\"/rest/storage-volumes/.*\"} must be at least the capacity of the volume as defined in the server profile template\. The capacity of the volume can be corrected on the volumes page.  Alternatively, the volume\'s defined capacity can be corrected on the server profile template and volume template \(if present\) instead of changing the volume\'s capacity\.",
            "REGEX:Attachment id 1 for volume {\"name\":\"" + PROFILE4_VOLUME1_NAME + "\", \"uri\":\"/rest/storage-volumes/.*\"} does not match the data protection level setting in the template\.",
            "REGEX:Attachment id 2 for volume {\"name\":\"" + PROFILE4_VOLUME2_NAME + "\", \"uri\":\"/rest/storage-volumes/.*\"} does not match the volume template specified in the profile template\.",
            "REGEX:Change LUN type of volume attachment id 2 for volume {\"name\":\"" + PROFILE4_VOLUME2_NAME + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} to Auto\."
        ],
    }
}

profile5_spt_non_compliant = {
    "name": PROFILE5_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": [
            "REGEX:Change boot for connection 1 on port Mezzanine \(Mezz\) \d:\d-b to not bootable\.",
            "REGEX:Change boot setting of volume attachment id 1 for volume {\"name\":\"" + PROFILE5_VOLUME1_NAME + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} to not bootable\.",
            "REGEX:Attachment id 1 for volume {\"name\":\"" + PROFILE5_VOLUME1_NAME + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the provisioning setting in the template\.",
            "REGEX:Attachment id 1 for volume {\"name\":\"" + PROFILE5_VOLUME1_NAME + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} does not match the permanent setting in the template\.",
            "REGEX:Attachment id 1 for volume {\"name\":\"" + PROFILE5_VOLUME1_NAME + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} must be at least the capacity of the volume as defined in the server profile template\. The capacity of the volume can be corrected on the volumes page.  Alternatively, the volume\'s defined capacity can be corrected on the server profile template and volume template \(if present\) instead of changing the volume\'s capacity\."
        ],
    }
}

ts8_create_sp_from_spt_profile1 = {
    "type": "ServerProfileV10",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE1_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "FibreChannel",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            },

        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description that's different",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STORESERV_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description that's different",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STORESERV_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts8_create_sp_from_spt_profile2 = {
    "type": "ServerProfileV10",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE2_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE2_VOLUME1_NAME,
                        "description": "useful description",
                        "size": 214748364,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts8_create_sp_from_spt_profile3 = {
    "type": "ServerProfileV10",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE3_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid6DualParity",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts8_create_sp_from_spt_profile4 = {
    "type": "ServerProfileV10",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE4_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE4_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA84_Storage_Pool"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE4_VOLUME1_NAME,
                        "description": "useful description",
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                        "storagePool": "SP:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Manual",
                "lun": 1,
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE4_VOLUME2_NAME,
                        "description": "useful description",
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                        "storagePool": "SP:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Manual",
                "lun": 2,
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts8_create_sp_from_spt_profile5 = {
    "type": "ServerProfileV10",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE5_NAME,
    "serverProfileTemplateUri": 'SPT:' + PROFILE5_NAME,
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
        "connections": [
            {
                "functionType": "FibreChannel",
                "id": 1,
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE5_VOLUME1_NAME,
                        "description": "useful description",
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STORESERV_STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts9_edit_spt_profile1 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "FibreChannel",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            },

        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description",
                        "size": 107374182400,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STORESERV_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description",
                        "size": 30000000000,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STORESERV_STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
}

ts9_edit_spt_profile2 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE2_VOLUME1_NAME,
                        "description": "Existing private volume used as framework",
                        "size": 2684354560,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts9_edit_spt_profile3 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid6DualParity",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts9_edit_spt_profile4 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE4_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA84_Storage_Pool"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE4_VOLUME1_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 107374182400,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Manual",
                "lun": 1,
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE4_VOLUME2_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME13,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts9_edit_spt_profile5 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE5_NAME,
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
        "connections": [
            {
                "functionType": "FibreChannel",
                "id": 1,
                "name": "Connection 1",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE5_VOLUME1_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 107374182400,
                        "provisioningType": "Thin",
                        "isShareable": True,
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STORESERV_STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts9_edit2_spt_profile1 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "FibreChannel",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            },

        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STORESERV_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL
                    },
                    "isPermanent": True,
                    "templateUri": 'SVT:' + STORESERV_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    },
}

ts9_edit2_spt_profile2 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE2_VOLUME1_NAME,
                        "description": "Existing private volume used as framework",
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts9_edit2_spt_profile3 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE3_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_SLPT_STORAGE_POOL_NETWORK,
            },
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA_Cluster_116"
        }],
        "volumeAttachments": [
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid6DualParity",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts9_edit2_spt_profile4 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE4_NAME,
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
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "Ethernet",
                "id": 2,
                "name": "Connection 2",
                "networkUri": STOREVIRTUAL_MLPT_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{
            "chapLevel": "MutualChap",
            "storageSystemUri": "SSYS:VSA84_Storage_Pool"
        }],
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE4_VOLUME1_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror3Way",
                        "storagePool": "SP:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "NotBootable",
                "lunType": "Manual",
                "lun": 1,
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    },
                ],
            },
            {
                "id": 2,
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE4_VOLUME2_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Manual",
                "lun": 2,
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}

ts9_edit2_spt_profile5 = {
    "type": "ServerProfileTemplateV6",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE5_NAME,
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
        "connections": [
            {
                "functionType": "FibreChannel",
                "id": 1,
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORESERV_STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE5_VOLUME1_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 10737418240,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STORESERV_STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
            },
        ]
    }
}


# EDIT VT TEST DATA

# Edit to increase volume size
edit_storevirtual_template1 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 107374182400,
            "minimum": 41943040000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Full",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid0None",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        },
        "templateVersion": {
            "default": "1.1",
            "description": "Version of the template",
            "meta": {
                "locked": True
            },
            "required": True,
            "title": "Template version",
            "type": "string"
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
    "description": ""
}

# Edit to change isShareable
edit_storeserv_template1 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "maximum": 17592186044416,
            "minimum": 2684354560,
            "required": True,
            "description": "The capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": True,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "A common provisioning group URI reference",
            "default": STORESERV_STORAGE_POOL
        },
        "snapshotPool": {
            "meta": {
                "locked": True,
                "semanticType": "device-snapshot-storage-pool"
            },
            "type": "string",
            "title": "Snapshot Pool",
            "format": "x-uri-reference",
            "default": STORESERV_STORAGE_POOL,
            "description": "A URI reference to the common provisioning group used to create snapshots"
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full",
            ],
            "meta": {
                "locked": True,
                "createOnly": True
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Thin",
            "description": "The provisioning type for the volume"
        },
        "templateVersion": {
            "default": "1.1",
            "description": "Version of the template",
            "meta": {
                "locked": True
            },
            "required": True,
            "title": "Template version",
            "type": "string"
        },
        "isDeduplicated": {
            "default": False,
            "description": "Enables or disables deduplication of the volume",
            "meta": {
                "locked": True
            },
            "title": "Is Deduplicated",
            "type": "boolean"
        },
    },
    "name": STORESERV_VOLUME_TEMPLATE_NAME1,
    "description": ""
}

# Edit to change dataProtectionLevel
edit_storevirtual_template15 = {
    "properties": {
        "name": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Volume name",
            "required": True,
            "maxLength": 100,
            "minLength": 1,
            "description": "A volume name between 1 and 100 characters"
        },
        "size": {
            "meta": {
                "locked": True,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 10737418240,
            "minimum": 4194304000,
            "required": True,
            "description": "Capacity of the volume in bytes"
        },
        "description": {
            "meta": {
                "locked": False
            },
            "type": "string",
            "title": "Description",
            "default": "",
            "maxLength": 2000,
            "minLength": 0,
            "description": "A description for the volume"
        },
        "isShareable": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Is Shareable",
            "default": False,
            "description": "The shareability of the volume"
        },
        "storagePool": {
            "meta": {
                "locked": False,
                "createOnly": True,
                "semanticType": "device-storage-pool"
            },
            "type": "string",
            "title": "Storage Pool",
            "format": "x-uri-reference",
            "required": True,
            "description": "StoragePoolURI the volume should be added to",
            "default": STOREVIRTUAL_SLPT_STORAGE_SYSTEM
        },
        "provisioningType": {
            "enum": [
                "Thin",
                "Full"
            ],
            "meta": {
                "locked": True,
                "createOnly": "True",
                "semanticType": "device-provisioningType"
            },
            "type": "string",
            "title": "Provisioning Type",
            "default": "Thin",
            "description": "The provisioning type for the volume"
        },
        "dataProtectionLevel": {
            "enum": [
                "NetworkRaid0None",
                "NetworkRaid5SingleParity",
                "NetworkRaid10Mirror2Way",
                "NetworkRaid10Mirror3Way",
                "NetworkRaid10Mirror4Way",
                "NetworkRaid6DualParity"
            ],
            "meta": {
                "locked": True,
                "semanticType": "device-dataProtectionLevel"
            },
            "type": "string",
            "title": "Data Protection Level",
            "default": "NetworkRaid0None",
            "required": True,
            "description": "Indicates the number and configuration of data copies in the Storage Pool"
        },
        "isAdaptiveOptimizationEnabled": {
            "meta": {
                "locked": True
            },
            "type": "boolean",
            "title": "Adaptive Optimization",
            "default": True,
            "description": ""
        },
        "templateVersion": {
            "default": "1.1",
            "description": "Version of the template",
            "meta": {
                "locked": True
            },
            "required": True,
            "title": "Template version",
            "type": "string"
        }
    },
    "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
    "description": ""
}

ts10_expected_spt_alerts = {
    "members": [
        {
            "type": "AlertResourceV3",
            "parentAlert": None,
            "childAlerts": [],
            "serviceEventSource": False,
            "serviceEventDetails": None,
            "resourceUri": "REGEX:\/rest\/server-profile-templates\/.*",
            "physicalResourceType": "server-profile-templates",
            "alertState": "Active",
            "associatedResource": {
                "resourceUri": "REGEX:\/rest\/server-profile-templates\/.*",
                "resourceCategory": "server-profile-templates",
                "resourceName": PROFILE3_NAME,
                "associationType": "HAS_A"
            },
            "severity": "Warning",
            "alertTypeID": "spt.VolumeValidationFailure",
            "healthCategory": "ServerProfileTemplate",
            "urgency": "Medium",
            "lifeCycle": False,
            "activityUri": None,
            "resourceID": "REGEX:.*",
            "associatedEventUris": [
                "REGEX:\/rest\/events\/.*"
            ],
            "assignedToUser": None,
            "changeLog": [],
            "clearedByUser": None,
            "clearedTime": None,
            "correctiveAction": "REGEX:Edit the volume attachments or modify their volume template {\"name\":\"" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15 + "\", \"uri\":\"\/rest\/storage-volume-templates\/.*\"} to correct the issues\.",
            "description": "REGEX:The following volume attachments are inconsistent with their volume template or invalid\. Creation of server profiles from this server profile template will fail until all volume attachment issues are corrected:\\n(\\u2022|\\u2023|\\u25E6|\\u2043|\\u2219) " + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15 + ":\\nUnable to set the field 'dataProtectionLevel' because it is locked by the template\.\\nSet the value of the field equal to the value specified for this field in the associated volume template and try again\.",
            "category": "alerts",
            "uri": "REGEX:\/rest\/alerts\/.*"
        },
        {
            "type": "AlertResourceV3",
            "parentAlert": None,
            "childAlerts": [],
            "serviceEventSource": False,
            "serviceEventDetails": None,
            "resourceUri": "REGEX:\/rest\/server-profile-templates\/.*",
            "physicalResourceType": "server-profile-templates",
            "alertState": "Active",
            "associatedResource": {
                "resourceUri": "REGEX:\/rest\/server-profile-templates\/.*",
                "resourceCategory": "server-profile-templates",
                "resourceName": PROFILE1_NAME,
                "associationType": "HAS_A"
            },
            "severity": "Warning",
            "alertTypeID": "spt.VolumeValidationFailure",
            "healthCategory": "ServerProfileTemplate",
            "urgency": "Medium",
            "lifeCycle": False,
            "activityUri": None,
            "resourceID": "REGEX:.*",
            "associatedEventUris": [
                "REGEX:\/rest\/events\/.*"
            ],
            "assignedToUser": None,
            "changeLog": [],
            "clearedByUser": None,
            "clearedTime": None,
            "correctiveAction": "REGEX:Edit the volume attachments or modify their volume template {\"name\":\"" + STORESERV_VOLUME_TEMPLATE_NAME1 + "\", \"uri\":\"\/rest\/storage-volume-templates\/.*\"} to correct the issues.",
            "description": "REGEX:The following volume attachments are inconsistent with their volume template or invalid\. Creation of server profiles from this server profile template will fail until all volume attachment issues are corrected:\\n.* " + STORESERV_VOLUME_TEMPLATE_NAME1 + ":\\nUnable to set the field 'isShareable' because it is locked by the template\.\\nSet the value of the field equal to the value specified for this field in the associated volume template and try again\.",
            "category": "alerts",
            "uri": "REGEX:\/rest\/alerts\/.*"
        },
        {
            "type": "AlertResourceV3",
            "parentAlert": None,
            "childAlerts": [],
            "serviceEventSource": False,
            "serviceEventDetails": None,
            "resourceUri": "REGEX:\/rest\/server-profile-templates\/.*",
            "physicalResourceType": "server-profile-templates",
            "alertState": "Active",
            "associatedResource": {
                "resourceUri": "REGEX:\/rest\/server-profile-templates\/.*",
                "resourceCategory": "server-profile-templates",
                "resourceName": PROFILE1_NAME,
                "associationType": "HAS_A"
            },
            "severity": "Warning",
            "alertTypeID": "spt.VolumeValidationFailure",
            "healthCategory": "ServerProfileTemplate",
            "urgency": "Medium",
            "lifeCycle": False,
            "activityUri": None,
            "resourceID": "REGEX:.*",
            "associatedEventUris": [
                "REGEX:\/rest\/events\/.*"
            ],
            "assignedToUser": None,
            "changeLog": [],
            "clearedByUser": None,
            "clearedTime": None,
            "correctiveAction": "REGEX:Edit the volume attachments or modify their volume template {\"name\":\"" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1 + "\", \"uri\":\"\/rest\/storage-volume-templates\/.*\"} to correct the issues\.",
            "description": "REGEX:The following volume attachments are inconsistent with their volume template or invalid\. Creation of server profiles from this server profile template will fail until all volume attachment issues are corrected:\\n.* " + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1 + ":\\nUnable to set the field 'size' because it is locked by the template\.\\nSet the value of the field equal to the value specified for this field in the associated volume template and try again\.",
            "category": "alerts",
            "uri": "REGEX:\/rest\/alerts\/.*"
        },
    ],
    "total": 3,
    "count": 3
}

ts10_expected_sp_alerts = {
    "members": [
        {
            "type": "AlertResourceV3",
            "parentAlert": None,
            "childAlerts": [],
            "serviceEventSource": False,
            "serviceEventDetails": None,
            "resourceUri": "REGEX:\/rest\/server-profiles\/.*",
            "physicalResourceType": "server-profiles",
            "alertState": "Active",
            "associatedResource": {
                "resourceUri": "REGEX:\/rest\/server-profiles\/.*",
                "resourceCategory": "server-profiles",
                "resourceName": PROFILE3_NAME,
                "associationType": "HAS_A"
            },
            "severity": "Warning",
            "alertTypeID": "profilemgr.SAN.VOLUME_INCONSISTENT_WITH_TEMPLATE",
            "healthCategory": "Storage",
            "urgency": "Immediate",
            "lifeCycle": False,
            "activityUri": None,
            "associatedEventUris": [
                "REGEX:\/rest\/events\/.*"
            ],
            "assignedToUser": None,
            "changeLog": [],
            "clearedByUser": None,
            "clearedTime": None,
            "correctiveAction": "Edit the volume or volume template to restore template consistency.",
            "description": "REGEX:Volume {\"name\":\"" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15 + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} is inconsistent with its volume template, {\"name\":\"" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15 + "\", \"uri\":\"\/rest\/storage-volume-templates\/.*\"}\.",
            "category": "alerts",
            "uri": "REGEX:\/rest\/alerts\/.*"
        },
        {
            "type": "AlertResourceV3",
            "parentAlert": None,
            "childAlerts": [],
            "serviceEventSource": False,
            "serviceEventDetails": None,
            "resourceUri": "REGEX:\/rest\/server-profiles\/.*",
            "physicalResourceType": "server-profiles",
            "alertState": "Active",
            "associatedResource": {
                "resourceUri": "REGEX:\/rest\/server-profiles\/.*",
                "resourceCategory": "server-profiles",
                "resourceName": PROFILE1_NAME,
                "associationType": "HAS_A"
            },
            "severity": "Warning",
            "alertTypeID": "profilemgr.SAN.VOLUME_INCONSISTENT_WITH_TEMPLATE",
            "healthCategory": "Storage",
            "urgency": "Immediate",
            "lifeCycle": False,
            "activityUri": None,
            "associatedEventUris": [
                "REGEX:\/rest\/events\/.*"
            ],
            "assignedToUser": None,
            "changeLog": [],
            "clearedByUser": None,
            "clearedTime": None,
            "correctiveAction": "Edit the volume or volume template to restore template consistency.",
            "description": "REGEX:Volume {\"name\":\"" + STORESERV_VOLUME_TEMPLATE_NAME1 + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} is inconsistent with its volume template\, {\"name\":\"" + STORESERV_VOLUME_TEMPLATE_NAME1 + "\", \"uri\":\"\/rest\/storage-volume-templates\/.*\"}\.",
            "category": "alerts",
            "uri": "REGEX:\/rest\/alerts\/.*"
        },
        {
            "type": "AlertResourceV3",
            "parentAlert": None,
            "childAlerts": [],
            "serviceEventSource": False,
            "serviceEventDetails": None,
            "resourceUri": "REGEX:\/rest\/server-profiles\/.*",
            "physicalResourceType": "server-profiles",
            "alertState": "Active",
            "associatedResource": {
                "resourceUri": "REGEX:\/rest\/server-profiles\/.*",
                "resourceCategory": "server-profiles",
                "resourceName": PROFILE1_NAME,
                "associationType": "HAS_A"
            },
            "severity": "Warning",
            "alertTypeID": "profilemgr.SAN.VOLUME_INCONSISTENT_WITH_TEMPLATE",
            "healthCategory": "Storage",
            "urgency": "Immediate",
            "lifeCycle": False,
            "activityUri": None,
            "associatedEventUris": [
                "REGEX:\/rest\/events\/.*"
            ],
            "assignedToUser": None,
            "changeLog": [],
            "clearedByUser": None,
            "clearedTime": None,
            "correctiveAction": "Edit the volume or volume template to restore template consistency.",
            "description": "REGEX:Volume {\"name\":\"" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1 + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} is inconsistent with its volume template, {\"name\":\"" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1 + "\", \"uri\":\"\/rest\/storage-volume-templates\/.*\"}\.",
            "category": "alerts",
            "uri": "REGEX:\/rest\/alerts\/."
        },
    ],
    "total": 3,
    "count": 3
}

ts10_expected_spt_alerts2 = {
    "members": [
        {
            "type": "AlertResourceV3",
            "parentAlert": None,
            "childAlerts": [],
            "serviceEventSource": False,
            "serviceEventDetails": None,
            "resourceUri": "REGEX:\/rest\/server-profile-templates\/.*",
            "physicalResourceType": "server-profile-templates",
            "alertState": "Active",
            "associatedResource": {
                "resourceUri": "REGEX:\/rest\/server-profile-templates\/.*",
                "resourceCategory": "server-profile-templates",
                "resourceName": PROFILE3_NAME,
                "associationType": "HAS_A"
            },
            "severity": "Warning",
            "eTag": "REGEX:.*",
            "created": "REGEX:.*",
            "modified": "REGEX:.*",
            "alertTypeID": "spt.VolumeValidationFailure",
            "healthCategory": "ServerProfileTemplate",
            "urgency": "Medium",
            "lifeCycle": False,
            "activityUri": None,
            "resourceID": "REGEX:.*",
            "associatedEventUris": [
                "REGEX:\/rest\/events\/.*"
            ],
            "assignedToUser": None,
            "changeLog": [],
            "clearedByUser": None,
            "clearedTime": None,
            "correctiveAction": "REGEX:Edit the volume attachments or modify their volume template {\"name\":\"" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15 + "\", \"uri\":\"\/rest\/storage-volume-templates\/.*\"} to correct the issues\.",
            "description": "REGEX:The following volume attachments are inconsistent with their volume template or invalid\. Creation of server profiles from this server profile template will fail until all volume attachment issues are corrected:\\n.* " + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15 + ":\\nUnable to set the field 'dataProtectionLevel' because it is locked by the template\.\\nSet the value of the field equal to the value specified for this field in the associated volume template and try again\.",
            "category": "alerts",
            "uri": "REGEX:\/rest\/alerts\/.*"
        },
        {
            "type": "AlertResourceV3",
            "parentAlert": None,
            "childAlerts": [],
            "serviceEventSource": False,
            "serviceEventDetails": None,
            "resourceUri": "REGEX:\/rest\/server-profile-templates\/.*",
            "physicalResourceType": "server-profile-templates",
            "alertState": "Active",
            "associatedResource": {
                "resourceUri": "REGEX:\/rest\/server-profile-templates\/.*",
                "resourceCategory": "server-profile-templates",
                "resourceName": PROFILE1_NAME,
                "associationType": "HAS_A"
            },
            "severity": "Warning",
            "eTag": "REGEX:.*",
            "created": "REGEX:.*",
            "modified": "REGEX:.*",
            "alertTypeID": "spt.VolumeValidationFailure",
            "healthCategory": "ServerProfileTemplate",
            "urgency": "Medium",
            "lifeCycle": False,
            "activityUri": None,
            "resourceID": "REGEX:.*",
            "associatedEventUris": [
                "REGEX:\/rest\/events\/.*"
            ],
            "assignedToUser": None,
            "changeLog": [],
            "clearedByUser": None,
            "clearedTime": None,
            "correctiveAction": "REGEX:Edit the volume attachments or modify their volume template {\"name\":\"" + STORESERV_VOLUME_TEMPLATE_NAME1 + "\", \"uri\":\"\/rest\/storage-volume-templates\/.*\"} to correct the issues.",
            "description": "REGEX:The following volume attachments are inconsistent with their volume template or invalid\. Creation of server profiles from this server profile template will fail until all volume attachment issues are corrected:\\n.* " + STORESERV_VOLUME_TEMPLATE_NAME1 + ":\\nUnable to set the field 'isShareable' because it is locked by the template\.\\nSet the value of the field equal to the value specified for this field in the associated volume template and try again\.",
            "category": "alerts",
            "uri": "REGEX:\/rest\/alerts\/.*"
        },
    ],
    "total": 2,
    "count": 2
}

ts10_expected_sp_alerts2 = {
    "members": [
        {
            "type": "AlertResourceV3",
            "parentAlert": None,
            "childAlerts": [],
            "serviceEventSource": False,
            "serviceEventDetails": None,
            "resourceUri": "REGEX:\/rest\/server-profiles\/.*",
            "physicalResourceType": "server-profiles",
            "alertState": "Active",
            "associatedResource": {
                "resourceUri": "REGEX:\/rest\/server-profiles\/.*",
                "resourceCategory": "server-profiles",
                "resourceName": PROFILE3_NAME,
                "associationType": "HAS_A"
            },
            "severity": "Warning",
            "alertTypeID": "profilemgr.SAN.VOLUME_INCONSISTENT_WITH_TEMPLATE",
            "healthCategory": "Storage",
            "urgency": "Immediate",
            "lifeCycle": False,
            "activityUri": None,
            "associatedEventUris": [
                "REGEX:\/rest\/events\/.*"
            ],
            "assignedToUser": None,
            "changeLog": [],
            "clearedByUser": None,
            "clearedTime": None,
            "correctiveAction": "Edit the volume or volume template to restore template consistency.",
            "description": "REGEX:Volume {\"name\":\"" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15 + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} is inconsistent with its volume template, {\"name\":\"" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15 + "\", \"uri\":\"\/rest\/storage-volume-templates\/.*\"}\.",
            "category": "alerts",
            "uri": "REGEX:\/rest\/alerts\/.*"
        },
        {
            "type": "AlertResourceV3",
            "parentAlert": None,
            "childAlerts": [],
            "serviceEventSource": False,
            "serviceEventDetails": None,
            "resourceUri": "REGEX:\/rest\/server-profiles\/.*",
            "physicalResourceType": "server-profiles",
            "alertState": "Active",
            "associatedResource": {
                "resourceUri": "REGEX:\/rest\/server-profiles\/.*",
                "resourceCategory": "server-profiles",
                "resourceName": PROFILE1_NAME,
                "associationType": "HAS_A"
            },
            "severity": "Warning",
            "alertTypeID": "profilemgr.SAN.VOLUME_INCONSISTENT_WITH_TEMPLATE",
            "healthCategory": "Storage",
            "urgency": "Immediate",
            "lifeCycle": False,
            "activityUri": None,
            "associatedEventUris": [
                "REGEX:\/rest\/events\/.*"
            ],
            "assignedToUser": None,
            "changeLog": [],
            "clearedByUser": None,
            "clearedTime": None,
            "correctiveAction": "Edit the volume or volume template to restore template consistency.",
            "description": "REGEX:Volume {\"name\":\"" + STORESERV_VOLUME_TEMPLATE_NAME1 + "\", \"uri\":\"\/rest\/storage-volumes\/.*\"} is inconsistent with its volume template\, {\"name\":\"" + STORESERV_VOLUME_TEMPLATE_NAME1 + "\", \"uri\":\"\/rest\/storage-volume-templates\/.*\"}\.",
            "category": "alerts",
            "uri": "REGEX:\/rest\/alerts\/.*"
        },
    ],
    "total": 2,
    "count": 2
}

ts10_expected_alerts_cleared = {
    "total": 0,
    "count": 0
}

create_volume_templates = [
    storevirtual_template1.copy(),
    storevirtual_template2.copy(),
    storevirtual_template3.copy(),
    storevirtual_template4.copy(),
    storevirtual_template5.copy(),
    storevirtual_template6.copy(),
    storevirtual_template7.copy(),
    storevirtual_template8.copy(),
    storevirtual_template9.copy(),
    storevirtual_template10.copy(),
    storevirtual_template11.copy(),
    storevirtual_template12.copy(),
    storevirtual_template13.copy(),
    storevirtual_template14.copy(),
    storevirtual_template15.copy(),
    storevirtual_template16.copy(),
    storevirtual_template17.copy(),
    storevirtual_template18.copy(),
    storevirtual_template19.copy(),
    storevirtual_template20.copy(),
    storevirtual_template21.copy(),
    storevirtual_template22.copy(),
    storevirtual_template23.copy(),
    storevirtual_template24.copy(),
    storeserv_template1.copy(),
    storeserv_template2.copy(),
    storeserv_template3.copy(),
    storeserv_template4.copy(),
]

ts0_create_spt = [
    ts0_create_server_profile_template1.copy(),
    ts0_create_server_profile_template2.copy(),
    ts0_create_server_profile_template3.copy(),
    ts0_create_server_profile_template4.copy(),
    ts0_create_server_profile_template5.copy(),
]

ts0_edit_spt = [
    ts0_edit_server_profile_template1.copy(),
    ts0_edit_server_profile_template2.copy(),
    ts0_edit_server_profile_template3.copy(),
    ts0_edit_server_profile_template4.copy(),
    ts0_edit_server_profile_template5.copy(),
]

ts1_create_spt = [
    ts1_create_server_profile_template1.copy(),
    ts1_create_server_profile_template2.copy(),
    ts1_create_server_profile_template3.copy(),
    ts1_create_server_profile_template4.copy(),
    ts1_create_server_profile_template5.copy(),
]

ts1_verify_create_spt_v600 = [
    ts1_verify_create_server_profile_template1_v600.copy(),
    ts0_verify_create_server_profile_template2.copy(),
    ts0_verify_create_server_profile_template3.copy(),
    ts0_verify_create_server_profile_template4.copy(),
    ts0_verify_create_server_profile_template5.copy(),
]

ts1_edit_spt = [
    ts1_edit_server_profile_template1.copy(),
    ts1_edit_server_profile_template2.copy(),
    ts1_edit_server_profile_template3.copy(),
    ts1_edit_server_profile_template4.copy(),
    ts1_edit_server_profile_template5.copy(),
]

ts1_verify_edit_spt_v600 = [
    ts1_verify_edit_server_profile_template1_v600.copy(),
    ts0_edit_server_profile_template2.copy(),
    ts1_verify_edit_server_profile_template3_v600.copy(),
    ts0_edit_server_profile_template4.copy(),
    ts0_edit_server_profile_template5.copy(),
]

ts2_verify_edit_spt_v600 = [
    ts2_verify_edit_server_profile_template1.copy(),
    ts0_edit_server_profile_template2.copy(),
    ts1_verify_edit_server_profile_template3_v600.copy(),
    ts0_edit_server_profile_template4.copy(),
    ts0_edit_server_profile_template5.copy(),
]

negative_create_profile_template_tasks = [
    # Volume actually gets called 'null'
    # {
    #     'keyword': 'Add Server Profile Template',
    #     'argument': negative_spt1.copy(),
    #     'taskState': 'Error',
    #     'errorMessage': 'NULL_VOLUME_NAME'},
    # Volume actually gets called '3'
    # {
    #     'keyword': 'Add Server Profile Template',
    #     'argument': negative_spt2.copy(),
    #     'taskState': 'Error',
    #     'errorMessage': 'INVALID_VOLUME_NAME'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt3.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_DESCRIPTION'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt4.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_SIZE'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt5.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_SIZE'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt6.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_SIZE_TOO_LARGE'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt7.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_DATA_PROTECTION_LEVEL_LOCKED'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt8.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_DATA_PROTECTION_LEVEL'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt9.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_DATA_PROTECTION_LEVEL'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt10.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_SHARABLE_MUST_BE_TRUE_OR_FALSE'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt11.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_SHARABLE'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt12.copy(),
        'taskState': 'Error',
        'errorMessage': 'ShareablePendingVolumeAttachmentNotSupported'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt13.copy(),
        'taskState': 'Error',
        'errorMessage': 'ShareablePendingVolumeAttachmentNotSupported'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt14.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_PROVISIONING_TYPE_LOCKED'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt15.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_PROVISIONING_TYPE'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt16.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_PROVISIONING_TYPE'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt17.copy(),
        'taskState': 'Error',
        'errorMessage': 'MISSING_REQUIRED_FIELD_VOLUME'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt19.copy(),
        'taskState': 'Error',
        'errorMessage': 'MISSING_REQUIRED_FIELD_VOLUME'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt20.copy(),
        'taskState': 'Error',
        'errorMessage': 'STORAGE_POOL_DOES_NOT_MATCH_TEMPLATE'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt21.copy(),
        'taskState': 'Error',
        'errorMessage': 'Managed_Volume_No_Bootable_Connections'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt22.copy(),
        'taskState': 'Error',
        'errorMessage': 'DuplicateBootVolumePriority'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt23.copy(),
        'taskState': 'Error',
        'status_code': 400,
        'errorMessage': 'UNRECOGNIZED_JSON_FIELD'},
]

ts4_all_templates = [
    negative_spt1.copy(),
    negative_spt2.copy(),
    negative_spt3.copy(),
    negative_spt4.copy(),
    negative_spt5.copy(),
    negative_spt6.copy(),
    negative_spt7.copy(),
    negative_spt8.copy(),
    negative_spt9.copy(),
    negative_spt10.copy(),
    negative_spt11.copy(),
    negative_spt12.copy(),
    negative_spt13.copy(),
    negative_spt14.copy(),
    negative_spt15.copy(),
    negative_spt16.copy(),
    negative_spt17.copy(),
    negative_spt18.copy(),
    negative_spt19.copy(),
    negative_spt20.copy(),
    negative_spt21.copy(),
    negative_spt22.copy(),
    negative_spt23.copy(),
]

create_negative_edit_profile_templates = [
    create_negative_edit_profile_template.copy(),
]

negative_edit_profile_template_tasks = [
    # Volume actually gets called 'null'
    # {
    #     'keyword': 'Edit Server Profile Template',
    #     'argument': negative_edit_spt1.copy(),
    #     'taskState': 'Error',
    #     'errorMessage': 'NULL_VOLUME_NAME'},
    # Volume actually gets called '3'
    # {
    #     'keyword': 'Edit Server Profile Template',
    #     'argument': negative_edit_spt2.copy(),
    #     'taskState': 'Error',
    #     'errorMessage': 'INVALID_VOLUME_NAME'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt3.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_DESCRIPTION'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt4.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_SIZE'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt5.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_SIZE'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt6.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_SIZE_TOO_LARGE'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt7.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_DATA_PROTECTION_LEVEL_LOCKED'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt8.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_DATA_PROTECTION_LEVEL'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt9.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_DATA_PROTECTION_LEVEL'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt10.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_SHARABLE_MUST_BE_TRUE_OR_FALSE'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt11.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_SHARABLE'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt12.copy(),
        'taskState': 'Error',
        'errorMessage': 'ShareablePendingVolumeAttachmentNotSupported'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt13.copy(),
        'taskState': 'Error',
        'errorMessage': 'ShareablePendingVolumeAttachmentNotSupported'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt14.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_PROVISIONING_TYPE_LOCKED'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt15.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_PROVISIONING_TYPE'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt16.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_PROVISIONING_TYPE'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt17.copy(),
        'taskState': 'Error',
        'errorMessage': 'MISSING_REQUIRED_FIELD_VOLUME'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt19.copy(),
        'taskState': 'Error',
        'errorMessage': 'MISSING_REQUIRED_FIELD_VOLUME'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt20.copy(),
        'taskState': 'Error',
        'errorMessage': 'STORAGE_POOL_DOES_NOT_MATCH_TEMPLATE'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt21.copy(),
        'taskState': 'Error',
        'errorMessage': 'Managed_Volume_No_Bootable_Connections'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt22.copy(),
        'taskState': 'Error',
        'errorMessage': 'DuplicateBootVolumePriority'},
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_edit_spt23.copy(),
        'taskState': 'Error',
        'errorMessage': 'UNRECOGNIZED_JSON_FIELD'},
]

remove_negative_edit_profile_template = [
    create_negative_edit_profile_template.copy(),
]

ts6_create_spt = [
    ts6_create_spt_profile1.copy(),
    ts6_create_spt_profile2.copy(),
    ts6_create_spt_profile3.copy(),
    ts6_create_spt_profile4.copy(),
    ts6_create_spt_profile5.copy(),
]

ts6_create_sp_from_spt_v600 = [
    ts6_create_sp_from_spt_profile1.copy(),
    ts6_create_sp_from_spt_profile2.copy(),
    ts6_create_sp_from_spt_profile3.copy(),
    ts6_create_sp_from_spt_profile4.copy(),
    ts6_create_sp_from_spt_profile5.copy(),
]

ts6_verify_sp_from_spt_v600 = [
    ts6_verify_create_sp_from_spt_profile1.copy(),
    ts6_verify_create_sp_from_spt_profile2.copy(),
    ts6_verify_create_sp_from_spt_profile3.copy(),
    ts6_verify_create_sp_from_spt_profile4.copy(),
    ts6_verify_create_sp_from_spt_profile5.copy(),
]

ts6_verify_volumes = [
    ts6_verify_volume1_profile1.copy(),
    ts6_verify_volume2_profile1.copy(),
    ts6_verify_volume1_profile2.copy(),
    ts6_verify_volume2_profile2.copy(),
    ts6_verify_volume2_profile3.copy(),
    ts6_verify_volume1_profile4.copy(),
    ts6_verify_volume2_profile4.copy(),
    ts6_verify_volume1_profile5.copy(),
]

sp_compliance = [
    profile1_compliance.copy(),
    profile2_compliance.copy(),
    profile3_compliance.copy(),
    profile4_compliance.copy(),
    profile5_compliance.copy(),
]

ts6_delete_new_volumes = [
    {"properties": {"name": PROFILE2_VOLUME1_NAME}},
    {"properties": {"name": STORESERV_VOLUME_TEMPLATE_NAME1}},
]

ts7_create_spt = [
    ts7_create_spt_profile1.copy(),
    ts7_create_spt_profile2.copy(),
    ts7_create_spt_profile3.copy(),
    ts7_create_spt_profile4.copy(),
    ts7_create_spt_profile5.copy(),
]

ts7_create_sp_from_spt_v500 = [
    ts7_create_sp_from_spt_profile1.copy(),
    ts7_create_sp_from_spt_profile2.copy(),
    ts7_create_sp_from_spt_profile3.copy(),
    ts7_create_sp_from_spt_profile4.copy(),
    ts7_create_sp_from_spt_profile5.copy(),
]

ts7_verify_sp_from_spt_v500 = [
    ts7_verify_create_sp_from_spt_profile1.copy(),
    ts7_verify_create_sp_from_spt_profile2.copy(),
    ts7_verify_create_sp_from_spt_profile3.copy(),
    ts7_verify_create_sp_from_spt_profile4.copy(),
    ts7_verify_create_sp_from_spt_profile5.copy(),
]

ts7_verify_volumes = [
    ts7_verify_volume1_profile1.copy(),
    ts7_verify_volume2_profile1.copy(),
    ts7_verify_volume1_profile2.copy(),
    ts7_verify_volume2_profile2.copy(),
    ts7_verify_volume2_profile3.copy(),
    ts7_verify_volume1_profile4.copy(),
    ts7_verify_volume2_profile4.copy(),
    ts7_verify_volume1_profile5.copy(),
]

ts8_create_sp_non_compliant = [
    ts8_create_sp_from_spt_profile1.copy(),
    ts8_create_sp_from_spt_profile2.copy(),
    ts8_create_sp_from_spt_profile3.copy(),
    ts8_create_sp_from_spt_profile4.copy(),
    ts8_create_sp_from_spt_profile5.copy(),
]

sp_non_compliant = [
    profile1_sp_non_compliant.copy(),
    profile2_sp_non_compliant.copy(),
    profile3_sp_non_compliant.copy(),
    profile4_sp_non_compliant.copy(),
    profile5_sp_non_compliant.copy(),
]

ts8_delete_new_volumes = [
    {"properties": {"name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1}},
    {"properties": {"name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15}},
    {"properties": {"name": PROFILE4_VOLUME1_NAME}},
    {"properties": {"name": PROFILE4_VOLUME2_NAME}},
    {"properties": {"name": PROFILE5_VOLUME1_NAME}},
]

ts9_edit_spt_non_compliant = [
    ts9_edit_spt_profile1.copy(),
    ts9_edit_spt_profile2.copy(),
    ts9_edit_spt_profile3.copy(),
    ts9_edit_spt_profile4.copy(),
    ts9_edit_spt_profile5.copy(),
]

spt_non_compliant = [
    profile1_spt_non_compliant.copy(),
    profile2_spt_non_compliant.copy(),
    profile3_spt_non_compliant.copy(),
    profile4_spt_non_compliant.copy(),
    profile5_spt_non_compliant.copy(),
]

ts9_edit_spt_compliant = [
    ts9_edit2_spt_profile1.copy(),
    ts9_edit2_spt_profile2.copy(),
    ts9_edit2_spt_profile3.copy(),
    ts9_edit2_spt_profile4.copy(),
    ts9_edit2_spt_profile5.copy(),
]

ts10_edit_volume_template = [
    edit_storevirtual_template1.copy(),
    edit_storeserv_template1.copy(),
    edit_storevirtual_template15.copy(),
]

ts10_verify_spt_warning = [
    ts6_create_spt_profile1.copy(),
    ts6_create_spt_profile3.copy(),
]

ts10_verify_sp_warning = [
    ts6_verify_create_sp_from_spt_profile1.copy(),
    ts6_verify_create_sp_from_spt_profile3.copy(),
]

ts10_edit2_volume_template = [
    storevirtual_template1_copy.copy(),
]

ts10_edit3_volume_template = [
    storeserv_template1_copy.copy(),
    storevirtual_template15_copy.copy(),
]

all_new_volumes = [
    {"properties": {"name": PROFILE2_VOLUME1_NAME}},
    {"properties": {"name": STORESERV_VOLUME_TEMPLATE_NAME1}},
    {"properties": {"name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1}},
    {"properties": {"name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15}},
    {"properties": {"name": PROFILE4_VOLUME1_NAME}},
    {"properties": {"name": PROFILE4_VOLUME2_NAME}},
    {"properties": {"name": PROFILE5_VOLUME1_NAME}},
]

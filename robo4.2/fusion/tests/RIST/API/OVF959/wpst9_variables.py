admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

EG_NAME = 'EG1'

# Enclosures
ENC1 = 'wpst9'
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
# Server Hardware Types
SERVER_HARDWARE_TYPE1 = 'BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class'

STOREVIRTUAL_SLPT_STORAGE_SYSTEM = 'VSA_Cluster_116'
STOREVIRTUAL_MLPT_STORAGE_SYSTEM = 'VSA84_Storage_Pool'
STORESERV_STORAGE_SYSTEM = 'wpst3par-7200-5-srv'
STORESERV_STORAGE_POOL = 'FC_wpst9_r5'

STOREVIRTUAL_VOLUME_TEMPLATE_NAME1 = 'OVF959-StoreVirtual-RAID-0-Full-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME2 = 'OVF959-StoreVirtual-RAID-5-Full-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME3 = 'OVF959-StoreVirtual-RAID-6-Full-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME4 = 'OVF959-StoreVirtual-RAID-10-Full-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME5 = 'OVF959-StoreVirtual-RAID-10+1-Full-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME6 = 'OVF959-StoreVirtual-RAID-10+2-Full-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME7 = 'OVF959-StoreVirtual-RAID-0-Full-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME8 = 'OVF959-StoreVirtual-RAID-5-Full-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME9 = 'OVF959-StoreVirtual-RAID-6-Full-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME10 = 'OVF959-StoreVirtual-RAID-10-Full-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME11 = 'OVF959-StoreVirtual-RAID-10_1-Full-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME12 = 'OVF959-StoreVirtual-RAID-10_2-Full-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME13 = 'OVF959-StoreVirtual-RAID-0-Thin-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME14 = 'OVF959-StoreVirtual-RAID-5-Thin-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME15 = 'OVF959-StoreVirtual-RAID-6-Thin-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME16 = 'OVF959-StoreVirtual-RAID-10-Thin-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME17 = 'OVF959-StoreVirtual-RAID-10_1-Thin-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME18 = 'OVF959-StoreVirtual-RAID-10_2-Thin-Private'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME19 = 'OVF959-StoreVirtual-RAID-0-Thin-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME20 = 'OVF959-StoreVirtual-RAID-5-Thin-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME21 = 'OVF959-StoreVirtual-RAID-6-Thin-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME22 = 'OVF959-StoreVirtual-RAID-10-Thin-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME23 = 'OVF959-StoreVirtual-RAID-10_1-Thin-Shared'
STOREVIRTUAL_VOLUME_TEMPLATE_NAME24 = 'OVF959-StoreVirtual-RAID-10_2-Thin-Shared'
STORESERV_VOLUME_TEMPLATE_NAME1 = 'OVF959-StoreServ-Thin-Private'
STORESERV_VOLUME_TEMPLATE_NAME2 = 'OVF959-StoreServ-Full-Private'
STORESERV_VOLUME_TEMPLATE_NAME3 = 'OVF959-StoreServ-Thin-Shared'
STORESERV_VOLUME_TEMPLATE_NAME4 = 'OVF959-StoreServ-Full-Shared'

STOREVIRTUAL_EXISTING_SHARED_VOLUME1 = "dhcp-shared-volume1"
STOREVIRTUAL_EXISTING_PRIVATE_VOLUME1 = "wpst9-bay1-dhcp-managed-volume"
STOREVIRTUAL_EXISTING_PRIVATE_VOLUME2 = "wpst9-bay5-dhcp-managed-volume"


DHCP_BOOT_TARGET_IP = "192.168.21.59"
INITIATOR_GATEWAY = "192.168.0.1"
INITIATOR_SUBNET_MASK = "255.255.192.0"

STOREVIRTUAL_STORAGE_POOL_NETWORK = 'ETH:network-untagged'
STORESERV_STORAGE_POOL_NETWORK = 'FC:DA1'

# Profiles
PROFILE1_NAME = 'OVF959-CGW-Profile1'
PROFILE2_NAME = 'OVF959-CGW-Profile2'
PROFILE3_NAME = 'OVF959-CGW-Profile3'
PROFILE3_VOLUME1_NAME = 'OVF959-CGW-Profile3-Private-Thin-RAID-5'
PROFILE4_NAME = 'OVF959-CGW-Profile4'
PROFILE4_VOLUME1_NAME = 'OVF959-CGW-Profile4-StoreVirtual-MLPT-Private-Thin-RAID-10-3way'
PROFILE4_VOLUME2_NAME = 'OVF959-CGW-Profile4-StoreVirtual-MLPT-Shared-Full-RAID-0'
PROFILE5_NAME = 'OVF959-CGW-Profile5'
PROFILE5_VOLUME1_NAME = 'OVF959-StoreServ-Full-Private'

existing_volumes = [
    {
        "storageSystemUri": STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
        "name": STOREVIRTUAL_EXISTING_PRIVATE_VOLUME1,
        "deviceVolumeName": STOREVIRTUAL_EXISTING_PRIVATE_VOLUME1,
        "isShareable": False,
    },
    {
        "storageSystemUri": STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
        "name": STOREVIRTUAL_EXISTING_PRIVATE_VOLUME2,
        "deviceVolumeName": STOREVIRTUAL_EXISTING_PRIVATE_VOLUME2,
        "isShareable": False,
    },
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "minimum": 4194304,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "maximum": 17592186044416,
            "minimum": 268435456,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "maximum": 17592186044416,
            "minimum": 268435456,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "maximum": 17592186044416,
            "minimum": 268435456,
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
                "locked": False
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
                "locked": False,
                "semanticType": "capacity"
            },
            "type": "integer",
            "title": "Capacity",
            "default": 1073741824,
            "maximum": 17592186044416,
            "minimum": 268435456,
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
                "locked": False
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


# TS0 CREATE SERVER PROFILES WITH V600 API

# one volume using templateUri:STOREVIRTUAL_VOLUME_TEMPLATE_NAME1
ts0_create_server_profile1 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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

# Existing StoreVirtual private volume
ts0_create_server_profile2 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_PRIVATE_VOLUME1,
                "volume": None,
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
ts0_create_server_profile3 = {
    "type": "ServerProfileV9",
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
        "connectionSettings": {
            "connections": [
                {
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
                    "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
                }
            ]
        }
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
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid5SingleParity",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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
ts0_create_server_profile4 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror3Way",
                        "storagePool": "SP:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                },
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
ts0_create_server_profile5 = {
    "type": "ServerProfileV9",
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
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STORESERV_STORAGE_POOL,
                },
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


# TS0 EDIT SERVER PROFILES WITH V600 API

# Add a shared StoreServ volume
ts0_edit_server_profile1 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
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
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STORESERV_VOLUME_TEMPLATE_NAME1,
                        "description": "useful description",
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL
                    },
                    "isPermanent": True,
                    "templateUri": 'SVT:' + STORESERV_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "isBootVolume": False,
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

# Add an existing shared StoreVirtual volume
ts0_edit_server_profile2 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_PRIVATE_VOLUME1,
                "volume": None,
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
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": False,
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

# remove volume 1 and add a bootable StoreVirtual private volume from template
ts0_edit_server_profile3 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            },
        ]
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
                        "description": "",
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid6DualParity",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                },
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
ts0_edit_server_profile4 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + PROFILE4_VOLUME1_NAME,
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "isBootVolume": False,
                "lunType": "Manual",
                "lun": 1,
                "storagePaths": [],
            },
            {
                "id": 2,
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": PROFILE4_VOLUME2_NAME,
                        "description": "Private volume from ROOT template",
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                },
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
ts0_edit_server_profile5 = {
    "type": "ServerProfileV9",
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
        "connections": []
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


# TS0 VERIFY CREATE SERVER PROFILES WITH V600 API

# one volume using templateUri:STOREVIRTUAL_VOLUME_TEMPLATE_NAME1
ts0_verify_create_server_profile1 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                "volume": None,
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

# Existing StoreVirtual Private volume
ts0_verify_create_server_profile2 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_PRIVATE_VOLUME1,
                "volume": None,
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
ts0_verify_create_server_profile3 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + PROFILE3_VOLUME1_NAME,
                "volume": None,
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
ts0_verify_create_server_profile4 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + PROFILE4_VOLUME1_NAME,
                "volume": None,
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

# StoreServ private volume from Root template
ts0_verify_create_server_profile5 = {
    "type": "ServerProfileV9",
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
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + PROFILE5_VOLUME1_NAME,
                "volume": None,
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


# TS0 VERIFY EDIT SERVER PROFILES WITH V600 API

# Add a shared StoreServ volume
ts0_verify_edit_server_profile1 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                "volume": None,
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
                "volumeUri": "v:" + STORESERV_VOLUME_TEMPLATE_NAME1,
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "isBootVolume": False,
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

# Add an existing shared StoreVirtual volume
ts0_verify_edit_server_profile2 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_PRIVATE_VOLUME1,
                "volume": None,
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
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": False,
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

# remove volume 1 and add a bootable StoreVirtual private volume from template
ts0_verify_edit_server_profile3 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            },
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 2,
                "volumeUri": "v:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                "volume": None,
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
ts0_verify_edit_server_profile4 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + PROFILE4_VOLUME1_NAME,
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "isBootVolume": False,
                "lunType": "Manual",
                "lun": 1,
                "storagePaths": [],
            },
            {
                "id": 2,
                "volumeUri": "v:" + PROFILE4_VOLUME2_NAME,
                "volume": None,
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
ts0_verify_edit_server_profile5 = {
    "type": "ServerProfileV9",
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
        "connections": []
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


# TS0 VERIFY VOLUMES AFTER CREATE

ts0_verify_volume1_create_server_profile1 = {
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
    "provisionedCapacity": "1073741824",
    "provisioningType": "Full",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV6",
    "uri": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
    "volumeTemplateUri": "SVT:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1
}

ts0_verify_volume1_create_server_profile2 = {
    "category": "storage-volumes",
    "description": "",
    "deviceSpecificAttributes": {
        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
        "isAdaptiveOptimizationEnabled": True,
    },
    "deviceVolumeName": STOREVIRTUAL_EXISTING_PRIVATE_VOLUME1,
    "isPermanent": True,
    "isShareable": False,
    "name": STOREVIRTUAL_EXISTING_PRIVATE_VOLUME1,
    "provisionedCapacity": "21474836480",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV6",
    "uri": STOREVIRTUAL_EXISTING_PRIVATE_VOLUME1,
    "volumeTemplateUri": None,
}

ts0_verify_volume1_create_server_profile3 = {
    "category": "storage-volumes",
    "description": "Private volume from ROOT template",
    "deviceSpecificAttributes": {
        "dataProtectionLevel": "NetworkRaid5SingleParity",
        "isAdaptiveOptimizationEnabled": True,
    },
    "deviceVolumeName": PROFILE3_VOLUME1_NAME,
    "isPermanent": True,
    "isShareable": False,
    "name": PROFILE3_VOLUME1_NAME,
    "provisionedCapacity": "1073741824",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV6",
    "uri": PROFILE3_VOLUME1_NAME,
    "volumeTemplateUri": None,
}

ts0_verify_volume1_create_server_profile4 = {
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
    "provisionedCapacity": "1073741824",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV6",
    "uri": PROFILE4_VOLUME1_NAME,
    "volumeTemplateUri": None,
}

ts0_verify_volume1_create_server_profile5 = {
    "category": "storage-volumes",
    "description": "Private volume from ROOT template",
    "deviceVolumeName": PROFILE5_VOLUME1_NAME,
    "isPermanent": False,
    "isShareable": False,
    "name": PROFILE5_VOLUME1_NAME,
    "provisionedCapacity": "1073741824",
    "provisioningType": "Full",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STORESERV_STORAGE_POOL,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV6",
    "uri": PROFILE5_VOLUME1_NAME,
    "volumeTemplateUri": None,
}


# TS0 VERIFY VOLUMES AFTER EDIT

ts0_verify_volume2_edit_server_profile1 = {
    "category": "storage-volumes",
    "description": "useful description",
    "deviceVolumeName": STORESERV_VOLUME_TEMPLATE_NAME1,
    "isPermanent": True,
    "isShareable": False,
    "name": STORESERV_VOLUME_TEMPLATE_NAME1,
    "provisionedCapacity": "1073741824",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STORESERV_STORAGE_POOL,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV6",
    "uri": STORESERV_VOLUME_TEMPLATE_NAME1,
    "volumeTemplateUri": "SVT:" + STORESERV_VOLUME_TEMPLATE_NAME1
}

ts0_verify_volume2_edit_server_profile2 = {
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
    "type": "StorageVolumeV6",
    "uri": STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
    "volumeTemplateUri": None,
}

ts0_verify_volume2_edit_server_profile3 = {
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
    "provisionedCapacity": "1073741824",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV6",
    "uri": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
    "volumeTemplateUri": "SVT:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
}

ts0_verify_volume2_edit_server_profile4 = {
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
    "provisionedCapacity": "1073741824",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV6",
    "uri": PROFILE4_VOLUME2_NAME,
    "volumeTemplateUri": None,
}


# TS1 CREATE SERVER PROFILES WITH V500 API

# one volume using templateUri:STOREVIRTUAL_VOLUME_TEMPLATE_NAME1
ts1_create_server_profile1 = {
    "type": "ServerProfileV7",
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
    "connections": [
        {
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
            "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
        }
    ],
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
                "volumeProvisionedCapacityBytes": "1073741824",
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
ts1_create_server_profile2 = {
    "type": "ServerProfileV7",
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
    "connections": [
        {
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
            "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_PRIVATE_VOLUME1,
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

# StoreVirtual private volume from Root template
ts1_create_server_profile3 = {
    "type": "ServerProfileV7",
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
    "connections": [
        {
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
            "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
        }
    ],
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
                "volumeProvisionedCapacityBytes": "1073741824",
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
ts1_create_server_profile4 = {
    "type": "ServerProfileV7",
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
    "connections": [
        {
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
            "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
        }
    ],
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
                "volumeProvisionedCapacityBytes": "1073741824",
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
ts1_create_server_profile5 = {
    "type": "ServerProfileV7",
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
                "volumeUri": None,
                "volumeName": PROFILE5_VOLUME1_NAME,
                "volumeDescription": "Private volume from ROOT template",
                "volumeStoragePoolUri": "SPOOL:" + STORESERV_STORAGE_POOL,
                "volumeProvisionedCapacityBytes": "1073741824",
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


# TS1 EDIT SERVER PROFILES WITH V500 API

# Add a shared StoreServ volume
ts1_edit_server_profile1 = {
    "type": "ServerProfileV7",
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
    "connections": [
        {
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
            "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                "isBootVolume": True,
                "lunType": "Auto",
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
                "volumeProvisionedCapacityBytes": "1073741824",
                "volumeProvisionType": "Thin",
                "volumeShareable": False,
                "volumeStoragePoolUri": "SPOOL:" + STORESERV_STORAGE_POOL,
                "permanent": True,
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "isBootVolume": False,
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

# Add an existing shared StoreVirtual volume
ts1_edit_server_profile2 = {
    "type": "ServerProfileV7",
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
    "connections": [
        {
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
            "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_PRIVATE_VOLUME1,
                "volumeStoragePoolUri": "SPOOL:" + STORESERV_STORAGE_POOL,
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
                "volumeStoragePoolUri": "SPOOL:" + STORESERV_STORAGE_POOL,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": False,
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

# remove volume 1 and add a bootable StoreVirtual private volume from template
ts1_edit_server_profile3 = {
    "type": "ServerProfileV7",
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
    "connections": [
        {
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
            "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
        },
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 2,
                "volumeUri": None,
                "volumeName": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
                "dataProtectionLevel": "NetworkRaid6DualParity",
                "volumeProvisionedCapacityBytes": "1073741824",
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
ts1_edit_server_profile4 = {
    "type": "ServerProfileV7",
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
    "connections": [
        {
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
            "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + PROFILE4_VOLUME1_NAME,
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "isBootVolume": False,
                "lunType": "Manual",
                "lun": 1,
                "storagePaths": [],
            },
            {
                "id": 2,
                "volumeUri": None,
                "volumeName": PROFILE4_VOLUME2_NAME,
                "volumeDescription": "Private volume from ROOT template",
                "dataProtectionLevel": "NetworkRaid0None",
                "volumeProvisionedCapacityBytes": "1073741824",
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
ts1_edit_server_profile5 = {
    "type": "ServerProfileV7",
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
    "connections": [],
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}


# TS0 VERIFY CREATE SERVER PROFILES WITH V500 API

# one volume using templateUri:STOREVIRTUAL_VOLUME_TEMPLATE_NAME1
ts1_verify_create_server_profile1 = {
    "type": "ServerProfileV7",
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
    "connections": [
        {
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
            "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
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
                "permanent": False,
            },
        ]
    }
}

# Existing StoreVirtual private volume
ts1_verify_create_server_profile2 = {
    "type": "ServerProfileV7",
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
    "connections": [
        {
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
            "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_PRIVATE_VOLUME1,
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

# StoreVirtual private volume from Root template
ts1_verify_create_server_profile3 = {
    "type": "ServerProfileV7",
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
    "connections": [
        {
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
            "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + PROFILE3_VOLUME1_NAME,
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

# StoreVirtual MLPT private volume from Root template
ts1_verify_create_server_profile4 = {
    "type": "ServerProfileV7",
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
    "connections": [
        {
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
            "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + PROFILE4_VOLUME1_NAME,
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
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

# StoreServ private volume from Root template
ts1_verify_create_server_profile5 = {
    "type": "ServerProfileV7",
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
                "volumeUri": "v:" + PROFILE5_VOLUME1_NAME,
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


# TS0 VERIFY EDIT SERVER PROFILES WITH V500 API

# one volume using templateUri:STOREVIRTUAL_VOLUME_TEMPLATE_NAME1
ts1_verify_edit_server_profile1 = {
    "type": "ServerProfileV7",
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
    "connections": [
        {
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
            "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
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
                "permanent": False,
            },
            {
                "id": 2,
                "volumeUri": "v:" + STORESERV_VOLUME_TEMPLATE_NAME1,
                "volumeStoragePoolUri": "SPOOL:" + STORESERV_STORAGE_POOL,
                "volumeStorageSystemUri": "SSYS:" + STORESERV_STORAGE_SYSTEM,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [],
            },
        ]
    }
}

# add an existing shared StoreVirtual volume
ts1_verify_edit_server_profile2 = {
    "type": "ServerProfileV7",
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
    "connections": [
        {
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
            "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_PRIVATE_VOLUME1,
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
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_SHARED_VOLUME1,
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [],
            },
        ]
    }
}

# remove volume 1 and add a bootable StoreVirtual private volume from template
ts1_verify_edit_server_profile3 = {
    "type": "ServerProfileV7",
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
    "connections": [
        {
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
            "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
        },
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 2,
                "volumeUri": "v:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
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
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# add a StoreVirtual MLPT private volume from Root template and disable volume1 from being bootable
ts1_verify_edit_server_profile4 = {
    "type": "ServerProfileV7",
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
    "connections": [
        {
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
            "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": "v:" + PROFILE4_VOLUME1_NAME,
                "volumeStoragePoolUri": "SPOOL:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_MLPT_STORAGE_SYSTEM,
                "isBootVolume": False,
                "lunType": "Manual",
                "lun": 1,
                "storagePaths": [],
            },
            {
                "id": 2,
                "volumeUri": "v:" + PROFILE4_VOLUME2_NAME,
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

# remove the bootable volume and the connection
ts1_verify_edit_server_profile5 = {
    "type": "ServerProfileV7",
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
    "connections": [],
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}


# TS1 VERIFY VOLUMES AFTER CREATE

ts1_verify_volume1_create_server_profile1 = {
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
    "provisionedCapacity": "1073741824",
    "provisioningType": "Full",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV6",
    "uri": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
    "volumeTemplateUri": None,
}


# TS1 VERIFY VOLUMES AFTER EDIT

ts1_verify_volume2_edit_server_profile1 = {
    "category": "storage-volumes",
    "description": "",
    "deviceVolumeName": STORESERV_VOLUME_TEMPLATE_NAME1,
    "isPermanent": True,
    "isShareable": False,
    "name": STORESERV_VOLUME_TEMPLATE_NAME1,
    "provisionedCapacity": "1073741824",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STORESERV_STORAGE_POOL,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV6",
    "uri": STORESERV_VOLUME_TEMPLATE_NAME1,
    "volumeTemplateUri": None,
}

ts1_verify_volume2_edit_server_profile3 = {
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
    "provisionedCapacity": "1073741824",
    "provisioningType": "Thin",
    "state": "Managed",
    "status": "OK",
    "storagePoolUri": STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
    "templateConsistency": "Consistent",
    "type": "StorageVolumeV6",
    "uri": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15,
    "volumeTemplateUri": None,
}


# NEGATIVE CREATE SERVER PROFILE TASKS

# null volume name
negative_sp1 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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

# invalid volume name with volume template
negative_sp2 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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

# Invalid description
negative_sp3 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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

# Invalid size
negative_sp4 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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

# null size
negative_sp5 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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

# size too large for storaage system
negative_sp6 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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

# invalid data protection level with template
negative_sp7 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid11None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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

# invalid data protection level
negative_sp8 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid11None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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

# null data protection level
negative_sp9 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": None,
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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

# null isShareable
negative_sp10 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": None,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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

# Invalid isShareable
negative_sp11 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": 3,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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

# isShareable==True and Non-Permanent
negative_sp12 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": True,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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

# isShareable==True and is bootable
negative_sp13 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": True,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME7,
                },
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


# Data Provisioning Type Different from Template
negative_sp14 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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

# Invalid Data Provisioning Type
negative_sp15 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Medium",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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

# Null Data Provisioning Type
negative_sp16 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": None,
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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

# Null Storage Pool
negative_sp17 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": None,
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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

# Invalid isPermanent
negative_sp18 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                    },
                    "isPermanent": "A",
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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

# Null Template Uri
negative_sp19 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                    },
                    "isPermanent": False,
                    "templateUri": None,
                },
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

# Template Uri From Wrong Storage System/pool
negative_sp20 = {
    "type": "ServerProfileV9",
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
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL,
                    },
                    "isPermanent": False,
                    "templateUri": "SVT:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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

# Bootable volume but no bootable connections
negative_sp21 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                    },
                    "isPermanent": False,
                    "templateUri": "SVT:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
                "lunType": "Auto",
                "storagePaths": [],
            },
        ]
    }
}

# multiple Bootable volumes
negative_sp22 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                    },
                    "isPermanent": False,
                    "templateUri": "SVT:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_PRIVATE_VOLUME2,
                "volume": None,
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

# POST with v600 API and v500 Request Body
negative_sp23 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                "volumeProvisionedCapacityBytes": "1073741824",
                "volumeProvisionType": "Thin",
                "volumeShareable": False,
                "dataProtectionLevel": "NetworkRaid10Mirror3Way",
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


# NEGATIVE EDIT SERVER PROFILE TASKS

# create profile for negative edit validation tests
create_negative_edit_profile = {
    "type": "ServerProfileV9",
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
        "connections": []
    },
}

# null volume name
negative_edit_sp1 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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

# invalid volume name with volume template
negative_edit_sp2 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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

# Invalid description
negative_edit_sp3 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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

# Invalid size
negative_edit_sp4 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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

# null size
negative_edit_sp5 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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

# size too large for storaage system
negative_edit_sp6 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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

# invalid data protection level with template
negative_edit_sp7 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid11None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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

# invalid data protection level
negative_edit_sp8 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid11None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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

# null data protection level
negative_edit_sp9 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": None,
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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

# null isShareable
negative_edit_sp10 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": None,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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

# Invalid isShareable
negative_edit_sp11 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": 3,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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

# isShareable==True and Non-Permanent
negative_edit_sp12 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": True,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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

# isShareable==True and is bootable
negative_edit_sp13 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": True,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": True,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME7,
                },
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


# Data Provisioning Type Different from Template
negative_edit_sp14 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'SVT:' + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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

# Invalid Data Provisioning Type
negative_edit_sp15 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Medium",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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

# Null Data Provisioning Type
negative_edit_sp16 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": None,
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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

# Null Storage Pool
negative_edit_sp17 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": None,
                    },
                    "isPermanent": False,
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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

# Invalid isPermanent
negative_edit_sp18 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                    },
                    "isPermanent": "A",
                    "templateUri": 'ROOT:' + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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

# Null Template Uri
negative_edit_sp19 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                    },
                    "isPermanent": False,
                    "templateUri": None,
                },
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

# Template Uri From Wrong Storage System/pool
negative_edit_sp20 = {
    "type": "ServerProfileV9",
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
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STORESERV_STORAGE_POOL,
                    },
                    "isPermanent": False,
                    "templateUri": "SVT:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Bootable volume but no bootable connections
negative_edit_sp21 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                    },
                    "isPermanent": False,
                    "templateUri": "SVT:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": True,
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
negative_edit_sp22 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                    },
                    "isPermanent": False,
                    "templateUri": "SVT:" + STOREVIRTUAL_VOLUME_TEMPLATE_NAME1,
                },
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
                "volumeUri": "v:" + STOREVIRTUAL_EXISTING_PRIVATE_VOLUME2,
                "volume": None,
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

# PUT with v600 API and v500 Request Body
negative_edit_sp23 = {
    "type": "ServerProfileV9",
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
        "connections": [
            {
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                "volumeProvisionedCapacityBytes": "1073741824",
                "volumeProvisionType": "Thin",
                "volumeShareable": False,
                "dataProtectionLevel": "NetworkRaid10Mirror3Way",
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
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}


# multiple Bootable volumes that together are too large for storage system but, individually fit
negative_test = {
    "type": "ServerProfileV9",
    "serverHardwareTypeUri": SERVER_HARDWARE_TYPE1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "Negative_Test",
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
                "networkUri": STOREVIRTUAL_STORAGE_POOL_NETWORK,
            }
        ]
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
                        "size": 107374182400,
                        "provisioningType": "Full",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                    },
                    "isPermanent": False,
                    "templateUri": "ROOT:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
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
                "volumeUri": None,
                "volume": {
                    "properties": {
                        "name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME7,
                        "description": "",
                        "size": 107374182400,
                        "provisioningType": "Full",
                        "isShareable": True,
                        "dataProtectionLevel": "NetworkRaid0None",
                        "storagePool": "SP:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                    },
                    "isPermanent": True,
                    "templateUri": "ROOT:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_SLPT_STORAGE_SYSTEM,
                "isBootVolume": False,
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

ts0_create_sp = [
    ts0_create_server_profile1.copy(),
    ts0_create_server_profile2.copy(),
    ts0_create_server_profile3.copy(),
    ts0_create_server_profile4.copy(),
    ts0_create_server_profile5.copy(),
]

ts0_verify_create_sp_v600 = [
    ts0_verify_create_server_profile1.copy(),
    ts0_verify_create_server_profile2.copy(),
    ts0_verify_create_server_profile3.copy(),
    ts0_verify_create_server_profile4.copy(),
    ts0_verify_create_server_profile5.copy(),
]

ts0_verify_create_sp_v500 = [
    ts1_verify_create_server_profile1.copy(),
    ts1_verify_create_server_profile2.copy(),
    ts1_verify_create_server_profile3.copy(),
    ts1_verify_create_server_profile4.copy(),
    ts1_verify_create_server_profile5.copy(),
]

ts0_verify_volumes_after_create = [
    ts0_verify_volume1_create_server_profile1.copy(),
    ts0_verify_volume1_create_server_profile2.copy(),
    ts0_verify_volume1_create_server_profile3.copy(),
    ts0_verify_volume1_create_server_profile4.copy(),
    ts0_verify_volume1_create_server_profile5.copy(),
]

ts0_edit_sp = [
    ts0_edit_server_profile1.copy(),
    ts0_edit_server_profile2.copy(),
    ts0_edit_server_profile3.copy(),
    ts0_edit_server_profile4.copy(),
    ts0_edit_server_profile5.copy(),
]

ts0_verify_edit_sp_v600 = [
    ts0_verify_edit_server_profile1.copy(),
    ts0_verify_edit_server_profile2.copy(),
    ts0_verify_edit_server_profile3.copy(),
    ts0_verify_edit_server_profile4.copy(),
    ts0_verify_edit_server_profile5.copy(),
]

ts0_verify_edit_sp_v500 = [
    ts1_verify_edit_server_profile1.copy(),
    ts1_verify_edit_server_profile2.copy(),
    ts1_verify_edit_server_profile3.copy(),
    ts1_verify_edit_server_profile4.copy(),
    ts1_verify_edit_server_profile5.copy(),
]

ts0_verify_volumes_after_edit = [
    ts0_verify_volume1_create_server_profile1.copy(),
    ts0_verify_volume2_edit_server_profile1.copy(),
    ts0_verify_volume1_create_server_profile2.copy(),
    ts0_verify_volume2_edit_server_profile2.copy(),
    ts0_verify_volume1_create_server_profile3.copy(),
    ts0_verify_volume2_edit_server_profile3.copy(),
    ts0_verify_volume1_create_server_profile4.copy(),
    ts0_verify_volume2_edit_server_profile4.copy(),
]

ts0_verify_nonpermanent_volumes_after_edit = [
    ts0_verify_volume1_create_server_profile5.copy(),
]

ts0_verify_nonpermanent_volumes_after_delete = [
    ts0_verify_volume1_create_server_profile1.copy(),
    ts0_verify_volume2_edit_server_profile3.copy(),
    ts0_verify_volume1_create_server_profile4.copy(),
    ts0_verify_volume2_edit_server_profile4.copy(),
    ts0_verify_volume1_create_server_profile5.copy(),
]

ts0_verify_permanent_volumes_after_delete = [
    ts0_verify_volume2_edit_server_profile1.copy(),
    ts0_verify_volume1_create_server_profile2.copy(),
    ts0_verify_volume2_edit_server_profile2.copy(),
    ts0_verify_volume1_create_server_profile3.copy(),
]

ts0_delete_new_volumes = [
    {"properties": {"name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1}},
    {"properties": {"name": STORESERV_VOLUME_TEMPLATE_NAME1}},
    {"properties": {"name": PROFILE3_VOLUME1_NAME}},
    {"properties": {"name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15}},
    {"properties": {"name": PROFILE4_VOLUME1_NAME}},
    {"properties": {"name": PROFILE4_VOLUME2_NAME}},
    {"properties": {"name": PROFILE5_VOLUME1_NAME}},
]

ts1_create_sp = [
    ts1_create_server_profile1.copy(),
    ts1_create_server_profile2.copy(),
    ts1_create_server_profile3.copy(),
    ts1_create_server_profile4.copy(),
    ts1_create_server_profile5.copy(),
]

ts1_verify_create_sp_v600 = [
    ts0_verify_create_server_profile1.copy(),
    ts0_verify_create_server_profile2.copy(),
    ts0_verify_create_server_profile3.copy(),
    ts0_verify_create_server_profile4.copy(),
    ts0_verify_create_server_profile5.copy(),
]

ts1_verify_create_sp_v500 = [
    ts1_verify_create_server_profile1.copy(),
    ts1_verify_create_server_profile2.copy(),
    ts1_verify_create_server_profile3.copy(),
    ts1_verify_create_server_profile4.copy(),
    ts1_verify_create_server_profile5.copy(),
]

ts1_verify_volumes_after_create = [
    ts1_verify_volume1_create_server_profile1.copy(),
    ts0_verify_volume1_create_server_profile2.copy(),
    ts0_verify_volume1_create_server_profile3.copy(),
    ts0_verify_volume1_create_server_profile4.copy(),
    ts0_verify_volume1_create_server_profile5.copy(),
]

ts1_edit_sp = [
    ts1_edit_server_profile1.copy(),
    ts1_edit_server_profile2.copy(),
    ts1_edit_server_profile3.copy(),
    ts1_edit_server_profile4.copy(),
    ts1_edit_server_profile5.copy(),
]

ts1_verify_edit_sp_v600 = [
    ts0_verify_edit_server_profile1.copy(),
    ts0_verify_edit_server_profile2.copy(),
    ts0_verify_edit_server_profile3.copy(),
    ts0_verify_edit_server_profile4.copy(),
    ts0_verify_edit_server_profile5.copy(),
]

ts1_verify_edit_sp_v500 = [
    ts1_verify_edit_server_profile1.copy(),
    ts1_verify_edit_server_profile2.copy(),
    ts1_verify_edit_server_profile3.copy(),
    ts1_verify_edit_server_profile4.copy(),
    ts1_verify_edit_server_profile5.copy(),
]

ts1_verify_volumes_after_edit = [
    ts1_verify_volume1_create_server_profile1.copy(),
    ts1_verify_volume2_edit_server_profile1.copy(),
    ts0_verify_volume1_create_server_profile2.copy(),
    ts0_verify_volume2_edit_server_profile2.copy(),
    ts0_verify_volume1_create_server_profile3.copy(),
    ts1_verify_volume2_edit_server_profile3.copy(),
    ts0_verify_volume1_create_server_profile4.copy(),
    ts0_verify_volume2_edit_server_profile4.copy(),
]

ts1_verify_nonpermanent_volumes_after_edit = [
    ts0_verify_volume1_create_server_profile5.copy(),
]

ts1_verify_nonpermanent_volumes_after_delete = [
    ts0_verify_volume1_create_server_profile1.copy(),
    ts0_verify_volume2_edit_server_profile3.copy(),
    ts0_verify_volume1_create_server_profile4.copy(),
    ts0_verify_volume2_edit_server_profile4.copy(),
    ts0_verify_volume1_create_server_profile5.copy(),
]

ts1_verify_permanent_volumes_after_delete = [
    ts1_verify_volume2_edit_server_profile1.copy(),
    ts0_verify_volume1_create_server_profile2.copy(),
    ts0_verify_volume2_edit_server_profile2.copy(),
    ts0_verify_volume1_create_server_profile3.copy(),
]

ts1_delete_new_volumes = [
    {"properties": {"name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME1}},
    {"properties": {"name": STORESERV_VOLUME_TEMPLATE_NAME1}},
    {"properties": {"name": PROFILE3_VOLUME1_NAME}},
    {"properties": {"name": STOREVIRTUAL_VOLUME_TEMPLATE_NAME15}},
    {"properties": {"name": PROFILE4_VOLUME1_NAME}},
    {"properties": {"name": PROFILE4_VOLUME2_NAME}},
    {"properties": {"name": PROFILE5_VOLUME1_NAME}},
]

ts2_verify_volumes_after_create = [
    ts0_verify_volume1_create_server_profile1.copy(),
    ts0_verify_volume1_create_server_profile2.copy(),
    ts0_verify_volume1_create_server_profile3.copy(),
    ts0_verify_volume1_create_server_profile4.copy(),
    ts0_verify_volume1_create_server_profile5.copy(),
]

ts2_verify_volumes_after_edit = [
    ts0_verify_volume1_create_server_profile1.copy(),
    ts1_verify_volume2_edit_server_profile1.copy(),
    ts0_verify_volume1_create_server_profile2.copy(),
    ts0_verify_volume2_edit_server_profile2.copy(),
    ts0_verify_volume1_create_server_profile3.copy(),
    ts1_verify_volume2_edit_server_profile3.copy(),
    ts0_verify_volume1_create_server_profile4.copy(),
    ts0_verify_volume2_edit_server_profile4.copy(),
]

ts2_verify_nonpermanent_volumes_after_edit = [
    ts0_verify_volume1_create_server_profile5.copy(),
]

ts2_verify_nonpermanent_volumes_after_delete = [
    ts0_verify_volume1_create_server_profile1.copy(),
    ts1_verify_volume2_edit_server_profile3.copy(),
    ts0_verify_volume1_create_server_profile4.copy(),
    ts0_verify_volume2_edit_server_profile4.copy(),
    ts0_verify_volume1_create_server_profile5.copy(),
]

ts2_verify_permanent_volumes_after_delete = [
    ts0_verify_volume1_create_server_profile2.copy(),
    ts0_verify_volume2_edit_server_profile2.copy(),
    ts0_verify_volume1_create_server_profile3.copy(),
]

ts3_verify_volumes_after_create = [
    ts1_verify_volume1_create_server_profile1.copy(),
    ts0_verify_volume1_create_server_profile2.copy(),
    ts0_verify_volume1_create_server_profile3.copy(),
    ts0_verify_volume1_create_server_profile4.copy(),
    ts0_verify_volume1_create_server_profile5.copy(),
]

ts3_verify_volumes_after_edit = [
    ts1_verify_volume1_create_server_profile1.copy(),
    ts0_verify_volume2_edit_server_profile1.copy(),
    ts0_verify_volume1_create_server_profile2.copy(),
    ts0_verify_volume2_edit_server_profile2.copy(),
    ts0_verify_volume1_create_server_profile3.copy(),
    ts0_verify_volume2_edit_server_profile3.copy(),
    ts0_verify_volume1_create_server_profile4.copy(),
    ts0_verify_volume2_edit_server_profile4.copy(),
]

ts3_verify_nonpermanent_volumes_after_edit = [
    ts0_verify_volume1_create_server_profile5.copy(),
]

ts3_verify_nonpermanent_volumes_after_delete = [
    ts1_verify_volume1_create_server_profile1.copy(),
    ts0_verify_volume2_edit_server_profile3.copy(),
    ts0_verify_volume1_create_server_profile4.copy(),
    ts0_verify_volume2_edit_server_profile4.copy(),
    ts0_verify_volume1_create_server_profile5.copy(),
]

ts3_verify_permanent_volumes_after_delete = [
    ts0_verify_volume1_create_server_profile2.copy(),
    ts0_verify_volume2_edit_server_profile2.copy(),
    ts0_verify_volume1_create_server_profile3.copy(),
]

negative_create_profile_tasks = [
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp1.copy(),
        'taskState': 'Error',
        'errorMessage': 'NULL_VOLUME_NAME'},
    # {
    #     'keyword': 'Add Server Profile',
    #     'argument': negative_sp2.copy(),
    #     'taskState': 'Error',
    #     'errorMessage': 'INVALID_VOLUME_NAME'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp3.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_DESCRIPTION'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp4.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_SIZE'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp5.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_SIZE'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp6.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_SIZE_TOO_LARGE'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp7.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_DATA_PROTECTION_LEVEL_LOCKED'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp8.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_DATA_PROTECTION_LEVEL'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp9.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_DATA_PROTECTION_LEVEL'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp10.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_SHARABLE_MUST_BE_TRUE_OR_FALSE'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp11.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_SHARABLE'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp12.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_ISSHAREABLE_MUST_BE_FALSE'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp13.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_ISSHAREABLE_MUST_BE_FALSE'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp14.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_PROVISIONING_TYPE_LOCKED'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp15.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_PROVISIONING_TYPE'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp16.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_PROVISIONING_TYPE'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp17.copy(),
        'taskState': 'Error',
        'errorMessage': 'MISSING_REQUIRED_FIELD_VOLUME'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp19.copy(),
        'taskState': 'Error',
        'errorMessage': 'MISSING_REQUIRED_VOLUME_FILED'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp20.copy(),
        'taskState': 'Error',
        'errorMessage': 'UNEXPECTED_ERROR'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp21.copy(),
        'taskState': 'Error',
        'errorMessage': 'Storage_path_disabled_not_exist'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp22.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_bootable_volumes'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp23.copy(),
        'taskState': 'Error',
        'errorMessage': 'MISSING_VOLUMEURI_FIELD'},
]

negative_edit_profile_tasks = [
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp1.copy(),
        'taskState': 'Error',
        'errorMessage': 'NULL_VOLUME_NAME'},
    # {
    #     'keyword': 'Edit Server Profile',
    #     'argument': negative_edit_sp2.copy(),
    #     'taskState': 'Error',
    #     'errorMessage': 'INVALID_VOLUME_NAME'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp3.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_DESCRIPTION'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp4.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_SIZE'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp5.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_SIZE'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp6.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_SIZE_TOO_LARGE'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp7.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_DATA_PROTECTION_LEVEL_LOCKED'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp8.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_DATA_PROTECTION_LEVEL'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp9.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_DATA_PROTECTION_LEVEL'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp10.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_SHARABLE_MUST_BE_TRUE_OR_FALSE'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp11.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_SHARABLE'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp12.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_ISSHAREABLE_MUST_BE_FALSE'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp13.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_ISSHAREABLE_MUST_BE_FALSE'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp14.copy(),
        'taskState': 'Error',
        'errorMessage': 'VOLUME_PROVISIONING_TYPE_LOCKED'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp15.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_PROVISIONING_TYPE'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp16.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_VOLUME_PROVISIONING_TYPE'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp17.copy(),
        'taskState': 'Error',
        'errorMessage': 'MISSING_REQUIRED_FIELD_VOLUME'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp19.copy(),
        'taskState': 'Error',
        'errorMessage': 'MISSING_REQUIRED_VOLUME_FILED'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp20.copy(),
        'taskState': 'Error',
        'errorMessage': 'UNEXPECTED_ERROR'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp21.copy(),
        'taskState': 'Error',
        'errorMessage': 'Storage_path_disabled_not_exist'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp22.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_bootable_volumes'},
    {
        'keyword': 'Edit Server Profile',
        'argument': negative_edit_sp23.copy(),
        'taskState': 'Error',
        'errorMessage': 'MISSING_VOLUMEURI_FIELD'},
]

"""
OVF1072 C7000
"""
# pylint: disable=E0401,E0602
from copy import deepcopy
from dto import *
from env_variables_C7000 import *

# from robot.libraries.BuiltIn import BuiltIn

# Credentials

admin_credentials = deepcopy(ADMIN_CREDENTIALS_COMMON)
oa_credentials = deepcopy(OA_CREDENTIALS_COMMON)
cliq_credentials = deepcopy(STOREVIRTUAL_SLPT_STATIC_CLIQ_CREDENTIALS)
ilo_credentials = deepcopy(ILO_CREDENTIALS_COMMON)
# hpmctp_credentials = deepcopy(HPMCTP_CREDENTIALS_COMMON)

# Enclosures, Interconnects, Server Hardware, LIG, and EG
# Enclosures
ENC1 = 'wpst22'
ENC1_OA1 = "16.125.77.71"
ENC2 = 'wpst23'
ENC2_OA1 = "16.125.77.80"
ENC3 = 'wpst26'
ENC3_OA1 = "16.125.79.45"
# Interconnects
ENC1ICBAY1 = '%s, interconnect 1' % ENC1
ENC1ICBAY2 = '%s, interconnect 2' % ENC1
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY4 = '%s, interconnect 4' % ENC1
ENC1ICBAY5 = '%s, interconnect 5' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
ENC2ICBAY1 = '%s, interconnect 1' % ENC2
ENC2ICBAY2 = '%s, interconnect 2' % ENC2
ENC2ICBAY3 = '%s, interconnect 3' % ENC2
ENC2ICBAY4 = '%s, interconnect 4' % ENC2
ENC2ICBAY5 = '%s, interconnect 5' % ENC2
ENC2ICBAY6 = '%s, interconnect 6' % ENC2
ENC3ICBAY1 = '%s, interconnect 1' % ENC3
ENC3ICBAY2 = '%s, interconnect 2' % ENC3
ENC3ICBAY3 = '%s, interconnect 3' % ENC3
ENC3ICBAY4 = '%s, interconnect 4' % ENC3
ENC3ICBAY5 = '%s, interconnect 5' % ENC3
ENC3ICBAY6 = '%s, interconnect 6' % ENC3
# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1  # BL465c Gen8
ENC1SHBAY2 = '%s, bay 2' % ENC1  # BL465c Gen8
ENC1SHBAY3 = '%s, bay 3' % ENC1  # BL465c Gen8
ENC1SHBAY4 = '%s, bay 4' % ENC1  # BL420c Gen8
ENC1SHBAY5 = '%s, bay 5' % ENC1  # BL460c Gen9
ENC1SHBAY6 = '%s, bay 6' % ENC1  # BL460c G6
ENC1SHBAY8 = '%s, bay 7' % ENC1  # BL495c G5
ENC1SHBAY14 = '%s, bay 14' % ENC1  # BL460c Gen10
ENC1SHBAY16 = '%s, bay 16' % ENC1  # BL460c Gen10
ENC2SHBAY1 = '%s, bay 1' % ENC2  # BL465c Gen8
ENC2SHBAY2 = '%s, bay 2' % ENC2  # BL465c Gen8
ENC2SHBAY3 = '%s, bay 3' % ENC2  # BL465c Gen8
ENC2SHBAY4 = '%s, bay 4' % ENC2  # BL420c Gen8
ENC2SHBAY5 = '%s, bay 5' % ENC2  # BL460c Gen9
ENC2SHBAY6 = '%s, bay 6' % ENC2  # BL460c G6
ENC2SHBAY7 = '%s, bay 7' % ENC2  # BL2x220c G5
ENC2SHBAY10 = '%s, bay 10' % ENC2  # BL460c Gen10
ENC2SHBAY16 = '%s, bay 16' % ENC2  # BL460c Gen10
ENC3SHBAY1 = '%s, bay 1' % ENC3  # BL465c Gen8
ENC3SHBAY2 = '%s, bay 2' % ENC3  # BL465c Gen8
ENC3SHBAY3 = '%s, bay 3' % ENC3  # BL465c Gen8
ENC3SHBAY4 = '%s, bay 4' % ENC3  # BL420c Gen8
ENC3SHBAY5 = '%s, bay 5' % ENC3  # BL460c Gen9
ENC3SHBAY7 = '%s, bay 7' % ENC3  # BL660c Gen9
ENC3SHBAY8 = '%s, bay 8' % ENC3  # BL660c Gen8
ENC3SHBAY9 = '%s, bay 9' % ENC3  # BL460c G7
ENC3SHBAY10 = '%s, bay 10' % ENC3  # BL465c G7
# LIGs and EGs
LIG1_NAME = 'LIG22'
EG1_NAME = 'EG22'
LIG2_NAME = 'LIG23'
EG2_NAME = 'EG23'
LIG3_NAME = 'LIG26'
EG3_NAME = 'EG26'

enclosures_expected = [
    {"type": ENCLOSURE_TYPE, "name": "wpst22", "state": "Configured", },
    {"type": ENCLOSURE_TYPE, "name": "wpst23", "state": "Configured", },
    {"type": ENCLOSURE_TYPE, "name": "wpst23", "state": "Configured", },
]

interconnects_expected = [
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC1ICBAY1,
        "productName": "HP VC FlexFabric 10Gb/24-Port Module",
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC1ICBAY2,
        "productName": "HP VC FlexFabric 10Gb/24-Port Module",
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC1ICBAY3,
        "productName": "HP VC FlexFabric 10Gb/24-Port Module",
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC1ICBAY4,
        "productName": "HP VC FlexFabric 10Gb/24-Port Module",
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC1ICBAY5,
        "productName": "HP VC 8Gb 20-Port FC Module",
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC1ICBAY6,
        "productName": "HP VC 8Gb 20-Port FC Module",
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC2ICBAY1,
        "productName": "HP VC FlexFabric-20/40 F8 Module",
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC2ICBAY2,
        "productName": "HP VC FlexFabric-20/40 F8 Module",
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC2ICBAY3,
        "productName": "HP VC FlexFabric 10Gb/24-Port Module",
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC2ICBAY4,
        "productName": "HP VC FlexFabric 10Gb/24-Port Module",
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC2ICBAY5,
        "productName": "HP VC 8Gb 20-Port FC Module",
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC2ICBAY6,
        "productName": "HP VC 8Gb 20-Port FC Module",
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC3ICBAY1,
        "productName": "HP VC FlexFabric 10Gb/24-Port Module",
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC3ICBAY2,
        "productName": "HP VC FlexFabric 10Gb/24-Port Module",
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC3ICBAY3,
        "productName": "HP VC FlexFabric 10Gb/24-Port Module",
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC3ICBAY4,
        "productName": "HP VC FlexFabric 10Gb/24-Port Module",
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC3ICBAY5,
        "productName": "HP VC 8Gb 24-Port FC Module",
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC3ICBAY6,
        "productName": "HP VC 8Gb 24-Port FC Module",
    },
]

NAME_PREFIX = 'C7000-Reg1-OVF1072-'
# StRM
# StoreServ
STORESERV1_NAME = 'wpst3par-7200-7-srv'
STORESERV1_HOSTNAME = 'wpst3par-7200-7-srv.vse.rdlabs.hpecorp.net'
STORESERV1_POOL1 = 'FVT_C7000_reg1_r1'
STORESERV1_POOL2 = 'FVT_C7000_reg1_r5'
STORESERV1_POOL3 = 'FVT_C7000_reg1_r6'
# StoreVirtual
STOREVIRTUAL1_NAME = 'VSA_Cluster_173-2'
STOREVIRTUAL1_HOSTNAME = '16.71.149.173'
STOREVIRTUAL1_VIP = '192.168.21.71'
STOREVIRTUAL1_POOL = 'VSA_Cluster_173-2'
STOREVIRTUAL2_NAME = 'VSA84_Storage_Pool'
STOREVIRTUAL2_HOSTNAME = '16.71.151.84'
STOREVIRTUAL2_VIP = '16.71.151.84'
STOREVIRTUAL2_POOL = 'VSA84_Storage_Pool'
# Volume templates
VOLUME_TEMPLATE_3PAR1_POOL1_PRIVATE = "3par1-pool1-private"
VOLUME_TEMPLATE_3PAR1_POOL1_SHARED = "3par1-pool1-shared"
VOLUME_TEMPLATE_VSA1_RAID5_PRIVATE = "vsa1-raid5-private"
VOLUME_TEMPLATE_VSA1_RAID5_SHARED = "vsa1-raid5-shared"
VOLUME_TEMPLATE_VSA2_RAID0_PRIVATE = "vsa2-raid0-private"
VOLUME_TEMPLATE_VSA2_RAID0_SHARED = "vsa2-raid0-shared"
# Volumes
VOLUME_NAME_PREFIX = NAME_PREFIX
# Pre-existing volumes in storage systems
VOLUME_EXIST_VSA1_SHARED = VOLUME_NAME_PREFIX + 'vsa1-exist-shared'
VOLUME_EXIST_VSA1_PRIV = VOLUME_NAME_PREFIX + 'vsa1-exist-priv'
# Created volumes in OV
VOLUME_PROFILE1_3PAR1_PRIV = VOLUME_NAME_PREFIX + 'profile1-3par1-priv'
VOLUME_PROFILE2_3PAR1_PRIV = VOLUME_NAME_PREFIX + 'profile2-3par1-priv'
VOLUME_3PAR1_SHARED = VOLUME_NAME_PREFIX + '3par1-shared'
VOLUME_PROFILE1_VSA1_PRIV = VOLUME_NAME_PREFIX + 'profile1-vsa1-priv'
VOLUME_PROFILE2_VSA1_PRIV = VOLUME_NAME_PREFIX + 'profile2-vsa1-priv'
VOLUME_VSA1_SHARED = VOLUME_NAME_PREFIX + 'vsa1-shared'
VOLUME_PROFILE1_VSA2_PRIV = VOLUME_NAME_PREFIX + 'profile1-vsa2-priv'
VOLUME_PROFILE2_VSA2_PRIV = VOLUME_NAME_PREFIX + 'profile2-vsa2-priv'
VOLUME_VSA2_SHARED = VOLUME_NAME_PREFIX + 'vsa2-shared'

storage_systems = [
    {
        'type': STORAGE_SYSTEM_TYPE, 'name': STORESERV1_NAME, 'family': 'StoreServ',
        "hostname": STORESERV1_HOSTNAME, 'credentials': {'username': 'fusionadm', 'password': 'hpvse1'},
        "deviceSpecificAttributes": {
            "discoveredDomains": [
                "NO DOMAIN",
                "wpst20",
                "wpst22",
                "wpst23",
                "wpst26",
                "wpst30",
                "wpst31",
                "wpst32",
                "wpst33",
                "wpst34",
                "wpst8",
                "wpst9",
            ],
            "managedDomain": "FVT_C7000_reg1",
        },
    },
    {
        'type': STORAGE_SYSTEM_TYPE, 'name': STOREVIRTUAL1_NAME, "family": "StoreVirtual",
        "hostname": STOREVIRTUAL1_HOSTNAME, "credentials": {"username": "admin", "password": 'admin'},
        "ports": [
            {
                "name": STOREVIRTUAL1_VIP,
                "expectedNetworkUri": "ETH:network-untagged",
                "expectedNetworkName": "network-untagged",
                "mode": "Managed",
            },
        ],
    },
    {
        'type': STORAGE_SYSTEM_TYPE, 'name': STOREVIRTUAL2_NAME, "family": "StoreVirtual",
        "hostname": STOREVIRTUAL2_HOSTNAME, "credentials": {"username": "admin", "password": 'admin'},
        "ports": [
            {
                "name": STOREVIRTUAL2_VIP,
                "expectedNetworkUri": "ETH:network-tunnel",
                "expectedNetworkName": "network-tunnel",
                "mode": "Managed",
            }, ],
    },
]

storage_pools = [
    {
        "storageSystemUri": STORESERV1_NAME,
        "name": STORESERV1_POOL1,
        "isManaged": True,
    },
    {
        "storageSystemUri": STORESERV1_NAME,
        "name": STORESERV1_POOL2,
        "isManaged": True,
    },
    {
        "storageSystemUri": STORESERV1_NAME,
        "name": STORESERV1_POOL3,
        "isManaged": True,
    },
]

storage_volume_templates = [
    {
        "name": VOLUME_TEMPLATE_3PAR1_POOL1_PRIVATE, "description": "",
        "rootTemplateUri": STORESERV_ROOT_VOLUME_TEMPLATE,
        "properties": {
            "name": {
                "title": "Volume name", "description": "A volume name between 1 and 100 characters",
                "type": "string", "minLength": 1, "maxLength": 100, "required": True,
                "meta": {"locked": False}
            },
            "description": {
                "title": "Description", "description": "A description for the volume",
                "type": "string", "minLength": 0, "maxLength": 2000, "default": "3Par1 pool1 private",
                "meta": {"locked": False}
            },
            "storagePool": {
                "title": "Storage Pool", "description": "A common provisioning group URI reference",
                "type": "string", "required": True, "format": "x-uri-reference",
                "meta": {"locked": False, "createOnly": True, "semanticType": "device-storage-pool"},
                "default": STORESERV1_POOL1
            },
            "size": {
                "title": "Capacity", "description": "The capacity of the volume in bytes",
                "type": "integer", "required": True, "minimum": 1073741824, "maximum": 17592186044416,
                "meta": {"locked": False, "semanticType": "capacity"},
                "default": 1073741824,
            },
            "isShareable": {
                "title": "Is Shareable", "description": "The shareability of the volume",
                "type": "boolean", "meta": {"locked": False},
                "default": False,
            },
            "provisioningType": {
                "title": "Provisioning Type", "description": "The provisioning type for the volume",
                "type": "string", "enum": ["Thin", "Full"], "meta": {"locked": True, "createOnly": True},
                "default": "Thin"
            },
            "snapshotPool": {
                "title": "Snapshot Pool",
                "description": "A URI referenceto the common provisioning group used to create snapshots",
                "type": "string", "format": "x-uri-reference",
                "meta": {"locked": True, "semanticType": "device-snapshot-storage-pool"},
                "default": STORESERV1_POOL1,
            }
        },
    },
    {
        "name": VOLUME_TEMPLATE_3PAR1_POOL1_SHARED, "description": "",
        "rootTemplateUri": STORESERV_ROOT_VOLUME_TEMPLATE,
        "properties": {
            "name": {
                "title": "Volume name", "description": "A volume name between 1 and 100 characters",
                "type": "string", "minLength": 1, "maxLength": 100, "required": True,
                "meta": {"locked": False}
            },
            "description": {
                "title": "Description", "description": "A description for the volume",
                "type": "string", "minLength": 0, "maxLength": 2000, "default": "3Par pool1 shared",
                "meta": {"locked": False}
            },
            "storagePool": {
                "title": "Storage Pool", "description": "A common provisioning group URI reference",
                "type": "string", "required": True, "format": "x-uri-reference",
                "meta": {"locked": False, "createOnly": True, "semanticType": "device-storage-pool"},
                "default": STORESERV1_POOL1
            },
            "size": {
                "title": "Capacity", "description": "The capacity of the volume in bytes",
                "type": "integer", "required": True, "minimum": 1073741824, "maximum": 17592186044416,
                "meta": {"locked": False, "semanticType": "capacity"},
                "default": 1073741824,
            },
            "isShareable": {
                "title": "Is Shareable", "description": "The shareability of the volume",
                "type": "boolean", "meta": {"locked": False},
                "default": True,
            },
            "provisioningType": {
                "title": "Provisioning Type", "description": "The provisioning type for the volume",
                "type": "string", "enum": ["Thin", "Full"], "meta": {"locked": True, "createOnly": True},
                "default": "Thin"
            },
            "snapshotPool": {
                "title": "Snapshot Pool",
                "description": "A URI referenceto the common provisioning group used to create snapshots",
                "type": "string", "format": "x-uri-reference",
                "meta": {"locked": True, "semanticType": "device-snapshot-storage-pool"},
                "default": STORESERV1_POOL1,
            }
        },
    },
    {
        "name": VOLUME_TEMPLATE_VSA1_RAID5_PRIVATE, "description": "",
        "rootTemplateUri": STOREVIRTUAL_ROOT_VOLUME_TEMPLATE,
        "properties": {
            "name": {
                "title": "Volume name", "description": "A volume name between 1 and 100 characters",
                "type": "string", "minLength": 1, "maxLength": 100, "required": True, "meta": {"locked": False}
            },
            "description": {
                "title": "Description", "description": "A description for the volume",
                "type": "string", "minLength": 0, "maxLength": 2000,
                "default": "VSA1 RAID5 private",
                "meta": {"locked": False}
            },
            "storagePool": {
                "title": "Storage Pool", "description": "StoragePoolURI the volume should be added to",
                "type": "string", "format": "x-uri-reference", "required": True,
                "meta": {"locked": False, "createOnly": True, "semanticType": "device-storage-pool"},
                "default": STOREVIRTUAL1_POOL
            },
            "size": {
                "title": "Capacity", "description": "Capacity of the volume in bytes",
                "type": "integer", "minimum": 4194304, "required": True,
                "default": 1073741824,
                "meta": {"locked": False, "semanticType": "capacity"}
            },
            "dataProtectionLevel": {
                "title": "Data Protection Level",
                "description": "Indicates the number and configuration of data copies in the Storage Pool",
                "type": "string", "enum": ["NetworkRaid0None", "NetworkRaid5SingleParity", "NetworkRaid10Mirror2Way",
                                           "NetworkRaid10Mirror3Way", "NetworkRaid10Mirror4Way",
                                           "NetworkRaid6DualParity"],
                "default": "NetworkRaid5SingleParity",
                "required": True, "meta": {"locked": True, "semanticType": "device-dataProtectionLevel"}
            },
            "provisioningType": {
                "title": "Provisioning Type", "description": "The provisioning type for the volume",
                "type": "string", "enum": ["Thin", "Full"],
                "default": "Thin",
                "meta": {"locked": True, "createOnly": "True", "semanticType": "device-provisioningType"}
            },
            "isAdaptiveOptimizationEnabled": {
                "title": "Adaptive Optimization", "description": "",
                "type": "boolean", "default": True, "meta": {"locked": True}
            },
            "isShareable": {
                "title": "Is Shareable", "description": "The shareability of the volume",
                "type": "boolean", "default": False, "meta": {"locked": False}
            }
        },
    },
    {
        "name": VOLUME_TEMPLATE_VSA1_RAID5_SHARED, "description": "",
        "rootTemplateUri": STOREVIRTUAL_ROOT_VOLUME_TEMPLATE,
        "properties": {
            "name": {
                "title": "Volume name", "description": "A volume name between 1 and 100 characters",
                "type": "string", "minLength": 1, "maxLength": 100, "required": True, "meta": {"locked": False}
            },
            "description": {
                "title": "Description", "description": "A description for the volume",
                "type": "string", "minLength": 0, "maxLength": 2000,
                "default": "VSA1 RAID5 shared",
                "meta": {"locked": False}
            },
            "storagePool": {
                "title": "Storage Pool", "description": "StoragePoolURI the volume should be added to",
                "type": "string", "format": "x-uri-reference", "required": True,
                "meta": {"locked": False, "createOnly": True, "semanticType": "device-storage-pool"},
                "default": STOREVIRTUAL1_POOL
            },
            "size": {
                "title": "Capacity", "description": "Capacity of the volume in bytes",
                "type": "integer", "minimum": 4194304, "required": True,
                "default": 1073741824,
                "meta": {"locked": False, "semanticType": "capacity"}
            },
            "dataProtectionLevel": {
                "title": "Data Protection Level",
                "description": "Indicates the number and configuration of data copies in the Storage Pool",
                "type": "string", "enum": ["NetworkRaid0None", "NetworkRaid5SingleParity", "NetworkRaid10Mirror2Way",
                                           "NetworkRaid10Mirror3Way", "NetworkRaid10Mirror4Way",
                                           "NetworkRaid6DualParity"],
                "default": "NetworkRaid5SingleParity",
                "required": True, "meta": {"locked": True, "semanticType": "device-dataProtectionLevel"}
            },
            "provisioningType": {
                "title": "Provisioning Type", "description": "The provisioning type for the volume",
                "type": "string", "enum": ["Thin", "Full"],
                "default": "Thin",
                "meta": {"locked": True, "createOnly": "True", "semanticType": "device-provisioningType"}
            },
            "isAdaptiveOptimizationEnabled": {
                "title": "Adaptive Optimization", "description": "",
                "type": "boolean", "default": True, "meta": {"locked": True}
            },
            "isShareable": {
                "title": "Is Shareable", "description": "The shareability of the volume",
                "type": "boolean", "default": True, "meta": {"locked": False}
            }
        },
    },
    {
        "name": VOLUME_TEMPLATE_VSA2_RAID0_PRIVATE, "description": "",
        "rootTemplateUri": STOREVIRTUAL_ROOT_VOLUME_TEMPLATE,
        "properties": {
            "name": {
                "title": "Volume name", "description": "A volume name between 1 and 100 characters",
                "type": "string", "minLength": 1, "maxLength": 100, "required": True, "meta": {"locked": False}
            },
            "description": {
                "title": "Description", "description": "A description for the volume",
                "type": "string", "minLength": 0, "maxLength": 2000,
                "default": "VSA2 RAID0 private",
                "meta": {"locked": False}
            },
            "storagePool": {
                "title": "Storage Pool", "description": "StoragePoolURI the volume should be added to",
                "type": "string", "format": "x-uri-reference", "required": True,
                "meta": {"locked": False, "createOnly": True, "semanticType": "device-storage-pool"},
                "default": STOREVIRTUAL2_POOL
            },
            "size": {
                "title": "Capacity", "description": "Capacity of the volume in bytes",
                "type": "integer", "minimum": 4194304, "required": True,
                "default": 1073741824,
                "meta": {"locked": False, "semanticType": "capacity"}
            },
            "dataProtectionLevel": {
                "title": "Data Protection Level",
                "description": "Indicates the number and configuration of data copies in the Storage Pool",
                "type": "string", "enum": ["NetworkRaid0None", "NetworkRaid5SingleParity", "NetworkRaid10Mirror2Way",
                                           "NetworkRaid10Mirror3Way", "NetworkRaid10Mirror4Way",
                                           "NetworkRaid6DualParity"],
                "default": "NetworkRaid0None",
                "required": True, "meta": {"locked": True, "semanticType": "device-dataProtectionLevel"}
            },
            "provisioningType": {
                "title": "Provisioning Type", "description": "The provisioning type for the volume",
                "type": "string", "enum": ["Thin", "Full"],
                "default": "Thin",
                "meta": {"locked": True, "createOnly": "True", "semanticType": "device-provisioningType"}
            },
            "isAdaptiveOptimizationEnabled": {
                "title": "Adaptive Optimization", "description": "",
                "type": "boolean", "default": True, "meta": {"locked": True}
            },
            "isShareable": {
                "title": "Is Shareable", "description": "The shareability of the volume",
                "type": "boolean", "default": False, "meta": {"locked": False}
            }
        },
    },
    {
        "name": VOLUME_TEMPLATE_VSA2_RAID0_SHARED, "description": "",
        "rootTemplateUri": STOREVIRTUAL_ROOT_VOLUME_TEMPLATE,
        "properties": {
            "name": {
                "title": "Volume name", "description": "A volume name between 1 and 100 characters",
                "type": "string", "minLength": 1, "maxLength": 100, "required": True, "meta": {"locked": False}
            },
            "description": {
                "title": "Description", "description": "A description for the volume",
                "type": "string", "minLength": 0, "maxLength": 2000,
                "default": "VSA2 RAID0 shared",
                "meta": {"locked": False}
            },
            "storagePool": {
                "title": "Storage Pool", "description": "StoragePoolURI the volume should be added to",
                "type": "string", "format": "x-uri-reference", "required": True,
                "meta": {"locked": False, "createOnly": True, "semanticType": "device-storage-pool"},
                "default": STOREVIRTUAL2_POOL
            },
            "size": {
                "title": "Capacity", "description": "Capacity of the volume in bytes",
                "type": "integer", "minimum": 4194304, "required": True,
                "default": 1073741824,
                "meta": {"locked": False, "semanticType": "capacity"}
            },
            "dataProtectionLevel": {
                "title": "Data Protection Level",
                "description": "Indicates the number and configuration of data copies in the Storage Pool",
                "type": "string", "enum": ["NetworkRaid0None", "NetworkRaid5SingleParity", "NetworkRaid10Mirror2Way",
                                           "NetworkRaid10Mirror3Way", "NetworkRaid10Mirror4Way",
                                           "NetworkRaid6DualParity"],
                "default": "NetworkRaid0None",
                "required": True, "meta": {"locked": True, "semanticType": "device-dataProtectionLevel"}
            },
            "provisioningType": {
                "title": "Provisioning Type", "description": "The provisioning type for the volume",
                "type": "string", "enum": ["Thin", "Full"],
                "default": "Thin",
                "meta": {"locked": True, "createOnly": "True", "semanticType": "device-provisioningType"}
            },
            "isAdaptiveOptimizationEnabled": {
                "title": "Adaptive Optimization", "description": "",
                "type": "boolean", "default": True, "meta": {"locked": True}
            },
            "isShareable": {
                "title": "Is Shareable", "description": "The shareability of the volume",
                "type": "boolean", "default": True, "meta": {"locked": False}
            }
        },
    },
]

storage_volumes = [
    {
        "properties": {
            "name": VOLUME_PROFILE1_3PAR1_PRIV, "description": "", "storagePool": STORESERV1_POOL1, "size": 1073741824,
            "provisioningType": "Thin", "isShareable": False, "snapshotPool": STORESERV1_POOL1
        },
        "templateUri": VOLUME_TEMPLATE_3PAR1_POOL1_PRIVATE, "isPermanent": True,
    },
    {
        "properties": {
            "name": VOLUME_PROFILE2_3PAR1_PRIV, "description": "", "storagePool": STORESERV1_POOL1, "size": 1073741824,
            "provisioningType": "Thin", "isShareable": False, "snapshotPool": STORESERV1_POOL1
        },
        "templateUri": 'ROOT', "isPermanent": True,
    },
    {
        "properties": {
            "name": VOLUME_3PAR1_SHARED, "description": "", "storagePool": STORESERV1_POOL1, "size": 1073741824,
            "provisioningType": "Thin", "isShareable": True, "snapshotPool": STORESERV1_POOL1
        },
        "templateUri": 'ROOT', "isPermanent": True,
    },
    {
        "properties": {
            "name": VOLUME_PROFILE1_VSA1_PRIV, "description": "", "storagePool": STOREVIRTUAL1_POOL,
            "size": 1073741824, "dataProtectionLevel": "NetworkRaid5SingleParity", "provisioningType": "Thin",
            "isShareable": False, "isAdaptiveOptimizationEnabled": True
        },
        "templateUri": VOLUME_TEMPLATE_VSA1_RAID5_PRIVATE, "isPermanent": True,
    },
    {
        "properties": {
            "name": VOLUME_PROFILE2_VSA1_PRIV, "description": "", "storagePool": STOREVIRTUAL1_POOL,
            "size": 1073741824, "dataProtectionLevel": "NetworkRaid5SingleParity", "provisioningType": "Thin",
            "isShareable": False, "isAdaptiveOptimizationEnabled": True
        },
        "templateUri": VOLUME_TEMPLATE_VSA1_RAID5_PRIVATE, "isPermanent": True,
    },
    {
        "properties": {
            "name": VOLUME_VSA1_SHARED, "description": "", "storagePool": STOREVIRTUAL1_POOL,
            "size": 1073741824, "dataProtectionLevel": "NetworkRaid5SingleParity", "provisioningType": "Thin",
            "isShareable": True, "isAdaptiveOptimizationEnabled": True
        },
        "templateUri": VOLUME_TEMPLATE_VSA1_RAID5_SHARED, "isPermanent": True,
    },
    {
        "properties": {
            "name": VOLUME_PROFILE1_VSA2_PRIV, "description": "", "storagePool": STOREVIRTUAL2_POOL,
            "size": 1073741824, "dataProtectionLevel": "NetworkRaid0None", "provisioningType": "Thin",
            "isShareable": False, "isAdaptiveOptimizationEnabled": True
        },
        "templateUri": VOLUME_TEMPLATE_VSA2_RAID0_PRIVATE, "isPermanent": True,
    },
    {
        "properties": {
            "name": VOLUME_PROFILE2_VSA2_PRIV, "description": "", "storagePool": STOREVIRTUAL2_POOL,
            "size": 1073741824, "dataProtectionLevel": "NetworkRaid0None", "provisioningType": "Thin",
            "isShareable": False, "isAdaptiveOptimizationEnabled": True
        },
        "templateUri": 'ROOT', "isPermanent": True,
    },
    {
        "properties": {
            "name": VOLUME_VSA2_SHARED, "description": "", "storagePool": STOREVIRTUAL2_POOL,
            "size": 1073741824, "dataProtectionLevel": "NetworkRaid0None", "provisioningType": "Thin",
            "isShareable": True, "isAdaptiveOptimizationEnabled": True
        },
        "templateUri": 'ROOT', "isPermanent": True,
    },

]

existing_storage_volumes = [
    {
        "name": VOLUME_EXIST_VSA1_SHARED,
        'description': '',
        'storageSystemUri': STOREVIRTUAL1_NAME,
        'deviceVolumeName': VOLUME_EXIST_VSA1_SHARED,
        'isShareable': True
    },
    {
        "name": VOLUME_EXIST_VSA1_PRIV,
        'description': '',
        'storageSystemUri': STOREVIRTUAL1_NAME,
        'deviceVolumeName': VOLUME_EXIST_VSA1_PRIV,
        'isShareable': False
    },
]

# Profile bootable iSCSI connection
INITIATOR_GATEWAY = "192.168.0.1"
INITIATOR_SUBNET_MASK = "255.255.192.0"
INITIATOR_IP_1 = "192.168.22.63"
INITIATOR_IP_2 = "192.168.22.64"
VSA1_FIRST_BOOT_TARGET_IP = STOREVIRTUAL1_VIP
VSA2_FIRST_BOOT_TARGET_IP = STOREVIRTUAL2_VIP
VSA1_BOOT_TARGET_NAME_REGEX = 'REGEX:iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:\d*:'
VSA2_BOOT_TARGET_NAME_REGEX = 'REGEX:iqn.2015-11.com.hpe:storevirtual.vsa84-mg'

# Profiles
PROFILE_NAME_PREFIX = NAME_PREFIX
# NTS1 negative profiles, new volumes, server, EG and ENC
NTS1_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'nts1-profile1'
NTS1_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'nts1-profile2'
NTS1_PROFILE3_NAME = PROFILE_NAME_PREFIX + 'nts1-profile3'
NTS1_PROFILE4_NAME = PROFILE_NAME_PREFIX + 'nts1-profile4'
NTS1_PROFILE5_NAME = PROFILE_NAME_PREFIX + 'nts1-profile5'
NTS1_PROFILE6_NAME = PROFILE_NAME_PREFIX + 'nts1-profile6'
NTS1_PROFILE7_NAME = PROFILE_NAME_PREFIX + 'nts1-profile7'
NTS1_PROFILE8_NAME = PROFILE_NAME_PREFIX + 'nts1-profile8'
NTS1_PROFILE9_NAME = PROFILE_NAME_PREFIX + 'nts1-profile9'
VOLUME_NTS1_PROFILE_VOL1 = 'nts1-profile-vol1'
VOLUME_NTS1_PROFILE_VOL2 = 'nts1-profile-vol2'
NTS1_PROFILE_EG = EG1_NAME
NTS1_PROFILE_SERVER = ENC1SHBAY3
# NTS2 negative profiles, volumes, server, EG, and ENC
NTS2_PROFILE1_NAME = PROFILE_NAME_PREFIX + 'nts2-profile1'
NTS2_PROFILE2_NAME = PROFILE_NAME_PREFIX + 'nts2-profile2'
VOLUME_NTS2_VOL = 'nts2-vol'
NTS2_PROFILE1_SERVER = ENC3SHBAY3
NTS2_PROFILE1_EG = EG3_NAME
NTS2_PROFILE1_ENC = ENC3
NTS2_PROFILE2_SERVER = ENC1SHBAY5
NTS2_PROFILE2_EG = EG1_NAME
NTS2_PROFILE2_ENC = ENC1
# NTS3 profile, volumes, server, EG, and ENC
NTS3_PROFILE_NAME = PROFILE_NAME_PREFIX + 'nts3-profile'
NTS3_PROFILE_IQN = "iqn.2015-02.com.hpe:oneview-" + NTS3_PROFILE_NAME
VOLUME_NTS3_PROFILE_VOL1 = 'nts3-profile-vol1'
VOLUME_NTS3_PROFILE_VOL2 = 'nts3-profile-vol2'
NTS3_PROFILE_SERVER = ENC1SHBAY3
NTS3_PROFILE_EG = EG1_NAME
NTS3_PROFILE_ENC = ENC1
# NTS4 profile, volumes, server, EG, and ENC
NTS4_PROFILE_NAME = PROFILE_NAME_PREFIX + 'nts4-profile'
NTS4_PROFILE_IQN = "iqn.2015-02.com.hpe:oneview-" + NTS4_PROFILE_NAME
NTS4_PROFILE_IQN_EDIT = "iqn.2015-02.com.hpe:oneview-" + \
                        NTS4_PROFILE_NAME + '-new'
VOLUME_NTS4_PROFILE_3PAR1_EPH_PRIV = 'nts4-profile-3par-eph-priv'
VOLUME_NTS4_PROFILE_VSA1_EPH_PRIV_1 = 'nts4-profile-vsa1-eph-priv-1'
VOLUME_NTS4_PROFILE_VSA1_EPH_PRIV_2 = 'nts4-profile-vsa1-eph-priv-2'
VOLUME_NTS4_PROFILE_VSA2_EPH_PRIV_1 = 'nts4-profile-vsa2-eph-priv-1'
VOLUME_NTS4_PROFILE_VSA2_EPH_PRIV_2 = 'nts4-profile-vsa2-eph-priv-2'
NTS4_PROFILE_SAN_OS = "VMware (ESXi)"
NTS4_PROFILE_SERVER = ENC1SHBAY3
NTS4_PROFILE_EG = EG1_NAME
NTS4_PROFILE_ENC = ENC1
# PTS1 and PTS2 positive profiles and new volumes
PROFILE1_NAME = PROFILE_NAME_PREFIX + "profile1"
PROFILE1_IQN = "iqn.2015-02.com.hpe:oneview-" + PROFILE1_NAME
PROFILE1_IQN_EDIT = "iqn.2015-02.com.hpe:oneview-" + PROFILE1_NAME + '-new'
VOLUME_PROFILE1_3PAR1_PERM_PRIV = PROFILE_NAME_PREFIX + 'profile1-3par1-perm-priv'
VOLUME_PROFILE1_3PAR1_EPH_PRIV = PROFILE_NAME_PREFIX + 'profile1-3par1-eph-priv'
VOLUME_PROFILE1_VSA1_PERM_PRIV = PROFILE_NAME_PREFIX + 'profile1-vsa1-perm-priv'
VOLUME_PROFILE1_VSA1_EPH_PRIV = PROFILE_NAME_PREFIX + 'profile1-vsa1-eph-priv'
VOLUME_PROFILE1_VSA2_PERM_PRIV = PROFILE_NAME_PREFIX + 'profile1-vsa2-perm-priv'
VOLUME_PROFILE1_VSA2_EPH_PRIV = PROFILE_NAME_PREFIX + 'profile1-vsa2-eph-priv'
PROFILE2_NAME = PROFILE_NAME_PREFIX + "profile2"
PROFILE2_IQN = "iqn.2015-02.com.hpe:oneview-" + PROFILE2_NAME
PROFILE2_IQN_EDIT = "iqn.2015-02.com.hpe:oneview-" + PROFILE2_NAME + '-new'
VOLUME_PROFILE2_3PAR1_PERM_PRIV = PROFILE_NAME_PREFIX + 'profile2-3par1-perm-priv'
VOLUME_PROFILE2_3PAR1_EPH_PRIV = PROFILE_NAME_PREFIX + 'profile2-3par1-eph-priv'
VOLUME_PROFILE2_VSA1_PERM_PRIV = PROFILE_NAME_PREFIX + 'profile2-vsa1-perm-priv'
VOLUME_PROFILE2_VSA1_EPH_PRIV = PROFILE_NAME_PREFIX + 'profile2-vsa1-eph-priv'
VOLUME_PROFILE2_VSA2_PERM_PRIV = PROFILE_NAME_PREFIX + 'profile2-vsa2-perm-priv'
VOLUME_PROFILE2_VSA2_EPH_PRIV = PROFILE_NAME_PREFIX + 'profile2-vsa2-eph-priv'
# profiles server, EG, and ENC
PROFILE1_SERVER = ENC1SHBAY3
PROFILE1_EG = EG1_NAME
PROFILE1_ENC = ENC1
PROFILE1_MOVE_SERVER = ENC3SHBAY7
PROFILE1_MOVE_EG = EG3_NAME
PROFILE1_MOVE_ENC = ENC3
PROFILE2_SERVER = ENC1SHBAY5
PROFILE2_EG = EG1_NAME
PROFILE2_ENC = ENC1
PROFILE2_MOVE_SERVER = ENC3SHBAY3
PROFILE2_MOVE_EG = EG3_NAME
PROFILE2_MOVE_ENC = ENC3
# OVS17830 hostOSType
ESXI = "VMware (ESXi)"
OLD_RHE = "RHE Linux (5.x, 6.x)"
NEW_RHE = "RHE Linux (5.x, 6.x, 7.x)"
OLD_SUSE = "SuSE (10.x, 11.x)"
NEW_SUSE = "SuSE (10.x, 11.x, 12.x)"
# SV VA Storage Target REGEX
VSA1_STORAGE_PATH_TARGET_NAME_REGEX = 'REGEX:iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:\d*:'
VSA2_STORAGE_PATH_TARGET_NAME_REGEX = 'REGEX:iqn.2015-11.com.hpe:storevirtual.vsa84-mg'
CHAP_SECRET_REGEX = 'REGEX:.{16}'
MCHAP_SECRET_REGEX = CHAP_SECRET_REGEX

# Test Sets
# NTS1 Create profile to fail validation
# Bootable volume and non-bootable connection
nts1_profile1 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS1_PROFILE1_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS1_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS1_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:1", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:2", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": False, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "VMware (ESXi)", "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS1_PROFILE_VOL1,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL2_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL2_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": None,
            }
        ]

    }
}

# Bootable connection and non-bootable volume
nts1_profile2 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS1_PROFILE2_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS1_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS1_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1, "name": "", "functionType": "iSCSI", "portId": "Auto", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged", "mac": None, "wwpn": None, "wwnn": None,
                "ipv4": {
                    "ipAddressSource": "UserDefined", "subnetMask": INITIATOR_SUBNET_MASK, "gateway": "",
                    "ipAddress": INITIATOR_IP_1
                },
                "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume", "iscsi": None}
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "VMware (ESXi)", "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_NTS1_PROFILE_VOL1,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL1_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid5SingleParity"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL1_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": None,
            }]

    }
}

# Multiple bootable volumes
nts1_profile3 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS1_PROFILE3_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS1_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS1_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1, "name": "", "functionType": "iSCSI", "portId": "Auto", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged", "mac": None, "wwpn": None, "wwnn": None,
                "ipv4": {
                    "ipAddressSource": "UserDefined", "subnetMask": INITIATOR_SUBNET_MASK, "gateway": "",
                    "ipAddress": INITIATOR_IP_1
                },
                "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume", "iscsi": None}
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "VMware (ESXi)", "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_NTS1_PROFILE_VOL1,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL1_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid5SingleParity"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL1_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": None,
            }, {
                "id": 2,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_NTS1_PROFILE_VOL2,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL1_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL1_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": None,
            }]
    }
}

# Invalid lun=0 for MLPT VSA volume
nts1_profile4 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS1_PROFILE4_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS1_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS1_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:1", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:2", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": False, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "VMware (ESXi)", "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "NotBootable",
                "lun": 0,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS1_PROFILE_VOL1,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL2_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL2_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": None,
            }]
    }
}

# non-unique LUN number for MLPT VSA volumes
nts1_profile5 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS1_PROFILE5_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS1_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS1_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:1", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:2", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": False, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "VMware (ESXi)", "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "NotBootable",
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS1_PROFILE_VOL1,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL2_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL2_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": None,
            }, {
                "id": 2,
                "bootVolumePriority": "NotBootable",
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS1_PROFILE_VOL2,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL2_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL2_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": None,
            }]
    }
}

# Inviad lunType for SLPT VSA volume
nts1_profile6 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS1_PROFILE6_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS1_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS1_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 3, "name": "", "functionType": "Ethernet", "portId": "Flb 1:1", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 4, "name": "", "functionType": "Ethernet", "portId": "Flb 1:2", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": False}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "VMware (ESXi)", "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "NotBootable",
                "lun": 0,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS1_PROFILE_VOL1,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL1_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid5SingleParity"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL1_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": None,
            }]
    }
}

# No port configuration
nts1_profile7 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS1_PROFILE7_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS1_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS1_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:1", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:2", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": False, "order": ["HardDisk", "CD", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "VMware (ESXi)", "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS1_PROFILE_VOL1,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL1_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid5SingleParity"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL1_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": None,
            }]

    }
}

# Mixed paths for VSA volume, one enabled and the other disabled
nts1_profile8 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS1_PROFILE8_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS1_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS1_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 3, "name": "", "functionType": "Ethernet", "portId": "Flb 1:1", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 4, "name": "", "functionType": "Ethernet", "portId": "Flb 1:2", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": False}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "VMware (ESXi)", "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS1_PROFILE_VOL1,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL1_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid5SingleParity"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL1_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": None,
            }]

    }
}

nts1_negative_profile_tasks = [
    {
        'keyword': 'Add Server Profile',
        'argument': nts1_profile1.copy(),
        'taskState': 'Error',
        'errorMessage': 'Bootable_volume_nonbootable_connection'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': nts1_profile2.copy(),
        'taskState': 'Error',
        'errorMessage': 'SP_Bootable_connection_nonbootable_volume'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': nts1_profile3.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_bootable_volumes'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': nts1_profile4.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalidate_LUN_MLPT_VSA'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': nts1_profile5.copy(),
        'taskState': 'Error',
        'errorMessage': 'LUN_not_unique_MLPT_VSA'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': nts1_profile6.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_lunType_SLPT_VSA'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': nts1_profile7.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_NETWORK_ON_STORAGE_PATH'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': nts1_profile8.copy(),
        'taskState': 'Error',
        'errorMessage': 'Mixed_paths_VSA'
    },
]

# NTS 2, create SP to fail SAN validation
nts2_profile1 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS2_PROFILE1_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS2_PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + NTS2_PROFILE1_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:1", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:2", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "VMware (ESXi)", "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "NotBootable",
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL2_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid6DualParity"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL2_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": None,
            }]
    }
}
# Attach private presented volume
nts2_profile2 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS2_PROFILE2_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS2_PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + NTS2_PROFILE2_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 3, "name": "", "functionType": "Ethernet", "portId": "Flb 1:1", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 4, "name": "", "functionType": "Ethernet", "portId": "Flb 1:2", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
    "bootMode": {"manageMode": True, "mode": "BIOS"},
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "VMware (ESXi)", "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_EXIST_VSA1_PRIV,
            }]
    }
}

nts2_profiles_delete = [
    nts2_profile1.copy(),
    nts2_profile2.copy(),
]

nts2_negative_profile_tasks = [
    {
        'keyword': 'Add Server Profile',
        'argument': nts2_profile1.copy(),
        'taskState': 'Error',
        'errorMessage': 'Unsupported_DataProtectionLevel_VSA'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': nts2_profile2.copy(),
        'taskState': 'Error',
        'errorMessage': 'SP_attach_private_presented_volume'
    },
]

# NTS3, edit profile to fail validation
nts3_profile_create = {
    "type": SERVER_PROFILE_TYPE, "name": NTS3_PROFILE_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS3_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS3_PROFILE_EG,
    "enclosureUri": 'ENC:' + NTS3_PROFILE_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": NTS3_PROFILE_IQN,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 2, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 3, "name": "", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 4, "name": "", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:1-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:2-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
}

# Bootable volume and non-bootable connection
nts3_profile_edit1 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS3_PROFILE_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS3_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS3_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 2, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 3, "name": "", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 4, "name": "", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:1-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:2-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": False, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "VMware (ESXi)", "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS3_PROFILE_VOL1,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL2_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL2_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": None,
            }]

    }
}

# Bootable connection and non-bootable volume
nts3_profile_edit2 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS3_PROFILE_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS3_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS3_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 2, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 3, "name": "", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None,
                "ipv4": {
                    "ipAddressSource": "UserDefined", "subnetMask": INITIATOR_SUBNET_MASK, "gateway": "",
                    "ipAddress": INITIATOR_IP_1
                },
                "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume", "iscsi": None}
            },
            {
                "id": 4, "name": "", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:1-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:2-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "VMware (ESXi)", "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_NTS3_PROFILE_VOL1,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL1_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid5SingleParity"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL1_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": None,
            }]
    }
}

# Multiple bootable volumes
nts3_profile_edit3 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS3_PROFILE_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS3_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS3_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 2, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 3, "name": "", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None,
                "ipv4": {
                    "ipAddressSource": "UserDefined", "subnetMask": INITIATOR_SUBNET_MASK, "gateway": "",
                    "ipAddress": INITIATOR_IP_1
                },
                "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume", "iscsi": None},
            },
            {
                "id": 4, "name": "", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:1-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:2-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "VMware (ESXi)", "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_NTS3_PROFILE_VOL1,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL1_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid5SingleParity"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL1_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": None,
            }, {
                "id": 2,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_NTS3_PROFILE_VOL2,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL1_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL1_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": None,
            }]
    }
}

# Invalid lun=0 for MLPT VSA volume
nts3_profile_edit4 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS3_PROFILE_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS3_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS3_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 2, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 3, "name": "", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 4, "name": "", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:1-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:2-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": False, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "VMware (ESXi)", "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "NotBootable",
                "lun": 0,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS3_PROFILE_VOL1,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL2_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL2_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": None,
            }]
    }
}

# non-unique LUN number for MLPT VSA volumes
nts3_profile_edit5 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS3_PROFILE_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS3_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS3_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 2, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 3, "name": "", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 4, "name": "", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:1-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:2-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": False, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "VMware (ESXi)", "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "NotBootable",
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS3_PROFILE_VOL1,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL2_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL2_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": None,
            }, {
                "id": 2,
                "bootVolumePriority": "NotBootable",
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS3_PROFILE_VOL2,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL2_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL2_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": None,
            }]
    }
}

# Inviad lunType for SLPT VSA volume
nts3_profile_edit6 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS3_PROFILE_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS3_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS3_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 2, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 3, "name": "", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 4, "name": "", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:1-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:2-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": False}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "VMware (ESXi)", "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "NotBootable",
                "lun": 0,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS3_PROFILE_VOL1,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL1_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid5SingleParity"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL1_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": None,
            }]
    }
}

# No port configuration
nts3_profile_edit7 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS3_PROFILE_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS3_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS3_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 2, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 3, "name": "", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 4, "name": "", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:1-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:2-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": False, "order": ["HardDisk", "CD", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "VMware (ESXi)", "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS3_PROFILE_VOL1,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL1_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid5SingleParity"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL1_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": None,
            }]
    }
}

# Mixed paths for VSA volume, one enabled and the other disabled
nts3_profile_edit8 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS3_PROFILE_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS3_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS3_PROFILE_EG,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 2, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 3, "name": "", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 4, "name": "", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:1-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:2-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": False}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "VMware (ESXi)", "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS3_PROFILE_VOL1,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL1_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid5SingleParity"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL1_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": None,
            }]
    }
}

nts3_profiles_create = [
    nts3_profile_create.copy(),
]

nts3_negative_profile_tasks = [
    {
        'keyword': 'Edit Server Profile',
        'argument': nts3_profile_edit1.copy(),
        'taskState': 'Error',
        'errorMessage': 'Bootable_volume_nonbootable_connection'
    },
    {
        'keyword': 'Edit Server Profile',
        'argument': nts3_profile_edit2.copy(),
        'taskState': 'Error',
        'errorMessage': 'SP_Bootable_connection_nonbootable_volume'
    },
    {
        'keyword': 'Edit Server Profile',
        'argument': nts3_profile_edit3.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_bootable_volumes'
    },
    {
        'keyword': 'Edit Server Profile',
        'argument': nts3_profile_edit4.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalidate_LUN_MLPT_VSA'
    },
    {
        'keyword': 'Edit Server Profile',
        'argument': nts3_profile_edit5.copy(),
        'taskState': 'Error',
        'errorMessage': 'LUN_not_unique_MLPT_VSA'
    },
    {
        'keyword': 'Edit Server Profile',
        'argument': nts3_profile_edit6.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_lunType_SLPT_VSA'
    },
    {
        'keyword': 'Edit Server Profile',
        'argument': nts3_profile_edit7.copy(),
        'taskState': 'Error',
        'errorMessage': 'VSA_not_attached_to_network'
    },
    {
        'keyword': 'Edit Server Profile',
        'argument': nts3_profile_edit8.copy(),
        'taskState': 'Error',
        'errorMessage': 'Mixed_paths_VSA'
    },

]
# NTS4, edit profile SAN attribure to fail power asssert test
nts4_profile_create = {
    "type": SERVER_PROFILE_TYPE, "name": NTS4_PROFILE_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS4_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS4_PROFILE_EG,
    "enclosureUri": 'ENC:' + NTS4_PROFILE_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": NTS4_PROFILE_IQN,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 2, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 3, "name": "", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 4, "name": "", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 5, "name": "", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4":
                {
                    "ipAddressSource": "UserDefined", "subnetMask": INITIATOR_SUBNET_MASK, "gateway": "",
                    "ipAddress": INITIATOR_IP_1
                },
                "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume", "iscsi": None}
            },
            {
                "id": 6, "name": "", "functionType": "iSCSI", "portId": "Mezz 1:2-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": ESXI, "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS4_PROFILE_3PAR1_EPH_PRIV,
                        "description": "",
                        "storagePool": "SPOOL:" + STORESERV1_POOL1,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                    },
                    "templateUri": "ROOT:" + STORESERV1_POOL1,
                },
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": None,
            }, {
                "id": 2,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS4_PROFILE_VSA1_EPH_PRIV_1,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL1_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid5SingleParity"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL1_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": None,
            }, {
                "id": 3,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS4_PROFILE_VSA1_EPH_PRIV_2,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL1_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid5SingleParity"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL1_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": None,
            }, {
                "id": 4,
                "bootVolumePriority": "Primary",
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS4_PROFILE_VSA2_EPH_PRIV_1,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL2_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL2_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": None,
            }, {
                "id": 5,
                "bootVolumePriority": "NotBootable",
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": []
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": []
                    }],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS4_PROFILE_VSA2_EPH_PRIV_2,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL2_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None"
                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL2_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": None,
            }]
    }
}

nts4_profile_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": NTS4_PROFILE_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS4_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS4_PROFILE_EG,
    "enclosureUri": 'ENC:' + NTS4_PROFILE_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": NTS4_PROFILE_IQN,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:1",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:2",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
            },
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 5, "name": "", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                    "ipAddressSource": "UserDefined", "subnetMask": INITIATOR_SUBNET_MASK, "gateway": "",
                    "ipAddress": INITIATOR_IP_1
                },
                "boot": {
                    "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                    "iscsi": {
                        'mutualChapName': NTS4_PROFILE_IQN, 'chapName': NTS4_PROFILE_IQN,
                        'initiatorName': NTS4_PROFILE_IQN,
                        'chapLevel': 'MutualChap', 'initiatorNameSource': 'ProfileInitiatorName',
                        'bootTargetName': VSA2_BOOT_TARGET_NAME_REGEX,
                        'bootTargetLun': '1', 'firstBootTargetIp': VSA2_FIRST_BOOT_TARGET_IP
                    }
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Mezz 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": ESXI, "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "state": "Attached",
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
                "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_3PAR1_EPH_PRIV,
            }, {
                "id": 2,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_VSA1_EPH_PRIV_1,
            }, {
                "id": 3,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_VSA1_EPH_PRIV_2,
            }, {
                "id": 4,
                "bootVolumePriority": "Primary",
                "lun": 1,
                "lunType": "Manual",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"
                            }
                        ]
                    },
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_VSA2_EPH_PRIV_1,
            }, {
                "id": 5,
                "bootVolumePriority": "NotBootable",
                "lun": 2,
                "lunType": "Manual",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_VSA2_EPH_PRIV_2,
            }]
    }
}

# edit bootable volume
nts4_profile_edit1 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS4_PROFILE_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS4_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS4_PROFILE_EG,
    "enclosureUri": 'ENC:' + NTS4_PROFILE_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": NTS4_PROFILE_IQN,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:1",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:2",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
            },
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 5, "name": "", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                    "ipAddressSource": "UserDefined", "subnetMask": INITIATOR_SUBNET_MASK, "gateway": "",
                    "ipAddress": INITIATOR_IP_1
                },
                "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume", "iscsi": None},
            },
            {
                "id": 6,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Mezz 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": ESXI, "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "NotBootable",
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
                "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_3PAR1_EPH_PRIV,
            }, {
                "id": 2,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_VSA1_EPH_PRIV_1,
            }, {
                "id": 3,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_VSA1_EPH_PRIV_2,
            }, {
                "id": 4,
                "bootVolumePriority": "NotBootable",
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"
                            }
                        ]
                    },
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_VSA2_EPH_PRIV_1,
            }, {
                "id": 5,
                "bootVolumePriority": "Primary",
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_VSA2_EPH_PRIV_2,
            }]
    }
}

# edit bootable iSCSI connection
nts4_profile_edit2 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS4_PROFILE_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS4_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS4_PROFILE_EG,
    "enclosureUri": 'ENC:' + NTS4_PROFILE_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": NTS4_PROFILE_IQN,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:1",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:2",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
            },
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {},
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 5, "name": "", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                    "ipAddressSource": "UserDefined", "subnetMask": INITIATOR_SUBNET_MASK, "gateway": "",
                    "ipAddress": INITIATOR_IP_2
                },
                "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume", "iscsi": None},
            },
            {
                "id": 6,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Mezz 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": ESXI, "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "NotBootable",
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
                "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_3PAR1_EPH_PRIV,
            }, {
                "id": 2,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"
                            }
                        ]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_VSA1_EPH_PRIV_1,
            }, {
                "id": 3,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_VSA1_EPH_PRIV_2,
            }, {
                "id": 4,
                "bootVolumePriority": "Primary",
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_VSA2_EPH_PRIV_1,
            }, {
                "id": 5,
                "bootVolumePriority": "NotBootable",
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"
                            }]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [{
                            "ipAddress": STOREVIRTUAL2_VIP,
                            "tcpPort": "3260"
                        }]
                    },
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_VSA2_EPH_PRIV_2,
            }]
    }
}

# edit profile iQN
nts4_profile_edit3 = {
    "type": SERVER_PROFILE_TYPE, "name": NTS4_PROFILE_NAME, "description": "",
    "serverHardwareUri": 'SH:' + NTS4_PROFILE_SERVER, "enclosureGroupUri": 'EG:' + NTS4_PROFILE_EG,
    "enclosureUri": 'ENC:' + NTS4_PROFILE_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": NTS4_PROFILE_IQN_EDIT,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:1",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:2",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
            },
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {}
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 5, "name": "", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                    "ipAddressSource": "UserDefined", "subnetMask": INITIATOR_SUBNET_MASK, "gateway": "",
                    "ipAddress": INITIATOR_IP_1
                },
                "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume", "iscsi": None},
            },
            {
                "id": 6,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Mezz 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": ESXI, "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "bootVolumePriority": "NotBootable",
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
            "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_3PAR1_EPH_PRIV,
        }, {
            "id": 2,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260"
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260"
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_VSA1_EPH_PRIV_1,
        }, {
            "id": 3,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260"
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260"
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_VSA1_EPH_PRIV_2,
        }, {
            "id": 4,
            "bootVolumePriority": "Primary",
            "lun": 1,
            "lunType": "Manual",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260"
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260"
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_VSA2_EPH_PRIV_1,
        }, {
            "id": 5,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260"
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260"
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_NTS4_PROFILE_VSA2_EPH_PRIV_2,
        }]
    }
}

nts4_profiles_create = [
    nts4_profile_create.copy(),
]

nts4_profiles_create_expected = [
    nts4_profile_create_expected.copy(),
]

nts4_negative_profile_tasks = [
    {
        'keyword': 'Edit Server Profile',
        'argument': nts4_profile_edit1.copy(),
        'taskState': 'Error',
        'errorMessage': 'Server_Not_off_Profile_Edit'
    },
    {
        'keyword': 'Edit Server Profile',
        'argument': nts4_profile_edit2.copy(),
        'taskState': 'Error',
        'errorMessage': 'Server_Not_off_Profile_Edit'
    },
    {
        'keyword': 'Edit Server Profile',
        'argument': nts4_profile_edit3.copy(),
        'taskState': 'Error',
        'errorMessage': 'Server_Not_off_Profile_Edit'
    },
]

# PTS1 and PTS2 profiles
# Profile1, existing and new volume attachments, redundant storage paths
profile1_create = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE1_NAME, "description": "",
    "serverHardwareUri": 'SH:' + PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PROFILE1_EG,
    "enclosureUri": 'ENC:' + PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": PROFILE1_IQN,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 2, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 3, "name": "", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 4, "name": "", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:1-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:2-a", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": OLD_RHE, "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 1,
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "isEnabled": True,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                    "targets": []
                }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_3PAR1_PRIV,
        }, {
            "id": 2,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,
        }, {
            "id": 3,
            "bootVolumePriority": "NotBootable",
            "lun": 3,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": VOLUME_PROFILE1_3PAR1_PERM_PRIV,
                    "description": "",
                    "storagePool": "SPOOL:" + STORESERV1_POOL1,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                },
                "templateUri": "ROOT:" + STORESERV1_POOL1,
            },
            "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
            "volumeUri": None,
        }, {
            "id": 4,
            "bootVolumePriority": "NotBootable",
            "lun": 4,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": VOLUME_PROFILE1_3PAR1_EPH_PRIV,
                    "description": "",
                    "storagePool": "SPOOL:" + STORESERV1_POOL1,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                },
                "templateUri": "ROOT:" + STORESERV1_POOL1,
            },
            "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
            "volumeUri": None,
        }, {
            "id": 11,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA1_PRIV,
        }, {
            "id": 12,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA1_SHARED,
        }, {
            "id": 13,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": VOLUME_PROFILE1_VSA1_PERM_PRIV,
                    "description": "",
                    "storagePool": "SPOOL:" + STOREVIRTUAL1_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity"
                },
                "templateUri": "ROOT:" + STOREVIRTUAL1_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
            "volumeUri": None,
        }, {
            "id": 14,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": VOLUME_PROFILE1_VSA1_EPH_PRIV,
                    "description": "",
                    "storagePool": "SPOOL:" + STOREVIRTUAL1_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity"
                },
                "templateUri": "ROOT:" + STOREVIRTUAL1_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
            "volumeUri": None,
        }, {
            "id": 21,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA2_PRIV,
        }, {
            "id": 22,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
        }, {
            "id": 23,
            "bootVolumePriority": "NotBootable",
            "lun": 3,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": VOLUME_PROFILE1_VSA2_PERM_PRIV,
                    "description": "",
                    "storagePool": "SPOOL:" + STOREVIRTUAL2_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid0None"
                },
                "templateUri": "ROOT:" + STOREVIRTUAL2_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
            "volumeUri": None,
        }, {
            "id": 24,
            "bootVolumePriority": "NotBootable",
            "lun": 4,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": VOLUME_PROFILE1_VSA2_EPH_PRIV,
                    "description": "",
                    "storagePool": "SPOOL:" + STOREVIRTUAL2_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid0None"
                },
                "templateUri": "ROOT:" + STOREVIRTUAL2_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
            "volumeUri": None,
        }]
    }
}

profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE1_NAME, "description": "",
    "serverHardwareUri": 'SH:' + PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PROFILE1_EG,
    "enclosureUri": 'ENC:' + PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": PROFILE1_IQN,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "",
                "state": "Deployed",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:1",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
            },
            {
                "id": 2,
                "name": "",
                "state": "Deployed",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:2",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
            },
            {
                "id": 3,
                "name": "",
                "state": "Deployed",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 4,
                "name": "",
                "state": "Deployed",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 5,
                "name": "",
                "state": "Deployed",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            },
            {
                "id": 6,
                "name": "",
                "state": "Deployed",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": OLD_RHE, "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "state": "Attached",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_3PAR1_PRIV,
        }, {
            "id": 2,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "state": "Attached",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,
        }, {
            "id": 3,
            "bootVolumePriority": "NotBootable",
            "lun": 3,
            "lunType": "Manual",
            "state": "Attached",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_3PAR1_PERM_PRIV,
        }, {
            "id": 4,
            "bootVolumePriority": "NotBootable",
            "lun": 4,
            "lunType": "Manual",
            "state": "Attached",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_3PAR1_EPH_PRIV,
        }, {
            "id": 11,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE1_VSA1_PRIV
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE1_VSA1_PRIV
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA1_PRIV,
        }, {
            "id": 12,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_VSA1_SHARED
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_VSA1_SHARED
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA1_SHARED,
        }, {
            "id": 13,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE1_VSA1_PERM_PRIV
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE1_VSA1_PERM_PRIV
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA1_PERM_PRIV,
        }, {
            "id": 14,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE1_VSA1_EPH_PRIV
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE1_VSA1_EPH_PRIV
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA1_EPH_PRIV,
        }, {
            "id": 21,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA2_PRIV,
        }, {
            "id": 22,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
        }, {
            "id": 23,
            "bootVolumePriority": "NotBootable",
            "lun": 3,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA2_PERM_PRIV,
        }, {
            "id": 24,
            "bootVolumePriority": "NotBootable",
            "lun": 4,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA2_EPH_PRIV,
        }],
        "sanSystemCredentials":
            [
                {
                    "chapSecret": CHAP_SECRET_REGEX,
                    "chapLevel": "MutualChap",
                    "chapSource": "AutoGenerated",
                    "chapName": PROFILE1_IQN,
                    "mutualChapName": PROFILE1_IQN,
                    "mutualChapSecret": MCHAP_SECRET_REGEX,
                    "storageSystemUri": "REGEX:/rest/storage-systems/\w{8}(-\w{4}){3}-\w{12}"
                },
                {
                    "chapSecret": CHAP_SECRET_REGEX,
                    "chapLevel": "MutualChap",
                    "chapSource": "AutoGenerated",
                    "chapName": PROFILE1_IQN,
                    "mutualChapName": PROFILE1_IQN,
                    "mutualChapSecret": MCHAP_SECRET_REGEX,
                    "storageSystemUri": "REGEX:/rest/storage-systems/\w{8}(-\w{4}){3}-\w{12}"
                }
        ],
    }
}

profile1_efuse_off_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE1_NAME, "description": "",
    "enclosureGroupUri": 'EG:' + PROFILE1_EG, "enclosureUri": 'ENC:' + PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": PROFILE1_IQN,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "",
                "state": "Reserved",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:1",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
            },
            {
                "id": 2,
                "name": "",
                "state": "Reserved",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:2",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
            },
            {
                "id": 3,
                "name": "",
                "state": "Reserved",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 4,
                "name": "",
                "state": "Reserved",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 5,
                "name": "",
                "state": "Reserved",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            },
            {
                "id": 6,
                "name": "",
                "state": "Reserved",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": OLD_RHE, "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "state": "Reserved",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_3PAR1_PRIV,
        }, {
            "id": 2,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "state": "Reserved",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,
        }, {
            "id": 3,
            "bootVolumePriority": "NotBootable",
            "lun": 3,
            "lunType": "Manual",
            "state": "Reserved",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_3PAR1_PERM_PRIV,
        }, {
            "id": 4,
            "bootVolumePriority": "NotBootable",
            "lun": 4,
            "lunType": "Manual",
            "state": "Reserved",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_3PAR1_EPH_PRIV,
        }, {
            "id": 11,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Reserved",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA1_PRIV,
        }, {
            "id": 12,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Reserved",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA1_SHARED,
        }, {
            "id": 13,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Reserved",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA1_PERM_PRIV,
        }, {
            "id": 14,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Reserved",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA1_EPH_PRIV,
        }, {
            "id": 21,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "state": "Reserved",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA2_PRIV,
        }, {
            "id": 22,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "state": "Reserved",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
        }, {
            "id": 23,
            "bootVolumePriority": "NotBootable",
            "lun": 3,
            "lunType": "Manual",
            "state": "Reserved",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA2_PERM_PRIV,
        }, {
            "id": 24,
            "bootVolumePriority": "NotBootable",
            "lun": 4,
            "lunType": "Manual",
            "state": "Reserved",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA2_EPH_PRIV,
        }],
        "sanSystemCredentials":
            [
                {
                    "chapSecret": CHAP_SECRET_REGEX,
                    "chapLevel": "MutualChap",
                    "chapSource": "AutoGenerated",
                    "chapName": PROFILE1_IQN,
                    "mutualChapName": PROFILE1_IQN,
                    "mutualChapSecret": MCHAP_SECRET_REGEX,
                    "storageSystemUri": "REGEX:/rest/storage-systems/\w{8}(-\w{4}){3}-\w{12}"
                },
                {
                    "chapSecret": CHAP_SECRET_REGEX,
                    "chapLevel": "MutualChap",
                    "chapSource": "AutoGenerated",
                    "chapName": PROFILE1_IQN,
                    "mutualChapName": PROFILE1_IQN,
                    "mutualChapSecret": MCHAP_SECRET_REGEX,
                    "storageSystemUri": "REGEX:/rest/storage-systems/\w{8}(-\w{4}){3}-\w{12}"
                }
        ],
    }
}

# Profile1, existing and new volume attachments, non-redudant storage
# path, profile iQN
profile1_edit = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE1_NAME, "description": "",
    "serverHardwareUri": 'SH:' + PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PROFILE1_EG,
    "enclosureUri": 'ENC:' + PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": PROFILE1_IQN_EDIT,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 2, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 3, "name": "", "functionType": "iSCSI", "portId": "Flb 1:1", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 4, "name": "", "functionType": "iSCSI", "portId": "Flb 1:2", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:1", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:2", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": OLD_RHE, "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 1,
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "isEnabled": False,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                    "targets": []
                }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_3PAR1_PRIV,
        }, {
            "id": 2,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": False,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,
        }, {
            "id": 3,
            "bootVolumePriority": "NotBootable",
            "lun": 3,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": False,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_3PAR1_PERM_PRIV,
        }, {
            "id": 4,
            "bootVolumePriority": "NotBootable",
            "lun": 4,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": False,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_3PAR1_EPH_PRIV,
        }, {
            "id": 11,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA1_PRIV,
        }, {
            "id": 12,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA1_SHARED,
        }, {
            "id": 13,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA1_PERM_PRIV,
        }, {
            "id": 14,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA1_EPH_PRIV,
        }, {
            "id": 21,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA2_PRIV,
        }, {
            "id": 22,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
        }, {
            "id": 23,
            "bootVolumePriority": "NotBootable",
            "lun": 3,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA2_PERM_PRIV,
        }, {
            "id": 24,
            "bootVolumePriority": "NotBootable",
            "lun": 4,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA2_EPH_PRIV,
        }]
    }
}

profile1_edit_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE1_NAME, "description": "",
    "serverHardwareUri": 'SH:' + PROFILE1_SERVER, "enclosureGroupUri": 'EG:' + PROFILE1_EG,
    "enclosureUri": 'ENC:' + PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": PROFILE1_IQN_EDIT,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "",
                "state": "Deployed",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:1",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
            },
            {
                "id": 2,
                "name": "",
                "state": "Deployed",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:2",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
            },
            {
                "id": 3,
                "name": "",
                "state": "Deployed",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 4,
                "name": "",
                "state": "Deployed",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 5,
                "name": "",
                "state": "Deployed",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            },
            {
                "id": 6,
                "name": "",
                "state": "Deployed",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": OLD_RHE, "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 1,
                    "targetSelector": "Auto",
                },
                {
                    "isEnabled": False,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_3PAR1_PRIV,
        }, {
            "id": 2,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 1,
                    "targetSelector": "Auto",
                },
                {
                    "isEnabled": False,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,
        }, {
            "id": 3,
            "bootVolumePriority": "NotBootable",
            "lun": 3,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 1,
                    "targetSelector": "Auto",
                },
                {
                    "isEnabled": False,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_3PAR1_PERM_PRIV,
        }, {
            "id": 4,
            "bootVolumePriority": "NotBootable",
            "lun": 4,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 1,
                    "targetSelector": "Auto",
                },
                {
                    "isEnabled": False,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_3PAR1_EPH_PRIV,
        }, {
            "id": 11,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE1_VSA1_PRIV
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA1_PRIV,
        }, {
            "id": 12,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_VSA1_SHARED
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA1_SHARED,
        }, {
            "id": 13,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE1_VSA1_PERM_PRIV
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA1_PERM_PRIV,
        }, {
            "id": 14,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE1_VSA1_EPH_PRIV
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA1_EPH_PRIV,
        }, {
            "id": 21,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA2_PRIV,
        }, {
            "id": 22,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
        }, {
            "id": 23,
            "bootVolumePriority": "NotBootable",
            "lun": 3,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA2_PERM_PRIV,
        }, {
            "id": 24,
            "bootVolumePriority": "NotBootable",
            "lun": 4,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA2_EPH_PRIV,
        }],
        "sanSystemCredentials":
            [
                {
                    "chapSecret": CHAP_SECRET_REGEX,
                    "chapLevel": "MutualChap",
                    "chapSource": "AutoGenerated",
                    "chapName": PROFILE1_IQN,
                    "mutualChapName": PROFILE1_IQN,
                    "mutualChapSecret": MCHAP_SECRET_REGEX,
                    "storageSystemUri": "REGEX:/rest/storage-systems/\w{8}(-\w{4}){3}-\w{12}"
                },
                {
                    "chapSecret": CHAP_SECRET_REGEX,
                    "chapLevel": "MutualChap",
                    "chapSource": "AutoGenerated",
                    "chapName": PROFILE1_IQN,
                    "mutualChapName": PROFILE1_IQN,
                    "mutualChapSecret": MCHAP_SECRET_REGEX,
                    "storageSystemUri": "REGEX:/rest/storage-systems/\w{8}(-\w{4}){3}-\w{12}"
                }
        ],
    }
}

# Profile1 move
profile1_move = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE1_NAME, "description": "",
    "serverHardwareUri": 'SH:' + PROFILE1_MOVE_SERVER, "enclosureGroupUri": 'EG:' + PROFILE1_MOVE_EG,
    "enclosureUri": 'ENC:' + PROFILE1_MOVE_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": PROFILE1_IQN_EDIT,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 3, "name": "", "functionType": "iSCSI", "portId": "Flb 1:1", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 4, "name": "", "functionType": "iSCSI", "portId": "Flb 1:2", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Flb 2:1", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Flb 2:2", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": False, "order": ["HardDisk"]},
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": NEW_RHE, "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 11,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA1_PRIV,
        }, {
            "id": 12,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA1_SHARED,
        }, {
            "id": 21,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA2_PRIV,
        }, {
            "id": 22,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
        }]
    }
}

profile1_move_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE1_NAME, "description": "",
    "serverHardwareUri": 'SH:' + PROFILE1_MOVE_SERVER, "enclosureGroupUri": 'EG:' + PROFILE1_MOVE_EG,
    "enclosureUri": 'ENC:' + PROFILE1_MOVE_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": PROFILE1_IQN_EDIT,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 3,
                "name": "",
                "state": "Deployed",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 4,
                "name": "",
                "state": "Deployed",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 5,
                "name": "",
                "state": "Deployed",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            },
            {
                "id": 6,
                "name": "",
                "state": "Deployed",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {"manageBoot": False, "order": []},
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": NEW_RHE, "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 11,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE1_VSA1_PRIV
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA1_PRIV,
        }, {
            "id": 12,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_VSA1_SHARED
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA1_SHARED,
        }, {
            "id": 21,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE1_VSA2_PRIV,
        }, {
            "id": 22,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
        }],
        "sanSystemCredentials":
            [
                {
                    "chapSecret": CHAP_SECRET_REGEX,
                    "chapLevel": "MutualChap",
                    "chapSource": "AutoGenerated",
                    "chapName": PROFILE1_IQN,
                    "mutualChapName": PROFILE1_IQN,
                    "mutualChapSecret": MCHAP_SECRET_REGEX,
                    "storageSystemUri": "REGEX:/rest/storage-systems/\w{8}(-\w{4}){3}-\w{12}"
                },
                {
                    "chapSecret": CHAP_SECRET_REGEX,
                    "chapLevel": "MutualChap",
                    "chapSource": "AutoGenerated",
                    "chapName": PROFILE1_IQN,
                    "mutualChapName": PROFILE1_IQN,
                    "mutualChapSecret": MCHAP_SECRET_REGEX,
                    "storageSystemUri": "REGEX:/rest/storage-systems/\w{8}(-\w{4}){3}-\w{12}"
                }
        ],
    }
}
# Profile2, existing volume attachments, redundant storage paths
profile2_create = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE2_NAME, "description": "",
    "serverHardwareUri": 'SH:' + PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PROFILE2_EG,
    "enclosureUri": 'ENC:' + PROFILE2_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": PROFILE2_IQN,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 2, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 3, "name": "", "functionType": "iSCSI", "portId": "Flb 1:1", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 4, "name": "", "functionType": "iSCSI", "portId": "Flb 1:2", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:1", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:2", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
    "bootMode": {"manageMode": True, "mode": "BIOS"},
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": NEW_SUSE, "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 1,
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "isEnabled": True,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                    "targets": []
                }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_3PAR1_PRIV,
        }, {
            "id": 2,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,
        }, {
            "id": 11,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_PRIV,
        }, {
            "id": 12,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA1_SHARED,
        }, {
            "id": 21,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_PRIV,
        }, {
            "id": 22,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
        }]

    }
}

profile2_create_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE2_NAME, "description": "",
    "serverHardwareUri": 'SH:' + PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PROFILE2_EG,
    "enclosureUri": 'ENC:' + PROFILE2_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": PROFILE2_IQN,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "",
                "state": "Deployed",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:1",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
            },
            {
                "id": 2,
                "name": "",
                "state": "Deployed",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:2",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
            },
            {
                "id": 3,
                "name": "",
                "state": "Deployed",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 4,
                "name": "",
                "state": "Deployed",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 5,
                "name": "",
                "state": "Deployed",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            },
            {
                "id": 6,
                "name": "",
                "state": "Deployed",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
    "bootMode": {"manageMode": True, "mode": "BIOS"},
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": NEW_SUSE, "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "state": "Attached",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_3PAR1_PRIV,
        }, {
            "id": 2,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "state": "Attached",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,
        }, {
            "id": 11,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE2_VSA1_PRIV
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE2_VSA1_PRIV
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_PRIV,
        }, {
            "id": 12,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_VSA1_SHARED
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_VSA1_SHARED
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA1_SHARED,
        }, {
            "id": 21,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_PRIV,
        }, {
            "id": 22,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
        }],
        "sanSystemCredentials":
            [
                {
                    "chapSecret": CHAP_SECRET_REGEX,
                    "chapLevel": "MutualChap",
                    "chapSource": "AutoGenerated",
                    "chapName": PROFILE2_IQN,
                    "mutualChapName": PROFILE2_IQN,
                    "mutualChapSecret": MCHAP_SECRET_REGEX,
                    "storageSystemUri": "REGEX:/rest/storage-systems/\w{8}(-\w{4}){3}-\w{12}"
                },
                {
                    "chapSecret": CHAP_SECRET_REGEX,
                    "chapLevel": "MutualChap",
                    "chapSource": "AutoGenerated",
                    "chapName": PROFILE2_IQN,
                    "mutualChapName": PROFILE2_IQN,
                    "mutualChapSecret": MCHAP_SECRET_REGEX,
                    "storageSystemUri": "REGEX:/rest/storage-systems/\w{8}(-\w{4}){3}-\w{12}"
                }
        ],
    }
}

profile2_efuse_off_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE2_NAME, "description": "",
    "enclosureGroupUri": 'EG:' + PROFILE2_EG, "enclosureUri": 'ENC:' + PROFILE2_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": PROFILE2_IQN,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "",
                "state": "Reserved",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:1",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
            },
            {
                "id": 2,
                "name": "",
                "state": "Reserved",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:2",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
            },
            {
                "id": 3,
                "name": "",
                "state": "Reserved",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 4,
                "name": "",
                "state": "Reserved",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 5,
                "name": "",
                "state": "Reserved",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            },
            {
                "id": 6,
                "name": "",
                "state": "Reserved",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
    "bootMode": {"manageMode": True, "mode": "BIOS"},
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": NEW_SUSE, "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "state": "Reserved",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_3PAR1_PRIV,
        }, {
            "id": 2,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "state": "Reserved",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,
        }, {
            "id": 11,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Reserved",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_PRIV,
        }, {
            "id": 12,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Reserved",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA1_SHARED,
        }, {
            "id": 21,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "state": "Reserved",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_PRIV,
        }, {
            "id": 22,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "state": "Reserved",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
        }],
        "sanSystemCredentials":
            [
                {
                    "chapSecret": CHAP_SECRET_REGEX,
                    "chapLevel": "MutualChap",
                    "chapSource": "AutoGenerated",
                    "chapName": PROFILE2_IQN,
                    "mutualChapName": PROFILE2_IQN,
                    "mutualChapSecret": MCHAP_SECRET_REGEX,
                    "storageSystemUri": "REGEX:/rest/storage-systems/\w{8}(-\w{4}){3}-\w{12}"
                },
                {
                    "chapSecret": CHAP_SECRET_REGEX,
                    "chapLevel": "MutualChap",
                    "chapSource": "AutoGenerated",
                    "chapName": PROFILE2_IQN,
                    "mutualChapName": PROFILE2_IQN,
                    "mutualChapSecret": MCHAP_SECRET_REGEX,
                    "storageSystemUri": "REGEX:/rest/storage-systems/\w{8}(-\w{4}){3}-\w{12}"
                }
        ],
    }
}

# Profile2, existing and new volume attachments, redundant storage paths,
# profile iQN
profile2_edit = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE2_NAME, "description": "",
    "serverHardwareUri": 'SH:' + PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PROFILE2_EG,
    "enclosureUri": 'ENC:' + PROFILE2_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": PROFILE2_IQN_EDIT,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 2, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 3, "name": "", "functionType": "iSCSI", "portId": "Flb 1:1", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 4, "name": "", "functionType": "iSCSI", "portId": "Flb 1:2", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:1", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:2", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
    "bootMode": {"manageMode": True, "mode": "BIOS"},
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": NEW_SUSE, "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 1,
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "isEnabled": True,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                    "targets": []
                }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_3PAR1_PRIV,
        }, {
            "id": 2,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,
        }, {
            "id": 3,
            "bootVolumePriority": "NotBootable",
            "lun": 3,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": VOLUME_PROFILE2_3PAR1_PERM_PRIV,
                    "description": "",
                    "storagePool": "SPOOL:" + STORESERV1_POOL1,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                },
                "templateUri": "ROOT:" + STORESERV1_POOL1,
            },
            "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
            "volumeUri": None,
        }, {
            "id": 4,
            "bootVolumePriority": "NotBootable",
            "lun": 4,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": VOLUME_PROFILE2_3PAR1_EPH_PRIV,
                    "description": "",
                    "storagePool": "SPOOL:" + STORESERV1_POOL1,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                },
                "templateUri": "ROOT:" + STORESERV1_POOL1,
            },
            "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
            "volumeUri": None,
        }, {
            "id": 11,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_PRIV,
        }, {
            "id": 12,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA1_SHARED,
        }, {
            "id": 13,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": VOLUME_PROFILE2_VSA1_PERM_PRIV,
                    "description": "",
                    "storagePool": "SPOOL:" + STOREVIRTUAL1_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity"
                },
                "templateUri": "ROOT:" + STOREVIRTUAL1_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
            "volumeUri": None,
        }, {
            "id": 14,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": VOLUME_PROFILE2_VSA1_EPH_PRIV,
                    "description": "",
                    "storagePool": "SPOOL:" + STOREVIRTUAL1_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid5SingleParity"
                },
                "templateUri": "ROOT:" + STOREVIRTUAL1_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
            "volumeUri": None,
        }, {
            "id": 21,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_PRIV,
        }, {
            "id": 22,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
        }, {
            "id": 23,
            "bootVolumePriority": "NotBootable",
            "lun": 3,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": VOLUME_PROFILE2_VSA2_PERM_PRIV,
                    "description": "",
                    "storagePool": "SPOOL:" + STOREVIRTUAL2_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid0None"
                },
                "templateUri": "ROOT:" + STOREVIRTUAL2_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
            "volumeUri": None,
        }, {
            "id": 24,
            "bootVolumePriority": "NotBootable",
            "lun": 4,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": VOLUME_PROFILE2_VSA2_EPH_PRIV,
                    "description": "",
                    "storagePool": "SPOOL:" + STOREVIRTUAL2_POOL,
                    "size": 1073741824,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid0None"
                },
                "templateUri": "ROOT:" + STOREVIRTUAL2_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
            "volumeUri": None,
        }]
    }
}

profile2_edit_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE2_NAME, "description": "",
    "serverHardwareUri": 'SH:' + PROFILE2_SERVER, "enclosureGroupUri": 'EG:' + PROFILE2_EG,
    "enclosureUri": 'ENC:' + PROFILE2_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": PROFILE2_IQN_EDIT,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "",
                "state": "Deployed",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:1",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
            },
            {
                "id": 2,
                "name": "",
                "state": "Deployed",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:2",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
            },
            {
                "id": 3,
                "name": "",
                "state": "Deployed",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 4,
                "name": "",
                "state": "Deployed",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 5,
                "name": "",
                "state": "Deployed",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            },
            {
                "id": 6,
                "name": "",
                "state": "Deployed",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
    "bootMode": {"manageMode": True, "mode": "BIOS"},
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": NEW_SUSE, "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "state": "Attached",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_3PAR1_PRIV,
        }, {
            "id": 2,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "state": "Attached",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,
        }, {
            "id": 3,
            "bootVolumePriority": "NotBootable",
            "lun": 3,
            "lunType": "Manual",
            "state": "Attached",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_3PAR1_PERM_PRIV,
        }, {
            "id": 4,
            "bootVolumePriority": "NotBootable",
            "lun": 4,
            "lunType": "Manual",
            "state": "Attached",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_3PAR1_EPH_PRIV,
        }, {
            "id": 11,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE2_VSA1_PRIV
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE2_VSA1_PRIV
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_PRIV,
        }, {
            "id": 12,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_VSA1_SHARED
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_VSA1_SHARED
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA1_SHARED,
        }, {
            "id": 13,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE2_VSA1_PERM_PRIV
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE2_VSA1_PERM_PRIV
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_PERM_PRIV,
        }, {
            "id": 14,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE2_VSA1_EPH_PRIV
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE2_VSA1_EPH_PRIV
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_EPH_PRIV,
        }, {
            "id": 21,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_PRIV,
        }, {
            "id": 22,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
        }, {
            "id": 23,
            "bootVolumePriority": "NotBootable",
            "lun": 3,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_PERM_PRIV,
        }, {
            "id": 24,
            "bootVolumePriority": "NotBootable",
            "lun": 4,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_EPH_PRIV,
        }],
        "sanSystemCredentials":
            [
                {
                    "chapSecret": CHAP_SECRET_REGEX,
                    "chapLevel": "MutualChap",
                    "chapSource": "AutoGenerated",
                    "chapName": PROFILE2_IQN,
                    "mutualChapName": PROFILE2_IQN,
                    "mutualChapSecret": MCHAP_SECRET_REGEX,
                    "storageSystemUri": "REGEX:/rest/storage-systems/\w{8}(-\w{4}){3}-\w{12}"
                },
                {
                    "chapSecret": CHAP_SECRET_REGEX,
                    "chapLevel": "MutualChap",
                    "chapSource": "AutoGenerated",
                    "chapName": PROFILE2_IQN,
                    "mutualChapName": PROFILE2_IQN,
                    "mutualChapSecret": MCHAP_SECRET_REGEX,
                    "storageSystemUri": "REGEX:/rest/storage-systems/\w{8}(-\w{4}){3}-\w{12}"
                }
        ],
    }
}

# Profile2 move
profile2_move = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE2_NAME, "description": "",
    "serverHardwareUri": 'SH:' + PROFILE2_MOVE_SERVER, "enclosureGroupUri": 'EG:' + PROFILE2_MOVE_EG,
    "enclosureUri": 'ENC:' + PROFILE2_MOVE_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": PROFILE2_IQN,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 2, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 3, "name": "", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 4, "name": "", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:1", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            },
            {
                "id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 1:2", "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": OLD_SUSE, "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 1,
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "isEnabled": True,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                    "targets": []
                }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_3PAR1_PRIV,
        }, {
            "id": 2,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,
        }, {
            "id": 3,
            "bootVolumePriority": "NotBootable",
            "lun": 3,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_3PAR1_PERM_PRIV,
        }, {
            "id": 4,
            "bootVolumePriority": "NotBootable",
            "lun": 4,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 2,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_3PAR1_EPH_PRIV,
        }, {
            "id": 11,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
            }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_PRIV,
        }, {
            "id": 12,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
            }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA1_SHARED,
        }, {
            "id": 13,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
            }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_PERM_PRIV,
        }, {
            "id": 14,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 3,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": []
            }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_EPH_PRIV,
        }, {
            "id": 21,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_PRIV,
        }, {
            "id": 22,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
            }],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
        }, {
            "id": 23,
            "bootVolumePriority": "NotBootable",
            "lun": 3,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
            }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_PERM_PRIV,
        }, {
            "id": 24,
            "bootVolumePriority": "NotBootable",
            "lun": 4,
            "lunType": "Manual",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 5,
                "targetSelector": "Auto",
                "targets": []
            },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": []
            }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_EPH_PRIV,
        }]
    }
}

profile2_move_expected = {
    "type": SERVER_PROFILE_TYPE, "name": PROFILE2_NAME, "description": "",
    "serverHardwareUri": 'SH:' + PROFILE2_MOVE_SERVER, "enclosureGroupUri": 'EG:' + PROFILE2_MOVE_EG,
    "enclosureUri": 'ENC:' + PROFILE2_MOVE_ENC,
    "iscsiInitiatorNameType": "UserDefined", "iscsiInitiatorName": PROFILE2_IQN,
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "",
                "state": "Deployed",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:1",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-a',
            },
            {
                "id": 2,
                "name": "",
                "state": "Deployed",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:2",
                "requestedMbps": "Auto",
                "networkUri": 'FC:fa-b',
            },
            {
                "id": 3,
                "name": "",
                "state": "Deployed",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 4,
                "name": "",
                "state": "Deployed",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
            },
            {
                "id": 5,
                "name": "",
                "state": "Deployed",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            },
            {
                "id": 6,
                "name": "",
                "state": "Deployed",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]}, "bootMode": None,
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": OLD_SUSE, "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "state": "Attached",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_3PAR1_PRIV,
        }, {
            "id": 2,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "state": "Attached",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,
        }, {
            "id": 3,
            "bootVolumePriority": "NotBootable",
            "lun": 3,
            "lunType": "Manual",
            "state": "Attached",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_3PAR1_PERM_PRIV,
        }, {
            "id": 4,
            "bootVolumePriority": "NotBootable",
            "lun": 4,
            "lunType": "Manual",
            "state": "Attached",
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
                }, ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_3PAR1_EPH_PRIV,
        }, {
            "id": 11,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE2_VSA1_PRIV
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE2_VSA1_PRIV
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_PRIV,
        }, {
            "id": 12,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_VSA1_SHARED
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_VSA1_SHARED
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA1_SHARED,
        }, {
            "id": 13,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE2_VSA1_PERM_PRIV
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE2_VSA1_PERM_PRIV
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_PERM_PRIV,
        }, {
            "id": 14,
            "bootVolumePriority": "NotBootable",
            "lunType": "Auto",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 3,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE2_VSA1_EPH_PRIV
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 4,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL1_VIP,
                        "tcpPort": "3260",
                        "name": VSA1_STORAGE_PATH_TARGET_NAME_REGEX + VOLUME_PROFILE2_VSA1_EPH_PRIV
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_EPH_PRIV,
        }, {
            "id": 21,
            "bootVolumePriority": "NotBootable",
            "lun": 1,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_PRIV,
        }, {
            "id": 22,
            "bootVolumePriority": "NotBootable",
            "lun": 2,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
        }, {
            "id": 23,
            "bootVolumePriority": "NotBootable",
            "lun": 3,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_PERM_PRIV,
        }, {
            "id": 24,
            "bootVolumePriority": "NotBootable",
            "lun": 4,
            "lunType": "Manual",
            "state": "Attached",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 5,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
                {
                    "isEnabled": True,
                    "connectionId": 6,
                    "targetSelector": "Auto",
                    "targets": [{
                        "ipAddress": STOREVIRTUAL2_VIP,
                        "tcpPort": "3260",
                        "name": VSA2_STORAGE_PATH_TARGET_NAME_REGEX
                    }]
                },
            ],
            "volume": None,
            "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_EPH_PRIV,
        }],
        "sanSystemCredentials":
            [
                {
                    "chapSecret": CHAP_SECRET_REGEX,
                    "chapLevel": "MutualChap",
                    "chapSource": "AutoGenerated",
                    "chapName": PROFILE2_IQN,
                    "mutualChapName": PROFILE2_IQN,
                    "mutualChapSecret": MCHAP_SECRET_REGEX,
                    "storageSystemUri": "REGEX:/rest/storage-systems/\w{8}(-\w{4}){3}-\w{12}"
                },
                {
                    "chapSecret": CHAP_SECRET_REGEX,
                    "chapLevel": "MutualChap",
                    "chapSource": "AutoGenerated",
                    "chapName": PROFILE2_IQN,
                    "mutualChapName": PROFILE2_IQN,
                    "mutualChapSecret": MCHAP_SECRET_REGEX,
                    "storageSystemUri": "REGEX:/rest/storage-systems/\w{8}(-\w{4}){3}-\w{12}"
                }
        ],
    }
}

# PTS1, create, edit, and move profiles
pts1_profiles_create = [
    profile1_create.copy(),
    profile2_create.copy()
]

pts1_profiles_create_expected = [
    profile1_create_expected,
    profile2_create_expected,
]

pts1_profiles_edit = [
    profile1_edit.copy(),
    profile2_edit.copy()
]

pts1_profiles_edit_expected = [
    profile1_edit_expected,
    profile2_edit_expected,
]

pts1_profiles_move = [
    profile1_move.copy(),
    profile2_move.copy()
]

pts1_profiles_move_expected = [
    profile1_move_expected,
    profile2_move_expected,
]

pts1_profiles_delete = [
    profile1_move.copy(),
    profile2_move.copy()
]

pts1_all_profiles = [
    profile1_create.copy(),
    profile1_move.copy(),
    profile2_create.copy(),
    profile2_move.copy(),
]

new_ephemeral_volumes = [
    {"name": VOLUME_PROFILE1_3PAR1_EPH_PRIV, },
    {"name": VOLUME_PROFILE1_VSA1_EPH_PRIV, },
    {"name": VOLUME_PROFILE1_VSA2_EPH_PRIV, },
    {"name": VOLUME_PROFILE2_3PAR1_EPH_PRIV, },
    {"name": VOLUME_PROFILE2_VSA1_EPH_PRIV, },
    {"name": VOLUME_PROFILE2_VSA2_EPH_PRIV, },
]

new_permanent_volumes = [
    {"name": VOLUME_PROFILE1_3PAR1_PERM_PRIV, },
    {"name": VOLUME_PROFILE1_VSA1_PERM_PRIV, },
    {"name": VOLUME_PROFILE1_VSA2_PERM_PRIV, },
    {"name": VOLUME_PROFILE2_3PAR1_PERM_PRIV, },
    {"name": VOLUME_PROFILE2_VSA1_PERM_PRIV, },
    {"name": VOLUME_PROFILE2_VSA2_PERM_PRIV, },
]

pts2_profiles_efuse_off_expected = [
    profile1_efuse_off_expected,
    profile2_efuse_off_expected,
]

pts2_profiles_efuse_on_expected = [
    profile1_create_expected,
    profile2_create_expected,
]

suite_setup_profiles = [
    profile1_create.copy(),
    profile1_move.copy(),
    profile2_create.copy(),
    profile2_move.copy(),
]
